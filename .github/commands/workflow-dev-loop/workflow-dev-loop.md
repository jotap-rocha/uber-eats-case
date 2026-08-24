---
name: workflow-dev-loop
description: |
  Ponto de entrada do workflow Dev Loop (L2): encaminha para /devloop-init, /devloop-phase,
  /devloop-craft, /devloop-execute, /devloop-round e /devloop-fixer. Estado em
  .github/sdd/dev-loop-runs/{RUN_ID}/.
---

# `/workflow-dev-loop` — Dev Loop (entrada)

**Arquivo canônico:** `.github/commands/workflow-dev-loop/workflow-dev-loop.md` (este documento).

Roteador do fluxo de **implementação Nível 2**. Execute os passos **na ordem**, um slash por objetivo.

## Passos

1. **`/devloop-init <RUN_ID>`** — Cria `.github/sdd/dev-loop-runs/{RUN_ID}/`, manifest, stubs de fases e `artifacts/`.  
   Ex.: `/devloop-init feat-auth-login`

2. **`/devloop-phase <RUN_ID> <phase_id>`** — **Uma fase por invocação** (não misturar no mesmo chat).  
   Ordem obrigatória (ver [`.github/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`](../../sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml)):

   `gate` → `requirements` → `design` → `craft` → `prompt_review` → `execute` → `reflect`

   - **`gate`** — obrigatório; confirma L2 vs L3 antes de continuar.
   - **`prompt_review`** — gate **humano** obrigatório; só avançar para execute com OK explícito.
   - **Pipeline Databricks/Spark:** fases `requirements`/`design`/`craft` devem incluir mandatos de [`.github/sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml`](../../sdd/architecture/PIPELINE_MANDATORY_PRACTICES.yaml) (anexos `PIPELINE_OPS_*_APPENDIX.md`).
   - Cada `/devloop-phase` deve encerrar com **`Próximo comando:`** e o slash completo.

3. **`/devloop-execute <RUN_ID>`** — Só após `prompt_review` = pass. Roda `/dev tasks/PROMPT_{RUN_ID}.md`.

4. **`/devloop-round <RUN_ID>`** — Revalida tarefas falhas após execute ou fixers.

5. **`/devloop-fixer <RUN_ID> <task_ref> — <instrução>`** — Correção guiada de uma tarefa do PROMPT.

6. **`/devloop-phase <RUN_ID> reflect`** — Gera `DEVLOOP_SUMMARY.md` e encerra o RUN.

## Atalhos

| Slash | Equivalente |
| ----- | ------------- |
| `/devloop-craft <RUN_ID>` | `/devloop-phase <RUN_ID> craft` |

## Referência rápida

| Slash | Arquivo |
| ----- | ------- |
| `/workflow-dev-loop` | [`workflow-dev-loop.md`](workflow-dev-loop.md) |
| `/devloop-init` | [`devloop-init.md`](devloop-init.md) |
| `/devloop-phase` | [`devloop-phase.md`](devloop-phase.md) |
| `/devloop-craft` | [`devloop-craft.md`](devloop-craft.md) |
| `/devloop-execute` | [`devloop-execute.md`](devloop-execute.md) |
| `/devloop-round` | [`devloop-round.md`](devloop-round.md) |
| `/devloop-fixer` | [`devloop-fixer.md`](devloop-fixer.md) |
| `/dev` | [`.github/commands/dev/dev.md`](../dev/dev.md) |

Agentes: `.github/agents/workflow-dev-loop/` · Runs: `.github/sdd/dev-loop-runs/` · Guia: [`DEV_LOOP_Guia_Comandos.md`](../../../get_started/DEV_LOOP_Guia_Comandos.md)

## O que pedir ao agente

> Seguir o workflow Dev Loop: criar ou usar RUN com `/devloop-init`. Após init, **`Próximo comando:`** `/devloop-phase <RUN_ID> gate`. Em cada fase, indicar o próximo slash na ordem do CONTRACTS. Não executar `/devloop-execute` sem `prompt_review` aprovado pelo humano. Ao terminar `reflect`, gerar `DEVLOOP_SUMMARY.md`.
