# Anexo — Requisitos operacionais de pipeline (mandato)

> **Quando anexar:** fase Dev Loop `requirements` ou SDD `/define` quando o projecto é pipeline Databricks/Spark.
> **Fonte:** `.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml`

Copie esta secção para `artifacts/{run_id}_requirements.md` ou para o DEFINE. Marque MUST/SHOULD/N/A; use `injected_by_pipeline_mandate` se o analista não pediu.

---

## 1. Contrato de dados

- [ ] **DC-M01** Documento `docs/data-contract-{dataset}.md` (owner, SLA, frequência, evolução schema)
- [ ] **DC-M02** `docs/CHANGELOG-data-contract-{dataset}.md` versionado
- [ ] **DC-M03** Código espelha contrato (`schemas.py`, listas colunas, metadados UC)
- [ ] **DC-M04** Runbook schema drift / adoptar coluna
- [ ] **DC-M05** Testes offline de contrato

## 2. Medalhão e UC

- [ ] **MED-M01** Linhagem Bronze (`_ingest_ts`, `_source_file`, `_run_id`, `_batch_id`)
- [ ] **MED-M02** Projeção explícita Silver/Gold
- [ ] **MED-M03** Comentários UC G02
- [ ] **MED-M04** Política idempotência/reprocessamento documentada

## 3. Qualidade e quarentena

- [ ] **DQ-M01** Expectations por camada
- [ ] **DQ-M02** Quarentena UC (não drop silencioso)
- [ ] **DQ-M03** `_dq_violated_rules`, `_quarantined_at`
- [ ] **DQ-M04** Métricas quarentena (DQ-003)
- [ ] **DQ-M05** Runbook linhas em quarentena após correção

## 4. Schema drift

- [ ] **SD-M01** Schema fixo + rescue (se Auto Loader / origem variável)
- [ ] **SD-M02** Colunas extra → quarentena rastreável
- [ ] **SD-M03** Alerta Teams/email em drift
- [ ] **SD-M04** Runbook reprocessamento path novo

## 5. Teams / alertas

- [ ] **TM-M01** Alerta falha pipeline/DLT
- [ ] **TM-M02** Webhooks DSV/PRD + `.env.example`
- [ ] **TM-M03** Smoke test antes de PRD
- [ ] **TM-M04** `max_retries: 0` + reprocessamento manual
- [ ] **TM-M05** Card acionável (camada, tabela, run_id)
- [ ] **TM-M06** Cards Teams concisos (todos os tipos — ver teams-card-format.md)

## 6. Observabilidade

- [ ] **OBS-M01** Logs JSON estruturados
- [ ] **OBS-M02** Sentinela freshness (se SLA dados)
- [ ] **OBS-M03** Dashboards quarentena/custo

## 7. Segurança e testes

- [ ] **GOV-M01** Secrets fora do código
- [ ] **GOV-M02** Checklist grants UC
- [ ] **TEST-M01** Testes unitários offline
- [ ] **TEST-M02** Pipeline review antes de PRD

## 8. PyODBC → SQL Server (se aplicável)

- [ ] **PYODBC-M01** Gate humano: APPEND vs Overwrite (`AskUserQuestion`)
- [ ] **PYODBC-M02** Se Overwrite: truncate=false (recomendado) vs true (risco)
- [ ] **PYODBC-M03** Decisão em `PYODBC_WRITE_MODE_GATE.md` ou secção no DEFINE

Ver: `.cursor/kb/data-engineering-practices/pyodbc-sqlserver-write-mode.md`

---

**Critérios de aceite:** todos MUST marcados ou N/A justificado antes de `/design` ou fase `design` do Dev Loop.
