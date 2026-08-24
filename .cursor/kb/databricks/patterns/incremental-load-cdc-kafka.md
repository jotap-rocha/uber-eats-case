# Incremental load — CDC Debezium via Kafka

> **Purpose**: Continuação de [incremental-load.md](incremental-load.md).  
> **MCP Validated**: 2026-04-20

## CDC from Databases (Debezium → Kafka → Databricks)

```python
from pyspark.sql.functions import from_json, col, lit
from pyspark.sql.types import StructType, StringType, LongType

debezium_schema = StructType() \
    .add("op", StringType()) \
    .add("before", StringType()) \
    .add("after", StringType()) \
    .add("ts_ms", LongType())

cdc_stream = (spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "broker:9092")
    .option("subscribe", "dbserver1.public.customers")
    .option("startingOffsets", "earliest")
    .load())

parsed = (cdc_stream
    .select(from_json(col("value").cast("string"), debezium_schema).alias("e"))
    .select(
        col("e.op"),
        from_json(col("e.after"), customer_schema).alias("after"),
        from_json(col("e.before"), customer_schema).alias("before"),
        col("e.ts_ms"),
    ))

def apply_cdc_batch(batch_df, batch_id):
    upserts = batch_df.filter(col("op").isin(["c", "u", "r"])) \
        .select("after.*").withColumn("_deleted", lit(False))
    deletes = batch_df.filter(col("op") == "d") \
        .select("before.*").withColumn("_deleted", lit(True))
    upsert_to_silver(upserts.union(deletes))

(parsed.writeStream
    .foreachBatch(apply_cdc_batch)
    .option("checkpointLocation", "/checkpoints/cdc_customers/")
    .start()
    .awaitTermination())
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `cloudFiles.maxFilesPerTrigger` | unlimited | Max files per micro-batch |
| `cloudFiles.useNotifications` | `false` | Use cloud event notifications |
| `spark.databricks.delta.schema.autoMerge.enabled` | `false` | Schema evolution on MERGE |

## See Also

- [incremental-load.md](incremental-load.md)
