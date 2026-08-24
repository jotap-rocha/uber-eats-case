# Layout `src/`, execução e organização do projeto

> **Propósito:** Código instalável, imports estáveis e entrypoints claros — sem gambiarras de `sys.path`.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

Adotar **layout `src/`** (`pyproject.toml` na raiz, pacote sob `src/`) garante que o código viva num **pacote importável**, alinhado a testes e a `pip install -e .`. O job não deve depender da pasta de trabalho atual para encontrar módulos via `sys.path.append`.

## Árvore orientativa (generalizável)

```text
projeto/
├── pyproject.toml
├── .venv/
├── src/
│   ├── app/           # entrypoints mínimos (CLI / __main__)
│   ├── jobs/        # orquestração por job ou tarefa agendada (opcional)
│   ├── core/        # regras de negócio e domínio partilhado (opcional)
│   └── utils/       # logging, conectores, helpers sem regra de negócio
└── tests/           # espelha estrutura ou agrupa por domínio
```

Para o **padrão completo** de automação — `config/dev|prod`, `integrations/` (database, cloud, messaging), **facade de cofre** e testes `unit`/`integration` — ver a KB **[design-automation-project-patterns](../../design-automation-project-patterns/concepts/estrutura-pastas-src-layout.md)**.

Nomes `jobs/` / `core/` são **sugestão**; o essencial é **separar** entrypoint, regras e infra (como em [solid-scripts.md](solid-scripts.md)).

## Regra de execução

| Preferir | Evitar |
|----------|--------|
| `python -m src.app.modulo_principal` (módulo qualificado; ex.: job **Sentinela** → `python -m src.app`) | `python caminho/aleatorio/script.py` que altera `sys.path` |
| `pip install -e .` em desenvolvimento | `sys.path.append("..")` ou manipulação manual de path para “encontrar” `src` |

Testes e CI devem usar o **mesmo** modelo de import que produção.

## Camadas (resumo)

1. **`app/`** — argumentos, config, `logging`, `SystemExit` / códigos de saída.
2. **`core/` / serviços** — fluxo e regras sem `pyodbc` direto.
3. **`utils/` ou `infra/`** — drivers, HTTP, ficheiros; mapear para tipos do domínio antes de subir.

## Relacionado

- [solid-scripts.md](solid-scripts.md)
- [logging-exit-codes.md](logging-exit-codes.md)
- [../patterns/injecao-dependencias.md](../patterns/injecao-dependencias.md)
- [../../design-automation-project-patterns/index.md](../../design-automation-project-patterns/index.md)
