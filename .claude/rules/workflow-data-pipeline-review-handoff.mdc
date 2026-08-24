---
description: Workflow Data Pipeline Review — ao concluir init, lane, round ou fixer, indicar sempre o próximo comando slash na ordem canônica
alwaysApply: true
---

# Workflow Data Pipeline Review — handoff obrigatório

Quando estiveres a executar ou a **concluir** um passo do fluxo definido em [`.claude/commands/workflow-data-pipeline-review/workflow-data-pipeline-review.md`](mdc:.claude/commands/workflow-data-pipeline-review/workflow-data-pipeline-review.md) (ou comandos `pipeline-review-*`), **inclui sempre** um bloco explícito de próximo passo.

## Ordem canônica das lanes

Fonte única: [`execution_order_recommended`](mdc:.claude/sdd/architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml) em `.claude/sdd/architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml`:

`data_contracts → architecture_medallion → data_quality → idempotency_reprocessing → code_quality_solid → error_handling_resilience → orchestration_messaging → observability_logging → performance_cost → security_governance → ml_ai_dataops`

## O que responder ao usuário

1. **Após `/pipeline-review-init <RUN_ID>`** — linha **`Próximo comando:`** com `` `/pipeline-review-lane <RUN_ID> data_contracts` ``.
2. **Após `/pipeline-review-lane <RUN_ID> <lane>`** se `<lane>` **não** for `ml_ai_dataops` — **`Próximo comando:`** com `` `/pipeline-review-lane <RUN_ID> <próxima_lane>` ``.
3. **Após `/pipeline-review-lane … ml_ai_dataops`** — indicar path a `REVIEW_SUMMARY.md` no RUN e **`Próximos comandos (pós-lanes):`** `` `/pipeline-review-round <RUN_ID>` ``, `` `/pipeline-review-fixer <RUN_ID> <lane> — …` ``, e opcional `` `/pipeline-review-init <novo_RUN_ID>` ``.
4. **Após `/pipeline-review-round <RUN_ID>`** — **`Próximo comando sugerido:`** conforme estado do manifest.
5. **Após `/pipeline-review-fixer …`** — **`Próximo comando sugerido:`** tipicamente `` `/pipeline-review-round <RUN_ID>` ``.

Não substituir este handoff por referência vaga a “continuar o workflow”; o comando completo com o mesmo `RUN_ID` deve aparecer no texto.
