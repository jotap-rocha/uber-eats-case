# Spark Performance Optimization

> **Purpose**: Optimize PySpark jobs — partitioning, caching, broadcast joins, AQE, skew handling, Z-ordering vs liquid clustering
> **MCP Validated**: 2026-04-20

## When to Use

- Jobs running slower than expected (check Spark UI for bottlenecks)
- OOM errors on driver or executors
- Excessive shuffle detected in query plans
- Large joins causing data skew

## Partitioning Strategy

```python
# ─── Partition sizing rule: aim for 128MB per partition ──────────────────────

# Check current partition count and sizes
df.rdd.getNumPartitions()  # Current partition count

# repartition() — full shuffle, creates equal-sized partitions
# Use: before heavy aggregations, to fix skew, before write
df_balanced = df.repartition(200)  # Explicit partition count
df_by_key   = df.repartition(200, "country")  # Partition by column

# coalesce() — reduces partitions WITHOUT shuffle (narrow transformation)
# Use: before writing small result sets
df_small = df.coalesce(10)  # Only reduces, never increases

# Partition count guidelines:
# shuffle.partitions = 2-4x total executor cores
# 200 partitions is default (often too many for small data)
spark.conf.set("spark.sql.shuffle.partitions", "400")  # Adjust per cluster size

# Auto-detect partition count (AQE handles this automatically)
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
```

## Caching: cache() vs persist()

```python
from pyspark import StorageLevel

# cache() = persist(MEMORY_AND_DISK)
# Use: when DataFrame is reused multiple times in the same job
df.cache()        # Lazy — materializes on first action
df.count()        # Triggers materialization

# persist() with explicit storage level
df.persist(StorageLevel.MEMORY_AND_DISK)   # Default: spills to disk
df.persist(StorageLevel.MEMORY_ONLY)       # Fails if not enough memory
df.persist(StorageLevel.DISK_ONLY)         # Slower but reliable
df.persist(StorageLevel.MEMORY_AND_DISK_SER)  # Serialized (less memory, more CPU)

# ALWAYS unpersist when done — releases memory
df.unpersist()

# When to cache:
#   - DataFrame used 3+ times in pipeline
#   - Training ML models (multiple passes over data)
# When NOT to cache:
#   - One-time use (wastes memory)
#   - Very large DataFrames (use disk-based caching or Delta)

# Delta table caching (disk-based, persists across sessions)
spark.conf.set("spark.databricks.io.cache.enabled", "true")
```

## Broadcast Joins

```python
from pyspark.sql.functions import broadcast

# Broadcast join: replicate small table to all workers — eliminates shuffle
# Use when one side is < broadcast threshold (default: 10MB)

# Explicit broadcast hint
result = large_df.join(broadcast(small_lookup_df), "key")

# Adjust broadcast threshold (increase for larger lookup tables)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "50mb")  # 50MB

# Disable broadcast (when you know it'll cause OOM)
spark.conf.set("spark.sql.autoBroadcastJoinThreshold", "-1")

# Join types and cost:
# broadcast join  → no shuffle, fastest (limited by driver memory)
# sort-merge join → 2 shuffles (default for large-large joins)
# shuffle hash    → 1 shuffle (medium tables)
```

## Adaptive Query Execution (AQE)

```python
# AQE (enabled by default in DBR 7.3+) dynamically optimizes at runtime:
# 1. Coalesces shuffle partitions (reduces 200 → actual needed)
# 2. Converts sort-merge joins to broadcast joins when stats available
# 3. Handles data skew by splitting skewed partitions

# Ensure AQE is enabled
spark.conf.set("spark.sql.adaptive.enabled", "true")
spark.conf.set("spark.sql.adaptive.coalescePartitions.enabled", "true")
spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")

# AQE skew join threshold (partition 5x larger than median = skewed)
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionFactor", "5")
spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "256mb")
```

## *Skew*, clustering e *pushdown*

Continuação: [spark-optimization-skew-clustering.md](spark-optimization-skew-clustering.md).

## See Also

- [patterns/etl-pipeline.md](etl-pipeline.md)
- [concepts/delta-lake.md](../concepts/delta-lake.md)
- [concepts/clusters.md](../concepts/clusters.md)
