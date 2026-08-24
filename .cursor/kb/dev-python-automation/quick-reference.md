# dev-python-automation — referência rápida

> **MCP Validated:** 2026-05-07

## PEP 8+

| Regra | Detalhe |
|-------|---------|
| **Baseline** | Considerar a **PEP 8 na íntegra** em review; este KB resume o que automatizar |
| **Nomes** | `snake_case` / `PascalCase` / `UPPER_SNAKE`; preferir descritivos |
| **Indentação** | 4 espaços |
| **Ferramentas** | **Ruff** *lint* + *format* (ecossistema único, rápido) |
| **APIs públicas** | Type hints obrigatórios em parâmetros e retorno |

## SOLID (resumo)

| Letra | Lembrete |
|-------|------------|
| **S** | Uma responsabilidade por unidade (ler DB ≠ regra ≠ email) |
| **O** | Estender com novas classes/`Protocol`, não inflar `if` |
| **L** | *Fakes* substituem reais sem quebrar contrato |
| **I** | Portas pequenas (ler vs escrever) |
| **D** | Injetar abstrações; ver `patterns/injecao-dependencias.md` |

## Projeto e execução

| Preferir | Evitar |
|----------|--------|
| Layout **`src/`** + `pyproject.toml` | Scripts que só “funcionam” com `cd` mágico |
| `python -m pacote.modulo` ou `pip install -e .` | `sys.path.append(...)` |

**Árvore detalhada** (`config/`, `core` vs `integrations`, vault): [design-automation-project-patterns](../design-automation-project-patterns/quick-reference.md).

## Ambiente e CI

| Peça | Nota |
|------|------|
| **venv** | Obrigatório por projeto |
| **Versão Python** | pyenv / asdf / uv / imagem com pin — documentar |
| **pre-commit** | Ruff (e opcionalmente mypy/pyright) antes do merge |

## SQL Server (Python)

| Peça | Orientação |
|------|--------------|
| Driver | ODBC 17/18 + DSN ou connection string |
| API | `pyodbc` ou SQLAlchemy `mssql+pyodbc` |
| Queries | Sempre parametrizadas |

## Logs e erros

| Tema | Orientação |
|------|------------|
| Exceções | Hierarquia de domínio (`JobError`, …) |
| Validação | *Fail fast* no início da função pública |
| Níveis | `INFO` fluxo, `WARNING` recuperável, `ERROR` fatal/intervenção |

## Ligações

| Documento | Caminho |
|-----------|---------|
| Índice | `index.md` |
| Checklist | `specs/automation-job-checklist.yaml` |
