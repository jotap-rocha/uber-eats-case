---
domain: gcp-bigquery
description: BigQuery como warehouse no GCP — datasets, LOAD DATA/bq load a partir do GCS, MERGE para SCD2, custo on-demand por TiB lido vs editions, free tier/sandbox, guardrails (maximum_bytes_billed, partição/cluster); por que não Dataproc/Spark
mcp_validated: "2026-10-16"
confidence: 0.8
---

# KB: BigQuery (warehouse GCP)

Paridade com `azure-synapse` (Dedicated SQL Pool + COPY INTO + MERGE SCD2). Diferença central:
BigQuery é **serverless** — não há pool para pausar; o custo vem de **bytes lidos** (on-demand)
ou de **slots** (editions) e de storage.

## Papel

`role: warehouse` — camada analítica gerenciada: carga em massa a partir do lake GCS
(`gcp-gcs`), modelagem dimensional com SCD2 via `MERGE`, consultas SQL padrão (GoogleSQL).
Recebe também streaming do `gcp-dataflow` (Storage Write API).

## Capability map

| Pergunta | Onde achar |
|---|---|
| Dataset, região, tabela particionada/clusterizada? | [concepts/datasets-and-tables.md](concepts/datasets-and-tables.md) |
| On-demand vs editions, free tier, sandbox, guardrails? | [concepts/cost-model.md](concepts/cost-model.md) |
| Carga em massa do GCS (`LOAD DATA`, `bq load`) | [patterns/bulk-load.md](patterns/bulk-load.md) |
| SCD2 com `MERGE` | [patterns/merge-scd2.md](patterns/merge-scd2.md) |
| Cheatsheet | [quick-reference.md](quick-reference.md) |

## Learning path

1. `concepts/cost-model.md` — antes de rodar a primeira query
2. `concepts/datasets-and-tables.md` — mesma região do bucket; partição + cluster
3. `patterns/bulk-load.md` — raw/curated a partir do GCS
4. `patterns/merge-scd2.md` — dimensão histórica

## Custo e free tier

- **Free Tier (Always Free, por billing account/mês):** **1 TiB de query** on-demand e
  **10 GiB de storage**. Batch load a partir do GCS **não cobra** (usa pool compartilhado).
- **Sandbox:** sem cartão nem billing; 10 GiB de storage (limite vitalício), 1 TiB/mês de query,
  tabelas/partições expiram em **60 dias**, **sem DML** (logo sem `MERGE`/SCD2) e sem streaming.
  Serve para aprender SQL, não para este pattern.
- **Conta nova:** Free Trial de **US$ 300 / 90 dias** (verificado 2026-10-16).
- **On-demand:** cobra por TiB processado (**~US$ 6,25/TiB** em US — **a validar** na página
  de pricing para a região), mínimo de 10 MB por tabela referenciada.
- **O que queima crédito:** `SELECT *` em tabela grande, query sem filtro de partição,
  ferramentas de BI fazendo refresh contínuo, reservas de editions esquecidas (slot-hora).
- **Limitar:** `maximum_bytes_billed` por query/job, quota custom "Query usage per day"
  por projeto/usuário, `require_partition_filter`, dry-run antes de rodar.
- **Parar/destruir:** não há pausa nem custo ocioso de compute em on-demand; o que fica é
  storage. Labs: `default_table_expiration_ms` no dataset e `bq rm -r -f <dataset>` /
  `terraform destroy` no fim do dia. Reservas de editions: **apagar** (slots cobram ligados).
- **Budgets:** budget com alertas 50/90/100% no billing account (só alerta, não bloqueia).
- **Regra:** criar → testar → destruir no mesmo dia.

## SI

- Identidade: SA do pipeline com `roles/bigquery.jobUser` no **projeto** +
  `roles/bigquery.dataEditor` só nos **datasets** que escreve; leitores com `dataViewer`.
- Para carga do GCS: a mesma SA com `roles/storage.objectViewer` no bucket de origem.
- PII: colunas sensíveis com policy tags (column-level security) ou views mascaradas;
  nunca PII em nomes de tabela/label/log de job.
- Placeholders: `<GCP_PROJECT_ID>`, `<REGION>`, `<BUCKET>`, `<SA_EMAIL>`, `<DATASET>`.

## Por que este serviço

| Alternativa (GCP) | Por que não para este caso |
|---|---|
| Dataproc (Spark/Hive em cluster) | Cluster de VMs para gerir/pagar mesmo ocioso; SCD2 exige Delta/Iceberg/Hudi + código Spark — BigQuery faz `MERGE` nativo em SQL |
| Dataproc Serverless / BigQuery Spark procedures | Útil para transformações não-SQL; para carga + `MERGE` dimensional é custo e complexidade extra |
| Cloud SQL / AlloyDB | OLTP; não escala para varredura analítica colunar |
| BigLake / tabelas externas sobre GCS | Ótimo para leitura do lake; DML/SCD2 em tabela externa é limitado — dimensão fica em tabela nativa |

Paridade com o levantamento Azure: lá "por que não Serverless nem Fabric"; aqui "por que não
Dataproc/Spark" — mesma lógica: SQL gerenciado + MERGE nativo vence cluster para SCD2.
