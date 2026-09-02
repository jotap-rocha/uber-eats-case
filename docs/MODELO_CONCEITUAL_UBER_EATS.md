# Modelo Conceitual do Domínio — Uber Eats

> Fonte: ciclo SDD arquivado em `.claude/sdd/archive/MODELO_CONCEITUAL_UBER_EATS/` (modelagem inicial), `.claude/sdd/features/*_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md` (correção estrutural, Onda 1) e `.claude/sdd/features/*_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md` (unificação de identidade, Onda 2).
>
> Reaproveitado sem alteração nas 3 arquiteturas (Warehouse, Lakehouse, Kappa) × 3 clouds (Azure, AWS, GCP) do roadmap em [`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`](ROADMAP_ARQUITETURA_MULTICLOUD.md) — Fase 0.
>
> Fonte única de dados: `gen/unified/uber-eats.json` — gerador único (Postgres real + MinIO no mesmo processo): 2 tabelas Postgres (`users`, `drivers`) + 17 streams MinIO (MySQL, MongoDB, Kafka simulados).
>
> **Estado:** todos os bugs mecânicos e gaps estruturais identificados no modelo estão **resolvidos** (Onda 1 + Onda 2). Nenhuma pendência conhecida — ver seção "Estado da implementação" ao final.

---

## Entidades (13)

| Entidade | Stream de origem | Por que é entidade |
|----------|-------------------|---------------------|
| Usuário | Postgres real, tabela `users` (fonte única desde a Onda 2) | Identidade própria, referenciado como pai por Pedido e Incidente |
| Restaurante | `mysql/restaurants` | Identidade própria, referenciado por Produto, Pedido, Avaliação, Estoque |
| Produto | `mysql/products` | Identidade própria, referenciado por Item de Pedido, Estoque |
| Motorista | Postgres real, tabela `drivers` (fonte única desde a Onda 2) | Identidade própria, referenciado por Turno e Entrega (não estava na lista original de 8 entidades do `plan.md` — incluído por decisão explícita, já que a lista era planejamento, não fechada) |
| Pedido | `kafka/orders` | Entidade central da transação |
| Item de Pedido | `mongodb/items` | Entidade fraca — só existe no contexto de um Pedido |
| Pagamento | `kafka/payments` | Identidade própria, referenciado por Recibo |
| Entrega | `kafka/route` | Identidade própria, liga Pedido + Motorista |
| Avaliação | `mysql/ratings` | Identidade própria — entidade incompleta hoje (ver gap estrutural) |
| Recibo | `kafka/receipts` | Documento com identidade própria (`receipt_id`); conteúdo derivado do pedido/pagamento não desqualifica entidade |
| Estoque | `postgres/inventory` | Entidade associativa entre Restaurante e Produto, com atributo próprio (quantidade) |
| Turno | `kafka/shift` | Entidade fraca de Motorista — motorista tem vários turnos ao longo do tempo, embarcar como atributo perderia histórico |
| Incidente | `mongodb/support` | Reclamação/ocorrência ligada a um pedido específico (categorias: atraso, item errado, item faltando, pagamento — `order_id` obrigatório em todo registro); não é atendimento genérico |

### Critério de classificação

- **É entidade** quando representa um "objeto" de negócio com identidade própria e é referenciado por outras coisas como origem/pai (mesmo que dependente — caso de entidade fraca).
- **Não é entidade** quando é: histórico de mudança de estado de uma entidade já existente; artefato derivado *sem* identidade própria; construção de apresentação/agrupamento; evento comportamental de alta frequência sem identidade de negócio; ou processo de outro domínio de negócio.
- Ter conteúdo derivado (ex.: valor copiado de outra entidade) **não** desqualifica algo de ser entidade — o que importa é ter identidade própria persistente.

### Streams fora do modelo core

| Stream | Categoria | Motivo |
|--------|-----------|--------|
| `kafka/status` | Histórico de estado | Subentidade de Pedido — evolução de status ao longo do tempo, não objeto novo |
| `kafka/events` | Histórico de estado | Subentidade de Pagamento — state machine `created→authorized→captured→(succeeded\|refunded)→settled/closed` |
| `mysql/menu` | Construção de apresentação | Agrupamento de exibição de Produto, sem identidade de negócio própria |
| `kafka/gps` | Telemetria de alta frequência | Já corretamente vinculado à Entrega (fork key = order_id via `kafka/route`); cardinalidade altíssima, sem identidade de negócio |
| `mongodb/recommendations` | Evento comportamental | Log de interação (view/click/add_to_cart), não entidade de negócio |
| `kafka/search` | Evento comportamental | Log de busca, mesma lógica |

### Streams aposentados (Onda 1 e 2)

| Stream | Motivo | Onda |
|--------|--------|------|
| `mongodb/users` | Fonte secundária da mesma entidade Usuário — absorvida | 1 |
| `mssql/users` | Substituída pela tabela `users` do Postgres real (fonte única de Usuário) | 2 |
| `postgres/drivers` | Substituída pela tabela `drivers` do Postgres real (fonte única de Motorista) | 2 |

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
| Pedido | *(histórico) Status do Pedido* | 1:N | `order_id` | subentidade, não linha própria |
| Pagamento | Recibo | 1:1 | `payment_id` | |
| Pagamento | *(histórico) Eventos do Pagamento* | 1:N | `payment_id` | subentidade |
| Avaliação | Pedido | 1:1 (opcional) | `order_id` | ✅ corrigido — Usuário/Restaurante obtidos transitivamente via Pedido |

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

**Limitação conhecida, não bloqueante:** a origem da Entrega (`start_lat/lon`) aponta para *um* restaurante real via lookup simples, não necessariamente o do mesmo pedido — amarrar ao restaurante exato exigiria lookup encadeado (pedido→restaurante→coordenada), não confirmado como suportado pelo ShadowTraffic. Possível refinamento futuro (Onda 3), não um gap de integridade referencial.

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

---

## Histórico do processo

Modelagem inicial: ciclo SDD arquivado em `.claude/sdd/archive/MODELO_CONCEITUAL_UBER_EATS/`. Correção estrutural (Onda 1): `.claude/sdd/features/*_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md`. Unificação de identidade (Onda 2): `.claude/sdd/features/*_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md`.
