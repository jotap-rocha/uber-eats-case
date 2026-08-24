# Airflow — Knowledge Base (práticas de DAG)

> **Propósito:** Padrões de desenho para **Apache Airflow 2.11.x** no ecossistema Data Lake — **TaskFlow**, idempotência, pipelines em fases, retries/callbacks e **dynamic task mapping**.  
> **Infra / edge (314, systemd, F5):** ver [**migration-hub**](../migration-hub/data-stack/airflow/README.md) e [**EDGE-314**](../migration-hub/data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md).

**MCP Validated:** 2026-05-11 (revisão editorial; exemplos validados contra convenções 2.11.x; tags de classificação documentadas).

---

## Navegação rápida

| Tipo | Ficheiro |
|------|-----------|
| Referência rápida | [quick-reference.md](quick-reference.md) |
| TaskFlow (`@dag`, `@task`) | [concepts/taskflow-api.md](concepts/taskflow-api.md) |
| Tags obrigatórias (área, stack, frequência — padrão PT) | [concepts/dag-metadata-tags.md](concepts/dag-metadata-tags.md) |
| Idempotência e macros | [concepts/idempotencia-macros-templates.md](concepts/idempotencia-macros-templates.md) |
| Pipeline: pré-check → carga → pós-check | [patterns/pipeline-pre-check-load-post-check.md](patterns/pipeline-pre-check-load-post-check.md) |
| Retries, callbacks, SLA | [patterns/retries-callbacks-alertas.md](patterns/retries-callbacks-alertas.md) |
| Dynamic task mapping | [patterns/dynamic-task-mapping.md](patterns/dynamic-task-mapping.md) |

---

## Conceitos-chave

| Conceito | Resumo |
|----------|--------|
| **TaskFlow** | DAG como função Python com `@dag` e `@task`; menos boilerplate; XCom entre tasks tipado. |
| **Idempotência** | Re-run do mesmo `logical date` não duplica efeitos — macros (`{{ ds }}`), overwrite de partição, evitar `datetime.now()`. |
| **Três fases (decidido)** | **Pré-check** (diff fonte/destino), **job de carga**, **pós-check** (sucesso + contagens). |
| **Resiliência** | `retries` / `retry_delay`; `on_failure_callback` (Teams/Slack/e-mail). |
| **Tags de classificação** | Três tags por DAG, nesta ordem: área (`data_driven`, …), stack (`python`, `spark`, `dbt`), frequência PT (`horario`, `diaria`, `mensal`); ver [dag-metadata-tags.md](concepts/dag-metadata-tags.md). |

---

## Percurso sugerido

1. Ler [dag-metadata-tags.md](concepts/dag-metadata-tags.md), [taskflow-api.md](concepts/taskflow-api.md) e [quick-reference.md](quick-reference.md).  
2. Fixar idempotência com [idempotencia-macros-templates.md](concepts/idempotencia-macros-templates.md).  
3. Modelar cargas com [pipeline-pre-check-load-post-check.md](patterns/pipeline-pre-check-load-post-check.md).  
4. Acrescentar [retries-callbacks-alertas.md](patterns/retries-callbacks-alertas.md) e [dynamic-task-mapping.md](patterns/dynamic-task-mapping.md).

---

## Agente / ferramentas

| Contexto | Onde ir |
|----------|---------|
| Criar ou refatorar DAG (TaskFlow, tags, Teams) | [airflow-dag-builder](../../agents/data-engineering/airflow-dag-builder.md) |
| Ambiente 314, permissões `airflow`, paths do volume | [big-data-cluster-expert](../../agents/data-engineering/big-data-cluster-expert.md) |
| DAGs em `/DATALAKE/dags`, jobs em `workspace/prd/` | [EDGE-314](../migration-hub/data-stack/airflow/EDGE-314-OPERACAO-E-VALIDACAO.md) § DAGs finas + venv por projeto |
| Boas práticas Python (layout dados vs automação) | [python-developer](../../agents/code-quality/python-developer.md) + [design-pipelines-patterns](../design-pipelines-patterns/index.md) ou [design-automation-project-patterns](../design-automation-project-patterns/index.md) |
