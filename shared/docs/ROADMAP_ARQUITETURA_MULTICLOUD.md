# Uber Eats — Roadmap de Arquiteturas de Dados Multi-Cloud

**Documento de planejamento**

**Versão:** 1.9

**Data:** Setembro/2026

> Renomeado de `docs/plan.md` para `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (v1.1) — mesmo documento, nome mais intuitivo, refletindo o próprio título. Ver "Histórico de revisões" ao final.

---

## 1. Objetivo

Implementar as arquiteturas **Warehouse**, **Lakehouse** e **Kappa**, reaproveitando o dado do projeto pessoal "Uber Eats", distribuídas nas 3 principais clouds (**Azure**, **AWS** e **GCP**) — sendo:

- **Azure**: as 3 arquiteturas completas, reaproveitando o trabalho de Lakehouse já feito com Databricks
- **AWS** e **GCP**: as 3 arquiteturas completas, usando a **stack de dados nativa** de cada cloud (sem Databricks)

**Finalidade:** fortalecer simultaneamente o conhecimento de arquitetura de dados e das 3 principais clouds, consolidando portfólio técnico para processos seletivos.

---

## 2. Premissas e princípios

| Princípio | Detalhe |
|---|---|
| Cadência | ~3h por semana, sem prazo fixo — as estimativas de tempo abaixo servem como bússola, não como compromisso |
| Abertura de conta cloud | Somente no início de cada fase correspondente, dado que os créditos de free tier têm validade curta (Azure: 30 dias; AWS: até 6 meses; GCP: 90 dias) |
| IaC / CI-CD | **Terraform** como ferramenta única de provisionamento de infraestrutura, reaproveitada nas 3 clouds. **DAB** (Databricks Asset Bundles) usado especificamente para deploy de jobs/pipelines Databricks — aplicável somente na Fase 1 (Azure) |
| Uso do Databricks | Restrito à Azure. Em AWS e GCP, o objetivo é praticar a stack de dados nativa de cada cloud (Glue/Iceberg/Athena na AWS; BigLake/Dataproc/BigQuery no GCP) |
| Portabilidade de motor por camada (v1.2, **revisto na v1.6 para a Fase 2, e na v1.7 para a Fase 3**) | O **modelo de domínio** (13+ entidades, `docs/MODELO_CONCEITUAL_UBER_EATS.md`) e a **mecânica de CDC** (replication slot/log, PK obrigatória, soft delete) são fixos e reaproveitados nas 3 clouds. A v1.2 previa que Oracle e MinIO seriam substituídos por motores nativos de cada cloud nas Fases 2/3 — **decisão revista no `/define` da Fase 2/AWS (v1.6) e no `/brainstorm` da Fase 3/GCP (v1.7): os mesmos sistemas self-hosted da Fase 0 (Oracle, MinIO, Postgres, MongoDB, rodando em Docker/ShadowTraffic) são reaproveitados como fonte, com a AWS e a GCP ingerindo deles via rede** (DMS/DataSync na AWS; Datastream/Storage Transfer Service/Debezium Server na GCP), em vez de recriar motores nativos equivalentes. Motivo: manter o dado gerado por `gen-unified` como fonte única entre as 3 clouds ("reaproveitando o dado do projeto pessoal", Seção 1), evitando duplicar geração/seed por cloud. Exige conectividade de rede até os containers locais — na AWS, via EC2 na mesma VPC (`BRAINSTORM_INGESTAO_AWS_FASE2.md`/`DEFINE_INGESTAO_AWS_FASE2.md`); na GCP, via bastion + túnel SSH reverso, sem migrar os containers (`BRAINSTORM_INGESTAO_GCP_FASE3.md`) |
| Ingestão/CDC por fase (v1.4) | Fase 1/Azure: **dois trilhos deliberadamente separados**, não uma ferramenta única — ver subseção "Fase 1 — Arquitetura de Ingestão" abaixo para o desenho completo (real-time via Airbyte OSS/Debezium→Event Hub; batch via Airbyte→ADLS Gen2 só para o Synapse). Fases 2/3: ingestão nativa da cloud (AWS DMS; GCP Datastream) em vez de Airbyte/Debezium — **sob avaliação**, decisão de alto nível tomada em brainstorm (`/intake`), detalhamento e pendências identificadas ficam para o `/define` de cada fase (ver notas "🔶 Em avaliação" nas seções de Fase 2 e Fase 3). Para não reescrever a Silver a cada fase, a Bronze deve expor um **contrato canônico de metadados de CDC** (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) — cada ferramenta de ingestão emite um formato próprio (`_ab_cdc_*` no Airbyte, `op`/`before`/`after` no Debezium, metadados próprios no DMS/Datastream) e a Silver nunca deve ler o formato nativo diretamente. **Pendência transversal:** o mapeamento de metadados de ordenação (LSN/SCN do Debezium vs. metadados do DMS vs. do Datastream) para o campo canônico `cdc_sequence` ainda não foi desenhado — fica para o `/define` de cada fase 2/3 |
| Gestão de custo | Responsabilidade do usuário — priorizar sempre serviços serverless/on-demand (Redshift Serverless, Synapse Serverless SQL Pool, BigQuery on-demand, Databricks com auto-termination agressivo) para evitar cobrança de recurso ligado sem uso |

---

## 3. Fases

### Fase 0 — Fundação (local, bloqueante)

| Item | Descrição | Status |
|---|---|---|
| Shadow Traffic — integridade referencial (Onda 1) | Corrigir integridade referencial entre os geradores simulados (MySQL, MongoDB, Kafka dentro do MinIO), garantindo que entidades-filho referenciem corretamente chaves de entidades-pai já existentes | ✅ Concluído — `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/` |
| Unificação de identidade Postgres×MinIO (Onda 2) | Migrar Usuário/Motorista para fonte única (Postgres real), PK sequencial em vez de UUID, reconciliar dimensão única de motorista | ✅ Concluído — `.claude/sdd/archive/UNIFICACAO_IDENTIDADE_POSTGRES_MINIO/` |
| Modelo conceitual | Desenhar entidades e relacionamentos do domínio Uber Eats (usuário, restaurante, produto, pedido, item de pedido, pagamento, entrega, avaliação, motorista, estoque, turno, incidente, recibo) — modelo único, reaproveitado nas 3 arquiteturas e nas 3 clouds | ✅ Concluído — `docs/MODELO_CONCEITUAL_UBER_EATS.md` |
| Diversificação de fontes (Onda 3) | Sair de 2 sistemas (Postgres real + MinIO simulado) para 4 sistemas heterogêneos, com CDC real e mutação de estado — ver subseção "Fase 0 — Onda 3" abaixo | ✅ Brainstorm concluído — `.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`; falta `/define` |
| Agentes | Carregar com conhecimento de arquitetura de dados (Warehouse, Lakehouse, Kappa, medalhão, modelagem dimensional). Conhecimento específico de cada cloud entra sob demanda, a partir da fase correspondente | Contínuo |

**Critério de saída (revisado na v1.1):** consulta de join entre as fontes de dados — hoje 2 sistemas (Postgres, MinIO), alvo de 4 (Postgres, Oracle, MongoDB, MinIO) após a Onda 3 — retorna resultado consistente, sem registros órfãos; e a mutação de estado (UPDATE/DELETE) em Postgres/Oracle é capturada corretamente pelo CDC (Airbyte para Postgres, Debezium/Kafka Connect para Oracle).

---

#### Fase 0 — Onda 3: Diversificação de fontes (brainstorm concluído)

> Brainstorm conduzido via `/intake` (múltiplas rodadas com `@medallion-architect` e `@databricks-data-engineer`) e formalizado via `/brainstorm`. Documento completo: [`BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`](../.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md). Próximo passo: `/define`.

**Objetivo:** sair de 2 sistemas (Postgres real + MinIO simulado) para 4, cada um hospedando um domínio de negócio coerente, com CDC real e mutação de estado (`UPDATE`/`DELETE`, não só `INSERT`).

**Alocação final:**

| Sistema | Entidades | CDC |
|---|---|---|
| **Postgres** | Usuário, Motorista (mutável: `drivers.status` etc.) | Airbyte OSS (mantém) |
| **Oracle** (novo) | Restaurante, Produto, Estoque, **Pedido, Item de Pedido, Pagamento, Recibo** (mutáveis: `orders.status`, `payments.status`) | Debezium/Kafka Connect (novo — conector Oracle CDC do Airbyte é pago/Enterprise) |
| **MongoDB** (novo) | Satélite "Perfil de Restaurante" (menu + horários) — cadastro estático, FK para `restaurant_id` | Não aplicável (sem CDC; sem sink de escrita no ShadowTraffic) |
| **MinIO** (mantém) | Entrega, Avaliação, Turno, Incidente + streams fora do core | Airbyte OSS (mantém) |

**Decisão-chave tomada durante o `/brainstorm`:** Pedido e Pagamento migram para o Oracle (não ficam no MinIO como cogitado inicialmente) porque o usuário decidiu **aposentar os logs append-only `kafka/status`/`kafka/events`** — a mudança de status passa a ser a mutação real da linha, capturada pelo CDC. Descartado de vez: um segundo MinIO/datalake.

**Sequenciamento (mitigação de risco, mesmo método das Ondas 1/2):** 1) provar o mecanismo `fork`+`stateMachine` no Postgres (Motorista) — infra já madura; 2) levantar o Oracle com Restaurante/Produto/Estoque, insert-only, validar CDC básico; 3) só então aplicar mutação real a Pedido/Pagamento no Oracle e aposentar os logs antigos. Detalhe completo no BRAINSTORM.

**Escopo por fase (v1.2):** a topologia de 4 sistemas e a ingestão via Airbyte+Debezium são específicas da Fase 0/1 (Azure). Nas Fases 2/3, Oracle e MinIO são substituídos pelos motores nativos de cada cloud — ver Seção 2 ("Portabilidade de motor por camada").

---

### Fase 1 — Azure (3 arquiteturas completas)

| Ordem | Arquitetura | Ferramenta principal | Observação |
|---|---|---|---|
| 1ª | Warehouse | Synapse (**Dedicated SQL Pool**, v1.4 — não Serverless, não Fabric) | Modelagem dimensional (schema estrela + SCD tipo 2) — foco principal de aprendizado da fase. Serverless SQL Pool não suporta DML/`MERGE` (não é possível fazer SCD2 nele); Fabric foi avaliado e descartado — critério é "o que o mercado pede em vaga hoje", não "o que a Microsoft direciona agora" |
| 2ª | Lakehouse | Databricks (reaproveitado do projeto já existente, **Free Edition**) + ADLS Gen2 | Silver/Gold e Unity Catalog mantidos como já implementados; a **ingestão da Bronze é revisada na v1.8** — consolidada via external table sobre o ADLS Gen2 (ver "Fase 1 — Arquitetura de Ingestão"), substituindo o `read_kafka()`/Redpanda do Oracle e o sync direto Airbyte→Databricks do Postgres usados hoje na Fase 0. Free Edition: workspace hospedado fora da subscription Azure (Terraform não o provisiona); DAB **confirmado funcionando** via Service Principal ou PAT |
| 3ª | Kappa | Event Hubs + Stream Analytics (ou Spark Structured Streaming) | Streaming em ambiente já conhecido, reduzindo o risco de aprender conceito novo (Kappa) e cloud nova ao mesmo tempo |

**IaC/CI-CD:** Terraform (ADLS Gen2, Synapse, Event Hubs — **não** o workspace Databricks Free Edition, que fica fora da subscription) + DAB (jobs/pipelines do Lakehouse, validado no Free Edition) + pipeline CI/CD (ex: GitHub Actions). Padrão estabelecido nesta fase, reaproveitado nas seguintes.

---

#### Fase 1 — Arquitetura de Ingestão (Azure, revisada — v1.9)

> ✅ **Brainstorm (v1.8) + Design (v1.9) concluídos** — `.claude/sdd/features/BRAINSTORM_INGESTAO_AZURE_FASE1.md` e `DESIGN_INGESTAO_AZURE_FASE1.md`. O brainstorm fechou a lacuna de artefato que a Fase 1 tinha (era a única fase sem um `BRAINSTORM_INGESTAO_*` dedicado) e revisou dois pontos da decisão original v1.4 (MinIO no trilho batch; Bronze do Lakehouse consolidada via ADLS). O `/design` foi além do que o brainstorm/define previam: descobriu que **Postgres e Oracle não precisam de 2 capturas por fonte** — o Kafka Connect já resolve isso nativamente (ver nota "Captura única" abaixo).

**Captura única por fonte relacional — achado do `/design` (v1.9):** diferente do que a v1.8 registrava (Postgres com 2 replication slots simultâneos; Oracle com 1 captura e 2 sinks configurados no mesmo conector Debezium), o desenho final usa **1 única captura CDC por fonte** (Postgres via Airbyte→Event Hub; Oracle via Debezium/Kafka Connect→Event Hub). O trilho batch (ADLS) é alimentado por um **Kafka Connect Sink Connector** (HDFS 2 Sink Connector, compatível com `abfss://`) que **consome o mesmo tópico do Event Hub** que o Stream Analytics também consome — não uma 2ª captura independente. Isso **elimina** (não apenas mitiga por sequenciamento, como nas Fases 2/AWS e 3/GCP) o risco de concorrência de replication slot/LogMiner. MinIO e MongoDB não entram nessa consolidação — a notificação de bucket do MinIO carrega só metadados do evento (não o conteúdo do objeto), então o Airbyte continua fazendo a cópia real do objeto pro ADLS; o MongoDB nunca esteve no trilho real-time.

**Dois trilhos continuam logicamente separados (Stream Analytics nunca lê o ADLS), mas agora compartilham a mesma captura de origem para Postgres/Oracle:**

| Trilho | Fonte | Ferramenta | Destino | Motivo |
|---|---|---|---|---|
| Real-time (Kappa) | Postgres | Airbyte OSS (CDC, replication slot) | Event Hub | Única captura desta fonte (v1.9) — escreve direto no endpoint Kafka-compatível do Event Hub via destino nativo "Kafka" do Airbyte (SASL_SSL) |
| Real-time (Kappa) | Oracle | Debezium/Kafka Connect (LogMiner) | Event Hub | Única captura desta fonte (v1.9) — mesmo mecanismo já validado localmente na Fase 0 (Redpanda), troca só `bootstrap.servers`/auth pro Event Hub |
| Real-time (Kappa) | MinIO | Notificação de bucket nativa do MinIO (destino Kafka) | Event Hub | MinIO publica evento de objeto (create/delete) direto num tópico Kafka — sem ferramenta de ingestão adicional |
| Batch (Warehouse + Lakehouse) | Postgres | Kafka Connect Sink (HDFS 2, `abfss://`), consumindo o **mesmo tópico** da captura real-time | ADLS Gen2 | v1.9: substitui a 2ª conexão Airbyte/2º replication slot da v1.8 — mesma captura, 2º consumidor |
| Batch (Warehouse + Lakehouse) | Oracle | Mesmo Sink Connector acima, consumindo o **mesmo tópico** da captura real-time | ADLS Gen2 | v1.9: substitui o "2º sink dedicado no conector Debezium" da v1.8 — agora é um conector Kafka Connect separado (sink), não uma 2ª saída do mesmo conector |
| Batch (Warehouse + Lakehouse) | MongoDB | Airbyte, snapshot/full-refresh, path particionado por data | ADLS Gen2 | Fonte estática (~500 documentos) — CDC seria decorativo. Path particionado (não overwrite-in-place) viabiliza o reference data input do Stream Analytics (Etapa 4) |
| Batch (Warehouse + Lakehouse) | MinIO | Airbyte | ADLS Gen2 | v1.8: **novo** — MinIO passa a alimentar também o trilho batch, para que o Lakehouse tenha todas as fontes consolidadas no mesmo ADLS/Bronze |

**Consumidores (v1.8, revisado):**
- **Databricks (Lakehouse):** **external tables** sobre o ADLS Gen2/Bronze (Unity Catalog, storage credential/Azure AD), aplicando `APPLY CHANGES`/merge por `cdc_sequence` em lote a partir dos metadados de CDC do arquivo. Decisão explícita do usuário — substitui o `read_kafka()` já funcional do Oracle (trocaria só o broker pro Event Hub) e o sync direto Airbyte→Databricks já funcional do Postgres, priorizando um único padrão de ingestão para o Lakehouse em vez de manter 3 mecanismos distintos por fonte; substitui também a Lakehouse Federation usada hoje para o MongoDB por ingestão real (Airbyte).
- **Synapse Dedicated (Warehouse):** `COPY INTO` a partir do ADLS Gen2, seguido de `MERGE` para SCD2, aplicando o contrato canônico de CDC.
- **Stream Analytics (Kappa):** lê o stream principal **só** do Event Hub (trilho real-time) — decisão original mantida (v1.8 reafirma): deliberadamente não lê o ADLS Gen2 do trilho batch para eventos, para não descaracterizar o Kappa como um Lambda architecture disfarçado. Enriquece Pedido/Restaurante via **reference data input** (recurso nativo do Stream Analytics), fazendo join contra a cópia do MongoDB já pousada no ADLS Gen2/Bronze pelo trilho batch — mesmo papel do lookup no S3/Bronze (Lambda, AWS) e na tabela Iceberg (Dataflow, GCP), aqui sem cache/TTL manual.

**Achado técnico (v1.8):** Airbyte e Debezium/Kafka Connect conseguem escrever direto no Event Hub via seu endpoint compatível com protocolo Kafka, sem componente-ponte — mesmo padrão documentado pela Microsoft ("Kafka Connect para Event Hubs"). Restrição real: os tópicos internos do Kafka Connect (`connect-offsets`/`connect-configs`/`connect-status`) exigem tópicos compactados, suportados só a partir do tier **Standard** do Event Hubs Namespace (não Basic). O Stream Analytics tem suporte nativo a **reference data input** (join de um stream contra um dataset lento/estático em Blob/ADLS, com path pattern de atualização) — resolve o enriquecimento de Pedido/Restaurante com o MongoDB sem precisar do cache com TTL (Lambda, AWS) nem do side input (Dataflow, GCP) usados nas outras fases.

**Decisão explicitamente avaliada e descartada:** manter os 3 mecanismos de ingestão do Lakehouse como já existem na Fase 0 (Oracle via `read_kafka()`, Postgres via sync direto Airbyte→Databricks, MinIO/MongoDB via Auto Loader/Federation), só trocando storage/broker — mais rápido de implementar, mas o usuário preferiu consolidar num único padrão (external table sobre ADLS). Também avaliado e descartado: Event Hub ler também do ADLS Gen2 (trilho batch) além do MinIO direto — manteria a decisão original de o Kappa nunca ler do trilho batch, evitando repetir o erro já descartado na v1.4 (unificar tudo num trilho único faria o Kappa não ser Kappa de fato).

---

### Fase 2 — AWS (3 arquiteturas, stack 100% nativa)

> ✅ **Brainstorm de ingestão concluído (v1.5)** — `.claude/sdd/features/BRAINSTORM_INGESTAO_AWS_FASE2.md`. A escolha de ferramenta por arquitetura abaixo está fechada; o desenho fino de ingestão também já foi decidido nesta rodada (equivalente à subseção "Fase 1 — Arquitetura de Ingestão"), faltando só o `/define` desta fase para detalhar implementação.

**Fase 2 — Arquitetura de Ingestão (dois trilhos, mesmo princípio da Fase 1):**

| Trilho | Fonte | Ferramenta | Destino | Motivo |
|---|---|---|---|---|
| Real-time (Kappa) | Postgres | AWS DMS, ongoing replication/CDC (task dedicada) | Kinesis Data Streams | Kinesis como target nativo do DMS — sem passar pelo S3, para o Kappa não virar micro-lote disfarçado |
| Real-time (Kappa) | Oracle | AWS DMS, ongoing replication/CDC (task dedicada) | Kinesis Data Streams | Mesmo motivo do Postgres |
| Real-time (Kappa) | MinIO | Notificação de bucket nativa (destino Webhook) → Lambda ponte (`PutRecord`) | Kinesis Data Streams | Kinesis não fala protocolo Kafka; MSK foi cogitado e descartado por não ser serverless (brokers sempre ligados) |
| Batch (Warehouse + Lakehouse) | Postgres | AWS DMS, 2ª task, ongoing replication/CDC | S3 (Bronze) | Mesmo padrão da Fase 1 (2ª conexão dedicada ao trilho batch) |
| Batch (Warehouse + Lakehouse) | Oracle | AWS DMS, 2ª task, ongoing replication/CDC | S3 (Bronze) | Idem |
| Batch (Warehouse + Lakehouse) | MongoDB | AWS DMS, task única, full load/snapshot (sem CDC) | S3 (Bronze) | Fonte estática por decisão já fechada na Onda 3 — CDC seria decorativo |
| Batch (Warehouse + Lakehouse) | MinIO | AWS DataSync, location "Self-managed object storage", sync agendado | S3 (Bronze) | DMS não tem conector para object storage genérico — MinIO não é um motor de banco de dados |

**Consumidores:** Redshift Serverless faz `COPY`/`MERGE` a partir do S3 (Bronze) — sem target DMS nativo direto no Redshift; Glue+Iceberg+Athena leem o mesmo S3; Kinesis (modo on-demand) é o único destino do trilho real-time, consumido pelo Kappa (Flink ou Lambda, decisão pendente do `/define`) — o consumidor faz **lookup/enriquecimento contra a cópia do MongoDB no S3/Bronze** (menu/horário do restaurante) sem que o MongoDB entre pelo Kinesis.

**Decisão explicitamente avaliada e descartada:** usar o S3 como fronteira única também para o trilho real-time (DMS/DataSync → S3 → evento `ObjectCreated` → Lambda → Kinesis). Mais barato (uma só leitura de log por fonte), mas o Kappa herdaria o intervalo de entrega do DMS/DataSync ao S3 antes de disparar o evento — o usuário priorizou fidelidade ao Kappa "de verdade" sobre essa economia, mesmo padrão de decisão já tomado na Fase 1.

| Ordem | Arquitetura | Ferramenta principal |
|---|---|---|
| 1ª | Warehouse | Redshift Serverless |
| 2ª | Lakehouse | Glue + Iceberg + Athena |
| 3ª | Kappa | Kinesis Data Streams (on-demand) + Flink/Lambda |

**Fontes e ingestão (v1.2):** Oracle e MinIO da Fase 0 são substituídos pelos papéis equivalentes em serviços nativos AWS (banco relacional gerenciado + S3 — motor exato a decidir no `/define` da fase). Ingestão/CDC via **AWS DMS** (Postgres, Oracle, MongoDB) e **AWS DataSync** (MinIO) — não via Airbyte/Debezium/MSK.

**IaC/CI-CD:** Terraform (sem DAB — não há Databricks nesta fase).

---

### Fase 3 — GCP (3 arquiteturas, stack 100% nativa)

> ✅ **Brainstorm de ingestão concluído (v1.7)** — `.claude/sdd/features/BRAINSTORM_INGESTAO_GCP_FASE3.md`. A escolha de ferramenta por arquitetura abaixo está fechada; o desenho fino de ingestão também já foi decidido nesta rodada (equivalente às subseções "Fase 1"/"Fase 2 — Arquitetura de Ingestão"), faltando só o `/define` desta fase para detalhar implementação.

**Fase 3 — Arquitetura de Ingestão (dois trilhos, mesmo princípio das Fases 1 e 2):**

| Trilho | Fonte | Ferramenta | Destino | Motivo |
|---|---|---|---|---|
| Real-time (Kappa) | Postgres | Debezium Server (logical decoding) | Pub/Sub | Datastream **não tem Pub/Sub como destino** nativo (só BigQuery, Cloud Storage e BigLake Iceberg) — Debezium Server tem sink documentado para Pub/Sub; única exceção deliberada à regra "só ferramenta nativa da cloud" nesta fase |
| Real-time (Kappa) | Oracle | Debezium Server (LogMiner, já validado na Onda 3) | Pub/Sub | Mesmo motivo do Postgres |
| Real-time (Kappa) | MinIO | Notificação de bucket nativa (destino Webhook) → Cloud Function ponte | Pub/Sub | Mesmo papel da Lambda ponte da Fase 2/AWS — MinIO chama a URL pública da function, sem expor porta própria |
| Batch (Warehouse + Lakehouse) | Postgres | Datastream, CDC (via bastion GCE + túnel SSH reverso) | GCS (Bronze) → BigLake Iceberg tables | Datastream cobre as 3 fontes relacionais/documentais num único serviço; destino direto em Iceberg elimina o hop manual GCS→Dataproc que a v1.2/1.3 assumia |
| Batch (Warehouse + Lakehouse) | Oracle | Datastream, CDC via LogMiner (via túnel) | GCS (Bronze) → BigLake Iceberg tables | Idem |
| Batch (Warehouse + Lakehouse) | MongoDB | Datastream, full load/snapshot (sem CDC — fonte estática) | GCS (Bronze) → BigLake Iceberg tables | GA desde set/2025 (confirmado em `docs/adversarial/architectural-reply.md`) |
| Batch (Warehouse + Lakehouse) | MinIO | Storage Transfer Service, fonte "S3-compatible" via agente local (outbound) | GCS (Bronze) | Datastream não tem conector para object storage genérico — MinIO não é um motor de banco de dados; equivalente direto ao AWS DataSync |

**Conectividade (achado desta fase):** Datastream é *pull-based* — exige túnel SSH reverso (bastion GCE público + `autossh`) partindo da máquina local, já que a Fase 0 permanece rodando localmente (decisão explícita: não migrar para uma VM na nuvem, ao contrário da EC2 da Fase 2/AWS). Já o Debezium Server e a Cloud Function ponte são *push-based* — conectam para fora, sem precisar de túnel nem porta exposta.

**Consumidores:** **BigQuery** faz `LOAD`/`MERGE` físico a partir dos mesmos arquivos brutos do GCS/Bronze para o seu storage nativo — decisão explícita do usuário por performance e por paridade de método com Redshift (AWS) e Synapse (Azure); consulta em tempo de execução via BigLake (query-in-place) foi avaliada e descartada. **Dataplex Universal Catalog** cataloga/governa as tabelas Iceberg do BigLake sobre o mesmo GCS/Bronze — papel equivalente ao Unity Catalog (Azure/Databricks) e ao Glue Catalog (AWS). **Dataproc** processa/consulta essas mesmas tabelas Iceberg (Lakehouse), sem ingestão adicional. **Dataflow** é o consumidor do Kappa — lê só do Pub/Sub, enriquecendo Pedido/Restaurante com lookup na cópia do MongoDB já pousada como tabela Iceberg pelo trilho batch.

**Decisão explicitamente avaliada e descartada:** BigQuery consultando as tabelas Iceberg do BigLake em tempo de execução, sem carga física própria. É um contraste arquitetural genuíno (o BigQuery moderno dissolve a fronteira Warehouse/Lakehouse), mas o usuário priorizou performance e método igual/similar nas 3 nuvens para permitir comparação justa na Fase 4 — consulta ad-hoc direta ao dado bruto fica reservada a engenheiro/analista, não ao consumo de cliente.

| Ordem | Arquitetura | Ferramenta principal |
|---|---|---|
| 1ª | Warehouse | BigQuery |
| 2ª | Lakehouse | BigLake/Dataproc + Iceberg |
| 3ª | Kappa | Pub/Sub + Dataflow |

**Fontes e ingestão (v1.7, revisado):** mesma decisão já tomada na Fase 2/AWS (v1.6) — os sistemas self-hosted da Fase 0 (Oracle, MinIO, Postgres, MongoDB em Docker/ShadowTraffic) são reaproveitados como fonte via ingestão de rede (Datastream/Storage Transfer Service/Debezium Server), em vez de recriar motores nativos GCP equivalentes. Ingestão/CDC via **Datastream** (Postgres, Oracle, MongoDB — trilho batch), **Debezium Server** (Postgres, Oracle — trilho real-time, exceção à regra de ferramenta nativa) e **Storage Transfer Service** (MinIO).

**IaC/CI-CD:** Terraform (sem DAB).

---

### Fase 4 — Consolidação

- README comparativo entre as 9 combinações arquitetura × cloud, com custo, latência e complexidade medidos na prática (não copiados de terceiros)
- Documentação das decisões técnicas tomadas e dos problemas reais enfrentados em cada fase
- Destaque específico para o contraste "Lakehouse via Databricks (Azure)" vs. "Lakehouse nativo (Glue/Iceberg na AWS, BigLake/Dataproc no GCP)" — mesmo padrão arquitetural implementado de formas diferentes
- Repositório organizado por cloud/arquitetura, pronto para apresentação em processo seletivo

---

## 4. Estimativa de norte temporal

| Fase | Sessões (~3h) estimadas | Tempo corrido aproximado |
|---|---|---|
| 0 — Fundação (Ondas 1-2, concluídas) | ~4-6 | 1 a 1,5 mês |
| 0 — Onda 3 (diversificação de fontes, planejada) | ~4-6 adicionais | ~1 a 1,5 mês adicional |
| 1 — Azure (3 arquiteturas) | ~8-10 | ~2 a 2,5 meses |
| 2 — AWS (3 arquiteturas) | ~14-16 | ~3,5 a 4 meses |
| 3 — GCP (3 arquiteturas) | ~10-12 | ~2,5 a 3 meses |
| 4 — Consolidação | ~3-4 | ~1 mês |
| **Total** | **~44-54** | **~11,5 a 14,5 meses** |

*Estimativas servem como referência de planejamento; ajustes ao longo do caminho são esperados e não invalidam o roadmap. A Fase 0 já ultrapassou o orçamento original de 4-6 sessões (Ondas 1+2 o consumiram) — a Onda 3 é um orçamento adicional explícito, não uma correção de estimativa.*

---

## 5. Lacunas de conhecimento endereçadas por fase

| Fase | Lacuna principal atacada |
|---|---|
| 0 (Ondas 1-2) | Modelagem relacional |
| 0 (Onda 3) | CDC real multi-motor (Airbyte + Debezium/Kafka Connect), Oracle como fonte, modelagem documental (MongoDB), geração sintética de mutação de estado (ShadowTraffic `fork`/`stateMachine`) |
| 1 (Warehouse) | Modelagem dimensional |
| 1 (Kappa) | Streaming/Kafka (em ambiente já conhecido) |
| 2 | AWS como cloud (maior lacuna declarada); CDC gerenciado (AWS DMS, MSK Connect) |
| 3 | GCP como cloud; streaming em ambiente novo (Pub/Sub + Dataflow); CDC gerenciado (Datastream) |
| DevOps/DataOps | Terraform + CI/CD, presente desde a Fase 1 |

---

## Histórico de revisões

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | Agosto/2026 | Documento inicial (`docs/plan.md`) |
| 1.1 | Setembro/2026 | Renomeado para `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`. Fase 0 detalhada com status real (Ondas 1-2 concluídas) e nova subseção "Onda 3 — Diversificação de fontes" capturando o brainstorm de expansão para Postgres+Oracle+MongoDB+MinIO com CDC real. Estimativa de norte temporal e lacunas de conhecimento atualizadas de acordo |
| 1.2 | Setembro/2026 | Esclarecido que a topologia de 4 sistemas e Airbyte+Debezium são específicos da Fase 0/1 (Azure). Novos princípios "Portabilidade de motor por camada" e "Ingestão/CDC por fase": nas Fases 2/3, Oracle e MinIO são substituídos pelos motores relacionais e object storage nativos de cada cloud, e a ingestão passa a ser nativa (AWS DMS/MSK Connect; GCP Datastream) em vez de Airbyte/Debezium. Adicionado requisito de contrato canônico de metadados de CDC na Bronze, para a Silver não depender do formato específico de cada ferramenta de ingestão |
| 1.3 | Setembro/2026 | Brainstorm da Onda 3 formalizado (`/brainstorm` → `.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`). Alocação final: Pedido, Pagamento, Item de Pedido e Recibo migram para o Oracle (não ficam no MinIO como cogitado inicialmente), porque os logs append-only `kafka/status`/`kafka/events` são aposentados em favor de mutação real capturada por CDC. Segundo MinIO descartado definitivamente. Adicionado sequenciamento em 3 etapas (Postgres/Motorista → Oracle plumbing → Oracle/Pedido+Pagamento) para isolar o risco do mecanismo de mutação, nunca testado neste projeto |
| 1.4 | Setembro/2026 | Rodada de revisão adversarial da Fase 1/Azure fechada (log em `adversarial-reply.md`). Decisões: Synapse **Dedicated SQL Pool** (não Serverless — não suporta DML/MERGE/SCD2; não Fabric — critério de mercado). Databricks **Free Edition** confirmado (Terraform não provisiona o workspace; DAB validado via Service Principal/PAT). Nova subseção "Fase 1 — Arquitetura de Ingestão": dois trilhos deliberados — real-time (Airbyte OSS CDC/Postgres + Debezium-LogMiner/Oracle + notificação Kafka nativa/MinIO, tudo via Event Hub, alimentando Databricks Structured Streaming e Stream Analytics) e batch (Airbyte modo Standard/snapshot → ADLS Gen2 CSV, só para o Synapse). Decisão explícita de **não** unificar tudo num trilho batch único, para preservar a lacuna de conhecimento da Onda 3 (CDC real multi-motor) e a legitimidade do Kappa. Fases 2 (AWS) e 3 (GCP) marcadas como **🔶 sob avaliação**, com achados preliminares registrados (DMS unifica Postgres/Oracle/Mongo→Redshift/S3/Kinesis, mas Kinesis não fala protocolo Kafka; Datastream unifica Postgres/Oracle/Mongo→BigQuery/BigLake Iceberg diretamente, mas não alcança Pub/Sub) — desenho fino de ingestão de cada fase permanece pendente do respectivo `/define` |
| 1.5 | Setembro/2026 | Brainstorm de ingestão da Fase 2/AWS formalizado (`/brainstorm` → `.claude/sdd/features/BRAINSTORM_INGESTAO_AWS_FASE2.md`), fechando a pendência "🔶 sob avaliação" da v1.4. Decisões: dois trilhos separados (mesmo princípio da Fase 1) — real-time via **DMS ongoing replication → Kinesis Data Streams nativo** (Postgres/Oracle) e **notificação de bucket do MinIO (Webhook) → Lambda ponte → Kinesis**; batch via **DMS → S3** (2ª task para Postgres/Oracle, task única full load para MongoDB estático) e **AWS DataSync** (MinIO, via location "Self-managed object storage" — DMS não tem conector para object storage genérico). Redshift e Glue/Athena passam a ler só do S3 (sem target DMS nativo direto no Redshift), mesmo padrão `COPY INTO` da Fase 1. **MSK descartado explicitamente** por não ser serverless (contraria o princípio de custo da Seção 2). MongoDB (estático) não entra pelo Kinesis, mas **é consumido pelo Kappa via lookup/enriquecimento** do consumidor (Flink/Lambda) contra a cópia já aterrissada no S3/Bronze — sem 2ª cópia nem caminho de ingestão dedicado |
| 1.6 | Setembro/2026 | `/define` da Fase 2/AWS resolveu uma ambiguidade entre o brainstorm (v1.5) e o princípio "Portabilidade de motor por camada" (v1.2): decidido que a Fase 2 **reaproveita os mesmos sistemas self-hosted da Fase 0** (Oracle, MinIO, Postgres, MongoDB em Docker/ShadowTraffic) como fonte via ingestão de rede (DMS/DataSync), em vez de substituí-los por motores nativos AWS (RDS/S3 direto) como a v1.2 previa originalmente. Princípio da Seção 2 atualizado para refletir essa decisão, explicitamente escopada à Fase 2 — a Fase 3 (GCP) mantém a redação original da v1.2 até seu próprio `/define`. Nova exigência registrada: conectividade de rede da AWS até os containers locais (VPN/IP público/túnel) |
| 1.7 | Setembro/2026 | Brainstorm de ingestão da Fase 3/GCP formalizado (`/brainstorm` → `.claude/sdd/features/BRAINSTORM_INGESTAO_GCP_FASE3.md`), fechando a pendência "🔶 sob avaliação" da v1.4. Decisões: dois trilhos separados (mesmo princípio das Fases 1/2) — real-time via **Debezium Server → Pub/Sub direto** (Postgres/Oracle; Datastream não tem Pub/Sub como destino nativo) e **notificação de bucket do MinIO (Webhook) → Cloud Function ponte → Pub/Sub**; batch via **Datastream → GCS/Bronze → BigLake Iceberg tables** (Postgres/Oracle CDC; MongoDB full load/snapshot) e **Storage Transfer Service** (MinIO, fonte "S3-compatible" via agente local). Conectividade do Datastream (pull-based) resolvida via bastion GCE + túnel SSH reverso, mantendo a Fase 0 local — ao contrário da AWS, que migrou para EC2 na mesma VPC; Debezium Server e a Cloud Function ponte são push-based e não precisam de túnel. Dataplex Universal Catalog fecha o papel de catalogação equivalente ao Unity Catalog/Glue. **Decisão explícita do usuário:** BigQuery sempre faz carga física (`LOAD`/`MERGE`) a partir do GCS/Bronze para seu storage nativo — consulta em tempo de execução via BigLake (query-in-place) foi avaliada e descartada, por performance e por paridade de método com Redshift/Synapse na comparação da Fase 4. Princípio "Portabilidade de motor por camada" (Seção 2) estendido para também cobrir a Fase 3 |
| 1.8 | Setembro/2026 | Brainstorm de ingestão da Fase 1/Azure formalizado (`/brainstorm` → `.claude/sdd/features/BRAINSTORM_INGESTAO_AZURE_FASE1.md`), fechando a lacuna de artefato que a Fase 1 tinha (única fase sem `BRAINSTORM_INGESTAO_*` dedicado — a v1.4 vinha só de rodadas de `/intake`/revisão adversarial). Revisa dois pontos da decisão v1.4: (1) **MinIO passa a alimentar também o trilho batch** (Airbyte → ADLS Gen2), não só o real-time; (2) a **Bronze do Lakehouse é consolidada via external table sobre o ADLS Gen2** (Unity Catalog), com o lote batch de Postgres/Oracle carregando eventos de CDC (Airbyte modo CDC/replication slot; Debezium com sink dedicado de arquivo preservando `op`/`before`/`after`/SCN) para não perder o histórico de mutação da Onda 3 — decisão explícita do usuário, que descarta o `read_kafka()`/Redpanda do Oracle e o sync direto Airbyte→Databricks do Postgres já funcionais na Fase 0, e substitui a Lakehouse Federation do MongoDB por ingestão real via Airbyte. Mantidas: Stream Analytics lê só o Event Hub para eventos (nunca o ADLS batch); Postgres/Oracle no real-time continuam via Airbyte CDC/Debezium-LogMiner → Event Hub. **Nova decisão (mesma sessão):** o MongoDB enriquece o Kappa via **reference data input** do Stream Analytics, fazendo join contra a cópia já pousada no ADLS Gen2/Bronze pelo trilho batch — mesma lógica de enriquecimento já usada na AWS (lookup no S3/Bronze via Lambda) e na GCP (lookup na tabela Iceberg via Dataflow), aqui resolvida por um recurso nativo do Stream Analytics, sem cache/TTL manual. **Achado técnico:** Event Hubs expõe endpoint compatível com protocolo Kafka — Airbyte (destino nativo "Kafka") e Kafka Connect/Debezium escrevem direto nele sem componente-ponte, mas o Kafka Connect exige tier **Standard** do Event Hubs Namespace (tópicos internos compactados não suportados no Basic) |
| 1.9 | Setembro/2026 | `/define` (`DEFINE_INGESTAO_AZURE_FASE1.md`) e `/design` (`DESIGN_INGESTAO_AZURE_FASE1.md`) concluídos. O `/design` descobriu uma simplificação real sobre a v1.8: Postgres e Oracle não precisam de 2 capturas por fonte — o trilho batch (ADLS) passa a ser alimentado por um **Kafka Connect Sink Connector** (HDFS 2, `abfss://`) que **consome o mesmo tópico do Event Hub** que a captura real-time já publica, em vez de uma 2ª conexão Airbyte (Postgres) ou um 2º sink no mesmo conector Debezium (Oracle). Isso **elimina** o risco de concorrência de replication slot/LogMiner que as Fases 2/AWS e 3/GCP só conseguiram mitigar por sequenciamento — não existe mais essa janela de risco na Fase 1. Outras decisões de Design: storage credential do Unity Catalog via **Service Principal** (não managed identity — Free Edition fica fora da subscription); Bronze do Databricks via **Auto Loader (`read_files`)** em pipeline **Triggered** (não uma "external table" estática, termo do brainstorm) — reaproveita a sintaxe `APPLY CHANGES INTO`/`SEQUENCE BY cdc_sequence` já validada na Onda 3, só trocando a fonte; MinIO usa notificação nativa tipo **Kafka** (não Webhook) direto pro Event Hub, eliminando a função-ponte que AWS e GCP precisaram; MongoDB grava no ADLS em **path particionado por data**, viabilizando o reference data input do Stream Analytics. **Achado favorável adicional:** o mapeamento canônico de CDC (`cdc_operation`/`cdc_commit_ts`/`cdc_sequence`/`cdc_source_system`) não muda nesta fase — Postgres/Oracle reaproveitam o mesmo mapeamento já feito na Onda 3 (Airbyte/Debezium), diferente da AWS (DMS) e da GCP (Datastream/Debezium Server), que precisaram mapear ferramentas novas |
