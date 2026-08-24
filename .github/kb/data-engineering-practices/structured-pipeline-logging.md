# Pattern — Logs estruturados de pipeline

> **Quando usar:** diagnóstico operacional sem abrir código ou UI DLT.

## Formato

JSON parseável com campos mínimos:

| Campo | Exemplo |
|-------|---------|
| `event` | `pipeline_run_started`, `pipeline_run_outcome`, `dq_quarantine_metrics` |
| `run_id` | job run ou applicationId |
| `layer` | `bronze`, `silver`, `gold` |
| `process` | `ingest_arquivos_sensiveis` |
| `table` | FQCN UC |
| `outcome` | `success`, `failure`, `warn` |
| `timestamp` | ISO-8601 |

## Onde emitir

- Início/fim de steps DLT (`@guard_dlt_step`)
- Notebook pós-run (métricas DQ — DLT não lê tabelas do mesmo DAG)
- Sentinela freshness

## Dashboards

Queries SQL em `docs/dashboards/` para duração, custo, quarentena.

## Referência

Varonis: `pipeline_json_log.py`, `emit_dq_quarantine_metrics_logs.py`.
