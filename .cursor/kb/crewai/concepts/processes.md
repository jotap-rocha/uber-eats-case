# Process (CrewAI)

> **Finalidade:** definir como as tasks fluem entre agentes.
> **Confiança:** 0.90 · **MCP validado:** 2026-04-13

## Visão geral

`Process.sequential` executa tasks na ordem da lista: simples e previsível. `Process.hierarchical` introduz um **gestor** que pode delegar — útil quando há triagem e especialização, com custo e complexidade superiores (configuração de LLM gestor, limites de delegação).

## Sequencial

```python
from crewai import Crew, Process

crew = Crew(
    agents=[triage, specialist, reporter],
    tasks=[t1, t2, t3],
    process=Process.sequential,
)
```

## Hierárquico (ideia)

- Adequado quando o primeiro agente **decide** qual ramo seguir ou precisa de **replaneamento**.
- Exige disciplina: objetivos claros, `allow_delegation` bem definido, e revisão humana em ações sensíveis.

## Matriz rápida

| Critério | Sequencial | Hierárquico |
|----------|------------|-------------|
| Previsibilidade | Alta | Média |
| Custo tokens | Tipicamente menor | Maior |
| Exploração de hipóteses | Baixa | Maior |

## Relacionados

- [crews.md](crews.md)
- [../patterns/escalation-workflow.md](../patterns/escalation-workflow.md)
