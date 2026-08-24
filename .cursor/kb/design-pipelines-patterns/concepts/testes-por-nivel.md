# Testes por nível (`tests/`)

> **Propósito:** Mapear `unit/`, `integrated/`, `system/` à pirâmide de testes do pipeline.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-15

## Overview

Cada nível tem **ficheiros obrigatórios** na árvore (`__init__.py` + módulo exemplo). Amplie com `test_*.py` conforme o runner (pytest) do projeto.

## Níveis

| Pasta | Âmbito | Exemplo neste layout |
|-------|--------|----------------------|
| `tests/unit/` | Unidades isoladas, mocks de IO | `connection_database.py` — factory de conexão mockada |
| `tests/integrated/` | ETL com dependências reais ou containers | `etl.py` — extract→transform→load com `data/raw/` |
| `tests/system/` | Pipeline completo como em produção (ou ambiente de staging) | `pipeline_source_1.py` — invoca o mesmo entrypoint que o job |

## Quick Reference

| Input | Output | Notes |
|-------|--------|-------|
| Bug em transform | teste em `unit` ou `integrated` | Preferir dados mínimos em `data/raw/` |
| Regressão de agendamento | teste em `system` | Pode ser marcado como lento (`pytest -m slow`) |

## Common Mistakes

### Wrong

Apenas testes manuais em notebook sem pasta `tests/`.

### Correct

CI executa `pytest tests/`; notebooks em `docs/` ou fora do caminho crítico de release.

## Related

- [separacao-etl-vs-pipelines.md](separacao-etl-vs-pipelines.md)
- [../../dev-python-engineering/concepts/testing-pipelines.md](../../dev-python-engineering/concepts/testing-pipelines.md)
