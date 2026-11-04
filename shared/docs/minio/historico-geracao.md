# MinIO: histórico da geração

O MinIO saiu do escopo da Fase 0 pela [ADR 010](../../../docs/adr/010-minio-fora-do-escopo-da-geracao.md). Este documento
guarda o que o ShadowTraffic gravava nele até 2026-11-04 (template `shared/gen/unified/uber-eats.json.template`, antes da
regeração), para que a geração possa ser refeita no futuro. Não contém dados, só a estrutura e a lógica.

## Armazenamento

| Item | Valor |
|---|---|
| Serviço | `minio-ubereats` (`minio/minio`), API na porta 9000 e console na 9001; volume `minio_data` |
| Credenciais | `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY` do `shared/gen/.env` (nunca no git) |
| Bucket | `uber-eats`, criado pelo serviço `minio-setup` (`mc mb --ignore-existing`) |
| Conexão no ShadowTraffic | `kind: s3`, `endpoint: http://minio-ubereats:9000`, `pathStyleAccess: true` |
| Formato | JSONL (`bucketConfigs.format: jsonl`), um objeto por evento, em `<keyPrefix>` |
| Prefixo | `<origem simulada>/<entidade>/`. A origem (`kafka`, `mysql`, `mongodb`) era só um rótulo: nenhum desses sistemas rodava |
| Ritmo | Os 8 geradores não tinham `localConfigs` (sem `throttleMs` nem `maxEvents`): rodavam no ritmo padrão do ShadowTraffic |
| Campo comum | `dt_current_timestamp`, hora da geração (`now`) em `yyyy-MM-dd HH:mm:ss.SSS` (todos menos `kafka/search`) |

Os `lookup` apontavam para as tabelas **antigas**, antes da [ADR 006](../../../docs/adr/006-inversao-de-dominios-entre-oracle-e-postgres.md):
`users` e `drivers` no Postgres; `orders`, `products` e `restaurants` no Oracle. Cada `lookup` sorteava uma linha
independente, então campos de um mesmo evento podiam vir de linhas sem relação entre si (ver "Incoerências conhecidas").

## Arquivos

Notação: `uuid` = `_gen: uuid`; `U[a,b]` = `uniformDistribution` com as casas decimais indicadas; `oneOf` = sorteio uniforme
na lista; `lookup T.c` = coluna `c` de uma linha qualquer da tabela `T`; datas em `formatDateTime`.

### `kafka/shift/` (turno do motorista)

| Campo | Lógica |
|---|---|
| `shift_id` | uuid |
| `driver_id` | lookup Postgres `drivers.driver_id` |
| `start_time` | var `shift_start` = U[2021-01-01, agora] em ms, formato `yyyy-MM-dd HH:mm:ss` |
| `end_time` | `shift_start + shift_duration_ms`, com `shift_duration_ms` = U[1 h, 8 h] |
| `shift_duration_min` | `shift_duration_ms / 60000` (formato `#.#####`) |
| `available` | boolean |
| `city` | lookup Postgres `drivers.city` |
| `region` | fixo `BR` |
| `shift_type` | oneOf `Morning`, `Afternoon`, `Evening`, `Overnight` |
| `device_os` | oneOf `iOS`, `Android` |
| `login_method` | oneOf `App`, `Web`, `Partner Kiosk` |
| `num_orders` | var U[0, 15] inteiro |
| `distance_covered_km` | U[0, 50], 2 casas |
| `earnings_brl` | `num_orders × payout_per_order`, com `payout_per_order` = U[5, 20], 2 casas (formato `#.##`) |
| `shift_rating` | U[3, 5], 2 casas |
| `issues_reported` | oneOf `None`, `Late Start`, `Low Battery`, `App Crash`, `Lost GPS`, `Accident` |

Destino no modelo novo: tabela `shifts` no Postgres (L1b, decisão 13).

### `kafka/route/` (rota da entrega)

| Campo | Lógica |
|---|---|
| `route_id` | uuid |
| `order_id` | lookup Oracle `orders.order_id` |
| `driver_id` | lookup Postgres `drivers.driver_id` |
| `start_lat`, `start_lon` | lookup Oracle `restaurants.lat` e `restaurants.lon` |
| `end_lat`, `end_lon` | lookup Postgres `users.lat` e `users.lon` |
| `distance_km` | U[0,5, 10], 2 casas |
| `estimated_duration_min` | U[5, 45] inteiro |
| `start_time` | var `start_ts_ms` = U[2021-01-01, agora], formato `yyyy-MM-dd HH:mm:ss` |
| `end_time` | `start_ts_ms + travel_time_ms`, com `travel_time_ms` = U[5 min, 45 min] |

Destino no modelo novo: tabela `deliveries` no Postgres (L1b, decisão 13).

### `kafka/gps/` (pontos de rastreio)

Gerador com `fork`: uma linha do tempo por `order_id` lido do próprio bucket (`lookup` em `kafka/route/`, caminho
`data.order_id`), até 20 em paralelo (`maxForks: 20`).

| Campo | Lógica |
|---|---|
| `gps_id` | uuid |
| `order_id` | `forkKey` (o `order_id` da rota) |
| `lat`, `lon`, `direction_deg`, `duration_ms` | var `gps_point` = `geoWander` na caixa [-23,6, -46,7] a [-23,5, -46,6] (São Paulo), `speed: 15`, `scale: 0.02`; campos `latitude`, `longitude`, `heading`, `duration` |
| `speed_kph` | fixo 15 |
| `accuracy_m` | U[5, 50], 1 casa |
| `altitude` | U[700, 780], 1 casa |
| `timestamp` | `now`, `yyyy-MM-dd HH:mm:ss.SSS` |

Sem destino no modelo novo. A L1b (decisão 13) previa trocar `order_id` por `delivery_id`.

### `mysql/menu/` (seção de cardápio)

| Campo | Lógica |
|---|---|
| `menu_section_id` | uuid |
| `restaurant_id` | lookup Oracle `restaurants.restaurant_id` |
| `name` | oneOf `Starters`, `Main Dishes`, `Sides`, `Beverages`, `Desserts`, `Combos` |
| `description` | `#{Lorem.sentence}`, locale pt-BR |
| `active` | boolean |

Destino no modelo novo: `menu_items[].section` do perfil no MongoDB (RN-23).

### `mysql/ratings/` (avaliação)

| Campo | Lógica |
|---|---|
| `rating_id` | `sequentialInteger` a partir de 1 |
| `uuid` | uuid |
| `order_id` | lookup Oracle `orders.order_id` |
| `rating` | U[1, 5] inteiro |
| `timestamp` | U[2021-01-01, agora], `yyyy-MM-dd HH:mm:ss` |

Destino no modelo novo: `driver_ratings` e `restaurant_ratings` no Postgres (L3).

### `mongodb/support/` (chamado de suporte)

| Campo | Lógica |
|---|---|
| `ticket_id` | uuid |
| `user_id` | lookup Postgres `users.user_id` |
| `order_id` | lookup Oracle `orders.order_id` |
| `category` | oneOf `Late Delivery`, `Wrong Item`, `Missing Item`, `Payment Issue`, `Other` |
| `description` | `#{Lorem.paragraph}`, locale pt-BR |
| `status` | oneOf `Open`, `In Progress`, `Resolved`, `Closed` |
| `opened_at` | `now`, `yyyy-MM-dd HH:mm:ss` |

Destino no modelo novo: `incidents` e `incident_items` no Postgres (L3).

### `mongodb/recommendations/` (evento de recomendação)

| Campo | Lógica |
|---|---|
| `event_id` | uuid |
| `user_id` | lookup Postgres `users.user_id` |
| `event_type` | oneOf `view`, `click`, `add_to_cart`, `recommendation_served` |
| `product_id` | lookup Oracle `products.product_id` |
| `timestamp` | `now`, `yyyy-MM-dd HH:mm:ss.SSS` |

Sem destino no modelo novo.

### `kafka/search/` (busca)

| Campo | Lógica |
|---|---|
| `search_id` | uuid |
| `user_id` | lookup Postgres `users.user_id` |
| `query_text` | `#{Lorem.sentence}`, locale pt-BR |
| `filters` | oneOf `Vegetarian`, `Fast Delivery`, `Top Rated`, `Open Now`, `Deals` (um só valor) |
| `result_count` | U[0, 50] inteiro |
| `clicked_product_id` | lookup Oracle `products.product_id` |
| `timestamp` | `now`, `yyyy-MM-dd HH:mm:ss.SSS` |

Sem `dt_current_timestamp`. Sem destino no modelo novo.

## Incoerências conhecidas

Corrigir antes de reativar:

1. **Lookups independentes.** Na rota, o restaurante de partida e o cliente de chegada não são os do pedido; o motorista
   não é o atribuído. Na busca, o produto clicado não depende do texto nem dos filtros.
2. **Datas aleatórias desde 2021** em `shift`, `route` e `ratings`, sem relação com a data do pedido.
3. **GPS sem ligação com a rota**: a caixa é fixa em São Paulo, qualquer que seja a cidade, e não parte de `start_lat/lon`
   nem chega a `end_lat/lon`.
4. **Textos em Lorem** (`query_text`, `description`) e categorias em inglês, fora do padrão de domínios em minúsculas do
   modelo novo.
5. **Dinheiro em ponto flutuante** (`earnings_brl`), o que fere a L0 #3.

## Para reativar no modelo novo

Ponto de partida (a decidir de novo em `/grill-with-docs`, com regra de negócio que use o dado):

| Arquivo | Chaves no modelo novo |
|---|---|
| `kafka/gps` | `delivery_id` (Postgres `deliveries`) e `driver_id` (Oracle `drivers`), com a trajetória entre as coordenadas de coleta e de entrega e a cidade do pedido; só para entregas em andamento |
| `kafka/search` | `customer_id` (Oracle `customers`), `city_id`; resultado e clique em `product_id` de restaurantes da cidade (Postgres `products`) |
| `mongodb/recommendations` | `customer_id`, `product_id` e, se o funil for usado, ligação com `checkout_id` |

Como o ShadowTraffic não tem estado entre geradores (ADR 007), o GPS coerente com a entrega provavelmente teria de vir do
simulador de operação (ADR 009), que conhece a entrega e o motorista atribuído.

## O que consumia o MinIO

Código parado, a rever quando cada fase de nuvem for retomada (ADR 010, decisão 3):

| Trilha | Peças |
|---|---|
| Fase 0 | Serviços `minio-ubereats` e `minio-setup` no `docker-compose.yml`; scripts em `scripts/infra/` e `scripts/all/` |
| Azure | Airbyte MinIO → ADLS (`azure/docs/airbyte-minio-adls-config.md`); notificação Kafka do bucket (`azure/docs/minio/`); `azure/infra/fase1-ingestao/` e `azure/sql/` |
| AWS | DataSync (`datasync.tf`) e ponte Lambda MinIO → Kinesis (`aws/src/lambda_minio_kinesis_bridge/`, teste em `aws/tests/`) |
| GCP | Storage Transfer (`storage_transfer.tf`) e ponte Cloud Function MinIO → Pub/Sub (`gcp/src/cloud_function_minio_pubsub_bridge/`, teste em `gcp/tests/`) |
