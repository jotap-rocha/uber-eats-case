---
domain: gcp-dataflow
description: Dataflow (Apache Beam) streaming no GCP — jobs e Streaming Engine, templates Google (Kafka/Managed Kafka → BigQuery), side inputs como reference data (slowly-changing a partir do GCS), janelas, custo por vCPU/memória-hora e drain vs cancel
mcp_validated: "2026-10-16"
confidence: 0.7
---

# KB: Dataflow (stream processing GCP)

Paridade com `azure-stream-analytics` (sintaxe de query, reference data input, path pattern).
No GCP a "query" é um **pipeline Apache Beam** (Python/Java/YAML ou template pronto), e o
reference data vira **side input** recarregado do GCS.

## Papel

`role: stream-processing` — processamento contínuo gerenciado: lê do `gcp-managed-kafka`,
enriquece com reference data do `gcp-gcs`, aplica janelas e grava no `gcp-bigquery`.

## Capability map

| Pergunta | Onde achar |
|---|---|
| Job streaming, workers, Streaming Engine, custo, drain/cancel? | [concepts/streaming-jobs-and-cost.md](concepts/streaming-jobs-and-cost.md) |
| Templates Google (classic/flex) e quando usar? | [concepts/templates.md](concepts/templates.md) |
| Janelas, watermark, side inputs? | [concepts/windows-and-side-inputs.md](concepts/windows-and-side-inputs.md) |
| Reference data slowly-changing do GCS | [patterns/reference-data.md](patterns/reference-data.md) |
| Managed Kafka → BigQuery sem código | [patterns/kafka-to-bigquery-template.md](patterns/kafka-to-bigquery-template.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Learning path

1. `## Custo e free tier` abaixo
2. `concepts/streaming-jobs-and-cost.md` → `concepts/templates.md`
3. `patterns/kafka-to-bigquery-template.md` — primeiro job sem escrever código
4. `concepts/windows-and-side-inputs.md` → `patterns/reference-data.md`

## Custo e free tier

- **Sem free tier** próprio do Dataflow. Só o **Free Trial (US$ 300 / 90 dias)** cobre.
  Recursos auxiliares (GCS de staging, BigQuery) usam seus próprios free tiers.
- **Cobrança por segundo** de worker: vCPU-hora + GiB-hora de memória + disco
  (+ Streaming Engine Compute Units ou dados processados no Streaming Engine).
  Referência `us-central1` streaming: ~US$ 0,069/vCPU-h, ~US$ 0,0036/GiB-h,
  ~US$ 0,089/SECU — **a validar** em `cloud.google.com/dataflow/pricing`.
- **Streaming roda 24/7** até ser parado: 1 worker `n1-standard-2` + Streaming Engine fica na
  casa de dezenas a ~US$ 100+/mês (**a validar** com a calculadora). Autoscaling pode subir
  workers sozinho → limitar `--max-workers`/`maxNumWorkers`.
- **Parar:** `gcloud dataflow jobs drain <JOB_ID>` (termina o que está em buffer, continua
  cobrando até acabar) ou `cancel` (para já, pode perder in-flight). Job parado não cobra.
- **Budgets:** budget + alertas 50/90/100% (só alerta, não para o job).
- **Regra:** criar → testar → **drain/cancel** no mesmo dia; conferir
  `gcloud dataflow jobs list --status=active` vazio antes de encerrar.

## SI

- Job roda como **worker service account** dedicada (`--service-account-email=<SA_EMAIL>`),
  não a SA default do Compute. Papéis mínimos: `roles/dataflow.worker`,
  `roles/managedkafka.client` (fonte Kafka), `roles/bigquery.dataEditor` no dataset de
  destino + `roles/bigquery.jobUser`, `objectViewer` no bucket `ref`, `objectUser` no `tmp`.
- Quem lança: `roles/dataflow.developer` + `roles/iam.serviceAccountUser` na SA.
- Workers com IP privado (`--disable-public-ips` / `usePublicIps=false`) na subnet que alcança
  o Kafka.
- Parâmetros de template aparecem no console/logs → **nunca** senha em parâmetro; use
  Secret Manager (templates aceitam referência de secret em alguns parâmetros — **a validar**
  por template).
- Placeholders: `<GCP_PROJECT_ID>`, `<REGION>`, `<BUCKET>`, `<SA_EMAIL>`, `<CLUSTER>`.

## Por que este serviço

| Alternativa (GCP) | Por que não como padrão |
|---|---|
| Dataproc + Spark Structured Streaming | Cluster para operar; sem autoscaling/drain gerenciados equivalentes |
| Managed Kafka Connect BigQuery Sink | Só move dados; sem janelas/enriquecimento/side input |
| BigQuery continuous queries | SQL contínuo sobre BigQuery; fonte Kafka não é nativa — **a validar** se atende |
| Cloud Run / Functions consumindo Kafka | Sem estado, janelas nem exactly-once — ok para lógica trivial |

Dataflow é o equivalente direto do Stream Analytics: gerenciado, autoscaling, janelas e
reference data, com templates prontos para Kafka → BigQuery.
