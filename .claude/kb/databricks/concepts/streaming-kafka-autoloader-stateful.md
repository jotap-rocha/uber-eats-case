# Streaming — Kafka, Auto Loader e estado

> **Purpose**: Extensão de [streaming.md](streaming.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Kafka Source and Sink

```python
from pyspark.sql.functions import col

kafka_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("subscribe", "orders,events") \
    .option("startingOffsets", '{"orders":{"0":100},"events":{"0":-2}}') \
    .load()

from pyspark.sql.functions import from_json
from pyspark.sql.types import StructType, StringType, DoubleType, TimestampType

schema = StructType().add("order_id", StringType()).add("amount", DoubleType()).add("ts", TimestampType())
parsed = kafka_df.select(from_json(col("value").cast("string"), schema).alias("msg")).select("msg.*")

parsed.writeStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker:9092") \
    .option("topic", "processed-orders") \
    .option("checkpointLocation", "/checkpoint/kafka-output/") \
    .start()
```

## Auto Loader (cloudFiles)

```python
df = spark.readStream \
    .format("cloudFiles") \
    .option("cloudFiles.format", "json") \
    .option("cloudFiles.schemaLocation", "/Volumes/catalog/schema/vol/schema/events/") \
    .option("cloudFiles.useNotifications", "true") \
    .load("/Volumes/catalog/schema/vol/landing/events/")
```

## Stateful Operations

```python
windowed_counts = events_df \
    .withWatermark("event_ts", "5 minutes") \
    .groupBy(window("event_ts", "10 minutes"), "user_id") \
    .count()

deduplicated = events_df.withWatermark("event_ts", "1 hour").dropDuplicates(["event_id", "event_ts"])
```

## Related

- [streaming.md](streaming.md)
- [patterns/incremental-load-cdc-kafka.md](../patterns/incremental-load-cdc-kafka.md)
