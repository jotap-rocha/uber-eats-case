---
name: devloop-execute
description: |
  Executa o PROMPT do RUN via dev-loop-executor (/dev tasks/PROMPT_*.md). Exige prompt_review=pass.
---

# `/devloop-execute` — Execução do PROMPT

**Canônico:** `.github/commands/workflow-dev-loop/devloop-execute.md`

## Usage

```bash
/devloop-execute <RUN_ID>
/devloop-execute feat-auth-login --dry-run
/devloop-execute feat-auth-login --resume
/devloop-execute feat-auth-login --mode afk
```

## Pré-requisito obrigatório

`phases.prompt_review.status` = **`pass`** no `DEVLOOP_MANIFEST.yaml` (OK humano em `phases/prompt_review.md`).

Se não pass → **`Próximo comando:`** `` `/devloop-phase <RUN_ID> prompt_review` ``

## O que faz

1. Lê manifest → `prompt_file` (ex.: `.github/dev/tasks/PROMPT_{RUN_ID}.md`)
2. Marca `phases.execute: in_progress`
3. Executa como **`/dev tasks/PROMPT_{RUN_ID}.md`** (opções repassadas: `--dry-run`, `--resume`, `--mode`)
4. Atualiza manifest (`execute`: pass/fail) e `phases/execute.md`
5. Append em `DEVLOOP_LOG.md`

## Resposta obrigatória

- **`Próximo comando:`** `` `/devloop-phase <RUN_ID> reflect` `` se concluído com sucesso
- Se falhas: `` `/devloop-round <RUN_ID>` `` ou `` `/devloop-fixer <RUN_ID> <task> — …` ``

## Agente

**`devloop-execute`** — `.github/agents/workflow-dev-loop/devloop-execute.md`  
Motor: `dev-loop-executor` + [`.github/commands/dev/dev.md`](../dev/dev.md)
