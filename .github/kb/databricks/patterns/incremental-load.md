# Incremental Load Patterns

> **Purpose**: Implement efficient incremental data loads — Auto Loader, MERGE INTO upserts, watermarks, and CDC patterns
> **MCP Validated**: 2026-04-20

## When to Use

- Loading new files arriving in cloud storage (Auto Loader)
- Upserting records from source systems (MERGE INTO)
- Processing database CDC streams (Debezium → Kafka)
- Replacing expensive full table reloads with incremental updates

## Auto Loader with Schema Inference and Hints

```python
from pyspark.sql.functions import col, current_timestamp

# ─── Basic Auto Loader (streaming incremental file ingest) ─────────────────

raw_stream = (spark.readStream
    .format("cloudFiles")
    .option("cloudFiles.format", "json")
    # Schema location: Auto Loader infers and evolves schema here
    .option("cloudFiles.schemaLocation",
            "/Volumes/catalog/schema/vol/schemas/events/")
    # Schema hints: pre-define known columns to avoid type inference errors
    .option("cloudFiles.schemaHints",
            "id BIGINT, user_id STRING, amount DOUBLE, event_ts TIMESTAMP")
    # Include files already in the directory on first run
    .option("cloudFiles.includeExistingFiles", "true")
    # Use file notifications (S3/Event Grid) instead of directory listing
    .option("cloudFiles.useNotifications", "true")
    # Max files per micro-batch (controls throughput)
    .option("cloudFiles.maxFilesPerTrigger", "1000")
    # Add file metadata
    .option("cloudFiles.includeExistingFiles", "true")
    .load("/Volumes/catalog/schema/vol/landing/events/"))

# Enrich with ingestion metadata
bronze_stream = (raw_stream
    .withColumn("_ingest_ts", current_timestamp())
    .withColumn("_source_file", col("_metadata.file_path"))
    .withColumn("_file_modification_time",
                col("_metadata.file_modification_time")))

# Write to Delta bronze table (streaming write)
bronze_query = (bronze_stream.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation",
            "/Volumes/catalog/schema/vol/checkpoints/bronze_events/")
    .trigger(availableNow=True)  # Process all backlog, then stop
    .table("prod_catalog.bronze.events"))

bronze_query.awaitTermination()
```

## MERGE INTO for Upserts

```python
from delta.tables import DeltaTable
from pyspark.sql.functions import col, sha2, concat_ws

# ─── MERGE INTO: full upsert pattern ────────────────────────────────────────

def upsert_to_silver(updates_df):
    """Merge new/updated records into silver table."""
    target_table = "prod_catalog.silver.customers"

    if DeltaTable.isDeltaTable(spark, target_table):
        delta_target = DeltaTable.forName(spark, target_table)

        (delta_target.alias("target")
            .merge(
                updates_df.alias("source"),
                # Match condition (natural key)
                "target.customer_id = source.customer_id"
            )
            # Update if any column changed (use hash for efficiency)
            .whenMatchedUpdate(
                condition="target._row_hash != source._row_hash",
                set={
                    "name":       "source.name",
                    "email":      "source.email",
                    "status":     "source.status",
                    "updated_at": "source.updated_at",
                    "_row_hash":  "source._row_hash",
                }
            )
            # Insert new records
            .whenNotMatchedInsertAll()
            # Delete records marked for deletion (from CDC)
            .whenMatchedDelete(
                condition="source._operation = 'DELETE'"
            )
            .execute())
    else:
        # First load: create table
        updates_df.write \
            .format("delta") \
            .saveAsTable(target_table)

# Add hash for efficient change detection
updates_with_hash = updates_df.withColumn(
    "_row_hash",
    sha2(concat_ws("|", col("name"), col("email"), col("status")), 256)
)
upsert_to_silver(updates_with_hash)
```

## Watermark-Based Incremental Reads

```python
# Read only new data since last run using max timestamp watermark
import json

CHECKPOINT_TABLE = "prod_catalog.pipeline_meta.watermarks"
PIPELINE_KEY = "silver_orders_etl"

def get_watermark() -> str:
    """Get last processed timestamp from watermark table."""
    try:
        result = spark.sql(f"""
            SELECT max_processed_ts
            FROM {CHECKPOINT_TABLE}
            WHERE pipeline_key = '{PIPELINE_KEY}'
        """).collect()
        if result:
            return str(result[0]["max_processed_ts"])
    except Exception:
        pass
    return "1970-01-01 00:00:00"  # Default: process all

def save_watermark(max_ts: str):
    """Save new watermark after successful processing."""
    spark.sql(f"""
        MERGE INTO {CHECKPOINT_TABLE} AS target
        USING (SELECT '{PIPELINE_KEY}' AS pipeline_key,
                      TIMESTAMP '{max_ts}' AS max_processed_ts) AS source
        ON target.pipeline_key = source.pipeline_key
        WHEN MATCHED THEN UPDATE SET max_processed_ts = source.max_processed_ts
        WHEN NOT MATCHED THEN INSERT *
    """)

# Main incremental load
last_ts = get_watermark()
print(f"Processing records after: {last_ts}")

new_records = spark.sql(f"""
    SELECT *
    FROM prod_catalog.bronze.orders
    WHERE _ingest_ts > TIMESTAMP '{last_ts}'
""")

if new_records.count() > 0:
    # Process and write
    process_and_upsert(new_records)

    # Update watermark
    max_ts = new_records.agg({"_ingest_ts": "max"}).collect()[0][0]
    save_watermark(str(max_ts))
    print(f"Updated watermark to: {max_ts}")
```

## CDC (Debezium → Kafka → Databricks)

Continuação: [incremental-load-cdc-kafka.md](incremental-load-cdc-kafka.md).

## See Also

- [patterns/medallion-architecture.md](medallion-architecture.md)
- [patterns/dlt-pipeline.md](dlt-pipeline.md)
- [concepts/streaming.md](../concepts/streaming.md)
- [concepts/delta-lake.md](../concepts/delta-lake.md)
