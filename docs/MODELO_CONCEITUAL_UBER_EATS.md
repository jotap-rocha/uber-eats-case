# Modelo Conceitual do Domínio — Uber Eats

> Fonte: BRAINSTORM/DEFINE/DESIGN em [`.claude/sdd/features/BRAINSTORM_MODELO_CONCEITUAL_UBER_EATS.md`](../.claude/sdd/features/BRAINSTORM_MODELO_CONCEITUAL_UBER_EATS.md), [`DEFINE_MODELO_CONCEITUAL_UBER_EATS.md`](../.claude/sdd/features/DEFINE_MODELO_CONCEITUAL_UBER_EATS.md) e [`DESIGN_MODELO_CONCEITUAL_UBER_EATS.md`](../.claude/sdd/features/DESIGN_MODELO_CONCEITUAL_UBER_EATS.md).
>
> Reaproveitado sem alteração nas 3 arquiteturas (Warehouse, Lakehouse, Kappa) × 3 clouds (Azure, AWS, GCP) do roadmap em [`docs/plan.md`](plan.md) — Fase 0.
>
> Fonte única de dados: `gen/minio/uber-eats.json` (20 streams simulando Postgres, MySQL, MongoDB e Kafka).

---

## Entidades (13)

| Entidade | Stream de origem | Por que é entidade |
|----------|-------------------|---------------------|
| Usuário | `mssql/users` (absorve `mongodb/users`) | Identidade própria, referenciado como pai por Pedido e Incidente |
| Restaurante | `mysql/restaurants` | Identidade própria, referenciado por Produto, Pedido, Avaliação, Estoque |
| Produto | `mysql/products` | Identidade própria, referenciado por Item de Pedido, Estoque |
| Motorista | `postgres/drivers` | Identidade própria, referenciado por Turno e Entrega (não estava na lista original de 8 entidades do `plan.md` — incluído por decisão explícita, já que a lista era planejamento, não fechada) |
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

### Streams fora do modelo core (7)

| Stream | Categoria | Motivo |
|--------|-----------|--------|
| `kafka/status` | Histórico de estado | Subentidade de Pedido — evolução de status ao longo do tempo, não objeto novo |
| `kafka/events` | Histórico de estado | Subentidade de Pagamento — state machine `created→authorized→captured→(succeeded\|refunded)→settled/closed` |
| `mysql/menu` | Construção de apresentação | Agrupamento de exibição de Produto, sem identidade de negócio própria |
| `kafka/gps` | Telemetria de alta frequência | Já corretamente vinculado à Entrega (fork key = order_id via `kafka/route`); cardinalidade altíssima, sem identidade de negócio |
| `mongodb/recommendations` | Evento comportamental | Log de interação (view/click/add_to_cart), não entidade de negócio |
| `kafka/search` | Evento comportamental | Log de busca, mesma lógica |
| `mongodb/users` | Fonte secundária da mesma entidade | Absorvida por Usuário no modelo-alvo; deixa de existir como fonte separada |

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

---

## Decisão de chave canônica

Nos 3 casos de chave dupla (Usuário, Restaurante, Motorista), **o ID técnico sequencial vence** como chave-alvo de junção (`user_id`, `restaurant_id`, `driver_id`).

CPF, CNPJ e license_number **não são eliminados** — continuam existindo como atributos normais da entidade, só deixam de ser usados como chave de relacionamento. Motivo: CPF é PII sensível e não deveria se propagar como FK por todo o domínio; IDs técnicos são estáveis e não variam de formato entre fontes.

---

## Bugs mecânicos (correção definida)

| Bug | De (estado atual) | Para (correção) |
|-----|---------------------|-------------------|
| `kafka/orders.payment_key` | Gera UUID aleatório, não referencia nenhum pagamento real | Fazer lookup em `kafka/payments.payment_id` |
| `mongodb/items.product_id` | Gera string própria (`PRD-####`, 4 dígitos), nunca bate com Produto | Fazer lookup em `mysql/products.product_id` (formato `PRD-#####`, 5 dígitos) |

---

## Gaps estruturais (discovery obrigatório da próxima feature)

| Gap | Entidades envolvidas | Por que não resolvido aqui |
|-----|------------------------|------------------------------|
| Entrega sem coordenada real (`kafka/route` lat/lon são aleatórios, não ligados a Restaurante/Usuário) | Entrega, Restaurante, Usuário | Exige atributo novo de geolocalização — fora do escopo "só conceitual" desta feature |
| Avaliação sem ligação a Usuário/Pedido | Avaliação, Usuário, Pedido | Exige decisão de regra de negócio (toda avaliação requer um pedido? pode existir sem?) — não é só correção de chave |

**Encaminhamento:** ambos entram como discovery obrigatório na próxima feature (correção de integridade referencial do Shadow Traffic).

---

## Histórico do processo

Ciclo completo SDD (Brainstorm → Define → Design → Build) documentado em `.claude/sdd/features/*_MODELO_CONCEITUAL_UBER_EATS.md`. Consulte o BRAINSTORM para o detalhamento das perguntas de descoberta, abordagens exploradas e YAGNI aplicado.
