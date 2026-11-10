# Seeds de cidades, catálogo e perfis

**Status:** done (retroativo, evidência coletada em 2026-11-10)  
**Blocked by:** none

**Commit:** `8a7e42a`

## What to build

`python -m simulator.seed {cities,catalog,profiles,all}`, idempotente, e `simulator.gate`.

## Acceptance criteria

- [x] `ac1` Os seeds geram cidades, catálogo e perfis coerentes e são idempotentes.
  - Prova: `pytest tests/test_seed.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
