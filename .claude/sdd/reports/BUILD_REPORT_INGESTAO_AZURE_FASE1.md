# BUILD REPORT: Arquitetura de Ingestão — Fase 1 (Azure)

| Campo | Valor |
|-------|-------|
| **Feature** | INGESTAO_AZURE_FASE1 |
| **Escopo deste Build** | Manifesto completo do DESIGN — Etapas 1-4 (33 itens: Terraform, Kafka Connect/Debezium, SQL, Databricks DLT, testes, docs) |
| **Input** | `.claude/sdd/features/DESIGN_INGESTAO_AZURE_FASE1.md` |
| **Data** | 2026-09-12 |

---

## Summary

| Métrica | Valor |
|---------|-------|
| Itens do manifesto | 31/33 completos; 1 revelado como não-aplicável ao código versionado (item 27 — ver Desvios); 1 já resolvido no `/design` (item 31 — roadmap) |
| Arquivos Terraform criados | 10 (`infra/azure/fase1-ingestao/`) |
| Arquivos Kafka Connect/Debezium criados | 6 (`debezium/`) — 2 além do manifesto original (ver Desvios) |
| Arquivos SQL criados | 2 (`sql/azure/`) |
| Scripts Databricks DLT editados | 10 (`pipeline/bronze/*.sql` ×9, `pipeline/silver/ingestion_mongo_perfil_restaurante.sql`) |
| Scripts Databricks DLT criados | 1 (`pipeline/bronze/ingest_mongodb_perfil_restaurante.sql`, novo) |
| Documentação criada | 7 (`docs/azure/` ×4, `docs/minio/kafka-notification-config-azure.md`, `docs/data-contract-cdc-azure.md`, mais a nota de desvio) |
| Código Python criado | 1 módulo (`src/azure/cdc_contract/mapping.py`) + 1 arquivo de teste |
| `docker-compose.yml` | Editado — novo serviço `kafka-connect-azure` (cluster dedicado, ver Desvios) |
| `gen/.env.template` | Editado — nova seção "Azure (Fase 1)" |
| Testes unitários | **6/6 passaram** (`pytest tests/azure`) |
| Lint (`ruff`) | **0 erros** (`ruff check src/azure tests/azure`) |
| `terraform validate` | ❌ **Não executado** — binário Terraform não disponível neste ambiente (mesma limitação registrada no build da AWS) |
| Deploy/teste em Azure real | **Não aplicável nesta sessão** — conta Azure ainda não foi aberta (mesmo princípio do roadmap: abrir conta só no início da fase) |

---

## O que foi implementado

### Etapa 1 — Captura única + hub (Event Hub) + landing batch independente (itens 1-9)

| Item | Arquivo | Status |
|------|---------|--------|
| 1 | `infra/azure/fase1-ingestao/resource_group.tf` | ✅ |
| 2 | `infra/azure/fase1-ingestao/storage_account.tf` | ✅ — corrigido para `azurerm_storage_data_lake_gen2_filesystem` (ver Desvios) |
| 3 | `infra/azure/fase1-ingestao/event_hubs.tf` | ✅ Namespace tier Standard + 3 Event Hubs + authorization rule |
| 4 | `infra/azure/fase1-ingestao/service_principal.tf` | ✅ App Registration + role assignment (Storage Blob Data Contributor no Storage Account) |
| 5 | `docs/azure/airbyte-kafka-eventhub-config.md` | ✅ |
| 6 | `debezium/connect-worker-eventhub.properties.template` | ✅ — mantido como referência; a config real do container usa variáveis de ambiente (ver Desvios) |
| 7 | `docs/minio/kafka-notification-config-azure.md` | ✅ |
| 8 | `docs/azure/airbyte-mongodb-adls-config.md` | ✅ |
| 9 | `docs/azure/airbyte-minio-adls-config.md` | ✅ |

### Etapa 2 — Landing batch via sink (Postgres/Oracle) + Synapse (itens 10-14)

| Item | Arquivo | Status |
|------|---------|--------|
| 10 | `debezium/adls-sink-connector.json.template` | ✅ |
| 11 | `debezium/register-adls-sink-connector.ps1` | ✅ |
| 12 | `infra/azure/fase1-ingestao/synapse.tf` | ✅ Dedicated SQL Pool (DW100c) |
| 13 | `sql/azure/synapse_copy_merge.sql` | ✅ Padrão de referência (`orders`) — demais tabelas replicam o padrão |
| 14 | `docs/data-contract-cdc-azure.md` | ✅ |

### Etapa 3 — Lakehouse (itens 15-27)

| Item | Arquivo | Status |
|------|---------|--------|
| 15 | `infra/azure/fase1-ingestao/unity_catalog_credential.tf` | ✅ Storage credential (Service Principal) + external location + grant |
| 16 | `pipeline/bronze/ingest_postgres_drivers.sql` | ✅ Editado — `STREAM(uber_eats.raw.drivers)` → `read_files()` |
| 17 | `pipeline/bronze/ingest_postgres_users.sql` | ✅ Editado — mesma mudança |
| 18-24 | `pipeline/bronze/ingest_oracle_{orders,payments,receipts,order_items,inventory,products,restaurants}.sql` | ✅ Editados (7 arquivos) — `read_kafka()` → `read_files(format=>'text')`, resto inalterado |
| 25 | `pipeline/bronze/ingest_mongodb_perfil_restaurante.sql` | ✅ Criado — Bronze nova, dedupe por `restaurant_id` (mais recente por `_file_modification_time`) |
| 26 | `pipeline/silver/ingestion_mongo_perfil_restaurante.sql` | ✅ Editado — Federation → `live.bronze_perfil_restaurante` |
| 27 | `pipeline/silver/ingestion_kafka_*.sql` (6 arquivos) | ⚠️ **Não editado** — descoberta durante o Build: nenhum desses arquivos referencia um path físico (leem `STREAM(live.gps)` etc., resolvido pelo grafo do próprio pipeline) — ver Desvios e `docs/azure/minio-bronze-path-migration-note.md` |

### Etapa 4 — Kappa (itens 28-30)

| Item | Arquivo | Status |
|------|---------|--------|
| 28 | `infra/azure/fase1-ingestao/stream_analytics.tf` | ✅ Job + 3 inputs (Event Hub) + reference data input (MongoDB) + output placeholder |
| 29 | `sql/azure/stream_analytics_query.sql` | ✅ |
| 30 | `tests/azure/test_adls_sink_cdc_mapping.py` | ✅ 6 testes — todos passaram |

### Transversal (itens 31-33)

| Item | Status |
|------|--------|
| 31 — Atualizar roadmap com achado do `/design` (captura única) | ✅ Já feito durante o `/design` (v1.9) — sem trabalho adicional aqui |
| 32 — Verificar modelo conceitual | ✅ Confirmado no-op — `docs/MODELO_CONCEITUAL_UBER_EATS.md` já declara o modelo reaproveitado sem alteração entre as 3 clouds |
| 33 | `infra/azure/fase1-ingestao/variables.tf`, `outputs.tf`, `versions.tf` | ✅ |

---

## Desvios do DESIGN durante a implementação

1. **Cluster Kafka Connect dedicado (`kafka-connect-azure`), separado do `kafka-connect` existente.** O DESIGN falou em "worker apontado pro Event Hub" de forma genérica. Ao implementar, ficou claro que repontar o `bootstrap.servers` do `kafka-connect` **existente** (usado hoje pelo Debezium Oracle→Redpanda local, `pipeline/bronze/ingest_oracle_orders.sql` na Fase 0) quebraria esse pipeline local. Criado um serviço **novo e separado** em `docker-compose.yml` (`kafka-connect-azure`, porta 8084), com seu próprio `oracle-connector-azure.json.template` e `register-oracle-connector-azure.ps1` — nenhum arquivo da Fase 0/Onda 3 foi tocado.
2. **Config do worker via variáveis de ambiente, não arquivo `.properties`.** O `connect-worker-eventhub.properties.template` (item 6) foi mantido como referência de documentação, mas o container real (`quay.io/debezium/connect:3.0`, mesma imagem já usada em `kafka-connect`) é configurado por variáveis de ambiente `CONNECT_*` — mesmo padrão já usado no serviço `kafka-connect` existente. Ajustado em `docker-compose.yml`.
3. **Item 27 não corresponde a código versionado.** Os scripts `pipeline/silver/ingestion_kafka_*.sql`/`ingestion_mysql_menu.sql` não têm nenhuma referência de path físico (leem `STREAM(live.gps)`, resolvido internamente pelo grafo do pipeline Lakeflow) — a definição da fonte física dessas tabelas Bronze vive na configuração do workspace Databricks, fora deste repositório. Documentado como ação operacional pendente em `docs/azure/minio-bronze-path-migration-note.md`, sem editar arquivos que não precisavam mudar.
4. **`azurerm_storage_container` trocado por `azurerm_storage_data_lake_gen2_filesystem`.** O `azurerm_synapse_workspace` exige especificamente um ID no formato do segundo resource type. Corrigido em `storage_account.tf`, com as referências de `service_principal.tf`, `synapse.tf` e `stream_analytics.tf` ajustadas — os 2 role assignments passaram a usar escopo no Storage Account (não no filesystem), já que esse resource não expõe um `resource_manager_id` próprio.
5. **Provider `random` adicionado** (`versions.tf`) — necessário para `random_password.synapse_admin`, usado em `synapse.tf` e não declarado no `providers` original.
6. **Correção de sintaxe XML** em `debezium/hadoop-conf/core-site.xml.template`: o comentário continha `--` (hífen duplo), inválido dentro de comentários XML — só foi encontrado rodando `xml.etree.ElementTree.parse()` de verdade, não por leitura visual.
7. **Módulo Python novo (`src/azure/cdc_contract/mapping.py`) não estava no manifesto original.** Diferente da AWS/GCP (que tinham Lambdas/Cloud Functions reais para testar), esta feature é 100% configuração de serviços gerenciados — sem esse módulo, o item 30 (teste de contrato) não teria nenhum código real para validar. Criado para o teste ter substância, não só ler visualmente os templates JSON.

---

## Issues Encountered

### `terraform validate` não executou — binário indisponível neste ambiente

Diferente do build da AWS (que baixou o binário e falhou só no handshake TLS local), esta sessão não tinha o Terraform instalado e não foi feito o download (para não repetir o mesmo custo/risco já documentado). **Mitigação:** revisão manual de todos os 10 arquivos `.tf`, que encontrou e corrigiu 2 problemas reais antes mesmo de uma tentativa de `plan` (resource type do storage container/filesystem; provider `random` faltando) — ver Desvios #4 e #5. **Ação pendente para o usuário:** rodar `terraform init && terraform validate && terraform plan` num ambiente com o binário disponível, antes de qualquer `apply` real, especialmente quando a conta Azure for aberta.

### Bug real encontrado por validação de verdade, não por leitura visual

`debezium/hadoop-conf/core-site.xml.template` tinha um comentário XML inválido (`--` duplo) — só apareceu rodando `xml.etree.ElementTree.parse()` (ver Desvio #6). Reforça o mesmo padrão já visto no build da AWS: testes/validações reais encontram bugs que leitura visual não encontra.

### Testes unitários — sem problemas

`pytest` já estava disponível no `.venv` do projeto (usado por outras features). As 6 asserções cobrem tanto o mapeamento de campos (Postgres/Oracle) quanto a validade estrutural dos 2 templates JSON de conector — todas passaram na primeira execução, sem precisar de correção de código.

---

## Verificação executada

| ID | Verificação | Resultado |
|----|--------------|-----------|
| V-001 | `pytest tests/azure -v` | ✅ 6/6 passaram |
| V-002 | `ruff check src/azure tests/azure` | ✅ 0 erros |
| V-003 | `python -c "import yaml; yaml.safe_load(open('docker-compose.yml'))"` | ✅ YAML válido |
| V-004 | `python -c "import xml.etree.ElementTree as ET; ET.parse(...)"` sobre `core-site.xml.template` | ✅ Válido (após correção do Desvio #6) |
| V-005 | Revisão manual de todos os 10 `.tf` (referências cruzadas, resource types, providers) | ✅ Feita — 2 problemas reais encontrados e corrigidos (Desvios #4, #5) |
| V-006 | `terraform init`/`validate`/`plan` | ❌ Não executado — binário indisponível neste ambiente |
| V-007 | Deploy real (`terraform apply`) / smoke test contra Azure de verdade | **Não aplicável** — conta Azure ainda não aberta |

## Pendências antes do commit

Conforme `.claude/skills/git-boas-praticas-versionamento/SKILL.md`, commit é proposto e aguarda confirmação do usuário. **Atenção:** `docker-compose.yml` e `gen/.env.template` já estavam modificados (uncommitted) antes desta sessão, pelo trabalho da Fase 3/GCP — esta sessão adicionou mudanças **em cima** dessas, sem sobrepor nada (revisão feita via `git diff` antes de editar).

## Status: ✅ COMPLETE (com 1 verificação não executável neste ambiente, 1 item do manifesto revelado como não-aplicável ao código)

Todo o trabalho de código do manifesto foi implementado; os testes unitários passam de verdade (não só leitura visual), e a revisão manual dos `.tf` encontrou e corrigiu 2 problemas reais que só apareceriam num `terraform plan`. A única verificação que não pôde rodar (`terraform validate`) é uma limitação deste ambiente (binário ausente), não um problema do código — recomenda-se rodar `terraform init && terraform validate && terraform plan` no ambiente normal do usuário antes de qualquer `apply`, e validar de ponta a ponta o comportamento do Kafka Connect HDFS 2 Sink Connector contra o Event Hub real (risco sinalizado em `docs/data-contract-cdc-azure.md`) assim que a conta Azure for aberta.

**Próximo passo:** revisar o código gerado, confirmar o commit, e quando a conta Azure for aberta (início real da Fase 1): preencher os `.tfvars` com credenciais reais, rodar `terraform validate`/`plan` num ambiente com o binário disponível, e seguir o sequenciamento Etapa 1 → 2 → 3 → 4 já documentado no DEFINE/DESIGN.
