# Tipificação e contratos de dados

> **Purpose:** Falhar cedo, barato e com mensagens claras nas fronteiras.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

**Type hints** documentam APIs públicas e habilitam `mypy`/`pyright`. Para **dados tabulares**, valide na entrada/saída de cada estágio (arquivo lido, resposta HTTP, tabela entregue) com esquemas — Pandera para DataFrames, pydantic para registros/config — em vez de assumir colunas e dtypes.

## The Pattern

```python
from pydantic import BaseModel, Field


class JobConfig(BaseModel):
    input_uri: str
    output_uri: str
    max_rows: int | None = Field(default=None, ge=1)


def load_config(raw: dict) -> JobConfig:
    return JobConfig.model_validate(raw)
```

```python
import pandera.pandas as pa


schema = pa.DataFrameSchema(
    {
        "id": pa.Column(int, coerce=True),
        "amount": pa.Column(float, pa.Check.ge(0)),
    }
)


def validate_batch(df):
    return schema.validate(df, lazy=True)
```

## Quick Reference

| Fronteira | Ferramenta típica |
|-----------|-------------------|
| Config/env | pydantic |
| DataFrame em pipeline | Pandera (ou equivalente) |
| Funções puras | Tipos + testes |

## Common Mistakes

### Wrong

```python
def run(path):
    df = pd.read_parquet(path)
    return df["amout"].sum()  # typo silencioso ou KeyError tarde
```

### Correct

```python
def run(path: str) -> float:
    df = schema.validate(pd.read_parquet(path))
    return float(df["amount"].sum())
```

## Related

- [testing-pipelines](testing-pipelines.md)
- [../patterns/schema-boundary.md](../patterns/schema-boundary.md)
- [../../pydantic/specs/index.md](../../pydantic/specs/index.md) — KB pydantic (índice em `specs/`)
