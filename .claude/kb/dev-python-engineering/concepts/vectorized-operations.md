# Operações vetorizadas

> **Purpose:** Evitar loops Python sobre grandes volumes tabulares.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

NumPy, Pandas e Polars aplicam operações em **blocos** (C/Rust/LLVM), amortizando o custo do interpretador. Loops `for` ou `DataFrame.apply(axis=1)` em datasets grandes convertem milhões de chamadas Python — típico anti-pattern de performance.

## The Pattern

```python
import pandas as pd


def add_tax(amount: pd.Series, rate: pd.Series) -> pd.Series:
    return (amount * (1 + rate)).astype("float32")


def enrich(df: pd.DataFrame) -> pd.DataFrame:
    return df.assign(total=add_tax(df["amount"], df["vat_rate"]))
```

Em Polars: preferir expressões lazy (`scan_parquet` → `with_columns`). Em Spark: operações colunares e joins broadcast quando aplicável.

## Quick Reference

| API | Evitar | Preferir |
|-----|--------|----------|
| Pandas | `iterrows`, `apply(axis=1)` genérico | `assign`, operações vetoriais, `merge` com chaves índice |
| NumPy | loop Python sobre elementos | broadcasting, `einsum` quando útil |
| Polars | colecionar cedo demais | lazy + `sink_parquet` |

## Common Mistakes

### Wrong

```python
def score_rows(df):
    out = []
    for _, row in df.iterrows():
        out.append(row["a"] * row["b"])
    df["score"] = out
```

### Correct

```python
df["score"] = df["a"] * df["b"]
```

## Related

- [memory-dtypes](memory-dtypes.md)
- [parallelism-gil](parallelism-gil.md)
- [../patterns/parallelism-choice.md](../patterns/parallelism-choice.md)
