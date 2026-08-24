# MLOps — Registry, serving e drift

> **Purpose**: Continuação de [mlops-pipeline.md](mlops-pipeline.md).  
> **MCP Validated**: 2026-04-20

## Steps 4–6

```python
from mlflow import MlflowClient

client = MlflowClient(registry_uri="databricks-uc")
versions = client.search_model_versions("name='prod_catalog.ml_models.fraud_detector'")
latest_version = max(int(v.version) for v in versions)
auc = float(client.get_metric_history(run_id, "test_roc_auc")[0].value)

if auc >= 0.85:
    client.set_registered_model_alias(
        name="prod_catalog.ml_models.fraud_detector",
        alias="champion",
        version=latest_version,
    )

import requests

endpoint_config = {
    "config": {
        "served_entities": [
            {
                "entity_name": "prod_catalog.ml_models.fraud_detector",
                "entity_version": str(latest_version),
                "workload_size": "Small",
                "scale_to_zero_enabled": True,
            }
        ]
    }
}
response = requests.put(
    f"{WORKSPACE_URL}/api/2.0/serving-endpoints/fraud-detector-endpoint/config",
    headers={"Authorization": f"Bearer {TOKEN}"},
    json=endpoint_config["config"],
)

spark.sql("""
    SELECT DATE(request_time) AS date, COUNT(*) AS num_requests
    FROM prod_catalog.ml_inference.fraud_detector_requests
    WHERE request_time >= CURRENT_DATE - INTERVAL 7 DAYS
    GROUP BY DATE(request_time)
""")
```

## See Also

- [mlops-pipeline.md](mlops-pipeline.md)
