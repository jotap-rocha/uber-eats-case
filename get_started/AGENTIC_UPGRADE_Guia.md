# Guia — Atualizar projeto agentic (upgrade com merge)

> **Quando usar:** o projeto **já tem** `.cursor/` (ou espelhos) e você quer trazer novidades de um **template agentic fonte** **sem apagar** expert, `CONTEXT.md`, PROMPTs locais nem RUNs de workflow.

**Script:** [`agentspec/upgrade_agentic.py`](../agentspec/upgrade_agentic.py)  
**Detalhes técnicos:** [`agentspec/INSTALL_UPGRADE.md`](../agentspec/INSTALL_UPGRADE.md)

---

## Pré-requisitos

- Python 3.9+
- `PyYAML` recomendado (`pip install pyyaml`) — merge automático de `AGENT_ROUTER.yaml` e `kb/_index.yaml`
- Caminho do **template** (este repositório) e do **projeto destino** (seu pipeline já agentic)

Substitua `/path/to/seu-projeto-agentic` pelo caminho real do seu projeto.

---

## Procedimento em 3 passos (canônico)

### 1) Auditar (não grava)

Simula o upgrade e gera relatório em `.agentic-upgrade/UPGRADE_REPORT.md` no projeto destino.

```bash
python3 agentspec/upgrade_agentic.py \
  --target /path/to/seu-projeto-agentic \
  --source /path/to/template-agentic-fonte \
  --dry-run
```

**O que verificar no relatório:**

| Métrica | Significado |
|---------|-------------|
| `added` | Arquivos que serão criados |
| `identical` | Já em dia com o template |
| `preserved` | Protegidos pela política (expert, CONTEXT, PROMPTs locais) |
| `conflict` | Diferem do template — **destino mantido**; revisão manual depois |

### 2) Aplicar

Grava novidades e faz merge de YAML; conflitos ficam em `.agentic-upgrade/incoming/` vs `preserved/`.

```bash
python3 agentspec/upgrade_agentic.py \
  --target /path/to/seu-projeto-agentic \
  --source /path/to/template-agentic-fonte \
  --apply
```

**Opcional — espelhar `.claude/` e `.github/`** (após merge em `.cursor/`):

```bash
python3 agentspec/upgrade_agentic.py \
  --target /path/to/seu-projeto-agentic \
  --source /path/to/template-agentic-fonte \
  --ecosystem all \
  --apply
```

### 3) Validar

```bash
cd /path/to/seu-projeto-agentic
python3 scripts/validate-agent-router.py
```

Se `scripts/validate-agentic-template.py` existir no destino:

```bash
python3 scripts/validate-agentic-template.py --root . --mode project
```

### Pipelines Databricks com Teams (após upgrade)

Se o projeto usar **Asset Bundle** + alertas Teams, consulte (macro, qualquer pipeline):

| Recurso | Caminho no template |
|---------|---------------------|
| Guia humano | [`docs/DATABRICKS_TEAMS_PIPELINES.md`](../docs/DATABRICKS_TEAMS_PIPELINES.md) |
| KB agentes | [`.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md`](../.cursor/kb/teams-notifications/patterns/databricks-ambientes-e-smoke-test.md) |
| Job sem retry | [`.cursor/kb/databricks/patterns/pipeline-failure-teams-no-retry.md`](../.cursor/kb/databricks/patterns/pipeline-failure-teams-no-retry.md) |

Referência de implementação: repositório Varonis (`docs/guia-teams-databricks.md`).

---

## Passo 4 — Conflitos e merge fino (assistente)

Se o relatório listar `conflict` > 0:

```text
/dev tasks/PROMPT_UPGRADE_AGENTIC.md
```

Compare `.agentic-upgrade/incoming/` (template) com `preserved/` (seu projeto) e funda por seção (`##`), sem substituir arquivos inteiros.

---

## Usar `/intake` antes, durante ou depois do upgrade

O comando **`/intake`** não executa o script; ele **triagem agentes** e responde com síntese. Use para decidir *o que* atualizar antes de rodar o CLI, ou para interpretar o relatório.

### Exemplos de pergunta

```text
/intake Meu projeto já tem .cursor/ antigo. O que o template agentic fonte tem a mais em workflows e agentes?

/intake Li o UPGRADE_REPORT.md após dry-run: quais conflitos devo resolver manualmente primeiro?

/intake Depois do upgrade_agentic --apply, preciso instalar só Dev Loop ou já está no merge?
```

### Fluxo recomendado com `/intake`

```text
1. /intake  →  entender lacunas (workflows, KB, comandos novos)
2. dry-run  →  UPGRADE_REPORT.md com números
3. --apply  →  trazer arquivos novos + merge YAML
4. /intake  →  priorizar conflitos .md se houver
5. PROMPT_UPGRADE_AGENTIC  →  merge manual
6. validate-agent-router.py
```

Documentação do comando: [`.cursor/commands/intake.md`](../.cursor/commands/intake.md)

---

## O que nunca é sobrescrito

| Path | Motivo |
|------|--------|
| `agents/domain/*-expert.md` | Especialista do seu domínio |
| `CONTEXT.md`, `README.md`, `.cursorrules` | Triângulo de contexto local |
| `dev/tasks/PROMPT_*.md` (exceto bootstrap) | PROMPTs da sua equipe |
| RUNs em `sdd/reviews/`, `sdd/dev-loop-runs/`, etc. | Histórico de execução |

Com `--force`, outros conflitos podem ser sobrescritos; a lista acima **continua protegida**.

---

## Comparar com outros instaladores

| Ferramenta | Cenário |
|------------|---------|
| **`upgrade_agentic.py`** | Projeto **já agentic** — merge preservando destino |
| [`install_agentspec.py`](../agentspec/install_agentspec.py) | Projeto **vazio** (greenfield) |
| [`install_dev_loop.py`](install_dev_loop/install_dev_loop.py) | Só pacote Dev Loop |
| [`bootstrap-agentic-project.py`](scripts/bootstrap-agentic-project.py) | Cópia quase integral do template |

---

## Troubleshooting

| Sintoma | Ação |
|---------|------|
| `Fonte .cursor/ ausente` | Confira `--source` apontando para a raiz do template |
| Muitos `conflict` | Normal em projetos antigos; use `PROMPT_UPGRADE_AGENTIC.md` |
| `validate-agent-router` falha | Revise merge de `AGENT_ROUTER.yaml`; rode sem `--no-merge-router` |
| Quero sobrescrever tudo | `--force` (expert e CONTEXT ainda preservados) |

---

## Referências

- Política de merge e flags: [`agentspec/INSTALL_UPGRADE.md`](../agentspec/INSTALL_UPGRADE.md)
- Índice da documentação: [`docs/00-INDEX.md`](../docs/00-INDEX.md)
- Instalação greenfield: [`agentspec/INSTALL_AGENTSPEC.md`](../agentspec/INSTALL_AGENTSPEC.md)
