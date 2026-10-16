---
domain: spark
description: Apache Spark — modelo de execução distribuída, DataFrame/RDD/SQL, lazy evaluation, tuning de cluster
mcp_validated: null
confidence: null
---

# KB: Apache Spark

Base de conhecimento de Apache Spark para engenharia de dados distribuída: modelo de execução,
otimização de joins, particionamento e tuning de cluster. Princípio central: **entender o plano
de execução antes de otimizar** — a maioria dos problemas de performance em Spark é join mal
escolhido, skew não tratado, ou configuração de executor genérica demais para a carga real.

## Conformidade DE (ponte)

Fonte: `data-engineering.yaml` — este KB **não** duplica severidade nem texto normativo.

| Âncora | Relação |
|---|---|
| `DE-A*` | Universal |
| pacote **B** (`DE-B*`) | jobs Spark / YARN |

## Conceitos

| Arquivo | Tópico |
|---|---|
| [execution-model.md](concepts/execution-model.md) | Partições, stages, shuffle — como o Spark distribui trabalho |
| [dataframe-vs-rdd-vs-sql.md](concepts/dataframe-vs-rdd-vs-sql.md) | Quando usar cada API, Catalyst optimizer, Tungsten |
| [lazy-evaluation.md](concepts/lazy-evaluation.md) | Transformações vs ações, logical/physical plan, `explain()` |
| [memory-management.md](concepts/memory-management.md) | Unified memory (storage vs execution), spill para disco |

## Padrões

| Arquivo | Tópico |
|---|---|
| [join-optimization.md](patterns/join-optimization.md) | Broadcast join vs shuffle (sort-merge) join, quando forçar cada um |
| [partitioning-skew.md](patterns/partitioning-skew.md) | `repartition`/`coalesce`, salting, AQE skew join |
| [pyspark-idioms.md](patterns/pyspark-idioms.md) | Transformações idiomáticas, o que evitar (UDF, `collect()`, loops) |
| [cluster-tuning.md](patterns/cluster-tuning.md) | executor cores/memory, `spark.sql.shuffle.partitions`, AQE |

## Quick Reference

Ver [quick-reference.md](quick-reference.md) — cheatsheet de configs, decision tree de join e
checklist de diagnóstico de skew. Ler só se a tarefa exigir esse nível de detalhe operacional.

## Nota de validação

Este domínio foi criado **sem acesso ao Context-7 MCP** nesta sessão (ferramenta não disponível
no ambiente de execução). O conteúdo reflete conhecimento estável e amplamente documentado do
Spark (APIs e comportamento de execução não mudam com frequência entre minor versions), mas
`mcp_validated`/`confidence` ficam `null` até uma auditoria real via Context-7 — não invente
esses valores. Rode o Modo 2 (auditoria) deste skill assim que o MCP estiver disponível.

## Conteudo adicional do projeto

Arquivos mantidos de versoes anteriores desta KB (nao listados acima):

- [README.md](README.md)
- `01-quick-start/` (1 arquivos), ex.: [01-quick-start/quick-start.md](01-quick-start/quick-start.md)
- `02-rdd-accumulators-broadcasts-vars/` (1 arquivos), ex.: [02-rdd-accumulators-broadcasts-vars/rdd-accumulators-broadcasts-vars.md](02-rdd-accumulators-broadcasts-vars/rdd-accumulators-broadcasts-vars.md)
- `03-sql-dataframes-datasets/` (1 arquivos), ex.: [03-sql-dataframes-datasets/sql-dataframes-datasets.md](03-sql-dataframes-datasets/sql-dataframes-datasets.md)
- `04-structured-streaming/` (10 arquivos), ex.: [04-structured-streaming/img/async-progress.png](04-structured-streaming/img/async-progress.png)
- `05-spark-streaming-guide/` (3 arquivos), ex.: [05-spark-streaming-guide/img/streaming-arch.png](05-spark-streaming-guide/img/streaming-arch.png)
- `06-pyspark-quickstart/` (3 arquivos), ex.: [06-pyspark-quickstart/01-quickstart-dataframe.md](06-pyspark-quickstart/01-quickstart-dataframe.md)
- `07-spark-sql/` (4 arquivos), ex.: [07-spark-sql/01-spark-sql-apachearrow.md](07-spark-sql/01-spark-sql-apachearrow.md)
- `08-spark-pandas-api-on-spark/` (9 arquivos), ex.: [08-spark-pandas-api-on-spark/01-spark-pandas-options-settings.md](08-spark-pandas-api-on-spark/01-spark-pandas-options-settings.md)
- `09-spark-user-guide/` (7 arquivos), ex.: [09-spark-user-guide/chapter01-dataframes.md](09-spark-user-guide/chapter01-dataframes.md)
- `10-spark-api-reference/` (20 arquivos), ex.: [10-spark-api-reference/01-spark-sql-core-concepts.md](10-spark-api-reference/01-spark-sql-core-concepts.md)
- `11-pandas-api-on-spark/` (12 arquivos), ex.: [11-pandas-api-on-spark/01-pandas-api-on-spark-input-output.md](11-pandas-api-on-spark/01-pandas-api-on-spark-input-output.md)
- `12-spark-core/` (1 arquivos), ex.: [12-spark-core/01-spark-core.md](12-spark-core/01-spark-core.md)
- `13-spark-resource-management/` (1 arquivos), ex.: [13-spark-resource-management/01-spark-resource-management.md](13-spark-resource-management/01-spark-resource-management.md)
- `14-spark-errors/` (1 arquivos), ex.: [14-spark-errors/01-spark-errors.md](14-spark-errors/01-spark-errors.md)
- `15-spark-logger/` (1 arquivos), ex.: [15-spark-logger/01-spark-logger.md](15-spark-logger/01-spark-logger.md)
- `16-spark-testing/` (1 arquivos), ex.: [16-spark-testing/01-spark-testing.md](16-spark-testing/01-spark-testing.md)
