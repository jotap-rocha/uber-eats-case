---
name: pipeline-review-round
description: |
  Revalida pendências do Data Pipeline Review após lanes/fixers, procurando regressões e novos achados incrementais.
---

# `/pipeline-review-round` — Revalidação incremental

**Canônico:** `.cursor/commands/workflow-data-pipeline-review/pipeline-review-round.md`.

Entrada do fluxo: [`workflow-data-pipeline-review.md`](workflow-data-pipeline-review.md) → `/workflow-data-pipeline-review`.

## Usage

```bash
/pipeline-review-round <RUN_ID>
/pipeline-review-round pr-1842-pipeline-dim-cliente
```

## O que faz

1. Lê `.cursor/sdd/data-pipeline-reviews/{RUN_ID}/REVIEW_MANIFEST.yaml`.
2. Reabre lanes com status `fail`, `pending` ou `in_progress`.
3. Roda checks rasos do contrato e greps de regressão no escopo das lanes afetadas.
4. Adiciona novos findings sem renumerar antigos.
5. Incrementa `round`, atualiza `REVIEW_LOG.md` e sugere próximo comando.

## Agente

**`data-pipeline-review-round`** — `.cursor/agents/workflow-data-pipeline-review/data-pipeline-review-round.md`
