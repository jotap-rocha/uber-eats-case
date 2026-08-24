# Pattern — Cards Teams para schema drift (formato conciso)

> **Escopo:** schema drift / schema_rescue. **Formato geral de todos os cards:** [teams-card-format.md](./teams-card-format.md).

## Formato canónico (2 cards)

### Card 1 — Conclusão (verde)

**Título:** `Varonis ingestão — concluída com sucesso`

```text
✅ Ingestão concluída

`dsv` · `varonis` · job bronze_ingest_varonis · DLT SUCCESS

⚠️ Schema drift detectado — detalhes no card laranja enviado nesta execução.
```

- **Não** repetir colunas, quarentena nem probe landing.
- Se **sem** drift: `Sem schema drift na quarentena (lookback recente).`

### Card 2 — Schema drift (laranja)

**Título:** `Varonis — schema drift (N col. · M quarentena)`

```text
⚠️ Schema drift — export fora do contrato SI

N coluna(s) extra · M linhas em quarentena · `dsv` / `varonis`

Colunas novas: `Col1`, `Col2` (+2)
Possível rename (ausentes): `Stale (direct)` (+1)
Exemplos: `teste.csv` (+3 ficheiros)

Próximo passo
1. Confirmar com SI se a alteração é intencional
2. Sim → actualizar contrato + deploy + reenviar CSV (path novo)
3. Não → corrigir export na landing
```

## Regras específicas drift

| Regra | Detalhe |
|-------|---------|
| **Separar cards** | Sucesso ≠ diagnóstico drift |
| **Limite colunas** | Máx. 4 + `(+N)` |
| **Sem contrato completo** | Não listar 11+ cabeçalhos SI |
| **`schema_drift_card_sent`** | Card verde referencia laranja — não duplica |

## Código

- `build_schema_drift_message()`, `build_ingest_completion_message()`
- `SchemaDriftContext`, `IngestCompletionContext.schema_drift_card_sent`
