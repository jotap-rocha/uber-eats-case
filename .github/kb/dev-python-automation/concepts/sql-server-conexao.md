# Conexão a SQL Server a partir de Python

> **Propósito:** Drivers ODBC, strings de conexão e ciclo de vida seguro.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Visão geral

O ecossistema típico é **ODBC Driver for SQL Server** + **`pyodbc`** ou **SQLAlchemy** com dialect `mssql+pyodbc`. A connection string inclui servidor, base, autenticação (Windows, SQL login, Azure AD conforme ambiente) e frequentemente `Encrypt=yes` em cenários modernos.

## Prática

```python
import pyodbc

CONN_STR = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=host;DATABASE=db;"
    "UID=user;PWD=***;"
    "Encrypt=yes;TrustServerCertificate=no;"
)


def open_connection(timeout_s: int = 30) -> pyodbc.Connection:
    return pyodbc.connect(CONN_STR, timeout=timeout_s)
```

- Use **context managers** ou `try/finally` para `close()`.
- **Timeouts:** `timeout` na conexão; para comandos longos, investigar `SET QUERY_GOVERNOR_COST_LIMIT` ou timeout no cursor conforme driver.
- **Pooling:** SQLAlchemy pode gerir pool; com `pyodbc` cru, evitar abrir conexão por linha em loops grandes.

## Referência rápida

| Tema | Nota |
|------|------|
| TLS/certificados | Erros comuns após mudança de `Encrypt`/`TrustServerCertificate` |
| Firewall | Porta 1433 ou instância dinâmica — documentar no runbook |
| Secrets | String montada a partir de vault/env, não literal em código |

## Erros comuns

Concatenar utilizador/password em f-strings logadas — vazar credenciais em agregadores de log.

## Relacionado

- [sql-server-consultas-transacoes.md](sql-server-consultas-transacoes.md)
- [config-segredos.md](../patterns/config-segredos.md)
