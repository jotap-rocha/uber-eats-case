# Simulador: cache de referência e escritas comuns

**Status:** done (retroativo, evidência coletada em 2026-11-10)  
**Blocked by:** tasks/regeracao-f5/07-simulador-regras-reembolsos.md

**Commit:** `c80c3f1`

## What to build

Módulos `reference` e `store`: leitura de cadastros (Oracle), catálogo (Postgres) e janelas (Mongo), e escritas comuns.

## Acceptance criteria

- [x] `ac1` O cache de referência lê as três fontes e respeita o refresh configurado.
  - Prova: `pytest tests/test_reference.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
