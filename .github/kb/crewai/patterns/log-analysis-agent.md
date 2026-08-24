# Padrão: agente de análise de logs

> **Problema:** LLM precisa de **evidência** extraída de forma controlada, não do log bruto completo.
> **MCP validado:** 2026-04-13

## Quando usar

- Jobs Spark/Airflow com stack traces longos.
- Necessidade de filtrar por janela temporal ou `correlation_id`.

## Implementação

1. **Tool** `fetch_logs(job_id, from_ts, to_ts, grep)` com limite de linhas e bytes.
2. **Agent** com `goal` explícito: “só concluir com citações de linhas devolvidas pela tool”.
3. **Task** com `expected_output`: formato fixo (ex.: JSON ou markdown com secções).

```python
@tool("get_errors")
def get_errors(job_id: str) -> str:
    """Últimos erros ERROR/FATAL, truncado a 16 KiB."""
    ...

analyst = Agent(
    role="Log analyst",
    goal="Explicar falha com base apenas no output das tools.",
    tools=[get_errors],
    ...
)
```

## Configuração

| Definição | Descrição |
|-----------|-----------|
| Truncagem | Obrigatória antes de enviar ao modelo. |
| PII | Mascarar tokens, emails, IPs internos se política o exigir. |

## Ver também

- [../concepts/tools.md](../concepts/tools.md)
- [circuit-breaker.md](circuit-breaker.md)
