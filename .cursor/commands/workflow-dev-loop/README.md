# Comandos — workflow Dev Loop (L2)

Arquivos canônicos (editar em `.cursor/`):

| Comando | Ficheiro |
|---------|----------|
| `/workflow-dev-loop` | [`workflow-dev-loop.md`](workflow-dev-loop.md) — entrada |
| `/devloop-init` | [`devloop-init.md`](devloop-init.md) |
| `/devloop-phase` | [`devloop-phase.md`](devloop-phase.md) |
| `/devloop-craft` | [`devloop-craft.md`](devloop-craft.md) |
| `/devloop-execute` | [`devloop-execute.md`](devloop-execute.md) |
| `/devloop-round` | [`devloop-round.md`](devloop-round.md) |
| `/devloop-fixer` | [`devloop-fixer.md`](devloop-fixer.md) |

Estado: `.cursor/sdd/dev-loop-runs/{RUN_ID}/` · Agentes: `.cursor/agents/workflow-dev-loop/`

**Handoff:** cada `/devloop-phase` → **Próximo comando** explícito; `prompt_review` pass → `/devloop-execute`; fim de `reflect` → `DEVLOOP_SUMMARY.md`.
