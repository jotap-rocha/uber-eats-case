# Simulador: compra, ciclo do atendimento, frota e pós-entrega

**Status:** done (retroativo, aguarda aprovação de waiver)  
**Blocked by:** tasks/regeracao-f5/08-simulador-referencia-escritas.md

**Commit:** `81ef6f6`

## What to build

Módulos `purchase`, `kitchen`, `fleet`, `aftersales`, `engine` e o CLI `python -m simulator run`.

## Acceptance criteria

- [x] `ac1` Histórico curto num Postgres descartável passa T1 a T16 e T6c com 0 violação, e a mesma semente dá o mesmo resultado.

**Waiver proposto:** Provado em 2 dias de histórico (parada e retomada) e em 3 dias ponta a ponta com gate 47/47; `test_engine_db.py` só roda com DSN. (precisa de aprovação humana explícita)

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
