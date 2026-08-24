---
name: workflow-makeapp-review
description: |
  Ponto de entrada do workflow MakeApp Review: encaminha para /reviewer-init, /reviewer-lane,
  /reviewer-round e /reviewer-fixer. Estado em .github/sdd/reviews/{RUN_ID}/.
---

# `/workflow-makeapp-review` — MakeApp Review (entrada)

**Arquivo canônico:** `.github/commands/workflow-makeapp-review/workflow-makeapp-review.md` (este documento).

Este comando é só o **roteador**: execute os passos abaixo **na ordem**, um slash por objetivo.

## Passos

1. **`/reviewer-init <RUN_ID>`** — Cria `.github/sdd/reviews/{RUN_ID}/`, manifest, stubs de lanes e log inicial.  
   Ex.: `/reviewer-init pr-1842`

2. **`/reviewer-lane <RUN_ID> <lane_id>`** — Uma **lane por invocação** (não misturar no mesmo chat).  
   Ordem recomendada (ver [`.github/sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml`](../../sdd/architecture/WORKFLOW_MAKEAPP_REVIEW_CONTRACTS.yaml)):

   `security` → `backend` → `frontend` → `databricks` → `performance` → `ui_ux`

   Cada execução de `/reviewer-lane` deve **encerar indicando o próximo slash** (`Próximo comando:`). Ao terminar **`ui_ux`**, o agente gera **`REVIEW_SUMMARY.md`** no RUN (consolidado de todas as lanes) e indica **`/reviewer-round`**, **`/reviewer-fixer`** e opcional novo **`/reviewer-init`**.

3. **`/reviewer-round <RUN_ID>`** — Revalida pendências após as lanes.

4. **`/reviewer-fixer <RUN_ID>`** — Aplica correções guiadas e atualiza o manifest.

## Referência rápida

| Slash | Arquivo |
| ----- | ------- |
| `/intake` | [`../intake.md`](../intake.md) + dados em [`../../sdd/architecture/AGENT_ROUTER.yaml`](../../sdd/architecture/AGENT_ROUTER.yaml) — triagem leve antes de revisão ou implementação |
| `/workflow-makeapp-review` | [`workflow-makeapp-review.md`](workflow-makeapp-review.md) |
| `/reviewer-init` | [`reviewer-init.md`](reviewer-init.md) |
| `/reviewer-lane` | [`reviewer-lane.md`](reviewer-lane.md) |
| `/reviewer-round` | [`reviewer-round.md`](reviewer-round.md) |
| `/reviewer-fixer` | [`reviewer-fixer.md`](reviewer-fixer.md) |

Agentes: `.github/agents/workflow-makeapp-review/` · Índice: [`README.md`](README.md)

## O que pedir ao agente depois de invocar este comando

Copie e adapte:

> Seguir o workflow MakeApp Review: já tenho ou vou criar o RUN com `/reviewer-init`. Após o init, usar **`Próximo comando:`** `/reviewer-lane <RUN_ID> security`. Em cada `/reviewer-lane`, o agente deve indicar o próximo slash na ordem do CONTRACTS; ao terminar `ui_ux`, deve gerar `REVIEW_SUMMARY.md` e indicar `reviewer-round` / `reviewer-fixer` / novo `reviewer-init`.
