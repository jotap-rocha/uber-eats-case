# Padrões de desenho — projeto de automação (pastas e camadas)

> **Propósito:** **Árvore de pastas**, contrato **`src/app` = só `main.py`**, **`core` = orquestração**, **`integrations` = execução**, config YAML vs cofre, fail fast — generalizável (ex.: **Sentinela**).
> **MCP Validated:** 2026-05-07

## Regra — pacote sob `src/`

Layout universal em `src/app`, `src/core`, `src/integrations`, `src/utils` — ver [estrutura-pastas-src-layout.md](concepts/estrutura-pastas-src-layout.md). O nome em `[project] name` no `pyproject.toml` é a distribuição pip, não obrigar pasta extra.

## Navegação

### Contratos de camada (ler primeiro)

| Ficheiro | Tema |
|----------|------|
| [concepts/app-main-contract.md](concepts/app-main-contract.md) | **`main.py` apenas**: config, raiz, PRD/TST, dry-run, start→core, finish, `--show` |
| [concepts/core-orquestracao.md](concepts/core-orquestracao.md) | Orquestrador em **`core`** (passos Sentinela: molde → verificar → mensagem → certificar → finalizar) |
| [concepts/integrations-execucao.md](concepts/integrations-execucao.md) | **`integrations`** — módulos que executam IO de facto |

### Outros conceitos (≤150 linhas)

| Ficheiro | Tema |
|----------|------|
| [concepts/filosofia-camadas.md](concepts/filosofia-camadas.md) | PEP 8, SOLID, fail fast |
| [concepts/estrutura-pastas-src-layout.md](concepts/estrutura-pastas-src-layout.md) | Árvore consolidada |
| [concepts/parametros-vs-segredos.md](concepts/parametros-vs-segredos.md) | YAML vs cofre |

### Padrões

| Ficheiro | Tema |
|----------|------|
| [patterns/yaml-multi-ambiente.md](patterns/yaml-multi-ambiente.md) | `dev/` / `prod/` |
| [patterns/ponto-unico-vault.md](patterns/ponto-unico-vault.md) | Facade única de secrets |

### Specs

| Ficheiro | Tema |
|----------|------|
| [specs/project-layout-example.yaml](specs/project-layout-example.yaml) | Manifesto da árvore |

---

## Referência rápida

- [quick-reference.md](quick-reference.md)

---

## Relação com **dev-python-automation**

[dev-python-automation](../dev-python-automation/index.md) cobre **como escrever** Python (PEP 8, Ruff, OOP no agente, DI, SQL). Esta KB define **onde** e **qual contrato de camada**.

---

## Agente **python-developer**

[python-developer](../../agents/code-quality/python-developer.md): estrutura obrigatória desta KB + **código orientado a objetos** (classes, métodos públicos/`_privados`, funções onde fizer sentido dentro desse modelo). Ao criar ficheiros, respeitar **`app` só `main.py`** e orquestração só em **`core`**.
