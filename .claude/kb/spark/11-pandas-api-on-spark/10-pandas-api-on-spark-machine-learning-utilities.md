# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/ml.html#

# Machine Learning utilities#

## MLflow#

Arbitrary MLflow models can be used with pandas-on-Spark Dataframes, provided they implement the âpyfuncâ flavor. This is the case for most frameworks supported by MLflow (scikit-learn, pytorch, tensorflow, â¦). See comprehensive examples in [`load_model()`](api/pyspark.pandas.mlflow.load_model.html#pyspark.pandas.mlflow.load_model "pyspark.pandas.mlflow.load_model") for more information.

Note

The MLflow package must be installed in order to use this module.

[`PythonModelWrapper`](api/pyspark.pandas.mlflow.PythonModelWrapper.html#pyspark.pandas.mlflow.PythonModelWrapper "pyspark.pandas.mlflow.PythonModelWrapper")(model_uri,Â return_type_hint) | A wrapper around MLflow's Python object model.  
---|---  
[`load_model`](api/pyspark.pandas.mlflow.load_model.html#pyspark.pandas.mlflow.load_model "pyspark.pandas.mlflow.load_model")(model_uri[,Â predict_type]) | Loads an MLflow model into a wrapper that can be used both for pandas and pandas-on-Spark DataFrame.  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/ml.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.mlflow.PythonModelWrapper.html

# pyspark.pandas.mlflow.PythonModelWrapper#

_class _pyspark.pandas.mlflow.PythonModelWrapper(_model_uri_ , _return_type_hint_)[[source]](../../../_modules/pyspark/pandas/mlflow.html#PythonModelWrapper)#
    

A wrapper around MLflowâs Python object model.

This wrapper acts as a predictor on pandas-on-Spark

Methods

`predict`(data) | Returns a prediction on the data.  
---|---  
  
[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.mlflow.PythonModelWrapper.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.mlflow.load_model.html

# pyspark.pandas.mlflow.load_model#

pyspark.pandas.mlflow.load_model(_model_uri_ , _predict_type ='infer'_)[[source]](../../../_modules/pyspark/pandas/mlflow.html#load_model)#
    

Loads an MLflow model into a wrapper that can be used both for pandas and pandas-on-Spark DataFrame.

Parameters
    

**model_uri** str
    

URI pointing to the model. See MLflow documentation for more details.

**predict_type** a python basic type, a numpy basic type, a Spark type or âinferâ.
    

This is the return type that is expected when calling the predict function of the model. If âinferâ is specified, the wrapper will attempt to automatically determine the return type based on the model type.

Returns
    

PythonModelWrapper
    

A wrapper around MLflow PythonModel objects. This wrapper is expected to adhere to the interface of mlflow.pyfunc.PythonModel.

Notes

Currently, the model prediction can only be merged back with the existing dataframe. Other columns must be manually joined. For example, this code will not work:
    
    
    >>> df = ps.DataFrame({"x1": [2.0], "x2": [3.0], "z": [-1]})
    >>> features = df[["x1", "x2"]]
    >>> y = model.predict(features)
    >>> # Works:
    >>> features["y"] = y   
    >>> # Will fail with a message about dataframes not aligned.
    >>> df["y"] = y   
    

A current workaround is to use the .merge() function, using the feature values as merging keys.
    
    
    >>> features['y'] = y
    >>> everything = df.merge(features, on=['x1', 'x2'])
    >>> everything
        x1   x2  z         y
    0  2.0  3.0 -1  1.376932
    

Examples

Here is a full example that creates a model with scikit-learn and saves the model with
    

MLflow. The model is then loaded as a predictor that can be applied on a pandas-on-Spark Dataframe.

We first initialize our MLflow environment:
    
    
    >>> from mlflow.tracking import MlflowClient, set_tracking_uri
    >>> import mlflow.sklearn
    >>> from tempfile import mkdtemp
    >>> d = mkdtemp("pandas_on_spark_mlflow")
    >>> set_tracking_uri("file:%s"%d)
    >>> client = MlflowClient()
    >>> exp_id = mlflow.create_experiment("my_experiment")
    >>> exp = mlflow.set_experiment("my_experiment")
    

We aim at learning this numerical function using a simple linear regressor.
    
    
    >>> from sklearn.linear_model import LinearRegression
    >>> train = pd.DataFrame({"x1": np.arange(8), "x2": np.arange(8)**2,
    ...                       "y": np.log(2 + np.arange(8))})
    >>> train_x = train[["x1", "x2"]]
    >>> train_y = train[["y"]]
    >>> with mlflow.start_run():
    ...     lr = LinearRegression()
    ...     lr.fit(train_x, train_y)
    ...     mlflow.sklearn.log_model(lr, "model")
    LinearRegression...
    

Now that our model is logged using MLflow, we load it back and apply it on a pandas-on-Spark dataframe:
    
    
    >>> from pyspark.pandas.mlflow import load_model
    >>> run_info = client.search_runs(exp_id)[-1].info
    >>> model = load_model("runs:/{run_id}/model".format(run_id=run_info.run_id))
    >>> prediction_df = ps.DataFrame({"x1": [2.0], "x2": [4.0]})
    >>> prediction_df["prediction"] = model.predict(prediction_df)
    >>> prediction_df
        x1   x2  prediction
    0  2.0  4.0    1.355551
    

The model also works on pandas DataFrames as expected:
    
    
    >>> model.predict(prediction_df[["x1", "x2"]].to_pandas())
    array([[1.35555142]])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.mlflow.load_model.rst.txt)
