# BRAINSTORM: Modelo Conceitual do Domínio Uber Eats

| Campo | Valor |
|-------|-------|
| **Feature** | MODELO_CONCEITUAL_UBER_EATS |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/plan.md`), item "Modelo conceitual" |
| **Status** | ✅ Shipped |
| **Data** | 2026-08-24 |

---

## Ideia inicial

O usuário elaborou um roadmap multi-cloud (`docs/plan.md`) para implementar as arquiteturas Warehouse, Lakehouse e Kappa nas 3 clouds (Azure, AWS, GCP), reaproveitando os dados do projeto pessoal Uber Eats. A Fase 0 (bloqueante) exige corrigir a integridade referencial do Shadow Traffic e desenhar um modelo conceitual único, reaproveitado nas 3 arquiteturas e 3 clouds. Esta feature cobre exclusivamente o desenho do modelo conceitual — a correção do Shadow Traffic fica para a próxima feature.

---

## Decisões de escopo (organização do processo)

| # | Decisão | Resposta |
|---|---------|----------|
| 1 | Como organizar o roadmap de 5 fases dentro do SDD? | Um ciclo BRAINSTORM→DEFINE→DESIGN→BUILD→SHIP por item de trabalho real, aberto conforme a necessidade surge — não um ciclo por Fase inteira nem por arquitetura×cloud completa (fica grande demais / não cabe). |
| 2 | Qual o primeiro item a virar feature? | Modelo conceitual do domínio, por anteceder logicamente a correção de integridade referencial (define o que é "relacionamento correto" antes de corrigir o gerador). |

---

## Discovery Questions & Answers

| # | Pergunta | Resposta | Impacto |
|---|----------|----------|---------|
| 1 | Nível de profundidade: só entidades+relacionamentos+cardinalidade, ou também atributos-chave? | Só conceitual — entidades, relacionamentos, cardinalidade. Sem atributos/tipos. | Mantém separação limpa com a modelagem dimensional da Fase 1 (Warehouse). |
| 2 | O modelo deve mapear cada entidade à origem técnica atual (Postgres/MySQL/MongoDB/Kafka)? | Sim, mapear à origem — serve de insumo direto pra corrigir o Shadow Traffic depois. | Toda entidade no modelo final indica de qual stream/gerador vem hoje. |
| 3 | Formato de entrega? | Apenas tabela textual (sem diagrama Mermaid/visual). | Deliverable é 100% tabelas markdown. |
| 4 (sample collection) | Existem amostras adicionais além do que foi encontrado por exploração própria? | Não — o gerador (`gen/minio/uber-eats.json`) é a fonte única da verdade; todos os dados nascem dele. | Nenhuma fonte externa a considerar. |

---

## Sample Data Inventory

| Tipo | Localização | Cobertura | Notas |
|------|-------------|-----------|-------|
| Gerador ShadowTraffic (MinIO) | `gen/minio/uber-eats.json` | 20 streams simulando 4 origens (Postgres, MySQL, MongoDB, Kafka) | Fonte única e completa da verdade para o domínio — confirmado pelo usuário |
| DDL Postgres real | `sql/create_users_table.sql` | Tabela `users` (schema OLTP rico, campos de perfil/pedido agregado) | Schema real, separado da simulação MinIO |
| DDL Postgres real | `sql/create_drivers_table.sql` | Tabela `drivers` | Schema real |
| Planejamento | `docs/plan.md` | Lista original de 8 entidades-alvo (Fase 0) | Ponto de partida, não lista fechada — Motorista foi adicionado apesar de não estar na lista original |

---

## Abordagens exploradas

### Abordagem A: Modelo alvo / prescritivo ⭐ Recomendado (escolhido)

**O que faz:** define a chave canônica e o relacionamento correto para cada entidade, documentando os desvios atuais do gerador como "a corrigir".

**Por que escolhido:** vira o contrato que a próxima feature (correção do Shadow Traffic) implementa diretamente, sem reabrir a pergunta "qual chave é a certa".

### Abordagem B: Modelo descritivo (as-is)

**O que faz:** só registra entidades/relacionamentos/cardinalidade/origem exatamente como estão hoje no gerador, sem prescrever qual chave deveria vencer.

**Por que não escolhido:** mais rápido, mas empurra a decisão de qual chave usar para depois — não serve como contrato de correção.

---

## Critério de classificação: entidade vs. não-entidade

- **É entidade** quando representa um "objeto" de negócio com identidade própria e é referenciado por outras coisas como origem/pai (mesmo que dependente — caso de entidade fraca).
- **Não é entidade** quando é: histórico de mudança de estado de uma entidade já existente; artefato derivado de outras entidades *sem* identidade própria; construção de apresentação/agrupamento; evento comportamental de alta frequência sem identidade de negócio; ou processo de outro domínio de negócio.
- Ter conteúdo derivado (ex.: valor copiado de outra entidade) **não** desqualifica algo de ser entidade — o que importa é ter identidade própria persistente. Corrigido durante a validação: Recibo e Estoque foram reclassificados de "não-entidade" para entidade por esse motivo.

---

## Entidades (13)

| Entidade | Stream de origem | Por que é entidade |
|----------|-------------------|---------------------|
| Usuário | `mssql/users` (absorve `mongodb/users`) | Identidade própria, referenciado como pai por Pedido e Incidente |
| Restaurante | `mysql/restaurants` | Identidade própria, referenciado por Produto, Pedido, Avaliação, Estoque |
| Produto | `mysql/products` | Identidade própria, referenciado por Item de Pedido, Estoque |
| Motorista | `postgres/drivers` | Identidade própria, referenciado por Turno e Entrega (não estava na lista original do `plan.md` — incluído por decisão do usuário, já que a lista era planejamento, não fechada) |
| Pedido | `kafka/orders` | Entidade central da transação |
| Item de Pedido | `mongodb/items` | Entidade fraca — só existe no contexto de um Pedido |
| Pagamento | `kafka/payments` | Identidade própria, referenciado por Recibo |
| Entrega | `kafka/route` | Identidade própria, liga Pedido + Motorista |
| Avaliação | `mysql/ratings` | Identidade própria — entidade incompleta hoje (ver gap estrutural) |
| Recibo | `kafka/receipts` | Documento com identidade própria (`receipt_id`); conteúdo derivado não desqualifica entidade |
| Estoque | `postgres/inventory` | Entidade associativa entre Restaurante e Produto, com atributo próprio (quantidade) |
| Turno | `kafka/shift` | Entidade fraca de Motorista — motorista tem vários turnos ao longo do tempo, embarcar como atributo perderia histórico |
| Incidente | `mongodb/support` | Reclamação/ocorrência ligada a um pedido específico (categorias: atraso, item errado, item faltando, pagamento — `order_id` obrigatório em todo registro); não é atendimento genérico |

## Não-entidades (7)

| Stream | Categoria | Motivo |
|--------|-----------|--------|
| `kafka/status` | Histórico de estado | Subentidade de Pedido — evolução de status ao longo do tempo, não objeto novo |
| `kafka/events` | Histórico de estado | Subentidade de Pagamento — state machine `created→authorized→captured→(succeeded\|refunded)→settled/closed` |
| `mysql/menu` | Construção de apresentação | Agrupamento de exibição de Produto, sem identidade de negócio própria |
| `kafka/gps` | Telemetria de alta frequência | Ping de localização já corretamente vinculado à Entrega (fork key = order_id via `kafka/route`); cardinalidade altíssima, sem identidade de negócio |
| `mongodb/recommendations` | Evento comportamental | Log de interação (view/click/add_to_cart), não entidade de negócio |
| `kafka/search` | Evento comportamental | Log de busca, mesma lógica |
| `mongodb/users` | Fonte secundária da mesma entidade | Não é entidade separada — absorvida por Usuário no modelo-alvo; deixa de existir como fonte separada |

---

## Relacionamentos e cardinalidade (modelo-alvo)

| Entidade | Relaciona-se com | Cardinalidade | Chave-alvo | Observação / gap |
|----------|-------------------|----------------|------------|-------------------|
| Usuário | Pedido | 1:N | `user_id` | absorve mongodb/users; cpf/email/endereço viram atributos |
| Usuário | Incidente | 1:N | `user_id` | |
| Restaurante | Produto | 1:N | `restaurant_id` | cnpj vira atributo |
| Restaurante | Pedido | 1:N | `restaurant_id` | hoje pedido usa `cnpj` (restaurant_key) — a corrigir |
| Restaurante | Avaliação | 1:N | `restaurant_id` | hoje avaliação usa `cnpj` (restaurant_identifier) — a corrigir |
| Restaurante ↔ Produto | Estoque | N:N (via Estoque) | `restaurant_id` + `product_id` | Estoque é entidade associativa |
| Produto | Item de Pedido | 1:N | `product_id` | **bug:** item de pedido gera product_id próprio (`PRD-####`, 4 díg.) em vez de referenciar Produto (`PRD-#####`, 5 díg.) |
| Motorista | Turno | 1:N | `driver_id` | |
| Motorista | Entrega | 1:N | `driver_id` | |
| Pedido | Item de Pedido | 1:N | `order_id` | |
| Pedido | Pagamento | 1:1 | `order_id` / `payment_id` | **bug:** `payment_key` do pedido é UUID aleatório, não referencia pagamento real |
| Pedido | Recibo | 1:1 | `order_id` | |
| Pedido | Entrega | 1:1 | `order_id` | rota não referencia coordenadas reais (ver gap estrutural) |
| Pedido | Incidente | 1:N | `order_id` | |
| Pedido | *(histórico) Status do Pedido* | 1:N | `order_id` | subentidade, não linha própria |
| Pagamento | Recibo | 1:1 | `payment_id` | |
| Pagamento | *(histórico) Eventos do Pagamento* | 1:N | `payment_id` | subentidade |
| Avaliação | Usuário / Pedido | — | — | **gap estrutural não resolvido** — ver seção própria |

### Decisão de chave canônica

Nos 3 casos de chave dupla (Usuário, Restaurante, Motorista), **o ID técnico sequencial vence** como chave-alvo de junção (`user_id`, `restaurant_id`, `driver_id`). CPF, CNPJ e license_number **não são eliminados** — continuam existindo como atributos normais da entidade, só deixam de ser usados como chave de relacionamento.

---

## Correções mecânicas estabelecidas (Grupo 1 — resolução definitiva)

| Bug | Correção estabelecida |
|-----|------------------------|
| `kafka/orders.payment_key` gera UUID aleatório | Deve fazer lookup em `kafka/payments.payment_id` |
| `mongodb/items.product_id` gera string própria (`PRD-####`, 4 dígitos) | Deve fazer lookup em `mysql/products.product_id` (formato `PRD-#####`, 5 dígitos) |

## Gaps estruturais — não resolvidos nesta feature (Grupo 2)

| Gap | Entidades envolvidas | Por que não resolvido aqui |
|-----|------------------------|------------------------------|
| Entrega sem coordenada real (`kafka/route` lat/lon são aleatórios, não ligados a Restaurante/Usuário) | Entrega, Restaurante, Usuário | Exige atributo novo de geolocalização — fora do escopo "só conceitual" desta feature |
| Avaliação sem ligação a Usuário/Pedido | Avaliação, Usuário, Pedido | Exige decisão de regra de negócio (toda avaliação requer um pedido? pode existir sem?) — não é só correção de chave |

**Encaminhamento:** ambos entram como discovery obrigatório na próxima feature (correção de integridade referencial do Shadow Traffic).

---

## Features removidas / reclassificadas (YAGNI)

| Item | Decisão | Razão |
|------|---------|-------|
| `mysql/menu` | Fora do modelo core | Construção de apresentação, sem identidade de negócio |
| `mongodb/recommendations` | Fora do modelo core | Evento comportamental, não entidade |
| `kafka/search` | Fora do modelo core | Evento comportamental, não entidade |
| `kafka/gps` | Fora do modelo core (telemetria de Entrega) | Sem identidade de negócio, cardinalidade altíssima |
| `kafka/status`, `kafka/events` | Subentidade/histórico, não linha própria | São a evolução de estado de Pedido/Pagamento, não objetos novos |
| `mongodb/users` | Absorvida por Usuário, eliminada como fonte separada | Mesma entidade, apenas segunda fonte de atributos |
| `postgres/inventory` (Estoque) | **Incluída** (reclassificada de "não-entidade") | Tem identidade própria (`stock_id`) — entidade associativa Restaurante↔Produto |
| `kafka/receipts` (Recibo) | **Incluída** (reclassificada de "não-entidade") | Documento com identidade própria; conteúdo derivado não desqualifica entidade |
| `postgres/drivers` (Motorista) | **Incluída** (não estava no `plan.md` original) | `plan.md` é planejamento, não lista fechada; comporta-se como entidade real |
| `kafka/shift` (Turno) | **Incluída como entidade fraca** (não embarcada como atributo) | Motorista tem múltiplos turnos ao longo do tempo — embarcar como atributo perderia histórico |
| `mongodb/support` (Incidente) | **Incluída**, renomeada de "Ticket de Suporte" para "Incidente" | Conteúdo real é focado em falha de cumprimento de pedido (4 de 5 categorias), não atendimento genérico; `order_id` obrigatório em todo registro |

---

## Draft Requirements para /define

1. Documentar as 13 entidades do domínio Uber Eats com relacionamento, cardinalidade e chave-alvo canônica (ID técnico, não chave natural).
2. Estabelecer CPF/CNPJ/license_number como atributos, não chaves de junção, em todo o domínio.
3. Registrar os 2 bugs de integridade referencial (payment_key, product_id) como itens de correção mecânica para a próxima feature.
4. Registrar os 2 gaps estruturais (geolocalização da Entrega, ligação de Avaliação) como discovery obrigatório da próxima feature, sem propor solução de atributo/regra de negócio aqui.
5. Reaproveitar este modelo, sem alteração, nas 3 arquiteturas (Warehouse, Lakehouse, Kappa) e 3 clouds (Azure, AWS, GCP) do roadmap em `docs/plan.md`.

---

## Status: ✅ Shipped

**Revisão:** Arquivado após `/ship` concluído — ver `SHIPPED_2026-08-24.md` nesta mesma pasta.
