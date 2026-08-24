# Input/Output — PySpark 4.0.1 documentation
[`DataFrameReader.csv`](about:blank/api/pyspark.sql.DataFrameReader.csv.html#pyspark.sql.DataFrameReader.csv "pyspark.sql.DataFrameReader.csv")(path\[, schema, sep, ...\])

Loads a CSV file and returns the result as a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameReader.format`](about:blank/api/pyspark.sql.DataFrameReader.format.html#pyspark.sql.DataFrameReader.format "pyspark.sql.DataFrameReader.format")(source)

Specifies the input data source format.

[`DataFrameReader.jdbc`](about:blank/api/pyspark.sql.DataFrameReader.jdbc.html#pyspark.sql.DataFrameReader.jdbc "pyspark.sql.DataFrameReader.jdbc")(url, table\[, column, ...\])

Construct a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") representing the database table named `table` accessible via JDBC URL `url` and connection `properties`.

[`DataFrameReader.json`](about:blank/api/pyspark.sql.DataFrameReader.json.html#pyspark.sql.DataFrameReader.json "pyspark.sql.DataFrameReader.json")(path\[, schema, ...\])

Loads JSON files and returns the results as a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameReader.load`](about:blank/api/pyspark.sql.DataFrameReader.load.html#pyspark.sql.DataFrameReader.load "pyspark.sql.DataFrameReader.load")(\[path, format, schema\])

Loads data from a data source and returns it as a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameReader.option`](about:blank/api/pyspark.sql.DataFrameReader.option.html#pyspark.sql.DataFrameReader.option "pyspark.sql.DataFrameReader.option")(key, value)

Adds an input option for the underlying data source.

[`DataFrameReader.options`](about:blank/api/pyspark.sql.DataFrameReader.options.html#pyspark.sql.DataFrameReader.options "pyspark.sql.DataFrameReader.options")(\*\*options)

Adds input options for the underlying data source.

[`DataFrameReader.orc`](about:blank/api/pyspark.sql.DataFrameReader.orc.html#pyspark.sql.DataFrameReader.orc "pyspark.sql.DataFrameReader.orc")(path\[, mergeSchema, ...\])

Loads ORC files, returning the result as a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameReader.parquet`](about:blank/api/pyspark.sql.DataFrameReader.parquet.html#pyspark.sql.DataFrameReader.parquet "pyspark.sql.DataFrameReader.parquet")(\*paths, \*\*options)

Loads Parquet files, returning the result as a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameReader.schema`](about:blank/api/pyspark.sql.DataFrameReader.schema.html#pyspark.sql.DataFrameReader.schema "pyspark.sql.DataFrameReader.schema")(schema)

Specifies the input schema.

[`DataFrameReader.table`](about:blank/api/pyspark.sql.DataFrameReader.table.html#pyspark.sql.DataFrameReader.table "pyspark.sql.DataFrameReader.table")(tableName)

Returns the specified table as a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[`DataFrameReader.text`](about:blank/api/pyspark.sql.DataFrameReader.text.html#pyspark.sql.DataFrameReader.text "pyspark.sql.DataFrameReader.text")(paths\[, wholetext, ...\])

Loads text files and returns a [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") whose schema starts with a string column named "value", and followed by partitioned columns if there are any.

[`DataFrameWriter.bucketBy`](about:blank/api/pyspark.sql.DataFrameWriter.bucketBy.html#pyspark.sql.DataFrameWriter.bucketBy "pyspark.sql.DataFrameWriter.bucketBy")(numBuckets, col, \*cols)

Buckets the output by the given columns.

[`DataFrameWriter.csv`](about:blank/api/pyspark.sql.DataFrameWriter.csv.html#pyspark.sql.DataFrameWriter.csv "pyspark.sql.DataFrameWriter.csv")(path\[, mode, ...\])

Saves the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in CSV format at the specified path.

[`DataFrameWriter.format`](about:blank/api/pyspark.sql.DataFrameWriter.format.html#pyspark.sql.DataFrameWriter.format "pyspark.sql.DataFrameWriter.format")(source)

Specifies the underlying output data source.

[`DataFrameWriter.insertInto`](about:blank/api/pyspark.sql.DataFrameWriter.insertInto.html#pyspark.sql.DataFrameWriter.insertInto "pyspark.sql.DataFrameWriter.insertInto")(tableName\[, ...\])

Inserts the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to the specified table.

[`DataFrameWriter.jdbc`](about:blank/api/pyspark.sql.DataFrameWriter.jdbc.html#pyspark.sql.DataFrameWriter.jdbc "pyspark.sql.DataFrameWriter.jdbc")(url, table\[, mode, ...\])

Saves the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to an external database table via JDBC.

[`DataFrameWriter.json`](about:blank/api/pyspark.sql.DataFrameWriter.json.html#pyspark.sql.DataFrameWriter.json "pyspark.sql.DataFrameWriter.json")(path\[, mode, ...\])

Saves the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in JSON format ([JSON Lines text format or newline-delimited JSON](http://jsonlines.org/)) at the specified path.

[`DataFrameWriter.mode`](about:blank/api/pyspark.sql.DataFrameWriter.mode.html#pyspark.sql.DataFrameWriter.mode "pyspark.sql.DataFrameWriter.mode")(saveMode)

Specifies the behavior when data or table already exists.

[`DataFrameWriter.option`](about:blank/api/pyspark.sql.DataFrameWriter.option.html#pyspark.sql.DataFrameWriter.option "pyspark.sql.DataFrameWriter.option")(key, value)

Adds an output option for the underlying data source.

[`DataFrameWriter.options`](about:blank/api/pyspark.sql.DataFrameWriter.options.html#pyspark.sql.DataFrameWriter.options "pyspark.sql.DataFrameWriter.options")(\*\*options)

Adds output options for the underlying data source.

[`DataFrameWriter.orc`](about:blank/api/pyspark.sql.DataFrameWriter.orc.html#pyspark.sql.DataFrameWriter.orc "pyspark.sql.DataFrameWriter.orc")(path\[, mode, ...\])

Saves the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in ORC format at the specified path.

[`DataFrameWriter.parquet`](about:blank/api/pyspark.sql.DataFrameWriter.parquet.html#pyspark.sql.DataFrameWriter.parquet "pyspark.sql.DataFrameWriter.parquet")(path\[, mode, ...\])

Saves the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in Parquet format at the specified path.

[`DataFrameWriter.partitionBy`](about:blank/api/pyspark.sql.DataFrameWriter.partitionBy.html#pyspark.sql.DataFrameWriter.partitionBy "pyspark.sql.DataFrameWriter.partitionBy")(\*cols)

Partitions the output by the given columns on the file system.

[`DataFrameWriter.save`](about:blank/api/pyspark.sql.DataFrameWriter.save.html#pyspark.sql.DataFrameWriter.save "pyspark.sql.DataFrameWriter.save")(\[path, format, mode, ...\])

Saves the contents of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to a data source.

[`DataFrameWriter.saveAsTable`](about:blank/api/pyspark.sql.DataFrameWriter.saveAsTable.html#pyspark.sql.DataFrameWriter.saveAsTable "pyspark.sql.DataFrameWriter.saveAsTable")(name\[, format, ...\])

Saves the content of the [`DataFrame`](about:blank/api/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as the specified table.

[`DataFrameWriter.sortBy`](about:blank/api/pyspark.sql.DataFrameWriter.sortBy.html#pyspark.sql.DataFrameWriter.sortBy "pyspark.sql.DataFrameWriter.sortBy")(col, \*cols)

Sorts the output in each bucket by the given columns on the file system.

[`DataFrameWriter.text`](about:blank/api/pyspark.sql.DataFrameWriter.text.html#pyspark.sql.DataFrameWriter.text "pyspark.sql.DataFrameWriter.text")(path\[, compression, ...\])

Saves the content of the DataFrame in a text file at the specified path.

[`DataFrameWriterV2.using`](about:blank/api/pyspark.sql.DataFrameWriterV2.using.html#pyspark.sql.DataFrameWriterV2.using "pyspark.sql.DataFrameWriterV2.using")(provider)

Specifies a provider for the underlying output data source.

[`DataFrameWriterV2.option`](about:blank/api/pyspark.sql.DataFrameWriterV2.option.html#pyspark.sql.DataFrameWriterV2.option "pyspark.sql.DataFrameWriterV2.option")(key, value)

Add a write option.

[`DataFrameWriterV2.options`](about:blank/api/pyspark.sql.DataFrameWriterV2.options.html#pyspark.sql.DataFrameWriterV2.options "pyspark.sql.DataFrameWriterV2.options")(\*\*options)

Add write options.

[`DataFrameWriterV2.tableProperty`](about:blank/api/pyspark.sql.DataFrameWriterV2.tableProperty.html#pyspark.sql.DataFrameWriterV2.tableProperty "pyspark.sql.DataFrameWriterV2.tableProperty")(property, value)

Add table property.

[`DataFrameWriterV2.partitionedBy`](about:blank/api/pyspark.sql.DataFrameWriterV2.partitionedBy.html#pyspark.sql.DataFrameWriterV2.partitionedBy "pyspark.sql.DataFrameWriterV2.partitionedBy")(col, \*cols)

Partition the output table created by create, createOrReplace, or replace using the given columns or transforms.

[`DataFrameWriterV2.create`](about:blank/api/pyspark.sql.DataFrameWriterV2.create.html#pyspark.sql.DataFrameWriterV2.create "pyspark.sql.DataFrameWriterV2.create")()

Create a new table from the contents of the data frame.

[`DataFrameWriterV2.replace`](about:blank/api/pyspark.sql.DataFrameWriterV2.replace.html#pyspark.sql.DataFrameWriterV2.replace "pyspark.sql.DataFrameWriterV2.replace")()

Replace an existing table with the contents of the data frame.

[`DataFrameWriterV2.createOrReplace`](about:blank/api/pyspark.sql.DataFrameWriterV2.createOrReplace.html#pyspark.sql.DataFrameWriterV2.createOrReplace "pyspark.sql.DataFrameWriterV2.createOrReplace")()

Create a new table or replace an existing table with the contents of the data frame.

[`DataFrameWriterV2.append`](about:blank/api/pyspark.sql.DataFrameWriterV2.append.html#pyspark.sql.DataFrameWriterV2.append "pyspark.sql.DataFrameWriterV2.append")()

Append the contents of the data frame to the output table.

[`DataFrameWriterV2.overwrite`](about:blank/api/pyspark.sql.DataFrameWriterV2.overwrite.html#pyspark.sql.DataFrameWriterV2.overwrite "pyspark.sql.DataFrameWriterV2.overwrite")(condition)

Overwrite rows matching the given filter condition with the contents of the data frame in the output table.

[`DataFrameWriterV2.overwritePartitions`](about:blank/api/pyspark.sql.DataFrameWriterV2.overwritePartitions.html#pyspark.sql.DataFrameWriterV2.overwritePartitions "pyspark.sql.DataFrameWriterV2.overwritePartitions")()

Overwrite all partition for which the data frame contains at least one row with the contents of the data frame in the output table.

[`MergeIntoWriter.whenMatched`](about:blank/api/pyspark.sql.MergeIntoWriter.whenMatched.html#pyspark.sql.MergeIntoWriter.whenMatched "pyspark.sql.MergeIntoWriter.whenMatched")(\[condition\])

Initialize a WhenMatched action with a condition.

[`MergeIntoWriter.whenNotMatched`](about:blank/api/pyspark.sql.MergeIntoWriter.whenNotMatched.html#pyspark.sql.MergeIntoWriter.whenNotMatched "pyspark.sql.MergeIntoWriter.whenNotMatched")(\[condition\])

Initialize a WhenNotMatched action with a condition.

[`MergeIntoWriter.whenNotMatchedBySource`](about:blank/api/pyspark.sql.MergeIntoWriter.whenNotMatchedBySource.html#pyspark.sql.MergeIntoWriter.whenNotMatchedBySource "pyspark.sql.MergeIntoWriter.whenNotMatchedBySource")(\[...\])

Initialize a WhenNotMatchedBySource action with a condition.

[`MergeIntoWriter.withSchemaEvolution`](about:blank/api/pyspark.sql.MergeIntoWriter.withSchemaEvolution.html#pyspark.sql.MergeIntoWriter.withSchemaEvolution "pyspark.sql.MergeIntoWriter.withSchemaEvolution")()

Enable automatic schema evolution for this merge operation.

[`MergeIntoWriter.merge`](about:blank/api/pyspark.sql.MergeIntoWriter.merge.html#pyspark.sql.MergeIntoWriter.merge "pyspark.sql.MergeIntoWriter.merge")()

Execute the merge operation.

# pyspark.sql.DataFrameReader.csv — PySpark 4.0.1 documentation
DataFrameReader.csv(_path_, _schema\=None_, _sep\=None_, _encoding\=None_, _quote\=None_, _escape\=None_, _comment\=None_, _header\=None_, _inferSchema\=None_, _ignoreLeadingWhiteSpace\=None_, _ignoreTrailingWhiteSpace\=None_, _nullValue\=None_, _nanValue\=None_, _positiveInf\=None_, _negativeInf\=None_, _dateFormat\=None_, _timestampFormat\=None_, _maxColumns\=None_, _maxCharsPerColumn\=None_, _maxMalformedLogPerPartition\=None_, _mode\=None_, _columnNameOfCorruptRecord\=None_, _multiLine\=None_, _charToEscapeQuoteEscaping\=None_, _samplingRatio\=None_, _enforceSchema\=None_, _emptyValue\=None_, _locale\=None_, _lineSep\=None_, _pathGlobFilter\=None_, _recursiveFileLookup\=None_, _modifiedBefore\=None_, _modifiedAfter\=None_, _unescapedQuoteHandling\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.csv)
[#](#pyspark.sql.DataFrameReader.csv "Permalink to this definition")

Loads a CSV file and returns the result as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

This function will go through the input once to determine the input schema if `inferSchema` is enabled. To avoid going through the entire data once, disable `inferSchema` option or specify the schema explicitly using `schema`.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str or list

string, or list of strings, for input path(s), or RDD of Strings storing CSV rows.

**schema**[`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") or str, optional

an optional [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") for the input schema or a DDL-formatted string (For example `col0 INT, col1 DOUBLE`).

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a CSV file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="csv") as d:
...     # Write a DataFrame into a CSV file
...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
...     df.write.mode("overwrite").format("csv").save(d)
...
...     # Read the CSV file as a DataFrame with 'nullValue' option set to 'Hyukjin Kwon'.
...     spark.read.csv(d, schema=df.schema, nullValue="Hyukjin Kwon").show()
+---+----+
|age|name|
+---+----+
|100|NULL|
+---+----+

```
# pyspark.sql.DataFrameReader.format — PySpark 4.0.1 documentation
DataFrameReader.format(_source_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.format)
[#](#pyspark.sql.DataFrameReader.format "Permalink to this definition")

Specifies the input data source format.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**source**str

string, name of the data source, e.g. ‘json’, ‘parquet’.

Examples

```
>>> spark.read.format('json')
<...readwriter.DataFrameReader object ...>

```


Write a DataFrame into a JSON file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="format") as d:
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


# pyspark.sql.DataFrameReader.jdbc — PySpark 4.0.1 documentation
DataFrameReader.jdbc(_url_, _table_, _column\=None_, _lowerBound\=None_, _upperBound\=None_, _numPartitions\=None_, _predicates\=None_, _properties\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.jdbc)
[#](#pyspark.sql.DataFrameReader.jdbc "Permalink to this definition")

Construct a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") representing the database table named `table` accessible via JDBC URL `url` and connection `properties`.

Partitions of the table will be retrieved in parallel if either `column` or `predicates` is specified. `lowerBound`, `upperBound` and `numPartitions` is needed when `column` is specified.

If both `column` and `predicates` are specified, `column` will be used.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**table**str

the name of the table

**column**str, optional

alias of `partitionColumn` option. Refer to `partitionColumn` in [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html#data-source-option) for the version you use.

**predicates**list, optional

a list of expressions suitable for inclusion in WHERE clauses; each one defines one partition of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

**properties**dict, optional

a dictionary of JDBC database connection arguments. Normally at least properties “user” and “password” with their corresponding values. For example { ‘user’ : ‘SYSTEM’, ‘password’ : ‘mypassword’ }

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html#data-source-option) for the version you use.

Notes

Don’t create too many partitions in parallel on a large cluster; otherwise Spark might crash your external database systems.

# pyspark.sql.DataFrameReader.json — PySpark 4.0.1 documentation
DataFrameReader.json(_path_, _schema\=None_, _primitivesAsString\=None_, _prefersDecimal\=None_, _allowComments\=None_, _allowUnquotedFieldNames\=None_, _allowSingleQuotes\=None_, _allowNumericLeadingZero\=None_, _allowBackslashEscapingAnyCharacter\=None_, _mode\=None_, _columnNameOfCorruptRecord\=None_, _dateFormat\=None_, _timestampFormat\=None_, _multiLine\=None_, _allowUnquotedControlChars\=None_, _lineSep\=None_, _samplingRatio\=None_, _dropFieldIfAllNull\=None_, _encoding\=None_, _locale\=None_, _pathGlobFilter\=None_, _recursiveFileLookup\=None_, _modifiedBefore\=None_, _modifiedAfter\=None_, _allowNonNumericNumbers\=None_, _useUnsafeRow\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.json)
[#](#pyspark.sql.DataFrameReader.json "Permalink to this definition")

Loads JSON files and returns the results as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

[JSON Lines](http://jsonlines.org/) (newline-delimited JSON) is supported by default. For JSON (one record per file), set the `multiLine` parameter to `true`.

If the `schema` parameter is not specified, this function goes through the input once to determine the input schema.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str, list or `RDD`

string represents path to the JSON dataset, or a list of paths, or RDD of Strings storing JSON objects.

**schema**[`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") or str, optional

an optional [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") for the input schema or a DDL-formatted string (For example `col0 INT, col1 DOUBLE`).

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option) for the version you use.

Examples

Example 1: Write a DataFrame into a JSON file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="json1") as d:
...     # Write a DataFrame into a JSON file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin"}]
...     ).write.mode("overwrite").format("json").save(d)
...
...     # Read the JSON file as a DataFrame.
...     spark.read.json(d).show()
+---+-------+
|age|   name|
+---+-------+
|100|Hyukjin|
+---+-------+

```


Example 2: Read JSON from multiple files in a directory

```
>>> from tempfile import TemporaryDirectory
>>> with TemporaryDirectory(prefix="json2") as d1, TemporaryDirectory(prefix="json3") as d2:
...     # Write a DataFrame into a JSON file
...     spark.createDataFrame(
...         [{"age": 30, "name": "Bob"}]
...     ).write.mode("overwrite").format("json").save(d1)
...
...     # Read the JSON files as a DataFrame.
...     spark.createDataFrame(
...         [{"age": 25, "name": "Alice"}]
...     ).write.mode("overwrite").format("json").save(d2)
...     spark.read.json([d1, d2]).show()
+---+-----+
|age| name|
+---+-----+
| 25|Alice|
| 30|  Bob|
+---+-----+

```


Example 3: Read JSON with a custom schema

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="json4") as d:
...     # Write a DataFrame into a JSON file
...     spark.createDataFrame(
...        [{"age": 30, "name": "Bob"}]
...     ).write.mode("overwrite").format("json").save(d)
...     custom_schema = "name STRING, age INT"
...     spark.read.json(d, schema=custom_schema).show()
+----+---+
|name|age|
+----+---+
| Bob| 30|
+----+---+

```


# pyspark.sql.DataFrameReader.load — PySpark 4.0.1 documentation
DataFrameReader.load(_path\=None_, _format\=None_, _schema\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.load)
[#](#pyspark.sql.DataFrameReader.load "Permalink to this definition")

Loads data from a data source and returns it as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str or list, optional

optional string or a list of string for file-system backed data sources.

**format**str, optional

optional string for format of the data source. Default to ‘parquet’.

**schema**[`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") or str, optional

optional [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") for the input schema or a DDL-formatted string (For example `col0 INT, col1 DOUBLE`).

**\*\*options**dict

all other string options

Examples

Load a CSV file with format, schema and options specified.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="load") as d:
...     # Write a DataFrame into a CSV file with a header
...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
...     df.write.option("header", True).mode("overwrite").format("csv").save(d)
...
...     # Read the CSV file as a DataFrame with 'nullValue' option set to 'Hyukjin Kwon',
...     # and 'header' option set to `True`.
...     df = spark.read.load(
...         d, schema=df.schema, format="csv", nullValue="Hyukjin Kwon", header=True)
...     df.printSchema()
...     df.show()
root
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)
+---+----+
|age|name|
+---+----+
|100|NULL|
+---+----+

```

# pyspark.sql.DataFrameReader.option — PySpark 4.0.1 documentation
DataFrameReader.option(_key_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.option)
[#](#pyspark.sql.DataFrameReader.option "Permalink to this definition")

Adds an input option for the underlying data source.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**key**str

The key for the option to set.

**value**

The value for the option to set.

Examples

```
>>> spark.read.option("key", "value")
<...readwriter.DataFrameReader object ...>

```


Specify the option ‘nullValue’ with reading a CSV file.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="option") as d:
...     # Write a DataFrame into a CSV file
...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
...     df.write.mode("overwrite").format("csv").save(d)
...
...     # Read the CSV file as a DataFrame with 'nullValue' option set to 'Hyukjin Kwon'.
...     spark.read.schema(df.schema).option(
...         "nullValue", "Hyukjin Kwon").format('csv').load(d).show()
+---+----+
|age|name|
+---+----+
|100|NULL|
+---+----+

```
# pyspark.sql.DataFrameReader.options — PySpark 4.0.1 documentation
DataFrameReader.options(_\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.options)
[#](#pyspark.sql.DataFrameReader.options "Permalink to this definition")

Adds input options for the underlying data source.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**\*\*options**dict

The dictionary of string keys and primitive-type values.

Examples

```
>>> spark.read.options(key="value")
<...readwriter.DataFrameReader object ...>

```


Specify options in a dictionary.

```
>>> spark.read.options(**{"k1": "v1", "k2": "v2"})
<...readwriter.DataFrameReader object ...>

```


Specify the option ‘nullValue’ and ‘header’ with reading a CSV file.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="options") as d:
...     # Write a DataFrame into a CSV file with a header.
...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
...     df.write.option("header", True).mode("overwrite").format("csv").save(d)
...
...     # Read the CSV file as a DataFrame with 'nullValue' option set to 'Hyukjin Kwon',
...     # and 'header' option set to `True`.
...     spark.read.options(
...         nullValue="Hyukjin Kwon",
...         header=True
...     ).format('csv').load(d).show()
+---+----+
|age|name|
+---+----+
|100|NULL|
+---+----+

```

# pyspark.sql.DataFrameReader.orc — PySpark 4.0.1 documentation
DataFrameReader.orc(_path_, _mergeSchema\=None_, _pathGlobFilter\=None_, _recursiveFileLookup\=None_, _modifiedBefore\=None_, _modifiedAfter\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.orc)
[#](#pyspark.sql.DataFrameReader.orc "Permalink to this definition")

Loads ORC files, returning the result as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str or list

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a ORC file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="orc") as d:
...     # Write a DataFrame into a ORC file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.mode("overwrite").format("orc").save(d)
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.orc(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```

# pyspark.sql.DataFrameReader.parquet — PySpark 4.0.1 documentation
DataFrameReader.parquet(_\*paths_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.parquet)
[#](#pyspark.sql.DataFrameReader.parquet "Permalink to this definition")

Loads Parquet files, returning the result as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**paths**str

One or more file paths to read the Parquet files from.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

A DataFrame containing the data from the Parquet files.

Other Parameters

**\*\*options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option) for the version you use.

Examples

Create sample dataframes.

```
>>> df = spark.createDataFrame(
...     [(10, "Alice"), (15, "Bob"), (20, "Tom")], schema=["age", "name"])
>>> df2 = spark.createDataFrame([(70, "Alice"), (80, "Bob")], schema=["height", "name"])

```


Write a DataFrame into a Parquet file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="parquet1") as d:
...     # Write a DataFrame into a Parquet file.
...     df.write.mode("overwrite").format("parquet").save(d)
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.parquet(d).orderBy("name").show()
+---+-----+
|age| name|
+---+-----+
| 10|Alice|
| 15|  Bob|
| 20|  Tom|
+---+-----+

```


Read a Parquet file with a specific column.

```
>>> with tempfile.TemporaryDirectory(prefix="parquet2") as d:
...     df.write.mode("overwrite").format("parquet").save(d)
...
...     # Read the Parquet file with only the 'name' column.
...     spark.read.schema("name string").parquet(d).orderBy("name").show()
+-----+
| name|
+-----+
|Alice|
|  Bob|
|  Tom|
+-----+

```


Read multiple Parquet files and merge schema.

```
>>> with tempfile.TemporaryDirectory(prefix="parquet3") as d1:
...     with tempfile.TemporaryDirectory(prefix="parquet4") as d2:
...         df.write.mode("overwrite").format("parquet").save(d1)
...         df2.write.mode("overwrite").format("parquet").save(d2)
...
...         spark.read.option(
...             "mergeSchema", "true"
...         ).parquet(d1, d2).select(
...             "name", "age", "height"
...         ).orderBy("name", "age").show()
+-----+----+------+
| name| age|height|
+-----+----+------+
|Alice|NULL|    70|
|Alice|  10|  NULL|
|  Bob|NULL|    80|
|  Bob|  15|  NULL|
|  Tom|  20|  NULL|
+-----+----+------+

```

# pyspark.sql.DataFrameReader.schema — PySpark 4.0.1 documentation
DataFrameReader.schema(_schema_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.schema)
[#](#pyspark.sql.DataFrameReader.schema "Permalink to this definition")

Specifies the input schema.

Some data sources (e.g. JSON) can infer the input schema automatically from data. By specifying the schema here, the underlying data source can skip the schema inference step, and thus speed up data loading.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**schema**[`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") or str

a [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") object or a DDL-formatted string (For example `col0 INT, col1 DOUBLE`).

Examples

```
>>> spark.read.schema("col0 INT, col1 DOUBLE")
<...readwriter.DataFrameReader object ...>

```


Specify the schema with reading a CSV file.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="schema") as d:
...     spark.read.schema("col0 INT, col1 DOUBLE").format("csv").load(d).printSchema()
root
 |-- col0: integer (nullable = true)
 |-- col1: double (nullable = true)

```


# pyspark.sql.DataFrameReader.table — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameReader.table

DataFrameReader.table(_tableName_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.table)
[#](#pyspark.sql.DataFrameReader.table "Permalink to this definition")

Returns the specified table as a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**tableName**str

string, name of the table.

Examples

```
>>> df = spark.range(10)
>>> df.createOrReplaceTempView('tblA')
>>> spark.read.table('tblA').show()
+---+
| id|
+---+
|  0|
|  1|
|  2|
|  3|
|  4|
|  5|
|  6|
|  7|
|  8|
|  9|
+---+
>>> _ = spark.sql("DROP TABLE tblA")

```


# pyspark.sql.DataFrameReader.text — PySpark 4.0.1 documentation
DataFrameReader.text(_paths_, _wholetext\=False_, _lineSep\=None_, _pathGlobFilter\=None_, _recursiveFileLookup\=None_, _modifiedBefore\=None_, _modifiedAfter\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameReader.text)
[#](#pyspark.sql.DataFrameReader.text "Permalink to this definition")

Loads text files and returns a [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") whose schema starts with a string column named “value”, and followed by partitioned columns if there are any. The text files must be encoded as UTF-8.

By default, each line in the text file is a new row in the resulting DataFrame.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**paths**str or list

string, or list of strings, for input path(s).

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a text file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="text") as d:
...     # Write a DataFrame into a text file
...     df = spark.createDataFrame([("a",), ("b",), ("c",)], schema=["alphabets"])
...     df.write.mode("overwrite").format("text").save(d)
...
...     # Read the text file as a DataFrame.
...     spark.read.schema(df.schema).text(d).sort("alphabets").show()
+---------+
|alphabets|
+---------+
|        a|
|        b|
|        c|
+---------+

```


# pyspark.sql.DataFrameWriter.bucketBy — PySpark 4.0.1 documentation
DataFrameWriter.bucketBy(_numBuckets_, _col_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.bucketBy)
[#](#pyspark.sql.DataFrameWriter.bucketBy "Permalink to this definition")

Buckets the output by the given columns. If specified, the output is laid out on the file system similar to Hive’s bucketing scheme, but with a different bucket hash function and is not compatible with Hive’s bucketing.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**numBuckets**int

the number of buckets to save

**col**str, list or tuple

a name of a column, or a list of names.

**cols**str

additional names (optional). If col is a list it should be empty.

Notes

Applicable for file-based data sources in combination with [`DataFrameWriter.saveAsTable()`](about:blank/pyspark.sql.DataFrameWriter.saveAsTable.html#pyspark.sql.DataFrameWriter.saveAsTable "pyspark.sql.DataFrameWriter.saveAsTable").

Examples

Write a DataFrame into a Parquet file in a buckted manner, and read it back.

```
>>> from pyspark.sql.functions import input_file_name
>>> # Write a DataFrame into a Parquet file in a bucketed manner.
... _ = spark.sql("DROP TABLE IF EXISTS bucketed_table")
>>> spark.createDataFrame([
...     (100, "Hyukjin Kwon"), (120, "Hyukjin Kwon"), (140, "Haejoon Lee")],
...     schema=["age", "name"]
... ).write.bucketBy(2, "name").mode("overwrite").saveAsTable("bucketed_table")
>>> # Read the Parquet file as a DataFrame.
... spark.read.table("bucketed_table").sort("age").show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
|120|Hyukjin Kwon|
|140| Haejoon Lee|
+---+------------+
>>> _ = spark.sql("DROP TABLE bucketed_table")

```


# pyspark.sql.DataFrameWriter.csv — PySpark 4.0.1 documentation
DataFrameWriter.csv(_path_, _mode\=None_, _compression\=None_, _sep\=None_, _quote\=None_, _escape\=None_, _header\=None_, _nullValue\=None_, _escapeQuotes\=None_, _quoteAll\=None_, _dateFormat\=None_, _timestampFormat\=None_, _ignoreLeadingWhiteSpace\=None_, _ignoreTrailingWhiteSpace\=None_, _charToEscapeQuoteEscaping\=None_, _encoding\=None_, _emptyValue\=None_, _lineSep\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.csv)
[#](#pyspark.sql.DataFrameWriter.csv "Permalink to this definition")

Saves the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in CSV format at the specified path.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str

the path in any Hadoop supported file system

**mode**str, optional

specifies the behavior of the save operation when data already exists.

*   `append`: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   `overwrite`: Overwrite existing data.
    
*   `ignore`: Silently ignore this operation if data already exists.
    
*   `error` or `errorifexists` (default case): Throw an exception if data already
    
    exists.
    

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a CSV file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="csv") as d:
...     # Write a DataFrame into a CSV file
...     df = spark.createDataFrame([{"age": 100, "name": "Hyukjin Kwon"}])
...     df.write.csv(d, mode="overwrite")
...
...     # Read the CSV file as a DataFrame with 'nullValue' option set to 'Hyukjin Kwon'.
...     spark.read.schema(df.schema).format("csv").option(
...         "nullValue", "Hyukjin Kwon").load(d).show()
+---+----+
|age|name|
+---+----+
|100|NULL|
+---+----+

```


# pyspark.sql.DataFrameWriter.format — PySpark 4.0.1 documentation
DataFrameWriter.format(_source_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.format)
[#](#pyspark.sql.DataFrameWriter.format "Permalink to this definition")

Specifies the underlying output data source.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**source**str

string, name of the data source, e.g. ‘json’, ‘parquet’.

Examples

```
>>> spark.range(1).write.format('parquet')
<...readwriter.DataFrameWriter object ...>

```


Write a DataFrame into a Parquet file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="format") as d:
...     # Write a DataFrame into a Parquet file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.mode("overwrite").format("parquet").save(d)
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.format('parquet').load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```
# pyspark.sql.DataFrameWriter.insertInto — PySpark 4.0.1 documentation
DataFrameWriter.insertInto(_tableName_, _overwrite\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.insertInto)
[#](#pyspark.sql.DataFrameWriter.insertInto "Permalink to this definition")

Inserts the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to the specified table.

It requires that the schema of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") is the same as the schema of the table.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**overwrite**bool, optional

If true, overwrites existing data. Disabled by default

Notes

Unlike [`DataFrameWriter.saveAsTable()`](about:blank/pyspark.sql.DataFrameWriter.saveAsTable.html#pyspark.sql.DataFrameWriter.saveAsTable "pyspark.sql.DataFrameWriter.saveAsTable"), [`DataFrameWriter.insertInto()`](#pyspark.sql.DataFrameWriter.insertInto "pyspark.sql.DataFrameWriter.insertInto") ignores the column names and just uses position-based resolution.

Examples

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tblA")
>>> df = spark.createDataFrame([
...     (100, "Hyukjin Kwon"), (120, "Hyukjin Kwon"), (140, "Haejoon Lee")],
...     schema=["age", "name"]
... )
>>> df.write.saveAsTable("tblA")

```


Insert the data into ‘tblA’ table but with different column names.

```
>>> df.selectExpr("age AS col1", "name AS col2").write.insertInto("tblA")
>>> spark.read.table("tblA").sort("age").show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
|100|Hyukjin Kwon|
|120|Hyukjin Kwon|
|120|Hyukjin Kwon|
|140| Haejoon Lee|
|140| Haejoon Lee|
+---+------------+
>>> _ = spark.sql("DROP TABLE tblA")

```

# pyspark.sql.DataFrameWriter.jdbc — PySpark 4.0.1 documentation
DataFrameWriter.jdbc(_url_, _table_, _mode\=None_, _properties\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.jdbc)
[#](#pyspark.sql.DataFrameWriter.jdbc "Permalink to this definition")

Saves the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to an external database table via JDBC.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**table**str

Name of the table in the external database.

**mode**str, optional

specifies the behavior of the save operation when data already exists.

*   `append`: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   `overwrite`: Overwrite existing data.
    
*   `ignore`: Silently ignore this operation if data already exists.
    
*   `error` or `errorifexists` (default case): Throw an exception if data already exists.
    

**properties**dict

a dictionary of JDBC database connection arguments. Normally at least properties “user” and “password” with their corresponding values. For example { ‘user’ : ‘SYSTEM’, ‘password’ : ‘mypassword’ }

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html#data-source-option) for the version you use.

Notes

Don’t create too many partitions in parallel on a large cluster; otherwise Spark might crash your external database systems.


# pyspark.sql.DataFrameWriter.json — PySpark 4.0.1 documentation
DataFrameWriter.json(_path_, _mode\=None_, _compression\=None_, _dateFormat\=None_, _timestampFormat\=None_, _lineSep\=None_, _encoding\=None_, _ignoreNullFields\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.json)
[#](#pyspark.sql.DataFrameWriter.json "Permalink to this definition")

Saves the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in JSON format ([JSON Lines text format or newline-delimited JSON](http://jsonlines.org/)) at the specified path.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str

the path in any Hadoop supported file system

**mode**str, optional

specifies the behavior of the save operation when data already exists.

*   `append`: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   `overwrite`: Overwrite existing data.
    
*   `ignore`: Silently ignore this operation if data already exists.
    
*   `error` or `errorifexists` (default case): Throw an exception if data already exists.
    

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a JSON file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="json") as d:
...     # Write a DataFrame into a JSON file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.json(d, mode="overwrite")
...
...     # Read the JSON file as a DataFrame.
...     spark.read.format("json").load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```


# pyspark.sql.DataFrameWriter.mode — PySpark 4.0.1 documentation
DataFrameWriter.mode(_saveMode_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.mode)
[#](#pyspark.sql.DataFrameWriter.mode "Permalink to this definition")

Specifies the behavior when data or table already exists.

Options include:

*   append: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   overwrite: Overwrite existing data.
    
*   error or errorifexists: Throw an exception if data already exists.
    
*   ignore: Silently ignore this operation if data already exists.
    

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

Raise an error when writing to an existing path.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="mode1") as d:
...     spark.createDataFrame(
...         [{"age": 80, "name": "Xinrong Meng"}]
...     ).write.mode("error").format("parquet").save(d) 
Traceback (most recent call last):
    ...
...AnalysisException: ...

```


Write a Parquet file back with various options, and read it back.

```
>>> with tempfile.TemporaryDirectory(prefix="mode2") as d:
...     # Overwrite the path with a new Parquet file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.mode("overwrite").format("parquet").save(d)
...
...     # Append another DataFrame into the Parquet file
...     spark.createDataFrame(
...         [{"age": 120, "name": "Takuya Ueshin"}]
...     ).write.mode("append").format("parquet").save(d)
...
...     # Append another DataFrame into the Parquet file
...     spark.createDataFrame(
...         [{"age": 140, "name": "Haejoon Lee"}]
...     ).write.mode("ignore").format("parquet").save(d)
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.parquet(d).show()
+---+-------------+
|age|         name|
+---+-------------+
|120|Takuya Ueshin|
|100| Hyukjin Kwon|
+---+-------------+

```


# pyspark.sql.DataFrameWriter.option — PySpark 4.0.1 documentation
DataFrameWriter.option(_key_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.option)
[#](#pyspark.sql.DataFrameWriter.option "Permalink to this definition")

Adds an output option for the underlying data source.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**key**str

The key for the option to set.

**value**

The value for the option to set.

Examples

```
>>> spark.range(1).write.option("key", "value")
<...readwriter.DataFrameWriter object ...>

```


Specify the option ‘nullValue’ with writing a CSV file.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="option") as d:
...     # Write a DataFrame into a CSV file with 'nullValue' option set to 'Hyukjin Kwon'.
...     df = spark.createDataFrame([(100, None)], "age INT, name STRING")
...     df.write.option("nullValue", "Hyukjin Kwon").mode("overwrite").format("csv").save(d)
...
...     # Read the CSV file as a DataFrame.
...     spark.read.schema(df.schema).format('csv').load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```

# pyspark.sql.DataFrameWriter.options — PySpark 4.0.1 documentation
DataFrameWriter.options(_\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.options)
[#](#pyspark.sql.DataFrameWriter.options "Permalink to this definition")

Adds output options for the underlying data source.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**\*\*options**dict

The dictionary of string keys and primitive-type values.

Examples

```
>>> spark.range(1).write.options(key="value")
<...readwriter.DataFrameWriter object ...>

```


Specify options in a dictionary.

```
>>> spark.range(1).write.options(**{"k1": "v1", "k2": "v2"})
<...readwriter.DataFrameWriter object ...>

```


Specify the option ‘nullValue’ and ‘header’ with writing a CSV file.

```
>>> from pyspark.sql.types import StructType,StructField, StringType, IntegerType
>>> schema = StructType([
...     StructField("age",IntegerType(),True),
...     StructField("name",StringType(),True),
... ])
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="options") as d:
...     # Write a DataFrame into a CSV file with 'nullValue' option set to 'Hyukjin Kwon',
...     # and 'header' option set to `True`.
...     df = spark.createDataFrame([(100, None)], schema=schema)
...     df.write.options(nullValue="Hyukjin Kwon", header=True).mode(
...         "overwrite").format("csv").save(d)
...
...     # Read the CSV file as a DataFrame.
...     spark.read.option("header", True).format('csv').load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```


# pyspark.sql.DataFrameWriter.orc — PySpark 4.0.1 documentation
DataFrameWriter.orc(_path_, _mode\=None_, _partitionBy\=None_, _compression\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.orc)
[#](#pyspark.sql.DataFrameWriter.orc "Permalink to this definition")

Saves the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in ORC format at the specified path.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str

the path in any Hadoop supported file system

**mode**str, optional

specifies the behavior of the save operation when data already exists.

*   `append`: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   `overwrite`: Overwrite existing data.
    
*   `ignore`: Silently ignore this operation if data already exists.
    
*   `error` or `errorifexists` (default case): Throw an exception if data already exists.
    

**partitionBy**str or list, optional

names of partitioning columns

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-orc.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a ORC file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="orc") as d:
...     # Write a DataFrame into a ORC file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.orc(d, mode="overwrite")
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.format("orc").load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```

# pyspark.sql.DataFrameWriter.parquet — PySpark 4.0.1 documentation
DataFrameWriter.parquet(_path_, _mode\=None_, _partitionBy\=None_, _compression\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.parquet)
[#](#pyspark.sql.DataFrameWriter.parquet "Permalink to this definition")

Saves the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") in Parquet format at the specified path.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str

the path in any Hadoop supported file system

**mode**str, optional

specifies the behavior of the save operation when data already exists.

*   `append`: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   `overwrite`: Overwrite existing data.
    
*   `ignore`: Silently ignore this operation if data already exists.
    
*   `error` or `errorifexists` (default case): Throw an exception if data already exists.
    

**partitionBy**str or list, optional

names of partitioning columns

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-parquet.html#data-source-option) for the version you use.

Examples

Write a DataFrame into a Parquet file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="parquet") as d:
...     # Write a DataFrame into a Parquet file
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}]
...     ).write.parquet(d, mode="overwrite")
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.format("parquet").load(d).show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
+---+------------+

```


# pyspark.sql.DataFrameWriter.partitionBy — PySpark 4.0.1 documentation
DataFrameWriter.partitionBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.partitionBy)
[#](#pyspark.sql.DataFrameWriter.partitionBy "Permalink to this definition")

Partitions the output by the given columns on the file system.

If specified, the output is laid out on the file system similar to Hive’s partitioning scheme.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**str or list

name of columns

Examples

Write a DataFrame into a Parquet file in a partitioned manner, and read it back.

```
>>> import tempfile
>>> import os
>>> with tempfile.TemporaryDirectory(prefix="partitionBy") as d:
...     # Write a DataFrame into a Parquet file in a partitioned manner.
...     spark.createDataFrame(
...         [{"age": 100, "name": "Hyukjin Kwon"}, {"age": 120, "name": "Ruifeng Zheng"}]
...     ).write.partitionBy("name").mode("overwrite").format("parquet").save(d)
...
...     # Read the Parquet file as a DataFrame.
...     spark.read.parquet(d).sort("age").show()
...
...     # Read one partition as a DataFrame.
...     spark.read.parquet(f"{d}{os.path.sep}name=Hyukjin Kwon").show()
+---+-------------+
|age|         name|
+---+-------------+
|100| Hyukjin Kwon|
|120|Ruifeng Zheng|
+---+-------------+
+---+
|age|
+---+
|100|
+---+

```


# pyspark.sql.DataFrameWriter.save — PySpark 4.0.1 documentation
DataFrameWriter.save(_path\=None_, _format\=None_, _mode\=None_, _partitionBy\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.save)
[#](#pyspark.sql.DataFrameWriter.save "Permalink to this definition")

Saves the contents of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to a data source.

The data source is specified by the `format` and a set of `options`. If `format` is not specified, the default data source configured by `spark.sql.sources.default` will be used.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str, optional

the path in a Hadoop supported file system

**format**str, optional

the format used to save

**mode**str, optional

specifies the behavior of the save operation when data already exists.

*   `append`: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   `overwrite`: Overwrite existing data.
    
*   `ignore`: Silently ignore this operation if data already exists.
    
*   `error` or `errorifexists` (default case): Throw an exception if data already exists.
    

**partitionBy**list, optional

names of partitioning columns

**\*\*options**dict

all other string options

Examples

Write a DataFrame into a JSON file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="save") as d:
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


# pyspark.sql.DataFrameWriter.saveAsTable — PySpark 4.0.1 documentation
DataFrameWriter.saveAsTable(_name_, _format\=None_, _mode\=None_, _partitionBy\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.saveAsTable)
[#](#pyspark.sql.DataFrameWriter.saveAsTable "Permalink to this definition")

Saves the content of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") as the specified table.

In the case the table already exists, behavior of this function depends on the save mode, specified by the mode function (default to throwing an exception). When mode is Overwrite, the schema of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") does not need to be the same as that of the existing table.

*   append: Append contents of this [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") to existing data.
    
*   overwrite: Overwrite existing data.
    
*   error or errorifexists: Throw an exception if data already exists.
    
*   ignore: Silently ignore this operation if data already exists.
    

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**str

the table name

**format**str, optional

the format used to save

**mode**str, optional

one of append, overwrite, error, errorifexists, ignore (default: error)

**partitionBy**str or list

names of partitioning columns

**\*\*options**dict

all other string options

Notes

When mode is Append, if there is an existing table, we will use the format and options of the existing table. The column order in the schema of the [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") doesn’t need to be the same as that of the existing table. Unlike [`DataFrameWriter.insertInto()`](about:blank/pyspark.sql.DataFrameWriter.insertInto.html#pyspark.sql.DataFrameWriter.insertInto "pyspark.sql.DataFrameWriter.insertInto"), [`DataFrameWriter.saveAsTable()`](#pyspark.sql.DataFrameWriter.saveAsTable "pyspark.sql.DataFrameWriter.saveAsTable") will use the column names to find the correct column positions.

Examples

Creates a table from a DataFrame, and read it back.

```
>>> _ = spark.sql("DROP TABLE IF EXISTS tblA")
>>> spark.createDataFrame([
...     (100, "Hyukjin Kwon"), (120, "Hyukjin Kwon"), (140, "Haejoon Lee")],
...     schema=["age", "name"]
... ).write.saveAsTable("tblA")
>>> spark.read.table("tblA").sort("age").show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
|120|Hyukjin Kwon|
|140| Haejoon Lee|
+---+------------+
>>> _ = spark.sql("DROP TABLE tblA")

```


# pyspark.sql.DataFrameWriter.sortBy — PySpark 4.0.1 documentation
DataFrameWriter.sortBy(_col_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.sortBy)
[#](#pyspark.sql.DataFrameWriter.sortBy "Permalink to this definition")

Sorts the output in each bucket by the given columns on the file system.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**str, tuple or list

a name of a column, or a list of names.

**cols**str

additional names (optional). If col is a list it should be empty.

Examples

Write a DataFrame into a Parquet file in a sorted-buckted manner, and read it back.

```
>>> from pyspark.sql.functions import input_file_name
>>> # Write a DataFrame into a Parquet file in a sorted-bucketed manner.
... _ = spark.sql("DROP TABLE IF EXISTS sorted_bucketed_table")
>>> spark.createDataFrame([
...     (100, "Hyukjin Kwon"), (120, "Hyukjin Kwon"), (140, "Haejoon Lee")],
...     schema=["age", "name"]
... ).write.bucketBy(1, "name").sortBy("age").mode(
...     "overwrite").saveAsTable("sorted_bucketed_table")
>>> # Read the Parquet file as a DataFrame.
... spark.read.table("sorted_bucketed_table").sort("age").show()
+---+------------+
|age|        name|
+---+------------+
|100|Hyukjin Kwon|
|120|Hyukjin Kwon|
|140| Haejoon Lee|
+---+------------+
>>> _ = spark.sql("DROP TABLE sorted_bucketed_table")

```


# pyspark.sql.DataFrameWriter.text — PySpark 4.0.1 documentation
DataFrameWriter.text(_path_, _compression\=None_, _lineSep\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriter.text)
[#](#pyspark.sql.DataFrameWriter.text "Permalink to this definition")

Saves the content of the DataFrame in a text file at the specified path. The text files will be encoded as UTF-8.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**path**str

the path in any Hadoop supported file system

Other Parameters

**Extra options**

For the extra options, refer to [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-text.html#data-source-option) for the version you use.

Notes

The DataFrame must have only one column that is of string type. Each row becomes a new line in the output file.

Examples

Write a DataFrame into a text file and read it back.

```
>>> import tempfile
>>> with tempfile.TemporaryDirectory(prefix="text") as d:
...     # Write a DataFrame into a text file
...     df = spark.createDataFrame([("a",), ("b",), ("c",)], schema=["alphabets"])
...     df.write.mode("overwrite").text(d)
...
...     # Read the text file as a DataFrame.
...     spark.read.schema(df.schema).format("text").load(d).sort("alphabets").show()
+---------+
|alphabets|
+---------+
|        a|
|        b|
|        c|
+---------+

```


# pyspark.sql.DataFrameWriterV2.using — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.using

DataFrameWriterV2.using(_provider_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.using)
[#](#pyspark.sql.DataFrameWriterV2.using "Permalink to this definition")

Specifies a provider for the underlying output data source. Spark’s default catalog supports “parquet”, “json”, etc.

# pyspark.sql.DataFrameWriterV2.option — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.option

DataFrameWriterV2.option(_key_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.option)
[#](#pyspark.sql.DataFrameWriterV2.option "Permalink to this definition")

Add a write option.

# pyspark.sql.DataFrameWriterV2.options — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.options

DataFrameWriterV2.options(_\*\*options_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.options)
[#](#pyspark.sql.DataFrameWriterV2.options "Permalink to this definition")

Add write options.


# pyspark.sql.DataFrameWriterV2.tableProperty — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.tableProperty

DataFrameWriterV2.tableProperty(_property_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.tableProperty)
[#](#pyspark.sql.DataFrameWriterV2.tableProperty "Permalink to this definition")

Add table property.


# pyspark.sql.DataFrameWriterV2.partitionedBy — PySpark 4.0.1 documentation
DataFrameWriterV2.partitionedBy(_col_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.partitionedBy)
[#](#pyspark.sql.DataFrameWriterV2.partitionedBy "Permalink to this definition")

Partition the output table created by create, createOrReplace, or replace using the given columns or transforms.

When specified, the table data will be stored by these values for efficient reads.

For example, when a table is partitioned by day, it may be stored in a directory layout like:

*   table/day=2019-06-01/
    
*   table/day=2019-06-02/
    

Partitioning is one of the most widely used techniques to optimize physical data layout. It provides a coarse-grained index for skipping unnecessary data reads when queries have predicates on the partitioned columns. In order for partitioning to work well, the number of distinct values in each column should typically be less than tens of thousands.

col and cols support only the following functions:

*   `pyspark.sql.functions.years()`
    
*   `pyspark.sql.functions.months()`
    
*   `pyspark.sql.functions.days()`
    
*   `pyspark.sql.functions.hours()`
    
*   `pyspark.sql.functions.bucket()`


# pyspark.sql.DataFrameWriterV2.create — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.create

DataFrameWriterV2.create()
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.create)
[#](#pyspark.sql.DataFrameWriterV2.create "Permalink to this definition")

Create a new table from the contents of the data frame.

The new table’s schema, partition layout, properties, and other configuration will be based on the configuration set on this writer.


# pyspark.sql.DataFrameWriterV2.replace — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.replace

DataFrameWriterV2.replace()
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.replace)
[#](#pyspark.sql.DataFrameWriterV2.replace "Permalink to this definition")

Replace an existing table with the contents of the data frame.

The existing table’s schema, partition layout, properties, and other configuration will be replaced with the contents of the data frame and the configuration set on this writer.

[Show Source](../../../_sources/reference/pyspark.sql/api/pyspark.sql.DataFrameWriterV2.replace.rst.txt)


# pyspark.sql.DataFrameWriterV2.createOrReplace — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.createOrReplace

DataFrameWriterV2.createOrReplace()
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.createOrReplace)
[#](#pyspark.sql.DataFrameWriterV2.createOrReplace "Permalink to this definition")

Create a new table or replace an existing table with the contents of the data frame.

The output table’s schema, partition layout, properties, and other configuration will be based on the contents of the data frame and the configuration set on this writer. If the table exists, its configuration and data will be replaced.


# pyspark.sql.DataFrameWriterV2.append — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.append

DataFrameWriterV2.append()
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.append)
[#](#pyspark.sql.DataFrameWriterV2.append "Permalink to this definition")

Append the contents of the data frame to the output table.


# pyspark.sql.DataFrameWriterV2.overwrite — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.overwrite

DataFrameWriterV2.overwrite(_condition_)
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.overwrite)
[#](#pyspark.sql.DataFrameWriterV2.overwrite "Permalink to this definition")

Overwrite rows matching the given filter condition with the contents of the data frame in the output table.


# pyspark.sql.DataFrameWriterV2.overwritePartitions — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.DataFrameWriterV2.overwritePartitions

DataFrameWriterV2.overwritePartitions()
[\[source\]](about:blank/_modules/pyspark/sql/readwriter.html#DataFrameWriterV2.overwritePartitions)
[#](#pyspark.sql.DataFrameWriterV2.overwritePartitions "Permalink to this definition")

Overwrite all partition for which the data frame contains at least one row with the contents of the data frame in the output table.

This operation is equivalent to Hive’s INSERT OVERWRITE … PARTITION, which replaces partitions dynamically depending on the contents of the data frame.


# pyspark.sql.MergeIntoWriter.whenMatched — PySpark 4.0.1 documentation
MergeIntoWriter.whenMatched(_condition\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/merge.html#MergeIntoWriter.whenMatched)
[#](#pyspark.sql.MergeIntoWriter.whenMatched "Permalink to this definition")

Initialize a WhenMatched action with a condition.

This WhenMatched action will be executed when a source row matches a target table row based on the merge condition and the specified condition is satisfied.

This WhenMatched can be followed by one of the following merge actions:

*   updateAll: Update all the matched target table rows with source dataset rows.
    
*   update(Dict): Update all the matched target table rows while changing only a subset of columns based on the provided assignment.
    
*   delete: Delete all target rows that have a match in the source table.


# pyspark.sql.MergeIntoWriter.whenNotMatched — PySpark 4.0.1 documentation
MergeIntoWriter.whenNotMatched(_condition\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/merge.html#MergeIntoWriter.whenNotMatched)
[#](#pyspark.sql.MergeIntoWriter.whenNotMatched "Permalink to this definition")

Initialize a WhenNotMatched action with a condition.

This WhenNotMatched action will be executed when a source row does not match any target row based on the merge condition and the specified condition is satisfied.

This WhenNotMatched can be followed by one of the following merge actions:

*   insertAll: Insert all rows from the source that are not already in the target table.
    
*   insert(Dict): Insert all rows from the source that are not already in the target table, with the specified columns based on the provided assignment.


# pyspark.sql.MergeIntoWriter.whenNotMatchedBySource — PySpark 4.0.1 documentation
MergeIntoWriter.whenNotMatchedBySource(_condition\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/merge.html#MergeIntoWriter.whenNotMatchedBySource)
[#](#pyspark.sql.MergeIntoWriter.whenNotMatchedBySource "Permalink to this definition")

Initialize a WhenNotMatchedBySource action with a condition.

This WhenNotMatchedBySource action will be executed when a target row does not match any rows in the source table based on the merge condition and the specified condition is satisfied.

This WhenNotMatchedBySource can be followed by one of the following merge actions:

*   updateAll: Update all the not matched target table rows with source dataset rows.
    
*   update(Dict): Update all the not matched target table rows while changing only the specified columns based on the provided assignment.
    
*   delete: Delete all target rows that have no matches in the source table.


# pyspark.sql.MergeIntoWriter.withSchemaEvolution — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.MergeIntoWriter.withSchemaEvolution

MergeIntoWriter.withSchemaEvolution()
[\[source\]](about:blank/_modules/pyspark/sql/merge.html#MergeIntoWriter.withSchemaEvolution)
[#](#pyspark.sql.MergeIntoWriter.withSchemaEvolution "Permalink to this definition")

Enable automatic schema evolution for this merge operation.


# pyspark.sql.MergeIntoWriter.merge — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.sql.MergeIntoWriter.merge

MergeIntoWriter.merge()
[\[source\]](about:blank/_modules/pyspark/sql/merge.html#MergeIntoWriter.merge)
[#](#pyspark.sql.MergeIntoWriter.merge "Permalink to this definition")

Execute the merge operation.

