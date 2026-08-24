# TaskFlow API (`@dag`, `@task`)

> **Propósito:** Escrever DAGs como **funções Python** com menos boilerplate e **XCom** tipado entre tasks.  
> **Alvo:** Airflow **≥ 2.11** (cluster com **2.11.1**).

## Porquê migrar do estilo clássico

| Clássico (`PythonOperator`) | TaskFlow |
|----------------------------|----------|
| Muitos `op_args` / kwargs opacos | Argumentos e retornos Python normais |
| XCom manual com chaves mágicas | Retorno da `@task` → input da seguinte |
| DAG longa e repetitiva | Leitura próxima de um script linear |

## Forma canónica

```python
from datetime import datetime
from airflow.decorators import dag, task
from airflow.operators.python import get_current_context

@dag(
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["example"],
)
def spark_pipeline_automation():
    @task
    def prepare_spark_conf() -> str:
        return "--conf spark.executor.memory=4g"

    @task
    def build_paths() -> dict:
        ctx = get_current_context()
        ds = ctx["ds"]
        return {"raw": f"/data/raw/dt={ds}", "curated": f"/data/cur/dt={ds}"}

    conf = prepare_spark_conf()
    paths = build_paths()
    conf >> paths

spark_pipeline_automation()
```

Instanciar no final (`spark_pipeline_automation()`) regista a DAG.

## Sensores e espera por dados

O exemplo com **`@task.sensor`** depende de **API exacta** da tua versão (sensores TaskFlow evoluem entre minors). Regras seguras:

1. **Deferrable sensors** (`PythonSensor`, `BlobSensor`, etc.) como operators no grafo TaskFlow — continuam a compor com `>>`.
2. **`@task`** que valida pré-condição (ex.: ficheiro existe) com **retries** curtos — simples e testável.
3. Consultar a doc **2.11.x** do projeto para *decorators* de sensor quando estiverem estáveis no teu pin.

Evitar sensores bloqueantes sem *deferrable* em DAGs com muita concorrência no **LocalExecutor**.

## Boas práticas

- **Uma responsabilidade** por `@task` (alinhado ao pattern de pré-check / carga / pós-check).
- **Tipagem** nos retornos (`-> dict`, `-> str`) para legibilidade e testes.
- **Operadores pesados** (`SparkSubmitOperator`, etc.): TaskFlow pode **invocá-los** dentro de uma `@task` ou mantê-los como nós explícitos ligados ao grafo TaskFlow.

## Relacionado

- [idempotencia-macros-templates.md](idempotencia-macros-templates.md) — `ds` e re-execução.  
- [../patterns/pipeline-pre-check-load-post-check.md](../patterns/pipeline-pre-check-load-post-check.md) — fases da carga.
