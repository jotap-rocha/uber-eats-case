# Crew (CrewAI)

> **Finalidade:** executar um conjunto ordenado de tarefas com agentes partilhando processo e configuração.
> **Confiança:** 0.95 · **MCP validado:** 2026-04-13

## Visão geral

`Crew` agrega `agents`, `tasks`, `process` (estratégia de coordenação), flags de execução (`verbose`, `memory`) e chama `kickoff()` para produzir o resultado final. Inputs comuns (`inputs=dict`) substituem placeholders `{{chave}}` nas descrições das tasks.

## Padrão

```python
from crewai import Crew, Process

crew = Crew(
    agents=[researcher, writer],
    tasks=[summarize, report],
    process=Process.sequential,
    verbose=True,
)

result = crew.kickoff(inputs={"incident_id": "INC-4421"})
print(result.raw)
```

## Referência rápida

| Parâmetro | Uso |
|-----------|-----|
| `process=Process.sequential` | Ordem da lista `tasks`. |
| `process=Process.hierarchical` | Requer `manager_llm` / agente gestor conforme docs atuais. |
| `full_output` / tracing | Depende da versão; usar observabilidade oficial (CrewAI tracing) em produção. |

## Erros comuns

### Evitar

```python
Crew(agents=[a], tasks=[], process=Process.sequential).kickoff()
```

### Preferir

```python
# Validar pré-condições antes do kickoff
assert tasks, "tasks vazias"
crew = Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=True)
out = crew.kickoff(inputs={})
```

## Relacionados

- [processes.md](processes.md)
- [memory.md](memory.md)
- [../patterns/circuit-breaker.md](../patterns/circuit-breaker.md)
