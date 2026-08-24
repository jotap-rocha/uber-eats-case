# Tools (CrewAI)

> **Finalidade:** dar ao agente ações determinísticas (API, DB read-only, ficheiros) com limites claros.
> **Confiança:** 0.90 · **MCP validado:** 2026-04-13

## Visão geral

Tools são funções ou classes que o CrewAI expõe ao LLM com **nome**, **descrição** e **schema de argumentos**. Em pipelines de dados, prefira **read-only**, timeouts explícitos e logs estruturados do lado da tool (não confiar só no texto do modelo).

## Padrão (função)

```python
from crewai.tools import tool

@tool("fetch_job_logs")
def fetch_job_logs(job_id: str, tail: int = 200) -> str:
    """Obtém as últimas N linhas de log do job (somente leitura)."""
    # implementação real: client SDK / HTTP
    return "... log text ..."
```

## Referência rápida

| Prática | Motivo |
|---------|--------|
| Args pequenos e tipados | Menos alucinação de parâmetros. |
| Sem credenciais nos args | Usar env / vault na implementação. |
| Timeout + limite de bytes | Evita estouro de contexto do LLM. |

## Erros comuns

### Evitar

```python
@tool("run_any_sql")
def run_any_sql(q: str) -> str:
    return db.execute(q)  # perigoso
```

### Preferir

```python
@tool("get_table_sample")
def get_table_sample(schema: str, table: str, limit: int = 50) -> str:
    """SELECT limitado, allowlist de tabelas."""
    ...
```

## Relacionados

- [agents.md](agents.md)
- [../patterns/log-analysis-agent.md](../patterns/log-analysis-agent.md)
