# Change Data Capture (CDC) in Lakeflow

> Source: https://docs.databricks.com/aws/en/dlt/cdc

## Overview

Change Data Capture (CDC) processes data changes from change data feeds or database snapshots, enabling incremental data processing and historical tracking.

## CDC APIs

### 1. AUTO CDC
Processes changes from a change data feed (CDF)

### 2. AUTO CDC FROM SNAPSHOT
Processes changes in database snapshots (Python only, Public Preview)

## SCD Type Processing

### SCD Type 1
**Update records directly. History is not retained for updated records.**

```python
dlt.create_auto_cdc_flow(
    target="customers",
    source="customers_cdc_stream",
    keys=["customer_id"],
    sequence_by=col("timestamp"),
    stored_as_scd_type=1
)
```

**Use cases:**
- Current state tracking
- No historical analysis needed
- Storage optimization

### SCD Type 2
**Retain a history of records on all updates or on updates to a specified set of columns**

```python
dlt.create_auto_cdc_flow(
    target="customers_history",
    source="customers_cdc_stream",
    keys=["customer_id"],
    sequence_by=col("timestamp"),
    stored_as_scd_type=2
)
```

**Generated columns:**
- `__START_AT`: When record became active
- `__END_AT`: When record became inactive (NULL for current)
- `__IS_CURRENT`: Boolean flag for current record

**Use cases:**
- Audit trails
- Historical analysis
- Point-in-time queries
- Compliance requirements

## Sequencing Requirements

### Single Column Sequencing

```python
sequence_by=col("timestamp")
```

### Multiple Column Sequencing

```python
sequence_by=struct("date", "sequence_number")
```

### Critical Rules

✅ **DO:**
- Use sortable data types (timestamps, integers, dates)
- Ensure one distinct update per key at each sequencing value
- Handle timezone consistency for timestamps

❌ **DON'T:**
- Use NULL sequencing values (unsupported)
- Have duplicate sequence values for the same key
- Mix timezone-aware and timezone-naive timestamps

## Complete Python Example

```python
import dlt
from pyspark.sql import functions as F

# Bronze: Raw CDC events
@dlt.table()
def users_cdc_bronze():
    return (
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format", "json")
        .load("s3://bucket/cdc/users/")
    )

# Silver: Cleaned CDC events
@dlt.table()
@dlt.expect_or_drop("valid_operation", "operation IN ('INSERT', 'UPDATE', 'DELETE')")
@dlt.expect_or_drop("valid_sequence", "sequence_num IS NOT NULL")
def users_cdc_silver():
    return dlt.read_stream("users_cdc_bronze")

# Gold: Current state (SCD Type 1)
dlt.create_streaming_table("users_current")

dlt.apply_changes(
    target="users_current",
    source="users_cdc_silver",
    keys=["user_id"],
    sequence_by="sequence_num",
    apply_as_deletes=F.expr("operation = 'DELETE'"),
    except_column_list=["operation", "sequence_num"],
    stored_as_scd_type=1
)

# Gold: Historical tracking (SCD Type 2)
dlt.create_streaming_table("users_history")

dlt.apply_changes(
    target="users_history",
    source="users_cdc_silver",
    keys=["user_id"],
    sequence_by="sequence_num",
    apply_as_deletes=F.expr("operation = 'DELETE'"),
    except_column_list=["operation", "sequence_num"],
    stored_as_scd_type=2
)
```

## Complete SQL Example

```sql
-- Bronze: Raw CDC events
CREATE OR REFRESH STREAMING TABLE users_cdc_bronze
AS SELECT *
FROM STREAM read_files("s3://bucket/cdc/users/", format => "json")

-- Silver: Cleaned CDC events
CREATE OR REFRESH STREAMING TABLE users_cdc_silver(
    CONSTRAINT valid_operation
    EXPECT (operation IN ('INSERT', 'UPDATE', 'DELETE'))
    ON VIOLATION DROP ROW,

    CONSTRAINT valid_sequence
    EXPECT (sequence_num IS NOT NULL)
    ON VIOLATION DROP ROW
)
AS SELECT * FROM STREAM users_cdc_bronze

-- Gold: Current state (SCD Type 1)
CREATE OR REFRESH STREAMING TABLE users_current;

APPLY CHANGES INTO users_current
FROM STREAM users_cdc_silver
KEYS (user_id)
SEQUENCE BY sequence_num
COLUMNS * EXCEPT (operation, sequence_num)
STORED AS SCD TYPE 1

-- Gold: Historical tracking (SCD Type 2)
CREATE OR REFRESH STREAMING TABLE users_history;

APPLY CHANGES INTO users_history
FROM STREAM users_cdc_silver
KEYS (user_id)
SEQUENCE BY sequence_num
COLUMNS * EXCEPT (operation, sequence_num)
STORED AS SCD TYPE 2
```

## Advanced Features

### Delete Handling

```python
apply_as_deletes=F.expr("operation = 'DELETE'")
```

### Track Specific Columns (SCD Type 2)

```python
dlt.apply_changes(
    target="users_history",
    source="users_cdc_silver",
    keys=["user_id"],
    sequence_by="sequence_num",
    track_history_column_list=["email", "phone"],  # Only track these columns
    stored_as_scd_type=2
)
```

### Exclude Columns from Target

```python
except_column_list=["operation", "timestamp", "source_system"]
```

## Out-of-Sequence Record Handling

CDC automatically handles out-of-order events using the sequence column:

```python
# Events arrive: sequence 3, 1, 2
# Lakeflow processes them in order: 1, 2, 3
sequence_by="timestamp"
```

## Requirements

- **Edition**: Serverless DLT or Pro/Advanced editions
- **Runtime**: Specific cloud and runtime environments
- **Sequencing column**: Must be sortable data type
- **Keys**: Must uniquely identify records

## Limitations

❌ NULL sequencing values not supported
❌ Requires one distinct update per key at each sequence value
❌ Must use supported data types for sequencing

## Best Practices

1. **Choose the right SCD type**:
   - Type 1 for current state
   - Type 2 for historical tracking

2. **Use appropriate sequence columns**:
   - Timestamps for time-based ordering
   - Auto-increment IDs for insertion ordering
   - Composite keys when needed

3. **Handle deletes explicitly**:
   - Define delete conditions clearly
   - Test delete logic thoroughly

4. **Monitor CDC performance**:
   - Track update latency
   - Monitor out-of-order event counts
   - Optimize sequence column indexing

5. **Test with edge cases**:
   - Out-of-order events
   - Duplicate sequence values
   - Late-arriving data
   - Delete operations
