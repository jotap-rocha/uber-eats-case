# Core Classes — PySpark 4.0.1 documentation
[`SparkSession`](about:blank/api/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession")(sparkContext\[, jsparkSession, ...\])

The entry point to programming Spark with the Dataset and DataFrame API.

[`Catalog`](about:blank/api/pyspark.sql.Catalog.html#pyspark.sql.Catalog "pyspark.sql.Catalog")(sparkSession)

User-facing catalog API, accessible through SparkSession.catalog.

[`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")(jdf, sql\_ctx)

A distributed collection of data grouped into named columns.

[`Column`](about:blank/api/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")(\*args, \*\*kwargs)

A column in a DataFrame.

[`Observation`](about:blank/api/pyspark.sql.Observation.html#pyspark.sql.Observation "pyspark.sql.Observation")(\*args, \*\*kwargs)

Class to observe (named) metrics on a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`Row`](about:blank/api/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row")(\*args, \*\*kwargs)

A row in [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`GroupedData`](about:blank/api/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData")(jgd, df)

A set of methods for aggregations on a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), created by [`DataFrame.groupBy()`](about:blank/api/pyspark.sql.DataFrame.groupBy.html#pyspark.sql.DataFrame.groupBy "pyspark.sql.DataFrame.groupBy").

[`PandasCogroupedOps`](about:blank/api/pyspark.sql.PandasCogroupedOps.html#pyspark.sql.PandasCogroupedOps "pyspark.sql.PandasCogroupedOps")(gd1, gd2)

A logical grouping of two [`GroupedData`](about:blank/api/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData"), created by [`GroupedData.cogroup()`](about:blank/api/pyspark.sql.GroupedData.cogroup.html#pyspark.sql.GroupedData.cogroup "pyspark.sql.GroupedData.cogroup").

[`DataFrameNaFunctions`](about:blank/api/pyspark.sql.DataFrameNaFunctions.html#pyspark.sql.DataFrameNaFunctions "pyspark.sql.DataFrameNaFunctions")(df)

Functionality for working with missing data in [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameStatFunctions`](about:blank/api/pyspark.sql.DataFrameStatFunctions.html#pyspark.sql.DataFrameStatFunctions "pyspark.sql.DataFrameStatFunctions")(df)

Functionality for statistic functions with [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`Window`](about:blank/api/pyspark.sql.Window.html#pyspark.sql.Window "pyspark.sql.Window")()

Utility functions for defining window in DataFrames.

[`DataFrameReader`](about:blank/api/pyspark.sql.DataFrameReader.html#pyspark.sql.DataFrameReader "pyspark.sql.DataFrameReader")(spark)

Interface used to load a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") from external storage systems (e.g.

[`DataFrameWriter`](about:blank/api/pyspark.sql.DataFrameWriter.html#pyspark.sql.DataFrameWriter "pyspark.sql.DataFrameWriter")(df)

Interface used to write a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to external storage systems (e.g.

[`DataFrameWriterV2`](about:blank/api/pyspark.sql.DataFrameWriterV2.html#pyspark.sql.DataFrameWriterV2 "pyspark.sql.DataFrameWriterV2")(df, table)

Interface used to write a class:pyspark.sql.dataframe.DataFrame to external storage using the v2 API.

[`UDFRegistration`](about:blank/api/pyspark.sql.UDFRegistration.html#pyspark.sql.UDFRegistration "pyspark.sql.UDFRegistration")(sparkSession)

Wrapper for user-defined function registration.

[`UDTFRegistration`](about:blank/api/pyspark.sql.UDTFRegistration.html#pyspark.sql.UDTFRegistration "pyspark.sql.UDTFRegistration")(sparkSession)

Wrapper for user-defined table function registration.

[`udf.UserDefinedFunction`](about:blank/api/pyspark.sql.udf.UserDefinedFunction.html#pyspark.sql.udf.UserDefinedFunction "pyspark.sql.udf.UserDefinedFunction")(func\[, returnType, ...\])

User defined function in Python

[`udtf.UserDefinedTableFunction`](about:blank/api/pyspark.sql.udtf.UserDefinedTableFunction.html#pyspark.sql.udtf.UserDefinedTableFunction "pyspark.sql.udtf.UserDefinedTableFunction")(func, returnType)

User-defined table function in Python

[`datasource.DataSource`](about:blank/api/pyspark.sql.datasource.DataSource.html#pyspark.sql.datasource.DataSource "pyspark.sql.datasource.DataSource")(options)

A base class for data sources.

[`datasource.DataSourceReader`](about:blank/api/pyspark.sql.datasource.DataSourceReader.html#pyspark.sql.datasource.DataSourceReader "pyspark.sql.datasource.DataSourceReader")()

A base class for data source readers.

[`datasource.DataSourceStreamReader`](about:blank/api/pyspark.sql.datasource.DataSourceStreamReader.html#pyspark.sql.datasource.DataSourceStreamReader "pyspark.sql.datasource.DataSourceStreamReader")()

A base class for streaming data source readers.

[`datasource.DataSourceWriter`](about:blank/api/pyspark.sql.datasource.DataSourceWriter.html#pyspark.sql.datasource.DataSourceWriter "pyspark.sql.datasource.DataSourceWriter")()

A base class for data source writers.

[`datasource.DataSourceRegistration`](about:blank/api/pyspark.sql.datasource.DataSourceRegistration.html#pyspark.sql.datasource.DataSourceRegistration "pyspark.sql.datasource.DataSourceRegistration")(sparkSession)

Wrapper for data source registration.

[`datasource.InputPartition`](about:blank/api/pyspark.sql.datasource.InputPartition.html#pyspark.sql.datasource.InputPartition "pyspark.sql.datasource.InputPartition")(value)

A base class representing an input partition returned by the partitions() method of `DataSourceReader`.

[`datasource.WriterCommitMessage`](about:blank/api/pyspark.sql.datasource.WriterCommitMessage.html#pyspark.sql.datasource.WriterCommitMessage "pyspark.sql.datasource.WriterCommitMessage")()

A commit message returned by the `DataSourceWriter.write()` and will be sent back to the driver side as input parameter of `DataSourceWriter.commit()` or `DataSourceWriter.abort()` method.

[`tvf.TableValuedFunction`](about:blank/api/pyspark.sql.tvf.TableValuedFunction.html#pyspark.sql.tvf.TableValuedFunction "pyspark.sql.tvf.TableValuedFunction")(sparkSession)

Interface for invoking table-valued functions in Spark SQL.

[`VariantVal`](about:blank/api/pyspark.sql.VariantVal.html#pyspark.sql.VariantVal "pyspark.sql.VariantVal")(value, metadata)

A class to represent a Variant value in Python.

[`table_arg.TableArg`](about:blank/api/pyspark.sql.table_arg.TableArg.html#pyspark.sql.table_arg.TableArg "pyspark.sql.table_arg.TableArg")()

Represents a table argument in PySpark.

# pyspark.sql.SparkSession — PySpark 4.0.1 documentation
_class_ pyspark.sql.SparkSession(_sparkContext_, _jsparkSession\=None_, _options\={}_)
[\[source\]](about:blank/_modules/pyspark/sql/session.html#SparkSession)
[#](#pyspark.sql.SparkSession "Permalink to this definition")

The entry point to programming Spark with the Dataset and DataFrame API.

A SparkSession can be used to create [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), register [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as tables, execute SQL over tables, cache tables, and read parquet files. To create a [`SparkSession`](#pyspark.sql.SparkSession "pyspark.sql.SparkSession"), use the following builder pattern:

Changed in version 3.4.0: Supports Spark Connect.

builder[#](#pyspark.sql.SparkSession.builder "Permalink to this definition")

Creates a `Builder` for constructing a [`SparkSession`](#pyspark.sql.SparkSession "pyspark.sql.SparkSession").

Changed in version 3.4.0: Supports Spark Connect.

Examples

Create a Spark session.

```
>>> spark = (
...     SparkSession.builder
...         .master("local")
...         .appName("Word Count")
...         .config("spark.some.config.option", "some-value")
...         .getOrCreate()
... )

```


Create a Spark session with Spark Connect.

```
>>> spark = (
...     SparkSession.builder
...         .remote("sc://localhost")
...         .appName("Word Count")
...         .config("spark.some.config.option", "some-value")
...         .getOrCreate()
... )  

```


Methods



* active(): addArtifact(*path[, pyfile, archive, file])
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Add artifact(s) to the client session.
* active(): addArtifacts(*path[, pyfile, archive, file])
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Add artifact(s) to the client session.
* active(): addTag(tag)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Add a tag to be assigned to all the operations started by this thread in this session.
* active(): clearProgressHandlers()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Clear all registered progress handlers.
* active(): clearTags()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Clear the current thread's operation tags.
* active(): copyFromLocalToFs(local_path, dest_path)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Copy file from local to cloud storage file system.
* active(): createDataFrame(data[, schema, ...])
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Creates a DataFrame from an RDD, a list, a pandas.DataFrame, a numpy.ndarray, or a pyarrow.Table.
* active(): getActiveSession()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Returns the active SparkSession for the current thread, returned by the builder
* active(): getTags()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Get the tags that are currently set to be assigned to all the operations started by this thread.
* active(): interruptAll()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Interrupt all operations of this session currently running on the connected server.
* active(): interruptOperation(op_id)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Interrupt an operation of this session with the given operationId.
* active(): interruptTag(tag)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Interrupt all operations of this session with the given operation tag.
* active(): newSession()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Returns a new SparkSession as new session, that has separate SQLConf, registered temporary views and UDFs, but shared SparkContext and table cache.
* active(): range(start[, end, step, numPartitions])
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Create a DataFrame with single pyspark.sql.types.LongType column named id, containing elements in a range from start to end (exclusive) with step value step.
* active(): registerProgressHandler(handler)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Register a progress handler to be called when a progress update is received from the server.
* active(): removeProgressHandler(handler)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Remove a progress handler that was previously registered.
* active(): removeTag(tag)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Remove a tag previously added to be assigned to all the operations started by this thread in this session.
* active(): sql(sqlQuery[, args])
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Returns a DataFrame representing the result of the given query.
* active(): stop()
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Stop the underlying SparkContext.
* active(): table(tableName)
  * Returns the active or default SparkSession for the current thread, returned by the builder.: Returns the specified table as a DataFrame.


Attributes



* builder: catalog
  * Creates a Builder for constructing a SparkSession.: Interface through which the user may create, drop, alter or query underlying databases, tables, functions, etc.
* builder: client
  * Creates a Builder for constructing a SparkSession.: Gives access to the Spark Connect client.
* builder: conf
  * Creates a Builder for constructing a SparkSession.: Runtime configuration interface for Spark.
* builder: dataSource
  * Creates a Builder for constructing a SparkSession.: Returns a DataSourceRegistration for data source registration.
* builder: profile
  * Creates a Builder for constructing a SparkSession.: Returns a Profile for performance/memory profiling.
* builder: read
  * Creates a Builder for constructing a SparkSession.: Returns a DataFrameReader that can be used to read data in as a DataFrame.
* builder: readStream
  * Creates a Builder for constructing a SparkSession.: Returns a DataStreamReader that can be used to read data streams as a streaming DataFrame.
* builder: sparkContext
  * Creates a Builder for constructing a SparkSession.: Returns the underlying SparkContext.
* builder: streams
  * Creates a Builder for constructing a SparkSession.: Returns a StreamingQueryManager that allows managing all the StreamingQuery instances active on this context.
* builder: tvf
  * Creates a Builder for constructing a SparkSession.: Returns a tvf.TableValuedFunction that can be used to call a table-valued function (TVF).
* builder: udf
  * Creates a Builder for constructing a SparkSession.: Returns a UDFRegistration for UDF registration.
* builder: udtf
  * Creates a Builder for constructing a SparkSession.: Returns a UDTFRegistration for UDTF registration.
* builder: version
  * Creates a Builder for constructing a SparkSession.: The version of Spark on which this application is running.


# pyspark.sql.Catalog — PySpark 4.0.1 documentation
[`cacheTable`](about:blank/pyspark.sql.Catalog.cacheTable.html#pyspark.sql.Catalog.cacheTable "pyspark.sql.Catalog.cacheTable")(tableName\[, storageLevel\])

Caches the specified table in-memory or with given storage level.

[`clearCache`](about:blank/pyspark.sql.Catalog.clearCache.html#pyspark.sql.Catalog.clearCache "pyspark.sql.Catalog.clearCache")()

Removes all cached tables from the in-memory cache.

[`createExternalTable`](about:blank/pyspark.sql.Catalog.createExternalTable.html#pyspark.sql.Catalog.createExternalTable "pyspark.sql.Catalog.createExternalTable")(tableName\[, path, ...\])

Creates a table based on the dataset in a data source.

[`createTable`](about:blank/pyspark.sql.Catalog.createTable.html#pyspark.sql.Catalog.createTable "pyspark.sql.Catalog.createTable")(tableName\[, path, source, ...\])

Creates a table based on the dataset in a data source.

[`currentCatalog`](about:blank/pyspark.sql.Catalog.currentCatalog.html#pyspark.sql.Catalog.currentCatalog "pyspark.sql.Catalog.currentCatalog")()

Returns the current default catalog in this session.

[`currentDatabase`](about:blank/pyspark.sql.Catalog.currentDatabase.html#pyspark.sql.Catalog.currentDatabase "pyspark.sql.Catalog.currentDatabase")()

Returns the current default database in this session.

[`databaseExists`](about:blank/pyspark.sql.Catalog.databaseExists.html#pyspark.sql.Catalog.databaseExists "pyspark.sql.Catalog.databaseExists")(dbName)

Check if the database with the specified name exists.

[`dropGlobalTempView`](about:blank/pyspark.sql.Catalog.dropGlobalTempView.html#pyspark.sql.Catalog.dropGlobalTempView "pyspark.sql.Catalog.dropGlobalTempView")(viewName)

Drops the global temporary view with the given view name in the catalog.

[`dropTempView`](about:blank/pyspark.sql.Catalog.dropTempView.html#pyspark.sql.Catalog.dropTempView "pyspark.sql.Catalog.dropTempView")(viewName)

Drops the local temporary view with the given view name in the catalog.

[`functionExists`](about:blank/pyspark.sql.Catalog.functionExists.html#pyspark.sql.Catalog.functionExists "pyspark.sql.Catalog.functionExists")(functionName\[, dbName\])

Check if the function with the specified name exists.

[`getDatabase`](about:blank/pyspark.sql.Catalog.getDatabase.html#pyspark.sql.Catalog.getDatabase "pyspark.sql.Catalog.getDatabase")(dbName)

Get the database with the specified name.

[`getFunction`](about:blank/pyspark.sql.Catalog.getFunction.html#pyspark.sql.Catalog.getFunction "pyspark.sql.Catalog.getFunction")(functionName)

Get the function with the specified name.

[`getTable`](about:blank/pyspark.sql.Catalog.getTable.html#pyspark.sql.Catalog.getTable "pyspark.sql.Catalog.getTable")(tableName)

Get the table or view with the specified name.

[`isCached`](about:blank/pyspark.sql.Catalog.isCached.html#pyspark.sql.Catalog.isCached "pyspark.sql.Catalog.isCached")(tableName)

Returns true if the table is currently cached in-memory.

[`listCatalogs`](about:blank/pyspark.sql.Catalog.listCatalogs.html#pyspark.sql.Catalog.listCatalogs "pyspark.sql.Catalog.listCatalogs")(\[pattern\])

Returns a list of catalogs in this session.

[`listColumns`](about:blank/pyspark.sql.Catalog.listColumns.html#pyspark.sql.Catalog.listColumns "pyspark.sql.Catalog.listColumns")(tableName\[, dbName\])

Returns a list of columns for the given table/view in the specified database.

[`listDatabases`](about:blank/pyspark.sql.Catalog.listDatabases.html#pyspark.sql.Catalog.listDatabases "pyspark.sql.Catalog.listDatabases")(\[pattern\])

Returns a list of databases available across all sessions.

[`listFunctions`](about:blank/pyspark.sql.Catalog.listFunctions.html#pyspark.sql.Catalog.listFunctions "pyspark.sql.Catalog.listFunctions")(\[dbName, pattern\])

Returns a list of functions registered in the specified database.

[`listTables`](about:blank/pyspark.sql.Catalog.listTables.html#pyspark.sql.Catalog.listTables "pyspark.sql.Catalog.listTables")(\[dbName, pattern\])

Returns a list of tables/views in the specified database.

[`recoverPartitions`](about:blank/pyspark.sql.Catalog.recoverPartitions.html#pyspark.sql.Catalog.recoverPartitions "pyspark.sql.Catalog.recoverPartitions")(tableName)

Recovers all the partitions of the given table and updates the catalog.

[`refreshByPath`](about:blank/pyspark.sql.Catalog.refreshByPath.html#pyspark.sql.Catalog.refreshByPath "pyspark.sql.Catalog.refreshByPath")(path)

Invalidates and refreshes all the cached data (and the associated metadata) for any DataFrame that contains the given data source path.

[`refreshTable`](about:blank/pyspark.sql.Catalog.refreshTable.html#pyspark.sql.Catalog.refreshTable "pyspark.sql.Catalog.refreshTable")(tableName)

Invalidates and refreshes all the cached data and metadata of the given table.

[`registerFunction`](about:blank/pyspark.sql.Catalog.registerFunction.html#pyspark.sql.Catalog.registerFunction "pyspark.sql.Catalog.registerFunction")(name, f\[, returnType\])

An alias for `spark.udf.register()`.

[`setCurrentCatalog`](about:blank/pyspark.sql.Catalog.setCurrentCatalog.html#pyspark.sql.Catalog.setCurrentCatalog "pyspark.sql.Catalog.setCurrentCatalog")(catalogName)

Sets the current default catalog in this session.

[`setCurrentDatabase`](about:blank/pyspark.sql.Catalog.setCurrentDatabase.html#pyspark.sql.Catalog.setCurrentDatabase "pyspark.sql.Catalog.setCurrentDatabase")(dbName)

Sets the current default database in this session.

[`tableExists`](about:blank/pyspark.sql.Catalog.tableExists.html#pyspark.sql.Catalog.tableExists "pyspark.sql.Catalog.tableExists")(tableName\[, dbName\])

Check if the table or view with the specified name exists.

[`uncacheTable`](about:blank/pyspark.sql.Catalog.uncacheTable.html#pyspark.sql.Catalog.uncacheTable "pyspark.sql.Catalog.uncacheTable")(tableName)

Removes the specified table from the in-memory cache.

# pyspark.sql.DataFrame — PySpark 4.0.1 documentation
A distributed collection of data grouped into named columns.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Notes

A DataFrame should only be created as described above. It should not be directly created via using the constructor.

Examples

A [`DataFrame`](#pyspark.sql.DataFrame "pyspark.sql.DataFrame") is equivalent to a relational table in Spark SQL, and can be created using various functions in [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession"):

```
>>> people = spark.createDataFrame([
...     {"deptId": 1, "age": 40, "name": "Hyukjin Kwon", "gender": "M", "salary": 50},
...     {"deptId": 1, "age": 50, "name": "Takuya Ueshin", "gender": "M", "salary": 100},
...     {"deptId": 2, "age": 60, "name": "Xinrong Meng", "gender": "F", "salary": 150},
...     {"deptId": 3, "age": 20, "name": "Haejoon Lee", "gender": "M", "salary": 200}
... ])

```


Once created, it can be manipulated using the various domain-specific-language (DSL) functions defined in: [`DataFrame`](#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

To select a column from the [`DataFrame`](#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), use the apply method:

A more concrete example:

```
>>> # To create DataFrame using SparkSession
... department = spark.createDataFrame([
...     {"id": 1, "name": "PySpark"},
...     {"id": 2, "name": "ML"},
...     {"id": 3, "name": "Spark SQL"}
... ])

```


```
>>> people.filter(people.age > 30).join(
...     department, people.deptId == department.id).groupBy(
...     department.name, "gender").agg(
...         {"salary": "avg", "age": "max"}).sort("max(age)").show()
+-------+------+-----------+--------+
|   name|gender|avg(salary)|max(age)|
+-------+------+-----------+--------+
|PySpark|     M|       75.0|      50|
|     ML|     F|      150.0|      60|
+-------+------+-----------+--------+

```


Methods



* agg(*exprs): alias(alias)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame with an alias set.
* agg(*exprs): approxQuantile(col, probabilities, relativeError)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Calculates the approximate quantiles of numerical columns of a DataFrame.
* agg(*exprs): asTable()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Converts the DataFrame into a table_arg.TableArg object, which can be used as a table argument in a TVF(Table-Valued Function) including UDTF (User-Defined Table Function).
* agg(*exprs): cache()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Persists the DataFrame with the default storage level (MEMORY_AND_DISK_DESER).
* agg(*exprs): checkpoint([eager])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a checkpointed version of this DataFrame.
* agg(*exprs): coalesce(numPartitions)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame that has exactly numPartitions partitions.
* agg(*exprs): colRegex(colName)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Selects column based on the column name specified as a regex and returns it as Column.
* agg(*exprs): collect()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns all the records in the DataFrame as a list of Row.
* agg(*exprs): corr(col1, col2[, method])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Calculates the correlation of two columns of a DataFrame as a double value.
* agg(*exprs): count()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the number of rows in this DataFrame.
* agg(*exprs): cov(col1, col2)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Calculate the sample covariance for the given columns, specified by their names, as a double value.
* agg(*exprs): createGlobalTempView(name)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Creates a global temporary view with this DataFrame.
* agg(*exprs): createOrReplaceGlobalTempView(name)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Creates or replaces a global temporary view using the given name.
* agg(*exprs): createOrReplaceTempView(name)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Creates or replaces a local temporary view with this DataFrame.
* agg(*exprs): createTempView(name)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Creates a local temporary view with this DataFrame.
* agg(*exprs): crossJoin(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the cartesian product with another DataFrame.
* agg(*exprs): crosstab(col1, col2)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Computes a pair-wise frequency table of the given columns.
* agg(*exprs): cube(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Create a multi-dimensional cube for the current DataFrame using the specified columns, allowing aggregations to be performed on them.
* agg(*exprs): describe(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Computes basic statistics for numeric and string columns.
* agg(*exprs): distinct()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame containing the distinct rows in this DataFrame.
* agg(*exprs): drop(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame without specified columns.
* agg(*exprs): dropDuplicates([subset])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame with duplicate rows removed, optionally only considering certain columns.
* agg(*exprs): dropDuplicatesWithinWatermark([subset])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame with duplicate rows removed,
* agg(*exprs): drop_duplicates([subset])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: drop_duplicates() is an alias for dropDuplicates().
* agg(*exprs): dropna([how, thresh, subset])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame omitting rows with null or NaN values.
* agg(*exprs): exceptAll(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame containing rows in this DataFrame but not in another DataFrame while preserving duplicates.
* agg(*exprs): exists()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a Column object for an EXISTS Subquery.
* agg(*exprs): explain([extended, mode])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Prints the (logical and physical) plans to the console for debugging purposes.
* agg(*exprs): fillna(value[, subset])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame which null values are filled with new value.
* agg(*exprs): filter(condition)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Filters rows using the given condition.
* agg(*exprs): first()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the first row as a Row.
* agg(*exprs): foreach(f)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Applies the f function to all Row of this DataFrame.
* agg(*exprs): foreachPartition(f)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Applies the f function to each partition of this DataFrame.
* agg(*exprs): freqItems(cols[, support])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Finding frequent items for columns, possibly with false positives.
* agg(*exprs): groupBy(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Groups the DataFrame by the specified columns so that aggregation can be performed on them.
* agg(*exprs): groupby(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: groupby() is an alias for groupBy().
* agg(*exprs): groupingSets(groupingSets, *cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Create multi-dimensional aggregation for the current DataFrame using the specified grouping sets, so we can run aggregation on them.
* agg(*exprs): head([n])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the first n rows.
* agg(*exprs): hint(name, *parameters)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Specifies some hint on the current DataFrame.
* agg(*exprs): inputFiles()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a best-effort snapshot of the files that compose this DataFrame.
* agg(*exprs): intersect(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame containing rows only in both this DataFrame and another DataFrame.
* agg(*exprs): intersectAll(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame containing rows in both this DataFrame and another DataFrame while preserving duplicates.
* agg(*exprs): isEmpty()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Checks if the DataFrame is empty and returns a boolean value.
* agg(*exprs): isLocal()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns True if the collect() and take() methods can be run locally (without any Spark executors).
* agg(*exprs): join(other[, on, how])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Joins with another DataFrame, using the given join expression.
* agg(*exprs): lateralJoin(other[, on, how])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Lateral joins with another DataFrame, using the given join expression.
* agg(*exprs): limit(num)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Limits the result count to the number specified.
* agg(*exprs): localCheckpoint([eager, storageLevel])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a locally checkpointed version of this DataFrame.
* agg(*exprs): mapInArrow(func, schema[, barrier, profile])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Maps an iterator of batches in the current DataFrame using a Python native function that is performed on pyarrow.RecordBatchs both as input and output, and returns the result as a DataFrame.
* agg(*exprs): mapInPandas(func, schema[, barrier, profile])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Maps an iterator of batches in the current DataFrame using a Python native function that is performed on pandas DataFrames both as input and output, and returns the result as a DataFrame.
* agg(*exprs): melt(ids, values, variableColumnName, ...)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
* agg(*exprs): mergeInto(table, condition)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Merges a set of updates, insertions, and deletions based on a source table into a target table.
* agg(*exprs): metadataColumn(colName)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Selects a metadata column based on its logical column name and returns it as a Column.
* agg(*exprs): observe(observation, *exprs)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Define (named) metrics to observe on the DataFrame.
* agg(*exprs): offset(num)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new :class: DataFrame by skipping the first n rows.
* agg(*exprs): orderBy(*cols, **kwargs)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame sorted by the specified column(s).
* agg(*exprs): pandas_api([index_col])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Converts the existing DataFrame into a pandas-on-Spark DataFrame.
* agg(*exprs): persist([storageLevel])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Sets the storage level to persist the contents of the DataFrame across operations after the first time it is computed.
* agg(*exprs): printSchema([level])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Prints out the schema in the tree format.
* agg(*exprs): randomSplit(weights[, seed])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Randomly splits this DataFrame with the provided weights.
* agg(*exprs): registerTempTable(name)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Registers this DataFrame as a temporary table using the given name.
* agg(*exprs): repartition(numPartitions, *cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame partitioned by the given partitioning expressions.
* agg(*exprs): repartitionByRange(numPartitions, *cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame partitioned by the given partitioning expressions.
* agg(*exprs): replace(to_replace[, value, subset])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame replacing a value with another value.
* agg(*exprs): rollup(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Create a multi-dimensional rollup for the current DataFrame using the specified columns, allowing for aggregation on them.
* agg(*exprs): sameSemantics(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns True when the logical query plans inside both DataFrames are equal and therefore return the same results.
* agg(*exprs): sample([withReplacement, fraction, seed])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a sampled subset of this DataFrame.
* agg(*exprs): sampleBy(col, fractions[, seed])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a stratified sample without replacement based on the fraction given on each stratum.
* agg(*exprs): scalar()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a Column object for a SCALAR Subquery containing exactly one row and one column.
* agg(*exprs): select(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Projects a set of expressions and returns a new DataFrame.
* agg(*exprs): selectExpr(*expr)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Projects a set of SQL expressions and returns a new DataFrame.
* agg(*exprs): semanticHash()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a hash code of the logical query plan against this DataFrame.
* agg(*exprs): show([n, truncate, vertical])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Prints the first n rows of the DataFrame to the console.
* agg(*exprs): sort(*cols, **kwargs)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame sorted by the specified column(s).
* agg(*exprs): sortWithinPartitions(*cols, **kwargs)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame with each partition sorted by the specified column(s).
* agg(*exprs): subtract(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame containing rows in this DataFrame but not in another DataFrame.
* agg(*exprs): summary(*statistics)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Computes specified statistics for numeric and string columns.
* agg(*exprs): tail(num)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the last num rows as a list of Row.
* agg(*exprs): take(num)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the first num rows as a list of Row.
* agg(*exprs): to(schema)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame where each row is reconciled to match the specified schema.
* agg(*exprs): toArrow()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the contents of this DataFrame as PyArrow pyarrow.Table.
* agg(*exprs): toDF(*cols)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame that with new specified column names
* agg(*exprs): toJSON([use_unicode])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Converts a DataFrame into a RDD of string.
* agg(*exprs): toLocalIterator([prefetchPartitions])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns an iterator that contains all of the rows in this DataFrame.
* agg(*exprs): toPandas()
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns the contents of this DataFrame as Pandas pandas.DataFrame.
* agg(*exprs): transform(func, *args, **kwargs)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame.
* agg(*exprs): transpose([indexColumn])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame.
* agg(*exprs): union(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame containing the union of rows in this and another DataFrame.
* agg(*exprs): unionAll(other)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Return a new DataFrame containing the union of rows in this and another DataFrame.
* agg(*exprs): unionByName(other[, allowMissingColumns])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame containing union of rows in this and another DataFrame.
* agg(*exprs): unpersist([blocking])
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Marks the DataFrame as non-persistent, and remove all blocks for it from memory and disk.
* agg(*exprs): unpivot(ids, values, variableColumnName, ...)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
* agg(*exprs): where(condition)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: where() is an alias for filter().
* agg(*exprs): withColumn(colName, col)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame by adding a column or replacing the existing column that has the same name.
* agg(*exprs): withColumnRenamed(existing, new)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame by renaming an existing column.
* agg(*exprs): withColumns(*colsMap)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame by adding multiple columns or replacing the existing columns that have the same names.
* agg(*exprs): withColumnsRenamed(colsMap)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame by renaming multiple columns.
* agg(*exprs): withMetadata(columnName, metadata)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Returns a new DataFrame by updating an existing column with metadata.
* agg(*exprs): withWatermark(eventTime, delayThreshold)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Defines an event time watermark for this DataFrame.
* agg(*exprs): writeTo(table)
  * Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).: Create a write configuration builder for v2 sources.


Attributes



* columns: dtypes
  * Retrieves the names of all columns in the DataFrame as a list.: Returns all column names and their data types as a list.
* columns: executionInfo
  * Retrieves the names of all columns in the DataFrame as a list.: Returns a ExecutionInfo object after the query was executed.
* columns: isStreaming
  * Retrieves the names of all columns in the DataFrame as a list.: Returns True if this DataFrame contains one or more sources that continuously return data as it arrives.
* columns: na
  * Retrieves the names of all columns in the DataFrame as a list.: Returns a DataFrameNaFunctions for handling missing values.
* columns: plot
  * Retrieves the names of all columns in the DataFrame as a list.: Returns a plot.core.PySparkPlotAccessor for plotting functions.
* columns: rdd
  * Retrieves the names of all columns in the DataFrame as a list.: Returns the content as an pyspark.RDD of Row.
* columns: schema
  * Retrieves the names of all columns in the DataFrame as a list.: Returns the schema of this DataFrame as a pyspark.sql.types.StructType.
* columns: sparkSession
  * Retrieves the names of all columns in the DataFrame as a list.: Returns Spark session that created this DataFrame.
* columns: stat
  * Retrieves the names of all columns in the DataFrame as a list.: Returns a DataFrameStatFunctions for statistic functions.
* columns: storageLevel
  * Retrieves the names of all columns in the DataFrame as a list.: Get the DataFrame's current storage level.
* columns: write
  * Retrieves the names of all columns in the DataFrame as a list.: Interface for saving the content of the non-streaming DataFrame out into external storage.
* columns: writeStream
  * Retrieves the names of all columns in the DataFrame as a list.: Interface for saving the content of the streaming DataFrame out into external storage.
* columns: is_cached
  * Retrieves the names of all columns in the DataFrame as a list.: 

# pyspark.sql.Column — PySpark 4.0.1 documentation
_class_ pyspark.sql.Column(_\*args_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column)
[#](#pyspark.sql.Column "Permalink to this definition")

A column in a DataFrame.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

Column instances can be created by

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])

```


Select a column out of a DataFrame >>> df.name Column<’name’> >>> df\[“name”\] Column<’name’>

Create from an expression

```
>>> df.age + 1
Column<...>
>>> 1 / df.age
Column<...>

```


Methods



* alias(*alias, **kwargs): asc()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Returns a sort expression based on the ascending order of the column.
* alias(*alias, **kwargs): asc_nulls_first()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Returns a sort expression based on ascending order of the column, and null values return before non-null values.
* alias(*alias, **kwargs): asc_nulls_last()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Returns a sort expression based on ascending order of the column, and null values appear after non-null values.
* alias(*alias, **kwargs): astype(dataType)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: astype() is an alias for cast().
* alias(*alias, **kwargs): between(lowerBound, upperBound)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Check if the current column's values are between the specified lower and upper bounds, inclusive.
* alias(*alias, **kwargs): bitwiseAND(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Compute bitwise AND of this expression with another expression.
* alias(*alias, **kwargs): bitwiseOR(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: "
* alias(*alias, **kwargs): bitwiseXOR(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Compute bitwise XOR of this expression with another expression.
* alias(*alias, **kwargs): cast(dataType)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Casts the column into type dataType.
* alias(*alias, **kwargs): contains(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Contains the other element.
* alias(*alias, **kwargs): desc()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Returns a sort expression based on the descending order of the column.
* alias(*alias, **kwargs): desc_nulls_first()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Returns a sort expression based on the descending order of the column, and null values appear before non-null values.
* alias(*alias, **kwargs): desc_nulls_last()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Returns a sort expression based on the descending order of the column, and null values appear after non-null values.
* alias(*alias, **kwargs): dropFields(*fieldNames)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: An expression that drops fields in StructType by name.
* alias(*alias, **kwargs): endswith(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: String ends with.
* alias(*alias, **kwargs): eqNullSafe(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Equality test that is safe for null values.
* alias(*alias, **kwargs): getField(name)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: An expression that gets a field by name in a StructType.
* alias(*alias, **kwargs): getItem(key)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: An expression that gets an item at position ordinal out of a list, or gets an item by key out of a dict.
* alias(*alias, **kwargs): ilike(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: SQL ILIKE expression (case insensitive LIKE).
* alias(*alias, **kwargs): isNaN()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: True if the current expression is NaN.
* alias(*alias, **kwargs): isNotNull()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: True if the current expression is NOT null.
* alias(*alias, **kwargs): isNull()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: True if the current expression is null.
* alias(*alias, **kwargs): isin(*cols)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.
* alias(*alias, **kwargs): like(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: SQL like expression.
* alias(*alias, **kwargs): name(*alias, **kwargs)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: name() is an alias for alias().
* alias(*alias, **kwargs): otherwise(value)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Evaluates a list of conditions and returns one of multiple possible result expressions.
* alias(*alias, **kwargs): outer()
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Mark this column as an outer column if its expression refers to columns from an outer query.
* alias(*alias, **kwargs): over(window)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Define a windowing column.
* alias(*alias, **kwargs): rlike(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: SQL RLIKE expression (LIKE with Regex).
* alias(*alias, **kwargs): startswith(other)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: String starts with.
* alias(*alias, **kwargs): substr(startPos, length)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Return a Column which is a substring of the column.
* alias(*alias, **kwargs): try_cast(dataType)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: This is a special version of cast that performs the same operation, but returns a NULL value instead of raising an error if the invoke method throws exception.
* alias(*alias, **kwargs): when(condition, value)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: Evaluates a list of conditions and returns one of multiple possible result expressions.
* alias(*alias, **kwargs): withField(fieldName, col)
  * Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).: An expression that adds/replaces a field in StructType by name.

# pyspark.sql.Observation — PySpark 4.0.1 documentation
_class_ pyspark.sql.Observation(_\*args_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/observation.html#Observation)
[#](#pyspark.sql.Observation "Permalink to this definition")

Class to observe (named) metrics on a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Metrics are aggregation expressions, which are applied to the DataFrame while it is being processed by an action.

The metrics have the following guarantees:

*   It will compute the defined aggregates (metrics) on all the data that is flowing through the Dataset during the action.
    
*   It will report the value of the defined aggregate columns as soon as we reach the end of the action.
    

The metrics columns must either contain a literal (e.g. lit(42)), or should contain one or more aggregate functions (e.g. sum(a) or sum(a + b) + avg(c) - lit(1)). Expressions that contain references to the input Dataset’s columns must always be wrapped in an aggregate function.

An Observation instance collects the metrics while the first action is executed. Subsequent actions do not modify the metrics returned by Observation.get. Retrieval of the metric via Observation.get blocks until the first action has finished and metrics become available.

New in version 3.3.0.

Notes

This class does not support streaming datasets.

Examples

```
>>> from pyspark.sql.functions import col, count, lit, max
>>> from pyspark.sql import Observation
>>> df = spark.createDataFrame([["Alice", 2], ["Bob", 5]], ["name", "age"])
>>> observation = Observation("my metrics")
>>> observed_df = df.observe(observation, count(lit(1)).alias("count"), max(col("age")))
>>> observed_df.count()
2
>>> observation.get
{'count': 2, 'max(age)': 5}

```


Attributes


# pyspark.sql.Row — PySpark 4.0.1 documentation
_class_ pyspark.sql.Row(_\*args_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#Row)
[#](#pyspark.sql.Row "Permalink to this definition")

A row in [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). The fields in it can be accessed:

*   like attributes (`row.key`)
    
*   like dictionary values (`row[key]`)
    

`key in row` will search through row keys.

Row can be used to create a row object by using named arguments. It is not allowed to omit a named argument to represent that the value is None or missing. This should be explicitly set to None in this case.

Changed in version 3.0.0: Rows created from named arguments no longer have field names sorted alphabetically and will be ordered in the position as entered.

Examples

```
>>> from pyspark.sql import Row
>>> row = Row(name="Alice", age=11)
>>> row
Row(name='Alice', age=11)
>>> row['name'], row['age']
('Alice', 11)
>>> row.name, row.age
('Alice', 11)
>>> 'name' in row
True
>>> 'wrong_key' in row
False

```


Row also can be used to create another Row like class, then it could be used to create Row objects, such as

```
>>> Person = Row("name", "age")
>>> Person
<Row('name', 'age')>
>>> 'name' in Person
True
>>> 'wrong_key' in Person
False
>>> Person("Alice", 11)
Row(name='Alice', age=11)

```


This form can also be used to create rows as tuple values, i.e. with unnamed fields.

```
>>> row1 = Row("Alice", 11)
>>> row2 = Row(name="Alice", age=11)
>>> row1 == row2
True

```


Methods


|asDict([recursive])        |Return as a dict                      |
|---------------------------|--------------------------------------|
|count(value, /)            |Return number of occurrences of value.|
|index(value[, start, stop])|Return first index of value.          |

# pyspark.sql.GroupedData — PySpark 4.0.1 documentation
_class_ pyspark.sql.GroupedData(_jgd_, _df_)
[\[source\]](about:blank/_modules/pyspark/sql/group.html#GroupedData)
[#](#pyspark.sql.GroupedData "Permalink to this definition")

A set of methods for aggregations on a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), created by [`DataFrame.groupBy()`](about:blank/pyspark.sql.DataFrame.groupBy.html#pyspark.sql.DataFrame.groupBy "pyspark.sql.DataFrame.groupBy").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* agg(*exprs): apply(udf)
  * Compute aggregates and returns the result as a DataFrame.: It is an alias of pyspark.sql.GroupedData.applyInPandas(); however, it takes a pyspark.sql.functions.pandas_udf() whereas pyspark.sql.GroupedData.applyInPandas() takes a Python native function.
* agg(*exprs): applyInArrow(func, schema)
  * Compute aggregates and returns the result as a DataFrame.: Maps each group of the current DataFrame using an Arrow udf and returns the result as a DataFrame.
* agg(*exprs): applyInPandas(func, schema)
  * Compute aggregates and returns the result as a DataFrame.: Maps each group of the current DataFrame using a pandas udf and returns the result as a DataFrame.
* agg(*exprs): applyInPandasWithState(func, ...)
  * Compute aggregates and returns the result as a DataFrame.: Applies the given function to each group of data, while maintaining a user-defined per-group state.
* agg(*exprs): avg(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes average values for each numeric columns for each group.
* agg(*exprs): cogroup(other)
  * Compute aggregates and returns the result as a DataFrame.: Cogroups this group with another group so that we can run cogrouped operations.
* agg(*exprs): count()
  * Compute aggregates and returns the result as a DataFrame.: Counts the number of records for each group.
* agg(*exprs): max(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes the max value for each numeric columns for each group.
* agg(*exprs): mean(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes average values for each numeric columns for each group.
* agg(*exprs): min(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes the min value for each numeric column for each group.
* agg(*exprs): pivot(pivot_col[, values])
  * Compute aggregates and returns the result as a DataFrame.: Pivots a column of the current DataFrame and performs the specified aggregation.
* agg(*exprs): sum(*cols)
  * Compute aggregates and returns the result as a DataFrame.: Computes the sum for each numeric columns for each group.
* agg(*exprs): transformWithStateInPandas(...[, ...])
  * Compute aggregates and returns the result as a DataFrame.: Invokes methods defined in the stateful processor used in arbitrary state API v2.


# pyspark.sql.PandasCogroupedOps — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.PandasCogroupedOps

_class_ pyspark.sql.PandasCogroupedOps(_gd1_, _gd2_)
[\[source\]](about:blank/_modules/pyspark/sql/pandas/group_ops.html#PandasCogroupedOps)
[#](#pyspark.sql.PandasCogroupedOps "Permalink to this definition")

A logical grouping of two [`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData"), created by [`GroupedData.cogroup()`](about:blank/pyspark.sql.GroupedData.cogroup.html#pyspark.sql.GroupedData.cogroup "pyspark.sql.GroupedData.cogroup").

New in version 3.0.0.

Changed in version 3.4.0: Support Spark Connect.

Methods



* applyInArrow(func, schema): applyInPandas(func, schema)
  * Applies a function to each cogroup using Arrow and returns the result as a DataFrame.: Applies a function to each cogroup using pandas and returns the result as a DataFrame.


# pyspark.sql.DataFrameNaFunctions — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.DataFrameNaFunctions

_class_ pyspark.sql.DataFrameNaFunctions(_df_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameNaFunctions)
[#](#pyspark.sql.DataFrameNaFunctions "Permalink to this definition")

Functionality for working with missing data in [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* drop([how, thresh, subset]): fill(value[, subset])
  * Returns a new DataFrame omitting rows with null or NaN values.: Returns a new DataFrame which null values are filled with new value.
* drop([how, thresh, subset]): replace(to_replace[, value, subset])
  * Returns a new DataFrame omitting rows with null or NaN values.: Returns a new DataFrame replacing a value with another value.


# pyspark.sql.DataFrameStatFunctions — PySpark 4.0.1 documentation
_class_ pyspark.sql.DataFrameStatFunctions(_df_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions)
[#](#pyspark.sql.DataFrameStatFunctions "Permalink to this definition")

Functionality for statistic functions with [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* approxQuantile(col, probabilities, relativeError): corr(col1, col2[, method])
  * Calculates the approximate quantiles of numerical columns of a DataFrame.: Calculates the correlation of two columns of a DataFrame as a double value.
* approxQuantile(col, probabilities, relativeError): cov(col1, col2)
  * Calculates the approximate quantiles of numerical columns of a DataFrame.: Calculate the sample covariance for the given columns, specified by their names, as a double value.
* approxQuantile(col, probabilities, relativeError): crosstab(col1, col2)
  * Calculates the approximate quantiles of numerical columns of a DataFrame.: Computes a pair-wise frequency table of the given columns.
* approxQuantile(col, probabilities, relativeError): freqItems(cols[, support])
  * Calculates the approximate quantiles of numerical columns of a DataFrame.: Finding frequent items for columns, possibly with false positives.
* approxQuantile(col, probabilities, relativeError): sampleBy(col, fractions[, seed])
  * Calculates the approximate quantiles of numerical columns of a DataFrame.: Returns a stratified sample without replacement based on the fraction given on each stratum.


# pyspark.sql.Window — PySpark 4.0.1 documentation
_class_ pyspark.sql.Window[\[source\]](about:blank/_modules/pyspark/sql/window.html#Window)
[#](#pyspark.sql.Window "Permalink to this definition")

Utility functions for defining window in DataFrames.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Notes

When ordering is not defined, an unbounded window frame (rowFrame, unboundedPreceding, unboundedFollowing) is used by default. When ordering is defined, a growing window frame (rangeFrame, unboundedPreceding, currentRow) is used by default.

Examples

```
>>> # ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
>>> window = Window.orderBy("date").rowsBetween(Window.unboundedPreceding, Window.currentRow)

```


```
>>> # PARTITION BY country ORDER BY date RANGE BETWEEN 3 PRECEDING AND 3 FOLLOWING
>>> window = Window.orderBy("date").partitionBy("country").rangeBetween(-3, 3)

```


Methods



* orderBy(*cols): partitionBy(*cols)
  * Creates a WindowSpec with the ordering defined.: Creates a WindowSpec with the partitioning defined.
* orderBy(*cols): rangeBetween(start, end)
  * Creates a WindowSpec with the ordering defined.: Creates a WindowSpec with the frame boundaries defined, from start (inclusive) to end (inclusive).
* orderBy(*cols): rowsBetween(start, end)
  * Creates a WindowSpec with the ordering defined.: Creates a WindowSpec with the frame boundaries defined, from start (inclusive) to end (inclusive).


Attributes


|currentRow        |   |
|------------------|---|
|unboundedFollowing|   |
|unboundedPreceding|   |


# pyspark.sql.DataFrameReader — PySpark 4.0.1 documentation
_class_ pyspark.sql.DataFrameReader(_spark_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader)
[#](#pyspark.sql.DataFrameReader "Permalink to this definition")

Interface used to load a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") from external storage systems (e.g. file systems, key-value stores, etc). Use [`SparkSession.read`](about:blank/pyspark.sql.SparkSession.read.html#pyspark.sql.SparkSession.read "pyspark.sql.SparkSession.read") to access this.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* csv(path[, schema, sep, encoding, quote, ...]): format(source)
  * Loads a CSV file and returns the result as a  DataFrame.: Specifies the input data source format.
* csv(path[, schema, sep, encoding, quote, ...]): jdbc(url, table[, column, lowerBound, ...])
  * Loads a CSV file and returns the result as a  DataFrame.: Construct a DataFrame representing the database table named table accessible via JDBC URL url and connection properties.
* csv(path[, schema, sep, encoding, quote, ...]): json(path[, schema, primitivesAsString, ...])
  * Loads a CSV file and returns the result as a  DataFrame.: Loads JSON files and returns the results as a DataFrame.
* csv(path[, schema, sep, encoding, quote, ...]): load([path, format, schema])
  * Loads a CSV file and returns the result as a  DataFrame.: Loads data from a data source and returns it as a DataFrame.
* csv(path[, schema, sep, encoding, quote, ...]): option(key, value)
  * Loads a CSV file and returns the result as a  DataFrame.: Adds an input option for the underlying data source.
* csv(path[, schema, sep, encoding, quote, ...]): options(**options)
  * Loads a CSV file and returns the result as a  DataFrame.: Adds input options for the underlying data source.
* csv(path[, schema, sep, encoding, quote, ...]): orc(path[, mergeSchema, pathGlobFilter, ...])
  * Loads a CSV file and returns the result as a  DataFrame.: Loads ORC files, returning the result as a DataFrame.
* csv(path[, schema, sep, encoding, quote, ...]): parquet(*paths, **options)
  * Loads a CSV file and returns the result as a  DataFrame.: Loads Parquet files, returning the result as a DataFrame.
* csv(path[, schema, sep, encoding, quote, ...]): schema(schema)
  * Loads a CSV file and returns the result as a  DataFrame.: Specifies the input schema.
* csv(path[, schema, sep, encoding, quote, ...]): table(tableName)
  * Loads a CSV file and returns the result as a  DataFrame.: Returns the specified table as a DataFrame.
* csv(path[, schema, sep, encoding, quote, ...]): text(paths[, wholetext, lineSep, ...])
  * Loads a CSV file and returns the result as a  DataFrame.: Loads text files and returns a DataFrame whose schema starts with a string column named "value", and followed by partitioned columns if there are any.
* csv(path[, schema, sep, encoding, quote, ...]): xml(path[, rowTag, schema, ...])
  * Loads a CSV file and returns the result as a  DataFrame.: Loads a XML file and returns the result as a  DataFrame.


# pyspark.sql.DataFrameWriter — PySpark 4.0.1 documentation
_class_ pyspark.sql.DataFrameWriter(_df_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter)
[#](#pyspark.sql.DataFrameWriter "Permalink to this definition")

Interface used to write a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to external storage systems (e.g. file systems, key-value stores, etc). Use [`DataFrame.write`](about:blank/pyspark.sql.DataFrame.write.html#pyspark.sql.DataFrame.write "pyspark.sql.DataFrame.write") to access this.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* bucketBy(numBuckets, col, *cols): clusterBy(*cols)
  * Buckets the output by the given columns.: Clusters the data by the given columns to optimize query performance.
* bucketBy(numBuckets, col, *cols): csv(path[, mode, compression, sep, quote, ...])
  * Buckets the output by the given columns.: Saves the content of the DataFrame in CSV format at the specified path.
* bucketBy(numBuckets, col, *cols): format(source)
  * Buckets the output by the given columns.: Specifies the underlying output data source.
* bucketBy(numBuckets, col, *cols): insertInto(tableName[, overwrite])
  * Buckets the output by the given columns.: Inserts the content of the DataFrame to the specified table.
* bucketBy(numBuckets, col, *cols): jdbc(url, table[, mode, properties])
  * Buckets the output by the given columns.: Saves the content of the DataFrame to an external database table via JDBC.
* bucketBy(numBuckets, col, *cols): json(path[, mode, compression, dateFormat, ...])
  * Buckets the output by the given columns.: Saves the content of the DataFrame in JSON format (JSON Lines text format or newline-delimited JSON) at the specified path.
* bucketBy(numBuckets, col, *cols): mode(saveMode)
  * Buckets the output by the given columns.: Specifies the behavior when data or table already exists.
* bucketBy(numBuckets, col, *cols): option(key, value)
  * Buckets the output by the given columns.: Adds an output option for the underlying data source.
* bucketBy(numBuckets, col, *cols): options(**options)
  * Buckets the output by the given columns.: Adds output options for the underlying data source.
* bucketBy(numBuckets, col, *cols): orc(path[, mode, partitionBy, compression])
  * Buckets the output by the given columns.: Saves the content of the DataFrame in ORC format at the specified path.
* bucketBy(numBuckets, col, *cols): parquet(path[, mode, partitionBy, compression])
  * Buckets the output by the given columns.: Saves the content of the DataFrame in Parquet format at the specified path.
* bucketBy(numBuckets, col, *cols): partitionBy(*cols)
  * Buckets the output by the given columns.: Partitions the output by the given columns on the file system.
* bucketBy(numBuckets, col, *cols): save([path, format, mode, partitionBy])
  * Buckets the output by the given columns.: Saves the contents of the DataFrame to a data source.
* bucketBy(numBuckets, col, *cols): saveAsTable(name[, format, mode, partitionBy])
  * Buckets the output by the given columns.: Saves the content of the DataFrame as the specified table.
* bucketBy(numBuckets, col, *cols): sortBy(col, *cols)
  * Buckets the output by the given columns.: Sorts the output in each bucket by the given columns on the file system.
* bucketBy(numBuckets, col, *cols): text(path[, compression, lineSep])
  * Buckets the output by the given columns.: Saves the content of the DataFrame in a text file at the specified path.
* bucketBy(numBuckets, col, *cols): xml(path[, rowTag, mode, attributePrefix, ...])
  * Buckets the output by the given columns.: Saves the content of the DataFrame in XML format at the specified path.


# pyspark.sql.DataFrameWriterV2 — PySpark 4.0.1 documentation
_class_ pyspark.sql.DataFrameWriterV2(_df_, _table_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2)
[#](#pyspark.sql.DataFrameWriterV2 "Permalink to this definition")

Interface used to write a class:pyspark.sql.dataframe.DataFrame to external storage using the v2 API.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* append(): clusterBy(col, *cols)
  * Append the contents of the data frame to the output table.: Clusters the data by the given columns to optimize query performance.
* append(): create()
  * Append the contents of the data frame to the output table.: Create a new table from the contents of the data frame.
* append(): createOrReplace()
  * Append the contents of the data frame to the output table.: Create a new table or replace an existing table with the contents of the data frame.
* append(): option(key, value)
  * Append the contents of the data frame to the output table.: Add a write option.
* append(): options(**options)
  * Append the contents of the data frame to the output table.: Add write options.
* append(): overwrite(condition)
  * Append the contents of the data frame to the output table.: Overwrite rows matching the given filter condition with the contents of the data frame in the output table.
* append(): overwritePartitions()
  * Append the contents of the data frame to the output table.: Overwrite all partition for which the data frame contains at least one row with the contents of the data frame in the output table.
* append(): partitionedBy(col, *cols)
  * Append the contents of the data frame to the output table.: Partition the output table created by create, createOrReplace, or replace using the given columns or transforms.
* append(): replace()
  * Append the contents of the data frame to the output table.: Replace an existing table with the contents of the data frame.
* append(): tableProperty(property, value)
  * Append the contents of the data frame to the output table.: Add table property.
* append(): using(provider)
  * Append the contents of the data frame to the output table.: Specifies a provider for the underlying output data source.

# pyspark.sql.UDFRegistration — PySpark 4.0.1 documentation
_class_ pyspark.sql.UDFRegistration(_sparkSession_)
[\[source\]](about:blank/_modules/pyspark/sql/udf.html#UDFRegistration)
[#](#pyspark.sql.UDFRegistration "Permalink to this definition")

Wrapper for user-defined function registration. This instance can be accessed by `spark.udf` or `sqlContext.udf`.

New in version 1.3.1.

Methods



* register(name, f[, returnType]): registerJavaFunction(name, javaClassName[, ...])
  * Register a Python function (including lambda function) or a user-defined function as a SQL function.: Register a Java user-defined function as a SQL function.
* register(name, f[, returnType]): registerJavaUDAF(name, javaClassName)
  * Register a Python function (including lambda function) or a user-defined function as a SQL function.: Register a Java user-defined aggregate function as a SQL function.



# pyspark.sql.UDTFRegistration — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.UDTFRegistration

_class_ pyspark.sql.UDTFRegistration(_sparkSession_)
[\[source\]](about:blank/_modules/pyspark/sql/udtf.html#UDTFRegistration)
[#](#pyspark.sql.UDTFRegistration "Permalink to this definition")

Wrapper for user-defined table function registration. This instance can be accessed by `spark.udtf` or `sqlContext.udtf`.

New in version 3.5.0.

Methods


# pyspark.sql.udf.UserDefinedFunction — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.udf.UserDefinedFunction

_class_ pyspark.sql.udf.UserDefinedFunction(_func_, _returnType\=StringType()_, _name\=None_, _evalType\=100_, _deterministic\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/udf.html#UserDefinedFunction)
[#](#pyspark.sql.udf.UserDefinedFunction "Permalink to this definition")

User defined function in Python

New in version 1.3.

Notes

The constructor of this class is not supposed to be directly called. Use [`pyspark.sql.functions.udf()`](about:blank/pyspark.sql.functions.udf.html#pyspark.sql.functions.udf "pyspark.sql.functions.udf") or [`pyspark.sql.functions.pandas_udf()`](about:blank/pyspark.sql.functions.pandas_udf.html#pyspark.sql.functions.pandas_udf "pyspark.sql.functions.pandas_udf") to create this instance.

Methods



Attributes


# pyspark.sql.udtf.UserDefinedTableFunction — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.udtf.UserDefinedTableFunction

_class_ pyspark.sql.udtf.UserDefinedTableFunction(_func_, _returnType_, _name\=None_, _evalType\=300_, _deterministic\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/udtf.html#UserDefinedTableFunction)
[#](#pyspark.sql.udtf.UserDefinedTableFunction "Permalink to this definition")

User-defined table function in Python

New in version 3.5.0.

Notes

The constructor of this class is not supposed to be directly called. Use [`pyspark.sql.functions.udtf()`](about:blank/pyspark.sql.functions.udtf.html#pyspark.sql.functions.udtf "pyspark.sql.functions.udtf") to create this instance.

This API is evolving.

Methods



Attributes


# pyspark.sql.datasource.DataSource — PySpark 4.0.1 documentation
_class_ pyspark.sql.datasource.DataSource(_options_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSource)
[#](#pyspark.sql.datasource.DataSource "Permalink to this definition")

A base class for data sources.

This class represents a custom data source that allows for reading from and/or writing to it. The data source provides methods to create readers and writers for reading and writing data, respectively. At least one of the methods [`DataSource.reader()`](about:blank/pyspark.sql.datasource.DataSource.reader.html#pyspark.sql.datasource.DataSource.reader "pyspark.sql.datasource.DataSource.reader") or [`DataSource.writer()`](about:blank/pyspark.sql.datasource.DataSource.writer.html#pyspark.sql.datasource.DataSource.writer "pyspark.sql.datasource.DataSource.writer") must be implemented by any subclass to make the data source either readable or writable (or both).

After implementing this interface, you can start to load your data source using `spark.read.format(...).load()` and save data using `df.write.format(...).save()`.

Methods



* name(): reader(schema)
  * Returns a string represents the format name of this data source.: Returns a DataSourceReader instance for reading data.
* name(): schema()
  * Returns a string represents the format name of this data source.: Returns the schema of the data source.
* name(): simpleStreamReader(schema)
  * Returns a string represents the format name of this data source.: Returns a SimpleDataSourceStreamReader instance for reading data.
* name(): streamReader(schema)
  * Returns a string represents the format name of this data source.: Returns a DataSourceStreamReader instance for reading streaming data.
* name(): streamWriter(schema, overwrite)
  * Returns a string represents the format name of this data source.: Returns a DataSourceStreamWriter instance for writing data into a streaming sink.
* name(): writer(schema, overwrite)
  * Returns a string represents the format name of this data source.: Returns a DataSourceWriter instance for writing data.



# pyspark.sql.datasource.DataSourceReader — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.datasource.DataSourceReader

_class_ pyspark.sql.datasource.DataSourceReader[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceReader)
[#](#pyspark.sql.datasource.DataSourceReader "Permalink to this definition")

A base class for data source readers. Data source readers are responsible for outputting data from a data source.

Methods


|partitions()   |Returns an iterator of partitions for this data source.                        |
|---------------|-------------------------------------------------------------------------------|
|read(partition)|Generates data for a given partition and returns an iterator of tuples or rows.|


# pyspark.sql.datasource.DataSourceStreamReader — PySpark 4.0.1 documentation
_class_ pyspark.sql.datasource.DataSourceStreamReader[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader)
[#](#pyspark.sql.datasource.DataSourceStreamReader "Permalink to this definition")

A base class for streaming data source readers. Data source stream readers are responsible for outputting data from a streaming data source.

Methods



* commit(end): initialOffset()
  * Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.: Return the initial offset of the streaming data source.
* commit(end): latestOffset()
  * Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.: Returns the most recent offset available.
* commit(end): partitions(start, end)
  * Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.: Returns a list of InputPartition given the start and end offsets.
* commit(end): read(partition)
  * Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.: Generates data for a given partition and returns an iterator of tuples or rows.
* commit(end): stop()
  * Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.: Stop this source and free any resources it has allocated.


# pyspark.sql.datasource.DataSourceWriter — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.datasource.DataSourceWriter

_class_ pyspark.sql.datasource.DataSourceWriter[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceWriter)
[#](#pyspark.sql.datasource.DataSourceWriter "Permalink to this definition")

A base class for data source writers. Data source writers are responsible for saving the data to the data source.

Methods


|abort(messages) |Aborts this writing job due to task failures.           |
|----------------|--------------------------------------------------------|
|commit(messages)|Commits this writing job with a list of commit messages.|
|write(iterator) |Writes data into the data source.                       |


# pyspark.sql.datasource.DataSourceRegistration — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.datasource.DataSourceRegistration

_class_ pyspark.sql.datasource.DataSourceRegistration(_sparkSession_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceRegistration)
[#](#pyspark.sql.datasource.DataSourceRegistration "Permalink to this definition")

Wrapper for data source registration. This instance can be accessed by `spark.dataSource`.

Methods


# pyspark.sql.datasource.InputPartition — PySpark 4.0.1 documentation
_class_ pyspark.sql.datasource.InputPartition(_value_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#InputPartition)
[#](#pyspark.sql.datasource.InputPartition "Permalink to this definition")

A base class representing an input partition returned by the partitions() method of [`DataSourceReader`](about:blank/pyspark.sql.datasource.DataSourceReader.html#pyspark.sql.datasource.DataSourceReader "pyspark.sql.datasource.DataSourceReader").

Notes

This class must be picklable.

Examples

Use the default input partition implementation:

```
>>> def partitions(self):
...     return [InputPartition(1)]

```


Subclass the input partition class:

```
>>> from dataclasses import dataclass
>>> @dataclass
... class RangeInputPartition(InputPartition):
...     start: int
...     end: int

```


```
>>> def partitions(self):
...     return [RangeInputPartition(1, 3), RangeInputPartition(4, 6)]

```


# pyspark.sql.datasource.WriterCommitMessage — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Core Classes](../core_classes.html)
*   pyspark.sql.datasource.WriterCommitMessage

_class_ pyspark.sql.datasource.WriterCommitMessage[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#WriterCommitMessage)
[#](#pyspark.sql.datasource.WriterCommitMessage "Permalink to this definition")

A commit message returned by the [`DataSourceWriter.write()`](about:blank/pyspark.sql.datasource.DataSourceWriter.write.html#pyspark.sql.datasource.DataSourceWriter.write "pyspark.sql.datasource.DataSourceWriter.write") and will be sent back to the driver side as input parameter of [`DataSourceWriter.commit()`](about:blank/pyspark.sql.datasource.DataSourceWriter.commit.html#pyspark.sql.datasource.DataSourceWriter.commit "pyspark.sql.datasource.DataSourceWriter.commit") or [`DataSourceWriter.abort()`](about:blank/pyspark.sql.datasource.DataSourceWriter.abort.html#pyspark.sql.datasource.DataSourceWriter.abort "pyspark.sql.datasource.DataSourceWriter.abort") method.

Notes

This class must be picklable.


# pyspark.sql.tvf.TableValuedFunction — PySpark 4.0.1 documentation
_class_ pyspark.sql.tvf.TableValuedFunction(_sparkSession_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction)
[#](#pyspark.sql.tvf.TableValuedFunction "Permalink to this definition")

Interface for invoking table-valued functions in Spark SQL.

Methods



* collations(): explode(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element in the given array or map.
* collations(): explode_outer(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element with position in the given array or map.
* collations(): inline(input)
  * Get all of the Spark SQL string collations.: Explodes an array of structs into a table.
* collations(): inline_outer(input)
  * Get all of the Spark SQL string collations.: Explodes an array of structs into a table.
* collations(): json_tuple(input, *fields)
  * Get all of the Spark SQL string collations.: Creates a new row for a json column according to the given field names.
* collations(): posexplode(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element with position in the given array or map.
* collations(): posexplode_outer(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element with position in the given array or map.
* collations(): range(start[, end, step, numPartitions])
  * Get all of the Spark SQL string collations.: Create a DataFrame with single pyspark.sql.types.LongType column named id, containing elements in a range from start to end (exclusive) with step value step.
* collations(): sql_keywords()
  * Get all of the Spark SQL string collations.: Get Spark SQL keywords.
* collations(): stack(n, *fields)
  * Get all of the Spark SQL string collations.: Separates col1, ..., colk into n rows.
* collations(): variant_explode(input)
  * Get all of the Spark SQL string collations.: Separates a variant object/array into multiple rows containing its fields/elements.
* collations(): variant_explode_outer(input)
  * Get all of the Spark SQL string collations.: Separates a variant object/array into multiple rows containing its fields/elements.


# pyspark.sql.VariantVal — PySpark 4.0.1 documentation
_class_ pyspark.sql.VariantVal(_value_, _metadata_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantVal)
[#](#pyspark.sql.VariantVal "Permalink to this definition")

A class to represent a Variant value in Python.

New in version 4.0.0.

Parameters

**value**bytes

The bytes representing the value component of the Variant.

**metadata**bytes

The bytes representing the metadata component of the Variant.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }'''} ])
>>> v = df.select(sf.parse_json(df.json).alias("var")).head().var
>>> v.toPython()
{'a': 1}
>>> v.toJson()
'{"a":1}'

```


Methods



Methods


|parseJson(json_str)|Convert the VariantVal to a nested Python object of Python data types.|
|-------------------|----------------------------------------------------------------------|
|toJson([zone_id])  |Convert the VariantVal to a JSON string.                              |
|toPython()         |Convert the VariantVal to a Python data structure.                    |


# pyspark.sql.table_arg.TableArg — PySpark 4.0.1 documentation
_class_ pyspark.sql.table\_arg.TableArg[\[source\]](about:blank/_modules/pyspark/sql/table_arg.html#TableArg)
[#](#pyspark.sql.table_arg.TableArg "Permalink to this definition")

Represents a table argument in PySpark.

This class provides methods to specify partitioning, ordering, and single-partition constraints when passing a DataFrame as a table argument to TVF(Table-Valued Function)s including UDTF(User-Defined Table Function)s.

Methods


|orderBy(*cols)       |Orders the data within each partition by the specified columns.|
|---------------------|---------------------------------------------------------------|
|partitionBy(*cols)   |Partitions the data based on the specified columns.            |
|withSinglePartition()|Forces the data to be processed in a single partition.         |
