# MLflow — Model Registry e serving

> **Purpose**: Extensão de [mlflow.md](mlflow.md).  
> **Confidence**: 0.95  
> **MCP Validated**: 2026-04-20

## Model Registry (Unity Catalog — DBR 13.2+)

```python
import mlflow
from mlflow import MlflowClient

mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="main.fraud_detection.rf_classifier",
)
client = MlflowClient(registry_uri="databricks-uc")
client.set_registered_model_alias(
    name="main.fraud_detection.rf_classifier",
    alias="champion",
    version=3,
)
model = mlflow.sklearn.load_model("models:/main.fraud_detection.rf_classifier@champion")
```

## Model Serving (Mosaic AI)

```python
import requests

token = dbutils.secrets.get("my-scope", "databricks-token")
endpoint_url = "https://workspace.azuredatabricks.net/serving-endpoints/fraud-detector/invocations"
response = requests.post(
    endpoint_url,
    headers={"Authorization": f"Bearer {token}"},
    json={"dataframe_records": [{"feature1": 0.5, "feature2": 1.2, "feature3": "cat_a"}]},
)
```

## Common Mistakes

### Wrong

```python
with mlflow.start_run():
    mlflow.log_metric("accuracy", 0.92)
```

### Correct

```python
mlflow.set_experiment("/Users/user@company.com/my-project")
with mlflow.start_run(run_name="baseline"):
    mlflow.log_metric("accuracy", 0.92)
```

## Related

- [mlflow.md](mlflow.md)
- [patterns/mlops-pipeline-registry-serving.md](../patterns/mlops-pipeline-registry-serving.md)
