---
name: devloop-round
description: |
  Revalida tarefas falhas do PROMPT após execute ou fixers; incrementa round no manifest.
---

# `/devloop-round` — Revalidação incremental

**Canônico:** `.github/commands/workflow-dev-loop/devloop-round.md`

## Usage

```bash
/devloop-round <RUN_ID>
```

Opcional: colar `git diff` ou listar arquivos alterados.

## O que faz

1. Lê manifest + `PROMPT_*.md` + `progress/PROGRESS_*.md`
2. Incrementa `round` no manifest
3. Reexecuta verificações das tarefas em falha ou incompletas
4. Atualiza `phases/execute.md` e log

**Próximo comando sugerido:** `/devloop-fixer`, `/devloop-execute --resume`, ou `/devloop-phase <RUN_ID> reflect`

## Agente

**`devloop-round`** — `.github/agents/workflow-dev-loop/devloop-round.md`
