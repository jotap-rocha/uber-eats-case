# Padrão: fluxo medir → hipótese → validar

> **Purpose:** Transformar profiling em mudanças seguras e mensuráveis.
> **MCP Validated:** 2026-05-06

## When to Use

- Antes de qualquer refatoração de performance afirmada.
- Quando o SLA do job mudou (mais dados, menos janela).
- Depois de mudança de versão de biblioteca ou runtime.

## Implementation

```python
from __future__ import annotations

import json
import time
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass(frozen=True)
class Baseline:
    job_name: str
    duration_s: float
    rows: int
    notes: str


def timed_run(job_name: str, rows: int, fn, *args, **kwargs) -> Baseline:
    t0 = time.perf_counter()
    fn(*args, **kwargs)
    return Baseline(
        job_name=job_name,
        duration_s=time.perf_counter() - t0,
        rows=rows,
        notes="representative subset",
    )


def persist(b: Baseline, path: Path) -> None:
    path.write_text(json.dumps(asdict(b), indent=2))
```

1. Correr job com **subset representativo** (volume e cardinalidade semelhantes ao pico).
2. Guardar baseline (`duration`, linhas, versões em `notes` ou ficheiro sibling).
3. `cProfile` → identificar top funções → `line_profiler` na suspeita.
4. Uma hipótese por vez (ex.: remover `apply`, trocar dtype, empurrar filtro para leitura).
5. Comparar nova medição; regressão → reverter ou investigar variância (I/O compartilhado).

## Configuration

| Campo | Default | Description |
|-------|---------|-------------|
| `subset_fraction` | `0.05` | Fração de dados com distribuição fiel |
| `repeat` | `3` | Repetições para média em benchmarks micro |

## Example Usage

```python
from pathlib import Path


def job_once():
    ...


if __name__ == "__main__":
    b = timed_run("daily_curated", rows=1_000_000, fn=job_once)
    persist(b, Path("reports/baseline.json"))
```

## See Also

- [../concepts/profiling-baseline.md](../concepts/profiling-baseline.md)
- [../concepts/io-columnar.md](../concepts/io-columnar.md)
