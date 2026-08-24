# Relatório consolidado Data Pipeline Review — **RUN_ID**

**Gerado em:** REPLACE_ISO8601 (UTC)  
**Manifest:** [`REVIEW_MANIFEST.yaml`](./REVIEW_MANIFEST.yaml)  
**Branch / PR:** _(do manifest, se preenchido)_

## Estado por lane

| Lane | Status (manifest) | Relatório |
|------|-------------------|-----------|
| data_contracts | _pending / pass / fail_ | [lanes/data_contracts.md](./lanes/data_contracts.md) |
| architecture_medallion | _pending / pass / fail_ | [lanes/architecture_medallion.md](./lanes/architecture_medallion.md) |
| data_quality | _pending / pass / fail_ | [lanes/data_quality.md](./lanes/data_quality.md) |
| idempotency_reprocessing | _pending / pass / fail_ | [lanes/idempotency_reprocessing.md](./lanes/idempotency_reprocessing.md) |
| code_quality_solid | _pending / pass / fail_ | [lanes/code_quality_solid.md](./lanes/code_quality_solid.md) |
| error_handling_resilience | _pending / pass / fail_ | [lanes/error_handling_resilience.md](./lanes/error_handling_resilience.md) |
| orchestration_messaging | _pending / pass / fail_ | [lanes/orchestration_messaging.md](./lanes/orchestration_messaging.md) |
| observability_logging | _pending / pass / fail_ | [lanes/observability_logging.md](./lanes/observability_logging.md) |
| performance_cost | _pending / pass / fail_ | [lanes/performance_cost.md](./lanes/performance_cost.md) |
| security_governance | _pending / pass / fail_ | [lanes/security_governance.md](./lanes/security_governance.md) |
| ml_ai_dataops | _pending / pass / fail_ | [lanes/ml_ai_dataops.md](./lanes/ml_ai_dataops.md) |

## Achados consolidados por lane

Resumo das linhas da tabela **Findings** de cada `lanes/<lane>.md` (`blocker` / `major` primeiro).

### data_contracts

- _(DC-xxx …)_

### architecture_medallion

- _(MED-xxx …)_

### data_quality

- _(DQ-xxx …)_

### idempotency_reprocessing

- _(IDEMP-xxx …)_

### code_quality_solid

- _(CODE-xxx …)_

### error_handling_resilience

- _(ERR-xxx …)_

### orchestration_messaging

- _(ORCH-xxx …)_

### observability_logging

- _(OBS-xxx …)_

### performance_cost

- _(PERF-xxx …)_

### security_governance

- _(GOV-xxx …)_

### ml_ai_dataops

- _(AIML-xxx …)_

## Próximos passos sugeridos

1. `/pipeline-review-round RUN_ID` — revalidar após correções.
2. `/pipeline-review-fixer RUN_ID <lane> — <finding>` — corrigir com escopo explícito.
3. Novo ciclo completo: `/pipeline-review-init <novo_RUN_ID>` e repetir lanes se a branch mudou muito.
