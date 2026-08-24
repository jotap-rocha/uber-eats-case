---
name: reviewer-fixer
description: |
  Correções guiadas pelo usuário para findings de uma lane; obriga atualização de
  REVIEW_MANIFEST.yaml, lanes/<lane>.md e REVIEW_LOG.md para não repetir trabalho.
---

# `/reviewer-fixer` — Ajustes com estado sincronizado

**Canónico:** `.claude/commands/workflow-makeapp-review/reviewer-fixer.md`. Atalho: [`../review/reviewer-fixer.md`](../review/reviewer-fixer.md).

Entrada do fluxo: [`workflow-makeapp-review.md`](workflow-makeapp-review.md) → `/workflow-makeapp-review`.

## Usage

```bash
/reviewer-fixer <RUN_ID> <lane_id> — <instrução explícita>

/reviewer-fixer pr-1842 security — corrigir SEC-002 e atualizar CORS conforme finding
/reviewer-fixer pr-1842 frontend — FE-001 remover chave hardcoded em componente X
```

**Sem instrução explícita** → o agente deve pedir clarificação antes de editar código.

---

## O que faz

1. Lê `lanes/{lane_id}.md` e `REVIEW_MANIFEST.yaml`.
2. Altera **só** o escopo pedido (código/config).
3. Marca findings tratados no `lanes/*.md`.
4. Atualiza `status` da lane no manifest se não restarem blockers/major.
5. Linha em `REVIEW_LOG.md`.

O agente deve encerrar com **`Próximo comando sugerido:`** (em geral `/reviewer-round <RUN_ID>`).

---

## Agente

**`makeapp-review-fixer`** — `.claude/agents/workflow-makeapp-review/makeapp-review-fixer.md`

---

## Fluxo típico

```text
/reviewer-lane RUN security   → findings SEC-001 … + Próximo comando: /reviewer-lane RUN backend
…
/reviewer-lane RUN ui_ux      → REVIEW_SUMMARY.md + Próximos: round / fixer / novo init
/reviewer-fixer RUN security — SEC-001 … + Próximo: /reviewer-round RUN
/reviewer-round RUN          → confirmar ou novos achados
```
