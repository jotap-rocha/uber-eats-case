# Simulador: opção --days e script de execução

**Status:** done  
**Blocked by:** tasks/regeracao-f5/09-simulador-compra-ciclo-posentrega.md

## What to build

Opção `--days` no CLI e `scripts/simulator/run-simulator.ps1` (histórico até agora, `-Live`, `-Status`).

## Acceptance criteria

- [x] `ac1` `default_start` usa `--days` quando informado e `clock.backfill_days` caso contrário.
  - Prova: `pytest tests/test_default_start.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
