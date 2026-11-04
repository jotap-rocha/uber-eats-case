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
| F3 | MongoDB (`restaurant_profiles`). O MinIO saiu do escopo ([ADR 010](../../../docs/adr/010-minio-fora-do-escopo-da-geracao.md); lógica guardada em [`minio/historico-geracao.md`](../minio/historico-geracao.md)) | aprovada |
| F4 | CDC: configuração do Debezium, tópicos, contrato `cdc_*` visto da fonte | aprovada |
| F5 | Plano da regeração: ordem de carga, divisão gerador × simulador, testes T1 a T19 como consultas | aprovada |

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
dígitos). Isso corrige a tradução "`bigint` → `NUMBER(19)`" da L1a e do handoff. **Depois:** o teste da F4 mostrou que,
com `decimal.handling.mode=string`, o Debezium 3.7 entrega também `NUMBER(18)` e `NUMBER(9)` como texto; a Bronze faz `CAST`
(F4.3 e decisões da F4).

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

---

## F3. MongoDB

Uma coleção: **`restaurant_profiles`** no banco `ubereats` (L1a), um documento por restaurante com as janelas de funcionamento
(RN-41) e o cardápio (RN-23). O MinIO saiu do escopo ([ADR 010](../../../docs/adr/010-minio-fora-do-escopo-da-geracao.md)).

### F3.0 Quem gera o perfil

**Achado.** A ADR 009 (decisão 2) pôs o MongoDB com o ShadowTraffic, mas **o ShadowTraffic não tem conexão para MongoDB**
(a lista de conexões da doc tem Kafka, Postgres, MySQL, Oracle, S3, filesystem, Redis, webhook, Pub/Sub e outras, sem Mongo).
Hoje o perfil vem de um seed estático em JavaScript (`shared/mongo/init/01_perfil_restaurante.js.template`), rodado uma vez
na criação do contêiner, com cardápio sem `product_id` (contradiz a RN-23). Além disso, o cardápio tem de listar os produtos
**do próprio restaurante**, cada um uma vez (T18), o que os `lookup` independentes do ShadowTraffic não garantem.

**Proposta (recomendada): seed em Python, no pacote do simulador**, rodado depois da carga dos cadastros: lê `restaurants` e
`products` no Postgres e grava um perfil por restaurante, com todos os produtos dele, 1 ou 2 janelas e as seções. Idempotente
(`replaceOne` com `upsert` por `_id`), então pode rodar de novo se entrarem restaurantes. Corrige a ADR 009 com um adendo.

Alternativas: manter o seed em JavaScript (o `mongosh` não lê o Postgres; o cardápio teria de adivinhar os ids); ou o
simulador criar o perfil quando encontra restaurante sem perfil (mais peça no laço principal, sem ganho).

**Achado para a F5.** A mesma coerência vale para o catálogo no Postgres: todo produto precisa de ficha técnica com itens de
estoque do mesmo restaurante, e os `lookup` independentes do ShadowTraffic também não garantem isso. A divisão da carga do
catálogo (ShadowTraffic ou seed em Python) fica para a F5.

### F3.1 Documento

| Campo | Tipo BSON | Regra |
|---|---|---|
| `_id` | `long` | **O `restaurant_id`** (`ext → Postgres.restaurants`). Chave natural: unicidade de graça e chave simples no CDC |
| `service_windows` | array, 1 a 2 | RN-41 |
| `service_windows[].start_time`, `end_time` | `string` `HH:MM` | Hora de Brasília; `end_time` > `start_time` no mesmo dia (sem virar a meia-noite na v1) |
| `menu_items` | array, ao menos 1 | Item de Cardápio (RN-23) |
| `menu_items[].product_id` | `long` | `ext → Postgres.products`, do mesmo restaurante; único em toda a coleção |
| `menu_items[].section` | `string` | `starters`, `mains`, `sides`, `desserts`, `drinks`, `combos` |
| `menu_items[].display_order` | `int` | ≥ 1 |
| `menu_items[].highlighted` | `bool` | |
| `menu_items[].customizations` | array de `string` | Rótulos sem preço (ex.: "sem cebola"); sem repetição |
| `created_at`, `updated_at` | `date` | Instante BSON (UTC por definição); quem grava é o seed |

Nome e preço **não** ficam no item (vêm do produto, RN-23); o validador recusa campos extras.

### F3.2 Validador e índice

```javascript
// Banco ubereats, coleção restaurant_profiles (um documento por restaurante).
db = db.getSiblingDB("ubereats");

const hhmm = "^([01][0-9]|2[0-3]):[0-5][0-9]$";

db.createCollection("restaurant_profiles", {
  validationLevel: "strict",
  validationAction: "error",
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: ["_id", "service_windows", "menu_items", "created_at", "updated_at"],
      additionalProperties: false,
      properties: {
        _id: { bsonType: "long", minimum: 1, description: "restaurant_id (ext → Postgres.restaurants)" },
        service_windows: {
          bsonType: "array", minItems: 1, maxItems: 2,
          items: {
            bsonType: "object",
            required: ["start_time", "end_time"],
            additionalProperties: false,
            properties: {
              start_time: { bsonType: "string", pattern: hhmm },
              end_time: { bsonType: "string", pattern: hhmm }
            }
          }
        },
        menu_items: {
          bsonType: "array", minItems: 1,
          items: {
            bsonType: "object",
            required: ["product_id", "section", "display_order", "highlighted", "customizations"],
            additionalProperties: false,
            properties: {
              product_id: { bsonType: "long", minimum: 1 },
              section: { enum: ["starters", "mains", "sides", "desserts", "drinks", "combos"] },
              display_order: { bsonType: "int", minimum: 1 },
              highlighted: { bsonType: "bool" },
              customizations: {
                bsonType: "array", uniqueItems: true,
                items: { bsonType: "string", minLength: 1, maxLength: 60 }
              }
            }
          }
        },
        created_at: { bsonType: "date" },
        updated_at: { bsonType: "date" }
      }
    }
  }
});

// Um produto aparece no máximo uma vez em todo o conjunto de cardápios (cada produto é de um só restaurante).
db.restaurant_profiles.createIndex({ "menu_items.product_id": 1 }, { name: "uq_restaurant_profiles_product", unique: true });
print("ok: coleção e índice criados");
```

O validador (`$jsonSchema`, `strict` e `error`) faz o papel do `CHECK` da F1: tipo, obrigatoriedade, lista de valores,
formato da hora e quantidade de janelas. O que ele não vê fica com o seed e os testes:

| Regra | Quem garante |
|---|---|
| Produto do mesmo restaurante; todo restaurante tem perfil | Seed e T18 |
| Mesmo produto duas vezes **no mesmo** perfil | Seed e T18 (o índice único do MongoDB não compara itens do mesmo documento) |
| Janelas sem sobreposição e `end_time` > `start_time` | Seed e teste novo da F5 |

### F3.3 Diferenças em relação ao lógico

| Campo | Lógico | Físico proposto | Motivo |
|---|---|---|---|
| `restaurant_id` | campo `integer`, único | vira o **`_id`** (`long`) | Unicidade pelo próprio `_id` |
| `product_id` | `integer` | `long` | Mesmo tamanho do `bigint` do Postgres |
| `section` | `string` livre | lista em minúsculas | Domínio, como os demais |
| `customizations` | lista | lista de `string` sem preço | Sem dinheiro no MongoDB |
| `created_at`, `updated_at` | — | `date` (instante UTC) | Rastro, como nas outras tabelas. Exceção à L0 #4: o tipo de data do BSON é sempre instante; a Bronze converte para `America/Sao_Paulo` |

### F3.4 Validação

Contêiner descartável `mongo:7` (sem volume; o `mongo-ubereats` não foi tocado), em 2026-11-04.

| Teste | Resultado |
|---|---|
| Perfil com 2 janelas e com 1 janela | Aceitos |
| Restaurante repetido; mesmo produto em outro perfil | Recusados (`E11000`) |
| 3 janelas, nenhuma janela, `24:00`, cardápio vazio, seção fora da lista, `product_id` `double`, preço no item, campo `restaurant_id` solto | Recusados (`Document failed validation`) |
| Mesmo produto duas vezes no mesmo perfil | **Aceito**: fica com o seed e o T18 |

**Para a F4:** o CDC do MongoDB (change streams, que o Airbyte usa) exige **replica set**; o `mongo-ubereats` de hoje roda
sozinho (sem `--replSet`).

### Decisões da revisão da F3 (2026-11-04)

| # | Tema | Decisão |
|---|---|---|
| 1 | Quem gera o perfil | **Seed em Python no pacote do simulador**, depois da carga dos cadastros: lê `restaurants` e `products` no Postgres e grava um perfil por restaurante (`replaceOne` com `upsert` por `_id`). Substitui o seed em JavaScript. Adendo na [ADR 009](../../../docs/adr/009-simulador-cria-a-compra-numa-transacao.md) |
| 2 | Chave do documento | **`_id` = `restaurant_id`** (`long`) |
| 3 | Datas de rastro | **`date` do BSON** (instante UTC); a Bronze converte para `America/Sao_Paulo`. Única exceção à L0 #4 |
| 4 | Validador e diferenças | **Aceitos**: `$jsonSchema` estrito, índice único `uq_restaurant_profiles_product`, seções em minúsculas, personalizações como texto sem preço |

**Para a F4:** o MongoDB precisa de replica set para o CDC. **Para a F5:** quem carrega o catálogo do Postgres com fichas
técnicas coerentes (ShadowTraffic ou seed em Python).

---

## F4. CDC

Captura das três fontes regeneradas: **Debezium** (Kafka Connect) no Postgres e no Oracle, **Airbyte** no MongoDB
([ADR 006](../../../docs/adr/006-inversao-de-dominios-entre-oracle-e-postgres.md), decisão 4). Os templates dos conectores
locais e as propriedades do Debezium Server (GCP) já seguem esta seção; os da Azure ficam para a Fase 1 (F4.7); o `docker-compose.yml` e os scripts de init dos bancos mudam só na
regeração (F5). Nada foi registrado nem aplicado em `postgres-ubereats`, `oracle-ubereats`, `mongo-ubereats` ou
`kafka-connect`.

### F4.0 Convenções

| # | Tema | Proposta |
|---|---|---|
| 1 | Versão | **Debezium 3.7** (`quay.io/debezium/connect:3.7`, `quay.io/debezium/server:3.7`), ver F4.1 |
| 2 | Formato da mensagem | **JSON sem schema** (`schemas.enable=false`) e **envelope completo** (`before`, `after`, `source`, `op`), sem o SMT `ExtractNewRecordState`. A Bronze lê o envelope e grava as colunas `cdc_*`; a Silver nunca lê o formato nativo |
| 3 | Decimal | `decimal.handling.mode=string` nos dois conectores (F0, decisão 2) |
| 4 | Tempo | Sem transform (F0, decisão 3). `time.precision.mode` no padrão: `timestamp` vira `MicroTimestamp` (µs); `DATE` do Oracle vira `Timestamp` (ms) |
| 5 | Snapshot | `snapshot.mode=initial`, com o conector **registrado depois do DDL e antes da carga**: todo evento da regeração chega como `c`, com `ts_ms` e posição de log reais. Um `r` (snapshot de recuperação) é tratado como `c` |
| 6 | Tópicos | `<prefixo>.<schema>.<tabela>`, criados pelo próprio conector (`topic.creation.default.*`): 1 partição, `cleanup.policy=delete`, retenção de 7 dias (F4.5) |
| 7 | Exclusão | Tombstone ligado (padrão): depois do `d` vem uma mensagem de valor nulo com a mesma chave. A Bronze descarta valor nulo |
| 8 | Segredos | Templates com `REPLACE_*`; as senhas ficam no `shared/gen/.env` (`POSTGRES_DEBEZIUM_USER`, `POSTGRES_DEBEZIUM_PASSWORD`, `ORACLE_DBZ_PASSWORD`) |

### F4.1 Versão do Debezium

Hoje: `quay.io/debezium/connect:3.0` (`kafka-connect`, `kafka-connect-azure`) e `debezium/server:3.0` (Docker Hub, Fase 3).
O `BOOLEAN` nativo do Oracle 23 continua sem suporte no 3.7 (F2, decisão 2), então o motivo para subir é outro:

- **Custo zero agora.** Com a regeração do zero não há offset, slot nem histórico de schema para migrar. Depois que os
  conectores estiverem rodando, a troca de versão passa a exigir teste de compatibilidade de offsets.
- **Suporte.** O projeto Debezium só corrige a série mais recente; o 3.0 é de 2024 e usa Kafka Connect 3.x. O 3.7
  (GA no fim de setembro de 2026) roda sobre Kafka Connect 4.3.
- **Imagens.** O Docker Hub não tem `debezium/server:3.7` nem `debezium/connect:3.7`: as imagens novas só saem no
  `quay.io`. A troca corrige também a origem da imagem do Debezium Server.
- **Testado aqui.** O 3.7.0.Final passou na validação da F4.8 com os DDL da F1 e da F2.

Alternativa: manter o 3.0 (funciona com tudo da F4, mas fica numa série sem correções e a troca futura custa mais).

### F4.2 Conector Postgres

Não existia template local (o Postgres era capturado pelo Airbyte antes da ADR 006). Novo arquivo
[`config/shared/debezium/postgres-connector.json.template`](../../../config/shared/debezium/postgres-connector.json.template).

**No banco** (script de init da regeração, rodado pelo dono das tabelas):

```sql
-- Usuário só do CDC: replicação + leitura para o snapshot.
CREATE ROLE dbz_ubereats WITH LOGIN REPLICATION PASSWORD :'dbz_password';   -- POSTGRES_DEBEZIUM_PASSWORD
GRANT USAGE ON SCHEMA ubereats TO dbz_ubereats;
GRANT SELECT ON ALL TABLES IN SCHEMA ubereats TO dbz_ubereats;
ALTER DEFAULT PRIVILEGES IN SCHEMA ubereats GRANT SELECT ON TABLES TO dbz_ubereats;

-- Publicação do schema inteiro (Postgres 15+): tabela nova do schema entra sozinha.
CREATE PUBLICATION dbz_ubereats FOR TABLES IN SCHEMA ubereats;
```

**No servidor** (`command` do `postgres-ubereats`): `wal_level=logical` (já existe) e **`max_slot_wal_keep_size=4GB`**. Sem
esse teto, um conector parado faz o slot reter WAL sem limite no VHDX da D: (risco da ADR 006). Com ele, se o atraso passar
de 4 GB o slot é invalidado e o conector precisa de novo snapshot: perde-se a continuidade, não o disco.

**`REPLICA IDENTITY`:** fica o **padrão** (chave primária), porque toda tabela da F1 tem PK. No `u`, o `after` vem completo;
no `d`, o `before` traz **só a chave** (as outras colunas chegam com zero ou texto vazio, visto no teste). A Bronze usa só a
chave no `d`. `FULL` aumentaria o WAL de `orders` sem uso na Bronze SCD1.

Propriedades do conector (o template completo traz também os conversores JSON):

| Propriedade | Valor |
|---|---|
| `connector.class` | `io.debezium.connector.postgresql.PostgresConnector` |
| `database.user` / `database.dbname` | `dbz_ubereats` / o `POSTGRES_DB` do `.env` |
| `topic.prefix` | `postgres` |
| `plugin.name` | `pgoutput` |
| `publication.name` / `publication.autocreate.mode` | `dbz_ubereats` / `disabled` (a publicação nasce no init, e o usuário do CDC não precisa ser dono das tabelas) |
| `slot.name` | `dbz_ubereats` (um slot por consumidor: `dbz_ubereats_kappa` no conector do Kappa na Fase 1, `dbz_ubereats_gcp` na Fase 3, todos sobre a mesma publicação) |
| `schema.include.list` | `ubereats` |
| `snapshot.mode` | `initial` |
| `decimal.handling.mode` | `string` |
| `heartbeat.interval.ms` | `60000` (mantém o slot avançando quando nada muda; tópico `__debezium-heartbeat.postgres`) |
| `topic.creation.default.*` | `replication.factor=1`, `partitions=1`, `cleanup.policy=delete`, `retention.ms=604800000` |

### F4.3 Conector Oracle

Mudanças no [`config/shared/debezium/oracle-connector.json.template`](../../../config/shared/debezium/oracle-connector.json.template)
(o resto fica: `c##dbzuser`, `FREE`/`FREEPDB1`, prefixo `oracle`, `online_catalog`, `snapshot.mode=initial`, conversores JSON):

| Propriedade | Antes | Agora |
|---|---|---|
| `table.include.list` | `RESTAURANTS`, `PRODUCTS`, `INVENTORY`, `ORDERS`, `PAYMENTS`, `ORDER_ITEMS`, `RECEIPTS` | `UBEREATS.CITIES,UBEREATS.CUSTOMERS,UBEREATS.DRIVERS` |
| `decimal.handling.mode` | `double` | `string` |
| `converters` | — | `boolean` |
| `boolean.type` | — | `io.debezium.connector.oracle.converters.NumberOneToBooleanConverter` |
| `boolean.selector` | — | `.*CUSTOMERS.EMAIL_VERIFIED,.*CUSTOMERS.PHONE_VERIFIED` |
| `schema.history.internal.store.only.captured.tables.ddl` | — | `true` (o histórico guarda só o DDL das 3 tabelas) |
| `topic.creation.default.*` | — | Iguais aos do Postgres |

O `00_enable_archivelog.sql` e o `01_create_user.sh` (archivelog, supplemental logging `ALL COLUMNS`, grants do
`c##dbzuser`) continuam valendo. Com `ALL COLUMNS`, o `before` do Oracle vem completo também no `d`.

**Achado do teste (corrige a F0.2).** Com `decimal.handling.mode=string`, **`NUMBER(18)` e `NUMBER(9)` também chegam como
texto** (`"CUSTOMER_ID": "1"`, inclusive na chave da mensagem): no 3.7, a regra "`NUMBER(p,0)` com p ≤ 18 vira `int64`"
não vale nesse modo. A Bronze faz `CAST` para `BIGINT`/`INT` (ela já declara o tipo de cada coluna). Os tipos `NUMBER(18)` e
`NUMBER(9)` da F2 continuam: valem pelo `CHECK` de tamanho e pela tradução para os warehouses.

### F4.4 MongoDB

O Airbyte exige **replica set** para o conector MongoDB, até em full refresh (a doc lista replica set ou cluster shardado;
nó único serve para desenvolvimento). O `mongo-ubereats` roda sozinho, então a regeração muda o serviço:

```yaml
  mongo-ubereats:
    image: mongo:7
    command: ["--replSet", "rs0", "--bind_ip_all", "--oplogSize", "1024"]
    healthcheck:
      # O rs.initiate fica no init (shared/mongo/init/00_replica_set.js); o healthcheck só confere o primário.
      test: ["CMD", "mongosh", "--quiet", "--eval", "db.hello().isWritablePrimary ? 0 : 1"]
      interval: 10s
      retries: 20
      start_period: 10s
```

| Ponto | Proposta |
|---|---|
| Nome do membro | `localhost:27017` (corrigido na F5.2; era `mongo-ubereats:27017`). Quem está fora da rede do compose (Airbyte via `abctl`, seed e simulador no Windows) conecta com **`directConnection=true`**, sem descoberta do replica set (senão o driver tenta resolver `mongo-ubereats`) |
| Oplog | `--oplogSize 1024` (MB; corrigido na F5.2, a opção `--oplogSizeMB` não existe no `mongod`): o padrão é 5% do disco, alto para a D: |
| **Depois (F5.2)** | O teste do init mostrou duas correções. (1) O entrypoint da imagem `mongo:7` só tira o `--replSet` do `mongod` temporário do init **quando há usuário root** (autenticação); sem autenticação, o init roda em replica set não iniciado e o `createCollection` falha com `not primary`. O `rs.initiate` passa para o init (`00_replica_set.js`, antes da coleção), com o membro `localhost:27017`, porque o `mongod` do init só escuta em 127.0.0.1. Todo cliente fora do compose já usa `directConnection=true`, e a partir do Windows `localhost:27017` é a porta publicada. (2) A opção do oplog é `--oplogSize` |
| Autenticação | O Mongo roda **sem** autenticação hoje. Se for ligada, replica set exige `keyFile`; fica fora da F4 |
| Captura no Airbyte | **Incremental por change stream** (CDC), modo de atualização *Lookup* (documento inteiro). O seed é idempotente e pode reescrever perfis (`replaceOne`); o CDC entrega essas mudanças e as exclusões, e o full refresh releria a coleção inteira a cada sync. Substitui a decisão antiga "MongoDB sem CDC" (`azure/docs/data-contract-cdc-azure.md`) |

### F4.5 Tópicos

| Fonte | Tópico | Observação |
|---|---|---|
| Postgres | `postgres.ubereats.<tabela>` (28) | Minúsculas, como no banco |
| Postgres | `__debezium-heartbeat.postgres` | Heartbeat (F4.2) |
| Oracle | `oracle.UBEREATS.CITIES`, `.CUSTOMERS`, `.DRIVERS` | Maiúsculas, como o Oracle guarda |
| Oracle | `schema-changes.oracle-ubereats` | Histórico de schema; criado pelo conector |
| MongoDB | — | O Airbyte grava direto no destino (sem barramento na Fase 0) |
| Connect | `connect_configs`, `connect_offsets`, `connect_status` | Já existem |

Partição e retenção no Redpanda: **1 partição** (a ordem por chave vale de qualquer jeito; uma partição mantém a ordem total
de cada tópico) e **`delete` com 7 dias**, que cobrem uma semana de pipeline parado. Sem compactação: o histórico de
mudanças é o dado do Kappa.

### F4.6 Contrato `cdc_*` visto da fonte

| Coluna | Postgres (Debezium) | Oracle (Debezium) | MongoDB (Airbyte) | Tipo na Bronze |
|---|---|---|---|---|
| `cdc_operation` | `op` (`c`, `u`, `d`; `r` → `c`) | `op` (idem) | `_ab_cdc_deleted_at` preenchido → `d`, senão `u` | `STRING` |
| `cdc_commit_ts` | `source.ts_ms` (commit) | `source.ts_ms` (= `commit_ts_ms`, precisão de segundo) | `_ab_cdc_updated_at` | `TIMESTAMP` (instante UTC) |
| `cdc_sequence` | `source.lsn` (número) | `source.scn` (texto) | `_ab_cdc_cursor` | `DECIMAL(20,0)` |
| `cdc_source_system` | `'postgres-ubereats'` | `'oracle-ubereats'` | `'mongodb-ubereats'` | `STRING` |

- **Ordem por chave.** LSN e SCN da **mudança** crescem para a mesma linha (duas transações não mexem na mesma linha ao
  mesmo tempo), então servem de `SEQUENCE BY`. Duas mudanças da mesma linha **na mesma transação** poderiam repetir o SCN no
  Oracle; lá só o ShadowTraffic escreve, uma linha por comando, então o risco fica registrado e não tratado.
- **Transação.** A compra inteira (ADR 009) chega com o mesmo `source.txId` e o mesmo `ts_ms` em todos os tópicos (visto no
  teste). A Bronze guarda `source.txId` como `cdc_tx_id`, fora do contrato canônico, para quem quiser remontar a compra.
- **`DECIMAL(20,0)`** porque LSN e SCN são inteiros sem sinal de 64 bits.
- **MongoDB.** Os nomes dos metadados do Airbyte (`_ab_cdc_*`) ficam a confirmar na primeira sync da regeração.

Tipos de dado no evento e na Bronze:

| Origem | Exemplo no evento | Bronze |
|---|---|---|
| `numeric(p,s)` / `NUMBER(p,s)` | `"39.90"` | `DECIMAL(p,s)` |
| `bigint`, `integer`, `smallint` (Postgres) | `1` | `BIGINT`, `INT`, `SMALLINT` |
| `NUMBER(18)`, `NUMBER(9)` (Oracle) | `"1"` | `CAST` para `BIGINT`, `INT` (F4.3) |
| `boolean` / `NUMBER(1)` com o conversor | `true` | `BOOLEAN` |
| `timestamp` / `TIMESTAMP` (`*_at` de negócio) | µs da hora do relógio lida como UTC | `TIMESTAMP_NTZ`, convertido com fuso de sessão UTC (F0, decisão 3) |
| `DATE` do Oracle (`date_of_birth`) | ms da meia-noite | `DATE` |
| `date` do BSON (MongoDB) | instante UTC | `TIMESTAMP_NTZ` em `America/Sao_Paulo` (F3, decisão 3) |
| `char(n)`, `varchar(n)` | texto | `STRING` |

### F4.7 Trilhas de nuvem

| Arquivo | Mudança | Quando |
|---|---|---|
| `config/azure/debezium/*` | **Não mudam na F4.** O desenho da Fase 1 mudou ([ADR 012](../../../docs/adr/012-captura-dedicada-ao-kappa-na-fase-1.md)): os templates da Azure são refeitos no planejamento da Fase 1 | Fase 1 |
| `config/gcp/debezium-server/postgres/application.properties` | `schema.include.list=ubereats`, `publication.name=dbz_ubereats`, `publication.autocreate.mode=disabled`, `slot.name=dbz_ubereats_gcp`, `decimal.handling.mode=string`; sai `database.server.name` (removida no 2.0); tópicos Pub/Sub `postgres-gcp.ubereats.<tabela>` | Feito |
| `config/gcp/debezium-server/oracle/application.properties` | As mudanças da F4.3, mais **histórico de schema em arquivo** (`FileSchemaHistory`), que faltava e o conector Oracle exige; sai `database.server.name` | Feito |
| `cdc_source_system` | O `InsertField` do GCP passa a gravar a **fonte** (`postgres-ubereats`, `oracle-ubereats`), como nas outras trilhas; a trilha já está no caminho do dado | Feito |
| `docker-compose.yml` | `kafka-connect` e `kafka-connect-azure` em `quay.io/debezium/connect:3.7`; `debezium-server-*` em `quay.io/debezium/server:3.7`; `max_slot_wal_keep_size` no Postgres; replica set no Mongo (F4.4); `kafka-connect` depende também do `postgres-ubereats` | Regeração |
| Scripts de init (`shared/sql/postgres/`, `shared/mongo/init/`) | Usuário e publicação do CDC (F4.2) | Regeração |
| Fase 1, Event Hubs | **Desenho da [ADR 012](../../../docs/adr/012-captura-dedicada-ao-kappa-na-fase-1.md).** Warehouse e lakehouse recebem pelo Debezium e pelo Airbyte locais, que gravam no storage; o Kappa tem um **conector dedicado**, só com as tabelas do problema de negócio, publicando no Event Hubs. O Standard tem teto de **10 event hubs por namespace** e retenção máxima de 7 dias: tirando os 3 internos do Connect (e o heartbeat, se houver tabela do Postgres), sobram até 6 ou 7 tabelas. O conector do Kappa é registrado só quando a fase do Kappa começar. Se ele capturar tabela do Oracle, o histórico de schema fica em **arquivo local** (`FileSchemaHistory`), não no Event Hubs: o conector o relê a cada restart e o perderia depois de 7 dias | Fase 1 |
| AWS (DMS) | Fora da F4: a Fase 2 não usa Debezium | Fase 2 |

### F4.8 Validação

Contêineres descartáveis em 2026-11-04, numa rede própria (`f4net`), sem volume nomeado e sem porta no host:
`postgres:15` e `gvenzl/oracle-free:23.4-full` com `TZ=America/Sao_Paulo`, `redpandadata/redpanda`, `mongo:7` e
`quay.io/debezium/connect:3.7`. Removidos ao final, com os volumes anônimos; os contêineres e volumes do projeto não foram
tocados. DDL da F1 (6 tabelas) e da F2 (3 tabelas), com os conectores da F4.2 e da F4.3.

| Teste | Resultado |
|---|---|
| Conectores Postgres e Oracle no 3.7.0.Final | `RUNNING`; tópicos e heartbeat criados com 1 partição |
| `numeric(12,2)` / `NUMBER(9,6)` | Texto exato (`"39.90"`, `"-23.550520"`) |
| `boolean` (Postgres) e `NUMBER(1)` com o conversor | `true` / `false` |
| `placed_at = '2026-11-04 12:34:56.789'` nos dois bancos | `1793795696789000` µs: a hora do relógio, lida como UTC (F0.4 confirmada) |
| Default `created_at` | Hora de Brasília (13:05 com UTC 16:05) |
| `source.ts_ms` com o contêiner em Brasília | Instante UTC real nos dois bancos |
| Compra numa transação (pedido, atendimento, item) | Mesmo `txId` e `ts_ms`; LSN crescente dentro da transação |
| `DELETE` no Postgres | `before` só com a chave; tombstone em seguida |
| `DELETE` no Oracle | `before` completo |
| `NUMBER(18)`, `NUMBER(9)` no Oracle | **Texto** (F4.3) |
| `DATE` do Oracle | ms da meia-noite (`1990-05-17`) |
| Mongo com `--replSet rs0` e `rs.initiate` no healthcheck | `PRIMARY`; change stream com `directConnection=true` entregou insert e update |

### Decisões da revisão da F4 (2026-11-04)

| # | Tema | Decisão |
|---|---|---|
| 1 | Versão do Debezium | **3.7** (`quay.io/debezium/connect:3.7` e `quay.io/debezium/server:3.7`), trocada na regeração. Registrada na [ADR 011](../../../docs/adr/011-cdc-debezium-3-7-e-replica-set-no-mongodb.md) com o replica set do MongoDB |
| 2 | Chaves do Oracle como texto | **`CAST` na Bronze** para `BIGINT`/`INT`; sem SMT no conector e sem `precise`. Corrige a F0.2 |
| 3 | Captura do MongoDB | **Replica set `rs0` de 1 nó** (init no healthcheck, `directConnection=true` fora do compose) e **CDC por change stream** no Airbyte, modo *Lookup* ([ADR 011](../../../docs/adr/011-cdc-debezium-3-7-e-replica-set-no-mongodb.md)) |
| 4 | Quando aplicar | **Templates agora** (conectores locais e GCP, nesta branch, sem registrar nada); `docker-compose.yml` e scripts de init na regeração. Os da Azure ficam para a Fase 1 (decisão 5) |
| 5 | Fase 1 (Azure) | **Captura dedicada ao Kappa** ([ADR 012](../../../docs/adr/012-captura-dedicada-ao-kappa-na-fase-1.md)): warehouse e lakehouse pelo Debezium e Airbyte locais até o storage; o Kappa com conector próprio, só as tabelas do problema, dentro do Event Hubs Standard, registrado quando a fase do Kappa começar. Revê a decisão 5 da ADR 006 |

Valem como propostas aceitas o resto da F4: JSON sem schema com envelope completo, `REPLICA IDENTITY` padrão, publicação do
schema com usuário próprio, `max_slot_wal_keep_size=4GB`, 1 partição com 7 dias, contrato `cdc_*` da F4.6 e
`cdc_source_system` pela fonte em todas as trilhas.

**Para a F5:** ordem da regeração com os conectores registrados depois do DDL e antes da carga; scripts de init do CDC no
Postgres e o replica set no compose; conferir os metadados `_ab_cdc_*` na primeira sync do Airbyte.

---

## F5. Plano da regeração

Como regenerar as três fontes com o modelo das F0 a F4: o que muda nos arquivos, em que ordem a regeração roda, quem carrega
cada tabela, como o dinheiro é arredondado e como se prova que o dado saiu certo (T1 a T19). **Nada desta seção foi
aplicado:** a execução é a etapa seguinte do fluxo, e cada operação destrutiva (remoção de volume, de contêiner ou de
conector) pede confirmação na hora, como manda o `CLAUDE.md`.

### F5.0 O que sai e o que entra

| Peça | Hoje | Depois da regeração |
|---|---|---|
| `postgres-ubereats` | `public.users` e `public.drivers` (~69 MB, domínio Pessoas antigo) | Schema `ubereats` com as 28 tabelas da F1, usuário e publicação do CDC (F4.2), `TZ` e `max_slot_wal_keep_size` |
| `oracle-ubereats` | Schema `UBEREATS` com as 7 tabelas antigas do domínio Pedido (~11,8 GB, no teto de 12 GB) | `CITIES`, `CUSTOMERS`, `DRIVERS` (F2), gatilho de logon e `TZ` |
| `mongo-ubereats` | Perfil do seed em JavaScript (500 fixo, cardápio sem `product_id`), nó sozinho | `restaurant_profiles` com validador (F3), replica set `rs0` (F4.4) |
| `redpanda` | Tópicos do modelo antigo e `connect_offsets` com o SCN do Oracle antigo | Vazio; tópicos novos criados pelos conectores (F4.5) |
| `kafka-connect` | Debezium 3.0 com `oracle-ubereats-connector` antigo | Debezium 3.7 com os conectores Postgres e Oracle novos |
| `gen-unified` | Template com Pessoas no Postgres, Pedido no Oracle e 8 geradores do MinIO | Só `customers`, `drivers` (Oracle) e `restaurants` (Postgres) |
| Simulador | Não existe | Pacote Python: seeds, compra e ciclo (ADR 009) |
| Airbyte | Conexão antiga com o Postgres | Fonte MongoDB por change stream (ADR 011) |
| `minio-ubereats` | Bucket com o histórico | **Intocado** (ADR 010); o `gen-unified` deixa de depender dele |

### F5.1 Estratégia: recriar os volumes

**Proposta (recomendada): recriar os volumes dos três bancos e o contêiner do Redpanda, com os scripts de init como fonte
única do schema.**

- **O Oracle precisa liberar os 11,8 GB de qualquer jeito.** O schema novo é o mesmo usuário `UBEREATS` (F2.0 #1) e não
  cabe ao lado das tabelas antigas. Apagar tabela por tabela deixa o volume com o histórico de archivelog e a área de
  recuperação do banco antigo.
- **O init do Postgres e do MongoDB só roda com volume vazio.** Com o volume atual, o DDL teria de ser aplicado por fora, e o
  repositório deixaria de reproduzir o banco do zero.
- **O Redpanda guarda os offsets do conector antigo.** O conector Oracle novo tem o mesmo nome (`oracle-ubereats-connector`)
  e leria do `connect_offsets` um SCN do banco antigo. O Redpanda não tem volume no compose: recriar o contêiner zera
  tópicos, configs e offsets de uma vez.
- **Quem clonar o repositório reproduz o mesmo banco**, que é o objetivo de portfólio.

Alternativa: manter os volumes e aplicar o DDL por script (schema `ubereats` ao lado de `public` no Postgres; no Oracle,
`DROP` das 7 tabelas antigas mais purga do archivelog; no Redpanda, apagar os offsets pela API do Connect). São mais passos
destrutivos, um por um, e o init deixa de ser a fonte.

**Achado do Oracle.** O compose monta `shared/sql/oracle` em `/container-entrypoint-startdb.d`. Na imagem `gvenzl/oracle-free`
essa pasta roda **a cada partida do contêiner** (conferido no `container-entrypoint.sh` da imagem 23.4); só
`/container-entrypoint-initdb.d` roda uma vez, na criação do banco. Hoje o `SHUTDOWN`/`STARTUP` do archivelog e os `CREATE`
rodam em todo start. Na regeração a montagem passa para `initdb.d`.

### F5.2 Arquivos que mudam antes da execução

Tudo nesta tabela é código versionado, feito e testado na branch antes de tocar em contêiner.

| Arquivo | Mudança |
|---|---|
| `docker-compose.yml` | `TZ=America/Sao_Paulo` no Postgres e no Oracle (F0, decisão 3); `-c max_slot_wal_keep_size=4GB` no Postgres (F4.2); Oracle montado em `/container-entrypoint-initdb.d` (F5.1); Mongo com `--replSet rs0 --bind_ip_all --oplogSize 1024` e o healthcheck da F4.4 (corrigida); `kafka-connect` e `kafka-connect-azure` em `quay.io/debezium/connect:3.7`, `debezium-server-*` em `quay.io/debezium/server:3.7` (ADR 011); `kafka-connect` depende do Postgres e do Oracle saudáveis; `gen-unified` sem `minio-setup` no `depends_on` |
| `shared/sql/postgres/` | Saem `create_users_table.sql` e `create_drivers_table.sql` (vão para `shared/sql/legacy/postgres/`). Entram `00_schema.sql` (schema, `search_path` do usuário da aplicação e `set_updated_at`), `01_catalogo.sql`, `02_operacao.sql`, `03_dinheiro.sql`, `04_pos_entrega.sql`, `05_indices_triggers.sql` (F1.1 a F1.5) e `06_cdc.sh` (usuário `dbz_ubereats` com a senha do `.env` e a publicação, F4.2) |
| `shared/sql/oracle/` | Ficam `00_enable_archivelog.sql` e `01_create_user.sh`. `02_create_tables.sh` e `03_create_tables_pedido_pagamento.sh` vão para `shared/sql/legacy/oracle/`; entra um `02_create_tables.sh` novo com o DDL e o gatilho de logon da F2 |
| `shared/mongo/init/` | `01_perfil_restaurante.js(.template)` vai para `shared/mongo/legacy/`; entram `00_replica_set.js` (`rs.initiate` com o membro `localhost:27017` e espera do primário, F4.4 corrigida) e `01_restaurant_profiles.js` (validador e índice da F3.2). O `setup-configs.ps1` deixa de renderizar o seed do Mongo |
| `shared/gen/unified/uber-eats.json.template` | Fica só com `customers` e `drivers` (Oracle) e `restaurants` (Postgres), nas colunas da F1 e da F2; sai a conexão `minio` e os 8 geradores dela (ADR 010). Edição pela skill `shadowtraffic-adicionar-generator-seguro` |
| `shared/gen/reference/cities.csv` | **Novo** (F5.4): código do IBGE, nome, UF e centro (latitude, longitude) de cada cidade |
| `shared/gen/parameters.yaml` | **Novo** (F5.8) |
| `shared/gen/simulator/` | **Novo pacote Python**: `seed` (cidades, catálogo, estoque inicial, perfis), `money` (F5.7), `tracking` (F0.3), `clock` (F5.6), o laço do simulador e os testes (`pytest`, `ruff`) |
| `shared/gen/checks/` | **Novo**: uma consulta por invariante (F5.9), rodadas por `shared/gen/tests/test_invariants.py` |
| `scripts/ingestion/register-postgres-connector.ps1` | **Criado nesta fase** (sem registrar nada), igual ao do Oracle: injeta `POSTGRES_DEBEZIUM_PASSWORD` e `POSTGRES_DB` no template |
| `shared/gen/.env` (fora do git) | Entram `POSTGRES_DEBEZIUM_PASSWORD`, `TRACKING_SALT_ORDER` e `TRACKING_SALT_PAYMENT`; sai `RESTAURANT_COUNT`. O usuário do CDC é fixo no template (`dbz_ubereats`), então `POSTGRES_DEBEZIUM_USER` (F4.0 #8) não é necessário |

O simulador roda **no Windows** (ambiente virtual Python em `shared/gen/.venv`) na v1: conecta em `127.0.0.1` nas portas
publicadas e no Mongo com `directConnection=true` (F4.4). **Depois (F5.2):** `127.0.0.1`, não `localhost`: no Windows
`localhost` resolve primeiro para `::1`, e a conexão com a porta publicada só em IPv4 ficava pendurada (visto no teste
do seed). `SIMULATOR_<FONTE>_HOST`/`_PORT` mudam o destino sem tocar no `.env`. Virar serviço do compose fica para depois, quando o laço estiver estável.

### F5.3 Ordem da regeração

Cada passo tem uma checagem que precisa passar antes do próximo. "**Confirmação**" marca passo destrutivo: o agente mostra
o comando e espera o "ok" do usuário.

| # | Passo | Checagem |
|---|---|---|
| 0 | **Pré-requisitos.** Licença do ShadowTraffic renovada (vence por volta de 2026-11-07; skill `shadowtraffic-renovar-licenca`); F5.2 mesclada com `pytest` e `ruff` verdes; conexão antiga do Airbyte com o Postgres **desativada**; espaço livre na D: | `docker compose config` sem erro; `pytest shared/gen` verde |
| 1 | **Parar** `gen-unified` (já parado), `kafka-connect`, `debezium-server-*` e os três bancos (`docker compose stop`) | `docker ps` sem esses contêineres |
| 2 | **Remover** os contêineres `postgres-ubereats`, `oracle-ubereats`, `mongo-ubereats`, `redpanda` e `kafka-connect`, e os volumes `postgres_data`, `oracle_data` e `mongo_data`. **Confirmação por volume** | `docker volume ls` sem os três; `minio_data` intocado |
| 3 | **Subir os bancos** (`docker compose up -d postgres-ubereats oracle-ubereats mongo-ubereats`); o init cria tudo | Postgres: 28 tabelas em `ubereats`, `SHOW timezone` = `America/Sao_Paulo`, `SHOW max_slot_wal_keep_size` = `4GB`, publicação `dbz_ubereats` existe. Oracle: 3 tabelas, `ARCHIVELOG`, gatilho de logon válido. Mongo: `rs.status()` com `PRIMARY`, coleção com validador |
| 4 | **Subir** `redpanda` e `kafka-connect` (3.7) | `GET :8083/connector-plugins` lista os conectores Postgres e Oracle na versão 3.7 |
| 5 | **Registrar os conectores** (`register-postgres-connector.ps1`, `register-oracle-connector.ps1`), com as tabelas ainda vazias (F4.0 #5) | Os dois `RUNNING`; slot `dbz_ubereats` ativo em `pg_replication_slots` |
| 6 | **Seed de cidades** nos dois bancos, a partir do `cities.csv` (`python -m simulator.seed cities`, em `shared/gen`) | T17 (parte das cidades) passa; eventos `c` em `postgres.ubereats.cities` e `oracle.UBEREATS.CITIES` |
| 7 | **ShadowTraffic, carga inicial** em lote (`maxEvents` da F5.8), pela skill `shadowtraffic-ajustar-geracao` (tabelas vazias: `startingFrom` = 1) | Contagens de `customers`, `drivers` e `restaurants` iguais aos parâmetros |
| 8 | **Seed de catálogo e perfis** (F5.4): produtos, itens de estoque, fichas, estoque inicial e `restaurant_profiles` (`python -m simulator.seed catalog` e `profiles`; o conteúdo vem de `shared/gen/reference/catalog.yaml`) | `python -m simulator.gate` passa (gate da carga: T1 a T19 com as tabelas de operação ainda vazias) |
| 9 | **Airbyte**: fonte MongoDB por change stream, modo *Lookup*, `directConnection=true`, com um destino de conferência (Local JSON). Na primeira sync, conferir os nomes `_ab_cdc_*` (risco da ADR 011) | Metadados conferidos; F4.6 corrigida se os nomes forem outros. O destino de verdade vem com a fase de cada nuvem |
| 10 | **Simulador**: histórico (F5.6) e depois tempo real | Logs sem recusa do banco; eventos nos tópicos `postgres.ubereats.*` |
| 11 | **Gate da regeração**: `python -m simulator.gate` (T1 a T19) com 0 linhas; contagens por status dentro do esperado pelas probabilidades (F5.8); compra no CDC com o mesmo `source.txId` em todos os tópicos | Regeração aprovada; `CLAUDE.md` e `HANDOFF.md` atualizados (o Oracle novo continua tratado como produção, como todos os bancos) |
| 12 | **Operação contínua**: ShadowTraffic em ritmo lento (cadastros novos e `last_login`) e simulador ligados; no fim da sessão, os dois param | Skill de operação do simulador (consequência da ADR 007) |

Não há volta de dado: tudo é sintético. Se um passo de 3 a 8 falhar, corrige-se o código e a regeração recomeça no passo 2
(de novo com confirmação).

### F5.4 Catálogo: quem carrega o quê

**Problema (achado da F3).** Todo produto precisa de ficha técnica com itens de estoque do **mesmo restaurante** (T4), o
produto pronto aponta para um item de estoque dele mesmo (ADR 007, decisão 2) e o nome do item tem de combinar com o
produto. Os `lookup` do ShadowTraffic são independentes entre si e não garantem nada disso. As cidades têm outro problema:
precisam ser **idênticas nos dois bancos** (T17), e duas listas geradas por geradores separados podem divergir.

**Proposta (recomendada).**

| Tabela | Quem carrega | Por quê |
|---|---|---|
| `cities` (Oracle e Postgres) | **Seed** a partir de `shared/gen/reference/cities.csv` | Uma fonte, dois bancos: idênticas por construção. O `setup-configs.ps1` injeta a mesma lista no template, para os cadastros sortearem cidade e coordenada perto do centro |
| `customers`, `drivers` (Oracle) | **ShadowTraffic** | Cadastro plano com dado falso: o forte da ferramenta |
| `restaurants` (Postgres) | **ShadowTraffic** | Idem; carga inicial em lote (o catálogo depende dele) |
| `products`, `stock_items`, `product_recipes` | **Seed de catálogo** (Python) | Por restaurante, coerente com `cuisine_type`: produto pronto com item `ready` de mesmo nome; pré-pronto em porções; insumos em gramas; ficha com 1 a 4 linhas |
| Estoque inicial | **Seed de catálogo** | Um movimento `restock` por item, com `occurred_at` às 00:00 do dia da carga (antes de qualquer janela, que o seed nunca abre antes das 06:00), e `quantity_on_hand` atualizado na mesma transação (T6) |
| `restaurant_profiles` (MongoDB) | **Seed de perfis** (F3, decisão 1) | Lê `restaurants` e `products` depois do catálogo |

Muda a ADR 009 (decisão 2): o ShadowTraffic deixa de carregar `cities`, `products`, `stock_items` e `product_recipes`. Fica
registrado num segundo adendo.

Alternativas: o ShadowTraffic carregar também `products` e `stock_items`, com o seed fazendo só as fichas (nomes de
produto e de item não combinariam, e o produto pronto não acharia "ele mesmo"); ou o seed carregar todo o Postgres,
inclusive `restaurants` (o ShadowTraffic ficaria só com o Oracle).

**Restaurante novo depois da carga.** A v1 carrega restaurantes só no lote inicial. Se o ShadowTraffic voltar a criar
restaurantes, o seed (idempotente) roda de novo, e o simulador ignora restaurante sem perfil ou sem catálogo (RN-23).

### F5.5 Divisão gerador × simulador

Atualiza as tabelas "Quem escreve" da L1b, da L2 e da L3 (a ADR 009 já as tinha deixado desatualizadas).

| Peça | Tabelas | Operações |
|---|---|---|
| ShadowTraffic | Oracle `customers`, `drivers`; Postgres `restaurants` | INSERT com `sequentialInteger`; UPDATE só de `status` e `last_login`. **Nunca** muda `city_id` nem endereço: o T17 compara a cidade do pedido com a cidade atual do cliente |
| Seed (pacote do simulador) | `cities` (dois bancos), `products`, `stock_items`, `product_recipes`, o `restock` inicial, `restaurant_profiles` | INSERT idempotente (`ON CONFLICT DO NOTHING`; `replaceOne` com `upsert` no Mongo) |
| Simulador | As outras 22 tabelas do Postgres; `restock` recorrente e baixa em `stock_movements`; UPDATE de `stock_items.quantity_on_hand` | INSERT com identidade (F0, decisão 8), UPDATE de ciclo; lê `customers` e `drivers` no Oracle e as janelas no Mongo |

`stock_movements` tem dois escritores do mesmo pacote (o seed só no `restock` inicial). Os dois usam a identidade do
banco, então não há colisão de chave, que era o motivo da regra "um dono de INSERT por tabela".

**Um processo, um escritor.** O simulador é um laço único sobre uma fila de ações por instante (próximo pedido, prazo de
aceite, fim de preparo, chegada do motorista, confirmação automática...). Sem concorrência entre escritores no Postgres:
nenhuma corrida de saldo de estoque nem de atribuição, e a ordem da identidade acompanha a ordem de commit (o T6b usa isso).

### F5.6 Relógio: histórico e tempo real

**Problema.** Ligado só em tempo real, o simulador começa sem passado: a Gold e o BI da primeira semana teriam um dia de
dado, e as regras de prazo longo (incidente em até 24 h) só apareceriam no dia seguinte.

**Proposta (recomendada): histórico simulado de N dias e depois tempo real.** O simulador recebe o relógio por injeção
(`clock`). No modo histórico, ele percorre o tempo simulado a partir de `backfill_days` atrás o mais rápido que o banco
aguenta, com as mesmas regras, e grava os `*_at` de negócio no tempo simulado. Quando alcança o relógio de parede, troca
para tempo real e segue sem parar.

| Consequência | Efeito |
|---|---|
| `created_at`/`updated_at` | Default do banco = hora real da escrita (rastro técnico). No histórico diferem dos `*_at` de negócio; a Silver e a Gold usam os de negócio |
| CDC | O histórico chega como rajada de eventos `c`/`u` com `cdc_commit_ts` real; a retenção de 7 dias (F4.5) cobre. A ordem por chave continua valendo |
| Cadastros | O simulador só usa cliente com `signup_date` ≤ instante da compra e motorista com `registration_date` ≤ abertura do turno; o ShadowTraffic gera essas datas espalhadas nos anos anteriores |
| Estoque | O `restock` inicial passa a ser às 00:00 do **primeiro dia do histórico** |
| Testes | Iguais nos dois modos: nenhum T usa `created_at` |

Alternativas: só tempo real (simples, mas sem passado); ou relógio acelerado contínuo (o dado nunca fica "ao vivo", o que
tira o sentido do Kappa).

### F5.7 Dinheiro: arredondamento, última parcela e taxa de entrega

Fecha a F0.7. Tudo em `Decimal`, dentro da transação da compra, na ordem abaixo.

1. **Modo de arredondamento: `ROUND_HALF_UP`** para centavos. É o que o Postgres (`round(numeric, 2)`), o Spark e o SQL do
   Databricks (`round`) fazem com valor positivo: os testes da F5.9 e a Silver recalculam sem divergir nem num centavo.
2. **Ordem dos componentes** (`component_number`): para cada item em (`restaurant_order_id`, `line_number`), o `item` e
   depois o `service_fee`; o `delivery_fee` por último.
3. **Taxa de serviço:** total = `round(itens × service_fee_rate)`; rateada pelos itens na proporção do bruto, cada parcela
   arredondada e **a última absorve a diferença** (RN-33).
4. **Taxa de entrega:** `round(delivery_fee_base + delivery_fee_per_km × distância estimada)`, com a distância da menor rota
   (L4, decisão 2), em linha reta × `route_detour_factor`, calculada na compra. Fica congelada (RN-33): se um atendimento for
   rejeitado depois, o `distance_km` da entrega pode mudar, e o valor cobrado não. **Lacuna do lógico:** a L4 não tinha fórmula
   nem parâmetro para esse valor.
5. **Imposto:** total = `round(total_amount × tax_rate)`; por componente, `round(bruto × tax_rate)` (alíquota sobre o bruto,
   RN-09), e o último (`delivery_fee`, o maior componente fixo) absorve a diferença. Assim a soma do imposto dos componentes é
   o imposto do total, e a absorção nunca deixa o imposto negativo.
6. **Custo do meio, comissão e parte do motorista:** `round(base × taxa)`, uma parcela só.
7. **Reembolso de componente inteiro** (atendimento cancelado, motivos de entrega): devolve o bruto e o imposto exatos do
   componente.
8. **Reembolso parcial** (incidente de `q` de `Q` unidades, com `r` já devolvidas): **diferença de acumulados**,
   `round(G × (r + q) / Q) − round(G × r / Q)`, no bruto `G` e no imposto. A soma das parcelas fecha exatamente o componente
   quando todas as unidades voltam, e o total não depende da ordem dos incidentes (T9).

Exemplo (conferido em `Decimal` e gravado no teste da F5.9): itens de 10,00, 15,00 e 4,99; taxa de serviço 12%; entrega
7,49; imposto 8%.

| # | Componente | Bruto | Imposto | Conta |
|---|---|---|---|---|
| 1 | item, linha 1 | 10,00 | 0,80 | |
| 2 | service_fee, linha 1 | 1,20 | 0,10 | 3,60 × 10,00 / 29,99 = 1,2004 |
| 3 | item, linha 2 | 15,00 | 1,20 | |
| 4 | service_fee, linha 2 | 1,80 | 0,14 | 3,60 × 15,00 / 29,99 = 1,8006 |
| 5 | item, linha 3 | 4,99 | 0,40 | |
| 6 | service_fee, linha 3 | 0,60 | 0,05 | última: 3,60 − 3,00 |
| 7 | delivery_fee | 7,49 | 0,60 | última: 3,29 − 2,69 |
| | **Total** | **41,08** | **3,29** | serviço = round(29,99 × 0,12) = 3,60; imposto = round(41,08 × 0,08) = 3,29 |

Reembolso parcial de 10,00 (Q = 3) em três incidentes de uma unidade: 3,33, 3,34 e 3,33; soma 10,00.

### F5.8 Parâmetros (`shared/gen/parameters.yaml`)

Os da L4 mais os novos desta fase. Valores são **sugestão inicial** (L4, decisão 5): ajustam-se na regeração sem mudar o
código. Percentuais são copiados para a linha quando usados.

```yaml
scale:                         # carga inicial (ShadowTraffic e seeds)
  cities_file: shared/gen/reference/cities.csv   # 5 capitais na v1: SP, RJ, BH, Curitiba, Porto Alegre
  customers: 20000
  drivers: 1500
  restaurants_per_city: 50
  products_per_restaurant: [8, 20]
  recipe_lines: [1, 4]
  restaurants_with_two_windows: 0.6
clock:
  backfill_days: 30            # F5.6; 0 = só tempo real
demand:
  peak_orders_per_hour_per_city: 30
  hourly_factor: {"11": 0.8, "12": 1.0, "13": 0.9, "19": 0.9, "20": 1.0, "21": 0.7}   # demais horas: 0.2
  second_restaurant_share: 0.08          # pedidos com 2 atendimentos (RN-03)
  items_per_restaurant_order: [1, 4]
  quantity_per_item: [1, 3]
behavior:                      # probabilidades por oportunidade
  attempt_declined: 0.08
  max_payment_attempts: 3
  customer_cancels_in_analysis: 0.02
  restaurant_declines: 0.03
  restaurant_ignores: 0.01               # vira analysis_timeout (RN-28)
  restaurant_issue_after_accept: 0.005
  prep_overrun_lognormal_sigma: 0.35     # atraso de preparo; o cliente pode cancelar por restaurant_late
  driver_gives_up: 0.03
  customer_absent: 0.01
  driver_unable: 0.005
  customer_confirms: 0.6                 # o resto confirma sozinho em auto_confirm_delay
  incident: 0.04
  incident_upheld: 0.7
  driver_rating: 0.5
  restaurant_rating: 0.4
  tip: 0.3
  shift_hours: [3, 8]
money:                         # L4, mais a taxa de entrega (F5.7)
  rounding: ROUND_HALF_UP
  tax_rate: "0.0800"
  service_fee_rate: "0.1200"
  payment_fee_rate: {card: "0.0299", pix: "0.0099", wallet: "0.0250"}
  commission_rate: "0.2500"
  driver_share_rate: "0.8000"
  delivery_fee_base: "4.99"
  delivery_fee_per_km: "1.00"
  tip_min: "1.00"
  tip_max: "100.00"
stock:
  restock_target_days: 2       # repõe até cobrir N dias de consumo médio
timing:                        # L4 (valores das regras são fixos)
  incident_window_h: 24
  rating_tip_window_min: 20
  auto_confirm_delay_min: 10
  analysis_timeout_min: 5
  prep_tolerance: 0.5
  max_restaurants_per_order: 2
  max_driver_give_ups: 3
  average_speed_kmh: 25
  promise_slack_min: 10
  route_detour_factor: 1.3
  profile_cache_refresh_min: 15
text:
  rating_comment_by_band: shared/gen/reference/rating_comments.yaml
```

Ordem de grandeza: cerca de 900 pedidos por dia (5 cidades × média de 15 por hora × 12 h de janela), uns 27 mil no
histórico de 30 dias e perto de 700 mil linhas no Postgres. Folgado para a D:, para o slot de 4 GB e para o Oracle (só
cadastros).

### F5.9 Testes T1 a T19

Cada invariante vira uma consulta que **devolve as linhas que o violam**: passa com 0 linhas. As do Postgres ficam em
`shared/gen/checks/tNN_*.sql`; `shared/gen/tests/test_invariants.py` roda uma por uma e falha com a amostra das violadoras
(contagem e chaves, sem dado de pessoa). Os testes que cruzam bancos rodam em Python.

| # | Onde | Complementos em relação à L4 |
|---|---|---|
| T1 a T5 | SQL | T2 confere também a existência da entrega e os estados finais de pedido e entrega; T4 confere que todo produto tem ficha e que a baixa é ficha × quantidade; T5 confere que o motorista não volta a entrega de que desistiu e que não tem duas entregas ou dois turnos ao mesmo tempo |
| T6 | SQL (saldo) e Python (janelas) | Saldo nunca negativo **ao longo do tempo**, não só no fim. Reposição fora das janelas: para cada `restock`, a hora de `occurred_at` não cai em nenhuma janela do perfil (lido no Mongo) |
| T7 | SQL e `pytest` | A consulta confere presença e ausência de `promised_at` e que ele não é anterior ao último aceite. O congelamento é testado na unidade do simulador, contra a fórmula da RN-28 |
| T8 a T11 | SQL | T8 confere também imposto do total, custo do meio, taxa de serviço e um só `delivery_fee` (F5.7); T10, os valores dos repasses; T11, que todo atendimento retirado e toda entrega devida têm repasse |
| T9 (ordem) | `pytest` | "Não depende da ordem dos cancelamentos": teste de propriedade com todas as permutações de cancelamento e de incidentes sobre compras sorteadas |
| T12 a T16 | SQL | Janelas da regra (24 h e 20 min, fixas na L4) |
| T17 | Python | Lê os ids de cliente e motorista no Oracle e confere todo `ext → Oracle.*` do Postgres (`orders`, `checkouts`, `incidents`, avaliações, `shifts`, atribuições, repasses, gorjetas); compara `cities` linha a linha; `orders.city_id` = `customers.city_id` e `shifts.city_id` = `drivers.city_id` (válido porque o ShadowTraffic não muda cidade, F5.5) |
| T18 | Python | Todo `menu_items[].product_id` existe e é do restaurante do `_id`; todo restaurante tem perfil; nenhum produto repetido no mesmo perfil |
| **T19** | Python | **Novo (F3.2):** em cada perfil, `end_time` > `start_time` e janelas sem sobreposição |

<details>
<summary>Consultas T1 a T16 (Postgres, schema <code>ubereats</code>)</summary>

```sql
-- Cada consulta devolve as linhas que VIOLAM o invariante. Passa = 0 linhas.
SET search_path TO ubereats;

-- t01a_atendimentos_por_pedido
SELECT o.order_id, count(ro.restaurant_order_id) AS n
FROM orders o LEFT JOIN restaurant_orders ro ON ro.order_id = o.order_id
GROUP BY o.order_id
HAVING count(ro.restaurant_order_id) NOT BETWEEN 1 AND 2;

-- t01b_restaurante_da_cidade
SELECT ro.restaurant_order_id
FROM restaurant_orders ro
JOIN orders o ON o.order_id = ro.order_id
LEFT JOIN restaurants r ON r.restaurant_id = ro.restaurant_id
WHERE r.restaurant_id IS NULL OR r.city_id <> o.city_id;

-- t02a_derivacao_rn16
WITH a AS (
  SELECT order_id,
         count(*) FILTER (WHERE status NOT IN ('cancelled', 'rejected')) AS ativos,
         count(*) FILTER (WHERE status = 'picked_up')                    AS retirados,
         count(*) FILTER (WHERE status = 'ready_for_pickup')             AS prontos,
         count(*) FILTER (WHERE status = 'in_analysis')                  AS em_analise
  FROM restaurant_orders GROUP BY order_id
), d AS (
  SELECT o.order_id, o.status,
         CASE WHEN a.ativos = 0                THEN 'cancelled'
              WHEN a.retirados = a.ativos      THEN 'out_for_delivery'
              WHEN a.retirados > 0             THEN 'partially_picked_up'
              WHEN a.prontos = a.ativos        THEN 'ready_for_pickup'
              WHEN a.prontos > 0               THEN 'partially_ready'
              WHEN a.em_analise > 0            THEN 'in_analysis'
              ELSE 'preparing' END AS derivado
  FROM orders o JOIN a ON a.order_id = o.order_id
)
SELECT * FROM d
WHERE (status NOT IN ('delivered', 'completed', 'undelivered') AND status <> derivado)
   OR (status IN ('delivered', 'completed', 'undelivered') AND derivado <> 'out_for_delivery');

-- t02b_entrega_do_pedido
SELECT o.order_id, o.status, d.status AS delivery_status
FROM orders o LEFT JOIN deliveries d ON d.order_id = o.order_id
WHERE d.delivery_id IS NULL
   OR (o.status = 'out_for_delivery') <> (d.status = 'in_transit')
   OR (o.status = 'cancelled') <> (d.status = 'cancelled')
   OR (o.status IN ('delivered', 'completed')) <> (d.status = 'delivered')
   OR (o.status = 'undelivered') <> (d.status = 'undelivered');

-- t03a_encadeamento_pedido
SELECT t.order_id, t.sequence_number
FROM order_status_transitions t
LEFT JOIN order_status_transitions p
  ON p.order_id = t.order_id AND p.sequence_number = t.sequence_number - 1
WHERE t.sequence_number > 1
  AND (p.order_id IS NULL OR t.from_status IS DISTINCT FROM p.to_status OR t.occurred_at < p.occurred_at);

-- t03b_encadeamento_atendimento
SELECT t.restaurant_order_id, t.sequence_number
FROM restaurant_order_status_transitions t
LEFT JOIN restaurant_order_status_transitions p
  ON p.restaurant_order_id = t.restaurant_order_id AND p.sequence_number = t.sequence_number - 1
WHERE t.sequence_number > 1
  AND (p.restaurant_order_id IS NULL OR t.from_status IS DISTINCT FROM p.to_status OR t.occurred_at < p.occurred_at);

-- t03c_transicoes_permitidas_atendimento
SELECT t.restaurant_order_id, t.sequence_number, t.from_status, t.to_status
FROM restaurant_order_status_transitions t
WHERE t.from_status IS NOT NULL
  AND (t.from_status, t.to_status) NOT IN (VALUES
    ('in_analysis', 'accepted'), ('in_analysis', 'rejected'), ('in_analysis', 'cancelled'),
    ('accepted', 'preparing'), ('accepted', 'cancelled'), ('preparing', 'cancelled'),
    ('preparing', 'ready_for_pickup'), ('ready_for_pickup', 'picked_up'));

-- t03d_transicoes_permitidas_pedido
SELECT t.order_id, t.sequence_number, t.from_status, t.to_status
FROM order_status_transitions t
WHERE t.from_status IS NOT NULL
  AND NOT (
       (t.from_status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup', 'partially_picked_up')
        AND t.to_status IN ('in_analysis', 'preparing', 'partially_ready', 'ready_for_pickup', 'partially_picked_up',
                            'out_for_delivery', 'cancelled')
        AND t.to_status <> t.from_status)
    OR (t.from_status = 'out_for_delivery' AND t.to_status IN ('delivered', 'undelivered'))
    OR (t.from_status = 'delivered' AND t.to_status = 'completed'));

-- t03e_status_igual_ultima_transicao
SELECT o.order_id, o.status, l.to_status
FROM orders o
LEFT JOIN LATERAL (SELECT t.to_status FROM order_status_transitions t
                   WHERE t.order_id = o.order_id ORDER BY t.sequence_number DESC LIMIT 1) l ON true
WHERE l.to_status IS DISTINCT FROM o.status
UNION ALL
SELECT ro.restaurant_order_id, ro.status, l.to_status
FROM restaurant_orders ro
LEFT JOIN LATERAL (SELECT t.to_status FROM restaurant_order_status_transitions t
                   WHERE t.restaurant_order_id = ro.restaurant_order_id ORDER BY t.sequence_number DESC LIMIT 1) l ON true
WHERE l.to_status IS DISTINCT FROM ro.status;

-- t04a_produto_do_restaurante
SELECT oi.restaurant_order_id, oi.line_number
FROM order_items oi
JOIN restaurant_orders ro ON ro.restaurant_order_id = oi.restaurant_order_id
LEFT JOIN products p ON p.product_id = oi.product_id
WHERE p.product_id IS NULL OR p.restaurant_id <> ro.restaurant_id;

-- t04b_ficha_do_mesmo_restaurante
SELECT pr.product_id, pr.stock_item_id
FROM product_recipes pr
LEFT JOIN products p ON p.product_id = pr.product_id
LEFT JOIN stock_items s ON s.stock_item_id = pr.stock_item_id
WHERE p.product_id IS NULL OR s.stock_item_id IS NULL OR s.restaurant_id <> p.restaurant_id
UNION ALL
SELECT p.product_id, NULL FROM products p                                  -- todo produto tem ficha (RN-37)
WHERE NOT EXISTS (SELECT 1 FROM product_recipes pr WHERE pr.product_id = p.product_id);

-- t04c_baixa_do_mesmo_restaurante
SELECT m.stock_movement_id
FROM stock_movements m
JOIN stock_items s ON s.stock_item_id = m.stock_item_id
JOIN restaurant_orders ro ON ro.restaurant_order_id = m.restaurant_order_id
WHERE s.restaurant_id <> ro.restaurant_id;

-- t04d_baixa_igual_ficha_vezes_quantidade
WITH esperado AS (
  SELECT oi.restaurant_order_id, pr.stock_item_id, sum(pr.quantity * oi.quantity) AS qtd
  FROM order_items oi JOIN product_recipes pr ON pr.product_id = oi.product_id
  WHERE EXISTS (SELECT 1 FROM restaurant_order_status_transitions t
                WHERE t.restaurant_order_id = oi.restaurant_order_id AND t.to_status = 'preparing')
  GROUP BY oi.restaurant_order_id, pr.stock_item_id
), gravado AS (
  SELECT restaurant_order_id, stock_item_id, quantity AS qtd
  FROM stock_movements WHERE movement_type = 'consumption'
)
SELECT coalesce(e.restaurant_order_id, g.restaurant_order_id) AS restaurant_order_id,
       coalesce(e.stock_item_id, g.stock_item_id) AS stock_item_id, e.qtd AS esperado, g.qtd AS gravado
FROM esperado e FULL JOIN gravado g
  ON g.restaurant_order_id = e.restaurant_order_id AND g.stock_item_id = e.stock_item_id
WHERE e.qtd IS DISTINCT FROM g.qtd;

-- t05a_turno_da_atribuicao
SELECT a.delivery_id, a.assignment_number
FROM driver_assignments a
JOIN deliveries d ON d.delivery_id = a.delivery_id
JOIN orders o ON o.order_id = d.order_id
LEFT JOIN shifts s ON s.shift_id = a.shift_id
WHERE s.shift_id IS NULL OR s.driver_id <> a.driver_id OR s.city_id <> o.city_id
   OR a.assigned_at < s.opened_at OR a.assigned_at > coalesce(s.closed_at, 'infinity');

-- t05b_desistencia
SELECT a.delivery_id, a.assignment_number
FROM driver_assignments a
JOIN deliveries d ON d.delivery_id = a.delivery_id
LEFT JOIN LATERAL (SELECT min(ro.picked_up_at) AS primeira_retirada
                   FROM restaurant_orders ro WHERE ro.order_id = d.order_id) f ON true
WHERE a.release_reason = 'driver_gave_up'
  AND (a.assignment_number >= 4 OR a.released_at > f.primeira_retirada);

-- t05c_motorista_nao_volta
SELECT delivery_id, driver_id FROM driver_assignments
GROUP BY delivery_id, driver_id HAVING count(*) > 1;

-- t05d_turnos_e_entregas_sem_sobreposicao
SELECT 'shift' AS tipo, s1.shift_id AS a, s2.shift_id AS b
FROM shifts s1 JOIN shifts s2 ON s2.driver_id = s1.driver_id AND s2.shift_id > s1.shift_id
WHERE tsrange(s1.opened_at, coalesce(s1.closed_at, 'infinity'), '[)')
   && tsrange(s2.opened_at, coalesce(s2.closed_at, 'infinity'), '[)')
UNION ALL
SELECT 'assignment', a1.delivery_id, a2.delivery_id
FROM driver_assignments a1 JOIN driver_assignments a2
  ON a2.driver_id = a1.driver_id AND (a2.delivery_id, a2.assignment_number) > (a1.delivery_id, a1.assignment_number)
WHERE tsrange(a1.assigned_at, coalesce(a1.released_at, 'infinity'), '[)')
   && tsrange(a2.assigned_at, coalesce(a2.released_at, 'infinity'), '[)');

-- t06a_saldo_igual_movimentos
SELECT s.stock_item_id, s.quantity_on_hand, coalesce(m.saldo, 0) AS saldo
FROM stock_items s
LEFT JOIN (SELECT stock_item_id,
                  sum(CASE movement_type WHEN 'restock' THEN quantity ELSE -quantity END) AS saldo
           FROM stock_movements GROUP BY stock_item_id) m ON m.stock_item_id = s.stock_item_id
WHERE s.quantity_on_hand <> coalesce(m.saldo, 0);

-- t06b_saldo_nunca_negativo_no_tempo
SELECT stock_item_id, stock_movement_id, saldo FROM (
  SELECT stock_item_id, stock_movement_id,
         sum(CASE movement_type WHEN 'restock' THEN quantity ELSE -quantity END)
           OVER (PARTITION BY stock_item_id ORDER BY occurred_at, stock_movement_id) AS saldo
  FROM stock_movements) x
WHERE saldo < 0;

-- t07a_prazo_prometido
WITH a AS (
  SELECT order_id,
         count(*) FILTER (WHERE status NOT IN ('cancelled', 'rejected')) AS ativos,
         count(*) FILTER (WHERE status = 'in_analysis')                  AS em_analise,
         max(accepted_at) FILTER (WHERE status NOT IN ('cancelled', 'rejected')) AS ultimo_aceite
  FROM restaurant_orders GROUP BY order_id
)
SELECT d.delivery_id, d.promised_at, a.ativos, a.em_analise
FROM deliveries d JOIN a ON a.order_id = d.order_id
WHERE (a.ativos > 0 AND a.em_analise = 0 AND d.promised_at IS NULL)
   OR (a.em_analise > 0 AND d.promised_at IS NOT NULL)
   OR (d.promised_at < a.ultimo_aceite);

-- t07b_aceite_registrado_no_cancelado
SELECT ro.restaurant_order_id
FROM restaurant_orders ro
WHERE ro.accepted_at IS NULL
  AND EXISTS (SELECT 1 FROM restaurant_order_status_transitions t
              WHERE t.restaurant_order_id = ro.restaurant_order_id AND t.to_status = 'accepted');

-- t08a_pagamento
SELECT p.payment_id
FROM payments p
JOIN orders o ON o.order_id = p.order_id
LEFT JOIN (SELECT payment_id, sum(gross_amount) AS bruto, sum(tax_amount) AS imposto
           FROM payment_components GROUP BY payment_id) c ON c.payment_id = p.payment_id
LEFT JOIN payment_attempts a ON a.checkout_id = p.checkout_id AND a.attempt_number = p.attempt_number
LEFT JOIN checkouts k ON k.checkout_id = p.checkout_id
WHERE c.bruto IS DISTINCT FROM p.total_amount
   OR c.imposto IS DISTINCT FROM round(p.total_amount * p.tax_rate, 2)
   OR p.payment_fee_amount <> round(p.total_amount * p.payment_fee_rate, 2)
   OR p.paid_at <> o.placed_at
   OR o.checkout_id <> p.checkout_id
   OR a.result IS DISTINCT FROM 'approved' OR a.amount <> p.total_amount
   OR k.amount IS DISTINCT FROM p.total_amount;

-- t08b_componentes_por_item
WITH itens AS (
  SELECT ro.order_id, oi.restaurant_order_id, oi.line_number, oi.total_amount
  FROM order_items oi JOIN restaurant_orders ro ON ro.restaurant_order_id = oi.restaurant_order_id
)
SELECT p.payment_id, i.restaurant_order_id, i.line_number
FROM payments p JOIN itens i ON i.order_id = p.order_id
LEFT JOIN payment_components ci ON ci.payment_id = p.payment_id AND ci.component_type = 'item'
  AND ci.restaurant_order_id = i.restaurant_order_id AND ci.line_number = i.line_number
LEFT JOIN payment_components cs ON cs.payment_id = p.payment_id AND cs.component_type = 'service_fee'
  AND cs.restaurant_order_id = i.restaurant_order_id AND cs.line_number = i.line_number
WHERE ci.gross_amount IS DISTINCT FROM i.total_amount OR cs.payment_id IS NULL;

-- t08c_taxas_do_pagamento
SELECT p.payment_id
FROM payments p
LEFT JOIN (SELECT payment_id,
                  sum(gross_amount) FILTER (WHERE component_type = 'item')         AS itens,
                  sum(gross_amount) FILTER (WHERE component_type = 'service_fee')  AS servico,
                  count(*)          FILTER (WHERE component_type = 'delivery_fee') AS entregas
           FROM payment_components GROUP BY payment_id) c ON c.payment_id = p.payment_id
WHERE c.entregas IS DISTINCT FROM 1
   OR c.servico IS DISTINCT FROM round(c.itens * p.service_fee_rate, 2);

-- t09a_reembolsado_por_componente
SELECT r.payment_id, rc.component_number
FROM refund_components rc
JOIN refunds r ON r.refund_id = rc.refund_id
LEFT JOIN payment_components pc ON pc.payment_id = r.payment_id AND pc.component_number = rc.component_number
GROUP BY r.payment_id, rc.component_number, pc.gross_amount, pc.tax_amount
HAVING pc.gross_amount IS NULL OR sum(rc.gross_amount) > pc.gross_amount OR sum(rc.tax_amount) > pc.tax_amount;

-- t09b_soma_dos_reembolsos
SELECT 'refund' AS nivel, r.refund_id AS id
FROM refunds r
LEFT JOIN (SELECT refund_id, sum(gross_amount) AS bruto FROM refund_components GROUP BY refund_id) c
  ON c.refund_id = r.refund_id
WHERE c.bruto IS DISTINCT FROM r.total_amount
UNION ALL
SELECT 'payment', p.payment_id
FROM payments p JOIN refunds r ON r.payment_id = p.payment_id
GROUP BY p.payment_id, p.total_amount HAVING sum(r.total_amount) > p.total_amount;

-- t09c_estorno_total
SELECT p.payment_id, o.status
FROM orders o
JOIN payments p ON p.order_id = o.order_id
JOIN deliveries d ON d.order_id = o.order_id
LEFT JOIN (SELECT payment_id, sum(total_amount) AS devolvido FROM refunds GROUP BY payment_id) r
  ON r.payment_id = p.payment_id
WHERE (o.status = 'cancelled' OR (o.status = 'undelivered' AND d.failure_reason = 'driver_unable'))
  AND r.devolvido IS DISTINCT FROM p.total_amount;

-- t10_copias_e_valores_dos_repasses
SELECT 'restaurant_payout' AS tabela, rp.restaurant_order_id AS id
FROM restaurant_payouts rp
LEFT JOIN restaurant_orders ro ON ro.restaurant_order_id = rp.restaurant_order_id
LEFT JOIN (SELECT restaurant_order_id, sum(total_amount) AS itens FROM order_items GROUP BY restaurant_order_id) i
  ON i.restaurant_order_id = rp.restaurant_order_id
WHERE ro.restaurant_id IS DISTINCT FROM rp.restaurant_id
   OR i.itens IS DISTINCT FROM rp.items_amount
   OR rp.commission_amount <> round(rp.items_amount * rp.commission_rate, 2)
UNION ALL
SELECT 'driver_payout', dp.delivery_id
FROM driver_payouts dp
JOIN deliveries d ON d.delivery_id = dp.delivery_id
JOIN payments p ON p.order_id = d.order_id
LEFT JOIN payment_components pc ON pc.payment_id = p.payment_id AND pc.component_type = 'delivery_fee'
LEFT JOIN driver_assignments a ON a.delivery_id = dp.delivery_id AND a.release_reason = 'delivery_finished'
WHERE a.driver_id IS DISTINCT FROM dp.driver_id OR a.shift_id IS DISTINCT FROM dp.shift_id
   OR pc.gross_amount IS DISTINCT FROM dp.delivery_fee_amount
   OR dp.payout_amount <> round(dp.delivery_fee_amount * dp.driver_share_rate, 2)
UNION ALL
SELECT 'tip', t.delivery_id
FROM tips t
LEFT JOIN driver_assignments a ON a.delivery_id = t.delivery_id AND a.release_reason = 'delivery_finished'
WHERE a.driver_id IS DISTINCT FROM t.driver_id;

-- t11_repasse_so_quando_devido
SELECT 'restaurant_payout_indevido' AS caso, rp.restaurant_order_id AS id
FROM restaurant_payouts rp JOIN restaurant_orders ro ON ro.restaurant_order_id = rp.restaurant_order_id
WHERE ro.status <> 'picked_up'
UNION ALL
SELECT 'restaurant_payout_faltando', ro.restaurant_order_id
FROM restaurant_orders ro
WHERE ro.status = 'picked_up'
  AND NOT EXISTS (SELECT 1 FROM restaurant_payouts rp WHERE rp.restaurant_order_id = ro.restaurant_order_id)
UNION ALL
SELECT CASE WHEN dp.delivery_id IS NULL THEN 'driver_payout_faltando' ELSE 'driver_payout_indevido' END,
       coalesce(dp.delivery_id, d.delivery_id)
FROM deliveries d FULL JOIN driver_payouts dp ON dp.delivery_id = d.delivery_id
WHERE (dp.delivery_id IS NOT NULL)
   <> (d.status = 'delivered' OR (d.status = 'undelivered' AND d.failure_reason = 'customer_absent'))
UNION ALL
SELECT 'tip_indevida', t.delivery_id
FROM tips t JOIN deliveries d ON d.delivery_id = t.delivery_id
WHERE d.status <> 'delivered';

-- t12_janelas_pos_entrega
SELECT 'incident' AS origem, i.incident_id AS id
FROM incidents i JOIN deliveries d ON d.order_id = i.order_id
WHERE d.status <> 'delivered' OR i.opened_at NOT BETWEEN d.finished_at AND d.finished_at + interval '24 hours'
UNION ALL
SELECT 'driver_rating', r.delivery_id
FROM driver_ratings r JOIN deliveries d ON d.delivery_id = r.delivery_id
WHERE d.status <> 'delivered' OR r.rated_at NOT BETWEEN d.finished_at AND d.finished_at + interval '20 minutes'
UNION ALL
SELECT 'restaurant_rating', rr.restaurant_order_id
FROM restaurant_ratings rr
JOIN restaurant_orders ro ON ro.restaurant_order_id = rr.restaurant_order_id
JOIN deliveries d ON d.order_id = ro.order_id
WHERE d.status <> 'delivered' OR rr.rated_at NOT BETWEEN d.finished_at AND d.finished_at + interval '20 minutes'
UNION ALL
SELECT 'tip', t.delivery_id
FROM tips t JOIN deliveries d ON d.delivery_id = t.delivery_id
WHERE d.status <> 'delivered' OR t.paid_at NOT BETWEEN d.finished_at AND d.finished_at + interval '20 minutes';

-- t13a_item_do_incidente
SELECT ii.incident_id, ii.restaurant_order_id, ii.line_number
FROM incident_items ii
JOIN incidents i ON i.incident_id = ii.incident_id
LEFT JOIN restaurant_orders ro ON ro.restaurant_order_id = ii.restaurant_order_id
LEFT JOIN order_items oi ON oi.restaurant_order_id = ii.restaurant_order_id AND oi.line_number = ii.line_number
WHERE oi.restaurant_order_id IS NULL OR ro.order_id <> i.order_id OR ro.status <> 'picked_up';

-- t13b_teto_da_quantidade
SELECT ii.restaurant_order_id, ii.line_number, oi.quantity, sum(ii.quantity) AS reclamado
FROM incident_items ii
JOIN incidents i ON i.incident_id = ii.incident_id
JOIN order_items oi ON oi.restaurant_order_id = ii.restaurant_order_id AND oi.line_number = ii.line_number
WHERE i.status <> 'dismissed'
GROUP BY ii.restaurant_order_id, ii.line_number, oi.quantity
HAVING sum(ii.quantity) > oi.quantity;

-- t14a_reembolso_do_incidente
SELECT i.incident_id, i.status
FROM incidents i LEFT JOIN refunds r ON r.incident_id = i.incident_id
WHERE (i.status = 'upheld') <> (r.refund_id IS NOT NULL)
   OR r.refunded_at <> i.decided_at;

-- t14b_quantidade_reembolsada
SELECT r.refund_id, rc.component_number
FROM refunds r
JOIN refund_components rc ON rc.refund_id = r.refund_id
JOIN payment_components pc ON pc.payment_id = r.payment_id AND pc.component_number = rc.component_number
LEFT JOIN incident_items ii ON ii.incident_id = r.incident_id
  AND ii.restaurant_order_id = pc.restaurant_order_id AND ii.line_number = pc.line_number
WHERE r.origin_type = 'incident' AND pc.component_type = 'item'
  AND rc.quantity IS DISTINCT FROM ii.quantity;

-- t15_atraso_procedente
SELECT i.incident_id
FROM incidents i JOIN deliveries d ON d.order_id = i.order_id
WHERE i.reason = 'late_delivery' AND i.status = 'upheld'
  AND (d.promised_at IS NULL OR d.finished_at <= d.promised_at);

-- t16_gorjeta_e_copias
SELECT 'tip_depois_de_nota_baixa' AS caso, t.delivery_id AS id
FROM tips t JOIN driver_ratings r ON r.delivery_id = t.delivery_id
WHERE r.rating <= 3 AND t.paid_at >= r.rated_at
UNION ALL
SELECT 'driver_rating_copia', r.delivery_id
FROM driver_ratings r
JOIN deliveries d ON d.delivery_id = r.delivery_id
JOIN orders o ON o.order_id = d.order_id
LEFT JOIN driver_assignments a ON a.delivery_id = r.delivery_id AND a.release_reason = 'delivery_finished'
WHERE a.driver_id IS DISTINCT FROM r.driver_id OR o.customer_id <> r.customer_id
UNION ALL
SELECT 'restaurant_rating_copia', rr.restaurant_order_id
FROM restaurant_ratings rr
JOIN restaurant_orders ro ON ro.restaurant_order_id = rr.restaurant_order_id
JOIN orders o ON o.order_id = ro.order_id
WHERE ro.restaurant_id <> rr.restaurant_id OR o.customer_id <> rr.customer_id
UNION ALL
SELECT 'incident_copia', i.incident_id
FROM incidents i JOIN orders o ON o.order_id = i.order_id
WHERE o.customer_id <> i.customer_id;
```

</details>

**Validação** (2026-11-04). Contêiner descartável `postgres:15` com `TZ=America/Sao_Paulo`, sem volume nomeado e sem porta
no host, removido ao final com `docker rm -v`; DDL da F1 extraído deste documento (28 tabelas e os 11 triggers).

| Teste | Resultado |
|---|---|
| As 36 consultas no banco vazio | Sem erro; 0 linhas |
| Uma compra válida da ADR 009 (2 tentativas, a 1ª recusada; 3 itens; componentes do exemplo da F5.7) mais catálogo, fichas e `restock` inicial | 0 linhas em todas |
| Violações plantadas: restaurante de outra cidade, componente com bruto errado, lacuna na sequência de transições, reembolso acima do bruto do componente, saldo diferente dos movimentos | Falharam exatamente T1b, T8a, T3a e T3e, T9a e T6a; nenhuma outra |
| Exemplo da F5.7 em `Decimal` com `ROUND_HALF_UP` | Fecha em 41,08 e 3,29; reembolso parcial 3,33 + 3,34 + 3,33 |
| **Depois (F5.2):** as consultas viraram `shared/gen/checks/*.sql`, rodadas pelo `test_invariants_no_postgres` (só leitura, com `UBEREATS_CHECKS_DSN`) contra um Postgres criado pelo init novo (`shared/sql/postgres/`) | Compra válida: passa. Com as mesmas violações: falha listando exatamente T1b, T3a, T3e, T6a, T8a e T9a. T6c, T17, T18 e T19 têm testes de unidade em Python |

O ciclo completo (aceite, preparo, atribuição, entrega e pós-entrega) só ganha dado positivo quando o simulador existir: a
validação de T5 e T10 a T16 contra dado real fica para os testes do simulador e para o gate da regeração (passo 11).

### F5.10 Riscos

| Risco | Mitigação |
|---|---|
| Archivelog do Oracle acumula. O teste do init (F5.2) mostrou que ele vai para `$ORACLE_HOME/dbs/arch`, **na camada do contêiner, fora do volume `oracle_data`**: cresce no VHDX e some quando o contêiner é recriado | O Oracle só recebe cadastros (pouca mudança). Conferir o tamanho de `dbs/arch` no gate (passo 11); se crescer, apagar archivelog já lido pelo Debezium com RMAN (operação com confirmação). Recriar o contêiner com o conector parado no meio de um archivelog obriga a novo snapshot |
| Rajada do histórico pesa no HDD da D: | Uma transação por compra; o ritmo do histórico é limitado pelo banco, não pelo relógio |
| Slot do Postgres retém WAL com o conector parado | `max_slot_wal_keep_size=4GB` (F4.2); acima disso o slot é invalidado e o conector refaz o snapshot |
| Licença do ShadowTraffic vence antes da execução | Passo 0; a carga em lote leva minutos, e o contínuo é opcional |
| Simulador parado = nenhum pedido novo (ADR 009) | Skill de operação, parada limpa e retomada pelo estado do banco (o relógio retoma do último evento gravado) |

### Decisões da revisão da F5 (2026-11-04)

| # | Tema | Decisão |
|---|---|---|
| 1 | Estratégia dos contêineres | **Recriar os volumes** `postgres_data`, `oracle_data` e `mongo_data` e os contêineres dos três bancos, do Redpanda e do `kafka-connect`, com confirmação por volume na execução. Os scripts de init são a fonte única do schema; o Oracle passa a montar os scripts em `/container-entrypoint-initdb.d`. `minio_data` intocado |
| 2 | Catálogo e cidades | **ShadowTraffic** com `customers`, `drivers` e `restaurants`; **seed em Python** com `cities` (dois bancos, de `shared/gen/reference/cities.csv`), `products`, `stock_items`, `product_recipes`, o `restock` inicial e os perfis do MongoDB. Segundo adendo da [ADR 009](../../../docs/adr/009-simulador-cria-a-compra-numa-transacao.md) |
| 3 | Relógio do simulador | **Histórico simulado de 30 dias** (`backfill_days`) e depois tempo real, com relógio injetado; `*_at` de negócio no tempo simulado e `created_at`/`updated_at` com a hora real. No mesmo adendo da ADR 009 |
| 4 | Dinheiro | **`ROUND_HALF_UP`**; ordem dos componentes item → `service_fee` por linha e `delivery_fee` por último; a última parcela absorve a diferença; reembolso parcial por diferença de acumulados. **Taxa de entrega** = `delivery_fee_base` + `delivery_fee_per_km` × distância da menor rota (linha reta × `route_detour_factor`), congelada na compra; completa os parâmetros da L4 |

Valem como propostas aceitas o resto da F5: a ordem da F5.3 (conectores registrados antes de qualquer carga, gate depois
da carga e gate final com T1 a T19), as mudanças de arquivo da F5.2, a divisão da F5.5 (um processo e um escritor no
simulador; o ShadowTraffic nunca muda cidade nem endereço), os parâmetros iniciais da F5.8, as consultas da F5.9 e o T19
novo. O `register-postgres-connector.ps1` foi criado nesta fase, sem registrar nada.

**Para a execução da regeração:** implementar a F5.2 numa branch própria (simulador, seeds, checks, init, compose,
template), com `pytest` e `ruff` verdes, e só então rodar a F5.3 a partir do passo 0. A licença do ShadowTraffic vence por
volta de 2026-11-07.
