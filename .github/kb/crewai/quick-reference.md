# CrewAI — referência rápida

> Tabelas compactas. Exemplos completos nos `concepts/` e `patterns/`.

## Objetos principais

| Classe | Responsabilidade |
|--------|------------------|
| `Agent` | Papel, objetivo, backstory, LLM, `tools`. |
| `Task` | Trabalho atómico; `description`, `expected_output`, `agent`. |
| `Crew` | Conjunto de agentes + tarefas + `process` + execução (`kickoff`). |
| `Process` | Ordem/coordenação (ex.: sequencial, hierárquico). |

## `kickoff` vs inputs

| Necessidade | Abordagem |
|-------------|-----------|
| Entrada única para a crew | `crew.kickoff(inputs={"incident_id": "..."})` |
| Contexto só numa tarefa | `Task(..., context=[outra_task])` ou descrição rica |

## Processos

| `process` | Quando |
|-----------|--------|
| Sequencial | Pipeline linear de tarefas dependentes. |
| Hierárquico | Gestor delega; útil para triagem → especialistas. |

## Ferramentas

| Não fazer | Fazer |
|-----------|--------|
| Colocar segredos na `backstory` | Variáveis de ambiente + tools que leem env |
| Ferramenta sem schema claro | Docstring + args tipados / Pydantic onde couber |

## Memória

| Tipo de necessidade | Leitura |
|---------------------|---------|
| Lembrar decisões entre tasks | `concepts/memory.md` |
| Output estruturado entre agentes | `expected_output` + parsing ou modelo Pydantic |

## Erros comuns

| Sintoma | Causa provável |
|---------|----------------|
| Agente “inventa” APIs internas | Objetivo vago; falta de tools read-only |
| Loops de retry | Sem limite; ver `patterns/circuit-breaker.md` |
| Output inconsistente | `expected_output` pouco específico |

## Relacionados no repo

| Tema | KB |
|------|-----|
| Validação de JSON/LLM | `pydantic/` |
| Modelos e roteamento de API | `openrouter/` |
