# Ambiente reproduzível

> **Purpose:** Mesmo código, mesmas dependências, mesmo resultado esperado.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

“Funciona na minha máquina” em dados costuma ser **versão de pandas/pyarrow**, libc ou drivers. Fixar dependências com **`pyproject.toml`** + lockfile (`uv`, Poetry, pip-tools) e alinhar **imagens Docker** ao runtime do cluster (Airflow worker, Spark executor Python) reduz surpresas.

## The Pattern

```toml
# pyproject.toml (exemplo mínimo)
[project]
name = "pipeline-x"
version = "0.1.0"
requires-python = ">=3.11,<3.13"
dependencies = [
  "pandas==2.2.*",
  "pyarrow==17.*",
]
```

Fluxo: `uv lock` ou `poetry lock` em CI; artefacto promovido para prod. Documentar **Python minor** e **glibc** quando há wheels nativos.

## Quick Reference

| Ferramenta | Papel |
|------------|--------|
| uv / Poetry / pip-tools | Lock transitivo reproduzível |
| Containers | Paridade com worker YARN/K8s |
| Constraints extras | `manylinux`, CUDA, JDK só quando aplicável |

## Common Mistakes

### Wrong

```text
pip install pandas pyarrow  # sem versões fixas em produção
```

### Correct

```text
uv sync --frozen  # ou pip install -r requirements.txt gerado com hashes
```

## Related

- [testing-pipelines](testing-pipelines.md)
- [pipeline-architecture](pipeline-architecture.md)
