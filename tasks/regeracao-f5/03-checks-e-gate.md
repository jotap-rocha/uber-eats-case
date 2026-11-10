# Consultas de invariante e gate de verificação

**Status:** done (retroativo, aguarda aprovação de waiver)  
**Blocked by:** none

**Commit:** `136d2a2`

## What to build

36 consultas `shared/gen/checks/*.sql` (T1 a T16), checks T6c, T17 a T19 em Python e o executor.

## Acceptance criteria

- [x] `ac1` O gate executa T1 a T19 nos três bancos e fecha com 0 linha de violação.

**Waiver proposto:** Executado contra os bancos em 2026-11-10 (47 de 47 verificações); o teste `test_invariants.py` só roda com DSN e pula sem ele. (precisa de aprovação humana explícita)

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
