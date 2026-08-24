# From/to pandas and PySpark DataFrames — PySpark 4.0.1 documentation
Users from pandas and/or PySpark face API compatibility issue sometimes when they work with pandas API on Spark. Since pandas API on Spark does not target 100% compatibility of both pandas and PySpark, users need to do some workaround to port their pandas and/or PySpark codes or get familiar with pandas API on Spark in this case. This page aims to describe it.

pandas[#](#pandas "Permalink to this headline")
-----------------------------------------------

pandas users can access the full pandas API by calling [`DataFrame.to_pandas()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_pandas.html#pyspark.pandas.DataFrame.to_pandas "pyspark.pandas.DataFrame.to_pandas"). pandas-on-Spark DataFrame and pandas DataFrame are similar. However, the former is distributed and the latter is in a single machine. When converting to each other, the data is transferred between multiple machines and the single client machine.

For example, if you need to call `pandas_df.values` of pandas DataFrame, you can do as below:

```
>>> import pyspark.pandas as ps
>>>
>>> psdf = ps.range(10)
>>> pdf = psdf.to_pandas()
>>> pdf.values
array([[0],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8],
       [9]])

```


pandas DataFrame can be a pandas-on-Spark DataFrame easily as below:

```
>>> ps.from_pandas(pdf)
   id
0   0
1   1
2   2
3   3
4   4
5   5
6   6
7   7
8   8
9   9

```


Note that converting pandas-on-Spark DataFrame to pandas requires to collect all the data into the client machine; therefore, if possible, it is recommended to use pandas API on Spark or PySpark APIs instead.

PySpark[#](#pyspark "Permalink to this headline")
-------------------------------------------------

PySpark users can access the full PySpark APIs by calling [`DataFrame.to_spark()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_spark.html#pyspark.pandas.DataFrame.to_spark "pyspark.pandas.DataFrame.to_spark"). pandas-on-Spark DataFrame and Spark DataFrame are virtually interchangeable.

For example, if you need to call `spark_df.filter(...)` of Spark DataFrame, you can do as below:

```
>>> import pyspark.pandas as ps
>>>
>>> psdf = ps.range(10)
>>> sdf = psdf.to_spark().filter("id > 5")
>>> sdf.show()
+---+
| id|
+---+
|  6|
|  7|
|  8|
|  9|
+---+

```


Spark DataFrame can be a pandas-on-Spark DataFrame easily as below:

```
>>> sdf.pandas_api()
   id
0   6
1   7
2   8
3   9

```


However, note that a new default index is created when pandas-on-Spark DataFrame is created from Spark DataFrame. See [Default Index Type](about:blank/options.html#default-index-type). In order to avoid this overhead, specify the column to use as an index when possible.

```
>>> # Create a pandas-on-Spark DataFrame with an explicit index.
... psdf = ps.DataFrame({'id': range(10)}, index=range(10))
>>> # Keep the explicit index.
... sdf = psdf.to_spark(index_col='index')
>>> # Call Spark APIs
... sdf = sdf.filter("id > 5")
>>> # Uses the explicit index to avoid to create default index.
... sdf.pandas_api(index_col='index')
       id
index
6       6
7       7
8       8
9       9

```
