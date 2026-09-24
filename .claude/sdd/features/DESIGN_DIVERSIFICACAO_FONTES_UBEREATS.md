# DESIGN: Diversificação de Fontes de Dados (Onda 3)

| Campo | Valor |
|-------|-------|
| **Feature** | DIVERSIFICACAO_FONTES_UBEREATS |
| **Input** | `.claude/sdd/features/DEFINE_DIVERSIFICACAO_FONTES_UBEREATS.md` |
| **Status** | ✅ Complete (Designed) |
| **Data** | 2026-09-06 |

---

## Architecture Overview

```text
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                    ETAPA 1 — Provar mutação no Postgres (Motorista)                    │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  gen-unified (ShadowTraffic, connection: postgres)                                    │
│    drivers: fork(key=driver_id) + stateMachine → INSERT, depois op:update em          │
│    status/total_deliveries/total_earnings/average_rating na MESMA linha               │
│                    │                                                                   │
│                    ▼                                                                   │
│  postgres-ubereats (wal_level=logical, já configurado)                                │
│                    │  CDC lógico                                                       │
│                    ▼                                                                   │
│  Airbyte (já configurado) ──► raw.drivers (Databricks) ──► Bronze (já existe,          │
│                                                              APPLY CHANGES INTO)        │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│              ETAPA 2 — Levantar Oracle (Restaurante/Produto/Estoque, insert-only)       │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  gen-unified (ganha connection: oracle)                                               │
│    restaurants/products/inventory: migram de MinIO (bucket data) para Oracle           │
│    (table/row), insert-only nesta etapa, com sqlHint/tablePolicy:manual na PK          │
│                    │                                                                   │
│                    ▼                                                                   │
│  oracle-ubereats (gvenzl/oracle-free, ARCHIVELOG + supplemental logging)               │
│                    │  LogMiner CDC                                                     │
│                    ▼                                                                   │
│  Kafka Connect + Debezium Oracle connector ──► Redpanda (tópicos oracle.*)             │
│                    │                                                                   │
│                    ▼                                                                   │
│  Databricks Structured Streaming (leitura direta do tópico Kafka) ──► Bronze (novo)    │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│     ETAPA 3 — Mutação real em Pedido/Pagamento no Oracle; aposentar histórico          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  gen-unified: orders/payments migram de MinIO (fork+stateMachine → novo evento         │
│    kafka/status|events) para Oracle (fork+stateMachine → op:update na MESMA linha,     │
│    mesmo padrão provado na Etapa 1). items/receipts seguem os pais para o Oracle       │
│  kafka/status e kafka/events REMOVIDOS do config                                       │
│                    │                                                                   │
│                    ▼  (mesmo caminho Debezium/Kafka Connect/Redpanda da Etapa 2)        │
│  Bronze (orders, payments) com APPLY CHANGES INTO via contrato canônico de CDC         │
└──────────────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────────────┐
│                    Transversal — MongoDB (satélite estático) + MinIO (mantém)          │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  mongo-ubereats: seed único (docker-entrypoint-initdb.d/*.js) — "Perfil de             │
│    Restaurante" (menu + horários), restaurant_id 1..N espelhando o range               │
│    sequencial que o gen-unified vai gerar para restaurants no Oracle                   │
│  MinIO: Entrega, Avaliação, Turno, Incidente + streams fora do core — sem mudança      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

**Contrato canônico de CDC (transversal a Postgres/Airbyte e Oracle/Debezium), aplicado na Bronze:**

| Coluna canônica | De onde vem (Airbyte/Postgres) | De onde vem (Debezium/Oracle, via Kafka) |
|---|---|---|
| `cdc_operation` | derivada de `_ab_cdc_deleted_at` (`I`/`U`/`D`) | `payload.op` (`c`/`u`/`d`) |
| `cdc_commit_ts` | `_ab_cdc_updated_at` | `payload.source.ts_ms` |
| `cdc_sequence` | `_ab_cdc_lsn` | `payload.source.scn` |
| `cdc_source_system` | constante `'postgres-ubereats'` | constante `'oracle-ubereats'` |

A Silver **nunca** lê `_ab_cdc_*` nem `payload.*` diretamente — só as 4 colunas canônicas. Isso é o que permite trocar Airbyte/Debezium por DMS/Datastream nas Fases 2/3 sem reescrever Silver (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` v1.2/1.3).

---

## Decisões (ADRs inline)

### Decisão 1 — Kafka Connect + Debezium precisa de um broker Kafka real; usar Redpanda, não Kafka+Zookeeper

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Data** | 2026-09-06 |

**Contexto:** o projeto hoje não tem nenhum broker Kafka real — todo `kafka/*` no MinIO é só um prefixo de pasta simulado pelo ShadowTraffic. Debezium/Kafka Connect, porém, precisa publicar eventos de CDC reais num broker Kafka de verdade.

**Escolha:** subir **Redpanda** (`redpandadata/redpanda`, 1 único container, API compatível com Kafka) em vez do stack tradicional Kafka+Zookeeper (2-3 containers).

**Racional:** o projeto já tem um histórico de cuidado com footprint de RAM local (Airbyte sozinho consome ~3.8GB — ver `docs/airbyte/README.md`). Redpanda é single-binary, sem Zookeeper, e é 100% compatível com o protocolo Kafka que o Kafka Connect/Debezium esperam — não muda nenhum código de conector.

**Alternativas rejeitadas:**
1. Confluent Kafka + Zookeeper — funciona, mas 2-3 containers a mais rodando 24/7 só para simular CDC de um portfólio local.
2. Debezium Server (modo standalone, sem Kafka Connect) — não precisa de broker Kafka, mas os sinks nativos documentados (Kinesis, Pub/Sub, Redis) não incluem "gravar direto num tópico que o Databricks lê via Spark-Kafka" de forma tão direta quanto um tópico Kafka/Redpanda padrão; também foge do requisito explícito do usuário ("Debezium/Kafka Connect").

**Consequências:** +1 container novo (`redpanda`), +1 container novo (`kafka-connect` rodando a imagem `debezium/connect`). Ambos health-checked como os serviços existentes.

### Decisão 2 — Bronze do Oracle lê direto do tópico Kafka via Spark Structured Streaming, sem Airbyte

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** hoje a Bronze de Postgres é alimentada por Airbyte (que materializa `raw.<tabela>` e a Bronze lê via `STREAM(uber_eats.raw.<tabela>)`). Para o Oracle, o CDC já chega como tópico Kafka (via Debezium/Kafka Connect) — não há motivo para adicionar mais um hop (Airbyte lendo de Kafka) quando o Databricks lê Kafka nativamente.

**Escolha:** a Bronze do Oracle (`ingest_oracle_<tabela>.sql`) lê diretamente do tópico Kafka via `read_stream().format("kafka")`, parseia o envelope Debezium (`payload.before`/`after`/`op`/`source`) e aplica `APPLY CHANGES INTO`, igual ao padrão já usado para Postgres.

**Alternativas rejeitadas:**
1. Rotear o tópico Kafka de volta por um source Kafka do Airbyte, só para manter "tudo passa pelo Airbyte" — hop desnecessário, mais um ponto de falha, sem ganho.

**Consequências:** dois padrões de Bronze CDC coexistem no projeto (Airbyte-based e Kafka-based) — mitigado pelo contrato canônico de CDC (Decisão transversal acima), que unifica o que a Silver enxerga.

### Decisão 3 — `order_id`/`payment_id` migram de UUID para sequencial ao entrarem no Oracle

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** `docs/MODELO_CONCEITUAL_UBER_EATS.md` já registra a decisão de chave canônica das Ondas 1/2: "o ID técnico sequencial vence" para Usuário/Restaurante/Motorista. Pedido/Pagamento hoje usam `_gen: uuid`.

**Escolha:** ao migrarem para o Oracle (Etapa 3), `order_id` e `payment_id` passam de `_gen: uuid` para `_gen: sequentialInteger`, pelo mesmo motivo já documentado (consistência de estilo, join mais barato).

**Alternativas rejeitadas:**
1. Manter UUID no Oracle — evitaria reescrever os 6 lookups que hoje apontam para `kafka/orders.order_id`, mas quebraria a consistência já estabelecida e reintroduziria o tipo de inconsistência de chave que as Ondas 1/2 corrigiram.

**Consequências:** todo consumidor de `order_id`/`payment_id` (Item, Recibo, Entrega, Avaliação, Incidente — os que ficam no MinIO fazendo lookup cross-connection) precisa ser atualizado no mesmo Build. Blast radius já era esperado (ver DEFINE, A-001).

### Decisão 4 — Reaproveitar `fork`+`stateMachine` já existente em `kafka/status`/`kafka/events`, só trocando o alvo

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** inspecionado `gen/unified/uber-eats.json.template` — `kafka/status` (linha ~2257) e `kafka/events` (linha ~1296) **já usam `fork`+`stateMachine`** hoje, para gerar uma sequência de eventos por Pedido/Pagamento. O mecanismo não é 100% novo neste repo — só nunca foi combinado com `op: update` mirando uma `connection` relacional.

**Escolha:** o gerador de `drivers` (Etapa 1) e depois `orders`/`payments` (Etapa 3) reaproveitam a mesma estrutura `fork.key` + `stateMachine.states`, mudando o destino: em vez de `bucket`/`data` (novo objeto no S3 a cada transição), viram `table`/`row` com `op: update` e `where` referenciando a `forkKey` (mesma linha, UPDATE em vez de INSERT novo).

**Consequências:** reduz o risco relativo (mecanismo parcialmente validado no próprio repo), mas não elimina a necessidade do sequenciamento em 3 etapas do DEFINE — a combinação `fork`+`stateMachine`+`op:update` contra uma `connection` real nunca foi testada.

### Decisão 5 — Satélite MongoDB: seed determinístico por range de `restaurant_id`, não por lookup em tempo de execução

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o MongoDB não tem sink de escrita no ShadowTraffic (confirmado no BRAINSTORM) — a coleção "Perfil de Restaurante" não pode ser gerada pelo `gen-unified`. Mas o `restaurant_id` do Oracle é `sequentialInteger` a partir de 1 — **determinístico**.

**Escolha:** um script de seed (`mongo/init/01_perfil_restaurante.js`, montado em `docker-entrypoint-initdb.d/` do `mongo-ubereats`) gera `RESTAURANT_COUNT` documentos com `restaurant_id: 1..N`, onde `RESTAURANT_COUNT` é a mesma env var usada como `maxEvents` do gerador `restaurants` — uma única fonte de verdade para o tamanho da população, referenciada nos dois lugares.

**Alternativas rejeitadas:**
1. Gerar o seed depois de já existir dado de restaurante (ex. via query no Oracle) — adiciona uma dependência de ordem de startup (Mongo dependeria de Oracle já ter dados), contra o padrão de inicialização paralela que o `docker-compose.yml` já usa.

**Consequências:** se `RESTAURANT_COUNT` mudar no futuro, os dois lugares (gerador + seed Mongo) precisam mudar juntos — documentar isso explicitamente no `gen/.env.template`.

### Decisão 6 — Oracle local usa `gvenzl/oracle-free:23-full` (não a tag `slim`), para ARCHIVELOG + LogMiner funcionarem

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** Debezium precisa de `ARCHIVELOG` mode + supplemental logging habilitados no Oracle para capturar CDC via LogMiner (achado do `/intake`, Parte 1.5 do relatório do `@medallion-architect`).

**Escolha:** usar a tag `-full` da imagem `gvenzl/oracle-free`, e rodar um script de inicialização (`sql/oracle/00_enable_archivelog.sql`, montado em `/container-entrypoint-startdb.d/`) que habilita `ARCHIVELOG` + `supplemental logging` na primeira subida.

**Consequências:** imagem maior (~2.25GB) e RAM adicional — reforça a recomendação já existente de rodar geradores/serviços pesados sob demanda, não o tempo todo (mesmo princípio já aplicado ao Airbyte).

### Decisão 7 — Bronze/Silver do Oracle seguem o padrão de nomenclatura por domínio desde o nascimento (não migram depois)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |

**Contexto:** o DEFINE já fixou a convenção de nomear Silver por domínio de negócio (`silver_orders`, não `silver_kafka_orders`).

**Escolha:** toda tabela nova desta feature (Oracle e MongoDB) já nasce com o nome de domínio final. As tabelas Silver **existentes** que migram de origem (`ingestion_kafka_orders.sql` → `ingestion_oracle_orders.sql`, produzindo `silver_orders` em vez de `silver_kafka_orders`) são renomeadas no mesmo Build, não depois.

**Consequências:** Gold (`load_order_unit_economics.sql`, `load_restaurant_performance.sql`) precisa atualizar as referências de tabela Silver no mesmo Build — sem tabela transitória "das duas formas".

---

## File Manifest

### Etapa 1 — Postgres/Motorista (provar mutação)

| # | Arquivo | Ação | Propósito | Dependências |
|---|---------|--------|-----------|---------------|
| 1 | `gen/unified/uber-eats.json.template` | Editar | Reescrever gerador `drivers`: `fork.key=driver_id` + `stateMachine` com estado inicial (INSERT) e transições `op:update` para `status`/`total_deliveries`/`total_earnings`/`average_rating` | — |
| 2 | `pipeline/bronze/ingest_postgres_drivers.sql` | Verificar (provável no-op) | Confirmar que `APPLY CHANGES INTO` + `SEQUENCE BY _ab_cdc_updated_at` já captura UPDATE corretamente com o novo padrão de mutação | 1 |

### Etapa 2 — Oracle plumbing (Restaurante, Produto, Estoque — insert-only)

| # | Arquivo | Ação | Propósito | Dependências |
|---|---------|--------|-----------|---------------|
| 3 | `docker-compose.yml` | Editar | Adicionar serviços: `oracle-ubereats` (`gvenzl/oracle-free:23-full`), `redpanda`, `kafka-connect` (`debezium/connect`) | — |
| 4 | `sql/oracle/00_enable_archivelog.sql` | Criar | Habilita `ARCHIVELOG` + supplemental logging no primeiro boot do Oracle | 3 |
| 5 | `sql/oracle/create_restaurants_table.sql` | Criar | DDL Oracle de `restaurants`, com PK explícita | 3 |
| 6 | `sql/oracle/create_products_table.sql` | Criar | DDL Oracle de `products` | 3 |
| 7 | `sql/oracle/create_inventory_table.sql` | Criar | DDL Oracle de `inventory` (Estoque) | 3 |
| 8 | `gen/unified/uber-eats.json.template` | Editar | Adicionar `connections.oracle`; migrar geradores `restaurants`/`products`/`inventory` de `bucket`/`data` (MinIO) para `table`/`row` (Oracle), com `sqlHint` na PK; atualizar lookups que hoje apontam para `mysql/restaurants`/`mysql/products`/`postgres/inventory` no MinIO para apontar para `connection: oracle` | 5, 6, 7 |
| 9 | `debezium/oracle-restaurants-connector.json` | Criar | Config do connector Debezium Oracle (registrado via REST API do Kafka Connect) | 3, 4 |
| 10 | `pipeline/bronze/ingest_oracle_restaurants.sql` | Criar | Lê tópico Kafka via Structured Streaming, parseia envelope Debezium, `APPLY CHANGES INTO`, projeta as 4 colunas canônicas de CDC | 9 |
| 11 | `pipeline/bronze/ingest_oracle_products.sql` | Criar | Mesmo padrão de 10, para `products` | 9 |
| 12 | `pipeline/bronze/ingest_oracle_inventory.sql` | Criar | Mesmo padrão de 10, para `inventory` | 9 |
| 13 | `pipeline/silver/ingestion_oracle_restaurants.sql` | Criar (substitui `ingestion_mysql_restaurants.sql`) | Silver `silver_restaurants`, lendo da nova Bronze | 10 |
| 14 | `pipeline/silver/ingestion_oracle_products.sql` | Criar (substitui `ingestion_mysql_products.sql`) | Silver `silver_products` | 11 |
| 15 | `pipeline/silver/ingestion_oracle_inventory.sql` | Criar (substitui `ingestion_postgres_inventory.sql`) | Silver `silver_inventory` | 12 |
| 16 | `pipeline/gold/load_restaurant_performance.sql`, `load_order_unit_economics.sql` | Editar | Atualizar referência de `silver_mysql_restaurants` para `silver_restaurants` | 13 |
| 17 | `mongo/init/01_perfil_restaurante.js` | Criar | Seed estático: `RESTAURANT_COUNT` documentos, `restaurant_id: 1..N`, menu + horários | 8 (N deve bater com `maxEvents` de `restaurants`) |
| 18 | `docker-compose.yml` | Editar (mesmo arquivo de #3) | Adicionar serviço `mongo-ubereats` (`mongo:7`), montando `mongo/init/` | 17 |
| 19 | `pipeline/bronze/ingest_mongo_perfil_restaurante.sql` OU leitura direta no Silver | Criar | Ingestão do satélite (population estática — pode ser lida direto via conector Mongo do Spark, sem CDC) | 17, 18 |
| 20 | `pipeline/silver/ingestion_mongo_perfil_restaurante.sql` | Criar | Silver `silver_restaurant_profile`, com validação de FK contra `silver_restaurants` | 19, 13 |

### Etapa 3 — Oracle/Pedido+Pagamento com mutação real; aposentar histórico

| # | Arquivo | Ação | Propósito | Dependências |
|---|---------|--------|-----------|---------------|
| 21 | `sql/oracle/create_orders_table.sql` | Criar | DDL Oracle de `orders`, com `order_id INT PRIMARY KEY` (Decisão 3) | Etapa 2 completa |
| 22 | `sql/oracle/create_payments_table.sql` | Criar | DDL Oracle de `payments` | Etapa 2 completa |
| 23 | `sql/oracle/create_order_items_table.sql` | Criar | DDL Oracle de `order_items` (Item de Pedido) | 21 |
| 24 | `sql/oracle/create_receipts_table.sql` | Criar | DDL Oracle de `receipts` (Recibo) | 22 |
| 25 | `gen/unified/uber-eats.json.template` | Editar | Migrar `orders`/`payments` de `bucket`/`data`+`fork`(→S3) para `table`/`row`+`fork`+`stateMachine`(→`op:update` no Oracle), aplicando o padrão validado na Etapa 1 (Decisão 4); migrar `mongodb/items`→`order_items` e `kafka/receipts`→`receipts` para `table`/`row` no Oracle; **remover** os geradores de `kafka/status` e `kafka/events`; atualizar todo lookup que hoje aponta para `kafka/orders`/`kafka/payments` no MinIO (Entrega, Avaliação, Incidente) para `connection: oracle` | 21-24 |
| 26 | `debezium/oracle-orders-connector.json`, `debezium/oracle-payments-connector.json` | Criar | Configs Debezium para as novas tabelas | 25 |
| 27 | `pipeline/bronze/ingest_oracle_orders.sql`, `ingest_oracle_payments.sql`, `ingest_oracle_order_items.sql`, `ingest_oracle_receipts.sql` | Criar | Mesmo padrão de Bronze Kafka-based da Etapa 2 | 26 |
| 28 | `pipeline/silver/ingestion_oracle_orders.sql` (substitui `ingestion_kafka_orders.sql`) | Criar | Silver `silver_orders` | 27 |
| 29 | `pipeline/silver/ingestion_oracle_payments.sql` (substitui `ingestion_kafka_payments.sql`) | Criar | Silver `silver_payments` | 27 |
| 30 | `pipeline/silver/ingestion_oracle_order_items.sql` (substitui `ingestion_mongodb_items.sql`) | Criar | Silver `silver_order_items` | 27 |
| 31 | `pipeline/silver/ingestion_oracle_receipts.sql` (substitui `ingestion_kafka_receipts.sql`) | Criar | Silver `silver_receipts` | 27 |
| 32 | `pipeline/silver/ingestion_kafka_route.sql`, `ingestion_mysql_ratings.sql`, `ingestion_mongodb_support.sql` | Editar | Atualizar lookup de `order_id` para a nova origem (`silver_orders`/Oracle em vez de `kafka/orders`/MinIO) | 28 |
| 33 | `pipeline/silver/ingestion_kafka_status.sql`, `ingestion_kafka_events.sql` | Remover | Streams aposentados — status/eventos viram a própria mutação da linha em `silver_orders`/`silver_payments` | 25 |
| 34 | `pipeline/gold/load_order_unit_economics.sql` | Editar | Atualizar todas as referências de Silver renomeada | 28, 29 |
| 35 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Editar | Estado final: 4 sistemas, entidade nova (Perfil de Restaurante), streams aposentados, tabela de nomenclatura antiga→nova | Todas |

### Transversal (contrato de CDC, independente da etapa)

| # | Arquivo | Ação | Propósito |
|---|---------|--------|-----------|
| 36 | `pipeline/bronze/_cdc_contract_view.sql` (nome sugerido) ou view inline em cada Bronze | Criar | Projeta `cdc_operation`/`cdc_commit_ts`/`cdc_sequence`/`cdc_source_system` a partir de `_ab_cdc_*` (Postgres) ou `payload.*` (Oracle/Debezium) — aplicado em `ingest_postgres_*.sql` (retrofit) e em todos os `ingest_oracle_*.sql` novos |

---

## Code Patterns

### 1. Gerador `drivers` com mutação real (Etapa 1)

```json
{
  "table": "drivers",
  "fork": {
    "key": { "_gen": "sequentialInteger", "startingFrom": 1 },
    "maxForks": 5000,
    "keepAlive": true
  },
  "stateMachine": {
    "_gen": "stateMachine",
    "initial": "insertIt",
    "transitions": {
      "insertIt": "goingOnline",
      "goingOnline": "goingOffline",
      "goingOffline": "goingOnline"
    },
    "states": {
      "insertIt": {
        "row": {
          "driver_id": { "_gen": "var", "var": "forkKey" },
          "name": { "_gen": "string", "expr": "#{Name.fullName}" },
          "status": { "value": "offline" },
          "total_deliveries": { "value": 0 },
          "total_earnings": { "value": 0.0 },
          "average_rating": { "value": 0.0 }
        }
      },
      "goingOnline": {
        "op": "update",
        "where": { "driver_id": { "_gen": "var", "var": "forkKey" } },
        "row": {
          "status": { "value": "available" },
          "total_deliveries": { "_gen": "math", "expr": "prev + 1" },
          "average_rating": { "_gen": "uniformDistribution", "bounds": [3.5, 5.0], "decimals": 1 }
        }
      },
      "goingOffline": {
        "op": "update",
        "where": { "driver_id": { "_gen": "var", "var": "forkKey" } },
        "row": { "status": { "value": "offline" } }
      }
    }
  },
  "connection": "postgres"
}
```

> Nota: campos de cadastro (email, telefone, veículo etc.) permanecem no estado `insertIt`, sem mudança — só os campos mutáveis (Goals da feature) entram nas transições de UPDATE.

### 2. Gerador `restaurants` migrado para Oracle (Etapa 2, insert-only)

```json
{
  "table": "restaurants",
  "sqlHint": {
    "restaurant_id": "NUMBER(10) PRIMARY KEY"
  },
  "row": {
    "restaurant_id": { "_gen": "sequentialInteger", "startingFrom": 1 },
    "name": { "_gen": "string", "expr": "#{Company.name} Restaurante", "locale": ["pt", "BR"] },
    "cuisine_type": { "_gen": "oneOf", "choices": ["Italian", "Chinese", "Japanese", "Mexican", "Indian", "American", "French"] },
    "average_rating": { "_gen": "uniformDistribution", "bounds": [0.0, 5.0], "decimals": 1 },
    "lat": { "_gen": "uniformDistribution", "bounds": [-23.6, -23.55], "decimals": 6 },
    "lon": { "_gen": "uniformDistribution", "bounds": [-46.65, -46.6], "decimals": 6 }
  },
  "connection": "oracle"
}
```

> `sqlHint` força o tipo/constraint exato na DDL auto-gerada (Constraint da Decisão de PK — sem isso, LogMiner não replica UPDATE/DELETE nessa tabela).

### 3. `docker-compose.yml` — serviços novos (Etapa 2)

```yaml
  oracle-ubereats:
    image: gvenzl/oracle-free:23-full
    container_name: oracle-ubereats
    ports:
      - "1521:1521"
    env_file: ./gen/.env
    environment:
      - ORACLE_PASSWORD=${ORACLE_PASSWORD}
    volumes:
      - oracle_data:/opt/oracle/oradata
      - ./sql/oracle:/container-entrypoint-startdb.d
    healthcheck:
      test: ["CMD", "healthcheck.sh"]
      interval: 20s
      timeout: 10s
      retries: 10

  redpanda:
    image: redpandadata/redpanda:latest
    container_name: redpanda
    command:
      - redpanda start --smp 1 --memory 1G --overprovisioned --node-id 0
        --kafka-addr PLAINTEXT://0.0.0.0:9092 --advertise-kafka-addr PLAINTEXT://redpanda:9092
    ports:
      - "9092:9092"

  kafka-connect:
    image: debezium/connect:2.7
    container_name: kafka-connect
    depends_on:
      - redpanda
      - oracle-ubereats
    environment:
      - BOOTSTRAP_SERVERS=redpanda:9092
      - GROUP_ID=uber-eats-connect
      - CONFIG_STORAGE_TOPIC=connect_configs
      - OFFSET_STORAGE_TOPIC=connect_offsets
      - STATUS_STORAGE_TOPIC=connect_status
    ports:
      - "8083:8083"

  mongo-ubereats:
    image: mongo:7
    container_name: mongo-ubereats
    ports:
      - "27017:27017"
    volumes:
      - mongo_data:/data/db
      - ./mongo/init:/docker-entrypoint-initdb.d
```

### 4. Connector Debezium Oracle (registrado via `POST http://localhost:8083/connectors`)

```json
{
  "name": "oracle-restaurants-connector",
  "config": {
    "connector.class": "io.debezium.connector.oracle.OracleConnector",
    "database.hostname": "oracle-ubereats",
    "database.port": "1521",
    "database.user": "c##dbzuser",
    "database.password": "${env:ORACLE_DBZ_PASSWORD}",
    "database.dbname": "FREE",
    "topic.prefix": "oracle",
    "schema.include.list": "UBEREATS",
    "table.include.list": "UBEREATS.RESTAURANTS,UBEREATS.PRODUCTS,UBEREATS.INVENTORY"
  }
}
```

### 5. Bronze Kafka-based com contrato de CDC canônico (`ingest_oracle_restaurants.sql`)

```sql
CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_restaurants_raw AS
SELECT
  from_json(CAST(value AS STRING), '<schema Debezium envelope>') AS payload
FROM STREAM(kafka.`oracle.UBEREATS.RESTAURANTS`);

CREATE TEMPORARY STREAMING LIVE VIEW view_oracle_restaurants_pre_processed AS
SELECT
  payload.after.*,
  payload.op                                          AS cdc_operation,
  CAST(payload.source.ts_ms AS TIMESTAMP)             AS cdc_commit_ts,
  payload.source.scn                                  AS cdc_sequence,
  'oracle-ubereats'                                   AS cdc_source_system,
  current_timestamp()                                 AS _datetime_ingestion
FROM STREAM(live.view_oracle_restaurants_raw);

CREATE OR REFRESH STREAMING TABLE ods_oracle_restaurants
COMMENT "ODS de restaurantes, origem Oracle via Debezium/Kafka Connect.";
APPLY CHANGES INTO
  uber_eats.bronze.ods_oracle_restaurants
FROM STREAM(live.view_oracle_restaurants_pre_processed)
KEYS(restaurant_id)
APPLY AS DELETE WHEN cdc_operation = 'd'
SEQUENCE BY cdc_sequence
STORED AS SCD TYPE 1;
```

> Mesmo padrão de `ingest_postgres_drivers.sql`, só trocando a origem (Kafka em vez de `STREAM(uber_eats.raw.*)`) e o `SEQUENCE BY` (SCN do Oracle, monotônico, em vez de timestamp — evita empate em rajada de updates, risco já sinalizado no BRAINSTORM).

### 6. Silver renomeada por domínio (`ingestion_oracle_restaurants.sql`)

Mesmo padrão de 5 seções (leitura → normalização → tipagem → limpeza → metadados) já usado em `ingestion_postgres_drivers.sql`, produzindo `silver.silver_restaurants` (não `silver_mysql_restaurants`).

---

## Correções pós-teste real (Build da Etapa 2)

O Design original acertou a arquitetura geral, mas **7 detalhes concretos só apareceram testando de verdade** (Oracle+Redpanda+Kafka Connect reais, não só leitura de doc). Registrados aqui para quem for implementar Etapa 3 no mesmo padrão:

| # | O que o Design assumia | O que a realidade exigiu | Onde |
|---|---|---|---|
| 1 | `gvenzl/oracle-free:23-full` (tag rolling) | A tag rolante resolveu para uma versão muito recente ("Oracle AI Database 26ai", `version_full=23.26.3.0.0`) cujo formato de versão o parser do Debezium (testado 2.7 **e** 3.0) não reconhece (`Failed to resolve Oracle database version`). Fixar em `gvenzl/oracle-free:23.4-full` (versão clássica, `23.4.0.24.05`) resolveu | `docker-compose.yml` |
| 2 | `image: debezium/connect:2.7` (Docker Hub) | Não existe nessa tag/registro — a imagem oficial atual é `quay.io/debezium/connect`, não `docker.io/debezium/connect`. E `2.7` não tem build compatível com a versão do Oracle acima; `3.0` funcionou | `docker-compose.yml` |
| 3 | `connectionConfigs.serviceName` para a conexão Oracle do ShadowTraffic | O ShadowTraffic rejeita a config (`required key [db] not found`) — o campo certo é `db`, igual ao Postgres, não `serviceName` | `gen/unified/uber-eats.json.template` |
| 4 | Connector Debezium só com `connector.class`/credenciais/`table.include.list` | Faltavam `schema.history.internal.kafka.bootstrap.servers` e `schema.history.internal.kafka.topic` (obrigatórios para conectores relacionais historizados) — sem eles a task falha ao iniciar (`Error configuring an instance of KafkaSchemaHistory`) | `debezium/oracle-connector.json.template` |
| 5 | Colunas `NUMBER` do Oracle chegariam como número no JSON | Sem `decimal.handling.mode`, o Debezium serializa `NUMBER` como bytes base64 (`"LQ=="`) quando `schemas.enable=false` — inutilizável pro `CAST` do Bronze. `decimal.handling.mode: double` resolve (troca precisão exata por simplicidade — reavaliar para `payments` na Etapa 3, onde precisão importa mais) | `debezium/oracle-connector.json.template` |
| 6 | Colunas de data (`created_at`, `updated_at`, `last_updated`) como `TIMESTAMP` no Oracle | `ORA-01843: invalid month` — o ShadowTraffic escreve a data como string no formato `yyyy-MM-dd HH:mm:ss` e o Oracle tenta conversão implícita com o `NLS_DATE_FORMAT` da sessão, que não bate. Same fix que o projeto já usa no Postgres (`sql/create_users_table.sql`): guardar como `VARCHAR2`, converter para `TIMESTAMP` só na Silver | `sql/oracle/02_create_tables.sh`, Bronze/Silver de `products`/`inventory` |
| 7 | FKs explícitas (`fk_products_restaurant`, `fk_inventory_restaurant`, `fk_inventory_product`) no DDL Oracle | `ORA-02291: integrity constraint violated` — o ShadowTraffic faz lookup por valor **já gerado** (lógico), mas a escrita em conexões/tabelas diferentes não é sincronizada fisicamente; o commit do pai pode não ter acontecido ainda. Removidas as FKs, mesmo padrão que `users`/`drivers` (que também não têm FK) — integridade é validada por join real no Gold, não por constraint | `sql/oracle/02_create_tables.sh` |

**Achado operacional adicional (não é bug de config, é timing):** o healthcheck do `oracle-ubereats` pode reportar "healthy" numa janela estreita antes do listener terminar de registrar o serviço `FREEPDB1` (`ORA-12514`) ou antes do ciclo shutdown/mount/archivelog/open do `00_enable_archivelog.sql` terminar (`ORA-01109: database not open`). Ambos são **transitórios** — um `docker-compose up -d --force-recreate gen-unified` alguns segundos depois resolve. Não bloqueante, mas documentar para quem for automatizar isso (ex.: `start-all.ps1` futuramente esperar mais um pouco após Oracle "healthy" antes de subir `gen-unified`, se isso incomodar no dia a dia).

---

## Testing Strategy

| Tipo de teste | Escopo | Quando |
|---|---|---|
| Validação estática (grep/JSON parse) | `gen/unified/uber-eats.json.template` válido; 0 referências soltas a `kafka/status`/`kafka/events`/`mysql/restaurants` etc. após cada etapa | Build, antes de regenerar dados (mesmo padrão das Ondas 1/2) |
| Smoke test de mutação (Etapa 1) | `SELECT status FROM drivers WHERE driver_id=1` muda de valor entre duas leituras, sem novo `driver_id` | Manual, após subir `gen-unified` com o gerador novo |
| Smoke test de CDC Oracle (Etapa 2) | Registrar o connector via REST API; confirmar mensagens chegando no tópico `oracle.UBEREATS.RESTAURANTS` (`kcat`/`rpk topic consume`) | Manual, antes de escrever a Bronze |
| Join de integridade (Etapa 2 e 3) | Mesma disciplina das Ondas 1/2: 0 órfãos nos joins entre Silver renomeada e os consumidores (Entrega/Avaliação/Incidente → Oracle; Perfil de Restaurante → Oracle) | Pipeline Databricks completo, Bronze→Silver→Gold |
| `/pipeline-review-init` | Lane `data_contracts`, `architecture_medallion`, `idempotency_reprocessing` no mínimo (mandato MED-M04 do DEFINE) | Após o Build completo, antes de considerar a Onda 3 encerrada |

---

## Riscos carregados do DEFINE (com mitigação de design)

| Risco (DEFINE) | Mitigação de design |
|---|---|
| A-001 — fork+stateMachine pode não escalar de Motorista para Pedido (blast radius maior) | Decisão 4 reduz o risco (mecanismo já parcialmente validado no repo via `kafka/status`); sequenciamento do DEFINE mantido (Etapa 1 antes de 3) |
| A-002 — Oracle local pode não suportar LogMiner sem custo | Decisão 6 (tag `-full` + script de ARCHIVELOG) é a mitigação direta; se falhar, é um blocker de Build a escalar antes de prosseguir — não further design necessário |
| A-003 — lookup cross-connection MinIO→Oracle pode se comportar diferente de MinIO→Postgres | Mesma mecânica de `_gen: lookup` com `connection: oracle` em vez de `connection: postgres` — sintaxe idêntica à já usada para `postgres.users`/`postgres.drivers` nos itens 25/32 do manifesto; validar no Build com o mesmo teste de integridade das Ondas 1/2 |
| A-004 — Gold pode ter suposições implícitas sobre origem MinIO além da chave | Itens 16/34 do manifesto tratam isso explicitamente — grep por `silver_kafka_orders`/`silver_mysql_restaurants` antes de considerar o Build completo |

---

## Status: ✅ Complete (Designed)

**Próximo passo:** `/build .claude/sdd/features/DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md`
