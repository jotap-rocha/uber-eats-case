---
name: devloop-phase
description: |
  Executa UMA fase do Dev Loop (gate, requirements, design, craft, prompt_review, reflect).
  Atualiza phases/<phase>.md e DEVLOOP_MANIFEST.yaml. Uma fase por conversa.
---

# `/devloop-phase` — Uma fase por conversa

**Canônico:** `.claude/commands/workflow-dev-loop/devloop-phase.md`  
Entrada: [`workflow-dev-loop.md`](workflow-dev-loop.md)

## Usage

```bash
/devloop-phase <RUN_ID> <phase_id>

/devloop-phase feat-auth-login gate
/devloop-phase feat-auth-login requirements
/devloop-phase feat-auth-login design
/devloop-phase feat-auth-login craft
/devloop-phase feat-auth-login prompt_review
/devloop-phase feat-auth-login reflect
```

**phase_id:** `gate` | `requirements` | `design` | `craft` | `prompt_review` | `reflect`

> Execução de código: use **`/devloop-execute`** (fase `execute`), não `/devloop-phase execute`.

## Ordem canônica

`gate` → `requirements` → `design` → `craft` → `prompt_review` → **execute** (`/devloop-execute`) → `reflect`

Fonte: [`.claude/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`](../../sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml)

## Regras

- Uma fase por invocação; não avançar fase se a anterior não estiver `pass` (exceto `waived` explícito).
- **`prompt_review`:** gate humano — registrar OK explícito em `phases/prompt_review.md` antes de `/devloop-execute`.
- **`gate`:** se `escalate_sdd`, parar e indicar SDD (`/brainstorm`, `/design`, `/build`).
- Relatório completo em `phases/{phase_id}.md`; chat = resumo + **`Próximo comando:`**.

## Resposta obrigatória do agente

1. Após cada fase exceto `reflect`: **`Próximo comando:`** `` `/devloop-phase <RUN_ID> <próxima_fase>` ``  
   (após `craft` → próximo é sempre `prompt_review`; após `prompt_review` pass → `/devloop-execute`)
2. Após `prompt_review` com OK: **`Próximo comando:`** `` `/devloop-execute <RUN_ID>` ``
3. Após `reflect`: gerar `DEVLOOP_SUMMARY.md` + **`Próximos comandos (pós-run):`** round/fixer ou novo init

## Agente

**`devloop-phase`** — `.claude/agents/workflow-dev-loop/devloop-phase.md`
