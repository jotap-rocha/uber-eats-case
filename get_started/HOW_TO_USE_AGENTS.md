# HOW_TO_USE_AGENTS

Guia de referência para os **agentes** deste repositório: onde estão, para que servem e como acioná-los no **Cursor**, no **Claude Code** e no **GitHub Copilot** (VS Code ou editor compatível).

**Quem está clonando o template:** leia antes [`START_HERE.md`](START_HERE.md) — resume **personalização** (triângulo `CONTEXT.md` + `.cursorrules` + `docs/00-INDEX.md`) e o papel de **`.cursor/`** como referência principal.

Para a estrutura geral de projetos com agentes, veja também [`MANUAL_AGENTES.md`](MANUAL_AGENTES.md).

**Definition of Done (processo do time):** quando uma mudança afetar **como se roda, navega ou depura** o projeto, abra PR (ou inclua na mesma entrega) com atualização de **`CONTEXT.md`** e, se aplicável, de **`.cursorrules`**, **`.cursor/CURSOR.MD`**, **`.github/copilot-instructions.md`**, **`.claude/CLAUDE.md`** (trechos equivalentes) e **`.cursor/commands/core/router.md`** (sobretudo se mudarem agentes ou prioridades de roteamento). Assim a documentação de contexto vira critério explícito de entrega, e não só texto de apoio nos agentes.

---

## Referência principal e outras ferramentas

| Papel | Caminho base |
|-------|----------------|
| **Referência principal (dia a dia no Cursor)** | `.cursor/agents/`, `.cursor/kb/`, `.cursor/commands/`, `.cursor/sdd/` |
| **Claude Code** | `.claude/agents/`, `.claude/kb/`, … (quando existirem) |
| **GitHub Copilot** | `.github/agents/`, `.github/kb/`, `.github/commands/`, … (quando existirem) |

**Não há sincronização automática** entre essas árvores. Se o time versionar mais de uma, **alinhe manualmente** ao fechar PR quando a política exigir conteúdo equivalente.

As **tabelas** abaixo listam arquivos por **nome** (ex.: `spark-expert.md`); o caminho completo segue o padrão:

- Cursor: `.cursor/agents/<pasta>/<arquivo>.md`
- Claude Code: `.claude/agents/<pasta>/<arquivo>.md`
- GitHub Copilot: `.github/agents/<pasta>/<arquivo>.md`

---

## O que é um “agente” aqui?

Cada agente é um arquivo Markdown com **instruções de sistema** (papéis, fluxos, exemplos em frontmatter e corpo). O assistente da ferramenta **pode** seguir esse conteúdo quando você:

- **referencia o arquivo** no chat (caminho do workspace), ou
- **cola trechos** relevantes (“Quick Reference”, critérios de decisão), ou
- no Cursor, usa o **painel de Agentes** / Composer apontando para o `.md`.

Eles **não rodam sozinhos**: você os “liga” ao contexto da conversa ou da tarefa.

**Comandos slash** (ex.: `/dev`, `/create-pr`, `/core/agent`) estão documentados sob **`.cursor/commands/`** (e podem ter cópias em `.github/commands/`). No Cursor, use-os como atalho de fluxo; no Claude Code e no Copilot, o equivalente é **abrir o `.md` do comando** e seguir o roteiro ou pedir ao assistente para aplicar aquele fluxo.

---

## Como usar no Cursor

### 1. Referenciar o arquivo do agente (`@`)

No chat ou no Composer, digite `@` e escolha o arquivo, por exemplo:

- `@.cursor/agents/data-engineering/spark-expert.md`

Assim o modelo lê as regras daquele agente **nesta interação**.

**Exemplo de mensagem:**

```text
@.cursor/agents/data-engineering/spark-troubleshooter.md

Meu job PySpark falhou com java.lang.OutOfMemoryError no executor.
O que ajustar primeiro: shuffle, memória ou número de partições?
```

### 2. Abrir o painel de Agentes

1. Abra a área de **Agentes** (ou criação de agente personalizado, conforme sua versão do Cursor).
2. Selecione ou associe o arquivo `.md` do agente desejado em `.cursor/agents/...`.
3. Descreva a tarefa; o conteúdo do `.md` orienta comportamento e ferramentas sugeridas no frontmatter.

### 3. Copiar um trecho objetivo do `.md`

Se a conversa estiver longa, você pode colar no prompt uma seção curta do agente (por exemplo “Ações Imediatas” ou “Quick Reference”) + sua pergunta. Útil quando o arquivo é grande.

### 4. Encadear agentes (fluxo SDD / Dev Loop)

Alguns agentes foram pensados em sequência (ver tabela **workflow** e **dev**). Exemplo de roteiro em uma única thread:

```text
1) @.cursor/agents/workflow/brainstorm-agent.md — esboçar ideias e riscos da feature X
2) @.cursor/agents/workflow/define-agent.md — transformar em requisitos estruturados
3) @.cursor/agents/workflow/design-agent.md — desenho técnico e manifesto de arquivos
4) @.cursor/agents/workflow/build-agent.md — implementar conforme o design
```

Para o **Dev Loop**, use `prompt-crafter` para gerar um `PROMPT_*.md` e depois `dev-loop-executor` para executá-lo com verificações.

### 5. Roteamento

- [`.cursor/commands/core/router.md`](../.cursor/commands/core/router.md)
- Comando **`/core/agent`** — [`.cursor/commands/core/agent.md`](../.cursor/commands/core/agent.md) (um agente, resposta direta)
- Comando **`/intake`** — [`.cursor/commands/intake.md`](../.cursor/commands/intake.md) (1–3 agentes, execução paralela quando possível, **resposta consolidada** na mesma conversa)

```text
/intake Como garantir idempotência no reprocessamento medallion com falhas parciais no Spark?
```

---

## Como usar no Claude Code

1. **Caminhos dos agentes** — Use **`.claude/agents/`** quando existir (ex.: `.claude/agents/data-engineering/spark-expert.md`). Inclua o arquivo no contexto da sessão conforme o Claude Code permitir (@ arquivo, drag-and-drop ou comando de referência).

2. **Guia da ferramenta** — Leia **[`.claude/CLAUDE.md`](../.claude/CLAUDE.md)** e o resumo em **[`CLAUDE.md`](../CLAUDE.md)** na raiz (se existir). Roteamento em **`.claude/commands/core/router.md`**.

3. **KB e comandos** — **`.claude/kb/`**, **`.claude/commands/`**, **`.claude/sdd/`** quando existirem.

4. **Edição** — Preferência do time: evoluir **`.cursor/`**; se alguém editar só **`.claude/`**, alinhar com **`.cursor/`** antes do merge quando essa for a referência acordada.

**Exemplo equivalente ao do Cursor:**

```text
@.claude/agents/data-engineering/spark-troubleshooter.md

Meu job PySpark falhou com java.lang.OutOfMemoryError no executor.
O que ajustar primeiro: shuffle, memória ou número de partições?
```

---

## Como usar no GitHub Copilot (VS Code)

1. **Caminhos dos agentes** — Use **`.github/agents/`** quando existir (ex.: `.github/agents/data-engineering/spark-expert.md`). Referencie esse caminho no chat do Copilot (anexar arquivo, `#file` ou arrastar o arquivo para o contexto, conforme a UI).

2. **Instruções de projeto** — Leia **[`.github/copilot-instructions.md`](../.github/copilot-instructions.md)**. Atualize quando mudar visão do produto (em paralelo a `CONTEXT.md` e `.cursor/CURSOR.MD`).

3. **Comandos documentados** — Os fluxos em **`.github/commands/`** podem seguir o mesmo roteiro que **`.cursor/commands/`** (ex.: dev, review, create-pr). Use como **roteiro**: abra o `.md` e peça ao Copilot para seguir o passo a passo.

4. **Slash commands do Cursor** — Atalhos como `/dev` são **específicos do Cursor**. No Copilot, descreva a intenção (“executar o fluxo do arquivo `.github/commands/dev/dev.md` para…”) ou cole o trecho relevante do comando.

**Exemplo equivalente:**

```text
#file:.github/agents/data-engineering/spark-troubleshooter.md

Meu job PySpark falhou com java.lang.OutOfMemoryError no executor.
O que ajustar primeiro: shuffle, memória ou número de partições?
```

(A sintaxe exata de referência a arquivo depende da versão do Copilot Chat; o importante é **incluir o conteúdo do agente** na conversa.)

---

## Agente expert do repositório (opcional)

Se existir um agente **focado no produto deste repositório**, registre o caminho em [`.cursor/commands/core/router.md`](../.cursor/commands/core/router.md) (seção *Agente expert do repositório*) e use-o nas tarefas de domínio:

- **Cursor:** `@.cursor/agents/...`
- **Claude Code:** `.claude/agents/...`
- **Copilot:** `.github/agents/...`

Enquanto não houver arquivo dedicado, combine **roteamento automático** com o router:

- consulte [`.cursor/commands/core/router.md`](../.cursor/commands/core/router.md) ou o comando `/core/agent` no Cursor (veja [`.cursor/commands/core/agent.md`](../.cursor/commands/core/agent.md))

---

## Lista de agentes por pasta

> **Nota:** Vários agentes em `domain/` foram concebidos para cenários **GCP / pipelines genéricos** (Cloud Run, faturas, etc.). Ainda podem servir como referência de arquitetura; para pipelines de dados neste repositório, priorize agentes `data-engineering` e, se aplicável, `spark-expert-on-premises.md` (Spark on-prem + vault + JDBC, alinhado ao `CONTEXT.md`).

### `workflow/` — fluxo SDD (Spec-Driven Development)

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `brainstorm-agent.md` | `brainstorm-agent` | Fase 0: explorar ideias e intenção com requisitos vagos |
| `define-agent.md` | `define-agent` | Fase 1: requisitos estruturados e validação |
| `design-agent.md` | `design-agent` | Fase 2: arquitetura, manifesto de arquivos, matching de agentes |
| `build-agent.md` | `build-agent` | Fase 3: implementação a partir do design |
| `iterate-agent.md` | `iterate-agent` | Atualizar documentos quando requisitos mudam entre fases |
| `ship-agent.md` | `ship-agent` | Fase 4: arquivo, lições aprendidas, doc “SHIPPED” |

### `dev/` — Dev Loop (desenvolvimento agentico)

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `big-data-orchestrator.md` | `big-data-orchestrator` | Entrada on-prem: spark-submit YARN, `config/spark.conf`, delegação entre especialistas Spark |
| `python-project-architect.md` | `python-project-architect` | Classificar projeto dados vs automação, layout OOP, KBs de design |
| `prompt-crafter.md` | `prompt-crafter` | Construir interativamente um `PROMPT.md` executável |
| `dev-loop-executor.md` | `dev-loop-executor` | Executar `PROMPT_*.md` com laços de verificação e prioridades |

**Exemplo (prompt-crafter) — Cursor:**

```text
@.cursor/agents/dev/prompt-crafter.md

Quero um PROMPT.md para implementar validação de parâmetros CLI do projeto.
Faça as perguntas necessárias e depois gere o arquivo completo.
```

**Mesmo agente — Claude Code / Copilot:** troque o prefixo para `.claude/agents/...` ou `.github/agents/...` conforme a ferramenta.

### `data-engineering/` — Spark, Lakeflow, Airflow, arquitetura de lago

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `airflow-dag-builder.md` | `airflow-dag-builder` | Criar/refatorar DAGs TaskFlow 2.11.x (tags, Teams, venv/logs no 314) |
| `big-data-cluster-expert.md` | `big-data-cluster-expert` | Cluster on-prem DATALAKE 311–314, migration-hub, SSH, Airflow, `/DATALAKE/dags` |
| `spark-cluster-migration-expert.md` | `spark-cluster-migration-expert` | Migração operacional Standalone → YARN, portação de jobs, KB migration-hub |
| `spark-expert.md` | `spark-expert` | PySpark / SparkSQL / streaming / produção |
| `spark-specialist.md` | `spark-specialist` | Otimização, arquitetura, troubleshooting amplo |
| `spark-troubleshooter.md` | `spark-troubleshooter` | Erros, falhas, comportamento inesperado |
| `spark-performance-analyzer.md` | `spark-performance-analyzer` | Jobs lentos, gargalos, tuning |
| `spark-streaming-architect.md` | `spark-streaming-architect` | Structured Streaming, Kafka, tempo real |
| `medallion-architect.md` | `medallion-architect` | Camadas Bronze/Silver/Gold, modelagem |
| `lakeflow-architect.md` | `lakeflow-architect` | Databricks Lakeflow / DLT, Medallion |
| `lakeflow-expert.md` | `lakeflow-expert` | DLT operacional, CDC, qualidade |
| `lakeflow-pipeline-builder.md` | `lakeflow-pipeline-builder` | Construir pipelines DLT / DABs |
| `spark-expert-on-premises.md` | `spark-expert-on-premises` | Spark on-prem + vault (ex. OCI) + JDBC; alinhar estrutura ao `CONTEXT.md` e ao código real |

### `code-quality/` — qualidade de código e testes

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `python-developer.md` | `python-developer` | Python para engenharia de dados, clean code |
| `code-reviewer.md` | `code-reviewer` | Revisão segurança, manutenibilidade |
| `dual-reviewer.md` | `dual-reviewer` | Revisão combinada (ferramentas + análise profunda) |
| `code-cleaner.md` | `code-cleaner` | Limpeza, DRY, modernização Python |
| `code-documenter.md` | `code-documenter` | README, APIs, documentação de produção |
| `test-generator.md` | `test-generator` | pytest, testes Spark, fixtures |

### `ai-ml/` — LLMs, prompts, GenAI

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `llm-specialist.md` | `llm-specialist` | Engenharia de prompt, extração estruturada |
| `ai-prompt-specialist.md` | `ai-prompt-specialist` | Otimização de prompts e saída estruturada |
| `genai-architect.md` | `genai-architect` | Sistemas multi-agente, fluxos LLM em produção |
| `crewai-builder.md` | `crewai-builder` | Implementação **CrewAI** (Python): Agent, Task, Crew, tools, padrões da KB `crewai` |
| `ai-data-engineer.md` | *(frontmatter incorreto: `test-generator`)* | O corpo do arquivo replica o **Test Generator**; prefira `test-generator.md` até alinhar o frontmatter |

### `communication/` — comunicação e explicação

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `adaptive-explainer.md` | `adaptive-explainer` | Explicar conceitos para públicos mistos |
| `metting-analyst.md` | `meeting-analyst` | Notas de reunião → documentação acionável |
| `the-planner.md` | `the-planner` | Planejamento estratégico, arquitetura, roadmap e riscos (KB + MCP) |
| `aide-slide-builder.md` | `aide-slide-builder` | Decks HTML Formação AIDE (`aide-slides`) |
| `aide-slide-planner.md` | `aide-slide-planner` | Planejar mapa de slides AIDE |
| `aide-slide-fixer.md` | `aide-slide-fixer` | Corrigir decks AIDE pós-review |
| `aide-slide-reviewer.md` | `aide-slide-reviewer` | Revisão de qualidade decks AIDE |
| `icatu-slide-planner.md` | `icatu-slide-planner` | Slide-map Icatu (tipos `slide--icatu-*`, chunks) antes do HTML — só planeamento |
| `icatu-slide-builder.md` | `icatu-slide-builder` | Decks HTML **marca Icatu** (`icatu-slides` + PDFs `templates/ppts/ICATU/`) |
| `icatu-slide-reviewer.md` | `icatu-slide-reviewer` | Revisão read-only de decks Icatu (paleta + KB + checklist PDFs) |
| `icatu-slide-fixer.md` | `icatu-slide-fixer` | Correções cirúrgicas em HTML Icatu com base no relatório do revisor |

**Fluxo slides Icatu (ordem sugerida):** `icatu-slide-planner` → `icatu-slide-builder` → `icatu-slide-reviewer` → `icatu-slide-fixer` (se necessário) → `icatu-slide-reviewer` de novo. Detalhes, diagrama e exceções: [`.cursor/kb/icatu-slides/fluxo-agentes.md`](../.cursor/kb/icatu-slides/fluxo-agentes.md).

### `exploration/` — repositório e KB

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `agent-architect.md` | `agent-architect` | Criar/refatorar arquivos de agente (`.md`), frontmatter, registro no `router.md` e em `HOW_TO_USE_AGENTS.md` |
| `codebase-explorer.md` | `codebase-explorer` | Onboarding, saúde do repo, resumos executivos |
| `kb-architect.md` | `kb-architect` | Criar/auditar seções de knowledge base |

### `domain/` — domínio (GCP / pipelines de exemplo)

| Arquivo | Nome | Resumo |
|---------|------|--------|
| `pipeline-architect.md` | `pipeline-architect` | Arquitetura event-driven (ex.: GCP serverless) |
| `infra-deployer.md` | `infra-deployer` | Terraform / Terragrunt multi-ambiente |
| `function-developer.md` | `function-developer` | Cloud Run / funções Python |
| `extraction-specialist.md` | `extraction-specialist` | Extração com LLM / visão / Pydantic |
| `dataops-builder.md` | `dataops-builder` | DataOps com orquestração multi-agente |
| `sql-capacity-expert.md` | `sql-capacity-expert` | Especialista do projeto `sql-capacity-prd` usando a KB `sql-capacity` (execução, troubleshooting, SSL e fallback) |
| `key-oci-expert.md` | `key-oci-expert` | `key_oci`, OCI Vault, `.config`, OCIDs e bridge MCP — KB `key-oci` |
| `teams-notifications-expert.md` | `teams-notifications-expert` | Orquestração de alertas **Teams** em pipelines (`pymsteams`, Sentinel, Trilha) — KB `teams-notifications` |

### `_template/`

| Arquivo | Uso |
|---------|-----|
| `agent.template.md` | Modelo para criar **novos** agentes (placeholders `{agent-name}`, etc.) |

---

## Knowledge base — pipelines on-prem (DATALAKE)

Índice canónico: [`.cursor/kb/_index.yaml`](../.cursor/kb/_index.yaml). Entradas principais:

| Domínio | Entrada | Uso |
|---------|---------|-----|
| `migration-hub/` | [`.cursor/kb/migration-hub/index.md`](../.cursor/kb/migration-hub/index.md) | Cluster 311–314, migração, SSH, Airflow 314, spark-submit |
| `airflow/` | [`.cursor/kb/airflow/index.md`](../.cursor/kb/airflow/index.md) | TaskFlow, tags, idempotência, retries/Teams |
| `design-pipelines-patterns/` | [`.cursor/kb/design-pipelines-patterns/index.md`](../.cursor/kb/design-pipelines-patterns/index.md) | Árvore obrigatória de projetos **dados** |
| `design-automation-project-patterns/` | [`.cursor/kb/design-automation-project-patterns/index.md`](../.cursor/kb/design-automation-project-patterns/index.md) | Layout `src/app` + `core` + `integrations` |
| `dev-python-engineering/` | [`.cursor/kb/dev-python-engineering/index.md`](../.cursor/kb/dev-python-engineering/index.md) | Performance e engenharia Python para dados |
| `dev-python-automation/` | [`.cursor/kb/dev-python-automation/index.md`](../.cursor/kb/dev-python-automation/index.md) | Jobs operacionais, SQL Server, PEP 8/SOLID |

---

## Boas práticas rápidas

1. **Um agente por objetivo** — misturar “revisor de código” e “especialista de pipeline” na mesma mensagem pode diluir o foco; use dois passos se precisar dos dois.
2. **Contexto mínimo** — mencione job, ambiente, trecho de log ou caminho de arquivo relevante; o agente acelera com dados concretos.
3. **Alinhar com o projeto** — regras globais em [`.cursorrules`](../.cursorrules) e contexto em [`CONTEXT.md`](../CONTEXT.md); para Copilot, reforce com [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) quando necessário.
4. **Várias árvores** — se o time mantém `.claude/` ou `.github/` além de `.cursor/`, alinhe alterações **manualmente** quando a política exigir o mesmo conteúdo.

---

## Sugestões de melhoria (código / manutenção)

- Corrigir o frontmatter de [`.cursor/agents/ai-ml/ai-data-engineer.md`](../.cursor/agents/ai-ml/ai-data-engineer.md) para refletir um “AI data engineer” real **ou** remover o arquivo se for duplicata acidental de `test-generator`.
- ~~Unificar `the-planner` e `meeting-analyst`~~ — `the-planner` agora usa `name: the-planner` (distinto de `meeting-analyst`).

---

*Última atualização: tabela de agentes baseada na árvore **`.cursor/agents/`**. Ao adicionar novos `.md`, inclua uma linha na tabela correspondente.*
