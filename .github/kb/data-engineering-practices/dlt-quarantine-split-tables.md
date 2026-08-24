# Pattern — Quarentena explícita (split valid / quarantine)

> **Quando usar:** qualquer pipeline DLT/Spark onde registos inválidos não devem entrar na camada principal.

## Política

| Tipo inválido | Destino | Regra exemplo |
|---------------|---------|---------------|
| Parse corrupt | `{layer}.*_quarentena` | `_corrupt_record` preenchido |
| Schema drift | `{layer}.*_quarentena` | `_rescued_data` preenchido |
| DQ negócio | `{layer}.*_quarentena` | regras Silver (path, flags, bounds) |

**Prioridade split:** corrupt > schema_rescue > válido.

## Colunas audit obrigatórias

- `_dq_violated_rules` — nome(s) da regra falhada (CSV)
- `_quarantined_at` — timestamp UTC

## Implementação

```python
def split_valid_and_quarantine(df) -> tuple[DataFrame, DataFrame]:
    valid = df.filter(passes_all_rules).select(*MAIN_COLUMNS)
    quarantine = df.filter(~passes_all_rules).withColumn(
        "_quarantined_at", F.current_timestamp()
    ).withColumn("_dq_violated_rules", violated_rules_expr)
    return valid, quarantine
```

## Tabelas UC

- `{catalog}.bronze.{leaf}_quarentena`
- `{catalog}.silver.{leaf}_quarentena`

Quarentena é **append** (trilha auditoria) — re-run pode duplicar eventos (aceite operacional).

## Runbook pós-correção

Linhas em quarentena **não migram** automaticamente. Reprocessar origem com path novo; quarentena antiga pode permanecer como histórico.

## Referência

Varonis: `dlt_bronze_expectations.py`, `dlt_silver_expectations.py`.
