# MLflow on Databricks

> **Purpose**: Master MLflow — experiments, runs, autologging, model flavors, Model Registry (Unity Catalog), and model serving
> **Confidence**: 0.95
> **MCP Validated**: 2026-04-20

## Overview

MLflow is an open-source ML lifecycle platform deeply integrated into Databricks. It tracks experiments (params, metrics, artifacts), manages model versions via the Model Registry in Unity Catalog, and deploys models via Mosaic AI Model Serving. MLflow 3 (2025) uses Unity Catalog as the default registry.

## Tracking: Experiments and Runs

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Set experiment (creates if not exists)
mlflow.set_experiment("/Users/user@company.com/fraud-detection")

# Manual tracking
with mlflow.start_run(run_name="rf-v1-experiment") as run:
    # Log parameters
    mlflow.log_param("n_estimators", 100)
    mlflow.log_param("max_depth", 10)
    mlflow.log_param("random_state", 42)

    # Train model
    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    # Log metrics
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("f1_score", f1_score(y_test, y_pred))

    # Log artifacts (files, images, configs)
    mlflow.log_artifact("feature_importance.png")
    mlflow.log_dict({"features": feature_names}, "features.json")

    # Log model
    mlflow.sklearn.log_model(model, "model",
        registered_model_name="main.fraud_detection.rf_classifier")

    print(f"Run ID: {run.info.run_id}")
```

## mlflow.autolog()

```python
# Autologging captures params, metrics, and models automatically
# Supported frameworks (as of DBR 15.x):
#   sklearn, xgboost, lightgbm, pytorch, tensorflow/keras,
#   spark ML, statsmodels, prophet, fastai

# Enable autologging (Databricks enables this automatically in notebooks)
mlflow.autolog(
    log_input_examples=True,    # Log sample inputs
    log_model_signatures=True,  # Log input/output schema
    log_models=True,            # Auto-register model
    disable=False,
    exclusive=False,            # Allow manual logging too
    silent=False,
)

# Framework-specific autolog
mlflow.sklearn.autolog()
mlflow.xgboost.autolog()
mlflow.pytorch.autolog()

# Train — everything logged automatically
from sklearn.linear_model import LogisticRegression
with mlflow.start_run():
    model = LogisticRegression().fit(X_train, y_train)
    # Params, metrics, and model logged automatically
```

## Model Flavors

```python
# Each flavor defines how a model is saved and loaded

# sklearn flavor
mlflow.sklearn.log_model(sklearn_model, "model")
loaded = mlflow.sklearn.load_model("runs:/run_id/model")

# PyTorch flavor
mlflow.pytorch.log_model(torch_model, "model")

# TensorFlow/Keras flavor
mlflow.tensorflow.log_model(keras_model, "model")

# Spark ML flavor
mlflow.spark.log_model(spark_pipeline, "model")

# pyfunc — generic Python model (custom prediction logic)
class FraudDetector(mlflow.pyfunc.PythonModel):
    def predict(self, context, model_input, params=None):
        # Custom preprocessing + prediction
        return self.model.predict(model_input)

mlflow.pyfunc.log_model("model", python_model=FraudDetector())
```

## Registro de modelos, serving e erros comuns

Continuação: [mlflow-registry-serving.md](mlflow-registry-serving.md).

## Related

- [concepts/feature-store.md](feature-store.md)
- [patterns/mlops-pipeline.md](../patterns/mlops-pipeline.md)
