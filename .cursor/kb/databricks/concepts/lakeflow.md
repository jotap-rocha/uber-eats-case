# Lakeflow Declarative Pipelines (DLT)

> **Purpose**: Master Lakeflow / Delta Live Tables — streaming tables, materialized views, expectations, CDC, and pipeline modes
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Lakeflow Declarative Pipelines (formerly Delta Live Tables / DLT) is Databricks' declarative framework for building batch and streaming data pipelines. You declare what data should look like; Databricks manages execution, orchestration, error handling, and data quality. DLT code still works unchanged — Lakeflow SDP is fully backward-compatible.

## Streaming Tables vs Materialized Views

| Feature | Streaming Table | Materialized View |
|---------|-----------------|-------------------|
| Processes data | Incrementally (new rows only) | Full refresh or incremental |
| Source type | Streaming (Kafka, Auto Loader) | Any (batch or streaming) |
| Supports APPEND | Yes | Limited |
| Aggregate queries | No | Yes |
| Typical use | Bronze, Silver ingest | Gold aggregations |

```python
import dlt
from pyspark.sql.functions import col, to_timestamp

# STREAMING TABLE — processes new data incrementally
@dlt.table(
    comment="Raw bronze events from landing zone",
    table_properties={"quality": "bronze"}
)
def bronze_events():
    return (spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.schemaLocation", "/Volumes/catalog/schema/vol/schemas/events")
        .load("/Volumes/catalog/schema/vol/landing/events/"))

# MATERIALIZED VIEW — recomputed when pipeline runs
@dlt.table(
    comment="Daily aggregated metrics — Gold layer",
    table_properties={"quality": "gold"}
)
def gold_daily_metrics():
    return dlt.read("silver_events") \
        .groupBy("event_date", "category") \
        .agg({"amount": "sum", "*": "count"})
```

## @dlt.table vs @dlt.view

```python
# @dlt.table — persisted as Delta table in Unity Catalog
@dlt.table(name="silver_events")
def silver_events():
    return dlt.read_stream("bronze_events").filter(col("id").isNotNull())

# @dlt.view — logical view, NOT persisted (like SQL VIEW)
# Use for intermediate transformations within the same pipeline
@dlt.view
def enriched_events():
    return dlt.read("silver_events").join(dlt.read("dim_users"), "user_id")
```

## Expectations (Data Quality)

```python
# @dlt.expect — log violations but continue
@dlt.table
@dlt.expect("valid_amount", "amount > 0")
def silver_transactions():
    return dlt.read_stream("bronze_transactions")

# @dlt.expect_or_drop — drop invalid rows
@dlt.table
@dlt.expect_or_drop("non_null_id", "id IS NOT NULL")
@dlt.expect_or_drop("valid_status", "status IN ('active', 'pending', 'closed')")
def silver_customers():
    return dlt.read_stream("bronze_customers")

# @dlt.expect_or_fail — fail the pipeline on ANY violation
@dlt.table
@dlt.expect_or_fail("no_duplicates", "COUNT(*) = COUNT(DISTINCT id)")
def silver_critical():
    return dlt.read_stream("bronze_critical")

# Multiple expectations as dict
expectations = {
    "valid_id":     "id IS NOT NULL",
    "valid_amount": "amount BETWEEN 0 AND 1000000",
    "valid_date":   "event_date >= '2020-01-01'",
}

@dlt.table
@dlt.expect_all(expectations)          # log violations
# @dlt.expect_all_or_drop(expectations) # drop violations
# @dlt.expect_all_or_fail(expectations) # fail on violation
def silver_orders():
    return dlt.read_stream("bronze_orders")
```

## Modos de pipeline, Auto Loader em DLT, CDC e erros

Continuação: [lakeflow-pipeline-modes-cdc.md](lakeflow-pipeline-modes-cdc.md).

## Related

- [concepts/streaming.md](streaming.md)
- [concepts/delta-lake.md](delta-lake.md)
- [patterns/dlt-pipeline.md](../patterns/dlt-pipeline.md)
- [patterns/medallion-architecture.md](../patterns/medallion-architecture.md)
