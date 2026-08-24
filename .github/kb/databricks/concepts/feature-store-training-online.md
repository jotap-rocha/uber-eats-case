# Feature Store — treino, online serving e decisões

> **Purpose**: Extensão de [feature-store.md](feature-store.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Training with Feature Store

```python
import mlflow

with mlflow.start_run():
    model = train_model(training_df)
    fe.log_model(
        model=model,
        artifact_path="model",
        flavor=mlflow.sklearn,
        training_set=training_set,
        registered_model_name="main.fraud_detection.fraud_classifier",
    )
```

## Online Store (Real-Time Serving)

```python
from databricks.feature_engineering.entities.feature_serving_endpoint import (
    ServedEntity,
    EndpointCoreConfig,
)

fe.create_feature_serving_endpoint(
    name="customer-features-online",
    config=EndpointCoreConfig(
        served_entities=[
            ServedEntity(
                feature_spec_name="main.feature_store.customer_features_spec",
                workload_size="Small",
                scale_to_zero_enabled=True,
            )
        ]
    )
)
```

## Decision Matrix

| Use Case | Choose |
|----------|--------|
| Model training with historical features | Feature lookup with timestamp_lookup_key |
| Batch inference | Feature lookup without timestamp |
| Real-time inference (<10ms) | Online store serving endpoint |
| Ad-hoc feature exploration | spark.table("main.feature_store.xxx") |

## Related

- [feature-store.md](feature-store.md)
