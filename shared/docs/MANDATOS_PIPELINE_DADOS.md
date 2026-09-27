# Mandatos de pipeline de dados

Checklist obrigatório ao **criar ou evoluir** um repositório de pipeline Databricks ou Spark local.

**Fonte machine-readable:** [`.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml`](../.cursor/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml)

**Referência de implementação:** repositório `databricks-varonis-dataflow-prd` (Varonis).

---

## Quando aplicar

- Ingestão/transformação medalhão (Bronze → Silver → Gold)
- DLT / Lakeflow / Auto Loader / Spark batch ou streaming
- Dados em Unity Catalog ou Delta Lake

**Não aplicar** a bibliotecas puras, apps web sem ETL, ou docs-only.

---

## Fluxos que enforcem estes mandatos

| Fluxo | O que faz |
|-------|-----------|
| **SDD** `/define`, `/design` | Injeta secção mandato se analista omitir |
| **Dev Loop** `requirements`, `design`, `craft` | Anexos `PIPELINE_OPS_*_APPENDIX.md` |
| **Pipeline Review** `/pipeline-review-init` | Lanes cruzam checks com mandatos |
| **Intake** `/intake` | Roteia para agentes + KB patterns |

---

## Resumo dos mandatos (9 categorias)

### 1. Contrato de dados
Documento operacional + CHANGELOG + código espelhado + testes offline.

### 2. Medalhão
Linhagem, projeção explícita, metadados UC G02, idempotência documentada.

### 3. Qualidade e quarentena
Expectations, split valid/quarantine, métricas DQ, runbook pós-correção.

### 4. Schema drift
Schema fixo + rescue, quarentena `schema_rescue`, alerta Teams, runbook adoptar coluna.

### 5. Teams
Falha DLT, webhooks DSV/PRD, smoke test, `max_retries: 0`, cards acionáveis, **formato conciso TM-M06** (Tier A/B — ver `teams-card-format.md`).

### 6. Observabilidade
Logs JSON, sentinela freshness, dashboards.

### 7. Erros
Fail-fast RAW, distinção drift/corrupt/DQ/infra nos logs.

### 8. Governança
Secrets fora do código, checklist grants UC.

### 9. Testes
Unitários offline + pipeline review antes de PRD.

---

## KB patterns

| Pattern | Path |
|---------|------|
| Schema drift rescue | `.cursor/kb/data-engineering-practices/schema-drift-autoloader-rescue.md` |
| Quarentena split | `.cursor/kb/data-engineering-practices/dlt-quarantine-split-tables.md` |
| Métricas DQ | `.cursor/kb/data-engineering-practices/dq-quarantine-metrics-uc.md` |
| Sentinela | `.cursor/kb/data-engineering-practices/sentinela-freshness-teams.md` |
| Logs JSON | `.cursor/kb/data-engineering-practices/structured-pipeline-logging.md` |
| Teams schema drift (card conciso) | `.cursor/kb/data-engineering-practices/teams-schema-drift-card-format.md` |
| Teams — formato geral (todos cards) | `.cursor/kb/data-engineering-practices/teams-card-format.md` |

---

## Ao bootstrap de novo repo pipeline

1. `install_agentspec.py` ou `upgrade_agentic.py --apply`
2. Copiar `docs/data-contract-TEMPLATE.md` → `docs/data-contract-{dataset}.md`
3. SDD `/define` — verificar secção mandato injectada
4. SDD `/design` — file manifest completo
5. `/pipeline-review-init` antes de PRD

---

## Lições Varonis (por que isto existe)

Capacidades implementadas **manualmente** após o pipeline inicial:

- Alertas Teams (falha, schema drift, conclusão job, sentinela)
- Schema drift Auto Loader rescue + quarentena
- Contrato versionado + runbook reprocessamento
- Métricas quarentena UC

### PyODBC → SQL Server

Gate humano obrigatório em SDD/Dev Loop:

1. **APPEND** ou **Overwrite?**
2. Se Overwrite: **`truncate=false`** (recomendado) ou `true` (risco drop/recreate STRING)?

Template: `.cursor/sdd/templates/PYODBC_WRITE_MODE_GATE.md`  
KB: `.cursor/kb/data-engineering-practices/pyodbc-sqlserver-write-mode.md`

Estes itens passam a ser **pedidos pelo processo**, não descobertos em produção.
