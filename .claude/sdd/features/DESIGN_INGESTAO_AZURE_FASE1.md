# DESIGN: Arquitetura de Ingestão — Fase 1 (Azure)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AZURE_FASE1 |
| **Input** | `.claude/sdd/features/DEFINE_INGESTAO_AZURE_FASE1.md` |
| **Status** | ✅ Complete (Designed) |
| **Data** | 2026-09-12 |

---

## Architecture Overview

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│   ETAPA 1 — Captura única + hub (Event Hub) + landing batch independente (MongoDB/MinIO)│
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Fase 0 (Postgres/Oracle/MongoDB/MinIO em Docker/ShadowTraffic) permanece LOCAL         │
│                                                                                          │
│  Postgres ──Airbyte OSS (CDC, replication slot, destino "Kafka")──┐                    │
│  Oracle   ──Debezium/Kafka Connect (LogMiner, worker apontado     │                    │
│             pro Event Hub)─────────────────────────────────────────┤                    │
│  MinIO    ──notificação de bucket nativa (destino "Kafka")────────┤                    │
│                                                                     ▼                    │
│                                                    Event Hubs Namespace (tier Standard) │
│                                                    3 tópicos: postgres.*, oracle.*, minio│
│                                                                                          │
│  MongoDB ──Airbyte (snapshot/full-refresh, particionado por data)──┐                    │
│  MinIO   ──Airbyte (sync agendado)──────────────────────────────────┤                    │
│                                                                       ▼                  │
│                                                          ADLS Gen2 (Bronze)             │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│         ETAPA 2 — Landing batch via sink (Postgres/Oracle) + Synapse                    │
├──────────────────────────────────────────────────────────────────────────────────────┤
│         Event Hubs Namespace (tópicos postgres.*, oracle.* da Etapa 1)                 │
│                              │                                                          │
│                              ▼                                                          │
│         Kafka Connect Sink Connector (ADLS Gen2/HDFS2-based) — consome os              │
│         MESMOS tópicos que o Stream Analytics consome (Etapa 3), não uma               │
│         2ª captura — preserva op/before/after/SCN e LSN                                │
│                              │                                                          │
│                              ▼                                                          │
│              ADLS Gen2 (Bronze) ── já une Postgres + Oracle (via sink) +               │
│              MongoDB + MinIO (via Airbyte direto, Etapa 1)                              │
│                              │                                                          │
│                              ▼                                                          │
│                  Synapse Dedicated (COPY INTO + MERGE, SCD2)                            │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│                    ETAPA 3 — Lakehouse (zero ingestão nova)                             │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                    ADLS Gen2 (Bronze, já populado na Etapa 2)                           │
│                              │                                                          │
│                              ▼                                                          │
│    Unity Catalog external location (storage credential via Service Principal)          │
│                              │                                                          │
│                              ▼                                                          │
│    Databricks — Bronze via Auto Loader (`read_files`), pipeline em modo Triggered       │
│    (batch), `APPLY CHANGES INTO ... SEQUENCE BY cdc_sequence` — substitui               │
│    `read_kafka()` (Oracle), sync direto Airbyte→Databricks (Postgres) e                │
│    Lakehouse Federation (MongoDB) usados hoje na Fase 0                                │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│                 ETAPA 4 — Kappa (consumo real-time, hub já existe desde a Etapa 1)      │
├──────────────────────────────────────────────────────────────────────────────────────┤
│         Event Hubs Namespace (tópicos postgres.*, oracle.*, minio.* da Etapa 1)        │
│                              │                                                          │
│                              ▼                                                          │
│         Stream Analytics (job de streaming) ── reference data input                    │
│                    │ (join contra o path particionado do MongoDB no ADLS)              │
│                    ▼                                                                   │
│         Saída enriquecida (destino final a detalhar no `/build`)                       │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Achado de Design (muda o desenho do DEFINE):** o DEFINE previa 2 capturas independentes por fonte relacional (1 batch/ADLS + 1 real-time/Event Hub), com o risco de concorrência confinado à Etapa 3 (Assumptions A-001/A-002). Neste `/design`, percebeu-se que **o Kafka Connect já resolve isso nativamente**: como o Event Hub fala Kafka, um **Sink Connector** pode consumir o mesmo tópico que a captura já publica (Postgres via Airbyte "Kafka" destination; Oracle via Debezium) e gravar no ADLS — não é preciso uma 2ª captura. Isso **elimina** (não apenas mitiga) o risco de 2 replication slots concorrentes no Postgres e de 2 sessões LogMiner concorrentes no Oracle — ver Decisão 1. MinIO e MongoDB não entram nessa consolidação: a notificação de bucket do MinIO carrega só metadados do evento (não o conteúdo do objeto), então o Airbyte continua fazendo a cópia real do objeto pro ADLS; o MongoDB nunca esteve no trilho real-time. Como consequência, o sequenciamento por etapa deste Design não é mais organizado por "isolar a etapa de maior risco" (não existe mais tal etapa) — é organizado por **dependência técnica**: o hub (Event Hub) precisa existir antes do sink; o sink precisa existir antes do Synapse/Databricks lerem Postgres/Oracle do ADLS.

**Contrato canônico de CDC — sem mapeamento novo (achado favorável desta fase):** ao contrário da AWS (DMS) e da GCP (Datastream/Debezium Server), que precisaram mapear os metadados proprietários de ferramentas novas para o contrato canônico, a Fase 1 **reaproveita as mesmas ferramentas já mapeadas na Onda 3** (Airbyte para Postgres, Debezium/Kafka Connect para Oracle — ver `pipeline/bronze/ingest_postgres_drivers.sql` e `pipeline/bronze/ingest_oracle_orders.sql`, já em produção local). O mapeamento não muda; só o meio físico muda (tópico Redpanda/tabela raw → tópico Event Hub/arquivo ADLS):

| Coluna canônica | Postgres (Airbyte) — inalterado desde a Onda 3 | Oracle (Debezium) — inalterado desde a Onda 3 |
|---|---|---|
| `cdc_operation` | `_ab_cdc_deleted_at` (`NULL`→`u`, preenchido→`d`) | `payload.op` (`c`/`u`/`d`) |
| `cdc_commit_ts` | `_ab_cdc_updated_at` | `payload.source.ts_ms` |
| `cdc_sequence` | `_ab_cdc_lsn` | `payload.source.scn` |
| `cdc_source_system` | constante `'postgres-ubereats'` | constante `'oracle-ubereats'` |

A Silver continua sem ler o formato nativo diretamente — mesma disciplina já estabelecida.

---

## Decisões (ADRs inline)

### Decisão 1 — Postgres e Oracle usam 1 única captura por fonte; o ADLS é alimentado por um Sink Connector consumindo o mesmo tópico do Event Hub (elimina, não mitiga, a concorrência de captura)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Data** | 2026-09-12 |

**Contexto:** o DEFINE assumia 2 capturas por fonte (Assumptions A-001, A-002): Postgres com 2 replication slots simultâneos, Oracle com 1 captura LogMiner e 2 sinks configurados diretamente no conector Debezium.

**Escolha:** Postgres mantém só a captura real-time (Airbyte, destino nativo "Kafka" → Event Hub). Oracle mantém só a captura real-time (Debezium/Kafka Connect, worker apontado pro Event Hub). O landing batch no ADLS Gen2 é feito por um **Kafka Connect Sink Connector** (ver Decisão 2) rodando no mesmo cluster Kafka Connect, configurado para **consumir os tópicos `postgres.*`/`oracle.*` do Event Hub** — o mesmo tópico que o Stream Analytics também consome (Etapa 4). Captura única, 2 consumidores independentes.

**Racional:** Kafka Connect já é desenhado para isso — múltiplos conectores (source e sink) compartilhando o mesmo cluster/tópicos é o caso de uso padrão, não um workaround. Eliminar a 2ª captura remove por completo o risco que a AWS (A-003) e a GCP (A-003) tiveram que mitigar por sequenciamento (nunca eliminaram, só confinaram a uma janela) — aqui não existe mais essa janela de risco.

**Alternativas rejeitadas:**
1. Manter 2 capturas independentes (proposta original do DEFINE) — mais simples de explicar isoladamente, mas reintroduz exatamente o risco que a AWS e a GCP tiveram (limite de replication slots, concorrência no LogMiner) sem necessidade técnica real.

**Consequências:** o Event Hub deixa de ser "só do Kappa" — vira infraestrutura compartilhada entre os 4 consumidores finais (Synapse, Databricks, Stream Analytics, e indiretamente qualquer coisa que leia o ADLS). Isso muda o sequenciamento (ver Etapas 1-4 acima): o Event Hub precisa existir **antes** do Synapse/Databricks conseguirem ler Postgres/Oracle, mesmo que o Warehouse/Lakehouse não tenham requisito de real-time. MongoDB e MinIO **não** entram nesta consolidação (ver Achado de Design acima) — mantêm o Airbyte→ADLS direto do DEFINE.

### Decisão 2 — Sink Connector para o ADLS é o Kafka Connect HDFS 2 Sink Connector, apontado para `abfss://`

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE deixou em aberto (Open Question) o formato exato e a ferramenta do sink Kafka Connect → ADLS.

**Escolha:** **Kafka Connect HDFS 2 Sink Connector** (`io.confluent.connect.hdfs.HdfsSinkConnector`), configurado com `store.url=abfss://bronze@<storage-account>.dfs.core.windows.net/`, `hadoop.conf.dir` apontando pro `core-site.xml` com as credenciais do Service Principal (`fs.azure.account.auth.type=OAuth`) e `format.class=io.confluent.connect.hdfs.json.JsonFormat` — mesmo formato JSON já usado pelo Airbyte hoje (MinIO, `docs/airbyte/README.md`), preservando consistência de formato entre os dois mecanismos de landing no mesmo Bronze.

**Racional:** o ADLS Gen2 implementa a interface Hadoop-compatível (`abfss://`), e o HDFS 2 Sink Connector já sabe escrever em qualquer `FileSystem` compatível com Hadoop — não é necessário um conector Azure-específico proprietário nem escrever um sink customizado.

**Alternativas rejeitadas:**
1. Sink customizado (Python/Java) escrevendo direto na API do ADLS — mais controle, mas reintroduz um componente customizado que a Decisão 1 do brainstorm já tinha evitado (achado técnico: "sem componente-ponte").
2. Azure Data Lake Storage Gen2 Sink Connector (Confluent, licenciamento comercial) — funcionalmente equivalente, mas exige licença Confluent Platform; o HDFS 2 Sink Connector é Apache 2.0/Confluent Community License, suficiente para este portfólio.

**Consequências:** o particionamento de arquivo (`flush.size`, `rotate.interval.ms`) precisa ser ajustado no `/build` para equilibrar frescura do dado no Synapse/Databricks vs. número de arquivos pequenos no ADLS (mesma preocupação de qualquer sink baseado em Hadoop `FileSystem`).

### Decisão 3 — Bronze do Databricks consumida via Auto Loader (`read_files`) sobre external location, pipeline em modo Triggered — não uma UC "external table" estática

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE usou o termo "external table" (linguagem do brainstorm) para descrever o consumo do Databricks sobre o ADLS. Ao inspecionar o código já existente (`pipeline/bronze/ingest_oracle_orders.sql`, `pipeline/bronze/ingest_postgres_drivers.sql`), ficou claro que a forma idiomática de fazer isso no Lakeflow/DLT é **Auto Loader**, não uma tabela externa estática.

**Escolha:** cada arquivo em `pipeline/bronze/*.sql` passa a ler `STREAM read_files(path => 'abfss://bronze@<storage-account>.dfs.core.windows.net/<fonte>/<tabela>/', format => 'json')` no lugar de `STREAM read_kafka(...)` (Oracle) ou `STREAM(uber_eats.raw.*)` (Postgres). O pipeline Lakeflow roda em **modo Triggered** (não Continuous) — cada execução processa só os arquivos novos desde a última, comportamento de lote, mas usando a mesma sintaxe `CREATE OR REFRESH STREAMING TABLE ... APPLY CHANGES INTO ... SEQUENCE BY cdc_sequence` já validada na Onda 3. A external location do Unity Catalog (Decisão 4) é o objeto de governança; `read_files` é o mecanismo de leitura.

**Racional:** preserva 100% da sintaxe DLT/`APPLY CHANGES`/`SEQUENCE BY` já testada — a única mudança real é a fonte (`read_kafka`/tabela raw → `read_files`) e o modo de trigger (Continuous → Triggered). Uma "external table" UC estática (via `CREATE TABLE ... USING DELTA LOCATION` ou tabela não-Delta) não ofereceria o `APPLY CHANGES`/upsert incremental que a Bronze precisa para aplicar CDC — só serve para dado já materializado, não para processar um fluxo de eventos de mudança.

**Alternativas rejeitadas:**
1. UC external table estática (Parquet/Delta externo) + `MERGE` manual em SQL puro — perderia o `APPLY CHANGES INTO`/expectations nativos do Lakeflow, exigindo reescrever a lógica de upsert que já existe.

**Consequências:** todos os 9 arquivos Bronze existentes (`ingest_postgres_drivers.sql`, `ingest_postgres_users.sql`, 7× `ingest_oracle_*.sql`) precisam ser editados; MongoDB ganha um arquivo Bronze novo que não existia (`ingest_mongodb_perfil_restaurante.sql`), já que hoje ele só tem Silver (via Federation, Decisão 6).

### Decisão 4 — Storage credential do Unity Catalog via Service Principal (Azure AD App Registration), não managed identity/Access Connector

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE (Assumption A-004) deixou em aberto se o Databricks Free Edition conseguiria autenticar contra o ADLS Gen2 via managed identity, dado que o workspace fica fora da subscription Azure.

**Escolha:** **Service Principal** (Azure AD App Registration, client secret) — o mecanismo de autenticação padrão do Unity Catalog quando o workspace não é um recurso Azure Databricks dentro da subscription (o "Access Connector for Databricks", que usa managed identity, só existe para workspaces provisionados via Azure Marketplace/ARM na própria subscription — não é o caso do Free Edition). O client secret é armazenado como Databricks secret scope, nunca em código versionado.

**Racional:** resolve A-004 de forma definitiva, sem depender de um recurso Azure que o Free Edition não suporta.

**Alternativas rejeitadas:**
1. Access Connector for Databricks (managed identity) — não aplicável, exige workspace provisionado dentro da subscription via ARM/Marketplace.

**Consequências:** rotação do client secret é responsabilidade manual (Service Principal secrets expiram, tipicamente em até 24 meses) — documentar a data de expiração no runbook do `/build`.

### Decisão 5 — MinIO usa notificação nativa tipo "Kafka" (não "Webhook") apontando direto pro Event Hub

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** AWS e GCP precisaram de uma função ponte (Lambda/Cloud Function) porque Kinesis e Pub/Sub não falam protocolo Kafka. O brainstorm já confirmou (achado técnico #5) que o Event Hub fala Kafka nativamente.

**Escolha:** configurar o MinIO com `mc admin config set minio/ notify_kafka:eventhub brokers="<namespace>.servicebus.windows.net:9093" sasl="on" sasl_mechanism="PLAIN" sasl_username="$ConnectionString" sasl_password="<connection-string>" tls="on"` — notificação de bucket nativa tipo **Kafka**, não Webhook. O bucket é então configurado com `mc event add minio/uber-eats arn:minio:sqs::eventhub:kafka --event put,delete`.

**Racional:** elimina completamente a necessidade de um componente-ponte customizado (Lambda/Cloud Function) que as outras 2 clouds precisaram — MinIO já tem um target Kafka nativo, e o Event Hub já fala Kafka; não há tradução de protocolo necessária.

**Consequências:** nenhuma função customizada nova para monitorar/testar (diferente de AWS/GCP) — reduz a superfície do mandato "Teams/observabilidade" desta feature a só o Kafka Connect (Decisão 1/2).

### Decisão 6 — Airbyte grava o MongoDB em caminho particionado por data (não overwrite-in-place), para viabilizar o reference data input do Stream Analytics

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE deixou em aberto a frequência de atualização do reference data input do Stream Analytics contra a cópia do MongoDB no ADLS. O Stream Analytics reconhece atualização de reference data via **path pattern** com tokens de data/hora (`{date}`/`{time}`), não via sobrescrita de um arquivo fixo.

**Escolha:** a sync do Airbyte para MongoDB grava em `abfss://bronze@.../mongodb/perfil_restaurante/{yyyy}/{MM}/{dd}/perfil_restaurante.json` a cada execução (não overwrite-in-place do mesmo arquivo) — o Stream Analytics configura o reference data input com esse mesmo path pattern, e o serviço automaticamente usa a versão mais recente disponível no momento de cada evento processado.

**Racional:** é o único jeito documentado de o Stream Analytics atualizar reference data automaticamente sem reiniciar o job manualmente. Como o MongoDB é estático (Onda 3), a frequência da sync do Airbyte (a definir no `/build`, ex. diária) já é mais que suficiente.

**Alternativas rejeitadas:**
1. Overwrite-in-place + reference data "estática" (upload manual/reinício de job a cada mudança) — inviável operacionalmente, exigiria intervenção manual toda vez que o cadastro de restaurante mudasse.

**Consequências:** acumula um histórico de snapshots do MongoDB no ADLS (1 arquivo por dia) — aceitável dado o volume (~500 documentos); política de retenção/limpeza fica para o `/build`.

---

## File Manifest

### Etapa 1 — Captura única + hub (Event Hub) + landing batch independente

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 1 | `infra/azure/fase1-ingestao/resource_group.tf` | Criar | Resource Group da Fase 1 | @infra-deployer | — |
| 2 | `infra/azure/fase1-ingestao/storage_account.tf` | Criar | Storage Account com hierarchical namespace habilitado (ADLS Gen2), container `bronze` | @infra-deployer | 1 |
| 3 | `infra/azure/fase1-ingestao/event_hubs.tf` | Criar | Event Hubs Namespace (**tier Standard**) + 3 Event Hubs (`postgres`, `oracle`, `minio`) | @infra-deployer | 1 |
| 4 | `infra/azure/fase1-ingestao/service_principal.tf` | Criar | Azure AD App Registration (Service Principal) + role assignment `Storage Blob Data Contributor` no container `bronze` (Decisão 4) | @infra-deployer | 2 |
| 5 | `docs/azure/airbyte-kafka-eventhub-config.md` | Criar | Configuração do destino nativo "Kafka" do Airbyte (Postgres CDC) apontando pro endpoint Kafka-compatível do Event Hub (SASL_SSL, connection string) | (general) | 3 |
| 6 | `debezium/connect-worker-eventhub.properties.template` | Criar | Worker config do Kafka Connect (`bootstrap.servers`, `sasl.jaas.config`) apontando pro Event Hub — usado pelo conector Oracle já existente (`debezium/oracle-connector.json.template`) | (general) | 3 |
| 7 | `docs/minio/kafka-notification-config-azure.md` | Criar | Configuração da notificação de bucket nativa do MinIO tipo "Kafka" apontando pro Event Hub (Decisão 5) | (general) | 3 |
| 8 | `docs/azure/airbyte-mongodb-adls-config.md` | Criar | Configuração da sync do Airbyte (MongoDB, snapshot/full-refresh) com destino ADLS Gen2, path particionado por data (Decisão 6) | (general) | 2, 4 |
| 9 | `docs/azure/airbyte-minio-adls-config.md` | Criar | Configuração da sync do Airbyte (MinIO → ADLS Gen2), destino Azure Blob Storage (hierarchical namespace) | (general) | 2, 4 |

### Etapa 2 — Landing batch via sink (Postgres/Oracle) + Synapse

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 10 | `debezium/adls-sink-connector.json.template` | Criar | Kafka Connect HDFS 2 Sink Connector, consumindo os tópicos `postgres.*`/`oracle.*` do Event Hub, gravando em `abfss://bronze@.../` (Decisão 1, 2) | (general) | 3, 4, 6 |
| 11 | `debezium/register-adls-sink-connector.ps1` | Criar | Script de registro do sink na API REST do Kafka Connect (mesmo padrão de `debezium/register-oracle-connector.ps1`) | (general) | 10 |
| 12 | `infra/azure/fase1-ingestao/synapse.tf` | Criar | Synapse Workspace + Dedicated SQL Pool | @infra-deployer | 1 |
| 13 | `sql/azure/synapse_copy_merge.sql` | Criar | Scripts `COPY INTO` + `MERGE` (SCD2) por tabela, a partir do ADLS Gen2/Bronze, projetando as 4 colunas canônicas de CDC | @databricks-sql-analyst (padrão de MERGE/SCD reaproveitável, mesmo raciocínio das Fases 2/3) | 12 |
| 14 | `docs/data-contract-cdc-azure.md` | Criar | Confirma que o mapeamento canônico de CDC (Onda 3, Airbyte/Debezium) **não muda** nesta fase — só o meio físico (arquivo ADLS em vez de tópico Redpanda/tabela raw) | (general) | — |

### Etapa 3 — Lakehouse (zero ingestão nova)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 15 | `infra/azure/fase1-ingestao/unity_catalog_credential.tf` | Criar | Storage credential (Service Principal, Decisão 4) + external location do Unity Catalog apontando pro container ADLS Gen2/Bronze | @infra-deployer | 4 |
| 16 | `pipeline/bronze/ingest_postgres_drivers.sql` | Editar | Trocar `STREAM(uber_eats.raw.drivers)` por `STREAM read_files(...)` sobre a external location (Decisão 3) | @databricks-pipeline-architect | 15 |
| 17 | `pipeline/bronze/ingest_postgres_users.sql` | Editar | Mesma mudança do item 16, para `users` | @databricks-pipeline-architect | 15 |
| 18 | `pipeline/bronze/ingest_oracle_orders.sql` | Editar | Trocar `STREAM read_kafka(bootstrapServers => 'redpanda:9092', ...)` por `STREAM read_files(...)` sobre a external location; pipeline passa a modo Triggered (Decisão 3) | @databricks-pipeline-architect | 15 |
| 19 | `pipeline/bronze/ingest_oracle_payments.sql` | Editar | Mesma mudança do item 18 | @databricks-pipeline-architect | 15 |
| 20 | `pipeline/bronze/ingest_oracle_receipts.sql` | Editar | Mesma mudança do item 18 | @databricks-pipeline-architect | 15 |
| 21 | `pipeline/bronze/ingest_oracle_order_items.sql` | Editar | Mesma mudança do item 18 | @databricks-pipeline-architect | 15 |
| 22 | `pipeline/bronze/ingest_oracle_inventory.sql` | Editar | Mesma mudança do item 18 | @databricks-pipeline-architect | 15 |
| 23 | `pipeline/bronze/ingest_oracle_products.sql` | Editar | Mesma mudança do item 18 | @databricks-pipeline-architect | 15 |
| 24 | `pipeline/bronze/ingest_oracle_restaurants.sql` | Editar | Mesma mudança do item 18 | @databricks-pipeline-architect | 15 |
| 25 | `pipeline/bronze/ingest_mongodb_perfil_restaurante.sql` | Criar | Novo — Bronze via `read_files` (snapshot/full-refresh, `LIVE TABLE` não streaming) sobre o path do MongoDB no ADLS, substitui a leitura direta por Lakehouse Federation na Silver (`pipeline/silver/ingestion_mongo_perfil_restaurante.sql`, que passa a ler `live.bronze_perfil_restaurante` em vez de `mongo_ubereats.ubereats.perfil_restaurante`) | @databricks-pipeline-architect | 15 |
| 26 | `pipeline/silver/ingestion_mongo_perfil_restaurante.sql` | Editar | Trocar a fonte de Lakehouse Federation (`mongo_ubereats....`) pela nova Bronze do item 25 | @databricks-pipeline-architect | 25 |
| 27 | `pipeline/silver/ingestion_kafka_gps.sql`, `ingestion_kafka_ratings.sql`, `ingestion_kafka_route.sql`, `ingestion_kafka_search.sql`, `ingestion_kafka_shift.sql`, `ingestion_mysql_menu.sql` | Editar (6 arquivos) | Trocar o path de leitura do Auto Loader de MinIO (`s3a://uber-eats/...`) para ADLS Gen2 (`abfss://bronze@.../minio/...`) — descoberta desta rodada de `/design`: não estava no escopo do DEFINE, mas é consequência direta de "Migração leve: troca de storage" do roadmap (Fase 1, linha Lakehouse) | @databricks-pipeline-architect | 9, 15 |

### Etapa 4 — Kappa (consumo real-time)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 28 | `infra/azure/fase1-ingestao/stream_analytics.tf` | Criar | Job Stream Analytics: input do Event Hub (3 tópicos), reference data input (path do MongoDB no ADLS, Decisão 6), query de enriquecimento | @infra-deployer | 3, 9 |
| 29 | `sql/azure/stream_analytics_query.sql` | Criar | Query ASA: `JOIN` do stream de eventos com o reference data input, projetando Pedido/Restaurante enriquecidos | (general) | 28 |
| 30 | `tests/azure/test_adls_sink_cdc_mapping.py` | Criar | Teste de contrato: valida que arquivos gravados pelo sink (item 10) preservam `op`/`before`/`after`/SCN (Oracle) e `_ab_cdc_*` (Postgres) | @test-generator | 10 |

### Transversal

| # | Arquivo | Ação | Propósito |
|---|---------|--------|-----------|
| 31 | `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` | Editar | Registrar o achado de Design (Decisão 1 — captura única, sem 2ª captura por fonte) como refinamento da v1.8; documentar que o sequenciamento por etapa mudou de "isolar risco" para "dependência técnica" |
| 32 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Verificar (provável no-op) | Confirmar que nenhuma mudança de modelo de domínio é necessária — feature de ingestão/infra |
| 33 | `infra/azure/fase1-ingestao/variables.tf`, `outputs.tf`, `versions.tf` | Criar | Boilerplate Terraform (providers `azurerm` + `databricks`, variáveis sensíveis nunca hardcoded) | — |

---

## Code Patterns

### 1. Event Hubs Namespace (tier Standard) + Event Hub por fonte

```hcl
resource "azurerm_eventhub_namespace" "fase1" {
  name                = "ubereats-fase1-eventhub-ns"
  location            = azurerm_resource_group.fase1.location
  resource_group_name = azurerm_resource_group.fase1.name
  sku                 = "Standard"   # obrigatório para Kafka Connect (tópicos internos compactados)
  capacity            = 1
}

resource "azurerm_eventhub" "postgres" {
  name                = "postgres"
  namespace_name      = azurerm_eventhub_namespace.fase1.name
  resource_group_name = azurerm_resource_group.fase1.name
  partition_count     = 2
  message_retention   = 1
}
# azurerm_eventhub "oracle" e "minio" seguem o mesmo padrão
```

### 2. Kafka Connect worker — Event Hub como backend (Etapa 1, item 6)

```properties
# debezium/connect-worker-eventhub.properties.template
bootstrap.servers=UBEREATS-FASE1-EVENTHUB-NS.servicebus.windows.net:9093
security.protocol=SASL_SSL
sasl.mechanism=PLAIN
sasl.jaas.config=org.apache.kafka.common.security.plain.PlainLoginModule required username="$ConnectionString" password="REPLACE_EVENTHUB_NAMESPACE_CONNECTION_STRING";

group.id=ubereats-fase1-connect-cluster
offset.storage.topic=connect-offsets
config.storage.topic=connect-configs
status.storage.topic=connect-status
offset.storage.replication.factor=1
config.storage.replication.factor=1
status.storage.replication.factor=1

key.converter=org.apache.kafka.connect.json.JsonConverter
value.converter=org.apache.kafka.connect.json.JsonConverter
```

### 3. Kafka Connect HDFS 2 Sink Connector — Event Hub → ADLS Gen2 (Etapa 2, item 10, Decisão 1/2)

```json
{
  "name": "adls-bronze-sink-connector",
  "config": {
    "connector.class": "io.confluent.connect.hdfs.HdfsSinkConnector",
    "tasks.max": "2",
    "topics": "postgres.public.drivers,postgres.public.users,oracle.UBEREATS.ORDERS,oracle.UBEREATS.PAYMENTS,oracle.UBEREATS.RECEIPTS,oracle.UBEREATS.ORDER_ITEMS,oracle.UBEREATS.INVENTORY,oracle.UBEREATS.PRODUCTS,oracle.UBEREATS.RESTAURANTS",
    "store.url": "abfss://bronze@REPLACE_STORAGE_ACCOUNT.dfs.core.windows.net/",
    "format.class": "io.confluent.connect.hdfs.json.JsonFormat",
    "flush.size": "100",
    "rotate.interval.ms": "60000",
    "hadoop.conf.dir": "/etc/kafka-connect/hadoop-conf",
    "key.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable": "false",
    "value.converter.schemas.enable": "false"
  }
}
```

```xml
<!-- hadoop-conf/core-site.xml — autenticação OAuth via Service Principal (Decisão 4) -->
<configuration>
  <property><name>fs.azure.account.auth.type</name><value>OAuth</value></property>
  <property><name>fs.azure.account.oauth.provider.type</name>
    <value>org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider</value></property>
  <property><name>fs.azure.account.oauth2.client.id</name><value>REPLACE_SP_CLIENT_ID</value></property>
  <property><name>fs.azure.account.oauth2.client.secret</name><value>REPLACE_SP_CLIENT_SECRET</value></property>
  <property><name>fs.azure.account.oauth2.client.endpoint</name>
    <value>https://login.microsoftonline.com/REPLACE_TENANT_ID/oauth2/token</value></property>
</configuration>
```

### 4. MinIO — notificação nativa tipo Kafka apontando pro Event Hub (Etapa 1, item 7, Decisão 5)

```bash
mc admin config set minio/ notify_kafka:eventhub \
  brokers="UBEREATS-FASE1-EVENTHUB-NS.servicebus.windows.net:9093" \
  topic="minio" \
  sasl="on" \
  sasl_mechanism="PLAIN" \
  sasl_username='$ConnectionString' \
  sasl_password="REPLACE_EVENTHUB_NAMESPACE_CONNECTION_STRING" \
  tls="on"

mc admin service restart minio/
mc event add minio/uber-eats arn:minio:sqs::eventhub:kafka --event put,delete
```

### 5. Databricks Bronze — Oracle via `read_files` (Auto Loader), modo Triggered (Etapa 3, item 18, Decisão 3)

```sql
-- pipeline/bronze/ingest_oracle_orders.sql (trecho alterado)
CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_orders_raw AS
SELECT
  CAST(value AS STRING) AS json_value
FROM STREAM read_files(
  path => 'abfss://bronze@REPLACE_STORAGE_ACCOUNT.dfs.core.windows.net/oracle/orders/',
  format => 'json'
);
-- Restante do arquivo (view_oracle_orders_pre_processed, APPLY CHANGES INTO,
-- SEQUENCE BY cdc_sequence) permanece EXATAMENTE igual — só a fonte mudou.
```

### 6. Unity Catalog — storage credential (Service Principal) + external location (Etapa 3, item 15, Decisão 4)

```hcl
resource "databricks_storage_credential" "adls_bronze" {
  name = "adls-bronze-fase1-credential"
  azure_service_principal {
    directory_id   = var.azure_tenant_id
    application_id = azuread_application.fase1_sp.application_id
    client_secret  = azuread_application_password.fase1_sp.value
  }
}

resource "databricks_external_location" "bronze" {
  name            = "adls-bronze-fase1"
  url             = "abfss://bronze@${azurerm_storage_account.fase1.name}.dfs.core.windows.net/"
  credential_name = databricks_storage_credential.adls_bronze.name
}
```

### 7. Synapse Dedicated — `COPY INTO` + `MERGE` (SCD2) a partir do ADLS Gen2/Bronze

```sql
-- sql/azure/synapse_copy_merge.sql (exemplo: orders)
COPY INTO staging.stg_orders
FROM 'https://REPLACE_STORAGE_ACCOUNT.dfs.core.windows.net/bronze/oracle/orders/'
WITH (
  FILE_TYPE = 'JSON',
  CREDENTIAL = (IDENTITY = 'Managed Identity')
);

MERGE INTO warehouse.orders AS target
USING (
  SELECT *
  FROM staging.stg_orders
  QUALIFY ROW_NUMBER() OVER (PARTITION BY order_id ORDER BY cdc_sequence DESC) = 1
) AS source
ON target.order_id = source.order_id
WHEN MATCHED AND source.cdc_operation = 'd' THEN DELETE
WHEN MATCHED THEN UPDATE SET target.status = source.status, target._cdc_commit_ts = source.cdc_commit_ts
WHEN NOT MATCHED AND source.cdc_operation != 'd' THEN
  INSERT (order_id, status, _cdc_commit_ts) VALUES (source.order_id, source.status, source.cdc_commit_ts);
```

---

## Testing Strategy

| Tipo de teste | Escopo | Quando |
|---|---|---|
| `terraform validate`/`terraform plan` | Toda a infraestrutura do manifesto (Etapas 1-4) | Antes de qualquer `apply`, em cada etapa |
| Smoke test Event Hub (Etapa 1) | Destino "Kafka" do Airbyte e worker do Kafka Connect conseguem produzir no Event Hub (tier Standard aceita os tópicos internos do Connect) | Manual, logo após o Event Hub subir — valida Assumption A-003 do DEFINE |
| Smoke test MinIO → Event Hub (Etapa 1) | `mc event add` configurado; um objeto novo no MinIO aparece no tópico `minio` do Event Hub em segundos | Manual, após configurar a notificação (Decisão 5) |
| Smoke test do Sink Connector (Etapa 2) | Sink consome os tópicos `postgres.*`/`oracle.*`; arquivos aparecem no ADLS Gen2/Bronze preservando `op`/`before`/`after`/SCN e `_ab_cdc_*` | `tests/azure/test_adls_sink_cdc_mapping.py` (item 30) + manual |
| Smoke test Synapse (Etapa 2) | `COPY INTO` + `MERGE` executa sem erro; contagem de linhas bate com a origem | Manual, após o primeiro ciclo do sink |
| Smoke test Databricks Bronze (Etapa 3) | Pipeline Triggered executa `read_files` + `APPLY CHANGES INTO` sem erro para as 9 tabelas Postgres/Oracle e a nova MongoDB | Manual, após a external location subir |
| Join de integridade (Etapas 2-3) | Mesma disciplina das Ondas 1-3 e das Fases 2/3: query Synapse/Databricks entre entidades relacionadas retorna 0 órfãos | Após cada etapa concluída |
| Smoke test Stream Analytics (Etapa 4) | `UPDATE` real em Postgres/Oracle; evento aparece no Event Hub; job ASA processa e enriquece via reference data input | Manual, após deploy do job (item 28) |
| `/pipeline-review-init` | Lanes `data_contracts`, `architecture_medallion`, `idempotency_reprocessing`, `security_governance` no mínimo (mandatos MED-M04/GOV-M01/GOV-M02 do DEFINE) | Após o Build completo de cada etapa, antes de avançar para a próxima |

---

## Riscos carregados do DEFINE (com mitigação de design)

| Risco (DEFINE) | Mitigação de design |
|---|---|
| A-001 — Kafka Connect com 2 sinks simultâneos a partir de 1 captura Oracle | **Eliminado, não mitigado** — Decisão 1 remove a necessidade de 2 sinks no MESMO conector; agora são 2 conectores independentes (1 source, 1 sink) compartilhando o Event Hub como qualquer topologia Kafka Connect padrão |
| A-002 — Postgres com 2 replication slots simultâneos | **Eliminado, não mitigado** — Decisão 1 remove a 2ª conexão Airbyte; só existe 1 captura CDC do Postgres |
| A-003 — Event Hubs Standard tier suporta os tópicos internos do Kafka Connect | Ainda não eliminado — mitigação continua sendo o smoke test da Etapa 1, primeira coisa a validar no `/build`, antes de qualquer conector real ser configurado |
| A-004 — Autenticação do Unity Catalog contra o ADLS Gen2 (workspace fora da subscription) | Resolvido pela Decisão 4 (Service Principal) — sem mais incerteza de design, só a rotação do client secret fica como item operacional do `/build` |

---

## Status: ✅ Complete (Designed)

**Próximo passo:** `/build .claude/sdd/features/DESIGN_INGESTAO_AZURE_FASE1.md`
