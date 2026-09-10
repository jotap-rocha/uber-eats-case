# Modelo Conceitual do Domínio — Uber Eats

> Fonte: ciclo SDD arquivado em `.claude/sdd/archive/MODELO_CONCEITUAL_UBER_EATS/` (modelagem inicial), `.claude/sdd/features/*_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md` (correção estrutural, Onda 1), `.claude/sdd/features/*_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` (unificação de identidade, Onda 2) e `.claude/sdd/features/*_DIVERSIFICACAO_FONTES_UBEREATS.md` (diversificação de fontes + mutação real, Onda 3).
>
> Reaproveitado sem alteração nas 3 arquiteturas (Warehouse, Lakehouse, Kappa) × 3 clouds (Azure, AWS, GCP) do roadmap em [`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`](ROADMAP_ARQUITETURA_MULTICLOUD.md) — Fase 0.
>
> Fonte de dados: `gen/unified/uber-eats.json` — gerador único (Postgres + Oracle no mesmo processo) + satélite MongoDB (seed estático) + MinIO (streams remanescentes). 4 sistemas ao todo: **Postgres** (`users`, `drivers` — mutação real de linha), **Oracle** (`restaurants`, `products`, `inventory`, `orders`, `payments`, `order_items`, `receipts` — insert-only e mutação real, capturado via Debezium/Kafka Connect/Redpanda), **MongoDB** (`restaurant_profile`, satélite estático, sem CDC) e **MinIO** (streams remanescentes: Entrega, Avaliação, Turno, Incidente e os fora-do-modelo-core).
>
> **Estado:** todos os bugs mecânicos e gaps estruturais identificados no modelo estão **resolvidos** (Onda 1 + Onda 2 + Onda 3). Nenhuma pendência conhecida no modelo em si — ver seção "Estado da implementação" ao final (a Onda 3 tem pendências de *validação em Databricks real*, fora do escopo deste documento).

---

## Entidades (14)

| Entidade | Stream de origem | Por que é entidade |
|----------|-------------------|---------------------|
| Usuário | Postgres real, tabela `users` (fonte única desde a Onda 2) | Identidade própria, referenciado como pai por Pedido e Incidente |
| Restaurante | Oracle real, tabela `restaurants` (migrado de `mysql/restaurants` na Onda 3, Etapa 2) | Identidade própria, referenciado por Produto, Pedido, Avaliação, Estoque, Perfil de Restaurante |
| Produto | Oracle real, tabela `products` (migrado de `mysql/products` na Onda 3, Etapa 2) | Identidade própria, referenciado por Item de Pedido, Estoque |
| Motorista | Postgres real, tabela `drivers` (fonte única desde a Onda 2; ganha mutação real de linha — `status`/`total_deliveries`/`total_earnings`/`average_rating` — na Onda 3, Etapa 1) | Identidade própria, referenciado por Turno e Entrega (não estava na lista original de 8 entidades do `plan.md` — incluído por decisão explícita, já que a lista era planejamento, não fechada) |
| Pedido | Oracle real, tabela `orders` (migrado de `kafka/orders` na Onda 3, Etapa 3; mutação real de linha nas 9 fases do ciclo de vida, substitui o histórico append-only `kafka/status`) | Entidade central da transação |
| Item de Pedido | Oracle real, tabela `order_items` (migrado de `mongodb/items` na Onda 3, Etapa 3) | Entidade fraca — só existe no contexto de um Pedido |
| Pagamento | Oracle real, tabela `payments` (migrado de `kafka/payments` na Onda 3, Etapa 3; mutação real de linha nos 4 estados finais, substitui o histórico append-only `kafka/events`) | Identidade própria, referenciado por Recibo |
| Entrega | `kafka/route` | Identidade própria, liga Pedido + Motorista |
| Avaliação | `mysql/ratings` | Identidade própria — entidade incompleta hoje (ver gap estrutural) |
| Recibo | Oracle real, tabela `receipts` (migrado de `kafka/receipts` na Onda 3, Etapa 3) | Documento com identidade própria (`receipt_id`); conteúdo derivado do pedido/pagamento não desqualifica entidade |
| Estoque | Oracle real, tabela `inventory` (migrado de `postgres/inventory` na Onda 3, Etapa 2) | Entidade associativa entre Restaurante e Produto, com atributo próprio (quantidade) |
| Turno | `kafka/shift` | Entidade fraca de Motorista — motorista tem vários turnos ao longo do tempo, embarcar como atributo perderia histórico |
| Incidente | `mongodb/support` | Reclamação/ocorrência ligada a um pedido específico (categorias: atraso, item errado, item faltando, pagamento — `order_id` obrigatório em todo registro); não é atendimento genérico |
| Perfil de Restaurante | MongoDB satélite, coleção `restaurant_profile` (seed estático, Onda 3, Etapa 2 — nova entidade) | Entidade fraca de Restaurante — menu + horários de funcionamento; população determinística (`restaurant_id: 1..N`, mesmo `RESTAURANT_COUNT` do gerador Oracle), sem sink de escrita no ShadowTraffic e sem CDC (satélite estático, não mutável em runtime) |

### Critério de classificação

- **É entidade** quando representa um "objeto" de negócio com identidade própria e é referenciado por outras coisas como origem/pai (mesmo que dependente — caso de entidade fraca).
- **Não é entidade** quando é: histórico de mudança de estado de uma entidade já existente; artefato derivado *sem* identidade própria; construção de apresentação/agrupamento; evento comportamental de alta frequência sem identidade de negócio; ou processo de outro domínio de negócio.
- Ter conteúdo derivado (ex.: valor copiado de outra entidade) **não** desqualifica algo de ser entidade — o que importa é ter identidade própria persistente.

### Streams fora do modelo core

| Stream | Categoria | Motivo |
|--------|-----------|--------|
| `mysql/menu` | Construção de apresentação | Agrupamento de exibição de Produto, sem identidade de negócio própria |
| `kafka/gps` | Telemetria de alta frequência | Já corretamente vinculado à Entrega (fork key = order_id via `kafka/route`); cardinalidade altíssima, sem identidade de negócio |
| `mongodb/recommendations` | Evento comportamental | Log de interação (view/click/add_to_cart), não entidade de negócio |
| `kafka/search` | Evento comportamental | Log de busca, mesma lógica |

### Streams aposentados (Onda 1, 2 e 3)

| Stream | Motivo | Onda |
|--------|--------|------|
| `mongodb/users` | Fonte secundária da mesma entidade Usuário — absorvida | 1 |
| `mssql/users` | Substituída pela tabela `users` do Postgres real (fonte única de Usuário) | 2 |
| `postgres/drivers` | Substituída pela tabela `drivers` do Postgres real (fonte única de Motorista) | 2 |
| `mysql/restaurants` | Substituída pela tabela `restaurants` do Oracle real | 3 |
| `mysql/products` | Substituída pela tabela `products` do Oracle real | 3 |
| `postgres/inventory` | Substituída pela tabela `inventory` do Oracle real | 3 |
| `kafka/orders` | Substituída pela tabela `orders` do Oracle real, com mutação de linha | 3 |
| `kafka/payments` | Substituída pela tabela `payments` do Oracle real, com mutação de linha | 3 |
| `mongodb/items` | Substituída pela tabela `order_items` do Oracle real | 3 |
| `kafka/receipts` | Substituída pela tabela `receipts` do Oracle real | 3 |
| `kafka/status` | **Removido por completo** — histórico append-only de status do Pedido vira mutação real de linha em `orders` (não é mais modelado como stream separado nem como subentidade) | 3 |
| `kafka/events` | **Removido por completo** — histórico append-only de eventos do Pagamento vira mutação real de linha em `payments` | 3 |

---

## Relacionamentos e cardinalidade (modelo-alvo)

| Entidade | Relaciona-se com | Cardinalidade | Chave-alvo | Observação / gap |
|----------|-------------------|----------------|------------|-------------------|
| Usuário | Pedido | 1:N | `user_id` | ✅ fonte única desde a Onda 2 (Postgres real); cpf/email/endereço permanecem como atributos |
| Usuário | Incidente | 1:N | `user_id` | ✅ mesma fonte única |
| Restaurante | Produto | 1:N | `restaurant_id` | cnpj vira atributo |
| Restaurante | Pedido | 1:N | `restaurant_id` | ✅ corrigido (era `cnpj`) |
| Restaurante | Avaliação | 1:N | `restaurant_id` (via Pedido, transitivo) | ✅ corrigido — Avaliação não referencia mais Restaurante direto, vem transitivamente pelo Pedido |
| Restaurante ↔ Produto | Estoque | N:N (via Estoque) | `restaurant_id` + `product_id` | Estoque é entidade associativa |
| Produto | Item de Pedido | 1:N | `product_id` | ✅ corrigido (era string própria incompatível) |
| Motorista | Turno | 1:N | `driver_id` | ✅ fonte única desde a Onda 2 (Postgres real) |
| Motorista | Entrega | 1:N | `driver_id` | ✅ mesma fonte única |
| Pedido | Item de Pedido | 1:N | `order_id` | |
| Pedido | Pagamento | 1:1 | `order_id` | ✅ corrigido — `payment_key` **removido** de Pedido (era circular, ver nota); a relação já existia corretamente via `kafka/payments.order_key` |
| Pedido | Recibo | 1:1 | `order_id` | |
| Pedido | Entrega | 1:1 | `order_id` | ✅ corrigido — origem (restaurante) e destino (usuário, Postgres real) usam coordenada real |
| Pedido | Incidente | 1:N | `order_id` | |
| Pagamento | Recibo | 1:1 | `payment_id` | |
| Avaliação | Pedido | 1:1 (opcional) | `order_id` | ✅ corrigido — Usuário/Restaurante obtidos transitivamente via Pedido |
| Restaurante | Perfil de Restaurante | 1:1 | `restaurant_id` | ✅ novo (Onda 3) — satélite MongoDB, população determinística por range de `restaurant_id` |

**Nota (Onda 3):** as linhas *(histórico) Status do Pedido* e *(histórico) Eventos do Pagamento*, que existiam aqui como subentidades 1:N, foram **removidas do modelo** — não existem mais como stream separado nem como registro histórico append-only. `status` (Pedido) e o estado de `payments` (Pagamento) agora são **mutação real da própria linha** em `orders`/`payments` no Oracle, capturada via CDC (Debezium) como uma sequência de `UPDATE`s reais, não mais como uma tabela de eventos à parte.

---

## Decisão de chave canônica

Nos 3 casos de chave dupla (Usuário, Restaurante, Motorista), **o ID técnico sequencial vence** como chave-alvo de junção (`user_id`, `restaurant_id`, `driver_id`) — resolvido nas Ondas 1 (Restaurante) e 2 (Usuário/Motorista).

CPF, CNPJ e license_number **não são eliminados** — continuam existindo como atributos normais da entidade, só deixam de ser usados como chave de relacionamento. Motivo: CPF é PII sensível e não deveria se propagar como FK por todo o domínio; IDs técnicos são estáveis e não variam de formato entre fontes.

**Nota sobre Usuário/Motorista (Onda 2):** a tabela Postgres real já existia com PK `uuid` antes desta correção. Em vez de adotar o UUID como chave-alvo (o que evitaria mexer no schema já em produção), decidiu-se **migrar o schema real para `int` sequencial** — prioridade de consistência de estilo com Restaurante sobre não alterar uma tabela existente. Isso exigiu regenerar os dados já carregados (a migração de PK não é incremental).

---

## Bugs mecânicos (✅ resolvidos)

| Bug | Estado anterior | Correção implementada |
|-----|---------------------|-------------------------|
| `kafka/orders.payment_key` | Gerava UUID aleatório, não referenciava nenhum pagamento real | **Removido** — não "corrigido para lookup" como planejado inicialmente: seria circular (`kafka/payments.order_key` já depende do pedido existir; o inverso não é possível na mesma geração). A relação pedido↔pagamento já existia corretamente via `kafka/payments.order_key` |
| `mongodb/items.product_id` | Gerava string própria (`PRD-####`, 4 dígitos), nunca batia com Produto | Lookup em `mysql/products.product_id` (formato `PRD-#####`, 5 dígitos) |

---

## Gaps estruturais (✅ todos resolvidos)

| Gap | Correção implementada | Onda |
|-----|-------------------------|------|
| Avaliação sem ligação a Usuário/Pedido | `mysql/ratings` ganhou `order_id` (lookup obrigatório em `kafka/orders`); `restaurant_identifier` removido — Restaurante e Usuário vêm transitivamente via Pedido | 1 |
| Entrega sem coordenada real — origem | `mysql/restaurants` ganhou `lat`/`lon`; `kafka/route.start_lat/lon` faz lookup real em Restaurante | 1 |
| Restaurante — chave dupla (`cnpj` vs `restaurant_id`) | `kafka/orders.restaurant_key` e `mysql/ratings` migrados para `restaurant_id`; `cnpj` mantido como atributo | 1 |
| Usuário/Motorista — duas populações desconectadas (Postgres real UUID vs MinIO simulado int) | Gerador unificado (1 processo, `connections: postgres` + `minio`); Postgres real vira fonte única; `mssql/users`, `mongodb/users`, `postgres/drivers` aposentados | 2 |
| Usuário/Motorista — chave dupla (`cpf`/`license_number` vs ID) | PK do Postgres real migrada de `uuid` para `int` sequencial; todo consumidor MinIO referencia o ID real via lookup cruzado | 2 |
| Entrega — coordenada de destino (Usuário) | `kafka/route.end_lat/end_lon` faz lookup real em `users.lat/lon` (Postgres) | 2 |
| `silver_drivers_profile` (MinIO) vs. `silver_drivers_performance` (Postgres real) | Reconciliadas numa única tabela `silver_drivers`, incluindo `vehicle_make`/`vehicle_model`/`vehicle_year`/`license_number`/`city` adicionados ao Postgres real para não perder atributos | 2 |

**Limitação conhecida, não bloqueante:** a origem da Entrega (`start_lat/lon`) aponta para *um* restaurante real via lookup simples, não necessariamente o do mesmo pedido — amarrar ao restaurante exato exigiria lookup encadeado (pedido→restaurante→coordenada), não confirmado como suportado pelo ShadowTraffic. Não endereçado na Onda 3 (fora do escopo entregue — a Onda 3 focou em diversificação de fontes e mutação real, não em refinar esta lookup); possível refinamento futuro, não é um gap de integridade referencial.

---

## Estado da implementação

### Onda 1 — Shadow Traffic (correção dentro do MinIO)

| Componente | Arquivo | Mudança |
|------------|---------|---------|
| Gerador | (então `gen/minio/uber-eats.json`, hoje parte de `gen/unified/uber-eats.json`) | `orders`: removidos `payment_key`, `rating_key`; `restaurant_key` migrado para `restaurant_id`. `mongodb/items.product_id`: lookup real. `mysql/ratings`: `+order_id`, `-restaurant_identifier`. `mysql/restaurants`: `+lat`, `+lon`. `kafka/route.start_lat/lon`: lookup real |
| Silver | `ingestion_kafka_orders.sql`, `ingestion_kafka_ratings.sql`, `ingestion_mysql_restaurants.sql` | Colunas renomeadas/adicionadas |
| Gold | `load_order_unit_economics.sql`, `load_restaurant_performance.sql` | Join por `id_restaurante` em vez de `cnpj` |

### Onda 2 — Unificação de identidade Postgres×MinIO

| Componente | Arquivo | Mudança |
|------------|---------|---------|
| Infraestrutura | `docker-compose.yml` | 3 containers (`gen-drivers`, `gen-users`, `gen-minio`) → 1 (`gen-unified`) |
| Gerador | `gen/unified/uber-eats.json(.template)` (novo, substitui `gen/postgres/*` e `gen/minio/uber-eats.json`) | `connections: postgres + minio`; `users`/`drivers` no Postgres real; todo consumidor MinIO redirecionado |
| Schema real | `sql/create_users_table.sql`, `create_drivers_table.sql` | PK `uuid`→`int`; `drivers` ganha `vehicle_make`, `vehicle_model`, `vehicle_year`, `license_number`, `city` |
| Automação | `gen/setup-configs.ps1`, `scripts/start-generators.ps1`, `stop-generators.ps1`, `start-all.ps1`, `reset-all.ps1` | Apontam para o gerador único |
| Silver | `ingestion_kafka_orders.sql` (renomeia `cpf_usuario`→`id_usuario`); `ingestion_postgres_drivers.sql` (novo, substitui os 2 scripts antigos de motorista) | Dimensão única de motorista |
| Documentação | Este arquivo | Zero pendências |

**Pendente de execução manual** (fora do que o Build de código cobre): a migração de PK exige recriar o volume Postgres (`docker-compose down -v`) para que `sql/*.sql` rode de novo; depois regenerar os dados e rodar o pipeline Databricks completo (Bronze→Silver→Gold) para confirmar 0 registros órfãos — ver `BUILD_REPORT_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` para o checklist exato.

### Onda 3 — Diversificação de fontes + mutação real (Postgres/Oracle/MongoDB)

Três etapas sequenciais, cada uma validada em ambiente real (Docker local) ponta a ponta antes de avançar para a próxima — ver `.claude/sdd/reports/BUILD_REPORT_DIVERSIFICACAO_FONTES_UBEREATS_ETAPA{1,2,3}.md` para o detalhe completo de cada Build, incluindo os bugs reais encontrados e corrigidos em cada etapa.

| Etapa | Componente | Mudança |
|-------|------------|---------|
| 1 — Motorista/Postgres | Gerador | `drivers` ganha `fork.key=driver_id` + `stateMachine`: `INSERT` inicial, depois `op:update` na mesma linha para `status`/`total_deliveries`/`total_earnings`/`average_rating` — primeira prova real do mecanismo de mutação de linha (mesmo padrão reaproveitado nas Etapas 2/3) |
| 2 — Restaurante/Produto/Estoque/Oracle | Infraestrutura | `docker-compose.yml` ganha `oracle-ubereats` (`gvenzl/oracle-free:23.4-full`, ARCHIVELOG+LogMiner), `redpanda` (broker Kafka-compatível), `kafka-connect` (`quay.io/debezium/connect:3.0`), `mongo-ubereats` (seed estático) |
| 2 | Gerador | `restaurants`/`products`/`inventory` migram de `bucket`/`data` (MinIO) para `table`/`row` (Oracle), insert-only; conector Debezium Oracle registrado via REST API |
| 2 | Bronze/Silver | `ingest_oracle_{restaurants,products,inventory}.sql` (Kafka→Structured Streaming, contrato canônico de CDC) e `ingestion_oracle_{restaurants,products,inventory}.sql` (substituem `ingestion_mysql_restaurants`/`ingestion_mysql_products`/`ingestion_postgres_inventory`) |
| 2 | Satélite | `mongo/init/01_perfil_restaurante.js` — seed de `RESTAURANT_COUNT` documentos (`restaurant_id: 1..N`, menu + horários); `ingestion_mongo_perfil_restaurante.sql` produz `silver_restaurant_profile` |
| 3 — Pedido/Pagamento/Oracle | Gerador | `orders`/`payments` migram de `bucket`/`data`+`fork`(→S3) para `table`/`row`+`fork`+`stateMachine`(→`op:update` no Oracle), mesmo padrão da Etapa 1; `order_items`/`receipts` seguem para Oracle; `kafka/status` e `kafka/events` **removidos** do gerador |
| 3 | Schema real | `sql/oracle/03_create_tables_pedido_pagamento.sh` — `orders`, `payments`, `order_items`, `receipts`; `order_id`/`payment_id` migram de `uuid` para `sequentialInteger` (mesmo critério de chave canônica já aplicado a Usuário/Restaurante/Motorista) |
| 3 | Bronze/Silver | `ingest_oracle_{orders,payments,order_items,receipts}.sql` e `ingestion_oracle_{orders,payments,order_items,receipts}.sql` (substituem `ingestion_kafka_orders`/`ingestion_kafka_payments`/`ingestion_mongodb_items`/`ingestion_kafka_receipts`); `ingestion_kafka_status.sql`/`ingestion_kafka_events.sql` **removidos** |
| 3 | Gold | `load_order_unit_economics.sql`, `load_restaurant_performance.sql` — referências de Silver atualizadas para os nomes por domínio |
| Transversal | Nomenclatura | Convenção de nomear Silver por domínio de negócio (não por sistema de origem) aplicada a **todo** o projeto no commit `817dade`, não só às tabelas desta Onda — ver tabela de nomenclatura abaixo |

**Tabela de nomenclatura antiga → nova (Silver, por causa da migração de origem):**

| Silver antiga (por sistema) | Silver nova (por domínio) | Origem antiga → nova |
|---|---|---|
| `silver_mysql_restaurants` | `silver_restaurants` | `mysql/restaurants` (MinIO) → `restaurants` (Oracle) |
| `silver_mysql_products` | `silver_products` | `mysql/products` (MinIO) → `products` (Oracle) |
| `silver_postgres_inventory` | `silver_inventory` | `postgres/inventory` (MinIO) → `inventory` (Oracle) |
| `silver_kafka_orders` | `silver_orders` | `kafka/orders` (MinIO) → `orders` (Oracle, mutação real) |
| `silver_kafka_payments` | `silver_payments` | `kafka/payments` (MinIO) → `payments` (Oracle, mutação real) |
| `silver_mongodb_items` | `silver_order_items` | `mongodb/items` (MinIO) → `order_items` (Oracle) |
| `silver_kafka_receipts` | `silver_receipts` | `kafka/receipts` (MinIO) → `receipts` (Oracle) |
| `silver_kafka_status` | *(removida)* | Histórico append-only aposentado — vira mutação de linha em `silver_orders` |
| `silver_kafka_events` | *(removida)* | Histórico append-only aposentado — vira mutação de linha em `silver_payments` |
| *(inexistente)* | `silver_restaurant_profile` | Nova (Onda 3) — satélite MongoDB `restaurant_profile` |

**Pendente de execução manual** (registrado nos 3 `BUILD_REPORT_*`, não bloqueante para o modelo conceitual em si):
1. Pipeline Bronze→Silver→Gold completo não foi executado num workspace Databricks real — validação local cobriu Oracle/ShadowTraffic/CDC (Debezium/Redpanda), não a leitura via `read_kafka()` dentro do Lakeflow real.
2. Lakehouse Federation para MongoDB não validada (depende de conexão Unity Catalog criada manualmente na plataforma).

---

## Histórico do processo

Modelagem inicial: ciclo SDD arquivado em `.claude/sdd/archive/MODELO_CONCEITUAL_UBER_EATS/`. Correção estrutural (Onda 1): `.claude/sdd/features/*_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md`. Unificação de identidade (Onda 2): `.claude/sdd/features/*_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md`. Diversificação de fontes + mutação real (Onda 3): `.claude/sdd/features/*_DIVERSIFICACAO_FONTES_UBEREATS.md` (BRAINSTORM/DEFINE/DESIGN) e `.claude/sdd/reports/BUILD_REPORT_DIVERSIFICACAO_FONTES_UBEREATS_ETAPA{1,2,3}.md`.
