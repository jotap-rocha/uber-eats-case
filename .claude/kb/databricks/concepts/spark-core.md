# Spark Core Concepts

> **Purpose**: Master Apache Spark fundamentals — SparkSession, DataFrame API, lazy evaluation, execution model, and common operations
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Apache Spark is a distributed computing engine for large-scale data processing. Databricks is built on Spark and adds optimizations (Photon, AQE, Delta Lake). Spark uses lazy evaluation — transformations build a logical plan (DAG), and actions trigger physical execution across a cluster.

## SparkSession Creation

```python
# In Databricks notebooks — SparkSession is pre-created as `spark`
spark  # already available — no need to create

# Outside Databricks (local dev / Databricks Connect)
from pyspark.sql import SparkSession

spark = (SparkSession.builder
    .appName("MyApp")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate())
```

## DataFrame API vs SQL

```python
# DataFrame API — programmatic, composable, type-aware
result = (df
    .filter("status = 'active'")
    .groupBy("country")
    .agg({"revenue": "sum"})
    .orderBy("sum(revenue)", ascending=False))

# SQL — readable, familiar, great for ad-hoc
spark.sql("""
    SELECT country, SUM(revenue) AS total_revenue
    FROM catalog.schema.orders
    WHERE status = 'active'
    GROUP BY country
    ORDER BY total_revenue DESC
""")

# Mixed — register temp view, then query
df.createOrReplaceTempView("orders_view")
spark.sql("SELECT * FROM orders_view WHERE amount > 1000")
```

**Rule:** DataFrame API for programmatic pipelines; SQL for exploration and when working with analysts.

## Lazy Evaluation: Transformations vs Actions

```python
# TRANSFORMATIONS — lazy, build DAG (no execution)
df2 = df.filter("age > 18")        # filter
df3 = df2.select("name", "email")  # projection
df4 = df3.withColumn("upper_name", upper(col("name")))  # derived column
df5 = df4.join(other_df, "id")     # shuffle join

# ACTIONS — trigger execution
df5.count()           # returns Int
df5.collect()         # returns List[Row] — avoid on large datasets
df5.show(20)          # prints to notebook
df5.write.save(...)   # write to storage
df5.first()           # returns first Row
```

## Execution Model: DAG → Stages → Tasks

```text
Action triggered
  └── Spark builds Physical Plan (DAG)
        └── DAG splits into Stages (separated by shuffles)
              └── Each Stage splits into Tasks
                    └── Tasks run on Executors (1 task per partition)

Shuffle = data movement across network (expensive)
         Triggered by: groupBy, join, orderBy, distinct
```

## Schema: Inference vs Explicit

```python
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType

# Schema inference — convenient but slow on CSV/JSON (requires scan)
df = spark.read.option("inferSchema", "true").csv("/path/data.csv")

# Explicit schema — RECOMMENDED for production
schema = StructType([
    StructField("id",       IntegerType(), nullable=False),
    StructField("name",     StringType(),  nullable=True),
    StructField("amount",   DoubleType(),  nullable=True),
    StructField("event_ts", StringType(),  nullable=True),
])
df = spark.read.schema(schema).csv("/Volumes/catalog/schema/vol/data.csv")
```

## Common DataFrame Operations

Agregações, *window functions*, *joins* e operações frequentes — ver:

- [spark-core-dataframe-operations.md](spark-core-dataframe-operations.md)

## Common Mistakes

### Wrong
```python
# Collecting large DataFrame to driver — OOM risk
all_rows = big_df.collect()
for row in all_rows:
    process(row)
```

### Correct
```python
# Use Spark transformations — stay distributed
result = big_df.groupBy("key").agg(_sum("value"))
result.write.format("delta").save("/path/output")
```

## Related

- [concepts/delta-lake.md](delta-lake.md)
- [patterns/etl-pipeline.md](../patterns/etl-pipeline.md)
- [patterns/spark-optimization.md](../patterns/spark-optimization.md)
