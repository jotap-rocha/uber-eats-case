# Tipagem — fronteiras e APIs públicas

> **Propósito:** Falhar cedo em CLI, configuração e dados externos (DB, filas).
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-07

## Visão geral

Em jobs, bugs tardios vêm de **argv**, ficheiros de config ou **rows** tratados como `Any`. Além das **fronteiras**, o projeto deve exigir **type hints em todas as assinaturas públicas** (funções e métodos expostos a outros módulos): parâmetros e retorno explícitos. Módulos privados podem seguir política do *type checker* (`mypy` / `pyright` no `pyproject`).

Use **modelos validados** (ex.: pydantic) nas entradas — foco em **dicts estruturados**, **dataclasses** ou **TypedDict** para contratos claros sem assumir colunas de analytics.

## Padrão

```python
from pydantic import BaseModel, Field, PositiveInt


class DbJobSettings(BaseModel):
    server: str
    database: str
    command_timeout_s: PositiveInt = Field(default=30)


def load_settings(env_prefix: str = "JOB_") -> DbJobSettings:
    ...
```

```python
from typing import TypedDict


class PendingRow(TypedDict):
    id: int
    payload: str
```

## Referência rápida

| Fronteira | Abordagem |
|-----------|-----------|
| Flags CLI | `argparse` + tipos explícitos ou biblioteca tipada |
| Env | pydantic `BaseSettings` ou validação centralizada |
| Resultado de query | Converter para modelo/dataclass antes das regras |

## Erros comuns

### Errado

```python
def handle(row):
    send_email(row["emial"])
```

### Certo

```python
def handle(row: PendingRow) -> None:
    ...
```

## Relacionado

- [pep8-legibilidade.md](pep8-legibilidade.md)
- [sql-server-consultas-transacoes.md](sql-server-consultas-transacoes.md)
