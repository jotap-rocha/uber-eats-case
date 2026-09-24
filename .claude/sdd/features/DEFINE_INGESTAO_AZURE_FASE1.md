# DEFINE: Arquitetura de Ingestão — Fase 1 (Azure)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AZURE_FASE1 |
| **Fase do roadmap** | Fase 1 — Azure (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_INGESTAO_AZURE_FASE1.md` |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-12 |

---

## Problem Statement

A Fase 1 (Azure) já tinha a ferramenta de cada arquitetura fechada (Synapse Dedicated, Databricks Free Edition, Event Hubs+Stream Analytics) e um desenho de ingestão registrado no roadmap (v1.4), mas — ao contrário das Fases 2/AWS e 3/GCP — **nunca formalizado como artefato `BRAINSTORM_INGESTAO_*`**, vindo só de rodadas de `/intake` com revisão adversarial. Ao revisitar esse desenho, duas lacunas reais apareceram: (1) o MinIO só alimentava o trilho real-time, nunca o batch, deixando o Synapse/Lakehouse sem essa fonte; e (2) não havia decisão sobre como o Databricks deveria consumir o lote batch pousado no ADLS Gen2 (external table vs. ingestão para dentro do managed lake do Free Edition). A investigação dessa 2ª lacuna revelou uma tensão maior: **a Fase 0 já implementa ingestão real e funcional** para o Lakehouse (Oracle via `read_kafka()`/Redpanda com `APPLY CHANGES`, Postgres via sync direto Airbyte→Databricks, MongoDB via Lakehouse Federation) — migrar para Azure não é um simples "trocar de storage" como o roadmap assumia, é decidir se esses 3 mecanismos são preservados (mais rápido, mas heterogêneo) ou substituídos por um único padrão consolidado (mais lento de montar, mas mais simples de operar e documentar). Sem essa decisão fechada, a Fase 1 não pode avançar para `/design`/`/build`: não dá para desenhar o Terraform, escrever a Bronze do Databricks nem provisionar o Event Hubs sem saber que mecanismo cada fonte realmente usa.

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados avançando a Fase 1 (primeira cloud) do roadmap multi-cloud | Sem esta decisão fechada, a Fase 1 fica bloqueada antes de abrir a conta Azure — não é possível desenhar Terraform, estimar custo real (tier do Event Hubs), nem saber se o trabalho já pronto na Fase 0 (Bronze do Oracle via Kafka, sync do Postgres) será reaproveitado ou descartado |

## Goals

| Etapa | Prioridade | Meta |
|-------|------------|------|
| 1 (Warehouse + landing batch) | **MUST** | Configurar a 2ª conexão do **Airbyte** para Postgres em **modo CDC** (replication slot), destino **ADLS Gen2/Bronze** |
| 1 (Warehouse + landing batch) | **MUST** | Configurar o **Debezium/Kafka Connect** do Oracle com um sink dedicado gravando arquivos no ADLS Gen2/Bronze, preservando os campos de CDC (`op`/`before`/`after`/SCN) |
| 1 (Warehouse + landing batch) | **MUST** | Configurar o **Airbyte** para MongoDB (snapshot/full-refresh, sem CDC) e para MinIO, ambos com destino ADLS Gen2/Bronze |
| 1 (Warehouse + landing batch) | **MUST** | Configurar o **Synapse Dedicated** para `COPY INTO` + `MERGE` (SCD2) a partir do ADLS Gen2/Bronze, aplicando o contrato canônico de CDC |
| 2 (Lakehouse) | **MUST** | Provisionar a **storage credential** (Service Principal/managed identity) e a **external location** do Unity Catalog apontando pro mesmo container ADLS Gen2/Bronze da Etapa 1 — sem nenhuma ingestão nova |
| 2 (Lakehouse) | **MUST** | Reescrever a Bronze do Databricks (hoje `read_kafka()` para Oracle, sync direto Airbyte→Databricks para Postgres, Lakehouse Federation para MongoDB) para ler das **external tables** e aplicar `APPLY CHANGES`/upsert por `cdc_sequence` **em lote** |
| 3 (Kappa) | **MUST** | Provisionar o **Event Hubs Namespace em tier Standard** (pré-requisito para os tópicos internos compactados do Kafka Connect) |
| 3 (Kappa) | **MUST** | Configurar o destino nativo **"Kafka"** do Airbyte (Postgres, CDC/replication slot) apontando pro endpoint Kafka-compatível do Event Hub |
| 3 (Kappa) | **MUST** | Reapontar o **Kafka Connect do Debezium/Oracle** (`bootstrap.servers`) para o mesmo endpoint Kafka-compatível do Event Hub — 2º sink da mesma captura LogMiner, ao lado do sink ADLS da Etapa 1 |
| 3 (Kappa) | **MUST** | Configurar a **notificação de bucket nativa do MinIO** (destino Kafka) apontando direto pro Event Hub — sem componente-ponte |
| 3 (Kappa) | **MUST** | Configurar o job do **Stream Analytics** lendo do Event Hub, com **reference data input** apontando pro caminho do MongoDB no ADLS Gen2/Bronze, enriquecendo Pedido/Restaurante |
| 3 (Kappa) | **MUST** | Mapear os metadados de ordenação nativos do Debezium (SCN) e do Airbyte (`_ab_cdc_lsn`/`_ab_cdc_updated_at`) para o campo canônico `cdc_sequence`, cobrindo tanto a variante streaming (Event Hub) quanto a variante lote (ADLS) |
| — | **MUST** | Provisionar toda a infraestrutura acima via **Terraform** (ADLS Gen2, Synapse, Event Hubs — exceto o workspace Databricks Free Edition, fora da subscription), conforme princípio já fixado no roadmap (Seção 2) |
| — | **SHOULD** | Registrar logs estruturados no Kafka Connect/Debezium (2 sinks simultâneos por captura) — maior risco de falha silenciosa do que um conector com sink único |
| — | **SHOULD** | Recomendar `/pipeline-review-init` após o Build desta feature, mesma prática já usada nas Ondas 1-3 e nas Fases 2/AWS e 3/GCP |

## Sequenciamento (mitigação de risco)

Mesmo método já usado nas Ondas 1-3 (Fase 0) e nas Fases 2/AWS e 3/GCP: validar uma arquitetura de cada vez, não todas simultaneamente, para isolar risco e não sobrecarregar os sistemas on-premise (Postgres/Oracle/MongoDB/MinIO em Docker/ShadowTraffic) com capturas concorrentes.

| Etapa | Escopo | Por que nessa ordem |
|-------|--------|----------------------|
| **1** | Warehouse + landing batch: Airbyte (Postgres CDC, MongoDB snapshot, MinIO) + Debezium sink dedicado (Oracle) → ADLS Gen2/Bronze → Synapse Dedicated | Primeira e única captura de CDC nesta fase até este ponto — 1 captura por fonte relacional, sem concorrência |
| **2** | Lakehouse: storage credential + external tables sobre o mesmo ADLS Gen2/Bronze da Etapa 1 | Zero ingestão nova — reaproveita a landing já validada na Etapa 1, sem tocar nos bancos on-premise de novo. Também a etapa em que o trabalho já existente na Fase 0 (`read_kafka()`, sync direto, Federation) é oficialmente descontinuado em favor do padrão único |
| **3** | Kappa: Event Hubs Namespace + 2º sink do Debezium/Oracle + destino Kafka do Airbyte/Postgres + notificação nativa do MinIO + Stream Analytics (com reference data input) | Única etapa que introduz uma **2ª captura CDC concorrente do Postgres** (2º replication slot, independente do da Etapa 1) e um **2º sink na mesma captura LogMiner do Oracle** — janela de risco conhecida e limitada, última etapa desta fase |

**Decisão explícita:** o risco de concorrência de CDC no Postgres (Assumption A-002) não é eliminado pelo desenho, mas é **confinado à Etapa 3** — mesma lógica de mitigação já aplicada nas Fases 2/AWS (A-003) e 3/GCP (A-003). Diferente das outras 2 clouds, o Oracle **não** introduz uma 2ª captura concorrente aqui — é a mesma captura LogMiner do Debezium ganhando um 2º sink (Assumption A-001), um risco de natureza diferente (falha de um sink não deve derrubar o outro).

## Success Criteria

- [ ] 2ª conexão do Airbyte ativa para Postgres, modo CDC/replication slot, destino ADLS Gen2/Bronze
- [ ] Debezium/Kafka Connect do Oracle com sink dedicado gravando arquivos no ADLS Gen2/Bronze, preservando `op`/`before`/`after`/SCN
- [ ] Conexões do Airbyte ativas para MongoDB (snapshot/full-refresh) e MinIO, ambas com destino ADLS Gen2/Bronze
- [ ] Synapse Dedicated executa `COPY INTO` + `MERGE` com sucesso a partir do ADLS Gen2/Bronze, aplicando SCD2
- [ ] Storage credential + external location do Unity Catalog provisionadas, apontando pro container ADLS Gen2/Bronze
- [ ] Bronze do Databricks lê das external tables e aplica `APPLY CHANGES`/upsert por `cdc_sequence` em lote — nenhuma referência restante a `read_kafka()`/Redpanda, sync direto Airbyte→Databricks ou Lakehouse Federation
- [ ] Event Hubs Namespace provisionado em tier Standard
- [ ] Destino "Kafka" do Airbyte (Postgres real-time) e `bootstrap.servers` do Kafka Connect (Oracle real-time) apontando pro endpoint Kafka-compatível do Event Hub, sem componente-ponte
- [ ] Notificação de bucket nativa do MinIO publicando direto no Event Hub
- [ ] Stream Analytics processa eventos do Event Hub e enriquece Pedido/Restaurante via reference data input contra a cópia do MongoDB no ADLS
- [ ] Campo `cdc_sequence` preenchido de forma consistente e ordenável, a partir do Debezium (SCN) e do Airbyte (`_ab_cdc_lsn`), tanto na variante streaming quanto na variante lote
- [ ] Toda a infraestrutura acima (exceto o workspace Databricks Free Edition) existe como código Terraform versionado — 0 recursos criados manualmente no portal Azure

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Airbyte Postgres CDC batch | 2ª conexão Airbyte (modo CDC) configurada, destino ADLS | Um `UPDATE` ocorre em `drivers` no Postgres | O arquivo/registro correspondente aparece no ADLS Gen2/Bronze, com metadados `_ab_cdc_*` preservados |
| AT-002 | Airbyte Postgres CDC real-time | Destino "Kafka" do Airbyte configurado pro Event Hub (Etapa 3) | O mesmo tipo de `UPDATE` ocorre | O evento aparece no tópico do Event Hub em poucos segundos, sem passar pelo ADLS |
| AT-003 | Debezium Oracle — sink ADLS | Kafka Connect com sink dedicado ADLS configurado | Um `UPDATE` de status ocorre em `orders`/`payments` no Oracle | O arquivo aparece no ADLS Gen2/Bronze com `op`/`before`/`after`/SCN preservados |
| AT-004 | Debezium Oracle — sink Event Hub | Kafka Connect com `bootstrap.servers` apontando pro Event Hub (Etapa 3) | O mesmo `UPDATE` ocorre | O evento aparece no Event Hub em poucos segundos — falha em um sink não impede o outro |
| AT-005 | Airbyte MongoDB snapshot | Conexão Airbyte (snapshot/full-refresh) configurada | Sync executado | Dados aparecem no ADLS Gen2/Bronze; nenhum stream de CDC contínuo existe para o MongoDB |
| AT-006 | Airbyte MinIO batch | Conexão Airbyte configurada, destino ADLS | Sync executado | Objetos do MinIO aparecem no ADLS Gen2/Bronze |
| AT-007 | Notificação nativa MinIO → Event Hub | Notificação de bucket (destino Kafka) configurada | Um objeto novo é escrito no MinIO | O evento aparece no Event Hub sem componente-ponte intermediário |
| AT-008 | Synapse consome do ADLS | Dados presentes no ADLS Gen2/Bronze | `COPY INTO` + `MERGE` executado | Tabela do Synapse Dedicated atualizada com SCD2 aplicado |
| AT-009 | Databricks external table + APPLY CHANGES | External tables configuradas sobre o ADLS Gen2/Bronze | Pipeline Bronze do Databricks executado | Tabela Bronze atualizada via `APPLY CHANGES`/upsert por `cdc_sequence`; nenhum job usa mais `read_kafka()`, sync direto ou Federation |
| AT-010 | Stream Analytics + reference data | Job do Stream Analytics rodando, reference data input configurado contra a cópia do MongoDB no ADLS | Um evento de Pedido chega no Event Hub | O evento sai enriquecido com dado do MongoDB (menu/horário), sem acessar o ADLS via outro caminho |
| AT-011 | `cdc_sequence` mapeado (streaming + lote) | Evento processado via Airbyte ou Debezium chega no Event Hub ou no ADLS | Inspecionar o schema/valor da coluna em ambos os destinos | `cdc_sequence` preenchido de forma consistente e ordenável nas duas variantes |
| AT-012 | Infraestrutura via Terraform | Todos os recursos (exceto workspace Databricks Free Edition) definidos como módulo/config Terraform | `terraform plan`/`apply` executado | Nenhum recurso precisa ser criado manualmente no portal Azure |

## Out of Scope

| Item | Por que fica para depois |
|------|-----------------------------|
| Reaproveitar o `read_kafka()`/Redpanda do Oracle e o sync direto Airbyte→Databricks do Postgres | Avaliado e descartado no brainstorm — usuário priorizou um único padrão de ingestão (external table) para o Lakehouse, mesmo custando descartar trabalho já pronto |
| Lakehouse Federation para o MongoDB | Descartada no brainstorm — usuário quer ingestão real (Airbyte), não consulta federada ao vivo |
| Snapshot simples (sem CDC) para o lote batch de Postgres/Oracle | Avaliado e descartado no brainstorm — perderia o histórico de mutação da Onda 3 |
| Event Hub lendo do ADLS Gen2 além do MinIO/Postgres/Oracle diretos | Avaliado e descartado no brainstorm — mantém a decisão original de o Kappa nunca ler do trilho batch (evita repetir o "Lambda architecture disfarçado" já descartado na v1.4) |
| Componente-ponte (Lambda/Cloud Function equivalente) entre Airbyte/Debezium/MinIO e o Event Hub | Confirmado no brainstorm que todos falam Kafka nativamente contra o endpoint do Event Hub, sem intermediário — diferente da AWS e da GCP |
| Dimensionamento fino do Event Hubs Namespace (throughput units/partições) e do Synapse Dedicated (DWU) | Detalhe de implementação — fica para o `/design` |
| Formato exato do arquivo de sink do Kafka Connect para o ADLS (Avro/JSON/Parquet) e frequência de flush/rotação | Decisão de performance/frescura — fica para o `/design` |
| Mapeamento exato dos metadados de ordenação (SCN do Debezium vs. `_ab_cdc_lsn` do Airbyte) para `cdc_sequence` | Pendência transversal já registrada no roadmap (v1.4) — fica para o `/design` desta feature |

## Constraints

- Kafka Connect (usado pelo Debezium) exige tópicos internos compactados (`connect-offsets`/`connect-configs`/`connect-status`), suportados só a partir do tier **Standard** do Event Hubs Namespace — não Basic
- O Postgres precisa suportar **2 replication slots simultâneos** a partir da Etapa 3 (1 batch/ADLS da Etapa 1 + 1 real-time/Event Hub da Etapa 3) — capacidade do self-hosted a validar
- O Oracle usa **1 única captura LogMiner** (Debezium) com **2 sinks** (ADLS + Event Hub) — não deve ser tratado como 2 capturas independentes; falha em um sink não pode derrubar o outro
- MongoDB continua sem sink de escrita/CDC no ShadowTraffic (decisão da Onda 3) — nenhuma parte desta feature pode assumir que o MongoDB muta
- MinIO não tem conector de CDC — só Airbyte (batch) e notificação nativa de bucket (real-time)
- O trilho real-time (Kappa) não pode depender do ADLS Gen2/trilho batch em nenhum ponto — decisão explícita de manter dois trilhos separados, mesmo princípio das Fases 2/3
- Toda credencial (Airbyte, Debezium/Kafka Connect, Unity Catalog storage credential, Event Hub) deve seguir a mesma disciplina já aplicada nas fases anteriores: nunca versionada, sempre via secret manager/variável Terraform
- Custo: Event Hubs Standard não é o tier mais barato (exceção ao princípio serverless/on-demand da Seção 2), mas é o mínimo necessário para Kafka Connect funcionar
- O workspace Databricks Free Edition fica fora da subscription Azure — Terraform não o provisiona; DAB cobre jobs/pipelines via Service Principal ou PAT
- As 3 arquiteturas (Warehouse, Lakehouse, Kappa) são construídas e validadas **em ordem, uma de cada vez** — mesmo método de mitigação de risco já usado nas Ondas 1-3 e nas Fases 2/3. A 2ª captura/sink real-time (Postgres/Oracle) e o Event Hubs Namespace só existem a partir da Etapa 3, a última desta fase

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | O Kafka Connect do Debezium/Oracle consegue manter 2 sinks simultâneos (arquivo ADLS + Event Hub) a partir de uma única captura LogMiner, sem duplicar nem perder eventos entre os sinks | Se não suportar, pode ser necessário 2 conectores Debezium independentes (2 capturas LogMiner concorrentes), reintroduzindo pro Oracle o mesmo risco de concorrência que hoje só existe pro Postgres | [ ] Validar no início do `/design` |
| A-002 | O Postgres self-hosted suporta 2 replication slots simultâneos (batch da Etapa 1 + real-time da Etapa 3) sem degradar performance nem exceder `max_replication_slots` | Se não suportar, pode ser necessário reduzir para 1 captura com fan-out (como no Oracle), redesenhando a Etapa 3 | [ ] Validar no `/design`. **Risco parcialmente mitigado pelo sequenciamento:** o 2º slot só é criado na Etapa 3, a última desta fase |
| A-003 | O tier **Standard** do Event Hubs Namespace suporta plenamente os tópicos internos compactados exigidos pelo Kafka Connect, sem workaround adicional (achado do brainstorm baseado em documentação, ainda não validado num ambiente Azure real) | Se não suportar plenamente, pode ser necessário tier Premium/Dedicated, alterando a estimativa de custo da fase | [ ] Validar no `/design`, antes de comprometer o orçamento |
| A-004 | O Databricks Unity Catalog (Free Edition, workspace fora da subscription Azure) consegue autenticar contra o ADLS Gen2 via Service Principal/managed identity sem exigir uma configuração de rede especial (o workspace não está na mesma VNet do storage) | Se houver restrição, pode ser necessário liberar acesso público controlado no ADLS ou usar um mecanismo de conectividade adicional | [ ] Validar no `/design` |

## Requisitos operacionais de pipeline (mandato)

Esta feature introduz ingestão nova para o medalhão (Bronze via ADLS Gen2) e um trilho de streaming real (Event Hub) — o sinal `medalhão bronze silver gold` + `landing raw csv json parquet` + `unity catalog pipeline` de `PIPELINE_MANDATORY_PRACTICES.yaml` se aplica.

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **MUST** — DC-M04 aplica diretamente | O mapeamento dos metadados de ordenação do Debezium (SCN) e do Airbyte (`_ab_cdc_lsn`) para `cdc_sequence` (Meta/AT-011) precisa cobrir, pela 1ª vez no projeto, **duas variantes do mesmo dado** (streaming via Event Hub, lote via ADLS) — mais exigente que o mapeamento único já feito pra Onda 3, AWS e GCP. Documento operacional formal (DC-M01) segue N/A justificado — projeto de portfólio pessoal, o próprio roadmap + este DEFINE cumprem o papel comunicativo |
| Medalhão e UC (MED-M01-04) | **MUST** — MED-M01, MED-M02 e MED-M04 aplicam | MED-M01: Bronze via external table sobre o ADLS precisa preservar linhagem (`_ingest_ts`, `_source_file`, `_run_id`) mesmo sem Auto Loader tradicional. MED-M02: Silver/Gold seguem projeção explícita, sem `select *`, já convenção do projeto. MED-M04: **simplificação real desta fase** — como o Databricks não consome mais o Event Hub (Decisão #3 do brainstorm), não há o risco de "dupla leitura da mesma mudança gerando 2 efeitos" que AWS e GCP tiveram entre os 2 trilhos; a idempotência fica concentrada no `APPLY CHANGES`/`MERGE` por `cdc_sequence` do lado ADLS→Databricks/Synapse |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Esta feature define topologia de ingestão, não introduz um novo pipeline de qualidade — segue o mesmo padrão de tipagem defensiva já usado no projeto |
| Schema drift (SD-M01-04) | **N/A justificado** | Sem Auto Loader com schema variável — os geradores têm schema fixo, e Airbyte/Debezium replicam esquema já definido nas fontes relacionais |
| Teams / alertas (TM-M01-06) | **SHOULD** — TM-M01 recomendado, não MUST | O Kafka Connect com 2 sinks simultâneos (Oracle) é o componente com maior risco de falha silenciosa parcial (um sink cai, o outro continua) — recomenda-se alerta operacional, mas sem SLA de produção 24/7 que torne isso bloqueante |
| Observabilidade (OBS-M01-03) | **SHOULD** — OBS-M01 recomendado para o Kafka Connect (2 sinks) | Logs estruturados ajudam a diferenciar falha de sink ADLS vs. sink Event Hub, dado que são independentes; sem SLA de freshness formal |
| Erros e resiliência (ERR-M01-02) | Fica para o `/design` | Fail-fast e distinção de tipos de erro (falha de sink vs. schema vs. limite de replication slot) são detalhamento de implementação |
| Segurança (GOV-M01-02) | **MUST — as duas aplicam** | GOV-M01: credenciais (Airbyte, Debezium/Kafka Connect, Event Hub, storage credential) nunca versionadas, sempre via secret manager/variável Terraform. **GOV-M02 (grants UC) aplica nesta fase** — diferente da AWS e da GCP (N/A lá, sem Unity Catalog): a external location/external table sobre o ADLS Gen2 exige checklist de grants explícito |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 aplica | Recomenda-se `/pipeline-review-init` após o Build desta feature, mesma prática das Ondas 1-3 e das Fases 2/3 |
| PyODBC (PYODBC-M01-05) | **N/A** | Não há PyODBC/SQL Server nesta feature |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, específico — as 2 lacunas originais (MinIO fora do batch, mecanismo do Databricks indefinido) e a tensão real descoberta (reaproveitar vs. substituir a ingestão já funcional da Fase 0) estão explicitamente identificadas e resolvidas |
| Users | 2/3 | Único usuário/persona (projeto pessoal) |
| Goals | 3/3 | Priorizados MUST/SHOULD, sequenciados por etapa, cada um ligado a um componente e mecanismo técnico específico já validado no brainstorm |
| Success | 3/3 | Critérios testáveis via inspeção de conexão Airbyte, sink do Kafka Connect, tópico do Event Hub, query no Synapse/Databricks |
| Scope | 3/3 | Fora de escopo, constraints e assumptions delimitam claramente o que fica para o `/design`, incluindo os 2 riscos técnicos mais sensíveis (concorrência de replication slot no Postgres, dual-sink no Oracle) |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

- Dimensionamento do Event Hubs Namespace (throughput units, partições por tópico) e do Synapse Dedicated (DWU) — detalhar no `/design`
- Formato exato do arquivo de sink do Kafka Connect para o ADLS (Avro/JSON/Parquet) e frequência de flush/rotação — impacta a frescura do dado no Warehouse/Lakehouse batch — a definir no `/design`
- Mapeamento exato dos metadados de ordenação (SCN do Debezium vs. `_ab_cdc_lsn` do Airbyte) para `cdc_sequence`, nas 2 variantes (streaming/lote) — detalhar no `/design` (ver DC-M04)
- Se o Postgres self-hosted suporta 2 replication slots concorrentes sem degradar performance — spike técnico recomendado no início do `/design` (ver A-002)
- Se o Kafka Connect do Debezium/Oracle suporta 2 sinks simultâneos de forma independente (falha isolada) — validar no `/design` (ver A-001)
- Se o tier Standard do Event Hubs realmente cobre os tópicos internos do Kafka Connect sem workaround — validar no `/design` antes de comprometer o orçamento (ver A-003)
- Estratégia de autenticação do Unity Catalog contra o ADLS Gen2 (Service Principal vs. managed identity), dado que o workspace Free Edition fica fora da subscription — detalhar no `/design` (ver A-004)
- Política de retomada/backfill do Kafka Connect (sink ADLS) em caso de falha prolongada — detalhar no `/design`
- Frequência de atualização (path pattern) do reference data input do Stream Analytics contra a cópia do MongoDB no ADLS — impacta a frescura do enriquecimento de Pedido/Restaurante — a definir no `/design`

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-09-12 | Documento inicial, extraído de `BRAINSTORM_INGESTAO_AZURE_FASE1.md`. Todas as 7 decisões de escopo já haviam sido fechadas no brainstorm — extração direta, sem nova rodada de perguntas. Adicionado sequenciamento em 3 etapas (Warehouse/landing batch → Lakehouse → Kappa), mesma disciplina de mitigação de risco das Fases 2/AWS e 3/GCP, com uma assimetria nova registrada: o Oracle introduz risco de dual-sink (1 captura, 2 destinos), não de dupla captura concorrente como o Postgres. Também identificado que, diferente da AWS/GCP, esta feature ativa **GOV-M02 (grants UC)** por usar Unity Catalog |

---

## Status: ✅ Complete (Defined)

**Próximo passo:** `/design .claude/sdd/features/DEFINE_INGESTAO_AZURE_FASE1.md`
