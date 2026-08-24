# Módulos Python legíveis (alinhado python-developer)

> **Purpose:** Código de dados fácil de manter: tipos, estruturas imutáveis e fluxos claros.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

O agente **python-developer** recomenda **dataclasses** `frozen` para registros, **generators** para parsing/streaming, **type hints** em APIs públicas e **logging** em vez de `print`. Isso combina com pipelines grandes: menos estado mutável implícito e consumo de memória previsível.

## The Pattern

```python
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
import logging


logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class Row:
    id: int
    amount: float


def iter_rows(path: Path) -> Iterator[Row]:
    with path.open() as f:
        for line_no, line in enumerate(f, 1):
            try:
                yield parse_line(line)
            except ValueError:
                logger.warning("skip_bad_line", extra={"line": line_no})
```

Handlers por tipo de linha em **registo** (`dict[str, Callable]`) mantêm extensibilidade sem `if` gigantes.

## Quick Reference

| Tema | Orientação |
|------|------------|
| Modelos | `@dataclass(frozen=True)` para linhas de negócio |
| Streams | `yield` / iteradores em vez de listas gigantes |
| Saída operacional | `logging` com `extra` estruturado |
| Estilo | Evitar comentários que só repetem o código; nomes claros |

## Common Mistakes

### Wrong

```python
def load(path):
    print("loading")
    rows = []
    for line in open(path):
        rows.append(parse(line))
    return rows  # materializa tudo
```

### Correct

```python
def load(path: Path) -> Iterator[Row]:
    logger.info("loading", extra={"path": str(path)})
    yield from iter_rows(path)
```

## Related

- [memory-dtypes](memory-dtypes.md)
- [pipeline-architecture](pipeline-architecture.md)
- [../../../agents/code-quality/python-developer.md](../../../agents/code-quality/python-developer.md)
