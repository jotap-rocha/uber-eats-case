# Uber Eats — Roadmap de Arquiteturas de Dados Multi-Cloud

**Documento de planejamento**

**Versão:** 1.0

**Data:** Agosto/2026

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

| Item | Descrição |
|---|---|
| Shadow Traffic | Corrigir integridade referencial entre os geradores (Postgres, MongoDB, MySQL, Kafka), garantindo que entidades-filho referenciem corretamente chaves de entidades-pai já existentes |
| Modelo conceitual | Desenhar entidades e relacionamentos do domínio Uber Eats (usuário, restaurante, produto, pedido, item de pedido, pagamento, entrega, avaliação) — modelo único, reaproveitado nas 3 arquiteturas e nas 3 clouds |
| Agentes | Carregar com conhecimento de arquitetura de dados (Warehouse, Lakehouse, Kappa, medalhão, modelagem dimensional). Conhecimento específico de cada cloud entra sob demanda, a partir da fase correspondente |

**Critério de saída:** consulta de join entre as 4 fontes de dados retorna resultado consistente, sem registros órfãos.

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
| 0 — Fundação | ~4-6 | 1 a 1,5 mês |
| 1 — Azure (3 arquiteturas) | ~8-10 | ~2 a 2,5 meses |
| 2 — AWS (3 arquiteturas) | ~14-16 | ~3,5 a 4 meses |
| 3 — GCP (3 arquiteturas) | ~10-12 | ~2,5 a 3 meses |
| 4 — Consolidação | ~3-4 | ~1 mês |
| **Total** | **~40-48** | **~10 a 13 meses** |

*Estimativas servem como referência de planejamento; ajustes ao longo do caminho são esperados e não invalidam o roadmap.*

---

## 5. Lacunas de conhecimento endereçadas por fase

| Fase | Lacuna principal atacada |
|---|---|
| 0 | Modelagem relacional |
| 1 (Warehouse) | Modelagem dimensional |
| 1 (Kappa) | Streaming/Kafka (em ambiente já conhecido) |
| 2 | AWS como cloud (maior lacuna declarada) |
| 3 | GCP como cloud; streaming em ambiente novo (Pub/Sub + Dataflow) |
| DevOps/DataOps | Terraform + CI/CD, presente desde a Fase 1 |