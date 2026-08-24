# CrewAI — Knowledge Base

> Orquestração multi-agente em Python para fluxos autónomos (monitorização DataOps, triagem, relatórios). **Nota:** “creaw ai” costuma referir-se a **CrewAI** (`crewai` no PyPI).
> **MCP validado:** 2026-04-13

## Navegação rápida

### Conceitos (≤ 150 linhas)

| Ficheiro | Finalidade |
|----------|------------|
| [concepts/agents.md](concepts/agents.md) | `Agent`: papel, objetivo, LLM, ferramentas, backstory. |
| [concepts/tasks.md](concepts/tasks.md) | `Task`: descrição, agente, contexto, saída esperada. |
| [concepts/crews.md](concepts/crews.md) | `Crew`: composição, `kickoff()`, processo, verbosidade. |
| [concepts/tools.md](concepts/tools.md) | Ferramentas custom e integração com agentes. |
| [concepts/memory.md](concepts/memory.md) | Memória entre passos e partilha de contexto. |
| [concepts/processes.md](concepts/processes.md) | `Process`: sequencial vs hierárquico. |

### Padrões (≤ 200 linhas)

| Ficheiro | Finalidade |
|----------|------------|
| [patterns/triage-investigation-report.md](patterns/triage-investigation-report.md) | Crew de triagem → investigação → relatório. |
| [patterns/log-analysis-agent.md](patterns/log-analysis-agent.md) | Agente focado em logs e extração estruturada. |
| [patterns/escalation-workflow.md](patterns/escalation-workflow.md) | Critérios de escalação e handoff entre agentes. |
| [patterns/slack-integration.md](patterns/slack-integration.md) | Resumos e alertas para canais (tool ou pós-processo). |
| [patterns/circuit-breaker.md](patterns/circuit-breaker.md) | Limitar tentativas e falhar de forma controlada. |
| [patterns/crew-coordination.md](patterns/crew-coordination.md) | Convenções de contexto e ordem de tarefas. |

## Referência rápida

- [quick-reference.md](quick-reference.md) — tabelas e decisões em 1 página.

## Percurso de leitura

| Nível | Ficheiros |
|-------|-----------|
| Início | `concepts/agents.md` → `concepts/tasks.md` → `concepts/crews.md` |
| Intermédio | `concepts/processes.md`, `patterns/crew-coordination.md` |
| Operações | `patterns/triage-investigation-report.md`, `patterns/circuit-breaker.md` |

## Uso com agentes

| Agente / contexto | Ficheiros |
|-------------------|-----------|
| `kb-architect`, pipelines agentic | `index.md`, `patterns/*`, [`.claude/kb/pydantic/`](../pydantic/) para saídas estruturadas |

## Ver também

- [`.claude/kb/_index.yaml`](../_index.yaml) — registo `crewai`.
- Documentação oficial: [https://docs.crewai.com/](https://docs.crewai.com/)
