# Lakeflow — modos de pipeline, Auto Loader, CDC e métricas

> **Purpose**: Extensão de [lakeflow.md](lakeflow.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Pipeline Modes

```python
{
  "continuous": false,
  "development": false
}
```

## Auto Loader Integration in DLT

```python
@dlt.table(comment="Bronze raw files via Auto Loader")
def bronze_raw():
    return (spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "csv")
        .option("cloudFiles.schemaLocation",
                "/Volumes/catalog/schema/vol/schema_hints/raw/")
        .option("cloudFiles.inferColumnTypes", "true")
        .option("cloudFiles.schemaHints", "id BIGINT, event_ts TIMESTAMP")
        .load("/Volumes/catalog/schema/vol/landing/raw/"))
```

## CDC with apply_changes()

```python
from pyspark.sql.functions import col, expr

dlt.create_streaming_table("silver_customers_cdc")

dlt.apply_changes(
    target="silver_customers_cdc",
    source="bronze_customers_changes",
    keys=["customer_id"],
    sequence_by=col("updated_at"),
    apply_as_deletes=expr("operation = 'DELETE'"),
    apply_as_truncates=expr("operation = 'TRUNCATE'"),
    column_list=["customer_id", "name", "email", "status"],
    except_column_list=["_metadata"],
)
```

## Pipeline Event Log and Metrics

```python
spark.sql("""
    SELECT timestamp, event_type,
           details:flow_progress.metrics.num_output_rows AS output_rows,
           details:flow_progress.data_quality.dropped_records AS dropped_rows
    FROM catalog.schema.my_pipeline._dlt_event_log
    WHERE event_type = 'flow_progress'
    ORDER BY timestamp DESC LIMIT 50
""")
```

## Common Mistakes

### Wrong

```python
@dlt.table
def bronze_events():
    return spark.read.format("json").load("/landing/")
```

### Correct

```python
@dlt.table
def bronze_events():
    return spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "json") \
        .load("/Volumes/catalog/schema/vol/landing/")
```

## Related

- [lakeflow.md](lakeflow.md)
