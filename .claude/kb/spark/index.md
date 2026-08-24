# Apache Spark Knowledge Base

**Comprehensive documentation for Apache Spark, SparkSQL, and PySpark**

## 📚 Documentation Structure

### [01 - Quick Start](01-quick-start/)
- **[quick-start.md](01-quick-start/quick-start.md)** - Introduction to Spark, interactive shell, basic operations

### [02 - RDD Concepts](02-rdd-accumulators-broadcasts-vars/)
- **[rdd-accumulators-broadcasts-vars.md](02-rdd-accumulators-broadcasts-vars/rdd-accumulators-broadcasts-vars.md)** - RDD concepts (for understanding only), accumulators, broadcast variables
- **Note:** RDD API should not be used in production code. Use DataFrame API instead.

### [03 - SQL, DataFrames and Datasets](03-sql-dataframes-datasets/)
- **[sql-dataframes-datasets.md](03-sql-dataframes-datasets/sql-dataframes-datasets.md)** - SparkSQL, DataFrame API, Dataset API, unified execution engine

### [04 - Structured Streaming](04-structured-streaming/)
- **[structuredstreaming.md](04-structured-streaming/img/structuredstreaming.md)** - Streaming DataFrames, micro-batch processing, continuous processing, watermarks, windowing

### [05 - Spark Streaming (Legacy)](05-spark-streaming-guide/)
- **[spark-streaming-guide.md](05-spark-streaming-guide/spark-streaming-guide.md)** - Legacy DStreams API (use Structured Streaming for new projects)

### [06 - PySpark Quickstart](06-pyspark-quickstart/)
- **[01-quickstart-dataframe.md](06-pyspark-quickstart/01-quickstart-dataframe.md)** - PySpark DataFrame API quickstart
- **[02-quickstart-spark-connect.md](06-pyspark-quickstart/02-quickstart-spark-connect.md)** - Spark Connect for remote Spark sessions
- **[03-quickstart-pandas-api-spark.md](06-pyspark-quickstart/03-quickstart-pandas-api-spark.md)** - Pandas API on Spark quickstart

### [07 - Spark SQL](07-spark-sql/)
- **[01-spark-sql-apachearrow.md](07-spark-sql/01-spark-sql-apachearrow.md)** - Apache Arrow integration for Python performance
- **[02-spark-sql-python-userdefined-table-functions.md](07-spark-sql/02-spark-sql-python-userdefined-table-functions.md)** - User Defined Table Functions (UDTF)
- **[03-spark-sql-python-data-type-convertions.md](07-spark-sql/03-spark-sql-python-data-type-convertions.md)** - Python to Spark data type conversions
- **[04-spark-sql-python-to-spark-type-conversions.md](07-spark-sql/04-spark-sql-python-to-spark-type-conversions.md)** - Type conversion reference

### [08 - Pandas API on Spark](08-spark-pandas-api-on-spark/)
- **[01-spark-pandas-options-settings.md](08-spark-pandas-api-on-spark/01-spark-pandas-options-settings.md)** - Configuration and options
- **[02-spark-pandas-pyspark-dataframes.md](08-spark-pandas-api-on-spark/02-spark-pandas-pyspark-dataframes.md)** - Converting between Pandas and PySpark DataFrames
- **[03-spark-pandas-transform-apply-functions.md](08-spark-pandas-api-on-spark/03-spark-pandas-transform-apply-functions.md)** - Transform and apply functions
- **[04-spark-pandas-type-support-pandas-api-spark.md](08-spark-pandas-api-on-spark/04-spark-pandas-type-support-pandas-api-spark.md)** - Type support and compatibility
- **[05-spark-pandas-type-hints-pandas-api-spark.md](08-spark-pandas-api-on-spark/05-spark-pandas-type-hints-pandas-api-spark.md)** - Type hints support
- **[06-spark-pandas-from-to-other-DBMSes.md](08-spark-pandas-api-on-spark/06-spark-pandas-from-to-other-DBMSes.md)** - Database connectivity
- **[07-spark-pandas-best-practices.md](08-spark-pandas-api-on-spark/07-spark-pandas-best-practices.md)** - Best practices and performance tips
- **[08-spark-pandas-supported-pandas-api.md](08-spark-pandas-api-on-spark/08-spark-pandas-supported-pandas-api.md)** - Supported Pandas API reference
- **[09-spark-pandas.faq.md](08-spark-pandas-api-on-spark/09-spark-pandas.faq.md)** - Frequently asked questions

### [09 - Spark User Guide](09-spark-user-guide/)
- **[chapter01-dataframes.md](09-spark-user-guide/chapter01-dataframes.md)** - DataFrames fundamentals
- **[chapter02-pyspark-datatypes.md](09-spark-user-guide/chapter02-pyspark-datatypes.md)** - PySpark data types
- **[chapter03-functions-junctions.md](09-spark-user-guide/chapter03-functions-junctions.md)** - Built-in functions and operations
- **[chapter04-bug-busting.md](09-spark-user-guide/chapter04-bug-busting.md)** - Debugging and troubleshooting
- **[chapter05-unleasing-UDFs-UDTs.md](09-spark-user-guide/chapter05-unleasing-UDFs-UDTs.md)** - User Defined Functions and Types
- **[chapter06-oldsql-newtricks-runinmgsqlonspark.md](09-spark-user-guide/chapter06-oldsql-newtricks-runinmgsqlonspark.md)** - Running SQL on Spark
- **[chapter07-load-and-behold-data-loading.md](09-spark-user-guide/chapter07-load-and-behold-data-loading.md)** - Data loading patterns

### [10 - Spark API Reference](10-spark-api-reference/)
- **[01-spark-sql-core-concepts.md](10-spark-api-reference/01-spark-sql-core-concepts.md)** - Core SparkSQL concepts
- **[02-sql-sql-spark-session.md](10-spark-api-reference/02-sql-sql-spark-session.md)** - SparkSession API
- **[03-sql-sql-spark-configuration.md](10-spark-api-reference/03-sql-sql-spark-configuration.md)** - Configuration options
- **[04-sql-sql-spark-input-output.md](10-spark-api-reference/04-sql-sql-spark-input-output.md)** - Input/output operations
- **[05-sql-sql-spark-dataframe.md](10-spark-api-reference/05-sql-sql-spark-dataframe.md)** - DataFrame API reference
- **[06-sql-sql-spark-column.md](10-spark-api-reference/06-sql-sql-spark-column.md)** - Column operations
- **[07-sql-sql-spark-data-types.md](10-spark-api-reference/07-sql-sql-spark-data-types.md)** - Data types reference
- **[08-sql-sql-spark-rows.md](10-spark-api-reference/08-sql-sql-spark-rows.md)** - Row operations
- **[09-sql-sql-spark-functions.md](10-spark-api-reference/09-sql-sql-spark-functions.md)** - Built-in functions
- **[10-sql-sql-spark-window.md](10-spark-api-reference/10-sql-sql-spark-window.md)** - Window functions
- **[11-sql-sql-spark-grouping.md](10-spark-api-reference/11-sql-sql-spark-grouping.md)** - Grouping operations
- **[12-sql-sql-spark-catalog.md](10-spark-api-reference/12-sql-sql-spark-catalog.md)** - Catalog API
- **[13-sql-sql-spark-avro.md](10-spark-api-reference/13-sql-sql-spark-avro.md)** - Avro support
- **[14-sql-sql-spark-observation.md](10-spark-api-reference/14-sql-sql-spark-observation.md)** - Observation API
- **[15-sql-sql-spark-UDF.md](10-spark-api-reference/15-sql-sql-spark-UDF.md)** - User Defined Functions
- **[16-sql-sql-spark-UDTF.md](10-spark-api-reference/16-sql-sql-spark-UDTF.md)** - User Defined Table Functions
- **[17-sql-sql-spark-variantVal.md](10-spark-api-reference/17-sql-sql-spark-variantVal.md)** - Variant data type
- **[18-sql-sql-spark-protobuf.md](10-spark-api-reference/18-sql-sql-spark-protobuf.md)** - Protobuf support
- **[19-sql-sql-spark-python-datasource.md](10-spark-api-reference/19-sql-sql-spark-python-datasource.md)** - Python data sources
- **[20-sql-sql-spark-stateful-processor.md](10-spark-api-reference/20-sql-sql-spark-stateful-processor.md)** - Stateful processing

### [11 - Pandas API on Spark Reference](11-pandas-api-on-spark/)
- **[01-pandas-api-on-spark-input-output.md](11-pandas-api-on-spark/01-pandas-api-on-spark-input-output.md)** - I/O operations
- **[02-pandas-api-on-spark-general-function.md](11-pandas-api-on-spark/02-pandas-api-on-spark-general-function.md)** - General functions
- **[03-pandas-api-on-spark-series.md](11-pandas-api-on-spark/03-pandas-api-on-spark-series.md)** - Series operations
- **[04-pandas-api-on-spark-dataframe.md](11-pandas-api-on-spark/04-pandas-api-on-spark-dataframe.md)** - DataFrame operations
- **[05-pandas-api-on-spark-index-objetcs.md](11-pandas-api-on-spark/05-pandas-api-on-spark-index-objetcs.md)** - Index objects
- **[06-pandas-api-on-spark-window.md](11-pandas-api-on-spark/06-pandas-api-on-spark-window.md)** - Window operations
- **[07-pandas-api-on-spark-groupby.md](11-pandas-api-on-spark/07-pandas-api-on-spark-groupby.md)** - GroupBy operations
- **[08-pandas-api-on-spark-resampling.md](11-pandas-api-on-spark/08-pandas-api-on-spark-resampling.md)** - Time series resampling
- **[09-pandas-api-on-spark-options-and-settings.md](11-pandas-api-on-spark/09-pandas-api-on-spark-options-and-settings.md)** - Options and settings
- **[10-pandas-api-on-spark-machine-learning-utilities.md](11-pandas-api-on-spark/10-pandas-api-on-spark-machine-learning-utilities.md)** - ML utilities
- **[11-pandas-api-on-spark-extensions.md](11-pandas-api-on-spark/11-pandas-api-on-spark-extensions.md)** - Extensions
- **[12-pandas-api-on-spark-testing.md](11-pandas-api-on-spark/12-pandas-api-on-spark-testing.md)** - Testing utilities

### [12 - Spark Core](12-spark-core/)
- **[01-spark-core.md](12-spark-core/01-spark-core.md)** - SparkContext, SparkSession, core concepts

### [13 - Resource Management](13-spark-resource-management/)
- **[01-spark-resource-management.md](13-spark-resource-management/01-spark-resource-management.md)** - Resource profiles, executor/task resource requests, GPU support

### [14 - Error Handling](14-spark-errors/)
- **[01-spark-errors.md](14-spark-errors/01-spark-errors.md)** - Exception classes, error handling, troubleshooting

### [15 - Logging](15-spark-logger/)
- **[01-spark-logger.md](15-spark-logger/01-spark-logger.md)** - PySparkLogger, structured JSON logging

### [16 - Testing](16-spark-testing/)
- **[01-spark-testing.md](16-spark-testing/01-spark-testing.md)** - Testing utilities, assertDataFrameEqual, assertSchemaEqual

## 🚀 Quick Start

### Create Your First Spark Application (PySpark)

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, count

# Create SparkSession
spark = SparkSession.builder \
    .appName("MyFirstApp") \
    .getOrCreate()

# Read data
df = spark.read.parquet("path/to/data")

# Transformations
df_filtered = df.filter(col("age") > 18)
df_aggregated = df.groupBy("category").agg(
    sum("amount").alias("total"),
    count("*").alias("count")
)

# Write data
df_aggregated.write.mode("overwrite").parquet("path/to/output")
```

### Create Your First Spark Application (SparkSQL)

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyFirstApp") \
    .getOrCreate()

# Register DataFrame as temporary view
df = spark.read.parquet("path/to/data")
df.createOrReplaceTempView("my_table")

# Execute SQL query
result = spark.sql("""
    SELECT 
        category,
        SUM(amount) as total,
        COUNT(*) as count
    FROM my_table
    WHERE age > 18
    GROUP BY category
    ORDER BY total DESC
""")

# Write result
result.write.mode("overwrite").parquet("path/to/output")
```

### Structured Streaming Example

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import window, col, count, to_timestamp

spark = SparkSession.builder \
    .appName("StreamingApp") \
    .getOrCreate()

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

## 🎯 Common Patterns

### Pattern 1: ETL Pipeline
```
Read → Transform → Write
```

### Pattern 2: Broadcast Join
```python
from pyspark.sql.functions import broadcast

# Broadcast small lookup table
df_large = spark.read.parquet("path/to/large/table")
df_small = spark.read.parquet("path/to/small/lookup")

df_joined = df_large.join(
    broadcast(df_small),
    df_large.id == df_small.id,
    "left"
)
```

### Pattern 3: Window Functions
```python
from pyspark.sql import Window
from pyspark.sql.functions import row_number, lag, sum

window_spec = Window.partitionBy("category").orderBy("date")

df = df.withColumn("row_num", row_number().over(window_spec))
df = df.withColumn("prev_value", lag("amount", 1).over(window_spec))
df = df.withColumn("running_total", sum("amount").over(
    Window.partitionBy("category")
         .orderBy("date")
         .rowsBetween(Window.unboundedPreceding, Window.currentRow)
))
```

### Pattern 4: Caching for Reuse
```python
# Cache frequently used DataFrame
df_expensive = expensive_operation(df).cache()

# Use cached DataFrame multiple times
df1 = df_expensive.filter(...)
df2 = df_expensive.groupBy(...)

# Unpersist when done
df_expensive.unpersist()
```

## 🔑 Key Concepts

| Concept | Description |
|---------|-------------|
| **DataFrame** | Distributed collection of data organized into named columns (primary API) |
| **SparkSQL** | SQL interface for querying DataFrames |
| **Structured Streaming** | Scalable and fault-tolerant stream processing engine |
| **Catalyst Optimizer** | Query optimization engine that optimizes DataFrame operations |
| **Tungsten** | Execution engine with code generation and columnar storage |
| **Adaptive Query Execution (AQE)** | Runtime optimization that adjusts query plans based on runtime statistics |
| **Broadcast Join** | Efficient join strategy for small tables |
| **Partitioning** | Data distribution strategy across cluster nodes |
| **Watermark** | Time-based threshold for handling late data in streaming |
| **Checkpointing** | Fault tolerance mechanism for streaming queries |

## 💡 Best Practices

### ✅ DO
1. **Use DataFrame API** instead of RDD API for better performance
2. **Enable Adaptive Query Execution (AQE)** for automatic optimization
3. **Use broadcast joins** for small tables (< 10MB)
4. **Cache frequently used DataFrames** to avoid recomputation
5. **Set appropriate partitioning** (avoid too many small partitions)
6. **Use built-in functions** instead of UDFs when possible
7. **Configure watermarks** appropriately for streaming windows
8. **Set up checkpointing** for long-running streaming jobs
9. **Use SparkSQL** for complex queries when appropriate
10. **Monitor Spark UI** for performance insights

### ❌ DON'T
1. **Don't use RDD API** in production code (use DataFrame API)
2. **Don't collect large DataFrames** to driver (causes OOM)
3. **Don't create too many partitions** (causes overhead)
4. **Don't skip caching** for DataFrames used multiple times
5. **Don't use Python UDFs** when built-in functions exist
6. **Don't ignore data skew** (use AQE or repartition)
7. **Don't hardcode configurations** (use environment variables)
8. **Don't forget to unpersist** cached DataFrames when done
9. **Don't use legacy DStreams** (use Structured Streaming)
10. **Don't ignore null handling** in filters and joins

## 🎓 Learning Path

### Beginner
1. Read [quick-start.md](01-quick-start/quick-start.md)
2. Follow [01-quickstart-dataframe.md](06-pyspark-quickstart/01-quickstart-dataframe.md)
3. Learn [sql-dataframes-datasets.md](03-sql-dataframes-datasets/sql-dataframes-datasets.md)
4. Practice [chapter01-dataframes.md](09-spark-user-guide/chapter01-dataframes.md)

### Intermediate
5. Master [structuredstreaming.md](04-structured-streaming/img/structuredstreaming.md)
6. Understand [chapter03-functions-junctions.md](09-spark-user-guide/chapter03-functions-junctions.md)
7. Learn window functions [10-sql-sql-spark-window.md](10-spark-api-reference/10-sql-sql-spark-window.md)
8. Study [01-spark-sql-apachearrow.md](07-spark-sql/01-spark-sql-apachearrow.md) for performance

### Advanced
9. Optimize with [13-spark-resource-management.md](13-spark-resource-management/01-spark-resource-management.md)
10. Debug with [chapter04-bug-busting.md](09-spark-user-guide/chapter04-bug-busting.md)
11. Handle errors with [01-spark-errors.md](14-spark-errors/01-spark-errors.md)
12. Test with [01-spark-testing.md](16-spark-testing/01-spark-testing.md)
13. Use logging with [01-spark-logger.md](15-spark-logger/01-spark-logger.md)
14. Explore [20-sql-sql-spark-stateful-processor.md](10-spark-api-reference/20-sql-sql-spark-stateful-processor.md)

## 🔍 MCP Integration

This knowledge base is designed to work with Cursor Code's MCP capabilities:

### Local KB Search (Primary)
```bash
# Grep for specific topics
grep -r "structured streaming" .claude/kb/spark/
grep -r "broadcast" .claude/kb/spark/
grep -r "dataframe" .claude/kb/spark/
```

### MCP Fallback (Real-time Updates)
- `mcp__ref-tools__ref_search_documentation` - Latest Spark documentation
- `mcp__exa__get_code_context_exa` - Real-world Spark examples
- `WebFetch` - Fetch latest Apache Spark docs

### Search Strategy
1. **Local first** - Fast, comprehensive, offline-capable
2. **MCP validation** - Verify latest updates
3. **Web search** - Community solutions, Stack Overflow

## 📊 Quick Reference

### SparkSession Creation
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()
```

### Common DataFrame Operations
```python
# Read
df = spark.read.format("parquet").load("path")
df = spark.read.json("path")
df = spark.read.csv("path", header=True, inferSchema=True)

# Transform
df_filtered = df.filter(col("age") > 18)
df_selected = df.select("name", "age")
df_grouped = df.groupBy("category").agg(sum("amount"))

# Write
df.write.mode("overwrite").parquet("path")
df.write.mode("append").format("delta").save("path")
```

### Common SparkSQL Patterns
```sql
-- Create temporary view
CREATE OR REPLACE TEMP VIEW my_view AS SELECT * FROM table

-- Window functions
SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY date) as rn
FROM table

-- Aggregations
SELECT category, SUM(amount) as total, COUNT(*) as count
FROM table
GROUP BY category
HAVING total > 1000
```

### Streaming Operations
```python
# Read stream
stream = spark.readStream.format("kafka").load()

# Write stream
query = stream.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()
```

### Performance Tuning
```python
# Repartition
df = df.repartition(200)

# Coalesce (no shuffle)
df = df.coalesce(10)

# Cache
df.cache()
df.persist(StorageLevel.MEMORY_AND_DISK)

# Broadcast
from pyspark.sql.functions import broadcast
df = df1.join(broadcast(df2), "key")
```

## 🌐 External Resources

- [Apache Spark Official Documentation](https://spark.apache.org/docs/latest/)
- [PySpark API Reference](https://spark.apache.org/docs/latest/api/python/)
- [Spark SQL Guide](https://spark.apache.org/docs/latest/sql-programming-guide.html)
- [Structured Streaming Guide](https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html)
- [Spark Community](https://spark.apache.org/community.html)

## 📝 Version Info

- **Last Updated**: 2025-01-06
- **Spark Version**: 4.0.1
- **Coverage**: 68+ documentation files
- **Focus**: SparkSQL and PySpark (DataFrame API)

## ⚠️ Important Notes

### RDD API Deprecation
- **RDD API should NOT be used in production code**
- RDD concepts are documented for understanding Spark's architecture only
- Always prefer DataFrame API for better performance and optimization
- Spark Connect (4.0+) does not support direct RDD operations

### Migration Path
- If you see RDD code, convert it to DataFrame API
- Use `df.rdd` only when absolutely necessary (rare cases)
- Prefer built-in functions over UDFs
- Use SparkSQL for complex queries

---

**For questions or issues, use MCP tools to search latest documentation or community resources.**





