# Padrão: escolher paralelismo por perfil de trabalho

> **Purpose:** Evitar threads onde o GIL impede ganho e evitar clusters onde um processo basta.
> **MCP Validated:** 2026-05-06

## When to Use

- Job Python single-node antes de mover para Spark/Dask.
- Serviços que misturam fetch HTTP e CPU local.
- Funções `pool.map` introduzem regressão de memória por pickling.

## Implementation

```python
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def io_bound_tasks(urls: list[str]) -> list[int]:
    def fetch(u: str) -> int:
        ...

    with ThreadPoolExecutor(max_workers=16) as pool:
        return list(pool.map(fetch, urls))


def cpu_bound_tasks(parts: list[list[float]]) -> list[float]:
    def work(chunk: list[float]) -> float:
        return sum(x * x for x in chunk)

    with ProcessPoolExecutor(max_workers=4) as pool:
        return list(pool.map(work, parts))
```

**Check-list rápida:** se o perfil mostra espera em rede/disco → threads/async. Se mostra bytecode Python em loop → processos ou vetorização. Se dados não cabem num nó ou precisa fault tolerance → framework distribuído.

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `max_workers` (threads) | `min(32, os.cpu_count()+4)` | Ajustar a limites do endpoint |
| `max_workers` (processos) | `cpu_count()` | Evitar oversubscription memória |

## Example Usage

```python
urls = [...]
sizes = io_bound_tasks(urls)
chunks = [parse(u) for u in urls]
scores = cpu_bound_tasks(chunks)
```

## See Also

- [../concepts/parallelism-gil.md](../concepts/parallelism-gil.md)
- [../concepts/vectorized-operations.md](../concepts/vectorized-operations.md)
