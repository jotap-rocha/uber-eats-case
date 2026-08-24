---
name: pipeline-review-fixer
description: |
  Aplica correções guiadas para findings do Data Pipeline Review e atualiza manifest/log/relatório da lane.
---

# `/pipeline-review-fixer` — Correção guiada

**Canônico:** `.cursor/commands/workflow-data-pipeline-review/pipeline-review-fixer.md`.

Entrada do fluxo: [`workflow-data-pipeline-review.md`](workflow-data-pipeline-review.md) → `/workflow-data-pipeline-review`.

## Usage

```bash
/pipeline-review-fixer <RUN_ID> <lane> — <instrução>
/pipeline-review-fixer pr-1842 data_quality — corrigir DQ-001 expectations ausentes na Silver
```

## Regras

- Exigir escopo explícito: lane + finding ID ou descrição inequívoca.
- Corrigir só o que foi pedido.
- Atualizar `lanes/<lane>.md`, `REVIEW_MANIFEST.yaml` e `REVIEW_LOG.md`.
- Terminar com **`Próximo comando sugerido:`**, normalmente `` `/pipeline-review-round <RUN_ID>` ``.

## Agente

**`data-pipeline-review-fixer`** — `.cursor/agents/workflow-data-pipeline-review/data-pipeline-review-fixer.md`
