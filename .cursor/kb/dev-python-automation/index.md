# Python para automação — estilo, SOLID e SQL Server

> **Propósito:** Boas práticas para **scripts e jobs** em Python: **toda a PEP 8** como referência (este KB destaca convenções e ferramentas), **SOLID** para evitar espaguete, **layout `src/`** e execução por módulo, **injeção de dependências**, integração **SQL Server** (pyodbc/SQLAlchemy), sem foco em pipelines analíticos pesados.
> **MCP Validated:** 2026-05-07

## Navegação rápida

### Conceitos (≤150 linhas)

| Ficheiro | Tema |
|----------|------|
| [concepts/pep8-legibilidade.md](concepts/pep8-legibilidade.md) | PEP 8 completa como baseline; Ruff; indentação; nomes; hints públicos |
| [concepts/solid-scripts.md](concepts/solid-scripts.md) | SOLID generalizado; SRP; OCP/LSP/ISP/DIP |
| [concepts/tipagem-fronteiras.md](concepts/tipagem-fronteiras.md) | Tipos em fronteiras e APIs públicas |
| [concepts/estrutura-modulos-job.md](concepts/estrutura-modulos-job.md) | Layout `src/`, `python -m`, sem `sys.path` |
| [concepts/logging-exit-codes.md](concepts/logging-exit-codes.md) | Exceções de domínio, fail fast, níveis de log, exit codes |
| [concepts/ambiente-reprodutivel.md](concepts/ambiente-reprodutivel.md) | venv, versão Python, pre-commit + Ruff |
| [concepts/sql-server-conexao.md](concepts/sql-server-conexao.md) | Drivers, DSN, ciclo de vida |
| [concepts/sql-server-consultas-transacoes.md](concepts/sql-server-consultas-transacoes.md) | Parâmetros, transações, timeouts |

### Padrões (≤200 linhas)

| Ficheiro | Tema |
|----------|------|
| [patterns/injecao-dependencias.md](patterns/injecao-dependencias.md) | DI, composição na `main`, desacoplamento |
| [patterns/repositorio-acesso-dados.md](patterns/repositorio-acesso-dados.md) | Repositório SQL Server |
| [patterns/retry-circuit-breaker.md](patterns/retry-circuit-breaker.md) | Retries e backoff |
| [patterns/config-segredos.md](patterns/config-segredos.md) | Config e segredos fora do Git |
| [patterns/testes-db-mocks.md](patterns/testes-db-mocks.md) | Mocks e contratos |

### Specs

| Ficheiro | Tema |
|----------|------|
| [specs/automation-job-checklist.yaml](specs/automation-job-checklist.yaml) | Checklist de revisão |

---

## Referência rápida

- [quick-reference.md](quick-reference.md)

---

## Relação com **dev-python-engineering**

A KB [dev-python-engineering](../dev-python-engineering/index.md) cobre **performance de dados**, I/O colunar, vetorização e paralelismo. Use **dev-python-automation** para **operação**, **estilo**, **arquitetura de pacote** e **SQL Server** em jobs.

---

## Relação com **design-automation-project-patterns**

Para a **árvore de pastas** consolidada (`config/`, `src/<pacote>/` com `core` vs `integrations`), **YAML por ambiente** e **facade única de vault**, ver [design-automation-project-patterns](../design-automation-project-patterns/index.md). **dev-python-automation** cobre o **como codificar** dentro dessa estrutura (PEP 8, Ruff, DI, SQL parametrizado).

---

## Agentes sugeridos

| Recurso | Uso |
|---------|-----|
| [python-developer.md](../../agents/code-quality/python-developer.md) | Estilo, dataclasses, testes |
