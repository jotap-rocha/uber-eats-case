# DLT Pipeline — Bronze to Gold

> **Purpose**: Complete Lakeflow Declarative Pipeline with Auto Loader, expectations, CDC, and Gold aggregations
> **MCP Validated**: 2026-04-20

## When to Use

- Building declarative data pipelines managed by Databricks
- Need automatic data quality enforcement with expectations
- Streaming ingestion via Auto Loader into medallion layers
- CDC processing with apply_changes()

## Implementation

```python
import dlt
from pyspark.sql.functions import (
    col, to_timestamp, trim, upper, sha2, concat_ws,
    current_timestamp, lit, when, coalesce, date_trunc
)
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, TimestampType

# ─── BRONZE: Raw ingest with Auto Loader ─────────────────────────────────────

@dlt.table(
    name="bronze_orders",
    comment="Raw orders — append-only landing zone",
    table_properties={
        "quality": "bronze",
        "delta.autoOptimize.optimizeWrite": "true",
    }
)
def bronze_orders():
    """Ingest raw order events from cloud storage via Auto Loader."""
    return (spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.schemaLocation",
                "/Volumes/catalog/schema/vol/schema_hints/orders/")
        .option("cloudFiles.schemaHints",
                "order_id STRING, customer_id STRING, amount DOUBLE, "
                "status STRING, order_ts STRING")
        .option("cloudFiles.inferColumnTypes", "true")
        .option("cloudFiles.includeExistingFiles", "true")
        .load("/Volumes/catalog/schema/vol/landing/orders/"))

@dlt.table(
    name="bronze_customers_cdc",
    comment="CDC stream from operational database (Debezium / Kafka)",
    table_properties={"quality": "bronze"}
)
def bronze_customers_cdc():
    """Read CDC events from Kafka."""
    from pyspark.sql.functions import from_json
    schema = StructType([
        StructField("op",          StringType(), True),
        StructField("customer_id", StringType(), True),
        StructField("name",        StringType(), True),
        StructField("email",       StringType(), True),
        StructField("country",     StringType(), True),
        StructField("updated_at",  StringType(), True),
    ])
    return (spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers",
                "{{secrets/prod/kafka-bootstrap}}")
        .option("subscribe", "dbserver1.public.customers")
        .option("startingOffsets", "latest")
        .load()
        .select(from_json(col("value").cast("string"), schema).alias("d"))
        .select("d.*"))

# ─── SILVER: Cleaned with expectations ────────────────────────────────────────

@dlt.table(
    name="silver_orders",
    comment="Cleaned, validated orders — deduplicated",
    table_properties={
        "quality": "silver",
        "delta.enableChangeDataFeed": "true",
    }
)
@dlt.expect_or_drop("non_null_order_id", "order_id IS NOT NULL")
@dlt.expect_or_drop("positive_amount",   "amount > 0")
@dlt.expect("valid_status",
    "status IN ('PENDING', 'PROCESSING', 'COMPLETED', 'CANCELLED')")
@dlt.expect("order_ts_not_future",
    "order_ts <= current_timestamp()")
def silver_orders():
    """Clean and validate bronze orders."""
    return (dlt.read_stream("bronze_orders")
        .withColumn("order_ts",   to_timestamp("order_ts", "yyyy-MM-dd'T'HH:mm:ss"))
        .withColumn("status",     trim(upper(col("status"))))
        .withColumn("amount",     coalesce(col("amount"), lit(0.0)))
        .withColumn("_row_hash",  sha2(
            concat_ws("|", col("order_id"), col("customer_id"),
                      col("amount"), col("status")), 256))
        .dropDuplicates(["order_id"]))

# Streaming table for CDC (must declare before apply_changes)
dlt.create_streaming_table(
    name="silver_customers",
    comment="SCD Type 1 customers — latest state via CDC MERGE",
    table_properties={"quality": "silver"}
)

dlt.apply_changes(
    target    = "silver_customers",
    source    = "bronze_customers_cdc",
    keys      = ["customer_id"],
    sequence_by = col("updated_at"),
    apply_as_deletes = col("op") == "d",
    except_column_list = ["op"],
)

# ─── INTERMEDIATE: Enriched view (not persisted) ───────────────────────────

@dlt.view(comment="Orders joined with customer data")
def enriched_orders():
    """Join silver orders with silver customers — logical view only."""
    orders    = dlt.read_stream("silver_orders")
    customers = dlt.read("silver_customers")
    return (orders
        .join(customers, "customer_id", "left")
        .select(
            col("order_id"),
            col("customer_id"),
            col("name").alias("customer_name"),
            col("country"),
            col("amount"),
            col("status"),
            col("order_ts"),
        ))

# ─── GOLD: Business aggregations (materialized views) ─────────────────────────

@dlt.table(
    name="gold_daily_revenue",
    comment="Daily revenue summary by country — business KPIs",
    table_properties={"quality": "gold"}
)
def gold_daily_revenue():
    """Aggregate completed orders into daily revenue metrics."""
    return (dlt.read("enriched_orders")
        .filter(col("status") == "COMPLETED")
        .withColumn("order_date", date_trunc("day", col("order_ts")))
        .groupBy("order_date", "country")
        .agg({
            "amount":    "sum",
            "order_id":  "count",
        })
        .withColumnRenamed("sum(amount)",   "total_revenue")
        .withColumnRenamed("count(order_id)", "num_orders"))

@dlt.table(
    name="gold_customer_metrics",
    comment="Customer lifetime metrics — revenue, order count, recency",
    table_properties={"quality": "gold"}
)
@dlt.expect("positive_ltv", "lifetime_value > 0")
def gold_customer_metrics():
    """Customer-level aggregations for analytics and ML features."""
    import pyspark.sql.functions as F
    return (dlt.read("enriched_orders")
        .filter(col("status") == "COMPLETED")
        .groupBy("customer_id", "customer_name", "country")
        .agg(
            F.sum("amount").alias("lifetime_value"),
            F.count("order_id").alias("total_orders"),
            F.max("order_ts").alias("last_order_ts"),
            F.avg("amount").alias("avg_order_value"),
        ))
```

## Configuração do pipeline (`bundle.yml`) e tabela de parâmetros

Ver [dlt-pipeline-bundle-config.md](dlt-pipeline-bundle-config.md).

## See Also

- [patterns/medallion-architecture.md](medallion-architecture.md)
- [patterns/incremental-load.md](incremental-load.md)
- [concepts/lakeflow.md](../concepts/lakeflow.md)
