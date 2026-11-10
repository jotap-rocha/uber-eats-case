# Handoff — uber-eats-case

> Gerado pelo install-harness em 2026-10-16. Atualize a cada handoff de sessão.

## Estado atual

Modelagem de dados: regras (RN-01 a RN-42), conceitual, **modelo logico L0 a L4** (PR #17) e **modelo fisico F0 a F5** (PR #18, 2026-11-04) aprovados e mesclados na `main`, em `shared/docs/modelagem/`. ADRs 006 a 012 aceitas (009 e 011 com adendos). **Implementacao da F5.2 na branch `feat/regeracao`** (simulador implementado e provado ponta a ponta nos tres bancos descartaveis em 2026-11-10, `python -m simulator.gate` com 47 de 47 verificacoes em 0 linha; sem push). Bancos atuais intocados: Oracle atual ainda tratado como producao; gerador nao religado.

## Proximos passos

1. ~~Fechar o bloco 5 (parte 5)~~ **Feito** em 2026-11-10: prova ponta a ponta, gate verde, documentacao no fisico (F5.8) e no `CONTEXT.md`, contêineres `f5-*` removidos. Detalhes em "Parte 5 do simulador" abaixo.
2. ~~Push e PR~~ **Feito**: PR #19 mesclado.
3. **Regeracao pela F5.3 em andamento (2026-11-10).** Ordem pela [ADR 013](docs/adr/013-snapshot-inicial-aceito-na-regeracao.md): 0, 1, 2, 3, 6, 7, 8, 10 (so historico), 11 (parte do banco), 4, 5, 10 (tempo real), 11 (parte do CDC), 9, 12. **Feitos:** passos 0 a 3 (contêineres e volumes antigos removidos com confirmacao; Postgres, Oracle e Mongo novos de pe e validados; sais e senha do Debezium no `.env`). Passos 6 a 8 tambem feitos: cidades (5 em cada banco), ShadowTraffic (250 restaurantes, 20.000 clientes, 1.500 motoristas), catalogo e perfis (2.850 produtos, 3.870 itens de estoque, 250 perfis), gate da carga 47/47 com 0 linha. O `gen-unified` antigo do projeto `uber-eats-case` foi removido (MinIO antigo mantido, ADR 010). **Proximo:** passo 10, so o historico (30 dias, ~2 h), sem conectores. Redpanda e Kafka Connect **nao sobem ainda** (memoria da maquina; so no passo 4). Pendente: desativar a conexao antiga do Airbyte com o Postgres (Airbyte parado de proposito, a pedido do usuario).
4. **Pipeline** (`shared/pipeline/`, hoje no modelo antigo): so depois da regeracao. A Bronze segue o contrato da F4.6.

## Workflow do agent-harness (adotado em 2026-11-10)

O projeto entrou no harness de forma retroativa: `.claude/projetos/regeracao-f5/` (STATUS e artefatos 00 a 04), `tasks/regeracao-f5/` (18 tasks, 1 a 12 feitas e 13 a 18 em rascunho) e `metrics/entregas.jsonl` so com entregas deste projeto (o legado do harness canonico foi para `metrics/legacy-harness/`). Waivers das tasks 2, 3, 9, 11 e 12 aguardam aprovacao do usuario. Proximos passos seguem a numeracao das tasks.

## O que ja esta na `feat/regeracao`

| Bloco | Commit | Conteudo |
|---|---|---|
| 1 | `0ab4d66` | `shared/gen/parameters.yaml`, `reference/cities.csv`, `simulator/params.py`, `money.py` (F5.7: componentes, ultima parcela, taxa de entrega, reembolso por diferenca de acumulados), `geo.py` (menor rota) |
| 2 | `25822d7` | Init dos bancos gerado do DDL aprovado: `shared/sql/postgres/00..06` (inclui `06_cdc.sh`), `shared/sql/oracle/02_create_tables.sh`, `shared/mongo/init/00_replica_set.js` e `01_restaurant_profiles.js`; antigos em `legacy/`; `.gitattributes` (LF nos `.sh`); Oracle montado em `initdb.d` |
| 3 | `136d2a2` | `shared/gen/checks/*.sql` (36 consultas, T1 a T16), `simulator/checks.py` (executor e T6c, T17, T18, T19 em Python), `tests/test_invariants.py` (gate com `UBEREATS_CHECKS_DSN`) |
| 4 | `8a7e42a` | Seeds: `reference/catalog.yaml`, `simulator/seed/` (`python -m simulator.seed {cities,catalog,profiles,all}`, idempotente), `simulator/gate.py` (`python -m simulator.gate`, so leitura, T1 a T19 nos tres bancos), `simulator/db.py` |
| 5 | `e8c8508`, `f2cc486`, `c80c3f1`, `81ef6f6` | Simulador em `shared/gen/simulator/`: fundacao (`tracking`, `clock`, `agenda`, `sim_params`), regras puras (`rules`, `refunds`), referencia e escritas (`reference`, `store`), compra e ciclo (`purchase`, `kitchen`, `fleet`, `aftersales`), laco e CLI (`engine`, `__main__`: `python -m simulator run [--until] [--max-events] [--seed]`). Parametros novos no `parameters.yaml` (secao `simulation`, `behavior`, `stock`) e textos em `reference/rating_comments.yaml` e `incident_descriptions.yaml` |
| 6 | `8b28567` | Template do ShadowTraffic so com `customers`, `drivers` (Oracle) e `restaurants` (Postgres), sem MinIO; cidades injetadas do CSV pelo `setup-configs.ps1`; `toggle-shadowtraffic.ps1` com `startingFrom`/`maxEvents` dos tres cadastros; `tests/test_template.py`; `docker-compose.yml` da F5.2 (TZ, `max_slot_wal_keep_size`, Debezium 3.7 no `quay.io`, replica set e healthcheck do Mongo, `gen-unified` sem MinIO) |

Gate local: `cd shared/gen && .venv/Scripts/python -m pytest -q` (99 passam e 1 pulado sem DSN; com `UBEREATS_SIM_DSN` apontando para um Postgres `f5-*` sao 100 e leva ~2 min), `ruff check .`, `mypy simulator`. O venv `shared/gen/.venv` e local (fora do git): `python -m venv shared/gen/.venv` e `pip install -r shared/gen/requirements.txt`.

**Achados da implementacao (ja registrados no fisico e nas ADRs):** `--oplogSize` (nao `--oplogSizeMB`); o init do Mongo sem autenticacao roda em replica set nao iniciado, entao o `rs.initiate` foi para o init com membro `localhost:27017`; healthcheck do Mongo com `quit(...)`; archivelog do Oracle fica fora do volume (`$ORACLE_HOME/dbs/arch`); no Windows usar `127.0.0.1`, nao `localhost` (IPv6 pendura a conexao). O template foi validado gravando de verdade num Oracle e num Postgres descartaveis.

## Parte 5 do simulador (o que falta do bloco 5)

**Feito e provado:** 4 commits (`e8c8508`, `f2cc486`, `c80c3f1`, `81ef6f6`). Testes de integracao em Postgres descartavel: 2 dias de historico + parada/retomada passam T1 a T16 e T6c com 0 violacao; mesma semente = mesmo resultado. Em 1 dia: ~92 compras, 19 desistencias, 9 nao entregues, estornos, incidentes procedentes e improcedentes.

**Resultado da parte 5 (2026-11-10):** os tres itens abaixo foram feitos. Licenca do ShadowTraffic renovada (vale ate 2026-12-10). Cadastros populados pelo ShadowTraffic descartavel (300/60/20), `seed all`, 3 dias simulados (2.049 compras), gate 47/47 com 0 linha; `DatabaseLoader` leu Oracle e Mongo reais sem ajuste. Sais de rastreio passados por variavel de ambiente (continuam fora do `.env`). Contagem dos testes locais sem DSN: 96 passam e 4 pulam (o total 100 bate com a contagem com DSN).

**Era o que faltava (historico):**
1. **Prova ponta a ponta com os tres bancos descartaveis** (`f5-postgres`, `f5-oracle`, `f5-mongo`; sem volume nomeado, portas `127.0.0.1:15xxx`, `docker rm -v` no fim). Subir com os inits de `shared/sql/` e `shared/mongo/init/`, popular `customers`/`drivers` no Oracle e `restaurants` no Postgres (ShadowTraffic exige licenca valida; sem ela, um script descartavel fora do projeto), rodar `python -m simulator.seed all` e `python -m simulator run --until ... --seed N`, e fechar com **`python -m simulator.gate`** (T1 a T19, os tres bancos). Variaveis: `SIMULATOR_<FONTE>_HOST/_PORT`, `TRACKING_SALT_ORDER` e `TRACKING_SALT_PAYMENT` (o `.env` ainda nao as tem).
2. **Documentacao:** registrar no fisico (F5.8) os parametros novos do simulador e as decisoes abaixo; atualizar `CONTEXT.md`/`shared/docs/00-INDEX.md` se o fluxo de uso mudou; este HANDOFF.
3. **Limpeza:** `docker rm -v` dos `f5-*` (hoje `f5-postgres` segue de pe, porta 15432, init do Postgres aplicado) e conferir que nao sobrou contêiner nem volume.

**Decisoes tomadas no bloco 5 (nao estao nas RN; registrar no fisico):**
- `promised_at` conta a partir do **ultimo aceite ativo** (`max(accepted_at)` dos ativos) + maior estimado + rota/velocidade + folga; recalculavel so com colunas gravadas.
- `driver_unable` so e sorteado com o pedido **a caminho**. A RN-07 diz "depois da primeira retirada", mas a tabela de transicoes e os T2a/T3d so aceitam "nao entregue" a partir de "a caminho"; "em coleta" fica fora da v1.
- O motivo `delivery_cancelled` da atribuicao **nao ocorre** nas regras atuais (motorista so e atribuido com um atendimento pronto, e pronto nao cancela, RN-13); o `CHECK` continua aceitando o valor.
- Simulador usa `SET synchronous_commit = off` na propria sessao (42 -> 18 ms por acao no HDD da D:); transacao segue atomica.
- `drivers_per_hourly_order = 1.0` (uma entrega dura ~40 min; 0,6 saturava a frota).
- Retomada: relogio volta ao ultimo evento gravado e entidades vivas ganham passos novos com sorteio novo; avaliacoes/gorjetas pendentes na hora da parada se perdem.

**Estimativa de carga:** ~13,5 acoes por pedido, ~900 pedidos/dia na escala da F5.8, ~18 ms por acao -> ~3,6 min por dia simulado, ~2 h para os 30 dias de `backfill_days`.

## Brief do simulador (bloco 5), original (escopo ja implementado)

Ler antes: `CLAUDE.md`, este arquivo, `shared/docs/modelagem/04-modelo-fisico.md` (F5.5 a F5.9, F1 para o DDL das 22 tabelas do simulador), `03-modelo-logico.md` (L1b vocabulario de status e transicoes, L2 reembolsos por origem, L3 pos-entrega, L4 parametros), `01-regras-de-negocio.md` (RN-01 a RN-42, tabela de transicoes), ADRs 007, 008 e 009. Reaproveitar `simulator/money.py`, `geo.py`, `params.py`, `db.py`, `checks.py` e o gate.

**Escopo:** pacote em `shared/gen/simulator/` com (a) `clock` injetado (historico de `backfill_days` e depois tempo real, F5.6); (b) um processo, um escritor, fila de acoes por instante (F5.5); (c) compra numa transacao (ADR 009: checkout, tentativas, pedido, atendimentos, itens, entrega, linha 1 das duas transicoes, pagamento, componentes, recibo), codigo de rastreio com os sais do `.env` (F0.3); (d) ciclo do atendimento, entrega, turno e atribuicao, estoque (baixa no preparo, reposicao fora das janelas), repasses, gorjeta, avaliacoes, incidentes e reembolsos; (e) leitura de `customers`/`drivers` no Oracle e das janelas no Mongo com cache (`profile_cache_refresh_min`); (f) CLI `python -m simulator run`. Testes: unidade de cada regra (inclusive o congelamento do `promised_at`, T7) e um teste de integracao que roda um historico curto num Postgres descartavel e passa no `python -m simulator.gate`.

**Restricoes:** nao tocar nos conteineres e volumes atuais (`oracle-ubereats`, `postgres-ubereats`, `mongo-ubereats`, `redpanda`, `kafka-connect`, `minio-ubereats`) antes da execucao combinada da F5.3. Nao religar o ShadowTraffic do projeto (rodar o ShadowTraffic em conteiner descartavel, contra bancos descartaveis, ja foi feito para validar o template). Testes so em conteineres descartaveis (`f5-*`, sem volume nomeado, `docker rm -v` no fim; portas publicadas em `127.0.0.1:15xxx`, as 58xxx sao reservadas no Windows). Nada de `DROP`/`TRUNCATE`/`down -v`/`volume rm` sem confirmacao. Nao imprimir registros crus de pessoas. Proximo ADR livre: 013.

**Pendencias registradas para depois:** Fase 1 refaz os templates de `config/azure/debezium/` no desenho da ADR 012; `HdfsSinkConnector` no Kafka Connect 4.x; consumidores antigos (`azure/sql/synapse_copy_merge.sql`, `shared/pipeline/bronze/*`) ainda nos topicos do modelo antigo; skill de operacao do simulador; KB do ShadowTraffic (`.claude/kb/shadowtraffic/specs/generator-targets-uber-eats.yaml`) ainda descreve os geradores antigos; `RESTAURANT_COUNT` pode sair do `.env`.
