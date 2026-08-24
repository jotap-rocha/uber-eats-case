---
name: sync-agents
description: |
  Mantém o índice local de agentes em `.cursor/agents/README.md` alinhado com os
  arquivos `*.md` reais (exclui README e `_template`). Inclui verificação automática
  via script e passos para regenerar tabelas no Cursor.
---

# Sync Agents — índice `.cursor/agents/README.md`

Garante que a seção **«Índice local (este repositório)»** em `.cursor/agents/README.md` reflete todos os agentes presentes em `.cursor/agents/**/*.md`, com **Total: N agentes** correto e uma linha por agente (link + finalidade).

## Uso rápido

```bash
# Verificação automática (CI ou pré-commit)
npm run sync-agents:check

# Ou diretamente
bash scripts/sync-agents-check.sh

# Listar contagens por pasta (auditoria rápida)
bash scripts/sync-agents-check.sh --list

# Listar todos os caminhos relativos (diff mental vs README)
bash scripts/sync-agents-check.sh --paths
```

No Cursor:

```text
/sync-agents
```

---

## O que valida o script

| Entrada | Regra |
|---------|--------|
| Ficheiros contados | `.cursor/agents/**/*.md` |
| Excluídos | `README.md`, `_template.md` |
| README | Deve conter exatamente `**Total: N agentes**` na linha introdutória do índice local (N = número de agentes) |

- **Exit 0:** N no README = número real de arquivos de agente.
- **Exit 1:** divergência, README sem o padrão, ou caminho em falta.

Isto **não** reescreve o README sozinho — apenas detecta desalinhamento. A actualização das tabelas e descrições é o passo seguinte (manual ou com assistente).

---

## Processo quando o check falhar

### 1. Descobrir o delta

```bash
bash scripts/sync-agents-check.sh --paths > /tmp/agents-disk.txt
# Comparar visualmente com as secções #### `pasta/` no README
```

Ou no Cursor: `Glob(".cursor/agents/**/*.md")` e filtrar mentalmente `README` e `_template`.

### 2. Actualizar o README

1. Abrir `.cursor/agents/README.md`.
2. Localizar **«Índice local (este repositório)»**.
3. Ajustar `**Total: N agentes**` para o valor actual (`bash scripts/sync-agents-check.sh --paths | wc -l` ou contagem manual).
4. Por pasta (`ai-ml/`, `code-quality/`, …):
   - Adicionar linha na tabela para cada novo `nome.md` com link relativo `pasta/nome.md`.
   - Remover linhas de agentes apagados.
   - Actualizar a coluna **Finalidade** (ler o `description:` no frontmatter do agente).

### 3. Regeneração assistida (recomendado para muitas alterações)

Pedir ao assistente no Cursor:

```text
/sync-agents — lista todos os .md em .cursor/agents exceto README e _template;
regenera só a seção «Índice local» do README com tabelas por pasta, links relativos
e uma linha de finalidade em português por agente (ler description no frontmatter).
```

O assistente deve:

1. Executar `bash scripts/sync-agents-check.sh --list` e `--paths` (ou equivalente).
2. Ler `name:` e `description:` de cada arquivo (primeiras linhas do YAML).
3. Substituir o bloco desde `### Índice local` até ao `---` imediatamente a seguir ao último `workflow/` (antes de `## How Agents Work`), preservando o resto do README intacto.

### 4. Confirmar

```bash
npm run sync-agents:check
```

---

## Integração CI (opcional)

Exemplo em job de pipeline:

```yaml
- name: Verificar índice de agentes
  run: npm run sync-agents:check
```

Ou hook git local (`pre-commit`): mesmo comando; falha se alguém adicionar agente sem actualizar o total no README.

---

## Convenções a preservar

- Um arquivo `*.md` por agente; `name:` no frontmatter = nome base do arquivo (kebab-case).
- Pastas estáveis (este repo): `ai-ml/`, `code-quality/`, `communication/`, `databricks/`, `data-engineering/`, `dev/`, `domain/`, `exploration/`, `infra/`, `workflow/`, `workflow-makeapp-review/`, `workflow-data-pipeline-review/`.
- Links no README: relativos ao directório `.cursor/agents/` (ex.: `[nome](data-engineering/nome.md)`).

---

## Checklist antes de concluir

```text
[ ] npm run sync-agents:check passa (exit 0)
[ ] **Total: N agentes** corresponde ao número de arquivos (exclui README e _template)
[ ] Cada pasta com agentes tem seção #### `pasta/` e tabela completa
[ ] Novos agentes têm linha com link e finalidade coerente com description do frontmatter
```

---

## Lembrete

> **Verificação é automática; o texto das tabelas continua sendo revisão humana ou uma edição assistida no Cursor — o script evita drift silencioso do número total.**
