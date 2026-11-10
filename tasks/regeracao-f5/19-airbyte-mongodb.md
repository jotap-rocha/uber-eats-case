# Airbyte: fonte MongoDB por change stream

**Status:** not started (rascunho a aprovar)  
**Blocked by:** tasks/regeracao-f5/18-tempo-real-e-gate-cdc.md

## What to build

Religar o Airbyte, desativar a conexão antiga com o Postgres e criar a fonte MongoDB (modo Lookup, `directConnection=true`) com destino de conferência.

## Acceptance criteria

- [ ] `ac1` Metadados `_ab_cdc_*` conferidos na primeira sync; F4.6 corrigida se os nomes forem outros.
- [ ] `ac2` Conexão antiga do Airbyte com o Postgres desativada.
