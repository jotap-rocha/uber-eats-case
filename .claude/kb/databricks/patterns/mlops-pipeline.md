# MLOps Pipeline on Databricks

> **Purpose**: End-to-end MLOps — feature engineering, MLflow training, Model Registry, serving endpoint, monitoring
> **MCP Validated**: 2026-04-20

## When to Use

- Building production ML pipelines on Databricks
- Need experiment tracking, model versioning, and governed deployment
- Integrating Feature Store for reproducible training sets
- Deploying models as REST API endpoints

## Implementation

```python
import mlflow
import mlflow.sklearn
from databricks.feature_engineering import FeatureEngineeringClient, FeatureLookup
from pyspark.sql.functions import col, count, sum as _sum, avg, max as _max, datediff, current_date
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, precision_score, recall_score, f1_score
import pandas as pd
import numpy as np

spark = SparkSession.builder.getOrCreate()
fe = FeatureEngineeringClient()

# ─── STEP 1: Feature Engineering → Feature Store ─────────────────────────────

def compute_customer_features():
    """Compute and store customer behavioral features."""
    orders = spark.table("prod_catalog.silver.orders")
    customers = spark.table("prod_catalog.silver.customers")

    features = (orders
        .filter(col("status") == "COMPLETED")
        .groupBy("customer_id")
        .agg(
            count("order_id").alias("total_orders_90d"),
            _sum("amount").alias("total_spend_90d"),
            avg("amount").alias("avg_order_value_90d"),
            _max("order_date").alias("last_order_date"),
        )
        .withColumn("days_since_last_order",
            datediff(current_date(), col("last_order_date")))
        .join(customers.select("customer_id", "country", "is_premium"), "customer_id"))

    fe.write_table(
        name="prod_catalog.feature_store.customer_features",
        df=features,
        mode="merge",
    )
    return features

# Create or update feature tables
compute_customer_features()

# ─── STEP 2: Build Training Set (Point-in-Time Safe) ─────────────────────────

# Labels: fraud events with timestamps
labels_df = spark.table("prod_catalog.ml_labels.fraud_labels")
# Schema: customer_id, label_ts, is_fraud (target)

feature_lookups = [
    FeatureLookup(
        table_name="prod_catalog.feature_store.customer_features",
        feature_names=[
            "total_orders_90d", "total_spend_90d",
            "avg_order_value_90d", "days_since_last_order",
            "is_premium"
        ],
        lookup_key="customer_id",
        timestamp_lookup_key="label_ts",  # Point-in-time: no data leakage
    ),
]

training_set = fe.create_training_set(
    df=labels_df,
    feature_lookups=feature_lookups,
    label="is_fraud",
    exclude_columns=["label_ts"],
)

training_df = training_set.load_df().toPandas()
X = training_df.drop(columns=["customer_id", "is_fraud"])
y = training_df["is_fraud"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

# ─── STEP 3: Training with MLflow Autolog ────────────────────────────────────

mlflow.set_experiment("/Users/ml-team@company.com/fraud-detection")

with mlflow.start_run(run_name="gbm-v1-fraud-detector") as run:
    # Enable autologging (captures params + metrics automatically)
    mlflow.sklearn.autolog(
        log_input_examples=True,
        log_model_signatures=True,
    )

    # Train model
    model = GradientBoostingClassifier(
        n_estimators=200,
        max_depth=5,
        learning_rate=0.05,
        subsample=0.8,
        random_state=42,
    )
    model.fit(X_train, y_train)

    # Additional custom metrics
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    y_pred = (y_pred_proba > 0.5).astype(int)

    mlflow.log_metrics({
        "test_roc_auc":  roc_auc_score(y_test, y_pred_proba),
        "test_precision": precision_score(y_test, y_pred),
        "test_recall":    recall_score(y_test, y_pred),
        "test_f1":        f1_score(y_test, y_pred),
    })

    # Log feature importance chart
    import matplotlib.pyplot as plt
    feat_importance = pd.Series(model.feature_importances_, index=X.columns)
    fig, ax = plt.subplots(figsize=(10, 6))
    feat_importance.nlargest(15).plot(kind="barh", ax=ax)
    ax.set_title("Top 15 Feature Importances")
    mlflow.log_figure(fig, "feature_importance.png")

    # Log model with Feature Store metadata
    fe.log_model(
        model=model,
        artifact_path="model",
        flavor=mlflow.sklearn,
        training_set=training_set,
        registered_model_name="prod_catalog.ml_models.fraud_detector",
    )

    run_id = run.info.run_id
    print(f"Run ID: {run_id}")
    print(f"ROC-AUC: {roc_auc_score(y_test, y_pred_proba):.4f}")
```

Passos de registro no Registry, *endpoint* e monitorização — ver [mlops-pipeline-registry-serving.md](mlops-pipeline-registry-serving.md).

## Configuration

| Setting | Default | Description |
|---------|---------|-------------|
| `mlflow.autolog` | `True` in Databricks | Auto-capture params/metrics |
| Model alias | `champion` | Active production model |
| Endpoint size | `Small` | 4 vCPU, auto-scales |
| `scale_to_zero_enabled` | `True` | Scales down when idle |

## See Also

- [mlops-pipeline-registry-serving.md](mlops-pipeline-registry-serving.md)
- [patterns/medallion-architecture.md](medallion-architecture.md)
- [concepts/mlflow.md](../concepts/mlflow.md)
- [concepts/feature-store.md](../concepts/feature-store.md)
