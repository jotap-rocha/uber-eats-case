---
name: devloop-fixer
description: |
  Correção guiada de uma tarefa do PROMPT; atualiza código, progress e manifest do RUN.
---

# `/devloop-fixer` — Correção guiada

**Canônico:** `.github/commands/workflow-dev-loop/devloop-fixer.md`

## Usage

```bash
/devloop-fixer <RUN_ID> <task_ref> — <instrução>

/devloop-fixer feat-auth-login T3 — corrigir validação de email no parser
/devloop-fixer feat-auth-login "Task 2" — adicionar teste unitário faltante
```

## O que faz

1. Escopo explícito (task_ref + instrução); se vago → pedir clarificação
2. Implementa só o pedido
3. Atualiza PROGRESS, `phases/execute.md`, manifest
4. Append em `DEVLOOP_LOG.md`

**Próximo comando sugerido:** `` `/devloop-round <RUN_ID>` ``

## Agente

**`devloop-fixer`** — `.github/agents/workflow-dev-loop/devloop-fixer.md`
