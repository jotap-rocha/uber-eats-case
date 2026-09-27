# DEFINE: Reorganização da Estrutura de Pastas da Raiz

| Campo | Valor |
|-------|-------|
| **Feature** | REORGANIZACAO_ESTRUTURA_RAIZ |
| **Origem** | Dev Loop `reorg-estrutura-raiz` — gate `escalate_sdd` (`.claude/sdd/dev-loop-runs/reorg-estrutura-raiz/phases/gate.md`) |
| **Input** | `.claude/sdd/features/BRAINSTORM_REORGANIZACAO_ESTRUTURA_RAIZ.md` |
| **Status** | ✅ Complete (Defined) |
| **Data** | 2026-09-27 |

---

## Problem Statement

A raiz do repositório acumulou **~40 entradas de topo** (contadas no brainstorm; hoje já mais, com Azure Fase 1/GCP Fase 3 commitados) misturando três eixos diferentes sem hierarquia clara: código/infra/docs/sql/tests **por nuvem** (`src/{aws,azure,gcp}`, `infra/{aws,azure,gcp}`, `sql/{aws,azure,gcp}`, `tests/{aws,azure,gcp}`, `docs/{azure,gcp}`), o que é **comum** às três nuvens (`pipeline/`, `gen/`, `mongo/`, `docs/` genérico), e pastas soltas de automação/config sem lar fixo (`debezium/`, `deploy/`, `scripts/`). Isso já dificulta comparar as 3 estratégias de ingestão lado a lado — o objetivo central deste portfolio — e centralizar configuração de conexão obriga a abrir 5+ pastas diferentes. O brainstorm já fechou a solução (Approach A: 6 agrupadores de topo por nuvem + `shared/` + `config/` + `scripts/`) e todas as decisões de escopo (8 perguntas respondidas, mapeamento validado como "Fechado" pelo usuário) — falta apenas formalizar isso em requisitos testáveis e resolver os pontos que o brainstorm deixou explicitamente para esta fase (mapeamento fino de pastas ambíguas, ver Open Questions).

## Target Users

| Usuário | Papel | Dor |
|---------|-------|-----|
| Autor do projeto (portfólio pessoal) | Desenvolvedor/arquiteto de dados mantendo e evoluindo o pipeline multi-cloud | Estrutura atual dispersa dificulta comparar AWS/Azure/GCP lado a lado, achar config de conexão e adicionar scripts sem criar mais uma pasta solta na raiz |
| Recrutador/avaliador técnico (leitor externo do portfolio) | Avalia a organização do repositório como sinal de qualidade de engenharia | Raiz com ~40 entradas sem hierarquia passa impressão de desorganização, mesmo com conteúdo tecnicamente correto |

## Goals

| Grupo | Prioridade | Meta |
|-------|------------|------|
| Estrutura de topo | **MUST** | Criar 6 agrupadores de topo: `aws/`, `azure/`, `gcp/`, `shared/`, `config/`, `scripts/` |
| `aws/` / `azure/` / `gcp/` | **MUST** | `git mv` de `src/{cloud}`, `infra/{cloud}`, `sql/{cloud}`, `tests/{cloud}`, `docs/{cloud}` (quando existir) e `requirements-{cloud}.txt` para dentro do agrupador da respectiva nuvem, preservando histórico do Git |
| `shared/` | **MUST** | `git mv` do que é comum às 3 nuvens: `pipeline/` (Bronze/Silver/Gold Databricks), `mongo/`, `gen/`, `sql/oracle/`, `sql/cdc configure/`, e os docs genéricos de `docs/` (roadmap, modelo conceitual, mandatos, guias, `adversarial/`, `airbyte/`, `automacao/`, `minio/` não-cloud-specific, `postgres/`, `shadowtraffic/`) |
| `config/` | **MUST** | Criar `config/{aws,azure,gcp,shared}/` contendo só dado de conexão/ambiente (não dependências, não scripts executáveis — fronteira já fixada na Pergunta 7 do brainstorm): templates de connector Debezium (`*.json.template`, `*.properties.template`), `hadoop-conf/*.xml.template`, unit files de deploy (`deploy/autossh/*.service`) |
| `scripts/` | **MUST** | Reorganizar `scripts/` em subpastas por assunto (infra, ingestão/CDC, ShadowTraffic, orquestração "tudo", validação, ferramental agentic) e absorver scripts hoje soltos em `debezium/` (`register-*.ps1`). **Exceção (corrigida em v1.1):** `sql/oracle/*.sh` **não** entram em `scripts/` — são scripts de init de container Oracle montados em `/container-entrypoint-startdb.d` e executados em ordem alfabética junto com os `.sql` da mesma pasta; ficam em `shared/sql/oracle/` junto do SQL, não em `scripts/` |
| Referências | **MUST** | Atualizar toda referência de path quebrada: `docker-compose.yml`, `databricks.yml`, scripts (`$PSScriptRoot`/paths relativos), `CONTEXT.md`, `.claude/CURSOR.MD` (e espelhos `.cursor/`/`.github/`), `.claude/commands/core/router.md`, `README.md`, links internos de `docs/` |
| Anomalias | **MUST** | Resolver antes ou durante o `git mv`: confirmar/remover `gen/unified/uber-eats.json;C` se for lixo; remover `__pycache__/` versionado de `tests/aws`, `tests/azure`, `src/aws`, `src/azure` e adicionar ao `.gitignore` |
| Reversibilidade | **MUST** | Executar em branch dedicada, com PR revisável — dado o blast radius (quality tier `production`, já fixado no brainstorm) |
| — | **SHOULD** | Rodar `/pipeline-review-init` (ou equivalente) após o `/build`, mesma prática já usada nas fases anteriores, focado em confirmar que a relocação não alterou comportamento |

## Sequenciamento (mitigação de risco)

| Etapa | Escopo | Por que nessa ordem |
|-------|--------|----------------------|
| **1** | `scripts/` — reorganizar em subpastas e corrigir `$PSScriptRoot`/paths relativos internos | Menor superfície (só a própria pasta + quem a chama), maior risco de quebra silenciosa (scripts que se chamam entre si) — validar o padrão de correção aqui antes de aplicar em escala |
| **2** | `aws/`, `azure/`, `gcp/` — mover conteúdo já isolado por nuvem (`src/{cloud}`, `infra/{cloud}`, `sql/{cloud}`, `tests/{cloud}`, `docs/{cloud}`, `requirements-{cloud}.txt`) | Cada nuvem é uma unidade fechada — baixo acoplamento entre si, pode ser feito e validado nuvem por nuvem |
| **3** | `shared/` — mover `pipeline/`, `gen/`, `mongo/`, `sql/oracle`, `sql/cdc configure`, docs genéricos | Depende dos agrupadores de nuvem já existirem (para separar o que é genuinamente comum do que só parecia comum) |
| **4** | `config/` — extrair templates de conexão (Debezium, hadoop-conf, deploy) para `config/{cloud}` | Depende de `aws/azure/gcp/shared` já existirem como destino |
| **5** | Referências — varrer e corrigir todo path quebrado (`docker-compose.yml`, `databricks.yml`, docs, agentic) | Última etapa — só depois que os arquivos já estão no destino final, para não corrigir referência duas vezes |
| **6** | Anomalias (`__pycache__`, `uber-eats.json;C`) + validação final | `python3 scripts/validate-agent-router.py` (ou novo path), `docker compose config`, smoke test dos scripts críticos |

## Success Criteria

- [ ] Raiz do repositório contém só os 6 agrupadores de topo (`aws/`, `azure/`, `gcp/`, `shared/`, `config/`, `scripts/`), o ferramental agentic (`agentspec/`, `.agentspec-test/`, `get_started/`, `install_dev_loop/`, `templates/`, `.claude/`, `.cursor/`, `.github/`) e os arquivos de configuração de ferramenta que precisam ficar na raiz (`docker-compose.yml`, `databricks.yml`, `README.md`, `CLAUDE.md`, `CONTEXT.md`, `LICENSE`, `.env*`)
- [ ] `debezium/` e `deploy/` como pastas soltas na raiz deixam de existir
- [ ] `scripts/` está organizado em subpastas por assunto, sem scripts soltos na raiz da pasta além de um `README.md` índice
- [ ] Nenhum path antigo (`src/aws`, `infra/azure`, `sql/gcp`, `debezium/`, `deploy/`, scripts antigos) remanescente em referência ativa (`docker-compose.yml`, `databricks.yml`, scripts, docs, arquivos agentic)
- [ ] `python3 scripts/validate-agent-router.py` (no novo path, se mudar) passa sem erro
- [ ] `docker compose config` resolve sem erro a partir da raiz
- [ ] Histórico de Git preservado (`git log --follow` funciona nos arquivos movidos)
- [ ] `__pycache__/` removido do controle de versão em `tests/aws`, `tests/azure`, `src/aws`, `src/azure`, com entrada correspondente em `.gitignore`
- [ ] `gen/unified/uber-eats.json;C` resolvido (removido, se confirmado lixo, ou justificado se não for)

## Acceptance Tests

| ID | Cenário | Given | When | Then |
|----|---------|-------|------|------|
| AT-001 | Scripts continuam funcionando após reorganizar `scripts/` | Scripts movidos para subpastas, `$PSScriptRoot`/paths relativos corrigidos | Rodar `.\scripts\<subpasta>\start-infra.ps1` e `.\scripts\<subpasta>\toggle-shadowtraffic.ps1 status` | Executam sem erro de path, com o mesmo comportamento de antes da reorganização |
| AT-002 | Docker Compose resolve após mover pastas | `docker-compose.yml` atualizado com os novos paths (volumes, `env_file`, build contexts) | Rodar `docker compose config` na raiz | Sai sem erro, sem path antigo (`./debezium/...`, `./sql/oracle/...` etc.) |
| AT-003 | Databricks bundle resolve após mover `pipeline/` para `shared/` | `databricks.yml` e jobs/pipelines atualizados com o novo path de `shared/pipeline/` | Rodar `databricks bundle validate` (se aplicável neste ambiente) | Sai sem erro, sem path antigo `pipeline/...` |
| AT-004 | Nenhuma nuvem quebrou depois de mover para agrupador próprio | `aws/`, `azure/`, `gcp/` populados a partir de `src/{cloud}`, `infra/{cloud}`, `sql/{cloud}`, `tests/{cloud}` | Rodar `pytest` dentro de `aws/tests`, `azure/tests`, `gcp/tests` (conforme path novo) | Testes passam com a mesma taxa de sucesso registrada nos `BUILD_REPORT_*` de cada fase |
| AT-005 | Validação do router de agentes continua passando | `AGENT_ROUTER.yaml` e `scripts/validate-agent-router.py` (ou novo path) atualizados | Rodar `python3 scripts/validate-agent-router.py` | Passa sem erro |
| AT-006 | Documentação e arquivos agentic sem referência quebrada | `CONTEXT.md`, `.claude/CURSOR.MD` (+ espelhos), `README.md`, `router.md`, docs internos atualizados | `grep -rn` pelos paths antigos (`src/aws`, `infra/azure`, `sql/gcp`, `debezium/`, `deploy/`) em arquivos ativos (fora de `.claude/sdd/archive/` e `dev-loop-runs/` históricos) | Nenhuma ocorrência fora de contexto histórico/arquivado |
| AT-007 | Histórico de Git preservado | Arquivos movidos via `git mv` | Rodar `git log --follow --oneline -- shared/pipeline/bronze/ingest_oracle_orders.sql` (exemplo) | Mostra o histórico de commits anterior à mudança de path |
| AT-008 | `config/` contém só dado de conexão | `config/{aws,azure,gcp,shared}/` criados | Inspecionar o conteúdo de `config/` | Nenhum arquivo `.py`/`.sh`/`.ps1` executável nem `requirements*.txt` dentro de `config/` |

## Out of Scope

| Item | Por que fica para depois |
|------|-----------------------------|
| Reorganizar `agentspec/`, `.agentspec-test/`, `get_started/`, `install_dev_loop/`, `templates/` | Decisão #3 do brainstorm — ferramental do formato agentic, ciclo de vida e dono diferentes do pipeline de dados |
| Mover `docker-compose.yml`/`databricks.yml` para fora da raiz (inclusive para dentro de `config/`) | Descartado no brainstorm (YAGNI) — ferramentas esperam esses arquivos na raiz por padrão; mover exigiria flags extras sem ganho claro |
| Centralizar o `.env` ativo fora da raiz | Docker Compose carrega `.env` da raiz por padrão — decisão fina de `/design` (ver Open Questions), não escopo fechado aqui |
| Alterar lógica de pipeline, Terraform ou código de aplicação | Escopo é só localização de arquivos e correção de referências — nenhuma mudança de comportamento |
| Mover `.env`/dependências de infraestrutura Terraform (`.tfvars`) para `config/` | `config/` é escopo de conexão/ambiente runtime (Debezium, hadoop-conf, deploy), não variáveis de Terraform — essas continuam junto ao módulo de cada nuvem |
| `git mv` nesta sessão sem branch dedicada | Quality tier `production` (fixado no brainstorm) exige branch + PR revisável, dado o blast radius |

## Constraints

- **Pré-condição já satisfeita:** o brainstorm bloqueava o `/build` até o trabalho não commitado (Azure Fase 1/GCP Fase 3/Diversificação de Fontes) ser commitado — isso já ocorreu nesta sessão (commits `e0c9363`, `1ac5f21`, `e56b70c`, `b1a28c5`). O reorg pode prosseguir para `/design`/`/build`.
- Toda movimentação de arquivo deve usar `git mv` (ou equivalente que preserve rename detection do Git) — nunca delete+create.
- `config/` é estritamente dado de conexão/ambiente — nunca dependências (`requirements*.txt` ficam junto do código de cada nuvem) nem scripts executáveis (ficam em `scripts/`), fronteira já fixada na Pergunta 7 do brainstorm.
- `scripts/` absorve **todo** script executável do repositório (exceto o que vive dentro de `agentspec/`/`install_dev_loop/`, fora de escopo, e exceto scripts de init de container — ver exceção abaixo), incluindo os hoje soltos em `debezium/register-*.ps1`.
- **Exceção (corrigida em v1.1):** `sql/oracle/*.sh` **não** vão para `scripts/` — são scripts de init de container Oracle, montados em `/container-entrypoint-startdb.d` e executados em ordem alfabética junto com os `.sql` da mesma pasta; ficam em `shared/sql/oracle/` junto do SQL, para não separar arquivos que o container espera na mesma pasta e quebrar a inicialização ordenada.
- Nenhum secret real pode ser movido/exposto durante o reorg — arquivos `.env` reais (não os `.template`) seguem as mesmas regras de `.gitignore` de hoje.
- Execução em branch dedicada, com PR revisável antes de mergear em `main` — dado o quality tier `production` e o blast radius (~90 arquivos com referência a paths que mudam, por levantamento desta sessão).
- Esta feature é 100% relocação de arquivo + atualização de referência — nenhuma categoria do `PIPELINE_MANDATORY_PRACTICES.yaml` introduz obrigação nova (ver seção de mandato abaixo), mesmo o sinal "medalhão bronze silver gold" disparando por mover `pipeline/`.

## Assumptions

| ID | Suposição | Impacto se errada | Validada? |
|----|-----------|---------------------|-----------|
| A-001 | `debezium/hadoop-conf/core-site.xml.template` é especificamente do trilho Azure (ABFS/ADLS), não genérico nem GCP (GCS) | Se for usado por mais de uma nuvem, precisa ir para `shared/` ou ser duplicado por nuvem em vez de só `config/azure/` | [ ] Validar no `/design`, inspecionando o conteúdo do XML |
| A-002 | `requirements.txt` (raiz, hoje vazio/quase vazio) é escopo do próprio ferramental agentic/scripts (ex.: `pyyaml` para `validate-agent-router.py`), não de uma nuvem específica — deve permanecer na raiz ou ir para `shared/` | Se depender de alguma nuvem específica, a divisão muda | [ ] Validar no `/design`, inspecionando conteúdo real e quem o instala |
| A-003 | ~~`sql/cdc configure/database-cdc-config.sql` é configuração de CDC genérica do Postgres (replication slot), comum às 3 nuvens, não específica de uma delas~~ — **Corrigido em v1.1:** inspeção confirmou que o script é T-SQL de **SQL Server** (`USE [owshq-mssql-dev]`, `sp_cdc_enable_db`, `sp_cdc_enable_table`), não Postgres. Não há serviço MSSQL no `docker-compose.yml` nem consumidor ativo do script — é legado/órfão, não CDC comum às 3 nuvens | Não deve ir para `shared/sql/` como "CDC comum" — destino a decidir no `/design` entre `shared/sql/legacy/` (com justificativa) ou remoção | [x] Corrigido nesta sessão (2026-09-27), destino final fica para o `/design` |
| A-004 | O `.env`/`.env.example` ativos na raiz podem permanecer na raiz (fora do reorg) sem quebrar a convenção do Docker Compose | Se o objetivo de "config centralizada" exigir mover o `.env` real também, precisa de `--env-file` explícito em todos os comandos `docker-compose`/scripts | [ ] Já sinalizado como decisão fina de `/design` no próprio brainstorm |
| A-005 | Nenhuma ferramenta externa (CI, links compartilhados, bookmarks) depende hoje de paths absolutos deste repositório que não sejam os já mapeados em `docs`/`.claude`/`.github`/`.cursor` | Se existir, algo quebra fora do repositório sem sinal local | [ ] Repositório não tem CI configurada hoje (`CLAUDE.md`) — risco considerado baixo |

## Requisitos operacionais de pipeline (mandato)

Sinal `medalhão bronze silver gold` de `PIPELINE_MANDATORY_PRACTICES.yaml` dispara por esta feature mover `pipeline/` (Bronze/Silver/Gold) para `shared/pipeline/` — mas é puramente relocação de arquivo, sem mudança de lógica/comportamento (`exclude_when: documentação pura` não se aplica literalmente, mas o espírito — nenhum runtime de pipeline muda — sim).

| Categoria | Status | Justificativa |
|-----------|--------|----------------|
| Contrato de dados (DC-M01-05) | **N/A justificado** | Nenhum contrato de dado muda — só o path físico dos arquivos `.sql` que já implementam o contrato existente |
| Medalhão e UC (MED-M01-04) | **N/A justificado** | Bronze/Silver/Gold mantêm exatamente a mesma lógica; só o path de `pipeline/` para `shared/pipeline/` muda. `databricks.yml`/jobs precisam apontar pro novo path (coberto em AT-003), mas isso é referência, não comportamento |
| Qualidade e quarentena (DQ-M01-05) | **N/A justificado** | Sem mudança de regra de qualidade |
| Schema drift (SD-M01-04) | **N/A justificado** | Sem mudança de schema ou Auto Loader |
| Teams / alertas (TM-M01-06) | **N/A justificado** | Sem mudança de alerta operacional |
| Observabilidade (OBS-M01-03) | **N/A justificado** | Sem mudança de logging/observabilidade |
| Erros e resiliência (ERR-M01-02) | **N/A justificado** | Sem mudança de tratamento de erro |
| Segurança (GOV-M01-02) | **MUST — GOV-M01 aplica** | Nenhum secret real pode ser exposto/perdido durante o `git mv` (ex.: `.env` real, `gen/unified/uber-eats.json` gerado) — checklist explícito no `/design` |
| Testes (TEST-M01-02) | **SHOULD** — TEST-M02 | Rodar a suíte de testes de cada nuvem (`pytest aws/tests`, `azure/tests`, `gcp/tests` nos novos paths) após o `git mv`, confirmando mesma taxa de sucesso dos `BUILD_REPORT_*` originais (AT-004) |
| PyODBC (PYODBC-M01-05) | **N/A** | Não se aplica a esta feature |

## Clarity Score Breakdown

| Elemento | Score | Justificativa |
|----------|-------|----------------|
| Problem | 3/3 | Claro e específico — dispersão da raiz, eixo de agrupamento já validado (nuvem no topo), dor concreta de configuração espalhada |
| Users | 3/3 | Dois usuários identificados (autor mantendo o repo, avaliador externo lendo), cada um com a dor associada |
| Goals | 3/3 | 8 metas MUST + 1 SHOULD, cada uma ligada a um grupo concreto de pastas/arquivos, sequenciadas por etapa com justificativa de ordem |
| Success | 3/3 | Critérios testáveis por comando (`docker compose config`, `validate-agent-router.py`, `git log --follow`, `pytest`), 8 acceptance tests com Given/When/Then |
| Scope | 3/3 | Fora de escopo, constraints e assumptions delimitam claramente o que fica para o `/design`, com as 5 ambiguidades reais do mapeamento (hadoop-conf, requirements.txt, cdc-configure, `.env`, ferramentas externas) explicitadas como assumptions a validar, não escondidas |
| **Total** | **15/15** | Acima do mínimo de 12 — segue para Design sem gaps bloqueantes. As 5 assumptions não bloqueiam o Define porque já têm dono (`/design`) e não mudam o formato/escopo geral, só o destino fino de ~5 arquivos específicos |

## Open Questions

- `debezium/hadoop-conf/core-site.xml.template` é Azure (ABFS) ou compartilhado com GCP (GCS)? — inspecionar conteúdo no início do `/design` (A-001)
- Destino de `requirements.txt` (raiz) — permanece na raiz, ou vai para `shared/`? — inspecionar quem o consome (A-002)
- ~~`sql/cdc configure/database-cdc-config.sql` é genérico ou específico de uma fase/nuvem?~~ — **Resolvido em v1.1:** é T-SQL de SQL Server legado/órfão (não Postgres, não CDC comum às 3 nuvens). Resta decidir no `/design` apenas o destino final: `shared/sql/legacy/` (com justificativa) ou remoção (A-003)
- Centralizar também o `.env` ativo (não só os `.template`) dentro de `config/`, ou mantê-lo na raiz por convenção do Docker Compose? — decisão fina já sinalizada no brainstorm para o `/design` (A-004)
- Nomes exatos das subpastas de `scripts/` por assunto (ex.: `scripts/infra/`, `scripts/ingestion/`, `scripts/shadowtraffic/`, `scripts/all/`, `scripts/validation/`, `scripts/tooling/`, ou outra convenção) — detalhar no `/design`, junto do file manifest completo pasta-a-pasta
- Path exato de destino de cada connector Debezium dentro de `config/{cloud}/` (ex.: `config/azure/debezium/`, `config/azure/hadoop-conf/`) — detalhar no `/design`
- Se `databricks.yml`/jobs Databricks deste ambiente estão de fato configurados para rodar `databricks bundle validate` localmente (AT-003 depende disso) — confirmar disponibilidade da ferramenta no início do `/design`, mesma ressalva já registrada nos builds Azure/GCP sobre `terraform` não estar disponível neste ambiente

## Revision History

| Versão | Data | Mudança |
|--------|------|---------|
| 1.0 | 2026-09-27 | Documento inicial, extraído de `BRAINSTORM_REORGANIZACAO_ESTRUTURA_RAIZ.md`. Todas as 8 decisões de escopo já estavam fechadas no brainstorm. Adicionado: sequenciamento em 6 etapas, 8 acceptance tests, resolução da pré-condição de commit (já satisfeita nesta sessão), e 5 assumptions explícitas cobrindo as ambiguidades de mapeamento fino que o brainstorm deixou para esta fase (hadoop-conf, `requirements.txt`, `cdc configure`, `.env` ativo, ferramentas externas) |
| 1.1 | 2026-09-27 | Correções pré-`/design` a partir de inspeção real do repositório (via `/intake`, agentes `@design-agent` e `@databricks-platform-engineer`): (1) A-003 corrigida — `sql/cdc configure/database-cdc-config.sql` é T-SQL de SQL Server legado/órfão, não CDC genérico do Postgres comum às 3 nuvens; (2) Constraint de `scripts/` corrigida — `sql/oracle/*.sh` **não** entram em `scripts/` (são scripts de init de container executados em ordem com os `.sql`); passam a ter exceção explícita, ficando em `shared/sql/oracle/` |

---

## Status: ✅ Complete (Defined)

**Próximo passo:** `/design .claude/sdd/features/DEFINE_REORGANIZACAO_ESTRUTURA_RAIZ.md`
