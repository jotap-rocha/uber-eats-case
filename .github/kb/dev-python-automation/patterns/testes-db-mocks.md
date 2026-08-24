# Testes com mocks e contratos (camada DB)

> **Propósito:** Validar regras sem dependência permanente de SQL Server em cada `pytest`.
> **MCP Validated:** 2026-05-06

## Quando usar

- Lógica em `services/` que depende de `QueueRepository` ou equivalente.
- CI sem instância SQL disponível.

## Implementação

1. **Fake in-memory:** implementação do `Protocol` com listas/dicts.
2. **unittest.mock:** patch de `cursor.execute` apenas quando não houver tempo para extrair repositório (dívida técnica).
3. **Testcontainers / DB efémero:** poucos testes de integração para garantir compatibilidade real de SQL (opcional, ROI).

```python
class FakeQueueRepo:
    def __init__(self, items: list[QueueItem]) -> None:
        self._items = items
        self.processed: list[int] = []

    def list_pending(self, limit: int) -> list[QueueItem]:
        return list(self._items[:limit])

    def mark_processed(self, ids: list[int]) -> None:
        self.processed.extend(ids)


def test_process_batch_marks_all():
    repo = FakeQueueRepo([QueueItem(1, "a"), QueueItem(2, "b")])
    n = process_batch(repo, limit=10)
    assert n == 2
    assert repo.processed == [1, 2]
```

## Contratos

- Testar que **queries dinâmicas** não são construídas sem parâmetros — revisão + lint onde possível.
- Um teste de integração mínimo valida **syntax** da SP ou `SELECT 1` em ambiente de staging.

## Veja também

- [repositorio-acesso-dados.md](repositorio-acesso-dados.md)
- [../concepts/tipagem-fronteiras.md](../concepts/tipagem-fronteiras.md)
