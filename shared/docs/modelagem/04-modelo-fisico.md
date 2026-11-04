# Modelo físico

Quarta etapa do fluxo (regras → adversarial → conceitual → lógico → **físico** → regeração). Parte do
[modelo lógico](03-modelo-logico.md) (L0 a L4) e das ADRs [006](../../../docs/adr/006-inversao-de-dominios-entre-oracle-e-postgres.md),
[007](../../../docs/adr/007-estoque-por-movimentos-e-gerador-hibrido.md) e [008](../../../docs/adr/008-historico-de-status-em-tabelas-de-transicao.md).
Revisão por fases. O DDL daqui é **documento**: só é aplicado na regeração, com confirmação (o Oracle atual segue tratado
como produção).

| Fase | Conteúdo | Status |
|---|---|---|
| F0 | Decisões transversais adiadas pelo lógico | aprovada |
| F1 | DDL Postgres: catálogo, operação, dinheiro, pós-entrega | aprovada |
| F2 | DDL Oracle: `customers`, `drivers`, `cities` | aprovada |
| F3 | MongoDB (`restaurant_profiles`). O MinIO saiu do escopo ([ADR 010](../../../docs/adr/010-minio-fora-do-escopo-da-geracao.md); lógica guardada em [`minio/historico-geracao.md`](../minio/historico-geracao.md)) | pendente |
| F4 | CDC: configuração do Debezium, tópicos, contrato `cdc_*` visto da fonte | pendente |
| F5 | Plano da regeração: ordem de carga, divisão gerador × simulador, testes T1 a T18 como consultas | pendente |

---

## F0. Decisões transversais

Pendências que o lógico deixou para o físico. F0.3, F0.5 e F0.7 dependem de quem cria a compra (F0.1); as outras são
independentes.

### F0.1 Quem cria a compra

**Problema.** Hoje (ADR 007 e L1b) o ShadowTraffic insere pedido, atendimentos, itens, entrega e a linha 1 das transições
em geradores separados, **sem transação comum**, e a L2 deixou em aberto se ele também cria checkout, tentativas,
pagamento, componentes e recibo. Três problemas saem daí:

1. **Guarda do simulador.** O simulador pode pegar um atendimento cujos itens ainda não chegaram e checar estoque errado
   (L1b, risco).
2. **Dinheiro.** `payment_components` exige alocar a taxa de serviço por item com "a última parcela absorve a diferença"
   (RN-33) e decompor o imposto do bruto (RN-09). O ShadowTraffic não tem estado entre geradores (ADR 007) nem laço sobre
   os itens de um pedido: a soma dos componentes bater com `total_amount` (T8) ficaria frágil.
3. **Código de rastreio.** O ShadowTraffic não calcula SHA-256; ou se usa um trigger no Postgres ou alguém atualiza a linha
   depois.

**Proposta (recomendada): o simulador cria a compra inteira, numa transação.** Checkout, tentativas, pedido, atendimentos,
itens, entrega, linha 1 das duas tabelas de transição, pagamento, componentes e recibo nascem juntos, em Python, com
`BEGIN ... COMMIT`. O ShadowTraffic fica com o que não tem estado: cadastros (Oracle `customers`, `drivers`, `cities`;
Postgres `cities`, `restaurants`, `products`, `stock_items`, `product_recipes`), o MongoDB (`restaurant_profiles`) e o
MinIO (`kafka/gps`). **Depois:** o MinIO saiu do escopo ([ADR 010](../../../docs/adr/010-minio-fora-do-escopo-da-geracao.md)).

| Consequência | Efeito |
|---|---|
| Guarda (F0.5) | **Some**: não existe atendimento sem itens visível a outra transação |
| Dinheiro (F0.7) | Resolvido em Python, em `Decimal`, com a regra da RN-33 testável em `pytest` |
| Código de rastreio (F0.3) | Calculado no simulador, antes do INSERT |
| Sequências (F0.8) | **Um único dono de INSERT por tabela**; sem colisão entre gerador e simulador |
| Leitura entre bancos | O simulador passa a ler `customers` no Oracle (cidade, endereço e coordenadas copiados na compra). Não é um tipo novo de leitura: ele já lê `drivers` para abrir turno (RN-42) |
| ADR 007 | A fronteira muda ("ShadowTraffic até em análise" vira "ShadowTraffic só cadastro e eventos"). Vira **ADR 009** |
| Ritmo de compras | Passa a ser parâmetro do simulador (pedidos por minuto por cidade), não `throttleMs` do template |

**Alternativas.**

- **B. ShadowTraffic cria pedido e itens; simulador cria o dinheiro depois.** Mantém a ADR 007, mas o pagamento nasce
  depois do pedido (ordem invertida no CDC), a guarda continua necessária e o `checkout_id` tem de ser combinado entre os
  dois (faixas de id).
- **C. ShadowTraffic cria tudo, inclusive o dinheiro.** Mantém a ADR 007 inteira, mas T8 e a RN-33 dependem de `math` em
  geradores sem estado, a guarda continua necessária e o código de rastreio exige trigger.

### F0.2 Decimal no Debezium

**Problema.** Por padrão (`decimal.handling.mode=precise`) o Debezium entrega `NUMERIC`/`NUMBER` como bytes codificados
(e `NUMERIC` sem escala como struct). O conector Oracle atual usa `double`, que fere a L0 #3 (dinheiro nunca em ponto
flutuante).

**Proposta (recomendada): `decimal.handling.mode=string`** nos dois conectores. A Bronze grava o texto e declara o tipo de
destino por coluna (`DECIMAL(12,2)`, `DECIMAL(12,3)`, `DECIMAL(9,6)`, `DECIMAL(5,4)`); a conversão é exata. Alternativas:
`precise` (exato, mas exige decodificar bytes com a escala do schema) e `double` (descartada pela L0 #3).

**Achado que vai para a F2.** No conector Oracle, `NUMBER(p,0)` só vira inteiro (`int64`) com p ≤ 18; `NUMBER(19)` e
`INTEGER` (que no Oracle é `NUMBER(38)`) caem no `decimal.handling.mode` e chegariam como texto. Proposta: chaves do
Oracle em **`NUMBER(18)`** (teto de 10^18 − 1, folgado) e inteiros pequenos em `NUMBER(9)` (o `city_id` do IBGE tem 7
dígitos). Isso corrige a tradução "`bigint` → `NUMBER(19)`" da L1a e do handoff.

### F0.3 Código de rastreio

Formato fixado na L1b (decisão 12): 12 caracteres base32 Crockford do SHA-256 de `order_id` com sal; o pagamento usa o
mesmo formato com outro sal. Não pode ser coluna gerada (o Postgres 15 não a publica na replicação lógica).

**Proposta (recomendada, se F0.1 = simulador): função Python no simulador**, chamada antes do INSERT de `orders` e
`payments`. Os dois sais ficam no `.env` (`TRACKING_SALT_ORDER`, `TRACKING_SALT_PAYMENT`), fora do git; o teste de
regeração recalcula o código e confere. Alternativa: **trigger `BEFORE INSERT`** com `pgcrypto` (vale para qualquer
escritor, mas põe regra de negócio no banco e o sal vira configuração do banco). Se F0.1 ficar com o ShadowTraffic, o
trigger passa a ser a única opção viável.

### F0.4 Timestamp sem fuso no Debezium

**Correção do que o lógico supôs.** O Debezium **não desloca** o valor: `TIMESTAMP` sem fuso (Postgres e Oracle) chega
como `MicroTimestamp`, micros desde a época **lidos como se a hora do relógio fosse UTC**. O deslocamento de 3 h só
aparece se o consumidor tratar esse número como instante e converter para `America/Sao_Paulo`.

**Proposta (recomendada): nenhum transform no conector; a Bronze declara.** Todo `*_at` de negócio é **hora de Brasília
sem fuso** e vira `TIMESTAMP_NTZ` na Bronze, convertido com fuso de sessão UTC (assim o número volta a ser a hora do
relógio, sem deslocar). Já `cdc_commit_ts` (vem de `source.ts_ms`) é **instante real em UTC** e vira `TIMESTAMP`. As duas
semânticas ficam escritas no contrato da Bronze (F4). Complementos na regeração: `TZ=America/Sao_Paulo` nos contêineres
Postgres e Oracle, e a sessão do simulador com `SET TIME ZONE 'America/Sao_Paulo'`, para `now()`/`SYSTIMESTAMP` gravarem
a hora de Brasília. Alternativa: transform que converte para texto ISO no conector (mais peça para manter, sem ganho).

### F0.5 Guarda do simulador

Se F0.1 = simulador, **não há guarda**: a compra é uma transação. Se ficar com o ShadowTraffic, a guarda proposta é: o
simulador só processa atendimento com ao menos um item, com entrega já criada e com `created_at` há pelo menos N
segundos (parâmetro `intake_min_age_s`, sugestão 10). Mesmo assim não garante que **todos** os itens chegaram.

### F0.6 Leitura das janelas de funcionamento

**Proposta (recomendada): o simulador lê `restaurant_profiles` direto do MongoDB**, só leitura, com cache recarregado a
cada N minutos (parâmetro `profile_cache_refresh_min`, sugestão 15). O MongoDB é a fonte das janelas (RN-41) e é o
ShadowTraffic que as gera: uma cópia de configuração divergiria. Alternativa: copiar as janelas para o arquivo de
parâmetros (estático; quebra se o gerador mudar os perfis).

### F0.7 Dinheiro da compra

Segue F0.1. Se o simulador criar a compra, ele calcula componentes, imposto embutido e taxas em `Decimal` (nunca
`float`); o modo de arredondamento e a regra da última parcela (RN-33) ficam para a F5. Se não, ver as alternativas B e C
de F0.1.

### F0.8 Sequências e `startingFrom`

**Proposta (recomendada): um único dono de INSERT por tabela.**

| Dono | Chave | Como |
|---|---|---|
| ShadowTraffic (cadastros) | `sequentialInteger` com `startingFrom` | A skill `shadowtraffic-ajustar-geracao` recalcula o `startingFrom` a cada religada, como hoje |
| Simulador (operação, dinheiro, pós-entrega) | `bigint GENERATED BY DEFAULT AS IDENTITY` no Postgres | O banco dá o próximo valor; nada a recalcular no restart |
| Entidade fraca (chave composta) | número da linha (`line_number`, `sequence_number`, `assignment_number`, ...) | Calculado pelo dono, dentro da transação do pai ou da mudança (a chave composta é a trava da RN-27) |

Coluna identidade é coluna comum para a replicação lógica: o Debezium a publica. Com regeração do zero, as identidades
começam em 1.

### F0.9 Arquivo de parâmetros

**Proposta (recomendada): `shared/gen/parameters.yaml`**, versionado, com os parâmetros da L4 mais os novos desta fase
(ritmo de compras, `profile_cache_refresh_min`). Lido pelo simulador e pelos testes (`pytest`). O ShadowTraffic não o lê
diretamente: se algum valor precisar ir ao template, o `shared/gen/setup-configs.ps1` o injeta na renderização, como já
faz com o `.env`. Segredos (os sais de F0.3) **não** vão nele.

### Decisões da revisão da F0 (2026-11-03)

| # | Tema | Decisão |
|---|---|---|
| 1 | Quem cria a compra | **Simulador, numa transação**: checkout, tentativas, pedido, atendimentos, itens, entrega, linha 1 das transições, pagamento, componentes e recibo. O ShadowTraffic fica com cadastros, MongoDB e `kafka/gps`. Muda a fronteira da ADR 007: registrada na [ADR 009](../../../docs/adr/009-simulador-cria-a-compra-numa-transacao.md) |
| 2 | Decimal no Debezium | **`decimal.handling.mode=string`** nos dois conectores; a Bronze declara `DECIMAL(p,s)` por coluna. No Oracle, chaves em **`NUMBER(18)`** e inteiros pequenos em **`NUMBER(9)`** (corrige o "`NUMBER(19)`" da L1a) |
| 3 | Timestamp sem fuso | **Sem transform no conector.** `*_at` de negócio é hora de Brasília e vira `TIMESTAMP_NTZ` na Bronze; `cdc_commit_ts` é instante UTC. `TZ=America/Sao_Paulo` nos contêineres e na sessão do simulador |
| 4 | Código de rastreio | **Função Python no simulador**, antes do INSERT de `orders` e `payments`; sais no `.env` (`TRACKING_SALT_ORDER`, `TRACKING_SALT_PAYMENT`) |
| 5 | Guarda do simulador | **Não é necessária**: a compra é uma transação (decorre da decisão 1) |
| 6 | Janelas de funcionamento | **Leitura direta do MongoDB**, só leitura, com cache (`profile_cache_refresh_min`, sugestão 15) |
| 7 | Dinheiro da compra | **Simulador**, em `Decimal`; arredondamento e última parcela (RN-33) na F5 |
| 8 | Sequências | **Um dono de INSERT por tabela**: `sequentialInteger` + `startingFrom` nos cadastros do ShadowTraffic; `bigint GENERATED BY DEFAULT AS IDENTITY` nas tabelas do simulador; número da linha das entidades fracas calculado na transação |
| 9 | Arquivo de parâmetros | **`shared/gen/parameters.yaml`**, versionado, lido pelo simulador e pelos testes; sem segredos |

---

## F1. DDL Postgres

As 28 tabelas do Postgres (ADR 006): catálogo e estoque (L1a), operação (L1b), dinheiro (L2) e pós-entrega (L3). O DDL
abaixo foi validado num Postgres 15 descartável (28 tabelas, 69 `CHECK`, trigger e índices únicos parciais testados).

### F1.0 Convenções físicas

| # | Tema | Proposta |
|---|---|---|
| 1 | Schema | Schema próprio **`ubereats`** (o `search_path` do usuário da aplicação aponta para ele). Facilita a publicação do CDC por schema (F4) e separa das tabelas antigas em `public` |
| 2 | Nulos | **`NOT NULL` em toda coluna**, salvo as marcadas "nulo" no lógico |
| 3 | Domínios | **`varchar` + `CHECK`** com a lista de valores do lógico (status, motivos, ator, tipos). Sem `ENUM` nativo: mudar um valor é trocar o `CHECK`, sem `ALTER TYPE` |
| 4 | Invariantes de linha | **`CHECK`** para o que se vê numa linha só: "motivo só no status X", "exatamente uma origem do reembolso", `quantity ≥ 1`, nota de 1 a 5, saldo ≥ 0 (RN-39). Vira o quarto mecanismo da L4, entre o índice único e o simulador |
| 5 | Texto | **`varchar(n)`** com tamanho explícito (documenta o limite e vale para os warehouses das trilhas). Códigos fixos em `char(n)` com `CHECK` de formato (CNPJ, CEP, UF, rastreio) |
| 6 | Chaves | Cadastros do ShadowTraffic: `bigint` sem default (o gerador fornece). Tabelas do simulador: `bigint GENERATED BY DEFAULT AS IDENTITY` (F0, decisão 8). `cities`: código do IBGE |
| 7 | Rastro | `created_at timestamp NOT NULL DEFAULT localtimestamp`; `updated_at` igual, mais um trigger que o preenche **só quando o escritor não o mudou** (o simulador pode gravar um instante próprio) |
| 8 | Nomes | `pk_<tabela>`, `uq_<tabela>_<colunas>`, `ck_<tabela>_<regra>`, `ix_<tabela>_<colunas>` |
| 9 | Sem FK | Invariante do projeto (L0 #9); integridade referencial nos testes (T1 a T18) |

`localtimestamp` devolve a hora da sessão sem fuso; com a sessão em `America/Sao_Paulo` (F0, decisão 3) é a hora de Brasília.

```sql
CREATE SCHEMA IF NOT EXISTS ubereats;
SET search_path TO ubereats;

CREATE FUNCTION set_updated_at() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN
  IF NEW.updated_at IS NOT DISTINCT FROM OLD.updated_at THEN
    NEW.updated_at := localtimestamp;
  END IF;
  RETURN NEW;
END $$;
```

O trigger `BEFORE UPDATE ... EXECUTE FUNCTION set_updated_at()` é criado em toda tabela que tem `updated_at` (lista no fim).

### F1.1 Catálogo e estoque (L1a)

```sql
CREATE TABLE cities (
  city_id     integer      NOT NULL,
  name        varchar(100) NOT NULL,
  state_code  char(2)      NOT NULL,
  created_at  timestamp    NOT NULL DEFAULT localtimestamp,
  updated_at  timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_cities PRIMARY KEY (city_id),
  CONSTRAINT ck_cities_city_id CHECK (city_id BETWEEN 1000000 AND 5999999),
  CONSTRAINT ck_cities_state_code CHECK (state_code ~ '^[A-Z]{2}$')
);

CREATE TABLE restaurants (
  restaurant_id  bigint        NOT NULL,
  name           varchar(150)  NOT NULL,
  cnpj           char(14)      NOT NULL,
  phone_number   varchar(20)   NOT NULL,
  address        varchar(200)  NOT NULL,
  postal_code    char(8)       NOT NULL,
  latitude       numeric(9,6)  NOT NULL,
  longitude      numeric(9,6)  NOT NULL,
  city_id        integer       NOT NULL,
  cuisine_type   varchar(50)   NOT NULL,
  status         varchar(20)   NOT NULL,
  created_at     timestamp     NOT NULL DEFAULT localtimestamp,
  updated_at     timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_restaurants PRIMARY KEY (restaurant_id),
  CONSTRAINT uq_restaurants_cnpj UNIQUE (cnpj),
  CONSTRAINT ck_restaurants_cnpj CHECK (cnpj ~ '^[0-9]{14}$'),
  CONSTRAINT ck_restaurants_postal_code CHECK (postal_code ~ '^[0-9]{8}$'),
  CONSTRAINT ck_restaurants_coords CHECK (latitude BETWEEN -90 AND 90 AND longitude BETWEEN -180 AND 180),
  CONSTRAINT ck_restaurants_status CHECK (status IN ('active', 'suspended', 'inactive'))
);

CREATE TABLE products (
  product_id      bigint        NOT NULL,
  restaurant_id   bigint        NOT NULL,
  name            varchar(150)  NOT NULL,
  product_type    varchar(50)   NOT NULL,
  price           numeric(12,2) NOT NULL,
  unit_cost       numeric(12,2) NOT NULL,
  calories        integer       NOT NULL,
  prep_time_min   integer       NOT NULL,
  is_vegetarian   boolean       NOT NULL,
  is_gluten_free  boolean       NOT NULL,
  is_active       boolean       NOT NULL,
  created_at      timestamp     NOT NULL DEFAULT localtimestamp,
  updated_at      timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_products PRIMARY KEY (product_id),
  CONSTRAINT ck_products_price CHECK (price > 0 AND unit_cost >= 0),
  CONSTRAINT ck_products_calories CHECK (calories >= 0),
  CONSTRAINT ck_products_prep_time CHECK (prep_time_min > 0)
);

CREATE TABLE stock_items (
  stock_item_id     bigint        NOT NULL,
  restaurant_id     bigint        NOT NULL,
  name              varchar(100)  NOT NULL,
  kind              varchar(20)   NOT NULL,
  unit              varchar(20)   NOT NULL,
  quantity_on_hand  numeric(12,3) NOT NULL DEFAULT 0,
  created_at        timestamp     NOT NULL DEFAULT localtimestamp,
  updated_at        timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_stock_items PRIMARY KEY (stock_item_id),
  CONSTRAINT uq_stock_items_restaurant_name UNIQUE (restaurant_id, name),
  CONSTRAINT ck_stock_items_kind CHECK (kind IN ('ready', 'prepared', 'ingredient')),
  CONSTRAINT ck_stock_items_unit CHECK (unit IN ('unit', 'gram', 'portion')),
  CONSTRAINT ck_stock_items_on_hand CHECK (quantity_on_hand >= 0)          -- RN-39
);

CREATE TABLE product_recipes (
  product_id     bigint        NOT NULL,
  stock_item_id  bigint        NOT NULL,
  quantity       numeric(12,3) NOT NULL,
  created_at     timestamp     NOT NULL DEFAULT localtimestamp,
  updated_at     timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_product_recipes PRIMARY KEY (product_id, stock_item_id),
  CONSTRAINT ck_product_recipes_quantity CHECK (quantity > 0)
);

CREATE TABLE stock_movements (
  stock_movement_id    bigint        GENERATED BY DEFAULT AS IDENTITY,
  stock_item_id        bigint        NOT NULL,
  movement_type        varchar(20)   NOT NULL,
  quantity             numeric(12,3) NOT NULL,
  restaurant_order_id  bigint,
  occurred_at          timestamp     NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_stock_movements PRIMARY KEY (stock_movement_id),
  CONSTRAINT ck_stock_movements_type CHECK (movement_type IN ('consumption', 'restock')),
  CONSTRAINT ck_stock_movements_quantity CHECK (quantity > 0),
  CONSTRAINT ck_stock_movements_order CHECK ((movement_type = 'consumption') = (restaurant_order_id IS NOT NULL))
);

CREATE UNIQUE INDEX uq_stock_movements_consumption                         -- RN-38
  ON stock_movements (restaurant_order_id, stock_item_id) WHERE movement_type = 'consumption';
```

`products.restaurant_id`, `product_recipes` e `stock_items` do mesmo restaurante continuam no teste T4 (cruza tabelas).
O `CHECK` de saldo ≥ 0 torna a RN-39 uma recusa do banco, além da checagem do simulador.

### F1.2 Operação (L1b)

Listas usadas pelos `CHECK` (iguais às do lógico):

- **Status do pedido:** `in_analysis`, `preparing`, `partially_ready`, `ready_for_pickup`, `partially_picked_up`,
  `out_for_delivery`, `delivered`, `completed`, `undelivered`, `cancelled`.
- **Status do atendimento:** `in_analysis`, `accepted`, `preparing`, `ready_for_pickup`, `picked_up`, `cancelled`, `rejected`.
- **Ator:** `customer`, `restaurant`, `driver`, `platform`.

```sql
CREATE TABLE orders (
  order_id       bigint       GENERATED BY DEFAULT AS IDENTITY,
  tracking_code  char(12)     NOT NULL,
  checkout_id    bigint       NOT NULL,
  customer_id    bigint       NOT NULL,                                     -- ext → Oracle.customers
  city_id        integer      NOT NULL,
  status         varchar(30)  NOT NULL DEFAULT 'in_analysis',
  placed_at      timestamp    NOT NULL,
  created_at     timestamp    NOT NULL DEFAULT localtimestamp,
  updated_at     timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_orders PRIMARY KEY (order_id),
  CONSTRAINT uq_orders_tracking_code UNIQUE (tracking_code),
  CONSTRAINT uq_orders_checkout_id UNIQUE (checkout_id),                    -- RN-15
  CONSTRAINT ck_orders_tracking_code CHECK (tracking_code ~ '^[0-9A-HJKMNP-TV-Z]{12}$'),
  CONSTRAINT ck_orders_status CHECK (status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup',
    'partially_picked_up', 'out_for_delivery', 'delivered', 'completed', 'undelivered', 'cancelled'))
);

CREATE TABLE restaurant_orders (
  restaurant_order_id  bigint       GENERATED BY DEFAULT AS IDENTITY,
  order_id             bigint       NOT NULL,
  restaurant_id        bigint       NOT NULL,
  status               varchar(20)  NOT NULL DEFAULT 'in_analysis',
  estimated_prep_min   integer,
  accepted_at          timestamp,
  driver_arrived_at    timestamp,
  picked_up_at         timestamp,
  end_reason           varchar(30),
  created_at           timestamp    NOT NULL DEFAULT localtimestamp,
  updated_at           timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_restaurant_orders PRIMARY KEY (restaurant_order_id),
  CONSTRAINT uq_restaurant_orders_order_restaurant UNIQUE (order_id, restaurant_id),   -- RN-05
  CONSTRAINT ck_restaurant_orders_status CHECK (status IN ('in_analysis', 'accepted', 'preparing',
    'ready_for_pickup', 'picked_up', 'cancelled', 'rejected')),
  CONSTRAINT ck_restaurant_orders_end_reason CHECK (
       (status = 'rejected'  AND end_reason IN ('restaurant_declined', 'out_of_stock', 'analysis_timeout'))
    OR (status = 'cancelled' AND end_reason IN ('customer_request', 'restaurant_late',
                                                'other_restaurant_dropped', 'restaurant_issue'))
    OR (status NOT IN ('rejected', 'cancelled') AND end_reason IS NULL)),
  CONSTRAINT ck_restaurant_orders_acceptance CHECK ((accepted_at IS NULL) = (estimated_prep_min IS NULL)),
  CONSTRAINT ck_restaurant_orders_accepted CHECK (                          -- RN-28, T7
    status NOT IN ('accepted', 'preparing', 'ready_for_pickup', 'picked_up') OR accepted_at IS NOT NULL),
  CONSTRAINT ck_restaurant_orders_prep CHECK (estimated_prep_min > 0),
  CONSTRAINT ck_restaurant_orders_picked_up CHECK ((status = 'picked_up') = (picked_up_at IS NOT NULL))
);

CREATE TABLE order_items (
  restaurant_order_id  bigint        NOT NULL,
  line_number          smallint      NOT NULL,
  product_id           bigint        NOT NULL,
  product_name         varchar(150)  NOT NULL,
  unit_price           numeric(12,2) NOT NULL,
  quantity             integer       NOT NULL,
  total_amount         numeric(12,2) NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_order_items PRIMARY KEY (restaurant_order_id, line_number),
  CONSTRAINT ck_order_items_line_number CHECK (line_number >= 1),
  CONSTRAINT ck_order_items_quantity CHECK (quantity >= 1),
  CONSTRAINT ck_order_items_total CHECK (unit_price >= 0 AND total_amount = unit_price * quantity)   -- RN-32
);

CREATE TABLE order_status_transitions (
  order_id         bigint       NOT NULL,
  sequence_number  smallint     NOT NULL,
  from_status      varchar(30),
  to_status        varchar(30)  NOT NULL,
  actor            varchar(20)  NOT NULL,
  reason           varchar(30),
  occurred_at      timestamp    NOT NULL,
  created_at       timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_order_status_transitions PRIMARY KEY (order_id, sequence_number),       -- RN-27
  CONSTRAINT ck_order_status_transitions_first CHECK (
    (sequence_number = 1) = (from_status IS NULL) AND (sequence_number > 1 OR to_status = 'in_analysis')),
  CONSTRAINT ck_order_status_transitions_status CHECK (
    to_status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup', 'partially_picked_up',
                  'out_for_delivery', 'delivered', 'completed', 'undelivered', 'cancelled')
    AND (from_status IS NULL OR from_status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup',
                  'partially_picked_up', 'out_for_delivery', 'delivered'))),
  CONSTRAINT ck_order_status_transitions_actor CHECK (actor IN ('customer', 'restaurant', 'driver', 'platform')),
  CONSTRAINT ck_order_status_transitions_reason CHECK (
    (to_status = 'undelivered' AND reason IN ('customer_absent', 'driver_unable'))
    OR (to_status <> 'undelivered' AND reason IS NULL))                    -- RN-30
);

CREATE TABLE restaurant_order_status_transitions (
  restaurant_order_id  bigint       NOT NULL,
  sequence_number      smallint     NOT NULL,
  from_status          varchar(20),
  to_status            varchar(20)  NOT NULL,
  actor                varchar(20)  NOT NULL,
  reason               varchar(30),
  occurred_at          timestamp    NOT NULL,
  created_at           timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_restaurant_order_status_transitions PRIMARY KEY (restaurant_order_id, sequence_number),
  CONSTRAINT ck_ro_status_transitions_first CHECK (
    (sequence_number = 1) = (from_status IS NULL) AND (sequence_number > 1 OR to_status = 'in_analysis')),
  CONSTRAINT ck_ro_status_transitions_status CHECK (
    to_status IN ('in_analysis', 'accepted', 'preparing', 'ready_for_pickup', 'picked_up', 'cancelled', 'rejected')
    AND (from_status IS NULL OR from_status IN ('in_analysis', 'accepted', 'preparing', 'ready_for_pickup'))),
  CONSTRAINT ck_ro_status_transitions_actor CHECK (actor IN ('customer', 'restaurant', 'driver', 'platform')),
  CONSTRAINT ck_ro_status_transitions_reason CHECK (
       (to_status = 'rejected'  AND reason IN ('restaurant_declined', 'out_of_stock', 'analysis_timeout'))
    OR (to_status = 'cancelled' AND reason IN ('customer_request', 'restaurant_late',
                                               'other_restaurant_dropped', 'restaurant_issue'))
    OR (to_status NOT IN ('rejected', 'cancelled') AND reason IS NULL))
);

CREATE TABLE deliveries (
  delivery_id        bigint        GENERATED BY DEFAULT AS IDENTITY,
  order_id           bigint        NOT NULL,
  status             varchar(30)   NOT NULL DEFAULT 'awaiting_assignment',
  dropoff_address    varchar(200)  NOT NULL,
  dropoff_latitude   numeric(9,6)  NOT NULL,
  dropoff_longitude  numeric(9,6)  NOT NULL,
  distance_km        numeric(6,2),
  promised_at        timestamp,
  finished_at        timestamp,
  failure_reason     varchar(30),
  created_at         timestamp     NOT NULL DEFAULT localtimestamp,
  updated_at         timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_deliveries PRIMARY KEY (delivery_id),
  CONSTRAINT uq_deliveries_order_id UNIQUE (order_id),                      -- RN-06
  CONSTRAINT ck_deliveries_status CHECK (status IN ('awaiting_assignment', 'assigned', 'in_transit',
    'delivered', 'undelivered', 'cancelled')),
  CONSTRAINT ck_deliveries_failure CHECK (
    (status = 'undelivered' AND failure_reason IN ('customer_absent', 'driver_unable'))
    OR (status <> 'undelivered' AND failure_reason IS NULL)),               -- RN-30
  CONSTRAINT ck_deliveries_finished CHECK ((status IN ('delivered', 'undelivered')) = (finished_at IS NOT NULL)),
  CONSTRAINT ck_deliveries_promise CHECK ((promised_at IS NULL) = (distance_km IS NULL) AND distance_km >= 0)
);

CREATE TABLE shifts (
  shift_id      bigint       GENERATED BY DEFAULT AS IDENTITY,
  driver_id     bigint       NOT NULL,                                      -- ext → Oracle.drivers
  city_id       integer      NOT NULL,
  status        varchar(10)  NOT NULL DEFAULT 'open',
  opened_at     timestamp    NOT NULL,
  closed_at     timestamp,
  close_reason  varchar(20),
  created_at    timestamp    NOT NULL DEFAULT localtimestamp,
  updated_at    timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_shifts PRIMARY KEY (shift_id),
  CONSTRAINT ck_shifts_status CHECK (status IN ('open', 'closed')),
  CONSTRAINT ck_shifts_closed CHECK (
    (status = 'closed' AND closed_at >= opened_at AND close_reason IN ('driver_closed', 'driver_unable'))
    OR (status = 'open' AND closed_at IS NULL AND close_reason IS NULL))   -- RN-42
);

CREATE UNIQUE INDEX uq_shifts_open_driver ON shifts (driver_id) WHERE status = 'open';           -- RN-42

CREATE TABLE driver_assignments (
  delivery_id        bigint       NOT NULL,
  assignment_number  smallint     NOT NULL,
  driver_id          bigint       NOT NULL,                                 -- ext → Oracle.drivers
  shift_id           bigint       NOT NULL,
  assigned_at        timestamp    NOT NULL,
  released_at        timestamp,
  release_reason     varchar(30),
  created_at         timestamp    NOT NULL DEFAULT localtimestamp,
  updated_at         timestamp    NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_driver_assignments PRIMARY KEY (delivery_id, assignment_number),
  CONSTRAINT ck_driver_assignments_number CHECK (assignment_number >= 1),
  CONSTRAINT ck_driver_assignments_release CHECK (
    (released_at IS NULL AND release_reason IS NULL)
    OR (released_at >= assigned_at
        AND release_reason IN ('driver_gave_up', 'delivery_cancelled', 'delivery_finished')))   -- RN-31
);

CREATE UNIQUE INDEX uq_driver_assignments_current_delivery
  ON driver_assignments (delivery_id) WHERE released_at IS NULL;          -- RN-31
CREATE UNIQUE INDEX uq_driver_assignments_current_driver
  ON driver_assignments (driver_id) WHERE released_at IS NULL;            -- RN-42
```

Ficam nos testes (cruzam linhas ou tabelas): a sequência de transições permitidas (T3), o máximo de 2 atendimentos (T1),
turnos sem sobreposição e o turno da atribuição (T5), `driver_gave_up` antes da primeira retirada (T5).

### F1.3 Dinheiro (L2)

```sql
CREATE TABLE checkouts (
  checkout_id  bigint        GENERATED BY DEFAULT AS IDENTITY,
  customer_id  bigint        NOT NULL,                                      -- ext → Oracle.customers
  amount       numeric(12,2) NOT NULL,
  created_at   timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_checkouts PRIMARY KEY (checkout_id),
  CONSTRAINT ck_checkouts_amount CHECK (amount > 0)
);

CREATE TABLE payment_attempts (
  checkout_id      bigint        NOT NULL,
  attempt_number   smallint      NOT NULL,
  amount           numeric(12,2) NOT NULL,
  payment_method   varchar(10)   NOT NULL,
  card_brand       varchar(20),
  wallet_provider  varchar(20),
  gateway          varchar(30)   NOT NULL,
  result           varchar(10)   NOT NULL,
  decline_reason   varchar(30),
  attempted_at     timestamp     NOT NULL,
  created_at       timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_payment_attempts PRIMARY KEY (checkout_id, attempt_number),
  CONSTRAINT ck_payment_attempts_number CHECK (attempt_number >= 1),
  CONSTRAINT ck_payment_attempts_amount CHECK (amount > 0),
  CONSTRAINT ck_payment_attempts_method CHECK (payment_method IN ('card', 'pix', 'wallet')),
  CONSTRAINT ck_payment_attempts_card CHECK ((payment_method = 'card') = (card_brand IS NOT NULL)),
  CONSTRAINT ck_payment_attempts_wallet CHECK ((payment_method = 'wallet') = (wallet_provider IS NOT NULL)),
  CONSTRAINT ck_payment_attempts_result CHECK (
    (result = 'approved' AND decline_reason IS NULL)
    OR (result = 'declined' AND decline_reason IN ('insufficient_funds', 'card_declined', 'expired_card',
                                                   'suspected_fraud', 'processing_error')))   -- RN-15
);

CREATE UNIQUE INDEX uq_payment_attempts_approved
  ON payment_attempts (checkout_id) WHERE result = 'approved';            -- RN-15

CREATE TABLE payments (
  payment_id          bigint        GENERATED BY DEFAULT AS IDENTITY,
  tracking_code       char(12)      NOT NULL,
  order_id            bigint        NOT NULL,
  checkout_id         bigint        NOT NULL,
  attempt_number      smallint      NOT NULL,
  total_amount        numeric(12,2) NOT NULL,
  tax_rate            numeric(5,4)  NOT NULL,
  service_fee_rate    numeric(5,4)  NOT NULL,
  payment_fee_rate    numeric(5,4)  NOT NULL,
  payment_fee_amount  numeric(12,2) NOT NULL,
  paid_at             timestamp     NOT NULL,
  created_at          timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_payments PRIMARY KEY (payment_id),
  CONSTRAINT uq_payments_tracking_code UNIQUE (tracking_code),
  CONSTRAINT uq_payments_order_id UNIQUE (order_id),                        -- RN-08
  CONSTRAINT uq_payments_attempt UNIQUE (checkout_id, attempt_number),
  CONSTRAINT ck_payments_tracking_code CHECK (tracking_code ~ '^[0-9A-HJKMNP-TV-Z]{12}$'),
  CONSTRAINT ck_payments_amounts CHECK (total_amount > 0 AND payment_fee_amount >= 0),
  CONSTRAINT ck_payments_rates CHECK (tax_rate BETWEEN 0 AND 1 AND service_fee_rate BETWEEN 0 AND 1
                                      AND payment_fee_rate BETWEEN 0 AND 1)
);

CREATE TABLE payment_components (
  payment_id           bigint        NOT NULL,
  component_number     smallint      NOT NULL,
  component_type       varchar(20)   NOT NULL,
  restaurant_order_id  bigint,
  line_number          smallint,
  gross_amount         numeric(12,2) NOT NULL,
  tax_amount           numeric(12,2) NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_payment_components PRIMARY KEY (payment_id, component_number),
  CONSTRAINT uq_payment_components_target
    UNIQUE NULLS NOT DISTINCT (payment_id, component_type, restaurant_order_id, line_number),   -- RN-20
  CONSTRAINT ck_payment_components_type CHECK (component_type IN ('item', 'service_fee', 'delivery_fee')),
  CONSTRAINT ck_payment_components_target CHECK (
    (restaurant_order_id IS NULL) = (line_number IS NULL)
    AND (component_type = 'delivery_fee') = (restaurant_order_id IS NULL)),
  CONSTRAINT ck_payment_components_amounts CHECK (gross_amount >= 0 AND tax_amount BETWEEN 0 AND gross_amount)
);

CREATE TABLE refunds (
  refund_id            bigint        GENERATED BY DEFAULT AS IDENTITY,
  payment_id           bigint        NOT NULL,
  origin_type          varchar(20)   NOT NULL,
  restaurant_order_id  bigint,
  incident_id          bigint,
  delivery_id          bigint,
  total_amount         numeric(12,2) NOT NULL,
  refunded_at          timestamp     NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_refunds PRIMARY KEY (refund_id),
  CONSTRAINT ck_refunds_origin CHECK (
    origin_type IN ('restaurant_order', 'incident', 'driver_unable')
    AND num_nonnulls(restaurant_order_id, incident_id, delivery_id) = 1
    AND (origin_type = 'restaurant_order') = (restaurant_order_id IS NOT NULL)
    AND (origin_type = 'incident') = (incident_id IS NOT NULL)
    AND (origin_type = 'driver_unable') = (delivery_id IS NOT NULL)),
  CONSTRAINT ck_refunds_amount CHECK (total_amount > 0)
);

CREATE UNIQUE INDEX uq_refunds_restaurant_order ON refunds (restaurant_order_id) WHERE restaurant_order_id IS NOT NULL;
CREATE UNIQUE INDEX uq_refunds_incident ON refunds (incident_id) WHERE incident_id IS NOT NULL;
CREATE UNIQUE INDEX uq_refunds_delivery ON refunds (delivery_id) WHERE delivery_id IS NOT NULL;

CREATE TABLE refund_components (
  refund_id         bigint        NOT NULL,
  component_number  smallint      NOT NULL,
  quantity          integer,
  gross_amount      numeric(12,2) NOT NULL,
  tax_amount        numeric(12,2) NOT NULL,
  created_at        timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_refund_components PRIMARY KEY (refund_id, component_number),
  CONSTRAINT ck_refund_components_quantity CHECK (quantity >= 1),
  CONSTRAINT ck_refund_components_amounts CHECK (gross_amount > 0 AND tax_amount BETWEEN 0 AND gross_amount)
);

CREATE TABLE restaurant_payouts (
  restaurant_order_id  bigint        NOT NULL,
  restaurant_id        bigint        NOT NULL,
  items_amount         numeric(12,2) NOT NULL,
  commission_rate      numeric(5,4)  NOT NULL,
  commission_amount    numeric(12,2) NOT NULL,
  payout_amount        numeric(12,2) NOT NULL,
  due_at               timestamp     NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_restaurant_payouts PRIMARY KEY (restaurant_order_id),
  CONSTRAINT ck_restaurant_payouts_amounts CHECK (
    commission_rate BETWEEN 0 AND 1 AND commission_amount BETWEEN 0 AND items_amount
    AND payout_amount = items_amount - commission_amount)
);

CREATE TABLE driver_payouts (
  delivery_id          bigint        NOT NULL,
  driver_id            bigint        NOT NULL,                              -- ext → Oracle.drivers
  shift_id             bigint        NOT NULL,
  delivery_fee_amount  numeric(12,2) NOT NULL,
  driver_share_rate    numeric(5,4)  NOT NULL,
  payout_amount        numeric(12,2) NOT NULL,
  due_at               timestamp     NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_driver_payouts PRIMARY KEY (delivery_id),
  CONSTRAINT ck_driver_payouts_amounts CHECK (
    driver_share_rate BETWEEN 0 AND 1 AND payout_amount BETWEEN 0 AND delivery_fee_amount)
);

CREATE TABLE tips (
  delivery_id  bigint        NOT NULL,
  driver_id    bigint        NOT NULL,                                      -- ext → Oracle.drivers
  amount       numeric(12,2) NOT NULL,
  paid_at      timestamp     NOT NULL,
  created_at   timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_tips PRIMARY KEY (delivery_id),                             -- RN-22
  CONSTRAINT ck_tips_amount CHECK (amount > 0)
);

CREATE TABLE receipts (
  payment_id  bigint     NOT NULL,
  issued_at   timestamp  NOT NULL,
  created_at  timestamp  NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_receipts PRIMARY KEY (payment_id)
);
```

`UNIQUE NULLS NOT DISTINCT` (Postgres 15+) cobre numa restrição só o "um componente por item e tipo" e o "um só
`delivery_fee` por pagamento" do catálogo da L4: a linha de taxa de entrega tem as duas referências nulas, e nulos iguais
colidem. O mínimo e o máximo da gorjeta são parâmetros (`tip_min`, `tip_max`), não `CHECK`: mudar o parâmetro não pode
invalidar linha antiga. As somas (T8, T9) e as cópias (T10) ficam nos testes.

### F1.4 Pós-entrega (L3)

```sql
CREATE TABLE incidents (
  incident_id        bigint        GENERATED BY DEFAULT AS IDENTITY,
  order_id           bigint        NOT NULL,
  customer_id        bigint        NOT NULL,                                -- ext → Oracle.customers
  reason             varchar(20)   NOT NULL,
  description        varchar(500),
  status             varchar(20)   NOT NULL DEFAULT 'open',
  opened_at          timestamp     NOT NULL,
  review_started_at  timestamp,
  decided_at         timestamp,
  created_at         timestamp     NOT NULL DEFAULT localtimestamp,
  updated_at         timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_incidents PRIMARY KEY (incident_id),
  CONSTRAINT ck_incidents_reason CHECK (reason IN ('missing_item', 'wrong_item', 'food_quality',
    'late_delivery', 'not_received', 'driver_unable')),
  CONSTRAINT ck_incidents_status CHECK (status IN ('open', 'in_review', 'upheld', 'dismissed')),
  CONSTRAINT ck_incidents_review CHECK (                                    -- RN-14: aberto → em análise → decidido
    (status IN ('in_review', 'upheld', 'dismissed')) = (review_started_at IS NOT NULL)
    AND (status IN ('upheld', 'dismissed')) = (decided_at IS NOT NULL)
    AND review_started_at >= opened_at AND decided_at >= review_started_at)
);

CREATE UNIQUE INDEX uq_incidents_delivery_reason                           -- L3, decisão 6
  ON incidents (order_id) WHERE reason IN ('late_delivery', 'not_received', 'driver_unable');

CREATE TABLE incident_items (
  incident_id          bigint     NOT NULL,
  restaurant_order_id  bigint     NOT NULL,
  line_number          smallint   NOT NULL,
  quantity             integer    NOT NULL,
  created_at           timestamp  NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_incident_items PRIMARY KEY (incident_id, restaurant_order_id, line_number),
  CONSTRAINT ck_incident_items_quantity CHECK (quantity >= 1)
);

CREATE TABLE driver_ratings (
  delivery_id  bigint        NOT NULL,
  driver_id    bigint        NOT NULL,                                      -- ext → Oracle.drivers
  customer_id  bigint        NOT NULL,                                      -- ext → Oracle.customers
  rating       smallint      NOT NULL,
  comment      varchar(500),
  rated_at     timestamp     NOT NULL,
  created_at   timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_driver_ratings PRIMARY KEY (delivery_id),                   -- RN-26
  CONSTRAINT ck_driver_ratings_rating CHECK (rating BETWEEN 1 AND 5)
);

CREATE TABLE restaurant_ratings (
  restaurant_order_id  bigint        NOT NULL,
  restaurant_id        bigint        NOT NULL,
  customer_id          bigint        NOT NULL,                              -- ext → Oracle.customers
  rating               smallint      NOT NULL,
  comment              varchar(500),
  rated_at             timestamp     NOT NULL,
  created_at           timestamp     NOT NULL DEFAULT localtimestamp,
  CONSTRAINT pk_restaurant_ratings PRIMARY KEY (restaurant_order_id),
  CONSTRAINT ck_restaurant_ratings_rating CHECK (rating BETWEEN 1 AND 5)
);
```

As `CHECK` de `review_started_at >= opened_at` e `decided_at >= review_started_at` passam quando um dos lados é nulo
(o `CHECK` só recusa `false`); a obrigatoriedade vem das igualdades acima delas.

### F1.5 Índices não únicos e triggers

Só o que o simulador consulta com frequência; o CDC não precisa de índice. Índices parciais sobre os estados "vivos"
ficam pequenos, porque a maioria das linhas termina em estado final.

```sql
CREATE INDEX ix_restaurant_orders_live ON restaurant_orders (status, created_at)
  WHERE status IN ('in_analysis', 'accepted', 'preparing', 'ready_for_pickup');   -- prazos da RN-28
CREATE INDEX ix_deliveries_live ON deliveries (status)
  WHERE status IN ('awaiting_assignment', 'assigned', 'in_transit');             -- atribuição (RN-06)
CREATE INDEX ix_deliveries_finished ON deliveries (finished_at)
  WHERE status = 'delivered';                                                    -- relógios de 10 min, 20 min e 24 h
CREATE INDEX ix_shifts_open_city ON shifts (city_id) WHERE status = 'open';      -- motorista livre na cidade (RN-35)
CREATE INDEX ix_driver_assignments_shift ON driver_assignments (shift_id);       -- ganho do turno (RN-36)
CREATE INDEX ix_stock_movements_item ON stock_movements (stock_item_id, occurred_at);
CREATE INDEX ix_product_recipes_stock_item ON product_recipes (stock_item_id);   -- comprometido no aceite (RN-39)
CREATE INDEX ix_products_restaurant ON products (restaurant_id);
CREATE INDEX ix_payment_components_item ON payment_components (restaurant_order_id, line_number)
  WHERE restaurant_order_id IS NOT NULL;                                         -- reembolso por atendimento
CREATE INDEX ix_refunds_payment ON refunds (payment_id);
CREATE INDEX ix_incidents_order ON incidents (order_id);
CREATE INDEX ix_incidents_live ON incidents (status) WHERE status IN ('open', 'in_review');
CREATE INDEX ix_incident_items_item ON incident_items (restaurant_order_id, line_number);  -- teto da RN-14
```

Trigger `set_updated_at` (F1.0) em: `cities`, `restaurants`, `products`, `stock_items`, `product_recipes`, `orders`,
`restaurant_orders`, `deliveries`, `shifts`, `driver_assignments`, `incidents`. As demais tabelas são só INSERT.

### Decisões da revisão da F1 (2026-11-04)

| # | Tema | Decisão |
|---|---|---|
| 1 | Restrições no banco | **`CHECK` de domínio e de invariante de linha** (F1.0 #3 e #4). A L4 ganha um quarto mecanismo, entre o índice único e o simulador: o `CHECK` recusa a escrita no banco para o que se vê numa linha só |
| 2 | Texto | **`varchar(n)`** com tamanho explícito; **`char(n)`** com `CHECK` de formato para CNPJ, CEP, UF e código de rastreio |
| 3 | Schema | **`ubereats`** |
| 4 | `updated_at` | **Trigger `set_updated_at`**, que preenche só quando o escritor não mudou o valor |
| 5 | Índices não únicos | **Os 13 da F1.5**, parciais nos estados vivos |

Achado do teste: o contêiner sem `TZ` gravou `localtimestamp` em UTC. Confirma o `TZ=America/Sao_Paulo` da F0 (decisão 3)
como passo obrigatório da regeração.

---

## F2. DDL Oracle

Banco do domínio **Pessoas** (ADR 006): `cities` (cópia idêntica à do Postgres), `customers` e `drivers`. As três tabelas
são cadastros do ShadowTraffic: ele faz o INSERT com a chave vinda de `sequentialInteger` (F0, decisão 8), e o simulador só
lê (abertura de turno e montagem da compra, ADR 009).

### F2.0 Convenções físicas

Valem as da F1.0, com as traduções abaixo.

| # | Tema | Proposta |
|---|---|---|
| 1 | Schema | O usuário de aplicação **`UBEREATS`** no PDB `FREEPDB1` (no Oracle, schema é usuário). Mesmo nome do schema do Postgres |
| 2 | Tipos | `bigint` → `NUMBER(18)`, `integer` → `NUMBER(9)`, `numeric(p,s)` → `NUMBER(p,s)`, `varchar(n)` → **`VARCHAR2(n CHAR)`**, `char(n)` → `CHAR(n CHAR)`. A semântica `CHAR` conta caracteres, não bytes: "São Paulo" em UTF-8 tem mais bytes que letras |
| 3 | Booleano | **`NUMBER(1)` + `CHECK (IN (0, 1))`**. O `BOOLEAN` nativo do Oracle 23 **não é suportado pelo Debezium** (doc 3.5: o conector pula a coluna e o dado se perde) |
| 4 | Chaves | `NUMBER(18)` sem default nem identidade: quem fornece é o ShadowTraffic |
| 5 | Rastro | `created_at`/`updated_at` com default **`CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP)`**: hora de Brasília calculada no banco, sem depender do fuso do contêiner nem da sessão. Trigger `BEFORE UPDATE` com a mesma regra da F1 (só preenche se o escritor não mudou) |
| 6 | Data | `date_of_birth` em `DATE` com `CHECK (date_of_birth = TRUNC(date_of_birth))` (o `DATE` do Oracle tem hora). No Debezium, `DATE` do Oracle chega como `io.debezium.time.Timestamp` (ms); a Bronze converte para `DATE` (F4) |
| 7 | Texto vazio | No Oracle, `''` é `NULL`. Coluna opcional tem de ser nula de verdade (`address_line2`); nas obrigatórias o `NOT NULL` recusa a string vazia |
| 8 | Nomes | Os mesmos da F1 (`pk_`, `uq_`, `ck_`, `ix_`), mais `trg_<tabela>_updated_at`. Sem aspas: o Oracle guarda em maiúsculas |

### F2.1 Datas vindas do ShadowTraffic

**Problema.** O ShadowTraffic grava datas como texto (`formatDateTime`), e o Oracle converte texto em `TIMESTAMP` pelo
`NLS_TIMESTAMP_FORMAT` da sessão, que por padrão é `DD-MON-RR HH.MI.SSXFF AM`. Foi por isso que as tabelas atuais guardam datas
em `VARCHAR2` (comentário em `shared/sql/oracle/02_create_tables.sh`), o que fere a L0 #4. Reproduzido no teste: `ORA-01843`.

**Proposta (recomendada): gatilho de logon no schema**, que fixa o formato ISO e o fuso de toda sessão do `UBEREATS`. O
template grava `yyyy-MM-dd HH:mm:ss[.SSS]` e `yyyy-MM-dd` para datas.

```sql
CREATE OR REPLACE TRIGGER trg_ubereats_logon
  AFTER LOGON ON ubereats.SCHEMA
BEGIN
  EXECUTE IMMEDIATE q'[ALTER SESSION SET NLS_DATE_FORMAT = 'YYYY-MM-DD']';
  EXECUTE IMMEDIATE q'[ALTER SESSION SET NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF']';
  EXECUTE IMMEDIATE q'[ALTER SESSION SET TIME_ZONE = 'America/Sao_Paulo']';
END;
/
```

Alternativas: manter `VARCHAR2` (fere a L0 #4 e empurra a conversão para a Bronze); ou um usuário só para o gerador com o
mesmo gatilho (mais um usuário sem ganho, porque o simulador só lê).

### F2.2 DDL

```sql
-- Conectado como UBEREATS em FREEPDB1 (o schema é o próprio usuário).

CREATE TABLE cities (
  city_id     NUMBER(9)           NOT NULL,
  name        VARCHAR2(100 CHAR)  NOT NULL,
  state_code  CHAR(2 CHAR)        NOT NULL,
  created_at  TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  updated_at  TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  CONSTRAINT pk_cities PRIMARY KEY (city_id),
  CONSTRAINT ck_cities_city_id CHECK (city_id BETWEEN 1000000 AND 5999999),
  CONSTRAINT ck_cities_state_code CHECK (REGEXP_LIKE(state_code, '^[A-Z]{2}$'))
);

CREATE TABLE customers (
  customer_id     NUMBER(18)          NOT NULL,
  first_name      VARCHAR2(60 CHAR)   NOT NULL,
  last_name       VARCHAR2(80 CHAR)   NOT NULL,
  email           VARCHAR2(150 CHAR)  NOT NULL,
  email_verified  NUMBER(1)           NOT NULL,
  phone_number    VARCHAR2(20 CHAR)   NOT NULL,
  phone_verified  NUMBER(1)           NOT NULL,
  address_line1   VARCHAR2(200 CHAR)  NOT NULL,
  address_line2   VARCHAR2(100 CHAR),
  postal_code     CHAR(8 CHAR)        NOT NULL,
  latitude        NUMBER(9,6)         NOT NULL,
  longitude       NUMBER(9,6)         NOT NULL,
  city_id         NUMBER(9)           NOT NULL,
  date_of_birth   DATE                NOT NULL,
  gender          VARCHAR2(20 CHAR)   NOT NULL,
  status          VARCHAR2(20 CHAR)   NOT NULL,
  signup_date     TIMESTAMP           NOT NULL,
  last_login      TIMESTAMP           NOT NULL,
  created_at      TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  updated_at      TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  CONSTRAINT pk_customers PRIMARY KEY (customer_id),
  CONSTRAINT uq_customers_email UNIQUE (email),
  CONSTRAINT ck_customers_flags CHECK (email_verified IN (0, 1) AND phone_verified IN (0, 1)),
  CONSTRAINT ck_customers_postal_code CHECK (REGEXP_LIKE(postal_code, '^[0-9]{8}$')),
  CONSTRAINT ck_customers_coords CHECK (latitude BETWEEN -90 AND 90 AND longitude BETWEEN -180 AND 180),
  CONSTRAINT ck_customers_birth CHECK (date_of_birth = TRUNC(date_of_birth)),
  CONSTRAINT ck_customers_gender CHECK (gender IN ('female', 'male', 'other', 'not_informed')),
  CONSTRAINT ck_customers_status CHECK (status IN ('active', 'suspended', 'inactive')),
  CONSTRAINT ck_customers_login CHECK (last_login >= signup_date)
);

CREATE TABLE drivers (
  driver_id          NUMBER(18)          NOT NULL,
  first_name         VARCHAR2(60 CHAR)   NOT NULL,
  last_name          VARCHAR2(80 CHAR)   NOT NULL,
  email              VARCHAR2(150 CHAR)  NOT NULL,
  phone_number       VARCHAR2(20 CHAR)   NOT NULL,
  vehicle_type       VARCHAR2(20 CHAR)   NOT NULL,
  vehicle_make       VARCHAR2(50 CHAR)   NOT NULL,
  vehicle_model      VARCHAR2(50 CHAR)   NOT NULL,
  vehicle_year       NUMBER(9)           NOT NULL,
  license_plate      CHAR(7 CHAR)        NOT NULL,
  license_number     CHAR(11 CHAR)       NOT NULL,
  city_id            NUMBER(9)           NOT NULL,
  status             VARCHAR2(20 CHAR)   NOT NULL,
  registration_date  TIMESTAMP           NOT NULL,
  last_login         TIMESTAMP           NOT NULL,
  created_at         TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  updated_at         TIMESTAMP           DEFAULT CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP) NOT NULL,
  CONSTRAINT pk_drivers PRIMARY KEY (driver_id),
  CONSTRAINT uq_drivers_license_plate UNIQUE (license_plate),
  CONSTRAINT uq_drivers_license_number UNIQUE (license_number),
  CONSTRAINT ck_drivers_vehicle_type CHECK (vehicle_type IN ('car', 'motorcycle', 'scooter')),
  CONSTRAINT ck_drivers_vehicle_year CHECK (vehicle_year BETWEEN 1990 AND 2100),
  CONSTRAINT ck_drivers_license_plate CHECK (REGEXP_LIKE(license_plate, '^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$')),
  CONSTRAINT ck_drivers_license_number CHECK (REGEXP_LIKE(license_number, '^[0-9]{11}$')),
  CONSTRAINT ck_drivers_status CHECK (status IN ('active', 'suspended', 'inactive')),
  CONSTRAINT ck_drivers_login CHECK (last_login >= registration_date)
);

CREATE INDEX ix_drivers_city_status ON drivers (city_id, status);

CREATE OR REPLACE TRIGGER trg_cities_updated_at
  BEFORE UPDATE ON cities FOR EACH ROW
BEGIN
  IF :NEW.updated_at = :OLD.updated_at THEN
    :NEW.updated_at := CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP);
  END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_customers_updated_at
  BEFORE UPDATE ON customers FOR EACH ROW
BEGIN
  IF :NEW.updated_at = :OLD.updated_at THEN
    :NEW.updated_at := CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP);
  END IF;
END;
/

CREATE OR REPLACE TRIGGER trg_drivers_updated_at
  BEFORE UPDATE ON drivers FOR EACH ROW
BEGIN
  IF :NEW.updated_at = :OLD.updated_at THEN
    :NEW.updated_at := CAST(SYSTIMESTAMP AT TIME ZONE 'America/Sao_Paulo' AS TIMESTAMP);
  END IF;
END;
/
```

Índice não único: `ix_drivers_city_status`, para o simulador achar motoristas ativos da cidade ao abrir turno (RN-35, RN-42).

### F2.3 Diferenças em relação ao lógico

| Coluna | Lógico | Físico proposto | Motivo |
|---|---|---|---|
| `customers.address_line2` | obrigatória | **nula** | Complemento é opcional, e `''` é `NULL` no Oracle |
| `customers.gender` | sem lista | `female`, `male`, `other`, `not_informed` | Domínio em minúsculas, como os demais |
| `drivers.vehicle_type` | sem lista | `car`, `motorcycle`, `scooter` | O gerador atual sorteia também `Bicycle`, que não tem placa nem CNH |
| `drivers.license_plate` | `varchar` | `CHAR(7)`, formato antigo ou Mercosul, **único** | `ABC1234` ou `ABC1D23` |
| `drivers.license_number` | `varchar` | `CHAR(11)` só dígitos, **único** | CNH tem 11 dígitos |
| `customers.last_login`, `drivers.last_login` | — | `CHECK` ≥ data de cadastro | Invariante de linha (F1.0 #4) |

### F2.4 Validação

DDL aplicado num contêiner descartável `gvenzl/oracle-free:23.4-full` (sem volume; o `oracle-ubereats` não foi tocado), em
2026-11-04. Resultado: 3 tabelas, 15 `CHECK`, 4 triggers (3 de `updated_at` e o de logon), sem erro.

| Teste | Resultado |
|---|---|
| Texto ISO num `TIMESTAMP` sem o gatilho de logon | `ORA-01843` (o problema de hoje) |
| O mesmo texto, com e sem fração, e `date_of_birth` em `yyyy-MM-dd`, com o gatilho | Gravado |
| Default de `created_at` com o contêiner em UTC | Hora de Brasília (08:41 com UTC 11:41) |
| 8 `CHECK` testados e o único do e-mail | Todos recusaram o valor inválido |
| `address_line1 = ''` | Recusado como `NULL` (`ORA-01407`) |
| Trigger de `updated_at` | Manteve o valor informado; preencheu quando o escritor não mudou |

### Decisões da revisão da F2 (2026-11-04)

| # | Tema | Decisão |
|---|---|---|
| 1 | Datas vindas do ShadowTraffic | **Gatilho de logon** no schema `UBEREATS`: `NLS_DATE_FORMAT = 'YYYY-MM-DD'`, `NLS_TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF'` e `TIME_ZONE = 'America/Sao_Paulo'`. Datas em `TIMESTAMP`/`DATE`, nunca em `VARCHAR2` |
| 2 | Booleano | **`NUMBER(1)` + `CHECK (0, 1)`**; na F4, o `NumberOneToBooleanConverter` entrega booleano no evento. Conferido na doc do Debezium 3.7 (estável mais recente): o `BOOLEAN` nativo do Oracle 23 segue sem suporte, então atualizar o Debezium não resolve isso (a atualização 3.0 → 3.7 é avaliada na F4 por outros motivos) |
| 3 | Tipo de veículo | **Só motorizado**: `car`, `motorcycle`, `scooter`; placa e CNH obrigatórias e únicas. O `Bicycle` do gerador atual sai na regeração |
| 4 | Diferenças em relação ao lógico | **Aceitas** as da F2.3: `address_line2` nula, lista de `gender`, placa `CHAR(7)` e CNH `CHAR(11)` únicas, `last_login` ≥ data de cadastro |

**Para a F4:** `date_of_birth` (`DATE` do Oracle) chega como `io.debezium.time.Timestamp` em ms; a Bronze converte para `DATE`.
