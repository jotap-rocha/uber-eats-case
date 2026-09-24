# DESIGN: Arquitetura de Ingestão — Fase 3 (GCP)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_GCP_FASE3 |
| **Input** | `.claude/sdd/features/DEFINE_INGESTAO_GCP_FASE3.md` |
| **Status** | ✅ Complete (Designed) |
| **Data** | 2026-09-11 |

---

## Architecture Overview

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│      ETAPA 1 — Warehouse (bastion + túnel SSH + Datastream batch + STS + BigQuery)     │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Fase 0 (Postgres/Oracle/MongoDB/MinIO em Docker/ShadowTraffic) permanece LOCAL         │
│  (Decisão distinta da AWS: sem migrar para GCE)                                        │
│                    │                                                                    │
│         ┌──────────┴──────────┐                                                        │
│         ▼                     ▼                                                        │
│  autossh (systemd,      MinIO (outbound,                                               │
│  máquina local) ──▶     agente STS local)                                              │
│  bastion GCE (público)         │                                                        │
│         │                      │                                                        │
│         ▼                      ▼                                                        │
│  Datastream (3 streams:  Storage Transfer Service                                      │
│  Postgres CDC, Oracle    (fonte "S3-compatible")                                        │
│  CDC/LogMiner, Mongo            │                                                        │
│  full load) via                 │                                                        │
│  "Forward SSH tunnel"           │                                                        │
│         │                       │                                                        │
│         └───────────┬───────────┘                                                        │
│                      ▼                                                                   │
│               GCS (Bronze) — arquivos JSON/Avro por evento (Datastream) + objetos (STS) │
│                      │                                                                   │
│                      ▼                                                                   │
│          BigQuery — job `LOAD`/`MERGE` periódico (storage nativo, sem query-in-place)   │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│              ETAPA 2 — Lakehouse (Dataplex + BigLake Iceberg + Dataproc)                │
├──────────────────────────────────────────────────────────────────────────────────────┤
│                        GCS (Bronze, já populado na Etapa 1)                              │
│                              │                                                          │
│                              ▼                                                          │
│         Job Dataproc (Spark + Iceberg writer) — MERGE dos arquivos brutos               │
│         do GCS/Bronze para tabelas Iceberg do BigLake (mesmo papel que o                │
│         Glue Crawler cumpriu na AWS, mas via job explícito)                             │
│                              │                                                          │
│                              ▼                                                          │
│              Dataplex Universal Catalog (metadados/governança) ──▶ Dataproc (consulta)  │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│     ETAPA 3 — Kappa (Debezium Server ×2 + Cloud Function ponte + Dataflow)              │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Debezium Server        Debezium Server        MinIO ──notificação──▶ Cloud            │
│  (postgres, logical     (oracle, LogMiner)      (bucket, Webhook)     Function ponte    │
│  decoding) ──▶ Pub/Sub  ──▶ Pub/Sub                                   ──▶ Pub/Sub       │
│  (push, sem túnel)      (push, sem túnel)                             (push, sem túnel) │
│      │                       │                                            │             │
│      └───────────────────────┴────────────────────────────────────────────┘             │
│                              ▼                                                          │
│                    Pub/Sub (tópico único do trilho real-time)                          │
│                              │                                                          │
│                              ▼                                                          │
│              Dataflow (pipeline Beam, consumidor do Kappa)                              │
│                    │ lookup/enriquecimento (side input com refresh periódico)           │
│                    ▼                                                                   │
│         BigLake Iceberg tables — cópia do MongoDB, já materializada na Etapa 2          │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Contrato canônico de CDC — extensão para o Datastream e o Debezium Server (transversal, aplicado desde a Etapa 1):**

| Coluna canônica | De onde vem (Datastream, Fase 3) | De onde vem (Debezium Server, Fase 3) |
|---|---|---|
| `cdc_operation` | `_metadata_change_type` (`INSERT`/`UPDATE`/`DELETE`/`UPSERT`) | `payload.op` (`c`/`u`/`d`) — mesmo envelope já usado pelo Debezium Connect da Onda 3 |
| `cdc_commit_ts` | `_metadata_source_timestamp` | `payload.source.ts_ms` |
| `cdc_sequence` | `_metadata_source.lsn` (Postgres) / `_metadata_source.scn` (Oracle) — Datastream não garante ordenação nativa, mas expõe esses campos por evento (achado do roadmap v1.4) | `payload.source.lsn` (Postgres) / `payload.source.scn` (Oracle) |
| `cdc_source_system` | constante por stream (`'postgres-datastream-gcp'`, `'oracle-datastream-gcp'`, `'mongo-datastream-gcp'`) | constante por instância (`'postgres-debezium-server-gcp'`, `'oracle-debezium-server-gcp'`) |

O consumo (BigQuery, Dataproc, Dataflow) **nunca** lê os campos nativos de Datastream/Debezium Server diretamente — só as 4 colunas canônicas, mesma disciplina já estabelecida na Onda 3, na Fase 2/AWS e agora estendida à Fase 3. **Nota de risco (carregada do DEFINE, A-002):** o formato exato de `_metadata_source.lsn`/`scn` do Datastream precisa ser confirmado com um teste real no início do `/build` — a leitura aqui é da documentação, não testada neste projeto ainda (mesmo padrão de risco já visto no Design da Onda 3/Oracle e da Fase 2/AWS/DMS).

---

## Decisões (ADRs inline)

### Decisão 1 — Bastion GCE mínimo + `autossh`/systemd na máquina local, sem migrar a Fase 0

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Data** | 2026-09-11 |

**Contexto:** o Datastream é *pull-based* — precisa iniciar a conexão até Postgres/Oracle/MongoDB. O DEFINE já fechou (decisão do usuário, brainstorm) que a Fase 0 permanece local, ao contrário da AWS (que migrou para EC2 dentro da VPC).

**Escolha:** uma **GCE VM mínima** (`e2-micro`, só como bastion — não roda o `docker-compose.yml`), com IP público e firewall restrito a Datastream + IP administrativo; um serviço **`autossh`** rodando como unit `systemd` na máquina local abre e mantém um túnel SSH reverso, mapeando portas do bastion (`127.0.0.1:15432`→Postgres local `5432`, `127.0.0.1:11521`→Oracle local `1521`, `127.0.0.1:27017`→MongoDB local `27017`) para as portas correspondentes na máquina local. O Datastream usa "Private connectivity — Forward SSH tunnel" apontando para o bastion, com o hostname do banco sendo `127.0.0.1` e a porta sendo a porta mapeada.

**Racional:** resolve a conectividade sem duplicar a infraestrutura da Fase 0 (diferente da AWS). O bastion é intencionalmente mínimo — não processa dado, só encaminha a conexão SSH.

**Alternativas rejeitadas:**
1. GCE VM replicando o `docker-compose.yml` da Fase 0 (espelhando a EC2 da AWS) — descartada no brainstorm (Abordagem D); usuário priorizou não duplicar a infraestrutura local.
2. IP público direto na máquina local com firewall restrito a IPs do Datastream — mesma objeção de segurança já levantada na AWS (expõe portas de banco de dados à internet, mesmo que filtradas).

**Consequências:** novo risco operacional específico desta fase (Assumption A-001 do DEFINE) — o túnel precisa se manter vivo; `autossh` reconecta automaticamente em caso de queda de rede, mas uma queda prolongada da máquina local interrompe o Datastream até a reconexão. Mitigação: `systemd` com `Restart=always` + `OBS-M01` (log estruturado de saúde do túnel, recomendado no DEFINE).

### Decisão 2 — Debezium Server como duas instâncias separadas (uma por fonte), não uma instância multi-conector

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o Debezium Server (diferente do Debezium Connect/Kafka Connect já usado na Onda 3 para o Oracle) roda como processo standalone, configurado via `application.properties`, e suporta **um único conector de origem por instância** (`debezium.source.connector.class`).

**Escolha:** dois containers novos no `docker-compose.yml` local — `debezium-server-postgres` (conector `io.debezium.connector.postgresql.PostgresConnector`, `slot.name` dedicado, diferente do slot já usado por qualquer consumidor existente) e `debezium-server-oracle` (conector `io.debezium.connector.oracle.OracleConnector`, LogMiner) — ambos com `debezium.sink.type=pubsub`, publicando em tópicos Pub/Sub distintos (`ubereats-kappa-postgres`, `ubereats-kappa-oracle`) ou no mesmo tópico com atributo de mensagem identificando a origem (decisão de implementação, ver Código Pattern 3).

**Racional:** Debezium Server não suporta múltiplos conectores na mesma instância — não há opção "compartilhada" a considerar. Dois containers pequenos e independentes são mais simples de operar/reiniciar isoladamente do que tentar uma solução multi-processo dentro de um único container.

**Consequências:** +2 containers no `docker-compose.yml` local (item já contabilizado no dimensionamento de recursos da máquina, que já roda Postgres+Oracle+MongoDB+MinIO+ShadowTraffic+Redpanda+Kafka Connect da Onda 3). Cada instância abre seu próprio replication slot (Postgres) ou sessão LogMiner (Oracle) — soma-se ao Airbyte (Onda 3, Postgres) e ao Debezium Connect existente (Onda 3, Oracle) já consumindo essas fontes, o que é exatamente o risco de concorrência registrado como Assumption A-003 do DEFINE.

### Decisão 3 — Storage Transfer Service via agente containerizado, reaproveitando o `docker-compose.yml` local (sem VM dedicada, diferente da AWS)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** a AWS precisou de uma EC2 dedicada só para rodar a AMI do agente DataSync (item 5, `infra/aws/fase2-ingestao/datasync.tf`). O agente on-premises do Storage Transfer Service, ao contrário, é distribuído como **imagem Docker** (`gcr.io/cloud-ingest/tsops-agent`), sem precisar de uma VM inteira.

**Escolha:** novo serviço `sts-agent` no `docker-compose.yml` **local** (não numa VM GCP), registrado no mesmo agent pool do projeto GCP, com acesso de rede ao `minio-ubereats` (mesma rede Docker) e credenciais de saída para a API do Storage Transfer Service (outbound, sem exigir túnel).

**Racional:** mais simples e mais barato que o padrão da AWS — não precisa de VM dedicada nem do bastion (STS é push-based do ponto de vista do agente, que inicia a conexão para fora).

**Alternativas rejeitadas:**
1. GCE VM dedicada rodando o agente (espelhando a AMI da AWS) — desnecessário, já que o agente oficial roda em container.

**Consequências:** +1 container no `docker-compose.yml` local; nenhuma infraestrutura GCP nova além do registro do agent pool e da location.

### Decisão 4 — BigQuery consome do GCS bruto (arquivos Datastream), não das tabelas Iceberg do BigLake

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE já fechou (decisão do usuário) que o BigQuery sempre carrega fisicamente, sem query-in-place. Isso implica escolher **de onde exatamente** o job `LOAD`/`MERGE` lê.

**Escolha:** o Datastream é configurado com destino **"Cloud Storage"** clássico (arquivos JSON/Avro por evento de mudança, um por tabela/partição de tempo) — não o destino nativo "BigLake Iceberg tables" que o Datastream também suporta. O BigQuery faz `LOAD DATA`/job em lote a partir desses arquivos brutos, seguido de `MERGE` usando o contrato canônico de CDC (dedup/upsert por `cdc_sequence`), para dentro do seu storage nativo. As tabelas Iceberg do BigLake (Etapa 2, Decisão 5) são materializadas **separadamente**, a partir do mesmo GCS/Bronze.

**Racional:** usar o destino "BigLake Iceberg tables" nativo do Datastream acopla a Etapa 1 (Warehouse) à Etapa 2 (Lakehouse) — a mesma tabela física serviria os dois papéis, o que reabriria a discussão de query-in-place já fechada no brainstorm (Abordagem B, rejeitada). Manter GCS bruto como landing único, com dois consumidores separados (BigQuery via `LOAD`/`MERGE`; BigLake Iceberg via job Dataproc), reproduz exatamente o padrão já usado na AWS (S3 alimentando Redshift `COPY`/`MERGE` **e** Glue/Iceberg/Athena, sem ingestão duplicada) e na Azure (ADLS Gen2 alimentando Synapse `COPY INTO` **e** Databricks).

**Alternativas rejeitadas:**
1. Datastream → destino nativo BigLake Iceberg tables, com BigQuery consultando essas mesmas tabelas — implicaria query-in-place, decisão já revertida pelo usuário no brainstorm.

**Consequências:** dois pipelines de consumo (BigQuery `LOAD`/`MERGE` e Dataproc Iceberg `MERGE`) leem o mesmo GCS/Bronze de forma independente — sem ingestão duplicada na origem, mas com duas lógicas de dedup/idempotência a manter (mandato MED-M04 do DEFINE).

### Decisão 5 — Job Dataproc materializa as tabelas Iceberg do BigLake (papel equivalente ao Glue Crawler da AWS, mas explícito)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** na AWS, o Glue Crawler infere e mantém o catálogo Iceberg sobre o S3/Bronze de forma quase automática. O GCP não tem um crawler equivalente que também escreva formato Iceberg verdadeiro (manifests/snapshots) — só cataloga o que já existe.

**Escolha:** um job **Dataproc (PySpark + Iceberg writer)**, agendado (Cloud Composer/Cloud Scheduler — detalhar no `/build`), lê os arquivos brutos do GCS/Bronze (mesmos consumidos pelo BigQuery na Decisão 4) e executa `MERGE INTO` numa tabela Iceberg gerenciada, usando o contrato canônico de CDC para idempotência — mesmo princípio do `APPLY CHANGES INTO` já usado no Databricks deste projeto (Onda 3).

**Racional:** o Dataproc já é a ferramenta de processamento da Lakehouse GCP (roadmap, "2ª arquitetura: BigLake/Dataproc + Iceberg") — reaproveitar o mesmo motor para materializar as tabelas evita introduzir uma ferramenta nova só para isso.

**Consequências:** a "frescura" do Lakehouse depende do agendamento deste job (mesma característica batch do Glue Crawler na AWS) — aceitável, já que o real-time é papel do Kappa (Etapa 3), não do Lakehouse.

### Decisão 6 — Dataflow como consumidor do Kappa, com lookup via side input refreshed periodicamente (mesmo princípio da Lambda da AWS)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE (A-004) deixou em aberto o mecanismo exato de lookup do consumidor contra a cópia do MongoDB.

**Escolha:** pipeline **Dataflow (Apache Beam, Python)**, streaming, lendo do Pub/Sub via `ReadFromPubSub`; o enriquecimento usa um **side input** (`beam.pvalue.AsDict`) recarregado periodicamente a partir da tabela Iceberg do MongoDB (via BigQuery Storage API ou leitura direta do BigLake), com o mesmo papel do cache-com-TTL da Lambda consumidora da AWS (`RestaurantProfileCache`).

**Racional:** side input com refresh periódico é o padrão idiomático do Beam/Dataflow para "tabela de referência pequena e quase estática" — evita uma leitura por evento (custo/latência) sem introduzir um serviço de cache dedicado (ex. Memorystore), consistente com a escolha equivalente já feita na AWS (Decisão 4 daquele Design).

**Alternativas rejeitadas:**
1. Leitura direta por evento (sem side input) — descartada pelo mesmo motivo já registrado na AWS: latência/custo desnecessários para uma fonte estática.
2. Memorystore/Redis dedicado — resolveria de forma mais robusta, mas é um serviço a mais para uma tabela de referência pequena (~500 documentos); reavaliar se o volume crescer muito, mesma ressalva já feita na AWS.

**Consequências:** mesma limitação já aceita na AWS — se o BigLake Iceberg for atualizado (novo `MERGE` do job Dataproc, Decisão 5) entre um refresh e outro do side input, pode haver inconsistência temporária; aceitável dado que o MongoDB é estático por definição (Onda 3).

### Decisão 7 — Cloud Function ponte (MinIO → Pub/Sub) desacoplada do consumidor do Kappa

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** mesmo racional da AWS (Decisão 5 daquele Design) — a ponte é infraestrutura pura (webhook → tópico), o consumidor tem lógica de negócio (enriquecimento).

**Escolha:** uma Cloud Function (Gen 2, Python, HTTP trigger via URL pública) só recebe a notificação de bucket do MinIO (destino Webhook) e publica no Pub/Sub; o Dataflow (Decisão 6) é o único responsável pelo enriquecimento.

**Racional:** MinIO não assina requisições (mesma limitação já documentada na AWS) — a validação de autenticidade é feita por um token estático no header `Authorization`, verificado dentro do handler, igual ao padrão já usado na Lambda ponte da AWS.

**Consequências:** +1 função Cloud Function no manifesto, com responsabilidade única — mesma vantagem de testabilidade já obtida na AWS.

---

## File Manifest

### Etapa 1 — Warehouse (bastion, Datastream, Storage Transfer Service, BigQuery)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 1 | `infra/gcp/fase3-ingestao/networking.tf` | Criar | VPC, subnet, firewall rules (Datastream + IP administrativo) para o bastion | @infra-deployer | — |
| 2 | `infra/gcp/fase3-ingestao/bastion.tf` | Criar | GCE VM mínima (`e2-micro`) como bastion SSH (Decisão 1) | @infra-deployer | 1 |
| 3 | `infra/gcp/fase3-ingestao/iam.tf` | Criar | Service accounts/roles least-privilege (Datastream, Storage Transfer Service, Cloud Function, Dataflow, Dataproc) | @infra-deployer | — |
| 4 | `deploy/autossh/ubereats-gcp-tunnel.service` | Criar | Unit `systemd` do `autossh` na máquina local, com `Restart=always` (Decisão 1) | (general) | 2 |
| 5 | `docs/gcp/bastion-ssh-tunnel-setup.md` | Criar | Passo a passo de configuração do túnel reverso, chaves SSH, portas mapeadas | (general) | 2, 4 |
| 6 | `infra/gcp/fase3-ingestao/datastream.tf` | Criar | 3 connection profiles (Postgres, Oracle, MongoDB) via "Forward SSH tunnel", + 3 streams com destino Cloud Storage (Decisão 4) | @infra-deployer | 2, 3, 5 |
| 7 | `infra/gcp/fase3-ingestao/gcs_bronze.tf` | Criar | Bucket GCS (Bronze), estrutura de prefixos por fonte/tabela | @infra-deployer | 3 |
| 8 | `infra/gcp/fase3-ingestao/storage_transfer.tf` | Criar | Agent pool + job de transferência (fonte "S3-compatible" → GCS/Bronze), agendado | @infra-deployer | 3, 7 |
| 9 | `docker-compose.yml` | Editar | Adicionar serviço `sts-agent` (Decisão 3), rede compartilhada com `minio-ubereats` | @infra-deployer | 8 |
| 10 | `sql/gcp/bigquery_load_merge.sql` | Criar | Job `LOAD`/`MERGE` por tabela, a partir do GCS/Bronze, projetando as 4 colunas canônicas de CDC (Decisão 4) | @databricks-sql-analyst (padrão de MERGE/SCD reaproveitável, mesmo raciocínio das Fases 1/2) | 6, 7 |
| 11 | `infra/gcp/fase3-ingestao/bigquery.tf` | Criar | Dataset BigQuery, tabelas nativas de destino, scheduled query ou Cloud Composer trigger para o item 10 | @infra-deployer | 3, 10 |
| 12 | `docs/data-contract-cdc-gcp-datastream.md` | Criar | Extensão do contrato canônico de CDC (Onda 3) com o mapeamento específico do Datastream (`_metadata_change_type`, `_metadata_source_timestamp`, `_metadata_source.lsn`/`scn` → contrato canônico) | (general) | — |

### Etapa 2 — Lakehouse (Dataplex, BigLake Iceberg, Dataproc)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 13 | `infra/gcp/fase3-ingestao/dataplex.tf` | Criar | Dataplex Universal Catalog: lake, zone, asset apontando para o GCS/Bronze e para as tabelas Iceberg do BigLake | @infra-deployer | 7 |
| 14 | `infra/gcp/fase3-ingestao/biglake_iceberg.tf` | Criar | Tabelas Iceberg gerenciadas do BigLake (conexão BigLake para o GCS/Bronze) | @infra-deployer | 7, 13 |
| 15 | `src/gcp/dataproc_iceberg_merge/merge_job.py` | Criar | Job PySpark: lê o GCS/Bronze, aplica `MERGE INTO` na tabela Iceberg do BigLake usando o contrato canônico de CDC (Decisão 5) | @databricks-data-engineer (padrão de MERGE/CDC idempotente reaproveitável) | 14 |
| 16 | `infra/gcp/fase3-ingestao/dataproc.tf` | Criar | Cluster/serverless batch Dataproc + agendamento (Cloud Scheduler) do job do item 15 | @infra-deployer | 3, 15 |
| 17 | `sql/gcp/dataproc_validation_queries.sql` | Criar | Queries de validação (contagem, join entre entidades, checagem de órfãos — mesma disciplina das Ondas 1/2/3 e da Fase 2/AWS) | (general) | 16 |

### Etapa 3 — Kappa (real-time)

| # | Arquivo | Ação | Propósito | Agente | Dependências |
|---|---------|--------|-----------|--------|---------------|
| 18 | `infra/gcp/fase3-ingestao/pubsub.tf` | Criar | Tópico(s) Pub/Sub do trilho real-time + subscription do Dataflow | @infra-deployer | 3 |
| 19 | `src/gcp/debezium_server_postgres/application.properties` | Criar | Config do Debezium Server: conector Postgres, `sink.type=pubsub`, slot dedicado (Decisão 2) | @databricks-data-engineer (mesmo padrão de config de CDC já usado no Debezium Connect da Onda 3) | 18 |
| 20 | `src/gcp/debezium_server_oracle/application.properties` | Criar | Config do Debezium Server: conector Oracle/LogMiner, `sink.type=pubsub` (Decisão 2) | @databricks-data-engineer | 18 |
| 21 | `docker-compose.yml` | Editar (mesmo arquivo do item 9) | Adicionar serviços `debezium-server-postgres` e `debezium-server-oracle` (imagem `debezium/server`), montando os `application.properties` dos itens 19/20 | @infra-deployer | 19, 20 |
| 22 | `src/gcp/cloud_function_minio_pubsub_bridge/main.py` | Criar | Recebe o Webhook de notificação de bucket do MinIO, valida o token estático, publica no Pub/Sub (Decisão 7) | @python-developer | 18 |
| 23 | `src/gcp/cloud_function_minio_pubsub_bridge/requirements.txt` | Criar | Dependências (`google-cloud-pubsub`, `functions-framework`) | @python-developer | 22 |
| 24 | `infra/gcp/fase3-ingestao/cloud_function_bridge.tf` | Criar | Deploy da Cloud Function (Gen 2) + URL HTTP pública + permissões | @infra-deployer | 3, 22, 23 |
| 25 | `docs/minio/webhook-notification-config-gcp.md` | Criar | Configuração da notificação de bucket do MinIO (destino Webhook, endpoint da Cloud Function do item 24) | (general) | 24 |
| 26 | `src/gcp/dataflow_kappa_consumer/pipeline.py` | Criar | Pipeline Beam: lê do Pub/Sub, identifica o tipo de entidade, aplica o side input de enriquecimento (Decisão 6) | @python-developer | 18 |
| 27 | `src/gcp/dataflow_kappa_consumer/mongo_lookup.py` | Criar | Carrega a cópia do MongoDB da tabela Iceberg do BigLake (Etapa 2), side input com refresh periódico (Decisão 6) | @python-developer | 14, 26 |
| 28 | `infra/gcp/fase3-ingestao/dataflow.tf` | Criar | Job Dataflow (streaming) + permissões de leitura BigLake/BigQuery | @infra-deployer | 3, 18, 26 |
| 29 | `src/gcp/cloud_function_minio_pubsub_bridge/teams_notify.py` | Criar | Alerta Teams em caso de falha da ponte (mandato SHOULD do DEFINE, TM-M01) | @teams-notifications-expert | 22 |
| 30 | `tests/gcp/test_cloud_function_bridge.py` | Criar | Testes unitários do parsing do Webhook e chamada de publish no Pub/Sub (mock do cliente) | @test-generator | 22 |
| 31 | `tests/gcp/test_dataflow_consumer_lookup.py` | Criar | Testes unitários do lookup/enriquecimento e do side input com refresh (mock do BigLake/BigQuery) | @test-generator | 26, 27 |

### Transversal

| # | Arquivo | Ação | Propósito |
|---|---------|--------|-----------|
| 32 | `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` | Verificar (provável no-op) | Confirmar que a versão v1.7 (já fechada no `/brainstorm`) reflete fielmente o resultado final deste `/design` — nenhuma decisão de Design contradiz o que já foi registrado |
| 33 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Verificar (provável no-op) | Confirmar que nenhuma mudança de modelo de domínio é necessária — esta feature é só de ingestão/infra, mesmo padrão da Fase 2/AWS |
| 34 | `infra/gcp/fase3-ingestao/variables.tf` | Criar | Variáveis (região, prefixo de projeto, CIDRs, credenciais sensíveis das fontes, tokens) — mesma disciplina de nunca hardcoded já usada em `infra/aws/fase2-ingestao/variables.tf` | — |
| 35 | `infra/gcp/fase3-ingestao/versions.tf`, `outputs.tf` | Criar | Boilerplate Terraform (providers, outputs relevantes) | 34 |

---

## Code Patterns

### 1. `systemd` unit — túnel SSH reverso (`autossh`), máquina local (Etapa 1)

```ini
# deploy/autossh/ubereats-gcp-tunnel.service
[Unit]
Description=Túnel SSH reverso Fase 3/GCP (Postgres/Oracle/MongoDB -> bastion GCE)
After=network-online.target
Wants=network-online.target

[Service]
Environment=AUTOSSH_GATETIME=0
ExecStart=/usr/bin/autossh -M 0 -N \
  -o "ServerAliveInterval 30" -o "ServerAliveCountMax 3" \
  -R 15432:localhost:5432 \
  -R 11521:localhost:1521 \
  -R 27017:localhost:27017 \
  -i /etc/ubereats-gcp/bastion_key \
  tunnel-user@BASTION_PUBLIC_IP
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

> O Datastream, ao configurar a "Forward SSH tunnel connectivity profile", aponta para `BASTION_PUBLIC_IP` como bastion, e usa `127.0.0.1:15432`/`11521`/`27017` (relativo ao bastion) como hostname/porta do banco — não o IP da máquina local, que nunca é exposto diretamente.

### 2. Datastream — stream Postgres CDC via túnel, destino Cloud Storage (Etapa 1)

```hcl
resource "google_datastream_connection_profile" "postgres_source" {
  connection_profile_id = "postgres-source-fase3"
  location               = var.gcp_region
  display_name           = "Postgres Fase 0 (via túnel)"

  postgresql_profile {
    hostname = "127.0.0.1"   # relativo ao bastion, via forward SSH tunnel
    port     = 15432
    username = "replication_user"
    password = var.postgres_password
    database = "ubereats"
  }

  forward_ssh_connectivity {
    hostname    = google_compute_instance.bastion.network_interface[0].access_config[0].nat_ip
    port        = 22
    username    = "tunnel-user"
    private_key = var.bastion_ssh_private_key
  }
}

resource "google_datastream_stream" "postgres_batch" {
  stream_id     = "postgres-batch-fase3"
  location      = var.gcp_region
  display_name  = "Postgres -> GCS Bronze (CDC)"

  source_config {
    source_connection_profile = google_datastream_connection_profile.postgres_source.id
    postgresql_source_config {
      publication   = "ubereats_datastream_pub"
      replication_slot = "ubereats_datastream_slot" # slot dedicado, distinto do Airbyte (Onda 3)
    }
  }

  destination_config {
    destination_connection_profile = google_datastream_connection_profile.gcs_bronze.id
    gcs_destination_config {
      path              = "/postgres"
      file_rotation_mb  = 100
      json_file_format {}
    }
  }

  backfill_all {}
}
```

### 3. Debezium Server — Postgres → Pub/Sub (Etapa 3, Decisão 2)

```properties
# src/gcp/debezium_server_postgres/application.properties
debezium.sink.type=pubsub
debezium.sink.pubsub.project.id=${GCP_PROJECT_ID}
debezium.sink.pubsub.ordering.enabled=true

debezium.source.connector.class=io.debezium.connector.postgresql.PostgresConnector
debezium.source.database.hostname=postgres-ubereats
debezium.source.database.port=5432
debezium.source.database.user=${POSTGRES_DEBEZIUM_USER}
debezium.source.database.password=${POSTGRES_DEBEZIUM_PASSWORD}
debezium.source.database.dbname=ubereats
debezium.source.slot.name=ubereats_debezium_server_slot
debezium.source.plugin.name=pgoutput
debezium.source.topic.prefix=postgres-gcp
debezium.source.database.server.name=postgres-gcp
# cdc_source_system canônico
debezium.transforms=addSourceSystem
debezium.transforms.addSourceSystem.type=org.apache.kafka.connect.transforms.InsertField$Value
debezium.transforms.addSourceSystem.static.field=cdc_source_system
debezium.transforms.addSourceSystem.static.value=postgres-debezium-server-gcp
```

```yaml
# docker-compose.yml — item 21 do manifesto
  debezium-server-postgres:
    image: debezium/server:3.0
    container_name: debezium-server-postgres
    depends_on:
      postgres-ubereats:
        condition: service_healthy
    env_file: ./gen/.env
    volumes:
      - ./src/gcp/debezium_server_postgres/application.properties:/debezium/conf/application.properties:ro
      - ./gen/gcp-credentials.json:/debezium/gcp-credentials.json:ro
    environment:
      - GOOGLE_APPLICATION_CREDENTIALS=/debezium/gcp-credentials.json

  debezium-server-oracle:
    image: debezium/server:3.0
    container_name: debezium-server-oracle
    depends_on:
      oracle-ubereats:
        condition: service_healthy
    env_file: ./gen/.env
    volumes:
      - ./src/gcp/debezium_server_oracle/application.properties:/debezium/conf/application.properties:ro
      - ./gen/gcp-credentials.json:/debezium/gcp-credentials.json:ro
    environment:
      - GOOGLE_APPLICATION_CREDENTIALS=/debezium/gcp-credentials.json
```

> Nota: `debezium.source.slot.name` do Postgres é deliberadamente **diferente** do slot já usado por qualquer consumidor existente (Airbyte da Onda 3) — Postgres suporta múltiplos replication slots concorrentes por natureza, o que reduz (mas não elimina, ver Assumption A-003) o risco de conflito, diferente do Oracle/LogMiner.

### 4. Cloud Function ponte — MinIO Webhook → Pub/Sub `publish` (Etapa 3, Decisão 7)

```python
# src/gcp/cloud_function_minio_pubsub_bridge/main.py
import json
import os

import functions_framework
from google.cloud import pubsub_v1

PROJECT_ID = os.environ["GCP_PROJECT_ID"]
TOPIC_ID = os.environ["PUBSUB_TOPIC_MINIO"]
AUTH_TOKEN = os.environ["MINIO_WEBHOOK_AUTH_TOKEN"]

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)


@functions_framework.http
def handler(request):
    """Recebe o payload do Webhook de notificação de bucket do MinIO
    (formato compatível com S3 Event Notification: Records[].s3.object.key etc.)
    e publica uma mensagem no Pub/Sub por objeto notificado."""
    if request.headers.get("Authorization") != f"Bearer {AUTH_TOKEN}":
        return ("unauthorized", 401)

    body = request.get_json(silent=True) or {}
    records = body.get("Records", [])

    for record in records:
        payload = {
            "bucket": record["s3"]["bucket"]["name"],
            "key": record["s3"]["object"]["key"],
            "event_name": record["eventName"],
            "cdc_source_system": "minio-ubereats",
        }
        publisher.publish(topic_path, json.dumps(payload).encode("utf-8"))

    return ({"processed": len(records)}, 200)
```

### 5. Dataflow — consumidor do Kappa com side input do MongoDB (Etapa 3, Decisão 6)

```python
# src/gcp/dataflow_kappa_consumer/pipeline.py
import json

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from mongo_lookup import load_restaurant_profiles


class EnrichWithRestaurantProfile(beam.DoFn):
    def process(self, element: bytes, profiles: dict):
        payload = json.loads(element)
        restaurant_id = payload.get("restaurant_id")
        if restaurant_id is not None and restaurant_id in profiles:
            payload["restaurant_profile"] = profiles[restaurant_id]
        yield payload


def run(pipeline_args: list[str]) -> None:
    options = PipelineOptions(pipeline_args, streaming=True)
    with beam.Pipeline(options=options) as pipeline:
        # Side input recarregado a cada janela fixa (ex. 5 min) — mesmo papel do
        # cache-com-TTL da Lambda consumidora na AWS (Decisão 6 deste Design).
        profiles_side_input = (
            pipeline
            | "PeriodicImpulse" >> beam.transforms.periodicsequence.PeriodicImpulse(
                fire_interval=300
            )
            | "LoadProfiles" >> beam.Map(lambda _: load_restaurant_profiles())
        )

        (
            pipeline
            | "ReadFromPubSub" >> beam.io.ReadFromPubSub(topic="projects/{}/topics/{}".format(
                "${GCP_PROJECT_ID}", "ubereats-kappa"
            ))
            | "Enrich" >> beam.ParDo(
                EnrichWithRestaurantProfile(), profiles=beam.pvalue.AsSingleton(profiles_side_input)
            )
            # Destino final (novo tópico, BigQuery streaming insert, log estruturado)
            # — detalhar no /build, quando o formato de consumo downstream do Kappa
            # for definido (mesma pendência já registrada na AWS).
        )
```

```python
# src/gcp/dataflow_kappa_consumer/mongo_lookup.py
"""Carrega a cópia do MongoDB ('Perfil de Restaurante') já materializada como
tabela Iceberg do BigLake (Etapa 2) — mesmo papel do RestaurantProfileCache
da AWS, mas via side input do Beam em vez de cache local com TTL."""
from google.cloud import bigquery

_client = bigquery.Client()


def load_restaurant_profiles() -> dict:
    query = "SELECT restaurant_id, menu, horarios FROM `biglake_iceberg.perfil_restaurante`"
    rows = _client.query(query).result()
    return {row["restaurant_id"]: dict(row) for row in rows}
```

### 6. BigQuery — `LOAD`/`MERGE` a partir do GCS/Bronze (Etapa 1, Decisão 4)

```sql
-- sql/gcp/bigquery_load_merge.sql (exemplo: restaurants)
LOAD DATA INTO `ubereats_bronze.stg_restaurants`
FROM FILES (
  format = 'JSON',
  uris = ['gs://ubereats-fase3-bronze/postgres/restaurants/*.json']
);

MERGE `ubereats_warehouse.restaurants` AS target
USING (
  SELECT *
  FROM `ubereats_bronze.stg_restaurants`
  QUALIFY ROW_NUMBER() OVER (PARTITION BY restaurant_id ORDER BY cdc_sequence DESC) = 1
) AS source
ON target.restaurant_id = source.restaurant_id
WHEN MATCHED AND source.cdc_operation = 'DELETE' THEN DELETE
WHEN MATCHED THEN UPDATE SET
  target.name = source.name,
  target.cuisine_type = source.cuisine_type,
  target.average_rating = source.average_rating,
  target._cdc_commit_ts = source.cdc_commit_ts
WHEN NOT MATCHED AND source.cdc_operation != 'DELETE' THEN
  INSERT (restaurant_id, name, cuisine_type, average_rating, _cdc_commit_ts)
  VALUES (source.restaurant_id, source.name, source.cuisine_type, source.average_rating, source.cdc_commit_ts);
```

---

## Testing Strategy

| Tipo de teste | Escopo | Quando |
|---|---|---|
| `terraform validate`/`terraform plan` | Toda a infraestrutura do manifesto (Etapas 1-3) | Antes de qualquer `apply`, em cada etapa |
| Smoke test de conectividade (Etapa 1) | Túnel `autossh` ativo; Datastream consegue abrir replication slot/LogMiner/oplog através do bastion | Manual, logo após o bastion e o túnel subirem |
| Smoke test Storage Transfer Service (Etapa 1) | Agente containerizado registrado no agent pool; job de sync executa e novos objetos do MinIO aparecem no GCS/Bronze | Manual, após configurar o job |
| Smoke test BigQuery (Etapa 1) | `LOAD`/`MERGE` executa sem erro; contagem de linhas bate com a origem | Manual, após o primeiro ciclo do job |
| Smoke test Dataproc/Iceberg (Etapa 2) | Job PySpark materializa a tabela Iceberg; Dataplex reconhece o asset | Manual, após o primeiro `MERGE` |
| Testes unitários — Cloud Function ponte (Etapa 3) | `tests/gcp/test_cloud_function_bridge.py`: parsing do Webhook, validação do token, chamada correta ao `publish` (mock do cliente Pub/Sub) | Build, antes do deploy |
| Testes unitários — Dataflow consumidor (Etapa 3) | `tests/gcp/test_dataflow_consumer_lookup.py`: enriquecimento correto, comportamento quando `restaurant_id` não existe no side input | Build, antes do deploy |
| Smoke test de streaming (Etapa 3) | `UPDATE` real em Postgres/Oracle; confirmar evento no Pub/Sub em segundos; confirmar que o Dataflow processa e enriquece | Manual, após deploy do Debezium Server e do Dataflow |
| Join de integridade (todas as etapas) | Mesma disciplina das Ondas 1/2/3 e da Fase 2/AWS: query BigQuery/Dataproc entre entidades relacionadas retorna 0 órfãos | Após cada etapa concluída |
| `/pipeline-review-init` | Lanes `data_contracts`, `architecture_medallion`, `idempotency_reprocessing`, `security_governance` no mínimo (mandatos MED-M04/GOV-M01 do DEFINE) | Após o Build completo de cada etapa, antes de avançar para a próxima |

---

## Riscos carregados do DEFINE (com mitigação de design)

| Risco (DEFINE) | Mitigação de design |
|---|---|
| A-001 — estabilidade do túnel SSH reverso | Decisão 1 (`autossh` + `systemd` com `Restart=always`) mitiga reconexões transitórias; queda prolongada da máquina local ainda interrompe o Datastream — sem solução de design adicional, risco aceito e documentado (`docs/gcp/bastion-ssh-tunnel-setup.md`) |
| A-002 — formato dos metadados de ordenação do Datastream/Debezium Server para `cdc_sequence` | Mapeamento proposto (Architecture Overview, tabela de contrato canônico) documentado em `docs/data-contract-cdc-gcp-datastream.md` (item 12) — precisa de confirmação com teste real no início do `/build`, mesmo padrão de risco já visto na Onda 3 (Oracle LogMiner) e na Fase 2/AWS (DMS) |
| A-003 — concorrência entre Datastream (Etapa 1) e Debezium Server (Etapa 3) na mesma fonte | Sequenciamento por etapa (Goals do DEFINE) confina o Debezium Server à Etapa 3, última do roadmap desta fase — mitigação operacional, não técnica. Postgres usa slots distintos (suporta múltiplos nativamente); Oracle/LogMiner é o caso de maior risco (mesma ressalva já registrada na Fase 2/AWS) — se não suportar, o plano B é uma única ferramenta de captura com fan-out (ex. só Debezium Server, com um sink adicional simulando o papel do Datastream), sem precisar redesenhar do zero |
| A-004 — latência do lookup do Dataflow contra o MongoDB (BigLake Iceberg) | Decisão 6 (side input com refresh periódico) resolve para o volume esperado (~500 documentos); reavaliar para Memorystore só se o volume crescer muito |

---

## Status: ✅ Complete (Designed)

**Próximo passo:** `/build .claude/sdd/features/DESIGN_INGESTAO_GCP_FASE3.md`
