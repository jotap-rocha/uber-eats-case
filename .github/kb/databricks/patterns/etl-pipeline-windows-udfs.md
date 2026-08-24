# ETL Pipeline — janelas, UDFs, Delta write e erros

> **Purpose**: Continuação de [etl-pipeline.md](etl-pipeline.md).  
> **MCP Validated**: 2026-04-20

## Implementation (continuação)

```python
# ─── STEP 4: Window Functions ─────────────────────────────────────────────────

customer_spend = enriched.groupBy("customer_id", "country") \
    .agg(_sum("amount").alias("total_spend"))

window_country = Window.partitionBy("country").orderBy(col("total_spend").desc())
ranked = customer_spend \
    .withColumn("country_rank", rank().over(window_country)) \
    .withColumn("spend_percentile", F.percent_rank().over(window_country))

window_daily = Window.partitionBy("customer_id").orderBy("order_date")
customer_history = enriched \
    .withColumn("running_spend",
        F.sum("amount").over(window_daily.rowsBetween(
            Window.unboundedPreceding, Window.currentRow))) \
    .withColumn("prev_order_amount", lag("amount", 1).over(window_daily)) \
    .withColumn("days_since_last_order",
        F.datediff(col("order_date"), lag("order_date", 1).over(window_daily)))

# ─── STEP 5: UDFs (use sparingly — prefer built-in functions) ─────────────────

@udf(returnType=StringType())
def classify_email_domain(email: str) -> str:
    if email is None:
        return "unknown"
    domain = email.split("@")[-1].lower()
    if domain in ["gmail.com", "yahoo.com", "hotmail.com"]:
        return "personal"
    return "business"

import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf(DoubleType())
def normalize_amount(amount: pd.Series) -> pd.Series:
    return (amount - amount.mean()) / amount.std()

enriched = enriched \
    .withColumn("email_type", classify_email_domain(col("email"))) \
    .withColumn("amount_normalized", normalize_amount(col("amount")))

# ─── STEP 6: Write to Delta ───────────────────────────────────────────────────

(enriched.write
    .format("delta")
    .mode("overwrite")
    .option("overwriteSchema", "true")
    .partitionBy("year", "month")
    .saveAsTable("prod_catalog.silver.enriched_orders"))

print(f"ETL complete. Wrote {enriched.count()} rows.")
```

## Error Handling

```python
from pyspark.sql.functions import col, when

df = spark.read \
    .option("mode", "PERMISSIVE") \
    .option("columnNameOfCorruptRecord", "_corrupt_record") \
    .schema(orders_schema.add("_corrupt_record", StringType())) \
    .csv("/Volumes/catalog/schema/vol/landing/orders/")

valid_df = df.filter(col("_corrupt_record").isNull()).drop("_corrupt_record")
invalid_df = df.filter(col("_corrupt_record").isNotNull())
invalid_df.write.format("delta").mode("append").saveAsTable("prod_catalog.bronze.orders_errors")
```

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `spark.sql.files.maxPartitionBytes` | `128MB` | Target partition size |
| `spark.sql.shuffle.partitions` | `200` | Shuffle partitions (set to 2-4x cores) |
| `spark.databricks.delta.optimizeWrite.enabled` | `true` | Auto-compact small writes |

## See Also

- [etl-pipeline.md](etl-pipeline.md)
