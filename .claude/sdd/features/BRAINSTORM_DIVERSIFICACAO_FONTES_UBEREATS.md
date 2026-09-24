# BRAINSTORM: Diversificação de Fontes de Dados (Onda 3)

| Campo | Valor |
|-------|-------|
| **Feature** | DIVERSIFICACAO_FONTES_UBEREATS |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`), Onda 3 |
| **Depende de** | `INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC` (Onda 1, shipped), `UNIFICACAO_IDENTIDADE_POSTGRES_MINIO` (Onda 2, shipped) |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-04 |

---

## Ideia inicial

As Ondas 1 e 2 corrigiram a integridade referencial dentro do MinIO e unificaram Usuário/Motorista no Postgres real, mas o projeto continuava com só 2 sistemas de origem (Postgres real + MinIO simulado), e nenhuma tabela do Postgres tinha um domínio de negócio claramente atribuído. O usuário queria evoluir para múltiplos sistemas de origem heterogêneos — inicialmente cogitou Oracle, um NoSQL e "outro MinIO" — para: (1) diversificar tecnologias praticadas no portfólio, e (2) dar a cada sistema um domínio de negócio coerente, não entidades soltas.

O brainstorm foi conduzido em várias rodadas via `/intake` (com `@medallion-architect` e `@databricks-data-engineer`) antes de ser formalizado neste documento via `/brainstorm`.

---

## Decisões de escopo

| # | Decisão | Resposta |
|---|---------|----------|
| 1 | Segundo MinIO representando outro datalake? | **Descartado.** O usuário esclareceu que "MinIO" no pedido original se referia ao já existente, não a um segundo. Redundante com os 3 datalakes reais que as Fases 1-3 do roadmap já entregam (ADLS Gen2, S3, GCS) |
| 2 | NoSQL — precisa ser MongoDB "de verdade" com dado vivo? | **Não.** MongoDB pode ficar com cadastro estático — decisivo porque o ShadowTraffic **não tem sink de escrita para MongoDB** (só Redis/KurrentDB gravam NoSQL); dado vivo exigiria componente de replicação extra fora do processo único |
| 3 | Usuário topa criar entidades novas fora das 13 já modeladas? | **Sim** — "estava esperando por isso". Libera modelar satélites documentais (ex. "Perfil de Restaurante") |
| 4 | Nome das tabelas do medalhão pode mudar? | **Sim** — Silver passa a nomear por **domínio de negócio** (`silver_orders`), não mais por sistema de origem (`silver_kafka_orders`). Barateia trocas de fonte futuras |
| 5 | Oracle precisa ter CDC ativo (não incremental por cursor)? | **Sim.** Descoberto que o conector Oracle CDC do Airbyte é `source-oracle-enterprise` (pago). Decisão: usar **Debezium/Kafka Connect** para o Oracle — novo componente de infraestrutura, mas CDC real e reaproveitável nas fases cloud futuras (ver Achado técnico) |
| 6 | Dá pra simular UPDATE/DELETE reais (não só INSERT) em Postgres/Oracle, pra CDC ficar mais fiel? | **Sim, confirmado na doc oficial do ShadowTraffic.** Campo `op: insert\|update\|delete` + mecanismo `fork`+`stateMachine` — ver Achado técnico |
| 7 | Mutação real de estado conflita com o histórico append-only já existente (`kafka/status`, `kafka/events`)? | Inicialmente avaliado como "complementa, não conflita" (regra: mesmo `stateMachine` alimentando os dois). Mas o usuário decidiu ir além: **abrir mão do histórico** — `kafka/status`/`kafka/events` foram criados sem o referencial relacional correto e já seriam descartados de qualquer forma |
| 8 | Pedido/Pagamento deveriam ir para o relacional também (não só ficar no MinIO)? | **Sim** — decisão revista durante o `/brainstorm`. Ao abrir mão do histórico, Pedido/Pagamento só conseguem expressar mudança de status via UPDATE real, então precisam estar num sistema relacional (Oracle) e entrar no escopo de mutação da v1 |
| 9 | Provar o mecanismo de mutação (`fork`+`stateMachine`) simultaneamente em Postgres e Oracle, ou um banco por vez? | **Um por vez.** Postgres primeiro (infraestrutura madura, CDC via Airbyte já funciona) isola o risco do mecanismo em si; só depois de provado se aplica o mesmo padrão já validado ao Oracle (que está sendo levantado do zero nesta mesma onda) |

---

## Achado técnico que desbloqueou/restringiu a feature

Consultado `docs.shadowtraffic.io` (conexões `postgres`/`oracle`, `stateMachine`, `fork`, `lookup`) e `docs.airbyte.com`/`docs.aws.amazon.com`/`docs.cloud.google.com` (via `/intake`, múltiplas rodadas):

- `kind: oracle` existe nativamente no ShadowTraffic desde a v0.17.0, com auto-DDL — pode entrar como uma 3ª `connection` no **mesmo processo único** do `gen-unified`, preservando o invariante que a Onda 2 resolveu (lookup só enxerga o que o mesmo processo gerou).
- **Não existe sink MongoDB** no ShadowTraffic — só Redis/KurrentDB gravam NoSQL. Qualquer entidade no Mongo precisa ser seed estático (população congelada), nunca gerada de forma independente/contínua.
- `op: insert|update|delete` funciona **de forma idêntica** em `postgres` e `oracle` — mecanismo oficial é `fork` (cria uma instância de gerador por chave, com ciclo de vida) + `stateMachine` (alterna entre os estados: `insertIt → updateIt → deleteIt`), com `where` referenciando a chave do fork para o UPDATE/DELETE acertar a linha certa. Existe caminho alternativo via `lookup` no `where` (preserva os geradores atuais), mas sem exemplo oficial — mais arriscado.
- O conector Oracle **com CDC** do Airbyte é `source-oracle-enterprise` (pago/Enterprise); o OSS só faz Full Refresh/incremental por cursor. **Debezium/Kafka Connect** roda CDC real sem essa limitação — decisão de usar esse par de ferramentas para o Oracle.
- Auto-DDL do ShadowTraffic **não cria PRIMARY KEY** — colunas-chave de entidades migradas para Postgres/Oracle precisam de `sqlHint`/`tablePolicy: manual` explícito, senão a réplica lógica falha silenciosamente ao tentar capturar UPDATE/DELETE.
- Nas fases cloud futuras (AWS/GCP, fora do escopo desta feature), os papéis de Oracle e MinIO são substituídos por serviços nativos de cada cloud (já registrado em `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` v1.2) — por isso a Bronze desta feature deve expor um contrato canônico de metadados de CDC, para a Silver não depender do formato específico do Airbyte/Debezium.

---

## Abordagens exploradas

### Abordagem A — Technology fit ⭐ Escolhida (com ajuste durante o brainstorm)

**O que faz:** cada sistema recebe o tipo de entidade em que é tecnicamente bom — cadastro de pessoas em Postgres, núcleo do modelo de negócio (com estado mutável real) em Oracle, satélite documental no Mongo, e o que é append-only por natureza no MinIO.

**Por que escolhida:** com as restrições 2-4 resolvidas (Mongo estático liberado, entidades novas autorizadas, renomeação aceita), essa é a única abordagem que dá suporte nativo a mutação real (só existe em sistema relacional) sem inventar componente de infraestrutura extra.

**Ajuste feito durante o `/brainstorm`:** a proposta original mantinha Pedido/Pagamento no MinIO (menor risco). O usuário pediu para reconsiderar — ao abrir mão do histórico append-only (`kafka/status`/`kafka/events`), Pedido/Pagamento passam a exigir mutação real para expressar status, então migram para o Oracle junto com Restaurante/Produto/Estoque.

### Abordagem B — Bounded context / DDD (rejeitada nesta rodada)

Cada sistema = um contexto delimitado (Identidade, Catálogo, Transação, Suporte). Rejeitada porque, com só 4 sistemas para 5 contextos naturais, sempre exige colapsar um contexto de forma um tanto arbitrária — a Abordagem A com o ajuste de Pedido/Pagamento chega numa alocação equivalente, mas por um critério mais objetivo (mutabilidade real).

### Abordagem C — Blast radius mínimo (descartada)

Congelar Pedido/Pagamento/Restaurante onde estão, mover só entidades de baixo risco (Estoque, Turno) para o Oracle. Descartada porque o usuário topou o risco maior em troca de um modelo mais coerente e mais fiel ao mundo real (Pedido/Pagamento como dados relacionais mutáveis é o padrão de mercado).

---

## Sequenciamento (mitigação de risco)

Given que o mecanismo de mutação nunca foi testado neste projeto e o Oracle está sendo levantado do zero, a v1 é dividida em 3 etapas, na ordem:

| Etapa | Escopo | Por que nessa ordem |
|-------|--------|----------------------|
| **1** | Postgres/Motorista: provar `fork`+`stateMachine` com `drivers.status` (+ `total_deliveries`/`total_earnings`/`average_rating`) | Infraestrutura já madura (CDC via Airbyte já funciona, `wal_level=logical` já ligado) — isola o risco do mecanismo de mutação em si |
| **2** | Oracle (plumbing): mover Restaurante/Produto/Estoque para lá (insert-only por enquanto), subir Debezium/Kafka Connect, validar CDC básico funcionando | Prova a infraestrutura nova (container, `connection` no gerador, Kafka Connect) sem somar o risco de mutação ainda não provada |
| **3** | Oracle/Pedido+Pagamento com mutação real, usando o padrão já validado na Etapa 1; retirar `kafka/status`/`kafka/events` | Só depois de mecanismo E infraestrutura provados separadamente |

---

## Sample Data Inventory

| Tipo | Localização | Relevância |
|------|-------------|------------|
| Gerador unificado atual | `gen/unified/uber-eats.json(.template)` | Alvo direto — ganha `connection: oracle`, geradores reescritos com `fork`+`stateMachine` para as entidades mutáveis |
| Modelo conceitual | `docs/MODELO_CONCEITUAL_UBER_EATS.md` | 13 entidades atuais, grafo de referência, streams fora do core (`kafka/status`, `kafka/events` a aposentar) |
| Roadmap | `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (Seção "Fase 0 — Onda 3") | Registra as decisões já fechadas antes deste `/brainstorm`; este documento formaliza e aprofunda |
| Silver atuais | `pipeline/silver/*.sql` (17 scripts) | Convenção de nome a trocar (por domínio, não por sistema); padrão de tipagem/projeção explícita a preservar |
| Bronze CDC atual | `pipeline/bronze/ingest_postgres_users.sql`, `ingest_postgres_drivers.sql` | Padrão `APPLY CHANGES INTO` + `SEQUENCE BY` já em uso — referência para o Bronze do Oracle |
| Schema Postgres | `sql/create_users_table.sql`, `create_drivers_table.sql` | Já têm PK `int` — replica identity já viável para UPDATE/DELETE |
| Docker Compose | `docker-compose.yml` | Ganha serviço(s) novos: Oracle (container) + Kafka Connect/Debezium |

---

## Escopo desta feature (Onda 3, v1)

| Item | Ação |
|------|------|
| Novo sistema: Oracle | Nova `connection: oracle` no gerador único; container novo no `docker-compose.yml`; recebe Restaurante, Produto, Estoque, Pedido, Item de Pedido, Pagamento, Recibo |
| CDC do Oracle | Debezium/Kafka Connect (novo componente); substitui o que seria um conector Airbyte pago |
| Novo sistema: MongoDB | Satélite documental "Perfil de Restaurante" (menu + horários de funcionamento), FK para `restaurant_id` (cadastro congelado no Oracle); população estática (seed único) |
| Mutação real (v1, faseada) | `drivers.status`/`total_deliveries`/`total_earnings`/`average_rating` (Etapa 1); `orders.status`, `payments.status` (Etapa 3), via `op`+`fork`+`stateMachine` |
| Retirar histórico append-only | `kafka/status` e `kafka/events` são aposentados — a mudança de status passa a ser a própria mutação da linha, capturada pelo CDC |
| Nomenclatura do medalhão | Tabelas Silver renomeadas por domínio de negócio (ex. `silver_orders`), não por sistema de origem |
| Contrato de CDC na Bronze | Colunas canônicas (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) para a Silver não depender do formato nativo de cada ferramenta de ingestão (relevante já agora — Airbyte × Debezium emitem formatos diferentes — e nas fases cloud futuras) |
| Postgres | Sem mudança de sistema — ganha só a capacidade de mutação real (Motorista) |
| MinIO | Mantém Entrega, Avaliação, Turno, Incidente + streams fora do core (GPS, search, recommendations, menu de apresentação) |
| Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` | Refletir os 4 sistemas, a entidade nova (Perfil de Restaurante), a aposentadoria de `kafka/status`/`kafka/events`, e o estado real pós-Build |

## Fora de escopo

| Item | Por que fica para depois |
|------|-----------------------------|
| Segundo MinIO/datalake | Descartado definitivamente — redundante com os datalakes reais das Fases 1-3 |
| MongoDB com dado vivo/mutável | ShadowTraffic não tem sink de escrita para Mongo; exigiria componente de replicação fora do processo único, não justificado nesta v1 |
| Mutação de Usuário, Restaurante, Produto | Fica para uma onda futura — v1 cobre só Motorista, Pedido, Pagamento (as entidades que perdem o histórico) |
| Escolha do motor relacional nativo para AWS/GCP | Decisão do `/define` de cada fase cloud (Fase 2/3), não desta feature — já registrado no roadmap |
| Amarrar a origem da Entrega ao restaurante exato do pedido | Limitação de lookup em 2 níveis, já registrada como possível "Onda futura" desde a Onda 1 |

## YAGNI aplicado

- Não construir um segundo MinIO "só para ter 4 gavetas visualmente simétricas" — cada sistema precisa de motivo de negócio, não simetria estética.
- Não tentar dar ao MongoDB dado vivo nesta v1 — o ganho de aprendizado de "documento aninhado/schema variável" já é capturado com população estática; dado vivo é sofisticação sem retorno proporcional agora.
- Não mover Usuário/Restaurante para mutação real nesta v1 — o valor de provar o mecanismo já é obtido com Motorista, Pedido e Pagamento.
- Não fazer hard delete em nenhuma entidade-pai (Usuário, Motorista) — quebraria a integridade referencial conquistada nas Ondas 1/2; soft delete obrigatório onde delete fizer sentido.

---

## Draft Requirements para `/define`

1. Adicionar `connection: oracle` ao `gen/unified/uber-eats.json`, no mesmo processo único do `gen-unified`.
2. Migrar Restaurante, Produto, Estoque para o Oracle (Etapa 2) — insert-only nesta etapa, com `sqlHint`/`tablePolicy: manual` explícito nas colunas-chave.
3. Subir Debezium/Kafka Connect como novo serviço no `docker-compose.yml`, com CDC real sobre o Oracle.
4. Criar o satélite documental "Perfil de Restaurante" (menu + horários) no MongoDB, com FK para `restaurant_id`, população estática.
5. Reescrever os geradores `drivers` (Postgres) com `fork`+`stateMachine`, implementando `op: update` para `status`/`total_deliveries`/`total_earnings`/`average_rating` (Etapa 1 — provar o mecanismo).
6. Após a Etapa 1 validada, aplicar o mesmo padrão aos geradores de Pedido e Pagamento no Oracle (`op: update` para `status`), migrando-os do MinIO para o Oracle (Etapa 3).
7. Migrar Item de Pedido (filho de Pedido) e Recibo (filho de Pagamento) para o Oracle junto com seus pais.
8. Aposentar `kafka/status` e `kafka/events` do gerador — a mudança de status passa a ser a mutação real da linha correspondente.
9. Definir e implementar o contrato canônico de metadados de CDC na camada Bronze (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`), com um shim por ferramenta de ingestão (Airbyte, Debezium).
10. Renomear as tabelas Silver afetadas para a convenção por domínio de negócio (ex. `silver_orders`, `silver_payments`, `silver_restaurants`), atualizando os scripts Gold correspondentes.
11. Validar com join real no Gold (Databricks) que os relacionamentos cross-connection (MinIO→Oracle para Entrega/Avaliação/Incidente referenciando Pedido; Mongo→Oracle para o satélite de Restaurante) retornam resultado consistente, sem órfãos — mesma disciplina de validação das Ondas 1/2.
12. Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` com o estado final: 4 sistemas, entidade nova (Perfil de Restaurante), streams aposentados, sem pendência conhecida.

## Open Questions

- Desenho exato do gerador Oracle para Pedido (que hoje é `kafka/orders`, a entidade de maior blast radius do modelo) — detalhar no `/design`, especialmente a ordem de migração dos consumidores (Item, Pagamento, Recibo, Entrega, Incidente, Avaliação) que hoje fazem lookup nele dentro do MinIO.
- Schema exato do satélite "Perfil de Restaurante" no MongoDB (estrutura do array de menu, formato de horários) — detalhar no `/define`.
- Se a licença do ShadowTraffic (hoje expirada, pendência já registrada desde as Ondas 1/2) precisa ser renovada antes de iniciar o Build desta feature — bloqueio operacional, não de design.

---

## Status: ✅ Complete (Defined)

**Revisão:** Brainstorm conduzido em múltiplas rodadas via `/intake` e formalizado via `/brainstorm` nesta sessão. Próximo passo: `/define .claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`.
