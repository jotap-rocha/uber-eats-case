# Databricks Feature Store (Mosaic AI Feature Store)

> **Purpose**: Master Databricks Feature Store — feature tables, point-in-time lookups, training sets, and online store
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

Mosaic AI Feature Store (formerly Databricks Feature Store) centralizes feature engineering for ML. Feature tables are Delta tables with metadata enabling reuse across models, point-in-time lookups to prevent data leakage, and online serving for low-latency inference. Feature tables live in Unity Catalog (DBR 13.1+).

## Creating Feature Tables

```python
from databricks.feature_engineering import FeatureEngineeringClient

fe = FeatureEngineeringClient()

# Compute features as a DataFrame
def compute_customer_features(df):
    return (df
        .groupBy("customer_id")
        .agg(
            F.count("order_id").alias("total_orders"),
            F.sum("amount").alias("total_spend"),
            F.avg("amount").alias("avg_order_value"),
            F.max("order_date").alias("last_order_date"),
        ))

customer_features = compute_customer_features(orders_df)

# Create feature table in Unity Catalog
fe.create_table(
    name="main.feature_store.customer_features",
    primary_keys=["customer_id"],
    timestamp_keys=["snapshot_date"],  # For point-in-time lookups
    df=customer_features,
    description="Customer-level behavioral features for fraud detection",
)
```

## Writing Features

```python
# Write (upsert) new feature values
fe.write_table(
    name="main.feature_store.customer_features",
    df=updated_features,
    mode="merge",   # merge = upsert; overwrite = full replace
)

# Append new time-series snapshots
fe.write_table(
    name="main.feature_store.customer_features",
    df=daily_snapshot,
    mode="merge",
)
```

## Point-in-Time Lookups (Preventing Data Leakage)

```python
from databricks.feature_engineering import FeatureLookup

# Labels DataFrame with event timestamps
labels_df = spark.table("main.ml.fraud_labels")
# Columns: customer_id, event_ts, is_fraud

# Define feature lookups
feature_lookups = [
    FeatureLookup(
        table_name="main.feature_store.customer_features",
        feature_names=["total_orders", "total_spend", "avg_order_value"],
        lookup_key="customer_id",
        timestamp_lookup_key="event_ts",  # Point-in-time: features at event time
    ),
    FeatureLookup(
        table_name="main.feature_store.device_features",
        feature_names=["device_risk_score", "ip_country"],
        lookup_key="device_id",
        # No timestamp_lookup_key = latest feature value
    ),
]

# Create training set — handles point-in-time join automatically
training_set = fe.create_training_set(
    df=labels_df,
    feature_lookups=feature_lookups,
    label="is_fraud",
    exclude_columns=["event_ts"],
)

training_df = training_set.load_df()
```

## Treino com Feature Store, *online store* e matriz de decisão

Continuação: [feature-store-training-online.md](feature-store-training-online.md).

## Related

- [concepts/mlflow.md](mlflow.md)
- [patterns/mlops-pipeline.md](../patterns/mlops-pipeline.md)
