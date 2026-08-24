# Paralelismo e GIL

> **Purpose:** Escolher o modelo certo para CPU-bound vs I/O-bound.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

O **GIL** limita paralelismo real de **threads** em código Python CPU-intensivo num processo. Para **I/O** (rede, disco), threads ou `asyncio` ajudam porque liberam o GIL à espera. Para **CPU** em Python puro, use **vários processos** ou delegue a bibliotecas nativas (NumPy em BLAS, Polars, Spark).

## The Pattern

```python
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fetch_many(urls: list[str]) -> list[bytes]:
    with ThreadPoolExecutor(max_workers=8) as ex:
        return list(ex.map(http_get, urls))


def cpu_heavy_chunks(chunks: list[list[float]]) -> list[float]:
    with ProcessPoolExecutor(max_workers=4) as ex:
        return list(ex.map(sum_squares, chunks))
```

Para dados maiores que memória de um nó: **Dask**, **Ray** ou **Spark** — paralelismo + particionamento de dados.

## Quick Reference

| Perfil | Modelo |
|--------|--------|
| Muitas chamadas HTTP | Threads / asyncio |
| Transformação CPU Python | Processos ou JIT (Numba) pontual |
| TB particionados | Framework distribuído |

## Common Mistakes

### Wrong

```python
# Esperar speedup linear com threads em parsing CPU-heavy em Python puro
from threading import Thread
for chunk in chunks:
    Thread(target=parse_py, args=(chunk,)).start()
```

### Correct

```python
# ProcessPool ou vetorizar / mover para motor colunar
with ProcessPoolExecutor() as ex:
    ex.map(parse_py, chunks)
```

## Related

- [vectorized-operations](vectorized-operations.md)
- [../patterns/parallelism-choice.md](../patterns/parallelism-choice.md)
