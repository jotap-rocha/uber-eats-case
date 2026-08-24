# Data Engineering Practices — índice

Padrões operacionais mandatórios para pipelines Databricks/Spark.

**Fonte canónica de mandatos:** [`.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml`](../../sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml)

| Pattern | Ficheiro |
|---------|----------|
| Schema drift (Auto Loader rescue) | [schema-drift-autoloader-rescue.md](./schema-drift-autoloader-rescue.md) |
| Quarentena split valid/quarantine | [dlt-quarantine-split-tables.md](./dlt-quarantine-split-tables.md) |
| Métricas DQ UC | [dq-quarantine-metrics-uc.md](./dq-quarantine-metrics-uc.md) |
| Sentinela freshness + Teams | [sentinela-freshness-teams.md](./sentinela-freshness-teams.md) |
| Logs estruturados JSON | [structured-pipeline-logging.md](./structured-pipeline-logging.md) |
| PyODBC SQL Server APPEND/Overwrite/TRUNCATE | [pyodbc-sqlserver-write-mode.md](./pyodbc-sqlserver-write-mode.md) |
| Teams schema drift (card conciso) | [teams-schema-drift-card-format.md](./teams-schema-drift-card-format.md) |
| Teams — formato geral (todos cards) | [teams-card-format.md](./teams-card-format.md) |

**Referência de implementação:** repositório `databricks-varonis-dataflow-prd`.

**Guia humano:** [`docs/MANDATOS_PIPELINE_DADOS.md`](../../../docs/MANDATOS_PIPELINE_DADOS.md)
