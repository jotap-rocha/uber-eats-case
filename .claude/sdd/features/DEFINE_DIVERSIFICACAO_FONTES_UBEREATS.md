# DEFINE: Diversificação de Fontes de Dados (Onda 3)

| Campo | Valor |
|-------|-------|
| **Feature** | DIVERSIFICACAO_FONTES_UBEREATS |
| **Fase do roadmap** | Fase 0 — Fundação (`docs/ROADMAP_ARQUITETURA_MULTICLOUD.md`), Onda 3 |
| **Input** | `.claude/sdd/features/BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md` |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-06 |

---

## Problem Statement

O projeto tem hoje só 2 sistemas de origem (Postgres real + MinIO simulado), sem que nenhuma tabela do Postgres tenha um domínio de negócio claramente atribuído, e com Pedido/Pagamento representando mudança de status via logs append-only paralelos (`kafka/status`, `kafka/events`) que foram criados sem o referencial relacional correto — o que nunca permitiu simular CDC realista de UPDATE/DELETE, só INSERT. Isso limita o valor de portfólio (menos tecnologias praticadas) e deixa o modelo de dados menos fiel ao mundo real (onde pedidos e pagamentos vivem em bancos relacionais com estado mutável, não em streams de eventos imutáveis desconectados de um sistema de registro).

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados avançando a Fase 0 do roadmap multi-cloud | Sem esta correção, o projeto fica limitado a 2 tecnologias de origem e a um padrão de CDC insert-only, não demonstrando o padrão de mercado mais comum (mutação real + Bronze CDC), e mantém dois logs de histórico mal referenciados sem lugar claro no modelo |

## Goals

| Etapa | Prioridade | Meta |
|-------|------------|------|
| — | **MUST** | Adicionar `connection: oracle` ao `gen/unified/uber-eats.json`, no mesmo processo único do `gen-unified` |
| 1 | **MUST** | Reescrever os geradores `drivers` (Postgres) com `fork`+`stateMachine`, implementando `op: update` para `status`/`total_deliveries`/`total_earnings`/`average_rating`, provando o mecanismo de mutação antes de aplicá-lo em outro sistema |
| 2 | **MUST** | Migrar Restaurante, Produto e Estoque para o Oracle (insert-only nesta etapa), com `sqlHint`/`tablePolicy: manual` explícito nas colunas-chave |
| 2 | **MUST** | Subir Debezium/Kafka Connect como novo serviço no `docker-compose.yml`, com CDC real sobre o Oracle, e validar que captura INSERT corretamente antes da Etapa 3 |
| 3 | **MUST** | Aplicar o padrão de mutação já validado na Etapa 1 aos geradores de Pedido e Pagamento no Oracle (`op: update` para `status`) |
| 3 | **MUST** | Migrar Pedido, Pagamento, Item de Pedido (filho de Pedido) e Recibo (filho de Pagamento) do MinIO para o Oracle |
| 3 | **MUST** | Aposentar `kafka/status` e `kafka/events` do gerador — a mudança de status passa a ser a mutação real da linha, capturada pelo CDC |
| — | **MUST** | Criar o satélite documental "Perfil de Restaurante" (menu + horários de funcionamento) no MongoDB, com FK para `restaurant_id`, população estática (seed único) |
| — | **MUST** | Definir e implementar o contrato canônico de metadados de CDC na Bronze (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`), com um shim por ferramenta de ingestão (Airbyte, Debezium) |
| — | **MUST** | Renomear as tabelas Silver afetadas para a convenção por domínio de negócio (ex. `silver_orders`, `silver_payments`, `silver_restaurants`), atualizando os scripts Gold correspondentes |
| — | **MUST** | Validar com join real no Gold (Databricks) que os relacionamentos cross-connection (MinIO→Oracle para Entrega/Avaliação/Incidente referenciando Pedido; MongoDB→Oracle para o satélite de Restaurante) retornam resultado consistente, sem órfãos |
| — | **MUST** | Atualizar `docs/MODELO_CONCEITUAL_UBER_EATS.md` com o estado final: 4 sistemas, entidade nova (Perfil de Restaurante), streams aposentados, sem pendência conhecida |
| — | **SHOULD** | Preservar sem alteração tudo que já funciona: Usuário/Motorista no Postgres (exceto o ganho de mutação), Entrega/Avaliação/Turno/Incidente no MinIO |

## Success Criteria

- [ ] `gen/unified/uber-eats.json` tem 3 `connections` ativas (`postgres`, `oracle`, `minio`) no mesmo processo — nenhum gerador Oracle roda como container separado
- [ ] `drivers.status` (e os demais campos da Etapa 1) sofrem UPDATE real, capturado como tal pelo Airbyte CDC — não aparece como um novo registro
- [ ] Restaurante, Produto e Estoque existem como tabelas Oracle, com PK explícita, capturados pelo Debezium/Kafka Connect
- [ ] `orders.status` e `payments.status` sofrem UPDATE real no Oracle, capturado pelo Debezium
- [ ] `kafka/status` e `kafka/events` não existem mais no gerador nem em nenhum script Silver/Gold
- [ ] Item de Pedido e Recibo saem do MinIO e passam a fazer lookup direto no Oracle (Pedido/Pagamento)
- [ ] MongoDB tem uma coleção com o satélite "Perfil de Restaurante" (menu + horários), com `restaurant_id` correspondendo a um Restaurante real no Oracle — 0 registros órfãos
- [ ] A Bronze expõe as 4 colunas canônicas de CDC (`cdc_operation`, `cdc_commit_ts`, `cdc_sequence`, `cdc_source_system`) para toda tabela alimentada por Airbyte ou Debezium
- [ ] Nenhuma tabela Silver do domínio core mantém nome por sistema de origem (`silver_kafka_*`, `silver_mysql_*`, `silver_postgres_*`) — todas nomeadas por domínio de negócio
- [ ] Query de join no Gold entre todas as entidades relacionadas (incluindo as que agora cruzam Oracle↔MinIO↔MongoDB) retorna 0 registros órfãos
- [ ] `docs/MODELO_CONCEITUAL_UBER_EATS.md` reflete os 4 sistemas e não lista nenhuma pendência de Onda 3

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Processo único preservado | `gen/unified/uber-eats.json` com `connection: oracle` adicionada | `docker-compose up gen-unified` | Um único container gerador roda; logs confirmam geração simultânea em Postgres, Oracle e MinIO |
| AT-002 | Mutação real no Postgres (Etapa 1) | Gerador `drivers` reescrito com `fork`+`stateMachine` | Regenerar dados | `SELECT status FROM drivers WHERE driver_id=X` muda de valor ao longo do tempo sem novo `driver_id` ser criado; Airbyte CDC replica a mudança como UPDATE |
| AT-003 | Oracle plumbing (Etapa 2) | Restaurante/Produto/Estoque migrados para Oracle, Debezium configurado | Regenerar dados (insert-only) | Tabelas existem no Oracle com PK; tópico Kafka do Debezium recebe evento de INSERT por registro criado |
| AT-004 | Mutação real no Oracle (Etapa 3) | Padrão da Etapa 1 aplicado a `orders`/`payments` no Oracle | Regenerar dados com mutação ativa | `orders.status` muda ao longo do tempo (ex. `created→delivered`); Debezium emite evento `op: u` com `before`/`after` |
| AT-005 | Histórico antigo aposentado | Migração da Etapa 3 concluída | Inspecionar `gen/unified/uber-eats.json` e scripts Silver/Gold | 0 ocorrências de `kafka/status` ou `kafka/events` |
| AT-006 | Item de Pedido e Recibo seguem os pais | Pedido/Pagamento no Oracle | Regenerar dados | `mongodb/items.order_id` e `kafka/receipts.payment_id` fazem lookup em `orders`/`payments` no Oracle, não mais em `kafka/orders`/`kafka/payments` do MinIO |
| AT-007 | Satélite MongoDB sem órfãos | Coleção "Perfil de Restaurante" criada | Join `mongo_perfil_restaurante` ↔ `oracle.restaurants` por `restaurant_id` | 0 registros órfãos — todo perfil corresponde a um restaurante real |
| AT-008 | Contrato de CDC canônico | Bronze de tabelas Airbyte e Debezium implementada | Inspecionar schema da Bronze | `cdc_operation`/`cdc_commit_ts`/`cdc_sequence`/`cdc_source_system` presentes e preenchidos corretamente para ambas as ferramentas |
| AT-009 | Nomenclatura por domínio | Silver renomeada | `SHOW TABLES LIKE 'silver_*'` | Nenhuma tabela do domínio core com prefixo de sistema de origem no nome |
| AT-010 | Join geral sem órfãos | Todas as migrações concluídas | Rodar pipeline Bronze→Silver→Gold completo | Join entre todas as entidades relacionadas (incluindo cross-connection Oracle↔MinIO↔MongoDB) retorna 0 órfãos |
| AT-011 | Soft delete preservado | Qualquer entidade com `op: delete` configurado | Inspecionar geradores | Nenhuma entidade-pai (Usuário, Motorista, Restaurante, Produto) usa hard delete — só soft delete (`status='deleted'` ou equivalente) |

## Out of Scope

| Item | Por que fica para depois |
|------|-----------------------------|
| Segundo MinIO/datalake | Descartado definitivamente — redundante com os datalakes reais das Fases 1-3 |
| MongoDB com dado vivo/mutável | ShadowTraffic não tem sink de escrita para Mongo; exigiria componente de replicação fora do processo único, não justificado nesta v1 |
| Mutação de Usuário, Restaurante, Produto | Fica para uma onda futura — v1 cobre só Motorista, Pedido, Pagamento (as entidades que perdem o histórico) |
| Escolha do motor relacional nativo para AWS/GCP | Decisão do `/define` de cada fase cloud (Fase 2/3), não desta feature — já registrado no roadmap |
| Amarrar a origem da Entrega ao restaurante exato do pedido | Limitação de lookup em 2 níveis, já registrada como possível onda futura desde a Onda 1 |
| Renovação da licença ShadowTraffic | Bloqueio operacional externo, não de escopo/design desta feature — deve ser resolvido antes do Build, não durante o Define/Design |

## Constraints

- Todo sistema novo (Oracle) deve entrar como `connection` do **mesmo processo único** do `gen-unified` — gerador separado recria o bug de "populações desconectadas" que a Onda 2 resolveu
- MongoDB não tem sink de escrita no ShadowTraffic — a coleção "Perfil de Restaurante" só pode ser população estática (seed único), nunca gerada de forma independente/contínua
- Auto-DDL do ShadowTraffic não cria PRIMARY KEY — toda coluna-chave migrada para Oracle precisa de `sqlHint`/`tablePolicy: manual` explícito, senão a réplica lógica (CDC) falha silenciosamente ao tentar capturar UPDATE/DELETE
- O mecanismo de mutação (`fork`+`stateMachine`) nunca foi testado neste projeto — deve ser provado num sistema por vez (Postgres primeiro, Etapa 1), não simultaneamente em Postgres e Oracle
- Validação final deve usar o pipeline Databricks real (Silver → Gold), consistente com as Ondas 1/2 — não uma query solta fora do fluxo de produção
- `docs/MODELO_CONCEITUAL_UBER_EATS.md` deve permanecer fiel ao estado real implementado a qualquer momento

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | O padrão `fork`+`stateMachine` provado em `drivers` (Etapa 1) se replica sem ajuste estrutural para `orders`/`payments` (Etapa 3), apesar de Pedido ter blast radius muito maior (6 entidades filhas fazem lookup nele) | Se a mecânica de fork não escalar para o volume/cardinalidade de Pedido, a Etapa 3 pode exigir um desenho diferente do validado na Etapa 1 | [ ] Validar no Design/Build |
| A-002 | O Debezium/Kafka Connect consegue ser configurado localmente em Docker sem custo de licença e sem exigir edição paga do Oracle (ex. LogMiner funciona em `gvenzl/oracle-free`) | Se a imagem Oracle local não suportar LogMiner/CDC completo, a Etapa 2/3 precisa de uma edição diferente (custo) ou de uma alternativa de captura | [ ] Confirmar no Design |
| A-003 | O lookup cross-connection MinIO→Oracle (para Entrega/Avaliação/Incidente referenciando Pedido no Oracle) funciona da mesma forma já comprovada para MinIO→Postgres na Onda 2 | Se o ShadowTraffic tratar diferente uma conexão `oracle` de uma `postgres` no lookup cruzado, entidades filhas no MinIO podem gerar `order_id` órfão | [ ] Confirmar via teste no Build, mesmo padrão de risco documentado na Onda 2 |
| A-004 | Migrar Pedido/Pagamento para Oracle não exige tocar nos scripts Gold além dos joins/keys — a lógica de negócio (`load_order_unit_economics.sql`, etc.) permanece válida | Se o Gold fizer suposições sobre a origem MinIO de `kafka/orders`/`kafka/payments` além da chave de join, pode exigir ajuste adicional não previsto | [ ] Confirmar via grep no Design, mesmo padrão de verificação da Onda 1 |

## Requisitos operacionais de pipeline (mandato)

Esta feature altera profundamente o pipeline medalhão (Bronze/Silver/Gold, múltiplas novas fontes CDC) — o sinal `medalhão bronze silver gold` + `autoloader cloudfiles ingestão` de `PIPELINE_MANDATORY_PRACTICES.yaml` se aplica.

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **SHOULD** — DC-M04 aplica | O contrato canônico de metadados de CDC (`cdc_operation` etc.) já é requisito MUST desta feature e cumpre o papel de DC-M04 (checklist de schema drift entre ferramentas de ingestão); documento operacional formal (DC-M01) fica N/A justificado — projeto de portfólio pessoal, `docs/MODELO_CONCEITUAL_UBER_EATS.md` cumpre o mesmo papel comunicativo |
| Medalhão e UC (MED-M01-04) | **MUST** — MED-M02 e MED-M04 aplicam diretamente | MED-M02 (projeção explícita): os novos scripts Silver do Oracle devem seguir o mesmo padrão de `CAST`/rename já usado nos scripts existentes. MED-M04 (idempotência/reprocessamento): esta feature introduz `op: update`/`delete` pela primeira vez — a política de idempotência via `APPLY CHANGES INTO` + `SEQUENCE BY` (já em uso para Postgres) deve ser replicada explicitamente para o Bronze do Oracle, com atenção a colisão de timestamp em rajada de updates (usar `_ab_cdc_lsn`/LSN do Debezium, não só timestamp, como já sinalizado no brainstorm) |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Esta feature corrige a origem/topologia dos dados, não introduz um novo pipeline de qualidade/quarentena — os registros das novas fontes seguem o mesmo padrão de tipagem defensiva já usado no projeto |
| Schema drift (SD-M01-04) | **N/A justificado** | Sem Auto Loader com schema variável envolvido nesta feature — os geradores têm schema fixo (Oracle com `sqlHint` explícito, Mongo com schema definido no seed) |
| Teams / alertas (TM-M01-06) | **N/A justificado** | Sem mudança no comportamento de falha/alerta em produção — fora do escopo de portfólio pessoal sem operação 24/7 |
| Observabilidade (OBS-M01-03) | **N/A justificado** | Sem SLA de freshness operacional formal — fora do escopo desta correção estrutural |
| Segurança (GOV-M01-02) | **MUST** — GOV-M01 aplica | Credenciais novas (Oracle, Debezium/Kafka Connect) devem seguir o padrão já em uso: só em `gen/.env`/secret scope, nunca versionadas — mesma disciplina já aplicada a Postgres/MinIO |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 aplica | Recomenda-se `/pipeline-review-init` após o Build desta feature, antes de considerar a Onda 3 encerrada — mesma recomendação já feita nas Ondas 1/2 |
| PyODBC (PYODBC-M01-05) | **N/A** | Não há PyODBC/SQL Server nesta feature |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro, específico, com causa raiz identificada (histórico mal referenciado) e ligado a arquivos/streams reais |
| Users | 2/3 | Um único usuário/persona (projeto pessoal) |
| Goals | 3/3 | Priorizados MUST/SHOULD, sequenciados por etapa, mensuráveis, ligados a arquivos e mecanismos reais |
| Success | 3/3 | Critérios testáveis via inspeção de schema, CDC e join real no Gold |
| Scope | 3/3 | Escopo, fora de escopo e YAGNI extensivamente delimitados no brainstorm; sequenciamento em 3 etapas reduz ambiguidade de execução |
| **Total** | **14/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes |

## Open Questions

- Schema exato do satélite "Perfil de Restaurante" no MongoDB (estrutura do array de menu, formato de horários) — fica para o `/design`
- Desenho exato de como o `fork`+`stateMachine` de Pedido/Pagamento vai lidar com o blast radius maior (6 entidades filhas fazendo lookup) comparado ao piloto em Motorista — fica para o `/design` (ver A-001)
- Confirmar se a imagem Oracle local (provável `gvenzl/oracle-free`) suporta LogMiner sem configuração paga — spike técnico recomendado no início do `/design` ou já no `/build` da Etapa 2, antes de comprometer o desenho completo do Debezium (ver A-002)

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-09-06 | Documento inicial, extraído de `BRAINSTORM_DIVERSIFICACAO_FONTES_UBEREATS.md` (input já validado em múltiplas rodadas de `/intake` + `/brainstorm`) |

---

## Status: ✅ Complete (Defined)

**Próximo passo:** `/design .claude/sdd/features/DEFINE_DIVERSIFICACAO_FONTES_UBEREATS.md`
