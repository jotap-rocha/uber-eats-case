# Filosofia: modularidade, SOLID e fail fast

> **Propósito:** Princípios que orientam a árvore de pastas e as fronteiras entre módulos.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

Automações **profissionais** tratam o repositório como **pacote instalável**, com camadas que limitam o acoplamento: quem define **regra de negócio** não escolhe driver ODBC nem monta payload HTTP.

## PEP 8 e tipagem

Seguir a **PEP 8 na íntegra** em revisão (nomes, indentação, imports). Tipagem explícita nas APIs públicas — detalhes de ferramentas (**Ruff**, pre-commit) estão em [dev-python-automation](../../dev-python-automation/concepts/pep8-legibilidade.md).

## SOLID e desacoplamento

| Ideia | Neste desenho |
|-------|----------------|
| **SRP** | `app/main.py` só bootstrap; `core` só roteiro; `integrations` só IO |
| **DIP** | `core` depende de interfaces ou funções injetadas construídas na composição (tipicamente antes do `start` em `main`) — ver [injecao-dependencias](../../dev-python-automation/patterns/injecao-dependencias.md) |
| **Integrações isoladas** | Subpastas por tipo: `database/`, `messaging/`, `cloud/` |

**Regra:** código em **`core`** não importa `pyodbc`, SDK de Teams ou cliente HTTP “raw”; recebe resultados já tipados dos adaptadores.

Contratos explícitos: [app-main-contract.md](app-main-contract.md), [core-orquestracao.md](core-orquestracao.md), [integrations-execucao.md](integrations-execucao.md).

## Fail fast

No **arranque** do entrypoint (logo após carregar config):

1. Validar ficheiros YAML obrigatórios e ambiente (`dev` vs `prod`).
2. Verificar conectividade mínima ou credencial de cofre **antes** de processar lotes grandes.
3. Falhar com **mensagem clara** e **código de saída** documentado — ver [logging-exit-codes](../../dev-python-automation/concepts/logging-exit-codes.md).

## Relacionado

- [estrutura-pastas-src-layout.md](estrutura-pastas-src-layout.md)
- [parametros-vs-segredos.md](parametros-vs-segredos.md)
