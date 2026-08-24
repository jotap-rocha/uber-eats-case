# Como Instalar o Dev Loop

> Agentic Development (Level 2) — instalação em qualquer projeto em 2 passos.

---

## O que é instalado

Dois arquivos na raiz do projeto de origem:

| Arquivo | Propósito |
|---------|-----------|
| `install_dev_loop.py` | Script Python que cria toda a estrutura de pastas e arquivos |
| `PROMPT_INIT_DEV_LOOP.md` | PROMPT que o Claude executa para adaptar ao projeto destino |

---

## Passo 1 — Rodar o instalador

Copie `install_dev_loop.py` para qualquer projeto e execute:

```bash
# Instalar no projeto atual
python3 install_dev_loop.py

# Instalar em outro projeto
python3 install_dev_loop.py --target /path/to/meu-outro-projeto

# Instalar em uma árvore específica
python3 install_dev_loop.py --ecosystem cursor

# Instalar nas três árvores suportadas (.claude, .cursor e .github)
python3 install_dev_loop.py --ecosystem all

# Preview antes de instalar (não escreve nada)
python3 install_dev_loop.py --dry-run --target /path/to/projeto

# Forçar sobrescrever arquivos existentes
python3 install_dev_loop.py --force --target /path/to/projeto
```

Por padrão, o script cria a árvore `.claude/`. Use `--ecosystem cursor`, `--ecosystem github` ou `--ecosystem all` para instalar em outras árvores.

O script cria **14 arquivos por ecossistema** automaticamente:

```text
.claude/
├── agents/dev/
│   ├── prompt-crafter.md       # Agente que cria PROMPT.md via perguntas
│   └── dev-loop-executor.md    # Agente que executa o loop com verificação
├── commands/dev/
│   └── dev.md                  # Slash command /dev
└── dev/
    ├── readme.md
    ├── _index.md                # Documentação completa
    ├── tasks/
    │   ├── PROMPT_INIT_DEV_LOOP.md
    │   └── .gitkeep             # Seus PROMPT_*.md ficam aqui
    ├── progress/.gitkeep        # Memory bridge (auto-gerenciado)
    ├── logs/.gitkeep            # Logs de execução
    ├── examples/.gitkeep
    └── templates/
        ├── PROMPT_TEMPLATE.md
        ├── PROGRESS_TEMPLATE.md
        ├── PROMPT_EXAMPLE_FEATURE.md
        └── PROMPT_EXAMPLE_KB.md
```

**Comportamento seguro por padrão:** arquivos existentes são ignorados (use `--force` para sobrescrever).

---

## Passo 2 — Customizar ao projeto

Após o install, execute o PROMPT de bootstrap na ferramenta correspondente:

```bash
# Default (.claude)
/dev tasks/PROMPT_INIT_DEV_LOOP.md
```

Se você instalou com `--ecosystem all`, execute o mesmo PROMPT uma vez por árvore quando quiser manter `.claude/`, `.cursor/` e `.github/` alinhadas manualmente.

O assistente vai automaticamente:

1. Explorar o projeto (tech stack, test framework, linter)
2. Adaptar os templates com os comandos reais do projeto
3. Criar um primeiro PROMPT de exemplo específico ao projeto
4. Adicionar ou atualizar uma seção Dev Loop no contexto da árvore (`CLAUDE.md`, `.cursor/CURSOR.md`, `.github/CURSOR.md`)
5. Manter as árvores instaladas alinhadas quando o projeto usa mais de uma

---

## Usando o Dev Loop

Após a instalação e customização, siga o fluxo passo a passo em **[`DEV_LOOP_Guia_Comandos.md`](../DEV_LOOP_Guia_Comandos.md)** (na raiz do projeto destino, ou copie o guia junto com o instalador).

Resumo:

```text
1. @meeting-analyst  →  *requirements*.md
2. @the-planner      →  *design*.md
3. /dev com @design + @requirements  →  PROMPT em dev/tasks/
4. /dev tasks/PROMPT_*.md
```

Comandos úteis:

```bash
# Craft a partir do design (anexe @requirements e @design no chat)
/dev "Gere PROMPT executável conforme o design anexado"

# Executar PROMPT
/dev tasks/PROMPT_MINHA_FEATURE.md

# Retomar sessão interrompida
/dev tasks/PROMPT_MINHA_FEATURE.md --resume

# Validar sem executar
/dev tasks/PROMPT_MINHA_FEATURE.md --dry-run
```

**Quando usar Dev Loop vs SDD:** tabela em `DEV_LOOP_Guia_Comandos.md` (L2 = `/dev`; L3 = `/brainstorm`, `/design`, `/build`).

## Workflow Dev Loop (instalado com o pacote)

O instalador também copia:

| Artefato | Destino no projeto |
|----------|-------------------|
| Comandos e agentes `devloop-*` | `.{claude,cursor,github}/commands|agents/workflow-dev-loop/` |
| Contrato e templates de RUN | `.{ecosystem}/sdd/architecture/WORKFLOW_DEV_LOOP_CONTRACTS.yaml`, `sdd/dev-loop-runs/` |
| Regra de handoff | `.{ecosystem}/rules/workflow-dev-loop-handoff.mdc` |
| Fragmento do roteador | `.{ecosystem}/sdd/architecture/AGENT_ROUTER_DEVLOOP_FRAGMENT.yaml` |
| Instruções de merge | `.{ecosystem}/sdd/architecture/AGENT_ROUTER_DEVLOOP_MERGE.md` |
| Guia humano | `DEV_LOOP_Guia_Comandos.md` (raiz do projeto) |
| `_index.md` do Dev Loop | Sincronizado com o template via `install_dev_loop/assets/dev/_index.md` |

Fluxo recomendado:

```text
/workflow-dev-loop
/devloop-init <RUN_ID>
/devloop-phase <RUN_ID> gate
# … requirements → design → craft → prompt_review
/devloop-execute <RUN_ID>
/devloop-phase <RUN_ID> reflect
```

Após instalar, execute `/dev tasks/PROMPT_INIT_DEV_LOOP.md` para adaptar o projeto (inclui verificação do workflow e RUN de exemplo).

### Manter paridade no repositório template

Após editar `.cursor/commands/workflow-dev-loop/`, agentes, CONTRACTS ou `dev/_index.md`:

```bash
./scripts/sync-workflow-bundle.sh
```

O script copia para `install_dev_loop/workflow_bundle/`, gera `assets/dev/_index.md` (`.cursor` → `__TREE__`), atualiza o guia em `assets/` e roda `validate-workflow-bundle.py`.

```bash
./scripts/sync-workflow-bundle.sh --dry-run   # pré-visualizar
python3 scripts/validate-workflow-bundle.py # só validar, sem copiar
```

---

## Referências

- Documentação completa: `.claude/dev/_index.md`
- Template de PROMPT: `.claude/dev/templates/PROMPT_TEMPLATE.md`
- Agente crafter: `.claude/agents/dev/prompt-crafter.md`
- Agente executor: `.claude/agents/dev/dev-loop-executor.md`
