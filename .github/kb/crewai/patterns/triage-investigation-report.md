# Padrão: triagem → investigação → relatório

> **Problema:** incidentes repetitivos precisam de pipeline humano-legível com separação de papéis.
> **MCP validado:** 2026-04-13

## Quando usar

- Alertas de pipeline/job com sintomas conhecidos.
- Necessidade de **rastreio** (quem disse o quê) e relatório final único.
- Equipa quer reutilizar a mesma crew com `inputs` diferentes.

## Implementação (esqueleto)

```python
# Pseudocódigo — ajustar imports à versão crewai do projeto
from crewai import Agent, Task, Crew, Process

triage = Agent(role="Triagem", goal="Classificar severidade e âmbito.", ...)
investigator = Agent(role="Investigação", goal="Correlacionar logs e métricas.", tools=[...])
author = Agent(role="Relatório", goal="Produzir sumário executivo.", ...)

t1 = Task(description="Classificar incidente {{incident_id}}...", agent=triage, ...)
t2 = Task(description="Profundizar na classe identificada...", agent=investigator, context=[t1], ...)
t3 = Task(description="Redigir relatório one-pager...", agent=author, context=[t1, t2], ...)

crew = Crew(agents=[triage, investigator, author], tasks=[t1, t2, t3], process=Process.sequential)
result = crew.kickoff(inputs={"incident_id": "INC-1"})
```

## Configuração

| Definição | Valor típico | Nota |
|-----------|--------------|------|
| `process` | `sequential` | Mantém narrativa auditável. |
| Tools em investigação | read-only | Evita “auto-remediação” não aprovada. |

## Ver também

- [escalation-workflow.md](escalation-workflow.md)
- [crew-coordination.md](crew-coordination.md)
