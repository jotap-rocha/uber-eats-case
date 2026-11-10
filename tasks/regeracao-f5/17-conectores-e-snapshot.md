# Conectores Debezium e snapshot inicial (ADR 013)

**Status:** not started (aprovada em 2026-11-10)  
**Blocked by:** tasks/regeracao-f5/16-gate-do-banco-pos-historico.md

## What to build

Subir Redpanda e Kafka Connect (versão mais nova compatível, confirmar com o usuário), registrar os conectores Postgres e Oracle com `snapshot.mode=initial`.

## Acceptance criteria

- [ ] `ac1` Os dois conectores `RUNNING`, snapshot concluído e slot `dbz_ubereats` ativo.
- [ ] `ac2` Eventos `r` nos tópicos `postgres.ubereats.*` e `oracle.UBEREATS.*`.
- [ ] `ac3` Tamanho de `dbs/arch` do Oracle conferido antes do registro.
