# Parâmetros, cidades e cálculo de dinheiro

**Status:** done (retroativo, evidência coletada em 2026-11-10)  
**Blocked by:** none

**Commit:** `0ab4d66`

## What to build

`shared/gen/parameters.yaml`, `reference/cities.csv` e os módulos `params`, `money` (F5.7) e `geo`.

## Acceptance criteria

- [x] `ac1` Componentes, última parcela, taxa de entrega e reembolso por diferença de acumulados passam nos testes; os parâmetros e as cidades carregam e a menor rota é calculada.
  - Prova: `pytest tests/test_money.py tests/test_params_geo.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
