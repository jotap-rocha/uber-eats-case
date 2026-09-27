# Contrato de CDC — extensão para o Datastream e o Debezium Server (GCP, Fase 3)

> Extensão do contrato canônico de CDC definido na Onda 3 (`DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md`) e já estendido para o DMS na Fase 2/AWS (`docs/data-contract-cdc-aws-dms.md`). Ver `DESIGN_INGESTAO_GCP_FASE3.md` para o desenho completo.

A Silver/consumo (BigQuery, Dataproc, Dataflow) **nunca** lê os campos nativos do Datastream ou do Debezium Server diretamente — só as 4 colunas canônicas abaixo.

| Coluna canônica | Datastream (trilho batch) | Debezium Server (trilho real-time) |
|---|---|---|
| `cdc_operation` | `_metadata_change_type` (`INSERT`/`UPDATE`/`DELETE`/`UPSERT`) | `payload.op` (`c`/`u`/`d`) — mesmo envelope do Debezium Connect já usado na Onda 3 (Oracle) |
| `cdc_commit_ts` | `_metadata_source_timestamp` | `payload.source.ts_ms` |
| `cdc_sequence` | `_metadata_source.lsn` (Postgres) / `_metadata_source.scn` (Oracle) | `payload.source.lsn` (Postgres) / `payload.source.scn` (Oracle) |
| `cdc_source_system` | `postgres-datastream-gcp` / `oracle-datastream-gcp` / `mongo-datastream-gcp` (constante por stream) | `postgres-debezium-server-gcp` / `oracle-debezium-server-gcp` (constante por instância, injetada via SMT `InsertField$Value`, ver `src/gcp/debezium_server_*/application.properties`) |

## 🔶 Risco não confirmado (A-002 do DEFINE)

O formato exato de `_metadata_source.lsn`/`scn` do Datastream é uma leitura da documentação pública do Google Cloud, **não testado neste projeto ainda** — mesmo padrão de risco já registrado no Design da Onda 3 (Oracle/LogMiner) e da Fase 2/AWS (DMS). Confirmar com um teste real (stream ativo + `UPDATE` real na fonte) no início do `/build` seguinte, antes de considerar o mapeamento definitivo.

## MongoDB — sem `cdc_sequence` significativo

O MongoDB é fonte estática (full load/snapshot, sem CDC — decisão da Onda 3). `cdc_operation` sempre `INSERT` (ou `UPSERT`, dependendo de como o Datastream trata o load inicial); `cdc_sequence` pode ser preenchido com o `_metadata_source_timestamp` do próprio load, só para manter a coluna presente no schema — nunca é usado para resolver conflito de ordenação real.

## Delete em cascata e `TRUNCATE` — limitação conhecida, sem mitigação de design

O Datastream ignora delete em cascata e `TRUNCATE` de tabela (achado do roadmap v1.4). Se o ShadowTraffic gerar delete de Pedido cascateando para Itens de Pedido, isso **não propaga automaticamente** para a tabela correspondente no GCS/Bronze. Registrado como risco aceito nesta feature — sem mitigação de design (fica para uma iteração futura, se o cenário de delete em cascata passar a ser exercitado de fato pelo gerador).
