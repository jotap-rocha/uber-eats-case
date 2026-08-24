# Padrão: circuit breaker em crews

> **Problema:** LLM + tools podem repetir chamadas ou esgotar quotas.
> **MCP validado:** 2026-04-13

## Quando usar

- APIs externas com rate limit.
- Jobs batch onde falha parcial não pode bloquear fila indefinidamente.

## Implementação

1. **Agente:** `max_iter` baixo + `goal` que proíbe mais de N chamadas à mesma tool.
2. **Tool:** contador em memória/redis por `job_id` + exceção clara ao exceder.
3. **Orquestrador:** `try/except` à volta de `kickoff()` com fallback (ticket humano).

```python
class ToolBudgetExceeded(Exception):
    pass

_CALLS: dict[str, int] = {}

def limited_fetch(job_id: str) -> str:
    _CALLS[job_id] = _CALLS.get(job_id, 0) + 1
    if _CALLS[job_id] > 5:
        raise ToolBudgetExceeded("log fetch cap")
    return fetch_logs_impl(job_id)
```

## Configuração

| Camada | Limite típico |
|--------|----------------|
| Tool | Chamadas / minuto por chave |
| Agent | `max_iter` coerente com o orçamento |

## Ver também

- [log-analysis-agent.md](log-analysis-agent.md)
