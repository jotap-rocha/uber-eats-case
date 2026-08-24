# Comandos — workflow MakeApp Review

Arquivos canônicos (editar aqui):

| Comando | Ficheiro |
|---------|----------|
| `/workflow-makeapp-review` | [`workflow-makeapp-review.md`](workflow-makeapp-review.md) — entrada (roteador) |
| `/reviewer-init` | [`reviewer-init.md`](reviewer-init.md) |
| `/reviewer-lane` | [`reviewer-lane.md`](reviewer-lane.md) |
| `/reviewer-round` | [`reviewer-round.md`](reviewer-round.md) |
| `/reviewer-fixer` | [`reviewer-fixer.md`](reviewer-fixer.md) |

Atalhos com o mesmo `name` no frontmatter: [`../review/`](../review/) (`reviewer-*.md` → links para esta pasta).

Estado das revisões: `.claude/sdd/reviews/{RUN_ID}/` · Agentes: `.claude/agents/workflow-makeapp-review/`.

**Handoff:** cada `/reviewer-lane` → **Próximo comando** explícito; fim de `ui_ux` → **`REVIEW_SUMMARY.md`** + passos pós-lanes (`reviewer-round`, `reviewer-fixer`, opcional novo `reviewer-init`).
