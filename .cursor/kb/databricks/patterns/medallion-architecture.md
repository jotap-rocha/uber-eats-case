# Medallion Architecture

> **Purpose**: Implement a production Bronze → Silver → Gold data lakehouse pipeline with Delta Lake
> **MCP Validated**: 2026-04-20

## When to Use

- Building a new data lakehouse from scratch
- Migrating from a data warehouse to a lakehouse
- Needing clear data quality tiers with auditability
- Supporting both analytical (Gold) and operational (Silver) consumers

## Implementation

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col, current_timestamp, to_date, sha2, concat_ws,
    when, coalesce, lit, trim, upper
)
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType
from delta.tables import DeltaTable

spark = SparkSession.builder.getOrCreate()

# ─── BRONZE: Raw Ingest (keep everything, add metadata) ──────────────────────

def ingest_bronze():
    """Read raw CSV from landing zone, append to bronze with metadata."""
    schema = StructType([
        StructField("order_id",    StringType(),    True),
        StructField("customer_id", StringType(),    True),
        StructField("amount",      DoubleType(),    True),
        StructField("status",      StringType(),    True),
        StructField("order_ts",    StringType(),    True),  # Raw string
    ])

    raw_df = (spark.read
        .format("csv")
        .schema(schema)
        .option("header", "true")
        .load("/Volumes/catalog/schema/vol/landing/orders/"))

    # Add bronze metadata (never modify source data)
    bronze_df = raw_df.withColumn("_ingest_ts", current_timestamp()) \
                      .withColumn("_source_file", col("_metadata.file_path")) \
                      .withColumn("_batch_id", lit("2025-01-01"))

    bronze_df.write \
        .format("delta") \
        .mode("append") \
        .saveAsTable("prod_catalog.bronze.orders")

    print(f"Bronze: ingested {bronze_df.count()} rows")

# ─── SILVER: Cleaned and Deduplicated ─────────────────────────────────────────

def transform_silver():
    """Clean, validate, deduplicate bronze → silver using MERGE."""
    bronze_df = spark.table("prod_catalog.bronze.orders")

    # Clean: type cast, trim, validate
    cleaned_df = (bronze_df
        .filter(col("order_id").isNotNull())
        .filter(col("amount") > 0)
        .withColumn("order_ts", col("order_ts").cast(TimestampType()))
        .withColumn("order_date", to_date(col("order_ts")))
        .withColumn("status", trim(upper(col("status"))))
        .withColumn("amount", coalesce(col("amount"), lit(0.0)))
        # SCD Type 1: generate surrogate key
        .withColumn("_hash", sha2(concat_ws("|",
            col("order_id"), col("customer_id"),
            col("amount"), col("status")), 256))
        .dropDuplicates(["order_id"])
        .drop("_ingest_ts", "_source_file", "_batch_id"))

    # MERGE INTO silver — upsert (SCD Type 1)
    if DeltaTable.isDeltaTable(spark, "prod_catalog.silver.orders"):
        silver_table = DeltaTable.forName(spark, "prod_catalog.silver.orders")
        (silver_table.alias("target")
            .merge(
                cleaned_df.alias("source"),
                "target.order_id = source.order_id"
            )
            .whenMatchedUpdateAll()
            .whenNotMatchedInsertAll()
            .execute())
    else:
        cleaned_df.write.format("delta").saveAsTable("prod_catalog.silver.orders")

    print(f"Silver: merged {cleaned_df.count()} rows")

# ─── GOLD: Business Aggregations ──────────────────────────────────────────────

def build_gold():
    """Aggregate silver → gold business metrics."""
    silver_df = spark.table("prod_catalog.silver.orders")

    # Gold: Daily revenue summary
    daily_revenue = (silver_df
        .filter(col("status") == "COMPLETED")
        .groupBy("order_date")
        .agg(
            {"amount": "sum", "order_id": "count"}
        )
        .withColumnRenamed("sum(amount)", "total_revenue")
        .withColumnRenamed("count(order_id)", "num_orders")
        .withColumn("avg_order_value", col("total_revenue") / col("num_orders"))
        .orderBy("order_date"))

    daily_revenue.write \
        .format("delta") \
        .mode("overwrite") \
        .option("overwriteSchema", "true") \
        .saveAsTable("prod_catalog.gold.daily_revenue")

    # Gold: Customer lifetime value
    customer_ltv = (silver_df
        .filter(col("status") == "COMPLETED")
        .groupBy("customer_id")
        .agg(
            {"amount": "sum", "order_id": "count",
             "order_date": "max"}
        )
        .withColumnRenamed("sum(amount)", "lifetime_value")
        .withColumnRenamed("count(order_id)", "total_orders")
        .withColumnRenamed("max(order_date)", "last_order_date"))

    customer_ltv.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable("prod_catalog.gold.customer_ltv")

    print("Gold: built daily_revenue and customer_ltv")
```

## SCD Type 2 (Slowly Changing Dimensions)

```python
from delta.tables import DeltaTable
from pyspark.sql.functions import current_timestamp, lit

def scd_type2_merge(updates_df, target_table_name: str, key_col: str):
    """Apply SCD Type 2 — keep full history with effective dates."""
    target = DeltaTable.forName(spark, target_table_name)

    # Step 1: expire existing rows that changed
    (target.alias("target")
        .merge(
            updates_df.alias("source"),
            f"target.{key_col} = source.{key_col} AND target.is_current = true"
        )
        .whenMatchedUpdate(
            condition="target._hash != source._hash",
            set={
                "is_current": "false",
                "valid_to": "current_timestamp()"
            }
        )
        .execute())

    # Step 2: insert new/changed rows
    new_rows = updates_df \
        .withColumn("valid_from", current_timestamp()) \
        .withColumn("valid_to", lit(None).cast(TimestampType())) \
        .withColumn("is_current", lit(True))

    new_rows.write \
        .format("delta") \
        .mode("append") \
        .saveAsTable(target_table_name)
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `delta.autoOptimize.optimizeWrite` | `true` | Auto-compact small files on write |
| `delta.autoOptimize.autoCompact` | `true` | Auto-compact after write |
| `spark.databricks.delta.schema.autoMerge.enabled` | `false` | Allow schema evolution on merge |

## See Also

- [patterns/etl-pipeline.md](etl-pipeline.md)
- [patterns/incremental-load.md](incremental-load.md)
- [concepts/delta-lake.md](../concepts/delta-lake.md)
