# Grouping — PySpark 4.0.1 documentation


* GroupedData.agg(*exprs): GroupedData.apply(udf)
  * Compute aggregates and returns the result as a DataFrame.: It is an alias of pyspark.sql.GroupedData.applyInPandas(); however, it takes a pyspark.sql.functions.pandas_udf() whereas pyspark.sql.GroupedData.applyInPandas() takes a Python native function.
* GroupedData.agg(*exprs): GroupedData.applyInArrow(func, schema)
  * Compute aggregates and returns the result as a DataFrame.: Maps each group of the current DataFrame using an Arrow udf and returns the result as a DataFrame.
* GroupedData.agg(*exprs): GroupedData.applyInPandas(func, schema)
  * Compute aggregates and returns the result as a DataFrame.: Maps each group of the current DataFrame using a pandas udf and returns the result as a DataFrame.
* GroupedData.agg(*exprs): GroupedData.applyInPandasWithState(func, ...)
  * Compute aggregates and returns the result as a DataFrame.: Applies the given function to each group of data, while maintaining a user-defined per-group state.
* GroupedData.agg(*exprs): GroupedData.avg(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes average values for each numeric columns for each group.
* GroupedData.agg(*exprs): GroupedData.cogroup(other)
  * Compute aggregates and returns the result as a DataFrame.: Cogroups this group with another group so that we can run cogrouped operations.
* GroupedData.agg(*exprs): GroupedData.count()
  * Compute aggregates and returns the result as a DataFrame.: Counts the number of records for each group.
* GroupedData.agg(*exprs): GroupedData.max(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes the max value for each numeric columns for each group.
* GroupedData.agg(*exprs): GroupedData.mean(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes average values for each numeric columns for each group.
* GroupedData.agg(*exprs): GroupedData.min(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes the min value for each numeric column for each group.
* GroupedData.agg(*exprs): GroupedData.pivot(pivot_col[, values])
  * Compute aggregates and returns the result as a DataFrame.: Pivots a column of the current DataFrame and performs the specified aggregation.
* GroupedData.agg(*exprs): GroupedData.sum(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes the sum for each numeric columns for each group.
* GroupedData.agg(*exprs): GroupedData.transformWithStateInPandas(...)
  * Compute aggregates and returns the result as a DataFrame.: Invokes methods defined in the stateful processor used in arbitrary state API v2.
* GroupedData.agg(*exprs): PandasCogroupedOps.applyInArrow(func, schema)
  * Compute aggregates and returns the result as a DataFrame.: Applies a function to each cogroup using Arrow and returns the result as a DataFrame.
* GroupedData.agg(*exprs): PandasCogroupedOps.applyInPandas(func, schema)
  * Compute aggregates and returns the result as a DataFrame.: Applies a function to each cogroup using pandas and returns the result as a DataFrame.


# pyspark.sql.GroupedData.agg — PySpark 4.0.1 documentation
GroupedData.agg(_\*exprs_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.agg)
[#](#pyspark.sql.GroupedData.agg "Permalink to this definition")

Compute aggregates and returns the result as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The available aggregate functions can be:

1.  built-in aggregation functions, such as avg, max, min, sum, count
    
2.  group aggregate pandas UDFs, created with [`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf")
    
    Note
    
    There is no partial aggregation with group aggregate UDFs, i.e., a full shuffle is required. Also, all the data of a group will be loaded into memory, so the user should be aware of the potential OOM risk if data is skewed and certain groups are too large to fit in memory.
    

If `exprs` is a single `dict` mapping from string to string, then the key is the column to perform aggregation on, and the value is the aggregate function.

Alternatively, `exprs` can also be a list of aggregate [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expressions.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**exprs**dict

a dict mapping from column name (string) to aggregate functions (string), or a list of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Notes

Built-in aggregation functions and group aggregate pandas UDFs cannot be mixed in a single call to this function.

Examples

```
>>> import pandas as pd  
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.functions import pandas_udf
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (3, "Alice"), (5, "Bob"), (10, "Bob")], ["age", "name"])
>>> df.show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  3|Alice|
|  5|  Bob|
| 10|  Bob|
+---+-----+

```


Group-by name, and count each group.

```
>>> df.groupBy(df.name)
GroupedData[grouping...: [name...], value: [age: bigint, name: string], type: GroupBy]

```


```
>>> df.groupBy(df.name).agg({"*": "count"}).sort("name").show()
+-----+--------+
| name|count(1)|
+-----+--------+
|Alice|       2|
|  Bob|       2|
+-----+--------+

```


Group-by name, and calculate the minimum age.

```
>>> df.groupBy(df.name).agg(sf.min(df.age)).sort("name").show()
+-----+--------+
| name|min(age)|
+-----+--------+
|Alice|       2|
|  Bob|       5|
+-----+--------+

```


Same as above but uses pandas UDF.

```
>>> @pandas_udf('int')  
... def min_udf(v: pd.Series) -> int:
...     return v.min()
...
>>> df.groupBy(df.name).agg(min_udf(df.age)).sort("name").show()  
+-----+------------+
| name|min_udf(age)|
+-----+------------+
|Alice|           2|
|  Bob|           5|
+-----+------------+

```

# pyspark.sql.GroupedData.apply — PySpark 4.0.1 documentation
GroupedData.apply(_udf_)
[#](#pyspark.sql.GroupedData.apply "Permalink to this definition")

It is an alias of [`pyspark.sql.GroupedData.applyInPandas()`](about:blank/pyspark.sql.GroupedData.applyInPandas.html#pyspark.sql.GroupedData.applyInPandas "pyspark.sql.GroupedData.applyInPandas"); however, it takes a [`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") whereas [`pyspark.sql.GroupedData.applyInPandas()`](about:blank/pyspark.sql.GroupedData.applyInPandas.html#pyspark.sql.GroupedData.applyInPandas "pyspark.sql.GroupedData.applyInPandas") takes a Python native function.

New in version 2.3.0.

Changed in version 3.4.0: Support Spark Connect.

Parameters

**udf**[`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf")

a grouped map user-defined function returned by [`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf").

Notes

It is preferred to use [`pyspark.sql.GroupedData.applyInPandas()`](about:blank/pyspark.sql.GroupedData.applyInPandas.html#pyspark.sql.GroupedData.applyInPandas "pyspark.sql.GroupedData.applyInPandas") over this API. This API will be deprecated in the future releases.

Examples

```
>>> from pyspark.sql.functions import pandas_udf, PandasUDFType
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
...     ("id", "v"))
>>> @pandas_udf("id long, v double", PandasUDFType.GROUPED_MAP)  
... def normalize(pdf):
...     v = pdf.v
...     return pdf.assign(v=(v - v.mean()) / v.std())
...
>>> df.groupby("id").apply(normalize).show()  
+---+-------------------+
| id|                  v|
+---+-------------------+
|  1|-0.7071067811865475|
|  1| 0.7071067811865475|
|  2|-0.8320502943378437|
|  2|-0.2773500981126146|
|  2| 1.1094003924504583|
+---+-------------------+

```


# pyspark.sql.GroupedData.applyInArrow — PySpark 4.0.1 documentation
GroupedData.applyInArrow(_func_, _schema_)
[#](#pyspark.sql.GroupedData.applyInArrow "Permalink to this definition")

Maps each group of the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using an Arrow udf and returns the result as a DataFrame.

The function should take a pyarrow.Table and return another pyarrow.Table. Alternatively, the user can pass a function that takes a tuple of pyarrow.Scalar grouping key(s) and a pyarrow.Table. For each group, all columns are passed together as a pyarrow.Table to the user-function and the returned pyarrow.Table are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The schema should be a `StructType` describing the schema of the returned pyarrow.Table. The column labels of the returned pyarrow.Table must either match the field names in the defined schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices. The length of the returned pyarrow.Table can be arbitrary.

New in version 4.0.0.

Parameters

**func**function

a Python native function that takes a pyarrow.Table and outputs a pyarrow.Table, or that takes one tuple (grouping keys) and a pyarrow.Table and outputs a pyarrow.Table.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the return type of the func in PySpark. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

Notes

This function requires a full shuffle. All the data of a group will be loaded into memory, so the user should be aware of the potential OOM risk if data is skewed and certain groups are too large to fit in memory.

This API is unstable, and for developers.

Examples

```
>>> from pyspark.sql.functions import ceil
>>> import pyarrow  
>>> import pyarrow.compute as pc  
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
...     ("id", "v"))  
>>> def normalize(table):
...     v = table.column("v")
...     norm = pc.divide(pc.subtract(v, pc.mean(v)), pc.stddev(v, ddof=1))
...     return table.set_column(1, "v", norm)
>>> df.groupby("id").applyInArrow(
...     normalize, schema="id long, v double").show()  
+---+-------------------+
| id|                  v|
+---+-------------------+
|  1|-0.7071067811865475|
|  1| 0.7071067811865475|
|  2|-0.8320502943378437|
|  2|-0.2773500981126146|
|  2| 1.1094003924504583|
+---+-------------------+

```


Alternatively, the user can pass a function that takes two arguments. In this case, the grouping key(s) will be passed as the first argument and the data will be passed as the second argument. The grouping key(s) will be passed as a tuple of Arrow scalars types, e.g., pyarrow.Int32Scalar and pyarrow.FloatScalar. The data will still be passed in as a pyarrow.Table containing all columns from the original Spark DataFrame. This is useful when the user does not want to hardcode grouping key(s) in the function.

```
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
...     ("id", "v"))  
>>> def mean_func(key, table):
...     # key is a tuple of one pyarrow.Int64Scalar, which is the value
...     # of 'id' for the current group
...     mean = pc.mean(table.column("v"))
...     return pyarrow.Table.from_pydict({"id": [key[0].as_py()], "v": [mean.as_py()]})
>>> df.groupby('id').applyInArrow(
...     mean_func, schema="id long, v double")  
+---+---+
| id|  v|
+---+---+
|  1|1.5|
|  2|6.0|
+---+---+

```


```
>>> def sum_func(key, table):
...     # key is a tuple of two pyarrow.Int64Scalars, which is the values
...     # of 'id' and 'ceil(df.v / 2)' for the current group
...     sum = pc.sum(table.column("v"))
...     return pyarrow.Table.from_pydict({
...         "id": [key[0].as_py()],
...         "ceil(v / 2)": [key[1].as_py()],
...         "v": [sum.as_py()]
...     })
>>> df.groupby(df.id, ceil(df.v / 2)).applyInArrow(
...     sum_func, schema="id long, `ceil(v / 2)` long, v double").show()  
+---+-----------+----+
| id|ceil(v / 2)|   v|
+---+-----------+----+
|  2|          5|10.0|
|  1|          1| 3.0|
|  2|          3| 5.0|
|  2|          2| 3.0|
+---+-----------+----+

```


# pyspark.sql.GroupedData.applyInPandas — PySpark 4.0.1 documentation
GroupedData.applyInPandas(_func_, _schema_)
[#](#pyspark.sql.GroupedData.applyInPandas "Permalink to this definition")

Maps each group of the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using a pandas udf and returns the result as a DataFrame.

The function should take a pandas.DataFrame and return another pandas.DataFrame. Alternatively, the user can pass a function that takes a tuple of the grouping key(s) and a pandas.DataFrame. For each group, all columns are passed together as a pandas.DataFrame to the user-function and the returned pandas.DataFrame are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The schema should be a `StructType` describing the schema of the returned pandas.DataFrame. The column labels of the returned pandas.DataFrame must either match the field names in the defined schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices. The length of the returned pandas.DataFrame can be arbitrary.

New in version 3.0.0.

Changed in version 3.4.0: Support Spark Connect.

Parameters

**func**function

a Python native function that takes a pandas.DataFrame and outputs a pandas.DataFrame, or that takes one tuple (grouping keys) and a pandas.DataFrame and outputs a pandas.DataFrame.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the return type of the func in PySpark. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

Notes

This function requires a full shuffle. All the data of a group will be loaded into memory, so the user should be aware of the potential OOM risk if data is skewed and certain groups are too large to fit in memory.

Examples

```
>>> import pandas as pd  
>>> from pyspark.sql.functions import ceil
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
...     ("id", "v"))  
>>> def normalize(pdf):
...     v = pdf.v
...     return pdf.assign(v=(v - v.mean()) / v.std())
...
>>> df.groupby("id").applyInPandas(
...     normalize, schema="id long, v double").show()  
+---+-------------------+
| id|                  v|
+---+-------------------+
|  1|-0.7071067811865475|
|  1| 0.7071067811865475|
|  2|-0.8320502943378437|
|  2|-0.2773500981126146|
|  2| 1.1094003924504583|
+---+-------------------+

```


Alternatively, the user can pass a function that takes two arguments. In this case, the grouping key(s) will be passed as the first argument and the data will be passed as the second argument. The grouping key(s) will be passed as a tuple of numpy data types, e.g., numpy.int32 and numpy.float64. The data will still be passed in as a pandas.DataFrame containing all columns from the original Spark DataFrame. This is useful when the user does not want to hardcode grouping key(s) in the function.

```
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
...     ("id", "v"))  
>>> def mean_func(key, pdf):
...     # key is a tuple of one numpy.int64, which is the value
...     # of 'id' for the current group
...     return pd.DataFrame([key + (pdf.v.mean(),)])
...
>>> df.groupby('id').applyInPandas(
...     mean_func, schema="id long, v double").show()  
+---+---+
| id|  v|
+---+---+
|  1|1.5|
|  2|6.0|
+---+---+

```


```
>>> def sum_func(key, pdf):
...     # key is a tuple of two numpy.int64s, which is the values
...     # of 'id' and 'ceil(df.v / 2)' for the current group
...     return pd.DataFrame([key + (pdf.v.sum(),)])
...
>>> df.groupby(df.id, ceil(df.v / 2)).applyInPandas(
...     sum_func, schema="id long, `ceil(v / 2)` long, v double").show()  
+---+-----------+----+
| id|ceil(v / 2)|   v|
+---+-----------+----+
|  2|          5|10.0|
|  1|          1| 3.0|
|  2|          3| 5.0|
|  2|          2| 3.0|
+---+-----------+----+

```


# pyspark.sql.GroupedData.applyInPandasWithState — PySpark 4.0.1 documentation
GroupedData.applyInPandasWithState(_func_, _outputStructType_, _stateStructType_, _outputMode_, _timeoutConf_)
[#](#pyspark.sql.GroupedData.applyInPandasWithState "Permalink to this definition")

Applies the given function to each group of data, while maintaining a user-defined per-group state. The result Dataset will represent the flattened record returned by the function.

For a streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), the function will be invoked first for all input groups and then for all timed out states where the input data is set to be empty. Updates to each group’s state will be saved across invocations.

The function should take parameters (key, Iterator\[pandas.DataFrame\], state) and return another Iterator\[pandas.DataFrame\]. The grouping key(s) will be passed as a tuple of numpy data types, e.g., numpy.int32 and numpy.float64. The state will be passed as `pyspark.sql.streaming.state.GroupState`.

For each group, all columns are passed together as pandas.DataFrame to the user-function, and the returned pandas.DataFrame across all invocations are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). Note that the user function should not make a guess of the number of elements in the iterator. To process all data, the user function needs to iterate all elements and process them. On the other hand, the user function is not strictly required to iterate through all elements in the iterator if it intends to read a part of data.

The outputStructType should be a `StructType` describing the schema of all elements in the returned value, pandas.DataFrame. The column labels of all elements in returned pandas.DataFrame must either match the field names in the defined schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices.

The stateStructType should be `StructType` describing the schema of the user-defined state. The value of the state will be presented as a tuple, as well as the update should be performed with the tuple. The corresponding Python types for :class:DataType are supported. Please refer to the page https://spark.apache.org/docs/latest/sql-ref-datatypes.html (Python tab).

The size of each pandas.DataFrame in both the input and output can be arbitrary. The number of pandas.DataFrame in both the input and output can also be arbitrary.

New in version 3.4.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters

**func**function

a Python native function to be called on every group. It should take parameters (key, Iterator\[pandas.DataFrame\], state) and return Iterator\[pandas.DataFrame\]. Note that the type of the key is tuple and the type of the state is `pyspark.sql.streaming.state.GroupState`.

**outputStructType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the type of the output records. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

**stateStructType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the type of the user-defined state. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

**outputMode**str

the output mode of the function.

**timeoutConf**str

timeout configuration for groups that do not receive data for a while. valid values are defined in `pyspark.sql.streaming.state.GroupStateTimeout`.

Notes

This function requires a full shuffle.

Examples

```
>>> import pandas as pd  
>>> from pyspark.sql.streaming.state import GroupStateTimeout
>>> def count_fn(key, pdf_iter, state):
...     assert isinstance(state, GroupStateImpl)
...     total_len = 0
...     for pdf in pdf_iter:
...         total_len += len(pdf)
...     state.update((total_len,))
...     yield pd.DataFrame({"id": [key[0]], "countAsString": [str(total_len)]})
...
>>> df.groupby("id").applyInPandasWithState(
...     count_fn, outputStructType="id long, countAsString string",
...     stateStructType="len long", outputMode="Update",
...     timeoutConf=GroupStateTimeout.NoTimeout) 

```


# pyspark.sql.GroupedData.avg — PySpark 4.0.1 documentation
GroupedData.avg(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.avg)
[#](#pyspark.sql.GroupedData.avg "Permalink to this definition")

Computes average values for each numeric columns for each group.

[`mean()`](about:blank/pyspark.sql.GroupedData.mean.html#pyspark.sql.GroupedData.mean "pyspark.sql.GroupedData.mean") is an alias for [`avg()`](#pyspark.sql.GroupedData.avg "pyspark.sql.GroupedData.avg").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**str

column names. Non-numeric columns are ignored.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice", 80), (3, "Alice", 100),
...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
>>> df.show()
+---+-----+------+
|age| name|height|
+---+-----+------+
|  2|Alice|    80|
|  3|Alice|   100|
|  5|  Bob|   120|
| 10|  Bob|   140|
+---+-----+------+

```


Group-by name, and calculate the mean of the age in each group.

```
>>> df.groupBy("name").avg('age').sort("name").show()
+-----+--------+
| name|avg(age)|
+-----+--------+
|Alice|     2.5|
|  Bob|     7.5|
+-----+--------+

```


Calculate the mean of the age and height in all data.

```
>>> df.groupBy().avg('age', 'height').show()
+--------+-----------+
|avg(age)|avg(height)|
+--------+-----------+
|     5.0|      110.0|
+--------+-----------+

```

# pyspark.sql.GroupedData.cogroup — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Grouping](../grouping.html)
*   pyspark.sql.GroupedData.cogroup

GroupedData.cogroup(_other_)
[#](#pyspark.sql.GroupedData.cogroup "Permalink to this definition")

Cogroups this group with another group so that we can run cogrouped operations.

New in version 3.0.0.

Changed in version 3.4.0: Support Spark Connect.

See [`PandasCogroupedOps`](about:blank/pyspark.sql.PandasCogroupedOps.html#pyspark.sql.PandasCogroupedOps "pyspark.sql.PandasCogroupedOps") for the operations that can be run.


# pyspark.sql.GroupedData.count — PySpark 4.0.1 documentation
GroupedData.count()
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.count)
[#](#pyspark.sql.GroupedData.count "Permalink to this definition")

Counts the number of records for each group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (3, "Alice"), (5, "Bob"), (10, "Bob")], ["age", "name"])
>>> df.show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  3|Alice|
|  5|  Bob|
| 10|  Bob|
+---+-----+

```


Group-by name, and count each group.

```
>>> df.groupBy(df.name).count().sort("name").show()
+-----+-----+
| name|count|
+-----+-----+
|Alice|    2|
|  Bob|    2|
+-----+-----+

```

# pyspark.sql.GroupedData.max — PySpark 4.0.1 documentation
GroupedData.max(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.max)
[#](#pyspark.sql.GroupedData.max "Permalink to this definition")

Computes the max value for each numeric columns for each group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice", 80), (3, "Alice", 100),
...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
>>> df.show()
+---+-----+------+
|age| name|height|
+---+-----+------+
|  2|Alice|    80|
|  3|Alice|   100|
|  5|  Bob|   120|
| 10|  Bob|   140|
+---+-----+------+

```


Group-by name, and calculate the max of the age in each group.

```
>>> df.groupBy("name").max("age").sort("name").show()
+-----+--------+
| name|max(age)|
+-----+--------+
|Alice|       3|
|  Bob|      10|
+-----+--------+

```


Calculate the max of the age and height in all data.

```
>>> df.groupBy().max("age", "height").show()
+--------+-----------+
|max(age)|max(height)|
+--------+-----------+
|      10|        140|
+--------+-----------+

```



# pyspark.sql.GroupedData.mean — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Grouping](../grouping.html)
*   pyspark.sql.GroupedData.mean

GroupedData.mean(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.mean)
[#](#pyspark.sql.GroupedData.mean "Permalink to this definition")

Computes average values for each numeric columns for each group.

[`mean()`](#pyspark.sql.GroupedData.mean "pyspark.sql.GroupedData.mean") is an alias for [`avg()`](about:blank/pyspark.sql.GroupedData.avg.html#pyspark.sql.GroupedData.avg "pyspark.sql.GroupedData.avg").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**str

column names. Non-numeric columns are ignored.

# pyspark.sql.GroupedData.min — PySpark 4.0.1 documentation
GroupedData.min(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.min)
[#](#pyspark.sql.GroupedData.min "Permalink to this definition")

Computes the min value for each numeric column for each group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**str

column names. Non-numeric columns are ignored.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice", 80), (3, "Alice", 100),
...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
>>> df.show()
+---+-----+------+
|age| name|height|
+---+-----+------+
|  2|Alice|    80|
|  3|Alice|   100|
|  5|  Bob|   120|
| 10|  Bob|   140|
+---+-----+------+

```


Group-by name, and calculate the min of the age in each group.

```
>>> df.groupBy("name").min("age").sort("name").show()
+-----+--------+
| name|min(age)|
+-----+--------+
|Alice|       2|
|  Bob|       5|
+-----+--------+

```


Calculate the min of the age and height in all data.

```
>>> df.groupBy().min("age", "height").show()
+--------+-----------+
|min(age)|min(height)|
+--------+-----------+
|       2|         80|
+--------+-----------+

```


# pyspark.sql.GroupedData.pivot — PySpark 4.0.1 documentation
GroupedData.pivot(_pivot\_col_, _values\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.pivot)
[#](#pyspark.sql.GroupedData.pivot "Permalink to this definition")

Pivots a column of the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") and performs the specified aggregation.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**pivot\_col**str

Name of the column to pivot.

**values**list, optional

List of values that will be translated to columns in the output DataFrame.

If `values` is not provided, Spark will eagerly compute the distinct values in `pivot_col` so it can determine the resulting schema of the transformation. To avoid any eager computations, provide an explicit list of values.

Examples

```
>>> from pyspark.sql import Row
>>> df1 = spark.createDataFrame([
...     Row(course="dotNET", year=2012, earnings=10000),
...     Row(course="Java", year=2012, earnings=20000),
...     Row(course="dotNET", year=2012, earnings=5000),
...     Row(course="dotNET", year=2013, earnings=48000),
...     Row(course="Java", year=2013, earnings=30000),
... ])
>>> df1.show()
+------+----+--------+
|course|year|earnings|
+------+----+--------+
|dotNET|2012|   10000|
|  Java|2012|   20000|
|dotNET|2012|    5000|
|dotNET|2013|   48000|
|  Java|2013|   30000|
+------+----+--------+
>>> df2 = spark.createDataFrame([
...     Row(training="expert", sales=Row(course="dotNET", year=2012, earnings=10000)),
...     Row(training="junior", sales=Row(course="Java", year=2012, earnings=20000)),
...     Row(training="expert", sales=Row(course="dotNET", year=2012, earnings=5000)),
...     Row(training="junior", sales=Row(course="dotNET", year=2013, earnings=48000)),
...     Row(training="expert", sales=Row(course="Java", year=2013, earnings=30000)),
... ])  
>>> df2.show()  
+--------+--------------------+
|training|               sales|
+--------+--------------------+
|  expert|{dotNET, 2012, 10...|
|  junior| {Java, 2012, 20000}|
|  expert|{dotNET, 2012, 5000}|
|  junior|{dotNET, 2013, 48...|
|  expert| {Java, 2013, 30000}|
+--------+--------------------+

```


Compute the sum of earnings for each year by course with each course as a separate column

```
>>> df1.groupBy("year").pivot(
...     "course", ["dotNET", "Java"]).sum("earnings").sort("year").show()
+----+------+-----+
|year|dotNET| Java|
+----+------+-----+
|2012| 15000|20000|
|2013| 48000|30000|
+----+------+-----+

```


Or without specifying column values (less efficient)

```
>>> df1.groupBy("year").pivot("course").sum("earnings").sort("year").show()
+----+-----+------+
|year| Java|dotNET|
+----+-----+------+
|2012|20000| 15000|
|2013|30000| 48000|
+----+-----+------+
>>> df2.groupBy(
...     "sales.year").pivot("sales.course").sum("sales.earnings").sort("year").show()
... 
+----+-----+------+
|year| Java|dotNET|
+----+-----+------+
|2012|20000| 15000|
|2013|30000| 48000|
+----+-----+------+

```


# pyspark.sql.GroupedData.sum — PySpark 4.0.1 documentation
GroupedData.sum(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData.sum)
[#](#pyspark.sql.GroupedData.sum "Permalink to this definition")

Computes the sum for each numeric columns for each group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**str

column names. Non-numeric columns are ignored.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice", 80), (3, "Alice", 100),
...     (5, "Bob", 120), (10, "Bob", 140)], ["age", "name", "height"])
>>> df.show()
+---+-----+------+
|age| name|height|
+---+-----+------+
|  2|Alice|    80|
|  3|Alice|   100|
|  5|  Bob|   120|
| 10|  Bob|   140|
+---+-----+------+

```


Group-by name, and calculate the sum of the age in each group.

```
>>> df.groupBy("name").sum("age").sort("name").show()
+-----+--------+
| name|sum(age)|
+-----+--------+
|Alice|       5|
|  Bob|      15|
+-----+--------+

```


Calculate the sum of the age and height in all data.

```
>>> df.groupBy().sum("age", "height").show()
+--------+-----------+
|sum(age)|sum(height)|
+--------+-----------+
|      20|        440|
+--------+-----------+

```

# pyspark.sql.GroupedData.transformWithStateInPandas — PySpark 4.0.1 documentation
GroupedData.transformWithStateInPandas(_statefulProcessor_, _outputStructType_, _outputMode_, _timeMode_, _initialState\=None_, _eventTimeColumnName\=''_)
[#](#pyspark.sql.GroupedData.transformWithStateInPandas "Permalink to this definition")

Invokes methods defined in the stateful processor used in arbitrary state API v2. It requires protobuf, pandas and pyarrow as dependencies to process input/state data. We allow the user to act on per-group set of input rows along with keyed state and the user can choose to output/return 0 or more rows.

For a streaming dataframe, we will repeatedly invoke the interface methods for new rows in each trigger and the user’s state/state variables will be stored persistently across invocations.

The statefulProcessor should be a Python class that implements the interface defined in `StatefulProcessor`.

The outputStructType should be a `StructType` describing the schema of all elements in the returned value, pandas.DataFrame. The column labels of all elements in returned pandas.DataFrame must either match the field names in the defined schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices.

The size of each pandas.DataFrame in both the input and output can be arbitrary. The number of pandas.DataFrame in both the input and output can also be arbitrary.

New in version 4.0.0.

Parameters

**statefulProcessor**`pyspark.sql.streaming.stateful_processor.StatefulProcessor`

Instance of StatefulProcessor whose functions will be invoked by the operator.

**outputStructType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

The type of the output records. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

**outputMode**str

The output mode of the stateful processor.

**timeMode**str

The time mode semantics of the stateful processor for timers and TTL.

**initialState**[`pyspark.sql.GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData")

Optional. The grouped dataframe as initial states used for initialization of state variables in the first batch.

Notes

This function requires a full shuffle.

Examples

```
>>> from typing import Iterator
...
>>> import pandas as pd 
...
>>> from pyspark.sql import Row
>>> from pyspark.sql.functions import col, split
>>> from pyspark.sql.streaming import StatefulProcessor, StatefulProcessorHandle
>>> from pyspark.sql.types import IntegerType, LongType, StringType, StructField, StructType
...
>>> spark.conf.set("spark.sql.streaming.stateStore.providerClass",
...     "org.apache.spark.sql.execution.streaming.state.RocksDBStateStoreProvider")
... # Below is a simple example to find erroneous sensors from temperature sensor data. The
... # processor returns a count of total readings, while keeping erroneous reading counts
... # in streaming state. A violation is defined when the temperature is above 100.
... # The input data is a DataFrame with the following schema:
... #    `id: string, temperature: long`.
... # The output schema and state schema are defined as below.
>>> output_schema = StructType([
...     StructField("id", StringType(), True),
...     StructField("count", IntegerType(), True)
... ])
>>> state_schema = StructType([
...     StructField("value", IntegerType(), True)
... ])
>>> class SimpleStatefulProcessor(StatefulProcessor):
...     def init(self, handle: StatefulProcessorHandle):
...         self.num_violations_state = handle.getValueState("numViolations", state_schema)
...
...     def handleInputRows(self, key, rows):
...         new_violations = 0
...         count = 0
...         exists = self.num_violations_state.exists()
...         if exists:
...             existing_violations_row = self.num_violations_state.get()
...             existing_violations = existing_violations_row[0]
...         else:
...             existing_violations = 0
...         for pdf in rows:
...             pdf_count = pdf.count()
...             count += pdf_count.get('temperature')
...             violations_pdf = pdf.loc[pdf['temperature'] > 100]
...             new_violations += violations_pdf.count().get('temperature')
...         updated_violations = new_violations + existing_violations
...         self.num_violations_state.update((updated_violations,))
...         yield pd.DataFrame({'id': key, 'count': count})
...
...     def close(self) -> None:
...         pass

```


Input DataFrame: +—+———–+ | id|temperature| +—+———–+ | 0| 123| | 0| 23| | 1| 33| | 1| 188| | 1| 88| +—+———–+

```
>>> df.groupBy("value").transformWithStateInPandas(statefulProcessor =
...     SimpleStatefulProcessor(), outputStructType=output_schema, outputMode="Update",
...     timeMode="None") 

```


Output DataFrame: +—+—–+ | id|count| +—+—–+ | 0| 2| | 1| 3| +—+—–+


# pyspark.sql.PandasCogroupedOps.applyInArrow — PySpark 4.0.1 documentation
PandasCogroupedOps.applyInArrow(_func_, _schema_)
[\[source\]](about:blank/_modules/pyspark/sql/pandas/group_ops.html#PandasCogroupedOps.applyInArrow)
[#](#pyspark.sql.PandasCogroupedOps.applyInArrow "Permalink to this definition")

Applies a function to each cogroup using Arrow and returns the result as a DataFrame.

The function should take two pyarrow.Tables and return another pyarrow.Table. Alternatively, the user can pass a function that takes a tuple of pyarrow.Scalar grouping key(s) and the two pyarrow.Tables. For each side of the cogroup, all columns are passed together as a pyarrow.Table to the user-function and the returned pyarrow.Table are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The schema should be a `StructType` describing the schema of the returned pyarrow.Table. The column labels of the returned pyarrow.Table must either match the field names in the defined schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices. The length of the returned pyarrow.Table can be arbitrary.

New in version 4.0.0.

Parameters

**func**function

a Python native function that takes two pyarrow.Tables, and outputs a pyarrow.Table, or that takes one tuple (grouping keys) and two `pyarrow.Table`s, and outputs a `pyarrow.Table`.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the return type of the func in PySpark. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

Notes

This function requires a full shuffle. All the data of a cogroup will be loaded into memory, so the user should be aware of the potential OOM risk if data is skewed and certain groups are too large to fit in memory.

This API is unstable, and for developers.

Examples

```
>>> import pyarrow  
>>> df1 = spark.createDataFrame([(1, 1.0), (2, 2.0), (1, 3.0), (2, 4.0)], ("id", "v1"))
>>> df2 = spark.createDataFrame([(1, "x"), (2, "y")], ("id", "v2"))
>>> def summarize(l, r):
...     return pyarrow.Table.from_pydict({
...         "left": [l.num_rows],
...         "right": [r.num_rows]
...     })
>>> df1.groupby("id").cogroup(df2.groupby("id")).applyInArrow(
...     summarize, schema="left long, right long"
... ).show()  
+----+-----+
|left|right|
+----+-----+
|   2|    1|
|   2|    1|
+----+-----+

```


Alternatively, the user can define a function that takes three arguments. In this case, the grouping key(s) will be passed as the first argument and the data will be passed as the second and third arguments. The grouping key(s) will be passed as a tuple of Arrow scalars types, e.g., pyarrow.Int32Scalar and pyarrow.FloatScalar. The data will still be passed in as two pyarrow.Tables containing all columns from the original Spark DataFrames.

```
>>> def summarize(key, l, r):
...     return pyarrow.Table.from_pydict({
...         "key": [key[0].as_py()],
...         "left": [l.num_rows],
...         "right": [r.num_rows]
...     })
>>> df1.groupby("id").cogroup(df2.groupby("id")).applyInArrow(
...     summarize, schema="key long, left long, right long"
... ).show()  
+---+----+-----+
|key|left|right|
+---+----+-----+
|  1|   2|    1|
|  2|   2|    1|
+---+----+-----+

```


# pyspark.sql.PandasCogroupedOps.applyInPandas — PySpark 4.0.1 documentation
PandasCogroupedOps.applyInPandas(_func_, _schema_)
[\[source\]](about:blank/_modules/pyspark/sql/pandas/group_ops.html#PandasCogroupedOps.applyInPandas)
[#](#pyspark.sql.PandasCogroupedOps.applyInPandas "Permalink to this definition")

Applies a function to each cogroup using pandas and returns the result as a DataFrame.

The function should take two pandas.DataFrames and return another pandas.DataFrame. Alternatively, the user can pass a function that takes a tuple of the grouping key(s) and the two pandas.DataFrames. For each side of the cogroup, all columns are passed together as a pandas.DataFrame to the user-function and the returned pandas.DataFrame are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The schema should be a `StructType` describing the schema of the returned pandas.DataFrame. The column labels of the returned pandas.DataFrame must either match the field names in the defined schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices. The length of the returned pandas.DataFrame can be arbitrary.

New in version 3.0.0.

Changed in version 3.4.0: Support Spark Connect.

Parameters

**func**function

a Python native function that takes two pandas.DataFrames, and outputs a pandas.DataFrame, or that takes one tuple (grouping keys) and two `pandas.DataFrame`s, and outputs a `pandas.DataFrame`.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the return type of the func in PySpark. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

Notes

This function requires a full shuffle. All the data of a cogroup will be loaded into memory, so the user should be aware of the potential OOM risk if data is skewed and certain groups are too large to fit in memory.

Examples

```
>>> df1 = spark.createDataFrame(
...     [(20000101, 1, 1.0), (20000101, 2, 2.0), (20000102, 1, 3.0), (20000102, 2, 4.0)],
...     ("time", "id", "v1"))
>>> df2 = spark.createDataFrame(
...     [(20000101, 1, "x"), (20000101, 2, "y")],
...     ("time", "id", "v2"))
>>> def asof_join(l, r):
...     return pd.merge_asof(l, r, on="time", by="id")
...
>>> df1.groupby("id").cogroup(df2.groupby("id")).applyInPandas(
...     asof_join, schema="time int, id int, v1 double, v2 string"
... ).show()  
+--------+---+---+---+
|    time| id| v1| v2|
+--------+---+---+---+
|20000101|  1|1.0|  x|
|20000102|  1|3.0|  x|
|20000101|  2|2.0|  y|
|20000102|  2|4.0|  y|
+--------+---+---+---+

```


Alternatively, the user can define a function that takes three arguments. In this case, the grouping key(s) will be passed as the first argument and the data will be passed as the second and third arguments. The grouping key(s) will be passed as a tuple of numpy data types, e.g., numpy.int32 and numpy.float64. The data will still be passed in as two pandas.DataFrame containing all columns from the original Spark DataFrames.

```
>>> def asof_join(k, l, r):
...     if k == (1,):
...         return pd.merge_asof(l, r, on="time", by="id")
...     else:
...         return pd.DataFrame(columns=['time', 'id', 'v1', 'v2'])
...
>>> df1.groupby("id").cogroup(df2.groupby("id")).applyInPandas(
...     asof_join, "time int, id int, v1 double, v2 string").show()  
+--------+---+---+---+
|    time| id| v1| v2|
+--------+---+---+---+
|20000101|  1|1.0|  x|
|20000102|  1|3.0|  x|
+--------+---+---+---+

```

