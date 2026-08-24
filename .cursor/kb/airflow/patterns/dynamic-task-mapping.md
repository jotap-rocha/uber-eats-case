# Dynamic Task Mapping (`.expand`)

> **Problema:** dez tabelas semelhantes não devem exigir **dez DAGs** copy-paste.  
> **Solução:** uma lista de trabalhos e **`.expand()`** para criar **N instâncias de task** em paralelo (limitadas por `max_active_tasks` / pool / executor).

## Padrão com TaskFlow

```python
from airflow.decorators import dag, task

@dag(schedule="@daily", catchup=False, ...)
def sync_tables():
    @task
    def table_list() -> list[str]:
        return ["dbo.A", "dbo.B", "dbo.C"]

    @task
    def sync_one(table: str) -> str:
        # carga idempotente para `table`
        return f"ok:{table}"

    sync_one.expand(table=table_list())

sync_tables()
```

- **`expand`:** um parâmetro iterável → N tasks.  
- **`expand_kwargs`:** lista de dicts quando há vários parâmetros por instância.

## Combinação com pré-check / carga / pós-check

1. Task inicial devolve **lista de tabelas** (ou dicts com fonte/destino).  
2. **`load.expand`** (ou três fases: `pre.expand` → mapear para `load` → `post.expand`) mantendo **mesmo `logical date`** em todas as instâncias.

Cuidado: **explosão de paralelismo** — afinar `max_active_tasks` na DAG e recursos do **LocalExecutor** no **314**.

## Quando não usar

- Ordens **estritamente sequenciais** entre todas as tabelas com dependências arbitrárias (usar grafo explícito ou sub-DAGs).  
- Listas **enormes** sem paginação — prefira batches ou DAGs agendadas por “wave”.

## Relacionado

- [taskflow-api.md](../concepts/taskflow-api.md).  
- [pipeline-pre-check-load-post-check.md](pipeline-pre-check-load-post-check.md).
