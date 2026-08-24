# I/O colunar e particionamento

> **Purpose:** Tirar partido de formatos analíticos e reduzir scans repetidos.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

**Parquet** (e formatos colunares semelhantes) permite ler só colunas e row groups necessários, comprimir por coluna e particionar por chaves de filtro frequentes. Reler o mesmo dataset várias vezes no mesmo job sem cache planeada é anti-pattern comum.

## The Pattern

```python
import polars as pl


lf = pl.scan_parquet("s3://bucket/events/year=*/month=*/*.parquet").select(
    ["event_id", "ts", "metric"]
)
df = lf.filter(pl.col("ts") >= pl.lit("2026-01-01")).collect(streaming=True)
```

Particionar por `year/month` ou por `tenant_id` quando queries filtram assim. Comprimir (`zstd`, `snappy`) — medir CPU vs rede em dados de produção.

## Quick Reference

| Necessidade | Abordagem |
|-------------|------------|
| Menos colunas lidas | `.select` antes de materializar |
| Predicados | `filter` pushdown quando suportado |
| Vários consumidores no mesmo job | Escrita intermedia particionada ou cache explícito |

## Common Mistakes

### Wrong

```python
# CSV gigante relido várias vezes no mesmo processo
for metric in metrics:
    pd.read_csv("huge.csv")[metric].describe()
```

### Correct

```python
df = pd.read_csv("huge.csv", usecols=["id"] + metrics)
for metric in metrics:
    df[metric].describe()
```

## Related

- [profiling-baseline](profiling-baseline.md)
- [memory-dtypes](memory-dtypes.md)
