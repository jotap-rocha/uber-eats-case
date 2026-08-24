# Memória, dtypes e cópias

> **Purpose:** Reduzir footprint e evitar cópias acidentais.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

Em pipelines tabulares, metade da memória pode ser desperdiçada com `float64`/object onde `float32`/categorical bastam. **Chunked processing** e **generators** mantêm uso estável em ficheiros grandes. Em Pandas, confundir **view** com **copy** produz bugs silenciosos e cópias extras.

## The Pattern

```python
import pandas as pd


def read_in_chunks(path: str, chunksize: int = 100_000):
    for chunk in pd.read_csv(path, chunksize=chunksize, dtype={"id": "Int32"}):
        yield process(chunk)


def downcast_floats(df: pd.DataFrame) -> pd.DataFrame:
    floats = df.select_dtypes(include="float").columns
    return df.astype({c: "float32" for c in floats})
```

Streams de registros: `yield from parser.lines(path)` evita materializar listas gigantes.

## Quick Reference

| Técnica | Efeito |
|---------|--------|
| dtypes menores | Menos RAM, por vezes mais cache-friendly |
| categorias | Strings repetidas → inteiros compactos |
| chunks / lazy | Pico de memória controlado |
| `.copy()` explícito | Quando vai mutar após slice |

## Common Mistakes

### Wrong

```python
subset = df[df.region == "EMEA"]
subset["x"] = 1  # SettingWithCopyWarning; comportamento ambíguo
```

### Correct

```python
subset = df.loc[df.region == "EMEA"].copy()
subset["x"] = 1
```

## Related

- [vectorized-operations](vectorized-operations.md)
- [io-columnar](io-columnar.md)
