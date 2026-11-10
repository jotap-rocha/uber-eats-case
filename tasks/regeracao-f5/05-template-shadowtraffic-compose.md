# Template do ShadowTraffic e compose da F5.2

**Status:** done (retroativo, evidência coletada em 2026-11-10)  
**Blocked by:** none

**Commit:** `8b28567`

## What to build

Template só com `customers`, `drivers` e `restaurants`, cidades injetadas do CSV e `docker-compose.yml` da F5.2.

## Acceptance criteria

- [x] `ac1` O template do ShadowTraffic é válido, sem MinIO, com os três cadastros e as cidades injetadas.
  - Prova: `pytest tests/test_template.py` em `shared/gen`

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
