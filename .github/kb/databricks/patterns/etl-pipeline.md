# ETL Pipeline with PySpark

> **Purpose**: Complete PySpark ETL — schema definition, multi-source reads, transformations, window functions, UDFs, Delta write
> **MCP Validated**: 2026-04-20

## When to Use

- Building batch data pipelines on Databricks
- Reading from multiple source formats (CSV, JSON, Parquet, Delta)
- Applying complex transformations before writing to Delta
- Migrating existing ETL from on-premise Spark or SQL

## Implementation

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import (
    StructType, StructField, StringType, IntegerType,
    DoubleType, TimestampType, BooleanType, ArrayType
)
from pyspark.sql.functions import (
    col, lit, when, coalesce, to_timestamp, to_date,
    trim, upper, lower, regexp_replace, split, explode,
    year, month, dayofmonth, date_format,
    sum as _sum, count, avg, max as _max, min as _min,
    rank, dense_rank, row_number, lag, lead,
    udf, pandas_udf
)
from pyspark.sql.window import Window
import pyspark.sql.functions as F

spark = SparkSession.builder.getOrCreate()

# ─── STEP 1: Schema Definitions (explicit = production-safe) ─────────────────

orders_schema = StructType([
    StructField("order_id",    StringType(),    nullable=False),
    StructField("customer_id", StringType(),    nullable=False),
    StructField("product_id",  StringType(),    nullable=True),
    StructField("amount",      DoubleType(),    nullable=True),
    StructField("quantity",    IntegerType(),   nullable=True),
    StructField("status",      StringType(),    nullable=True),
    StructField("order_ts",    StringType(),    nullable=True),
    StructField("tags",        StringType(),    nullable=True),  # comma-separated
])

customers_schema = StructType([
    StructField("customer_id", StringType(),  nullable=False),
    StructField("name",        StringType(),  nullable=True),
    StructField("email",       StringType(),  nullable=True),
    StructField("country",     StringType(),  nullable=True),
    StructField("created_at",  StringType(),  nullable=True),
    StructField("is_premium",  BooleanType(), nullable=True),
])

# ─── STEP 2: Read from Multiple Sources ──────────────────────────────────────

# CSV
orders_df = spark.read \
    .schema(orders_schema) \
    .option("header", "true") \
    .option("nullValue", "NULL") \
    .option("timestampFormat", "yyyy-MM-dd HH:mm:ss") \
    .csv("/Volumes/catalog/schema/vol/landing/orders/")

# JSON
events_df = spark.read \
    .option("multiLine", "false") \
    .option("inferSchema", "false") \
    .json("/Volumes/catalog/schema/vol/landing/events/")

# Parquet
products_df = spark.read \
    .parquet("/Volumes/catalog/schema/vol/reference/products/")

# Delta table
customers_df = spark.table("prod_catalog.silver.customers")

# ─── STEP 3: Transformations ──────────────────────────────────────────────────

# Cast, clean, filter
cleaned_orders = (orders_df
    .filter(col("order_id").isNotNull())
    .filter(col("amount") > 0)
    .withColumn("order_ts",   to_timestamp("order_ts", "yyyy-MM-dd HH:mm:ss"))
    .withColumn("order_date", to_date("order_ts"))
    .withColumn("year",       year("order_ts"))
    .withColumn("month",      month("order_ts"))
    .withColumn("status",     trim(upper("status")))
    .withColumn("amount",     coalesce(col("amount"), lit(0.0)))
    # Explode array column (tags = "tag1,tag2,tag3")
    .withColumn("tags_array", split(col("tags"), ","))
    .withColumn("tag",        explode("tags_array"))
    .drop("tags", "tags_array"))

# Join orders with customers (left join to keep all orders)
enriched = cleaned_orders.alias("o") \
    .join(customers_df.alias("c"), "customer_id", "left") \
    .join(products_df.alias("p"), "product_id", "left") \
    .select(
        col("o.order_id"),
        col("o.customer_id"),
        col("c.name").alias("customer_name"),
        col("c.country"),
        col("c.is_premium"),
        col("p.category").alias("product_category"),
        col("o.amount"),
        col("o.quantity"),
        col("o.status"),
        col("o.order_date"),
        col("o.year"),
        col("o.month"),
        col("o.tag"),
    )

# Derived columns with conditional logic
enriched = enriched \
    .withColumn("revenue_tier",
        when(col("amount") >= 1000, "high")
        .when(col("amount") >= 100,  "medium")
        .otherwise("low")) \
    .withColumn("is_international",
        when(col("country") != "US", True).otherwise(False))
```

*Window functions*, UDFs, escrita Delta, tratamento de erros e configuração — ver [etl-pipeline-windows-udfs.md](etl-pipeline-windows-udfs.md).

## See Also

- [patterns/medallion-architecture.md](medallion-architecture.md)
- [patterns/spark-optimization.md](spark-optimization.md)
- [concepts/delta-lake.md](../concepts/delta-lake.md)
