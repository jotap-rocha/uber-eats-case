# Idempotência, macros e templates

> **Regra de ouro:** executar **várias vezes** o mesmo período lógico deve produzir o **mesmo estado final** (sem duplicar dados nem corromper partições).

## Armadilhas comuns

| Armadilha | Porquê falha no re-run / backfill |
|-----------|-----------------------------------|
| `datetime.now()` / “hoje” em SQL ou paths | Reprocessar **ontem** escreve dados de **hoje** |
| `INSERT INTO` acumulativo sem chave | Duplicados a cada retry |
| Apagar ficheiros “à mão” antes de saber que a task terminou | Estado inconsistente se a task falhar a meio |

## Macros e contexto de execução

Usar **data da execução lógica**, não o relógio da máquina:

| Mecanismo | Uso típico |
|-----------|------------|
| `{{ ds }}` | Partição diária em templates Bash/Jinja |
| `{{ data_interval_start }}` | Início do intervalo (Airflow 2.2+) |
| `logical_date` / `context` em `@task` | Passar `**context` ou `pendulum` explícito quando necessário |

Exemplo de path particionado (template):

```text
/abfs/container/curated/table/dt={{ ds }}/
```

## Padrões idempotentes

- **Overwrite de partição:** para `dt={{ ds }}`, re-escrever só essa pasta/partição (Spark `overwrite`, `INSERT OVERWRITE`, equivalente em lakehouse).
- **Merge com chave de negócio:** `MERGE` / `UPSERT` determinístico em vez de append cego.
- **Retries seguros:** só depois de operações que podem repetir sem efeito colateral (por isso overwrite > append incremental sem dedupe).

## Relação com TaskFlow

Tasks que recebem `ds` como argumento devem obtê-lo via **template** (`op_args`) ou **`.expand`** sobre datas explícitas — nunca `datetime.now()` dentro da lógica que define **o que** ler/escrever.

## Relacionado

- [pipeline-pre-check-load-post-check.md](../patterns/pipeline-pre-check-load-post-check.md) — pré/pós-check por `logical date`.  
- [quick-reference.md](../quick-reference.md).
