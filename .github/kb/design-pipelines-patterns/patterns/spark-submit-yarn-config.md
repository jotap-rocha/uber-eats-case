# Padrão — `config/spark.conf` + spark-submit (YARN)

> **MCP Validated:** 2026-05-22

## When to Use

- Novo projeto PySpark em `workspace/prd/<projeto>/`
- Portar job legado com master Standalone fixo
- Alinhar DAG Airflow ao mesmo comando que desenvolvimento local

## Estrutura no repositório

```text
<projeto>/
├── config/
│   └── spark.conf          # propriedades Spark (versionado)
├── src/
│   ├── jobs/               # entrypoints spark-submit
│   └── utils/
│       └── spark_session.py   # getOrCreate() apenas
└── scripts/
    └── run-spark-job.sh    # opcional: atalho ao spark-submit
```

## Implementação

Ficheiro `config/spark.conf` (exemplo mínimo):

```properties
spark.master                      yarn
spark.submit.deployMode           client
spark.dynamicAllocation.enabled   true
spark.dynamicAllocation.maxExecutors  3
spark.executor.memory             2g
spark.sql.adaptive.enabled        true
spark.pyspark.python              /DATALAKE/opt/pyenv/versions/3.11.11/envs/<venv>/bin/python
spark.pyspark.driver.python       /DATALAKE/opt/pyenv/versions/3.11.11/envs/<venv>/bin/python
spark.jars                        /DATALAKE/opt/spark/jars/mssql-jdbc-12.6.3.jre11.jar
```

Execução:

```bash
/DATALAKE/opt/spark/bin/spark-submit --properties-file config/spark.conf src/jobs/meu_job.py
```

## See Also

- `.github/kb/migration-hub/spark/PADRAO-SPARK-SUBMIT-PROJETO-PRD.md`
- `.github/kb/migration-hub/spark/01-spark-3.5.2.md`
- [scaffold-projeto-dados.md](scaffold-projeto-dados.md)
