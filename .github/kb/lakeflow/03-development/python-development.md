# Python Development for Lakeflow Pipelines

> Source: https://docs.databricks.com/aws/en/dlt/python-dev

## Module Import

```python
import dlt
```

**All Lakeflow Declarative Pipelines Python APIs are implemented in the `dlt` module**

## Core Decorators

### @dlt.table()
Creates materialized views or streaming tables

```python
@dlt.table()
def my_table():
    return spark.read.format("json").load("/path/to/data")
```

### @dlt.view()
Creates temporary views for data transformation

```python
@dlt.view()
def my_temp_view():
    return spark.sql("SELECT * FROM source_table")
```

### @dlt.expect_or_drop()
Validates data quality by setting constraints

```python
@dlt.expect_or_drop("valid_data", "column IS NOT NULL")
@dlt.table()
def clean_data():
    return spark.read.table("raw_data")
```

## Data Loading Patterns

### Batch Loading

```python
@dlt.table()
def batch_table():
    return spark.read.format("json").load("/path/to/data")
```

### Streaming Loading

```python
@dlt.table()
def streaming_table():
    return spark.readStream.format("cloudFiles") \
        .option("cloudFiles.format", "json") \
        .load("/path/to/data")
```

### Auto Loader (Recommended for Cloud Storage)

```python
@dlt.table()
def incremental_load():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "parquet")
        .option("cloudFiles.schemaLocation", "/path/to/schema")
        .load("s3://bucket/path/")
    )
```

## Key Development Patterns

### 1. Functions Must Return DataFrames

```python
@dlt.table()
def my_table():
    # CORRECT: Returns a DataFrame
    return spark.read.table("source")

    # INCORRECT: Does not return a DataFrame
    # df = spark.read.table("source")
```

### 2. Table Names

```python
# Explicit table name
@dlt.table(name="custom_table_name")
def my_function():
    return spark.read.table("source")

# Inferred from function name
@dlt.table()
def orders():  # Table name will be "orders"
    return spark.read.table("raw_orders")
```

### 3. Programmatic Table Creation

```python
# Create multiple tables using loops
tables = ["orders", "customers", "products"]

for table_name in tables:
    @dlt.table(name=f"{table_name}_processed")
    def process_table():
        return spark.read.table(table_name)
```

### 4. Lazy Execution Model

```python
# INCORRECT: This won't work as expected
@dlt.table()
def wrong_pattern():
    df = spark.read.table("source")
    count = df.count()  # Triggers execution too early
    return df

# CORRECT: Keep operations lazy
@dlt.table()
def correct_pattern():
    return spark.read.table("source")
```

## Best Practices

### ✅ DO

1. **Avoid side effects** in dataset definition functions
2. **Ensure additive dataset definitions** in pipelines
3. **Use expectations** for data quality validation
4. **Return DataFrames** from all decorated functions
5. **Use Auto Loader** for incremental ingestion
6. **Leverage streaming** for real-time processing

### ❌ DON'T

1. **Don't trigger actions** (`.count()`, `.collect()`) in pipeline code
2. **Don't use non-deterministic** operations without sequence columns
3. **Don't modify external state** in table definitions
4. **Don't mix batch and streaming** without understanding semantics

## Complete Example

```python
import dlt
from pyspark.sql import functions as F

# Bronze: Raw data ingestion
@dlt.table(
    comment="Raw customer data from cloud storage",
    table_properties={"quality": "bronze"}
)
def customers_bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .option("cloudFiles.schemaLocation", "/tmp/schema/customers")
        .load("s3://bucket/customers/")
    )

# Silver: Data cleaning
@dlt.table(
    comment="Cleaned customer data",
    table_properties={"quality": "silver"}
)
@dlt.expect_or_drop("valid_id", "customer_id IS NOT NULL")
@dlt.expect_or_drop("valid_email", "email LIKE '%@%.%'")
def customers_silver():
    return (
        dlt.read_stream("customers_bronze")
        .select(
            "customer_id",
            "name",
            "email",
            F.current_timestamp().alias("processed_at")
        )
    )

# Gold: Business aggregations
@dlt.table(
    comment="Customer email domains summary",
    table_properties={"quality": "gold"}
)
def customer_domains():
    return (
        spark.read.table("customers_silver")
        .withColumn("domain", F.split(F.col("email"), "@")[1])
        .groupBy("domain")
        .count()
    )
```

## Advanced Features

### Change Data Capture (CDC)

```python
dlt.create_streaming_table("target_table")

dlt.apply_changes(
    target="target_table",
    source="source_cdc_stream",
    keys=["id"],
    sequence_by="timestamp",
    apply_as_deletes=F.expr("operation = 'DELETE'"),
    except_column_list=["operation", "timestamp"]
)
```

### Parameterization

```python
# Access pipeline parameters
catalog = spark.conf.get("catalog_name")
schema = spark.conf.get("schema_name")

@dlt.table()
def parameterized_table():
    return spark.read.table(f"{catalog}.{schema}.source_table")
```
