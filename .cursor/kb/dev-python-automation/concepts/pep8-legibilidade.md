# PEP 8+ — estilo, legibilidade e ferramentas

> **Propósito:** Código legível para humanos e para ferramentas (linters, type checkers, revisões).
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

A **PEP 8** é a referência completa de estilo para Python. Em revisão e CI, **todo o conjunto de regras PEP 8** deve ser considerado; este documento resume **convenções de equipa** e **automação** que as aplicam de forma consistente (não substitui a leitura da PEP 8 quando houver dúvida).

## Nomenclatura

| Elemento | Convenção | Nota |
|----------|-------------|------|
| Funções, variáveis, métodos | `snake_case` | Nomes **descritivos** (`get_user_balance`) em vez de genéricos demais (`balance`) quando o contexto não basta |
| Classes | `PascalCase` | |
| Constantes de módulo | `UPPER_SNAKE` | Valores imutáveis partilhados |

## Formatação e indentação

- **Indentação:** 4 espaços (não tabs), alinhado à PEP 8.
- **Ferramenta recomendada:** **Ruff** para *lint* e *format* (substitui de forma prática *flake8* + *isort* + *black* num único ecossistema rápido). O projeto pode fixar regras em `pyproject.toml` / `ruff.toml`.
- **Linha longa:** quebrar com parênteses ou extrair variável; respeitar `line-length` acordada (p.ex. 88 ou 100).

## Type hints

- **Obrigatório** em **assinaturas públicas** (funções e métodos expostos a outros módulos): parâmetros e tipo de retorno explícitos (`def process(batch: list[Row]) -> Report:`).
- Módulos internos muito pequenos podem relaxar só o que o *type checker* e o *code review* aceitarem — o padrão do projeto deve ser explícito no `pyproject` ou no guia de equipa.

```python
def load_pending(conn: Connection, limit: int) -> list[PendingRow]:
    ...
```

## Imports e documentação

- Ordem: stdlib → terceiros → locais; evitar imports não usados (Ruff remove/acusa).
- **Docstrings:** uma frase no módulo e em APIs públicas não óbvias; Args/Returns quando ajudar o consumidor.

## Erros comuns

| Evitar | Preferir |
|--------|----------|
| `except:` sem tipo | Capturar exceções específicas + log + re-raise ou código de saída |
| Nomes opacos (`tmp`, `x1`) | Nome que descreve papel no job |
| Ignorar avisos do Ruff “só desta vez” sem issue | Supressão pontual documentada |

## Relacionado

- [tipagem-fronteiras.md](tipagem-fronteiras.md)
- [../patterns/injecao-dependencias.md](../patterns/injecao-dependencias.md)
