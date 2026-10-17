---
domain: gcp-bigquery
topic: bulk-load
---

# Pattern: carga em massa do GCS para BigQuery

## Problema

Mover arquivos da zona `raw`/`curated` do lake (`gs://<BUCKET>/...`) para tabelas nativas,
de forma idempotente, barata e sem credencial no código. Equivale ao `COPY INTO` do Synapse.

## Solução

Usar **batch load** (grátis no pool compartilhado): `LOAD DATA` em SQL (orquestrável como
qualquer query) ou `bq load` / job de load via API. Preferir **Parquet/Avro** (schema
embutido, tipos preservados, compressão).

## 1. SQL — `LOAD DATA`

Append numa tabela existente:

```sql
LOAD DATA INTO `<GCP_PROJECT_ID>.raw.orders`
FROM FILES (
  format = 'PARQUET',
  uris   = ['gs://<BUCKET>/raw/orders/dt=2026-10-16/*.parquet']
);
```

Recarga idempotente de uma partição (sobrescreve só a partição):

```sql
LOAD DATA OVERWRITE `<GCP_PROJECT_ID>.raw.orders`
PARTITIONS (dt = DATE '2026-10-16')
PARTITION BY dt
FROM FILES (
  format = 'PARQUET',
  uris   = ['gs://<BUCKET>/raw/orders/dt=2026-10-16/*.parquet']
)
WITH PARTITION COLUMNS (dt DATE);
```

> Sintaxe de `PARTITIONS (...)` + `WITH PARTITION COLUMNS` (layout Hive `dt=...`):
> **a validar** contra a referência `LOAD DATA` antes de usar em produção. Alternativa
> segura: carregar em tabela de staging e fazer `DELETE` da partição + `INSERT` numa transação.

CSV com schema explícito:

```sql
LOAD DATA INTO `<GCP_PROJECT_ID>.raw.clientes` (cliente_id STRING, segmento STRING, dt DATE)
FROM FILES (format = 'CSV', skip_leading_rows = 1,
            uris = ['gs://<BUCKET>/raw/clientes/*.csv']);
```

## 2. CLI — `bq load`

```bash
bq load --source_format=PARQUET \
  --time_partitioning_field=dt --clustering_fields=cliente_id \
  <GCP_PROJECT_ID>:raw.orders "gs://<BUCKET>/raw/orders/dt=2026-10-16/*.parquet"

# substituir a partição do dia (decorador $YYYYMMDD)
bq load --replace --source_format=PARQUET \
  '<GCP_PROJECT_ID>:raw.orders$20261016' "gs://<BUCKET>/raw/orders/dt=2026-10-16/*.parquet"
```

## 3. Identidade e permissão

| Identidade | Papel |
|---|---|
| SA do pipeline (`<SA_EMAIL>`) | `roles/bigquery.jobUser` (projeto) |
| | `roles/bigquery.dataEditor` (dataset `raw`) |
| | `roles/storage.objectViewer` (bucket de origem) |

Orquestrador (Composer/Airflow, Cloud Run job, Workflows) roda **como** essa SA — sem chave.

## 4. Idempotência

- Particione por data de referência e recarregue a partição inteira (`--replace` com
  decorador ou `LOAD DATA OVERWRITE`).
- Nunca `append` cego em reprocessamento — duplica linhas.
- Registre na tabela de controle: `uris`, `job_id`, `output_rows`.

## 5. Verificação

```sql
SELECT dt, COUNT(*) FROM `<GCP_PROJECT_ID>.raw.orders`
WHERE dt = '2026-10-16' GROUP BY dt;
```

```bash
bq show -j <JOB_ID>      # status, outputRows, erros
```

## Limites e armadilhas

- Bucket e dataset em localizações compatíveis (ver `concepts/datasets-and-tables.md`).
- Arquivos muito pequenos (milhares de KB) deixam a carga lenta — compactar no lake.
- Quotas de load jobs por tabela/dia existem — agrupe arquivos por wildcard em vez de um job
  por arquivo.
- Sandbox: `LOAD` funciona, mas tabelas expiram em 60 dias.

## Custo

Batch load: sem cobrança de compute; paga storage resultante. Leitura do GCS na mesma região
sem egress.
