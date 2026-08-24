# Padrão: pipeline em estágios com observabilidade

> **Purpose:** Operações claras, reruns baratos e métricas acionáveis.
> **MCP Validated:** 2026-05-06

## When to Use

- DAGs Airflow ou jobs cron com múltiplas transformações.
- Equipes que precisam isolar falhas sem reler terabytes.
- Requisitos de auditoria (contagens in/out por estágio).

## Implementation

```python
from __future__ import annotations

import logging
import time
import uuid
from collections.abc import Callable
from typing import TypeVar

import pandas as pd


T = TypeVar("T")
logger = logging.getLogger(__name__)


def stage(
    name: str,
    run_id: str,
    fn: Callable[..., T],
    *args,
    **kwargs,
) -> T:
    start = time.perf_counter()
    logger.info("stage_start", extra={"stage": name, "run_id": run_id})
    try:
        out = fn(*args, **kwargs)
    except Exception:
        logger.exception("stage_fail", extra={"stage": name, "run_id": run_id})
        raise
    logger.info(
        "stage_end",
        extra={
            "stage": name,
            "run_id": run_id,
            "seconds": round(time.perf_counter() - start, 3),
        },
    )
    return out


def build(run_id: str | None = None) -> None:
    rid = run_id or str(uuid.uuid4())
    raw = stage("ingest", rid, pd.read_parquet, "landing/x.parquet")
    curated = stage("transform", rid, lambda d: d[d["amount"] > 0], raw)
    stage("deliver", rid, curated.to_parquet, f"curated/x/run_id={rid}/part.parquet")
```

**Idempotência:** usar `run_id` na pasta de saída ou `MERGE` deduplicado por chave natural. **Retomada:** estágios gravam artefacto intermédio consultável antes do próximo operador.

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `run_id` | UUID | Correlação entre logs e paths |
| log format | JSON | Ideal para agregação (ELK/Datadog) |

## Example Usage

```python
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    build(run_id="2026-05-06T02")
```

## See Also

- [../concepts/pipeline-architecture.md](../concepts/pipeline-architecture.md)
- [../concepts/io-columnar.md](../concepts/io-columnar.md)
