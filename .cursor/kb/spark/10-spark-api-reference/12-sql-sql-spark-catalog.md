# Catalog — PySpark 4.0.1 documentation
[`Catalog.cacheTable`](about:blank/api/pyspark.sql.Catalog.cacheTable.html#pyspark.sql.Catalog.cacheTable "pyspark.sql.Catalog.cacheTable")(tableName\[, storageLevel\])

Caches the specified table in-memory or with given storage level.

[`Catalog.clearCache`](about:blank/api/pyspark.sql.Catalog.clearCache.html#pyspark.sql.Catalog.clearCache "pyspark.sql.Catalog.clearCache")()

Removes all cached tables from the in-memory cache.

[`Catalog.createExternalTable`](about:blank/api/pyspark.sql.Catalog.createExternalTable.html#pyspark.sql.Catalog.createExternalTable "pyspark.sql.Catalog.createExternalTable")(tableName\[, ...\])

Creates a table based on the dataset in a data source.

[`Catalog.createTable`](about:blank/api/pyspark.sql.Catalog.createTable.html#pyspark.sql.Catalog.createTable "pyspark.sql.Catalog.createTable")(tableName\[, path, ...\])

Creates a table based on the dataset in a data source.

[`Catalog.currentCatalog`](about:blank/api/pyspark.sql.Catalog.currentCatalog.html#pyspark.sql.Catalog.currentCatalog "pyspark.sql.Catalog.currentCatalog")()

Returns the current default catalog in this session.

[`Catalog.currentDatabase`](about:blank/api/pyspark.sql.Catalog.currentDatabase.html#pyspark.sql.Catalog.currentDatabase "pyspark.sql.Catalog.currentDatabase")()

Returns the current default database in this session.

[`Catalog.databaseExists`](about:blank/api/pyspark.sql.Catalog.databaseExists.html#pyspark.sql.Catalog.databaseExists "pyspark.sql.Catalog.databaseExists")(dbName)

Check if the database with the specified name exists.

[`Catalog.dropGlobalTempView`](about:blank/api/pyspark.sql.Catalog.dropGlobalTempView.html#pyspark.sql.Catalog.dropGlobalTempView "pyspark.sql.Catalog.dropGlobalTempView")(viewName)

Drops the global temporary view with the given view name in the catalog.

[`Catalog.dropTempView`](about:blank/api/pyspark.sql.Catalog.dropTempView.html#pyspark.sql.Catalog.dropTempView "pyspark.sql.Catalog.dropTempView")(viewName)

Drops the local temporary view with the given view name in the catalog.

[`Catalog.functionExists`](about:blank/api/pyspark.sql.Catalog.functionExists.html#pyspark.sql.Catalog.functionExists "pyspark.sql.Catalog.functionExists")(functionName\[, dbName\])

Check if the function with the specified name exists.

[`Catalog.getDatabase`](about:blank/api/pyspark.sql.Catalog.getDatabase.html#pyspark.sql.Catalog.getDatabase "pyspark.sql.Catalog.getDatabase")(dbName)

Get the database with the specified name.

[`Catalog.getFunction`](about:blank/api/pyspark.sql.Catalog.getFunction.html#pyspark.sql.Catalog.getFunction "pyspark.sql.Catalog.getFunction")(functionName)

Get the function with the specified name.

[`Catalog.getTable`](about:blank/api/pyspark.sql.Catalog.getTable.html#pyspark.sql.Catalog.getTable "pyspark.sql.Catalog.getTable")(tableName)

Get the table or view with the specified name.

[`Catalog.isCached`](about:blank/api/pyspark.sql.Catalog.isCached.html#pyspark.sql.Catalog.isCached "pyspark.sql.Catalog.isCached")(tableName)

Returns true if the table is currently cached in-memory.

[`Catalog.listCatalogs`](about:blank/api/pyspark.sql.Catalog.listCatalogs.html#pyspark.sql.Catalog.listCatalogs "pyspark.sql.Catalog.listCatalogs")(\[pattern\])

Returns a list of catalogs in this session.

[`Catalog.listColumns`](about:blank/api/pyspark.sql.Catalog.listColumns.html#pyspark.sql.Catalog.listColumns "pyspark.sql.Catalog.listColumns")(tableName\[, dbName\])

Returns a list of columns for the given table/view in the specified database.

[`Catalog.listDatabases`](about:blank/api/pyspark.sql.Catalog.listDatabases.html#pyspark.sql.Catalog.listDatabases "pyspark.sql.Catalog.listDatabases")(\[pattern\])

Returns a list of databases available across all sessions.

[`Catalog.listFunctions`](about:blank/api/pyspark.sql.Catalog.listFunctions.html#pyspark.sql.Catalog.listFunctions "pyspark.sql.Catalog.listFunctions")(\[dbName, pattern\])

Returns a list of functions registered in the specified database.

[`Catalog.listTables`](about:blank/api/pyspark.sql.Catalog.listTables.html#pyspark.sql.Catalog.listTables "pyspark.sql.Catalog.listTables")(\[dbName, pattern\])

Returns a list of tables/views in the specified database.

[`Catalog.recoverPartitions`](about:blank/api/pyspark.sql.Catalog.recoverPartitions.html#pyspark.sql.Catalog.recoverPartitions "pyspark.sql.Catalog.recoverPartitions")(tableName)

Recovers all the partitions of the given table and updates the catalog.

[`Catalog.refreshByPath`](about:blank/api/pyspark.sql.Catalog.refreshByPath.html#pyspark.sql.Catalog.refreshByPath "pyspark.sql.Catalog.refreshByPath")(path)

Invalidates and refreshes all the cached data (and the associated metadata) for any DataFrame that contains the given data source path.

[`Catalog.refreshTable`](about:blank/api/pyspark.sql.Catalog.refreshTable.html#pyspark.sql.Catalog.refreshTable "pyspark.sql.Catalog.refreshTable")(tableName)

Invalidates and refreshes all the cached data and metadata of the given table.

[`Catalog.registerFunction`](about:blank/api/pyspark.sql.Catalog.registerFunction.html#pyspark.sql.Catalog.registerFunction "pyspark.sql.Catalog.registerFunction")(name, f\[, returnType\])

An alias for `spark.udf.register()`.

[`Catalog.setCurrentCatalog`](about:blank/api/pyspark.sql.Catalog.setCurrentCatalog.html#pyspark.sql.Catalog.setCurrentCatalog "pyspark.sql.Catalog.setCurrentCatalog")(catalogName)

Sets the current default catalog in this session.

[`Catalog.setCurrentDatabase`](about:blank/api/pyspark.sql.Catalog.setCurrentDatabase.html#pyspark.sql.Catalog.setCurrentDatabase "pyspark.sql.Catalog.setCurrentDatabase")(dbName)

Sets the current default database in this session.

[`Catalog.tableExists`](about:blank/api/pyspark.sql.Catalog.tableExists.html#pyspark.sql.Catalog.tableExists "pyspark.sql.Catalog.tableExists")(tableName\[, dbName\])

Check if the table or view with the specified name exists.

[`Catalog.uncacheTable`](about:blank/api/pyspark.sql.Catalog.uncacheTable.html#pyspark.sql.Catalog.uncacheTable "pyspark.sql.Catalog.uncacheTable")(tableName)

Removes the specified table from the in-memory cache.


# pyspark.sql.Catalog.cacheTable — PySpark 4.0.1 documentation
Catalog.cacheTable(_tableName_, _storageLevel\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.cacheTable)
[#](#pyspark.sql.Catalog.cacheTable "Permalink to this definition")

Caches the specified table in-memory or with given storage level. Default MEMORY\_AND\_DISK.

New in version 2.0.0.

Parameters

**tableName**str

name of the table to get.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name.

**storageLevel**`StorageLevel`, optional

storage level to set for persistence.

Changed in version 3.5.0: Allow to specify storage level.

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
>>> spark.catalog.cacheTable("tbl1")

```


or

```
>>> spark.catalog.cacheTable("tbl1", StorageLevel.OFF_HEAP)

```


Throw an analysis exception when the table does not exist.

```
>>> spark.catalog.cacheTable("not_existing_table")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


Using the fully qualified name for the table.

```
>>> spark.catalog.cacheTable("spark_catalog.default.tbl1")
>>> spark.catalog.uncacheTable("tbl1")
>>> _ = spark.sql("DROP TABLE tbl1")

```

# pyspark.sql.Catalog.clearCache — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.clearCache

Catalog.clearCache()
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.clearCache)
[#](#pyspark.sql.Catalog.clearCache "Permalink to this definition")

Removes all cached tables from the in-memory cache.

New in version 2.0.0.

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
>>> spark.catalog.clearCache()
>>> spark.catalog.isCached("tbl1")
False
>>> _ = spark.sql("DROP TABLE tbl1")

```


# pyspark.sql.Catalog.createExternalTable — PySpark 4.0.1 documentation
Catalog.createExternalTable(_tableName_, _path\=None_, _source\=None_, _schema\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.createExternalTable)
[#](#pyspark.sql.Catalog.createExternalTable "Permalink to this definition")

Creates a table based on the dataset in a data source.

It returns the DataFrame associated with the external table.

The data source is specified by the `source` and a set of `options`. If `source` is not specified, the default data source configured by `spark.sql.sources.default` will be used.

Optionally, a schema can be provided as the schema of the returned [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") and created external table.

New in version 2.0.0.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

# pyspark.sql.Catalog.createTable — PySpark 4.0.1 documentation
Catalog.createTable(_tableName_, _path\=None_, _source\=None_, _schema\=None_, _description\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.createTable)
[#](#pyspark.sql.Catalog.createTable "Permalink to this definition")

Creates a table based on the dataset in a data source.

New in version 2.2.0.

Parameters

**tableName**str

name of the table to create.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name.

**path**str, optional

the path in which the data for this table exists. When `path` is specified, an external table is created from the data at the given path. Otherwise a managed table is created.

**source**str, optional

the source of this table such as ‘parquet, ‘orc’, etc. If `source` is not specified, the default data source configured by `spark.sql.sources.default` will be used.

**schema**class:StructType, optional

the schema for this table.

**description**str, optional

the description of this table.

Changed in version 3.1.0: Added the `description` parameter.

**\*\*options**dict, optional

extra options to specify in the table.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

The DataFrame associated with the table.

Examples

Creating a managed table.

```
>>> _ = spark.catalog.createTable("tbl1", schema=spark.range(1).schema, source='parquet')
>>> _ = spark.sql("DROP TABLE tbl1")

```


Creating an external table

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="createTable") as d:
...     _ = spark.catalog.createTable(
...         "tbl2", schema=spark.range(1).schema, path=d, source='parquet')
>>> _ = spark.sql("DROP TABLE tbl2")

```


# pyspark.sql.Catalog.currentCatalog — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.currentCatalog

Catalog.currentCatalog()
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.currentCatalog)
[#](#pyspark.sql.Catalog.currentCatalog "Permalink to this definition")

Returns the current default catalog in this session.

New in version 3.4.0.

Examples

```
>>> spark.catalog.currentCatalog()
'spark_catalog'

```


# pyspark.sql.Catalog.currentDatabase — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.currentDatabase

Catalog.currentDatabase()
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.currentDatabase)
[#](#pyspark.sql.Catalog.currentDatabase "Permalink to this definition")

Returns the current default database in this session.

New in version 2.0.0.

Returns

str

The current default database name.

Examples

```
>>> spark.catalog.currentDatabase()
'default'

```



# pyspark.sql.Catalog.databaseExists — PySpark 4.0.1 documentation
Catalog.databaseExists(_dbName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.databaseExists)
[#](#pyspark.sql.Catalog.databaseExists "Permalink to this definition")

Check if the database with the specified name exists.

New in version 3.3.0.

Parameters

**dbName**str

name of the database to check existence

Changed in version 3.4.0: Allow `dbName` to be qualified with catalog name.

Returns

bool

Indicating whether the database exists

Examples

Check if ‘test\_new\_database’ database exists

```
>>> spark.catalog.databaseExists("test_new_database")
False
>>> _ = spark.sql("CREATE DATABASE test_new_database")
>>> spark.catalog.databaseExists("test_new_database")
True

```


Using the fully qualified name with the catalog name.

```
>>> spark.catalog.databaseExists("spark_catalog.test_new_database")
True
>>> _ = spark.sql("DROP DATABASE test_new_database")

```


# pyspark.sql.Catalog.dropGlobalTempView — PySpark 4.0.1 documentation
Catalog.dropGlobalTempView(_viewName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.dropGlobalTempView)
[#](#pyspark.sql.Catalog.dropGlobalTempView "Permalink to this definition")

Drops the global temporary view with the given view name in the catalog.

New in version 2.1.0.

Parameters

**viewName**str

name of the global view to drop.

Returns

bool

If the global view was successfully dropped or not.

Notes

If the view has been cached before, then it will also be uncached.

Examples

```
>>> spark.createDataFrame([(1, 1)]).createGlobalTempView("my_table")

```


Dropping the global view.

```
>>> spark.catalog.dropGlobalTempView("my_table")
True

```


Throw an exception if the global view does not exists.

```
>>> spark.table("global_temp.my_table")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


# pyspark.sql.Catalog.dropTempView — PySpark 4.0.1 documentation
Catalog.dropTempView(_viewName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.dropTempView)
[#](#pyspark.sql.Catalog.dropTempView "Permalink to this definition")

Drops the local temporary view with the given view name in the catalog. If the view has been cached before, then it will also be uncached. Returns true if this view is dropped successfully, false otherwise.

New in version 2.0.0.

Parameters

**viewName**str

name of the temporary view to drop.

Returns

bool

If the temporary view was successfully dropped or not.

New in version 2.1.0: The return type of this method was `None` in Spark 2.0, but changed to `bool` in Spark 2.1.

Examples

```
>>> spark.createDataFrame([(1, 1)]).createTempView("my_table")

```


Dropping the temporary view.

```
>>> spark.catalog.dropTempView("my_table")
True

```


Throw an exception if the temporary view does not exists.

```
>>> spark.table("my_table")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


# pyspark.sql.Catalog.functionExists — PySpark 4.0.1 documentation
Catalog.functionExists(_functionName_, _dbName\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.functionExists)
[#](#pyspark.sql.Catalog.functionExists "Permalink to this definition")

Check if the function with the specified name exists. This can either be a temporary function or a function.

New in version 3.3.0.

Parameters

**functionName**str

name of the function to check existence

Changed in version 3.4.0: Allow `functionName` to be qualified with catalog name

**dbName**str, optional

name of the database to check function existence in.

Returns

bool

Indicating whether the function exists

Notes

If no database is specified, the current database and catalog are used. This API includes all temporary functions.

Examples

```
>>> spark.catalog.functionExists("count")
True

```


Using the fully qualified name for function name.

```
>>> spark.catalog.functionExists("default.unexisting_function")
False
>>> spark.catalog.functionExists("spark_catalog.default.unexisting_function")
False

```


# pyspark.sql.Catalog.getDatabase — PySpark 4.0.1 documentation
Catalog.getDatabase(_dbName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.getDatabase)
[#](#pyspark.sql.Catalog.getDatabase "Permalink to this definition")

Get the database with the specified name. This throws an `AnalysisException` when the database cannot be found.

New in version 3.4.0.

Parameters

**dbName**str

name of the database to get.

Returns

`Database`

The database found by the name.

Examples

```
>>> spark.catalog.getDatabase("default")
Database(name='default', catalog='spark_catalog', description='default database', ...

```


Using the fully qualified name with the catalog name.

```
>>> spark.catalog.getDatabase("spark_catalog.default")
Database(name='default', catalog='spark_catalog', description='default database', ...

```


# pyspark.sql.Catalog.getFunction — PySpark 4.0.1 documentation
Catalog.getFunction(_functionName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.getFunction)
[#](#pyspark.sql.Catalog.getFunction "Permalink to this definition")

Get the function with the specified name. This function can be a temporary function or a function. This throws an `AnalysisException` when the function cannot be found.

New in version 3.4.0.

Parameters

**functionName**str

name of the function to check existence.

Returns

`Function`

The function found by the name.

Examples

```
>>> _ = spark.sql(
...     "CREATE FUNCTION my_func1 AS 'test.org.apache.spark.sql.MyDoubleAvg'")
>>> spark.catalog.getFunction("my_func1")
Function(name='my_func1', catalog='spark_catalog', namespace=['default'], ...

```


Using the fully qualified name for function name.

```
>>> spark.catalog.getFunction("default.my_func1")
Function(name='my_func1', catalog='spark_catalog', namespace=['default'], ...
>>> spark.catalog.getFunction("spark_catalog.default.my_func1")
Function(name='my_func1', catalog='spark_catalog', namespace=['default'], ...

```


Throw an analysis exception when the function does not exists.

```
>>> spark.catalog.getFunction("my_func2")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


# pyspark.sql.Catalog.getTable — PySpark 4.0.1 documentation
Catalog.getTable(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.getTable)
[#](#pyspark.sql.Catalog.getTable "Permalink to this definition")

Get the table or view with the specified name. This table can be a temporary view or a table/view. This throws an `AnalysisException` when no Table can be found.

New in version 3.4.0.

Parameters

**tableName**str

name of the table to get.

Changed in version 3.4.0: Allow tableName to be qualified with catalog name.

Returns

`Table`

The table found by the name.

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
>>> spark.catalog.getTable("tbl1")
Table(name='tbl1', catalog='spark_catalog', namespace=['default'], ...

```


Using the fully qualified name with the catalog name.

```
>>> spark.catalog.getTable("default.tbl1")
Table(name='tbl1', catalog='spark_catalog', namespace=['default'], ...
>>> spark.catalog.getTable("spark_catalog.default.tbl1")
Table(name='tbl1', catalog='spark_catalog', namespace=['default'], ...
>>> _ = spark.sql("DROP TABLE tbl1")

```


Throw an analysis exception when the table does not exist.

```
>>> spark.catalog.getTable("tbl1")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


# pyspark.sql.Catalog.isCached — PySpark 4.0.1 documentation
Catalog.isCached(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.isCached)
[#](#pyspark.sql.Catalog.isCached "Permalink to this definition")

Returns true if the table is currently cached in-memory.

New in version 2.0.0.

Parameters

**tableName**str

name of the table to get.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name.

Returns

bool

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
>>> spark.catalog.cacheTable("tbl1")
>>> spark.catalog.isCached("tbl1")
True

```


Throw an analysis exception when the table does not exist.

```
>>> spark.catalog.isCached("not_existing_table")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


Using the fully qualified name for the table.

```
>>> spark.catalog.isCached("spark_catalog.default.tbl1")
True
>>> spark.catalog.uncacheTable("tbl1")
>>> _ = spark.sql("DROP TABLE tbl1")

```


# pyspark.sql.Catalog.listCatalogs — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.listCatalogs

Catalog.listCatalogs(_pattern\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.listCatalogs)
[#](#pyspark.sql.Catalog.listCatalogs "Permalink to this definition")

Returns a list of catalogs in this session.

New in version 3.4.0.

Parameters

**pattern**str, optional

The pattern that the catalog name needs to match.

Returns

list

A list of `CatalogMetadata`.

Examples

```
>>> spark.catalog.listCatalogs()
[CatalogMetadata(name='spark_catalog', description=None)]

```


```
>>> spark.catalog.listCatalogs("spark*")
[CatalogMetadata(name='spark_catalog', description=None)]

```


```
>>> spark.catalog.listCatalogs("hive*")
[]

```

# pyspark.sql.Catalog.listColumns — PySpark 4.0.1 documentation
Catalog.listColumns(_tableName_, _dbName\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.listColumns)
[#](#pyspark.sql.Catalog.listColumns "Permalink to this definition")

Returns a list of columns for the given table/view in the specified database.

New in version 2.0.0.

Parameters

**tableName**str

name of the table to list columns.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name when `dbName` is None.

**dbName**str, optional

name of the database to find the table to list columns.

Returns

list

A list of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Notes

The order of arguments here is different from that of its JVM counterpart because Python does not support method overloading.

If no database is specified, the current database and catalog are used. This API includes all temporary views.

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tblA (name STRING, age INT) USING parquet")
>>> spark.catalog.listColumns("tblA")
[Column(name='name', description=None, dataType='string', nullable=True, ...
>>> _ = spark.sql("DROP TABLE tblA")

```



# pyspark.sql.Catalog.listDatabases — PySpark 4.0.1 documentation
Catalog.listDatabases(_pattern\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.listDatabases)
[#](#pyspark.sql.Catalog.listDatabases "Permalink to this definition")

Returns a list of databases available across all sessions.

New in version 2.0.0.

Parameters

**pattern**str, optional

The pattern that the database name needs to match.

Returns

list

A list of `Database`.

Examples

```
>>> spark.catalog.listDatabases()
[Database(name='default', catalog='spark_catalog', description='default database', ...

```


```
>>> spark.catalog.listDatabases("def*")
[Database(name='default', catalog='spark_catalog', description='default database', ...

```


```
>>> spark.catalog.listDatabases("def2*")
[]

```
# pyspark.sql.Catalog.listFunctions — PySpark 4.0.1 documentation
Catalog.listFunctions(_dbName\=None_, _pattern\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.listFunctions)
[#](#pyspark.sql.Catalog.listFunctions "Permalink to this definition")

Returns a list of functions registered in the specified database.

New in version 3.4.0.

Parameters

**dbName**str, optional

name of the database to list the functions. `dbName` can be qualified with catalog name.

**pattern**str, optional

The pattern that the function name needs to match.

Returns

list

A list of `Function`.

Notes

If no database is specified, the current database and catalog are used. This API includes all temporary functions.

Examples

```
>>> spark.catalog.listFunctions()
[Function(name=...

```


```
>>> spark.catalog.listFunctions(pattern="to_*")
[Function(name=...

```


```
>>> spark.catalog.listFunctions(pattern="*not_existing_func*")
[]

```

# pyspark.sql.Catalog.listTables — PySpark 4.0.1 documentation
Catalog.listTables(_dbName\=None_, _pattern\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.listTables)
[#](#pyspark.sql.Catalog.listTables "Permalink to this definition")

Returns a list of tables/views in the specified database.

New in version 2.0.0.

Parameters

**dbName**str, optional

name of the database to list the tables.

Changed in version 3.4.0: Allow `dbName` to be qualified with catalog name.

**pattern**str, optional

The pattern that the database name needs to match.

Returns

list

A list of `Table`.

Notes

If no database is specified, the current database and catalog are used. This API includes all temporary views.

Examples

```
>>> spark.range(1).createTempView("test_view")
>>> spark.catalog.listTables()
[Table(name='test_view', catalog=None, namespace=[], description=None, ...

```


```
>>> spark.catalog.listTables(pattern="test*")
[Table(name='test_view', catalog=None, namespace=[], description=None, ...

```


```
>>> spark.catalog.listTables(pattern="table*")
[]

```


```
>>> _ = spark.catalog.dropTempView("test_view")
>>> spark.catalog.listTables()
[]

```


# pyspark.sql.Catalog.recoverPartitions — PySpark 4.0.1 documentation
Catalog.recoverPartitions(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.recoverPartitions)
[#](#pyspark.sql.Catalog.recoverPartitions "Permalink to this definition")

Recovers all the partitions of the given table and updates the catalog.

New in version 2.1.1.

Parameters

**tableName**str

name of the table to get.

Notes

Only works with a partitioned table, and not a view.

Examples

The example below creates a partitioned table against the existing directory of the partitioned table. After that, it recovers the partitions.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="recoverPartitions") as d:
...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
...     spark.range(1).selectExpr(
...         "id as key", "id as value").write.partitionBy("key").mode("overwrite").save(d)
...     _ = spark.sql(
...          "CREATE TABLE tbl1 (key LONG, value LONG)"
...          "USING parquet OPTIONS (path '{}') PARTITIONED BY (key)".format(d))
...     spark.table("tbl1").show()
...     spark.catalog.recoverPartitions("tbl1")
...     spark.table("tbl1").show()
+-----+---+
|value|key|
+-----+---+
+-----+---+
+-----+---+
|value|key|
+-----+---+
|    0|  0|
+-----+---+
>>> _ = spark.sql("DROP TABLE tbl1")

```



# pyspark.sql.Catalog.refreshByPath — PySpark 4.0.1 documentation
Catalog.refreshByPath(_path_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.refreshByPath)
[#](#pyspark.sql.Catalog.refreshByPath "Permalink to this definition")

Invalidates and refreshes all the cached data (and the associated metadata) for any DataFrame that contains the given data source path.

New in version 2.2.0.

Parameters

**path**str

the path to refresh the cache.

Examples

The example below caches a table, and then removes the data.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="refreshByPath") as d:
...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
...     _ = spark.sql(
...         "CREATE TABLE tbl1 (col STRING) USING TEXT LOCATION '{}'".format(d))
...     _ = spark.sql("INSERT INTO tbl1 SELECT 'abc'")
...     spark.catalog.cacheTable("tbl1")
...     spark.table("tbl1").show()
+---+
|col|
+---+
|abc|
+---+

```


Because the table is cached, it computes from the cached data as below.

```
>>> spark.table("tbl1").count()
1

```


After refreshing the table by path, it shows 0 because the data does not exist anymore.

```
>>> spark.catalog.refreshByPath(d)
>>> spark.table("tbl1").count()
0

```


```
>>> _ = spark.sql("DROP TABLE tbl1")

```


# pyspark.sql.Catalog.recoverPartitions — PySpark 4.0.1 documentation
Catalog.recoverPartitions(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.recoverPartitions)
[#](#pyspark.sql.Catalog.recoverPartitions "Permalink to this definition")

Recovers all the partitions of the given table and updates the catalog.

New in version 2.1.1.

Parameters

**tableName**str

name of the table to get.

Notes

Only works with a partitioned table, and not a view.

Examples

The example below creates a partitioned table against the existing directory of the partitioned table. After that, it recovers the partitions.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="recoverPartitions") as d:
...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
...     spark.range(1).selectExpr(
...         "id as key", "id as value").write.partitionBy("key").mode("overwrite").save(d)
...     _ = spark.sql(
...          "CREATE TABLE tbl1 (key LONG, value LONG)"
...          "USING parquet OPTIONS (path '{}') PARTITIONED BY (key)".format(d))
...     spark.table("tbl1").show()
...     spark.catalog.recoverPartitions("tbl1")
...     spark.table("tbl1").show()
+-----+---+
|value|key|
+-----+---+
+-----+---+
+-----+---+
|value|key|
+-----+---+
|    0|  0|
+-----+---+
>>> _ = spark.sql("DROP TABLE tbl1")

```


# pyspark.sql.Catalog.refreshTable — PySpark 4.0.1 documentation
Catalog.refreshTable(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.refreshTable)
[#](#pyspark.sql.Catalog.refreshTable "Permalink to this definition")

Invalidates and refreshes all the cached data and metadata of the given table.

New in version 2.0.0.

Parameters

**tableName**str

name of the table to get.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name.

Examples

The example below caches a table, and then removes the data.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="refreshTable") as d:
...     _ = spark.sql("DROP TABLE IF EXISTS tbl1")
...     _ = spark.sql(
...         "CREATE TABLE tbl1 (col STRING) USING TEXT LOCATION '{}'".format(d))
...     _ = spark.sql("INSERT INTO tbl1 SELECT 'abc'")
...     spark.catalog.cacheTable("tbl1")
...     spark.table("tbl1").show()
+---+
|col|
+---+
|abc|
+---+

```


Because the table is cached, it computes from the cached data as below.

```
>>> spark.table("tbl1").count()
1

```


After refreshing the table, it shows 0 because the data does not exist anymore.

```
>>> spark.catalog.refreshTable("tbl1")
>>> spark.table("tbl1").count()
0

```


Using the fully qualified name for the table.

```
>>> spark.catalog.refreshTable("spark_catalog.default.tbl1")
>>> _ = spark.sql("DROP TABLE tbl1")

```


# pyspark.sql.Catalog.registerFunction — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.registerFunction

Catalog.registerFunction(_name_, _f_, _returnType\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.registerFunction)
[#](#pyspark.sql.Catalog.registerFunction "Permalink to this definition")

An alias for `spark.udf.register()`. See [`pyspark.sql.UDFRegistration.register()`](about:blank/pyspark.sql.UDFRegistration.register.html#pyspark.sql.UDFRegistration.register "pyspark.sql.UDFRegistration.register").

New in version 2.0.0.

Deprecated since version 2.3.0: Use `spark.udf.register()` instead.

Changed in version 3.4.0: Supports Spark Connect.

# pyspark.sql.Catalog.setCurrentCatalog — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.setCurrentCatalog

Catalog.setCurrentCatalog(_catalogName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.setCurrentCatalog)
[#](#pyspark.sql.Catalog.setCurrentCatalog "Permalink to this definition")

Sets the current default catalog in this session.

New in version 3.4.0.

Parameters

**catalogName**str

name of the catalog to set

Examples

```
>>> spark.catalog.setCurrentCatalog("spark_catalog")

```


# pyspark.sql.Catalog.setCurrentDatabase — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Catalog](../catalog.html)
*   pyspark.sql.Catalog.setCurrentDatabase

Catalog.setCurrentDatabase(_dbName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.setCurrentDatabase)
[#](#pyspark.sql.Catalog.setCurrentDatabase "Permalink to this definition")

Sets the current default database in this session.

New in version 2.0.0.

Examples

```
>>> spark.catalog.setCurrentDatabase("default")

```


# pyspark.sql.Catalog.tableExists — PySpark 4.0.1 documentation
Catalog.tableExists(_tableName_, _dbName\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.tableExists)
[#](#pyspark.sql.Catalog.tableExists "Permalink to this definition")

Check if the table or view with the specified name exists. This can either be a temporary view or a table/view.

New in version 3.3.0.

Parameters

**tableName**str

name of the table to check existence. If no database is specified, first try to treat `tableName` as a multi-layer-namespace identifier, then try `tableName` as a normal table name in the current database if necessary.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name when `dbName` is None.

**dbName**str, optional

name of the database to check table existence in.

Returns

bool

Indicating whether the table/view exists

Examples

This function can check if a table is defined or not:

```
>>> spark.catalog.tableExists("unexisting_table")
False
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
>>> spark.catalog.tableExists("tbl1")
True

```


Using the fully qualified names for tables.

```
>>> spark.catalog.tableExists("default.tbl1")
True
>>> spark.catalog.tableExists("spark_catalog.default.tbl1")
True
>>> spark.catalog.tableExists("tbl1", "default")
True
>>> _ = spark.sql("DROP TABLE tbl1")

```


Check if views exist:

```
>>> spark.catalog.tableExists("view1")
False
>>> _ = spark.sql("CREATE VIEW view1 AS SELECT 1")
>>> spark.catalog.tableExists("view1")
True

```


Using the fully qualified names for views.

```
>>> spark.catalog.tableExists("default.view1")
True
>>> spark.catalog.tableExists("spark_catalog.default.view1")
True
>>> spark.catalog.tableExists("view1", "default")
True
>>> _ = spark.sql("DROP VIEW view1")

```


Check if temporary views exist:

```
>>> _ = spark.sql("CREATE TEMPORARY VIEW view1 AS SELECT 1")
>>> spark.catalog.tableExists("view1")
True
>>> df = spark.sql("DROP VIEW view1")
>>> spark.catalog.tableExists("view1")
False

```


# pyspark.sql.Catalog.uncacheTable — PySpark 4.0.1 documentation
Catalog.uncacheTable(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/catalog.html#Catalog.uncacheTable)
[#](#pyspark.sql.Catalog.uncacheTable "Permalink to this definition")

Removes the specified table from the in-memory cache.

New in version 2.0.0.

Parameters

**tableName**str

name of the table to get.

Changed in version 3.4.0: Allow `tableName` to be qualified with catalog name.

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tbl1")
>>> _ = spark.sql("CREATE TABLE tbl1 (name STRING, age INT) USING parquet")
>>> spark.catalog.cacheTable("tbl1")
>>> spark.catalog.uncacheTable("tbl1")
>>> spark.catalog.isCached("tbl1")
False

```


Throw an analysis exception when the table does not exist.

```
>>> spark.catalog.uncacheTable("not_existing_table")
Traceback (most recent call last):
    ...
AnalysisException: ...

```


Using the fully qualified name for the table.

```
>>> spark.catalog.uncacheTable("spark_catalog.default.tbl1")
>>> spark.catalog.isCached("tbl1")
False
>>> _ = spark.sql("DROP TABLE tbl1")

```
