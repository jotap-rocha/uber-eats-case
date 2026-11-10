# Simulador: regras de estado, prazos e reembolsos

**Status:** done (retroativo, evidência coletada em 2026-11-10)  
**Blocked by:** tasks/regeracao-f5/06-simulador-fundacao.md

**Commit:** `f2cc486`

## What to build

Módulos `rules` e `refunds`: transições de status, `promised_at` congelado e reembolsos por origem.

## Acceptance criteria

- [x] `ac1` Transições, prazos e reembolsos seguem as regras RN e as origens da L2.
  - Prova: `pytest tests/test_rules.py tests/test_refunds.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
