# Pattern — Métricas de quarentena persistidas (DQ-003)

> **Quando usar:** operação precisa consultar volume de quarentena sem abrir UI DLT.

## Tabela UC

`{catalog}.silver.{leaf}_quarentena_metricas`

| Coluna | Significado |
|--------|-------------|
| `_run_id` | Correlação job/DLT |
| `_batch_id` | Lote lógico |
| `layer` | `bronze` ou `silver` |
| `quarantine_table` | FQCN tabela origem |
| `violated_rule` | Regra agregada |
| `record_count` | Contagem |
| `measured_at` | Timestamp medição |

## Implementação

- Streaming table DLT agregando `read_stream` das quarentenas Bronze + Silver
- Notebook pós-DLT opcional para emitir logs JSON (DLT não lê tabelas do mesmo DAG no load)

## Dashboards

SQL exemplo em `docs/dashboards/dq-quarentena-metricas.sql`.

## Referência

Varonis: `dlt_quarantine_metrics.py`, contrato §7.4.
