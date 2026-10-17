---
domain: gcp-bigquery
topic: quick-reference
---

# BigQuery — Quick Reference

### Dataset (lab)

```bash
bq --location=<REGION> mk --dataset \
  --default_table_expiration 86400 \
  <GCP_PROJECT_ID>:<DATASET>
```

### Carga do GCS

```sql
LOAD DATA INTO `<GCP_PROJECT_ID>.<DATASET>.orders_raw`
FROM FILES (format = 'PARQUET',
            uris = ['gs://<BUCKET>/raw/orders/dt=2026-10-16/*.parquet']);
```

```bash
bq load --source_format=PARQUET <DATASET>.orders_raw \
  "gs://<BUCKET>/raw/orders/dt=2026-10-16/*.parquet"
```

### Guardrails de custo

```bash
bq query --use_legacy_sql=false --dry_run 'SELECT ...'          # estima bytes
bq query --use_legacy_sql=false --maximum_bytes_billed=1000000000 'SELECT ...'  # 1 GB teto
```

```sql
CREATE TABLE `<DATASET>.fato_pedidos`
PARTITION BY DATE(dt_pedido)
CLUSTER BY cliente_id
OPTIONS (require_partition_filter = TRUE)
AS SELECT * FROM `<DATASET>.orders_raw`;
```

### Preços (verificar região)

| Item | Valor |
|---|---|
| Free tier query | 1 TiB/mês |
| Free tier storage | 10 GiB/mês |
| On-demand | ~US$ 6,25/TiB lido (**a validar** por região) |
| Batch load (pool compartilhado) | grátis |
| Editions | slot-hora (Standard/Enterprise/Enterprise Plus) — sem custo se sem reserva |
| Sandbox | sem cartão; 60 dias de expiração; **sem DML** |

### IAM mínimo (pipeline)

| Onde | Papel |
|---|---|
| Projeto | `roles/bigquery.jobUser` |
| Dataset de destino | `roles/bigquery.dataEditor` |
| Bucket de origem | `roles/storage.objectViewer` |

### SCD2 (esqueleto)

`MERGE` com `UNION ALL` (linha com `merge_key` NULL força o INSERT da nova versão) — ver
`patterns/merge-scd2.md`.

### Teardown

```bash
bq rm -r -f -d <GCP_PROJECT_ID>:<DATASET>
```

Regra: criar → testar → destruir no mesmo dia.
