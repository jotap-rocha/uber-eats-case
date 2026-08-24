# Comandos — workflow Data Pipeline Review

Arquivos canônicos (editar aqui):

| Comando | Ficheiro |
|---------|----------|
| `/workflow-data-pipeline-review` | [`workflow-data-pipeline-review.md`](workflow-data-pipeline-review.md) — entrada |
| `/pipeline-review-init` | [`pipeline-review-init.md`](pipeline-review-init.md) |
| `/pipeline-review-lane` | [`pipeline-review-lane.md`](pipeline-review-lane.md) |
| `/pipeline-review-round` | [`pipeline-review-round.md`](pipeline-review-round.md) |
| `/pipeline-review-fixer` | [`pipeline-review-fixer.md`](pipeline-review-fixer.md) |

Estado das revisões: `.github/sdd/data-pipeline-reviews/{RUN_ID}/` · Agentes: `.github/agents/workflow-data-pipeline-review/`.

**Handoff:** cada `/pipeline-review-lane` → **Próximo comando** explícito; fim de `ml_ai_dataops` → `REVIEW_SUMMARY.md` + passos pós-lanes (`pipeline-review-round`, `pipeline-review-fixer`, opcional novo `pipeline-review-init`).
