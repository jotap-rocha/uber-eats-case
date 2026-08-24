# Ambiente virtual, versão de Python e qualidade automática

> **Propósito:** Mesmo interpretador e dependências em dev, CI e execução agendada; *lint* antes do merge.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

Jobs que ignoram **versão de Python** ou pacotes soltos quebram após upgrades de driver ODBC. Fixe **`requires-python`** no `pyproject.toml`, isole com **venv** (ou container com digest) e **fixe dependências** (lockfile ou `requirements.txt` gerado).

## Versão do interpretador

- **pyenv**, **asdf**, **uv** com pin, ou imagem CI com tag explícita — o importante é **documentar e reproduzir** a mesma família de versão (ex. 3.11.x) que produção.
- Ficheiro **`.python-version`** (ou equivalente) alinhado ao servidor de execução, quando aplicável.

## Isolamento obrigatório

- **Um venv (ou env) por projeto** — não misturar `pip install` global com o job.
- Em CI: criar env limpo e `pip install -e ".[dev]"` ou o fluxo acordado.

## Qualidade antes do commit

- **pre-commit** (ou *hooks* no CI) para correr **Ruff** (e opcionalmente **mypy** / **pyright**) em ficheiros alterados — evita regressões de estilo e imports quebrados.

```toml
[project]
requires-python = ">=3.11"
dependencies = [
    "pyodbc>=5.0,<6",
]
```

## Referência rápida

| Evitar | Preferir |
|--------|----------|
| `pip install` manual em prod sem registo | Manifesto versionado + deploy reproduzível |
| CI sem *lint* | Mesmas regras que o editor (Ruff) |

## Erros comuns

Instalar só `pyodbc` via **pip** sem **unixODBC** (`libodbc.so.2`) e sem **driver Microsoft** no SO — falha ao importar ou ao `connect`. Em **RHEL 9** no cluster Data Lake: `unixODBC` + `msodbcsql17` (driver **ODBC Driver 17 for SQL Server**, alinhado a `src/integrations/database/sql_server.py`). Verificações: `ldconfig -p | grep libodbc`, `odbcinst -q -d`, `python -c "import pyodbc"`.

Checklist de deploy no repositório do job: [**README.md**](../../../../README.md) (secção **Linux / ODBC**) e KB **`/DATALAKE/.github/kb/migration-hub/infra/STATUS-AMBIENTE.md`**.

## Relacionado

- [config-segredos.md](../patterns/config-segredos.md)
- [pep8-legibilidade.md](pep8-legibilidade.md)
