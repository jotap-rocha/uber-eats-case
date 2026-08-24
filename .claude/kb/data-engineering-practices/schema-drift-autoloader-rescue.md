# Pattern — Schema drift com Auto Loader rescue

> **Quando usar:** ingestão de ficheiros (CSV/JSON) com cabeçalhos controlados por sistema externo (SI) que podem evoluir.

## Problema

Colunas novas ou renomeadas na origem causam perda silenciosa de dados ou falha total do pipeline.

## Solução recomendada (Opção B — Databricks)

| Componente | Configuração |
|------------|--------------|
| Schema RAW | **Fixo** — derivado do contrato (`CSV_HEADER_TO_BRONZE` ou equivalente) |
| Auto Loader | `cloudFiles.schemaEvolutionMode = rescue` |
| Colunas extra | JSON em `_rescued_data` (por linha) |
| Split DQ | Linhas com `_rescued_data` → quarentena `schema_rescue` |
| Alerta | Teams pós-run consultando quarentena |
| Bronze principal | **Nunca** contém `_rescued_data` |

## Fluxo

```text
CSV landing → Auto Loader (schema fixo + rescue)
    → staging → split: válido | corrupt | schema_rescue
    → Bronze principal | quarentena
    → Teams (card laranja se drift)
```

## Adoptar coluna nova (runbook)

1. Confirmar com owner de dados (SI/governança)
2. Actualizar `schemas.py` + `medallion_contract.py` + metadados UC
3. Bump contrato + CHANGELOG
4. Deploy bundle
5. **Reenviar CSV com path novo** na landing (Auto Loader não relê path antigo)
6. Quarentena histórica: manter como auditoria (PRD) ou purge selectivo (DSV)

## Referência

Repositório Varonis: `docs/guia-schema-drift-varonis.md`, `schema_drift_rescue.py`.

## Anti-patterns

- Schema inferido sem limite → colunas extra descartadas silenciosamente no `select`
- `expect_or_drop` sem quarentena → perda de dados sem trilha
- Adoptar coluna no código sem reprocessar ficheiros afectados
