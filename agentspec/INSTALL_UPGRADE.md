# Install / Upgrade agentic — referência técnica

> **Guia passo a passo (usuário):** [`../AGENTIC_UPGRADE_Guia.md`](../AGENTIC_UPGRADE_Guia.md)  
> **Script:** [`upgrade_agentic.py`](upgrade_agentic.py)

---

## Procedimento canônico (copiar e colar)

Substitua `/path/to/seu-projeto-agentic` pelo projeto destino.

### 1) Auditar (não grava)

```bash
python3 agentspec/upgrade_agentic.py \
  --target /path/to/seu-projeto-agentic \
  --source /path/to/template-agentic-fonte \
  --dry-run
```

Gera: `<destino>/.agentic-upgrade/UPGRADE_REPORT.md`

### 2) Aplicar

```bash
python3 agentspec/upgrade_agentic.py \
  --target /path/to/seu-projeto-agentic \
  --source /path/to/template-agentic-fonte \
  --apply
```

### 3) Validar

```bash
cd /path/to/seu-projeto-agentic
python3 scripts/validate-agent-router.py
```

### 4) Conflitos (opcional)

No Cursor, no **projeto destino**:

```text
/dev tasks/PROMPT_UPGRADE_AGENTIC.md
```

---

## Integração com `/intake`

| Momento | Comando `/intake` sugerido |
|---------|---------------------------|
| Antes do dry-run | `/intake O que o template tem a mais que meu .cursor/ em workflows, KB e comandos?` |
| Após dry-run | `/intake Com base em .agentic-upgrade/UPGRADE_REPORT.md, o que priorizar no merge manual?` |
| Após `--apply` | `/intake Valide se faltam workflows dev-loop ou pipeline-review no meu projeto` |

O `/intake` **não substitui** `upgrade_agentic.py`; use o script para alterar arquivos e o intake para **decidir e interpretar**.

Ver: [`.cursor/commands/intake.md`](../.cursor/commands/intake.md)

---

## Política de merge

| Situação | Comportamento |
|----------|----------------|
| Arquivo só na fonte | Copia |
| Idêntico | Ignora |
| Diferente | Mantém destino; staging em `.agentic-upgrade/` |
| `AGENT_ROUTER.yaml` | Merge por `id` / hint (destino vence duplicata) |
| `kb/_index.yaml` | Merge de `domains` |
| Expert, CONTEXT, PROMPTs locais, RUNs | Nunca sobrescreve |

---

## Flags CLI

| Flag | Descrição |
|------|-----------|
| `--target` | Projeto destino (obrigatório) |
| `--source` | Template (default: pai de `agentspec/`) |
| `--apply` | Gravar; omitir = dry-run |
| `--dry-run` | Explícito; equivalente a não usar `--apply` |
| `--force` | Sobrescrever conflitos (exceto preserve) |
| `--ecosystem` | `cursor` (default), `claude`, `github`, `all` |
| `--no-merge-router` | Não mergear roteador |
| `--no-merge-kb-index` | Não mergear `kb/_index.yaml` |
| `--report-json` | Exportar JSON do relatório |
| `--skip-validation` | Não rodar `validate-agent-router` ao final |

---

## Comparar instaladores

| Ferramenta | Cenário |
|------------|---------|
| **`upgrade_agentic.py`** | Destino já agentic — merge |
| `install_agentspec.py` | Greenfield |
| `install_dev_loop.py` | Só Dev Loop |
| `bootstrap-agentic-project.py` | Cópia quase integral |

---

## Artefatos gerados

| Path | Conteúdo |
|------|----------|
| `.agentic-upgrade/UPGRADE_REPORT.md` | Resumo humano |
| `.agentic-upgrade/incoming/` | Versão template dos conflitos |
| `.agentic-upgrade/preserved/` | Versão que permaneceu no destino |

A pasta `.agentic-upgrade/` está no `.gitignore` do template; commite só se quiser documentar o upgrade no PR.
