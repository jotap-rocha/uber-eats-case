# Structured Streaming

> **Purpose**: Master Spark Structured Streaming — triggers, watermarks, output modes, checkpointing, Kafka, and Auto Loader
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Structured Streaming is Spark's stream processing engine built on the DataFrame API. It treats a stream as an unbounded table and incrementally processes new data using micro-batches or continuous processing. Databricks adds Auto Loader for efficient file ingestion and deep integration with Delta Lake for exactly-once semantics.

## Streaming Programming Model

```python
# Read a streaming source (returns a streaming DataFrame)
stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "broker1:9092,broker2:9092") \
    .option("subscribe", "events-topic") \
    .option("startingOffsets", "latest") \
    .load()

# Apply transformations (same DataFrame API as batch)
processed = stream_df \
    .selectExpr("CAST(value AS STRING) AS json_value", "timestamp") \
    .select(from_json(col("json_value"), schema).alias("data"), "timestamp") \
    .select("data.*", "timestamp")

# Write to Delta (streaming sink)
query = processed.writeStream \
    .format("delta") \
    .outputMode("append") \
    .option("checkpointLocation", "/Volumes/catalog/schema/vol/checkpoints/events/") \
    .trigger(processingTime="1 minute") \
    .table("catalog.schema.streaming_events")

query.awaitTermination()
```

## Triggers

```python
# processingTime — micro-batch on fixed interval
.trigger(processingTime="30 seconds")
.trigger(processingTime="5 minutes")

# once — process all available data, then stop (legacy, prefer availableNow)
.trigger(once=True)

# availableNow — process all backlog, then stop
# More efficient than once: uses multiple micro-batches
.trigger(availableNow=True)

# continuous — experimental, ~1ms latency (limited operations)
.trigger(continuous="1 second")
```

## Watermarks for Late Data

```python
from pyspark.sql.functions import window, col

# Watermark tells Spark how late data can arrive
# 10 minute watermark = allow data up to 10 min late
windowed = stream_df \
    .withWatermark("event_ts", "10 minutes") \
    .groupBy(
        window(col("event_ts"), "5 minutes", "1 minute"),  # 5-min window, 1-min slide
        col("category")
    ) \
    .agg({"amount": "sum", "*": "count"})
```

## Output Modes

```python
# append — only new rows added since last trigger (default for simple transforms)
.outputMode("append")

# complete — entire result table each micro-batch (only with aggregations)
# WARNING: memory-intensive for large result sets
.outputMode("complete")

# update — only rows updated since last trigger (aggregations with watermark)
.outputMode("update")
```

## Checkpointing and Fault Tolerance

```python
# Checkpoint is REQUIRED for exactly-once semantics
# Stores: query progress, offsets, state
# Location: must be unique per query, persistent storage

query = df.writeStream \
    .format("delta") \
    .option("checkpointLocation",
            "/Volumes/catalog/schema/vol/checkpoints/unique-query-name/") \
    .start()

# Delta Lake provides exactly-once end-to-end with checkpointing
# If query fails and restarts, it continues from checkpoint

# Check active streams
for q in spark.streams.active:
    print(f"Query: {q.name}, Status: {q.status}")

# Wait for specific query
query.awaitTermination(timeout=60)  # or query.awaitTermination()
query.stop()
```

## Kafka, Auto Loader e operações com estado

Continuação: [streaming-kafka-autoloader-stateful.md](streaming-kafka-autoloader-stateful.md).

## Related

- [concepts/delta-lake.md](delta-lake.md)
- [concepts/lakeflow.md](lakeflow.md)
- [patterns/incremental-load.md](../patterns/incremental-load.md)
