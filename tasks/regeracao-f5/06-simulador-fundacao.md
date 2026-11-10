# Simulador: fundação (rastreio, relógio, agenda, parâmetros)

**Status:** done (retroativo, evidência coletada em 2026-11-10)  
**Blocked by:** none

**Commit:** `e8c8508`

## What to build

Módulos `tracking`, `clock`, `agenda` e `sim_params`.

## Acceptance criteria

- [x] `ac1` Código de rastreio, relógio injetado e agenda por instante se comportam como especificado.
  - Prova: `pytest tests/test_foundation.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
