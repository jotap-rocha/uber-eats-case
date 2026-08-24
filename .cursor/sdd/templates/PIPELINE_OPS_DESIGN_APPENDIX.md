# Anexo — Design operacional (componentes mandatórios)

> **Quando anexar:** fase Dev Loop `design` ou SDD `/design` para pipelines Databricks/Spark.

---

## File manifest mínimo

| Componente | Path sugerido | Obrigatório |
|------------|---------------|-------------|
| Contrato dados | `docs/data-contract-{dataset}.md` | Sim |
| Changelog contrato | `docs/CHANGELOG-data-contract-{dataset}.md` | Sim |
| Schemas / contrato código | `src/{package}/schemas.py`, `medallion_contract.py` | Sim |
| Metadados UC G02 | `src/{package}/dlt_uc_metadata.py` | Sim (UC) |
| Expectations Bronze | `src/{package}/dlt_bronze_expectations.py` | Sim |
| Expectations Silver | `src/{package}/dlt_silver_expectations.py` | Sim |
| Split quarentena | funções `split_*_valid_and_quarantine` | Sim |
| Métricas quarentena | `src/{package}/dlt_quarantine_metrics.py` | Recomendado |
| Teams notify | `src/{package}/teams_notify.py` | Sim |
| Guard DLT step | `src/{package}/dlt_step_guard.py` | Sim (DLT) |
| Schema drift rescue | `src/{package}/schema_drift_rescue.py` | Se Auto Loader |
| Pós-run notify | `src/{package}/pipeline_completion_notify.py` | Recomendado |
| Sentinela freshness | `src/{package}/sentinela/freshness.py` | Se SLA freshness |
| Smoke Teams | `notebooks/smoke_test_teams_*.py` | Sim |
| Logs JSON | `src/{package}/pipeline_json_log.py` | Recomendado |
| Guia drift | `docs/guia-schema-drift-{projeto}.md` | Se rescue |
| Guia Teams | `docs/guia-teams-{plataforma}.md` ou `DATABRICKS_TEAMS_PIPELINES.md` | Sim |
| Testes contrato | `tests/test_medallion_contract.py` | Sim |
| Bundle | `databricks.yml` | Sim (Databricks) |

## Decisões de arquitectura a documentar (ADR inline)

1. Idempotência: append + apply_changes vs MERGE vs dedupe streaming
2. Schema drift: rescue vs fail vs evolve
3. Quarentena: retenção vs purge (DSV vs PRD)
4. Canais alerta: Teams webhook vs Databricks native notification

## Agentes sugeridos (@)

| Tarefa | Agente |
|--------|--------|
| Medalhão DLT | `@databricks-pipeline-architect` |
| Schema drift | `@databricks-data-engineer` |
| Teams | `@teams-notifications-expert` |
| Contrato/testes | `@data-engineering-reviewer` |

## Verificação pós-build

- [ ] `/pipeline-review-init {RUN_ID}` antes de PRD
- [ ] Smoke Teams DSV OK
- [ ] Testes offline passam (`pytest` / `unittest`)
