# Spark optimization — skew, clustering e pushdown

> **Purpose**: Continuação de [spark-optimization.md](spark-optimization.md).  
> **MCP Validated**: 2026-04-20

## Data Skew: Salting Technique

```python
from pyspark.sql.functions import col, concat, lit, rand, floor, explode, array

num_salt_buckets = 10
large_skewed = df_large.withColumn(
    "salted_key",
    concat(col("customer_id"), lit("_"), (floor(rand() * num_salt_buckets)).cast("string")),
)
salt_array = array([lit(str(i)) for i in range(num_salt_buckets)])
small_exploded = df_small.withColumn("salt", explode(salt_array)).withColumn(
    "salted_key", concat(col("customer_id"), lit("_"), col("salt")),
)
result = large_skewed.join(small_exploded, "salted_key").drop("salted_key", "salt")
```

## Z-Ordering vs Liquid Clustering

```sql
OPTIMIZE prod_catalog.sales.orders ZORDER BY (customer_id, order_date);
CREATE TABLE prod_catalog.silver.orders CLUSTER BY (customer_id, order_date) USING DELTA;
ALTER TABLE prod_catalog.silver.orders CLUSTER BY (customer_id, status);
OPTIMIZE prod_catalog.silver.orders;
DESCRIBE DETAIL prod_catalog.silver.orders;
```

## Predicate Pushdown and Column Pruning

```python
df.filter(col("order_date") >= "2025-01-01").explain(mode="extended")
efficient_df = df.select("order_id", "customer_id", "amount")
df_jan = spark.table("prod_catalog.silver.orders").filter(
    (col("year") == 2025) & (col("month") == 1)
)
```

## Configuration Reference

| Setting | Recommended | Description |
|---------|-------------|-------------|
| `spark.sql.adaptive.enabled` | `true` | Enable AQE (default in DBR 7.3+) |
| `spark.sql.shuffle.partitions` | `2-4x cores` | Shuffle partition count |
| `spark.sql.autoBroadcastJoinThreshold` | `10-50mb` | Broadcast join size limit |
| `spark.databricks.io.cache.enabled` | `true` | Enable Delta disk cache |
| `spark.sql.files.maxPartitionBytes` | `128mb` | Target file partition size |

## See Also

- [spark-optimization.md](spark-optimization.md)
