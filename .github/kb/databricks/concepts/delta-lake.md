# Delta Lake

> **Purpose**: Master Delta Lake — ACID transactions, time travel, schema evolution, optimization commands, and Change Data Feed
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Delta Lake is an open-source storage format that adds reliability to data lakes. A Delta table is Parquet files plus a transaction log (`_delta_log/`). It provides ACID transactions, schema enforcement, time travel, and DML operations (UPDATE, DELETE, MERGE) on distributed storage. It is the default format for Databricks managed tables.

## Delta Format Internals

```text
my_table/
├── _delta_log/
│   ├── 00000000000000000000.json   # Initial snapshot
│   ├── 00000000000000000001.json   # Each commit = 1 JSON file
│   ├── 00000000000000000002.json
│   └── 00000000000000000010.checkpoint.parquet  # Checkpoint every 10 commits
├── part-00000-....snappy.parquet   # Data files
└── part-00001-....snappy.parquet
```

## ACID Guarantees

```python
# Atomicity — write either fully succeeds or fully fails
df.write.format("delta").mode("append").saveAsTable("catalog.schema.events")

# Isolation — concurrent readers/writers via optimistic concurrency control
# Multiple writers get serializable isolation

# Durability — all commits recorded in _delta_log before acknowledged
```

## Read and Write

```python
# Write (create or overwrite)
df.write.format("delta").mode("overwrite").saveAsTable("catalog.schema.my_table")

# Write with partitioning
df.write.format("delta") \
    .partitionBy("year", "month") \
    .mode("overwrite") \
    .saveAsTable("catalog.schema.events_partitioned")

# Read
df = spark.read.format("delta").table("catalog.schema.my_table")
# or
df = spark.table("catalog.schema.my_table")
```

## Time Travel

```python
# VERSION AS OF — read historical snapshot
df_v0 = spark.read.format("delta") \
    .option("versionAsOf", 0) \
    .table("catalog.schema.my_table")

# TIMESTAMP AS OF
df_ts = spark.read.format("delta") \
    .option("timestampAsOf", "2025-01-01") \
    .table("catalog.schema.my_table")

# SQL syntax
spark.sql("SELECT * FROM catalog.schema.my_table VERSION AS OF 5")
spark.sql("SELECT * FROM catalog.schema.my_table TIMESTAMP AS OF '2025-01-01'")

# View history
spark.sql("DESCRIBE HISTORY catalog.schema.my_table")
```

## Schema Enforcement vs Evolution

```python
# Schema enforcement (default) — rejects writes with incompatible schema
# This FAILS if df has extra/incompatible columns:
df.write.format("delta").mode("append").saveAsTable("catalog.schema.events")

# Schema evolution — mergeSchema merges new columns
df.write.format("delta") \
    .option("mergeSchema", "true") \
    .mode("append") \
    .saveAsTable("catalog.schema.events")

# Or via Spark config (session-level)
spark.conf.set("spark.databricks.delta.schema.autoMerge.enabled", "true")
```

## Manutenção avançada (OPTIMIZE, Z-order, DML, CDF)

Z-order, VACUUM, DML, Change Data Feed e *deletion vectors* — ver:

- [delta-lake-maintenance-advanced.md](delta-lake-maintenance-advanced.md)

## Related

- [concepts/spark-core.md](spark-core.md)
- [patterns/medallion-architecture.md](../patterns/medallion-architecture.md)
- [patterns/incremental-load.md](../patterns/incremental-load.md)
