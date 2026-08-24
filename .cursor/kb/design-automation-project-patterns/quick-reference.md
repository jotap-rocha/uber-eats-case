# design-automation-project-patterns — referência rápida

> **MCP Validated:** 2026-05-07

## `src/app/` — só `main.py`

| Permitido | Proibido |
|-----------|----------|
| Ajustes de config, raiz do projeto (auto), inferência **PRD** vs **não-PRD** pelo path, **dry-run**, **`start`** → `core`, **finish**, **`--show`** | Orquestração de cargas, SQL, Teams, loops de negócio |

Detalhe: [app-main-contract.md](concepts/app-main-contract.md).

## `src/core/` — arquiteto

Orquestração em sequência (ex. Sentinela): molde mestre → verificar carga → mensagem → certificar cobertura → finalizar negócio. Sem drivers.

Detalhe: [core-orquestracao.md](concepts/core-orquestracao.md).

## `src/integrations/` — mão na massa

BD, messaging, cloud — classes que executam ações reais.

Detalhe: [integrations-execucao.md](concepts/integrations-execucao.md).

## Config vs secrets

| Tipo | Onde |
|------|------|
| Parâmetros por ambiente | `config/<env>/*.yaml` |
| Senhas | Facade em `integrations/cloud/` |

## Ligações

| Documento | Caminho |
|-----------|---------|
| Árvore | `concepts/estrutura-pastas-src-layout.md` |
| Código + OOP | [../dev-python-automation/quick-reference.md](../dev-python-automation/quick-reference.md) |
| Agente | [../../agents/code-quality/python-developer.md](../../agents/code-quality/python-developer.md) |
