---
name: pipeline-review-lane
description: |
  Revisa uma única lane de pipeline de dados. Contexto mínimo: contrato + manifest + globs/KB da lane.
  Atualiza lanes/<lane>.md e REVIEW_MANIFEST.yaml.
---

# `/pipeline-review-lane` — Uma dimensão por conversa

**Canônico:** `.cursor/commands/workflow-data-pipeline-review/pipeline-review-lane.md`.

Entrada do fluxo: [`workflow-data-pipeline-review.md`](workflow-data-pipeline-review.md) → `/workflow-data-pipeline-review`.

## Usage

```bash
/pipeline-review-lane <RUN_ID> <lane_id>

/pipeline-review-lane pr-1842 data_contracts
/pipeline-review-lane pr-1842 architecture_medallion
/pipeline-review-lane pr-1842 data_quality
/pipeline-review-lane pr-1842 idempotency_reprocessing
/pipeline-review-lane pr-1842 code_quality_solid
/pipeline-review-lane pr-1842 error_handling_resilience
/pipeline-review-lane pr-1842 orchestration_messaging
/pipeline-review-lane pr-1842 observability_logging
/pipeline-review-lane pr-1842 performance_cost
/pipeline-review-lane pr-1842 security_governance
/pipeline-review-lane pr-1842 ml_ai_dataops
```

**lane_id** canônico: `data_contracts` | `architecture_medallion` | `data_quality` | `idempotency_reprocessing` | `code_quality_solid` | `error_handling_resilience` | `orchestration_messaging` | `observability_logging` | `performance_cost` | `security_governance` | `ml_ai_dataops`

## Regra de contexto

- Não pedir ao modelo para revisar todas as lanes neste comando.
- Relatório completo em `.cursor/sdd/data-pipeline-reviews/{RUN_ID}/lanes/{lane_id}.md`.
- No chat: resumo curto + pointer ao arquivo + bloco **Próximo comando**.

## Resposta do agente obrigatória

Ordem das lanes: `data_contracts → architecture_medallion → data_quality → idempotency_reprocessing → code_quality_solid → error_handling_resilience → orchestration_messaging → observability_logging → performance_cost → security_governance → ml_ai_dataops`.

1. **Após cada lane exceto `ml_ai_dataops`:** terminar com **`Próximo comando:`** `` `/pipeline-review-lane <RUN_ID> <próxima_lane>` ``.
2. **Após `ml_ai_dataops`:** gerar/atualizar `REVIEW_SUMMARY.md` e terminar com **`Próximos comandos (pós-lanes):`**
   - `` `/pipeline-review-round <RUN_ID>` ``
   - `` `/pipeline-review-fixer <RUN_ID> <lane> — <instrução>` ``
   - Opcional: novo ciclo `` `/pipeline-review-init <novo_RUN_ID>` ``

Detalhe do processo: `.cursor/agents/workflow-data-pipeline-review/data-pipeline-review-lane.md`.
