# Apache Arrow in PySpark — PySpark 4.0.1 documentation
Apache Arrow is an in-memory columnar data format that is used in Spark to efficiently transfer data between JVM and Python processes. This currently is most beneficial to Python users that work with Pandas/NumPy data. Its usage is not automatic and might require some minor changes to configuration or code to take full advantage and ensure compatibility. This guide will give a high-level description of how to use Arrow in Spark and highlight any differences when working with Arrow-enabled data.

Ensure PyArrow Installed[#](#ensure-pyarrow-installed "Permalink to this headline")
-----------------------------------------------------------------------------------

To use Apache Arrow in PySpark, [the recommended version of PyArrow](#recommended-pandas-and-pyarrow-versions) should be installed. If you install PySpark using pip, then PyArrow can be brought in as an extra dependency of the SQL module with the command `pip install pyspark[sql]`. Otherwise, you must ensure that PyArrow is installed and available on all cluster nodes. You can install it using pip or conda from the conda-forge channel. See PyArrow [installation](https://arrow.apache.org/docs/python/install.html) for details.

Conversion to/from Arrow Table[#](#conversion-to-from-arrow-table "Permalink to this headline")
-----------------------------------------------------------------------------------------------

From Spark 4.0, you can create a Spark DataFrame from a PyArrow Table with [`SparkSession.createDataFrame()`](about:blank/reference/pyspark.sql/api/pyspark.sql.SparkSession.createDataFrame.html#pyspark.sql.SparkSession.createDataFrame "pyspark.sql.SparkSession.createDataFrame"), and you can convert a Spark DataFrame to a PyArrow Table with [`DataFrame.toArrow()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.toArrow.html#pyspark.sql.DataFrame.toArrow "pyspark.sql.DataFrame.toArrow").

```
import pyarrow as pa
import numpy as np

# Create a PyArrow Table
table = pa.table([pa.array(np.random.rand(100)) for i in range(3)], names=["a", "b", "c"])

# Create a Spark DataFrame from the PyArrow Table
df = spark.createDataFrame(table)

# Convert the Spark DataFrame to a PyArrow Table
result_table = df.select("*").toArrow()

print(result_table.schema)
# a: double
# b: double
# c: double

```


Note that [`DataFrame.toArrow()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.toArrow.html#pyspark.sql.DataFrame.toArrow "pyspark.sql.DataFrame.toArrow") results in the collection of all records in the DataFrame to the driver program and should be done on a small subset of the data. Not all Spark and Arrow data types are currently supported and an error can be raised if a column has an unsupported type.

Enabling for Conversion to/from Pandas[#](#enabling-for-conversion-to-from-pandas "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

Arrow is available as an optimization when converting a Spark DataFrame to a Pandas DataFrame using the call [`DataFrame.toPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.toPandas.html#pyspark.sql.DataFrame.toPandas "pyspark.sql.DataFrame.toPandas") and when creating a Spark DataFrame from a Pandas DataFrame with [`SparkSession.createDataFrame()`](about:blank/reference/pyspark.sql/api/pyspark.sql.SparkSession.createDataFrame.html#pyspark.sql.SparkSession.createDataFrame "pyspark.sql.SparkSession.createDataFrame"). To use Arrow when executing these calls, users need to first set the Spark configuration `spark.sql.execution.arrow.pyspark.enabled` to `true`. This is disabled by default.

In addition, optimizations enabled by `spark.sql.execution.arrow.pyspark.enabled` could fallback automatically to non-Arrow optimization implementation if an error occurs before the actual computation within Spark. This can be controlled by `spark.sql.execution.arrow.pyspark.fallback.enabled`.

```
import numpy as np
import pandas as pd

# Enable Arrow-based columnar data transfers
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")

# Generate a Pandas DataFrame
pdf = pd.DataFrame(np.random.rand(100, 3))

# Create a Spark DataFrame from a Pandas DataFrame using Arrow
df = spark.createDataFrame(pdf)

# Convert the Spark DataFrame back to a Pandas DataFrame using Arrow
result_pdf = df.select("*").toPandas()

print("Pandas DataFrame result statistics:\n%s\n" % str(result_pdf.describe()))

```


Using the above optimizations with Arrow will produce the same results as when Arrow is not enabled.

Note that even with Arrow, [`DataFrame.toPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.toPandas.html#pyspark.sql.DataFrame.toPandas "pyspark.sql.DataFrame.toPandas") results in the collection of all records in the DataFrame to the driver program and should be done on a small subset of the data. Not all Spark data types are currently supported and an error can be raised if a column has an unsupported type. If an error occurs during [`SparkSession.createDataFrame()`](about:blank/reference/pyspark.sql/api/pyspark.sql.SparkSession.createDataFrame.html#pyspark.sql.SparkSession.createDataFrame "pyspark.sql.SparkSession.createDataFrame"), Spark will fall back to create the DataFrame without Arrow.

Pandas UDFs (a.k.a. Vectorized UDFs)
[#](#pandas-udfs-a-k-a-vectorized-udfs "Permalink to this headline")
--------------------------------------------------------------------------------------------------------

Pandas UDFs are user defined functions that are executed by Spark using Arrow to transfer data and Pandas to work with the data, which allows vectorized operations. A Pandas UDF is defined using the [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") as a decorator or to wrap the function, and no additional configuration is required. A Pandas UDF behaves as a regular PySpark function API in general.

Before Spark 3.0, Pandas UDFs used to be defined with `pyspark.sql.functions.PandasUDFType`. From Spark 3.0 with Python 3.6+, you can also use [Python type hints](https://www.python.org/dev/peps/pep-0484). Using Python type hints is preferred and using `pyspark.sql.functions.PandasUDFType` will be deprecated in the future release.

Note that the type hint should use `pandas.Series` in all cases but there is one variant that `pandas.DataFrame` should be used for its input or output type hint instead when the input or output column is of [`StructType`](about:blank/reference/pyspark.sql/api/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType"). The following example shows a Pandas UDF which takes long column, string column and struct column, and outputs a struct column. It requires the function to specify the type hints of `pandas.Series` and `pandas.DataFrame` as below:

```
import pandas as pd

from pyspark.sql.functions import pandas_udf

@pandas_udf("col1 string, col2 long")  # type: ignore[call-overload]
def func(s1: pd.Series, s2: pd.Series, s3: pd.DataFrame) -> pd.DataFrame:
    s3['col2'] = s1 + s2.str.len()
    return s3

# Create a Spark DataFrame that has three columns including a struct column.
df = spark.createDataFrame(
    [[1, "a string", ("a nested string",)]],
    "long_col long, string_col string, struct_col struct<col1:string>")

df.printSchema()
# root
# |-- long_column: long (nullable = true)
# |-- string_column: string (nullable = true)
# |-- struct_column: struct (nullable = true)
# |    |-- col1: string (nullable = true)

df.select(func("long_col", "string_col", "struct_col")).printSchema()
# |-- func(long_col, string_col, struct_col): struct (nullable = true)
# |    |-- col1: string (nullable = true)
# |    |-- col2: long (nullable = true)

```


In the following sections, it describes the combinations of the supported type hints. For simplicity, `pandas.DataFrame` variant is omitted.

### Series to Series[#](#series-to-series "Permalink to this headline")

The type hint can be expressed as `pandas.Series`, … -> `pandas.Series`.

By using [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") with the function having such type hints above, it creates a Pandas UDF where the given function takes one or more `pandas.Series` and outputs one `pandas.Series`. The output of the function should always be of the same length as the input. Internally, PySpark will execute a Pandas UDF by splitting columns into batches and calling the function for each batch as a subset of the data, then concatenating the results together.

The following example shows how to create this Pandas UDF that computes the product of 2 columns.

```
import pandas as pd

from pyspark.sql.functions import col, pandas_udf
from pyspark.sql.types import LongType

# Declare the function and create the UDF
def multiply_func(a: pd.Series, b: pd.Series) -> pd.Series:
    return a * b

multiply = pandas_udf(multiply_func, returnType=LongType())  # type: ignore[call-overload]

# The function for a pandas_udf should be able to execute with local Pandas data
x = pd.Series([1, 2, 3])
print(multiply_func(x, x))
# 0    1
# 1    4
# 2    9
# dtype: int64

# Create a Spark DataFrame, 'spark' is an existing SparkSession
df = spark.createDataFrame(pd.DataFrame(x, columns=["x"]))

# Execute function as a Spark vectorized UDF
df.select(multiply(col("x"), col("x"))).show()
# +-------------------+
# |multiply_func(x, x)|
# +-------------------+
# |                  1|
# |                  4|
# |                  9|
# +-------------------+

```


For detailed usage, please see [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf").

### Iterator of Series to Iterator of Series[#](#iterator-of-series-to-iterator-of-series "Permalink to this headline")

The type hint can be expressed as `Iterator[pandas.Series]` -> `Iterator[pandas.Series]`.

By using [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") with the function having such type hints above, it creates a Pandas UDF where the given function takes an iterator of `pandas.Series` and outputs an iterator of `pandas.Series`. The length of the entire output from the function should be the same length of the entire input; therefore, it can prefetch the data from the input iterator as long as the lengths are the same. In this case, the created Pandas UDF requires one input column when the Pandas UDF is called. To use multiple input columns, a different type hint is required. See Iterator of Multiple Series to Iterator of Series.

It is also useful when the UDF execution requires initializing some states although internally it works identically as Series to Series case. The pseudocode below illustrates the example.

```
@pandas_udf("long")
def calculate(iterator: Iterator[pd.Series]) -> Iterator[pd.Series]:
    # Do some expensive initialization with a state
    state = very_expensive_initialization()
    for x in iterator:
        # Use that state for the whole iterator.
        yield calculate_with_state(x, state)

df.select(calculate("value")).show()

```


The following example shows how to create this Pandas UDF:

```
from typing import Iterator

import pandas as pd

from pyspark.sql.functions import pandas_udf

pdf = pd.DataFrame([1, 2, 3], columns=["x"])
df = spark.createDataFrame(pdf)

# Declare the function and create the UDF
@pandas_udf("long")  # type: ignore[call-overload]
def plus_one(iterator: Iterator[pd.Series]) -> Iterator[pd.Series]:
    for x in iterator:
        yield x + 1

df.select(plus_one("x")).show()
# +-----------+
# |plus_one(x)|
# +-----------+
# |          2|
# |          3|
# |          4|
# +-----------+

```


For detailed usage, please see [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf").

### Iterator of Multiple Series to Iterator of Series[#](#iterator-of-multiple-series-to-iterator-of-series "Permalink to this headline")

The type hint can be expressed as `Iterator[Tuple[pandas.Series, ...]]` -> `Iterator[pandas.Series]`.

By using [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") with the function having such type hints above, it creates a Pandas UDF where the given function takes an iterator of a tuple of multiple `pandas.Series` and outputs an iterator of `pandas.Series`. In this case, the created pandas UDF requires multiple input columns as many as the series in the tuple when the Pandas UDF is called. Otherwise, it has the same characteristics and restrictions as the Iterator of Series to Iterator of Series case.

The following example shows how to create this Pandas UDF:

```
from typing import Iterator, Tuple

import pandas as pd

from pyspark.sql.functions import pandas_udf

pdf = pd.DataFrame([1, 2, 3], columns=["x"])
df = spark.createDataFrame(pdf)

# Declare the function and create the UDF
@pandas_udf("long")  # type: ignore[call-overload]
def multiply_two_cols(
        iterator: Iterator[Tuple[pd.Series, pd.Series]]) -> Iterator[pd.Series]:
    for a, b in iterator:
        yield a * b

df.select(multiply_two_cols("x", "x")).show()
# +-----------------------+
# |multiply_two_cols(x, x)|
# +-----------------------+
# |                      1|
# |                      4|
# |                      9|
# +-----------------------+

```


For detailed usage, please see [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf").

### Series to Scalar[#](#series-to-scalar "Permalink to this headline")

The type hint can be expressed as `pandas.Series`, … -> `Any`.

By using [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") with the function having such type hints above, it creates a Pandas UDF similar to PySpark’s aggregate functions. The given function takes pandas.Series and returns a scalar value. The return type should be a primitive data type, and the returned scalar can be either a python primitive type, e.g., `int` or `float` or a numpy data type, e.g., `numpy.int64` or `numpy.float64`. `Any` should ideally be a specific scalar type accordingly.

This UDF can be also used with [`GroupedData.agg()`](about:blank/reference/pyspark.sql/api/pyspark.sql.GroupedData.agg.html#pyspark.sql.GroupedData.agg "pyspark.sql.GroupedData.agg") and Window. It defines an aggregation from one or more `pandas.Series` to a scalar value, where each `pandas.Series` represents a column within the group or window.

Note that this type of UDF does not support partial aggregation and all data for a group or window will be loaded into memory. Also, only unbounded window is supported with Grouped aggregate Pandas UDFs currently. The following example shows how to use this type of UDF to compute mean with a group-by and window operations:

```
import pandas as pd

from pyspark.sql.functions import pandas_udf
from pyspark.sql import Window

df = spark.createDataFrame(
    [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
    ("id", "v"))

# Declare the function and create the UDF
@pandas_udf("double")  # type: ignore[call-overload]
def mean_udf(v: pd.Series) -> float:
    return v.mean()

df.select(mean_udf(df['v'])).show()
# +-----------+
# |mean_udf(v)|
# +-----------+
# |        4.2|
# +-----------+

df.groupby("id").agg(mean_udf(df['v'])).show()
# +---+-----------+
# | id|mean_udf(v)|
# +---+-----------+
# |  1|        1.5|
# |  2|        6.0|
# +---+-----------+

w = Window \
    .partitionBy('id') \
    .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
df.withColumn('mean_v', mean_udf(df['v']).over(w)).show()
# +---+----+------+
# | id|   v|mean_v|
# +---+----+------+
# |  1| 1.0|   1.5|
# |  1| 2.0|   1.5|
# |  2| 3.0|   6.0|
# |  2| 5.0|   6.0|
# |  2|10.0|   6.0|
# +---+----+------+

```


For detailed usage, please see [`pandas_udf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf").

Pandas Function APIs[#](#pandas-function-apis "Permalink to this headline")
---------------------------------------------------------------------------

Pandas Function APIs can directly apply a Python native function against the whole [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by using Pandas instances. Internally it works similarly with Pandas UDFs by using Arrow to transfer data and Pandas to work with the data, which allows vectorized operations. However, a Pandas Function API behaves as a regular API under PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") instead of [`Column`](about:blank/reference/pyspark.sql/api/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), and Python type hints in Pandas Functions APIs are optional and do not affect how it works internally at this moment although they might be required in the future.

From Spark 3.0, grouped map pandas UDF is now categorized as a separate Pandas Function API, `DataFrame.groupby().applyInPandas()`. It is still possible to use it with `pyspark.sql.functions.PandasUDFType` and `DataFrame.groupby().apply()` as it was; however, it is preferred to use `DataFrame.groupby().applyInPandas()` directly. Using `pyspark.sql.functions.PandasUDFType` will be deprecated in the future.

### Grouped Map[#](#grouped-map "Permalink to this headline")

Grouped map operations with Pandas instances are supported by `DataFrame.groupby().applyInPandas()` which requires a Python function that takes a `pandas.DataFrame` and return another `pandas.DataFrame`. It maps each group to each `pandas.DataFrame` in the Python function.

This API implements the “split-apply-combine” pattern which consists of three steps:

*   Split the data into groups by using [`DataFrame.groupBy()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.groupBy.html#pyspark.sql.DataFrame.groupBy "pyspark.sql.DataFrame.groupBy").
    
*   Apply a function on each group. The input and output of the function are both `pandas.DataFrame`. The input data contains all the rows and columns for each group.
    
*   Combine the results into a new PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").
    

To use `DataFrame.groupBy().applyInPandas()`, the user needs to define the following:

*   A Python function that defines the computation for each group.
    
*   A `StructType` object or a string that defines the schema of the output PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").
    

The column labels of the returned `pandas.DataFrame` must either match the field names in the defined output schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices. See [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame) on how to label columns when constructing a `pandas.DataFrame`.

Note that all data for a group will be loaded into memory before the function is applied. This can lead to out of memory exceptions, especially if the group sizes are skewed. The configuration for [maxRecordsPerBatch](#setting-arrow-batch-size) is not applied on groups and it is up to the user to ensure that the grouped data will fit into the available memory.

The following example shows how to use `DataFrame.groupby().applyInPandas()` to subtract the mean from each value in the group.

```
df = spark.createDataFrame(
    [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)],
    ("id", "v"))

def subtract_mean(pdf: pd.DataFrame) -> pd.DataFrame:
    # pdf is a pandas.DataFrame
    v = pdf.v
    return pdf.assign(v=v - v.mean())

df.groupby("id").applyInPandas(subtract_mean, schema="id long, v double").show()
# +---+----+
# | id|   v|
# +---+----+
# |  1|-0.5|
# |  1| 0.5|
# |  2|-3.0|
# |  2|-1.0|
# |  2| 4.0|
# +---+----+

```


For detailed usage, please see please see [`GroupedData.applyInPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.GroupedData.applyInPandas.html#pyspark.sql.GroupedData.applyInPandas "pyspark.sql.GroupedData.applyInPandas")

### Map[#](#map "Permalink to this headline")

Map operations with Pandas instances are supported by [`DataFrame.mapInPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.mapInPandas.html#pyspark.sql.DataFrame.mapInPandas "pyspark.sql.DataFrame.mapInPandas") which maps an iterator of `pandas.DataFrame`s to another iterator of `pandas.DataFrame`s that represents the current PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") and returns the result as a PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). The function takes and outputs an iterator of `pandas.DataFrame`. It can return the output of arbitrary length in contrast to some Pandas UDFs although internally it works similarly with Series to Series Pandas UDF.

The following example shows how to use [`DataFrame.mapInPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.mapInPandas.html#pyspark.sql.DataFrame.mapInPandas "pyspark.sql.DataFrame.mapInPandas"):

```
df = spark.createDataFrame([(1, 21), (2, 30)], ("id", "age"))

def filter_func(iterator: Iterable[pd.DataFrame]) -> Iterable[pd.DataFrame]:
    for pdf in iterator:
        yield pdf[pdf.id == 1]

df.mapInPandas(filter_func, schema=df.schema).show()
# +---+---+
# | id|age|
# +---+---+
# |  1| 21|
# +---+---+

```


For detailed usage, please see [`DataFrame.mapInPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.mapInPandas.html#pyspark.sql.DataFrame.mapInPandas "pyspark.sql.DataFrame.mapInPandas").

### Co-grouped Map[#](#co-grouped-map "Permalink to this headline")

Co-grouped map operations with Pandas instances are supported by `DataFrame.groupby().cogroup().applyInPandas()` which allows two PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")s to be cogrouped by a common key and then a Python function applied to each cogroup. It consists of the following steps:

*   Shuffle the data such that the groups of each dataframe which share a key are cogrouped together.
    
*   Apply a function to each cogroup. The input of the function is two `pandas.DataFrame` (with an optional tuple representing the key). The output of the function is a `pandas.DataFrame`.
    
*   Combine the `pandas.DataFrame`s from all groups into a new PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").
    

To use `groupBy().cogroup().applyInPandas()`, the user needs to define the following:

*   A Python function that defines the computation for each cogroup.
    
*   A `StructType` object or a string that defines the schema of the output PySpark [`DataFrame`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").
    

The column labels of the returned `pandas.DataFrame` must either match the field names in the defined output schema if specified as strings, or match the field data types by position if not strings, e.g. integer indices. See [pandas.DataFrame](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html#pandas.DataFrame). on how to label columns when constructing a `pandas.DataFrame`.

Note that all data for a cogroup will be loaded into memory before the function is applied. This can lead to out of memory exceptions, especially if the group sizes are skewed. The configuration for [maxRecordsPerBatch](#setting-arrow-batch-size) is not applied and it is up to the user to ensure that the cogrouped data will fit into the available memory.

The following example shows how to use `DataFrame.groupby().cogroup().applyInPandas()` to perform an asof join between two datasets.

```
import pandas as pd

df1 = spark.createDataFrame(
    [(20000101, 1, 1.0), (20000101, 2, 2.0), (20000102, 1, 3.0), (20000102, 2, 4.0)],
    ("time", "id", "v1"))

df2 = spark.createDataFrame(
    [(20000101, 1, "x"), (20000101, 2, "y")],
    ("time", "id", "v2"))

def merge_ordered(left: pd.DataFrame, right: pd.DataFrame) -> pd.DataFrame:
    return pd.merge_ordered(left, right)

df1.groupby("id").cogroup(df2.groupby("id")).applyInPandas(
    merge_ordered, schema="time int, id int, v1 double, v2 string").show()
# +--------+---+---+----+
# |    time| id| v1|  v2|
# +--------+---+---+----+
# |20000101|  1|1.0|   x|
# |20000102|  1|3.0|null|
# |20000101|  2|2.0|   y|
# |20000102|  2|4.0|null|
# +--------+---+---+----+

```


For detailed usage, please see [`PandasCogroupedOps.applyInPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.PandasCogroupedOps.applyInPandas.html#pyspark.sql.PandasCogroupedOps.applyInPandas "pyspark.sql.PandasCogroupedOps.applyInPandas")

Arrow Python UDFs[#](#arrow-python-udfs "Permalink to this headline")
---------------------------------------------------------------------

Arrow Python UDFs are user defined functions that are executed row-by-row, utilizing Arrow for efficient batch data transfer and serialization. To define an Arrow Python UDF, you can use the `udf()` decorator or wrap the function with the `udf()` method, ensuring the `useArrow` parameter is set to True. Additionally, you can enable Arrow optimization for Python UDFs throughout the entire SparkSession by setting the Spark configuration `spark.sql.execution.pythonUDF.arrow.enabled` to true. It’s important to note that the Spark configuration takes effect only when `useArrow` is either not set or set to None.

The type hints for Arrow Python UDFs should be specified in the same way as for default, pickled Python UDFs.

Here’s an example that demonstrates the usage of both a default, pickled Python UDF and an Arrow Python UDF:

```
from pyspark.sql.functions import udf

@udf(returnType='int')  # A default, pickled Python UDF
def slen(s):  # type: ignore[no-untyped-def]
    return len(s)

@udf(returnType='int', useArrow=True)  # An Arrow Python UDF
def arrow_slen(s):  # type: ignore[no-untyped-def]
    return len(s)

df = spark.createDataFrame([(1, "John Doe", 21)], ("id", "name", "age"))

df.select(slen("name"), arrow_slen("name")).show()
# +----------+----------------+
# |slen(name)|arrow_slen(name)|
# +----------+----------------+
# |         8|               8|
# +----------+----------------+


```


Compared to the default, pickled Python UDFs, Arrow Python UDFs provide a more coherent type coercion mechanism. UDF type coercion poses challenges when the Python instances returned by UDFs do not align with the user-specified return type. The default, pickled Python UDFs’ type coercion has certain limitations, such as relying on None as a fallback for type mismatches, leading to potential ambiguity and data loss. Additionally, converting date, datetime, and tuples to strings can yield ambiguous results. Arrow Python UDFs, on the other hand, leverage Arrow’s capabilities to standardize type coercion and address these issues effectively.

Usage Notes[#](#usage-notes "Permalink to this headline")
---------------------------------------------------------

### Supported SQL Types[#](#supported-sql-types "Permalink to this headline")

Currently, all Spark SQL data types are supported by Arrow-based conversion except [`ArrayType`](about:blank/reference/pyspark.sql/api/pyspark.sql.types.ArrayType.html#pyspark.sql.types.ArrayType "pyspark.sql.types.ArrayType") of [`TimestampType`](about:blank/reference/pyspark.sql/api/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType"). [`MapType`](about:blank/reference/pyspark.sql/api/pyspark.sql.types.MapType.html#pyspark.sql.types.MapType "pyspark.sql.types.MapType") and [`ArrayType`](about:blank/reference/pyspark.sql/api/pyspark.sql.types.ArrayType.html#pyspark.sql.types.ArrayType "pyspark.sql.types.ArrayType") of nested [`StructType`](about:blank/reference/pyspark.sql/api/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") are only supported when using PyArrow 2.0.0 and above.

### Setting Arrow Batch Size[#](#setting-arrow-batch-size "Permalink to this headline")

Data partitions in Spark are converted into Arrow record batches, which can temporarily lead to high memory usage in the JVM. To avoid possible out of memory exceptions, the size of the Arrow record batches can be adjusted by setting the conf `spark.sql.execution.arrow.maxRecordsPerBatch` to an integer that will determine the maximum number of rows for each batch. The default value is 10,000 records per batch. If the number of columns is large, the value should be adjusted accordingly. Using this limit, each data partition will be made into 1 or more record batches for processing.

### Timestamp with Time Zone Semantics[#](#timestamp-with-time-zone-semantics "Permalink to this headline")

Spark internally stores timestamps as UTC values, and timestamp data that is brought in without a specified time zone is converted as local time to UTC with microsecond resolution. When timestamp data is exported or displayed in Spark, the session time zone is used to localize the timestamp values. The session time zone is set with the configuration `spark.sql.session.timeZone` and will default to the JVM system local time zone if not set. Pandas uses a `datetime64` type with nanosecond resolution, `datetime64[ns]`, with optional time zone on a per-column basis.

When timestamp data is transferred from Spark to Pandas it will be converted to nanoseconds and each column will be converted to the Spark session time zone then localized to that time zone, which removes the time zone and displays values as local time. This will occur when calling [`DataFrame.toPandas()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.toPandas.html#pyspark.sql.DataFrame.toPandas "pyspark.sql.DataFrame.toPandas") or `pandas_udf` with timestamp columns.

When timestamp data is transferred from Spark to a PyArrow Table, it will remain in microsecond resolution with the UTC time zone. This occurs when calling [`DataFrame.toArrow()`](about:blank/reference/pyspark.sql/api/pyspark.sql.DataFrame.toArrow.html#pyspark.sql.DataFrame.toArrow "pyspark.sql.DataFrame.toArrow") with timestamp columns.

When timestamp data is transferred from Pandas or PyArrow to Spark, it will be converted to UTC microseconds. This occurs when calling [`SparkSession.createDataFrame()`](about:blank/reference/pyspark.sql/api/pyspark.sql.SparkSession.createDataFrame.html#pyspark.sql.SparkSession.createDataFrame "pyspark.sql.SparkSession.createDataFrame") with a Pandas DataFrame or PyArrow Table, or when returning a timestamp from a `pandas_udf`. These conversions are done automatically to ensure Spark will have data in the expected format, so it is not necessary to do any of these conversions yourself. Any nanosecond values will be truncated.

Note that a standard UDF (non-Pandas) will load timestamp data as Python datetime objects, which is different from a Pandas timestamp. It is recommended to use Pandas time series functionality when working with timestamps in `pandas_udf`s to get the best performance, see [here](https://pandas.pydata.org/pandas-docs/stable/timeseries.html) for details.

### Recommended Pandas and PyArrow Versions[#](#recommended-pandas-and-pyarrow-versions "Permalink to this headline")

For usage with pyspark.sql, the minimum supported versions of Pandas is 2.0.0 and PyArrow is 11.0.0. Higher versions may be used, however, compatibility and data correctness can not be guaranteed and should be verified by the user.

### Setting Arrow `self_destruct` for memory savings[#](#setting-arrow-self-destruct-for-memory-savings "Permalink to this headline")

Since Spark 3.2, the Spark configuration `spark.sql.execution.arrow.pyspark.selfDestruct.enabled` can be used to enable PyArrow’s `self_destruct` feature, which can save memory when creating a Pandas DataFrame via `toPandas` by freeing Arrow-allocated memory while building the Pandas DataFrame. This option can also save memory when creating a PyArrow Table via `toArrow`. This option is experimental. When used with `toPandas`, some operations may fail on the resulting Pandas DataFrame due to immutable backing arrays. Typically, you would see the error `ValueError: buffer source array is read-only`. Newer versions of Pandas may fix these errors by improving support for such cases. You can work around this error by copying the column(s) beforehand. Additionally, this conversion may be slower because it is single-threaded.