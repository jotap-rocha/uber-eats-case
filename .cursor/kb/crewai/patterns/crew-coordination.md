# Padrão: coordenação de crew

> **Problema:** agentes duplicam trabalho ou contradizem-se por falta de contrato de interfaces.
> **MCP validado:** 2026-04-13

## Quando usar

- ≥ 3 agentes ou ≥ 4 tasks.
- Outputs alimentam dashboards ou tickets automáticos.

## Implementação

- **Contrato de texto:** cada `expected_output` lista campos obrigatórios (ex.: `ROOT_CAUSE`, `EVIDENCE`, `CONFIDENCE`).
- **Ordem:** `Process.sequential` + `context=[...]` explícito em vez de depender só da memória implícita.
- **Nomes estáveis:** `role`/`goal` não mudar entre versões sem atualizar testes de snapshot do output.

## Convenções

| Convenção | Motivo |
|-----------|--------|
| IDs externos no `kickoff(inputs=...)` | Reproduzibilidade e logs. |
| Uma task = uma decisão principal | Facilita testes e revisão humana. |

## Exemplo de uso

```python
# Garantir que a task de relatório só vê outputs já estruturados
report = Task(
    description="Usar apenas as secções ROOT_CAUSE e EVIDENCE das tasks anteriores.",
    expected_output="Markdown com ## Resumo, ## Evidência, ## Riscos.",
    agent=reporter,
    context=[investigation_task],
)
```

## Ver também

- [../concepts/tasks.md](../concepts/tasks.md)
- [triage-investigation-report.md](triage-investigation-report.md)
