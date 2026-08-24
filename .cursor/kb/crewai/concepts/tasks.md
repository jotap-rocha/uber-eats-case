# Task (CrewAI)

> **Finalidade:** descrever uma unidade de trabalho com saída verificável.
> **Confiança:** 0.95 · **MCP validado:** 2026-04-13

## Visão geral

`Task` liga **descrição** (`description`), **agente responsável** (`agent`), **critério de qualidade da saída** (`expected_output`) e opcionalmente **contexto** (`context`: outras tasks já concluídas). Use `expected_output` explícito (formato, campos, o que não inventar).

## Padrão

```python
from crewai import Task

summarize = Task(
    description="Dado o incident_id em {{incident_id}}, sintetizar timeline em 5 bullets.",
    expected_output="Markdown: ## Timeline com bullets datados; sem PII.",
    agent=researcher,
)

report = Task(
    description="Transformar a timeline num relatório one-page para gestão.",
    expected_output="Markdown com: Resumo, Impacto, Próximos passos.",
    agent=writer,
    context=[summarize],
)
```

## Referência rápida

| Campo | Notas |
|-------|--------|
| `context` | Lista de `Task` cujo output alimenta esta task (ordem de crew importa). |
| `output_file` | Útil para artefactos longos (relatório em disco). |
| `human_input` | Pausa para aprovação humana quando o risco o exige. |

## Erros comuns

### Evitar

```python
Task(description="Arranja isto", agent=agent)
```

### Preferir

```python
Task(
    description="Listar apenas erros HTTP 5xx nos últimos 15 min (fonte: tool).",
    expected_output="Tabela markdown: timestamp, rota, código.",
    agent=agent,
)
```

## Relacionados

- [agents.md](agents.md)
- [crews.md](crews.md)
- [../patterns/triage-investigation-report.md](../patterns/triage-investigation-report.md)
