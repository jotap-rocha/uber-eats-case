---
name: reviewer-round
description: |
  Nova rodada incremental: revalida lanes com falha/pendência e deteta achados novos sem
  refazer lanes já pass sem motivo. Incrementa round no manifest e regista no REVIEW_LOG.
---

# `/reviewer-round` — Revisão incremental

**Canónico:** `.claude/commands/workflow-makeapp-review/reviewer-round.md`. Atalho: [`../review/reviewer-round.md`](../review/reviewer-round.md).

Entrada do fluxo: [`workflow-makeapp-review.md`](workflow-makeapp-review.md) → `/workflow-makeapp-review`.

## Usage

```bash
/reviewer-round <RUN_ID>
/reviewer-round pr-1842
```

Opcional na mesma mensagem: colar `git diff` ou indicar arquivos alterados para focar greps.

---

## O que faz

1. Lê `REVIEW_MANIFEST.yaml` e só `lanes/*.md` com `fail | pending | in_progress` (ou pedido explícito para incluir `pass`).
2. Incrementa `round` no manifest.
3. Reexecuta checks **rasos** + greps de regressão nas lanes alvo.
4. Acrescenta novos findings (novos IDs); marca resolvidos se evidência mostrar correção.
5. Append curto em `REVIEW_LOG.md`.

O agente deve encerrar com **`Próximo comando sugerido:`** (ex.: `/reviewer-fixer`, novo `/reviewer-init` ou encerramento do gate).

---

## Agente

**`makeapp-review-round`** — `.claude/agents/workflow-makeapp-review/makeapp-review-round.md`

---

## Quando usar

- Depois de merges/commits na branch em revisão
- Depois de `/reviewer-fixer` em vários itens
- Depois de `REVIEW_SUMMARY.md` se quiseres **atualizar** o consolidado (refazer `/reviewer-lane … ui_ux` ou ajustar manualmente)
- Antes de aprovar PR
