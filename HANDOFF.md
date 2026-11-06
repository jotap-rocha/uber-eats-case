# Handoff — uber-eats-case

> Gerado pelo install-harness em 2026-10-16. Atualize a cada handoff de sessão.

## Estado atual

Modelagem de dados: regras (RN-01 a RN-42), conceitual, **modelo logico L0 a L4** (PR #17) e **modelo fisico F0 a F5** (PR #18, 2026-11-04) aprovados e mesclados na `main`, em `shared/docs/modelagem/`. ADRs 006 a 012 aceitas (009 e 011 com adendos). **Implementacao da F5.2 em andamento na branch `feat/regeracao`** (5 de 6 blocos feitos, sem push). Bancos atuais intocados: Oracle atual ainda tratado como producao; gerador nao religado.

## Proximos passos

1. **Implementar o simulador (bloco 5 da F5.2)**: o unico bloco que falta, e o maior. Brief abaixo.
2. **Push e PR** da `feat/regeracao` quando o simulador estiver verde (titulo sugerido: `feat(regeracao): simulador, seeds, checks e init da F5.2`).
3. **Executar a regeracao** pela F5.3 (passos 0 a 12), com confirmacao em cada passo destrutivo. Antes: adicionar ao `shared/gen/.env` `POSTGRES_DEBEZIUM_PASSWORD`, `TRACKING_SALT_ORDER` e `TRACKING_SALT_PAYMENT`; desativar a conexao antiga do Airbyte com o Postgres; o usuario renova a licenca do ShadowTraffic antes (so conferir no passo 0).
4. **Pipeline** (`shared/pipeline/`, hoje no modelo antigo): so depois da regeracao. A Bronze segue o contrato da F4.6.

## O que ja esta na `feat/regeracao`

| Bloco | Commit | Conteudo |
|---|---|---|
| 1 | `0ab4d66` | `shared/gen/parameters.yaml`, `reference/cities.csv`, `simulator/params.py`, `money.py` (F5.7: componentes, ultima parcela, taxa de entrega, reembolso por diferenca de acumulados), `geo.py` (menor rota) |
| 2 | `25822d7` | Init dos bancos gerado do DDL aprovado: `shared/sql/postgres/00..06` (inclui `06_cdc.sh`), `shared/sql/oracle/02_create_tables.sh`, `shared/mongo/init/00_replica_set.js` e `01_restaurant_profiles.js`; antigos em `legacy/`; `.gitattributes` (LF nos `.sh`); Oracle montado em `initdb.d` |
| 3 | `136d2a2` | `shared/gen/checks/*.sql` (36 consultas, T1 a T16), `simulator/checks.py` (executor e T6c, T17, T18, T19 em Python), `tests/test_invariants.py` (gate com `UBEREATS_CHECKS_DSN`) |
| 4 | `8a7e42a` | Seeds: `reference/catalog.yaml`, `simulator/seed/` (`python -m simulator.seed {cities,catalog,profiles,all}`, idempotente), `simulator/gate.py` (`python -m simulator.gate`, so leitura, T1 a T19 nos tres bancos), `simulator/db.py` |
| 6 | (a commitar) | Template do ShadowTraffic so com `customers`, `drivers` (Oracle) e `restaurants` (Postgres), sem MinIO; cidades injetadas do CSV pelo `setup-configs.ps1`; `toggle-shadowtraffic.ps1` com `startingFrom`/`maxEvents` dos tres cadastros; `tests/test_template.py`; `docker-compose.yml` da F5.2 (TZ, `max_slot_wal_keep_size`, Debezium 3.7 no `quay.io`, replica set e healthcheck do Mongo, `gen-unified` sem MinIO) |

Gate local: `cd shared/gen && .venv/Scripts/python -m pytest -q` (49 passam, 1 pulado sem DSN), `ruff check .`, `mypy simulator`. O venv `shared/gen/.venv` e local (fora do git): `python -m venv shared/gen/.venv` e `pip install -r shared/gen/requirements.txt`.

**Achados da implementacao (ja registrados no fisico e nas ADRs):** `--oplogSize` (nao `--oplogSizeMB`); o init do Mongo sem autenticacao roda em replica set nao iniciado, entao o `rs.initiate` foi para o init com membro `localhost:27017`; healthcheck do Mongo com `quit(...)`; archivelog do Oracle fica fora do volume (`$ORACLE_HOME/dbs/arch`); no Windows usar `127.0.0.1`, nao `localhost` (IPv6 pendura a conexao). O template foi validado gravando de verdade num Oracle e num Postgres descartaveis.

## Brief do simulador (bloco 5), para a proxima sessao

Ler antes: `CLAUDE.md`, este arquivo, `shared/docs/modelagem/04-modelo-fisico.md` (F5.5 a F5.9, F1 para o DDL das 22 tabelas do simulador), `03-modelo-logico.md` (L1b vocabulario de status e transicoes, L2 reembolsos por origem, L3 pos-entrega, L4 parametros), `01-regras-de-negocio.md` (RN-01 a RN-42, tabela de transicoes), ADRs 007, 008 e 009. Reaproveitar `simulator/money.py`, `geo.py`, `params.py`, `db.py`, `checks.py` e o gate.

**Escopo:** pacote em `shared/gen/simulator/` com (a) `clock` injetado (historico de `backfill_days` e depois tempo real, F5.6); (b) um processo, um escritor, fila de acoes por instante (F5.5); (c) compra numa transacao (ADR 009: checkout, tentativas, pedido, atendimentos, itens, entrega, linha 1 das duas transicoes, pagamento, componentes, recibo), codigo de rastreio com os sais do `.env` (F0.3); (d) ciclo do atendimento, entrega, turno e atribuicao, estoque (baixa no preparo, reposicao fora das janelas), repasses, gorjeta, avaliacoes, incidentes e reembolsos; (e) leitura de `customers`/`drivers` no Oracle e das janelas no Mongo com cache (`profile_cache_refresh_min`); (f) CLI `python -m simulator run`. Testes: unidade de cada regra (inclusive o congelamento do `promised_at`, T7) e um teste de integracao que roda um historico curto num Postgres descartavel e passa no `python -m simulator.gate`.

**Restricoes:** nao tocar nos conteineres e volumes atuais (`oracle-ubereats`, `postgres-ubereats`, `mongo-ubereats`, `redpanda`, `kafka-connect`, `minio-ubereats`) antes da execucao combinada da F5.3. Nao religar o ShadowTraffic do projeto (rodar o ShadowTraffic em conteiner descartavel, contra bancos descartaveis, ja foi feito para validar o template). Testes so em conteineres descartaveis (`f5-*`, sem volume nomeado, `docker rm -v` no fim; portas publicadas em `127.0.0.1:15xxx`, as 58xxx sao reservadas no Windows). Nada de `DROP`/`TRUNCATE`/`down -v`/`volume rm` sem confirmacao. Nao imprimir registros crus de pessoas. Proximo ADR livre: 013.

**Pendencias registradas para depois:** Fase 1 refaz os templates de `config/azure/debezium/` no desenho da ADR 012; `HdfsSinkConnector` no Kafka Connect 4.x; consumidores antigos (`azure/sql/synapse_copy_merge.sql`, `shared/pipeline/bronze/*`) ainda nos topicos do modelo antigo; skill de operacao do simulador; KB do ShadowTraffic (`.claude/kb/shadowtraffic/specs/generator-targets-uber-eats.yaml`) ainda descreve os geradores antigos; `RESTAURANT_COUNT` pode sair do `.env`.
