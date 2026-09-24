# DEFINE: Arquitetura de Ingestão — Fase 3 (GCP)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_GCP_FASE3 |
| **Fase do roadmap** | Fase 3 — GCP (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_INGESTAO_GCP_FASE3.md` |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-11 |

---

## Problem Statement

O roadmap registrava a Fase 3 (GCP) como **🔶 sob avaliação**: a ferramenta de cada arquitetura (BigQuery, BigLake/Dataproc+Iceberg, Pub/Sub+Dataflow) já estava fechada, mas o desenho fino de ingestão — como as 4 fontes da Fase 0 (Postgres, Oracle, MongoDB, MinIO) alimentam esses 3 destinos — tinha só achados soltos, com duas pendências técnicas reais não resolvidas: (1) o Datastream não tem Pub/Sub como destino nativo (só BigQuery, Cloud Storage e BigLake Iceberg), o que travava o trilho real-time; e (2) não havia ferramenta de catalogação/governança do lakehouse definida, papel que o Unity Catalog e o AWS Glue cobrem nas outras duas fases. Havia também a mesma ambiguidade não resolvida que a Fase 2/AWS já havia enfrentado com o princípio "Portabilidade de motor por camada" (v1.2): a redação original previa Oracle/MinIO substituídos por motores nativos GCP, o que — se mantido — invalidaria o desenho de reaproveitar os sistemas self-hosted da Fase 0. Sem esse desenho fechado, a Fase 3 não pode avançar para `/design`/`/build`.

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados avançando a Fase 3 do roadmap multi-cloud | Sem esta decisão fechada, a Fase 3 fica bloqueada antes mesmo de abrir a conta GCP — não é possível desenhar Terraform, estimar custo real ou validar se o Kappa GCP vai ser genuinamente comparável ao das Fases 1/2 em rigor arquitetural |

## Goals

| Etapa | Prioridade | Meta |
|-------|------------|------|
| 1 (Warehouse) | **MUST** | Provisionar um bastion (GCE VM pública mínima) na VPC da Fase 3, com túnel SSH reverso (`autossh`/systemd na máquina local) mantendo Postgres/Oracle/MongoDB acessíveis ao Datastream via "Forward SSH tunnel connectivity profile" — sem migrar a Fase 0 para a nuvem |
| 1 (Warehouse) | **MUST** | Configurar 3 connection profiles + streams do **Datastream** (Postgres CDC, Oracle CDC via LogMiner, MongoDB full load/snapshot), destino GCS/Bronze, materializados como **tabelas Iceberg do BigLake** |
| 1 (Warehouse) | **MUST** | Configurar **Storage Transfer Service** com fonte "S3-compatible" apontando para o MinIO (via agente local, outbound), destino GCS/Bronze, com agendamento definido |
| 1 (Warehouse) | **MUST** | Configurar o job/pipeline `LOAD`/`MERGE` do **BigQuery** a partir dos arquivos brutos do GCS/Bronze para o storage nativo do BigQuery — carga física, sem query-in-place, aplicando o contrato canônico de CDC |
| 2 (Lakehouse) | **MUST** | Configurar **Dataplex Universal Catalog** sobre as tabelas Iceberg do BigLake (GCS/Bronze) já materializadas na Etapa 1 — sem nenhuma ingestão nova |
| 2 (Lakehouse) | **MUST** | Configurar **Dataproc** para processamento/consulta dessas mesmas tabelas Iceberg |
| 3 (Kappa) | **MUST** | Adicionar **Debezium Server** como novo serviço no `docker-compose.yml` local, capturando CDC de Postgres (logical decoding) e Oracle (LogMiner), com sink direto no **Pub/Sub** — trilho independente do Datastream, sem passar pelo GCS |
| 3 (Kappa) | **MUST** | Implementar a **Cloud Function ponte**: recebe a notificação de bucket (Webhook) do MinIO, publica no Pub/Sub |
| 3 (Kappa) | **MUST** | Implementar o pipeline **Dataflow** consumidor do Kappa: lê eventos exclusivamente do Pub/Sub, com **lookup/enriquecimento** contra a cópia do MongoDB já materializada como tabela Iceberg (ex.: menu/horário do restaurante ao processar um evento de Pedido) |
| 3 (Kappa) | **MUST** | Mapear os metadados de ordenação nativos do Datastream e do Debezium Server para o campo canônico `cdc_sequence` já definido no contrato de CDC da Onda 3 |
| — | **MUST** | Provisionar toda a infraestrutura acima via **Terraform** (sem criação manual de recursos GCP), conforme princípio já fixado no roadmap (Seção 2) |
| — | **SHOULD** | Registrar logs estruturados na Cloud Function ponte (MinIO→Pub/Sub) — é um componente customizado novo (não um conector gerenciado), com maior risco de falha silenciosa do que os demais caminhos |
| — | **SHOULD** | Recomendar `/pipeline-review-init` após o Build desta feature, mesma prática já usada nas Ondas 1/2/3 e na Fase 2/AWS |

## Sequenciamento (mitigação de risco)

Mesmo método já usado nas Ondas 1-3 (Fase 0) e na Fase 2/AWS: validar uma arquitetura de cada vez, não todas simultaneamente, para isolar risco e não sobrecarregar os sistemas on-premise (Postgres/Oracle/MongoDB/MinIO em Docker/ShadowTraffic) com leituras de CDC concorrentes — aqui agravado pelo fato de o Datastream (Etapa 1) e o Debezium Server (Etapa 3) serem **duas ferramentas diferentes** lendo potencialmente o mesmo replication slot (Postgres) ou o mesmo LogMiner (Oracle).

| Etapa | Escopo | Por que nessa ordem |
|-------|--------|----------------------|
| **1** | Warehouse: bastion + túnel SSH + Datastream (Postgres/Oracle/Mongo) → GCS/Bronze → BigLake Iceberg + Storage Transfer Service (MinIO) → BigQuery `LOAD`/`MERGE` | Primeira e única fonte de CDC no on-premise até este ponto (Datastream) — isola o risco da conectividade (túnel SSH) antes de somar uma 2ª ferramenta de captura |
| **2** | Lakehouse: Dataplex Universal Catalog + Dataproc sobre o mesmo GCS/Bronze da Etapa 1 | Zero ingestão nova — reaproveita o Datastream/STS já validado na Etapa 1, sem tocar nos bancos on-premise de novo |
| **3** | Kappa: Debezium Server (Postgres/Oracle → Pub/Sub) + Cloud Function ponte (MinIO) + Dataflow consumidor com lookup no MongoDB | Única etapa com 2 ferramentas de captura concorrentes por fonte (Datastream + Debezium Server, Postgres/Oracle) — janela de risco conhecida e limitada, última etapa da fase antes da Fase 4 (Consolidação) |

**Decisão explícita:** o risco de concorrência entre Datastream e Debezium Server lendo a mesma fonte (Assumption A-003) não é eliminado pelo desenho, mas é **confinado à Etapa 3** — mesma lógica de mitigação já aplicada na Fase 2/AWS (A-003 daquela feature).

## Success Criteria

- [ ] Bastion (GCE VM) provisionado; túnel SSH reverso (`autossh`) ativo e resiliente a partir da máquina local
- [ ] 3 streams do Datastream ativos (Postgres CDC, Oracle CDC, MongoDB full load), todos via "Forward SSH tunnel connectivity profile", destino GCS/Bronze
- [ ] Tabelas Iceberg do BigLake materializadas sobre o GCS/Bronze para Postgres, Oracle e MongoDB
- [ ] Storage Transfer Service com fonte "S3-compatible" configurada para o MinIO; sync agendado executa com sucesso e os objetos aparecem no GCS/Bronze
- [ ] BigQuery executa `LOAD`/`MERGE` com sucesso a partir do GCS/Bronze, para dentro do seu storage nativo — nenhuma consulta via BigLake/query-in-place usada como consumo do Warehouse
- [ ] Dataplex Universal Catalog cataloga as tabelas Iceberg do BigLake; Dataproc consulta/processa essas tabelas com sucesso
- [ ] Debezium Server ativo (container no `docker-compose.yml` local), capturando CDC de Postgres e Oracle, publicando eventos no Pub/Sub
- [ ] Notificação de bucket do MinIO (destino Webhook) aciona a Cloud Function ponte, que publica no Pub/Sub com sucesso — evento visível no tópico em segundos, não em lote
- [ ] Pipeline Dataflow processa eventos do Pub/Sub e enriquece com lookup na tabela Iceberg do MongoDB, sem consultar o Pub/Sub para isso
- [ ] Campo `cdc_sequence` preenchido de forma consistente e ordenável a partir dos metadados nativos do Datastream e do Debezium Server, alinhado ao contrato canônico da Onda 3
- [ ] Toda a infraestrutura acima existe como código Terraform versionado — 0 recursos criados manualmente no console GCP
- [ ] A conectividade de rede GCP↔sistemas self-hosted está documentada e validada (Datastream consegue abrir replication slot/LogMiner/change stream remotamente via túnel)

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Datastream Postgres batch | Stream Datastream (CDC) configurado via túnel SSH | Um `UPDATE` ocorre em `drivers` no Postgres | O evento aparece na tabela Iceberg do BigLake sobre o GCS/Bronze, no intervalo de entrega configurado |
| AT-002 | Datastream Oracle batch | Stream Datastream (CDC/LogMiner) configurado via túnel | Um `UPDATE` ocorre em `orders`/`payments` no Oracle | Mesmo comportamento do AT-001, para Oracle |
| AT-003 | Datastream MongoDB full load | Stream Datastream (full load/snapshot) configurado | Stream executado | Dados aparecem na tabela Iceberg do BigLake; nenhum stream de CDC contínuo existe para o MongoDB |
| AT-004 | Storage Transfer Service MinIO | Fonte "S3-compatible" configurada, agente local ativo | O sync agendado roda | Novos objetos do MinIO aparecem no GCS/Bronze |
| AT-005 | BigQuery carga física | Dados presentes no GCS/Bronze | `LOAD`/`MERGE` executado no BigQuery | Tabela BigQuery (storage nativo) atualizada; nenhuma consulta do Warehouse é feita via BigLake/query-in-place |
| AT-006 | Dataplex + Dataproc consomem o Iceberg | Tabelas Iceberg cadastradas no Dataplex Universal Catalog | Query/job executado no Dataproc | Retorna dado correto e atualizado, sem ingestão adicional |
| AT-007 | Debezium Server Postgres real-time | Debezium Server capturando Postgres (logical decoding), sink Pub/Sub | Um `UPDATE` ocorre em `drivers` no Postgres | O evento aparece no tópico Pub/Sub em poucos segundos, sem passar pelo GCS |
| AT-008 | Debezium Server Oracle real-time | Debezium Server capturando Oracle (LogMiner), sink Pub/Sub | Um `UPDATE` ocorre em `orders`/`payments` no Oracle | Mesmo comportamento do AT-007, para Oracle |
| AT-009 | Cloud Function ponte MinIO → Pub/Sub | Notificação de bucket do MinIO configurada (destino Webhook) | Um objeto novo é escrito no MinIO | A Cloud Function recebe o evento e publica no Pub/Sub com sucesso; evento visível no tópico |
| AT-010 | Dataflow com lookup no MongoDB | Pipeline Dataflow rodando, cópia Iceberg do MongoDB disponível | Um evento de Pedido chega no Pub/Sub | O consumidor enriquece o evento com dado do MongoDB (lido da tabela Iceberg), sem acessar o Pub/Sub para isso |
| AT-011 | `cdc_sequence` mapeado | Evento processado via Datastream ou Debezium Server chega na Bronze | Inspecionar o schema/valor da coluna | `cdc_sequence` preenchido de forma consistente e ordenável, conforme o contrato canônico, para ambas as ferramentas |
| AT-012 | Infraestrutura via Terraform | Todos os recursos acima definidos como módulo/config Terraform | `terraform plan`/`apply` executado | Nenhum recurso precisa ser criado manualmente no console GCP |

## Out of Scope

| Item | Por que fica para depois |
|------|-----------------------------|
| BigQuery consultando BigLake Iceberg em tempo de execução (query-in-place) | Avaliado e descartado no brainstorm — decisão do usuário por performance e por paridade de método com Redshift/Synapse na comparação da Fase 4 |
| CDC/mutação real para MongoDB | Fonte estática por decisão já fechada na Onda 3 — não é escopo desta feature reabrir isso |
| Substituir Oracle/MinIO por motores nativos GCP (Cloud SQL/GCS direto) | Decisão explicitamente fechada nesta rodada de `/define` (ver Problem Statement) — princípio v1.2/v1.6 do roadmap estendido para a Fase 3 (v1.7) |
| Migrar a Fase 0 para uma GCE VM (espelhando a EC2 da AWS) | Avaliado e descartado no brainstorm — usuário optou por manter containers locais + túnel SSH, aceitando o custo operacional do bastion |
| Dimensionamento fino do tipo de GCE VM (bastion) e dos workers do Dataflow | Detalhe de implementação — fica para o `/design` |
| Mecanismo exato do side input do Dataflow para o lookup no MongoDB (refresh periódico vs. reload por notificação) | Decisão de performance — fica para o `/design` |
| Estratégia de retomada/backfill do Debezium Server em caso de queda prolongada do túnel ou do próprio container | Detalhamento operacional — fica para o `/design` |

## Constraints

- Todo componente de ingestão pull-based (Datastream) precisa do túnel SSH reverso via bastion — sem isso, nenhum stream consegue sequer abrir conexão inicial; componentes push-based (Debezium Server, Cloud Function) não têm essa dependência
- MongoDB continua sem sink de escrita/CDC no ShadowTraffic (decisão da Onda 3) — nenhum stream ou pipeline desta feature pode assumir que o MongoDB muta
- Datastream não tem conector para object storage genérico — MinIO precisa necessariamente do Storage Transfer Service, não pode ser tratado como fonte Datastream
- Datastream não tem Pub/Sub como destino nativo — qualquer necessidade de streaming real a partir de Postgres/Oracle precisa passar pelo Debezium Server, nunca pelo Datastream
- O trilho real-time (Kappa) não pode depender do GCS/trilho batch em nenhum ponto — decisão explícita de manter dois trilhos separados, mesmo princípio das Fases 1/2
- BigQuery sempre carrega fisicamente do GCS/Bronze para seu storage nativo — nenhuma consulta de consumo do Warehouse pode ser feita via BigLake/query-in-place (decisão explícita do usuário)
- Toda credencial (Datastream connection profiles, Debezium Server, Cloud Function, Storage Transfer Service) deve seguir a mesma disciplina já aplicada nas fases anteriores: nunca versionada, sempre via secret manager/variável Terraform
- Custo de cada serviço deve favorecer serverless/on-demand por padrão, conforme princípio já fixado no roadmap (Seção 2)
- As 3 arquiteturas (Warehouse, Lakehouse, Kappa) são construídas e validadas **em ordem, uma de cada vez**, nunca todas simultaneamente desde o início — mesmo método de mitigação de risco já usado nas Ondas 1-3 e na Fase 2/AWS. O Debezium Server (trilho real-time) só existe a partir da Etapa 3, a última desta fase

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | O túnel SSH reverso (bastion GCE + `autossh`/systemd) consegue se manter estável o suficiente para o Datastream operar de forma contínua, sem exigir intervenção manual frequente | Se o túnel cair com frequência, a Fase 3 precisa reconsiderar a decisão desta rodada e migrar para uma GCE VM replicando a Fase 0 (Abordagem D, rejeitada no brainstorm) | [ ] Validar no início do `/design`, antes de comprometer o restante do desenho |
| A-002 | O Datastream e o Debezium Server expõem metadados de ordenação suficientes para reconstruir o `cdc_sequence` canônico, de forma similar ao que já foi mapeado para Airbyte/Debezium-Oracle na Onda 3 e para o DMS na Fase 2 | Se os metadados de qualquer uma das duas ferramentas forem insuficientes ou tiverem formato muito diferente, o contrato canônico de CDC pode precisar de um shim mais complexo do que o previsto | [ ] Confirmar no `/design`, mesma disciplina da Onda 3 e da Fase 2 |
| A-003 | O Datastream (Etapa 1) e o Debezium Server (Etapa 3) conseguem coexistir lendo a mesma fonte (replication slot do Postgres, LogMiner do Oracle) sem exceder limites de conexão concorrente do banco self-hosted | Se o motor de origem não suportar 2 leituras concorrentes de CDC por ferramentas diferentes, pode ser necessário desenhar um fan-out único (ex.: só Debezium Server, com um sink adicional simulando o papel do Datastream) | [ ] Validar no `/design`, especialmente para o Oracle (LogMiner tem histórico de restrições de concorrência — mesmo risco já registrado na Fase 2/AWS, A-003). **Risco parcialmente mitigado pelo sequenciamento:** o Debezium Server só é ativado na Etapa 3, a última do roadmap desta fase |
| A-004 | O consumidor Dataflow consegue fazer lookup na tabela Iceberg do MongoDB com latência aceitável, via side input com refresh periódico, sem precisar de um cache/side-table dedicado adicional | Se a latência for proibitiva, o `/design` precisa especificar um cache dedicado (ex. Memorystore/Redis) alimentado a partir do GCS/Bronze | [ ] Avaliar no `/design` |

## Requisitos operacionais de pipeline (mandato)

Esta feature introduz ingestão nova para o medalhão (Bronze via GCS) e um trilho de streaming real (Pub/Sub) — o sinal `medalhão bronze silver gold` + `landing raw csv json parquet` de `PIPELINE_MANDATORY_PRACTICES.yaml` se aplica.

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **MUST** — DC-M04 aplica diretamente | O mapeamento dos metadados de ordenação do Datastream e do Debezium Server para `cdc_sequence` (Meta/AT-011) é o mesmo checklist de schema/formato drift entre ferramentas de ingestão (DC-M04) já antecipado na Onda 3 e feito para o DMS na Fase 2 — agora precisa cobrir uma 4ª e 5ª ferramenta. Documento operacional formal (DC-M01) segue N/A justificado — projeto de portfólio pessoal, o próprio roadmap + este DEFINE cumprem o papel comunicativo |
| Medalhão e UC (MED-M01-04) | **MUST** — MED-M01, MED-M02 e MED-M04 aplicam | MED-M01: Bronze em GCS precisa preservar linhagem (`_ingest_ts`, `_source_stream`/`_run_id`) mesmo vindo de Datastream/Storage Transfer Service. MED-M02: consumo no BigQuery/Dataproc segue projeção explícita, sem `select *`, já convenção do projeto. MED-M04: a coexistência de Datastream (→ BigLake Iceberg/GCS) e Debezium Server (→ Pub/Sub) para a mesma fonte exige política de idempotência clara em cada destino — `MERGE`/upsert por `cdc_sequence` no lado GCS/BigQuery, e deduplicação por chave no lado Pub/Sub/Dataflow (2 leituras da mesma mudança não podem gerar 2 efeitos) |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Esta feature define topologia de ingestão, não introduz um novo pipeline de qualidade — segue o mesmo padrão de tipagem defensiva já usado no projeto |
| Schema drift (SD-M01-04) | **N/A justificado** | Sem Auto Loader com schema variável — os geradores têm schema fixo, e o Datastream/Debezium Server replicam esquema já definido nas fontes relacionais |
| Teams / alertas (TM-M01-06) | **SHOULD** — TM-M01 recomendado, não MUST | A Cloud Function ponte (MinIO→Pub/Sub) é um componente customizado novo, com risco maior de falha silenciosa do que os conectores gerenciados (Datastream/Storage Transfer Service) — recomenda-se alerta operacional em caso de falha, mas sem SLA de produção 24/7 que torne isso bloqueante |
| Observabilidade (OBS-M01-03) | **SHOULD** — OBS-M01 recomendado para a Cloud Function e para o túnel SSH | Logs estruturados na Cloud Function ajudam a diagnosticar falhas do componente customizado; monitorar a saúde do túnel `autossh` é recomendado dado o risco novo introduzido nesta fase (A-001), mas sem SLA de freshness formal |
| Erros e resiliência (ERR-M01-02) | Fica para o `/design` | Fail-fast e distinção de tipos de erro (queda do túnel vs. schema vs. throttling do Pub/Sub) são detalhamento de implementação, não de escopo de ingestão |
| Segurança (GOV-M01-02) | **MUST** — GOV-M01 aplica | Credenciais dos connection profiles do Datastream (Postgres/Oracle/Mongo), da Cloud Function, do Storage Transfer Service e do Debezium Server seguem a mesma disciplina já usada no projeto: nunca versionadas, sempre via secret manager/variável Terraform. GOV-M02 (grants UC) **N/A** — não há Unity Catalog nesta feature (Fase 3 é GCP nativa, governança via Dataplex) |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 aplica | Recomenda-se `/pipeline-review-init` após o Build desta feature, mesma prática das Ondas 1/2/3 e da Fase 2/AWS |
| PyODBC (PYODBC-M01-05) | **N/A** | Não há PyODBC/SQL Server nesta feature |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, específico, com as duas pendências técnicas originais (Pub/Sub ausente no Datastream, ferramenta de catalogação indefinida) e a ambiguidade de princípio (v1.2) explicitamente identificadas e resolvidas |
| Users | 2/3 | Único usuário/persona (projeto pessoal) |
| Goals | 3/3 | Priorizados MUST/SHOULD, sequenciados por etapa, cada um ligado a um componente e mecanismo técnico específico já validado no brainstorm |
| Success | 3/3 | Critérios testáveis via inspeção de stream Datastream, evento no Pub/Sub, query no BigQuery/Dataproc e schema da Bronze |
| Scope | 3/3 | Fora de escopo, constraints e assumptions delimitam claramente o que fica para o `/design`, incluindo os riscos técnicos mais sensíveis desta fase (estabilidade do túnel SSH, concorrência Datastream×Debezium Server) |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

- Mecanismo de resiliência do túnel `autossh` (restart automático se cair, alerta se ficar indisponível por muito tempo) — detalhar no `/design` (ver A-001)
- Formato exato dos metadados de ordenação emitidos pelo Datastream e pelo Debezium Server, para completar o mapeamento pro `cdc_sequence` canônico — detalhar no `/design` (ver A-002)
- Se Postgres/Oracle suportam Datastream e Debezium Server lendo a mesma fonte concorrentemente sem degradar performance — spike técnico recomendado no início do `/design` (ver A-003)
- Tipo/tamanho do GCE VM usado como bastion — detalhar no `/design`
- Mecanismo exato do side input do Dataflow para o lookup no MongoDB (refresh periódico vs. reload por notificação) — decisão de performance a tomar no `/design` (ver A-004)
- Frequência do job `LOAD`/`MERGE` do BigQuery e do agendamento do Storage Transfer Service (MinIO) — impacta a "frescura" do dado no Warehouse; a definir no `/design`
- Política de tratamento do delete em cascata/`TRUNCATE` ignorados pelo Datastream — mitigação ou risco aceito documentado, a decidir no `/design`

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-09-11 | Documento inicial, extraído de `BRAINSTORM_INGESTAO_GCP_FASE3.md`. Todas as decisões de escopo já haviam sido fechadas no brainstorm (conectividade via túnel SSH, Debezium Server para o Kappa, Dataplex como catálogo, BigQuery com carga física) — extração direta, sem necessidade de nova rodada de perguntas. Adicionado sequenciamento em 3 etapas (Warehouse → Lakehouse → Kappa), mesma disciplina de mitigação de risco da Fase 2/AWS |

---

## Status: ✅ Complete (Defined)

**Próximo passo:** `/design .claude/sdd/features/DEFINE_INGESTAO_GCP_FASE3.md`
