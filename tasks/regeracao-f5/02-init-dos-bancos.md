# Init dos bancos a partir do DDL aprovado

**Status:** done (retroativo, aguarda aprovação de waiver)  
**Blocked by:** none

**Commit:** `25822d7`

## What to build

Scripts de init de Postgres (`00..06`), Oracle (`02_create_tables.sh`) e Mongo (`00_replica_set.js`, `01_restaurant_profiles.js`).

## Acceptance criteria

- [x] `ac1` Em banco novo: Postgres com 28 tabelas, timezone `America/Sao_Paulo`, `max_slot_wal_keep_size=4GB`, publicação e role `dbz_ubereats`; Oracle com 3 tabelas, ARCHIVELOG e gatilho de logon ativo; Mongo `PRIMARY` com validador.

**Waiver proposto:** Verificado manualmente nos bancos novos em 2026-11-10 (passo 3 da F5.3); não há teste automatizado sem subir os bancos. (precisa de aprovação humana explícita)

> Task registrada retroativamente em 2026-11-10 ao adotar o workflow do agent-harness. Gate, revisor e número de intervenções não foram medidos na época e ficam sem dado.
