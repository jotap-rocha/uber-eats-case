# Testes em pipelines de dados

> **Purpose:** Confiança sem rodar o lake inteiro a cada commit.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

**Transformações puras** são baratas de testar em unitários com dados sintéticos pequenos. **Invariantes** amplas (ordenção preservada, somas conservadas) beneficiam de testes de propriedade pontuais. **Smoke tests** com amostra representativa capturam schemas reais; **benchmarks leves** podem alertar regressões de performance.

## The Pattern

```python
import pandas as pd
import pytest


def aggregate_sales(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("sku", as_index=False)["amount"].sum()


def test_aggregate_sales_preserves_total():
    df = pd.DataFrame({"sku": ["a", "a", "b"], "amount": [1.0, 2.0, 3.0]})
    out = aggregate_sales(df)
    assert out["amount"].sum() == pytest.approx(df["amount"].sum())
```

Para Hypothesis: gerar `DataFrame` mínimos respeitando schema esperado e verificar propriedades globais.

## Quick Reference

| Camada | Teste |
|--------|--------|
| Função pura | `pytest` + fixtures |
| Contrato de dados | Pandera no CI com fixture Parquet |
| Job longo | Smoke + métrica de tempo/memória em runner dedicado |

## Common Mistakes

### Wrong

```python
# Depender só de dados de produção copiados para dev (instável, PII)
def test_real():
    df = pd.read_parquet("/mnt/prod/sensitive.parquet")
```

### Correct

```python
def test_schema_contract(tmp_path):
    df = synthetic_fixture()
    df.to_parquet(tmp_path / "in.parquet")
    run_stage(tmp_path / "in.parquet", tmp_path / "out.parquet")
```

## Related

- [typing-contracts](typing-contracts.md)
- [profiling-baseline](profiling-baseline.md)
- [../patterns/schema-boundary.md](../patterns/schema-boundary.md)
