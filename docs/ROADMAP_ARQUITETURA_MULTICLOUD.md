# Uber Eats — Roadmap de Arquiteturas de Dados Multi-Cloud

**Documento de planejamento**

**Versão:** 1.1

**Data:** Setembro/2026

> Renomeado de `docs/plan.md` para `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (v1.1) — mesmo documento, nome mais intuitivo, refletindo o próprio título. Ver "Histórico de revisões" ao final.

---

## 1. Objetivo

Implementar as arquiteturas **Warehouse**, **Lakehouse** e **Kappa**, reaproveitando o dado do projeto pessoal "Uber Eats", distribuídas nas 3 principais clouds (**Azure**, **AWS** e **GCP**) — sendo:

- **Azure**: as 3 arquiteturas completas, reaproveitando o trabalho de Lakehouse já feito com Databricks
- **AWS** e **GCP**: as 3 arquiteturas completas, usando a **stack de dados nativa** de cada cloud (sem Databricks)

**Finalidade:** fortalecer simultaneamente o conhecimento de arquitetura de dados e das 3 principais clouds, consolidando portfólio técnico para processos seletivos.

---

## 2. Premissas e princípios

| Princípio | Detalhe |
|---|---|
| Cadência | ~3h por semana, sem prazo fixo — as estimativas de tempo abaixo servem como bússola, não como compromisso |
| Abertura de conta cloud | Somente no início de cada fase correspondente, dado que os créditos de free tier têm validade curta (Azure: 30 dias; AWS: até 6 meses; GCP: 90 dias) |
| IaC / CI-CD | **Terraform** como ferramenta única de provisionamento de infraestrutura, reaproveitada nas 3 clouds. **DAB** (Databricks Asset Bundles) usado especificamente para deploy de jobs/pipelines Databricks — aplicável somente na Fase 1 (Azure) |
| Uso do Databricks | Restrito à Azure. Em AWS e GCP, o objetivo é praticar a stack de dados nativa de cada cloud (Glue/Iceberg/Athena na AWS; BigLake/Dataproc/BigQuery no GCP) |
| Gestão de custo | Responsabilidade do usuário — priorizar sempre serviços serverless/on-demand (Redshift Serverless, Synapse Serverless SQL Pool, BigQuery on-demand, Databricks com auto-termination agressivo) para evitar cobrança de recurso ligado sem uso |

---

## 3. Fases

### Fase 0 — Fundação (local, bloqueante)

| Item | Descrição | Status |
|---|---|---|
| Shadow Traffic — integridade referencial (Onda 1) | Corrigir integridade referencial entre os geradores simulados (MySQL, MongoDB, Kafka dentro do MinIO), garantindo que entidades-filho referenciem corretamente chaves de entidades-pai já existentes | ✅ Concluído — `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/` |
| Unificação de identidade Postgres×MinIO (Onda 2) | Migrar Usuário/Motorista para fonte única (Postgres real), PK sequencial em vez de UUID, reconciliar dimensão única de motorista | ✅ Concluído — `.claude/sdd/archive/UNIFICACAO_IDENTIDADE_POSTGRES_MINIO/` |
| Modelo conceitual | Desenhar entidades e relacionamentos do domínio Uber Eats (usuário, restaurante, produto, pedido, item de pedido, pagamento, entrega, avaliação, motorista, estoque, turno, incidente, recibo) — modelo único, reaproveitado nas 3 arquiteturas e nas 3 clouds | ✅ Concluído — `docs/MODELO_CONCEITUAL_UBER_EATS.md` |
| Diversificação de fontes (Onda 3) | Sair de 2 sistemas (Postgres real + MinIO simulado) para 4 sistemas heterogêneos, com CDC real e mutação de estado — ver subseção "Fase 0 — Onda 3" abaixo | 🔜 Planejamento (brainstorm concluído nesta sessão; falta formalizar `/define`) |
| Agentes | Carregar com conhecimento de arquitetura de dados (Warehouse, Lakehouse, Kappa, medalhão, modelagem dimensional). Conhecimento específico de cada cloud entra sob demanda, a partir da fase correspondente | Contínuo |

**Critério de saída (revisado na v1.1):** consulta de join entre as fontes de dados — hoje 2 sistemas (Postgres, MinIO), alvo de 4 (Postgres, Oracle, MongoDB, MinIO) após a Onda 3 — retorna resultado consistente, sem registros órfãos; e a mutação de estado (UPDATE/DELETE) em Postgres/Oracle é capturada corretamente pelo CDC (Airbyte para Postgres, Debezium/Kafka Connect para Oracle).

---

#### Fase 0 — Onda 3: Diversificação de fontes (planejamento)

> Brainstorm conduzido via `/intake` (múltiplas rodadas com `@medallion-architect` e `@databricks-data-engineer`). Decisões abaixo refletem o estado atual do brainstorm — ainda não formalizadas em `/define`.

**Objetivo:** sair de 2 sistemas (Postgres real + MinIO simulado) para 4, cada um hospedando um domínio de negócio coerente (não entidades soltas), e tornar a ingestão mais fiel a um cenário real de CDC — capturando `UPDATE`/`DELETE`, não só `INSERT`.

| Decisão | Resumo | Confiança |
|---|---|---|
| Sistemas-alvo | **Postgres** (mantém), **Oracle** (novo), **MongoDB** (novo — cadastro estático/satélites documentais, não dado vivo), **MinIO** (mantém o já existente; descartada a ideia de um 2º MinIO — redundante com os datalakes reais que as Fases 1-3 já entregam) | Fechada |
| Critério de alocação | "Technology fit": entidades-mestre com estado mutável (Usuário, Motorista, Restaurante, Produto, Estoque) vão para Postgres/Oracle; streams append-only por natureza (Pedido, Pagamento, Entrega, Recibo, eventos, telemetria) permanecem no MinIO; satélites documentais estáticos (ex. "Perfil de Restaurante": menu, horários, tags, políticas) no MongoDB | Fechada — critério; alocação entidade-a-entidade final fica para o `/define` |
| Entidades novas no modelo | Autorizadas — ex. satélite documental do Restaurante, a modelar em detalhe no `/define` (hoje o modelo conceitual tem 13 entidades) | Fechada |
| CDC no Oracle | Via **Debezium/Kafka Connect** — o conector Oracle CDC do Airbyte é `source-oracle-enterprise`, pago/Enterprise; o OSS só faz Full Refresh ou incremental por cursor. Decisão: aceitar o componente de infraestrutura novo em troca de CDC real (melhor valor de portfólio: dois motores de CDC diferentes convivendo) | Fechada |
| CDC no Postgres | Mantém Airbyte OSS (já suportado; `wal_level=logical` já configurado em `docker-compose.yml`) | Fechada |
| Mutação de estado real (UPDATE/DELETE) | ShadowTraffic suporta `op: insert\|update\|delete` nativamente em conexões `postgres` e `oracle` (mecanismo `fork` + `stateMachine`, confirmado na doc oficial). Candidatos iniciais de v1: `drivers.status`, `users.total_orders`/`last_login`. O log append-only já existente (`kafka/status` para Pedido, `kafka/events` para Pagamento) é mantido — **regra de ouro:** estado mutável e log de transição devem ser alimentados pelo mesmo `stateMachine`, nunca gerados de forma independente (senão divergem) | Fechada quanto ao mecanismo; escopo exato da v1 e desenho fork×lookup ficam para o `/define` |
| Nomenclatura do medalhão | Tabelas Silver passam a nomear por **domínio de negócio** (ex. `silver_orders`), não mais por sistema de origem (ex. `silver_kafka_orders`) — deixa futuras trocas de fonte mais baratas | Fechada |

**Pendências antes de formalizar `/define`:**
- Desenho exato do gerador de mutação (reescrever `users`/`drivers` com `fork`+`stateMachine`, ou manter os geradores atuais e somar um segundo gerador de update via `lookup` no `where` — recomenda-se um protótipo rápido com `--stdout` antes de decidir)
- Escopo exato da v1 de mutação de estado (sugestão do brainstorm: começar só com `drivers.status` + `users.total_orders`/`last_login`, soft delete)
- Modelagem detalhada dos satélites documentais novos (schema do "Perfil de Restaurante" no MongoDB)
- Registro formal do processo em `.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md` (nome provisório) quando o usuário decidir avançar para `/brainstorm`/`/define`

**Riscos levantados no brainstorm (ver contexto completo na sessão que originou esta seção, a formalizar no `/define`):**
- Todo sistema novo precisa entrar como `connection` do **mesmo processo único** do `gen-unified` (Postgres/Oracle) — gerador separado recria o bug de "populações desconectadas" que a Onda 2 resolveu
- MongoDB sem sink no ShadowTraffic — população é seed estático (M1) ou satélite com FK para cadastro congelado (M3), nunca gerada de forma independente
- Auto-DDL do ShadowTraffic não cria PRIMARY KEY — colunas-chave migradas para Postgres/Oracle precisam de `sqlHint`/`tablePolicy: manual` explícito, senão a réplica lógica falha silenciosamente
- Hard delete em entidades-pai (Usuário, Motorista) quebra a integridade referencial das Ondas 1/2 — usar soft delete nessas entidades

---

### Fase 1 — Azure (3 arquiteturas completas)

| Ordem | Arquitetura | Ferramenta principal | Observação |
|---|---|---|---|
| 1ª | Warehouse | Synapse (Serverless SQL Pool) | Modelagem dimensional (schema estrela + SCD tipo 2) — foco principal de aprendizado da fase |
| 2ª | Lakehouse | Databricks (reaproveitado do projeto já existente) + ADLS Gen2 | Migração leve: troca de storage (MinIO → ADLS Gen2); processamento e camadas do medalhão mantidos como já implementados |
| 3ª | Kappa | Event Hubs + Stream Analytics (ou Spark Structured Streaming) | Streaming em ambiente já conhecido, reduzindo o risco de aprender conceito novo (Kappa) e cloud nova ao mesmo tempo |

**IaC/CI-CD:** Terraform (workspace Databricks, ADLS Gen2, Synapse, Event Hubs) + DAB (jobs/pipelines do Lakehouse) + pipeline CI/CD (ex: GitHub Actions). Padrão estabelecido nesta fase, reaproveitado nas seguintes.

---

### Fase 2 — AWS (3 arquiteturas, stack 100% nativa)

| Ordem | Arquitetura | Ferramenta principal |
|---|---|---|
| 1ª | Warehouse | Redshift Serverless |
| 2ª | Lakehouse | Glue + Iceberg + Athena |
| 3ª | Kappa | Kinesis (ou MSK) + Flink/Lambda |

**IaC/CI-CD:** Terraform (sem DAB — não há Databricks nesta fase).

---

### Fase 3 — GCP (3 arquiteturas, stack 100% nativa)

| Ordem | Arquitetura | Ferramenta principal |
|---|---|---|
| 1ª | Warehouse | BigQuery |
| 2ª | Lakehouse | BigLake/Dataproc + Iceberg |
| 3ª | Kappa | Pub/Sub + Dataflow |

**IaC/CI-CD:** Terraform (sem DAB).

---

### Fase 4 — Consolidação

- README comparativo entre as 9 combinações arquitetura × cloud, com custo, latência e complexidade medidos na prática (não copiados de terceiros)
- Documentação das decisões técnicas tomadas e dos problemas reais enfrentados em cada fase
- Destaque específico para o contraste "Lakehouse via Databricks (Azure)" vs. "Lakehouse nativo (Glue/Iceberg na AWS, BigLake/Dataproc no GCP)" — mesmo padrão arquitetural implementado de formas diferentes
- Repositório organizado por cloud/arquitetura, pronto para apresentação em processo seletivo

---

## 4. Estimativa de norte temporal

| Fase | Sessões (~3h) estimadas | Tempo corrido aproximado |
|---|---|---|
| 0 — Fundação (Ondas 1-2, concluídas) | ~4-6 | 1 a 1,5 mês |
| 0 — Onda 3 (diversificação de fontes, planejada) | ~4-6 adicionais | ~1 a 1,5 mês adicional |
| 1 — Azure (3 arquiteturas) | ~8-10 | ~2 a 2,5 meses |
| 2 — AWS (3 arquiteturas) | ~14-16 | ~3,5 a 4 meses |
| 3 — GCP (3 arquiteturas) | ~10-12 | ~2,5 a 3 meses |
| 4 — Consolidação | ~3-4 | ~1 mês |
| **Total** | **~44-54** | **~11,5 a 14,5 meses** |

*Estimativas servem como referência de planejamento; ajustes ao longo do caminho são esperados e não invalidam o roadmap. A Fase 0 já ultrapassou o orçamento original de 4-6 sessões (Ondas 1+2 o consumiram) — a Onda 3 é um orçamento adicional explícito, não uma correção de estimativa.*

---

## 5. Lacunas de conhecimento endereçadas por fase

| Fase | Lacuna principal atacada |
|---|---|
| 0 (Ondas 1-2) | Modelagem relacional |
| 0 (Onda 3) | CDC real multi-motor (Airbyte + Debezium/Kafka Connect), Oracle como fonte, modelagem documental (MongoDB), geração sintética de mutação de estado (ShadowTraffic `fork`/`stateMachine`) |
| 1 (Warehouse) | Modelagem dimensional |
| 1 (Kappa) | Streaming/Kafka (em ambiente já conhecido) |
| 2 | AWS como cloud (maior lacuna declarada) |
| 3 | GCP como cloud; streaming em ambiente novo (Pub/Sub + Dataflow) |
| DevOps/DataOps | Terraform + CI/CD, presente desde a Fase 1 |

---

## Histórico de revisões

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | Agosto/2026 | Documento inicial (`docs/plan.md`) |
| 1.1 | Setembro/2026 | Renomeado para `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`. Fase 0 detalhada com status real (Ondas 1-2 concluídas) e nova subseção "Onda 3 — Diversificação de fontes" capturando o brainstorm de expansão para Postgres+Oracle+MongoDB+MinIO com CDC real. Estimativa de norte temporal e lacunas de conhecimento atualizadas de acordo |
