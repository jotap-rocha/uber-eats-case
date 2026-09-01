# BRAINSTORM: Correção de Integridade Referencial do Shadow Traffic (Onda 1)

| Campo | Valor |
|-------|-------|
| **Feature** | INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/plan.md`) |
| **Depende de** | `MODELO_CONCEITUAL_UBER_EATS` (shipped) |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-08-24 |

---

## Ideia inicial

O `docs/MODELO_CONCEITUAL_UBER_EATS.md` (feature anterior, já shippada) documentou 2 bugs mecânicos, 1 decisão de chave canônica e 2 gaps estruturais no gerador Shadow Traffic (`gen/minio/uber-eats.json`). Esta feature corrige esses problemas de fato — dentro do escopo que é seguro resolver sem depender de uma reconciliação maior ainda não verificada tecnicamente.

---

## Decisões de escopo

| # | Decisão | Resposta |
|---|---------|----------|
| 1 | Quais dos 3 grupos de problema do modelo entram nesta feature? | Todos os 3 grupos foram considerados (bugs mecânicos, migração de chave, gaps estruturais), mas a análise revelou uma dependência técnica que exigiu dividir em ondas (ver #3). |
| 2 | Achado durante a exploração: existem 2 populações desconectadas de Usuário/Motorista (Postgres real via Airbyte CDC, UUID, sem CPF — vs. MinIO simulado, int sequencial, usado por `kafka/orders`) | Confirmado como achado real ao ler o pipeline Silver/Gold (`pipeline/bronze/ingest_postgres_users.sql`, `pipeline/silver/ingestion_postgres_profile.sql`, `pipeline/gold/load_user_financial_behavior.sql`). O join pedido→usuário e pedido→motorista no Gold não funciona hoje mesmo corrigindo só o MinIO. |
| 3 | Como abordar o risco técnico não verificado (ShadowTraffic suporta lookup cruzado entre configs Postgres e MinIO)? | **2 ondas.** Onda 1 (esta feature): tudo resolvível só dentro do MinIO. Onda 2 (próxima feature): unificação Postgres×MinIO, depois de confirmar viabilidade técnica. |
| 4 | O que fazer com o registro do modelo conceitual ao final? | `docs/MODELO_CONCEITUAL_UBER_EATS.md` **deve** ser atualizado no Build desta feature para refletir o estado real implementado + o que ainda está pendente (Onda 2) — o usuário vai passar esse documento para outro agente desenhar no Miro, então precisa ficar sempre fiel à realidade. |

---

## Discovery Questions & Answers

| # | Pergunta | Resposta | Impacto |
|---|----------|----------|---------|
| 1 | Como corrigir a Entrega sem coordenada real, dado que Restaurante/Usuário não tinham lat/lon? | Adicionar lat/lon a Restaurante e Usuário — **revisado depois**: Usuário já tem lat/lon no Postgres real (achado durante exploração), só Restaurante precisa ganhar o atributo novo. | Só o ponto de partida (Restaurante) é corrigido nesta feature; o destino (Usuário) fica para Onda 2. |
| 2 | Avaliação deve exigir um pedido específico, ou pode existir sem? | Exigir pedido — `rating_id` → lookup obrigatório em `kafka/orders.order_id`; Usuário/Restaurante vêm transitivamente do pedido. | Elimina a necessidade de `restaurant_identifier` direto em `mysql/ratings`. |
| 3 | O "pronto" inclui regerar os dados e validar com join real, ou só a correção do gerador? | Inclui regerar e validar — mas o join de validação será feito no **Databricks** (carregar dados corrigidos, ajustar colunas na Silver, testar join na Gold), não numa query solta no MinIO. | Muda a estratégia de verificação: exige rodar o pipeline Silver/Gold real, não só uma query ad-hoc. |

---

## Sample Data Inventory

| Tipo | Localização | Relevância |
|------|-------------|------------|
| Gerador Shadow Traffic (MinIO) | `gen/minio/uber-eats.json` | Alvo direto das correções desta feature |
| Bronze real Postgres | `pipeline/bronze/ingest_postgres_users.sql`, `ingest_postgres_drivers.sql` | Revelou a existência da população Postgres real (CDC via Airbyte, `uber_eats.raw.*`) |
| Silver real Postgres | `pipeline/silver/ingestion_postgres_users.sql` (`silver_postgres_users`), `ingestion_postgres_profile.sql` (`silver_drivers_profile`, na verdade lê `live.postgres_drivers` — bronze MinIO, não `ods_postgres_drivers`), `ingestion_ods_postgres_performance.sql` (`silver_drivers_performance`, essa sim de `ods_postgres_drivers` real) | Confirmou a duplicidade de fontes para Motorista |
| Silver dos streams MinIO afetados | `pipeline/silver/ingestion_kafka_orders.sql`, `ingestion_kafka_ratings.sql`, `ingestion_kafka_route.sql`, `ingestion_mongodb_items.sql`, `ingestion_mysql_restaurants.sql` | Mostra os nomes de coluna atuais (`cpf_usuario`, `cnpj_restaurante`) que precisarão de ajuste |
| Gold | `pipeline/gold/load_order_unit_economics.sql`, `load_restaurant_performance.sql`, `load_user_financial_behavior.sql` | Confirmou que hoje não há join pedido↔usuário nem pedido↔motorista real; join pedido↔restaurante existe via `cnpj` |

---

## Abordagens exploradas

### Abordagem A: Tudo de uma vez (rejeitada)

**O que faz:** resolve bugs mecânicos, migração de chave, gaps estruturais e unificação Postgres×MinIO numa única feature.

**Por que rejeitada:** a unificação Postgres×MinIO depende de uma capacidade do ShadowTraffic ainda não verificada (lookup cruzado entre dois configs de geração independentes). Se não for viável como imaginado, a feature inteira trava, mesmo as partes que já estariam prontas.

### Abordagem B: Duas ondas ⭐ Recomendado (escolhido)

**O que faz:** Onda 1 (esta feature) resolve tudo que é seguro dentro do MinIO — não depende de nenhuma capacidade técnica não verificada. Onda 2 (próxima feature) ataca a unificação Postgres×MinIO, com a viabilidade técnica investigada antes de comprometer o escopo.

**Por que escolhido:** entrega valor real e testável agora, sem risco de bloqueio total; isola a incerteza técnica numa feature própria, onde pode ser investigada com foco.

---

## Escopo desta feature (Onda 1)

| Item | Ação |
|------|------|
| `kafka/orders.payment_key` (UUID aleatório) | Corrigir → lookup em `kafka/payments.payment_id` |
| `mongodb/items.product_id` (formato incompatível, 4 dígitos) | Corrigir → lookup em `mysql/products.product_id` (formato correto, 5 dígitos) |
| Restaurante: chave dupla `cnpj` vs `restaurant_id` | Migrar para `restaurant_id` em `kafka/orders.restaurant_key` e `mysql/ratings.restaurant_identifier` |
| Avaliação sem ligação a Usuário/Pedido | `mysql/ratings` ganha lookup obrigatório em `kafka/orders.order_id`; remove `restaurant_identifier` direto (vem transitivamente do pedido) |
| Entrega sem coordenada — ponto de partida | Adicionar `lat`/`lon` a `mysql/restaurants`; `kafka/route.start_lat/lon` vira lookup |
| Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Refletir o estado real pós-Build desta feature + o que fica pendente pra Onda 2 (requisito explícito do usuário — o documento alimenta a criação de um diagrama no Miro por outro agente) |

## Fora de escopo (Onda 2 — feature futura)

| Item | Por que fica para depois |
|------|-----------------------------|
| Usuário/Motorista: migrar `cpf`/`license_number` para o UUID do Postgres real | Depende de unificar a geração Postgres×MinIO — risco técnico não verificado |
| Aposentar `mssql/users`, `mongodb/users`, `postgres/drivers` (MinIO) | Mesma dependência acima |
| Entrega — coordenada de destino (Usuário) | Usuário só tem `lat`/`lon` real no Postgres, que é trabalho de Onda 2 |
| Reconciliar `silver_drivers_profile` (MinIO) com `silver_drivers_performance` (Postgres real) | Mesma dependência de unificação |

## YAGNI aplicado

- Não vamos investigar ou implementar a unificação Postgres×MinIO nesta feature — vira discovery obrigatório da próxima (Onda 2), evitando comprometer prazo/escopo com uma incerteza técnica não resolvida.
- Não vamos mexer em `kafka/status`, `kafka/events` (subentidades/histórico) nem nos streams já classificados fora do modelo core (`mysql/menu`, `mongodb/recommendations`, `kafka/search`) — nada disso tem bug ou gap registrado.

---

## Draft Requirements para /define

1. Corrigir `payment_key` e `product_id` no gerador (`gen/minio/uber-eats.json`) com lookup correto.
2. Migrar Restaurante para `restaurant_id` como chave de junção em `kafka/orders` e `mysql/ratings`.
3. Adicionar lookup obrigatório de `mysql/ratings` para `kafka/orders.order_id`; remover referência direta a restaurante.
4. Adicionar `lat`/`lon` a `mysql/restaurants`; corrigir `kafka/route.start_lat/lon` para lookup real.
5. Regerar os dados (Shadow Traffic) com o gerador corrigido.
6. Ajustar as colunas afetadas na camada Silver (`ingestion_kafka_orders.sql`, `ingestion_kafka_ratings.sql`, `ingestion_kafka_route.sql`, `ingestion_mysql_restaurants.sql`, `ingestion_mongodb_items.sql`) para refletir os novos nomes/chaves.
7. Validar com join real na camada Gold (Databricks) que os relacionamentos corrigidos retornam resultado consistente, sem órfãos.
8. Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` com o estado real pós-Build e o que fica pendente para Onda 2.

---

## Status: ✅ Shipped

**Revisão:** Status atualizado após `/define` concluído com sucesso — ver `.claude/sdd/features/DEFINE_INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC.md`.
Shipped e arquivado em 2026-09-01.
