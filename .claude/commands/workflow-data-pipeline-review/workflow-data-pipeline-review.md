---
name: workflow-data-pipeline-review
description: |
  Ponto de entrada do workflow Data Pipeline Review: encaminha para /pipeline-review-init,
  /pipeline-review-lane, /pipeline-review-round e /pipeline-review-fixer. Estado em
  .claude/sdd/data-pipeline-reviews/{RUN_ID}/.
---

# `/workflow-data-pipeline-review` — Data Pipeline Review (entrada)

**Arquivo canônico:** `.claude/commands/workflow-data-pipeline-review/workflow-data-pipeline-review.md`.

Este comando é o **roteador** do review. Execute os passos abaixo na ordem, um slash por objetivo.

## Passos

1. **`/pipeline-review-init <RUN_ID>`** — Cria `.claude/sdd/data-pipeline-reviews/{RUN_ID}/`, manifest, stubs de lanes e log inicial.  
   Ex.: `/pipeline-review-init pr-1842-pipeline-dim-cliente`

2. **`/pipeline-review-lane <RUN_ID> <lane_id>`** — Uma lane por invocação.  
   Ordem recomendada (ver [`.claude/sdd/architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml`](../../sdd/architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml)):

   `data_contracts → architecture_medallion → data_quality → idempotency_reprocessing → code_quality_solid → error_handling_resilience → orchestration_messaging → observability_logging → performance_cost → security_governance → ml_ai_dataops`

   Cada execução deve encerrar indicando o **Próximo comando**. Ao terminar `ml_ai_dataops`, o agente gera `REVIEW_SUMMARY.md` no RUN e indica `/pipeline-review-round`, `/pipeline-review-fixer` e opcional novo `/pipeline-review-init`.

   **Mandatos operacionais:** cruzar findings com [`.claude/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml`](../../sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml) (Teams, schema drift, quarentena, sentinela, contrato).

3. **`/pipeline-review-round <RUN_ID>`** — Revalida pendências após as lanes.

4. **`/pipeline-review-fixer <RUN_ID> <lane> — <instrução>`** — Aplica correções guiadas e atualiza manifest/log.

## Referência rápida

| Slash | Arquivo |
| ----- | ------- |
| `/intake` | [`../intake.md`](../intake.md) + dados em [`../../sdd/architecture/AGENT_ROUTER.yaml`](../../sdd/architecture/AGENT_ROUTER.yaml) |
| `/workflow-data-pipeline-review` | [`workflow-data-pipeline-review.md`](workflow-data-pipeline-review.md) |
| `/pipeline-review-init` | [`pipeline-review-init.md`](pipeline-review-init.md) |
| `/pipeline-review-lane` | [`pipeline-review-lane.md`](pipeline-review-lane.md) |
| `/pipeline-review-round` | [`pipeline-review-round.md`](pipeline-review-round.md) |
| `/pipeline-review-fixer` | [`pipeline-review-fixer.md`](pipeline-review-fixer.md) |

Agentes: `.claude/agents/workflow-data-pipeline-review/` · Índice: [`README.md`](README.md)

## O que pedir ao agente depois de invocar este comando

> Seguir o workflow Data Pipeline Review: já tenho ou vou criar o RUN com `/pipeline-review-init`. Após o init, usar **`Próximo comando:`** `/pipeline-review-lane <RUN_ID> data_contracts`. Em cada `/pipeline-review-lane`, indicar o próximo slash na ordem do CONTRACTS; ao terminar `ml_ai_dataops`, gerar `REVIEW_SUMMARY.md` e indicar `pipeline-review-round` / `pipeline-review-fixer` / novo `pipeline-review-init`.
