# Estrutura de pastas consolidada (`src` layout)

> **Propósito:** Árvore de referência alinhada ao contrato **app = só main**, **core = orquestração**, **integrations = IO**.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

Código instalável sob **`src/`** como pacote top-level (`pyproject.toml` na raiz, `pip install -e .`). Detalhe **obrigatório** de cada camada:

| Pasta | Conteúdo permitido | Contrato |
|-------|-------------------|----------|
| **`src/app/`** | **Apenas `main.py`** | Ver [app-main-contract.md](app-main-contract.md) |
| **`src/core/`** | Orquestrador + domínio sem IO bruto | Ver [core-orquestracao.md](core-orquestracao.md) |
| **`src/integrations/`** | BD, messaging, cloud — execução real | Ver [integrations-execucao.md](integrations-execucao.md) |
| **`src/utils/`** | Helpers (ex.: `repo_root`), contratos partilhados | Sem regra de negócio Sentinela-specific |
| **`src/jobs/`** | Opcional; só se o projeto precisar de receitas **extra** — não substitui `core` |

## Árvore orientativa

```text
<projeto>/
├── pyproject.toml
├── config/{dev,prod}/...
├── src/
│   ├── __init__.py
│   ├── app/
│   │   └── main.py              # único módulo com lógica de bootstrap (ver contrato)
│   ├── core/
│   │   └── orchestrator.py      # exemplo — orquestração central
│   ├── integrations/
│   │   ├── cloud/
│   │   ├── database/
│   │   └── messaging/
│   └── utils/
└── tests/{unit,integration}/
```

`__main__.py` em `src/app/`, se existir, deve **só** delegar para `main()` sem lógica.

## Execução

`python -m src.app` após instalação editável — ver [estrutura-modulos-job](../../dev-python-automation/concepts/estrutura-modulos-job.md).

## Relacionado

- [filosofia-camadas.md](filosofia-camadas.md)
- [yaml-multi-ambiente.md](../patterns/yaml-multi-ambiente.md)
