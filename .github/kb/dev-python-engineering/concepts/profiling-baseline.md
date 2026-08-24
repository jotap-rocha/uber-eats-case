# Baseline e profiling

> **Purpose:** Decidir otimizações com medição, não intuição.
> **Confidence:** 0.95
> **MCP Validated:** 2026-05-06

## Overview

Em workloads de dados, o gargalo costuma ser I/O, joins mal pensados ou operações Python por linha — não a “micro-otimização” de uma função irrelevante. Um **baseline** (tempo, CPU, memória, linhas processadas) antes da mudança permite provar ganho e evitar regressões.

## The Pattern

```python
import cProfile
import pstats
from pstats import SortKey


def main() -> None:
    ...


if __name__ == "__main__":
    profiler = cProfile.Profile()
    profiler.enable()
    main()
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats(SortKey.CUMULATIVE)
    stats.print_stats(40)
```

Para linhas específicas: decorador `@profile` do `line_profiler` (`kernprof -l -v script.py`). Para produção: `py-spy record --pid …` (amostragem, baixo overhead).

## Quick Reference

| Situação | Ferramenta | Notas |
|----------|------------|--------|
| Primeira triagem | `cProfile` | Cumulative time mostra suspeitos |
| Função denunciada pelo perfil | `line_profiler` | Confirma ramos caros |
| Job já em execução | `py-spy` | Sem reiniciar com instrumentação pesada |

## Common Mistakes

### Wrong

```python
# Reescrita “mais rápida” sem medir o job completo
def transform(df):
    return df.apply(lambda r: expensive(r), axis=1)  # frequentemente péssimo
```

### Correct

```python
# Medir o pipeline com dados representativos; depois trocar por vetorização/API nativa
def transform(df):
    return df.assign(out=native_vectorized_expr(df))
```

## Related

- [vectorized-operations](vectorized-operations.md)
- [io-columnar](io-columnar.md)
- [../patterns/profiling-workflow.md](../patterns/profiling-workflow.md)
