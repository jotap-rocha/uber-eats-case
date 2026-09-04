# Uber Eats — Roadmap de Arquiteturas de Dados Multi-Cloud

**Documento de planejamento**

**Versão:** 1.3

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
| Portabilidade de motor por camada (v1.2) | O **modelo de domínio** (13+ entidades, `docs/MODELO_CONCEITUAL_UBER_EATS.md`) e a **mecânica de CDC** (replication slot/log, PK obrigatória, soft delete) são fixos e reaproveitados nas 3 clouds. A **implementação física** não é: Oracle e MinIO são específicos da Fase 0/1 (Azure). Nas Fases 2/3, os papéis equivalentes são servidos pelo motor relacional e pelo object storage nativos de cada cloud (ex.: AWS = banco relacional gerenciado da AWS + S3; GCP = banco relacional gerenciado do GCP + GCS) — o motor exato de cada fase é decidido no `/define` daquela fase, não aqui |
| Ingestão/CDC por fase (v1.2) | Fases 0/1: **Airbyte** (Postgres→Databricks) + **Debezium/Kafka Connect** (Oracle→Databricks) — ver Onda 3. Fases 2/3: ingestão nativa da cloud (ex.: AWS DMS e/ou MSK Connect; GCP Datastream) em vez de Airbyte/Debezium — decisão tomada em brainstorm (`/intake`), detalhamento fica para o `/define` de cada fase. Para não reescrever a Silver a cada fase, a Bronze deve expor um **contrato canônico de metadados de CDC** (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) — cada ferramenta de ingestão emite um formato próprio (`_ab_cdc_*` no Airbyte, `op`/`before`/`after` no Debezium, etc.) e a Silver nunca deve ler o formato nativo diretamente |
| Gestão de custo | Responsabilidade do usuário — priorizar sempre serviços serverless/on-demand (Redshift Serverless, Synapse Serverless SQL Pool, BigQuery on-demand, Databricks com auto-termination agressivo) para evitar cobrança de recurso ligado sem uso |

---

## 3. Fases

### Fase 0 — Fundação (local, bloqueante)

| Item | Descrição | Status |
|---|---|---|
| Shadow Traffic — integridade referencial (Onda 1) | Corrigir integridade referencial entre os geradores simulados (MySQL, MongoDB, Kafka dentro do MinIO), garantindo que entidades-filho referenciem corretamente chaves de entidades-pai já existentes | ✅ Concluído — `.claude/sdd/archive/INTEGRIDADE_REFERENCIAL_SHADOW_TRAFFIC/` |
| Unificação de identidade Postgres×MinIO (Onda 2) | Migrar Usuário/Motorista para fonte única (Postgres real), PK sequencial em vez de UUID, reconciliar dimensão única de motorista | ✅ Concluído — `.claude/sdd/archive/UNIFICACAO_IDENTIDADE_POSTGRES_MINIO/` |
| Modelo conceitual | Desenhar entidades e relacionamentos do domínio Uber Eats (usuário, restaurante, produto, pedido, item de pedido, pagamento, entrega, avaliação, motorista, estoque, turno, incidente, recibo) — modelo único, reaproveitado nas 3 arquiteturas e nas 3 clouds | ✅ Concluído — `docs/MODELO_CONCEITUAL_UBER_EATS.md` |
| Diversificação de fontes (Onda 3) | Sair de 2 sistemas (Postgres real + MinIO simulado) para 4 sistemas heterogêneos, com CDC real e mutação de estado — ver subseção "Fase 0 — Onda 3" abaixo | ✅ Brainstorm concluído — `.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`; falta `/define` |
| Agentes | Carregar com conhecimento de arquitetura de dados (Warehouse, Lakehouse, Kappa, medalhão, modelagem dimensional). Conhecimento específico de cada cloud entra sob demanda, a partir da fase correspondente | Contínuo |

**Critério de saída (revisado na v1.1):** consulta de join entre as fontes de dados — hoje 2 sistemas (Postgres, MinIO), alvo de 4 (Postgres, Oracle, MongoDB, MinIO) após a Onda 3 — retorna resultado consistente, sem registros órfãos; e a mutação de estado (UPDATE/DELETE) em Postgres/Oracle é capturada corretamente pelo CDC (Airbyte para Postgres, Debezium/Kafka Connect para Oracle).

---

#### Fase 0 — Onda 3: Diversificação de fontes (brainstorm concluído)

> Brainstorm conduzido via `/intake` (múltiplas rodadas com `@medallion-architect` e `@databricks-data-engineer`) e formalizado via `/brainstorm`. Documento completo: [`BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`](../.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md). Próximo passo: `/define`.

**Objetivo:** sair de 2 sistemas (Postgres real + MinIO simulado) para 4, cada um hospedando um domínio de negócio coerente, com CDC real e mutação de estado (`UPDATE`/`DELETE`, não só `INSERT`).

**Alocação final:**

| Sistema | Entidades | CDC |
|---|---|---|
| **Postgres** | Usuário, Motorista (mutável: `drivers.status` etc.) | Airbyte OSS (mantém) |
| **Oracle** (novo) | Restaurante, Produto, Estoque, **Pedido, Item de Pedido, Pagamento, Recibo** (mutáveis: `orders.status`, `payments.status`) | Debezium/Kafka Connect (novo — conector Oracle CDC do Airbyte é pago/Enterprise) |
| **MongoDB** (novo) | Satélite "Perfil de Restaurante" (menu + horários) — cadastro estático, FK para `restaurant_id` | Não aplicável (sem CDC; sem sink de escrita no ShadowTraffic) |
| **MinIO** (mantém) | Entrega, Avaliação, Turno, Incidente + streams fora do core | Airbyte OSS (mantém) |

**Decisão-chave tomada durante o `/brainstorm`:** Pedido e Pagamento migram para o Oracle (não ficam no MinIO como cogitado inicialmente) porque o usuário decidiu **aposentar os logs append-only `kafka/status`/`kafka/events`** — a mudança de status passa a ser a mutação real da linha, capturada pelo CDC. Descartado de vez: um segundo MinIO/datalake.

**Sequenciamento (mitigação de risco, mesmo método das Ondas 1/2):** 1) provar o mecanismo `fork`+`stateMachine` no Postgres (Motorista) — infra já madura; 2) levantar o Oracle com Restaurante/Produto/Estoque, insert-only, validar CDC básico; 3) só então aplicar mutação real a Pedido/Pagamento no Oracle e aposentar os logs antigos. Detalhe completo no BRAINSTORM.

**Escopo por fase (v1.2):** a topologia de 4 sistemas e a ingestão via Airbyte+Debezium são específicas da Fase 0/1 (Azure). Nas Fases 2/3, Oracle e MinIO são substituídos pelos motores nativos de cada cloud — ver Seção 2 ("Portabilidade de motor por camada").

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

**Fontes e ingestão (v1.2):** Oracle e MinIO da Fase 0 são substituídos pelos papéis equivalentes em serviços nativos AWS (banco relacional gerenciado + S3 — motor exato a decidir no `/define` da fase). Ingestão/CDC via **AWS DMS** (fontes com CDC compatível) e/ou **MSK Connect** rodando o mesmo Debezium aprendido na Fase 0 (útil se alguma fonte não tiver CDC suportado no DMS) — não via Airbyte.

**IaC/CI-CD:** Terraform (sem DAB — não há Databricks nesta fase).

---

### Fase 3 — GCP (3 arquiteturas, stack 100% nativa)

| Ordem | Arquitetura | Ferramenta principal |
|---|---|---|
| 1ª | Warehouse | BigQuery |
| 2ª | Lakehouse | BigLake/Dataproc + Iceberg |
| 3ª | Kappa | Pub/Sub + Dataflow |

**Fontes e ingestão (v1.2):** Oracle e MinIO da Fase 0 são substituídos pelos papéis equivalentes em serviços nativos GCP (banco relacional gerenciado + Cloud Storage — motor exato a decidir no `/define` da fase). Ingestão/CDC via **Datastream** (cobre Postgres, Oracle e MongoDB nativamente, com destino direto em BigQuery ou tabelas Iceberg do BigLake) — não via Airbyte/Debezium.

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
| 2 | AWS como cloud (maior lacuna declarada); CDC gerenciado (AWS DMS, MSK Connect) |
| 3 | GCP como cloud; streaming em ambiente novo (Pub/Sub + Dataflow); CDC gerenciado (Datastream) |
| DevOps/DataOps | Terraform + CI/CD, presente desde a Fase 1 |

---

## Histórico de revisões

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | Agosto/2026 | Documento inicial (`docs/plan.md`) |
| 1.1 | Setembro/2026 | Renomeado para `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`. Fase 0 detalhada com status real (Ondas 1-2 concluídas) e nova subseção "Onda 3 — Diversificação de fontes" capturando o brainstorm de expansão para Postgres+Oracle+MongoDB+MinIO com CDC real. Estimativa de norte temporal e lacunas de conhecimento atualizadas de acordo |
| 1.2 | Setembro/2026 | Esclarecido que a topologia de 4 sistemas e Airbyte+Debezium são específicos da Fase 0/1 (Azure). Novos princípios "Portabilidade de motor por camada" e "Ingestão/CDC por fase": nas Fases 2/3, Oracle e MinIO são substituídos pelos motores relacionais e object storage nativos de cada cloud, e a ingestão passa a ser nativa (AWS DMS/MSK Connect; GCP Datastream) em vez de Airbyte/Debezium. Adicionado requisito de contrato canônico de metadados de CDC na Bronze, para a Silver não depender do formato específico de cada ferramenta de ingestão |
| 1.3 | Setembro/2026 | Brainstorm da Onda 3 formalizado (`/brainstorm` → `.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`). Alocação final: Pedido, Pagamento, Item de Pedido e Recibo migram para o Oracle (não ficam no MinIO como cogitado inicialmente), porque os logs append-only `kafka/status`/`kafka/events` são aposentados em favor de mutação real capturada por CDC. Segundo MinIO descartado definitivamente. Adicionado sequenciamento em 3 etapas (Postgres/Motorista → Oracle plumbing → Oracle/Pedido+Pagamento) para isolar o risco do mecanismo de mutação, nunca testado neste projeto |
