# DEFINE: Arquitetura de Ingestão — Fase 2 (AWS)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AWS_FASE2 |
| **Fase do roadmap** | Fase 2 — AWS (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_INGESTAO_AWS_FASE2.md` |
| **Status** | ✅ Complete (Built) |
| **Data** | 2026-09-10 |

---

## Problem Statement

O roadmap registrava a Fase 2 (AWS) como **🔶 sob avaliação**: a ferramenta de cada arquitetura (Redshift Serverless, Glue+Iceberg+Athena, Kinesis) já estava fechada, mas o desenho fino de ingestão — como as 4 fontes da Fase 0 (Postgres, Oracle, MongoDB, MinIO) alimentam esses 3 destinos — tinha só achados soltos, com uma pendência técnica real não resolvida (Kinesis não fala protocolo Kafka, e a notificação nativa de bucket do MinIO só publica em Kafka/AMQP/NATS/Webhook). Sem esse desenho fechado, a Fase 2 não pode avançar para `/design`/`/build`: não dá para provisionar infraestrutura de ingestão sem saber se o Redshift recebe CDC direto do DMS ou só lê do S3, se o Kappa vai ter fidelidade real (dois trilhos, como a Fase 1) ou uma versão simplificada, e como um dado estático (MongoDB) participa de uma arquitetura de streaming. Havia também uma contradição não percebida até o `/define`: o princípio "Portabilidade de motor por camada" (v1.2) previa que Oracle/MinIO seriam substituídos por serviços nativos AWS na Fase 2, o que — se mantido — invalidaria parte do desenho de ingestão (torna o AWS DataSync desnecessário, torna "DMS lendo de Oracle" sem sentido).

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados avançando a Fase 2 do roadmap multi-cloud | Sem esta decisão fechada, a Fase 2 fica bloqueada antes mesmo de abrir a conta AWS — não é possível desenhar Terraform, estimar custo real ou validar se o Kappa AWS vai ser genuinamente comparável ao da Fase 1 em rigor arquitetural |

## Goals

| Etapa | Prioridade | Meta |
|-------|------------|------|
| 1 (Warehouse) | **MUST** | Configurar 1 task AWS DMS por fonte relacional/documental (Postgres, Oracle: ongoing replication/CDC; MongoDB: full load/snapshot) com target **S3/Bronze** |
| 1 (Warehouse) | **MUST** | Configurar **AWS DataSync** com location "Self-managed object storage" apontando para o MinIO, destino S3/Bronze, com agendamento de sync definido |
| 1 (Warehouse) | **MUST** | Estabelecer conectividade de rede da AWS até os containers self-hosted da Fase 0 (Postgres, Oracle, MongoDB, MinIO) — VPN Site-to-Site, IP público com security group restrito, ou túnel equivalente — pré-requisito para toda task DMS/DataSync funcionar |
| 1 (Warehouse) | **MUST** | Configurar **Redshift Serverless** para `COPY`/`MERGE` a partir do S3/Bronze — nenhum endpoint DMS aponta diretamente para o Redshift |
| 2 (Lakehouse) | **MUST** | Configurar **Glue Catalog + tabelas Iceberg** sobre o mesmo S3/Bronze já populado na Etapa 1, consumidas via **Athena** — sem nenhuma ingestão nova |
| 3 (Kappa) | **MUST** | Configurar uma 2ª task AWS DMS para Postgres e uma 2ª para Oracle: ongoing replication/CDC com target **Kinesis Data Streams** nativo (trilho real-time, adicional à task da Etapa 1) |
| 3 (Kappa) | **MUST** | Configurar a notificação de bucket nativa do MinIO (destino Webhook) disparando uma **AWS Lambda** ponte que executa `PutRecord`/`PutRecords` no Kinesis Data Streams — sem passar pelo S3 nesse caminho |
| 3 (Kappa) | **MUST** | Provisionar **Kinesis Data Streams em modo on-demand** (serverless) como único target do trilho real-time |
| 3 (Kappa) | **MUST** | Definir o consumidor do Kappa (Flink gerenciado ou Lambda) lendo eventos exclusivamente do Kinesis, com **lookup/enriquecimento** contra a cópia do MongoDB já aterrissada no S3/Bronze (ex.: menu/horário do restaurante ao processar um evento de Pedido) |
| 3 (Kappa) | **MUST** | Mapear os metadados de ordenação nativos do DMS (equivalente a LSN/SCN) para o campo canônico `cdc_sequence` já definido no contrato de CDC da Onda 3 |
| — | **MUST** | Provisionar toda a infraestrutura acima via **Terraform** (sem criação manual de recursos AWS), conforme princípio já fixado no roadmap (Seção 2) |
| — | **SHOULD** | Registrar logs estruturados na Lambda ponte (MinIO→Kinesis) — é um componente customizado novo (não um conector gerenciado), com maior risco de falha silenciosa do que os demais caminhos |
| — | **SHOULD** | Recomendar `/pipeline-review-init` após o Build desta feature, mesma prática já usada nas Ondas 1/2/3 |

## Sequenciamento (mitigação de risco)

Mesmo método já usado nas Ondas 1-3 (Fase 0): validar uma arquitetura de cada vez, não todas simultaneamente, para isolar risco e não sobrecarregar os sistemas on-premise (Postgres/Oracle/MongoDB/MinIO em Docker/ShadowTraffic) com leituras de CDC concorrentes.

| Etapa | Escopo | Por que nessa ordem |
|-------|--------|----------------------|
| **1** | Warehouse: 1 task DMS por fonte relacional/documental (batch) + DataSync (MinIO) → S3/Bronze → Redshift | Primeira e única carga de CDC no on-premise até este ponto — 1 leitura por fonte, sem concorrência |
| **2** | Lakehouse: Glue + Iceberg + Athena sobre o mesmo S3/Bronze da Etapa 1 | Zero ingestão nova — reaproveita a task DMS/DataSync já validada na Etapa 1, sem tocar nos bancos on-premise de novo |
| **3** | Kappa: 2ª task DMS por fonte (target Kinesis) + ponte MinIO→Lambda→Kinesis + consumidor com lookup no MongoDB | Única etapa com 2 leituras concorrentes de CDC por fonte (Postgres/Oracle) — janela de risco conhecida e limitada, porque é a última etapa da Fase 2: ao concluir, o projeto encerra nesta cloud e migra para a próxima fase (GCP) |

**Decisão explícita:** o risco de concorrência de CDC (Assumption A-003) não é eliminado pelo desenho, mas é **confinado à Etapa 3** — a janela em que 2 tasks DMS leem o mesmo replication slot/LogMiner é temporária (dura enquanto o Kappa está sendo validado), não permanente.

## Success Criteria

- [ ] 2 tasks DMS ativas para Postgres (1 target Kinesis Data Streams, 1 target S3/Bronze), ambas em ongoing replication/CDC
- [ ] 2 tasks DMS ativas para Oracle, mesmo padrão do Postgres
- [ ] 1 task DMS ativa para MongoDB, full load/snapshot, target S3/Bronze — nenhuma task de CDC ou target Kinesis criada para o MongoDB
- [ ] AWS DataSync com location "Self-managed object storage" configurada para o MinIO; sync agendado executa com sucesso e os objetos aparecem no S3/Bronze
- [ ] Notificação de bucket do MinIO (destino Webhook) aciona a Lambda ponte, que grava no Kinesis com sucesso — evento visível no stream em segundos, não em lote
- [ ] Kinesis Data Streams provisionado em modo on-demand, recebendo eventos de Postgres, Oracle e MinIO
- [ ] Redshift Serverless executa `COPY`/`MERGE` a partir do S3/Bronze com sucesso; nenhum endpoint DMS configurado apontando para o Redshift
- [ ] Glue Catalog + tabelas Iceberg criadas sobre o S3/Bronze; query via Athena retorna dado correto
- [ ] Consumidor do Kappa processa eventos do Kinesis e enriquece com lookup no MongoDB (lido do S3/Bronze), sem consultar o Kinesis para isso
- [ ] Campo `cdc_sequence` preenchido de forma consistente e ordenável a partir dos metadados nativos do DMS, alinhado ao contrato canônico da Onda 3
- [ ] Toda a infraestrutura acima existe como código Terraform versionado — 0 recursos criados manualmente no console AWS
- [ ] A conectividade de rede AWS↔sistemas self-hosted está documentada e validada (task DMS consegue abrir replication slot/LogMiner/oplog remotamente)

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | DMS Postgres real-time | Task DMS ongoing replication com target Kinesis configurada | Um `UPDATE` ocorre em `drivers` no Postgres | O evento aparece no Kinesis em poucos segundos, sem passar pelo S3 |
| AT-002 | DMS Postgres batch | 2ª task DMS ongoing replication com target S3 configurada | O mesmo `UPDATE` ocorre | O arquivo correspondente aparece no S3/Bronze no intervalo de entrega configurado do DMS |
| AT-003 | DMS Oracle real-time | Task DMS ongoing replication com target Kinesis configurada (Oracle) | Um `UPDATE` ocorre em `orders`/`payments` no Oracle | Mesmo comportamento do AT-001, para Oracle |
| AT-004 | DMS Oracle batch | 2ª task DMS ongoing replication com target S3 configurada (Oracle) | O mesmo `UPDATE` ocorre | Mesmo comportamento do AT-002, para Oracle |
| AT-005 | DMS MongoDB batch-only | Task DMS full load configurada para MongoDB | Task executada | Dados aparecem no S3/Bronze; nenhuma task de CDC ou target Kinesis existe para o MongoDB |
| AT-006 | DataSync MinIO | Location "Self-managed object storage" configurada | O sync agendado roda | Novos objetos do MinIO aparecem no S3/Bronze |
| AT-007 | Webhook MinIO → Lambda → Kinesis | Notificação de bucket do MinIO configurada (destino Webhook) | Um objeto novo é escrito no MinIO | A Lambda recebe o evento e grava no Kinesis com sucesso; evento visível no stream |
| AT-008 | Redshift consome do S3 | Dados presentes no S3/Bronze | `COPY`/`MERGE` executado no Redshift Serverless | Tabela Redshift atualizada; nenhum endpoint DMS aponta para o Redshift |
| AT-009 | Glue/Athena consomem do S3 | Dados presentes no S3/Bronze, tabela Iceberg + crawler configurados | Query executada no Athena | Retorna dado correto e atualizado |
| AT-010 | Kappa com lookup no MongoDB | Consumidor Flink/Lambda rodando, cópia do MongoDB disponível no S3/Bronze | Um evento de Pedido chega no Kinesis | O consumidor enriquece o evento com dado do MongoDB (lido do S3), sem acessar o Kinesis para isso |
| AT-011 | `cdc_sequence` mapeado | Evento processado via DMS chega na Bronze | Inspecionar o schema/valor da coluna | `cdc_sequence` preenchido de forma consistente e ordenável, conforme o contrato canônico |
| AT-012 | Infraestrutura via Terraform | Todos os recursos acima definidos como módulo/config Terraform | `terraform plan`/`apply` executado | Nenhum recurso precisa ser criado manualmente no console AWS |

## Out of Scope

| Item | Por que fica para depois |
|------|-----------------------------|
| MSK (Kafka gerenciado) | Descartado no brainstorm — contraria o princípio de priorizar serverless/on-demand (brokers sempre ligados, custo mesmo ocioso) |
| CDC/mutação real para MongoDB | Fonte estática por decisão já fechada na Onda 3 — não é escopo desta feature reabrir isso |
| Substituir Oracle/MinIO por motores nativos AWS (RDS/S3 direto) | Decisão explicitamente revertida nesta rodada de `/define` (ver Problem Statement) — o princípio v1.2 do roadmap foi atualizado para refletir o reaproveitamento dos sistemas da Fase 0 |
| Decisão equivalente para a Fase 3 (GCP) | Fora de escopo desta feature — a Fase 3 mantém a redação original da v1.2 até seu próprio `/define` |
| Dimensionamento fino de shards do Kinesis, configuração de Flink vs. Lambda no consumo do Kappa | Detalhe de implementação — fica para o `/design` |
| Mecanismo exato do lookup do consumidor contra o MongoDB no S3 (leitura direta vs. cache/side-table tipo DynamoDB) | Decisão de performance — fica para o `/design` |
| Método exato de conectividade de rede (VPN Site-to-Site vs. IP público vs. túnel SSH) | Vira uma decisão de segurança/infra a detalhar no `/design`, com trade-offs de custo e exposição |

## Constraints

- Todo componente de ingestão (DMS, DataSync) precisa de conectividade de rede real da AWS até os containers self-hosted da Fase 0 — sem isso, nenhuma task consegue sequer abrir conexão inicial
- MongoDB continua sem sink de escrita/CDC no ShadowTraffic (decisão da Onda 3) — nenhuma task ou pipeline desta feature pode assumir que o MongoDB muta
- DMS não tem conector para object storage genérico — MinIO precisa necessariamente do AWS DataSync, não pode ser tratado como fonte DMS
- Kinesis Data Streams não fala protocolo Kafka (API proprietária `PutRecord`/KCL) — qualquer integração do MinIO com o Kinesis precisa passar por uma ponte (Lambda), nunca por conexão direta
- O trilho real-time (Kappa) não pode depender do S3/trilho batch em nenhum ponto — decisão explícita de manter dois trilhos separados, mesmo princípio da Fase 1
- Toda credencial (DMS endpoints, Lambda, DataSync) deve seguir a mesma disciplina já aplicada nas fases anteriores: nunca versionada, sempre via secret manager/variável Terraform
- Custo de cada serviço deve favorecer serverless/on-demand por padrão (Kinesis on-demand, Redshift Serverless, Lambda) — MSK já descartado por esse motivo
- As 3 arquiteturas (Warehouse, Lakehouse, Kappa) são construídas e validadas **em ordem, uma de cada vez**, nunca todas simultaneamente desde o início — mesmo método de mitigação de risco já usado nas Ondas 1-3. A 2ª task DMS por fonte (target Kinesis) só existe a partir da Etapa 3 (Kappa), a última desta fase

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | É possível abrir conectividade de rede (VPN, IP público com security group restrito, ou túnel) entre a AWS e os containers Docker locais (Postgres/Oracle/MongoDB/MinIO) sem custo proibitivo nem exposição de segurança inaceitável | Se não for viável, toda a Fase 2 precisa reconsiderar a decisão desta rodada e migrar para motores nativos AWS (opção descartada neste `/define`) | [ ] Validar no início do `/design`, antes de comprometer o restante do desenho |
| A-002 | O DMS expõe metadados de ordenação (equivalente a LSN/SCN) suficientes para reconstruir o `cdc_sequence` canônico, de forma similar ao que já foi mapeado para Airbyte/Debezium na Onda 3 | Se os metadados do DMS forem insuficientes ou tiverem formato muito diferente, o contrato canônico de CDC pode precisar de um shim mais complexo do que o previsto | [ ] Confirmar no `/design`, mesma disciplina da Onda 3 |
| A-003 | Uma task DMS de ongoing replication/CDC consegue coexistir com uma 2ª task lendo o mesmo replication slot/LogMiner da mesma fonte (Postgres/Oracle), sem exceder limites de conexão concorrente do banco self-hosted | Se o motor de origem não suportar 2 leituras concorrentes de CDC, pode ser necessário desenhar um fan-out único (ex. 1 task → Kinesis, e Firehose replica pro S3), aproximando-se da Abordagem B rejeitada no brainstorm | [ ] Validar no `/design`, especialmente para o Oracle (LogMiner tem histórico de restrições de concorrência). **Risco parcialmente mitigado pelo sequenciamento:** a 2ª task só é criada na Etapa 3 (Kappa), a última do roadmap desta fase — a janela de concorrência é curta e conhecida, não um regime permanente |
| A-004 | O consumidor do Kappa consegue fazer lookup no S3 (cópia do MongoDB) com latência aceitável por evento, sem precisar de um cache/side-table dedicado | Se a latência de leitura direta do S3 por evento for proibitiva, o `/design` precisa especificar um cache (ex. DynamoDB) alimentado a partir do S3 | [ ] Avaliar no `/design` |

## Requisitos operacionais de pipeline (mandato)

Esta feature introduz ingestão nova para o medalhão (Bronze via S3) e um trilho de streaming real (Kinesis) — o sinal `medalhão bronze silver gold` + `landing raw csv json parquet` de `PIPELINE_MANDATORY_PRACTICES.yaml` se aplica.

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **MUST** — DC-M04 aplica diretamente | O mapeamento dos metadados de ordenação do DMS para `cdc_sequence` (Meta/AT-011) é exatamente o checklist de schema/formato drift entre ferramentas de ingestão (DC-M04) já antecipado na Onda 3 — agora precisa ser feito de fato para uma 3ª ferramenta (DMS, além de Airbyte/Debezium). Documento operacional formal (DC-M01) segue N/A justificado — projeto de portfólio pessoal, o próprio roadmap + este DEFINE cumprem o papel comunicativo |
| Medalhão e UC (MED-M01-04) | **MUST** — MED-M01, MED-M02 e MED-M04 aplicam | MED-M01: Bronze em S3 precisa preservar linhagem (`_ingest_ts`, `_source_file`/task DMS, `_run_id`) mesmo vindo de uma ferramenta nova (DMS/DataSync). MED-M02: Silver segue projeção explícita, sem `select *`, já convenção do projeto. MED-M04: a coexistência de 2 tasks DMS por fonte (Kinesis + S3) exige política de idempotência clara em cada target — `APPLY CHANGES INTO`/`MERGE` no lado que consome o S3, e deduplicação por chave no lado que consome o Kinesis (2 leituras da mesma mudança não podem gerar 2 efeitos) |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Esta feature define topologia de ingestão, não introduz um novo pipeline de qualidade — segue o mesmo padrão de tipagem defensiva já usado no projeto |
| Schema drift (SD-M01-04) | **N/A justificado** | Sem Auto Loader com schema variável — os geradores têm schema fixo, e o DMS replica esquema já definido nas fontes relacionais |
| Teams / alertas (TM-M01-06) | **SHOULD** — TM-M01 recomendado, não MUST | A Lambda ponte (MinIO→Kinesis) é um componente customizado novo, com risco maior de falha silenciosa do que os conectores gerenciados (DMS/DataSync) — recomenda-se alerta operacional em caso de falha, mas sem SLA de produção 24/7 que torne isso bloqueante |
| Observabilidade (OBS-M01-03) | **SHOULD** — OBS-M01 recomendado para a Lambda ponte | Logs estruturados na Lambda ajudam a diagnosticar falhas do único componente verdadeiramente customizado deste desenho; sem SLA de freshness formal para o restante (DMS/DataSync são gerenciados e já expõem métricas nativas) |
| Erros e resiliência (ERR-M01-02) | Fica para o `/design` | Fail-fast e distinção de tipos de erro (rede vs. schema vs. throttling do Kinesis) são detalhamento de implementação, não de escopo de ingestão |
| Segurança (GOV-M01-02) | **MUST** — GOV-M01 aplica | Credenciais dos endpoints DMS (Postgres/Oracle/Mongo), da Lambda e do DataSync seguem a mesma disciplina já usada no projeto: nunca versionadas, sempre via secret manager/variável Terraform. GOV-M02 (grants UC) **N/A** — não há Unity Catalog nesta feature (Fase 2 é AWS nativa) |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 aplica | Recomenda-se `/pipeline-review-init` após o Build desta feature, mesma prática das Ondas 1/2/3 |
| PyODBC (PYODBC-M01-05) | **N/A** | Não há PyODBC/SQL Server nesta feature |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, específico, com a pendência técnica original e a contradição de princípio (v1.2) explicitamente identificadas e resolvidas |
| Users | 2/3 | Único usuário/persona (projeto pessoal) |
| Goals | 3/3 | Priorizados MUST/SHOULD, cada um ligado a um componente e mecanismo técnico específico já validado no brainstorm |
| Success | 3/3 | Critérios testáveis via inspeção de task DMS, evento no Kinesis, query no Redshift/Athena e schema da Bronze |
| Scope | 3/3 | Fora de escopo, constraints e assumptions delimitam claramente o que fica para o `/design`, incluindo os 2 riscos técnicos mais sensíveis (conectividade de rede, concorrência de CDC no DMS) |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

- Método exato de conectividade de rede AWS↔sistemas self-hosted (VPN Site-to-Site vs. IP público com security group vs. túnel) — decisão de segurança/custo a tomar no `/design` (ver A-001)
- Formato exato dos metadados de ordenação emitidos pelo DMS, para completar o mapeamento pro `cdc_sequence` canônico — detalhar no `/design` (ver A-002)
- Se Postgres/Oracle suportam 2 tasks DMS concorrentes lendo o mesmo replication slot/LogMiner sem degradar performance — spike técnico recomendado no início do `/design` (ver A-003)
- Payload exato do Webhook de notificação do MinIO e formato esperado pela Lambda ponte antes do `PutRecord` — detalhar no `/design`
- Escolha entre Flink gerenciado (Kinesis Data Analytics) e Lambda como consumidor do Kappa — decisão de custo/complexidade a tomar no `/design`
- Mecanismo exato do lookup do consumidor contra o MongoDB no S3 (leitura direta vs. cache/side-table) — decisão de performance a tomar no `/design` (ver A-004)
- Decisão equivalente de "reaproveitar vs. substituir Oracle/MinIO" para a Fase 3 (GCP) — não é escopo desta feature, mas fica registrada como precedente a considerar no `/define` daquela fase

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-09-10 | Documento inicial, extraído de `BRAINSTORM_INGESTAO_AWS_FASE2.md`. Durante a extração, identificada e resolvida uma contradição entre o brainstorm e o princípio "Portabilidade de motor por camada" (v1.2 do roadmap) — decisão registrada: Fase 2 reaproveita os sistemas self-hosted da Fase 0, roadmap atualizado para v1.6 |
| 1.1 | 2026-09-10 | Adicionado sequenciamento em 3 etapas (Warehouse → Lakehouse → Kappa), a pedido do usuário, para não sobrecarregar os bancos on-premise com leituras de CDC concorrentes. A 2ª task DMS por fonte (target Kinesis) passa a existir só na Etapa 3 — Assumption A-003 atualizada para refletir que essa janela de risco é temporária, não permanente |
| 1.2 | 2026-09-10 | `/design` concluído (`DESIGN_INGESTAO_AWS_FASE2.md`). A-001 (conectividade de rede) resolvida com a decisão de migrar temporariamente os sistemas da Fase 0 para uma EC2 dentro da VPC da Fase 2; A-002 (metadados de ordenação do DMS) recebeu uma proposta técnica a confirmar no `/build`; escolhido AWS Lambda (não Flink gerenciado) como consumidor do Kappa |
| 1.3 | 2026-09-10 | `/build` concluído (`BUILD_REPORT_INGESTAO_AWS_FASE2.md`). Manifesto completo implementado (Terraform, 2 Lambdas, SQL, docs); 10/10 testes unitários passaram (moto mockando Kinesis/S3); `terraform validate` não executou por limitação do ambiente sandboxado (handshake TLS local), não do código — pendente rodar num ambiente normal antes do `apply` real |

---

## Status: ✅ Complete (Defined)

**Próximo passo:** `/ship .claude/sdd/features/DEFINE_INGESTAO_AWS_FASE2.md`
