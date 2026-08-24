# Padrão: contrato de schema na fronteira

> **Purpose:** Falhas baratas e mensagens claras entre equipas e estágios.
> **MCP Validated:** 2026-05-06

## When to Use

- Hand-offs entre ingestão bruta e camada curated.
- APIs internas que devolvem `DataFrame` ou lista de dicts.
- Jobs que escrevem para equipas downstream sem SLA formal.

## Implementation

```python
from __future__ import annotations

import pandera.pandas as pa
import pandas as pd


RAW_SCHEMA = pa.DataFrameSchema(
    {
        "event_id": pa.Column(str),
        "payload": pa.Column(str),
    },
    strict=True,
)

CURATED_SCHEMA = pa.DataFrameSchema(
    {
        "event_id": pa.Column(str),
        "amount": pa.Column(float, pa.Check.ge(0)),
    },
    strict=True,
)


def ingest_raw(path: str) -> pd.DataFrame:
    df = pd.read_parquet(path)
    return RAW_SCHEMA.validate(df, lazy=True)


def curate(df: pd.DataFrame) -> pd.DataFrame:
    out = (
        df.assign(amount=lambda d: d["payload"].map(parse_amount))
        .drop(columns=["payload"])
    )
    return CURATED_SCHEMA.validate(out, lazy=True)
```

Combine com pydantic para **camada de config** e nomes de partições — não misturar validação de ficheiro com validação de env.

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `lazy` | `True` | Pandera acumula erros por coluna |
| `strict` | contexto | `True` bloqueia colunas extra |

## Example Usage

```python
raw = ingest_raw("landing/events/run_id=2026-05-06/part.parquet")
clean = curate(raw)
clean.to_parquet("curated/events/run_id=2026-05-06/part.parquet")
```

## See Also

- [../concepts/typing-contracts.md](../concepts/typing-contracts.md)
- [../concepts/testing-pipelines.md](../concepts/testing-pipelines.md)
