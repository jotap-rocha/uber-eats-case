# Árvore de pastas obrigatória (raiz)

> **Propósito:** Definir o **contrato de layout** na raiz de um repositório Python de **dados** (pipelines, ETL, multi-fonte).
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-15

## Overview

A raiz deve conter **sempre** as pastas e ficheiros listados na KB e no manifesto [specs/project-layout-mandatory.yaml](../specs/project-layout-mandatory.yaml). Em Python, cada diretório importável usa **`__init__.py`** (o termo informal “init.py” refere-se a este ficheiro).

## Obrigatório na raiz

| Item | Função |
|------|--------|
| `logs/` | Destino único para ficheiros de log da aplicação e jobs |
| `config/` + `config.yaml` | Parâmetros de ligação e ambiente **sem** segredos no YAML |
| `data/raw/`, `data/processed/` | Dados locais de teste; alinhar pipelines ao mesmo input |
| `docs/` + `docs/README.md` | Decisões de arquitetura e guias para a equipa |
| `etl/extract|transform|load/` | Uma responsabilidade por fase; módulos testáveis |
| `pipelines/` | Orquestração: compõe ETL + contratos + I/O |
| `src/` | Código partilhado: `data/`, `utils/`, `validation/`, `contracts/` |
| `tests/unit|integrated|system/` | Pirâmide de testes alinhada ao pipeline |
| `sql/` | `.sql` versionados (ex.: `extract_source_1.sql`) |
| `.gitignore`, `environment.yaml`, `.config`, `.python_version`, `pyproject.toml`, `README.md` | Reprodutibilidade, segredos via Vault OCI, empacotamento |

## Segredos vs configuração

- **`config/config.yaml`**: hosts, nomes de recursos, flags de ambiente — **não** colocar passwords/tokens.
- **`.config`**: referência ao **OCI Vault** (ex.: OCIDs por ambiente), consumido tipicamente via `src/utils/key_oci.py`.

## Erro comum

Fundir extração pesada e orquestração no mesmo módulo. **Correto:** `etl/*` implementa passos atómicos; `pipelines/*` só encadeia e configura agendamento/argumentos.

## Related

- [separacao-etl-vs-pipelines.md](separacao-etl-vs-pipelines.md)
- [config-sql-secrets.md](config-sql-secrets.md)
- [../patterns/scaffold-projeto-dados.md](../patterns/scaffold-projeto-dados.md)
