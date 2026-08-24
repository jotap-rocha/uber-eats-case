# Consultas parametrizadas e transações (SQL Server)

> **Propósito:** Segurança (SQL injection), consistência e comportamento previsível em jobs.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Visão geral

**Nunca** interpolar entrada do utilizador ou de ficheiros diretamente em SQL com f-strings. Use **placeholders** (`?` em pyodbc) ou parâmetros nomeados no ORM. Para várias escritas relacionadas, agrupe em **transação** única (`COMMIT`/`ROLLBACK`).

## Padrão pyodbc

```python
def fetch_pending(cursor: pyodbc.Cursor, limit: int) -> list:
    cursor.execute(
        "SELECT id, payload FROM dbo.queue WHERE status = ? ORDER BY id",
        ("pending",),
    )
    return cursor.fetchmany(limit)


def mark_done(cursor: pyodbc.Cursor, conn: pyodbc.Connection, ids: list[int]) -> None:
    cursor.fast_executemany = True  # quando aplicável a batches
    cursor.executemany(
        "UPDATE dbo.queue SET status = 'done' WHERE id = ?",
        [(i,) for i in ids],
    )
    conn.commit()
```

## Transações

```python
with conn.claude() as cur:
    try:
        cur.execute("BEGIN TRANSACTION")
        ...
        conn.commit()
    except Exception:
        conn.rollback()
        raise
```

(Alternativa: `conn.autocommit = False` e `commit` explícito conforme estilo do projeto.)

## Referência rápida

| Situação | Orientação |
|----------|------------|
| Leitura só | Transação curta ou autocommit conforme isolamento desejado |
| Várias tabelas | Uma transação para atomicidade |
| Deadlocks | Retries com backoff no padrão de resiliência |

## Erros comuns

### Errado

```python
cursor.execute(f"SELECT * FROM t WHERE name = '{user_input}'")
```

### Certo

```python
cursor.execute("SELECT * FROM t WHERE name = ?", (user_input,))
```

## Relacionado

- [retry-circuit-breaker.md](../patterns/retry-circuit-breaker.md)
- [repositorio-acesso-dados.md](../patterns/repositorio-acesso-dados.md)
