# Handoff — uber-eats-case

> Gerado pelo install-harness em 2026-10-16. Atualize a cada handoff de sessão.

## Estado atual

Modelagem de dados: regras (RN-01 a RN-42), conceitual e **modelo logico L0 a L4 aprovados e mesclados na `main`** (PR #17, 2026-11-03), em `shared/docs/modelagem/`. ADRs 006 a 012 aceitas. Documentacao alinhada (links, avisos de obsoleto, roadmap 2.0). Oracle atual ainda tratado como producao; gerador nao religado. Branch de trabalho: `feat/modelo-fisico`.

## Proximos passos

1. **Modelo fisico** (`shared/docs/modelagem/04-modelo-fisico.md`), em fases com revisao por perguntas. **F0 aprovada** (2026-11-03; ADR 009: o simulador cria a compra numa transacao). **F1 aprovada** (2026-11-04; DDL Postgres, schema `ubereats`). MinIO fora do escopo (ADR 010, 2026-11-04; logica guardada em `shared/docs/minio/historico-geracao.md`). **F2 aprovada** (2026-11-04; DDL Oracle no schema `UBEREATS`, gatilho de logon para datas ISO, booleano em `NUMBER(1)`). **F3 aprovada** (2026-11-04; `restaurant_profiles` com `_id` = restaurant_id e validador `$jsonSchema`; gerado por seed em Python, adendo da ADR 009). **F4 aprovada** (2026-11-04; ADR 011: Debezium 3.7 e MongoDB em replica set `rs0` com CDC por change stream no Airbyte; chaves `NUMBER` do Oracle chegam como texto e a Bronze faz `CAST`; templates de conector local e GCP ja atualizados; ADR 012: na Azure, warehouse e lakehouse pelo Debezium/Airbyte locais ate o storage e o Kappa com conector dedicado no Event Hubs Standard, so na fase do Kappa). Proxima: **F5 plano da regeracao**.
2. **Regeracao dos dados do zero** (ADR 006/007/009/011): ShadowTraffic (cadastros) + seed Python do perfil no MongoDB + simulador de operacao (compra e ciclo). Renovar a licenca do ShadowTraffic antes (vence por volta de 2026-11-07).
3. **Pipeline** (`shared/pipeline/`, hoje no modelo antigo): so depois do fisico e da regeracao. A Bronze segue o contrato da F4.6 (envelope Debezium, `CAST` das chaves Oracle, `cdc_sequence` `DECIMAL(20,0)`, `cdc_tx_id`).

## Brief da F5 (plano da regeracao), para a proxima sessao

Ler antes: `CLAUDE.md`, este arquivo, `shared/docs/modelagem/04-modelo-fisico.md` (F0 a F4, sobretudo as notas "Para a F5" da F3 e da F4 e as "Decisoes da revisao"), `docs/adr/006`, `007`, `009`, `010` e `011`.

**Fluxo (o mesmo de F1 a F4):** escrever a secao F5 -> validar em containers descartaveis se for o caso -> revisar com `AskUserQuestion` (ate 4 perguntas, recomendada primeiro) -> "Decisoes da revisao da F5 (data)" e marcar "aprovada" -> atualizar este HANDOFF -> commit com acordo do usuario.

**O que a F5 precisa decidir/escrever:**

1. **Ordem da regeracao:** DDL (F1, F2, F3) -> usuario/publicacao do CDC no Postgres (F4.2) -> registrar conectores (antes da carga, F4.0 #5) -> cadastros (ShadowTraffic) -> seed do MongoDB -> simulador. Inclui as mudancas do `docker-compose.yml` que ficaram para a regeracao (F4.7): imagens 3.7 no `quay.io`, `max_slot_wal_keep_size=4GB`, replica set do Mongo, `TZ=America/Sao_Paulo` (F0).
2. **Catalogo do Postgres:** quem carrega produtos, estoque e fichas tecnicas coerentes (ShadowTraffic ou seed em Python), achado da F3.
3. **Divisao gerador x simulador** e parametros em `shared/gen/parameters.yaml` (F0.9); arredondamento e ultima parcela da RN-33 (F0.7).
4. **Testes T1 a T18 como consultas**, mais o teste novo das janelas do MongoDB (F3.2).
5. **Script de registro do conector Postgres** (ha `register-oracle-connector.ps1`, falta o do Postgres) e senha `POSTGRES_DEBEZIUM_PASSWORD` no `.env` (o `.env` ainda nao tem as variaveis `POSTGRES_DEBEZIUM_*`).
6. Conferir os metadados `_ab_cdc_*` do Airbyte na primeira sync do MongoDB.

**Pendencias registradas para depois:** Fase 1 refaz os templates de `config/azure/debezium/` no desenho da ADR 012 (sink do Redpanda local ao ADLS; conector do Kappa com as tabelas do problema, ate 10 event hubs contando os internos, historico do Oracle em arquivo); `HdfsSinkConnector` no Kafka Connect 4.x; consumidores antigos (`azure/sql/synapse_copy_merge.sql`, `shared/pipeline/bronze/*`) ainda nos topicos do modelo antigo.

**Restricoes:** nao aplicar config nos containers atuais (`oracle-ubereats`, `postgres-ubereats`, `mongo-ubereats`, `kafka-connect`) sem a regeracao combinada. Testes so em containers descartaveis, sem volume nomeado, com outros nomes, removidos ao final com `docker rm -v` (no Windows, portas 58xxx estao reservadas; usar `docker exec` em vez de publicar porta). Nao religar o ShadowTraffic. Nada de `DROP`/`TRUNCATE`/`down -v`/`volume rm` sem confirmacao. Nao imprimir registros crus de pessoas. Proximo ADR livre: 013.
