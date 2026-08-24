# Padrão repositório para SQL Server

> **Propósito:** Isolar SQL e mapeamento de linhas, facilitando SOLID e testes.
> **MCP Validated:** 2026-05-06

## Quando usar

- Mais de uma query ou stored procedure por domínio.
- Necessidade de **substituir** implementação em testes sem monkeypatch frágil.

## Implementação

Defina um **Protocol** ou ABC com operações de alto nível (`list_pending`, `save_result`). A implementação `SqlServerQueueRepository` usa `pyodbc` internamente e traduz **rows → dataclasses**.

```python
from collections.abc import Callable

import pyodbc
from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class QueueItem:
    id: int
    payload: str


class QueueRepository(Protocol):
    def list_pending(self, limit: int) -> list[QueueItem]: ...
    def mark_processed(self, ids: list[int]) -> None: ...


class SqlServerQueueRepository:
    def __init__(self, conn_factory: Callable[[], pyodbc.Connection]) -> None:
        self._conn_factory = conn_factory

    def list_pending(self, limit: int) -> list[QueueItem]:
        conn = self._conn_factory()
        try:
            with conn.claude() as cur:
                cur.execute(
                    "SELECT id, payload FROM dbo.queue WHERE status = ?",
                    ("pending",),
                )
                rows = cur.fetchmany(limit)
            return [QueueItem(id=r[0], payload=r[1]) for r in rows]
        finally:
            conn.close()
```

## Configuração

| Opção | Trade-off |
|-------|-----------|
| Nova conexão por operação | Simples; overhead em alta frequência |
| Pool SQLAlchemy | Melhor para serviços long-lived |
| Factory injetável | Essencial para testes com sqlite mock ou fake |

## Exemplo de uso

```python
def process_batch(repo: QueueRepository, limit: int = 50) -> int:
    items = repo.list_pending(limit)
    ...
    repo.mark_processed([i.id for i in items])
    return len(items)
```

## Veja também

- [../concepts/solid-scripts.md](../concepts/solid-scripts.md)
- [testes-db-mocks.md](testes-db-mocks.md)
