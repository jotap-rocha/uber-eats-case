# Data Pipeline Review

Revisões estruturadas para pipelines de engenharia de dados, com estado em disco e uma lane por invocação.

## Estrutura por RUN

```text
.github/sdd/data-pipeline-reviews/{RUN_ID}/
  REVIEW_MANIFEST.yaml
  REVIEW_LOG.md
  REVIEW_SUMMARY.md
  lanes/
    data_contracts.md
    architecture_medallion.md
    data_quality.md
    idempotency_reprocessing.md
    code_quality_solid.md
    error_handling_resilience.md
    orchestration_messaging.md
    observability_logging.md
    performance_cost.md
    security_governance.md
    ml_ai_dataops.md
```

## Comandos

| Comando | Função |
|---------|--------|
| `/workflow-data-pipeline-review` | Visão geral e ordem dos passos |
| `/pipeline-review-init` | Cria `RUN_ID`, manifest e stubs de lanes |
| `/pipeline-review-lane` | Revisa uma lane por vez e indica o próximo comando |
| `/pipeline-review-round` | Revalida pendências e procura regressões |
| `/pipeline-review-fixer` | Correções guiadas + atualização de manifest/log |

## Ordem recomendada

`data_contracts → architecture_medallion → data_quality → idempotency_reprocessing → code_quality_solid → error_handling_resilience → orchestration_messaging → observability_logging → performance_cost → security_governance → ml_ai_dataops`

## Contrato de lanes

Ver [`.github/sdd/architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml`](../architecture/WORKFLOW_DATA_PIPELINE_REVIEW_CONTRACTS.yaml).
