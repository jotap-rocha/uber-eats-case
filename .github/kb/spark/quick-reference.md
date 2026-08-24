# Spark Quick Reference Guide

**Fast lookup for common Spark patterns, syntax, and examples**

## 🚀 Core Syntax

### SparkSession Creation

| Pattern | Purpose | Example |
|---------|---------|---------|
| Basic | Simple SparkSession | `SparkSession.builder.appName("app").getOrCreate()` |
| With Config | Configured session | `SparkSession.builder.config("key", "value").getOrCreate()` |
| With AQE | Adaptive Query Execution | `.config("spark.sql.adaptive.enabled", "true")` |
| With Catalog | Unity Catalog | `.config("spark.sql.catalog.catalog_name", "...")` |

### DataFrame Operations

| Operation | Purpose | Example |
|-----------|---------|---------|
| `read.format()` | Read data | `spark.read.format("parquet").load("path")` |
| `read.parquet()` | Read Parquet | `spark.read.parquet("path")` |
| `read.json()` | Read JSON | `spark.read.json("path")` |
| `read.csv()` | Read CSV | `spark.read.csv("path", header=True, inferSchema=True)` |
| `write.mode()` | Write data | `df.write.mode("overwrite").parquet("path")` |
| `select()` | Select columns | `df.select("col1", "col2")` |
| `filter()` | Filter rows | `df.filter(col("age") > 18)` |
| `groupBy()` | Group and aggregate | `df.groupBy("key").agg(sum("amount"))` |
| `join()` | Join DataFrames | `df1.join(df2, "key", "inner")` |
| `withColumn()` | Add/modify column | `df.withColumn("new", col("old") * 2)` |
| `drop()` | Drop columns | `df.drop("col1", "col2")` |
| `distinct()` | Remove duplicates | `df.distinct()` |
| `orderBy()` | Sort | `df.orderBy(col("date").desc())` |
| `limit()` | Limit rows | `df.limit(100)` |
| `repartition()` | Repartition | `df.repartition(200)` |
| `coalesce()` | Reduce partitions | `df.coalesce(10)` |
| `cache()` | Cache DataFrame | `df.cache()` |
| `persist()` | Persist with level | `df.persist(StorageLevel.MEMORY_AND_DISK)` |
| `unpersist()` | Remove from cache | `df.unpersist()` |

### SparkSQL Keywords

| Keyword | Purpose | Example |
|---------|---------|---------|
| `CREATE OR REPLACE TEMP VIEW` | Create temporary view | `CREATE OR REPLACE TEMP VIEW my_view AS SELECT * FROM table` |
| `CREATE TABLE` | Create table | `CREATE TABLE my_table USING PARQUET LOCATION 'path'` |
| `INSERT INTO` | Insert data | `INSERT INTO table SELECT * FROM source` |
| `SELECT` | Query data | `SELECT * FROM table WHERE condition` |
| `WITH` | CTE (Common Table Expression) | `WITH cte AS (SELECT ...) SELECT * FROM cte` |
| `PARTITION BY` | Window partition | `ROW_NUMBER() OVER (PARTITION BY key ORDER BY date)` |
| `ORDER BY` | Window ordering | `LAG(value) OVER (ORDER BY date)` |
| `ROWS BETWEEN` | Window frame | `SUM(amount) OVER (ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)` |

### Window Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `ROW_NUMBER()` | Sequential numbering | `ROW_NUMBER() OVER (PARTITION BY key ORDER BY date)` |
| `RANK()` | Rank with gaps | `RANK() OVER (PARTITION BY key ORDER BY value DESC)` |
| `DENSE_RANK()` | Rank without gaps | `DENSE_RANK() OVER (PARTITION BY key ORDER BY value)` |
| `LAG()` | Previous value | `LAG(value, 1) OVER (ORDER BY date)` |
| `LEAD()` | Next value | `LEAD(value, 1) OVER (ORDER BY date)` |
| `FIRST_VALUE()` | First value in window | `FIRST_VALUE(value) OVER (PARTITION BY key)` |
| `LAST_VALUE()` | Last value in window | `LAST_VALUE(value) OVER (PARTITION BY key)` |
| `SUM() OVER()` | Running sum | `SUM(amount) OVER (PARTITION BY key ORDER BY date)` |
| `AVG() OVER()` | Running average | `AVG(value) OVER (PARTITION BY key)` |

### Structured Streaming

| Operation | Purpose | Example |
|-----------|---------|---------|
| `readStream.format()` | Read stream | `spark.readStream.format("kafka").load()` |
| `writeStream.outputMode()` | Write stream | `.writeStream.outputMode("append").start()` |
| `withWatermark()` | Set watermark | `.withWatermark("timestamp", "10 minutes")` |
| `trigger()` | Set trigger | `.trigger(processingTime="1 minute")` |
| `awaitTermination()` | Wait for stream | `query.awaitTermination()` |
| `stop()` | Stop stream | `query.stop()` |

## 📋 Common Patterns

### 1. Basic ETL Pipeline

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

spark = SparkSession.builder.appName("ETL").getOrCreate()

# Extract
df = spark.read.parquet("s3://bucket/raw/")

# Transform
df_cleaned = df.filter(col("age") > 18)
df_aggregated = df_cleaned.groupBy("category").agg(
    sum("amount").alias("total"),
    count("*").alias("count")
)

# Load
df_aggregated.write.mode("overwrite").parquet("s3://bucket/processed/")
```

### 2. Broadcast Join

```python
from pyspark.sql.functions import broadcast

# Small lookup table
df_small = spark.read.parquet("path/to/small/lookup")

# Large table
df_large = spark.read.parquet("path/to/large/table")

# Broadcast join (automatic for small tables, explicit is better)
df_joined = df_large.join(
    broadcast(df_small),
    df_large.id == df_small.id,
    "left"
)
```

### 3. Window Functions

```python
from pyspark.sql import Window
from pyspark.sql.functions import row_number, lag, sum, col

# Define window specification
window_spec = Window.partitionBy("category").orderBy("date")

# Row number
df = df.withColumn("row_num", row_number().over(window_spec))

# Previous value
df = df.withColumn("prev_amount", lag("amount", 1).over(window_spec))

# Running total
df = df.withColumn("running_total", sum("amount").over(
    Window.partitionBy("category")
         .orderBy("date")
         .rowsBetween(Window.unboundedPreceding, Window.currentRow)
))
```

### 4. Structured Streaming with Windowing

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col, count, to_timestamp

spark = SparkSession.builder.appName("Streaming").getOrCreate()

# Read stream
stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "topic") \
    .load()

# Process with windowing
windowed = stream \
    .select(
        col("key"),
        to_timestamp(col("timestamp")).alias("event_time"),
        col("value")
    ) \
    .withWatermark("event_time", "10 minutes") \
    .groupBy(
        window("event_time", "5 minutes"),
        "key"
    ) \
    .agg(count("*").alias("count"))

# Write stream
query = windowed.writeStream \
    .outputMode("update") \
    .format("console") \
    .option("checkpointLocation", "/path/to/checkpoint") \
    .start()

query.awaitTermination()
```

### 5. Caching for Reuse

```python
# Cache expensive computation
df_expensive = expensive_operation(df).cache()

# Use cached DataFrame multiple times
df_filtered = df_expensive.filter(col("status") == "active")
df_aggregated = df_expensive.groupBy("category").agg(sum("amount"))

# Unpersist when done
df_expensive.unpersist()
```

### 6. SparkSQL Queries

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("SQL").getOrCreate()

# Register DataFrame as view
df.createOrReplaceTempView("my_table")

# Execute SQL
result = spark.sql("""
    SELECT 
        category,
        SUM(amount) as total,
        COUNT(*) as count,
        AVG(amount) as average
    FROM my_table
    WHERE age > 18
    GROUP BY category
    HAVING total > 1000
    ORDER BY total DESC
""")

# Complex joins
result = spark.sql("""
    SELECT 
        a.id,
        a.name,
        b.category,
        b.amount
    FROM table_a a
    INNER JOIN table_b b ON a.id = b.id
    WHERE a.status = 'active'
""")
```

### 7. Handling Nulls

```python
from pyspark.sql.functions import col, isnull, coalesce, when

# Filter nulls
df_filtered = df.filter(col("column").isNotNull())

# Replace nulls
df_filled = df.withColumn("value", coalesce(col("value"), col("default"), lit(0)))

# Conditional null handling
df_conditional = df.withColumn(
    "value",
    when(col("value").isNull(), 0).otherwise(col("value"))
)
```

### 8. Data Type Conversions

```python
from pyspark.sql.functions import col, to_date, to_timestamp, cast
from pyspark.sql.types import IntegerType, StringType

# Date conversions
df = df.withColumn("date", to_date(col("date_string"), "yyyy-MM-dd"))
df = df.withColumn("timestamp", to_timestamp(col("ts_string"), "yyyy-MM-dd HH:mm:ss"))

# Type casting
df = df.withColumn("age_int", col("age_string").cast(IntegerType()))
df = df.withColumn("id_str", col("id").cast(StringType()))
```

## 🔧 Configuration Snippets

### SparkSession with AQE

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .config("spark.sql.adaptive.skewJoin.enabled", "true") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()
```

### Resource Configuration

```python
# Executor configuration
spark.conf.set("spark.executor.memory", "4g")
spark.conf.set("spark.executor.cores", "2")
spark.conf.set("spark.executor.instances", "10")

# Dynamic allocation
spark.conf.set("spark.dynamicAllocation.enabled", "true")
spark.conf.set("spark.dynamicAllocation.minExecutors", "2")
spark.conf.set("spark.dynamicAllocation.maxExecutors", "20")

# Serialization
spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
```

### Delta Lake Configuration

```python
# Enable Delta Lake
spark.conf.set("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
spark.conf.set("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

# Read Delta
df = spark.read.format("delta").load("path/to/delta/table")

# Write Delta
df.write.format("delta").mode("overwrite").save("path/to/delta/table")
```

## 🎯 Decision Matrix

### When to Use What

| Use Case | Choose |
|----------|--------|
| **Batch processing** | DataFrame API or SparkSQL |
| **Real-time streaming** | Structured Streaming |
| **Small table joins** | Broadcast join |
| **Large table joins** | Regular join (let AQE optimize) |
| **Frequently reused DataFrame** | Cache or persist |
| **Reduce partitions** | Coalesce (no shuffle) |
| **Increase partitions** | Repartition (with shuffle) |
| **Complex SQL queries** | SparkSQL |
| **Python transformations** | DataFrame API |
| **Performance optimization** | Enable AQE |
| **Cost optimization** | Dynamic allocation |
| **Low latency streaming** | Continuous processing mode |
| **Fault tolerance streaming** | Micro-batch with checkpointing |
| **Schema inference** | `inferSchema=True` (CSV/JSON) |
| **Explicit schema** | Define schema for better performance |

## ⚠️ Common Pitfalls

### ❌ DON'T

```python
# Don't use RDD API in production
rdd = spark.sparkContext.parallelize([1, 2, 3])
rdd_filtered = rdd.filter(lambda x: x > 1)  # ❌ Use DataFrame API instead

# Don't collect large DataFrames to driver
data = df.collect()  # ❌ Can cause OOM on driver
for row in data:
    process(row)

# Don't create too many partitions
df = df.repartition(10000)  # ❌ Too many small partitions

# Don't skip caching for reused DataFrames
df1 = expensive_operation(df)
df2 = df1.filter(...)
df3 = df1.groupBy(...)  # ❌ Recomputes df1

# Don't use Python UDFs when built-in functions exist
from pyspark.sql.functions import udf
def upper_udf(s):
    return s.upper()
upper = udf(upper_udf, StringType())
df = df.withColumn("upper", upper("name"))  # ❌ Use built-in upper() instead

# Don't ignore nulls in filters
df.filter(df.column == "value")  # ❌ Nulls excluded, might be unintended

# Don't forget to unpersist cached DataFrames
df.cache()
# ... use df ...
# ❌ Forgot to unpersist - wastes memory

# Don't use legacy DStreams
from pyspark.streaming import StreamingContext  # ❌ Use Structured Streaming
```

### ✅ DO

```python
# Use DataFrame API
df = spark.createDataFrame([(1,), (2,), (3,)], ["value"])
df_filtered = df.filter(col("value") > 1)  # ✅ DataFrame API

# Use foreachPartition or mapPartitions
def process_partition(iterator):
    for row in iterator:
        process(row)
    return iter([])

df.foreachPartition(process_partition)  # ✅ Process in executors

# Optimal partitioning
df = df.repartition(200)  # ✅ Optimal for most cases
df = df.coalesce(10)  # ✅ Reduce partitions without shuffle

# Cache for reuse
df1 = expensive_operation(df).cache()  # ✅ Cache
df2 = df1.filter(...)
df3 = df1.groupBy(...)
df1.unpersist()  # ✅ Clean up

# Use built-in functions
from pyspark.sql.functions import upper
df = df.withColumn("upper", upper("name"))  # ✅ Built-in function

# Handle nulls explicitly
from pyspark.sql.functions import col, isnull
df.filter((col("column") == "value") | col("column").isNull())  # ✅ Explicit null handling

# Always unpersist
df.cache()
# ... use df ...
df.unpersist()  # ✅ Clean up memory

# Use Structured Streaming
stream = spark.readStream.format("kafka").load()  # ✅ Structured Streaming
```

## 🔍 Troubleshooting Quick Lookup

| Error/Issue | Likely Cause | Solution |
|-------------|--------------|----------|
| **OutOfMemoryError (Driver)** | Collected large DataFrame | Use `foreachPartition` or `mapPartitions` |
| **OutOfMemoryError (Executor)** | Too much data per partition | Increase executor memory or repartition |
| **Task not serializable** | Non-serializable object in closure | Use broadcast variables or move logic |
| **Too many small partitions** | Excessive repartitioning | Use `coalesce()` or reduce partition count |
| **Data skew** | Uneven key distribution | Use AQE skew join or repartition with salt |
| **Slow joins** | Large table joins | Use broadcast for small tables, enable AQE |
| **Streaming query stopped** | Checkpoint corruption | Clear checkpoint or use new location |
| **Watermark not working** | Incorrect timestamp column | Use `to_timestamp()` to convert |
| **Schema mismatch** | Type incompatibility | Cast columns to correct types |
| **Broadcast timeout** | Table too large | Increase broadcast threshold or don't broadcast |
| **Partition discovery failed** | Invalid path or permissions | Check path and permissions |
| **Serialization error** | Kryo not configured | Enable Kryo serializer |

## 📊 Data Types & Conversions

### Common Data Types

```python
from pyspark.sql.types import (
    StringType, IntegerType, LongType, DoubleType, FloatType,
    BooleanType, DateType, TimestampType, DecimalType,
    ArrayType, MapType, StructType, StructField
)

# Define schema
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), False),
    StructField("amount", DoubleType(), True),
    StructField("tags", ArrayType(StringType()), True),
    StructField("metadata", MapType(StringType(), StringType()), True)
])
```

### Type Conversions

```python
from pyspark.sql.functions import col, to_date, to_timestamp, cast
from pyspark.sql.types import IntegerType, StringType

# String to number
df = df.withColumn("age_int", col("age_str").cast(IntegerType()))

# Number to string
df = df.withColumn("id_str", col("id").cast(StringType()))

# String to date
df = df.withColumn("date", to_date(col("date_string"), "yyyy-MM-dd"))

# String to timestamp
df = df.withColumn("timestamp", to_timestamp(col("ts_string"), "yyyy-MM-dd HH:mm:ss"))

# Date to string
from pyspark.sql.functions import date_format
df = df.withColumn("date_str", date_format(col("date"), "yyyy-MM-dd"))
```

### Null Handling

```python
from pyspark.sql.functions import col, isnull, coalesce, when, isnan

# Check for null
df.filter(col("column").isNotNull())
df.filter(col("column").isNull())

# Replace nulls
df = df.withColumn("value", coalesce(col("value"), col("default"), lit(0)))

# Conditional null handling
df = df.withColumn(
    "value",
    when(col("value").isNull(), 0).otherwise(col("value"))
)

# Handle NaN (for numeric columns)
df = df.filter(~isnan(col("numeric_column")))
```

## 🎓 Best Practices Checklist

### Before Production

- [ ] **Adaptive Query Execution (AQE)** enabled
- [ ] **Dynamic allocation** enabled for cost optimization
- [ ] **Broadcast joins** used for small tables (< 10MB)
- [ ] **Partitioning strategy** optimized (avoid too many small partitions)
- [ ] **Caching** applied to frequently reused DataFrames
- [ ] **Checkpointing** configured for long-running streaming jobs
- [ ] **Watermarks** set appropriately for streaming windows
- [ ] **Error handling** implemented for production resilience
- [ ] **Logging** configured with PySparkLogger
- [ ] **Testing** strategy in place using pyspark.testing
- [ ] **DataFrame API** used instead of RDD API
- [ ] **Built-in functions** preferred over UDFs
- [ ] **Schema defined** explicitly when possible
- [ ] **Resource limits** configured appropriately

### Code Quality

- [ ] **No RDD API** in production code
- [ ] **No collect()** for large DataFrames
- [ ] **Proper null handling** in filters and joins
- [ ] **Descriptive variable names**
- [ ] **Comments** for complex logic
- [ ] **Error handling** where appropriate
- [ ] **No hardcoded values** (use configs)
- [ ] **Cached DataFrames unpersisted** when done
- [ ] **Broadcast variables** used for small lookups
- [ ] **Partitioning** optimized for data size

## 🔗 Quick Links to Documentation

| Topic | File |
|-------|------|
| **Quick Start** | `.github/kb/spark/01-quick-start/quick-start.md` |
| **DataFrames** | `.github/kb/spark/03-sql-dataframes-datasets/sql-dataframes-datasets.md` |
| **PySpark Quickstart** | `.github/kb/spark/06-pyspark-quickstart/01-quickstart-dataframe.md` |
| **Structured Streaming** | `.github/kb/spark/04-structured-streaming/img/structuredstreaming.md` |
| **SparkSQL** | `.github/kb/spark/07-spark-sql/` |
| **Window Functions** | `.github/kb/spark/10-spark-api-reference/10-sql-sql-spark-window.md` |
| **Resource Management** | `.github/kb/spark/13-spark-resource-management/01-spark-resource-management.md` |
| **Error Handling** | `.github/kb/spark/14-spark-errors/01-spark-errors.md` |
| **Logging** | `.github/kb/spark/15-spark-logger/01-spark-logger.md` |
| **Testing** | `.github/kb/spark/16-spark-testing/01-spark-testing.md` |
| **User Guide** | `.github/kb/spark/09-spark-user-guide/chapter01-dataframes.md` |
| **Full Index** | `.github/kb/spark/index.md` |

## 💡 Pro Tips

1. **Always use DataFrame API** instead of RDD API for better performance
2. **Enable AQE** for automatic query optimization
3. **Use broadcast joins** for small tables (< 10MB)
4. **Cache frequently used DataFrames** but remember to unpersist
5. **Use coalesce()** to reduce partitions without shuffle
6. **Prefer built-in functions** over UDFs when possible
7. **Set watermarks** appropriately for streaming windows
8. **Use SparkSQL** for complex queries
9. **Define schemas explicitly** for better performance
10. **Monitor Spark UI** for performance insights
11. **Use dynamic allocation** for cost optimization
12. **Handle nulls explicitly** in filters and joins
13. **Test with representative data volumes** before production
14. **Use checkpointing** for fault tolerance in streaming
15. **Review execution plans** with `df.explain(True)`

## 🚨 RDD API Warning

⚠️ **RDD API should NOT be used in production code**

- RDD concepts are for understanding Spark's architecture only
- Always prefer DataFrame API for better performance and optimization
- Spark Connect (4.0+) does not support direct RDD operations
- If you see RDD code, convert it to DataFrame API

**Conversion Example:**
```python
# ❌ RDD API
rdd = spark.sparkContext.parallelize([1, 2, 3, 4, 5])
rdd_filtered = rdd.filter(lambda x: x > 2)
result = rdd_filtered.collect()

# ✅ DataFrame API
df = spark.createDataFrame([(1,), (2,), (3,), (4,), (5,)], ["value"])
df_filtered = df.filter(col("value") > 2)
result = df_filtered.collect()
```

---

**For detailed information, see the full documentation in `.github/kb/spark/`**





