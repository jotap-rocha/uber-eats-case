# UDF — PySpark 4.0.1 documentation


* udf.UserDefinedFunction.asNondeterministic(): udf.UserDefinedFunction.returnType
  * Updates UserDefinedFunction to nondeterministic.: 
* udf.UserDefinedFunction.asNondeterministic(): UDFRegistration.register(name, f[, returnType])
  * Updates UserDefinedFunction to nondeterministic.: Register a Python function (including lambda function) or a user-defined function as a SQL function.
* udf.UserDefinedFunction.asNondeterministic(): UDFRegistration.registerJavaFunction(name, ...)
  * Updates UserDefinedFunction to nondeterministic.: Register a Java user-defined function as a SQL function.
* udf.UserDefinedFunction.asNondeterministic(): UDFRegistration.registerJavaUDAF(name, ...)
  * Updates UserDefinedFunction to nondeterministic.: Register a Java user-defined aggregate function as a SQL function.


# pyspark.sql.udf.UserDefinedFunction.asNondeterministic — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [UDF](../udf.html)
*   pyspark.sql.udf.UserDefinedFunction.asNondeterministic

UserDefinedFunction.asNondeterministic()
[\[source\]](about:blank/_modules/pyspark/sql/udf.html#UserDefinedFunction.asNondeterministic)
[#](#pyspark.sql.udf.UserDefinedFunction.asNondeterministic "Permalink to this definition")

Updates UserDefinedFunction to nondeterministic.

New in version 2.3.

# pyspark.sql.udf.UserDefinedFunction.returnType — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [UDF](../udf.html)
*   pyspark.sql.udf.UserDefinedFunction.returnType

_property_ UserDefinedFunction.returnType[#](#pyspark.sql.udf.UserDefinedFunction.returnType "Permalink to this definition")


# pyspark.sql.UDFRegistration.register — PySpark 4.0.1 documentation
UDFRegistration.register(_name_, _f_, _returnType\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/udf.html#UDFRegistration.register)
[#](#pyspark.sql.UDFRegistration.register "Permalink to this definition")

Register a Python function (including lambda function) or a user-defined function as a SQL function.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str,

name of the user-defined function in SQL statements.

**f**function, [`pyspark.sql.functions.udf()`](about:blank/pyspark.sql.functions.udf.html#pyspark.sql.functions.udf "pyspark.sql.functions.udf") or [`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf")

a Python function, or a user-defined function. The user-defined function can be either row-at-a-time or vectorized. See [`pyspark.sql.functions.udf()`](about:blank/pyspark.sql.functions.udf.html#pyspark.sql.functions.udf "pyspark.sql.functions.udf") and [`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf").

**returnType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str, optional

the return type of the registered user-defined function. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string. returnType can be optionally specified when f is a Python function but not when f is a user-defined function. Please see the examples below.

Returns

function

a user-defined function

Notes

To register a nondeterministic Python function, users need to first build a nondeterministic user-defined function for the Python function and then register it as a SQL function.

Examples

1.  When f is a Python function:
    
    > returnType defaults to string type and can be optionally specified. The produced object must match the specified type. In this case, this API works as if register(name, f, returnType=StringType()).
    > 
    > ```
>>> strlen = spark.udf.register("stringLengthString", lambda x: len(x))
>>> spark.sql("SELECT stringLengthString('test')").collect()
[Row(stringLengthString(test)='4')]

```

    > 
    > ```
>>> spark.sql("SELECT 'foo' AS text").select(strlen("text")).collect()
[Row(stringLengthString(text)='3')]

```

    > 
    > ```
>>> from pyspark.sql.types import IntegerType
>>> _ = spark.udf.register("stringLengthInt", lambda x: len(x), IntegerType())
>>> spark.sql("SELECT stringLengthInt('test')").collect()
[Row(stringLengthInt(test)=4)]

```

    > 
    > ```
>>> from pyspark.sql.types import IntegerType
>>> _ = spark.udf.register("stringLengthInt", lambda x: len(x), IntegerType())
>>> spark.sql("SELECT stringLengthInt('test')").collect()
[Row(stringLengthInt(test)=4)]

```

    
2.  When f is a user-defined function (from Spark 2.3.0):
    
    > Spark uses the return type of the given user-defined function as the return type of the registered user-defined function. returnType should not be specified. In this case, this API works as if register(name, f).
    > 
    > ```
>>> from pyspark.sql.types import IntegerType
>>> from pyspark.sql.functions import udf
>>> slen = udf(lambda s: len(s), IntegerType())
>>> _ = spark.udf.register("slen", slen)
>>> spark.sql("SELECT slen('test')").collect()
[Row(slen(test)=4)]

```

    > 
    > ```
>>> import random
>>> from pyspark.sql.functions import udf
>>> from pyspark.sql.types import IntegerType
>>> random_udf = udf(lambda: random.randint(0, 100), IntegerType()).asNondeterministic()
>>> new_random_udf = spark.udf.register("random_udf", random_udf)
>>> spark.sql("SELECT random_udf()").collect()  
[Row(random_udf()=82)]

```

    > 
    > ```
>>> import pandas as pd  
>>> from pyspark.sql.functions import pandas_udf
>>> @pandas_udf("integer")  
... def add_one(s: pd.Series) -> pd.Series:
...     return s + 1
...
>>> _ = spark.udf.register("add_one", add_one)  
>>> spark.sql("SELECT add_one(id) FROM range(3)").collect()  
[Row(add_one(id)=1), Row(add_one(id)=2), Row(add_one(id)=3)]

```

    > 
    > ```
>>> @pandas_udf("integer")  
... def sum_udf(v: pd.Series) -> int:
...     return v.sum()
...
>>> _ = spark.udf.register("sum_udf", sum_udf)  
>>> q = "SELECT sum_udf(v1) FROM VALUES (3, 0), (2, 0), (1, 1) tbl(v1, v2) GROUP BY v2"
>>> spark.sql(q).collect()  
[Row(sum_udf(v1)=1), Row(sum_udf(v1)=5)]

```


# pyspark.sql.UDFRegistration.registerJavaFunction — PySpark 4.0.1 documentation
UDFRegistration.registerJavaFunction(_name_, _javaClassName_, _returnType\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/udf.html#UDFRegistration.registerJavaFunction)
[#](#pyspark.sql.UDFRegistration.registerJavaFunction "Permalink to this definition")

Register a Java user-defined function as a SQL function.

In addition to a name and the function itself, the return type can be optionally specified. When the return type is not specified we would infer it via reflection.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

name of the user-defined function

**javaClassName**str

fully qualified name of java class

**returnType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str, optional

the return type of the registered Java function. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

Examples

```
>>> from pyspark.sql.types import IntegerType
>>> spark.udf.registerJavaFunction(
...     "javaStringLength", "test.org.apache.spark.sql.JavaStringLength", IntegerType())
... 
>>> spark.sql("SELECT javaStringLength('test')").collect()  
[Row(javaStringLength(test)=4)]

```


```
>>> spark.udf.registerJavaFunction(
...     "javaStringLength2", "test.org.apache.spark.sql.JavaStringLength")
... 
>>> spark.sql("SELECT javaStringLength2('test')").collect()  
[Row(javaStringLength2(test)=4)]

```


```
>>> spark.udf.registerJavaFunction(
...     "javaStringLength3", "test.org.apache.spark.sql.JavaStringLength", "integer")
... 
>>> spark.sql("SELECT javaStringLength3('test')").collect()  
[Row(javaStringLength3(test)=4)]

```



# pyspark.sql.UDFRegistration.registerJavaUDAF — PySpark 4.0.1 documentation
UDFRegistration.registerJavaUDAF(_name_, _javaClassName_)
[\[source\]](about:blank/_modules/pyspark/sql/udf.html#UDFRegistration.registerJavaUDAF)
[#](#pyspark.sql.UDFRegistration.registerJavaUDAF "Permalink to this definition")

Register a Java user-defined aggregate function as a SQL function.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

namestr

name of the user-defined aggregate function

javaClassNamestr

fully qualified name of java class

Examples

```
>>> spark.udf.registerJavaUDAF("javaUDAF", "test.org.apache.spark.sql.MyDoubleAvg")
... 
>>> df = spark.createDataFrame([(1, "a"),(2, "b"), (3, "a")],["id", "name"])
>>> df.createOrReplaceTempView("df")
>>> q = "SELECT name, javaUDAF(id) as avg from df group by name order by name desc"
>>> spark.sql(q).collect()  
[Row(name='b', avg=102.0), Row(name='a', avg=102.0)]

```


