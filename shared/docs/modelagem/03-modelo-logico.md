# Modelo lógico

Terceira etapa do fluxo (regras → adversarial → conceitual → **lógico** → físico → regeração). Parte do
[modelo conceitual](02-modelo-conceitual.md) e das [regras de negócio](01-regras-de-negocio.md). Revisão por fases.

| Fase | Conteúdo | Status |
|---|---|---|
| L0 | Convenções transversais | aprovada |
| L1a | Pessoas, cidade e catálogo (parte do diagrama 2.1) | aprovada |
| L1b | Operação: pedido, atendimento, entrega, turno, atribuição, transições (parte do diagrama 2.1) | aprovada |
| L2 | Dinheiro (diagrama 2.2) | aprovada |
| L3 | Pós-entrega (diagrama 2.3) | aprovada |
| L4 | Visão integrada: restrições entre tabelas, parâmetros, ADR do histórico de status | aprovada |

---

## L0. Convenções transversais

Decididas com o usuário em 2026-11-01.

| # | Tema | Convenção |
|---|---|---|
| 1 | Nomes | Inglês em `snake_case` (tabelas e colunas), como as tabelas atuais (`orders`, `users`, `drivers`). O glossário em português fica no `CONTEXT.md`. |
| 2 | Chaves | **Toda chave de identificação é inteira sequencial** (`BIGINT` no Postgres, `NUMBER(19)` no Oracle). **Sem UUID** em nenhuma tabela. O gerador já usa `sequentialInteger` (confirmado em `users`; as demais tabelas são conferidas na L1). Entidade fraca usa chave composta com a chave do pai. |
| 2a | Código de rastreio | Única exceção ao inteiro: `pedido` e `pagamento` têm uma coluna extra com um **hash** para rastreio (código externo/visível ao cliente). É atributo, **não é chave**; as relações continuam pelo inteiro. Formato e tamanho do hash ficam para a L1/L2. |
| 3 | Dinheiro | **Decimal com 2 casas** (`NUMERIC(12,2)` no Postgres, `NUMBER(12,2)` no Oracle). Nunca ponto flutuante. A regra "a última parcela absorve a diferença" (RN-33) é feita em decimal. |
| 4 | Tempo | **Horário de Brasília** (`America/Sao_Paulo`), sem UTC. Coluna `TIMESTAMP` sem fuso, gravando a hora local; a sessão do banco e o gerador usam `America/Sao_Paulo`. Não há horário de verão desde 2019, então não há hora ambígua. |
| 5 | Janelas de tempo | 24 h (incidente), 20 min (avaliação), 10 min (confirmação automática) e demais limites de RN-28 são **parâmetros**, não colunas. |
| 6 | Status | Todo status é **coluna**, inclusive o do pedido. O banco transacional **não tem view**; view é só para análise de negócio (Gold). |
| 7 | Status do pedido | A RN-16 deriva o status do pedido a partir dos atendimentos. A coluna guarda esse valor e é atualizada **na mesma transação** que muda o atendimento. A regra da RN-16 vira uma **consulta de verificação nos testes**, não uma view. |
| 8 | Histórico de status | `order_status_transitions` e `restaurant_order_status_transitions` são **tabelas** (RN-18), como no conceitual. |
| 9 | Integridade | Sem chave estrangeira física (invariante do projeto). A integridade é lógica, garantida pelo gerador (`lookup`). |
| 10 | Referência entre bancos | Coluna com o identificador, sem chave estrangeira, **marcada no modelo** como `ext → Oracle.<tabela>` ou `ext → Postgres.<tabela>` para rastreio. Cada entidade mora em um único banco (ADR 006). |
| 11 | Cidade | Única entidade **duplicada**: tabela de referência `cities` nos dois bancos, com o **código do IBGE** como chave natural, para o mesmo valor valer dos dois lados. |

### Consequências para a etapa física e o CDC

- **Decimal no Debezium:** o conector entrega `NUMERIC`/`NUMBER` como bytes codificados por padrão. A etapa física deve fixar
  `decimal.handling.mode` (`string` ou `double`) e o contrato da Bronze deve declarar o tipo recebido.
- **Timestamp sem fuso no Debezium:** o conector interpreta `TIMESTAMP` sem fuso como se fosse UTC, o que deslocaria os instantes em
  3 horas. A etapa física deve tratar isso (conversor/transform no conector ou conversão declarada na Bronze) e o contrato
  da Bronze deve dizer que o horário é o de Brasília.
- **Status do pedido redundante:** a coluna e a derivação da RN-16 podem divergir se um fluxo esquecer a atualização; a verificação
  nos testes e no gerador é o que protege.

### Referências entre bancos já conhecidas (confirmar na L1/L2)

| Origem (banco) | Referência | Destino |
|---|---|---|
| Pedido (Postgres) | cliente | `ext → Oracle.customers` |
| Atribuição de motorista, repasse ao motorista, gorjeta, avaliação do motorista (Postgres) | motorista | `ext → Oracle.drivers` |
| Incidente, avaliação do restaurante (Postgres) | cliente | `ext → Oracle.customers` |
| Cliente, motorista (Oracle) | cidade | `cities` local (cópia) |
| Restaurante (Postgres) | cidade | `cities` local (cópia) |

### Decisão: o Turno mora no Postgres

O Turno é entidade fraca de Motorista no conceitual, mas fica no **Postgres**, ao lado da atribuição, da entrega e dos repasses:

- A RN-36 (só motorista com turno aberto recebe atribuição) vira checagem dentro de um único banco e uma única transação.
- Pedidos e ganho do turno são derivados de entregas e repasses, que já estão no Postgres.
- O Oracle fica com o cadastro estável de pessoas (`customers`, `drivers`) e `cities`. A ADR 006 só lista `users` e `drivers` no domínio Pessoas, então não há conflito.
- O turno guarda `driver_id` como `ext → Oracle.drivers`.
- Exceção à convenção 2: como o pai está em outro banco, o Turno tem **chave inteira sequencial própria** (`shift_id`), e a atribuição aponta para ela.

---

## L1a. Pessoas, cidade e catálogo

Banco de cada tabela: **Oracle** (Pessoas) · **Postgres** (pedido e catálogo) · **MongoDB** (perfil do restaurante).
Tipos em notação Postgres; no Oracle, `varchar` → `VARCHAR2`, `numeric` → `NUMBER`, `bigint` → `NUMBER(19)`.
Colunas de rastro (`created_at`, `updated_at`) em todas as tabelas, em horário de Brasília.

### cities (Oracle e Postgres, cópia idêntica)

| Coluna | Tipo | Observação |
|---|---|---|
| city_id | integer, PK | **Código do IBGE** (chave natural, igual nos dois bancos) |
| name | varchar | |
| state_code | char(2) | UF |

### customers (Oracle) — Cliente

| Coluna | Tipo | Observação |
|---|---|---|
| customer_id | bigint, PK | sequencial (hoje `user_id`) |
| first_name, last_name | varchar | o nome completo é derivado |
| email | varchar, único | |
| email_verified | boolean | |
| phone_number | varchar | |
| phone_verified | boolean | |
| address_line1, address_line2, postal_code | varchar | |
| latitude, longitude | numeric(9,6) | coordenada do endereço; destino da rota e base do prazo prometido (RN-28). Reaberto na L1b |
| city_id | integer | → `cities` (RN-35); estado e país saem (derivados da cidade; só Brasil) |
| date_of_birth | date | |
| gender | varchar | |
| status | varchar | `active`, `suspended`, `inactive` |
| signup_date, last_login | timestamp | |
| created_at, updated_at | timestamp | |

### drivers (Oracle) — Motorista

| Coluna | Tipo | Observação |
|---|---|---|
| driver_id | bigint, PK | sequencial |
| first_name, last_name | varchar | |
| email, phone_number | varchar | |
| vehicle_type, vehicle_make, vehicle_model | varchar | |
| vehicle_year | integer | |
| license_plate | varchar | |
| license_number | varchar | CNH |
| city_id | integer | → `cities` (RN-35: só aceita entrega na própria cidade) |
| status | varchar | `active`, `suspended`, `inactive` |
| registration_date, last_login | timestamp | |
| created_at, updated_at | timestamp | |

### restaurants (Postgres) — Restaurante

| Coluna | Tipo | Observação |
|---|---|---|
| restaurant_id | bigint, PK | sequencial |
| name | varchar | |
| cnpj | char(14), único | só dígitos |
| phone_number | varchar | |
| address, postal_code | varchar | |
| latitude, longitude | numeric(9,6) | ponto de retirada; origem da rota (RN-28). Reaberto na L1b |
| city_id | integer | → `cities` (RN-03, RN-35) |
| cuisine_type | varchar | |
| status | varchar | `active`, `suspended`, `inactive`; "aberto" é derivado das janelas (RN-41) |
| created_at, updated_at | timestamp | |

Horário de abertura e fechamento saem daqui: pertencem ao **Perfil de Restaurante** (RN-23), no MongoDB.

### products (Postgres) — Produto

| Coluna | Tipo | Observação |
|---|---|---|
| product_id | bigint, PK | sequencial |
| restaurant_id | bigint | → `restaurants` (um produto, um restaurante) |
| name | varchar | |
| product_type | varchar | |
| price | numeric(12,2) | preço atual; o item de pedido guarda cópia (RN-32) |
| unit_cost | numeric(12,2) | base do custo unitário na Gold |
| calories | integer | |
| prep_time_min | integer | |
| is_vegetarian, is_gluten_free | boolean | |
| is_active | boolean | desativar não afeta pedidos já aprovados (RN-32) |
| created_at, updated_at | timestamp | |

### stock_items (Postgres) — Item de Estoque

O que o restaurante estoca: produto pronto, pré-pronto ou insumo (RN-37, ADR 007).

| Coluna | Tipo | Observação |
|---|---|---|
| stock_item_id | bigint, PK | sequencial |
| restaurant_id | bigint | → `restaurants` |
| name | varchar | ex.: "arroz branco", "feijão cozido", "refrigerante lata" |
| kind | varchar | `ready` (pronto), `prepared` (pré-pronto), `ingredient` (insumo) |
| unit | varchar | `unit`, `gram`, `portion` |
| quantity_on_hand | numeric(12,3) | saldo; mantido pelo simulador **na mesma transação** do movimento; nunca negativo (RN-39) |
| created_at, updated_at | timestamp | |

Único: (`restaurant_id`, `name`).

### product_recipes (Postgres) — Ficha Técnica

| Coluna | Tipo | Observação |
|---|---|---|
| product_id | bigint, PK | → `products` |
| stock_item_id | bigint, PK | → `stock_items`; do **mesmo restaurante** do produto |
| quantity | numeric(12,3) | consumo por unidade vendida, na unidade do item |

Todo produto tem ao menos uma linha. Produto pronto: uma linha, quantidade 1, apontando para o item de estoque dele.

### stock_movements (Postgres) — Movimento de Estoque

| Coluna | Tipo | Observação |
|---|---|---|
| stock_movement_id | bigint, PK | sequencial |
| stock_item_id | bigint | → `stock_items` |
| movement_type | varchar | `consumption` (baixa no preparo, RN-38) ou `restock` (reposição, RN-40) |
| quantity | numeric(12,3) | sempre positiva; o tipo diz o sinal |
| restaurant_order_id | bigint, nulo | → `restaurant_orders` (L1b); obrigatório em `consumption`, nulo em `restock` |
| occurred_at | timestamp | reposição só fora das janelas (RN-40) |
| created_at | timestamp | |

Único: (`restaurant_order_id`, `stock_item_id`) quando `consumption` — no máximo uma baixa por atendimento e item (RN-38).

**Saldo disponível no aceite (RN-39):** `quantity_on_hand` menos o comprometido pelos atendimentos já aceitos e ainda não em
preparo (ficha × quantidade dos itens deles). O simulador calcula numa consulta, com o item de estoque travado, sem view.

### restaurant_profiles (MongoDB) — Perfil de Restaurante e Item de Cardápio

Um documento por restaurante (obrigatório, RN-23), com o cardápio aninhado.

| Campo | Tipo | Observação |
|---|---|---|
| restaurant_id | integer | `ext → Postgres.restaurants`, único |
| service_windows[] | lista | Janela de Funcionamento, 1 ou 2 (RN-41), iguais todos os dias |
| service_windows[].start_time, end_time | string "HH:MM" | horário de Brasília; sem sobreposição |
| menu_items[] | lista | Item de Cardápio, entidade fraca do perfil |
| menu_items[].product_id | integer | `ext → Postgres.products`; um produto aparece no máximo uma vez |
| menu_items[].section | string | |
| menu_items[].display_order | integer | |
| menu_items[].highlighted | boolean | |
| menu_items[].customizations | lista | |

Nome e preço **não** ficam no cardápio: vêm do produto.

### Referências externas desta fase

| De | Coluna | Para |
|---|---|---|
| `restaurant_profiles` (Mongo) | `restaurant_id` | `ext → Postgres.restaurants` |
| `restaurant_profiles.menu_items` (Mongo) | `product_id` | `ext → Postgres.products` |

O simulador (Postgres) lê as janelas do perfil (MongoDB) para agendar a reposição: é a única leitura entre bancos que a
operação faz. Fica para o físico decidir se ele lê do MongoDB ou de uma cópia de configuração.

### Decisões da revisão da L1a (2026-11-02)

| # | Tema | Decisão |
|---|---|---|
| 1 | Colunas agregadas e sem regra | **Saem** todas as listadas (agregados vão para a Gold) |
| 2 | `uuid` de `restaurants` | **Sai** (só inteiro sequencial) |
| 3 | `status` | Cliente e motorista: `active`/`suspended`/`inactive` |
| 4 | Estoque | **Revisado** (ADR 007): itens de estoque, ficha técnica e movimentos |
| 5 | `cuisine_type` | Só no restaurante |
| 6 | Status do restaurante | `active`/`suspended`/`inactive`; aberto ou fechado vem das janelas de funcionamento |
| 7 | Saldo do item de estoque | **Coluna** `quantity_on_hand`, atualizada pelo simulador na mesma transação do movimento |

---

## L1b. Operação: pedido, atendimento, entrega, turno e atribuição

Todas as tabelas no **Postgres** (ADR 006). Mesmas convenções da L1a: tipos em notação Postgres, `created_at`/`updated_at`
em horário de Brasília, sem FK física. Checkout e tentativa de pagamento aparecem no diagrama 2.1, mas ficam na **L2**
(dinheiro); aqui o pedido só aponta para o checkout (decisão 2).

### Vocabulário: atores, status e motivos

**Atores** (RN-01), usados em toda coluna de "quem": `customer`, `restaurant`, `driver`, `platform`. A rejeição automática
por prazo (RN-28) e a confirmação automática (RN-24) são da `platform`.

**Status do atendimento** (tabela de transições das regras):

| Valor | Regra | Terminal |
|---|---|---|
| `in_analysis` | em análise; **status inicial** | |
| `accepted` | aceito | |
| `preparing` | em preparo (dispara a baixa de estoque, RN-38) | |
| `ready_for_pickup` | pronto para retirada | |
| `picked_up` | retirado | sim (não muda mais; incidente não altera, RN-14) |
| `cancelled` | cancelado | sim |
| `rejected` | rejeitado | sim |

**Status do pedido:**

| Valor | Regra | Origem |
|---|---|---|
| `in_analysis` | em análise; **status inicial** | derivação RN-16 |
| `preparing` | em preparo | derivação RN-16 |
| `partially_ready` | parcialmente pronto | derivação RN-16 |
| `ready_for_pickup` | pronto para retirada | derivação RN-16 |
| `partially_picked_up` | em coleta | derivação RN-16 |
| `out_for_delivery` | a caminho | derivação RN-16 |
| `delivered` | entregue | evento do pedido (RN-24) |
| `completed` | concluído (terminal) | evento do pedido (RN-24) |
| `undelivered` | não entregue (terminal) | evento do pedido (RN-30) |
| `cancelled` | cancelado (terminal) | derivação RN-16 (nenhum atendimento ativo) |

**Status da entrega:**

| Valor | Significado |
|---|---|
| `awaiting_assignment` | sem motorista. **Status inicial** (a entrega nasce com o pedido, conceitual 3.2); a busca por motorista só começa quando o primeiro atendimento fica pronto (RN-06). Volta para cá quando o motorista desiste (RN-07) |
| `assigned` | com motorista, recolhendo ou aguardando nos restaurantes (RN-17) |
| `in_transit` | todos os atendimentos ativos recolhidos; o pedido fica `out_for_delivery` na mesma transação |
| `delivered` | o motorista finalizou (RN-24) |
| `undelivered` | não entregue (RN-30) |
| `cancelled` | todos os atendimentos cancelados ou rejeitados |

**Motivo de fim do atendimento** (`end_reason`). Cada motivo já diz o status e quem agiu:

| Motivo | Status | Quem | Regra |
|---|---|---|---|
| `restaurant_declined` | `rejected` | restaurant | o restaurante recusa na análise (tabela de transições) |
| `out_of_stock` | `rejected` | restaurant | RN-39 (falta saldo no aceite) |
| `analysis_timeout` | `rejected` | platform | RN-28 (5 minutos sem resposta) |
| `customer_request` | `cancelled` | customer | RN-12 (cliente cancela até "em análise") |
| `restaurant_late` | `cancelled` | customer | RN-12 e RN-28 (aceito ou em preparo, passou do estimado + 50%) |
| `other_restaurant_dropped` | `cancelled` | customer | RN-34 (o outro restaurante cancelou ou rejeitou; vale até ficar pronto) |
| `restaurant_issue` | `cancelled` | restaurant | RN-13 (restaurante cancela depois do aceite, até o fim do preparo) |

**Motivo de não entrega** (`deliveries.failure_reason`, RN-30): `customer_absent` (registrado pelo motorista, sem devolução,
RN-25) e `driver_unable` (registrado pela plataforma, estorno total).

**Motivo de liberação da atribuição** (`driver_assignments.release_reason`, RN-31): `driver_gave_up` (desistência, RN-07),
`delivery_cancelled` (todos os atendimentos cancelados; motorista liberado, RN-28) e `delivery_finished` (entrega terminou
em `delivered` ou `undelivered`; fecha a atribuição final).

### orders (Postgres) — Pedido

| Coluna | Tipo | Observação |
|---|---|---|
| order_id | bigint, PK | sequencial |
| tracking_code | char(12), único | código de rastreio visível ao cliente (hash, ver abaixo); atributo, não chave |
| checkout_id | bigint, único | → `checkouts` (L2); um checkout gera no máximo um pedido (RN-15) |
| customer_id | bigint | `ext → Oracle.customers` (RN-02) |
| city_id | integer | → `cities`; cidade dos restaurantes e do endereço de entrega, **copiada na compra** (RN-03, RN-35; decisão 9) |
| status | varchar | nasce `in_analysis`; atualizado na mesma transação que muda o atendimento ou a entrega (L0 #7) |
| placed_at | timestamp | momento da compra (aprovação do pagamento, RN-11) |
| created_at, updated_at | timestamp | |

Valores (itens, taxas, total) ficam no pagamento (L2). O motivo de não entrega fica na entrega e na transição do pedido.

**Código de rastreio (decisão 12).** 12 caracteres em base32 Crockford maiúsculo (sem `I`, `L`, `O`, `U`, fácil de ditar),
tirados do SHA-256 de `order_id` com um sal fixo. É determinístico (a regeração produz o mesmo código), não deixa adivinhar
o pedido vizinho e tem 60 bits (colisão desprezível na escala do projeto). Onde calcular fica para o físico, com uma
restrição: **não** como coluna gerada do Postgres, porque o Postgres 15 do projeto não publica coluna gerada na replicação
lógica (só a partir do 18) e o Debezium não a veria.

### restaurant_orders (Postgres) — Atendimento

| Coluna | Tipo | Observação |
|---|---|---|
| restaurant_order_id | bigint, PK | sequencial; já referenciado por `stock_movements.restaurant_order_id` (L1a) |
| order_id | bigint | → `orders` |
| restaurant_id | bigint | → `restaurants`; da cidade do pedido (RN-03) |
| status | varchar | nasce `in_analysis` |
| estimated_prep_min | integer, nulo | tempo estimado até ficar pronto; **fixado no aceite e imutável** (RN-28) |
| accepted_at | timestamp, nulo | começa o relógio de preparo; o atraso começa em `accepted_at` + estimado × 1,5 (RN-12, RN-28) |
| driver_arrived_at | timestamp, nulo | chegada do motorista ao restaurante (RN-17); numa reatribuição antes da retirada, vale a chegada do novo motorista |
| picked_up_at | timestamp, nulo | retirada; espera do motorista = `picked_up_at` − `driver_arrived_at` (RN-17); a primeira retirada trava o motorista (RN-07) |
| end_reason | varchar, nulo | só em `cancelled` e `rejected` (tabela de motivos acima) |
| created_at, updated_at | timestamp | `created_at` é o envio ao restaurante: começa o prazo de análise de 5 minutos (RN-28) |

Único: (`order_id`, `restaurant_id`), um atendimento por restaurante e pedido (RN-05). O máximo de 2 por pedido (RN-03) é
checado pelo gerador e nos testes.

Os demais instantes de mudança de status (preparo, pronto, cancelamento) ficam só nas transições (decisão 4).

### order_items (Postgres) — Item de Pedido

Entidade fraca do atendimento: chave composta com a do pai (L0 #2).

| Coluna | Tipo | Observação |
|---|---|---|
| restaurant_order_id | bigint, PK | → `restaurant_orders` |
| line_number | smallint, PK | 1, 2, ... dentro do atendimento (decisão 6) |
| product_id | bigint | → `products`, do restaurante do atendimento |
| product_name | varchar | cópia na compra (RN-32) |
| unit_price | numeric(12,2) | preço unitário da compra (RN-32) |
| quantity | integer | ≥ 1 |
| total_amount | numeric(12,2) | `unit_price` × `quantity`, o total contratado (RN-32) |
| created_at | timestamp | imutável depois de criado; sem `updated_at` |

O restaurante vendedor (RN-32) e o pedido vêm do atendimento: o restaurante de um atendimento nunca muda, então não precisa
de cópia. O `discount_applied` do gerador atual sai (sem regra).

### order_status_transitions (Postgres) — Transição de Status de Pedido

| Coluna | Tipo | Observação |
|---|---|---|
| order_id | bigint, PK | → `orders` |
| sequence_number | smallint, PK | 1 na criação, +1 a cada mudança |
| from_status | varchar, nulo | nulo na criação |
| to_status | varchar | |
| actor | varchar | quem causou; numa mudança derivada (RN-16), o ator do evento do atendimento que a provocou |
| reason | varchar, nulo | em `undelivered`, o motivo da RN-30. Em `completed` fica nulo: a causa é o ator (`customer` confirmou, `platform` confirmou automaticamente, RN-24 e RN-28) |
| occurred_at | timestamp | |
| created_at | timestamp | |

Só grava quando o status do pedido muda de fato: um atendimento que passa de aceito para em preparo com o pedido já
`preparing` não gera linha aqui (gera na tabela do atendimento).

### restaurant_order_status_transitions (Postgres) — Transição de Status de Atendimento

| Coluna | Tipo | Observação |
|---|---|---|
| restaurant_order_id | bigint, PK | → `restaurant_orders` |
| sequence_number | smallint, PK | 1 na criação, +1 a cada mudança |
| from_status | varchar, nulo | nulo na criação |
| to_status | varchar | só transições permitidas pela tabela das regras |
| actor | varchar | |
| reason | varchar, nulo | igual ao `end_reason` quando `to_status` é `cancelled` ou `rejected` |
| occurred_at | timestamp | |
| created_at | timestamp | |

Nas duas tabelas de transição, a criação é a **linha 1** (`from_status` nulo → `in_analysis`), gravada junto com o pai. Assim
o tempo em cada status sai só das transições.

**RN-27 (vale o que foi registrado primeiro) vira restrição:** toda mudança faz `UPDATE ... WHERE status = <de>` e insere a
transição com `sequence_number` = último + 1. Um segundo evento concorrente encontra o status já mudado (0 linhas) ou
colide na chave da transição, e é recusado. A chave composta é a trava.

### deliveries (Postgres) — Entrega

| Coluna | Tipo | Observação |
|---|---|---|
| delivery_id | bigint, PK | sequencial (decisão 7) |
| order_id | bigint, único | → `orders` (1:1, RN-06) |
| status | varchar | nasce `awaiting_assignment` |
| dropoff_address | varchar | endereço de entrega, copiado do cliente na compra (decisão 8) |
| dropoff_latitude, dropoff_longitude | numeric(9,6) | idem |
| distance_km | numeric(6,2), nulo | rota restaurante → restaurante (se 2) → cliente; base do prazo prometido (RN-28) |
| promised_at | timestamp, nulo | prazo prometido (RN-28); calculado e **congelado** quando o último atendimento ativo é aceito |
| finished_at | timestamp, nulo | finalização pelo motorista ou registro da falha. Começa os relógios de 10 min (confirmação automática, RN-24), 20 min (avaliação e gorjeta, RN-26) e 24 h (incidente, RN-14) |
| failure_reason | varchar, nulo | só em `undelivered`: `customer_absent` ou `driver_unable` (RN-30) |
| created_at, updated_at | timestamp | |

O motorista atual não é coluna: é o da atribuição vigente (RN-31). O critério da ordem dos restaurantes no cálculo da rota
fica para a L4 (parâmetros).

### shifts (Postgres) — Turno

| Coluna | Tipo | Observação |
|---|---|---|
| shift_id | bigint, PK | sequencial próprio (decisão do Turno no L0) |
| driver_id | bigint | `ext → Oracle.drivers` |
| city_id | integer | → `cities`; cidade do motorista **copiada na abertura**, para a RN-35 ser checada no Postgres (decisão 9) |
| status | varchar | `open`, `closed` |
| opened_at | timestamp | só motorista `active` no cadastro abre turno (RN-42) |
| closed_at | timestamp, nulo | |
| close_reason | varchar, nulo | `driver_closed` (o motorista fecha, sem atribuição vigente) ou `driver_unable` (a plataforma fecha na mesma transação da falha, RN-30 e RN-42) |
| created_at, updated_at | timestamp | |

Único: no máximo um turno `open` por motorista (índice único parcial). Turnos do mesmo motorista não se sobrepõem.
Pedidos e ganho do turno são derivados (RN-36): entregas pelas atribuições do turno e repasses da L2. `num_orders`,
`payout_per_order` e afins do gerador atual saem.

### driver_assignments (Postgres) — Atribuição de Motorista

Entidade fraca da entrega: chave composta com a do pai.

| Coluna | Tipo | Observação |
|---|---|---|
| delivery_id | bigint, PK | → `deliveries` |
| assignment_number | smallint, PK | 1, 2, ... na ordem das atribuições |
| driver_id | bigint | `ext → Oracle.drivers` |
| shift_id | bigint | → `shifts`; turno **aberto** do motorista na atribuição (RN-36), da cidade do pedido (RN-35) |
| assigned_at | timestamp | quando o primeiro atendimento fica pronto, ou depois, se não havia motorista (RN-06) |
| released_at | timestamp, nulo | nulo = vigente |
| release_reason | varchar, nulo | `driver_gave_up`, `delivery_cancelled` ou `delivery_finished` |
| created_at, updated_at | timestamp | |

Único: no máximo uma atribuição vigente por entrega e uma por motorista (índices únicos parciais em `delivery_id` e em
`driver_id` onde `released_at` é nulo; RN-42).

Restrições checadas pelo simulador e nos testes:

- `driver_gave_up` só antes da primeira retirada do pedido (RN-07) e nunca da 4ª atribuição em diante (RN-07: depois de 3
  desistências, a atribuição seguinte não se desfaz). A trava sai de `assignment_number`; não é coluna.
- O turno da atribuição é do mesmo motorista, estava `open` em `assigned_at` e tem `city_id` igual ao do pedido.
- O repasse ao motorista (L2) vai para o motorista da atribuição liberada com `delivery_finished`.
- Um motorista não aparece em duas atribuições da mesma entrega se a primeira foi liberada com `driver_gave_up` (RN-42).
- `delivery_finished` é gravado na finalização (`finished_at`), não na conclusão (RN-42).
- Turno com atribuição vigente não fecha, salvo `driver_unable` (RN-42).

### Quem escreve (gerador híbrido, ADR 007)

| Tabela | ShadowTraffic | Simulador |
|---|---|---|
| `orders` | INSERT (`in_analysis`) | UPDATE de `status` |
| `restaurant_orders` | INSERT (`in_analysis`) | todo UPDATE: aceite, rejeição (inclusive `analysis_timeout` e `out_of_stock`), preparo, pronto, chegada do motorista, retirada, cancelamentos |
| `order_items` | INSERT | — |
| `order_status_transitions`, `restaurant_order_status_transitions` | INSERT da linha 1 | INSERT das demais |
| `deliveries` | INSERT (`awaiting_assignment`) | UPDATE |
| `shifts` | — | INSERT e UPDATE (decisão 11) |
| `driver_assignments` | — | INSERT e UPDATE |
| `stock_movements` (L1a) | — | INSERT |

Regra simples: nestas tabelas o ShadowTraffic **só faz INSERT**; todo UPDATE é do simulador. O cancelamento do cliente em
análise (RN-12) também fica com o simulador: ele concorre com o aceite (RN-27), e a fronteira da ADR 007 diz que, depois de
"em análise", só o simulador escreve no atendimento.

**Risco:** o ShadowTraffic grava pedido, atendimentos, itens e entrega em inserts separados, sem transação comum. O simulador
não pode aceitar um atendimento cujos itens ainda não chegaram, porque a checagem de estoque sairia errada. O físico define a
guarda (por exemplo, só processar atendimento que já tenha itens e alguns segundos de idade).

**Verificações nos testes** (o conjunto completo vai para a L4): a consulta da RN-16 sobre `restaurant_orders` confere
`orders.status` até `out_for_delivery`; `deliveries.status = in_transit` exatamente quando o pedido está `out_for_delivery`;
toda linha de transição tem `from_status` igual ao `to_status` da linha anterior.

### Conferência das chaves no gerador atual

A L0 #2 pediu para conferir as chaves das demais tabelas. Estado do `uber-eats.json.template` hoje:

| Tabela ou arquivo atual | Chave hoje | No modelo novo |
|---|---|---|
| `users` (Postgres) | `sequentialInteger` | `customers.customer_id` (Oracle), mantém |
| `drivers` (Postgres) | `sequentialInteger` | mantém (vai para o Oracle) |
| `restaurants` (Oracle) | `sequentialInteger` + coluna `uuid` | mantém; o `uuid` sai (L1a #2) |
| `orders` (Oracle) | `sequentialInteger` (fork) | mantém (vai para o Postgres) |
| `payments` (Oracle) | `sequentialInteger` (fork) | L2 |
| `products` (Oracle) | texto `PRD-########` | **muda** para inteiro sequencial (a L1a já o declara `bigint`) |
| `order_items` (Oracle) | `uuid` | **muda** para (`restaurant_order_id`, `line_number`) |
| `inventory` (Oracle) | `uuid` | **sai**; vira `stock_items` (L1a) |
| `receipts` (Oracle) | `uuid` | L2 (muda para inteiro) |
| `kafka/shift` (MinIO) | `uuid` | **vira tabela** `shifts` (decisão 13) |
| `kafka/route` (MinIO) | `uuid` | **vira tabela** `deliveries` (decisão 13) |

Nada disso é editado agora: o gerador muda na regeração.

### Referências externas da L1b

| De | Coluna | Para |
|---|---|---|
| `orders` | `customer_id` | `ext → Oracle.customers` |
| `shifts` | `driver_id` | `ext → Oracle.drivers` |
| `driver_assignments` | `driver_id` | `ext → Oracle.drivers` |

`orders.city_id` e `shifts.city_id` são **cópias** da cidade do cliente e do motorista (Oracle), feitas no momento da compra
e da abertura do turno. Com elas, a RN-03, a RN-35 e a RN-36 são checadas dentro do Postgres, sem consulta entre bancos.

### Decisões da revisão da L1b (2026-11-02)

| # | Tema | Decisão |
|---|---|---|
| 1 | Nome físico do Atendimento | **`restaurant_orders`** (mais intuitivo que `fulfillments`); L0 #8 e L1a renomeados (`restaurant_order_status_transitions`, `stock_movements.restaurant_order_id`) |
| 2 | Checkout e tentativa de pagamento | **Ficam na L2**; a L1b só guarda `orders.checkout_id` |
| 3 | Status inicial | **`in_analysis`** para atendimento e pedido; "Order Placed" some; a criação é a linha 1 das transições |
| 4 | Instantes de status como colunas | **Só `accepted_at`, `driver_arrived_at` e `picked_up_at`**; os demais só nas transições |
| 5 | Motivo de cancelamento e rejeição | **Uma coluna `end_reason`**, cujo valor já diz o status e quem agiu |
| 6 | Chave do item de pedido | **(`restaurant_order_id`, `line_number`)** |
| 7 | Chave da entrega | **`delivery_id` próprio**, com `order_id` único |
| 8 | Coordenadas | **L1a reaberta**: `latitude`/`longitude` voltam em `customers` e `restaurants`. A entrega guarda cópia do destino, `distance_km` e `promised_at` congelado |
| 9 | Cidade copiada | **Sim**, em `orders` (na compra) e `shifts` (na abertura) |
| 10 | Uma entrega por vez por motorista | **RN-42** (grill de 2026-11-02): uma atribuição vigente por motorista; livre na finalização; quem desiste não volta à mesma entrega; impossibilitado fecha o turno (`shifts.close_reason`); turno não fecha com atribuição vigente; só motorista ativo abre turno |
| 11 | Turno, entrega e atribuição | **Simulador de operação**; adendo na [ADR 007](../../../docs/adr/007-estoque-por-movimentos-e-gerador-hibrido.md) |
| 12 | Código de rastreio | **12 caracteres base32 Crockford** do SHA-256 de `order_id` com sal, calculado fora do banco; mesmo formato para o pagamento na L2 |
| 13 | `kafka/shift` e `kafka/route` no MinIO | **Saem**; `kafka/gps` fica e passa a apontar `delivery_id` (`ext → Postgres.deliveries`) |

---

## L2. Dinheiro: checkout, pagamento, reembolso, repasses, gorjeta e recibo

Todas as tabelas no **Postgres** (ADR 006). Valores em `numeric(12,2)` (L0 #3); percentuais em `numeric(5,4)` (ex.:
`0.1200` = 12%). Sem FK física.

**Ideia central.** O pagamento é um **retrato congelado da compra** (RN-33): ele e os seus componentes nunca mudam. Tudo o
que acontece depois (reembolso, repasse, gorjeta) é um **evento próprio**, com linha nova. Os percentuais vigentes na compra
(imposto, taxa de serviço, meio de pagamento) e no fato gerador (comissão, parcela do motorista) são **copiados** para a
linha, porque os parâmetros podem mudar e o resultado antigo não pode mudar junto (decisão 8).

### Vocabulário

| Coluna | Valores | Regra |
|---|---|---|
| `payment_attempts.result` | `approved`, `declined` | RN-15 |
| `payment_attempts.decline_reason` | `insufficient_funds`, `card_declined`, `expired_card`, `suspected_fraud`, `processing_error` | RN-15 |
| `payment_attempts.payment_method` | `card`, `pix`, `wallet` | decisão 3 da L2 |
| `payment_components.component_type` | `item`, `service_fee`, `delivery_fee` | RN-19, RN-20, RN-33 |
| `refunds.origin_type` | `restaurant_order` (cancelado ou rejeitado), `incident` (procedente), `driver_unable` | RN-10, RN-14, RN-30 |

### checkouts (Postgres) — Checkout

| Coluna | Tipo | Observação |
|---|---|---|
| checkout_id | bigint, PK | sequencial |
| customer_id | bigint | `ext → Oracle.customers` |
| amount | numeric(12,2) | valor da intenção de compra; sem carrinho na v1 (conceitual, decisão 1) |
| created_at | timestamp | |

Gera **no máximo um** pedido e um pagamento (RN-15): garantido por `orders.checkout_id` único (L1b) e pela tentativa
aprovada única (abaixo). "Convertido" ou "abandonado" é derivado (tem ou não tentativa aprovada), não coluna.

### payment_attempts (Postgres) — Tentativa de Pagamento

Entidade fraca do checkout.

| Coluna | Tipo | Observação |
|---|---|---|
| checkout_id | bigint, PK | → `checkouts` |
| attempt_number | smallint, PK | 1, 2, ... |
| amount | numeric(12,2) | igual a `checkouts.amount` |
| payment_method | varchar | `card`, `pix`, `wallet` |
| card_brand | varchar, nulo | só em `card` (Visa, Mastercard, Elo, ...) |
| wallet_provider | varchar, nulo | só em `wallet` (Apple Pay, Google Pay, ...) |
| gateway | varchar | processador (hoje `provider`: Stripe, Adyen, ...) |
| result | varchar | `approved` ou `declined` |
| decline_reason | varchar, nulo | só em `declined` |
| attempted_at | timestamp | |
| created_at | timestamp | imutável |

Único: no máximo uma tentativa `approved` por checkout (índice único parcial). É o que torna a aprovação repetida
inofensiva (RN-15). A recusada nunca tem pedido nem pagamento.

Saem do gerador atual: `currency` (só Brasil, sempre BRL), `ip_address` e `user_agent` (sem regra), `card_exp_month` e
`card_exp_year`.

### payments (Postgres) — Pagamento

| Coluna | Tipo | Observação |
|---|---|---|
| payment_id | bigint, PK | sequencial |
| tracking_code | char(12), único | mesmo formato do pedido (L1b, decisão 12), com outro sal |
| order_id | bigint, único | → `orders` (1:1, RN-08) |
| checkout_id, attempt_number | bigint, smallint | → `payment_attempts`: a tentativa aprovada que o gerou. Único |
| total_amount | numeric(12,2) | valor pago: itens + taxa de serviço + taxa de entrega, imposto embutido (RN-19). Igual à soma dos componentes |
| tax_rate | numeric(5,4) | alíquota única vigente na compra (RN-09) |
| service_fee_rate | numeric(5,4) | percentual da taxa de serviço sobre os itens (RN-19) |
| payment_fee_rate | numeric(5,4) | custo do meio de pagamento sobre o valor pago (RN-29) |
| payment_fee_amount | numeric(12,2) | custo do meio de pagamento; da plataforma, **não devolvido** em estorno (RN-29) |
| paid_at | timestamp | aprovação; igual a `orders.placed_at` |
| created_at | timestamp | imutável; sem `updated_at` (o pagamento nunca muda, RN-08) |

O meio de pagamento é o da tentativa aprovada (não é copiado). Saem: `status` e os estados `pending`/`failed`/`refunded`
(RN-11), `refund_amount` (vira `refunds`), `net_amount`, `platform_fee` e `tax_amount` (derivados; decisão 1).

### payment_components (Postgres) — Componente do Pagamento

Entidade fraca do pagamento. Divisão **congelada na compra** (RN-33).

| Coluna | Tipo | Observação |
|---|---|---|
| payment_id | bigint, PK | → `payments` |
| component_number | smallint, PK | 1, 2, ... |
| component_type | varchar | `item`, `service_fee` ou `delivery_fee` |
| restaurant_order_id, line_number | bigint, smallint, nulos | → `order_items`; nulos só em `delivery_fee` |
| gross_amount | numeric(12,2) | valor bruto do componente, imposto embutido |
| tax_amount | numeric(12,2) | imposto decomposto do bruto (RN-33: decomposição, nunca acréscimo) |
| created_at | timestamp | imutável |

Por item do pedido há **dois** componentes: `item` (o `total_amount` do item) e `service_fee` (a parte da taxa de serviço
alocada a ele, decisão 2). A taxa de entrega é **um** componente por pagamento, sem atendimento (RN-20: nunca rateada).
Em toda alocação, cada parcela é calculada e a última absorve a diferença (RN-33).

Único: (`payment_id`, `component_type`, `restaurant_order_id`, `line_number`), e um só `delivery_fee` por pagamento.

### refunds (Postgres) — Reembolso

| Coluna | Tipo | Observação |
|---|---|---|
| refund_id | bigint, PK | sequencial |
| payment_id | bigint | → `payments` |
| origin_type | varchar | `restaurant_order`, `incident` ou `driver_unable` |
| restaurant_order_id | bigint, nulo | → `restaurant_orders`; só em `restaurant_order` |
| incident_id | bigint, nulo | → `incidents` (L3); só em `incident` |
| delivery_id | bigint, nulo | → `deliveries`; só em `driver_unable` |
| total_amount | numeric(12,2) | soma dos componentes reembolsados |
| refunded_at | timestamp | |
| created_at | timestamp | imutável |

Exatamente uma das três referências é preenchida, conforme `origin_type` (uma única origem, conceitual 2.2). Único: um
reembolso por atendimento, por incidente e por entrega (índices únicos parciais).

**Quem arca** não é coluna: sai da origem. `incident` e `driver_unable` são prejuízo da plataforma (RN-14, RN-30); em
`restaurant_order` o dinheiro só volta, porque não há repasse de atendimento não retirado (RN-29).

**O que cada origem devolve:**

| Origem | Componentes devolvidos | Regra |
|---|---|---|
| `restaurant_order` | `item` e `service_fee` de todos os itens do atendimento; mais o `delivery_fee` se não restar atendimento ativo | RN-21 |
| `incident` | `item` e `service_fee` dos itens apontados, na proporção da quantidade; `delivery_fee` só se o motivo for de entrega | RN-14 |
| `driver_unable` | tudo o que ainda não foi devolvido | RN-30 |

### refund_components (Postgres) — Componente Reembolsado

Entidade fraca do reembolso.

| Coluna | Tipo | Observação |
|---|---|---|
| refund_id | bigint, PK | → `refunds` |
| component_number | smallint, PK | → `payment_components`, junto com o `payment_id` do reembolso |
| quantity | integer, nulo | unidades devolvidas, em componente de item (incidente parcial) |
| gross_amount | numeric(12,2) | |
| tax_amount | numeric(12,2) | acompanha o bruto na mesma proporção (RN-09) |
| created_at | timestamp | imutável |

Invariantes (RN-33, checadas nos testes): o reembolsado acumulado por componente nunca passa do `gross_amount` dele; a
soma dos reembolsos nunca passa do `total_amount` do pagamento; cancelar todos os atendimentos devolve exatamente o
pagamento; a quantidade devolvida por item, somando incidentes, nunca passa da comprada (RN-14).

### restaurant_payouts (Postgres) — Repasse ao Restaurante

Entidade fraca 1:1 do atendimento: a chave é a do pai.

| Coluna | Tipo | Observação |
|---|---|---|
| restaurant_order_id | bigint, PK | → `restaurant_orders`; só atendimento **retirado** (RN-29) |
| restaurant_id | bigint | → `restaurants`; cópia do restaurante do atendimento, para consulta direta (decisão 7) |
| items_amount | numeric(12,2) | soma dos componentes `item` do atendimento |
| commission_rate | numeric(5,4) | comissão vigente na retirada |
| commission_amount | numeric(12,2) | retenção da plataforma |
| payout_amount | numeric(12,2) | `items_amount` − `commission_amount` |
| due_at | timestamp | a retirada (`restaurant_orders.picked_up_at`); obrigação reconhecida, não liquidação |
| created_at | timestamp | imutável |

Incidente procedente e cliente ausente não mexem no repasse (RN-29).

### driver_payouts (Postgres) — Repasse ao Motorista

Entidade fraca 1:1 da entrega.

| Coluna | Tipo | Observação |
|---|---|---|
| delivery_id | bigint, PK | → `deliveries`; só em `delivered`, ou `undelivered` por `customer_absent` (RN-29) |
| driver_id | bigint | `ext → Oracle.drivers`; cópia do motorista da atribuição liberada com `delivery_finished` (decisão 7) |
| shift_id | bigint | → `shifts`; cópia do turno dessa atribuição (base do ganho do turno, RN-36) |
| delivery_fee_amount | numeric(12,2) | o componente `delivery_fee` do pagamento |
| driver_share_rate | numeric(5,4) | parcela do motorista vigente na finalização |
| payout_amount | numeric(12,2) | parcela do motorista; o resto da taxa fica com a plataforma |
| due_at | timestamp | `deliveries.finished_at` |
| created_at | timestamp | imutável |

Teste: `driver_id` e `shift_id` batem com a atribuição liberada com `delivery_finished` (L1b).

### tips (Postgres) — Gorjeta

Entidade fraca 1:1 da entrega.

| Coluna | Tipo | Observação |
|---|---|---|
| delivery_id | bigint, PK | → `deliveries`; no máximo uma por entrega, só de pedido **entregue** ou **concluído** (RN-22) |
| driver_id | bigint | `ext → Oracle.drivers`; cópia do motorista da entrega (decisão 7) |
| amount | numeric(12,2) | entre o mínimo e o máximo (parâmetros, RN-22) |
| paid_at | timestamp | até 20 minutos depois de `deliveries.finished_at`, limite inclusivo (RN-26) |
| created_at | timestamp | imutável |

Fora do pagamento, sem retenção, nunca estornada (RN-22). Não existe se a nota do motorista for 3 ou menor (RN-26; a
avaliação é da L3).

### receipts (Postgres) — Recibo

Entidade fraca 1:1 do pagamento.

| Coluna | Tipo | Observação |
|---|---|---|
| payment_id | bigint, PK | → `payments` |
| issued_at | timestamp | emissão |
| created_at | timestamp | imutável |

Documento único da compra; reembolsos não o alteram (conceitual, decisão 5). Saem `total_amount`, `item_count` e
`receipt_url` (derivados ou sem uso).

### Quem escreve

| Tabela | ShadowTraffic | Simulador |
|---|---|---|
| `checkouts`, `payment_attempts`, `payments`, `payment_components`, `receipts` | INSERT na compra (decisão 10) | — |
| `refunds`, `refund_components` | — | INSERT no cancelamento, na rejeição e em `driver_unable`; incidente fica para a L3 |
| `restaurant_payouts` | — | INSERT na retirada |
| `driver_payouts` | — | INSERT na finalização |
| `tips` | — | INSERT (ação do cliente depois da entrega) |

Todas as tabelas da L2 são **só INSERT**: nenhuma linha de dinheiro é atualizada depois de gravada.

### Referências externas da L2

| De | Coluna | Para |
|---|---|---|
| `checkouts` | `customer_id` | `ext → Oracle.customers` |
| `driver_payouts`, `tips` | `driver_id` | `ext → Oracle.drivers` |

### Decisões da revisão da L2 (2026-11-02)

| # | Tema | Decisão |
|---|---|---|
| 1 | Totais do pagamento | **Só `total_amount` e `payment_fee_amount`**; imposto total, taxa da plataforma e líquido (RN-09) são derivados na Gold |
| 2 | Taxa de serviço | **Alocada por item**: o item tem até dois componentes (`item` e `service_fee`); diagrama 2.2 ajustado |
| 3 | Meios de pagamento | **`card`, `pix`, `wallet`**; boleto e moeda saem |
| 4 | Detalhe do meio | **Só na tentativa**; o pagamento aponta a tentativa aprovada |
| 5 | Motivos de recusa | **`insufficient_funds`, `card_declined`, `expired_card`, `suspected_fraud`, `processing_error`** |
| 6 | Origem do reembolso | **`origin_type` + três referências**, exatamente uma preenchida |
| 7 | Chaves 1:1 | **Chave do pai + cópia** para consulta direta: `restaurant_id` no repasse ao restaurante; `driver_id` e `shift_id` no repasse ao motorista; `driver_id` na gorjeta. Testes conferem a cópia contra a origem |
| 8 | Percentuais | **Congelados na linha** (pagamento e repasses) |
| 9 | Recibo | **Tabela mínima** `receipts(payment_id, issued_at)` |
| 10 | Geração do dinheiro da compra | **Só invariantes no lógico**; na regeração se decide se o ShadowTraffic dá conta ou se a compra vai para o simulador |

---

## L3. Pós-entrega: incidente e avaliação

Todas as tabelas no **Postgres** (ADR 006). Mesmas convenções: tipos em notação Postgres, horário de Brasília, sem FK
física. Os três relógios partem de `deliveries.finished_at` (L1b) e são **parâmetros** (L0 #5): 24 h para abrir incidente
(RN-14), 20 min para avaliar e dar gorjeta, limite inclusivo (RN-26).

**Escopo do pós-entrega.** Só pedido com entrega `delivered` (pedido `delivered` ou `completed`) tem incidente, avaliação ou
gorjeta. Em `undelivered` não há o que reclamar nem avaliar: `customer_absent` não tem devolução (RN-25) e `driver_unable`
já devolve tudo automaticamente (RN-30); avaliações e gorjeta são desconsideradas (RN-26). Nada do pós-entrega muda o
status do pedido, do atendimento ou da entrega (RN-14, RN-30), e um incidente aberto não impede a confirmação automática
(RN-28).

### Vocabulário

**Status do incidente** (RN-14: aberto → em análise → procedente ou improcedente; decidido não reabre na v1):

| Valor | Significado | Terminal |
|---|---|---|
| `open` | aberto pelo cliente; **status inicial** | |
| `in_review` | a plataforma começou a análise | |
| `upheld` | procedente: gera o reembolso **na mesma transação** | sim |
| `dismissed` | improcedente: sem reembolso | sim |

**Motivo do incidente** (`incidents.reason`). O motivo diz o que o incidente aponta e se a taxa de entrega volta (RN-14):

| Motivo | Tipo | Aponta itens | Devolve, se procedente |
|---|---|---|---|
| `missing_item` | item | sim, ao menos um | `item` e `service_fee` dos itens apontados, na proporção da quantidade |
| `wrong_item` | item | sim, ao menos um | idem |
| `food_quality` | item | sim, ao menos um | idem |
| `late_delivery` | entrega | não | só o `delivery_fee` |
| `not_received` | entrega | sim, **todos** os itens com saldo, gravados pelo simulador | tudo o que ainda não foi devolvido (itens, `service_fee` e `delivery_fee`) |
| `driver_unable` | entrega | sim, ao menos um | `item` e `service_fee` dos itens apontados, mais o `delivery_fee` |

**`driver_unable` no incidente ≠ estorno da RN-30 (decisão 1).** O estorno automático da RN-30 (origem `driver_unable` no
reembolso, L2) é de entrega que **não terminou**: o pedido fica `undelivered`, a plataforma registra a falha e não há
incidente. O incidente `driver_unable` é de entrega **finalizada** (`delivered`) em que o motorista não conseguiu entregar
parte dos itens (por exemplo, avariados no trajeto): o cliente reclama, a plataforma arbitra e, se procedente, devolve os
itens apontados e a taxa de entrega.

### incidents (Postgres) — Incidente

| Coluna | Tipo | Observação |
|---|---|---|
| incident_id | bigint, PK | sequencial; já referenciado por `refunds.incident_id` (L2) |
| order_id | bigint | → `orders`; pedido `delivered` ou `completed` |
| customer_id | bigint | `ext → Oracle.customers`; cópia do cliente do pedido, para consulta direta (L2, decisão 7) |
| reason | varchar | tabela de motivos acima |
| description | varchar, nulo | texto livre do cliente; na geração, texto sintético por motivo |
| status | varchar | nasce `open` |
| opened_at | timestamp | até `deliveries.finished_at` + 24 h, limite validado no próprio comando (RN-28) |
| review_started_at | timestamp, nulo | passagem a `in_review` |
| decided_at | timestamp, nulo | passagem a `upheld` ou `dismissed`; igual a `refunds.refunded_at` quando procedente |
| created_at, updated_at | timestamp | |

Único: no máximo **um incidente de entrega** (`late_delivery`, `not_received` ou `driver_unable`) por pedido (índice único parcial,
decisão 6). Incidentes de item podem ser vários.

Restrições checadas pelo simulador e nos testes:

- `late_delivery` só é procedente se houve atraso de fato: `finished_at` > `promised_at` (L1b). A condição é objetiva.
- `not_received` é improcedente quando o cliente estava ausente (RN-30). Como o pedido está `delivered`, o "ausente" é uma
  verdade escondida que o simulador sorteia; o modelo guarda só o desfecho.
- Procedente gera **exatamente um** reembolso com origem `incident` (L2), na mesma transação; improcedente nunca gera.
- As mudanças de status seguem a RN-27 da L1b: `UPDATE ... WHERE status = <de>`. O histórico do incidente fica nas colunas
  de instante, sem tabela de transições (decisão 4).

### incident_items (Postgres) — Incidente por Item

Entidade fraca do incidente.

| Coluna | Tipo | Observação |
|---|---|---|
| incident_id | bigint, PK | → `incidents` |
| restaurant_order_id, line_number | bigint, smallint, PK | → `order_items`; item de um atendimento **retirado** do pedido do incidente |
| quantity | integer | ≥ 1 |
| created_at | timestamp | imutável; gravado junto com o incidente |

Teto (RN-14): por item do pedido, a soma de `quantity` nos incidentes **não improcedentes** (`open`, `in_review`, `upheld`)
nunca passa de `order_items.quantity` (decisão 5). Um incidente em aberto reserva a quantidade; o improcedente a libera.
O componente reembolsado (`refund_components.quantity`, L2) repete a `quantity` do incidente por item.

### driver_ratings (Postgres) — Avaliação do Motorista

Entidade fraca 1:1 da entrega, como a gorjeta.

| Coluna | Tipo | Observação |
|---|---|---|
| delivery_id | bigint, PK | → `deliveries`; só entrega `delivered`; no máximo uma por entrega (RN-26) |
| driver_id | bigint | `ext → Oracle.drivers`; cópia do motorista da atribuição liberada com `delivery_finished` (L1b) |
| customer_id | bigint | `ext → Oracle.customers`; cópia do cliente do pedido |
| rating | smallint | 1 a 5 |
| comment | varchar, nulo | texto livre; na geração, frases sintéticas por faixa de nota |
| rated_at | timestamp | até `deliveries.finished_at` + 20 min, limite inclusivo (RN-26) |
| created_at | timestamp | imutável; a avaliação não é editada na v1 |

**Cruzamento com a gorjeta (RN-26):** não existe gorjeta com `paid_at` ≥ `rated_at` de uma avaliação com nota 3 ou menor. A
gorjeta dada **antes** da avaliação continua valendo ("uma gorjeta já dada nunca é invalidada"). O simulador decide a
avaliação antes de oferecer a gorjeta; o teste confere a ordem.

### restaurant_ratings (Postgres) — Avaliação do Restaurante

Entidade fraca 1:1 do atendimento.

| Coluna | Tipo | Observação |
|---|---|---|
| restaurant_order_id | bigint, PK | → `restaurant_orders`; só atendimento `picked_up` de pedido `delivered` ou `completed` (RN-26) |
| restaurant_id | bigint | → `restaurants`; cópia do restaurante do atendimento |
| customer_id | bigint | `ext → Oracle.customers`; cópia do cliente do pedido |
| rating | smallint | 1 a 5 |
| comment | varchar, nulo | como em `driver_ratings` |
| rated_at | timestamp | até `deliveries.finished_at` + 20 min, limite inclusivo |
| created_at | timestamp | imutável |

Avaliação ausente nunca vira zero: a Gold mostra quantidade e média, junto com as taxas de cancelamento, rejeição e atraso
(RN-26).

### Quem escreve

| Tabela | ShadowTraffic | Simulador |
|---|---|---|
| `incidents` | — | INSERT (ação do cliente) e UPDATE de status (análise e decisão da plataforma) |
| `incident_items` | — | INSERT junto com o incidente |
| `refunds`, `refund_components` com origem `incident` (L2) | — | INSERT na decisão procedente. **Fecha a pendência da L2** |
| `driver_ratings`, `restaurant_ratings` | — | INSERT (ação do cliente depois da entrega) |

Todo o pós-entrega é do **simulador**, porque depende do relógio de `finished_at` e cruza com gorjeta e reembolso. Das
tabelas da L3, só `incidents` recebe UPDATE.

### Referências externas da L3

| De | Coluna | Para |
|---|---|---|
| `incidents`, `driver_ratings`, `restaurant_ratings` | `customer_id` | `ext → Oracle.customers` |
| `driver_ratings` | `driver_id` | `ext → Oracle.drivers` |

Testes conferem as cópias: `customer_id` contra `orders`, `driver_id` contra a atribuição `delivery_finished`,
`restaurant_id` contra `restaurant_orders`.

### O gerador atual

| Arquivo atual (MinIO) | Hoje | No modelo novo |
|---|---|---|
| `mysql/ratings` | `rating_id` sequencial + `uuid`, uma nota por `order_id`, data aleatória desde 2021 | **sai**; vira `driver_ratings` e `restaurant_ratings` no Postgres |
| `mongodb/support` | `ticket_id` uuid; categorias `Late Delivery`, `Wrong Item`, `Missing Item`, `Payment Issue`, `Other`; status `Open`/`In Progress`/`Resolved`/`Closed`; descrição em Lorem | **sai**; vira `incidents` e `incident_items`. As categorias viram `late_delivery`, `wrong_item` e `missing_item` (as outras duas já saíram no conceitual) |

Com isso, o MinIO fica só com `kafka/gps` (L1b, decisão 13). Nada é editado agora: o gerador muda na regeração.

### Decisões da revisão da L3 (2026-11-02)

| # | Tema | Decisão |
|---|---|---|
| 1 | Motivo `driver_unable` no incidente | **Fica**, como motivo de entrega em pedido `delivered`: o motorista não entregou parte dos itens. Aponta itens e devolve itens, taxa de serviço e taxa de entrega. Distinto do estorno automático da RN-30 (entrega não finalizada) |
| 2 | Incidente em pedido não entregue | **Não existe**: incidente, avaliação e gorjeta só com entrega `delivered` |
| 3 | Devolução dos motivos de entrega | **Atraso**: só a taxa de entrega, procedente só se `finished_at` > `promised_at`. **Não recebido**: tudo o que resta, com todos os itens gravados no incidente |
| 4 | Histórico do incidente | **Colunas** `review_started_at` e `decided_at`; sem tabela de transições |
| 5 | Teto de quantidade por item | Soma dos incidentes **não improcedentes** (o aberto reserva, o improcedente libera) |
| 6 | Incidente de entrega repetido | **Um por pedido** (índice único parcial) |
| 7 | Avaliações | **Chave do pai + cópias** (`driver_id` ou `restaurant_id`, mais `customer_id`), imutáveis, testadas como na L2 |
| 8 | `mysql/ratings` e `mongodb/support` no MinIO | **Saem**; viram tabelas no Postgres. O MinIO fica só com `kafka/gps` |

---

## L4. Visão integrada: restrições, parâmetros e histórico de status

Fecha o modelo lógico: reúne o que as fases L1a a L3 deixaram para "os testes" e "a L4", fixa a lista de parâmetros e
formaliza o histórico de status. Não cria tabela nova.

### Quem garante cada restrição

Três mecanismos, do mais forte ao mais fraco (sem FK física, L0 #9):

| Mecanismo | O que garante | Quando falha |
|---|---|---|
| **Índice único** (inclusive parcial) | Unicidade e a trava da RN-27 | A escrita é recusada no banco |
| **Simulador** (dentro da transação) | Regras de estado, prazo e dinheiro na hora de gravar | O comando é recusado com aviso |
| **Teste de verificação** (consulta sobre os dados) | Tudo o que cruza tabelas ou bancos; é a rede de proteção do que o simulador esqueceu | O teste falha e a regeração não é aprovada |

### Catálogo 1: índices únicos

| Tabela | Único | Regra |
|---|---|---|
| `customers` | `email` | |
| `restaurants` | `cnpj` | |
| `stock_items` | (`restaurant_id`, `name`) | |
| `stock_movements` | (`restaurant_order_id`, `stock_item_id`) onde `consumption` | RN-38: uma baixa por atendimento e item |
| `orders` | `tracking_code`; `checkout_id` | RN-15: um checkout, no máximo um pedido |
| `restaurant_orders` | (`order_id`, `restaurant_id`) | RN-05 |
| `deliveries` | `order_id` | RN-06 |
| `shifts` | `driver_id` onde `status = open` | RN-42 |
| `driver_assignments` | `delivery_id` e `driver_id`, ambos onde `released_at` é nulo | RN-31, RN-42 |
| `payment_attempts` | `checkout_id` onde `result = approved` | RN-15 |
| `payments` | `tracking_code`; `order_id`; (`checkout_id`, `attempt_number`) | RN-08 |
| `payment_components` | (`payment_id`, `component_type`, `restaurant_order_id`, `line_number`); um `delivery_fee` por pagamento | RN-20 |
| `refunds` | `restaurant_order_id`, `incident_id`, `delivery_id`, cada um onde não nulo | um reembolso por origem |
| `incidents` | `order_id` onde `reason` é de entrega | L3, decisão 6 |

### Catálogo 2: invariantes verificados por teste

**Pedido e operação (L1a, L1b)**

| # | Invariante | Regra |
|---|---|---|
| T1 | Pedido com 1 ou 2 atendimentos, todos de restaurantes da `orders.city_id` | RN-03, RN-35 |
| T2 | `orders.status` igual à derivação da RN-16 até `out_for_delivery`; `deliveries.status = in_transit` exatamente quando o pedido está `out_for_delivery` | L0 #7 |
| T3 | Em toda tabela de transição, `from_status` é o `to_status` da linha anterior; só transições da tabela das regras; o status da linha-pai é o `to_status` da última transição | RN-18, L1b |
| T4 | Produto do item é do restaurante do atendimento; item de estoque da ficha e do movimento são do mesmo restaurante do produto | RN-37 |
| T5 | Atribuição: turno do mesmo motorista, `open` em `assigned_at`, com `city_id` igual ao do pedido; `driver_gave_up` só antes da primeira retirada e nunca da 4ª atribuição em diante | RN-07, RN-35, RN-36 |
| T6 | Saldo `quantity_on_hand` nunca negativo e igual à soma dos movimentos; reposição só fora das janelas do perfil | RN-39, RN-40 |
| T7 | `estimated_prep_min` e `accepted_at` preenchidos de `accepted` em diante; `promised_at` congelado quando o último atendimento ativo é aceito | RN-28 |

**Dinheiro (L2)**

| # | Invariante | Regra |
|---|---|---|
| T8 | `payments.total_amount` = soma dos `gross_amount` dos componentes; `paid_at` = `orders.placed_at`; valor do pagamento = valor da tentativa aprovada | RN-33 |
| T9 | Reembolsado acumulado por componente ≤ `gross_amount`; soma dos reembolsos ≤ `total_amount`; todos os atendimentos cancelados devolvem exatamente o pagamento; o resultado não depende da ordem dos cancelamentos | RN-33 |
| T10 | Cópias conferem com a origem: `restaurant_payouts.restaurant_id`, `driver_payouts.driver_id` e `shift_id`, `tips.driver_id` | L2, decisão 7 |
| T11 | Repasse ao restaurante só de atendimento `picked_up`; repasse ao motorista só de entrega `delivered` ou `customer_absent`; gorjeta só de entrega `delivered` | RN-29, RN-22 |

**Pós-entrega (L3)**

| # | Invariante | Regra |
|---|---|---|
| T12 | Incidente, avaliação e gorjeta só com entrega `delivered`; `incidents.opened_at` ≤ `finished_at` + 24 h; `rated_at` e `tips.paid_at` ≤ `finished_at` + 20 min (inclusivo) | RN-14, RN-26 |
| T13 | `incident_items` aponta item de atendimento `picked_up` do pedido do incidente; soma de `quantity` por item nos incidentes não improcedentes ≤ `order_items.quantity` | RN-14 |
| T14 | `upheld` ⇒ exatamente um reembolso `incident` com `refunded_at` = `decided_at` e `refund_components.quantity` = `incident_items.quantity`; `dismissed`, `open` e `in_review` ⇒ nenhum | RN-14 |
| T15 | `late_delivery` procedente ⇒ `finished_at` > `promised_at` | RN-14, RN-28 |
| T16 | Nenhuma gorjeta com `paid_at` ≥ `rated_at` de avaliação do motorista com nota ≤ 3; cópias de avaliação e incidente conferem com a origem | RN-26 |

**Entre bancos**

| # | Invariante | Regra |
|---|---|---|
| T17 | Todo `ext → Oracle.*` aponta para uma linha existente (cliente ou motorista); `cities` é idêntica nos dois bancos; `orders.city_id` = cidade do cliente na compra, `shifts.city_id` = cidade do motorista na abertura | L0 #10, #11 |
| T18 | Todo `menu_items[].product_id` e `restaurant_id` do MongoDB aponta para linha existente do Postgres; todo restaurante tem perfil | RN-23 |

### Parâmetros

Valores das regras estão fixados; os demais são **valor inicial sugerido**, para ajuste na regeração. Os percentuais são
**copiados para a linha** quando usados (L2, decisão 8), então mudar um parâmetro nunca altera dado antigo.

| Parâmetro | Valor | Onde é usado | Regra |
|---|---|---|---|
| `incident_window` | 24 h | abertura de incidente | RN-14 |
| `rating_tip_window` | 20 min, inclusivo | avaliação e gorjeta | RN-26 |
| `auto_confirm_delay` | 10 min | confirmação automática | RN-24, RN-28 |
| `analysis_timeout` | 5 min | rejeição automática | RN-28 |
| `prep_tolerance` | 50% | atraso do restaurante | RN-28 |
| `max_restaurants_per_order` | 2 | pedido | RN-03 |
| `max_driver_give_ups` | 3 | atribuição que não se desfaz | RN-07 |
| `average_speed_kmh` | sugestão: 25 | prazo prometido | RN-28 |
| `promise_slack_min` | sugestão: 10 | prazo prometido | RN-28 |
| `route_detour_factor` | sugestão: 1,3 (linha reta × fator) | `deliveries.distance_km` | RN-28 |
| `tax_rate` | sugestão: 0,0800 | `payments.tax_rate` | RN-09 |
| `service_fee_rate` | sugestão: 0,1200 | `payments.service_fee_rate` | RN-19 |
| `payment_fee_rate` | sugestão: `card` 0,0299; `pix` 0,0099; `wallet` 0,0250 | `payments.payment_fee_rate` | RN-29 |
| `commission_rate` | sugestão: 0,2500 | `restaurant_payouts.commission_rate` | RN-29 |
| `driver_share_rate` | sugestão: 0,8000 | `driver_payouts.driver_share_rate` | RN-29 |
| `tip_min`, `tip_max` | sugestão: 1,00 e 100,00 | `tips.amount` | RN-22 |
| `rating_comment_by_band` | frases sintéticas por faixa de nota | `comment` das avaliações | RN-26 |

**Ordem dos restaurantes na rota (pendência da L1b).** A distância de `deliveries.distance_km` percorre restaurante →
restaurante → cliente quando há dois. Sem posição do motorista, o critério precisa vir só das coordenadas dos três pontos.

### Histórico de status: ADR 008

A L0 #8 já fez do histórico de pedido e de atendimento **tabelas** (RN-18), contra a Onda 3, que o tinha removido em favor
de mutação de linha capturada por CDC. Falta registrar a decisão, porque é difícil de reverter (muda o contrato da Bronze e
o desenho da Silver) e tem troca real. A [ADR 008](../../../docs/adr/008-historico-de-status-em-tabelas-de-transicao.md) registra a decisão, com as alternativas: **A**, tabelas de
transição gravadas na mesma transação; **B**, só CDC, com a Silver reconstruindo o histórico (`apply_changes` com SCD2);
**C**, as duas coisas.

### Decisões da revisão da L4 (2026-11-02)

| # | Tema | Decisão |
|---|---|---|
| 1 | Parâmetros | **Arquivo único versionado**, lido por simulador, gerador e testes; sem tabela. O local fica para o físico |
| 2 | Ordem dos restaurantes na rota | **Menor rota total** (testa as duas ordens), desempate pelo menor `restaurant_id` |
| 3 | Gorjeta antes da confirmação | **Pedido `delivered` ou `completed`**. RN-22, conceitual (3.3) e `tips` ajustados: "concluída" vira "finalizada com sucesso" |
| 4 | Histórico de status | **Alternativa A** (tabelas de transição); registrada na [ADR 008](../../../docs/adr/008-historico-de-status-em-tabelas-de-transicao.md) |
| 5 | Valores iniciais | **Aceitos** como sugeridos; ajustáveis na regeração |
