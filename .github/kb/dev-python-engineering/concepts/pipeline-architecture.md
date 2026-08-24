# Arquitetura de pipelines

> **Purpose:** Separação clara, observabilidade e operações seguras.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

Dividir em **ingestão → transformação → entrega** com interfaces estáveis entre estágios facilita testes e reruns. **Logging estruturado** (nível, job_id, path, contagens) e **métricas** (linhas in/out, duração por estágio) permitem correlacionar com SLAs de negócio. **Idempotência** e **checkpoints** reduzem custo de falhas.

## The Pattern

```python
import logging
import time
from dataclasses import dataclass


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class StageResult:
    rows_in: int
    rows_out: int
    seconds: float


def run_stage(name: str, fn, *args, **kwargs) -> StageResult:
    t0 = time.perf_counter()
    out = fn(*args, **kwargs)
    elapsed = time.perf_counter() - t0
    logger.info(
        "stage_done",
        extra={"stage": name, "seconds": round(elapsed, 3), "rows_out": len(out)},
    )
    return StageResult(rows_in=-1, rows_out=len(out), seconds=elapsed)
```

Escrita para destinos finais: preferir **merge idempotente** ou partições versionadas (`run_id`) quando o sink permite.

## Quick Reference

| Preocupação | Prática |
|-------------|---------|
| Falha a meio | Escreve partições temporárias + `rename` atómico quando possível |
| Reprocessamento | Entrada versionada ou watermark explícito |
| Debug | Correlação `run_id` em todos os logs |

## Common Mistakes

### Wrong

```python
# Um único script de 2k linhas sem fronteiras nem métricas
def main():
    df = pd.read_csv("in.csv")
    ...  # dezenas de mutações implícitas
    df.to_parquet("out.parquet")
```

### Correct

```python
def main():
    raw = ingest()
    curated = transform(raw)
    deliver(curated)
```

## Related

- [io-columnar](io-columnar.md)
- [../patterns/staged-pipeline-observability.md](../patterns/staged-pipeline-observability.md)
