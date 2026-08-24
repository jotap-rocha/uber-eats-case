# Agent Spec Installer — instalação greenfield

Instala em um **projeto vazio** (ou quase vazio) toda a estrutura de desenvolvimento agentic deste template:

- **SDD** (comandos `/brainstorm`, `/define`, `/design`, `/build`, `/ship`, `/iterate`)
- **Dev Loop** (Nível 2: `/workflow-dev-loop`, `/devloop-*`, PROMPTs em `.cursor/dev/`)
- **Workflows de revisão** (`/workflow-makeapp-review`, `/workflow-data-pipeline-review`)
- **Agentes e KB** (`.cursor/agents/`, `.cursor/kb/`)
- **Roteador** (`AGENT_ROUTER.yaml`, `/router`)
- **Triângulo de contexto**: `CONTEXT.md` + `.cursorrules` + `docs/00-INDEX.md`

Diferente de `scripts/bootstrap-agentic-project.py` (que copia quase o repositório template inteiro), o instalador em `agentspec/` faz uma **cópia curada** — sem `install_dev_loop/`, `agentspec/`, runs de review/dev-loop reais, nem artefatos de CI do template.

---

## Pré-requisitos

- Python 3.9+
- `PyYAML` recomendado (`pip install pyyaml`) para atualizar o roteador automaticamente
- Este repositório como **fonte** (`--source`), ou o caminho onde o template está clonado

---

## Uso rápido

```bash
# Criar pasta do novo projeto
mkdir -p /path/to/meu-pipeline && cd /path/to/meu-pipeline
git init   # opcional

# Instalar a partir do template (ajuste --source se necessário)
python3 agentspec/install_agentspec.py \
  --target /path/to/meu-pipeline \
  --source /path/to/template-agentic-fonte \
  --project-name "Meu Pipeline" \
  --project-slug meu-pipeline \
  --description "Ingestão medallion em PySpark no Databricks" \
  --stack "python,pyspark,databricks" \
  --install-command "pip install -r requirements.txt"
```

### Simular (dry-run)

```bash
python3 agentspec/install_agentspec.py --dry-run --target /tmp/preview \
  --source . --project-name "Preview" --project-slug preview
```

### Apenas Cursor (sem espelhos)

```bash
python3 agentspec/install_agentspec.py --target /path/to/projeto --ecosystem cursor --force
```

Por padrão (`--ecosystem all`), o instalador cria `.cursor/` (canônico), `.claude/` e `.github/` com paths adaptados.

---

## O que é copiado

| Destino | Conteúdo |
|---------|----------|
| `.cursor/` | Agentes, KB, comandos SDD/Dev Loop/workflows, contratos SDD, regras, `dev/templates` |
| Raiz | `CONTEXT.md`, `.cursorrules`, `README.md`, `START_HERE.md`, guias de agentes/SDD/Dev Loop |
| `docs/` | `00-INDEX.md`, `inventario-ambiente.md.example` |
| `scripts/` | `validate-agent-router.py`, `validate-agentic-template.py`, `enable-git-hooks.sh` |
| `.cursor/dev/tasks/` | `PROMPT_INIT_AGENTSPEC.md`, `PROMPT_INIT_DEV_LOOP.md`, `PROMPT_HELLO_WORLD.md` |
| `.cursor/agents/domain/` | `{slug}-expert.md` gerado a partir de `templates/agent-expert.md.j2` |

### O que **não** é copiado

- Pastas `install_dev_loop/`, `agentspec/`, `templates/` (só usadas na geração)
- Runs reais em `sdd/reviews/`, `sdd/data-pipeline-reviews/`, `sdd/dev-loop-runs/` (apenas `_template/`)
- Conteúdo de `dev/progress/`, `dev/logs/` (apenas `.gitkeep`)
- `.cursor/mcp.json` (configuração local; copie de `mcp.example.json` se precisar)
- `.git/`, caches, `node_modules/`

---

## Parâmetros CLI

| Flag | Descrição |
|------|-----------|
| `--target` | Diretório do projeto destino (default: `.`) |
| `--source` | Raiz do template (default: pai de `agentspec/`) |
| `--ecosystem` | `all` (default — três ecossistemas), ou `cursor`, `claude`, `github` |
| `--project-name` | Nome legível do projeto |
| `--project-slug` | Slug kebab-case (expert + hints do router) |
| `--description` | Descrição curta |
| `--stack` | Stack para documentação |
| `--project-context` | Contexto extra do agente expert |
| `--agent-scope` | Escopo em Markdown do expert |
| `--force` | Sobrescrever arquivos existentes |
| `--dry-run` | Simular sem gravar |
| `--skip-validation` | Não rodar scripts de validação ao final |

---

## Após a instalação

1. Abra o projeto no **Cursor** e leia `START_HERE.md`.
2. No assistente, execute:
   ```
   /dev tasks/PROMPT_INIT_AGENTSPEC.md
   ```
3. Valide:
   ```bash
   python3 scripts/validate-agent-router.py
   python3 scripts/validate-agentic-template.py --root . --mode project
   ```
4. Inicie um **Dev Loop** (Nível 2):
   ```
   /workflow-dev-loop
   /devloop-init minha-feature
   ```
5. Para feature com rastreabilidade formal (Nível 3):
   ```
   /brainstorm
   ```
   Consulte `SDD_Guia_Comandos.md`.

---

## Comparação com outros instaladores

| Ferramenta | Quando usar |
|------------|-------------|
| **`agentspec/install_agentspec.py`** | Projeto **greenfield** — só estrutura agentic, sem lixo do template |
| **`agentspec/upgrade_agentic.py`** | Projeto **já agentic** — merge preservando destino. Guia: [`AGENTIC_UPGRADE_Guia.md`](../AGENTIC_UPGRADE_Guia.md) · técnico: [`INSTALL_UPGRADE.md`](INSTALL_UPGRADE.md) |
| `install_dev_loop/install_dev_loop.py` | Projeto que **já tem** `.cursor/` e só precisa do workflow Dev Loop |
| `scripts/bootstrap-agentic-project.py` | Clonar **quase o repo inteiro** como novo projeto template |

---

## Portabilidade

O instalador vive em `agentspec/` mas **lê a fonte** do repositório template via `--source`. Para instalar em outra máquina:

1. Clone este repositório template, ou
2. Aponte `--source` para o caminho do clone.

Não é necessário copiar só a pasta `agentspec/` isolada — ela depende de `.cursor/`, `templates/` e guias na raiz do template.

---

## Troubleshooting

- **`Fonte .cursor/ ausente`**: confira `--source` apontando para a raiz do template.
- **`PyYAML` ausente**: o roteador não será atualizado automaticamente; instale `pyyaml` e reexecute com `--force`.
- **Arquivos `skip-existing`**: use `--force` para sobrescrever.
- **Placeholders `{{PROJECT_*}}`**: reexecute com `--force` ou edite manualmente; a validação `validate-agentic-template.py` detecta resíduos.
