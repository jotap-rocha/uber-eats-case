# Spark Core — operações comuns em DataFrame

> **Purpose**: Extensão de [spark-core.md](spark-core.md) — filtros, agregações, *window functions* e *joins*.  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Common DataFrame Operations

```python
from pyspark.sql.functions import col, lit, when, coalesce, to_date, year, month
from pyspark.sql.functions import sum as _sum, count, avg, max as _max
from pyspark.sql.window import Window
import pyspark.sql.functions as F

# Filter + Select
df = df.filter(col("status").isin(["active", "pending"])) \
       .select("id", "name", col("amount").alias("revenue"))

# Derived columns
df = df.withColumn("year", year(to_date(col("event_ts")))) \
       .withColumn("category", when(col("amount") > 1000, "high").otherwise("low")) \
       .withColumn("filled_name", coalesce(col("name"), lit("unknown")))

# Aggregations
agg_df = df.groupBy("category", "year").agg(
    _sum("revenue").alias("total_revenue"),
    count("*").alias("num_events"),
    avg("revenue").alias("avg_revenue"),
)

# Window functions
window_spec = Window.partitionBy("category").orderBy(col("event_ts").desc())
df = df.withColumn("rank", F.rank().over(window_spec)) \
       .withColumn("running_total", F.sum("revenue").over(
           window_spec.rowsBetween(Window.unboundedPreceding, Window.currentRow)))

# Joins
joined = orders.join(customers, orders.customer_id == customers.id, "left")
```

## Related

- [spark-core.md](spark-core.md)
- [patterns/etl-pipeline-windows-udfs.md](../patterns/etl-pipeline-windows-udfs.md)
