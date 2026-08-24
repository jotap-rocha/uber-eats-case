# Módulos partilhados em `src/`

> **Propósito:** Papéis de `src/data`, `src/utils`, `src/validation`, `src/contracts`.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-15

## Overview

`src/` concentra lógica **reutilizável** entre pipelines. `etl/` e `pipelines/` importam daqui; evita duplicação entre fontes.

## Papéis

| Pasta | Conteúdo típico |
|-------|-----------------|
| `src/data/data_processing.py` | Funções/classes de limpeza e transformações **genéricas** (não específicas de uma única fonte, quando possível) |
| `src/utils/logger.py` | **Obrigatório** — configuração de logging (handlers para `logs/`, formato, níveis) |
| `src/utils/key_oci.py` | **Obrigatório** — integração OCI Vault / leitura de `.config` |
| `src/validation/data_validation.py` | Checks de qualidade (nulls, ranges, keys) |
| `src/contracts/source_contract_1.py` | Schema esperado (tipos, colunas) da fonte 1 |

## Quick Reference

| Input | Output | Notes |
|-------|--------|-------|
| Nova fonte | `contracts/source_contract_N.py` + testes | Alinhar com `sql/extract_source_N.sql` |
| Novo sink | reutilizar `load` + validação pós-carga | Validar contagens e checksums |

## Common Mistakes

### Wrong

Colocar `logger` ou Vault só dentro de um pipeline — outros jobs ficam inconsistentes.

### Correct

Todo o projeto importa o mesmo `get_logger()` e a mesma facade de secrets.

## Related

- [config-sql-secrets.md](config-sql-secrets.md)
- [../../dev-python-engineering/patterns/schema-boundary.md](../../dev-python-engineering/patterns/schema-boundary.md)
