# Memory (CrewAI)

> **Finalidade:** manter contexto entre passos sem duplicar prompts gigantes.
> **Confiança:** 0.85 · **MCP validado:** 2026-04-13

## Visão geral

Memória no CrewAI pode ser **curta** (resumos na própria crew) ou integrações mais ricas conforme versão (ex.: memória de entidade / storage externo — consultar a documentação da versão pinada no projeto). Na prática de DataOps: **primeiro** use `context=[...]` entre tasks; **depois** ative flags de memória da crew se precisar de continuidade automática.

## Quando usar

| Cenário | Abordagem |
|---------|-----------|
| Task B precisa do output de A | `context=[task_a]` |
| Muitas interações na mesma sessão | Memória da crew + resumos curtos |
| Auditoria / compliance | Persistir outputs em ficheiro ou fila, não só RAM |

## Anti-padrão

- Colocar dumps completos de logs na memória em texto livre → estoura tokens e mistura ruído.
- Preferir **extração estruturada** na task anterior (tabela curta) e passar só isso adiante.

## Relacionados

- [tasks.md](tasks.md)
- [crews.md](crews.md)
- [../../pydantic/concepts/base-model.md](../../pydantic/concepts/base-model.md) — saídas estruturadas quando combinar com Pydantic no projeto.
