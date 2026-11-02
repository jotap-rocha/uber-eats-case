# Modelo lógico

Terceira etapa do fluxo (regras → adversarial → conceitual → **lógico** → físico → regeração). Parte do
[modelo conceitual](02-modelo-conceitual.md) e das [regras de negócio](01-regras-de-negocio.md). Revisão por fases.

| Fase | Conteúdo | Status |
|---|---|---|
| L0 | Convenções transversais | aprovada |
| L1a | Pessoas, cidade e catálogo (parte do diagrama 2.1) | aprovada |
| L1b | Operação: pedido, atendimento, entrega, turno, atribuição, transições (parte do diagrama 2.1) | pendente |
| L2 | Dinheiro (diagrama 2.2) | pendente |
| L3 | Pós-entrega (diagrama 2.3) | pendente |
| L4 | Visão integrada: restrições entre tabelas, parâmetros, ADR do histórico de status | pendente |

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
| 8 | Histórico de status | `order_status_transitions` e `fulfillment_status_transitions` são **tabelas** (RN-18), como no conceitual. |
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
| fulfillment_id | bigint, nulo | → atendimento (L1b); obrigatório em `consumption`, nulo em `restock` |
| occurred_at | timestamp | reposição só fora das janelas (RN-40) |
| created_at | timestamp | |

Único: (`fulfillment_id`, `stock_item_id`) quando `consumption` — no máximo uma baixa por atendimento e item (RN-38).

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
