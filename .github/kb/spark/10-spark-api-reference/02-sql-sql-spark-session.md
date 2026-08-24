# Spark Session — PySpark 4.0.1 documentation
The entry point to programming Spark with the Dataset and DataFrame API. To create a Spark session, you should use `SparkSession.builder` attribute. See also [`SparkSession`](about:blank/api/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession").





* SparkSession.builder.appName(name): SparkSession.builder.config([key, value, ...])
  * Sets a name for the application, which will be shown in the Spark web UI.: Sets a config option.
* SparkSession.builder.appName(name): SparkSession.builder.enableHiveSupport()
  * Sets a name for the application, which will be shown in the Spark web UI.: Enables Hive support, including connectivity to a persistent Hive metastore, support for Hive SerDes, and Hive user-defined functions.
* SparkSession.builder.appName(name): SparkSession.builder.getOrCreate()
  * Sets a name for the application, which will be shown in the Spark web UI.: Gets an existing SparkSession or, if there is no existing one, creates a new one based on the options set in this builder.
* SparkSession.builder.appName(name): SparkSession.builder.master(master)
  * Sets a name for the application, which will be shown in the Spark web UI.: Sets the Spark master URL to connect to, such as "local" to run locally, "local[4]" to run locally with 4 cores, or "spark://master:7077" to run on a Spark standalone cluster.
* SparkSession.builder.appName(name): SparkSession.builder.remote(url)
  * Sets a name for the application, which will be shown in the Spark web UI.: Sets the Spark remote URL to connect to, such as "sc://host:port" to run it via Spark Connect server.




* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.addArtifacts(*path[, pyfile, ...])
  * Add artifact(s) to the client session.: Add artifact(s) to the client session.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.addTag(tag)
  * Add artifact(s) to the client session.: Add a tag to be assigned to all the operations started by this thread in this session.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.catalog
  * Add artifact(s) to the client session.: Interface through which the user may create, drop, alter or query underlying databases, tables, functions, etc.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.clearTags()
  * Add artifact(s) to the client session.: Clear the current thread's operation tags.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.conf
  * Add artifact(s) to the client session.: Runtime configuration interface for Spark.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.createDataFrame(data[, schema, ...])
  * Add artifact(s) to the client session.: Creates a DataFrame from an RDD, a list, a pandas.DataFrame, a numpy.ndarray, or a pyarrow.Table.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.dataSource
  * Add artifact(s) to the client session.: Returns a DataSourceRegistration for data source registration.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.getActiveSession()
  * Add artifact(s) to the client session.: Returns the active SparkSession for the current thread, returned by the builder
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.getTags()
  * Add artifact(s) to the client session.: Get the tags that are currently set to be assigned to all the operations started by this thread.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.interruptAll()
  * Add artifact(s) to the client session.: Interrupt all operations of this session currently running on the connected server.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.interruptOperation(op_id)
  * Add artifact(s) to the client session.: Interrupt an operation of this session with the given operationId.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.interruptTag(tag)
  * Add artifact(s) to the client session.: Interrupt all operations of this session with the given operation tag.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.newSession()
  * Add artifact(s) to the client session.: Returns a new SparkSession as new session, that has separate SQLConf, registered temporary views and UDFs, but shared SparkContext and table cache.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.profile
  * Add artifact(s) to the client session.: Returns a Profile for performance/memory profiling.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.removeTag(tag)
  * Add artifact(s) to the client session.: Remove a tag previously added to be assigned to all the operations started by this thread in this session.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.range(start[, end, step, ...])
  * Add artifact(s) to the client session.: Create a DataFrame with single pyspark.sql.types.LongType column named id, containing elements in a range from start to end (exclusive) with step value step.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.read
  * Add artifact(s) to the client session.: Returns a DataFrameReader that can be used to read data in as a DataFrame.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.readStream
  * Add artifact(s) to the client session.: Returns a DataStreamReader that can be used to read data streams as a streaming DataFrame.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.sparkContext
  * Add artifact(s) to the client session.: Returns the underlying SparkContext.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.sql(sqlQuery[, args])
  * Add artifact(s) to the client session.: Returns a DataFrame representing the result of the given query.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.stop()
  * Add artifact(s) to the client session.: Stop the underlying SparkContext.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.streams
  * Add artifact(s) to the client session.: Returns a StreamingQueryManager that allows managing all the StreamingQuery instances active on this context.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.table(tableName)
  * Add artifact(s) to the client session.: Returns the specified table as a DataFrame.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.tvf
  * Add artifact(s) to the client session.: Returns a tvf.TableValuedFunction that can be used to call a table-valued function (TVF).
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.udf
  * Add artifact(s) to the client session.: Returns a UDFRegistration for UDF registration.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.udtf
  * Add artifact(s) to the client session.: Returns a UDTFRegistration for UDTF registration.
* SparkSession.addArtifact(*path[, pyfile, ...]): SparkSession.version
  * Add artifact(s) to the client session.: The version of Spark on which this application is running.
* SparkSession.addArtifact(*path[, pyfile, ...]): is_remote()
  * Add artifact(s) to the client session.: Returns if the current running environment is for Spark Connect.


Spark Connect Only[#](#spark-connect-only "Permalink to this headline")
-----------------------------------------------------------------------





* SparkSession.clearProgressHandlers(): SparkSession.client
  * Clear all registered progress handlers.: Gives access to the Spark Connect client.
* SparkSession.clearProgressHandlers(): SparkSession.copyFromLocalToFs(local_path, ...)
  * Clear all registered progress handlers.: Copy file from local to cloud storage file system.
* SparkSession.clearProgressHandlers(): SparkSession.registerProgressHandler(handler)
  * Clear all registered progress handlers.: Register a progress handler to be called when a progress update is received from the server.
* SparkSession.clearProgressHandlers(): SparkSession.removeProgressHandler(handler)
  * Clear all registered progress handlers.: Remove a progress handler that was previously registered.


# pyspark.sql.SparkSession.active — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.active

_classmethod_ SparkSession.active()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.active)
[#](#pyspark.sql.SparkSession.active "Permalink to this definition")

Returns the active or default [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession") for the current thread, returned by the builder.

New in version 3.5.0.

Returns

[`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession")

Spark session if an active or default session exists for the current thread.

# pyspark.sql.SparkSession.builder.appName — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.builder.appName

builder.appName(_name_)
[#](#pyspark.sql.SparkSession.builder.appName "Permalink to this definition")

Sets a name for the application, which will be shown in the Spark web UI.

If no application name is set, a randomly generated name will be used.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

an application name

Returns

`SparkSession.Builder`

Examples

```
>>> SparkSession.builder.appName("My app")
<pyspark.sql.session.SparkSession.Builder...

```

# pyspark.sql.SparkSession.builder.config — PySpark 4.0.1 documentation
builder.config(_key\=None_, _value\=None_, _conf\=None_, _\*_, _map\=None_)
[#](#pyspark.sql.SparkSession.builder.config "Permalink to this definition")

Sets a config option. Options set using this method are automatically propagated to both `SparkConf` and `SparkSession`’s own configuration.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**key**str, optional

a key name string for configuration property

**value**str, optional

a value for configuration property

**conf**`SparkConf`, optional

an instance of `SparkConf`

**map: dictionary, optional**

a dictionary of configurations to set

New in version 3.4.0.

Returns

`SparkSession.Builder`

Examples

For an existing `SparkConf`, use conf parameter.

```
>>> from pyspark.conf import SparkConf
>>> conf = SparkConf().setAppName("example").setMaster("local")
>>> SparkSession.builder.config(conf=conf)
<pyspark.sql.session.SparkSession.Builder...

```


For a (key, value) pair, you can omit parameter names.

```
>>> SparkSession.builder.config("spark.some.config.option", "some-value")
<pyspark.sql.session.SparkSession.Builder...

```


Set multiple configurations.

```
>>> SparkSession.builder.config(
...     "spark.some.config.number", 123).config("spark.some.config.float", 0.123)
<pyspark.sql.session.SparkSession.Builder...

```


Set multiple configurations using a dictionary.

```
>>> SparkSession.builder.config(
...     map={"spark.some.config.number": 123, "spark.some.config.float": 0.123})
<pyspark.sql.session.SparkSession.Builder...

```


# pyspark.sql.SparkSession.builder.enableHiveSupport — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.builder.enableHiveSupport

builder.enableHiveSupport()
[#](#pyspark.sql.SparkSession.builder.enableHiveSupport "Permalink to this definition")

Enables Hive support, including connectivity to a persistent Hive metastore, support for Hive SerDes, and Hive user-defined functions.

New in version 2.0.0.

Returns

`SparkSession.Builder`

Examples

```
>>> SparkSession.builder.enableHiveSupport()
<pyspark.sql.session.SparkSession.Builder...

```

# pyspark.sql.SparkSession.builder.getOrCreate — PySpark 4.0.1 documentation
builder.getOrCreate()
[#](#pyspark.sql.SparkSession.builder.getOrCreate "Permalink to this definition")

Gets an existing `SparkSession` or, if there is no existing one, creates a new one based on the options set in this builder.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

`SparkSession`

Examples

This method first checks whether there is a valid global default SparkSession, and if yes, return that one. If no valid global default SparkSession exists, the method creates a new SparkSession and assigns the newly created SparkSession as the global default.

```
>>> s1 = SparkSession.builder.config("k1", "v1").getOrCreate()
>>> s1.conf.get("k1") == "v1"
True

```


The configuration of the SparkSession can be changed afterwards

```
>>> s1.conf.set("k1", "v1_new")
>>> s1.conf.get("k1") == "v1_new"
True

```


In case an existing SparkSession is returned, the config options specified in this builder will be applied to the existing SparkSession.

```
>>> s2 = SparkSession.builder.config("k2", "v2").getOrCreate()
>>> s1.conf.get("k1") == s2.conf.get("k1") == "v1_new"
True
>>> s1.conf.get("k2") == s2.conf.get("k2") == "v2"
True

```


# pyspark.sql.SparkSession.builder.master — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.builder.master

builder.master(_master_)
[#](#pyspark.sql.SparkSession.builder.master "Permalink to this definition")

Sets the Spark master URL to connect to, such as “local” to run locally, “local\[4\]” to run locally with 4 cores, or “spark://master:7077” to run on a Spark standalone cluster.

New in version 2.0.0.

Parameters

**master**str

a url for spark master

Returns

`SparkSession.Builder`

Examples

```
>>> SparkSession.builder.master("local")
<pyspark.sql.session.SparkSession.Builder...

```

# pyspark.sql.SparkSession.builder.remote — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.builder.remote

builder.remote(_url_)
[#](#pyspark.sql.SparkSession.builder.remote "Permalink to this definition")

Sets the Spark remote URL to connect to, such as “sc://host:port” to run it via Spark Connect server.

New in version 3.4.0.

Parameters

**url**str

URL to Spark Connect server

Returns

`SparkSession.Builder`

Examples

```
>>> SparkSession.builder.remote("sc://localhost")  
<pyspark.sql.session.SparkSession.Builder...

```


# pyspark.sql.SparkSession.addArtifact — PySpark 4.0.1 documentation
SparkSession.addArtifact(_\*path_, _pyfile\=False_, _archive\=False_, _file\=False_)
[#](#pyspark.sql.SparkSession.addArtifact "Permalink to this definition")

Add artifact(s) to the client session. Currently only local files are supported.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Parameters

**\*path**tuple of str

Artifact’s URIs to add.

**pyfile**bool

Whether to add them as Python dependencies such as .py, .egg, .zip or .jar files. The pyfiles are directly inserted into the path when executing Python functions in executors.

**archive**bool

Whether to add them as archives such as .zip, .jar, .tar.gz, .tgz, or .tar files. The archives are unpacked on the executor side automatically.

**file**bool

Add a file to be downloaded with this Spark job on every node. The `path` passed can only be a local file for now.


# pyspark.sql.SparkSession.addArtifacts — PySpark 4.0.1 documentation
SparkSession.addArtifacts(_\*path_, _pyfile\=False_, _archive\=False_, _file\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.addArtifacts)
[#](#pyspark.sql.SparkSession.addArtifacts "Permalink to this definition")

Add artifact(s) to the client session. Currently only local files are supported.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Parameters

**\*path**tuple of str

Artifact’s URIs to add.

**pyfile**bool

Whether to add them as Python dependencies such as .py, .egg, .zip or .jar files. The pyfiles are directly inserted into the path when executing Python functions in executors.

**archive**bool

Whether to add them as archives such as .zip, .jar, .tar.gz, .tgz, or .tar files. The archives are unpacked on the executor side automatically.

**file**bool

Add a file to be downloaded with this Spark job on every node. The `path` passed can only be a local file for now.

# pyspark.sql.SparkSession.addTag — PySpark 4.0.1 documentation
SparkSession.addTag(_tag_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.addTag)
[#](#pyspark.sql.SparkSession.addTag "Permalink to this definition")

Add a tag to be assigned to all the operations started by this thread in this session.

Often, a unit of execution in an application consists of multiple Spark executions. Application programmers can use this method to group all those jobs together and give a group tag. The application can use [`SparkSession.interruptTag()`](about:blank/pyspark.sql.SparkSession.interruptTag.html#pyspark.sql.SparkSession.interruptTag "pyspark.sql.SparkSession.interruptTag") to cancel all running executions with this tag.

There may be multiple tags present at the same time, so different parts of application may use different tags to perform cancellation at different levels of granularity.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Parameters

**tag**str

The tag to be added. Cannot contain ‘,’ (comma) character or be an empty string.

# pyspark.sql.SparkSession.catalog — PySpark 4.0.1 documentation
_property_ SparkSession.catalog[#](#pyspark.sql.SparkSession.catalog "Permalink to this definition")

Interface through which the user may create, drop, alter or query underlying databases, tables, functions, etc.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Catalog`](about:blank/pyspark.sql.Catalog.html#pyspark.sql.Catalog "pyspark.sql.Catalog")

Examples

```
>>> spark.catalog
<...Catalog object ...>

```


Create a temp view, show the list, and drop it.

```
>>> spark.range(1).createTempView("test_view")
>>> spark.catalog.listTables()  
[Table(name='test_view', catalog=None, namespace=[], description=None, ...
>>> _ = spark.catalog.dropTempView("test_view")

```

# pyspark.sql.SparkSession.clearTags — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.clearTags

SparkSession.clearTags()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.clearTags)
[#](#pyspark.sql.SparkSession.clearTags "Permalink to this definition")

Clear the current thread’s operation tags.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.


# pyspark.sql.SparkSession.conf — PySpark 4.0.1 documentation
_property_ SparkSession.conf[#](#pyspark.sql.SparkSession.conf "Permalink to this definition")

Runtime configuration interface for Spark.

This is the interface through which the user can get and set all Spark and Hadoop configurations that are relevant to Spark SQL. When getting the value of a config, this defaults to the value set in the underlying `SparkContext`, if any.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`pyspark.sql.conf.RuntimeConfig`](about:blank/pyspark.sql.conf.RuntimeConfig.html#pyspark.sql.conf.RuntimeConfig "pyspark.sql.conf.RuntimeConfig")

Examples

```
>>> spark.conf
<pyspark...RuntimeConf...>

```


Set a runtime configuration for the session

```
>>> spark.conf.set("key", "value")
>>> spark.conf.get("key")
'value'

```


# pyspark.sql.SparkSession.createDataFrame — PySpark 4.0.1 documentation
SparkSession.createDataFrame(_data_, _schema\=None_, _samplingRatio\=None_, _verifySchema\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.createDataFrame)
[#](#pyspark.sql.SparkSession.createDataFrame "Permalink to this definition")

Creates a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") from an `RDD`, a list, a `pandas.DataFrame`, a `numpy.ndarray`, or a `pyarrow.Table`.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Changed in version 4.0.0: Supports `pyarrow.Table`.

Parameters

**data**`RDD` or iterable

an RDD of any kind of SQL data representation ([`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row"), `tuple`, `int`, `boolean`, `dict`, etc.), or `list`, `pandas.DataFrame`, `numpy.ndarray`, or `pyarrow.Table`.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType"), str or list, optional

a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or a datatype string or a list of column names, default is None. The data type string format equals to [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>`.

When `schema` is a list of column names, the type of each column will be inferred from `data`.

When `schema` is `None`, it will try to infer the schema (column names and types) from `data`, which should be an RDD of either [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row"), `namedtuple`, or `dict`.

When `schema` is [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or a datatype string, it must match the real data, or an exception will be thrown at runtime. If the given schema is not [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType"), it will be wrapped into a [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") as its only field, and the field name will be “value”. Each record will also be wrapped into a tuple, which can be converted to row later.

**samplingRatio**float, optional

the sample ratio of rows used for inferring. The first few rows will be used if `samplingRatio` is `None`. This option is effective only when the input is `RDD`.

**verifySchema**bool, optional

verify data types of every row against schema. Enabled by default. When the input is `pyarrow.Table` or when the input class is `pandas.DataFrame` and spark.sql.execution.arrow.pyspark.enabled is enabled, this option is not effective. It follows Arrow type coercion. This option is not supported with Spark Connect.

New in version 2.1.0.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Notes

Usage with spark.sql.execution.arrow.pyspark.enabled=True is experimental.

Examples

Create a DataFrame from a list of tuples.

```
>>> spark.createDataFrame([('Alice', 1)]).show()
+-----+---+
|   _1| _2|
+-----+---+
|Alice|  1|
+-----+---+

```


Create a DataFrame from a list of dictionaries.

```
>>> d = [{'name': 'Alice', 'age': 1}]
>>> spark.createDataFrame(d).show()
+---+-----+
|age| name|
+---+-----+
|  1|Alice|
+---+-----+

```


Create a DataFrame with column names specified.

```
>>> spark.createDataFrame([('Alice', 1)], ['name', 'age']).show()
+-----+---+
| name|age|
+-----+---+
|Alice|  1|
+-----+---+

```


Create a DataFrame with the explicit schema specified.

```
>>> from pyspark.sql.types import *
>>> schema = StructType([
...    StructField("name", StringType(), True),
...    StructField("age", IntegerType(), True)])
>>> spark.createDataFrame([('Alice', 1)], schema).show()
+-----+---+
| name|age|
+-----+---+
|Alice|  1|
+-----+---+

```


Create a DataFrame with the schema in DDL formatted string.

```
>>> spark.createDataFrame([('Alice', 1)], "name: string, age: int").show()
+-----+---+
| name|age|
+-----+---+
|Alice|  1|
+-----+---+

```


Create an empty DataFrame. When initializing an empty DataFrame in PySpark, it’s mandatory to specify its schema, as the DataFrame lacks data from which the schema can be inferred.

```
>>> spark.createDataFrame([], "name: string, age: int").show()
+----+---+
|name|age|
+----+---+
+----+---+

```


Create a DataFrame from Row objects.

```
>>> from pyspark.sql import Row
>>> Person = Row('name', 'age')
>>> df = spark.createDataFrame([Person("Alice", 1)])
>>> df.show()
+-----+---+
| name|age|
+-----+---+
|Alice|  1|
+-----+---+

```


Create a DataFrame from a pandas DataFrame.

```
>>> spark.createDataFrame(df.toPandas()).show()  
+-----+---+
| name|age|
+-----+---+
|Alice|  1|
+-----+---+

```


```
>>> pdf = pandas.DataFrame([[1, 2]])  
>>> spark.createDataFrame(pdf).show()  
+---+---+
|  0|  1|
+---+---+
|  1|  2|
+---+---+

```


Create a DataFrame from a PyArrow Table.

```
>>> spark.createDataFrame(df.toArrow()).show()  
+-----+---+
| name|age|
+-----+---+
|Alice|  1|
+-----+---+

```


```
>>> table = pyarrow.table({'0': [1], '1': [2]})  
>>> spark.createDataFrame(table).show()  
+---+---+
|  0|  1|
+---+---+
|  1|  2|
+---+---+

```


# pyspark.sql.SparkSession.dataSource — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.dataSource

_property_ SparkSession.dataSource[#](#pyspark.sql.SparkSession.dataSource "Permalink to this definition")

Returns a `DataSourceRegistration` for data source registration.

New in version 4.0.0.

Returns

`DataSourceRegistration`

Notes

This feature is experimental and unstable.

# pyspark.sql.SparkSession.getActiveSession — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.getActiveSession

_classmethod_ SparkSession.getActiveSession()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.getActiveSession)
[#](#pyspark.sql.SparkSession.getActiveSession "Permalink to this definition")

Returns the active [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession") for the current thread, returned by the builder

New in version 3.0.0.

Changed in version 3.5.0: Supports Spark Connect.

Returns

[`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession")

Spark session if an active session exists for the current thread

Examples

```
>>> s = SparkSession.getActiveSession()
>>> df = s.createDataFrame([('Alice', 1)], ['name', 'age'])
>>> df.select("age").show()
+---+
|age|
+---+
|  1|
+---+

```


# pyspark.sql.SparkSession.getTags — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.getTags

SparkSession.getTags()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.getTags)
[#](#pyspark.sql.SparkSession.getTags "Permalink to this definition")

Get the tags that are currently set to be assigned to all the operations started by this thread.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Returns

set of str

Set of tags of interrupted operations.

# pyspark.sql.SparkSession.interruptAll — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.interruptAll

SparkSession.interruptAll()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.interruptAll)
[#](#pyspark.sql.SparkSession.interruptAll "Permalink to this definition")

Interrupt all operations of this session currently running on the connected server.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Returns

list of str

List of operationIds of interrupted operations.

Notes

There is still a possibility of operation finishing just as it is interrupted.

# pyspark.sql.SparkSession.interruptOperation — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.interruptOperation

SparkSession.interruptOperation(_op\_id_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.interruptOperation)
[#](#pyspark.sql.SparkSession.interruptOperation "Permalink to this definition")

Interrupt an operation of this session with the given operationId.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Returns

list of str

List of operationIds of interrupted operations.

Notes

There is still a possibility of operation finishing just as it is interrupted.

# pyspark.sql.SparkSession.interruptTag — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.interruptTag

SparkSession.interruptTag(_tag_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.interruptTag)
[#](#pyspark.sql.SparkSession.interruptTag "Permalink to this definition")

Interrupt all operations of this session with the given operation tag.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Returns

list of str

List of operationIds of interrupted operations.

Notes

There is still a possibility of operation finishing just as it is interrupted.

# pyspark.sql.SparkSession.newSession — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.newSession

SparkSession.newSession()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.newSession)
[#](#pyspark.sql.SparkSession.newSession "Permalink to this definition")

Returns a new [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession") as new session, that has separate SQLConf, registered temporary views and UDFs, but shared `SparkContext` and table cache.

New in version 2.0.0.

Returns

[`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession")

Spark session if an active session exists for the current thread

Examples

```
>>> spark.newSession()
<...SparkSession object ...>

```
# pyspark.sql.SparkSession.profile — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.profile

_property_ SparkSession.profile[#](#pyspark.sql.SparkSession.profile "Permalink to this definition")

Returns a `Profile` for performance/memory profiling.

New in version 4.0.0.

Returns

`Profile`

Notes

Supports Spark Connect.

# pyspark.sql.SparkSession.removeTag — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.removeTag

SparkSession.removeTag(_tag_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.removeTag)
[#](#pyspark.sql.SparkSession.removeTag "Permalink to this definition")

Remove a tag previously added to be assigned to all the operations started by this thread in this session. Noop if such a tag was not added earlier.

New in version 3.5.0.

Changed in version 4.0.0: Supports Spark Classic.

Parameters

**tag**list of str

The tag to be removed. Cannot contain ‘,’ (comma) character or be an empty string.

# pyspark.sql.SparkSession.range — PySpark 4.0.1 documentation
SparkSession.range(_start_, _end\=None_, _step\=1_, _numPartitions\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.range)
[#](#pyspark.sql.SparkSession.range "Permalink to this definition")

Create a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with single [`pyspark.sql.types.LongType`](about:blank/pyspark.sql.types.LongType.html#pyspark.sql.types.LongType "pyspark.sql.types.LongType") column named `id`, containing elements in a range from `start` to `end` (exclusive) with step value `step`.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**start**int

the start value

**end**int, optional

the end value (exclusive)

**step**int, optional

the incremental step (default: 1)

**numPartitions**int, optional

the number of partitions of the DataFrame

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Examples

```
>>> spark.range(1, 7, 2).show()
+---+
| id|
+---+
|  1|
|  3|
|  5|
+---+

```


If only one argument is specified, it will be used as the end value.

```
>>> spark.range(3).show()
+---+
| id|
+---+
|  0|
|  1|
|  2|
+---+

```


# pyspark.sql.SparkSession.read — PySpark 4.0.1 documentation
_property_ SparkSession.read[#](#pyspark.sql.SparkSession.read "Permalink to this definition")

Returns a [`DataFrameReader`](about:blank/pyspark.sql.DataFrameReader.html#pyspark.sql.DataFrameReader "pyspark.sql.DataFrameReader") that can be used to read data in as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrameReader`](about:blank/pyspark.sql.DataFrameReader.html#pyspark.sql.DataFrameReader "pyspark.sql.DataFrameReader")

Examples

```
>>> spark.read
<...DataFrameReader object ...>

```


Write a DataFrame into a JSON file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="read") as d:
...     # Write a DataFrame into a JSON file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.mode("overwrite").format("json").save(d)
...
...     # Read the JSON file as a DataFrame.
...     spark.read.format('json').load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```


# pyspark.sql.SparkSession.readStream — PySpark 4.0.1 documentation
_property_ SparkSession.readStream[#](#pyspark.sql.SparkSession.readStream "Permalink to this definition")

Returns a `DataStreamReader` that can be used to read data streams as a streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.0.0.

Changed in version 3.5.0: Supports Spark Connect.

Returns

`DataStreamReader`

Notes

This API is evolving.

Examples

```
>>> spark.readStream
<pyspark...DataStreamReader object ...>

```


The example below uses Rate source that generates rows continuously. After that, we operate a modulo by 3, and then write the stream out to the console. The streaming query stops in 3 seconds.

```
>>> import time
>>> df = spark.readStream.format("rate").load()
>>> df = df.selectExpr("value % 3 as v")
>>> q = df.writeStream.format("console").start()
>>> time.sleep(3)
>>> q.stop()

```


# pyspark.sql.SparkSession.sparkContext — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.sparkContext

_property_ SparkSession.sparkContext[#](#pyspark.sql.SparkSession.sparkContext "Permalink to this definition")

Returns the underlying `SparkContext`.

New in version 2.0.0.

Returns

`SparkContext`

Examples

```
>>> spark.sparkContext
<SparkContext master=... appName=...>

```


Create an RDD from the Spark context

```
>>> rdd = spark.sparkContext.parallelize([1, 2, 3])
>>> rdd.collect()
[1, 2, 3]

```

# pyspark.sql.SparkSession.sql — PySpark 4.0.1 documentation
SparkSession.sql(_sqlQuery_, _args\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.sql)
[#](#pyspark.sql.SparkSession.sql "Permalink to this definition")

Returns a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") representing the result of the given query. When `kwargs` is specified, this method formats the given string by using the Python standard formatter. The method binds named parameters to SQL literals or positional parameters from args. It doesn’t support named and positional parameters in the same SQL query.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect and parameterized SQL.

Changed in version 3.5.0: Added positional parameters.

Parameters

**sqlQuery**str

SQL query string.

**args**dict or list

A dictionary of parameter names to Python objects or a list of Python objects that can be converted to SQL literal expressions. See [Supported Data Types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html) for supported value types in Python. For example, dictionary keys: “rank”, “name”, “birthdate”; dictionary or list values: 1, “Steven”, datetime.date(2023, 4, 2). A value can be also a Column of a literal or collection constructor functions such as map(), array(), struct(), in that case it is taken as is.

New in version 3.4.0.

**kwargs**dict

Other variables that the user wants to set that can be referenced in the query

Changed in version 3.3.0: Added optional argument `kwargs` to specify the mapping of variables in the query. This feature is experimental and unstable.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Notes

In Spark Classic, a temporary view referenced in spark.sql is resolved immediately, while in Spark Connect it is lazily analyzed. So in Spark Connect if a view is dropped, modified or replaced after spark.sql, the execution may fail or generate different results.

Examples

Executing a SQL query.

```
>>> spark.sql("SELECT * FROM range(10) where id > 7").show()
+---+
| id|
+---+
|  8|
|  9|
+---+

```


Executing a SQL query with variables as Python formatter standard.

```
>>> spark.sql(
...     "SELECT * FROM range(10) WHERE id > {bound1} AND id < {bound2}", bound1=7, bound2=9
... ).show()
+---+
| id|
+---+
|  8|
+---+

```


```
>>> mydf = spark.range(10)
>>> spark.sql(
...     "SELECT {col} FROM {mydf} WHERE id IN {x}",
...     col=mydf.id, mydf=mydf, x=tuple(range(4))).show()
+---+
| id|
+---+
|  0|
|  1|
|  2|
|  3|
+---+

```


```
>>> spark.sql('''
...   SELECT m1.a, m2.b
...   FROM {table1} m1 INNER JOIN {table2} m2
...   ON m1.key = m2.key
...   ORDER BY m1.a, m2.b''',
...   table1=spark.createDataFrame([(1, "a"), (2, "b")], ["a", "key"]),
...   table2=spark.createDataFrame([(3, "a"), (4, "b"), (5, "b")], ["b", "key"])).show()
+---+---+
|  a|  b|
+---+---+
|  1|  3|
|  2|  4|
|  2|  5|
+---+---+

```


Also, it is possible to query using class:Column from [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

```
>>> mydf = spark.createDataFrame([(1, 4), (2, 4), (3, 6)], ["A", "B"])
>>> spark.sql("SELECT {df.A}, {df[B]} FROM {df}", df=mydf).show()
+---+---+
|  A|  B|
+---+---+
|  1|  4|
|  2|  4|
|  3|  6|
+---+---+

```


And substitute named parameters with the : prefix by SQL literals.

```
>>> from pyspark.sql.functions import create_map, lit
>>> spark.sql(
...   "SELECT *, element_at(:m, 'a') AS C FROM {df} WHERE {df[B]} > :minB",
...   {"minB" : 5, "m" : create_map(lit('a'), lit(1))}, df=mydf).show()
+---+---+---+
|  A|  B|  C|
+---+---+---+
|  3|  6|  1|
+---+---+---+

```


Or positional parameters marked by ? in the SQL query by SQL literals.

```
>>> from pyspark.sql.functions import array, lit
>>> spark.sql(
...   "SELECT *, element_at(?, 1) AS C FROM {df} WHERE {df[B]} > ? and ? < {df[A]}",
...   args=[array(lit(1), lit(2), lit(3)), 5, 2], df=mydf).show()
+---+---+---+
|  A|  B|  C|
+---+---+---+
|  3|  6|  1|
+---+---+---+

```



# pyspark.sql.SparkSession.stop — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.stop

SparkSession.stop()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.stop)
[#](#pyspark.sql.SparkSession.stop "Permalink to this definition")

Stop the underlying `SparkContext`.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

# pyspark.sql.SparkSession.streams — PySpark 4.0.1 documentation
_property_ SparkSession.streams[#](#pyspark.sql.SparkSession.streams "Permalink to this definition")

Returns a `StreamingQueryManager` that allows managing all the `StreamingQuery` instances active on this context.

New in version 2.0.0.

Changed in version 3.5.0: Supports Spark Connect.

Returns

`StreamingQueryManager`

Notes

This API is evolving.

Examples

```
>>> spark.streams
<pyspark...StreamingQueryManager object ...>

```


Get the list of active streaming queries

```
>>> sq = spark.readStream.format(
...     "rate").load().writeStream.format('memory').queryName('this_query').start()
>>> sqm = spark.streams
>>> [q.name for q in sqm.active]
['this_query']
>>> sq.stop()

```


# pyspark.sql.SparkSession.table — PySpark 4.0.1 documentation
SparkSession.table(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.table)
[#](#pyspark.sql.SparkSession.table "Permalink to this definition")

Returns the specified table as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**tableName**str

the table name to retrieve.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Notes

In Spark Classic, a temporary view referenced in spark.table is resolved immediately, while in Spark Connect it is lazily analyzed. So in Spark Connect if a view is dropped, modified or replaced after spark.table, the execution may fail or generate different results.

Examples

```
>>> spark.range(5).createOrReplaceTempView("table1")
>>> spark.table("table1").sort("id").show()
+---+
| id|
+---+
|  0|
|  1|
|  2|
|  3|
|  4|
+---+

```


# pyspark.sql.SparkSession.tvf — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.tvf

_property_ SparkSession.tvf[#](#pyspark.sql.SparkSession.tvf "Permalink to this definition")

Returns a [`tvf.TableValuedFunction`](about:blank/pyspark.sql.tvf.TableValuedFunction.html#pyspark.sql.tvf.TableValuedFunction "pyspark.sql.tvf.TableValuedFunction") that can be used to call a table-valued function (TVF).

New in version 4.0.0.

Returns

[`tvf.TableValuedFunction`](about:blank/pyspark.sql.tvf.TableValuedFunction.html#pyspark.sql.tvf.TableValuedFunction "pyspark.sql.tvf.TableValuedFunction")

Notes

This API is evolving.

Examples

```
>>> spark.tvf
<pyspark...TableValuedFunction object ...>

```


```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode(sf.array(sf.lit(1), sf.lit(2), sf.lit(3))).show()
+---+
|col|
+---+
|  1|
|  2|
|  3|
+---+

```


# pyspark.sql.SparkSession.udf — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.udf

_property_ SparkSession.udf[#](#pyspark.sql.SparkSession.udf "Permalink to this definition")

Returns a [`UDFRegistration`](about:blank/pyspark.sql.UDFRegistration.html#pyspark.sql.UDFRegistration "pyspark.sql.UDFRegistration") for UDF registration.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`UDFRegistration`](about:blank/pyspark.sql.UDFRegistration.html#pyspark.sql.UDFRegistration "pyspark.sql.UDFRegistration")

Examples

Register a Python UDF, and use it in SQL.

```
>>> strlen = spark.udf.register("strlen", lambda x: len(x))
>>> spark.sql("SELECT strlen('test')").show()
+------------+
|strlen(test)|
+------------+
|           4|
+------------+

```

# pyspark.sql.SparkSession.udtf — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.udtf

_property_ SparkSession.udtf[#](#pyspark.sql.SparkSession.udtf "Permalink to this definition")

Returns a [`UDTFRegistration`](about:blank/pyspark.sql.UDTFRegistration.html#pyspark.sql.UDTFRegistration "pyspark.sql.UDTFRegistration") for UDTF registration.

New in version 3.5.0.

Returns

[`UDTFRegistration`](about:blank/pyspark.sql.UDTFRegistration.html#pyspark.sql.UDTFRegistration "pyspark.sql.UDTFRegistration")

Notes

Supports Spark Connect.


# pyspark.sql.SparkSession.version — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.version

_property_ SparkSession.version[#](#pyspark.sql.SparkSession.version "Permalink to this definition")

The version of Spark on which this application is running.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

str

the version of Spark in string.

Examples

# pyspark.sql.is_remote — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.is\_remote

pyspark.sql.is\_remote()
[\[source\]](about:blank/_modules/pyspark/sql/utils.html#is_remote)
[#](#pyspark.sql.is_remote "Permalink to this definition")

Returns if the current running environment is for Spark Connect.

New in version 4.0.0.

Returns

bool

Notes

This will only return `True` if there is a remote session running. Otherwise, it returns `False`.

This API is unstable, and for developers.

Examples

```
>>> from pyspark.sql import is_remote
>>> is_remote()
False

```

# pyspark.sql.SparkSession.builder.create — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.builder.create

builder.create()
[#](#pyspark.sql.SparkSession.builder.create "Permalink to this definition")

Creates a new SparkSession. Can only be used in the context of Spark Connect and will throw an exception otherwise.

New in version 3.5.0.

Returns

`SparkSession`

Notes

This method will update the default and/or active session if they are not set.


# pyspark.sql.SparkSession.clearProgressHandlers — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.clearProgressHandlers

SparkSession.clearProgressHandlers()
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.clearProgressHandlers)
[#](#pyspark.sql.SparkSession.clearProgressHandlers "Permalink to this definition")

Clear all registered progress handlers.

New in version 4.0.

# pyspark.sql.SparkSession.client — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.client

_property_ SparkSession.client[#](#pyspark.sql.SparkSession.client "Permalink to this definition")

Gives access to the Spark Connect client. In normal cases this is not necessary to be used and only relevant for testing.

New in version 3.4.0.

Returns

`SparkConnectClient`

Notes

This API is unstable, and a developer API. It returns non-API instance `SparkConnectClient`. This is an API dedicated to Spark Connect client only. With regular Spark Session, it throws an exception.

[Show Source](../../../_sources/reference/pyspark.sql/api/pyspark.sql.SparkSession.client.rst.txt)


# pyspark.sql.SparkSession.copyFromLocalToFs — PySpark 4.0.1 documentation
SparkSession.copyFromLocalToFs(_local\_path_, _dest\_path_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.copyFromLocalToFs)
[#](#pyspark.sql.SparkSession.copyFromLocalToFs "Permalink to this definition")

Copy file from local to cloud storage file system. If the file already exits in destination path, old file is overwritten.

New in version 3.5.0.

Parameters

**local\_path: str**

Path to a local file. Directories are not supported. The path can be either an absolute path or a relative path.

**dest\_path: str**

The cloud storage path to the destination the file will be copied to. The path must be an an absolute path.

Notes

This API is a developer API. Also, this is an API dedicated to Spark Connect client only. With regular Spark Session, it throws an exception.

# pyspark.sql.SparkSession.registerProgressHandler — PySpark 4.0.1 documentation
SparkSession.registerProgressHandler(_handler_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.registerProgressHandler)
[#](#pyspark.sql.SparkSession.registerProgressHandler "Permalink to this definition")

Register a progress handler to be called when a progress update is received from the server.

New in version 4.0.

Parameters

**handler**ProgressHandler

A callable that follows the ProgressHandler interface. This handler will be called on every progress update.

Examples

```
>>> def progress_handler(stages, inflight_tasks, done):
...     print(f"{len(stages)} Stages known, Done: {done}")
>>> spark.registerProgressHandler(progress_handler)
>>> res = spark.range(10).repartition(1).collect()  
3 Stages known, Done: False
3 Stages known, Done: True
>>> spark.clearProgressHandlers()

```


# pyspark.sql.SparkSession.removeProgressHandler — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Spark Session](../spark_session.html)
*   pyspark.sql.SparkSession.removeProgressHandler

SparkSession.removeProgressHandler(_handler_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession.removeProgressHandler)
[#](#pyspark.sql.SparkSession.removeProgressHandler "Permalink to this definition")

Remove a progress handler that was previously registered.

New in version 4.0.

Parameters

**handler**ProgressHandler

The handler to remove if present in the list of progress handlers.

