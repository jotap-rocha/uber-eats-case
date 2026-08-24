# DataFrame — PySpark 4.0.1 documentation


* DataFrame.__getattr__(name): DataFrame.__getitem__(item)
  * Returns the Column denoted by name.: Returns the column as a Column.
* DataFrame.__getattr__(name): DataFrame.agg(*exprs)
  * Returns the Column denoted by name.: Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).
* DataFrame.__getattr__(name): DataFrame.alias(alias)
  * Returns the Column denoted by name.: Returns a new DataFrame with an alias set.
* DataFrame.__getattr__(name): DataFrame.approxQuantile(col, probabilities, ...)
  * Returns the Column denoted by name.: Calculates the approximate quantiles of numerical columns of a DataFrame.
* DataFrame.__getattr__(name): DataFrame.asTable()
  * Returns the Column denoted by name.: Converts the DataFrame into a table_arg.TableArg object, which can be used as a table argument in a TVF(Table-Valued Function) including UDTF (User-Defined Table Function).
* DataFrame.__getattr__(name): DataFrame.cache()
  * Returns the Column denoted by name.: Persists the DataFrame with the default storage level (MEMORY_AND_DISK_DESER).
* DataFrame.__getattr__(name): DataFrame.checkpoint([eager])
  * Returns the Column denoted by name.: Returns a checkpointed version of this DataFrame.
* DataFrame.__getattr__(name): DataFrame.coalesce(numPartitions)
  * Returns the Column denoted by name.: Returns a new DataFrame that has exactly numPartitions partitions.
* DataFrame.__getattr__(name): DataFrame.colRegex(colName)
  * Returns the Column denoted by name.: Selects column based on the column name specified as a regex and returns it as Column.
* DataFrame.__getattr__(name): DataFrame.collect()
  * Returns the Column denoted by name.: Returns all the records in the DataFrame as a list of Row.
* DataFrame.__getattr__(name): DataFrame.columns
  * Returns the Column denoted by name.: Retrieves the names of all columns in the DataFrame as a list.
* DataFrame.__getattr__(name): DataFrame.corr(col1, col2[, method])
  * Returns the Column denoted by name.: Calculates the correlation of two columns of a DataFrame as a double value.
* DataFrame.__getattr__(name): DataFrame.count()
  * Returns the Column denoted by name.: Returns the number of rows in this DataFrame.
* DataFrame.__getattr__(name): DataFrame.cov(col1, col2)
  * Returns the Column denoted by name.: Calculate the sample covariance for the given columns, specified by their names, as a double value.
* DataFrame.__getattr__(name): DataFrame.createGlobalTempView(name)
  * Returns the Column denoted by name.: Creates a global temporary view with this DataFrame.
* DataFrame.__getattr__(name): DataFrame.createOrReplaceGlobalTempView(name)
  * Returns the Column denoted by name.: Creates or replaces a global temporary view using the given name.
* DataFrame.__getattr__(name): DataFrame.createOrReplaceTempView(name)
  * Returns the Column denoted by name.: Creates or replaces a local temporary view with this DataFrame.
* DataFrame.__getattr__(name): DataFrame.createTempView(name)
  * Returns the Column denoted by name.: Creates a local temporary view with this DataFrame.
* DataFrame.__getattr__(name): DataFrame.crossJoin(other)
  * Returns the Column denoted by name.: Returns the cartesian product with another DataFrame.
* DataFrame.__getattr__(name): DataFrame.crosstab(col1, col2)
  * Returns the Column denoted by name.: Computes a pair-wise frequency table of the given columns.
* DataFrame.__getattr__(name): DataFrame.cube(*cols)
  * Returns the Column denoted by name.: Create a multi-dimensional cube for the current DataFrame using the specified columns, allowing aggregations to be performed on them.
* DataFrame.__getattr__(name): DataFrame.describe(*cols)
  * Returns the Column denoted by name.: Computes basic statistics for numeric and string columns.
* DataFrame.__getattr__(name): DataFrame.distinct()
  * Returns the Column denoted by name.: Returns a new DataFrame containing the distinct rows in this DataFrame.
* DataFrame.__getattr__(name): DataFrame.drop(*cols)
  * Returns the Column denoted by name.: Returns a new DataFrame without specified columns.
* DataFrame.__getattr__(name): DataFrame.dropDuplicates([subset])
  * Returns the Column denoted by name.: Return a new DataFrame with duplicate rows removed, optionally only considering certain columns.
* DataFrame.__getattr__(name): DataFrame.dropDuplicatesWithinWatermark([subset])
  * Returns the Column denoted by name.: Return a new DataFrame with duplicate rows removed,
* DataFrame.__getattr__(name): DataFrame.drop_duplicates([subset])
  * Returns the Column denoted by name.: drop_duplicates() is an alias for dropDuplicates().
* DataFrame.__getattr__(name): DataFrame.dropna([how, thresh, subset])
  * Returns the Column denoted by name.: Returns a new DataFrame omitting rows with null or NaN values.
* DataFrame.__getattr__(name): DataFrame.dtypes
  * Returns the Column denoted by name.: Returns all column names and their data types as a list.
* DataFrame.__getattr__(name): DataFrame.exceptAll(other)
  * Returns the Column denoted by name.: Return a new DataFrame containing rows in this DataFrame but not in another DataFrame while preserving duplicates.
* DataFrame.__getattr__(name): DataFrame.executionInfo
  * Returns the Column denoted by name.: Returns a ExecutionInfo object after the query was executed.
* DataFrame.__getattr__(name): DataFrame.exists()
  * Returns the Column denoted by name.: Return a Column object for an EXISTS Subquery.
* DataFrame.__getattr__(name): DataFrame.explain([extended, mode])
  * Returns the Column denoted by name.: Prints the (logical and physical) plans to the console for debugging purposes.
* DataFrame.__getattr__(name): DataFrame.fillna(value[, subset])
  * Returns the Column denoted by name.: Returns a new DataFrame which null values are filled with new value.
* DataFrame.__getattr__(name): DataFrame.filter(condition)
  * Returns the Column denoted by name.: Filters rows using the given condition.
* DataFrame.__getattr__(name): DataFrame.first()
  * Returns the Column denoted by name.: Returns the first row as a Row.
* DataFrame.__getattr__(name): DataFrame.foreach(f)
  * Returns the Column denoted by name.: Applies the f function to all Row of this DataFrame.
* DataFrame.__getattr__(name): DataFrame.foreachPartition(f)
  * Returns the Column denoted by name.: Applies the f function to each partition of this DataFrame.
* DataFrame.__getattr__(name): DataFrame.freqItems(cols[, support])
  * Returns the Column denoted by name.: Finding frequent items for columns, possibly with false positives.
* DataFrame.__getattr__(name): DataFrame.groupBy(*cols)
  * Returns the Column denoted by name.: Groups the DataFrame by the specified columns so that aggregation can be performed on them.
* DataFrame.__getattr__(name): DataFrame.groupingSets(groupingSets, *cols)
  * Returns the Column denoted by name.: Create multi-dimensional aggregation for the current DataFrame using the specified grouping sets, so we can run aggregation on them.
* DataFrame.__getattr__(name): DataFrame.head([n])
  * Returns the Column denoted by name.: Returns the first n rows.
* DataFrame.__getattr__(name): DataFrame.hint(name, *parameters)
  * Returns the Column denoted by name.: Specifies some hint on the current DataFrame.
* DataFrame.__getattr__(name): DataFrame.inputFiles()
  * Returns the Column denoted by name.: Returns a best-effort snapshot of the files that compose this DataFrame.
* DataFrame.__getattr__(name): DataFrame.intersect(other)
  * Returns the Column denoted by name.: Return a new DataFrame containing rows only in both this DataFrame and another DataFrame.
* DataFrame.__getattr__(name): DataFrame.intersectAll(other)
  * Returns the Column denoted by name.: Return a new DataFrame containing rows in both this DataFrame and another DataFrame while preserving duplicates.
* DataFrame.__getattr__(name): DataFrame.isEmpty()
  * Returns the Column denoted by name.: Checks if the DataFrame is empty and returns a boolean value.
* DataFrame.__getattr__(name): DataFrame.isLocal()
  * Returns the Column denoted by name.: Returns True if the collect() and take() methods can be run locally (without any Spark executors).
* DataFrame.__getattr__(name): DataFrame.isStreaming
  * Returns the Column denoted by name.: Returns True if this DataFrame contains one or more sources that continuously return data as it arrives.
* DataFrame.__getattr__(name): DataFrame.join(other[, on, how])
  * Returns the Column denoted by name.: Joins with another DataFrame, using the given join expression.
* DataFrame.__getattr__(name): DataFrame.limit(num)
  * Returns the Column denoted by name.: Limits the result count to the number specified.
* DataFrame.__getattr__(name): DataFrame.lateralJoin(other[, on, how])
  * Returns the Column denoted by name.: Lateral joins with another DataFrame, using the given join expression.
* DataFrame.__getattr__(name): DataFrame.localCheckpoint([eager, storageLevel])
  * Returns the Column denoted by name.: Returns a locally checkpointed version of this DataFrame.
* DataFrame.__getattr__(name): DataFrame.mapInPandas(func, schema[, ...])
  * Returns the Column denoted by name.: Maps an iterator of batches in the current DataFrame using a Python native function that is performed on pandas DataFrames both as input and output, and returns the result as a DataFrame.
* DataFrame.__getattr__(name): DataFrame.mapInArrow(func, schema[, ...])
  * Returns the Column denoted by name.: Maps an iterator of batches in the current DataFrame using a Python native function that is performed on pyarrow.RecordBatchs both as input and output, and returns the result as a DataFrame.
* DataFrame.__getattr__(name): DataFrame.metadataColumn(colName)
  * Returns the Column denoted by name.: Selects a metadata column based on its logical column name and returns it as a Column.
* DataFrame.__getattr__(name): DataFrame.melt(ids, values, ...)
  * Returns the Column denoted by name.: Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
* DataFrame.__getattr__(name): DataFrame.na
  * Returns the Column denoted by name.: Returns a DataFrameNaFunctions for handling missing values.
* DataFrame.__getattr__(name): DataFrame.observe(observation, *exprs)
  * Returns the Column denoted by name.: Define (named) metrics to observe on the DataFrame.
* DataFrame.__getattr__(name): DataFrame.offset(num)
  * Returns the Column denoted by name.: Returns a new :class: DataFrame by skipping the first n rows.
* DataFrame.__getattr__(name): DataFrame.orderBy(*cols, **kwargs)
  * Returns the Column denoted by name.: Returns a new DataFrame sorted by the specified column(s).
* DataFrame.__getattr__(name): DataFrame.persist([storageLevel])
  * Returns the Column denoted by name.: Sets the storage level to persist the contents of the DataFrame across operations after the first time it is computed.
* DataFrame.__getattr__(name): DataFrame.plot
  * Returns the Column denoted by name.: Returns a plot.core.PySparkPlotAccessor for plotting functions.
* DataFrame.__getattr__(name): DataFrame.printSchema([level])
  * Returns the Column denoted by name.: Prints out the schema in the tree format.
* DataFrame.__getattr__(name): DataFrame.randomSplit(weights[, seed])
  * Returns the Column denoted by name.: Randomly splits this DataFrame with the provided weights.
* DataFrame.__getattr__(name): DataFrame.rdd
  * Returns the Column denoted by name.: Returns the content as an pyspark.RDD of Row.
* DataFrame.__getattr__(name): DataFrame.registerTempTable(name)
  * Returns the Column denoted by name.: Registers this DataFrame as a temporary table using the given name.
* DataFrame.__getattr__(name): DataFrame.repartition(numPartitions, *cols)
  * Returns the Column denoted by name.: Returns a new DataFrame partitioned by the given partitioning expressions.
* DataFrame.__getattr__(name): DataFrame.repartitionByRange(numPartitions, ...)
  * Returns the Column denoted by name.: Returns a new DataFrame partitioned by the given partitioning expressions.
* DataFrame.__getattr__(name): DataFrame.replace(to_replace[, value, subset])
  * Returns the Column denoted by name.: Returns a new DataFrame replacing a value with another value.
* DataFrame.__getattr__(name): DataFrame.rollup(*cols)
  * Returns the Column denoted by name.: Create a multi-dimensional rollup for the current DataFrame using the specified columns, allowing for aggregation on them.
* DataFrame.__getattr__(name): DataFrame.sameSemantics(other)
  * Returns the Column denoted by name.: Returns True when the logical query plans inside both DataFrames are equal and therefore return the same results.
* DataFrame.__getattr__(name): DataFrame.sample([withReplacement, ...])
  * Returns the Column denoted by name.: Returns a sampled subset of this DataFrame.
* DataFrame.__getattr__(name): DataFrame.sampleBy(col, fractions[, seed])
  * Returns the Column denoted by name.: Returns a stratified sample without replacement based on the fraction given on each stratum.
* DataFrame.__getattr__(name): DataFrame.scalar()
  * Returns the Column denoted by name.: Return a Column object for a SCALAR Subquery containing exactly one row and one column.
* DataFrame.__getattr__(name): DataFrame.schema
  * Returns the Column denoted by name.: Returns the schema of this DataFrame as a pyspark.sql.types.StructType.
* DataFrame.__getattr__(name): DataFrame.select(*cols)
  * Returns the Column denoted by name.: Projects a set of expressions and returns a new DataFrame.
* DataFrame.__getattr__(name): DataFrame.selectExpr(*expr)
  * Returns the Column denoted by name.: Projects a set of SQL expressions and returns a new DataFrame.
* DataFrame.__getattr__(name): DataFrame.semanticHash()
  * Returns the Column denoted by name.: Returns a hash code of the logical query plan against this DataFrame.
* DataFrame.__getattr__(name): DataFrame.show([n, truncate, vertical])
  * Returns the Column denoted by name.: Prints the first n rows of the DataFrame to the console.
* DataFrame.__getattr__(name): DataFrame.sort(*cols, **kwargs)
  * Returns the Column denoted by name.: Returns a new DataFrame sorted by the specified column(s).
* DataFrame.__getattr__(name): DataFrame.sortWithinPartitions(*cols, **kwargs)
  * Returns the Column denoted by name.: Returns a new DataFrame with each partition sorted by the specified column(s).
* DataFrame.__getattr__(name): DataFrame.sparkSession
  * Returns the Column denoted by name.: Returns Spark session that created this DataFrame.
* DataFrame.__getattr__(name): DataFrame.stat
  * Returns the Column denoted by name.: Returns a DataFrameStatFunctions for statistic functions.
* DataFrame.__getattr__(name): DataFrame.storageLevel
  * Returns the Column denoted by name.: Get the DataFrame's current storage level.
* DataFrame.__getattr__(name): DataFrame.subtract(other)
  * Returns the Column denoted by name.: Return a new DataFrame containing rows in this DataFrame but not in another DataFrame.
* DataFrame.__getattr__(name): DataFrame.summary(*statistics)
  * Returns the Column denoted by name.: Computes specified statistics for numeric and string columns.
* DataFrame.__getattr__(name): DataFrame.tail(num)
  * Returns the Column denoted by name.: Returns the last num rows as a list of Row.
* DataFrame.__getattr__(name): DataFrame.take(num)
  * Returns the Column denoted by name.: Returns the first num rows as a list of Row.
* DataFrame.__getattr__(name): DataFrame.to(schema)
  * Returns the Column denoted by name.: Returns a new DataFrame where each row is reconciled to match the specified schema.
* DataFrame.__getattr__(name): DataFrame.toArrow()
  * Returns the Column denoted by name.: Returns the contents of this DataFrame as PyArrow pyarrow.Table.
* DataFrame.__getattr__(name): DataFrame.toDF(*cols)
  * Returns the Column denoted by name.: Returns a new DataFrame that with new specified column names
* DataFrame.__getattr__(name): DataFrame.toJSON([use_unicode])
  * Returns the Column denoted by name.: Converts a DataFrame into a RDD of string.
* DataFrame.__getattr__(name): DataFrame.toLocalIterator([prefetchPartitions])
  * Returns the Column denoted by name.: Returns an iterator that contains all of the rows in this DataFrame.
* DataFrame.__getattr__(name): DataFrame.toPandas()
  * Returns the Column denoted by name.: Returns the contents of this DataFrame as Pandas pandas.DataFrame.
* DataFrame.__getattr__(name): DataFrame.transform(func, *args, **kwargs)
  * Returns the Column denoted by name.: Returns a new DataFrame.
* DataFrame.__getattr__(name): DataFrame.transpose([indexColumn])
  * Returns the Column denoted by name.: Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame.
* DataFrame.__getattr__(name): DataFrame.union(other)
  * Returns the Column denoted by name.: Return a new DataFrame containing the union of rows in this and another DataFrame.
* DataFrame.__getattr__(name): DataFrame.unionAll(other)
  * Returns the Column denoted by name.: Return a new DataFrame containing the union of rows in this and another DataFrame.
* DataFrame.__getattr__(name): DataFrame.unionByName(other[, ...])
  * Returns the Column denoted by name.: Returns a new DataFrame containing union of rows in this and another DataFrame.
* DataFrame.__getattr__(name): DataFrame.unpersist([blocking])
  * Returns the Column denoted by name.: Marks the DataFrame as non-persistent, and remove all blocks for it from memory and disk.
* DataFrame.__getattr__(name): DataFrame.unpivot(ids, values, ...)
  * Returns the Column denoted by name.: Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set.
* DataFrame.__getattr__(name): DataFrame.where(condition)
  * Returns the Column denoted by name.: where() is an alias for filter().
* DataFrame.__getattr__(name): DataFrame.withColumn(colName, col)
  * Returns the Column denoted by name.: Returns a new DataFrame by adding a column or replacing the existing column that has the same name.
* DataFrame.__getattr__(name): DataFrame.withColumns(*colsMap)
  * Returns the Column denoted by name.: Returns a new DataFrame by adding multiple columns or replacing the existing columns that have the same names.
* DataFrame.__getattr__(name): DataFrame.withColumnRenamed(existing, new)
  * Returns the Column denoted by name.: Returns a new DataFrame by renaming an existing column.
* DataFrame.__getattr__(name): DataFrame.withColumnsRenamed(colsMap)
  * Returns the Column denoted by name.: Returns a new DataFrame by renaming multiple columns.
* DataFrame.__getattr__(name): DataFrame.withMetadata(columnName, metadata)
  * Returns the Column denoted by name.: Returns a new DataFrame by updating an existing column with metadata.
* DataFrame.__getattr__(name): DataFrame.withWatermark(eventTime, ...)
  * Returns the Column denoted by name.: Defines an event time watermark for this DataFrame.
* DataFrame.__getattr__(name): DataFrame.write
  * Returns the Column denoted by name.: Interface for saving the content of the non-streaming DataFrame out into external storage.
* DataFrame.__getattr__(name): DataFrame.writeStream
  * Returns the Column denoted by name.: Interface for saving the content of the streaming DataFrame out into external storage.
* DataFrame.__getattr__(name): DataFrame.writeTo(table)
  * Returns the Column denoted by name.: Create a write configuration builder for v2 sources.
* DataFrame.__getattr__(name): DataFrame.mergeInto(table, condition)
  * Returns the Column denoted by name.: Merges a set of updates, insertions, and deletions based on a source table into a target table.
* DataFrame.__getattr__(name): DataFrame.pandas_api([index_col])
  * Returns the Column denoted by name.: Converts the existing DataFrame into a pandas-on-Spark DataFrame.
* DataFrame.__getattr__(name): DataFrameNaFunctions.drop([how, thresh, subset])
  * Returns the Column denoted by name.: Returns a new DataFrame omitting rows with null or NaN values.
* DataFrame.__getattr__(name): DataFrameNaFunctions.fill(value[, subset])
  * Returns the Column denoted by name.: Returns a new DataFrame which null values are filled with new value.
* DataFrame.__getattr__(name): DataFrameNaFunctions.replace(to_replace[, ...])
  * Returns the Column denoted by name.: Returns a new DataFrame replacing a value with another value.
* DataFrame.__getattr__(name): DataFrameStatFunctions.approxQuantile(col, ...)
  * Returns the Column denoted by name.: Calculates the approximate quantiles of numerical columns of a DataFrame.
* DataFrame.__getattr__(name): DataFrameStatFunctions.corr(col1, col2[, method])
  * Returns the Column denoted by name.: Calculates the correlation of two columns of a DataFrame as a double value.
* DataFrame.__getattr__(name): DataFrameStatFunctions.cov(col1, col2)
  * Returns the Column denoted by name.: Calculate the sample covariance for the given columns, specified by their names, as a double value.
* DataFrame.__getattr__(name): DataFrameStatFunctions.crosstab(col1, col2)
  * Returns the Column denoted by name.: Computes a pair-wise frequency table of the given columns.
* DataFrame.__getattr__(name): DataFrameStatFunctions.freqItems(cols[, support])
  * Returns the Column denoted by name.: Finding frequent items for columns, possibly with false positives.
* DataFrame.__getattr__(name): DataFrameStatFunctions.sampleBy(col, fractions)
  * Returns the Column denoted by name.: Returns a stratified sample without replacement based on the fraction given on each stratum.


Table Argument[#](#table-argument "Permalink to this headline")
---------------------------------------------------------------

`DataFrame.asTable` returns a table argument in PySpark.

This class provides methods to specify partitioning, ordering, and single-partition constraints when passing a DataFrame as a table argument to TVF(Table-Valued Function)s including UDTF(User-Defined Table Function)s.


|TableArg.partitionBy(*cols)   |Partitions the data based on the specified columns.            |
|------------------------------|---------------------------------------------------------------|
|TableArg.orderBy(*cols)       |Orders the data within each partition by the specified columns.|
|TableArg.withSinglePartition()|Forces the data to be processed in a single partition.         |


Plotting[#](#plotting "Permalink to this headline")
---------------------------------------------------

The `DataFrame.plot` attribute serves both as a callable method and a namespace, providing access to various plotting functions via the `PySparkPlotAccessor`. Users can call specific plotting methods in the format `DataFrame.plot.<kind>`.



* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.bar(x, y, **kwargs)
  * Draw a stacked area plot.: Vertical bar plot.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.barh(x, y, **kwargs)
  * Draw a stacked area plot.: Make a horizontal bar plot.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.line(x, y, **kwargs)
  * Draw a stacked area plot.: Plot DataFrame as lines.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.pie(x, y, **kwargs)
  * Draw a stacked area plot.: Generate a pie plot.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.scatter(x, y, **kwargs)
  * Draw a stacked area plot.: Create a scatter plot with varying marker point size and color.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.box([column])
  * Draw a stacked area plot.: Make a box plot of the DataFrame columns.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.kde(bw_method[, column, ind])
  * Draw a stacked area plot.: Generate Kernel Density Estimate plot using Gaussian kernels.
* PySparkPlotAccessor.area(x, y, **kwargs): PySparkPlotAccessor.hist([column, bins])
  * Draw a stacked area plot.: Draw one histogram of the DataFrame’s columns.


# pyspark.sql.DataFrame.__getattr__ — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.\_\_getattr\_\_

DataFrame.\_\_getattr\_\_(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.__getattr__)
[#](#pyspark.sql.DataFrame.__getattr__ "Permalink to this definition")

Returns the [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") denoted by `name`.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

Column name to return as [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Requested column.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Retrieve a column instance.

```
>>> df.select(df.age).show()
+---+
|age|
+---+
|  2|
|  5|
+---+

```


# pyspark.sql.DataFrame.__getitem__ — PySpark 4.0.1 documentation
DataFrame.\_\_getitem\_\_(_item_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.__getitem__)
[#](#pyspark.sql.DataFrame.__getitem__ "Permalink to this definition")

Returns the column as a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**item**int, str, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), list or tuple

column index, column name, column, or a list or tuple of columns

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

a specified column, or a filtered or projected dataframe.

*   If the input item is an int or str, the output is a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").
    
*   If the input item is a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), the output is a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")
    
    filtered by this given [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").
    
*   If the input item is a list or tuple, the output is a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")
    
    projected by this given list or tuple.
    

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Retrieve a column instance.

```
>>> df.select(df['age']).show()
+---+
|age|
+---+
|  2|
|  5|
+---+

```


```
>>> df.select(df[1]).show()
+-----+
| name|
+-----+
|Alice|
|  Bob|
+-----+

```


Select multiple string columns as index.

```
>>> df[["name", "age"]].show()
+-----+---+
| name|age|
+-----+---+
|Alice|  2|
|  Bob|  5|
+-----+---+
>>> df[df.age > 3].show()
+---+----+
|age|name|
+---+----+
|  5| Bob|
+---+----+
>>> df[df[0] > 3].show()
+---+----+
|age|name|
+---+----+
|  5| Bob|
+---+----+

```


# pyspark.sql.DataFrame.agg — PySpark 4.0.1 documentation
DataFrame.agg(_\*exprs_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.agg)
[#](#pyspark.sql.DataFrame.agg "Permalink to this definition")

Aggregate on the entire [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") without groups (shorthand for `df.groupBy().agg()`).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**exprs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or dict of key and value strings

Columns or expressions to aggregate DataFrame by.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Aggregated DataFrame.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.agg({"age": "max"}).show()
+--------+
|max(age)|
+--------+
|       5|
+--------+
>>> df.agg(sf.min(df.age)).show()
+--------+
|min(age)|
+--------+
|       2|
+--------+

```


# pyspark.sql.DataFrame.alias — PySpark 4.0.1 documentation
DataFrame.alias(_alias_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.alias)
[#](#pyspark.sql.DataFrame.alias "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with an alias set.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**alias**str

an alias name to be set for the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Aliased DataFrame.

Examples

```
>>> from pyspark.sql.functions import col, desc
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df_as1 = df.alias("df_as1")
>>> df_as2 = df.alias("df_as2")
>>> joined_df = df_as1.join(df_as2, col("df_as1.name") == col("df_as2.name"), 'inner')
>>> joined_df.select(
...     "df_as1.name", "df_as2.name", "df_as2.age").sort(desc("df_as1.name")).show()
+-----+-----+---+
| name| name|age|
+-----+-----+---+
|  Tom|  Tom| 14|
|  Bob|  Bob| 16|
|Alice|Alice| 23|
+-----+-----+---+

```

# pyspark.sql.DataFrame.approxQuantile — PySpark 4.0.1 documentation
DataFrame.approxQuantile(_col_, _probabilities_, _relativeError_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.approxQuantile)
[#](#pyspark.sql.DataFrame.approxQuantile "Permalink to this definition")

Calculates the approximate quantiles of numerical columns of a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The result of this algorithm has the following deterministic bound: If the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") has N elements and if we request the quantile at probability p up to error err, then the algorithm will return a sample x from the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") so that the _exact_ rank of x is close to (p \* N). More precisely,

> floor((p - err) \* N) <= rank(x) <= ceil((p + err) \* N).

This method implements a variation of the Greenwald-Khanna algorithm (with some speed optimizations). The algorithm was first present in \[\[[https://doi.org/10.1145/375663.375670](https://doi.org/10.1145/375663.375670) Space-efficient Online Computation of Quantile Summaries\]\] by Greenwald and Khanna.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col: str, tuple or list**

Can be a single column name, or a list of names for multiple columns.

Changed in version 2.2.0: Added support for multiple columns.

**probabilities**list or tuple of floats

a list of quantile probabilities Each number must be a float in the range \[0, 1\]. For example 0.0 is the minimum, 0.5 is the median, 1.0 is the maximum.

**relativeError**float

The relative target precision to achieve (>= 0). If set to zero, the exact quantiles are computed, which could be very expensive. Note that values greater than 1 are accepted but gives the same result as 1.

Returns

list

the approximate quantiles at the given probabilities.

*   If the input col is a string, the output is a list of floats.
    
*   If the input col is a list or tuple of strings, the output is also a
    
    list, but each element in it is a list of floats, i.e., the output is a list of list of floats.
    

Notes

Null values will be ignored in numerical columns before calculation. For columns only containing null values, an empty list is returned.

Examples

Example 1: Calculating quantiles for a single column

```
>>> data = [(1,), (2,), (3,), (4,), (5,)]
>>> df = spark.createDataFrame(data, ["values"])
>>> quantiles = df.approxQuantile("values", [0.0, 0.5, 1.0], 0.05)
>>> quantiles
[1.0, 3.0, 5.0]

```


Example 2: Calculating quantiles for multiple columns

```
>>> data = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
>>> df = spark.createDataFrame(data, ["col1", "col2"])
>>> quantiles = df.approxQuantile(["col1", "col2"], [0.0, 0.5, 1.0], 0.05)
>>> quantiles
[[1.0, 3.0, 5.0], [10.0, 30.0, 50.0]]

```


Example 3: Handling null values

```
>>> data = [(1,), (None,), (3,), (4,), (None,)]
>>> df = spark.createDataFrame(data, ["values"])
>>> quantiles = df.approxQuantile("values", [0.0, 0.5, 1.0], 0.05)
>>> quantiles
[1.0, 3.0, 4.0]

```


Example 4: Calculating quantiles with low precision

```
>>> data = [(1,), (2,), (3,), (4,), (5,)]
>>> df = spark.createDataFrame(data, ["values"])
>>> quantiles = df.approxQuantile("values", [0.0, 0.2, 1.0], 0.1)
>>> quantiles
[1.0, 1.0, 5.0]

```


# pyspark.sql.DataFrame.asTable — PySpark 4.0.1 documentation
DataFrame.asTable()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.asTable)
[#](#pyspark.sql.DataFrame.asTable "Permalink to this definition")

Converts the DataFrame into a [`table_arg.TableArg`](about:blank/pyspark.sql.table_arg.TableArg.html#pyspark.sql.table_arg.TableArg "pyspark.sql.table_arg.TableArg") object, which can be used as a table argument in a TVF(Table-Valued Function) including UDTF (User-Defined Table Function).

After obtaining a TableArg from a DataFrame using this method, you can specify partitioning and ordering for the table argument by calling methods such as partitionBy, orderBy, and withSinglePartition on the TableArg instance. - partitionBy: Partitions the data based on the specified columns. This method cannot be called after withSinglePartition() has been called. - orderBy: Orders the data within partitions based on the specified columns. - withSinglePartition: Indicates that the data should be treated as a single partition. This method cannot be called after partitionBy() has been called.

New in version 4.0.0.

Returns

[`table_arg.TableArg`](about:blank/pyspark.sql.table_arg.TableArg.html#pyspark.sql.table_arg.TableArg "pyspark.sql.table_arg.TableArg")

A TableArg object representing a table argument.


# pyspark.sql.DataFrame.cache — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.cache

DataFrame.cache()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.cache)
[#](#pyspark.sql.DataFrame.cache "Permalink to this definition")

Persists the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with the default storage level (MEMORY\_AND\_DISK\_DESER).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Cached DataFrame.

Notes

The default storage level has changed to MEMORY\_AND\_DISK\_DESER to match Scala in 3.0.

Examples

```
>>> df = spark.range(1)
>>> df.cache()
DataFrame[id: bigint]

```


```
>>> df.explain()
== Physical Plan ==
InMemoryTableScan ...

```


# pyspark.sql.DataFrame.checkpoint — PySpark 4.0.1 documentation
DataFrame.checkpoint(_eager\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.checkpoint)
[#](#pyspark.sql.DataFrame.checkpoint "Permalink to this definition")

Returns a checkpointed version of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). Checkpointing can be used to truncate the logical plan of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), which is especially useful in iterative algorithms where the plan may grow exponentially. It will be saved to files inside the checkpoint directory set with `SparkContext.setCheckpointDir()`, or spark.checkpoint.dir configuration.

New in version 2.1.0.

Changed in version 4.0.0: Supports Spark Connect.

Parameters

**eager**bool, optional, default True

Whether to checkpoint this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") immediately.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Checkpointed DataFrame.

Notes

This API is experimental.

Examples

```
>>> df = spark.createDataFrame([
...     (14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.checkpoint(False)  
DataFrame[age: bigint, name: string]

```


# pyspark.sql.DataFrame.coalesce — PySpark 4.0.1 documentation
DataFrame.coalesce(_numPartitions_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.coalesce)
[#](#pyspark.sql.DataFrame.coalesce "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that has exactly numPartitions partitions.

Similar to coalesce defined on an `RDD`, this operation results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions. If a larger number of partitions is requested, it will stay at the current number of partitions.

However, if you’re doing a drastic coalesce, e.g. to numPartitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of numPartitions = 1). To avoid this, you can call repartition(). This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**numPartitions**int

specify the target number of partitions

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(0, 10, 1, 3).select(
...     sf.spark_partition_id().alias("partition")
... ).distinct().sort("partition").show()
+---------+
|partition|
+---------+
|        0|
|        1|
|        2|
+---------+

```


```
>>> from pyspark.sql import functions as sf
>>> spark.range(0, 10, 1, 3).coalesce(1).select(
...     sf.spark_partition_id().alias("partition")
... ).distinct().sort("partition").show()
+---------+
|partition|
+---------+
|        0|
+---------+

```


# pyspark.sql.DataFrame.colRegex — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.colRegex

DataFrame.colRegex(_colName_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.colRegex)
[#](#pyspark.sql.DataFrame.colRegex "Permalink to this definition")

Selects column based on the column name specified as a regex and returns it as [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**colName**str

string, column name specified as a regex.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Examples

```
>>> df = spark.createDataFrame([("a", 1), ("b", 2), ("c",  3)], ["Col1", "Col2"])
>>> df.select(df.colRegex("`(Col1)?+.+`")).show()
+----+
|Col2|
+----+
|   1|
|   2|
|   3|
+----+

```


# pyspark.sql.DataFrame.collect — PySpark 4.0.1 documentation
DataFrame.collect()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.collect)
[#](#pyspark.sql.DataFrame.collect "Permalink to this definition")

Returns all the records in the DataFrame as a list of [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

list

A list of [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row") objects, each representing a row in the DataFrame.

Notes

This method should only be used if the resulting list is expected to be small, as all the data is loaded into the driver’s memory.

Examples

Example: Collecting all rows of a DataFrame

```
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.collect()
[Row(age=14, name='Tom'), Row(age=23, name='Alice'), Row(age=16, name='Bob')]

```


Example: Collecting all rows after filtering

```
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.filter(df.age > 15).collect()
[Row(age=23, name='Alice'), Row(age=16, name='Bob')]

```


Example: Collecting all rows after selecting specific columns

```
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.select("name").collect()
[Row(name='Tom'), Row(name='Alice'), Row(name='Bob')]

```


Example: Collecting all rows after applying a function to a column

```
>>> from pyspark.sql.functions import upper
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.select(upper(df.name)).collect()
[Row(upper(name)='TOM'), Row(upper(name)='ALICE'), Row(upper(name)='BOB')]

```


Example: Collecting all rows from a DataFrame and converting a specific column to a list

```
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> rows = df.collect()
>>> [row["name"] for row in rows]
['Tom', 'Alice', 'Bob']

```


Example: Collecting all rows from a DataFrame and converting to a list of dictionaries

```
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> rows = df.collect()
>>> [row.asDict() for row in rows]
[{'age': 14, 'name': 'Tom'}, {'age': 23, 'name': 'Alice'}, {'age': 16, 'name': 'Bob'}]

```


# pyspark.sql.DataFrame.columns — PySpark 4.0.1 documentation
_property_ DataFrame.columns[#](#pyspark.sql.DataFrame.columns "Permalink to this definition")

Retrieves the names of all columns in the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as a list.

The order of the column names in the list reflects their order in the DataFrame.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

list

List of column names in the DataFrame.

Examples

Example 1: Retrieve column names of a DataFrame

```
>>> df = spark.createDataFrame(
...     [(14, "Tom", "CA"), (23, "Alice", "NY"), (16, "Bob", "TX")],
...     ["age", "name", "state"]
... )
>>> df.columns
['age', 'name', 'state']

```


Example 2: Using column names to project specific columns

```
>>> selected_cols = [col for col in df.columns if col != "age"]
>>> df.select(selected_cols).show()
+-----+-----+
| name|state|
+-----+-----+
|  Tom|   CA|
|Alice|   NY|
|  Bob|   TX|
+-----+-----+

```


Example 3: Checking if a specific column exists in a DataFrame

```
>>> "state" in df.columns
True
>>> "salary" in df.columns
False

```


Example 4: Iterating over columns to apply a transformation

```
>>> import pyspark.sql.functions as f
>>> for col_name in df.columns:
...     df = df.withColumn(col_name, f.upper(f.col(col_name)))
>>> df.show()
+---+-----+-----+
|age| name|state|
+---+-----+-----+
| 14|  TOM|   CA|
| 23|ALICE|   NY|
| 16|  BOB|   TX|
+---+-----+-----+

```


Example 5: Renaming columns and checking the updated column names

```
>>> df = df.withColumnRenamed("name", "first_name")
>>> df.columns
['age', 'first_name', 'state']

```


Example 6: Using the columns property to ensure two DataFrames have the same columns before a union

```
>>> df2 = spark.createDataFrame(
...     [(30, "Eve", "FL"), (40, "Sam", "WA")], ["age", "name", "location"])
>>> df.columns == df2.columns
False

```

# pyspark.sql.DataFrame.corr — PySpark 4.0.1 documentation
DataFrame.corr(_col1_, _col2_, _method\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.corr)
[#](#pyspark.sql.DataFrame.corr "Permalink to this definition")

Calculates the correlation of two columns of a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as a double value. Currently only supports the Pearson Correlation Coefficient. [`DataFrame.corr()`](#pyspark.sql.DataFrame.corr "pyspark.sql.DataFrame.corr") and [`DataFrameStatFunctions.corr()`](about:blank/pyspark.sql.DataFrameStatFunctions.corr.html#pyspark.sql.DataFrameStatFunctions.corr "pyspark.sql.DataFrameStatFunctions.corr") are aliases of each other.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**str

The name of the first column

**col2**str

The name of the second column

**method**str, optional

The correlation method. Currently only supports “pearson”

Returns

float

Pearson Correlation Coefficient of two columns.

Examples

```
>>> df = spark.createDataFrame([(1, 12), (10, 1), (19, 8)], ["c1", "c2"])
>>> df.corr("c1", "c2")
-0.3592106040535498
>>> df = spark.createDataFrame([(11, 12), (10, 11), (9, 10)], ["small", "bigger"])
>>> df.corr("small", "bigger")
1.0

```


# pyspark.sql.DataFrame.count — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.count

DataFrame.count()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.count)
[#](#pyspark.sql.DataFrame.count "Permalink to this definition")

Returns the number of rows in this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

int

Number of rows.

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

```


Return the number of rows in the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").


# pyspark.sql.DataFrame.cov — PySpark 4.0.1 documentation
DataFrame.cov(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.cov)
[#](#pyspark.sql.DataFrame.cov "Permalink to this definition")

Calculate the sample covariance for the given columns, specified by their names, as a double value. [`DataFrame.cov()`](#pyspark.sql.DataFrame.cov "pyspark.sql.DataFrame.cov") and [`DataFrameStatFunctions.cov()`](about:blank/pyspark.sql.DataFrameStatFunctions.cov.html#pyspark.sql.DataFrameStatFunctions.cov "pyspark.sql.DataFrameStatFunctions.cov") are aliases.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**str

The name of the first column

**col2**str

The name of the second column

Returns

float

Covariance of two columns.

Examples

```
>>> df = spark.createDataFrame([(1, 12), (10, 1), (19, 8)], ["c1", "c2"])
>>> df.cov("c1", "c2")
-18.0
>>> df = spark.createDataFrame([(11, 12), (10, 11), (9, 10)], ["small", "bigger"])
>>> df.cov("small", "bigger")
1.0

```


# pyspark.sql.DataFrame.createGlobalTempView — PySpark 4.0.1 documentation
DataFrame.createGlobalTempView(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.createGlobalTempView)
[#](#pyspark.sql.DataFrame.createGlobalTempView "Permalink to this definition")

Creates a global temporary view with this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

Name of the view.

Notes

The lifetime of this temporary view is tied to this Spark application. throws `TempTableAlreadyExistsException`, if the view name already exists in the catalog.

Examples

Example 1: Creating and querying a global temporary view

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.createGlobalTempView("people")
>>> df2 = spark.sql("SELECT * FROM global_temp.people")
>>> df2.show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Example 2: Attempting to create a duplicate global temporary view

```
>>> df.createGlobalTempView("people")  
Traceback (most recent call last):
...
AnalysisException: "Temporary table 'people' already exists;"

```


Example 3: Dropping a global temporary view

```
>>> spark.catalog.dropGlobalTempView("people")
True

```

# pyspark.sql.DataFrame.createOrReplaceGlobalTempView — PySpark 4.0.1 documentation
DataFrame.createOrReplaceGlobalTempView(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.createOrReplaceGlobalTempView)
[#](#pyspark.sql.DataFrame.createOrReplaceGlobalTempView "Permalink to this definition")

Creates or replaces a global temporary view using the given name.

The lifetime of this temporary view is tied to this Spark application.

New in version 2.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

Name of the view.

Examples

Example 1: Creating a global temporary view with a DataFrame

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.createOrReplaceGlobalTempView("people")

```


Example 2: Replacing a global temporary view with a filtered DataFrame

```
>>> df2 = df.filter(df.age > 3)
>>> df2.createOrReplaceGlobalTempView("people")
>>> df3 = spark.table("global_temp.people")
>>> sorted(df3.collect()) == sorted(df2.collect())
True

```


Example 3: Dropping a global temporary view >>> spark.catalog.dropGlobalTempView(“people”) True


# pyspark.sql.DataFrame.createOrReplaceTempView — PySpark 4.0.1 documentation
DataFrame.createOrReplaceTempView(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.createOrReplaceTempView)
[#](#pyspark.sql.DataFrame.createOrReplaceTempView "Permalink to this definition")

Creates or replaces a local temporary view with this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

Name of the view.

Notes

The lifetime of this temporary table is tied to the [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession") that was used to create this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Examples

Example 1: Creating a local temporary view named ‘people’.

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.createOrReplaceTempView("people")

```


Example 2: Replacing the local temporary view.

```
>>> df2 = df.filter(df.age > 3)
>>> # Replace the local temporary view with the filtered DataFrame
>>> df2.createOrReplaceTempView("people")
>>> # Query the temporary view
>>> df3 = spark.sql("SELECT * FROM people")
>>> # Check if the DataFrames are equal
... assert sorted(df3.collect()) == sorted(df2.collect())

```


Example 3: Dropping the temporary view.

```
>>> # Drop the local temporary view
... spark.catalog.dropTempView("people")
True

```


# pyspark.sql.DataFrame.createTempView — PySpark 4.0.1 documentation
DataFrame.createTempView(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.createTempView)
[#](#pyspark.sql.DataFrame.createTempView "Permalink to this definition")

Creates a local temporary view with this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The lifetime of this temporary table is tied to the [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession") that was used to create this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). throws `TempTableAlreadyExistsException`, if the view name already exists in the catalog.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

Name of the view.

Examples

Example 1: Creating and querying a local temporary view

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.createTempView("people")
>>> spark.sql("SELECT * FROM people").show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Example 2: Attempting to create a temporary view with an existing name

```
>>> df.createTempView("people")  
Traceback (most recent call last):
...
AnalysisException: "Temporary table 'people' already exists;"

```


Example 3: Creating and dropping a local temporary view

```
>>> spark.catalog.dropTempView("people")
True
>>> df.createTempView("people")

```


Example 4: Creating temporary views with multiple DataFrames with [`SparkSession.table()`](about:blank/pyspark.sql.SparkSession.table.html#pyspark.sql.SparkSession.table "pyspark.sql.SparkSession.table")

```
>>> df1 = spark.createDataFrame([(1, "John"), (2, "Jane")], schema=["id", "name"])
>>> df2 = spark.createDataFrame([(3, "Jake"), (4, "Jill")], schema=["id", "name"])
>>> df1.createTempView("table1")
>>> df2.createTempView("table2")
>>> result_df = spark.table("table1").union(spark.table("table2"))
>>> result_df.show()
+---+----+
| id|name|
+---+----+
|  1|John|
|  2|Jane|
|  3|Jake|
|  4|Jill|
+---+----+

```


# pyspark.sql.DataFrame.crossJoin — PySpark 4.0.1 documentation
DataFrame.crossJoin(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.crossJoin)
[#](#pyspark.sql.DataFrame.crossJoin "Permalink to this definition")

Returns the cartesian product with another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Right side of the cartesian product.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Joined DataFrame.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df2 = spark.createDataFrame(
...     [Row(height=80, name="Tom"), Row(height=85, name="Bob")])
>>> df.crossJoin(df2.select("height")).select("age", "name", "height").show()
+---+-----+------+
|age| name|height|
+---+-----+------+
| 14|  Tom|    80|
| 14|  Tom|    85|
| 23|Alice|    80|
| 23|Alice|    85|
| 16|  Bob|    80|
| 16|  Bob|    85|
+---+-----+------+

```


# pyspark.sql.DataFrame.crosstab — PySpark 4.0.1 documentation
DataFrame.crosstab(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.crosstab)
[#](#pyspark.sql.DataFrame.crosstab "Permalink to this definition")

Computes a pair-wise frequency table of the given columns. Also known as a contingency table. The first column of each row will be the distinct values of col1 and the column names will be the distinct values of col2. The name of the first column will be $col1\_$col2. Pairs that have no occurrences will have zero as their counts. [`DataFrame.crosstab()`](#pyspark.sql.DataFrame.crosstab "pyspark.sql.DataFrame.crosstab") and [`DataFrameStatFunctions.crosstab()`](about:blank/pyspark.sql.DataFrameStatFunctions.crosstab.html#pyspark.sql.DataFrameStatFunctions.crosstab "pyspark.sql.DataFrameStatFunctions.crosstab") are aliases.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**str

The name of the first column. Distinct items will make the first item of each row.

**col2**str

The name of the second column. Distinct items will make the column names of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Frequency matrix of two columns.

Examples

```
>>> df = spark.createDataFrame([(1, 11), (1, 11), (3, 10), (4, 8), (4, 8)], ["c1", "c2"])
>>> df.crosstab("c1", "c2").sort("c1_c2").show()
+-----+---+---+---+
|c1_c2| 10| 11|  8|
+-----+---+---+---+
|    1|  0|  2|  0|
|    3|  1|  0|  0|
|    4|  0|  0|  2|
+-----+---+---+---+

```

# pyspark.sql.DataFrame.cube — PySpark 4.0.1 documentation
DataFrame.cube(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.cube)
[#](#pyspark.sql.DataFrame.cube "Permalink to this definition")

Create a multi-dimensional cube for the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using the specified columns, allowing aggregations to be performed on them.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**list, str, int or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The columns to cube by. Each element should be a column name (string) or an expression ([`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")) or a column ordinal (int, 1-based) or list of them.

Changed in version 4.0.0: Supports column ordinal.

Returns

[`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData")

Cube of the data based on the specified columns.

Notes

A column ordinal starts from 1, which is different from the 0-based [`__getitem__()`](about:blank/pyspark.sql.DataFrame.__getitem__.html#pyspark.sql.DataFrame.__getitem__ "pyspark.sql.DataFrame.__getitem__").

Examples

```
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5)], schema=["name", "age"])

```


Example 1: Creating a cube on ‘name’, and calculate the number of rows in each dimensional.

```
>>> df.cube("name").count().orderBy("name").show()
+-----+-----+
| name|count|
+-----+-----+
| NULL|    2|
|Alice|    1|
|  Bob|    1|
+-----+-----+

```


Example 2: Creating a cube on ‘name’ and ‘age’, and calculate the number of rows in each dimensional.

```
>>> df.cube("name", df.age).count().orderBy("name", "age").show()
+-----+----+-----+
| name| age|count|
+-----+----+-----+
| NULL|NULL|    2|
| NULL|   2|    1|
| NULL|   5|    1|
|Alice|NULL|    1|
|Alice|   2|    1|
|  Bob|NULL|    1|
|  Bob|   5|    1|
+-----+----+-----+

```


Example 3: Also creating a cube on ‘name’ and ‘age’, but using the column ordinal.

```
>>> df.cube(1, 2).count().orderBy(1, 2).show()
+-----+----+-----+
| name| age|count|
+-----+----+-----+
| NULL|NULL|    2|
| NULL|   2|    1|
| NULL|   5|    1|
|Alice|NULL|    1|
|Alice|   2|    1|
|  Bob|NULL|    1|
|  Bob|   5|    1|
+-----+----+-----+

```


# pyspark.sql.DataFrame.describe — PySpark 4.0.1 documentation
DataFrame.describe(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.describe)
[#](#pyspark.sql.DataFrame.describe "Permalink to this definition")

Computes basic statistics for numeric and string columns.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

This includes count, mean, stddev, min, and max. If no columns are given, this function computes statistics for all numerical or string columns.

Parameters

**cols**str, list, optional

Column name or list of column names to describe by (default All columns).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new DataFrame that describes (provides statistics) given DataFrame.

See also

[`DataFrame.summary`](about:blank/pyspark.sql.DataFrame.summary.html#pyspark.sql.DataFrame.summary "pyspark.sql.DataFrame.summary")

Computes summary statistics for numeric and string columns.

Notes

This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Use summary for expanded statistics and control over which statistics to compute.

Examples

```
>>> df = spark.createDataFrame(
...     [("Bob", 13, 40.3, 150.5), ("Alice", 12, 37.8, 142.3), ("Tom", 11, 44.1, 142.2)],
...     ["name", "age", "weight", "height"],
... )
>>> df.describe(['age']).show()
+-------+----+
|summary| age|
+-------+----+
|  count|   3|
|   mean|12.0|
| stddev| 1.0|
|    min|  11|
|    max|  13|
+-------+----+

```


```
>>> df.describe(['age', 'weight', 'height']).show()
+-------+----+------------------+-----------------+
|summary| age|            weight|           height|
+-------+----+------------------+-----------------+
|  count|   3|                 3|                3|
|   mean|12.0| 40.73333333333333|            145.0|
| stddev| 1.0|3.1722757341273704|4.763402145525822|
|    min|  11|              37.8|            142.2|
|    max|  13|              44.1|            150.5|
+-------+----+------------------+-----------------+

```



# pyspark.sql.DataFrame.distinct — PySpark 4.0.1 documentation
DataFrame.distinct()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.distinct)
[#](#pyspark.sql.DataFrame.distinct "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing the distinct rows in this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with distinct records.

Examples

Remove duplicate rows from a DataFrame

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (23, "Alice")], ["age", "name"])
>>> df.distinct().show()
+---+-----+
|age| name|
+---+-----+
| 14|  Tom|
| 23|Alice|
+---+-----+

```


Count the number of distinct rows in a DataFrame

```
>>> df.distinct().count()
2

```


Get distinct rows from a DataFrame with multiple columns

```
>>> df = spark.createDataFrame(
...     [(14, "Tom", "M"), (23, "Alice", "F"), (23, "Alice", "F"), (14, "Tom", "M")],
...     ["age", "name", "gender"])
>>> df.distinct().show()
+---+-----+------+
|age| name|gender|
+---+-----+------+
| 14|  Tom|     M|
| 23|Alice|     F|
+---+-----+------+

```


Get distinct values from a specific column in a DataFrame

```
>>> df.select("name").distinct().show()
+-----+
| name|
+-----+
|  Tom|
|Alice|
+-----+

```


Count the number of distinct values in a specific column

```
>>> df.select("name").distinct().count()
2

```


Get distinct values from multiple columns in DataFrame

```
>>> df.select("name", "gender").distinct().show()
+-----+------+
| name|gender|
+-----+------+
|  Tom|     M|
|Alice|     F|
+-----+------+

```


Get distinct rows from a DataFrame with null values

```
>>> df = spark.createDataFrame(
...     [(14, "Tom", "M"), (23, "Alice", "F"), (23, "Alice", "F"), (14, "Tom", None)],
...     ["age", "name", "gender"])
>>> df.distinct().show()
+---+-----+------+
|age| name|gender|
+---+-----+------+
| 14|  Tom|     M|
| 23|Alice|     F|
| 14|  Tom|  NULL|
+---+-----+------+

```


Get distinct non-null values from a DataFrame

```
>>> df.distinct().filter(df.gender.isNotNull()).show()
+---+-----+------+
|age| name|gender|
+---+-----+------+
| 14|  Tom|     M|
| 23|Alice|     F|
+---+-----+------+

```


# pyspark.sql.DataFrame.drop — PySpark 4.0.1 documentation
DataFrame.drop(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.drop)
[#](#pyspark.sql.DataFrame.drop "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") without specified columns. This is a no-op if the schema doesn’t contain the given column name(s).

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols: str or :class:\`Column\`**

A name of the column, or the [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") to be dropped.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") without the specified columns.

Notes

*   When an input is a column name, it is treated literally without further interpretation. Otherwise, it will try to match the equivalent expression. So dropping a column by its name drop(colName) has a different semantic with directly dropping the column drop(col(colName)).
    

Examples

Example 1: Drop a column by name.

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.drop('age').show()
+-----+
| name|
+-----+
|  Tom|
|Alice|
|  Bob|
+-----+

```


Example 2: Drop a column by [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") object.

```
>>> df.drop(df.age).show()
+-----+
| name|
+-----+
|  Tom|
|Alice|
|  Bob|
+-----+

```


Example 3: Drop the column that joined both DataFrames on.

```
>>> df2 = spark.createDataFrame([(80, "Tom"), (85, "Bob")], ["height", "name"])
>>> df.join(df2, df.name == df2.name).drop('name').sort('age').show()
+---+------+
|age|height|
+---+------+
| 14|    80|
| 16|    85|
+---+------+

```


```
>>> df3 = df.join(df2)
>>> df3.show()
+---+-----+------+----+
|age| name|height|name|
+---+-----+------+----+
| 14|  Tom|    80| Tom|
| 14|  Tom|    85| Bob|
| 23|Alice|    80| Tom|
| 23|Alice|    85| Bob|
| 16|  Bob|    80| Tom|
| 16|  Bob|    85| Bob|
+---+-----+------+----+

```


Example 4: Drop two column by the same name.

```
>>> df3.drop("name").show()
+---+------+
|age|height|
+---+------+
| 14|    80|
| 14|    85|
| 23|    80|
| 23|    85|
| 16|    80|
| 16|    85|
+---+------+

```


Example 5: Can not drop col(‘name’) due to ambiguous reference.

```
>>> from pyspark.sql import functions as sf
>>> df3.drop(sf.col("name")).show()
Traceback (most recent call last):
...
pyspark.errors.exceptions.captured.AnalysisException: [AMBIGUOUS_REFERENCE] Reference...

```


Example 6: Can not find a column matching the expression “a.b.c”.

```
>>> from pyspark.sql import functions as sf
>>> df4 = df.withColumn("a.b.c", sf.lit(1))
>>> df4.show()
+---+-----+-----+
|age| name|a.b.c|
+---+-----+-----+
| 14|  Tom|    1|
| 23|Alice|    1|
| 16|  Bob|    1|
+---+-----+-----+

```


```
>>> df4.drop("a.b.c").show()
+---+-----+
|age| name|
+---+-----+
| 14|  Tom|
| 23|Alice|
| 16|  Bob|
+---+-----+

```


```
>>> df4.drop(sf.col("a.b.c")).show()
+---+-----+-----+
|age| name|a.b.c|
+---+-----+-----+
| 14|  Tom|    1|
| 23|Alice|    1|
| 16|  Bob|    1|
+---+-----+-----+

```


# pyspark.sql.DataFrame.dropDuplicates — PySpark 4.0.1 documentation
DataFrame.dropDuplicates(_subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.dropDuplicates)
[#](#pyspark.sql.DataFrame.dropDuplicates "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with duplicate rows removed, optionally only considering certain columns.

For a static batch [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), it just drops duplicate rows. For a streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), it will keep all data across triggers as intermediate state to drop duplicates rows. You can use [`withWatermark()`](about:blank/pyspark.sql.DataFrame.withWatermark.html#pyspark.sql.DataFrame.withWatermark "pyspark.sql.DataFrame.withWatermark") to limit how late the duplicate data can be and the system will accordingly limit the state. In addition, data older than watermark will be dropped to avoid any possibility of duplicates.

[`drop_duplicates()`](about:blank/pyspark.sql.DataFrame.drop_duplicates.html#pyspark.sql.DataFrame.drop_duplicates "pyspark.sql.DataFrame.drop_duplicates") is an alias for [`dropDuplicates()`](#pyspark.sql.DataFrame.dropDuplicates "pyspark.sql.DataFrame.dropDuplicates").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**subset**list of column names, optional

List of columns to use for duplicate comparison (default All columns).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame without duplicates.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([
...     Row(name='Alice', age=5, height=80),
...     Row(name='Alice', age=5, height=80),
...     Row(name='Alice', age=10, height=80)
... ])

```


Deduplicate the same rows.

```
>>> df.dropDuplicates().show()
+-----+---+------+
| name|age|height|
+-----+---+------+
|Alice|  5|    80|
|Alice| 10|    80|
+-----+---+------+

```


Deduplicate values on ‘name’ and ‘height’ columns.

```
>>> df.dropDuplicates(['name', 'height']).show()
+-----+---+------+
| name|age|height|
+-----+---+------+
|Alice|  5|    80|
+-----+---+------+

```


# pyspark.sql.DataFrame.dropDuplicatesWithinWatermark — PySpark 4.0.1 documentation
DataFrame.dropDuplicatesWithinWatermark(_subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.dropDuplicatesWithinWatermark)
[#](#pyspark.sql.DataFrame.dropDuplicatesWithinWatermark "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with duplicate rows removed,

optionally only considering certain columns, within watermark.

This only works with streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), and watermark for the input [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") must be set via [`withWatermark()`](about:blank/pyspark.sql.DataFrame.withWatermark.html#pyspark.sql.DataFrame.withWatermark "pyspark.sql.DataFrame.withWatermark").

For a streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), this will keep all data across triggers as intermediate state to drop duplicated rows. The state will be kept to guarantee the semantic, “Events are deduplicated as long as the time distance of earliest and latest events are smaller than the delay threshold of watermark.” Users are encouraged to set the delay threshold of watermark longer than max timestamp differences among duplicated events.

Note: too late data older than watermark will be dropped.

Parameters

**subset**List of column names, optional

List of columns to use for duplicate comparison (default All columns).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame without duplicates.

Notes

Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> from pyspark.sql.functions import timestamp_seconds
>>> df = spark.readStream.format("rate").load().selectExpr(
...     "value % 5 AS value", "timestamp")
>>> df.select("value", df.timestamp.alias("time")).withWatermark("time", '10 minutes')
DataFrame[value: bigint, time: timestamp]

```


Deduplicate the same rows.

```
>>> df.dropDuplicatesWithinWatermark() 

```


Deduplicate values on ‘value’ columns.

```
>>> df.dropDuplicatesWithinWatermark(['value'])  

```


# pyspark.sql.DataFrame.drop_duplicates — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.drop\_duplicates

DataFrame.drop\_duplicates(_subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.drop_duplicates)
[#](#pyspark.sql.DataFrame.drop_duplicates "Permalink to this definition")

[`drop_duplicates()`](#pyspark.sql.DataFrame.drop_duplicates "pyspark.sql.DataFrame.drop_duplicates") is an alias for [`dropDuplicates()`](about:blank/pyspark.sql.DataFrame.dropDuplicates.html#pyspark.sql.DataFrame.dropDuplicates "pyspark.sql.DataFrame.dropDuplicates").

New in version 1.4.0.


# pyspark.sql.DataFrame.dropna — PySpark 4.0.1 documentation
DataFrame.dropna(_how\='any'_, _thresh\=None_, _subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.dropna)
[#](#pyspark.sql.DataFrame.dropna "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") omitting rows with null or NaN values. [`DataFrame.dropna()`](#pyspark.sql.DataFrame.dropna "pyspark.sql.DataFrame.dropna") and [`DataFrameNaFunctions.drop()`](about:blank/pyspark.sql.DataFrameNaFunctions.drop.html#pyspark.sql.DataFrameNaFunctions.drop "pyspark.sql.DataFrameNaFunctions.drop") are aliases of each other.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**how**str, optional, the values that can be ‘any’ or ‘all’, default ‘any’.

If ‘any’, drop a row if it contains any nulls. If ‘all’, drop a row only if all its values are null.

**thresh: int, optional, default None.**

If specified, drop rows that have less than thresh non-null values. This overwrites the how parameter.

**subset**str, tuple or list, optional

optional list of column names to consider.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with null only rows excluded.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([
...     Row(age=10, height=80.0, name="Alice"),
...     Row(age=5, height=float("nan"), name="Bob"),
...     Row(age=None, height=None, name="Tom"),
...     Row(age=None, height=float("nan"), name=None),
... ])

```


Example 1: Drop the row if it contains any null or NaN.

```
>>> df.na.drop().show()
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
+---+------+-----+

```


Example 2: Drop the row only if all its values are null or NaN.

```
>>> df.na.drop(how='all').show()
+----+------+-----+
| age|height| name|
+----+------+-----+
|  10|  80.0|Alice|
|   5|   NaN|  Bob|
|NULL|  NULL|  Tom|
+----+------+-----+

```


Example 3: Drop rows that have less than thresh non-null and non-NaN values.

```
>>> df.na.drop(thresh=2).show()
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
|  5|   NaN|  Bob|
+---+------+-----+

```


Example 4: Drop rows with null and NaN values in the specified columns.

```
>>> df.na.drop(subset=['age', 'name']).show()
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
|  5|   NaN|  Bob|
+---+------+-----+

```


# pyspark.sql.DataFrame.dtypes — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.dtypes

_property_ DataFrame.dtypes[#](#pyspark.sql.DataFrame.dtypes "Permalink to this definition")

Returns all column names and their data types as a list.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

list

List of columns as tuple pairs.

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.dtypes
[('age', 'bigint'), ('name', 'string')]

```


# pyspark.sql.DataFrame.exceptAll — PySpark 4.0.1 documentation
DataFrame.exceptAll(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.exceptAll)
[#](#pyspark.sql.DataFrame.exceptAll "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing rows in this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") but not in another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") while preserving duplicates.

This is equivalent to EXCEPT ALL in SQL. As standard in SQL, this function resolves columns by position (not by name).

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

The other [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to compare to.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Examples

```
>>> df1 = spark.createDataFrame(
...         [("a", 1), ("a", 1), ("a", 1), ("a", 2), ("b",  3), ("c", 4)], ["C1", "C2"])
>>> df2 = spark.createDataFrame([("a", 1), ("b", 3)], ["C1", "C2"])
>>> df1.exceptAll(df2).show()
+---+---+
| C1| C2|
+---+---+
|  a|  1|
|  a|  1|
|  a|  2|
|  c|  4|
+---+---+

```


# pyspark.sql.DataFrame.executionInfo — PySpark 4.0.1 documentation
_property_ DataFrame.executionInfo[#](#pyspark.sql.DataFrame.executionInfo "Permalink to this definition")

Returns a ExecutionInfo object after the query was executed.

The executionInfo method allows to introspect information about the actual query execution after the successful execution. Accessing this member before the query execution will return None.

If the same DataFrame is executed multiple times, the execution info will be overwritten by the latest operation.

New in version 4.0.0.

Returns

An instance of ExecutionInfo or None when the value is not set yet.

Notes

This is an API dedicated to Spark Connect client only. With regular Spark Session, it throws an exception.

# pyspark.sql.DataFrame.exists — PySpark 4.0.1 documentation
DataFrame.exists()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.exists)
[#](#pyspark.sql.DataFrame.exists "Permalink to this definition")

Return a Column object for an EXISTS Subquery.

The exists method provides a way to create a boolean column that checks for the presence of related records in a subquery. When applied within a DataFrame, this method allows you to filter rows based on whether matching records exist in the related dataset. The resulting Column object can be used directly in filtering conditions or as a computed column.

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A Column object representing an EXISTS subquery

Examples

Setup sample data for customers and orders.

```
>>> data_customers = [
...     (101, "Alice", "USA"), (102, "Bob", "Canada"), (103, "Charlie", "USA"),
...     (104, "David", "Australia")
... ]
>>> data_orders = [
...     (1, 101, "2023-01-15", 250), (2, 102, "2023-01-20", 300),
...     (3, 103, "2023-01-25", 400), (4, 101, "2023-02-05", 150)
... ]
>>> customers = spark.createDataFrame(
...     data_customers, ["customer_id", "customer_name", "country"])
>>> orders = spark.createDataFrame(
...     data_orders, ["order_id", "customer_id", "order_date", "total_amount"])

```


Example 1: Filter for customers who have placed at least one order.

```
>>> from pyspark.sql import functions as sf
>>> customers.alias("c").where(
...     orders.alias("o").where(
...         sf.col("o.customer_id") == sf.col("c.customer_id").outer()
...     ).exists()
... ).orderBy("customer_id").show()
+-----------+-------------+-------+
|customer_id|customer_name|country|
+-----------+-------------+-------+
|        101|        Alice|    USA|
|        102|          Bob| Canada|
|        103|      Charlie|    USA|
+-----------+-------------+-------+

```


Example 2: Filter for customers who have never placed an order.

```
>>> from pyspark.sql import functions as sf
>>> customers.alias("c").where(
...     ~orders.alias("o").where(
...         sf.col("o.customer_id") == sf.col("c.customer_id").outer()
...     ).exists()
... ).orderBy("customer_id").show()
+-----------+-------------+---------+
|customer_id|customer_name|  country|
+-----------+-------------+---------+
|        104|        David|Australia|
+-----------+-------------+---------+

```


Example 3: Find Orders from Customers in the USA.

```
>>> from pyspark.sql import functions as sf
>>> orders.alias("o").where(
...     customers.alias("c").where(
...         (sf.col("c.customer_id") == sf.col("o.customer_id").outer())
...         & (sf.col("country") == "USA")
...     ).exists()
... ).orderBy("order_id").show()
+--------+-----------+----------+------------+
|order_id|customer_id|order_date|total_amount|
+--------+-----------+----------+------------+
|       1|        101|2023-01-15|         250|
|       3|        103|2023-01-25|         400|
|       4|        101|2023-02-05|         150|
+--------+-----------+----------+------------+

```


# pyspark.sql.DataFrame.explain — PySpark 4.0.1 documentation
DataFrame.explain(_extended\=None_, _mode\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.explain)
[#](#pyspark.sql.DataFrame.explain "Permalink to this definition")

Prints the (logical and physical) plans to the console for debugging purposes.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**extended**bool, optional

default `False`. If `False`, prints only the physical plan. When this is a string without specifying the `mode`, it works as the mode is specified.

**mode**str, optional

specifies the expected output format of plans.

*   `simple`: Print only a physical plan.
    
*   `extended`: Print both logical and physical plans.
    
*   `codegen`: Print a physical plan and generated codes if they are available.
    
*   `cost`: Print a logical plan and statistics if they are available.
    
*   `formatted`: Split explain output into two sections: a physical plan outline and node details.
    

Changed in version 3.0.0: Added optional argument mode to specify the expected output format of plans.

Examples

Example 1: Print out the physical plan only (default).

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.explain()  
== Physical Plan ==
*(1) Scan ExistingRDD[age...,name...]

```


Example 2: Print out all parsed, analyzed, optimized, and physical plans.

```
>>> df.explain(extended=True)
== Parsed Logical Plan ==
...
== Analyzed Logical Plan ==
...
== Optimized Logical Plan ==
...
== Physical Plan ==
...

```


Example 3: Print out the plans with two sections: a physical plan outline and node details.

```
>>> df.explain(mode="formatted")  
== Physical Plan ==
* Scan ExistingRDD (...)
(1) Scan ExistingRDD [codegen id : ...]
Output [2]: [age..., name...]
...

```


Example 4: Print a logical plan and statistics if they are available.

```
>>> df.explain(mode="cost")
== Optimized Logical Plan ==
...Statistics...
...

```

# pyspark.sql.DataFrame.fillna — PySpark 4.0.1 documentation
DataFrame.fillna(_value_, _subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.fillna)
[#](#pyspark.sql.DataFrame.fillna "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") which null values are filled with new value. [`DataFrame.fillna()`](#pyspark.sql.DataFrame.fillna "pyspark.sql.DataFrame.fillna") and [`DataFrameNaFunctions.fill()`](about:blank/pyspark.sql.DataFrameNaFunctions.fill.html#pyspark.sql.DataFrameNaFunctions.fill "pyspark.sql.DataFrameNaFunctions.fill") are aliases of each other.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**value**int, float, string, bool or dict, the value to replace null values with.

If the value is a dict, then subset is ignored and value must be a mapping from column name (string) to replacement value. The replacement value must be an int, float, boolean, or string.

**subset**str, tuple or list, optional

optional list of column names to consider. Columns specified in subset that do not have matching data types are ignored. For example, if value is a string, and subset contains a non-string column, then the non-string column is simply ignored.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with replaced null values.

Examples

```
>>> df = spark.createDataFrame([
...     (10, 80.5, "Alice", None),
...     (5, None, "Bob", None),
...     (None, None, "Tom", None),
...     (None, None, None, True)],
...     schema=["age", "height", "name", "bool"])

```


Example 1: Fill all null values with 50 for numeric columns.

```
>>> df.na.fill(50).show()
+---+------+-----+----+
|age|height| name|bool|
+---+------+-----+----+
| 10|  80.5|Alice|NULL|
|  5|  50.0|  Bob|NULL|
| 50|  50.0|  Tom|NULL|
| 50|  50.0| NULL|true|
+---+------+-----+----+

```


Example 2: Fill all null values with `False` for boolean columns.

```
>>> df.na.fill(False).show()
+----+------+-----+-----+
| age|height| name| bool|
+----+------+-----+-----+
|  10|  80.5|Alice|false|
|   5|  NULL|  Bob|false|
|NULL|  NULL|  Tom|false|
|NULL|  NULL| NULL| true|
+----+------+-----+-----+

```


Example 3: Fill all null values with to 50 and “unknown” for

‘age’ and ‘name’ column respectively.

```
>>> df.na.fill({'age': 50, 'name': 'unknown'}).show()
+---+------+-------+----+
|age|height|   name|bool|
+---+------+-------+----+
| 10|  80.5|  Alice|NULL|
|  5|  NULL|    Bob|NULL|
| 50|  NULL|    Tom|NULL|
| 50|  NULL|unknown|true|
+---+------+-------+----+

```


Example 4: Fill all null values with “Spark” for ‘name’ column.

```
>>> df.na.fill(value = 'Spark', subset = 'name').show()
+----+------+-----+----+
| age|height| name|bool|
+----+------+-----+----+
|  10|  80.5|Alice|NULL|
|   5|  NULL|  Bob|NULL|
|NULL|  NULL|  Tom|NULL|
|NULL|  NULL|Spark|true|
+----+------+-----+----+

```



# pyspark.sql.DataFrame.filter — PySpark 4.0.1 documentation
DataFrame.filter(_condition_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.filter)
[#](#pyspark.sql.DataFrame.filter "Permalink to this definition")

Filters rows using the given condition.

[`where()`](about:blank/pyspark.sql.DataFrame.where.html#pyspark.sql.DataFrame.where "pyspark.sql.DataFrame.where") is an alias for [`filter()`](#pyspark.sql.DataFrame.filter "pyspark.sql.DataFrame.filter").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**condition**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") of [`types.BooleanType`](about:blank/pyspark.sql.types.BooleanType.html#pyspark.sql.types.BooleanType "pyspark.sql.types.BooleanType") or a string of SQL expressions.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new DataFrame with rows that satisfy the condition.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice", "Math"), (5, "Bob", "Physics"), (7, "Charlie", "Chemistry")],
...     schema=["age", "name", "subject"])

```


Filter by [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") instances.

```
>>> df.filter(df.age > 3).show()
+---+-------+---------+
|age|   name|  subject|
+---+-------+---------+
|  5|    Bob|  Physics|
|  7|Charlie|Chemistry|
+---+-------+---------+
>>> df.where(df.age == 2).show()
+---+-----+-------+
|age| name|subject|
+---+-----+-------+
|  2|Alice|   Math|
+---+-----+-------+

```


Filter by SQL expression in a string.

```
>>> df.filter("age > 3").show()
+---+-------+---------+
|age|   name|  subject|
+---+-------+---------+
|  5|    Bob|  Physics|
|  7|Charlie|Chemistry|
+---+-------+---------+
>>> df.where("age = 2").show()
+---+-----+-------+
|age| name|subject|
+---+-----+-------+
|  2|Alice|   Math|
+---+-----+-------+

```


Filter by multiple conditions.

```
>>> df.filter((df.age > 3) & (df.subject == "Physics")).show()
+---+----+-------+
|age|name|subject|
+---+----+-------+
|  5| Bob|Physics|
+---+----+-------+
>>> df.filter((df.age == 2) | (df.subject == "Chemistry")).show()
+---+-------+---------+
|age|   name|  subject|
+---+-------+---------+
|  2|  Alice|     Math|
|  7|Charlie|Chemistry|
+---+-------+---------+

```


Filter by multiple conditions using SQL expression.

```
>>> df.filter("age > 3 AND name = 'Bob'").show()
+---+----+-------+
|age|name|subject|
+---+----+-------+
|  5| Bob|Physics|
+---+----+-------+

```


Filter using the [`Column.isin()`](about:blank/pyspark.sql.Column.isin.html#pyspark.sql.Column.isin "pyspark.sql.Column.isin") function.

```
>>> df.filter(df.name.isin("Alice", "Bob")).show()
+---+-----+-------+
|age| name|subject|
+---+-----+-------+
|  2|Alice|   Math|
|  5|  Bob|Physics|
+---+-----+-------+

```


Filter by a list of values using the [`Column.isin()`](about:blank/pyspark.sql.Column.isin.html#pyspark.sql.Column.isin "pyspark.sql.Column.isin") function.

```
>>> df.filter(df.subject.isin(["Math", "Physics"])).show()
+---+-----+-------+
|age| name|subject|
+---+-----+-------+
|  2|Alice|   Math|
|  5|  Bob|Physics|
+---+-----+-------+

```


Filter using the ~ operator to exclude certain values.

```
>>> df.filter(~df.name.isin(["Alice", "Charlie"])).show()
+---+----+-------+
|age|name|subject|
+---+----+-------+
|  5| Bob|Physics|
+---+----+-------+

```


Filter using the [`Column.isNotNull()`](about:blank/pyspark.sql.Column.isNotNull.html#pyspark.sql.Column.isNotNull "pyspark.sql.Column.isNotNull") function.

```
>>> df.filter(df.name.isNotNull()).show()
+---+-------+---------+
|age|   name|  subject|
+---+-------+---------+
|  2|  Alice|     Math|
|  5|    Bob|  Physics|
|  7|Charlie|Chemistry|
+---+-------+---------+

```


Filter using the [`Column.like()`](about:blank/pyspark.sql.Column.like.html#pyspark.sql.Column.like "pyspark.sql.Column.like") function.

```
>>> df.filter(df.name.like("Al%")).show()
+---+-----+-------+
|age| name|subject|
+---+-----+-------+
|  2|Alice|   Math|
+---+-----+-------+

```


Filter using the [`Column.contains()`](about:blank/pyspark.sql.Column.contains.html#pyspark.sql.Column.contains "pyspark.sql.Column.contains") function.

```
>>> df.filter(df.name.contains("i")).show()
+---+-------+---------+
|age|   name|  subject|
+---+-------+---------+
|  2|  Alice|     Math|
|  7|Charlie|Chemistry|
+---+-------+---------+

```


Filter using the [`Column.between()`](about:blank/pyspark.sql.Column.between.html#pyspark.sql.Column.between "pyspark.sql.Column.between") function.

```
>>> df.filter(df.age.between(2, 5)).show()
+---+-----+-------+
|age| name|subject|
+---+-----+-------+
|  2|Alice|   Math|
|  5|  Bob|Physics|
+---+-----+-------+

```

# pyspark.sql.DataFrame.first — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.first

DataFrame.first()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.first)
[#](#pyspark.sql.DataFrame.first "Permalink to this definition")

Returns the first row as a [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row")

First row if [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") is not empty, otherwise `None`.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.first()
Row(age=2, name='Alice')

```



# pyspark.sql.DataFrame.foreach — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.foreach

DataFrame.foreach(_f_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.foreach)
[#](#pyspark.sql.DataFrame.foreach "Permalink to this definition")

Applies the `f` function to all [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row") of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This is a shorthand for `df.rdd.foreach()`.

New in version 1.3.0.

Changed in version 4.0.0: Supports Spark Connect.

Parameters

**f**function

A function that accepts one parameter which will receive each row to process.

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> def func(person):
...     print(person.name)
...
>>> df.foreach(func)

```


# pyspark.sql.DataFrame.foreachPartition — PySpark 4.0.1 documentation
DataFrame.foreachPartition(_f_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.foreachPartition)
[#](#pyspark.sql.DataFrame.foreachPartition "Permalink to this definition")

Applies the `f` function to each partition of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This a shorthand for `df.rdd.foreachPartition()`.

New in version 1.3.0.

Changed in version 4.0.0: Supports Spark Connect.

Parameters

**f**function

A function that accepts one parameter which will receive each partition to process.

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> def func(itr):
...     for person in itr:
...         print(person.name)
...
>>> df.foreachPartition(func)

```


# pyspark.sql.DataFrame.freqItems — PySpark 4.0.1 documentation
DataFrame.freqItems(_cols_, _support\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.freqItems)
[#](#pyspark.sql.DataFrame.freqItems "Permalink to this definition")

Finding frequent items for columns, possibly with false positives. Using the frequent element count algorithm described in “[https://doi.org/10.1145/762471.762473](https://doi.org/10.1145/762471.762473), proposed by Karp, Schenker, and Papadimitriou”. [`DataFrame.freqItems()`](#pyspark.sql.DataFrame.freqItems "pyspark.sql.DataFrame.freqItems") and [`DataFrameStatFunctions.freqItems()`](about:blank/pyspark.sql.DataFrameStatFunctions.freqItems.html#pyspark.sql.DataFrameStatFunctions.freqItems "pyspark.sql.DataFrameStatFunctions.freqItems") are aliases.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**list or tuple

Names of the columns to calculate frequent items for as a list or tuple of strings.

**support**float, optional

The frequency with which to consider an item ‘frequent’. Default is 1%. The support must be greater than 1e-4.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with frequent items.

Notes

This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Examples

```
>>> df = spark.createDataFrame([(1, 11), (1, 11), (3, 10), (4, 8), (4, 8)], ["c1", "c2"])
>>> df.freqItems(["c1", "c2"]).show()  
+------------+------------+
|c1_freqItems|c2_freqItems|
+------------+------------+
|   [4, 1, 3]| [8, 11, 10]|
+------------+------------+

```


# pyspark.sql.DataFrame.groupBy — PySpark 4.0.1 documentation
DataFrame.groupBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.groupBy)
[#](#pyspark.sql.DataFrame.groupBy "Permalink to this definition")

Groups the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by the specified columns so that aggregation can be performed on them. See [`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData") for all the available aggregate functions.

`groupby()` is an alias for [`groupBy()`](#pyspark.sql.DataFrame.groupBy "pyspark.sql.DataFrame.groupBy").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**list, str, int or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The columns to group by. Each element can be a column name (string) or an expression ([`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")) or a column ordinal (int, 1-based) or list of them.

Changed in version 4.0.0: Supports column ordinal.

Returns

[`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData")

A [`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData") object representing the grouped data by the specified columns.

Notes

A column ordinal starts from 1, which is different from the 0-based [`__getitem__()`](about:blank/pyspark.sql.DataFrame.__getitem__.html#pyspark.sql.DataFrame.__getitem__ "pyspark.sql.DataFrame.__getitem__").

Examples

```
>>> df = spark.createDataFrame([
...     ("Alice", 2), ("Bob", 2), ("Bob", 2), ("Bob", 5)], schema=["name", "age"])

```


Example 1: Empty grouping columns triggers a global aggregation.

```
>>> df.groupBy().avg().show()
+--------+
|avg(age)|
+--------+
|    2.75|
+--------+

```


Example 2: Group-by ‘name’, and specify a dictionary to calculate the summation of ‘age’.

```
>>> df.groupBy("name").agg({"age": "sum"}).sort("name").show()
+-----+--------+
| name|sum(age)|
+-----+--------+
|Alice|       2|
|  Bob|       9|
+-----+--------+

```


Example 3: Group-by ‘name’, and calculate maximum values.

```
>>> df.groupBy(df.name).max().sort("name").show()
+-----+--------+
| name|max(age)|
+-----+--------+
|Alice|       2|
|  Bob|       5|
+-----+--------+

```


Example 4: Also group-by ‘name’, but using the column ordinal.

```
>>> df.groupBy(1).max().sort("name").show()
+-----+--------+
| name|max(age)|
+-----+--------+
|Alice|       2|
|  Bob|       5|
+-----+--------+

```


Example 5: Group-by ‘name’ and ‘age’, and calculate the number of rows in each group.

```
>>> df.groupBy(["name", df.age]).count().sort("name", "age").show()
+-----+---+-----+
| name|age|count|
+-----+---+-----+
|Alice|  2|    1|
|  Bob|  2|    2|
|  Bob|  5|    1|
+-----+---+-----+

```


Example 6: Also Group-by ‘name’ and ‘age’, but using the column ordinal.

```
>>> df.groupBy([df.name, 2]).count().sort("name", "age").show()
+-----+---+-----+
| name|age|count|
+-----+---+-----+
|Alice|  2|    1|
|  Bob|  2|    2|
|  Bob|  5|    1|
+-----+---+-----+

```


# pyspark.sql.DataFrame.groupingSets — PySpark 4.0.1 documentation
DataFrame.groupingSets(_groupingSets_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.groupingSets)
[#](#pyspark.sql.DataFrame.groupingSets "Permalink to this definition")

Create multi-dimensional aggregation for the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using the specified grouping sets, so we can run aggregation on them.

New in version 4.0.0.

Parameters

**groupingSets**sequence of sequence of columns or str

Individual set of columns to group on.

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Additional grouping columns specified by users. Those columns are shown as the output columns after aggregation.

Returns

[`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData")

Grouping sets of the data based on the specified columns.

Examples

Example 1: Group by city and car\_model, city, and all, and calculate the sum of quantity.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (100, 'Fremont', 'Honda Civic', 10),
...     (100, 'Fremont', 'Honda Accord', 15),
...     (100, 'Fremont', 'Honda CRV', 7),
...     (200, 'Dublin', 'Honda Civic', 20),
...     (200, 'Dublin', 'Honda Accord', 10),
...     (200, 'Dublin', 'Honda CRV', 3),
...     (300, 'San Jose', 'Honda Civic', 5),
...     (300, 'San Jose', 'Honda Accord', 8)
... ], schema="id INT, city STRING, car_model STRING, quantity INT")

```


```
>>> df.groupingSets(
...     [("city", "car_model"), ("city",), ()],
...     "city", "car_model"
... ).agg(sf.sum(sf.col("quantity")).alias("sum")).sort("city", "car_model").show()
+--------+------------+---+
|    city|   car_model|sum|
+--------+------------+---+
|    NULL|        NULL| 78|
|  Dublin|        NULL| 33|
|  Dublin|Honda Accord| 10|
|  Dublin|   Honda CRV|  3|
|  Dublin| Honda Civic| 20|
| Fremont|        NULL| 32|
| Fremont|Honda Accord| 15|
| Fremont|   Honda CRV|  7|
| Fremont| Honda Civic| 10|
|San Jose|        NULL| 13|
|San Jose|Honda Accord|  8|
|San Jose| Honda Civic|  5|
+--------+------------+---+

```


Example 2: Group by multiple columns and calculate both average and sum.

```
>>> df.groupingSets(
...     [("city", "car_model"), ("city",), ()],
...     "city", "car_model"
... ).agg(
...     sf.avg(sf.col("quantity")).alias("avg_quantity"),
...     sf.sum(sf.col("quantity")).alias("sum_quantity")
... ).sort("city", "car_model").show()
+--------+------------+------------------+------------+
|    city|   car_model|      avg_quantity|sum_quantity|
+--------+------------+------------------+------------+
|    NULL|        NULL|              9.75|          78|
|  Dublin|        NULL|              11.0|          33|
|  Dublin|Honda Accord|              10.0|          10|
|  Dublin|   Honda CRV|               3.0|           3|
|  Dublin| Honda Civic|              20.0|          20|
| Fremont|        NULL|10.666666666666666|          32|
| Fremont|Honda Accord|              15.0|          15|
| Fremont|   Honda CRV|               7.0|           7|
| Fremont| Honda Civic|              10.0|          10|
|San Jose|        NULL|               6.5|          13|
|San Jose|Honda Accord|               8.0|           8|
|San Jose| Honda Civic|               5.0|           5|
+--------+------------+------------------+------------+

```


# pyspark.sql.DataFrame.head — PySpark 4.0.1 documentation
DataFrame.head(_n\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.head)
[#](#pyspark.sql.DataFrame.head "Permalink to this definition")

Returns the first `n` rows.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**n**int, optional

default 1. Number of rows to return.

Returns

If n is supplied, return a list of [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row") of length n

or less if the DataFrame has fewer elements.

If n is missing, return a single Row.

Notes

This method should only be used if the resulting array is expected to be small, as all the data is loaded into the driver’s memory.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.head()
Row(age=2, name='Alice')
>>> df.head(1)
[Row(age=2, name='Alice')]
>>> df.head(0)
[]

```


# pyspark.sql.DataFrame.hint — PySpark 4.0.1 documentation
DataFrame.hint(_name_, _\*parameters_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.hint)
[#](#pyspark.sql.DataFrame.hint "Permalink to this definition")

Specifies some hint on the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

A name of the hint.

**parameters**str, list, float or int

Optional parameters.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Hinted DataFrame

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df2 = spark.createDataFrame([Row(height=80, name="Tom"), Row(height=85, name="Bob")])
>>> df.join(df2, "name").explain()  
== Physical Plan ==
...
... +- SortMergeJoin ...
...

```


Explicitly trigger the broadcast hashjoin by providing the hint in `df2`.

```
>>> df.join(df2.hint("broadcast"), "name").explain()
== Physical Plan ==
...
... +- BroadcastHashJoin ...
...

```

# pyspark.sql.DataFrame.inputFiles — PySpark 4.0.1 documentation
DataFrame.inputFiles()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.inputFiles)
[#](#pyspark.sql.DataFrame.inputFiles "Permalink to this definition")

Returns a best-effort snapshot of the files that compose this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). This method simply asks each constituent BaseRelation for its respective files and takes the union of all results. Depending on the source relations, this may not find all input files. Duplicates are removed.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

list

List of file paths.

Examples

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="inputFiles") as d:
...     # Write a single-row DataFrame into a JSON file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).repartition(1).write.json(d, mode="overwrite")
...
...     # Read the JSON file as a DataFrame.
...     df = spark.read.format("json").load(d)
...
...     # Returns the number of input files.
...     len(df.inputFiles())
1

```

# pyspark.sql.DataFrame.intersect — PySpark 4.0.1 documentation
DataFrame.intersect(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.intersect)
[#](#pyspark.sql.DataFrame.intersect "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing rows only in both this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") and another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). Note that any duplicates are removed. To preserve duplicates use [`intersectAll()`](about:blank/pyspark.sql.DataFrame.intersectAll.html#pyspark.sql.DataFrame.intersectAll "pyspark.sql.DataFrame.intersectAll").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that needs to be combined.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Combined DataFrame.

Notes

This is equivalent to INTERSECT in SQL.

Examples

Example 1: Intersecting two DataFrames with the same schema

```
>>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
>>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
>>> result_df = df1.intersect(df2).sort("C1", "C2")
>>> result_df.show()
+---+---+
| C1| C2|
+---+---+
|  a|  1|
|  b|  3|
+---+---+

```


Example 2: Intersecting two DataFrames with different schemas

```
>>> df1 = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "value"])
>>> df2 = spark.createDataFrame([(2, "B"), (3, "C")], ["id", "value"])
>>> result_df = df1.intersect(df2).sort("id", "value")
>>> result_df.show()
+---+-----+
| id|value|
+---+-----+
|  2|    B|
+---+-----+

```


Example 3: Intersecting all rows from two DataFrames with mismatched columns

```
>>> df1 = spark.createDataFrame([(1, 2), (1, 2), (3, 4)], ["A", "B"])
>>> df2 = spark.createDataFrame([(1, 2), (1, 2)], ["C", "D"])
>>> result_df = df1.intersect(df2).sort("A", "B")
>>> result_df.show()
+---+---+
|  A|  B|
+---+---+
|  1|  2|
+---+---+

```

# pyspark.sql.DataFrame.intersectAll — PySpark 4.0.1 documentation
DataFrame.intersectAll(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.intersectAll)
[#](#pyspark.sql.DataFrame.intersectAll "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing rows in both this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") and another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") while preserving duplicates.

This is equivalent to INTERSECT ALL in SQL. As standard in SQL, this function resolves columns by position (not by name).

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that needs to be combined.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Combined DataFrame.

Examples

Example 1: Intersecting two DataFrames with the same schema

```
>>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
>>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
>>> result_df = df1.intersectAll(df2).sort("C1", "C2")
>>> result_df.show()
+---+---+
| C1| C2|
+---+---+
|  a|  1|
|  a|  1|
|  b|  3|
+---+---+

```


Example 2: Intersecting two DataFrames with different schemas

```
>>> df1 = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "value"])
>>> df2 = spark.createDataFrame([(2, "B"), (3, "C")], ["id", "value"])
>>> result_df = df1.intersectAll(df2).sort("id", "value")
>>> result_df.show()
+---+-----+
| id|value|
+---+-----+
|  2|    B|
+---+-----+

```


Example 3: Intersecting all rows from two DataFrames with mismatched columns

```
>>> df1 = spark.createDataFrame([(1, 2), (1, 2), (3, 4)], ["A", "B"])
>>> df2 = spark.createDataFrame([(1, 2), (1, 2)], ["C", "D"])
>>> result_df = df1.intersectAll(df2).sort("A", "B")
>>> result_df.show()
+---+---+
|  A|  B|
+---+---+
|  1|  2|
|  1|  2|
+---+---+

```


# pyspark.sql.DataFrame.isEmpty — PySpark 4.0.1 documentation
DataFrame.isEmpty()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.isEmpty)
[#](#pyspark.sql.DataFrame.isEmpty "Permalink to this definition")

Checks if the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") is empty and returns a boolean value.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

bool

Returns `True` if the DataFrame is empty, `False` otherwise.

Notes

*   Unlike count(), this method does not trigger any computation.
    
*   An empty DataFrame has no rows. It may have columns, but no data.
    

Examples

Example 1: Checking if an empty DataFrame is empty

```
>>> df_empty = spark.createDataFrame([], 'a STRING')
>>> df_empty.isEmpty()
True

```


Example 2: Checking if a non-empty DataFrame is empty

```
>>> df_non_empty = spark.createDataFrame(["a"], 'STRING')
>>> df_non_empty.isEmpty()
False

```


Example 3: Checking if a DataFrame with null values is empty

```
>>> df_nulls = spark.createDataFrame([(None, None)], 'a STRING, b INT')
>>> df_nulls.isEmpty()
False

```


Example 4: Checking if a DataFrame with no rows but with columns is empty

```
>>> df_no_rows = spark.createDataFrame([], 'id INT, value STRING')
>>> df_no_rows.isEmpty()
True

```

# pyspark.sql.DataFrame.isLocal — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.isLocal

DataFrame.isLocal()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.isLocal)
[#](#pyspark.sql.DataFrame.isLocal "Permalink to this definition")

Returns `True` if the [`collect()`](about:blank/pyspark.sql.DataFrame.collect.html#pyspark.sql.DataFrame.collect "pyspark.sql.DataFrame.collect") and [`take()`](about:blank/pyspark.sql.DataFrame.take.html#pyspark.sql.DataFrame.take "pyspark.sql.DataFrame.take") methods can be run locally (without any Spark executors).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

bool

Examples

```
>>> df = spark.sql("SHOW TABLES")
>>> df.isLocal()
True

```

# pyspark.sql.DataFrame.isStreaming — PySpark 4.0.1 documentation
_property_ DataFrame.isStreaming[#](#pyspark.sql.DataFrame.isStreaming "Permalink to this definition")

Returns `True` if this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") contains one or more sources that continuously return data as it arrives. A [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that reads data from a streaming source must be executed as a `StreamingQuery` using the `start()` method in `DataStreamWriter`. Methods that return a single answer, (e.g., [`count()`](about:blank/pyspark.sql.DataFrame.count.html#pyspark.sql.DataFrame.count "pyspark.sql.DataFrame.count") or [`collect()`](about:blank/pyspark.sql.DataFrame.collect.html#pyspark.sql.DataFrame.collect "pyspark.sql.DataFrame.collect")) will throw an `AnalysisException` when there is a streaming source present.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

bool

Whether it’s streaming DataFrame or not.

Notes

This API is evolving.

Examples

```
>>> df = spark.readStream.format("rate").load()
>>> df.isStreaming
True

```

# pyspark.sql.DataFrame.join — PySpark 4.0.1 documentation
DataFrame.join(_other_, _on\=None_, _how\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.join)
[#](#pyspark.sql.DataFrame.join "Permalink to this definition")

Joins with another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), using the given join expression.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Right side of the join

**on**str, list or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

a string for the join column name, a list of column names, a join expression (Column), or a list of Columns. If on is a string or a list of strings indicating the name of the join column(s), the column(s) must exist on both sides, and this performs an equi-join.

**how**str, optional

default `inner`. Must be one of: `inner`, `cross`, `outer`, `full`, `fullouter`, `full_outer`, `left`, `leftouter`, `left_outer`, `right`, `rightouter`, `right_outer`, `semi`, `leftsemi`, `left_semi`, `anti`, `leftanti` and `left_anti`.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Joined DataFrame.

Examples

The following examples demonstrate various join types among `df1`, `df2`, and `df3`.

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(name="Alice", age=2), Row(name="Bob", age=5)])
>>> df2 = spark.createDataFrame([Row(name="Tom", height=80), Row(name="Bob", height=85)])
>>> df3 = spark.createDataFrame([
...     Row(name="Alice", age=10, height=80),
...     Row(name="Bob", age=5, height=None),
...     Row(name="Tom", age=None, height=None),
...     Row(name=None, age=None, height=None),
... ])

```


Inner join on columns (default)

```
>>> df.join(df2, "name").show()
+----+---+------+
|name|age|height|
+----+---+------+
| Bob|  5|    85|
+----+---+------+

```


```
>>> df.join(df3, ["name", "age"]).show()
+----+---+------+
|name|age|height|
+----+---+------+
| Bob|  5|  NULL|
+----+---+------+

```


Outer join on a single column with an explicit join condition.

When the join condition is explicited stated: df.name == df2.name, this will produce all records where the names match, as well as those that don’t (since it’s an outer join). If there are names in df2 that are not present in df, they will appear with NULL in the name column of df, and vice versa for df2.

```
>>> joined = df.join(df2, df.name == df2.name, "outer").sort(sf.desc(df.name))
>>> joined.show() 
+-----+----+----+------+
| name| age|name|height|
+-----+----+----+------+
|  Bob|   5| Bob|    85|
|Alice|   2|NULL|  NULL|
| NULL|NULL| Tom|    80|
+-----+----+----+------+

```


To unambiguously select output columns, specify the dataframe along with the column name:

```
>>> joined.select(df.name, df2.height).show() 
+-----+------+
| name|height|
+-----+------+
|  Bob|    85|
|Alice|  NULL|
| NULL|    80|
+-----+------+

```


However, in self-joins, direct column references can cause ambiguity:

```
>>> df.join(df, df.name == df.name, "outer").select(df.name).show() 
Traceback (most recent call last):
...
pyspark.errors.exceptions.captured.AnalysisException: Column name#0 are ambiguous...

```


A better approach is to assign aliases to the dataframes, and then reference the output columns from the join operation using these aliases:

```
>>> df.alias("a").join(
...     df.alias("b"), sf.col("a.name") == sf.col("b.name"), "outer"
... ).sort(sf.desc("a.name")).select("a.name", "b.age").show()
+-----+---+
| name|age|
+-----+---+
|  Bob|  5|
|Alice|  2|
+-----+---+

```


Outer join on a single column with implicit join condition using column name

When you provide the column name directly as the join condition, Spark will treat both name columns as one, and will not produce separate columns for df.name and df2.name. This avoids having duplicate columns in the output.

```
>>> df.join(df2, "name", "outer").sort(sf.desc("name")).show()
+-----+----+------+
| name| age|height|
+-----+----+------+
|  Tom|NULL|    80|
|  Bob|   5|    85|
|Alice|   2|  NULL|
+-----+----+------+

```


Outer join on multiple columns

```
>>> df.join(df3, ["name", "age"], "outer").sort("name", "age").show()
+-----+----+------+
| name| age|height|
+-----+----+------+
| NULL|NULL|  NULL|
|Alice|   2|  NULL|
|Alice|  10|    80|
|  Bob|   5|  NULL|
|  Tom|NULL|  NULL|
+-----+----+------+

```


Left outer join on columns

```
>>> df.join(df2, "name", "left_outer").show()
+-----+---+------+
| name|age|height|
+-----+---+------+
|Alice|  2|  NULL|
|  Bob|  5|    85|
+-----+---+------+

```


Right outer join on columns

```
>>> df.join(df2, "name", "right_outer").show()
+----+----+------+
|name| age|height|
+----+----+------+
| Tom|NULL|    80|
| Bob|   5|    85|
+----+----+------+

```


Left semi join on columns

```
>>> df.join(df2, "name", "left_semi").show()
+----+---+
|name|age|
+----+---+
| Bob|  5|
+----+---+

```


Left anti join on columns

```
>>> df.join(df2, "name", "left_anti").show()
+-----+---+
| name|age|
+-----+---+
|Alice|  2|
+-----+---+

```



# pyspark.sql.DataFrame.limit — PySpark 4.0.1 documentation
DataFrame.limit(_num_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.limit)
[#](#pyspark.sql.DataFrame.limit "Permalink to this definition")

Limits the result count to the number specified.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**num**int

Number of records to return. Will return this number of records or all records if the DataFrame contains less than this number of records.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Subset of the records

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.limit(1).show()
+---+----+
|age|name|
+---+----+
| 14| Tom|
+---+----+
>>> df.limit(0).show()
+---+----+
|age|name|
+---+----+
+---+----+

```


# pyspark.sql.DataFrame.lateralJoin — PySpark 4.0.1 documentation
DataFrame.lateralJoin(_other_, _on\=None_, _how\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.lateralJoin)
[#](#pyspark.sql.DataFrame.lateralJoin "Permalink to this definition")

Lateral joins with another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), using the given join expression.

A lateral join (also known as a correlated join) is a type of join where each row from one DataFrame is used as input to a subquery or a derived table that computes a result specific to that row. The right side DataFrame can reference columns from the current row of the left side DataFrame, allowing for more complex and context-dependent results than a standard join.

New in version 4.0.0.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Right side of the join

**on**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

a join expression (Column).

**how**str, optional

default `inner`. Must be one of: `inner`, `cross`, `left`, `leftouter`, and `left_outer`.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Joined DataFrame.

Examples

Setup a sample DataFrame.

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Row
>>> customers_data = [
...     Row(customer_id=1, name="Alice"), Row(customer_id=2, name="Bob"),
...     Row(customer_id=3, name="Charlie"), Row(customer_id=4, name="Diana")
... ]
>>> customers = spark.createDataFrame(customers_data)
>>> orders_data = [
...     Row(order_id=101, customer_id=1, order_date="2024-01-10",
...         items=[Row(product="laptop", quantity=5), Row(product="mouse", quantity=12)]),
...     Row(order_id=102, customer_id=1, order_date="2024-02-15",
...         items=[Row(product="phone", quantity=2), Row(product="charger", quantity=15)]),
...     Row(order_id=105, customer_id=1, order_date="2024-03-20",
...         items=[Row(product="tablet", quantity=4)]),
...     Row(order_id=103, customer_id=2, order_date="2024-01-12",
...         items=[Row(product="tablet", quantity=8)]),
...     Row(order_id=104, customer_id=2, order_date="2024-03-05",
...         items=[Row(product="laptop", quantity=7)]),
...     Row(order_id=106, customer_id=3, order_date="2024-04-05",
...         items=[Row(product="monitor", quantity=1)]),
... ]
>>> orders = spark.createDataFrame(orders_data)

```


Example 1 (use TVF): Expanding Items in Each Order into Separate Rows

```
>>> customers.join(orders, "customer_id").lateralJoin(
...     spark.tvf.explode(sf.col("items").outer()).select("col.*")
... ).select(
...     "customer_id", "name", "order_id", "order_date", "product", "quantity"
... ).orderBy("customer_id", "order_id", "product").show()
+-----------+-------+--------+----------+-------+--------+
|customer_id|   name|order_id|order_date|product|quantity|
+-----------+-------+--------+----------+-------+--------+
|          1|  Alice|     101|2024-01-10| laptop|       5|
|          1|  Alice|     101|2024-01-10|  mouse|      12|
|          1|  Alice|     102|2024-02-15|charger|      15|
|          1|  Alice|     102|2024-02-15|  phone|       2|
|          1|  Alice|     105|2024-03-20| tablet|       4|
|          2|    Bob|     103|2024-01-12| tablet|       8|
|          2|    Bob|     104|2024-03-05| laptop|       7|
|          3|Charlie|     106|2024-04-05|monitor|       1|
+-----------+-------+--------+----------+-------+--------+

```


Example 2 (use subquery): Finding the Two Most Recent Orders for Customer

```
>>> customers.alias("c").lateralJoin(
...     orders.alias("o")
...     .where(sf.col("o.customer_id") == sf.col("c.customer_id").outer())
...     .select("order_id", "order_date")
...     .orderBy(sf.col("order_date").desc())
...     .limit(2),
...     how="left"
... ).orderBy("customer_id", "order_id").show()
+-----------+-------+--------+----------+
|customer_id|   name|order_id|order_date|
+-----------+-------+--------+----------+
|          1|  Alice|     102|2024-02-15|
|          1|  Alice|     105|2024-03-20|
|          2|    Bob|     103|2024-01-12|
|          2|    Bob|     104|2024-03-05|
|          3|Charlie|     106|2024-04-05|
|          4|  Diana|    NULL|      NULL|
+-----------+-------+--------+----------+

```


# pyspark.sql.DataFrame.localCheckpoint — PySpark 4.0.1 documentation
DataFrame.localCheckpoint(_eager\=True_, _storageLevel\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.localCheckpoint)
[#](#pyspark.sql.DataFrame.localCheckpoint "Permalink to this definition")

Returns a locally checkpointed version of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). Checkpointing can be used to truncate the logical plan of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"), which is especially useful in iterative algorithms where the plan may grow exponentially. Local checkpoints are stored in the executors using the caching subsystem and therefore they are not reliable.

New in version 2.3.0.

Changed in version 4.0.0: Supports Spark Connect. Added storageLevel parameter.

Parameters

**eager**bool, optional, default True

Whether to checkpoint this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") immediately.

**storageLevel**`StorageLevel`, optional, default None

The StorageLevel with which the checkpoint will be stored. If not specified, default for RDD local checkpoints.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Checkpointed DataFrame.

Notes

This API is experimental.

Examples

```
>>> df = spark.createDataFrame([
...     (14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.localCheckpoint(False)
DataFrame[age: bigint, name: string]

```


# pyspark.sql.DataFrame.mapInPandas — PySpark 4.0.1 documentation
DataFrame.mapInPandas(_func_, _schema_, _barrier\=False_, _profile\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.mapInPandas)
[#](#pyspark.sql.DataFrame.mapInPandas "Permalink to this definition")

Maps an iterator of batches in the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using a Python native function that is performed on pandas DataFrames both as input and output, and returns the result as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This method applies the specified Python function to an iterator of pandas.DataFrames, each representing a batch of rows from the original DataFrame. The returned iterator of pandas.DataFrames are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). The size of the function’s input and output can be different. Each pandas.DataFrame size can be controlled by spark.sql.execution.arrow.maxRecordsPerBatch.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**func**function

a Python native function that takes an iterator of pandas.DataFrames, and outputs an iterator of pandas.DataFrames.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the return type of the func in PySpark. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

**barrier**bool, optional, default False

Use barrier mode execution, ensuring that all Python workers in the stage will be launched concurrently.

**profile**[`pyspark.resource.ResourceProfile`](about:blank/api/pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile"). The optional ResourceProfile

to be used for mapInPandas.

Examples

```
>>> df = spark.createDataFrame([(1, 21), (2, 30)], ("id", "age"))

```


Filter rows with id equal to 1:

```
>>> def filter_func(iterator):
...     for pdf in iterator:
...         yield pdf[pdf.id == 1]
...
>>> df.mapInPandas(filter_func, df.schema).show()  
+---+---+
| id|age|
+---+---+
|  1| 21|
+---+---+

```


Compute the mean age for each id:

```
>>> def mean_age(iterator):
...     for pdf in iterator:
...         yield pdf.groupby("id").mean().reset_index()
...
>>> df.mapInPandas(mean_age, "id: bigint, age: double").show()  
+---+----+
| id| age|
+---+----+
|  1|21.0|
|  2|30.0|
+---+----+

```


Add a new column with the double of the age:

```
>>> def double_age(iterator):
...     for pdf in iterator:
...         pdf["double_age"] = pdf["age"] * 2
...         yield pdf
...
>>> df.mapInPandas(
...     double_age, "id: bigint, age: bigint, double_age: bigint").show()  
+---+---+----------+
| id|age|double_age|
+---+---+----------+
|  1| 21|        42|
|  2| 30|        60|
+---+---+----------+

```


Set `barrier` to `True` to force the `mapInPandas` stage running in the barrier mode, it ensures all Python workers in the stage will be launched concurrently.

```
>>> df.mapInPandas(filter_func, df.schema, barrier=True).show()  
+---+---+
| id|age|
+---+---+
|  1| 21|
+---+---+

```

# pyspark.sql.DataFrame.mapInArrow — PySpark 4.0.1 documentation
DataFrame.mapInArrow(_func_, _schema_, _barrier\=False_, _profile\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.mapInArrow)
[#](#pyspark.sql.DataFrame.mapInArrow "Permalink to this definition")

Maps an iterator of batches in the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using a Python native function that is performed on pyarrow.RecordBatchs both as input and output, and returns the result as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This method applies the specified Python function to an iterator of pyarrow.RecordBatchs, each representing a batch of rows from the original DataFrame. The returned iterator of pyarrow.RecordBatchs are combined as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). The size of the function’s input and output can be different. Each pyarrow.RecordBatch size can be controlled by spark.sql.execution.arrow.maxRecordsPerBatch.

New in version 3.3.0.

Parameters

**func**function

a Python native function that takes an iterator of pyarrow.RecordBatchs, and outputs an iterator of pyarrow.RecordBatchs.

**schema**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str

the return type of the func in PySpark. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

**barrier**bool, optional, default False

Use barrier mode execution, ensuring that all Python workers in the stage will be launched concurrently.

**profile**[`pyspark.resource.ResourceProfile`](about:blank/api/pyspark.resource.ResourceProfile.html#pyspark.resource.ResourceProfile "pyspark.resource.ResourceProfile"). The optional ResourceProfile

to be used for mapInArrow.

Examples

```
>>> import pyarrow  
>>> df = spark.createDataFrame([(1, 21), (2, 30)], ("id", "age"))
>>> def filter_func(iterator):
...     for batch in iterator:
...         pdf = batch.to_pandas()
...         yield pyarrow.RecordBatch.from_pandas(pdf[pdf.id == 1])
>>> df.mapInArrow(filter_func, df.schema).show()  
+---+---+
| id|age|
+---+---+
|  1| 21|
+---+---+

```


Set `barrier` to `True` to force the `mapInArrow` stage running in the barrier mode, it ensures all Python workers in the stage will be launched concurrently.

```
>>> df.mapInArrow(filter_func, df.schema, barrier=True).show()  
+---+---+
| id|age|
+---+---+
|  1| 21|
+---+---+

```



# pyspark.sql.DataFrame.metadataColumn — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.metadataColumn

DataFrame.metadataColumn(_colName_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.metadataColumn)
[#](#pyspark.sql.DataFrame.metadataColumn "Permalink to this definition")

Selects a metadata column based on its logical column name and returns it as a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

A metadata column can be accessed this way even if the underlying data source defines a data column with a conflicting name.

New in version 4.0.0.

Parameters

**colName**str

string, metadata column name

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")


# pyspark.sql.DataFrame.melt — PySpark 4.0.1 documentation
DataFrame.melt(_ids_, _values_, _variableColumnName_, _valueColumnName_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.melt)
[#](#pyspark.sql.DataFrame.melt "Permalink to this definition")

Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to groupBy(…).pivot(…).agg(…), except for the aggregation, which cannot be reversed.

[`melt()`](#pyspark.sql.DataFrame.melt "pyspark.sql.DataFrame.melt") is an alias for [`unpivot()`](about:blank/pyspark.sql.DataFrame.unpivot.html#pyspark.sql.DataFrame.unpivot "pyspark.sql.DataFrame.unpivot").

New in version 3.4.0.

Parameters

**ids**str, Column, tuple, list, optional

Column(s) to use as identifiers. Can be a single column or column name, or a list or tuple for multiple columns.

**values**str, Column, tuple, list, optional

Column(s) to unpivot. Can be a single column or column name, or a list or tuple for multiple columns. If not specified or empty, use all columns that are not set as ids.

**variableColumnName**str

Name of the variable column.

**valueColumnName**str

Name of the value column.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Unpivoted DataFrame.

Notes

Supports Spark Connect.


# pyspark.sql.DataFrame.na — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.na

_property_ DataFrame.na[#](#pyspark.sql.DataFrame.na "Permalink to this definition")

Returns a [`DataFrameNaFunctions`](about:blank/pyspark.sql.DataFrameNaFunctions.html#pyspark.sql.DataFrameNaFunctions "pyspark.sql.DataFrameNaFunctions") for handling missing values.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrameNaFunctions`](about:blank/pyspark.sql.DataFrameNaFunctions.html#pyspark.sql.DataFrameNaFunctions "pyspark.sql.DataFrameNaFunctions")

Examples

```
>>> df = spark.sql("SELECT 1 AS c1, int(NULL) AS c2")
>>> type(df.na)
<class '...dataframe.DataFrameNaFunctions'>

```


Replace the missing values as 2.

```
>>> df.na.fill(2).show()
+---+---+
| c1| c2|
+---+---+
|  1|  2|
+---+---+

```


# pyspark.sql.DataFrame.observe — PySpark 4.0.1 documentation
DataFrame.observe(_observation_, _\*exprs_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.observe)
[#](#pyspark.sql.DataFrame.observe "Permalink to this definition")

Define (named) metrics to observe on the DataFrame. This method returns an ‘observed’ DataFrame that returns the same result as the input, with the following guarantees:

*   It will compute the defined aggregates (metrics) on all the data that is flowing through
    
    the Dataset at that point.
    
*   It will report the value of the defined aggregate columns as soon as we reach a completion
    
    point. A completion point is either the end of a query (batch mode) or the end of a streaming epoch. The value of the aggregates only reflects the data processed since the previous completion point.
    

The metrics columns must either contain a literal (e.g. lit(42)), or should contain one or more aggregate functions (e.g. sum(a) or sum(a + b) + avg(c) - lit(1)). Expressions that contain references to the input Dataset’s columns must always be wrapped in an aggregate function.

A user can observe these metrics by adding Python’s [`StreamingQueryListener`](about:blank/pyspark.ss/api/pyspark.sql.streaming.StreamingQueryListener.html#pyspark.sql.streaming.StreamingQueryListener "pyspark.sql.streaming.StreamingQueryListener"), Scala/Java’s `org.apache.spark.sql.streaming.StreamingQueryListener` or Scala/Java’s `org.apache.spark.sql.util.QueryExecutionListener` to the spark session.

New in version 3.3.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters

**observation**[`Observation`](about:blank/pyspark.sql.Observation.html#pyspark.sql.Observation "pyspark.sql.Observation") or str

str to specify the name, or an [`Observation`](about:blank/pyspark.sql.Observation.html#pyspark.sql.Observation "pyspark.sql.Observation") instance to obtain the metric.

Changed in version 3.4.0: Added support for str in this parameter.

**exprs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

column expressions ([`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

the observed [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Notes

When `observation` is [`Observation`](about:blank/pyspark.sql.Observation.html#pyspark.sql.Observation "pyspark.sql.Observation"), this method only supports batch queries. When `observation` is a string, this method works for both batch and streaming queries. Continuous execution is currently not supported yet.

Examples

When `observation` is [`Observation`](about:blank/pyspark.sql.Observation.html#pyspark.sql.Observation "pyspark.sql.Observation"), only batch queries work as below.

```
>>> from pyspark.sql.functions import col, count, lit, max
>>> from pyspark.sql import Observation
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> observation = Observation("my metrics")
>>> observed_df = df.observe(observation, count(lit(1)).alias("count"), max(col("age")))
>>> observed_df.count()
2
>>> observation.get
{'count': 2, 'max(age)': 5}

```


When `observation` is a string, streaming queries also work as below.

```
>>> from pyspark.sql.streaming import StreamingQueryListener
>>> import time
>>> class MyErrorListener(StreamingQueryListener):
...    def onQueryStarted(self, event):
...        pass
...
...    def onQueryProgress(self, event):
...        row = event.progress.observedMetrics.get("my_event")
...        # Trigger if the number of errors exceeds 5 percent
...        num_rows = row.rc
...        num_error_rows = row.erc
...        ratio = num_error_rows / num_rows
...        if ratio > 0.05:
...            # Trigger alert
...            pass
...
...    def onQueryIdle(self, event):
...        pass
...
...    def onQueryTerminated(self, event):
...        pass
...
>>> error_listener = MyErrorListener()
>>> spark.streams.addListener(error_listener)
>>> sdf = spark.readStream.format("rate").load().withColumn(
...     "error", col("value")
... )
>>> # Observe row count (rc) and error row count (erc) in the streaming Dataset
... observed_ds = sdf.observe(
...     "my_event",
...     count(lit(1)).alias("rc"),
...     count(col("error")).alias("erc"))
>>> try:
...     q = observed_ds.writeStream.format("console").start()
...     time.sleep(5)
...
... finally:
...     q.stop()
...     spark.streams.removeListener(error_listener)
...

```


# pyspark.sql.DataFrame.offset — PySpark 4.0.1 documentation
DataFrame.offset(_num_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.offset)
[#](#pyspark.sql.DataFrame.offset "Permalink to this definition")

Returns a new :class: DataFrame by skipping the first n rows.

New in version 3.4.0.

Changed in version 3.5.0: Supports classic PySpark.

Parameters

**num**int

Number of records to skip.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Subset of the records

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.offset(1).show()
+---+-----+
|age| name|
+---+-----+
| 23|Alice|
| 16|  Bob|
+---+-----+
>>> df.offset(10).show()
+---+----+
|age|name|
+---+----+
+---+----+

```


# pyspark.sql.DataFrame.orderBy — PySpark 4.0.1 documentation
DataFrame.orderBy(_\*cols_, _\*\*kwargs_)
[#](#pyspark.sql.DataFrame.orderBy "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") sorted by the specified column(s).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**int, str, list, or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

> list of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column names or column ordinals to sort by.

Changed in version 4.0.0: Supports column ordinal.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Sorted DataFrame.

Other Parameters

**ascending**bool or list, optional, default True

boolean or list of boolean. Sort ascending vs. descending. Specify list for multiple sort orders. If a list is specified, the length of the list must equal the length of the cols.

Notes

A column ordinal starts from 1, which is different from the 0-based [`__getitem__()`](about:blank/pyspark.sql.DataFrame.__getitem__.html#pyspark.sql.DataFrame.__getitem__ "pyspark.sql.DataFrame.__getitem__"). If a column ordinal is negative, it means sort descending.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Sort the DataFrame in ascending order.

```
>>> df.sort(sf.asc("age")).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


```
>>> df.sort(1).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Sort the DataFrame in descending order.

```
>>> df.sort(df.age.desc()).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.orderBy(df.age.desc()).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.sort("age", ascending=False).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.sort(-1).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


Specify multiple columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (2, "Alice"), (2, "Bob"), (5, "Bob")], schema=["age", "name"])
>>> df.orderBy(sf.desc("age"), "name").show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
|  2|  Bob|
+---+-----+

```


```
>>> df.orderBy(-1, "name").show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
|  2|  Bob|
+---+-----+

```


```
>>> df.orderBy(-1, 2).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
|  2|  Bob|
+---+-----+

```


Specify multiple columns for sorting order at ascending.

```
>>> df.orderBy(["age", "name"], ascending=[False, False]).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.orderBy([1, "name"], ascending=[False, False]).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.orderBy([1, 2], ascending=[False, False]).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|  Bob|
|  2|Alice|
+---+-----+

```

# pyspark.sql.DataFrame.persist — PySpark 4.0.1 documentation
DataFrame.persist(_storageLevel\=StorageLevel(True, True, False, True, 1)_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.persist)
[#](#pyspark.sql.DataFrame.persist "Permalink to this definition")

Sets the storage level to persist the contents of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") across operations after the first time it is computed. This can only be used to assign a new storage level if the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") does not have a storage level set yet. If no storage level is specified defaults to (MEMORY\_AND\_DISK\_DESER)

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**storageLevel**`StorageLevel`

Storage level to set for persistence. Default is MEMORY\_AND\_DISK\_DESER.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Persisted DataFrame.

Notes

The default storage level has changed to MEMORY\_AND\_DISK\_DESER to match Scala in 3.0.

Examples

```
>>> df = spark.range(1)
>>> df.persist()
DataFrame[id: bigint]

```


```
>>> df.explain()
== Physical Plan ==
InMemoryTableScan ...

```


Persists the data in the disk by specifying the storage level.

```
>>> from pyspark.storagelevel import StorageLevel
>>> df.persist(StorageLevel.DISK_ONLY)
DataFrame[id: bigint]

```

# pyspark.sql.DataFrame.plot — PySpark 4.0.1 documentation
_property_ DataFrame.plot[#](#pyspark.sql.DataFrame.plot "Permalink to this definition")

Returns a `plot.core.PySparkPlotAccessor` for plotting functions.

New in version 4.0.0.

Returns

`plot.core.PySparkPlotAccessor`

Notes

This API is experimental. It provides two ways to create plots: 1. Chaining style (e.g., df.plot.line(…)). 2. Explicit style (e.g., df.plot(kind=”line”, …)).

Examples

```
>>> data = [("A", 10, 1.5), ("B", 30, 2.5), ("C", 20, 3.5)]
>>> columns = ["category", "int_val", "float_val"]
>>> df = spark.createDataFrame(data, columns)
>>> type(df.plot)
<class 'pyspark.sql.plot.core.PySparkPlotAccessor'>
>>> df.plot.line(x="category", y=["int_val", "float_val"])  
>>> df.plot(kind="line", x="category", y=["int_val", "float_val"])  

```



# pyspark.sql.DataFrame.printSchema — PySpark 4.0.1 documentation
DataFrame.printSchema(_level\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.printSchema)
[#](#pyspark.sql.DataFrame.printSchema "Permalink to this definition")

Prints out the schema in the tree format. Optionally allows to specify how many levels to print if schema is nested.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**level**int, optional

How many levels to print for nested schemas.

New in version 3.5.0.

Examples

Example 1: Printing the schema of a DataFrame with basic columns

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.printSchema()
root
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)

```


Example 2: Printing the schema with a specified level for nested columns

```
>>> df = spark.createDataFrame([(1, (2, 2))], ["a", "b"])
>>> df.printSchema(1)
root
 |-- a: long (nullable = true)
 |-- b: struct (nullable = true)

```


Example 3: Printing the schema with deeper nesting level

```
>>> df.printSchema(2)
root
 |-- a: long (nullable = true)
 |-- b: struct (nullable = true)
 |    |-- _1: long (nullable = true)
 |    |-- _2: long (nullable = true)

```


Example 4: Printing the schema of a DataFrame with nullable and non-nullable columns

```
>>> df = spark.range(1).selectExpr("id AS nonnullable", "NULL AS nullable")
>>> df.printSchema()
root
 |-- nonnullable: long (nullable = false)
 |-- nullable: void (nullable = true)

```


# pyspark.sql.DataFrame.randomSplit — PySpark 4.0.1 documentation
DataFrame.randomSplit(_weights_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.randomSplit)
[#](#pyspark.sql.DataFrame.randomSplit "Permalink to this definition")

Randomly splits this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with the provided weights.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**weights**list

list of doubles as weights with which to split the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). Weights will be normalized if they don’t sum up to 1.0.

**seed**int, optional

The seed for sampling.

Returns

list

List of DataFrames.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([
...     Row(age=10, height=80, name="Alice"),
...     Row(age=5, height=None, name="Bob"),
...     Row(age=None, height=None, name="Tom"),
...     Row(age=None, height=None, name=None),
... ])

```


```
>>> splits = df.randomSplit([1.0, 2.0], 24)
>>> splits[0].count()
2
>>> splits[1].count()
2

```

# pyspark.sql.DataFrame.rdd — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.rdd

_property_ DataFrame.rdd[#](#pyspark.sql.DataFrame.rdd "Permalink to this definition")

Returns the content as an [`pyspark.RDD`](about:blank/api/pyspark.RDD.html#pyspark.RDD "pyspark.RDD") of [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row").

New in version 1.3.0.

Returns

`RDD`

Examples

```
>>> df = spark.range(1)
>>> type(df.rdd)
<class 'pyspark.core.rdd.RDD'>

```


# pyspark.sql.DataFrame.registerTempTable — PySpark 4.0.1 documentation
DataFrame.registerTempTable(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.registerTempTable)
[#](#pyspark.sql.DataFrame.registerTempTable "Permalink to this definition")

Registers this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as a temporary table using the given name.

The lifetime of this temporary table is tied to the [`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession") that was used to create this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

Name of the temporary table to register.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.registerTempTable("people")
>>> df2 = spark.sql("SELECT * FROM people")
>>> sorted(df.collect()) == sorted(df2.collect())
True
>>> spark.catalog.dropTempView("people")
True

```

# pyspark.sql.DataFrame.repartition — PySpark 4.0.1 documentation
DataFrame.repartition(_numPartitions_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.repartition)
[#](#pyspark.sql.DataFrame.repartition "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") partitioned by the given partitioning expressions. The resulting [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") is hash partitioned.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**numPartitions**int

can be an int to specify the target number of partitions or a Column. If it is a Column, it will be used as the first partitioning column. If not specified, the default number of partitions is used.

**cols**str or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

partitioning columns.

Changed in version 1.6.0: Added optional arguments to specify the partitioning columns. Also made numPartitions optional if partitioning columns are specified.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Repartitioned DataFrame.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(0, 64, 1, 9).withColumn(
...     "name", sf.concat(sf.lit("name_"), sf.col("id").cast("string"))
... ).withColumn(
...     "age", sf.col("id") - 32
... )
>>> df.select(
...     sf.spark_partition_id().alias("partition")
... ).distinct().sort("partition").show()
+---------+
|partition|
+---------+
|        0|
|        1|
|        2|
|        3|
|        4|
|        5|
|        6|
|        7|
|        8|
+---------+

```


Repartition the data into 10 partitions.

```
>>> df.repartition(10).select(
...     sf.spark_partition_id().alias("partition")
... ).distinct().sort("partition").show()
+---------+
|partition|
+---------+
|        0|
|        1|
|        2|
|        3|
|        4|
|        5|
|        6|
|        7|
|        8|
|        9|
+---------+

```


Repartition the data into 7 partitions by ‘age’ column.

```
>>> df.repartition(7, "age").select(
...     sf.spark_partition_id().alias("partition")
... ).distinct().sort("partition").show()
+---------+
|partition|
+---------+
|        0|
|        1|
|        2|
|        3|
|        4|
|        5|
|        6|
+---------+

```


Repartition the data into 3 partitions by ‘age’ and ‘name’ columns.

```
>>> df.repartition(3, "name", "age").select(
...     sf.spark_partition_id().alias("partition")
... ).distinct().sort("partition").show()
+---------+
|partition|
+---------+
|        0|
|        1|
|        2|
+---------+

```


# pyspark.sql.DataFrame.repartitionByRange — PySpark 4.0.1 documentation
DataFrame.repartitionByRange(_numPartitions_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.repartitionByRange)
[#](#pyspark.sql.DataFrame.repartitionByRange "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") partitioned by the given partitioning expressions. The resulting [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") is range partitioned.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**numPartitions**int

can be an int to specify the target number of partitions or a Column. If it is a Column, it will be used as the first partitioning column. If not specified, the default number of partitions is used.

**cols**str or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

partitioning columns.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Repartitioned DataFrame.

Notes

At least one partition-by expression must be specified. When no explicit sort order is specified, “ascending nulls first” is assumed.

Due to performance reasons this method uses sampling to estimate the ranges. Hence, the output may not be consistent, since sampling can return different values. The sample size can be controlled by the config spark.sql.execution.rangeExchange.sampleSizePerPartition.

Examples

Repartition the data into 2 partitions by range in ‘age’ column. For example, the first partition can have `(14, "Tom")` and `(16, "Bob")`, and the second partition would have `(23, "Alice")`.

```
>>> from pyspark.sql import functions as sf
>>> spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"]
... ).repartitionByRange(2, "age").select(
...     "age", "name", sf.spark_partition_id()
... ).show()
+---+-----+--------------------+
|age| name|SPARK_PARTITION_ID()|
+---+-----+--------------------+
| 14|  Tom|                   0|
| 16|  Bob|                   0|
| 23|Alice|                   1|
+---+-----+--------------------+

```



# pyspark.sql.DataFrame.replace — PySpark 4.0.1 documentation
DataFrame.replace(_to\_replace_, _value=<no value>_, _subset=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.replace)
[#](#pyspark.sql.DataFrame.replace "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") replacing a value with another value. [`DataFrame.replace()`](#pyspark.sql.DataFrame.replace "pyspark.sql.DataFrame.replace") and [`DataFrameNaFunctions.replace()`](about:blank/pyspark.sql.DataFrameNaFunctions.replace.html#pyspark.sql.DataFrameNaFunctions.replace "pyspark.sql.DataFrameNaFunctions.replace") are aliases of each other. Values to\_replace and value must have the same type and can only be numerics, booleans, or strings. Value can have None. When replacing, the new value will be cast to the type of the existing column. For numeric replacements all values to be replaced should have unique floating point representation. In case of conflicts (for example with {42: -1, 42.0: 1}) and arbitrary replacement will be used.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**to\_replace**bool, int, float, string, list or dict, the value to be replaced.

If the value is a dict, then value is ignored or can be omitted, and to\_replace must be a mapping between a value and a replacement.

**value**bool, int, float, string or None, optional

The replacement value must be a bool, int, float, string or None. If value is a list, value should be of the same length and type as to\_replace. If value is a scalar and to\_replace is a sequence, then value is used as a replacement for each item in to\_replace.

**subset**list, optional

optional list of column names to consider. Columns specified in subset that do not have matching data types are ignored. For example, if value is a string, and subset contains a non-string column, then the non-string column is simply ignored.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with replaced values.

Examples

```
>>> df = spark.createDataFrame([
...     (10, 80, "Alice"),
...     (5, None, "Bob"),
...     (None, 10, "Tom"),
...     (None, None, None)],
...     schema=["age", "height", "name"])

```


Example 1: Replace 10 to 20 in all columns.

```
>>> df.na.replace(10, 20).show()
+----+------+-----+
| age|height| name|
+----+------+-----+
|  20|    80|Alice|
|   5|  NULL|  Bob|
|NULL|    20|  Tom|
|NULL|  NULL| NULL|
+----+------+-----+

```


Example 2: Replace ‘Alice’ to null in all columns.

```
>>> df.na.replace('Alice', None).show()
+----+------+----+
| age|height|name|
+----+------+----+
|  10|    80|NULL|
|   5|  NULL| Bob|
|NULL|    10| Tom|
|NULL|  NULL|NULL|
+----+------+----+

```


Example 3: Replace ‘Alice’ to ‘A’, and ‘Bob’ to ‘B’ in the ‘name’ column.

```
>>> df.na.replace(['Alice', 'Bob'], ['A', 'B'], 'name').show()
+----+------+----+
| age|height|name|
+----+------+----+
|  10|    80|   A|
|   5|  NULL|   B|
|NULL|    10| Tom|
|NULL|  NULL|NULL|
+----+------+----+

```


Example 4: Replace 10 to 20 in the ‘name’ column.

```
>>> df.na.replace(10, 18, 'age').show()
+----+------+-----+
| age|height| name|
+----+------+-----+
|  18|    80|Alice|
|   5|  NULL|  Bob|
|NULL|    10|  Tom|
|NULL|  NULL| NULL|
+----+------+-----+

```


# pyspark.sql.DataFrame.rollup — PySpark 4.0.1 documentation
DataFrame.rollup(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.rollup)
[#](#pyspark.sql.DataFrame.rollup "Permalink to this definition")

Create a multi-dimensional rollup for the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") using the specified columns, allowing for aggregation on them.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**list, str, int or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The columns to roll-up by. Each element should be a column name (string) or an expression ([`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")) or a column ordinal (int, 1-based) or list of them.

Changed in version 4.0.0: Supports column ordinal.

Returns

[`GroupedData`](about:blank/pyspark.sql.GroupedData.html#pyspark.sql.GroupedData "pyspark.sql.GroupedData")

Rolled-up data based on the specified columns.

Notes

A column ordinal starts from 1, which is different from the 0-based [`__getitem__()`](about:blank/pyspark.sql.DataFrame.__getitem__.html#pyspark.sql.DataFrame.__getitem__ "pyspark.sql.DataFrame.__getitem__").

Examples

```
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5)], schema=["name", "age"])

```


Example 1: Rollup-by ‘name’, and calculate the number of rows in each dimensional.

```
>>> df.rollup("name").count().orderBy("name").show()
+-----+-----+
| name|count|
+-----+-----+
| NULL|    2|
|Alice|    1|
|  Bob|    1|
+-----+-----+

```


Example 2: Rollup-by ‘name’ and ‘age’, and calculate the number of rows in each dimensional.

```
>>> df.rollup("name", df.age).count().orderBy("name", "age").show()
+-----+----+-----+
| name| age|count|
+-----+----+-----+
| NULL|NULL|    2|
|Alice|NULL|    1|
|Alice|   2|    1|
|  Bob|NULL|    1|
|  Bob|   5|    1|
+-----+----+-----+

```


Example 3: Also Rollup-by ‘name’ and ‘age’, but using the column ordinal.

```
>>> df.rollup(1, 2).count().orderBy(1, 2).show()
+-----+----+-----+
| name| age|count|
+-----+----+-----+
| NULL|NULL|    2|
|Alice|NULL|    1|
|Alice|   2|    1|
|  Bob|NULL|    1|
|  Bob|   5|    1|
+-----+----+-----+

```


# pyspark.sql.DataFrame.sameSemantics — PySpark 4.0.1 documentation
DataFrame.sameSemantics(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.sameSemantics)
[#](#pyspark.sql.DataFrame.sameSemantics "Permalink to this definition")

Returns True when the logical query plans inside both [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")s are equal and therefore return the same results.

New in version 3.1.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

The other DataFrame to compare against.

Returns

bool

Whether these two DataFrames are similar.

Notes

The equality comparison here is simplified by tolerating the cosmetic differences such as attribute names.

This API can compare both [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")s very fast but can still return False on the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that return the same results, for instance, from different plans. Such false negative semantic can be useful when caching as an example.

This API is a developer API.

Examples

```
>>> df1 = spark.range(10)
>>> df2 = spark.range(10)
>>> df1.withColumn("col1", df1.id * 2).sameSemantics(df2.withColumn("col1", df2.id * 2))
True
>>> df1.withColumn("col1", df1.id * 2).sameSemantics(df2.withColumn("col1", df2.id + 2))
False
>>> df1.withColumn("col1", df1.id * 2).sameSemantics(df2.withColumn("col0", df2.id * 2))
True

```



# pyspark.sql.DataFrame.sample — PySpark 4.0.1 documentation
DataFrame.sample(_withReplacement\=None_, _fraction\=None_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.sample)
[#](#pyspark.sql.DataFrame.sample "Permalink to this definition")

Returns a sampled subset of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**withReplacement**bool, optional

Sample with replacement or not (default `False`).

**fraction**float, optional

Fraction of rows to generate, range \[0.0, 1.0\].

**seed**int, optional

Seed for sampling (default a random seed).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Sampled rows from given DataFrame.

Notes

This is not guaranteed to provide exactly the fraction specified of the total count of the given [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

fraction is required and, withReplacement and seed are optional.

Examples

```
>>> df = spark.range(10)
>>> df.sample(0.5, 3).count() 
7
>>> df.sample(fraction=0.5, seed=3).count() 
7
>>> df.sample(withReplacement=True, fraction=0.5, seed=3).count() 
1
>>> df.sample(1.0).count()
10
>>> df.sample(fraction=1.0).count()
10
>>> df.sample(False, fraction=1.0).count()
10

```


# pyspark.sql.DataFrame.sampleBy — PySpark 4.0.1 documentation
DataFrame.sampleBy(_col_, _fractions_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.sampleBy)
[#](#pyspark.sql.DataFrame.sampleBy "Permalink to this definition")

Returns a stratified sample without replacement based on the fraction given on each stratum.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column that defines strata

Changed in version 3.0.0: Added sampling by a column of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

**fractions**dict

sampling fraction for each stratum. If a stratum is not specified, we treat its fraction as zero.

**seed**int, optional

random seed

Returns

a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that represents the stratified sample

Examples

```
>>> from pyspark.sql.functions import col
>>> dataset = spark.range(0, 100).select((col("id") % 3).alias("key"))
>>> sampled = dataset.sampleBy("key", fractions={0: 0.1, 1: 0.2}, seed=0)
>>> sampled.groupBy("key").count().orderBy("key").show()
+---+-----+
|key|count|
+---+-----+
|  0|    3|
|  1|    6|
+---+-----+
>>> dataset.sampleBy(col("key"), fractions={2: 1.0}, seed=0).count()
33

```


# pyspark.sql.DataFrame.scalar — PySpark 4.0.1 documentation
DataFrame.scalar()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.scalar)
[#](#pyspark.sql.DataFrame.scalar "Permalink to this definition")

Return a Column object for a SCALAR Subquery containing exactly one row and one column.

The scalar() method is useful for extracting a Column object that represents a scalar value from a DataFrame, especially when the DataFrame results from an aggregation or single-value computation. This returned Column can then be used directly in select clauses or as predicates in filters on the outer DataFrame, enabling dynamic data filtering and calculations based on scalar values.

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A Column object representing a SCALAR subquery.

Examples

Setup a sample DataFrame.

```
>>> data = [
...     (1, "Alice", 45000, 101), (2, "Bob", 54000, 101), (3, "Charlie", 29000, 102),
...     (4, "David", 61000, 102), (5, "Eve", 48000, 101),
... ]
>>> employees = spark.createDataFrame(data, ["id", "name", "salary", "department_id"])

```


Example 1 (non-correlated): Filter for employees with salary greater than the average salary.

```
>>> from pyspark.sql import functions as sf
>>> employees.where(
...     sf.col("salary") > employees.select(sf.avg("salary")).scalar()
... ).select("name", "salary", "department_id").orderBy("name").show()
+-----+------+-------------+
| name|salary|department_id|
+-----+------+-------------+
|  Bob| 54000|          101|
|David| 61000|          102|
|  Eve| 48000|          101|
+-----+------+-------------+

```


Example 2 (correlated): Filter for employees with salary greater than the average salary in their department.

```
>>> from pyspark.sql import functions as sf
>>> employees.alias("e1").where(
...     sf.col("salary")
...     > employees.alias("e2").where(
...         sf.col("e2.department_id") == sf.col("e1.department_id").outer()
...     ).select(sf.avg("salary")).scalar()
... ).select("name", "salary", "department_id").orderBy("name").show()
+-----+------+-------------+
| name|salary|department_id|
+-----+------+-------------+
|  Bob| 54000|          101|
|David| 61000|          102|
+-----+------+-------------+

```


Example 3 (in select): Select the name, salary, and the proportion of the salary in the department.

```
>>> from pyspark.sql import functions as sf
>>> employees.alias("e1").select(
...     "name", "salary", "department_id",
...     sf.format_number(
...         sf.lit(100) * sf.col("salary") /
...             employees.alias("e2").where(
...                 sf.col("e2.department_id") == sf.col("e1.department_id").outer()
...             ).select(sf.sum("salary")).scalar().alias("avg_salary"),
...         1
...     ).alias("salary_proportion_in_department")
... ).orderBy("name").show()
+-------+------+-------------+-------------------------------+
|   name|salary|department_id|salary_proportion_in_department|
+-------+------+-------------+-------------------------------+
|  Alice| 45000|          101|                           30.6|
|    Bob| 54000|          101|                           36.7|
|Charlie| 29000|          102|                           32.2|
|  David| 61000|          102|                           67.8|
|    Eve| 48000|          101|                           32.7|
+-------+------+-------------+-------------------------------+

```


# pyspark.sql.DataFrame.schema — PySpark 4.0.1 documentation
_property_ DataFrame.schema[#](#pyspark.sql.DataFrame.schema "Permalink to this definition")

Returns the schema of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as a [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

`StructType`

Examples

Example 1: Retrieve the inferred schema of the current DataFrame.

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.schema
StructType([StructField('age', LongType(), True),
            StructField('name', StringType(), True)])

```


Example 2: Retrieve the schema of the current DataFrame (DDL-formatted schema).

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")],
...     "age INT, name STRING")
>>> df.schema
StructType([StructField('age', IntegerType(), True),
            StructField('name', StringType(), True)])

```


Example 3: Retrieve the specified schema of the current DataFrame.

```
>>> from pyspark.sql.types import StructType, StructField, StringType
>>> df = spark.createDataFrame(
...     [("a",), ("b",), ("c",)],
...     StructType([StructField("value", StringType(), False)]))
>>> df.schema
StructType([StructField('value', StringType(), False)])

```

# pyspark.sql.DataFrame.select — PySpark 4.0.1 documentation
DataFrame.select(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.select)
[#](#pyspark.sql.DataFrame.select "Permalink to this definition")

Projects a set of expressions and returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**str, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), or list

column names (string) or expressions ([`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")). If one of the column names is ‘\*’, that column is expanded to include all columns in the current [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A DataFrame with subset (or all) of columns.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Select all columns in the DataFrame.

```
>>> df.select('*').show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Select a column with other expressions in the DataFrame.

```
>>> df.select(df.name, (df.age + 10).alias('age')).show()
+-----+---+
| name|age|
+-----+---+
|Alice| 12|
|  Bob| 15|
+-----+---+

```

# pyspark.sql.DataFrame.selectExpr — PySpark 4.0.1 documentation
DataFrame.selectExpr(_\*expr_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.selectExpr)
[#](#pyspark.sql.DataFrame.selectExpr "Permalink to this definition")

Projects a set of SQL expressions and returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This is a variant of [`select()`](about:blank/pyspark.sql.DataFrame.select.html#pyspark.sql.DataFrame.select "pyspark.sql.DataFrame.select") that accepts SQL expressions.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A DataFrame with new/old columns transformed by expressions.

Examples

```
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.selectExpr("age * 2", "abs(age)").show()
+---------+--------+
|(age * 2)|abs(age)|
+---------+--------+
|        4|       2|
|       10|       5|
+---------+--------+

```

# pyspark.sql.DataFrame.semanticHash — PySpark 4.0.1 documentation
DataFrame.semanticHash()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.semanticHash)
[#](#pyspark.sql.DataFrame.semanticHash "Permalink to this definition")

Returns a hash code of the logical query plan against this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 3.1.0.

Changed in version 3.5.0: Supports Spark Connect.

Returns

int

Hash value.

Notes

Unlike the standard hash code, the hash is calculated against the query plan simplified by tolerating the cosmetic differences such as attribute names.

This API is a developer API.

Examples

```
>>> spark.range(10).selectExpr("id as col0").semanticHash()  
1855039936
>>> spark.range(10).selectExpr("id as col1").semanticHash()  
1855039936

```



# pyspark.sql.DataFrame.show — PySpark 4.0.1 documentation
DataFrame.show(_n\=20_, _truncate\=True_, _vertical\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.show)
[#](#pyspark.sql.DataFrame.show "Permalink to this definition")

Prints the first `n` rows of the DataFrame to the console.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**n**int, optional, default 20

Number of rows to show.

**truncate**bool or int, optional, default True

If set to `True`, truncate strings longer than 20 chars. If set to a number greater than one, truncates long strings to length `truncate` and align cells right.

**vertical**bool, optional

If set to `True`, print output rows vertically (one line per column value).

Examples

```
>>> df = spark.createDataFrame([
...     (14, "Tom"), (23, "Alice"), (16, "Bob"), (19, "This is a super long name")],
...     ["age", "name"])

```


Show [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

```
>>> df.show()
+---+--------------------+
|age|                name|
+---+--------------------+
| 14|                 Tom|
| 23|               Alice|
| 16|                 Bob|
| 19|This is a super l...|
+---+--------------------+

```


Show only top 2 rows.

```
>>> df.show(2)
+---+-----+
|age| name|
+---+-----+
| 14|  Tom|
| 23|Alice|
+---+-----+
only showing top 2 rows

```


Show full column content without truncation.

```
>>> df.show(truncate=False)
+---+-------------------------+
|age|name                     |
+---+-------------------------+
|14 |Tom                      |
|23 |Alice                    |
|16 |Bob                      |
|19 |This is a super long name|
+---+-------------------------+

```


Show [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") where the maximum number of characters is 3.

```
>>> df.show(truncate=3)
+---+----+
|age|name|
+---+----+
| 14| Tom|
| 23| Ali|
| 16| Bob|
| 19| Thi|
+---+----+

```


Show [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") vertically.

```
>>> df.show(vertical=True)
-RECORD 0--------------------
age  | 14
name | Tom
-RECORD 1--------------------
age  | 23
name | Alice
-RECORD 2--------------------
age  | 16
name | Bob
-RECORD 3--------------------
age  | 19
name | This is a super l...

```


# pyspark.sql.DataFrame.sort — PySpark 4.0.1 documentation
DataFrame.sort(_\*cols_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.sort)
[#](#pyspark.sql.DataFrame.sort "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") sorted by the specified column(s).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**int, str, list, or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

> list of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column names or column ordinals to sort by.

Changed in version 4.0.0: Supports column ordinal.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Sorted DataFrame.

Other Parameters

**ascending**bool or list, optional, default True

boolean or list of boolean. Sort ascending vs. descending. Specify list for multiple sort orders. If a list is specified, the length of the list must equal the length of the cols.

Notes

A column ordinal starts from 1, which is different from the 0-based [`__getitem__()`](about:blank/pyspark.sql.DataFrame.__getitem__.html#pyspark.sql.DataFrame.__getitem__ "pyspark.sql.DataFrame.__getitem__"). If a column ordinal is negative, it means sort descending.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Sort the DataFrame in ascending order.

```
>>> df.sort(sf.asc("age")).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


```
>>> df.sort(1).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Sort the DataFrame in descending order.

```
>>> df.sort(df.age.desc()).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.orderBy(df.age.desc()).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.sort("age", ascending=False).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.sort(-1).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```


Specify multiple columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (2, "Alice"), (2, "Bob"), (5, "Bob")], schema=["age", "name"])
>>> df.orderBy(sf.desc("age"), "name").show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
|  2|  Bob|
+---+-----+

```


```
>>> df.orderBy(-1, "name").show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
|  2|  Bob|
+---+-----+

```


```
>>> df.orderBy(-1, 2).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
|  2|  Bob|
+---+-----+

```


Specify multiple columns for sorting order at ascending.

```
>>> df.orderBy(["age", "name"], ascending=[False, False]).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.orderBy([1, "name"], ascending=[False, False]).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|  Bob|
|  2|Alice|
+---+-----+

```


```
>>> df.orderBy([1, 2], ascending=[False, False]).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|  Bob|
|  2|Alice|
+---+-----+

```


# pyspark.sql.DataFrame.sortWithinPartitions — PySpark 4.0.1 documentation
DataFrame.sortWithinPartitions(_\*cols_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.sortWithinPartitions)
[#](#pyspark.sql.DataFrame.sortWithinPartitions "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") with each partition sorted by the specified column(s).

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**int, str, list or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

list of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column names or column ordinals to sort by.

Changed in version 4.0.0: Supports column ordinal.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame sorted by partitions.

Other Parameters

**ascending**bool or list, optional, default True

boolean or list of boolean. Sort ascending vs. descending. Specify list for multiple sort orders. If a list is specified, the length of the list must equal the length of the cols.

Notes

A column ordinal starts from 1, which is different from the 0-based [`__getitem__()`](about:blank/pyspark.sql.DataFrame.__getitem__.html#pyspark.sql.DataFrame.__getitem__ "pyspark.sql.DataFrame.__getitem__"). If a column ordinal is negative, it means sort descending.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.sortWithinPartitions("age", ascending=False)
DataFrame[age: bigint, name: string]

```


```
>>> df.coalesce(1).sortWithinPartitions(1).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


```
>>> df.coalesce(1).sortWithinPartitions(-1).show()
+---+-----+
|age| name|
+---+-----+
|  5|  Bob|
|  2|Alice|
+---+-----+

```



# pyspark.sql.DataFrame.sparkSession — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.sparkSession

_property_ DataFrame.sparkSession[#](#pyspark.sql.DataFrame.sparkSession "Permalink to this definition")

Returns Spark session that created this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`SparkSession`](about:blank/pyspark.sql.SparkSession.html#pyspark.sql.SparkSession "pyspark.sql.SparkSession")

Examples

```
>>> df = spark.range(1)
>>> type(df.sparkSession)
<class '...session.SparkSession'>

```


# pyspark.sql.DataFrame.stat — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.stat

_property_ DataFrame.stat[#](#pyspark.sql.DataFrame.stat "Permalink to this definition")

Returns a [`DataFrameStatFunctions`](about:blank/pyspark.sql.DataFrameStatFunctions.html#pyspark.sql.DataFrameStatFunctions "pyspark.sql.DataFrameStatFunctions") for statistic functions.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrameStatFunctions`](about:blank/pyspark.sql.DataFrameStatFunctions.html#pyspark.sql.DataFrameStatFunctions "pyspark.sql.DataFrameStatFunctions")

Examples

```
>>> import pyspark.sql.functions as f
>>> df = spark.range(3).withColumn("c", f.expr("id + 1"))
>>> type(df.stat)
<class '...dataframe.DataFrameStatFunctions'>
>>> df.stat.corr("id", "c")
1.0

```

# pyspark.sql.DataFrame.storageLevel — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.storageLevel

_property_ DataFrame.storageLevel[#](#pyspark.sql.DataFrame.storageLevel "Permalink to this definition")

Get the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")’s current storage level.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

`StorageLevel`

Currently defined storage level.

Examples

```
>>> df1 = spark.range(10)
>>> df1.storageLevel
StorageLevel(False, False, False, False, 1)
>>> df1.cache().storageLevel
StorageLevel(True, True, False, True, 1)

```


```
>>> df2 = spark.range(5)
>>> df2.persist(StorageLevel.DISK_ONLY_2).storageLevel
StorageLevel(True, False, False, False, 2)

```



# pyspark.sql.DataFrame.subtract — PySpark 4.0.1 documentation
DataFrame.subtract(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.subtract)
[#](#pyspark.sql.DataFrame.subtract "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing rows in this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") but not in another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that needs to be subtracted.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Subtracted DataFrame.

Notes

This is equivalent to EXCEPT DISTINCT in SQL.

Examples

Example 1: Subtracting two DataFrames with the same schema

```
>>> df1 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3), ("c", 4)], ["C1", "C2"])
>>> df2 = spark.createDataFrame([("a", 1), ("a", 1), ("b", 3)], ["C1", "C2"])
>>> result_df = df1.subtract(df2)
>>> result_df.show()
+---+---+
| C1| C2|
+---+---+
|  c|  4|
+---+---+

```


Example 2: Subtracting two DataFrames with different schemas

```
>>> df1 = spark.createDataFrame([(1, "A"), (2, "B")], ["id", "value"])
>>> df2 = spark.createDataFrame([(2, "B"), (3, "C")], ["id", "value"])
>>> result_df = df1.subtract(df2)
>>> result_df.show()
+---+-----+
| id|value|
+---+-----+
|  1|    A|
+---+-----+

```


Example 3: Subtracting two DataFrames with mismatched columns

```
>>> df1 = spark.createDataFrame([(1, 2)], ["A", "B"])
>>> df2 = spark.createDataFrame([(1, 2)], ["C", "D"])
>>> result_df = df1.subtract(df2)
>>> result_df.show()
+---+---+
|  A|  B|
+---+---+
+---+---+

```


# pyspark.sql.DataFrame.summary — PySpark 4.0.1 documentation
DataFrame.summary(_\*statistics_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.summary)
[#](#pyspark.sql.DataFrame.summary "Permalink to this definition")

Computes specified statistics for numeric and string columns. Available statistics are: - count - mean - stddev - min - max - arbitrary approximate percentiles specified as a percentage (e.g., 75%)

If no statistics are given, this function computes count, mean, stddev, min, approximate quartiles (percentiles at 25%, 50%, and 75%), and max.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**statistics**str, optional

Column names to calculate statistics by (default All columns).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new DataFrame that provides statistics for the given DataFrame.

Notes

This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Examples

```
>>> df = spark.createDataFrame(
...     [("Bob", 13, 40.3, 150.5), ("Alice", 12, 37.8, 142.3), ("Tom", 11, 44.1, 142.2)],
...     ["name", "age", "weight", "height"],
... )
>>> df.select("age", "weight", "height").summary().show()
+-------+----+------------------+-----------------+
|summary| age|            weight|           height|
+-------+----+------------------+-----------------+
|  count|   3|                 3|                3|
|   mean|12.0| 40.73333333333333|            145.0|
| stddev| 1.0|3.1722757341273704|4.763402145525822|
|    min|  11|              37.8|            142.2|
|    25%|  11|              37.8|            142.2|
|    50%|  12|              40.3|            142.3|
|    75%|  13|              44.1|            150.5|
|    max|  13|              44.1|            150.5|
+-------+----+------------------+-----------------+

```


```
>>> df.select("age", "weight", "height").summary("count", "min", "25%", "75%", "max").show()
+-------+---+------+------+
|summary|age|weight|height|
+-------+---+------+------+
|  count|  3|     3|     3|
|    min| 11|  37.8| 142.2|
|    25%| 11|  37.8| 142.2|
|    75%| 13|  44.1| 150.5|
|    max| 13|  44.1| 150.5|
+-------+---+------+------+

```

# pyspark.sql.DataFrame.tail — PySpark 4.0.1 documentation
DataFrame.tail(_num_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.tail)
[#](#pyspark.sql.DataFrame.tail "Permalink to this definition")

Returns the last `num` rows as a `list` of [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row").

Running tail requires moving data into the application’s driver process, and doing so with a very large `num` can crash the driver process with OutOfMemoryError.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**num**int

Number of records to return. Will return this number of records or all records if the DataFrame contains less than this number of records.

Returns

list

List of rows

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

```


```
>>> df.tail(2)
[Row(age=23, name='Alice'), Row(age=16, name='Bob')]

```
# pyspark.sql.DataFrame.take — PySpark 4.0.1 documentation
DataFrame.take(_num_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.take)
[#](#pyspark.sql.DataFrame.take "Permalink to this definition")

Returns the first `num` rows as a `list` of [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.Row").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**num**int

Number of records to return. Will return this number of records or all records if the DataFrame contains less than this number of records..

Returns

list

List of rows

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

```


Return the first 2 rows of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

```
>>> df.take(2)
[Row(age=14, name='Tom'), Row(age=23, name='Alice')]

```

# pyspark.sql.DataFrame.to — PySpark 4.0.1 documentation
DataFrame.to(_schema_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.to)
[#](#pyspark.sql.DataFrame.to "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") where each row is reconciled to match the specified schema.

New in version 3.4.0.

Parameters

**schema**`StructType`

Specified schema.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Reconciled DataFrame.

Notes

*   Reorder columns and/or inner fields by name to match the specified schema.
    
*   Project away columns and/or inner fields that are not needed by the specified schema.
    
    Missing columns and/or inner fields (present in the specified schema but not input DataFrame) lead to failures.
    
*   Cast the columns and/or inner fields to match the data types in the specified schema,
    
    if the types are compatible, e.g., numeric to numeric (error if overflows), but not string to int.
    
*   Carry over the metadata from the specified schema, while the columns and/or inner fields
    
    still keep their own metadata if not overwritten by the specified schema.
    
*   Fail if the nullability is not compatible. For example, the column and/or inner field
    
    is nullable but the specified schema requires them to be not nullable.
    

Supports Spark Connect.

Examples

```
>>> from pyspark.sql.types import StructField, StringType
>>> df = spark.createDataFrame([("a", 1)], ["i", "j"])
>>> df.schema
StructType([StructField('i', StringType(), True), StructField('j', LongType(), True)])

```


```
>>> schema = StructType([StructField("j", StringType()), StructField("i", StringType())])
>>> df2 = df.to(schema)
>>> df2.schema
StructType([StructField('j', StringType(), True), StructField('i', StringType(), True)])
>>> df2.show()
+---+---+
|  j|  i|
+---+---+
|  1|  a|
+---+---+

```


# pyspark.sql.DataFrame.toArrow — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.toArrow

DataFrame.toArrow()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.toArrow)
[#](#pyspark.sql.DataFrame.toArrow "Permalink to this definition")

Returns the contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as PyArrow `pyarrow.Table`.

This is only available if PyArrow is installed and available.

New in version 4.0.0.

Notes

This method should only be used if the resulting PyArrow `pyarrow.Table` is expected to be small, as all the data is loaded into the driver’s memory.

This API is a developer API.

Examples

```
>>> df.toArrow()  
pyarrow.Table
age: int64
name: string
----
age: [[2,5]]
name: [["Alice","Bob"]]

```



# pyspark.sql.DataFrame.toDF — PySpark 4.0.1 documentation
DataFrame.toDF(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.toDF)
[#](#pyspark.sql.DataFrame.toDF "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that with new specified column names

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**\*cols**tuple

a tuple of string new column name. The length of the list needs to be the same as the number of columns in the initial [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with new column names.

Examples

```
>>> df = spark.createDataFrame([(14, "Tom"), (23, "Alice"),
...     (16, "Bob")], ["age", "name"])
>>> df.toDF('f1', 'f2').show()
+---+-----+
| f1|   f2|
+---+-----+
| 14|  Tom|
| 23|Alice|
| 16|  Bob|
+---+-----+

```



# pyspark.sql.DataFrame.toJSON — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.toJSON

DataFrame.toJSON(_use\_unicode\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.toJSON)
[#](#pyspark.sql.DataFrame.toJSON "Permalink to this definition")

Converts a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") into a `RDD` of string.

Each row is turned into a JSON document as one element in the returned RDD.

New in version 1.3.0.

Parameters

**use\_unicode**bool, optional, default True

Whether to convert to unicode or not.

Returns

`RDD`

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.toJSON().first()
'{"age":2,"name":"Alice"}'

```



# pyspark.sql.DataFrame.toLocalIterator — PySpark 4.0.1 documentation
DataFrame.toLocalIterator(_prefetchPartitions\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.toLocalIterator)
[#](#pyspark.sql.DataFrame.toLocalIterator "Permalink to this definition")

Returns an iterator that contains all of the rows in this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). The iterator will consume as much memory as the largest partition in this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). With prefetch it may consume up to the memory of the 2 largest partitions.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**prefetchPartitions**bool, optional

If Spark should pre-fetch the next partition before it is needed.

Changed in version 3.4.0: This argument does not take effect for Spark Connect.

Returns

Iterator

Iterator of rows.

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> list(df.toLocalIterator())
[Row(age=14, name='Tom'), Row(age=23, name='Alice'), Row(age=16, name='Bob')]

```


# pyspark.sql.DataFrame.toPandas — PySpark 4.0.1 documentation
DataFrame.toPandas()
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.toPandas)
[#](#pyspark.sql.DataFrame.toPandas "Permalink to this definition")

Returns the contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as Pandas `pandas.DataFrame`.

This is only available if Pandas is installed and available.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Notes

This method should only be used if the resulting Pandas `pandas.DataFrame` is expected to be small, as all the data is loaded into the driver’s memory.

Usage with `spark.sql.execution.arrow.pyspark.enabled=True` is experimental.

Examples

```
>>> df.toPandas()  
   age   name
0    2  Alice
1    5    Bob

```

# pyspark.sql.DataFrame.transform — PySpark 4.0.1 documentation
DataFrame.transform(_func_, _\*args_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.transform)
[#](#pyspark.sql.DataFrame.transform "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). Concise syntax for chaining custom transformations.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**func**function

a function that takes and returns a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

**\*args**

Positional arguments to pass to func.

New in version 3.3.0.

**\*\*kwargs**

Keyword arguments to pass to func.

New in version 3.3.0.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Transformed DataFrame.

Examples

```
>>> from pyspark.sql.functions import col
>>> df = spark.createDataFrame([(1, 1.0), (2, 2.0)], ["int", "float"])
>>> def cast_all_to_int(input_df):
...     return input_df.select([col(col_name).cast("int") for col_name in input_df.columns])
...
>>> def sort_columns_asc(input_df):
...     return input_df.select(*sorted(input_df.columns))
...
>>> df.transform(cast_all_to_int).transform(sort_columns_asc).show()
+-----+---+
|float|int|
+-----+---+
|    1|  1|
|    2|  2|
+-----+---+

```


```
>>> def add_n(input_df, n):
...     return input_df.select([(col(col_name) + n).alias(col_name)
...                             for col_name in input_df.columns])
>>> df.transform(add_n, 1).transform(add_n, n=10).show()
+---+-----+
|int|float|
+---+-----+
| 12| 12.0|
| 13| 13.0|
+---+-----+

```

# pyspark.sql.DataFrame.transpose — PySpark 4.0.1 documentation
DataFrame.transpose(_indexColumn\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.transpose)
[#](#pyspark.sql.DataFrame.transpose "Permalink to this definition")

Transposes a DataFrame such that the values in the specified index column become the new columns of the DataFrame. If no index column is provided, the first column is used as the default.

Please note: - All columns except the index column must share a least common data type. Unless they are the same data type, all columns are cast to the nearest common data type. - The name of the column into which the original column names are transposed defaults to “key”. - null values in the index column are excluded from the column names for the transposed table, which are ordered in ascending order.

New in version 4.0.0.

Parameters

**indexColumn**str or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

The single column that will be treated as the index for the transpose operation. This column will be used to transform the DataFrame such that the values of the indexColumn become the new columns in the transposed DataFrame. If not provided, the first column of the DataFrame will be used as the default.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Transposed DataFrame.

Notes

Supports Spark Connect.

Examples

```
>>> df = spark.createDataFrame(
...     [("A", 1, 2), ("B", 3, 4)],
...     ["id", "val1", "val2"],
... )
>>> df.show()
+---+----+----+
| id|val1|val2|
+---+----+----+
|  A|   1|   2|
|  B|   3|   4|
+---+----+----+

```


```
>>> df.transpose().show()
+----+---+---+
| key|  A|  B|
+----+---+---+
|val1|  1|  3|
|val2|  2|  4|
+----+---+---+

```


```
>>> df.transpose(df.id).show()
+----+---+---+
| key|  A|  B|
+----+---+---+
|val1|  1|  3|
|val2|  2|  4|
+----+---+---+

```


# pyspark.sql.DataFrame.union — PySpark 4.0.1 documentation
DataFrame.union(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.union)
[#](#pyspark.sql.DataFrame.union "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing the union of rows in this and another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that needs to be unioned.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing the combined rows with corresponding columns.

Notes

This method performs a SQL-style set union of the rows from both DataFrame objects, with no automatic deduplication of elements.

Use the distinct() method to perform deduplication of rows.

The method resolves columns by position (not by name), following the standard behavior in SQL.

Examples

Example 1: Combining two DataFrames with the same schema

```
>>> df1 = spark.createDataFrame([(1, 'A'), (2, 'B')], ['id', 'value'])
>>> df2 = spark.createDataFrame([(3, 'C'), (4, 'D')], ['id', 'value'])
>>> df3 = df1.union(df2)
>>> df3.show()
+---+-----+
| id|value|
+---+-----+
|  1|    A|
|  2|    B|
|  3|    C|
|  4|    D|
+---+-----+

```


Example 2: Combining two DataFrames with different schemas

```
>>> from pyspark.sql.functions import lit
>>> df1 = spark.createDataFrame([(100001, 1), (100002, 2)], schema="id LONG, money INT")
>>> df2 = spark.createDataFrame([(3, 100003), (4, 100003)], schema="money INT, id LONG")
>>> df1 = df1.withColumn("age", lit(30))
>>> df2 = df2.withColumn("age", lit(40))
>>> df3 = df1.union(df2)
>>> df3.show()
+------+------+---+
|    id| money|age|
+------+------+---+
|100001|     1| 30|
|100002|     2| 30|
|     3|100003| 40|
|     4|100003| 40|
+------+------+---+

```


Example 3: Combining two DataFrames with mismatched columns

```
>>> df1 = spark.createDataFrame([(1, 2)], ["A", "B"])
>>> df2 = spark.createDataFrame([(3, 4)], ["C", "D"])
>>> df3 = df1.union(df2)
>>> df3.show()
+---+---+
|  A|  B|
+---+---+
|  1|  2|
|  3|  4|
+---+---+

```


Example 4: Combining duplicate rows from two different DataFrames

```
>>> df1 = spark.createDataFrame([(1, 'A'), (2, 'B'), (3, 'C')], ['id', 'value'])
>>> df2 = spark.createDataFrame([(3, 'C'), (4, 'D')], ['id', 'value'])
>>> df3 = df1.union(df2).distinct().sort("id")
>>> df3.show()
+---+-----+
| id|value|
+---+-----+
|  1|    A|
|  2|    B|
|  3|    C|
|  4|    D|
+---+-----+

```




# pyspark.sql.DataFrame.unionAll — PySpark 4.0.1 documentation
DataFrame.unionAll(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.unionAll)
[#](#pyspark.sql.DataFrame.unionAll "Permalink to this definition")

Return a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing the union of rows in this and another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that needs to be combined

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing combined rows from both dataframes.

Notes

This method combines all rows from both DataFrame objects with no automatic deduplication of elements.

Use the distinct() method to perform deduplication of rows.

[`unionAll()`](#pyspark.sql.DataFrame.unionAll "pyspark.sql.DataFrame.unionAll") is an alias to [`union()`](about:blank/pyspark.sql.DataFrame.union.html#pyspark.sql.DataFrame.union "pyspark.sql.DataFrame.union")


# pyspark.sql.DataFrame.unionByName — PySpark 4.0.1 documentation
DataFrame.unionByName(_other_, _allowMissingColumns\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.unionByName)
[#](#pyspark.sql.DataFrame.unionByName "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing union of rows in this and another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This method performs a union operation on both input DataFrames, resolving columns by name (rather than position). When allowMissingColumns is True, missing columns will be filled with null.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Another [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that needs to be combined.

**allowMissingColumns**bool, optional, default False

Specify whether to allow missing columns.

New in version 3.1.0.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") containing the combined rows with corresponding columns of the two given DataFrames.

Examples

Example 1: Union of two DataFrames with same columns in different order.

```
>>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
>>> df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col0"])
>>> df1.unionByName(df2).show()
+----+----+----+
|col0|col1|col2|
+----+----+----+
|   1|   2|   3|
|   6|   4|   5|
+----+----+----+

```


Example 2: Union with missing columns and setting allowMissingColumns=True.

```
>>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
>>> df2 = spark.createDataFrame([[4, 5, 6]], ["col1", "col2", "col3"])
>>> df1.unionByName(df2, allowMissingColumns=True).show()
+----+----+----+----+
|col0|col1|col2|col3|
+----+----+----+----+
|   1|   2|   3|NULL|
|NULL|   4|   5|   6|
+----+----+----+----+

```


Example 3: Union of two DataFrames with few common columns.

```
>>> df1 = spark.createDataFrame([[1, 2, 3]], ["col0", "col1", "col2"])
>>> df2 = spark.createDataFrame([[4, 5, 6, 7]], ["col1", "col2", "col3", "col4"])
>>> df1.unionByName(df2, allowMissingColumns=True).show()
+----+----+----+----+----+
|col0|col1|col2|col3|col4|
+----+----+----+----+----+
|   1|   2|   3|NULL|NULL|
|NULL|   4|   5|   6|   7|
+----+----+----+----+----+

```


Example 4: Union of two DataFrames with completely different columns.

```
>>> df1 = spark.createDataFrame([[0, 1, 2]], ["col0", "col1", "col2"])
>>> df2 = spark.createDataFrame([[3, 4, 5]], ["col3", "col4", "col5"])
>>> df1.unionByName(df2, allowMissingColumns=True).show()
+----+----+----+----+----+----+
|col0|col1|col2|col3|col4|col5|
+----+----+----+----+----+----+
|   0|   1|   2|NULL|NULL|NULL|
|NULL|NULL|NULL|   3|   4|   5|
+----+----+----+----+----+----+

```


# pyspark.sql.DataFrame.unpersist — PySpark 4.0.1 documentation
DataFrame.unpersist(_blocking\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.unpersist)
[#](#pyspark.sql.DataFrame.unpersist "Permalink to this definition")

Marks the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as non-persistent, and remove all blocks for it from memory and disk.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**blocking**bool

Whether to block until all blocks are deleted.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Unpersisted DataFrame.

Notes

blocking default has changed to `False` to match Scala in 2.0.

Examples

```
>>> df = spark.range(1)
>>> df.persist()
DataFrame[id: bigint]
>>> df.unpersist()
DataFrame[id: bigint]
>>> df = spark.range(1)
>>> df.unpersist(True)
DataFrame[id: bigint]

```


# pyspark.sql.DataFrame.unpivot — PySpark 4.0.1 documentation
DataFrame.unpivot(_ids_, _values_, _variableColumnName_, _valueColumnName_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.unpivot)
[#](#pyspark.sql.DataFrame.unpivot "Permalink to this definition")

Unpivot a DataFrame from wide format to long format, optionally leaving identifier columns set. This is the reverse to groupBy(…).pivot(…).agg(…), except for the aggregation, which cannot be reversed.

This function is useful to massage a DataFrame into a format where some columns are identifier columns (“ids”), while all other columns (“values”) are “unpivoted” to the rows, leaving just two non-id columns, named as given by variableColumnName and valueColumnName.

When no “id” columns are given, the unpivoted DataFrame consists of only the “variable” and “value” columns.

The values columns must not be empty so at least one value must be given to be unpivoted. When values is None, all non-id columns will be unpivoted.

All “value” columns must share a least common data type. Unless they are the same data type, all “value” columns are cast to the nearest common data type. For instance, types IntegerType and LongType are cast to LongType, while IntegerType and StringType do not have a common data type and unpivot fails.

New in version 3.4.0.

Parameters

**ids**str, Column, tuple, list

Column(s) to use as identifiers. Can be a single column or column name, or a list or tuple for multiple columns.

**values**str, Column, tuple, list, optional

Column(s) to unpivot. Can be a single column or column name, or a list or tuple for multiple columns. If specified, must not be empty. If not specified, uses all columns that are not set as ids.

**variableColumnName**str

Name of the variable column.

**valueColumnName**str

Name of the value column.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Unpivoted DataFrame.

Notes

Supports Spark Connect.

Examples

```
>>> df = spark.createDataFrame(
...     [(1, 11, 1.1), (2, 12, 1.2)],
...     ["id", "int", "double"],
... )
>>> df.show()
+---+---+------+
| id|int|double|
+---+---+------+
|  1| 11|   1.1|
|  2| 12|   1.2|
+---+---+------+

```


```
>>> df.unpivot("id", ["int", "double"], "var", "val").show()
+---+------+----+
| id|   var| val|
+---+------+----+
|  1|   int|11.0|
|  1|double| 1.1|
|  2|   int|12.0|
|  2|double| 1.2|
+---+------+----+

```

# pyspark.sql.DataFrame.where — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.DataFrame.where

DataFrame.where(_condition_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.where)
[#](#pyspark.sql.DataFrame.where "Permalink to this definition")

[`where()`](#pyspark.sql.DataFrame.where "pyspark.sql.DataFrame.where") is an alias for [`filter()`](about:blank/pyspark.sql.DataFrame.filter.html#pyspark.sql.DataFrame.filter "pyspark.sql.DataFrame.filter").

New in version 1.3.0.


# pyspark.sql.DataFrame.withColumn — PySpark 4.0.1 documentation
DataFrame.withColumn(_colName_, _col_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.withColumn)
[#](#pyspark.sql.DataFrame.withColumn "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by adding a column or replacing the existing column that has the same name.

The column expression must be an expression over this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"); attempting to add a column from some other [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") will raise an error.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**colName**str

string, name of the new column.

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression for the new column.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with new or replaced column.

Notes

This method introduces a projection internally. Therefore, calling it multiple times, for instance, via loops in order to add multiple columns can generate big plans which can cause performance issues and even StackOverflowException. To avoid this, use [`select()`](about:blank/pyspark.sql.DataFrame.select.html#pyspark.sql.DataFrame.select "pyspark.sql.DataFrame.select") with multiple columns at once.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.withColumn('age2', df.age + 2).show()
+---+-----+----+
|age| name|age2|
+---+-----+----+
|  2|Alice|   4|
|  5|  Bob|   7|
+---+-----+----+

```

# pyspark.sql.DataFrame.withColumns — PySpark 4.0.1 documentation
DataFrame.withColumns(_\*colsMap_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.withColumns)
[#](#pyspark.sql.DataFrame.withColumns "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by adding multiple columns or replacing the existing columns that have the same names.

The colsMap is a map of column name and column, the column must only refer to attributes supplied by this Dataset. It is an error to add columns that refer to some other Dataset.

New in version 3.3.0: Added support for multiple columns adding

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**colsMap**dict

a dict of column name and [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"). Currently, only a single map is supported.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with new or replaced columns.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df.withColumns({'age2': df.age + 2, 'age3': df.age + 3}).show()
+---+-----+----+----+
|age| name|age2|age3|
+---+-----+----+----+
|  2|Alice|   4|   5|
|  5|  Bob|   7|   8|
+---+-----+----+----+

```



# pyspark.sql.DataFrame.withColumnRenamed — PySpark 4.0.1 documentation
DataFrame.withColumnRenamed(_existing_, _new_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.withColumnRenamed)
[#](#pyspark.sql.DataFrame.withColumnRenamed "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by renaming an existing column. This is a no-op if the schema doesn’t contain the given column name.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**existing**str

The name of the existing column to be renamed.

**new**str

The new name to be assigned to the column.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A new DataFrame with renamed column.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Example 1: Rename a single column

```
>>> df.withColumnRenamed("age", "age2").show()
+----+-----+
|age2| name|
+----+-----+
|   2|Alice|
|   5|  Bob|
+----+-----+

```


Example 2: Rename a column that does not exist (no-op)

```
>>> df.withColumnRenamed("non_existing", "new_name").show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Example 3: Rename multiple columns

```
>>> df.withColumnRenamed("age", "age2").withColumnRenamed("name", "name2").show()
+----+-----+
|age2|name2|
+----+-----+
|   2|Alice|
|   5|  Bob|
+----+-----+

```


# pyspark.sql.DataFrame.withColumnsRenamed — PySpark 4.0.1 documentation
DataFrame.withColumnsRenamed(_colsMap_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.withColumnsRenamed)
[#](#pyspark.sql.DataFrame.withColumnsRenamed "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by renaming multiple columns. This is a no-op if the schema doesn’t contain the given column names.

New in version 3.4.0: Added support for multiple columns renaming

Parameters

**colsMap**dict

A dict of existing column names and corresponding desired column names. Currently, only a single map is supported.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with renamed columns.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])

```


Example 1: Rename a single column

```
>>> df.withColumnsRenamed({"age": "age2"}).show()
+----+-----+
|age2| name|
+----+-----+
|   2|Alice|
|   5|  Bob|
+----+-----+

```


Example 2: Rename multiple columns

```
>>> df.withColumnsRenamed({"age": "age2", "name": "name2"}).show()
+----+-----+
|age2|name2|
+----+-----+
|   2|Alice|
|   5|  Bob|
+----+-----+

```


Example 3: Rename non-existing column (no-op)

```
>>> df.withColumnsRenamed({"non_existing": "new_name"}).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


Example 4: Rename with an empty dictionary (no-op)

```
>>> df.withColumnsRenamed({}).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  5|  Bob|
+---+-----+

```


# pyspark.sql.DataFrame.withMetadata — PySpark 4.0.1 documentation
DataFrame.withMetadata(_columnName_, _metadata_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.withMetadata)
[#](#pyspark.sql.DataFrame.withMetadata "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") by updating an existing column with metadata.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**columnName**str

string, name of the existing column to update the metadata.

**metadata**dict

dict, new metadata to be assigned to df.schema\[columnName\].metadata

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with updated metadata column.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> df_meta = df.withMetadata('age', {'foo': 'bar'})
>>> df_meta.schema['age'].metadata
{'foo': 'bar'}

```


# pyspark.sql.DataFrame.withWatermark — PySpark 4.0.1 documentation
DataFrame.withWatermark(_eventTime_, _delayThreshold_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.withWatermark)
[#](#pyspark.sql.DataFrame.withWatermark "Permalink to this definition")

Defines an event time watermark for this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame"). A watermark tracks a point in time before which we assume no more late data is going to arrive.

Spark will use this watermark for several purposes:

*   To know when a given time window aggregation can be finalized and thus can be emitted when using output modes that do not allow updates.
    
*   To minimize the amount of state that we need to keep for on-going aggregations.
    

The current watermark is computed by looking at the MAX(eventTime) seen across all of the partitions in the query minus a user specified delayThreshold. Due to the cost of coordinating this value across partitions, the actual watermark used is only guaranteed to be at least delayThreshold behind the actual event time. In some cases we may still process records that arrive more than delayThreshold late.

New in version 2.1.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters

**eventTime**str

the name of the column that contains the event time of the row.

**delayThreshold**str

the minimum delay to wait to data to arrive late, relative to the latest record that has been processed in the form of an interval (e.g. “1 minute” or “5 hours”).

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Watermarked DataFrame

Notes

This is a feature only for Structured Streaming.

This API is evolving.

Examples

```
>>> from pyspark.sql import Row
>>> from pyspark.sql.functions import timestamp_seconds
>>> df = spark.readStream.format("rate").load().selectExpr(
...     "value % 5 AS value", "timestamp")
>>> df.select("value", df.timestamp.alias("time")).withWatermark("time", '10 minutes')
DataFrame[value: bigint, time: timestamp]

```


Group the data by window and value (0 - 4), and compute the count of each group.

```
>>> import time
>>> from pyspark.sql.functions import window
>>> query = (df
...     .withWatermark("timestamp", "10 minutes")
...     .groupBy(
...         window(df.timestamp, "10 minutes", "5 minutes"),
...         df.value)
...     ).count().writeStream.outputMode("complete").format("console").start()
>>> time.sleep(3)
>>> query.stop()

```


# pyspark.sql.DataFrame.write — PySpark 4.0.1 documentation
_property_ DataFrame.write[#](#pyspark.sql.DataFrame.write "Permalink to this definition")

Interface for saving the content of the non-streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") out into external storage.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrameWriter`](about:blank/pyspark.sql.DataFrameWriter.html#pyspark.sql.DataFrameWriter "pyspark.sql.DataFrameWriter")

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], schema=["age", "name"])
>>> type(df.write)
<class '...readwriter.DataFrameWriter'>

```


Write the DataFrame as a table.

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tab2")
>>> df.write.saveAsTable("tab2")
>>> _ = spark.sql("DROP TABLE tab2")

```


# pyspark.sql.DataFrame.writeStream — PySpark 4.0.1 documentation
_property_ DataFrame.writeStream[#](#pyspark.sql.DataFrame.writeStream "Permalink to this definition")

Interface for saving the content of the streaming [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") out into external storage.

New in version 2.0.0.

Changed in version 3.5.0: Supports Spark Connect.

Returns

`DataStreamWriter`

Notes

This API is evolving.

Examples

```
>>> import time
>>> import tempfile
>>> df = spark.readStream.format("rate").load()
>>> type(df.writeStream)
<class '...streaming.readwriter.DataStreamWriter'>

```


```
>>> with tempfile.TemporaryDirectory(prefix="writeStream") as d:
...     # Create a table with Rate source.
...     query = df.writeStream.toTable(
...         "my_table", checkpointLocation=d)
...     time.sleep(3)
...     query.stop()

```


# pyspark.sql.DataFrame.writeTo — PySpark 4.0.1 documentation
DataFrame.writeTo(_table_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.writeTo)
[#](#pyspark.sql.DataFrame.writeTo "Permalink to this definition")

Create a write configuration builder for v2 sources.

This builder is used to configure and execute write operations.

For example, to append or create or replace existing tables.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**table**str

Target table name to write to.

Returns

[`DataFrameWriterV2`](about:blank/pyspark.sql.DataFrameWriterV2.html#pyspark.sql.DataFrameWriterV2 "pyspark.sql.DataFrameWriterV2")

DataFrameWriterV2 to use further to specify how to save the data

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])
>>> df.writeTo("catalog.db.table").append()  
>>> df.writeTo(                              
...     "catalog.db.table"
... ).partitionedBy("col").createOrReplace()

```

# pyspark.sql.DataFrame.mergeInto — PySpark 4.0.1 documentation
DataFrame.mergeInto(_table_, _condition_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.mergeInto)
[#](#pyspark.sql.DataFrame.mergeInto "Permalink to this definition")

Merges a set of updates, insertions, and deletions based on a source table into a target table.

New in version 4.0.0.

Parameters

**table**str

Target table name to merge into.

**condition**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The condition that determines whether a row in the target table matches one in the source DataFrame.

Returns

`MergeIntoWriter`

MergeIntoWriter to use further to specify how to merge the source DataFrame into the target table.

Notes

This method does not support streaming queries.

Examples

```
>>> from pyspark.sql.functions import expr
>>> source = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["id", "name"])
>>> (source.mergeInto("target", "id")  
...     .whenMatched().update({ "name": source.name })
...     .whenNotMatched().insertAll()
...     .whenNotMatchedBySource().delete()
...     .merge())

```

# pyspark.sql.DataFrame.pandas_api — PySpark 4.0.1 documentation
DataFrame.pandas\_api(_index\_col\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrame.pandas_api)
[#](#pyspark.sql.DataFrame.pandas_api "Permalink to this definition")

Converts the existing DataFrame into a pandas-on-Spark DataFrame.

New in version 3.2.0.

Changed in version 3.5.0: Supports Spark Connect.

If a pandas-on-Spark DataFrame is converted to a Spark DataFrame and then back to pandas-on-Spark, it will lose the index information and the original index will be turned into a normal column.

This is only available if Pandas is installed and available.

Parameters

**index\_col: str or list of str, optional**

Index column of table in Spark.

Returns

`PandasOnSparkDataFrame`

See also

`pyspark.pandas.frame.DataFrame.to_spark`

Examples

```
>>> df = spark.createDataFrame(
...     [(14, "Tom"), (23, "Alice"), (16, "Bob")], ["age", "name"])

```


```
>>> df.pandas_api()  
   age   name
0   14    Tom
1   23  Alice
2   16    Bob

```


We can specify the index columns.

```
>>> df.pandas_api(index_col="age")  
      name
age
14     Tom
23   Alice
16     Bob

```

# pyspark.sql.DataFrameNaFunctions.drop — PySpark 4.0.1 documentation
DataFrameNaFunctions.drop(_how\='any'_, _thresh\=None_, _subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameNaFunctions.drop)
[#](#pyspark.sql.DataFrameNaFunctions.drop "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") omitting rows with null or NaN values. [`DataFrame.dropna()`](about:blank/pyspark.sql.DataFrame.dropna.html#pyspark.sql.DataFrame.dropna "pyspark.sql.DataFrame.dropna") and [`DataFrameNaFunctions.drop()`](#pyspark.sql.DataFrameNaFunctions.drop "pyspark.sql.DataFrameNaFunctions.drop") are aliases of each other.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**how**str, optional, the values that can be ‘any’ or ‘all’, default ‘any’.

If ‘any’, drop a row if it contains any nulls. If ‘all’, drop a row only if all its values are null.

**thresh: int, optional, default None.**

If specified, drop rows that have less than thresh non-null values. This overwrites the how parameter.

**subset**str, tuple or list, optional

optional list of column names to consider.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with null only rows excluded.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([
...     Row(age=10, height=80.0, name="Alice"),
...     Row(age=5, height=float("nan"), name="Bob"),
...     Row(age=None, height=None, name="Tom"),
...     Row(age=None, height=float("nan"), name=None),
... ])

```


Example 1: Drop the row if it contains any null or NaN.

```
>>> df.na.drop().show()
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
+---+------+-----+

```


Example 2: Drop the row only if all its values are null or NaN.

```
>>> df.na.drop(how='all').show()
+----+------+-----+
| age|height| name|
+----+------+-----+
|  10|  80.0|Alice|
|   5|   NaN|  Bob|
|NULL|  NULL|  Tom|
+----+------+-----+

```


Example 3: Drop rows that have less than thresh non-null and non-NaN values.

```
>>> df.na.drop(thresh=2).show()
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
|  5|   NaN|  Bob|
+---+------+-----+

```


Example 4: Drop rows with null and NaN values in the specified columns.

```
>>> df.na.drop(subset=['age', 'name']).show()
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
|  5|   NaN|  Bob|
+---+------+-----+

```

# pyspark.sql.DataFrameNaFunctions.fill — PySpark 4.0.1 documentation
DataFrameNaFunctions.fill(_value_, _subset\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameNaFunctions.fill)
[#](#pyspark.sql.DataFrameNaFunctions.fill "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") which null values are filled with new value. [`DataFrame.fillna()`](about:blank/pyspark.sql.DataFrame.fillna.html#pyspark.sql.DataFrame.fillna "pyspark.sql.DataFrame.fillna") and [`DataFrameNaFunctions.fill()`](#pyspark.sql.DataFrameNaFunctions.fill "pyspark.sql.DataFrameNaFunctions.fill") are aliases of each other.

New in version 1.3.1.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**value**int, float, string, bool or dict, the value to replace null values with.

If the value is a dict, then subset is ignored and value must be a mapping from column name (string) to replacement value. The replacement value must be an int, float, boolean, or string.

**subset**str, tuple or list, optional

optional list of column names to consider. Columns specified in subset that do not have matching data types are ignored. For example, if value is a string, and subset contains a non-string column, then the non-string column is simply ignored.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with replaced null values.

Examples

```
>>> df = spark.createDataFrame([
...     (10, 80.5, "Alice", None),
...     (5, None, "Bob", None),
...     (None, None, "Tom", None),
...     (None, None, None, True)],
...     schema=["age", "height", "name", "bool"])

```


Example 1: Fill all null values with 50 for numeric columns.

```
>>> df.na.fill(50).show()
+---+------+-----+----+
|age|height| name|bool|
+---+------+-----+----+
| 10|  80.5|Alice|NULL|
|  5|  50.0|  Bob|NULL|
| 50|  50.0|  Tom|NULL|
| 50|  50.0| NULL|true|
+---+------+-----+----+

```


Example 2: Fill all null values with `False` for boolean columns.

```
>>> df.na.fill(False).show()
+----+------+-----+-----+
| age|height| name| bool|
+----+------+-----+-----+
|  10|  80.5|Alice|false|
|   5|  NULL|  Bob|false|
|NULL|  NULL|  Tom|false|
|NULL|  NULL| NULL| true|
+----+------+-----+-----+

```


Example 3: Fill all null values with to 50 and “unknown” for

‘age’ and ‘name’ column respectively.

```
>>> df.na.fill({'age': 50, 'name': 'unknown'}).show()
+---+------+-------+----+
|age|height|   name|bool|
+---+------+-------+----+
| 10|  80.5|  Alice|NULL|
|  5|  NULL|    Bob|NULL|
| 50|  NULL|    Tom|NULL|
| 50|  NULL|unknown|true|
+---+------+-------+----+

```


Example 4: Fill all null values with “Spark” for ‘name’ column.

```
>>> df.na.fill(value = 'Spark', subset = 'name').show()
+----+------+-----+----+
| age|height| name|bool|
+----+------+-----+----+
|  10|  80.5|Alice|NULL|
|   5|  NULL|  Bob|NULL|
|NULL|  NULL|  Tom|NULL|
|NULL|  NULL|Spark|true|
+----+------+-----+----+

```


# pyspark.sql.DataFrameNaFunctions.replace — PySpark 4.0.1 documentation
DataFrameNaFunctions.replace(_to\_replace_, _value=<no value>_, _subset=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameNaFunctions.replace)
[#](#pyspark.sql.DataFrameNaFunctions.replace "Permalink to this definition")

Returns a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") replacing a value with another value. [`DataFrame.replace()`](about:blank/pyspark.sql.DataFrame.replace.html#pyspark.sql.DataFrame.replace "pyspark.sql.DataFrame.replace") and [`DataFrameNaFunctions.replace()`](#pyspark.sql.DataFrameNaFunctions.replace "pyspark.sql.DataFrameNaFunctions.replace") are aliases of each other. Values to\_replace and value must have the same type and can only be numerics, booleans, or strings. Value can have None. When replacing, the new value will be cast to the type of the existing column. For numeric replacements all values to be replaced should have unique floating point representation. In case of conflicts (for example with {42: -1, 42.0: 1}) and arbitrary replacement will be used.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**to\_replace**bool, int, float, string, list or dict, the value to be replaced.

If the value is a dict, then value is ignored or can be omitted, and to\_replace must be a mapping between a value and a replacement.

**value**bool, int, float, string or None, optional

The replacement value must be a bool, int, float, string or None. If value is a list, value should be of the same length and type as to\_replace. If value is a scalar and to\_replace is a sequence, then value is used as a replacement for each item in to\_replace.

**subset**list, optional

optional list of column names to consider. Columns specified in subset that do not have matching data types are ignored. For example, if value is a string, and subset contains a non-string column, then the non-string column is simply ignored.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with replaced values.

Examples

```
>>> df = spark.createDataFrame([
...     (10, 80, "Alice"),
...     (5, None, "Bob"),
...     (None, 10, "Tom"),
...     (None, None, None)],
...     schema=["age", "height", "name"])

```


Example 1: Replace 10 to 20 in all columns.

```
>>> df.na.replace(10, 20).show()
+----+------+-----+
| age|height| name|
+----+------+-----+
|  20|    80|Alice|
|   5|  NULL|  Bob|
|NULL|    20|  Tom|
|NULL|  NULL| NULL|
+----+------+-----+

```


Example 2: Replace ‘Alice’ to null in all columns.

```
>>> df.na.replace('Alice', None).show()
+----+------+----+
| age|height|name|
+----+------+----+
|  10|    80|NULL|
|   5|  NULL| Bob|
|NULL|    10| Tom|
|NULL|  NULL|NULL|
+----+------+----+

```


Example 3: Replace ‘Alice’ to ‘A’, and ‘Bob’ to ‘B’ in the ‘name’ column.

```
>>> df.na.replace(['Alice', 'Bob'], ['A', 'B'], 'name').show()
+----+------+----+
| age|height|name|
+----+------+----+
|  10|    80|   A|
|   5|  NULL|   B|
|NULL|    10| Tom|
|NULL|  NULL|NULL|
+----+------+----+

```


Example 4: Replace 10 to 20 in the ‘name’ column.

```
>>> df.na.replace(10, 18, 'age').show()
+----+------+-----+
| age|height| name|
+----+------+-----+
|  18|    80|Alice|
|   5|  NULL|  Bob|
|NULL|    10|  Tom|
|NULL|  NULL| NULL|
+----+------+-----+

```



# pyspark.sql.DataFrameStatFunctions.approxQuantile — PySpark 4.0.1 documentation
DataFrameStatFunctions.approxQuantile(_col_, _probabilities_, _relativeError_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions.approxQuantile)
[#](#pyspark.sql.DataFrameStatFunctions.approxQuantile "Permalink to this definition")

Calculates the approximate quantiles of numerical columns of a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

The result of this algorithm has the following deterministic bound: If the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") has N elements and if we request the quantile at probability p up to error err, then the algorithm will return a sample x from the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") so that the _exact_ rank of x is close to (p \* N). More precisely,

> floor((p - err) \* N) <= rank(x) <= ceil((p + err) \* N).

This method implements a variation of the Greenwald-Khanna algorithm (with some speed optimizations). The algorithm was first present in \[\[[https://doi.org/10.1145/375663.375670](https://doi.org/10.1145/375663.375670) Space-efficient Online Computation of Quantile Summaries\]\] by Greenwald and Khanna.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col: str, tuple or list**

Can be a single column name, or a list of names for multiple columns.

Changed in version 2.2.0: Added support for multiple columns.

**probabilities**list or tuple of floats

a list of quantile probabilities Each number must be a float in the range \[0, 1\]. For example 0.0 is the minimum, 0.5 is the median, 1.0 is the maximum.

**relativeError**float

The relative target precision to achieve (>= 0). If set to zero, the exact quantiles are computed, which could be very expensive. Note that values greater than 1 are accepted but gives the same result as 1.

Returns

list

the approximate quantiles at the given probabilities.

*   If the input col is a string, the output is a list of floats.
    
*   If the input col is a list or tuple of strings, the output is also a
    
    list, but each element in it is a list of floats, i.e., the output is a list of list of floats.
    

Notes

Null values will be ignored in numerical columns before calculation. For columns only containing null values, an empty list is returned.

Examples

Example 1: Calculating quantiles for a single column

```
>>> data = [(1,), (2,), (3,), (4,), (5,)]
>>> df = spark.createDataFrame(data, ["values"])
>>> quantiles = df.approxQuantile("values", [0.0, 0.5, 1.0], 0.05)
>>> quantiles
[1.0, 3.0, 5.0]

```


Example 2: Calculating quantiles for multiple columns

```
>>> data = [(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)]
>>> df = spark.createDataFrame(data, ["col1", "col2"])
>>> quantiles = df.approxQuantile(["col1", "col2"], [0.0, 0.5, 1.0], 0.05)
>>> quantiles
[[1.0, 3.0, 5.0], [10.0, 30.0, 50.0]]

```


Example 3: Handling null values

```
>>> data = [(1,), (None,), (3,), (4,), (None,)]
>>> df = spark.createDataFrame(data, ["values"])
>>> quantiles = df.approxQuantile("values", [0.0, 0.5, 1.0], 0.05)
>>> quantiles
[1.0, 3.0, 4.0]

```


Example 4: Calculating quantiles with low precision

```
>>> data = [(1,), (2,), (3,), (4,), (5,)]
>>> df = spark.createDataFrame(data, ["values"])
>>> quantiles = df.approxQuantile("values", [0.0, 0.2, 1.0], 0.1)
>>> quantiles
[1.0, 1.0, 5.0]

```


# pyspark.sql.DataFrameStatFunctions.corr — PySpark 4.0.1 documentation
DataFrameStatFunctions.corr(_col1_, _col2_, _method\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions.corr)
[#](#pyspark.sql.DataFrameStatFunctions.corr "Permalink to this definition")

Calculates the correlation of two columns of a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as a double value. Currently only supports the Pearson Correlation Coefficient. [`DataFrame.corr()`](about:blank/pyspark.sql.DataFrame.corr.html#pyspark.sql.DataFrame.corr "pyspark.sql.DataFrame.corr") and [`DataFrameStatFunctions.corr()`](#pyspark.sql.DataFrameStatFunctions.corr "pyspark.sql.DataFrameStatFunctions.corr") are aliases of each other.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**str

The name of the first column

**col2**str

The name of the second column

**method**str, optional

The correlation method. Currently only supports “pearson”

Returns

float

Pearson Correlation Coefficient of two columns.

Examples

```
>>> df = spark.createDataFrame([(1, 12), (10, 1), (19, 8)], ["c1", "c2"])
>>> df.corr("c1", "c2")
-0.3592106040535498
>>> df = spark.createDataFrame([(11, 12), (10, 11), (9, 10)], ["small", "bigger"])
>>> df.corr("small", "bigger")
1.0

```


# pyspark.sql.DataFrameStatFunctions.cov — PySpark 4.0.1 documentation
DataFrameStatFunctions.cov(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions.cov)
[#](#pyspark.sql.DataFrameStatFunctions.cov "Permalink to this definition")

Calculate the sample covariance for the given columns, specified by their names, as a double value. [`DataFrame.cov()`](about:blank/pyspark.sql.DataFrame.cov.html#pyspark.sql.DataFrame.cov "pyspark.sql.DataFrame.cov") and [`DataFrameStatFunctions.cov()`](#pyspark.sql.DataFrameStatFunctions.cov "pyspark.sql.DataFrameStatFunctions.cov") are aliases.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**str

The name of the first column

**col2**str

The name of the second column

Returns

float

Covariance of two columns.

Examples

```
>>> df = spark.createDataFrame([(1, 12), (10, 1), (19, 8)], ["c1", "c2"])
>>> df.cov("c1", "c2")
-18.0
>>> df = spark.createDataFrame([(11, 12), (10, 11), (9, 10)], ["small", "bigger"])
>>> df.cov("small", "bigger")
1.0

```

# pyspark.sql.DataFrameStatFunctions.crosstab — PySpark 4.0.1 documentation
DataFrameStatFunctions.crosstab(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions.crosstab)
[#](#pyspark.sql.DataFrameStatFunctions.crosstab "Permalink to this definition")

Computes a pair-wise frequency table of the given columns. Also known as a contingency table. The first column of each row will be the distinct values of col1 and the column names will be the distinct values of col2. The name of the first column will be $col1\_$col2. Pairs that have no occurrences will have zero as their counts. [`DataFrame.crosstab()`](about:blank/pyspark.sql.DataFrame.crosstab.html#pyspark.sql.DataFrame.crosstab "pyspark.sql.DataFrame.crosstab") and [`DataFrameStatFunctions.crosstab()`](#pyspark.sql.DataFrameStatFunctions.crosstab "pyspark.sql.DataFrameStatFunctions.crosstab") are aliases.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**str

The name of the first column. Distinct items will make the first item of each row.

**col2**str

The name of the second column. Distinct items will make the column names of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Frequency matrix of two columns.

Examples

```
>>> df = spark.createDataFrame([(1, 11), (1, 11), (3, 10), (4, 8), (4, 8)], ["c1", "c2"])
>>> df.crosstab("c1", "c2").sort("c1_c2").show()
+-----+---+---+---+
|c1_c2| 10| 11|  8|
+-----+---+---+---+
|    1|  0|  2|  0|
|    3|  1|  0|  0|
|    4|  0|  0|  2|
+-----+---+---+---+

```


# pyspark.sql.DataFrameStatFunctions.freqItems — PySpark 4.0.1 documentation
DataFrameStatFunctions.freqItems(_cols_, _support\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions.freqItems)
[#](#pyspark.sql.DataFrameStatFunctions.freqItems "Permalink to this definition")

Finding frequent items for columns, possibly with false positives. Using the frequent element count algorithm described in “[https://doi.org/10.1145/762471.762473](https://doi.org/10.1145/762471.762473), proposed by Karp, Schenker, and Papadimitriou”. [`DataFrame.freqItems()`](about:blank/pyspark.sql.DataFrame.freqItems.html#pyspark.sql.DataFrame.freqItems "pyspark.sql.DataFrame.freqItems") and [`DataFrameStatFunctions.freqItems()`](#pyspark.sql.DataFrameStatFunctions.freqItems "pyspark.sql.DataFrameStatFunctions.freqItems") are aliases.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**list or tuple

Names of the columns to calculate frequent items for as a list or tuple of strings.

**support**float, optional

The frequency with which to consider an item ‘frequent’. Default is 1%. The support must be greater than 1e-4.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame with frequent items.

Notes

This function is meant for exploratory data analysis, as we make no guarantee about the backward compatibility of the schema of the resulting [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

Examples

```
>>> df = spark.createDataFrame([(1, 11), (1, 11), (3, 10), (4, 8), (4, 8)], ["c1", "c2"])
>>> df.freqItems(["c1", "c2"]).show()  
+------------+------------+
|c1_freqItems|c2_freqItems|
+------------+------------+
|   [4, 1, 3]| [8, 11, 10]|
+------------+------------+

```



# pyspark.sql.DataFrameStatFunctions.sampleBy — PySpark 4.0.1 documentation
DataFrameStatFunctions.sampleBy(_col_, _fractions_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/dataframe.html#DataFrameStatFunctions.sampleBy)
[#](#pyspark.sql.DataFrameStatFunctions.sampleBy "Permalink to this definition")

Returns a stratified sample without replacement based on the fraction given on each stratum.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column that defines strata

Changed in version 3.0.0: Added sampling by a column of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

**fractions**dict

sampling fraction for each stratum. If a stratum is not specified, we treat its fraction as zero.

**seed**int, optional

random seed

Returns

a new [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that represents the stratified sample

Examples

```
>>> from pyspark.sql.functions import col
>>> dataset = spark.range(0, 100).select((col("id") % 3).alias("key"))
>>> sampled = dataset.sampleBy("key", fractions={0: 0.1, 1: 0.2}, seed=0)
>>> sampled.groupBy("key").count().orderBy("key").show()
+---+-----+
|key|count|
+---+-----+
|  0|    3|
|  1|    6|
+---+-----+
>>> dataset.sampleBy(col("key"), fractions={2: 1.0}, seed=0).count()
33

```

# pyspark.sql.table_arg.TableArg.partitionBy — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.table\_arg.TableArg.partitionBy

TableArg.partitionBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/table_arg.html#TableArg.partitionBy)
[#](#pyspark.sql.table_arg.TableArg.partitionBy "Permalink to this definition")

Partitions the data based on the specified columns.


# pyspark.sql.table_arg.TableArg.orderBy — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.table\_arg.TableArg.orderBy

TableArg.orderBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/table_arg.html#TableArg.orderBy)
[#](#pyspark.sql.table_arg.TableArg.orderBy "Permalink to this definition")

Orders the data within each partition by the specified columns.

# pyspark.sql.table_arg.TableArg.withSinglePartition — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../dataframe.html)
*   pyspark.sql.table\_arg.TableArg.withSinglePartition

TableArg.withSinglePartition()
[\[source\]](about:blank/_modules/pyspark/sql/table_arg.html#TableArg.withSinglePartition)
[#](#pyspark.sql.table_arg.TableArg.withSinglePartition "Permalink to this definition")

Forces the data to be processed in a single partition.

# pyspark.sql.plot.core.PySparkPlotAccessor.area — PySpark 4.0.1 documentation
PySparkPlotAccessor.area(_x_, _y_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.area)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.area "Permalink to this definition")

Draw a stacked area plot.

An area plot displays quantitative data visually.

Parameters

**x**str

Name of column to use for the horizontal axis.

**y**str or list of str

Name(s) of the column(s) to plot.

**\*\*kwargs: Optional**

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> from datetime import datetime
>>> data = [
...     (3, 5, 20, datetime(2018, 1, 31)),
...     (2, 5, 42, datetime(2018, 2, 28)),
...     (3, 6, 28, datetime(2018, 3, 31)),
...     (9, 12, 62, datetime(2018, 4, 30))
... ]
>>> columns = ["sales", "signups", "visits", "date"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.area(x='date', y=['sales', 'signups', 'visits'])  

```


# pyspark.sql.plot.core.PySparkPlotAccessor.bar — PySpark 4.0.1 documentation
PySparkPlotAccessor.bar(_x_, _y_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.bar)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.bar "Permalink to this definition")

Vertical bar plot.

A bar plot is a plot that presents categorical data with rectangular bars with lengths proportional to the values that they represent. A bar plot shows comparisons among discrete categories. One axis of the plot shows the specific categories being compared, and the other axis represents a measured value.

Parameters

**x**str

Name of column to use for the horizontal axis.

**y**str or list of str

Name(s) of the column(s) to use for the vertical axis. Multiple columns can be plotted.

**\*\*kwargs**optional

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> data = [("A", 10, 1.5), ("B", 30, 2.5), ("C", 20, 3.5)]
>>> columns = ["category", "int_val", "float_val"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.bar(x="category", y="int_val")  
>>> df.plot.bar(x="category", y=["int_val", "float_val"])  

```

# pyspark.sql.plot.core.PySparkPlotAccessor.barh — PySpark 4.0.1 documentation
PySparkPlotAccessor.barh(_x_, _y_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.barh)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.barh "Permalink to this definition")

Make a horizontal bar plot.

A horizontal bar plot is a plot that presents quantitative data with rectangular bars with lengths proportional to the values that they represent. A bar plot shows comparisons among discrete categories. One axis of the plot shows the specific categories being compared, and the other axis represents a measured value.

Parameters

**x**str or list of str

Name(s) of the column(s) to use for the horizontal axis. Multiple columns can be plotted.

**y**str or list of str

Name(s) of the column(s) to use for the vertical axis. Multiple columns can be plotted.

**\*\*kwargs**optional

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Notes

In Plotly and Matplotlib, the interpretation of x and y for barh plots differs. In Plotly, x refers to the values and y refers to the categories. In Matplotlib, x refers to the categories and y refers to the values. Ensure correct axis labeling based on the backend used.

Examples

```
>>> data = [("A", 10, 1.5), ("B", 30, 2.5), ("C", 20, 3.5)]
>>> columns = ["category", "int_val", "float_val"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.barh(x="int_val", y="category")  
>>> df.plot.barh(
...     x=["int_val", "float_val"], y="category"
... )  

```

# pyspark.sql.plot.core.PySparkPlotAccessor.line — PySpark 4.0.1 documentation
PySparkPlotAccessor.line(_x_, _y_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.line)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.line "Permalink to this definition")

Plot DataFrame as lines.

Parameters

**x**str

Name of column to use for the horizontal axis.

**y**str or list of str

Name(s) of the column(s) to use for the vertical axis. Multiple columns can be plotted.

**\*\*kwargs**optional

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> data = [("A", 10, 1.5), ("B", 30, 2.5), ("C", 20, 3.5)]
>>> columns = ["category", "int_val", "float_val"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.line(x="category", y="int_val")  
>>> df.plot.line(x="category", y=["int_val", "float_val"])  

```


# pyspark.sql.plot.core.PySparkPlotAccessor.pie — PySpark 4.0.1 documentation
PySparkPlotAccessor.pie(_x_, _y_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.pie)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.pie "Permalink to this definition")

Generate a pie plot.

A pie plot is a proportional representation of the numerical data in a column.

Parameters

**x**str

Name of column to be used as the category labels for the pie plot.

**y**str, optional

Name of the column to plot. If not provided, subplots=True must be passed at kwargs.

**\*\*kwargs**

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> from datetime import datetime
>>> data = [
...     (3, 5, 20, datetime(2018, 1, 31)),
...     (2, 5, 42, datetime(2018, 2, 28)),
...     (3, 6, 28, datetime(2018, 3, 31)),
...     (9, 12, 62, datetime(2018, 4, 30))
... ]
>>> columns = ["sales", "signups", "visits", "date"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.pie(x='date', y='sales')  
>>> df.plot.pie(x='date', subplots=True)  

```



# pyspark.sql.plot.core.PySparkPlotAccessor.scatter — PySpark 4.0.1 documentation
PySparkPlotAccessor.scatter(_x_, _y_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.scatter)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.scatter "Permalink to this definition")

Create a scatter plot with varying marker point size and color.

The coordinates of each point are defined by two dataframe columns and filled circles are used to represent each point. This kind of plot is useful to see complex correlations between two variables. Points could be for instance natural 2D coordinates like longitude and latitude in a map or, in general, any pair of metrics that can be plotted against each other.

Parameters

**x**str

Name of column to use as horizontal coordinates for each point.

**y**str or list of str

Name of column to use as vertical coordinates for each point.

**\*\*kwargs: Optional**

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> data = [(5.1, 3.5, 0), (4.9, 3.0, 0), (7.0, 3.2, 1), (6.4, 3.2, 1), (5.9, 3.0, 2)]
>>> columns = ['length', 'width', 'species']
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.scatter(x='length', y='width')  

```

# pyspark.sql.plot.core.PySparkPlotAccessor.box — PySpark 4.0.1 documentation
PySparkPlotAccessor.box(_column\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.box)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.box "Permalink to this definition")

Make a box plot of the DataFrame columns.

Make a box-and-whisker plot from DataFrame columns, optionally grouped by some other columns. A box plot is a method for graphically depicting groups of numerical data through their quartiles. The box extends from the Q1 to Q3 quartile values of the data, with a line at the median (Q2). The whiskers extend from the edges of box to show the range of the data. By default, they extend no more than 1.5 \* IQR (IQR = Q3 - Q1) from the edges of the box, ending at the farthest data point within that interval. Outliers are plotted as separate dots.

Parameters

**column: str or list of str, optional**

Column name or list of names to be used for creating the box plot. If None (default), all numeric columns will be used.

**\*\*kwargs**

Extra arguments to precision: refer to a float that is used by pyspark to compute approximate statistics for building a boxplot. The default value is 0.01. Use smaller values to get more precise statistics.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> data = [
...     ("A", 50, 55),
...     ("B", 55, 60),
...     ("C", 60, 65),
...     ("D", 65, 70),
...     ("E", 70, 75),
...     ("F", 10, 15),
...     ("G", 85, 90),
...     ("H", 5, 150),
... ]
>>> columns = ["student", "math_score", "english_score"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.box()  
>>> df.plot.box(column="math_score")  
>>> df.plot.box(column=["math_score", "english_score"])  

```



# pyspark.sql.plot.core.PySparkPlotAccessor.kde — PySpark 4.0.1 documentation
PySparkPlotAccessor.kde(_bw\_method_, _column\=None_, _ind\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.kde)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.kde "Permalink to this definition")

Generate Kernel Density Estimate plot using Gaussian kernels.

In statistics, kernel density estimation (KDE) is a non-parametric way to estimate the probability density function (PDF) of a random variable. This function uses Gaussian kernels and includes automatic bandwidth determination.

Parameters

**bw\_method**int or float

The method used to calculate the estimator bandwidth. See KernelDensity in PySpark for more information.

**column: str or list of str, optional**

Column name or list of names to be used for creating the kde plot. If None (default), all numeric columns will be used.

**ind**List of float, NumPy array or integer, optional

Evaluation points for the estimated PDF. If None (default), 1000 equally spaced points are used. If ind is a NumPy array, the KDE is evaluated at the points passed. If ind is an integer, ind number of equally spaced points are used.

**\*\*kwargs**optional

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> data = [(5.1, 3.5, 0), (4.9, 3.0, 0), (7.0, 3.2, 1), (6.4, 3.2, 1), (5.9, 3.0, 2)]
>>> columns = ["length", "width", "species"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.kde(bw_method=0.3, ind=100)  
>>> df.plot.kde(column=["length", "width"], bw_method=0.3, ind=100)  
>>> df.plot.kde(column="length", bw_method=0.3, ind=100)  

```


# pyspark.sql.plot.core.PySparkPlotAccessor.hist — PySpark 4.0.1 documentation
PySparkPlotAccessor.hist(_column\=None_, _bins\=10_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/plot/core.html#PySparkPlotAccessor.hist)
[#](#pyspark.sql.plot.core.PySparkPlotAccessor.hist "Permalink to this definition")

Draw one histogram of the DataFrame’s columns.

A [histogram](https://en.wikipedia.org/wiki/Histogram) is a representation of the distribution of data.

Parameters

**column: str or list of str, optional**

Column name or list of names to be used for creating the hostogram plot. If None (default), all numeric columns will be used.

**bins**integer, default 10

Number of histogram bins to be used.

**\*\*kwargs**

Additional keyword arguments.

Returns

`plotly.graph_objs.Figure`

Examples

```
>>> data = [(5.1, 3.5, 0), (4.9, 3.0, 0), (7.0, 3.2, 1), (6.4, 3.2, 1), (5.9, 3.0, 2)]
>>> columns = ["length", "width", "species"]
>>> df = spark.createDataFrame(data, columns)
>>> df.plot.hist(bins=4)  
>>> df.plot.hist(column=["length", "width"])  
>>> df.plot.hist(column="length", bins=4)  

```
