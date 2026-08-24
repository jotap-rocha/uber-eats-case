# Agent (CrewAI)

> **Finalidade:** definir um participante autónomo com papel, objetivo e meios (LLM + tools).
> **Confiança:** 0.95 · **MCP validado:** 2026-04-13

## Visão geral

Um `Agent` condensa **quem** resolve o problema (`role`), **para quê** (`goal`), **como raciocinar** (`backstory`) e **que ações pode executar** (`tools`). O LLM escolhido (`llm`) deve ter permissões alinhadas ao risco das tools (só leitura vs escrita).

## Padrão mínimo

```python
from crewai import Agent
from crewai.llm import LLM

researcher = Agent(
    role="Analista de incidentes",
    goal="Resumir causas prováveis com base em evidências fornecidas.",
    backstory="Especialista em SRE; nunca inventa IDs de tickets.",
    llm=LLM(model="openai/gpt-4o-mini", base_url="...", api_key="..."),
    tools=[],  # ou ferramentas read-only
    verbose=True,
    allow_delegation=False,
)
```

## Referência rápida

| Campo | Efeito |
|-------|--------|
| `allow_delegation` | `False` reduz pedidos de sub-agentes em crews simples. |
| `max_iter` | Limite de raciocínio/retry por agente (mitigar loops). |
| `tools` | Lista de callables / classes tool registadas no CrewAI. |

## Erros comuns

### Evitar

```python
Agent(role="Fix", goal="Corrigir produção", backstory="Acesso root implícito", tools=[dangerous_shell])
```

### Preferir

```python
Agent(
    role="Analista",
    goal="Propor passos humanos; não executar escrita em produção.",
    backstory="Só usa tools read-only (logs, métricas).",
    tools=[read_logs, read_metrics],
)
```

## Relacionados

- [tasks.md](tasks.md) — atribuir trabalho ao agente.
- [tools.md](tools.md) — definir ferramentas seguras.
- [../patterns/crew-coordination.md](../patterns/crew-coordination.md) — convenções de equipa.
