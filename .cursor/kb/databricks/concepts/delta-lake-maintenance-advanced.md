# Delta Lake — manutenção e tópicos avançados

> **Purpose**: Extensão de [delta-lake.md](delta-lake.md) — Z-order, VACUUM, DML, CDF, *deletion vectors*.  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Z-Ordering for Data Skipping

```sql
OPTIMIZE catalog.schema.events ZORDER BY (user_id, event_date);
ALTER TABLE catalog.schema.events CLUSTER BY (user_id, event_date);
```

## OPTIMIZE and VACUUM

```sql
OPTIMIZE catalog.schema.events;
VACUUM catalog.schema.events RETAIN 168 HOURS;
VACUUM catalog.schema.events RETAIN 168 HOURS DRY RUN;
```

## DML Operations

```sql
UPDATE catalog.schema.customers
SET status = 'inactive'
WHERE last_login < '2024-01-01';

DELETE FROM catalog.schema.events
WHERE event_date < '2020-01-01';

MERGE INTO catalog.schema.customers AS target
USING catalog.schema.customer_updates AS source
ON target.id = source.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```

## Change Data Feed (CDF)

```python
spark.sql("""
    ALTER TABLE catalog.schema.my_table
    SET TBLPROPERTIES (delta.enableChangeDataFeed = true)
""")
changes = spark.read.format("delta") \
    .option("readChangeFeed", "true") \
    .option("startingVersion", 5) \
    .table("catalog.schema.my_table")
changes.filter("_change_type = 'update_postimage'").show()
```

## Deletion Vectors (DBR 12.2+)

```python
spark.sql("DESCRIBE DETAIL catalog.schema.my_table").select("properties").show(truncate=False)
```

## Related

- [delta-lake.md](delta-lake.md)
- [patterns/incremental-load.md](../patterns/incremental-load.md)
