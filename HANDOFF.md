# Handoff — uber-eats-case

> Gerado pelo install-harness em 2026-10-16. Atualize a cada handoff de sessão.

## Estado atual

Modelagem de dados: regras (RN-01 a RN-42), conceitual e **modelo logico L0 a L4 aprovados e mesclados na `main`** (PR #17, 2026-11-03), em `shared/docs/modelagem/`. **Modelo fisico F0 a F5 aprovado** na branch `feat/modelo-fisico`. ADRs 006 a 012 aceitas. Documentacao alinhada (links, avisos de obsoleto, roadmap 2.0). Oracle atual ainda tratado como producao; gerador nao religado. Branch de trabalho: `feat/modelo-fisico`.

## Proximos passos

1. **Modelo fisico** (`shared/docs/modelagem/04-modelo-fisico.md`): **F0 a F5 aprovadas** (F0 2026-11-03; F1 a F5 2026-11-04). ADRs 009 (com dois adendos), 010, 011 e 012. **F5** (plano da regeracao): recriar os volumes dos 3 bancos, do Redpanda e do `kafka-connect` (confirmacao por volume); scripts de init como fonte unica (Oracle passa de `container-entrypoint-startdb.d`, que roda a cada start, para `initdb.d`); ShadowTraffic so com `customers`, `drivers` e `restaurants`; seed Python com cidades (CSV unico), catalogo, estoque inicial e perfis; simulador com historico simulado de 30 dias e depois tempo real; dinheiro em `ROUND_HALF_UP` com taxa de entrega base + R$/km; consultas T1 a T16 validadas num Postgres descartavel, T17 a T19 em Python. `scripts/ingestion/register-postgres-connector.ps1` criado (nada registrado).
2. **Implementar a F5.2** numa branch propria (`feat/regeracao` ou similar): pacote `shared/gen/simulator/` (seeds, `money`, `tracking`, `clock`, laco), `shared/gen/checks/` + `shared/gen/tests/test_invariants.py` (consultas da F5.9), `shared/gen/parameters.yaml`, `shared/gen/reference/cities.csv`, init novo em `shared/sql/postgres/`, `shared/sql/oracle/` e `shared/mongo/init/` (antigos para `legacy/`), `docker-compose.yml` (F5.2) e template do ShadowTraffic reduzido (skill `shadowtraffic-adicionar-generator-seguro`). `pytest` e `ruff` verdes antes de tocar em conteiner.
3. **Executar a regeracao** pela F5.3 (passos 0 a 12), com confirmacao em cada passo destrutivo. Antes: renovar a licenca do ShadowTraffic (vence por volta de 2026-11-07), adicionar ao `.env` `POSTGRES_DEBEZIUM_PASSWORD`, `TRACKING_SALT_ORDER` e `TRACKING_SALT_PAYMENT`, desativar a conexao antiga do Airbyte com o Postgres.
4. **Pipeline** (`shared/pipeline/`, hoje no modelo antigo): so depois da regeracao. A Bronze segue o contrato da F4.6 (envelope Debezium, `CAST` das chaves Oracle, `cdc_sequence` `DECIMAL(20,0)`, `cdc_tx_id`).

## Brief da implementacao da F5.2, para a proxima sessao

Ler antes: `CLAUDE.md`, este arquivo, `shared/docs/modelagem/04-modelo-fisico.md` (F5 inteira; F1 a F4 para o DDL e o CDC), `docs/adr/009` (os dois adendos), `007`, `011`, e as regras de dinheiro RN-09, RN-19 a RN-22, RN-29 e RN-33 em `shared/docs/modelagem/01-regras-de-negocio.md`.

**Ordem sugerida:** (1) `parameters.yaml`, `cities.csv` e o modulo `money` com o exemplo da F5.7 como teste; (2) init dos bancos a partir do DDL da F1, F2 e F3, validado em conteineres descartaveis (sem volume nomeado, nomes `f5-*`, `docker rm -v` no fim; portas 58xxx reservadas no Windows, usar `docker exec`); (3) `shared/gen/checks/` com as consultas da F5.9 e o `test_invariants.py`; (4) seeds; (5) simulador (relogio injetado, um processo e um escritor, compra numa transacao); (6) compose e template do ShadowTraffic. Cada bloco com `pytest`/`ruff` verdes.

**Restricoes:** nao tocar nos conteineres e volumes atuais (`oracle-ubereats`, `postgres-ubereats`, `mongo-ubereats`, `redpanda`, `kafka-connect`, `minio-ubereats`) antes da execucao combinada da F5.3. Nao religar o ShadowTraffic. Nada de `DROP`/`TRUNCATE`/`down -v`/`volume rm` sem confirmacao. Nao imprimir registros crus de pessoas. Proximo ADR livre: 013.

**Pendencias registradas para depois:** Fase 1 refaz os templates de `config/azure/debezium/` no desenho da ADR 012; `HdfsSinkConnector` no Kafka Connect 4.x; consumidores antigos (`azure/sql/synapse_copy_merge.sql`, `shared/pipeline/bronze/*`) ainda nos topicos do modelo antigo; skill de operacao do simulador.
