# Requirements — dl-2026-08-17-get-started

> **Fase:** requirements (Dev Loop L2) · **Agente:** meeting-analyst
> **Pedido original:** "quero organizar todos os arquivos introdutórios da raiz do projeto em um get_started, além de diminuir a poluição visual"
> **Gate:** `continue_l2` (ver `phases/gate.md`)

---

## Executive Summary

| Aspecto | Detalhe |
|---|---|
| **Projeto** | Reorganizar os `.md` introdutórios da raiz de `dev-local-databricks-canonico` em `get_started/`, mantendo a raiz limpa. |
| **Problema** | 13 arquivos `.md` na raiz (11 candidatos a mover + `README.md` + `CLAUDE.md`) poluem visualmente o entrypoint do repositório no GitHub. |
| **Solução** | Mover 10 arquivos para `get_started/` (com índice próprio), atualizar todos os links que os referenciam (raiz, `docs/`, mirrors `.cursor/`/`.claude/`/`.github/`) e os caminhos hardcoded em 3 scripts de tooling. |
| **Prazo crítico** | Nenhum — reorganização documental, reversível via git. |

Confidence: **0.90** (STANDARD) — decisão de escopo raiz vs. `get_started/` é objetiva (papel reconhecido por ferramenta vs. guia humano); descoberta de referências foi feita via grep exaustivo no repositório, com uma lacuna conhecida documentada na seção *Riscos*.

---

## 1. Escopo — o que move e o que fica

### 1.1 Ficam na raiz (não mover)

| Arquivo | Motivo |
|---|---|
| `README.md` | Entrypoint padrão do GitHub (único remote desde a migração de Azure DevOps). |
| `CLAUDE.md` | Lido automaticamente por Claude Code na raiz do projeto. |

### 1.2 Movem para `get_started/` (10 arquivos)

| Arquivo | Observação |
|---|---|
| `START_HERE.md` | Onboarding agentic — primeira leitura sugerida pelo README. |
| `CONTEXT.md` | **Permanece na raiz** — ver nota abaixo; removido desta lista após verificação (contexto rápido é convenção de raiz, referenciado por `.claude/CLAUDE.md`/`.cursor` como "Leia primeiro"). |
| `DEV_LOOP_Guia_Comandos.md` | Guia Dev Loop L2 — também usado como fonte por `scripts/sync-workflow-bundle.sh` e `scripts/validate-workflow-bundle.py` (paths hardcoded, ver FR-007). |
| `SDD_Guia_Comandos.md` | Guia SDD L3 — também listado em `MAIN_FILES` de `scripts/validate-agentic-template.py` (path hardcoded, ver FR-007). |
| `HOW_TO_USE_AGENTS.md` | Índice de agentes e exemplos `@`. |
| `HOW_TO_MAKE_NEW_AGENT.md` | Passo a passo para criar agente novo. |
| `MANUAL_AGENTES.md` | Manual de leitura obrigatória (triângulo de projeto). |
| `AGENTIC_UPGRADE_Guia.md` | Guia de upgrade agentic (audit → apply → validate). |
| `COMO_TORNAR_PROJETO_AGENTIC.md` | Guia — sem referências reais de outros arquivos (órfão), exceto exceção nominal em `scripts/validate-agentic-template.py:177` (checagem por nome de arquivo, não por path — não quebra ao mover). |
| `CRIAR_AMBIENTE_VIRTUAL.md` | Guia — sem referências reais de outros arquivos (órfão confirmado via grep). |
| `copilot-instructions.md` (raiz) | Arquivo-ponte que só aponta para `.github/copilot-instructions.md` (o arquivo real lido pela convenção do GitHub Copilot). Não é lido automaticamente por nenhuma ferramenta nessa localização — seguro mover. **Não confundir com `.github/copilot-instructions.md`, que fica onde está.** |

**Correção importante em relação ao briefing inicial:** `CONTEXT.md` **não deve mover**. Está listado em `.claude/CLAUDE.md` / `.cursor` como parte do "Leia primeiro" ao lado de `README.md`, e o próprio `README.md` (raiz) trata `CONTEXT.md` como par de `START_HERE.md` na raiz. Manter `CONTEXT.md` na raiz preserva a convenção de "contexto rápido sempre visível" descrita nas regras do projeto (`CLAUDE.md`, `.claude/CLAUDE.md`). Portanto: **11 arquivos ficam na raiz** (`README.md`, `CLAUDE.md`, `CONTEXT.md`) e **10 movem**.

### 1.3 Critério aplicado

Fica na raiz **apenas** o que tem papel reconhecido por convenção de ferramenta/onboarding imediato (`README.md`, `CLAUDE.md`, `CONTEXT.md`). Todo guia "como fazer X" / manual / roteiro de comandos vai para `get_started/`.

---

## 2. Requisitos funcionais

### FR-001 — Mover os 10 arquivos para `get_started/`

Mover (git mv) os 10 arquivos listados em 1.2 para `get_started/<mesmo-nome>.md`. Nenhuma alteração de conteúdo nesta etapa além dos links (FR-005).

### FR-002 — Criar índice em `get_started/`

Criar `get_started/README.md` com tabela "arquivo → descrição → quando usar" (padrão já usado em `docs/00-INDEX.md`), cobrindo os 10 arquivos movidos. O `README.md` da raiz deve linkar para `get_started/README.md` como ponto de entrada da pasta.

### FR-003 — Atualizar arquivos da raiz que ficam mas referenciam arquivos movidos

| Arquivo | Referência atual | Ação |
|---|---|---|
| `README.md` (raiz) | `` [`START_HERE.md`](START_HERE.md) `` (linha 7); menção a `` `SDD_Guia_Comandos.md` `` (linha 18, texto/backtick) | Atualizar para `get_started/START_HERE.md` (link) e `get_started/SDD_Guia_Comandos.md` (texto); adicionar linha apontando para `get_started/README.md`. |
| `CONTEXT.md` (raiz) | Menções em backtick (não são links clicáveis, mas texto): `` `START_HERE.md` `` (linha 40), `` `DEV_LOOP_Guia_Comandos.md` `` (linha 48), `` `SDD_Guia_Comandos.md` `` (linha 50) | Atualizar texto para `get_started/START_HERE.md`, `get_started/DEV_LOOP_Guia_Comandos.md`, `get_started/SDD_Guia_Comandos.md`. |

### FR-004 — Atualizar `docs/00-INDEX.md`

Links reais (com `../`) que precisam de prefixo `get_started/` adicional:

- `` [`../START_HERE.md`](../START_HERE.md) `` → `` [`../get_started/START_HERE.md`](../get_started/START_HERE.md) ``
- `` [`../DEV_LOOP_Guia_Comandos.md`](../DEV_LOOP_Guia_Comandos.md) `` → `` [`../get_started/DEV_LOOP_Guia_Comandos.md`](../get_started/DEV_LOOP_Guia_Comandos.md) ``
- `` [`../SDD_Guia_Comandos.md`](../SDD_Guia_Comandos.md) `` → `` [`../get_started/SDD_Guia_Comandos.md`](../get_started/SDD_Guia_Comandos.md) ``
- `` [`../HOW_TO_USE_AGENTS.md`](../HOW_TO_USE_AGENTS.md) `` → `` [`../get_started/HOW_TO_USE_AGENTS.md`](../get_started/HOW_TO_USE_AGENTS.md) ``
- `` [`../AGENTIC_UPGRADE_Guia.md`](../AGENTIC_UPGRADE_Guia.md) `` → `` [`../get_started/AGENTIC_UPGRADE_Guia.md`](../get_started/AGENTIC_UPGRADE_Guia.md) ``

`../README.md` e `../CONTEXT.md` **não mudam** (continuam na raiz).

### FR-005 — Corrigir links de saída dos próprios arquivos movidos

Links **entre os 10 arquivos movidos** (mesmo destino de pasta) permanecem válidos sem alteração (ex.: `DEV_LOOP_Guia_Comandos.md` → `` [`HOW_TO_USE_AGENTS.md`](HOW_TO_USE_AGENTS.md) `` continua correto pois ambos ficam em `get_started/`).

Links de dentro desses arquivos **para fora da raiz antiga** (`.cursor/`, `docs/`, `agentspec/`) precisam ganhar um `../` a mais (a raiz do repo passa a ficar um nível acima):

| Arquivo movido | Links a corrigir (adicionar `../`) |
|---|---|
| `DEV_LOOP_Guia_Comandos.md` | `.cursor/commands/dev/dev.md`; `.cursor/agents/communication/metting-analyst.md` (2x); `.cursor/agents/communication/the-planner.md` (2x); `.cursor/commands/workflow/design.md`; `.cursor/agents/dev/prompt-crafter.md`; `.cursor/agents/dev/dev-loop-executor.md` (2x); `.cursor/commands/core/router.md`; `.cursor/commands/workflow/build.md` |
| `AGENTIC_UPGRADE_Guia.md` | `agentspec/INSTALL_UPGRADE.md` (2x); `docs/DATABRICKS_TEAMS_PIPELINES.md`; `.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md`; `.cursor/kb/databricks/patterns/pipeline-failure-teams-no-retry.md`; `.cursor/commands/intake.md`; `docs/00-INDEX.md`; `agentspec/INSTALL_AGENTSPEC.md` |
| `HOW_TO_USE_AGENTS.md` | `.cursor/commands/core/router.md` (2x); `.cursor/commands/core/agent.md` (2x); `.cursor/commands/intake.md`; `.claude/CLAUDE.md`; `CLAUDE.md` (raiz, agora `../CLAUDE.md`); `.github/copilot-instructions.md` (2x); `.cursor/kb/icatu-slides/fluxo-agentes.md`; `.cursor/kb/migration-hub/index.md`; `.cursor/kb/airflow/index.md`; `.cursor/kb/design-pipelines-patterns/index.md`; `.cursor/kb/design-automation-project-patterns/index.md`; `.cursor/kb/dev-python-engineering/index.md`; `.cursor/kb/dev-python-automation/index.md`; `.cursorrules` (raiz, agora `../.cursorrules`); `CONTEXT.md` (raiz, agora `../CONTEXT.md`); `.cursor/agents/ai-ml/ai-data-engineer.md` |
| `HOW_TO_MAKE_NEW_AGENT.md` | `.cursor/agents/data-engineering/spark-expert-on-premises.md` (2x); `docs/GUIA_CRIACAO_AGENTE_PROJETO.md`; `.cursor/agents/_template/agent.template.md`; `.cursor/commands/core/router.md` |

Bare-links entre movidos (`MANUAL_AGENTES.md`, `HOW_TO_USE_AGENTS.md`, `START_HERE.md`, `SDD_Guia_Comandos.md` citados uns nos outros) **não precisam de `../`** — permanecem corretos.

Menções em texto/backtick (não são hyperlinks Markdown, ex. tabelas descritivas em `MANUAL_AGENTES.md` linhas 17/19, `HOW_TO_USE_AGENTS.md` linhas 124/297 apontando para `.github/copilot-instructions.md`) **não quebram tecnicamente** (não são resolvidas por path), mas devem ser revisadas por precisão textual — prioridade menor, best-effort no craft.

### FR-006 — Atualizar mirrors `.cursor/` / `.claude/` / `.github/` (comandos e agentes)

Fonte canônica é `.cursor/`; qualquer correção deve ser replicada nos 3 espelhos para manter coerência (regra do projeto em `CLAUDE.md` raiz / `.claude/CLAUDE.md`). Links reais com `../../../` (relativos de arquivos a 3 níveis de profundidade) que apontam para docs agora movidos:

| Link atual (relativo) | Presente em (mesmo caminho relativo nos 3 mirrors) | Novo destino |
|---|---|---|
| `../../../DEV_LOOP_Guia_Comandos.md` | `agents/workflow-dev-loop/devloop-phase.md`; `commands/workflow-dev-loop/workflow-dev-loop.md` | `../../../get_started/DEV_LOOP_Guia_Comandos.md` |
| `../../../HOW_TO_MAKE_NEW_AGENT.md` | `agents/exploration/agent-architect.md` | `../../../get_started/HOW_TO_MAKE_NEW_AGENT.md` |
| `../../../HOW_TO_USE_AGENTS.md` | `agents/exploration/agent-architect.md` (2x); `commands/workflow/create-pr.md` | `../../../get_started/HOW_TO_USE_AGENTS.md` |
| `../../../MANUAL_AGENTES.md` | `agents/exploration/agent-architect.md` | `../../../get_started/MANUAL_AGENTES.md` |

Aplicar em `.cursor/`, `.claude/` e `.github/` (6 arquivos por padrão × 3 árvores = ~12 arquivos; usar os caminhos análogos, ex. `.claude/agents/workflow-dev-loop/devloop-phase.md`, `.cursor/agents/workflow-dev-loop/devloop-phase.md`, `.github/agents/workflow-dev-loop/devloop-phase.md`).

Além disso, `.cursor/dev/_index.md` tem um link de profundidade diferente: `` [`DEV_LOOP_Guia_Comandos.md`](../../DEV_LOOP_Guia_Comandos.md) `` → `` [`DEV_LOOP_Guia_Comandos.md`](../../get_started/DEV_LOOP_Guia_Comandos.md) ``. **Nota:** essa seção ("Workflow estruturado") existe hoje só em `.cursor/dev/_index.md` e está ausente em `.claude/dev/_index.md` / `.github/dev/_index.md` — drift pré-existente, fora de escopo desta RUN (não introduzir nem corrigir a divergência de conteúdo, só o path se for tocar o arquivo).

### FR-007 — Atualizar scripts de tooling com paths hardcoded para a raiz

Achado crítico de descoberta: 3 scripts têm paths absolutos/relativos hardcoded para os arquivos que vão mover. Sem esta correção, os scripts de validação/sync quebram silenciosamente ou com erro.

| Script | Linha(s) | Path atual | Novo path |
|---|---|---|---|
| `scripts/sync-workflow-bundle.sh` | 14 | `GUIDE_ROOT="${REPO_ROOT}/DEV_LOOP_Guia_Comandos.md"` | `GUIDE_ROOT="${REPO_ROOT}/get_started/DEV_LOOP_Guia_Comandos.md"` |
| `scripts/validate-workflow-bundle.py` | 80 | `guide_root = REPO_ROOT / "DEV_LOOP_Guia_Comandos.md"` | `guide_root = REPO_ROOT / "get_started" / "DEV_LOOP_Guia_Comandos.md"` |
| `scripts/validate-agentic-template.py` | 33-45 (`MAIN_FILES`) | `'START_HERE.md'`, `'SDD_Guia_Comandos.md'` | `'get_started/START_HERE.md'`, `'get_started/SDD_Guia_Comandos.md'` |

`scripts/validate-agentic-template.py:177` (exceção nominal para `COMO_TORNAR_PROJETO_AGENTIC.md` em `validate_old_template_names`) **não precisa mudar** — a checagem é por `path.name`, não por path completo, e continua funcionando com o arquivo em `get_started/`.

### FR-008 — Ressincronizar bundle do instalador após mover

Após FR-001 a FR-007, rodar `scripts/sync-workflow-bundle.sh` (ou `--dry-run` primeiro) para regenerar `install_dev_loop/assets/DEV_LOOP_Guia_Comandos.md` e `install_dev_loop/assets/dev/_index.md` a partir da nova localização, e então `python3 scripts/validate-workflow-bundle.py` para confirmar paridade. Isso é necessário porque esses assets são cópias geradas, não devem ser editadas manualmente.

---

## 3. Fora de escopo (explícito)

| Item | Motivo |
|---|---|
| `.claude/worktrees/age-of-empires-project-access-000743/**` | É um git worktree separado (cópia paralela de working tree para outra tarefa/branch); não faz parte da árvore de trabalho principal desta RUN. |
| `install_dev_loop/**` (exceto `assets/DEV_LOOP_Guia_Comandos.md` e `assets/dev/_index.md`, tratados via FR-008 regenerando, não editando à mão) | Bundle do instalador para **outros** projetos; menções a `DEV_LOOP_Guia_Comandos.md`/`HOW_TO_USE_AGENTS.md` ali são conteúdo textual genérico do pacote instalável, não links para os arquivos deste repositório. |
| `agentspec/**` | Mesma lógica — scripts/prompts de instalação para projetos novos, referências textuais genéricas. |
| `templates/*-generico.md` (`CURSOR.MD-generico.md`, `CONTEXT.md-generico.md`, `.cursorrules-generico.md`) | Templates para bootstrap de outros projetos; mencionam `HOW_TO_USE_AGENTS.md`/`MANUAL_AGENTES.md` como convenção de nome, não como link resolvido para este repo. |
| Conteúdo dos 10 arquivos movidos (além dos links) | Fora do pedido — apenas mover e corrigir referências, não reescrever conteúdo. |
| Drift de conteúdo entre `.cursor/dev/_index.md` e `.claude/dev/_index.md`/`.github/dev/_index.md` | Pré-existente, não introduzido por esta RUN; registrar como observação, não corrigir aqui. |

---

## 4. Critérios de aceite

1. Raiz do repositório contém apenas `README.md`, `CLAUDE.md`, `CONTEXT.md` como `.md` "soltos" de topo (fora pastas de config/código) — poluição visual reduzida de 13 para 3 arquivos `.md`.
2. `get_started/` contém os 10 arquivos movidos + `get_started/README.md` (índice).
3. Nenhum link Markdown quebrado: grep pós-execução por `AGENTIC_UPGRADE_Guia\.md|COMO_TORNAR_PROJETO_AGENTIC\.md|CRIAR_AMBIENTE_VIRTUAL\.md|DEV_LOOP_Guia_Comandos\.md|HOW_TO_MAKE_NEW_AGENT\.md|HOW_TO_USE_AGENTS\.md|MANUAL_AGENTES\.md|SDD_Guia_Comandos\.md|START_HERE\.md` fora de `get_started/`, `docs/`, `.cursor/`, `.claude/`, `.github/`, `README.md`, `CONTEXT.md` não deve mais aparecer sem o prefixo `get_started/` correspondente (excluindo diretórios fora de escopo da seção 3).
4. `python3 scripts/validate-agent-router.py` e `python3 scripts/validate-workflow-bundle.py` passam sem erro após a reorganização.
5. `.cursor/`, `.claude/`, `.github/` permanecem coerentes entre si (mesma correção replicada nos 3).

---

## 5. Riscos e pendências para a fase `design`

| # | Risco/Pendência | Impacto | Mitigação sugerida |
|---|---|---|---|
| R1 | Volume alto de arquivos tocados (~10 movidos + ~15-20 arquivos com links a corrigir, em 3 árvores mirror + 3 scripts) para uma RUN L2 | Médio — risco de esquecer algum link | Design deve quebrar em tarefas granulares por FR (001-008); craft deve incluir verificação objetiva por grep após cada bloco |
| R2 | Descoberta de links foi feita por grep textual (`\]\([^)]*\.md\)`); pode haver referências dinâmicas (ex. geradas por script, ou em `.mdc`/`.yaml` fora do padrão grepado) não capturadas | Baixo-médio | Design deve incluir um passo final de grep amplo (nome de cada arquivo movido, sem filtro de extensão) como verificação de saída, cobrindo toda a árvore exceto os diretórios da seção 3 |
| R3 | `.cursor/dev/_index.md` tem conteúdo (seção "Workflow estruturado") ausente em `.claude/`/`.github/` — drift pré-existente | Baixo | Não corrigir nesta RUN; apenas ajustar o path se o craft decidir tocar o arquivo |
| R4 | Scripts de tooling (`sync-workflow-bundle.sh`, `validate-workflow-bundle.py`, `validate-agentic-template.py`) têm paths hardcoded — sem FR-007/FR-008 a reorganização quebra validação silenciosamente | Alto | FR-007 e FR-008 são obrigatórios, não opcionais, e devem ser tarefas 🔴 (críticas) no craft |

---

## 6. Fontes / evidência de descoberta

- Listagem de `.md` na raiz: `ls *.md` (13 arquivos).
- Grep de referências com path real (`\]\([^)]*NOME\.md\)`) em toda a árvore, excluindo `.claude/worktrees/`, `install_dev_loop/`, `agentspec/`, `templates/`.
- Leitura de `README.md`, `CONTEXT.md`, `START_HERE.md`, `MANUAL_AGENTES.md`, `HOW_TO_USE_AGENTS.md`, `docs/00-INDEX.md`, `DEV_LOOP_Guia_Comandos.md`, `AGENTIC_UPGRADE_Guia.md` (raiz).
- Leitura de `scripts/sync-workflow-bundle.sh`, `scripts/validate-workflow-bundle.py`, `scripts/validate-agentic-template.py`, `scripts/validate-agent-router.py`, `scripts/bootstrap-agentic-project.py`.
- Comparação `.cursor/dev/_index.md` vs `.claude/dev/_index.md` vs `.github/dev/_index.md` (diff).
