# Padrão: escalação entre agentes

> **Problema:** nem todo incidente deve ir ao mesmo nível de profundidade ou ao mesmo canal.
> **MCP validado:** 2026-04-13

## Quando usar

- SLAs diferentes por severidade.
- Necessidade de **human-in-the-loop** só acima de um limiar.

## Implementação

- **Opção A — duas crews:** crew rápida de triagem; se output contiver `ESCALATE`, o orquestrador Python chama segunda crew (mais cara).
- **Opção B — task com ramo:** descrição da task obriga o agente a etiquetar `SEVERITY: P1|P2|P3`; o código downstream bifurca.

```python
def run_escalation(incident: dict):
    first = triage_crew.kickoff(inputs=incident)
    if "SEVERITY: P1" in first.raw:
        return deep_crew.kickoff(inputs=incident)
    return first
```

## Configuração

| Gatilho | Ação |
|---------|------|
| Palavra-chave estruturada | Parsing simples + segunda crew |
| Métrica externa | Orquestrador consulta API antes do kickoff |

## Ver também

- [triage-investigation-report.md](triage-investigation-report.md)
- [slack-integration.md](slack-integration.md)
