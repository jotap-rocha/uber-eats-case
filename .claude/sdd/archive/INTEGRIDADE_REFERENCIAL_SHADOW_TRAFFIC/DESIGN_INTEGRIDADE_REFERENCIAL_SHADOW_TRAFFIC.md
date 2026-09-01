# DESIGN: Correção de Integridade Referencial do Shadow Traffic (Onda 1)

| Campo | Valor |
|-------|-------|
| **Feature** | INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC |
| **Input** | `.claude/sdd/features/DEFINE_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md` |
| **Status** | ✅ Shipped |
| **Data** | 2026-08-24 |

---

## Architecture Overview

```text
┌──────────────────────────────────────────────────────────────────────────────┐
│                    FLUXO DE CORREÇÃO E VALIDAÇÃO                              │
├──────────────────────────────────────────────────────────────────────────────┤
│                                                                                │
│  [1] gen/minio/uber-eats.json (gerador)                                       │
│      - remove orders.payment_key, orders.rating_key                          │
│      - orders.restaurant_key: cnpj → restaurant_id                          │
│      - mongodb/items.product_id: gerado próprio → lookup mysql/products      │
│      - mysql/ratings: + order_id (lookup orders); - restaurant_identifier   │
│      - mysql/restaurants: + lat, lon                                         │
│      - kafka/route.start_lat/lon: aleatório → lookup mysql/restaurants      │
│                    │                                                         │
│                    ▼                                                         │
│  [2] Regenerar dados (Shadow Traffic → MinIO)                                │
│                    │                                                         │
│                    ▼                                                         │
│  [3] Bronze (Auto Loader, sem alteração)                                     │
│                    │                                                         │
│                    ▼                                                         │
│  [4] Silver — 3 scripts editados                                            │
│      ingestion_kafka_orders.sql | ingestion_kafka_ratings.sql               │
│      ingestion_mysql_restaurants.sql                                        │
│      (ingestion_kafka_route.sql e ingestion_mongodb_items.sql: SEM          │
│       mudança — já tratam as colunas afetadas genericamente)                │
│                    │                                                         │
│                    ▼                                                         │
│  [5] Gold — 2 scripts editados                                              │
│      load_order_unit_economics.sql | load_restaurant_performance.sql        │
│      (join cnpj_restaurante=cnpj → id_restaurante=id_restaurante)           │
│                    │                                                         │
│                    ▼                                                         │
│  [6] Validação: join real no Gold, 6 acceptance tests                       │
│                    │                                                         │
│                    ▼                                                         │
│  [7] docs/MODELO_CONCEITUAL_UBER_EATS.md atualizado (estado real + Onda 2)  │
│                                                                                │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Decisões de Arquitetura (ADRs inline)

### Decisão: Remover `payment_key` e `rating_key` de `kafka/orders`, em vez de "corrigir o lookup"

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** O DEFINE previa corrigir `orders.payment_key` fazendo lookup em `kafka/payments.payment_id`. Ao desenhar a implementação, isso se mostrou **circular**: `kafka/payments.order_key` já faz lookup em `kafka/orders.order_id` (pagamento depende do pedido já existir). Se `orders.payment_key` também dependesse de `kafka/payments` já existir, nenhum dos dois poderia ser gerado primeiro. O mesmo raciocínio já se aplicava a `rating_key` (por isso a decisão do Brainstorm já era adicionar `mysql/ratings.order_id`, tornando `orders.rating_key` redundante).

**Escolha:** Remover `orders.payment_key` e `orders.rating_key` inteiramente. A relação pedido↔pagamento já existe corretamente via `kafka/payments.order_key`; pedido↔avaliação via `mysql/ratings.order_id` (já decidido).

**Racional:** Os dois scripts Gold existentes (`load_order_unit_economics.sql`, `load_restaurant_performance.sql`) já fazem `JOIN silver_kafka_payments p ON o.id_pedido = p.id_pedido` — nunca usaram `payment_key`/`id_pagamento` do lado do pedido. Nenhum consumidor downstream depende desses campos. Removê-los não quebra nada e elimina o UUID órfão.

**Alternativas Rejeitadas:**
1. Manter `payment_key` como lookup em `kafka/payments.payment_id` — tecnicamente circular, ShadowTraffic não teria como resolver a ordem de geração.

**Consequências:** O manifesto de arquivos muda em relação ao Define original — nenhuma mudança na Silver para expor `id_pagamento`/`id_classificacao` do lado do pedido, já que esses campos deixam de existir na origem.

---

### Decisão: `Entrega.start_lat/lon` aponta para um restaurante real, não necessariamente o do mesmo pedido

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** O mecanismo `_gen: lookup` do ShadowTraffic amostra um registro **aleatório** já gerado do stream referenciado — não existe evidência no gerador atual de um lookup encadeado (pedido → restaurante do pedido → lat/lon desse restaurante). Amarrar a coordenada de partida exatamente ao restaurante do mesmo pedido exigiria uma segunda camada de lookup não verificada.

**Escolha:** `kafka/route.start_lat/start_lon` passa a fazer lookup em `mysql/restaurants.lat`/`lon` (coordenada real de *algum* restaurante), em vez de `uniformDistribution` numa bounding box sem relação com nada.

**Racional:** Resolve o problema central do gap (coordenada 100% sintética, sem qualquer ligação com dado real) sem depender de uma capacidade não confirmada. É uma melhoria real e verificável, mesmo não sendo a solução completa.

**Alternativas Rejeitadas:**
1. Investigar lookup em 2 níveis agora — risco de não funcionar e reverter, colocando a feature inteira em risco.

**Consequências:** AT-005 é revisado — passa a verificar que a coordenada de partida corresponde a **um** restaurante real existente (não mais aleatória fora de qualquer stream), não que corresponde ao restaurante específico do pedido. Amarrar ao restaurante exato do pedido fica registrado como item futuro (Onda 2/3).

---

### Decisão: Gold precisa de ajuste (resolve Open Question do Define)

| Atributo | Valor |
|----------|-------|
| **Status** | Accepted |
| **Date** | 2026-08-24 |

**Contexto:** O Define registrou como pendência (A-003) se os scripts Gold precisariam de ajuste. Confirmado: `load_order_unit_economics.sql` e `load_restaurant_performance.sql` fazem `JOIN ... ON o.cnpj_restaurante = r.cnpj`.

**Escolha:** Ambos os scripts Gold são editados para usar `id_restaurante` como chave de join, mantendo `cnpj` como atributo descritivo de saída (não eliminado, só deixa de ser chave).

**Racional:** Consistente com a decisão de chave canônica já tomada no modelo conceitual (ID técnico vence, chave natural vira atributo).

**Alternativas Rejeitadas:** nenhuma — não fazer esse ajuste quebraria o Gold assim que a Silver deixasse de expor `cnpj_restaurante`.

**Consequências:** 2 arquivos Gold entram no manifesto desta feature, além dos 3 Silver.

---

## File Manifest

| # | Arquivo | Ação | Mudança | Agente |
|---|---------|------|---------|--------|
| 1 | `gen/minio/uber-eats.json` | Edit | Remove `orders.payment_key`, `orders.rating_key`; `orders.restaurant_key` → lookup `restaurant_id`; `mongodb/items.product_id` → lookup `mysql/products.product_id`; `mysql/ratings`: + `order_id` (lookup orders), − `restaurant_identifier`; `mysql/restaurants`: + `lat`, `lon`; `kafka/route.start_lat/lon` → lookup `mysql/restaurants` | (direto) |
| 2 | `pipeline/silver/ingestion_kafka_orders.sql` | Edit | Remove colunas `id_classificacao`, `id_pagamento` do lado do pedido; renomeia `cnpj_restaurante` → `id_restaurante` | `@databricks-data-engineer` |
| 3 | `pipeline/silver/ingestion_kafka_ratings.sql` | Edit | Remove `cnpj_restaurante`; adiciona `id_pedido` (lookup); corrige nome enganoso `uuid` → `id_avaliacao_uuid` (não é usuário) | `@databricks-data-engineer` |
| 4 | `pipeline/silver/ingestion_mysql_restaurants.sql` | Edit | Adiciona `latitude`, `longitude` | `@databricks-data-engineer` |
| 5 | `pipeline/gold/load_order_unit_economics.sql` | Edit | Join `o.id_restaurante = r.id_restaurante` em vez de `cnpj` | `@databricks-pipeline-architect` |
| 6 | `pipeline/gold/load_restaurant_performance.sql` | Edit | Join `t.id_restaurante = r.id_restaurante`; mantém `r.cnpj` como atributo de saída | `@databricks-pipeline-architect` |
| 7 | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Edit | Reflete estado real pós-Build + pendências Onda 2 | (direto) |

**Sem alteração** (confirmado no Design, já tratam as colunas genericamente): `pipeline/silver/ingestion_kafka_route.sql`, `pipeline/silver/ingestion_mongodb_items.sql`.

---

## Content Patterns

### Gerador — `gen/minio/uber-eats.json`

```jsonc
// kafka/orders — REMOVER estes dois campos do bloco "data":
"rating_key": { "_gen": "lookup", "bucket": "uber-eats", "keyPrefix": "mysql/ratings/", "path": ["data", "uuid"] },
"payment_key": { "_gen": "uuid" },

// kafka/orders — TROCAR restaurant_key:
"restaurant_key": {
  "_gen": "lookup", "bucket": "uber-eats",
  "keyPrefix": "mysql/restaurants/", "path": ["data", "restaurant_id"]
},

// mongodb/items — TROCAR product_id:
"product_id": {
  "_gen": "lookup", "bucket": "uber-eats",
  "keyPrefix": "mysql/products/", "path": ["data", "product_id"]
},

// mysql/restaurants — ADICIONAR ao bloco "data":
"lat": { "_gen": "uniformDistribution", "bounds": [-23.60, -23.55], "decimals": 6 },
"lon": { "_gen": "uniformDistribution", "bounds": [-46.65, -46.60], "decimals": 6 },

// mysql/ratings — REMOVER restaurant_identifier, ADICIONAR order_id:
"order_id": {
  "_gen": "lookup", "bucket": "uber-eats",
  "keyPrefix": "kafka/orders/", "path": ["data", "order_id"]
},

// kafka/route — TROCAR start_lat/start_lon (mantém end_lat/end_lon como estão, Onda 2):
"start_lat": {
  "_gen": "lookup", "bucket": "uber-eats",
  "keyPrefix": "mysql/restaurants/", "path": ["data", "lat"]
},
"start_lon": {
  "_gen": "lookup", "bucket": "uber-eats",
  "keyPrefix": "mysql/restaurants/", "path": ["data", "lon"]
},
```

### Silver — `ingestion_kafka_orders.sql` (trecho `typed_table`)

```sql
-- Remover as linhas de rating_key e payment_key; renomear restaurant_key:
CAST(order_id AS STRING)      AS id_pedido,
CAST(user_key AS STRING)      AS cpf_usuario,        -- Onda 2: mantém como está
CAST(driver_key AS STRING)    AS id_motorista,        -- Onda 2: mantém como está
CAST(order_date AS TIMESTAMP) AS data_pedido,
CAST(total_amount AS DECIMAL(18, 2)) AS valor_pedido,
CAST(restaurant_key AS STRING) AS id_restaurante
```

### Silver — `ingestion_kafka_ratings.sql` (trecho `typed_table`)

```sql
CAST(rating_id AS STRING)     AS id_avaliacao,
CAST(uuid AS STRING)          AS id_avaliacao_uuid,   -- renomeado: não é usuário
CAST(order_id AS STRING)      AS id_pedido,           -- novo
CAST(rating AS DECIMAL(3, 1)) AS nota_avaliacao,
CAST(timestamp AS TIMESTAMP)  AS data_avaliacao
```

### Silver — `ingestion_mysql_restaurants.sql` (adicionar em `typed_table`, `cleansed_table` e manter no `silver_table`)

```sql
-- typed_table:
CAST(lat AS DOUBLE) AS latitude,
CAST(lon AS DOUBLE) AS longitude,

-- cleansed_table:
COALESCE(latitude, 0.0)  AS latitude,
COALESCE(longitude, 0.0) AS longitude,
```

### Gold — `load_order_unit_economics.sql`

```sql
-- orders_metrics CTE: trocar o.cnpj_restaurante por o.id_restaurante
-- JOIN final: trocar
LEFT JOIN silver_mysql_restaurants r ON m.cnpj_restaurante = r.cnpj;
-- por:
LEFT JOIN silver_mysql_restaurants r ON m.id_restaurante = r.id_restaurante;
```

### Gold — `load_restaurant_performance.sql`

```sql
-- transacoes_validas CTE: trocar o.cnpj_restaurante por o.id_restaurante
-- JOIN final: trocar
LEFT JOIN transacoes_validas t ON r.cnpj = t.cnpj_restaurante
-- por:
LEFT JOIN transacoes_validas t ON r.id_restaurante = t.id_restaurante
-- GROUP BY: adicionar r.id_restaurante; manter r.cnpj como atributo de saída
```

---

## Estratégia de Verificação

| ID | Verificação | Como checar | Cobre |
|----|--------------|--------------|-------|
| V-001 | Gerador sem campos removidos | `grep -c "payment_key\|rating_key" gen/minio/uber-eats.json` retorna 0 | ADR payment_key/rating_key |
| V-002 | Dados regenerados sem órfãos: pedido↔pagamento | Join `silver_kafka_orders` ↔ `silver_kafka_payments` por `id_pedido` no Databricks — 0 órfãos | AT-001 (revisado: join por id_pedido, não payment_key) |
| V-003 | Dados regenerados sem órfãos: item↔produto | Join `silver_mongodb_items` ↔ `silver_mysql_products` por `id_produto` — 0 órfãos | AT-002 |
| V-004 | Dados regenerados sem órfãos: pedido↔restaurante | Join `silver_kafka_orders` ↔ `silver_mysql_restaurants` por `id_restaurante` — 0 órfãos; nenhuma coluna usa `cnpj` como chave | AT-003 |
| V-005 | Avaliação ligada ao pedido | Join `silver_mysql_ratings` ↔ `silver_kafka_orders` por `id_pedido` — 100% com correspondência | AT-004 |
| V-006 | Coordenada de restaurante real (revisado) | `silver_kafka_route.latitude_inicial`/`longitude_inicial` correspondem a um `latitude`/`longitude` existente em `silver_mysql_restaurants` (não necessariamente do mesmo pedido) | AT-005 revisado |
| V-007 | Gold ajustado | `load_order_unit_economics` e `load_restaurant_performance` executam sem erro e retornam resultado não-vazio após a mudança de chave de join | Decisão "Gold precisa de ajuste" |
| V-008 | Modelo documentado atualizado | `docs/MODELO_CONCEITUAL_UBER_EATS.md` revisado manualmente contra o estado final do gerador/Silver/Gold | AT-006 |

---

## Testing Strategy

| Tipo | Escopo | Como |
|------|--------|------|
| Estático | Gerador JSON válido | `python -c "import json; json.load(open('gen/minio/uber-eats.json'))"` |
| Estático | SQL sem referência a colunas removidas | `grep -rn "cnpj_restaurante\|id_classificacao\|id_pagamento" pipeline/` deve retornar só ocorrências esperadas (ou nenhuma, após a correção) |
| Integração | Regeneração + join real | Rodar Shadow Traffic → MinIO → pipeline Databricks completo (Bronze→Silver→Gold) → executar V-002 a V-007 |

---

## Atualização de Status (após Build)

Ao concluir o BUILD, atualizar:
- `DEFINE_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md`: Status → `✅ Complete (Built)`; Next Step → `/ship`
- Este `DESIGN_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md`: Status → `✅ Complete (Built)`; Next Step → `/ship`

---

## Status: ⚠️ Complete (Built) — validação de integração pendente

**Próximo passo:** Regenerar dados + validar joins no Databricks; depois `/ship`
