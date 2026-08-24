# Padrão — spark-submit em projetos `workspace/prd`

> **MCP Validated:** 2026-05-22  
> **Referência viva:** `workspace/prd/data-onu-project/config/spark.conf`

## Resumo

Jobs PySpark em **`/DATALAKE/workspace/prd/<projeto>/`** executam com **`spark-submit`** e propriedades num ficheiro versionado **`config/spark.conf`** (formato nativo Spark). **YARN** agenda capacidade; o projeto **não** fixa `spark.executor.instances`.

## Comando canónico

```bash
cd /DATALAKE/workspace/prd/<projeto>
/DATALAKE/opt/spark/bin/spark-submit \
  --properties-file config/spark.conf \
  src/jobs/<job>.py
```

## Onde ficam as configurações

| Artefacto | Função |
|-----------|--------|
| **`config/spark.conf`** | Propriedades do **projeto** (memória por container, dynamic allocation, pyspark.python, spark.jars) |
| `/DATALAKE/opt/spark/conf/spark-defaults.conf` | Defaults do **cluster** (`spark.master yarn`, deploy client) |
| `/DATALAKE/opt/spark/conf/spark-env.sh` | `HADOOP_CONF_DIR`, `YARN_CONF_DIR`, `JAVA_HOME` |

**Não** usar `export SPARK_MASTER=...` no dia a dia do projeto — salvo override pontual no shell.

## Recursos: YARN + Dynamic Allocation

| Fazer | Não fazer |
|-------|-----------|
| `spark.dynamicAllocation.enabled=true` | `spark.executor.instances=N` fixo |
| `maxExecutors` alinhado aos NM (ex.: **3** para 312/313/314) | `spark.cores.max` (standalone) |
| `spark.executor.memory` = pedido **por container** | `spark.default.parallelism` / `shuffle.partitions` fixos altos |
| `spark.sql.adaptive.enabled=true` | Master `spark://host:7077` legado |

KB cluster: `migration-hub/architecture.md`, `migration-hub/planning.md`.

**Piloto validado (variante com `.venv` do projeto + JARs JDBC):** [`../migration/patterns/sql-capacity-yarn-prd-piloto.md`](../migration/patterns/sql-capacity-yarn-prd-piloto.md) — `data-sql-capacity-evolution-prd`, Job 08.

## Código Python do job

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
```

Sem `.master("spark://...")` nem blocos de memória duplicados no Python — tudo em `config/spark.conf`.

## Airflow (`/DATALAKE/dags`)

`BashOperator` com o **mesmo** `spark-submit` (stdout/stderr na UI):

```bash
set -euo pipefail
cd /DATALAKE/workspace/prd/<projeto>
/DATALAKE/opt/spark/bin/spark-submit --properties-file config/spark.conf src/jobs/<job>.py
```

## Layout do projeto (complemento)

Ver `.cursor/kb/design-pipelines-patterns/patterns/spark-submit-yarn-config.md` — pasta `config/` na árvore obrigatória.

## Anti-padrões

- Standalone `islnx011:7077` ou IPs legados no código
- Wrapper `.sh` como única forma de passar env (preferir `spark.conf`)
- `python job.py` sem `spark-submit` quando o job usa `SparkSession` em cluster YARN (driver precisa do classpath Spark do cluster)
