# DESIGN: Reorganização da Estrutura de Pastas da Raiz

| Campo | Valor |
|-------|-------|
| **Feature** | REORGANIZACAO_ESTRUTURA_RAIZ |
| **Input** | `.claude/sdd/features/DEFINE_REORGANIZACAO_ESTRUTURA_RAIZ.md` (v1.1) |
| **Status** | ✅ Complete (Designed) |
| **Data** | 2026-09-27 |
| **Mandato de pipeline** | N/A justificado — 100% relocação de arquivo, ver seção do DEFINE (não repetido aqui) |

---

## 1. Overview — Árvore da raiz (antes → depois)

```text
ANTES (raiz ~40+ entradas, 3 eixos misturados)          DEPOIS (6 agrupadores + ferramental agentic)
├── src/{aws,azure,gcp}/                                ├── aws/{src,infra,sql,tests,docs?,requirements-aws.txt}
├── infra/{aws,azure,gcp}/                               ├── azure/{src,infra,sql,tests,docs,requirements-azure?}
├── sql/{aws,azure,gcp,oracle,"cdc configure"}/          ├── gcp/{src,infra,sql,tests,docs,requirements-gcp.txt}
├── tests/{aws,azure,gcp}/                               ├── shared/
├── docs/{azure,gcp,adversarial,airbyte,automacao,       │   ├── pipeline/{bronze,silver,gold}
│         minio,postgres,shadowtraffic}/                │   ├── gen/{.env,.env.template,setup-configs.ps1,unified/}
├── pipeline/{bronze,silver,gold}/                       │   ├── mongo/init/
├── gen/{.env,.env.template,unified/,setup-configs.ps1}  │   ├── sql/{oracle/*.sql+*.sh, postgres/, legacy/}
├── mongo/init/                                          │   └── docs/{roadmap,modelo-conceitual,mandatos,guias,
├── debezium/{*.template,*.ps1,hadoop-conf/}             │       adversarial/,airbyte/,automacao/,minio/,postgres/,
├── deploy/autossh/                                      │       shadowtraffic/,PENDENCIAS-DOCKER-RESOURCES.md}
├── scripts/ (19 arquivos soltos na raiz da pasta)       ├── config/{aws,azure,gcp,shared}/  (só conexão/ambiente)
├── requirements.txt (raiz, vazio)                       │   ├── azure/{debezium/*.json.template,
├── requirements-{aws,gcp}.txt                            │   │        connect-worker-eventhub.properties.template,
└── docker-compose.yml, databricks.yml, README.md, …     │   │        hadoop-conf/core-site.xml.template}
                                                          │   ├── shared/debezium/oracle-connector.json.template
                                                          │   └── gcp/{deploy/autossh/*.service,
                                                          │            debezium-server/{oracle,postgres}/application.properties}
                                                          ├── scripts/{infra,ingestion,shadowtraffic,all,tooling,lib}/
                                                          │   └── README.md (índice)
                                                          └── docker-compose.yml, databricks.yml, README.md, CLAUDE.md,
                                                              CONTEXT.md, LICENSE, .env*, agentspec/, get_started/,
                                                              install_dev_loop/, templates/, .claude/, .cursor/, .github/
```

**Fora do escopo desta árvore (confirmado por inspeção — ver §3.9):** `.git/`, `.vscode/`, `.databricks/`, `.githooks/`, `.gitignore`, `.mcp.json`, `.cursorrules`, `.pytest_cache/`, `.ruff_cache/`, `.venv/`, `abctl-v0.30.3-windows-amd64/`, `logs/` — são dotfiles/dirs de ferramenta (IDE, git, ambiente virtual) ou já ignorados pelo Git; não fazem parte das "~40 entradas" que o problema-alvo descreve e não precisam de `git mv`.

## 2. Componentes

| Agrupador | Conteúdo | Owner conceitual |
|-----------|----------|-------------------|
| `aws/`, `azure/`, `gcp/` | Código, infra, SQL, testes e docs **específicos** de cada trilho de ingestão | Comparação lado a lado das 3 estratégias (objetivo central do portfolio) |
| `shared/` | O que roda igual nas 3 nuvens: pipeline Databricks, gerador ShadowTraffic, Mongo, SQL genérico, docs genéricos | Runtime comum |
| `config/{aws,azure,gcp,shared}/` | Só dado de conexão/ambiente (templates de connector, hadoop-conf, unit files de deploy) — nunca código nem dependências | Fronteira fixada na Pergunta 7 do brainstorm |
| `scripts/{infra,ingestion,shadowtraffic,all,tooling,lib}/` | Todo script executável do repo (exceto init de container — ver ADR-01) | Operação do ambiente local |

## 3. Decisões (ADRs inline)

### ADR-01 — Scripts de init de container ficam com o SQL, não em `scripts/`
| Atributo | Valor |
|---|---|
| Status | Accepted (já fechado no DEFINE v1.1) |
| Contexto | `sql/oracle/{01,02,03}_*.sh` são montados em `/container-entrypoint-startdb.d` e executados em ordem alfabética junto com `00_enable_archivelog.sql`. A Constraint original do DEFINE mandava todo `.sh` para `scripts/`. |
| Escolha | `sql/oracle/*.sh` + `*.sql` → `shared/sql/oracle/` (pasta inteira, intacta) |
| Alternativas rejeitadas | Mover `.sh` para `scripts/ingestion/` — rejeitado: separaria arquivos que o container Oracle espera na mesma pasta, quebrando a ordem de inicialização |
| Consequências | `scripts/` absorve só `debezium/register-*.ps1` como executável "solto" migrado |

### ADR-02 — `requirements.txt` (raiz) é removido
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | Confirmado por `grep -rl "requirements\.txt"` em todo o repo: **zero consumidores reais** apontam para o arquivo da raiz (todas as ocorrências são menções conceituais em KB/agentes, não instalação real). O arquivo está vazio (0 bytes). Não existe `requirements-azure.txt` — o padrão `requirements-{cloud}.txt` vale só para AWS/GCP. Não é in listada no allowlist de arquivos permitidos na raiz do Success Criteria do DEFINE. |
| Escolha | Remover `requirements.txt` (raiz) via `git rm` |
| Alternativas rejeitadas | Manter na raiz — rejeitado, não está no allowlist e não tem função; mover vazio para `shared/` — rejeitado, não há "pacote" `shared/` que o instale, só criaria um arquivo fantasma em outro lugar |
| Consequências | Pequena exceção à moldura "100% relocação" do DEFINE, mas de risco zero (arquivo vazio, sem consumidor confirmado) e alinhada ao Success Criteria (raiz só com os 6 agrupadores + allowlist) |

### ADR-03 — SQL Server legado vai para `shared/sql/legacy/`, não é removido
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | A-003 corrigida no DEFINE v1.1: `sql/cdc configure/database-cdc-config.sql` é T-SQL de SQL Server (`sp_cdc_enable_db`), sem serviço MSSQL no compose, sem consumidor ativo. |
| Escolha | `git mv "sql/cdc configure/database-cdc-config.sql" shared/sql/legacy/database-cdc-config.sql`, normalizando o nome de pasta (remove o espaço problemático) e adicionando `shared/sql/legacy/README.md` de 3 linhas explicando a origem/status órfão |
| Alternativas rejeitadas | Remover o arquivo — rejeitado: o DEFINE define esta feature como 100% relocação sem mudança de comportamento; decidir apagar código legado é uma decisão de limpeza separada, fora do escopo desta feature | Manter em `shared/sql/` misturado com CDC ativo — rejeitado: induziria o leitor a pensar que é CDC comum às 3 nuvens (era exatamente o erro do DEFINE v1.0) |
| Consequências | Preserva reversibilidade; deixa claro para o leitor (inclusive o avaliador externo) que é código órfão isolado, não parte do pipeline ativo |

### ADR-04 — `gen/.env` (real) vai para `shared/gen/.env`; `.env`/`.env.example` da raiz não se movem
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | Confirmado em `docker-compose.yml`: **todo** serviço usa `env_file: ./gen/.env` — o `.env` da raiz só alimenta a interpolação `${...}` dentro do próprio `docker-compose.yml` (ex.: nomes de imagem/porta). Mover `gen/` inteiro para `shared/gen/` já é MUST do DEFINE. |
| Escolha | `gen/.env`, `gen/.env.template`, `gen/setup-configs.ps1`, `gen/unified/` movem com `gen/` → `shared/gen/`. `env_file:` no compose passa de `./gen/.env` para `./shared/gen/.env` (8 ocorrências). `.env`/`.env.example` da raiz **permanecem na raiz** (já no allowlist do Success Criteria) |
| Alternativas rejeitadas | Centralizar `.env` real dentro de `config/shared/` — descartado no brainstorm (YAGNI, exigiria `--env-file` explícito em todo comando) |
| Consequências | Resolve A-004 sem necessidade de flag extra em nenhum comando `docker compose` |

### ADR-05 — Subpastas de `scripts/` e destino dos scripts de tooling agentic
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | Success Criteria do DEFINE exige `scripts/` "sem scripts soltos na raiz da pasta além de um README.md índice" — isso inclui, literalmente, `validate-agent-router.py`, `bootstrap-agentic-project.py`, `validate-agentic-template.py`, `validate-workflow-bundle.py`, `sync-workflow-bundle.sh`, `enable-git-hooks.sh`, `databricks-mcp-auth.ps1` (7 arquivos de tooling), hoje referenciados em **59 arquivos** (git hooks `.githooks/pre-commit`/`pre-push`, `agentspec/install_agentspec.py`, `agentspec/upgrade_agentic.py`, `install_dev_loop/`, `CLAUDE.md` + espelhos `.cursor/`/`.github/`, `.claude/CURSOR.MD`, `README.md`, docs internos) |
| Escolha | Subpastas: `scripts/infra/` (start/stop/reset-infra, start/stop-airbyte, toggle-ingestion), `scripts/shadowtraffic/` (toggle-shadowtraffic, shadowtraffic-report-loop, start/stop-generators), `scripts/all/` (start/stop-all), `scripts/tooling/` (os 7 arquivos de tooling agentic acima), `scripts/lib/` (shadowtraffic-common.ps1, mantém a exceção já existente no `.gitignore` `!scripts/lib/`). Todos os 59 consumidores são atualizados na Etapa 5 (maior lote de referências da feature) |
| Alternativas rejeitadas | Deixar tooling agentic na raiz de `scripts/` como excepção implícita — rejeitado: contradiz literalmente o Success Criteria do DEFINE, que já foi fechado e não é papel do `/design` reabrir |
| Consequências | Este é o maior blast radius de uma única decisão nesta feature — tratado como sub-etapa isolada e validado primeiro (é o que a Etapa 1 do Sequenciamento já reserva) |

### ADR-06 — Destino de cada connector Debezium e do Debezium Server GCP dentro de `config/`
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | `config/` é estritamente dado de conexão/ambiente. `src/gcp/debezium_server_{oracle,postgres}/application.properties` são hoje código no `src/gcp/`, mas o conteúdo é config de conexão (Kafka, GCP project, topic prefix) montado read-only pelo compose — mesma natureza dos `.json.template` do Debezium Connect. |
| Escolha | `config/shared/debezium/oracle-connector.json.template` (usa Redpanda local, alimenta `shared/pipeline/bronze/ingest_oracle_orders.sql`); `config/azure/debezium/{oracle-connector-azure,adls-sink-connector}.json.template` + `connect-worker-eventhub.properties.template`; `config/azure/hadoop-conf/core-site.xml.template`; `config/gcp/deploy/autossh/ubereats-gcp-tunnel.service`; `config/gcp/debezium-server/{oracle,postgres}/application.properties` (movidos de `src/gcp/debezium_server_*/`, que passam a conter só o `Dockerfile`/código, se houver). `debezium/register-*.ps1` (executáveis) → `scripts/ingestion/` |
| Alternativas rejeitadas | Manter `application.properties` em `src/gcp/` — rejeitado: contradiz a fronteira já fixada (config/ = conexão, não código) e deixa a config do Debezium Server fora do padrão dos outros connectors |
| Consequências | `docker-compose.yml` atualiza 2 mounts de `application.properties` (linhas ~168 e ~180) e 1 mount de `hadoop-conf` (linha ~232) |

### ADR-07 — AT-003 reescopado: sem edição em `databricks.yml`, validação condicional
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | `databricks.yml` não tem `resources:`/`include:` — nenhum path aponta para `pipeline/` hoje; o pipeline Lakeflow é anexado manualmente no Workspace (`pipeline/README.md`, seção "Como Usar no Lakeflow"). `databricks bundle validate` está disponível (CLI v1.12.1) mas falha por perfil ambíguo + token 403 — pré-condição de ambiente, não relacionada ao reorg (mesma ressalva já usada para `terraform` nos builds Azure/GCP). |
| Escolha | AT-003 passa a validar: (a) `databricks.yml` continua sintaticamente válido (não muda, nenhuma edição necessária); (b) comentário em `docker-compose.yml` (~linha 204: `pipeline/bronze/ingest_oracle_orders.sql` → `shared/pipeline/bronze/ingest_oracle_orders.sql`); (c) árvore ASCII e link relativo `../docs/minio/README.md` em `pipeline/README.md` (→ `shared/pipeline/README.md`, ajustar para `../../shared/docs/minio/README.md`); (d) `databricks bundle validate` fica documentado como condicional — roda se houver profile/token válido, senão o gate usa `grep` por `pipeline/` remanescente como fallback |
| Alternativas rejeitadas | Bloquear o `/build` até existir token válido — rejeitado: não é um problema introduzido pelo reorg, bloquear a feature por isso seria desproporcional |
| Consequências | AT-003 do DEFINE é reescrito no `/build` para refletir (b)+(c)+(d) em vez do texto original ("`databricks.yml` e jobs/pipelines atualizados") |

### ADR-08 — `.gitignore` atualizado no mesmo commit do `git mv`, com 2 regras novas
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | Regras hoje ancoradas na raiz (`gen/unified/uber-eats.json`, `gen/postgres/{drivers,users}.json`, `mongo/init/01_perfil_restaurante.js`, `!scripts/lib/`, `!scripts/lib/**`, `infra/**/.build/`) não têm `**/` — são ancoradas ao path exato a partir da raiz do `.gitignore`, logo **deixam de casar** com o novo path depois do `git mv`, abrindo uma janela onde um arquivo gerado com segredo poderia ser commitado por engano. Além disso, não existe hoje regra alguma para `debezium/hadoop-conf/core-site.xml` (real, com client secret do Service Principal Azure) nem para `gen/gcp-credentials.json` (montado 3x no compose, hoje ausente localmente) |
| Escolha | Atualizar no mesmo commit: `gen/unified/uber-eats.json` → `shared/gen/unified/uber-eats.json`; `gen/postgres/{drivers,users}.json` → `shared/gen/postgres/{drivers,users}.json`; `mongo/init/01_perfil_restaurante.js` → `shared/mongo/init/01_perfil_restaurante.js`; `!scripts/lib/`/`!scripts/lib/**` (sem mudança de path, `scripts/lib/` já é o destino). **Regras novas:** `config/azure/hadoop-conf/core-site.xml` (só o `.template` deve ser versionado) e `shared/gen/gcp-credentials.json` |
| Alternativas rejeitadas | Corrigir o `.gitignore` numa etapa separada, depois do move — rejeitado: abre janela real de exposição de segredo entre os dois commits |
| Consequências | Esta é a checagem de segurança mais crítica do `/build` (GOV-M01) — deve ser o primeiro item a validar em code review do PR |

### ADR-09 — Exemção de "referência quebrada" (AT-006) inclui SDD histórico de features já concluídas
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | `DESIGN_INGESTAO_AZURE_FASE1.md`, `DESIGN_INGESTAO_GCP_FASE3.md`, `DESIGN_DIVERSIFICACAO_FONTES_UBEREATS.md` e os respectivos `BUILD_REPORT_*.md` em `.claude/sdd/features/` e `.claude/sdd/reports/` citam paths antigos (`src/azure`, `infra/aws`, etc.), mas **não** estão em `.claude/sdd/archive/` nem `dev-loop-runs/` — a exemção literal do AT-006 do DEFINE não os cobre |
| Escolha | Tratar como registro histórico imutável (documentam o que existia no momento em que cada fase foi construída) — **não reescrever** esses paths. Só documentos "vivos" de navegação (`CONTEXT.md`, `README.md`, `.claude/CURSOR.MD`+espelhos, `.claude/commands/core/router.md`) são atualizados |
| Alternativas rejeitadas | Reescrever para manter consistência — rejeitado: falsificaria o registro histórico de "como era quando foi construído" |
| Consequências | AT-006 do `/build` deve excluir explicitamente `.claude/sdd/features/DESIGN_INGESTAO_*`, `DESIGN_DIVERSIFICACAO_*` e `.claude/sdd/reports/BUILD_REPORT_*` (além de `archive/` e `dev-loop-runs/`) do grep de validação |

### ADR-10 — `PENDENCIAS-DOCKER-RESOURCES.md` move para `shared/docs/`
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | Arquivo versionado na raiz, não está no allowlist do Success Criteria (`docker-compose.yml`, `databricks.yml`, `README.md`, `CLAUDE.md`, `CONTEXT.md`, `LICENSE`, `.env*`) — é nota de projeto, não config de ferramenta |
| Escolha | `git mv PENDENCIAS-DOCKER-RESOURCES.md shared/docs/PENDENCIAS-DOCKER-RESOURCES.md` |
| Consequências | Fecha um gap do mapeamento original do DEFINE (R4) |

### ADR-11 — Escopo explícito de dotfiles/dirs de ferramenta fora do reorg
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | `.vscode/`, `.databricks/`, `.githooks/`, `.gitignore`, `.mcp.json`, `.cursorrules`, `.pytest_cache/`, `.ruff_cache/`, `.venv/`, `abctl-v0.30.3-windows-amd64/`, `logs/` existem na raiz mas não apareciam no allowlist nem no escopo do DEFINE — confirmado por `git ls-files` que a maioria está no `.gitignore` (não versionada) e `.vscode/` é convenção de IDE |
| Escolha | Clarificar (sem mudar o DEFINE): esses itens ficam fora do escopo da feature — são geridos por ferramenta/ambiente local, não fazem parte das "~40 entradas" do problema original |
| Consequências | Nenhuma ação de `git mv`; apenas anotação para não gerar falso finding no `/pipeline-review-init` pós-`/build` |

### ADR-12 — Helper único de repo-root em `scripts/lib/`
| Atributo | Valor |
|---|---|
| Status | Accepted |
| Contexto | `scripts/lib/shadowtraffic-common.ps1:151` e vários scripts usam `Split-Path -Parent $PSScriptRoot` / `$PSScriptRoot\..\..\...` para acoplar caminhos entre pastas irmãs (`scripts/` ↔ `debezium/`, `gen/`). Mover um nível para dentro de subpastas (`scripts/ingestion/`, etc.) muda a profundidade e quebra esses cálculos silenciosamente |
| Escolha | Adicionar função `Get-RepoRoot` em `scripts/lib/shadowtraffic-common.ps1` (ou novo `scripts/lib/repo-root.ps1`), resolvendo via `git rev-parse --show-toplevel` com fallback para profundidade fixa; todo script novo/movido usa essa função em vez de `$PSScriptRoot\..\..` literal |
| Consequências | Elimina a classe de bug "profundidade errada após mover pasta" para futuras reorganizações também |

## 4. File Manifest (por etapa de sequenciamento)

Convenção: `git mv <origem> <destino>`. Diretórios inteiros são movidos como unidade salvo exceção listada.

### Etapa 1 — `scripts/`
| # | Origem | Destino | Ação |
|---|--------|---------|------|
| 1 | `scripts/start-infra.ps1`, `stop-infra.ps1`, `reset-all.ps1`, `start-airbyte.ps1`, `stop-airbyte.ps1`, `toggle-ingestion.ps1` | `scripts/infra/` | Move + corrigir `$PSScriptRoot` |
| 2 | `scripts/toggle-shadowtraffic.ps1`, `shadowtraffic-report-loop.ps1`, `start-generators.ps1`, `stop-generators.ps1` | `scripts/shadowtraffic/` | Move + corrigir `$PSScriptRoot` |
| 3 | `scripts/start-all.ps1`, `stop-all.ps1` | `scripts/all/` | Move + corrigir `$PSScriptRoot` |
| 4 | `scripts/validate-agent-router.py`, `bootstrap-agentic-project.py`, `validate-agentic-template.py`, `validate-workflow-bundle.py`, `sync-workflow-bundle.sh`, `enable-git-hooks.sh`, `databricks-mcp-auth.ps1` | `scripts/tooling/` | Move + atualizar 59 consumidores (ADR-05) |
| 5 | `scripts/lib/shadowtraffic-common.ps1` | `scripts/lib/` (sem mudança) | Modify — adiciona `Get-RepoRoot` (ADR-12) |
| 6 | `debezium/register-oracle-connector.ps1`, `register-oracle-connector-azure.ps1`, `register-adls-sink-connector.ps1` | `scripts/ingestion/` | Move |
| 7 | — | `scripts/README.md` | Modify — índice das subpastas |

### Etapa 2 — `aws/`, `azure/`, `gcp/`
| # | Origem | Destino |
|---|--------|---------|
| 8 | `src/aws/`, `infra/aws/`, `sql/aws/`, `tests/aws/`, `requirements-aws.txt` | `aws/{src,infra,sql,tests}/`, `aws/requirements.txt` |
| 9 | `src/azure/`, `infra/azure/`, `sql/azure/`, `tests/azure/`, `docs/azure/` | `azure/{src,infra,sql,tests,docs}/` |
| 10 | `src/gcp/` (exceto `debezium_server_*/application.properties`, ver #16), `infra/gcp/`, `sql/gcp/`, `tests/gcp/`, `docs/gcp/`, `requirements-gcp.txt` | `gcp/{src,infra,sql,tests,docs}/`, `gcp/requirements.txt` |
| 11 | `docs/data-contract-cdc-{aws-dms,azure,gcp-datastream}.md` | `{aws,azure,gcp}/docs/data-contract-cdc-*.md` |
| 12 | `docs/minio/kafka-notification-config-azure.md` | `azure/docs/minio/kafka-notification-config-azure.md` |
| 13 | `docs/minio/webhook-notification-config-gcp.md` | `gcp/docs/minio/webhook-notification-config-gcp.md` |

### Etapa 3 — `shared/`
| # | Origem | Destino |
|---|--------|---------|
| 14 | `pipeline/{bronze,silver,gold}/`, `pipeline/README.md` | `shared/pipeline/` |
| 15 | `gen/` (inteiro: `.env`, `.env.template`, `setup-configs.ps1`, `unified/`) | `shared/gen/` (ADR-04) |
| 16 | `mongo/init/` | `shared/mongo/init/` |
| 17 | `sql/oracle/` (`.sql`+`.sh` intactos, ADR-01) | `shared/sql/oracle/` |
| 18 | `sql/create_users_table.sql`, `sql/create_drivers_table.sql` | `shared/sql/postgres/` |
| 19 | `sql/cdc configure/database-cdc-config.sql` | `shared/sql/legacy/database-cdc-config.sql` + novo `shared/sql/legacy/README.md` (ADR-03) |
| 20 | `docs/00-INDEX.md`, `README.md`, `ROADMAP_ARQUITETURA_MULTICLOUD.md`, `MODELO_CONCEITUAL_UBER_EATS.md`, `MANDATOS_PIPELINE_DADOS.md`, `DATABRICKS_TEAMS_PIPELINES.md`, `GUIA_*.md`, `data-contract-TEMPLATE.md`, `inventario-ambiente.md.example`, `adversarial/`, `airbyte/`, `automacao/`, `postgres/`, `shadowtraffic/` | `shared/docs/` |
| 21 | `docs/minio/README.md`, `docs/minio/webhook-notification-config.md` | `shared/docs/minio/` (genérico, ADR fecha R4) |
| 22 | `PENDENCIAS-DOCKER-RESOURCES.md` | `shared/docs/PENDENCIAS-DOCKER-RESOURCES.md` (ADR-10) |

### Etapa 4 — `config/`
| # | Origem | Destino |
|---|--------|---------|
| 23 | `debezium/oracle-connector.json.template` | `config/shared/debezium/oracle-connector.json.template` |
| 24 | `debezium/oracle-connector-azure.json.template`, `adls-sink-connector.json.template`, `connect-worker-eventhub.properties.template` | `config/azure/debezium/` |
| 25 | `debezium/hadoop-conf/core-site.xml.template` | `config/azure/hadoop-conf/core-site.xml.template` |
| 26 | `deploy/autossh/ubereats-gcp-tunnel.service` | `config/gcp/deploy/autossh/ubereats-gcp-tunnel.service` |
| 27 | `src/gcp/debezium_server_oracle/application.properties`, `debezium_server_postgres/application.properties` | `config/gcp/debezium-server/{oracle,postgres}/application.properties` (ADR-06) |

### Etapa 5 — Referências (não move arquivo, edita conteúdo)
| # | Arquivo | Mudança |
|---|---------|---------|
| 28 | `docker-compose.yml` | 8× `env_file: ./gen/.env` → `./shared/gen/.env`; `./sql:/docker-entrypoint-initdb.d` → `./shared/sql/postgres:/docker-entrypoint-initdb.d`; `./sql/oracle:/container-entrypoint-startdb.d` → `./shared/sql/oracle:/...`; `./mongo/init:...` → `./shared/mongo/init:...`; 2× `application.properties` mount → `./config/gcp/debezium-server/...`; 3× `./gen/gcp-credentials.json` → `./shared/gen/gcp-credentials.json`; `./debezium/hadoop-conf:...` → `./config/azure/hadoop-conf:...`; comentário linha ~204 (ADR-07) |
| 29 | `.gitignore` | 5 regras reancoradas + 2 novas (ADR-08) |
| 30 | `CONTEXT.md` | Linhas 13–14 (`src/aws`, `infra/aws`) + tabela de estrutura geral |
| 31 | `README.md` | Árvore de pastas / links, se existirem |
| 32 | `.claude/CURSOR.MD` + espelhos `.cursor/CURSOR.MD`, `.github/CURSOR.MD` | Se citarem paths afetados |
| 33 | `.claude/commands/core/router.md` (+ espelhos) | Confirmar se cita paths afetados (inspeção não achou path literal, só placeholder genérico — revalidar no `/build`) |
| 34 | `.claude/skills/shadowtraffic-adicionar-generator-seguro/SKILL.md`, `shadowtraffic-ajustar-geracao/SKILL.md`, `shadowtraffic-renovar-licenca/SKILL.md` (+ espelhos) | Paths de `gen/`, `scripts/`, SQL init (R7) |
| 35 | `tests/azure/test_adls_sink_cdc_mapping.py` | `REPO_ROOT / "src" / "azure"` → `REPO_ROOT / "src"` (perde 1 nível); `REPO_ROOT / "debezium" / "*.template"` → `REPO_ROOT / "config" / "azure" / "debezium" / "*.template"` |
| 36 | `tests/aws/test_kappa_consumer_lookup.py`, `test_lambda_minio_kinesis_bridge.py` | `parents[2] / "src" / "aws"` → `parents[1] / "src"` |
| 37 | `tests/gcp/test_cloud_function_bridge.py`, `test_dataflow_consumer_lookup.py` | `parents[2] / "src" / "gcp"` → `parents[1] / "src"` |
| 38 | `src/azure/cdc_contract/mapping.py` → `azure/src/cdc_contract/mapping.py` | Autorreferência de comentário a `debezium/adls-sink-connector.json.template` → `config/azure/debezium/adls-sink-connector.json.template` |
| 39 | `docs/data-contract-cdc-aws-dms.md`, `-gcp-datastream.md` (após mover, #11) | Ajustar links internos relativos, se houver |

### Etapa 6 — Anomalias + validação final
| # | Item | Resultado da inspeção nesta sessão |
|---|------|-------------------------------------|
| 40 | `gen/unified/uber-eats.json;C` | **Confirmado inexistente** (`git ls-files` só mostra `uber-eats.json.template`) — Success Criteria já satisfeito, nenhuma ação |
| 41 | `__pycache__/` versionado em `tests/aws`, `tests/azure`, `src/aws`, `src/azure` | **Confirmado não versionado** (`git ls-files \| grep __pycache__` vazio; já cobertos por `.gitignore` linha 2) — Success Criteria já satisfeito, nenhuma ação |
| 42 | Validação final | `python3 scripts/tooling/validate-agent-router.py`, `docker compose config`, `pytest aws/tests azure/tests gcp/tests`, `databricks bundle validate` (condicional, ADR-07) |

## 5. Padrões de código

### 5.1 Helper de repo-root (ADR-12) — adicionar a `scripts/lib/shadowtraffic-common.ps1`

```powershell
function Get-RepoRoot {
    $root = (git rev-parse --show-toplevel 2>$null)
    if (-not $root) {
        # Fallback se não houver git no PATH: scripts/lib -> scripts -> raiz
        $root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
    }
    return $root
}
```

Scripts movidos/atualizados usam `$repoRoot = Get-RepoRoot` em vez de `$PSScriptRoot\..\..`.

### 5.2 `.gitignore` — diff conceitual (ADR-08)

```diff
- gen/postgres/drivers.json
- gen/postgres/users.json
- gen/unified/uber-eats.json
- mongo/init/01_perfil_restaurante.js
+ shared/gen/postgres/drivers.json
+ shared/gen/postgres/users.json
+ shared/gen/unified/uber-eats.json
+ shared/mongo/init/01_perfil_restaurante.js
+ config/azure/hadoop-conf/core-site.xml
+ shared/gen/gcp-credentials.json
```

### 5.3 `docker-compose.yml` — diff conceitual (item #28)

```diff
- env_file: ./gen/.env
+ env_file: ./shared/gen/.env
...
-   - ./sql:/docker-entrypoint-initdb.d
+   - ./shared/sql/postgres:/docker-entrypoint-initdb.d
...
-   - ./sql/oracle:/container-entrypoint-startdb.d
+   - ./shared/sql/oracle:/container-entrypoint-startdb.d
...
-   - ./src/gcp/debezium_server_postgres/application.properties:/debezium/conf/application.properties:ro
-   - ./gen/gcp-credentials.json:/debezium/gcp-credentials.json:ro
+   - ./config/gcp/debezium-server/postgres/application.properties:/debezium/conf/application.properties:ro
+   - ./shared/gen/gcp-credentials.json:/debezium/gcp-credentials.json:ro
...
-   - ./debezium/hadoop-conf:/etc/kafka-connect-azure/hadoop-conf:ro
+   - ./config/azure/hadoop-conf:/etc/kafka-connect-azure/hadoop-conf:ro
```

### 5.4 Sequência `git mv` — exemplo Etapa 1 (item #4)

```bash
mkdir -p scripts/tooling
git mv scripts/validate-agent-router.py scripts/tooling/validate-agent-router.py
git mv scripts/bootstrap-agentic-project.py scripts/tooling/bootstrap-agentic-project.py
git mv scripts/validate-agentic-template.py scripts/tooling/validate-agentic-template.py
git mv scripts/validate-workflow-bundle.py scripts/tooling/validate-workflow-bundle.py
git mv scripts/sync-workflow-bundle.sh scripts/tooling/sync-workflow-bundle.sh
git mv scripts/enable-git-hooks.sh scripts/tooling/enable-git-hooks.sh
git mv scripts/databricks-mcp-auth.ps1 scripts/tooling/databricks-mcp-auth.ps1
grep -rl "scripts/validate-agent-router.py" .githooks/ agentspec/ install_dev_loop/ CLAUDE.md .claude .cursor .github README.md
# atualizar cada um dos 59 consumidores confirmados antes de commitar a Etapa 1
```

## 6. Estratégia de Testes

| Acceptance Test | Ajuste feito no Design | Como validar no `/build` |
|---|---|---|
| AT-001 | Sem mudança — script real de smoke test | `.\scripts\infra\start-infra.ps1`, `.\scripts\shadowtraffic\toggle-shadowtraffic.ps1 status` |
| AT-002 | Adiciona mounts de `config/gcp/debezium-server` e `shared/*` | `docker compose config` sem path antigo |
| AT-003 | **Reescopado** (ADR-07) — sem edição em `databricks.yml`; valida comentário + README + bundle condicional | `grep -n "pipeline/" docker-compose.yml pipeline/README.md` (deve estar vazio fora de `shared/pipeline/`); `databricks bundle validate --profile <válido>` se disponível |
| AT-004 | Inclui reescrita de `parents[N]`/`REPO_ROOT` nos testes (item #35–37) | `pytest aws/tests azure/tests gcp/tests` |
| AT-005 | Path do script muda para `scripts/tooling/` | `python3 scripts/tooling/validate-agent-router.py` |
| AT-006 | **Exclui explicitamente** `.claude/sdd/features/DESIGN_INGESTAO_*`, `DESIGN_DIVERSIFICACAO_*`, `.claude/sdd/reports/BUILD_REPORT_*` da varredura (ADR-09) | `grep -rn` nos paths antigos, com os excludes acima |
| AT-007 | Sem mudança | `git log --follow --oneline -- shared/pipeline/bronze/ingest_oracle_orders.sql` |
| AT-008 | Sem mudança | Inspecionar `config/` — confirmar zero `.py`/`.sh`/`.ps1`/`requirements*.txt` |
| **Novo** | `.gitignore` protege segredo pós-move | `git check-ignore -v config/azure/hadoop-conf/core-site.xml shared/gen/gcp-credentials.json shared/gen/unified/uber-eats.json` — todos devem retornar match |
| **Novo** | Nenhum consumidor de `scripts/tooling/*` ficou órfão | `grep -rl "scripts/validate-agent-router.py\|scripts/bootstrap-agentic-project.py\|scripts/enable-git-hooks.sh"` fora de `scripts/tooling/` deve retornar vazio |

## 7. Quality Gate

```text
[x] Árvore antes/depois clara (§1)
[x] 12 decisões documentadas com racional e alternativas rejeitadas (§3)
[x] File manifest completo por etapa, confirmado por inspeção real do repo (não estimado) (§4)
[x] Padrões de código copy-paste (helper repo-root, diffs .gitignore/docker-compose, sequência git mv) (§5)
[x] Estratégia de teste cobre as 8 acceptance tests do DEFINE + 2 novas checagens de segurança/referência (§6)
[x] Sem dependência circular (scripts/tooling → consumidores é unidirecional)
```

## 8. Próximo passo

`/build .claude/sdd/features/DESIGN_REORGANIZACAO_ESTRUTURA_RAIZ.md` — em **branch dedicada** (quality tier `production`, blast radius confirmado ~40 arquivos de referência de conteúdo + ~90 arquivos movidos), com PR revisável antes de mergear em `main`, conforme Constraint do DEFINE.

## Status: ✅ Shipped

**Shipped and archived** em 2026-09-27 — ver `SHIPPED_2026-09-27.md` neste mesmo diretório. Build executado na branch `refactor/reorganizacao-estrutura-raiz` (pushed, ainda não mergeada em `main`).
