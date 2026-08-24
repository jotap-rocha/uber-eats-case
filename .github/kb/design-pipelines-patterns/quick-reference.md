# design-pipelines-patterns — referência rápida

> **MCP Validated:** 2026-05-15

## Árvore obrigatória (resumo)

| Pasta / ficheiro | Papel |
|------------------|--------|
| `logs/` | Logs centralizados |
| `config/config.yaml` | Parâmetros por ambiente (sem segredos) |
| `data/raw`, `data/processed` | Input de teste partilhado |
| `docs/README.md` | Arquitetura e guias |
| `etl/extract|transform|load` | ETL desacoplado (`extract_data.py`, etc.) |
| `pipelines/` | Orquestração (`pipeline_source_*.py`) |
| `src/data|utils|validation|contracts` | Partilhado; **`logger.py` e `key_oci.py` obrigatórios** |
| `tests/unit|integrated|system` | Pirâmide de testes |
| `sql/*.sql` | Queries versionadas |
| Raiz | `.gitignore`, `environment.yaml`, `.config`, `.python_version`, `pyproject.toml`, `README.md` |

## Convenção Python

| Escrito informalmente | Usar no repo |
|----------------------|--------------|
| `init.py` | `__init__.py` |

## Decision Matrix

| Use case | Onde colocar |
|----------|----------------|
| Nova query de extração | `sql/` + chamada em `etl/extract/` |
| Ordem dos passos muda | `pipelines/` apenas |
| Regra de qualidade reutilizável | `src/validation/` |
| Schema de saída da fonte N | `src/contracts/source_contract_N.py` |

## Common Pitfalls

| Don't | Do |
|-------|-----|
| Segredos no YAML commitado | Vault via `key_oci.py` + `.config` |
| Lógica de negócio só em notebooks | `etl/transform` + testes |
| Um único ficheiro “god” para tudo | Separar `etl` vs `pipelines` |

## Related Documentation

| Topic | Path |
|-------|------|
| Manifesto máquina | `specs/project-layout-mandatory.yaml` |
| Índice KB | `index.md` |
| Engenharia Python dados | `../dev-python-engineering/index.md` |
