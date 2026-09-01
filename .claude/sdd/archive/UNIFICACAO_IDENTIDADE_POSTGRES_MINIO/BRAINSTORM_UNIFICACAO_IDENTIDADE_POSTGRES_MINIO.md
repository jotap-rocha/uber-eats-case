# BRAINSTORM: Unificação de Identidade Postgres×MinIO (Onda 2)

| Campo | Valor |
|-------|-------|
| **Feature** | UNIFICACAO_IDENTIDADE_POSTGRES_MINIO |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/plan.md`) |
| **Depende de** | `INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC` (Onda 1, código pronto, validação de integração pendente) |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-08-24 |

---

## Ideia inicial

A Onda 1 corrigiu tudo que era resolvível só dentro do MinIO simulado, mas deixou registrado (em `docs/MODELO_CONCEITUAL_UBER_EATS.md`) que existem **duas populações desconectadas** de Usuário e Motorista: o Postgres real (via Airbyte CDC, chave UUID) e o MinIO simulado (usado por `kafka/orders` e outros streams, chave int sequencial). O risco técnico que impediu resolver isso na Onda 1 — se o ShadowTraffic suporta lookup cruzado entre uma conexão Postgres e uma conexão MinIO/S3 no mesmo config — foi **investigado e confirmado** na documentação oficial antes de abrir esta feature.

---

## Achado técnico que desbloqueou esta feature

Consultei `docs.shadowtraffic.io` (fontes ao final) e confirmei:

- O `_gen: lookup` funciona **entre tipos de conexão diferentes** dentro do mesmo config — a doc oficial mostra o exemplo exato do nosso caso (gerador Postgres `customers` referenciado por lookup a partir de um gerador Kafka `purchases`).
- Um único config pode definir múltiplas `connections` (ex.: `postgres` + `minio`), e cada gerador escolhe explicitamente qual usar via um campo `"connection"`.
- A ordem de disponibilidade para lookup é resolvida por **dependência em tempo de execução** ("eventos só ficam disponíveis pra lookup depois de escritos com sucesso"), não pela posição no array do config — o que também confirma retroativamente que a correção da Onda 1 (`mysql/ratings` referenciando `kafka/orders`, que aparece depois no arquivo) é segura.
- **Implicação de infraestrutura:** o lookup só enxerga o que o **mesmo processo/run** do ShadowTraffic gerou. Hoje `gen-drivers`, `gen-users` e `gen-minio` são 3 containers Docker independentes (`docker-compose.yml`) — para o lookup cruzado funcionar, os 3 precisam virar **um único gerador/processo**.

Fontes: [Lookup | ShadowTraffic](https://docs.shadowtraffic.io/functions/lookup/), [Overview | ShadowTraffic](https://docs.shadowtraffic.io/overview/)

---

## Discovery Questions & Answers

| # | Pergunta | Resposta | Impacto |
|---|----------|----------|---------|
| 1 | Consolidar os 3 containers geradores num único processo? | Sim — é a única forma confirmada de ter lookup cruzado real | `docker-compose.yml` perde `gen-drivers`/`gen-users`/`gen-minio` separados, ganha 1 serviço unificado |
| 2 | O que mais entra além de ligar Usuário/Motorista ao Postgres real? | Coordenada de destino da Entrega (Onda 1 deixou pendente) + reconciliar `silver_drivers_profile`×`silver_drivers_performance` numa única dimensão de motorista | Escopo cobre os 4 itens pendentes documentados na Onda 1 |
| 3 | A chave canônica de Usuário/Motorista deve ser o UUID que o Postgres real já usa, ou migrar o schema real para int sequencial? | **Migrar para int sequencial** — o usuário priorizou consistência de estilo com Restaurante sobre não mexer no schema existente | `sql/create_users_table.sql`, `create_drivers_table.sql` e os templates do gerador Postgres mudam de `_gen: uuid` para `_gen: sequentialInteger`; dados já carregados nas tabelas reais precisam ser regerados (mudança de tipo de PK) |
| 4 | Estratégia de entrega: tudo de uma vez, ou validar a unificação isolada primeiro? | Tudo de uma vez — a documentação oficial já traz um exemplo prático idêntico ao nosso caso, reduzindo a incerteza que justificou faseamento na Onda 1 | Uma única feature cobre unificação + migração de PK + redirecionamento de consumidores + geo destino + reconciliação de motorista |

---

## Sample Data Inventory

| Tipo | Localização | Relevância |
|------|-------------|------------|
| Templates do gerador Postgres real | `gen/postgres/users.json.template`, `drivers.json.template` | Confirmam `user_id`/`driver_id` como `_gen: uuid`; população totalmente independente do MinIO |
| DDL Postgres real | `sql/create_users_table.sql`, `create_drivers_table.sql` | Confirmam PK `uuid`; sem campo CPF em `users` |
| Orquestração | `docker-compose.yml` (serviços `gen-drivers`, `gen-users`, `gen-minio`) | Confirma 3 processos independentes hoje — ponto central a mudar |
| Gerador MinIO | `gen/minio/uber-eats.json` (já ajustado na Onda 1) | Vai ganhar a `connection: postgres` e os lookups cruzados |
| Silver motorista | `pipeline/silver/ingestion_postgres_profile.sql` (`silver_drivers_profile`, hoje MinIO), `ingestion_ods_postgres_performance.sql` (`silver_drivers_performance`, hoje Postgres real) | As duas tabelas a reconciliar |
| Documentação ShadowTraffic | `docs.shadowtraffic.io/functions/lookup/`, `/overview/` | Confirma viabilidade técnica e sintaxe exata |

---

## Abordagens exploradas

### Abordagem A: Unificação completa numa feature só ⭐ Recomendado (escolhido)

**O que faz:** consolida os 3 geradores, migra o schema real de UUID para sequencial, redireciona todos os consumidores MinIO, corrige o destino da Entrega e reconcilia a dimensão de motorista — tudo nesta feature.

**Por que escolhido:** a documentação oficial do ShadowTraffic já mostra um exemplo prático idêntico ao nosso caso de uso (Postgres→Kafka lookup), reduzindo a incerteza que motivou o faseamento da Onda 1. O risco técnico central já foi verificado antes de abrir a feature.

### Abordagem B: Validar unificação isolada primeiro (rejeitada)

**O que faz:** rodaria só a mudança de gerador (sem tocar Silver/Gold/schema real) para confirmar o lookup cruzado neste ambiente específico, antes de comprometer o restante do escopo.

**Por que rejeitada:** o risco que essa cautela mitigava (incerteza sobre a capacidade do ShadowTraffic) já foi resolvido via documentação oficial com exemplo prático equivalente — o custo adicional de uma etapa de validação isolada não se justifica mais.

---

## Escopo desta feature

| Item | Ação |
|------|------|
| Infraestrutura | Consolidar `gen-drivers` + `gen-users` + `gen-minio` (3 containers) em 1 gerador unificado, com `connections: postgres` + `minio` |
| Schema real | Migrar `sql/create_users_table.sql` e `create_drivers_table.sql`: PK de `uuid` para `int`/sequencial |
| Templates do gerador Postgres | `gen/postgres/users.json.template`, `drivers.json.template`: `user_id`/`driver_id` de `_gen: uuid` para `_gen: sequentialInteger` |
| Gerador unificado | `kafka/orders.user_key`/`driver_key` e demais consumidores MinIO (`mongodb/support`, `kafka/shift`, `kafka/route`, etc.) passam a fazer lookup no Postgres real via `connection: postgres` |
| Aposentar | `mssql/users`, `mongodb/users`, `postgres/drivers` (streams MinIO simulados) — Usuário e Motorista passam a ter fonte única |
| Entrega — destino | `kafka/route.end_lat/end_lon` vira lookup no `lat`/`lon` real do Usuário (Postgres) |
| Motorista — dimensão única | Reconciliar `silver_drivers_profile` (hoje MinIO) e `silver_drivers_performance` (hoje Postgres real) numa única tabela Silver, agora que os IDs batem |
| Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Refletir o estado final — modelo totalmente consistente, sem pendência conhecida |

## Fora de escopo

- Qualquer coisa já resolvida na Onda 1 (bugs mecânicos, chave de Restaurante, Avaliação→Pedido, origem da Entrega) — não revisitar
- Novas entidades, novos relatórios Gold, novas regras de negócio além do que já está documentado como pendência
- Ligar a origem da Entrega ao restaurante *exato* do pedido (limitação de lookup em 2 níveis, registrada na Onda 1 como possível Onda 3, não parte desta feature)

## YAGNI aplicado

- Não construir um "serviço de resolução de identidade" genérico — só a migração concreta necessária para este domínio.
- Não reabrir a decisão de chave canônica de Restaurante (já resolvida na Onda 1, sem problema).

---

## Draft Requirements para /define

1. Consolidar os 3 containers geradores num único serviço Docker/config ShadowTraffic com `connections: postgres` + `minio`.
2. Migrar `sql/create_users_table.sql`/`create_drivers_table.sql` e os templates do gerador Postgres de UUID para int sequencial.
3. Redirecionar `kafka/orders.user_key`/`driver_key` e todo consumidor MinIO de usuário/motorista para o Postgres real unificado.
4. Aposentar `mssql/users`, `mongodb/users`, `postgres/drivers` (MinIO) do gerador.
5. Corrigir `kafka/route.end_lat/end_lon` para lookup no Usuário real.
6. Reconciliar `silver_drivers_profile` e `silver_drivers_performance` numa única dimensão de motorista no Silver.
7. Regenerar dados e validar com join real no Gold (Databricks) que todos os relacionamentos — incluindo os desta Onda — retornam resultado consistente, sem órfãos.
8. Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` refletindo o estado final, sem pendências conhecidas.

---

## Status: ✅ Shipped

**Revisão:** Status atualizado após `/define` concluído com sucesso — ver `.claude/sdd/features/DEFINE_UNIFICACAO_IDENTIDADE_POSTGRES_MINIO.md`.
Shipped e arquivado em 2026-09-01.
