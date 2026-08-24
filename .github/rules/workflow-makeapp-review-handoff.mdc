---
description: Workflow MakeApp Review — ao concluir init, lane, round ou fixer, indicar sempre o próximo comando slash na ordem canônica
alwaysApply: true
---

# Workflow-makeapp-review — handoff obrigatório

Quando estiveres a executar ou a **concluir** um passo do fluxo definido em [`.github/commands/workflow-makeapp-review/workflow-makeapp-review.md`](mdc:.github/commands/workflow-makeapp-review/workflow-makeapp-review.md) (ou comandos `reviewer-*`), **inclui sempre** um bloco explícito de próximo passo:

## Ordem canônica das lanes

Fonte única: [`execution_order_recommended`](mdc:.github/sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml) em `.github/sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml`:

`security` → `backend` → `frontend` → `databricks` → `performance` → `ui_ux`

## O que responder ao usuário

1. **Após `/reviewer-init <RUN_ID>`** — linha **`Próximo comando:`** com `` `/reviewer-lane <RUN_ID> security` ``.
2. **Após `/reviewer-lane <RUN_ID> <lane>`** se `<lane>` **não** for `ui_ux` — **`Próximo comando:`** com `` `/reviewer-lane <RUN_ID> <próxima_lane>` `` (seguinte na lista acima).
3. **Após `/reviewer-lane … ui_ux`** — indicar path a **`REVIEW_SUMMARY.md`** no RUN e **`Próximos comandos (pós-lanes):`** `` `/reviewer-round <RUN_ID>` ``, `` `/reviewer-fixer <RUN_ID> <lane> — …` ``, e opcional `` `/reviewer-init <novo_RUN_ID>` `` para novo ciclo completo.
4. **Após `/reviewer-round <RUN_ID>`** — **`Próximo comando sugerido:`** (tipicamente fixer ou novo init / encerramento, conforme estado do manifest).
5. **Após `/reviewer-fixer …`** — **`Próximo comando sugerido:`** (tipicamente `` `/reviewer-round <RUN_ID>` ``).

Não substituir este handoff por vagas referências a “continuar o workflow”; o **comando completo** (com o mesmo `RUN_ID` que o usuário está usando) deve aparecer no texto da resposta.
