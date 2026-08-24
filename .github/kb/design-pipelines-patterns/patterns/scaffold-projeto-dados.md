# Scaffold de projeto de dados

> **Propósito:** Como **criar** ou **validar** um repositório que segue a árvore obrigatória.
> **MCP Validated:** 2026-05-15

## When to Use

- Novo repositório de ingestão / ETL / cargas BI.
- Refactor de um monólito para camadas ETL + pipelines.
- Code review de estrutura de pastas.

## Implementation

1. Copiar a árvore de [specs/project-layout-mandatory.yaml](../specs/project-layout-mandatory.yaml).
2. Garantir `pyproject.toml` com:
   - `[tool.pytest.ini_options]` `testpaths = ["tests"]`
   - opcional: `[project.scripts]` apontando para funções `main` em `pipelines/`.
3. Em cada pasta Python na raiz (`etl`, `pipelines`), manter `__init__.py` vazio ou com `__all__` mínimo.
4. `src/utils/logger.py`: configurar logger raiz ou `logging.getLogger(__name__)` com handler para `logs/app.log` (criar diretório em runtime se necessário).
5. `src/utils/key_oci.py`: ler `.config`, obter segredos do Vault, **nunca** logar valores sensíveis.

```python
# pipelines/pipeline_source_1.py (esqueleto ilustrativo)
from __future__ import annotations

import logging

from etl.extract import extract_data
from etl.load import load_data
from etl.transform import transform_data
from src.utils.logger import get_logger

log = get_logger(__name__)


class PipelineSource1:
    def run(self) -> None:
        log.info("start pipeline_source_1")
        raw = extract_data.run()
        clean = transform_data.run(raw)
        load_data.run(clean)
        log.info("done pipeline_source_1")


def main() -> None:
    PipelineSource1().run()
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `LOG_DIR` | `logs/` | Pode ser variável de ambiente para containers |
| `CONFIG_PATH` | `config/config.yaml` | Override em testes |

## Melhorias opcionais (não substituem o obrigatório)

| Sugestão | Motivo |
|----------|--------|
| `Makefile` ou `invoke`/`taskipy` | Comandos padronizados: `lint`, `test`, `pipeline` |
| `pre-commit` + Ruff | Mesma linha que [dev-python-engineering](../../dev-python-engineering/index.md) |
| Marcadores pytest `slow` / `integration` | CI rápido no PR; noite completo em `system` |
| `docs/diagrams/` (Mermaid exportado) | Arquitetura visível em PRs |
| Pastas `data/**` no `.gitignore` exceto amostras | Evitar commit acidental de volumes grandes |

## Example Usage

```bash
conda env create -f environment.yaml
pytest tests/unit -q
python -m pipelines.pipeline_source_1
```

## See Also

- [../concepts/obrigatoriedade-arvore.md](../concepts/obrigatoriedade-arvore.md)
- [../concepts/separacao-etl-vs-pipelines.md](../concepts/separacao-etl-vs-pipelines.md)
- [../../dev-python-engineering/concepts/reproducible-environment.md](../../dev-python-engineering/concepts/reproducible-environment.md)
