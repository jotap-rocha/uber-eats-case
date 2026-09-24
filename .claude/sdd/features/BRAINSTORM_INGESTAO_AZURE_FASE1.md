# BRAINSTORM: Arquitetura de Ingestão — Fase 1 (Azure)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AZURE_FASE1 |
| **Fase do roadmap** | Fase 1 — Azure (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Depende de** | Fase 0 (4 sistemas de origem: Postgres, Oracle, MongoDB, MinIO — `BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md`) |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-12 |

---

## Ideia inicial

A Fase 1/Azure já tinha uma arquitetura de ingestão registrada no roadmap (seção "Fase 1 — Arquitetura de Ingestão", v1.4), fechada em rodada adversarial de `/intake` — mas, ao contrário da Fase 2/AWS e da Fase 3/GCP, **nunca ganhou um artefato `BRAINSTORM_INGESTAO_*` formal**. O usuário pediu para fechar essa lacuna e trouxe uma proposta de desenho revisado —

```
MongoDB -> Airbyte -> ADLS
MinIO -> Airbyte -> ADLS
Postgres -> Airbyte -> ADLS
Oracle -> Debezium -> ADLS

Synapse: Consome do ADLS
Databricks: Vai consumir ou do ADLS, como um external table, ou será necessário uma ingestão
no lake gerenciado do free tier. Quero ser rápido, pois já uso Databricks e quero só
reaproveitar a primeira versão do projeto.

Event Hub: Consome do MinIO diretamente e do ADLS, Stream Analytics processa
```

— que difere do desenho já registrado em dois pontos: (1) inclui **MinIO no trilho batch** (não estava lá antes) e (2) propõe o **Event Hub também lendo do ADLS**, além do MinIO direto. Este brainstorm reconcilia a proposta com a decisão anterior, resolve a pendência real do Databricks (external table vs. ingestão gerenciada) e formaliza o artefato que faltava, no mesmo formato usado nas Fases 2/3.

---

## Decisões de escopo

| # | Decisão | Resposta |
|---|---------|----------|
| 1 | O Event Hub deve ler também do ADLS (trilho batch), além do MinIO direto — mudando a decisão original de o Stream Analytics nunca ler do ADLS? | **Não — mantida a decisão original.** Stream Analytics continua lendo só do Event Hub (real-time puro). MinIO entra no Event Hub via notificação nativa de bucket; o ADLS/trilho batch nunca alimenta o Kappa, preservando o mesmo princípio já usado nas Fases 2/3 (AWS/GCP) de não deixar o Kappa virar "Lambda architecture disfarçada" |
| 2 | Como o Databricks Free Edition deve consumir o dado batch pousado no ADLS Gen2? | **External table** sobre o ADLS Gen2 (Unity Catalog, via storage credential/Azure AD), não uma ingestão adicional para dentro do managed lake do workspace — sem cópia de dado, mais rápido de montar |
| 3 | O Lakehouse deve manter as entradas de streaming que já existem hoje (Oracle via `read_kafka()`/Redpanda, Postgres via Airbyte→Databricks direto) trocando só o broker/endpoint, ou consolidar tudo pelo ADLS batch? | **Consolidar tudo via external table sobre o ADLS** — decisão explícita do usuário, mesmo custando descartar o `read_kafka()` do Oracle (já funcional, trocaria só `bootstrapServers`/auth pro Event Hub) e o sync direto Airbyte→Databricks do Postgres (já funcional, sem custo de setup adicional). Prioriza um único padrão de ingestão para o Lakehouse desta fase em vez de manter 3 mecanismos distintos por fonte |
| 4 | Consolidar via ADLS sem perder o objetivo de "CDC real com mutação" (motivo da Onda 3): o lote no ADLS deve carregar eventos de CDC (op/before/after/sequência) ou pode ser snapshot periódico simples? | **Lote com CDC.** Oracle: Debezium/Kafka Connect grava os eventos CDC como arquivos no ADLS via sink dedicado (preserva `op`/`before`/`after`/SCN). Postgres: a 2ª conexão do Airbyte roda em **modo CDC** (replication slot), não Standard/snapshot — aceitando o custo de um 2º replication slot para preservar o histórico de mutação (ex.: os 8 status intermediários do pedido) tanto na Bronze do Lakehouse quanto no `MERGE` do Synapse |
| 5 | Airbyte e Debezium/Kafka Connect conseguem escrever direto no Event Hub, sem componente-ponte? | **Sim — confirmado.** O Event Hubs expõe um endpoint compatível com o protocolo Kafka. O Airbyte usa seu destino nativo "Kafka" apontando `bootstrap.servers` para `<namespace>.servicebus.windows.net:9093` (SASL_SSL, connection string como senha); o Kafka Connect do Debezium faz o mesmo, sem trocar nada da lógica do conector — é exatamente o padrão documentado pela Microsoft ("Kafka Connect para Event Hubs") e o mesmo princípio já usado localmente com Redpanda em `pipeline/bronze/ingest_oracle_orders.sql`. Restrição real: os tópicos internos do Kafka Connect (`connect-offsets`, `connect-configs`, `connect-status`) exigem tópicos compactados, suportados só a partir do tier **Standard** do Event Hubs Namespace (não Basic) |
| 6 | Como o MongoDB (satélite estático) entra na Fase 1, já que o Lakehouse hoje o lê via Lakehouse Federation? | **Mesma lógica das outras 2 clouds** (AWS: DMS full load; GCP: Datastream full load/snapshot) — **Airbyte, snapshot/full-refresh** (sem CDC, fonte estática) → ADLS Gen2 (Bronze), consolidado no mesmo lote batch de Postgres/Oracle/MinIO. **Lakehouse Federation é descartada** para esta fase — o usuário quer ingestão de fato (via Airbyte), não consulta federada ao vivo |
| 7 | O MongoDB deve enriquecer o Kappa (Stream Analytics), já que ele é estático e não entra pelo Event Hub? | **Sim — mesma lógica de AWS (lookup contra a cópia no S3/Bronze) e GCP (lookup contra a tabela Iceberg do BigLake).** Stream Analytics usa o recurso nativo **reference data input**, fazendo join do stream do Event Hub contra a cópia do MongoDB já pousada no ADLS Gen2/Bronze pelo trilho batch (Decisão #6) — sem cache/TTL manual nem componente novo, já que a Azure tem suporte nativo pra esse padrão |

---

## Achado técnico que desbloqueou/restringiu a feature

- **O Lakehouse já faz streaming de verdade hoje, e isso quase não custaria nada trocar.** `pipeline/bronze/ingest_oracle_orders.sql` já lê `STREAM read_kafka(bootstrapServers => 'redpanda:9092', subscribe => 'oracle.UBEREATS.ORDERS')` com `APPLY CHANGES INTO ... SEQUENCE BY cdc_sequence` — CDC real, streaming, já funcional. Como o Event Hubs fala protocolo Kafka nativamente, mover esse pipeline para Azure custaria só trocar `bootstrapServers`/autenticação. O usuário optou por **não** reaproveitar isso e consolidar via external table (Decisão #3) — trade-off consciente, documentado abaixo em "Abordagens exploradas".
- **O Postgres de hoje não passa por arquivo nenhum.** `docs/airbyte/README.md` documenta o destino "Databricks Lakehouse" do Airbyte escrevendo direto nas tabelas do catálogo (`main.uber_eats`/`main.uber_eats_raw`), sem ADLS/MinIO no meio. Migrar para a consolidação via ADLS é, portanto, uma mudança de mecanismo para o Postgres, não uma simples troca de endpoint.
- **Event Hubs Standard tier é pré-requisito para Kafka Connect/Debezium** (tópicos compactados internos do Connect não existem no tier Basic) — constraint de custo a registrar, já que o princípio de gestão de custo do roadmap (Seção 2) prioriza serviços serverless/on-demand; Event Hubs Standard não é serverless puro, mas é o mínimo necessário aqui.
- **MinIO no trilho batch é uma extensão real do desenho v1.4**, não uma correção — o roadmap original só tinha MinIO no trilho real-time (notificação nativa → Event Hub); a proposta do usuário adiciona MinIO ao trilho batch (Airbyte → ADLS), o que faz sentido para consistência com o padrão "todo o Bronze do Lakehouse vem do mesmo ADLS" (Decisão #3).

---

## Abordagens exploradas

### Abordagem A — Reaproveitamento máximo por fonte (recomendada pela IA, não escolhida)

**O que faz:** mantém os 3 mecanismos de ingestão do Lakehouse como já existem hoje — Oracle via `read_kafka()` (só troca o broker pro Event Hub), Postgres via Airbyte→Databricks direto (inalterado), MinIO/MongoDB via Auto Loader/Federation (só troca o storage MinIO→ADLS). Zero redesenho.

**Por que não foi escolhida:** o usuário priorizou ter **um único padrão de ingestão** para o Lakehouse desta fase (external table sobre ADLS) em vez de conviver com 3 mecanismos distintos por fonte, mesmo que isso descarte trabalho já pronto e funcional.

### Abordagem B — Consolidação via external table sobre ADLS, lote com CDC ⭐ Escolhida

**O que faz:** todo o Bronze do Lakehouse (Postgres, Oracle, MongoDB, MinIO) é lido via external table sobre o mesmo ADLS Gen2/Bronze que alimenta o Synapse. Para não perder a granularidade de mutação, o lote carrega eventos de CDC (Debezium sink dedicado para Oracle; Airbyte modo CDC/replication slot para Postgres), não snapshots simples.

**Por que escolhida:** um único padrão de ingestão para o Lakehouse, mais simples de explicar e operar nesta fase — trade-off aceito é abrir mão do streaming (Databricks passa a aplicar `APPLY CHANGES` em lote, não em tempo real), mas preserva o histórico de mutação que motivou a Onda 3.

### Abordagem C — Consolidação via external table sobre ADLS, snapshot simples (rejeitada)

**O que faz:** mesma consolidação da Abordagem B, mas o lote no ADLS seria um snapshot periódico simples (Airbyte Standard/full-refresh, sem CDC) para Postgres e Oracle — mais barato, sem 2º replication slot no Postgres.

**Por que rejeitada:** perderia o histórico de mutação (ex.: os 8 status intermediários do pedido) tanto na Bronze do Lakehouse quanto no `MERGE` do Synapse — undermina diretamente o motivo de ter trazido Oracle+Debezium na Onda 3 ("CDC real multi-motor... mutação real").

---

## Desenho consolidado

```
REAL-TIME (Kappa) — inalterado da decisão v1.4
Postgres ──Airbyte OSS (CDC, replication slot)─────────────▶ Event Hub ──▶ Stream Analytics
Oracle   ──Debezium/Kafka Connect (LogMiner)────────────────▶ Event Hub ──▶ Stream Analytics
MinIO    ──notificação de bucket nativa──────────────────────▶ Event Hub ──▶ Stream Analytics

BATCH (Warehouse + Lakehouse) — consolidado, lote com CDC
Postgres ──Airbyte, 2ª conexão, modo CDC (replication slot)─▶ ADLS Gen2 (Bronze)
Oracle   ──Debezium/Kafka Connect, sink dedicado (op/before/after/SCN)─▶ ADLS Gen2 (Bronze)
MongoDB  ──Airbyte, snapshot/full-refresh (estático)────────▶ ADLS Gen2 (Bronze)
MinIO    ──Airbyte──────────────────────────────────────────▶ ADLS Gen2 (Bronze)
```

**Consumidores:**
- **Synapse Dedicated (Warehouse):** `COPY INTO` a partir do ADLS Gen2/Bronze, seguido de `MERGE` para SCD2, aplicando o contrato canônico de CDC (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`).
- **Databricks (Lakehouse):** external tables sobre o mesmo ADLS Gen2/Bronze (Unity Catalog, storage credential/Azure AD), com `APPLY CHANGES`/upsert aplicado em lote a partir dos metadados de CDC do arquivo — substitui o `read_kafka()` do Oracle e o sync direto Airbyte→Databricks do Postgres usados hoje na Fase 0, e substitui a Lakehouse Federation usada hoje para o MongoDB.
- **Stream Analytics (Kappa):** lê o stream principal só do Event Hub — nunca do ADLS para eventos, preservando a decisão original de não descaracterizar o Kappa. Enriquece Pedido/Restaurante via **reference data input** (join contra a cópia do MongoDB já pousada no ADLS Gen2/Bronze pelo trilho batch) — mesmo papel do lookup no S3/Bronze (Lambda, AWS) e na tabela Iceberg (Dataflow, GCP), aqui resolvido com um recurso nativo do próprio Stream Analytics.

---

## Escopo desta feature

| Item | Ação |
|------|------|
| Event Hubs Namespace (tier Standard) | Provisionar com tier Standard (não Basic) — pré-requisito para Kafka Connect/Debezium (tópicos compactados internos) |
| Airbyte — destino Kafka (Event Hub) | Configurar destino "Kafka" apontando pro endpoint Kafka-compatível do Event Hub (SASL_SSL, connection string) para a conexão real-time de Postgres |
| Airbyte — 2ª conexão Postgres (modo CDC) | Nova conexão dedicada ao trilho batch, modo CDC/replication slot, destino ADLS Gen2 |
| Airbyte — MongoDB e MinIO (destino ADLS) | Configurar destino Azure Blob Storage/ADLS Gen2 para as syncs snapshot/full-refresh de MongoDB e MinIO |
| Debezium/Kafka Connect — sink Event Hub (real-time) | Apontar `bootstrap.servers` do Kafka Connect do Oracle pro endpoint Kafka-compatível do Event Hub |
| Debezium/Kafka Connect — sink dedicado ADLS (batch) | Configurar sink adicional do Kafka Connect gravando os eventos CDC do Oracle como arquivos no ADLS Gen2/Bronze |
| MinIO — notificação de bucket nativa | Configurar destino Webhook/Kafka-compatible apontando pro Event Hub (trilho real-time) |
| Unity Catalog — storage credential + external location | Provisionar credencial (Service Principal/managed identity) e external location apontando pro container ADLS Gen2/Bronze |
| Databricks — external tables + `APPLY CHANGES` em lote | Reescrever a Bronze (hoje `read_kafka()` para Oracle, sync direto para Postgres, Federation para MongoDB) para ler das external tables e aplicar merge por `cdc_sequence` |
| Synapse Dedicated — `COPY INTO` + `MERGE` | Pipeline de carga do ADLS Gen2/Bronze para o Synapse, aplicando SCD2 |
| Stream Analytics — reference data input (MongoDB) | Configurar o job do Stream Analytics com uma entrada de reference data apontando pro caminho do MongoDB no ADLS Gen2/Bronze, fazendo join contra o stream do Event Hub para enriquecer Pedido/Restaurante |
| Contrato canônico de CDC (extensão) | Mapear metadados de ordenação do Debezium (SCN) e do Airbyte (`_ab_cdc_*`) para o campo canônico `cdc_sequence`, incluindo a variante "lote" (arquivo) além da variante streaming já existente |
| Atualizar `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` | Registrar o desenho decidido nesta feature na subseção "Fase 1 — Arquitetura de Ingestão", incluindo a extensão de MinIO ao trilho batch e a consolidação do Lakehouse via ADLS |

## Fora de escopo

| Item | Por que fica para depois |
|------|-----------------------------|
| Reaproveitar o `read_kafka()`/Redpanda do Oracle e o sync direto Airbyte→Databricks do Postgres (Abordagem A) | Avaliada e descartada nesta rodada — usuário priorizou um único padrão de ingestão (external table) para o Lakehouse |
| Lakehouse Federation para o MongoDB | Descartada — usuário quer ingestão real (Airbyte), não consulta federada ao vivo |
| Snapshot simples (sem CDC) para o lote batch de Postgres/Oracle (Abordagem C) | Avaliada e descartada — perderia o histórico de mutação da Onda 3 |
| Event Hub lendo do ADLS além do MinIO direto | Avaliada e descartada — mantém a decisão original de o Kappa nunca ler do trilho batch |
| Dimensionamento exato do Event Hubs Namespace (throughput units/partições) e do Synapse Dedicated (DWU) | Detalhe de implementação — fica para o `/define`/`/design` |
| Mapeamento exato dos metadados de ordenação (SCN do Debezium, `_ab_cdc_lsn`/`_ab_cdc_updated_at` do Airbyte) para `cdc_sequence` | Pendência transversal já registrada no roadmap (v1.4) — fica para o `/define` desta feature |

## YAGNI aplicado

- Não manter os 3 mecanismos de ingestão distintos do Lakehouse "porque já funcionam" — o usuário decidiu explicitamente por um único padrão (external table sobre ADLS), mesmo custando descartar trabalho pronto; a Abordagem A fica documentada como avaliada, não como escopo extra.
- Não introduzir um componente-ponte (Lambda/Cloud Function equivalente) entre Airbyte/Debezium e o Event Hub — confirmado que ambos falam Kafka nativamente contra o endpoint do Event Hub, sem intermediário.
- Não resolver agora o mapeamento fino de metadados de ordenação (SCN/`_ab_cdc_*` → `cdc_sequence`) nem o dimensionamento de Event Hubs/Synapse — são decisões de design/implementação, não de arquitetura de ingestão; documentadas como pendência explícita.

---

## Draft Requirements para `/define`

1. Provisionar o Event Hubs Namespace em tier **Standard**, com os tópicos necessários para os 3 fluxos real-time (Postgres, Oracle, MinIO).
2. Configurar o destino "Kafka" do Airbyte para a conexão CDC de Postgres, apontando pro endpoint Kafka-compatível do Event Hub (SASL_SSL).
3. Criar a 2ª conexão do Airbyte para Postgres (modo CDC/replication slot), destino ADLS Gen2/Bronze — aceitando o 2º replication slot.
4. Configurar o Kafka Connect do Debezium/Oracle com dois sinks: um para o Event Hub (trilho real-time, troca de `bootstrap.servers`) e um sink dedicado gravando arquivos no ADLS Gen2/Bronze com os campos de CDC (`op`/`before`/`after`/SCN) preservados (trilho batch).
5. Configurar as conexões do Airbyte para MongoDB (snapshot/full-refresh) e MinIO (sync), ambas com destino ADLS Gen2/Bronze.
6. Configurar a notificação de bucket nativa do MinIO com destino compatível com o endpoint Kafka do Event Hub (trilho real-time).
7. Provisionar a storage credential (Service Principal/managed identity) e a external location do Unity Catalog apontando pro container ADLS Gen2/Bronze.
8. Reescrever a Bronze do Lakehouse (hoje `read_kafka()` para Oracle, sync direto para Postgres, Lakehouse Federation para MongoDB) para ler das external tables sobre o ADLS Gen2/Bronze e aplicar `APPLY CHANGES`/merge por `cdc_sequence` em lote.
9. Configurar o pipeline `COPY INTO` + `MERGE` do Synapse Dedicated a partir do ADLS Gen2/Bronze, aplicando SCD2.
9b. Configurar o reference data input do Stream Analytics apontando pro caminho do MongoDB no ADLS Gen2/Bronze, com padrão de atualização (path pattern) definido, e o join contra o stream do Event Hub para enriquecer Pedido/Restaurante.
10. Definir e documentar o mapeamento dos metadados de ordenação nativos do Debezium (SCN) e do Airbyte (`_ab_cdc_lsn`/`_ab_cdc_updated_at`) para o campo canônico `cdc_sequence`, cobrindo tanto a variante streaming (Event Hub) quanto a variante lote (ADLS).
11. Atualizar `docs/ROADMAP_ARQUITETURA_MULTICLOUD.md` (Fase 1), registrando o desenho decidido nesta feature — mesmo formato das subseções de Fase 2/3.

## Open Questions

- Dimensionamento do Event Hubs Namespace (throughput units, partições por tópico) e do Synapse Dedicated (DWU) — detalhar no `/define`.
- Formato exato do arquivo de sink do Kafka Connect para o ADLS (Avro/JSON/Parquet) e frequência de flush/rotação — impacta a frescura do dado no Warehouse/Lakehouse batch — a definir no `/define`.
- Mapeamento exato dos metadados de ordenação (SCN do Debezium vs. `_ab_cdc_lsn` do Airbyte) para `cdc_sequence` — pendência transversal já registrada no roadmap v1.4, ainda sem solução de design nesta rodada.
- Estratégia de autenticação do Databricks Unity Catalog contra o ADLS Gen2 (Service Principal vs. managed identity), dado que o workspace Free Edition fica fora da subscription Azure — detalhar no `/define`.
- Política de retomada/backfill do Kafka Connect (sink ADLS) em caso de falha prolongada — detalhar no `/define`.
- Frequência de atualização (path pattern) do reference data input do Stream Analytics contra a cópia do MongoDB no ADLS — impacta a frescura do enriquecimento de Pedido/Restaurante no Kappa; a definir no `/define`.

---

## Status: ✅ Complete (Defined)

**Revisão:** Brainstorm conduzido nesta sessão via `/brainstorm`, fechando a lacuna de artefato formal da Fase 1/Azure (única fase sem `BRAINSTORM_INGESTAO_*` dedicado) e revisando pontos específicos da decisão v1.4: adição de MinIO ao trilho batch, consolidação da Bronze do Lakehouse via external table sobre ADLS (com lote carregando CDC), e substituição da Lakehouse Federation do MongoDB por ingestão real via Airbyte. Próximo passo: `/define .claude/sdd/features/BRAINSTORM_INGESTAO_AZURE_FASE1.md`.
