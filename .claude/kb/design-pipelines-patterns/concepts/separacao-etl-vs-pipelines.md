# Separação ETL vs pipelines

> **Propósito:** Clarificar **camada de implementação** (`etl/`) vs **camada de orquestração** (`pipelines/`).
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-15

## Overview

`etl/` contém **fases reutilizáveis** com interfaces estáveis (extract → transform → load). `pipelines/` define **fluxos concretos** por fonte ou produto de dados: ordem dos passos, caminhos de ficheiros, escolha de contratos e queries SQL.

## O Pattern

| Camada | Responsabilidade | Exemplo |
|--------|------------------|---------|
| `etl/extract/extract_data.py` | Ler fonte A ou B via parâmetros; devolver estrutura em memória ou caminho intermédio | Cliente API, leitura de ficheiro, execução de `sql/` |
| `etl/transform/transform_data.py` | Regras de negócio e limpeza **sem** saber o cron | Normalização, joins em memória |
| `etl/load/load_data.py` | Escrita idempotente ou append controlado | Bulk insert, merge |
| `pipelines/pipeline_source_1.py` | Instanciar classes, injectar config, encadear ETL, logging | `PipelineSource1().run()` |

## Quick Reference

| Input | Output | Notes |
|-------|--------|-------|
| Novo conector | Novo código principalmente em `etl/extract` + `sql/` | Pipeline só referencia o novo passo |
| Nova regra de qualidade | `src/validation/data_validation.py` + testes | Contratos em `src/contracts/` se mudar schema |

## Common Mistakes

### Wrong

Orquestração com `subprocess` espalhada por `etl/` — mistura **como** com **o quê**.

### Correct

`pipelines/` chama APIs públicas dos módulos ETL (classes/métodos). Agendadores externos invocam `python -m pipelines.pipeline_source_1` ou entrypoint no `pyproject.toml`.

## Related

- [obrigatoriedade-arvore.md](obrigatoriedade-arvore.md)
- [../dev-python-engineering/concepts/pipeline-architecture.md](../../dev-python-engineering/concepts/pipeline-architecture.md)
