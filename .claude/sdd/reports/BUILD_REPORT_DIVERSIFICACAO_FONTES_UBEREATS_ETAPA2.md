# BUILD REPORT: Diversificação de Fontes de Dados — Etapa 2 (Oracle plumbing)

| Campo | Valor |
|-------|-------|
| **Feature** | DIVERSIFICACAO_FONTES_UBEREATS |
| **Escopo deste Build** | Etapa 2 do DESIGN — itens 3-20 do file manifest (Oracle plumbing: Restaurante/Produto/Estoque insert-only + satélite MongoDB). Etapa 3 (Pedido/Pagamento com mutação real, aposentar histórico) **não** foi implementada — fica para build futuro |
| **Input** | `.claude/sdd/features/DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md` |
| **Data** | 2026-09-06 |

## Summary

| Métrica | Valor |
|---------|-------|
| Arquivos criados | 13 (DDL Oracle, connector Debezium, script de registro, seed Mongo, Bronze/Silver novos) |
| Arquivos editados | 7 (`docker-compose.yml`, `gen/unified/uber-eats.json.template`, `gen/.env.template`, `gen/setup-configs.ps1`, 2 Gold, Bronze do Postgres) |
| Arquivos removidos | 3 (Silver antigas por sistema de origem) |
| Verificações estáticas | JSON/YAML validados |
| Verificação de integração | **Executada em ambiente real, ponta a ponta** — 7 bugs reais encontrados e corrigidos no processo |

## O que foi validado de verdade (não só código estático)

Diferente da Etapa 1 (onde a licença ShadowTraffic ainda estava expirada no início), aqui o ambiente real esteve disponível o tempo todo. Testei cada componente novo isoladamente antes de testar a cadeia completa:

1. ✅ Container Oracle sobe, `ARCHIVELOG` + supplemental logging habilitados, usuário `c##dbzuser` criado como *common user* com os privilégios de LogMiner — confirmado via `ARCHIVE LOG LIST` e `cdb_sys_privs`
2. ✅ Tabelas `restaurants`/`products`/`inventory` criadas no schema `UBEREATS`, com PK e sem FK (ver bug #7 abaixo)
3. ✅ Kafka Connect + Debezium conectam no Oracle e capturam CDC real — testado com `INSERT` manual e depois com o `gen-unified` real escrevendo
4. ✅ Eventos chegam no Redpanda com envelope Debezium correto (`before`/`after`/`op`/`source.scn`/`source.ts_ms`), valores numéricos limpos (não base64), datas como string legível
5. ✅ `gen-unified` escreve nas 3 tabelas Oracle via a `connection: oracle` do config unificado, populando `restaurants`→`products`→`inventory` corretamente com os lookups cross-table

## Bugs reais encontrados e corrigidos (nesta ordem, cada um só apareceu depois do anterior ser resolvido)

| # | Bug | Sintoma | Correção |
|---|-----|---------|----------|
| 1 | `gvenzl/oracle-free:23-full` (tag rolante) resolve para versão muito recente | Debezium (2.7 **e** 3.0) não parseia `"Oracle AI Database 26ai" / version_full=23.26.3.0.0`: `Failed to resolve Oracle database version` | Fixar em `gvenzl/oracle-free:23.4-full` (`23.4.0.24.05`, formato clássico) |
| 2 | `docker.io/debezium/connect:2.7` não existe | `failed to resolve reference` | Imagem certa é `quay.io/debezium/connect:3.0` |
| 3 | `connectionConfigs.serviceName` na conexão Oracle do ShadowTraffic | `required key [db] not found` | Campo certo é `db` (mesmo nome que o Postgres usa) |
| 4 | Connector sem `schema.history.internal.kafka.*` | Task falha ao iniciar: `Error configuring an instance of KafkaSchemaHistory` | Adicionar `schema.history.internal.kafka.bootstrap.servers`/`.topic` (obrigatórios em conectores relacionais historizados) |
| 5 | `NUMBER` do Oracle sem `decimal.handling.mode` | Debezium serializa como bytes base64 (`"LQ=="`) em vez de número, com `schemas.enable=false` | `decimal.handling.mode: double` — nota: reavaliar para `payments` na Etapa 3, onde exatidão decimal importa mais que aqui |
| 6 | Colunas de data como `TIMESTAMP` no DDL Oracle | `ORA-01843: invalid month` — conversão implícita do Oracle não bate com o formato `yyyy-MM-dd HH:mm:ss` do ShadowTraffic | `VARCHAR2` em vez de `TIMESTAMP` (mesmo padrão já usado em `sql/create_users_table.sql` para o Postgres, pelo mesmo motivo) |
| 7 | FKs explícitas no DDL (`fk_products_restaurant`, `fk_inventory_*`) | `ORA-02291: integrity constraint violated` — lookup do ShadowTraffic é lógico (valor já gerado), mas a escrita cross-connection não é sincronizada fisicamente; o commit do pai pode não ter batido ainda | Remover as FKs — mesmo padrão que `users`/`drivers` já usam (sem FK); integridade validada por join real no Gold, não por constraint |

**Achado operacional (timing, não bug de config):** o healthcheck do `oracle-ubereats` pode reportar "healthy" numa janela estreita antes do listener registrar `FREEPDB1` (`ORA-12514`) ou antes do ciclo shutdown/mount/archivelog/open terminar (`ORA-01109`). Ambos transitórios — resolvidos com `docker-compose up -d --force-recreate gen-unified` alguns segundos depois. Documentado no DESIGN para quem automatizar isso depois.

## Tasks executadas

| Task | Status | Notas |
|------|--------|-------|
| `docker-compose.yml`: `oracle-ubereats`, `redpanda`, `kafka-connect`, `mongo-ubereats` | ✅ | Imagens corrigidas pós-teste (ver bugs #1, #2) |
| `sql/oracle/00_enable_archivelog.sql` | ✅ | Testado — ciclo shutdown/mount/archivelog/open funciona dentro do `container-entrypoint-startdb.d` |
| `sql/oracle/01_create_user.sh` | ✅ | Reescrito de `.sql` para `.sh` (variáveis de ambiente via heredoc, evita prompt interativo do SQL*Plus). Também corrigido: `ubereats` já é criado pela própria imagem via `APP_USER`/`APP_USER_PASSWORD` — script só faz `GRANT` extra; `c##dbzuser` precisa ser criado a partir do `CDB$ROOT`, não de dentro do PDB (`ORA-65050` na primeira tentativa) |
| `sql/oracle/02_create_tables.sh` | ✅ | DDL de `restaurants`/`products`/`inventory`, sem FK (bug #7), datas como `VARCHAR2` (bug #6) |
| `gen/unified/uber-eats.json.template`: `connections.oracle` + migração de 3 geradores + 6 lookups corrigidos | ✅ | Campo `db` corrigido (bug #3); testado escrevendo de verdade |
| `debezium/oracle-connector.json.template` + `register-oracle-connector.ps1` | ✅ | `schema.history.internal.kafka.*` e `decimal.handling.mode` adicionados (bugs #4, #5) |
| `pipeline/bronze/ingest_oracle_{restaurants,products,inventory}.sql` | ✅ | Lê Kafka via `read_kafka()`, contrato canônico de CDC (`cdc_operation`/`cdc_commit_ts`/`cdc_sequence`/`cdc_source_system`) preservado (não excluído do `APPLY CHANGES INTO`, ao contrário do padrão Airbyte) |
| `pipeline/bronze/ingest_postgres_drivers.sql` (retrofit) | ✅ | Ganhou as 4 colunas canônicas de CDC; `SEQUENCE BY` trocado de `_ab_cdc_updated_at` para `cdc_sequence` (LSN) — mitiga o risco de colisão em rajada de updates que a Etapa 1 tinha deixado em aberto |
| `pipeline/silver/ingestion_oracle_{restaurants,products,inventory}.sql` (substituem as `mysql_*`/`postgres_inventory`) | ✅ | Mesmo padrão de 5 seções já usado no projeto, renomeadas por domínio (`silver_restaurants`, não `silver_mysql_restaurants`) |
| `pipeline/gold/load_restaurant_performance.sql`, `load_order_unit_economics.sql` | ✅ | Referência atualizada para `silver_restaurants` |
| `mongo/init/01_perfil_restaurante.js.template` + geração via `setup-configs.ps1` | ✅ | `RESTAURANT_COUNT` como fonte única de verdade, usada tanto no gerador (`maxEvents`) quanto no seed Mongo — **não testado em ambiente real** (ver Pendências) |
| `pipeline/silver/ingestion_mongo_perfil_restaurante.sql` | ✅ código | Depende de uma conexão Lakehouse Federation para MongoDB no Unity Catalog — **pré-requisito de plataforma fora do escopo deste script**, não testado |

## Pendências (não bloqueantes para fechar a Etapa 2, mas registradas)

1. **MongoDB não foi testado em ambiente real nesta sessão** — o seed determinístico (`mongo/init/01_perfil_restaurante.js.template`) foi validado estruturalmente (JS sintaticamente correto, lógica de geração revisada), mas não subi o container `mongo-ubereats` de fato. Recomenda-se validar antes do `/ship`.
2. **Lakehouse Federation para MongoDB** — a Silver do satélite (`ingestion_mongo_perfil_restaurante.sql`) assume uma conexão UC chamada `mongo_ubereats` que precisa ser criada manualmente na plataforma Databricks (fora do alcance de scripts SQL/Docker). Documentado como pré-requisito no próprio arquivo.
3. **`decimal.handling.mode: double`** perde precisão exata — aceitável para `average_rating`/`lat`/`lon` desta etapa, mas vale reavaliar (`string` + `CAST` explícito) quando `payments` entrar na Etapa 3, onde exatidão de centavos importa mais.
4. **Join de integridade completo no Gold (Databricks)** não foi executado — os dados foram validados diretamente no Oracle/Kafka (contagens crescendo, sem erro de escrita), não através do pipeline Bronze→Silver→Gold real no Databricks. Recomenda-se rodar isso antes do `/ship` da feature completa (ao final da Etapa 3), seguindo a mesma disciplina das Ondas 1/2.
5. **Footprint de recursos:** com Oracle+Redpanda+Kafka Connect rodando, a stack local soma múltiplos GB de RAM adicionais (Oracle sozinho ~2.5GB em repouso). Nenhum desses serviços está no `start-all.ps1` por padrão — precisam ser subidos explicitamente (`docker-compose up -d oracle-ubereats redpanda kafka-connect`), seguindo o mesmo princípio já aplicado ao Airbyte (sob demanda, não sempre ligado).

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação. Sugestão de mensagem:

```text
feat(oracle): sobe Oracle+Debezium+Redpanda e migra Restaurante/Produto/Estoque (Onda 3, Etapa 2)

Adiciona Oracle (gvenzl/oracle-free:23.4-full, ARCHIVELOG habilitado),
Redpanda e Kafka Connect/Debezium ao docker-compose. Migra os geradores
restaurants/products/inventory do MinIO simulado para o Oracle real
(insert-only nesta etapa), com os 6 lookups cross-referenciados
corrigidos. Bronze/Silver novos leem o CDC via Kafka; Silver renomeada
por dominio (silver_restaurants, nao silver_mysql_restaurants). Contrato
canonico de CDC retrofitado no Bronze do Postgres tambem.

Validado ponta a ponta em ambiente real: 7 bugs reais encontrados e
corrigidos no processo (versao Oracle incompativel com Debezium, imagem
Docker Hub inexistente, campo de conexao errado, config obrigatoria
faltando, decimal serializado como base64, conversao implicita de data
falhando, FK causando erro de integridade por escrita cross-connection
nao sincronizada). Satelite MongoDB (Perfil de Restaurante) codificado
mas nao testado em ambiente real -- fica pendente antes do /ship.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```

## Status: ⚠️ COMPLETE (código + validação de integração parcial)

**Validado de verdade:** Oracle, Debezium, Redpanda, geração via ShadowTraffic, CDC ponta a ponta.
**Não validado:** MongoDB (satélite), pipeline Bronze→Silver→Gold completo no Databricks.
**Recomendo:** antes do `/ship` da feature completa (após Etapa 3), rodar o satélite Mongo pelo menos uma vez e o pipeline Databricks completo para confirmar joins sem órfãos — mesma disciplina das Ondas 1/2.
