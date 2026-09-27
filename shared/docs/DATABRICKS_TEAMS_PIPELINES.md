# Databricks — Teams, ambientes (DSV/PRD) e pipelines sem retry

> **Documentação humana** do template Agent Spec. Fonte canónica para agentes: [`.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md`](../.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md).

Use este guia ao **criar ou clonar** um projeto Databricks com Asset Bundle que deve alertar o Microsoft Teams em falha e **não** reexecutar o job em loop.

---

## Princípios (macro — qualquer projeto)

| # | Regra |
|---|--------|
| 1 | **Job sem retry:** `max_retries: 0` (e `retry_on_timeout: false`) no job e em **cada** task. Erro → parar → analista corrige → nova run **manual**. |
| 2 | **Teams antes do `raise`:** card com camada, processo, tabela, ambiente, erro e trecho de código. |
| 3 | **DSV ≠ PRD:** variáveis `URL_WEBHOOK_<PROJETO>_DSV` e `_PRD` no `.env`; targets `dev` / `prd` no `databricks.yml`. |
| 4 | **Smoke test** por ambiente antes de forçar falha real no pipeline. |
| 5 | **Nunca** commitar URL de webhook no Git. |

---

## Onde ler no template

| Tema | Caminho |
|------|---------|
| Ambientes, smoke, checklist | [`.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md`](../.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md) |
| Sem retry + campos do card | [`.cursor/kb/databricks/patterns/pipeline-failure-teams-no-retry.md`](../.cursor/kb/databricks/patterns/pipeline-failure-teams-no-retry.md) |
| Falha genérica | [`.cursor/kb/teams-notifications/patterns/falha-de-pipeline.md`](../.cursor/kb/teams-notifications/patterns/falha-de-pipeline.md) |
| Quick reference | [`.cursor/kb/teams-notifications/quick-reference.md`](../.cursor/kb/teams-notifications/quick-reference.md) |
| Formato conciso (todos cards) | [`.cursor/kb/data-engineering-practices/teams-card-format.md`](../.cursor/kb/data-engineering-practices/teams-card-format.md) |
| Agente | `@teams-notifications-expert` — [`.cursor/agents/domain/teams-notifications-expert.md`](../.cursor/agents/domain/teams-notifications-expert.md) |
| Variáveis `.env` | [`.env.example`](../.env.example) |

---

## Referência de implementação

O repositório **Varonis** (`databricks-varonis-dataflow-prd`) implementa o padrão completo:

- `src/varonis_pipeline/teams_notify.py` — cards Tier A/B (`build_failure_message`, `build_schema_drift_message`, `build_gold_stale_message`)
- `src/varonis_pipeline/dlt_step_guard.py` — `@guard_dlt_step`
- `databricks.yml` — `job_task_max_retries: 0`, webhooks por target
- `notebooks/smoke_test_teams_notification.py` — smoke DSV/PRD
- `docs/guia-teams-databricks.md` — guia operacional do projeto

Ao iniciar um projeto novo: copiar a **estrutura** (módulo notify + guard + bundle + smoke), adaptar prefixos `URL_WEBHOOK_*` e catálogos UC.

---

## Mensagem de erro — o que o analista deve ver

**Formato Tier B** (resumo + detalhe): ver [teams-card-format.md](../.cursor/kb/data-engineering-practices/teams-card-format.md).

1. **Resumo:** camada/processo, tabela, ambiente, erro (1 linha), onde corrigir  
2. **Detalhe (após `---`):** stack `varonis_pipeline`, traceback, run tags Databricks quando disponíveis  

Depois do envio → **`raise`** (não engolir exceção).

---

## Smoke test — resumo

```bash
# 1) Deploy no target certo
databricks bundle deploy -t dev   # ou -t prd

# 2) Importar .env (uma vez por ambiente)
databricks workspace import .env ".../dev/files/.env" --overwrite
# ou .../prd/files/.env

# 3) Notebook smoke — validar diagnóstico:
#    environment + catalog + webhook_source com sufixo _DSV ou _PRD
```

Em PRD, se o diagnóstico mostrar `environment: dsv` com webhook PRD correto, usar widget `varonis_profile=prd` ou `deployment_profile="prd"` na API (ver KB).

---

## Checklist de entrega (novo projeto)

```text
[ ] max_retries: 0 em job e tasks (validar no UI Workflows)
[ ] targets dev/prd com teams_webhook_env_var distintos
[ ] Card de falha com camada, processo, tabela, código, erro
[ ] Smoke verde em DSV e PRD nos canais corretos
[ ] .env.example com _DSV e _PRD; .env no .gitignore
[ ] Sem URL de webhook no repositório
```
