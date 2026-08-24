# UDTF — PySpark 4.0.1 documentation


* udtf.UserDefinedTableFunction.asDeterministic(): udtf.UserDefinedTableFunction.returnType
  * Updates UserDefinedTableFunction to deterministic.: 
* udtf.UserDefinedTableFunction.asDeterministic(): UDTFRegistration.register(name, f)
  * Updates UserDefinedTableFunction to deterministic.: Register a Python user-defined table function as a SQL table function.


# pyspark.sql.udtf.UserDefinedTableFunction.asDeterministic — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [UDTF](../udtf.html)
*   pyspark.sql.udtf.UserDefinedTableFunction.asDeterministic

UserDefinedTableFunction.asDeterministic()
[\[source\]](about:blank/_modules/pyspark/sql/udtf.html#UserDefinedTableFunction.asDeterministic)
[#](#pyspark.sql.udtf.UserDefinedTableFunction.asDeterministic "Permalink to this definition")

Updates UserDefinedTableFunction to deterministic.


# pyspark.sql.udtf.UserDefinedTableFunction.returnType — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [UDTF](../udtf.html)
*   pyspark.sql.udtf.UserDefinedTableFunction.returnType

_property_ UserDefinedTableFunction.returnType[#](#pyspark.sql.udtf.UserDefinedTableFunction.returnType "Permalink to this definition")


# pyspark.sql.UDTFRegistration.register — PySpark 4.0.1 documentation
UDTFRegistration.register(_name_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/udtf.html#UDTFRegistration.register)
[#](#pyspark.sql.UDTFRegistration.register "Permalink to this definition")

Register a Python user-defined table function as a SQL table function.

New in version 3.5.0.

Parameters

**name**str

The name of the user-defined table function in SQL statements.

**f**function or [`pyspark.sql.functions.udtf()`](about:blank/pyspark.sql.functions.udtf.html#pyspark.sql.functions.udtf "pyspark.sql.functions.udtf")

The user-defined table function.

Returns

function

The registered user-defined table function.

Notes

Spark uses the return type of the given user-defined table function as the return type of the registered user-defined function.

To register a nondeterministic Python table function, users need to first build a nondeterministic user-defined table function and then register it as a SQL function.

Examples

```
>>> from pyspark.sql.functions import udtf
>>> @udtf(returnType="c1: int, c2: int")
... class PlusOne:
...     def eval(self, x: int):
...         yield x, x + 1
...
>>> _ = spark.udtf.register(name="plus_one", f=PlusOne)
>>> spark.sql("SELECT * FROM plus_one(1)").collect()
[Row(c1=1, c2=2)]

```


Use it with lateral join

```
>>> spark.sql("SELECT * FROM VALUES (0, 1), (1, 2) t(x, y), LATERAL plus_one(x)").collect()
[Row(x=0, y=1, c1=0, c2=1), Row(x=1, y=2, c1=1, c2=2)]

```


