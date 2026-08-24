---
name: devloop-craft
description: |
  Atalho para /devloop-phase <RUN_ID> craft — gera PROMPT_*.md a partir de requirements e design.
---

# `/devloop-craft` — Atalho fase craft

**Canônico:** `.claude/commands/workflow-dev-loop/devloop-craft.md`

Equivalente a:

```bash
/devloop-phase <RUN_ID> craft
```

Pré-requisitos: fases `gate`, `requirements` e `design` em `pass` no manifest.

Saída esperada: `.claude/dev/tasks/PROMPT_{RUN_ID}.md`

**Próximo comando após craft:** `` `/devloop-phase <RUN_ID> prompt_review` ``

Agente: `devloop-phase` (delega a `prompt-crafter`).
