# Input/Output — PySpark 4.0.1 documentation
Data Generator[#](#data-generator "Permalink to this headline")
---------------------------------------------------------------



Spark Metastore Table[#](#spark-metastore-table "Permalink to this headline")
-----------------------------------------------------------------------------


|read_table(name[, index_col])                |Read a Spark table and return a DataFrame.|
|---------------------------------------------|------------------------------------------|
|DataFrame.to_table(name[, format, mode, ...])|Write the DataFrame into a Spark table.   |


Delta Lake[#](#delta-lake "Permalink to this headline")
-------------------------------------------------------



* read_delta(path[, version, timestamp, index_col]): DataFrame.to_delta(path[, mode, ...])
  * Read a Delta Lake table on some file system and return a DataFrame.: Write the DataFrame out as a Delta Lake table.


Parquet[#](#parquet "Permalink to this headline")
-------------------------------------------------



* read_parquet(path[, columns, index_col, ...]): DataFrame.to_parquet(path[, mode, ...])
  * Load a parquet object from the file path, returning a DataFrame.: Write the DataFrame out as a Parquet file or directory.


ORC[#](#orc "Permalink to this headline")
-----------------------------------------



* read_orc(path[, columns, index_col]): DataFrame.to_orc(path[, mode, ...])
  * Load an ORC object from the file path, returning a DataFrame.: Write a DataFrame to the ORC format.


Generic Spark I/O[#](#generic-spark-i-o "Permalink to this headline")
---------------------------------------------------------------------





Flat File / CSV[#](#flat-file-csv "Permalink to this headline")
---------------------------------------------------------------



* read_csv(path[, sep, header, names, ...]): DataFrame.to_csv([path, sep, na_rep, ...])
  * Read CSV (comma-separated) file into DataFrame or Series.: Write object to a comma-separated values (csv) file.


Clipboard[#](#clipboard "Permalink to this headline")
-----------------------------------------------------


|read_clipboard([sep])               |Read text from clipboard and pass to read_csv.|
|------------------------------------|----------------------------------------------|
|DataFrame.to_clipboard([excel, sep])|Copy object to the system clipboard.          |


Excel[#](#excel "Permalink to this headline")
---------------------------------------------



* read_excel(io[, sheet_name, header, names, ...]): DataFrame.to_excel(excel_writer[, ...])
  * Read an Excel file into a pandas-on-Spark DataFrame or Series.: Write object to an Excel sheet.


JSON[#](#json "Permalink to this headline")
-------------------------------------------



* json_normalize(data[, sep]): read_json(path[, lines, index_col])
  * Normalize semi-structured JSON data into a flat table.: Convert a JSON string to DataFrame.
* json_normalize(data[, sep]): DataFrame.to_json([path, compression, ...])
  * Normalize semi-structured JSON data into a flat table.: Convert the object to a JSON string.


HTML[#](#html "Permalink to this headline")
-------------------------------------------



* read_html(io[, match, flavor, header, ...]): DataFrame.to_html([buf, columns, col_space, ...])
  * Read HTML tables into a list of DataFrame objects.: Render a DataFrame as an HTML table.


SQL[#](#sql "Permalink to this headline")
-----------------------------------------



* read_sql_table(table_name, con[, schema, ...]): read_sql_query(sql, con[, index_col])
  * Read SQL database table into a DataFrame.: Read SQL query into a DataFrame.
* read_sql_table(table_name, con[, schema, ...]): read_sql(sql, con[, index_col, columns])
  * Read SQL database table into a DataFrame.: Read SQL query or database table into a DataFrame.


# pyspark.pandas.range — PySpark 4.0.1 documentation
pyspark.pandas.range(_start_, _end\=None_, _step\=1_, _num\_partitions\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#range)
[#](#pyspark.pandas.range "Permalink to this definition")

Create a DataFrame with some range of numbers.

The resulting DataFrame has a single int64 column named id, containing elements in a range from `start` to `end` (exclusive) with step value `step`. If only the first parameter (i.e. start) is specified, we treat it as the end value with the start value being 0.

This is like the range function in SparkSession and is used primarily for testing.

Parameters

**start**int

the start value (inclusive)

**end**int, optional

the end value (exclusive)

**step**int, optional, default 1

the incremental step

**num\_partitions**int, optional

the number of partitions of the DataFrame

Returns

DataFrame

Examples

When the first parameter is specified, we generate a range of values up till that number.

```
>>> ps.range(5)
   id
0   0
1   1
2   2
3   3
4   4

```


When start, end, and step are specified:

```
>>> ps.range(start = 100, end = 200, step = 20)
    id
0  100
1  120
2  140
3  160
4  180

```


# pyspark.pandas.read_table — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.pandas.read\_table

pyspark.pandas.read\_table(_name_, _index\_col\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_table)
[#](#pyspark.pandas.read_table "Permalink to this definition")

Read a Spark table and return a DataFrame.

Parameters

**name**string

Table name in Spark.

**index\_col**str or list of str, optional, default: None

Index column of table in Spark.

Returns

DataFrame

Examples

```
>>> ps.range(1).to_table('%s.my_table' % db)
>>> ps.read_table('%s.my_table' % db)
   id
0   0

```


```
>>> ps.range(1).to_table('%s.my_table' % db, index_col="index")
>>> ps.read_table('%s.my_table' % db, index_col="index")  
       id
index
0       0

```


# pyspark.pandas.DataFrame.to_table — PySpark 4.0.1 documentation
DataFrame.to\_table(_name_, _format\=None_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_table)
[#](#pyspark.pandas.DataFrame.to_table "Permalink to this definition")

Write the DataFrame into a Spark table. [`DataFrame.spark.to_table()`](about:blank/pyspark.pandas.DataFrame.spark.to_table.html#pyspark.pandas.DataFrame.spark.to_table "pyspark.pandas.DataFrame.spark.to_table") is an alias of [`DataFrame.to_table()`](#pyspark.pandas.DataFrame.to_table "pyspark.pandas.DataFrame.to_table").

Parameters

**name**str, required

Table name in Spark.

**format**string, optional

Specifies the output data source format. Some common ones are:

*   ‘delta’
    
*   ‘parquet’
    
*   ‘orc’
    
*   ‘json’
    
*   ‘csv’
    

**mode**str {‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’}, default

‘overwrite’. Specifies the behavior of the save operation when the table exists already.

*   ‘append’: Append the new data to existing data.
    
*   ‘overwrite’: Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options**

Additional options passed directly to Spark.

Returns

None

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_table('%s.my_table' % db, partition_cols='date')

```

# pyspark.pandas.read_delta — PySpark 4.0.1 documentation
pyspark.pandas.read\_delta(_path_, _version\=None_, _timestamp\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_delta)
[#](#pyspark.pandas.read_delta "Permalink to this definition")

Read a Delta Lake table on some file system and return a DataFrame.

If the Delta Lake table is already stored in the catalog (aka the metastore), use ‘read\_table’.

Parameters

**path**string

Path to the Delta Lake table.

**version**string, optional

Specifies the table version (based on Delta’s internal transaction version) to read from, using Delta’s time travel feature. This sets Delta’s ‘versionAsOf’ option. Note that this parameter and timestamp parameter cannot be used together, otherwise it will raise a ValueError.

**timestamp**string, optional

Specifies the table version (based on timestamp) to read from, using Delta’s time travel feature. This must be a valid date or timestamp string in Spark, and sets Delta’s ‘timestampAsOf’ option. Note that this parameter and version parameter cannot be used together, otherwise it will raise a ValueError.

**index\_col**str or list of str, optional, default: None

Index column of table in Spark.

**options**

Additional options that can be passed onto Delta.

Returns

DataFrame

Examples

```
>>> ps.range(1).to_delta('%s/read_delta/foo' % path)  
>>> ps.read_delta('%s/read_delta/foo' % path)  
   id
0   0

```


```
>>> ps.range(10, 15, num_partitions=1).to_delta('%s/read_delta/foo' % path,
...                                             mode='overwrite')  
>>> ps.read_delta('%s/read_delta/foo' % path)  
   id
0  10
1  11
2  12
3  13
4  14

```


```
>>> ps.read_delta('%s/read_delta/foo' % path, version=0)  
   id
0   0

```


You can preserve the index in the roundtrip as below.

```
>>> ps.range(10, 15, num_partitions=1).to_delta(
...     '%s/read_delta/bar' % path, index_col="index")  
>>> ps.read_delta('%s/read_delta/bar' % path, index_col="index")  
       id
index
0      10
1      11
2      12
3      13
4      14

```


# pyspark.pandas.DataFrame.to_delta — PySpark 4.0.1 documentation
DataFrame.to\_delta(_path_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_delta)
[#](#pyspark.pandas.DataFrame.to_delta "Permalink to this definition")

Write the DataFrame out as a Delta Lake table.

Parameters

**path**str, required

Path to write to.

**mode**str

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default the index is always lost.

**options**dict

All other options passed directly into Delta Lake.

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


Create a new Delta Lake table, partitioned by one column:

```
>>> df.to_delta('%s/to_delta/foo' % path, partition_cols='date')  

```


Partitioned by two columns:

```
>>> df.to_delta('%s/to_delta/bar' % path,
...             partition_cols=['date', 'country'])  

```


Overwrite an existing table’s partitions, using the ‘replaceWhere’ capability in Delta:

```
>>> df.to_delta('%s/to_delta/bar' % path,
...             mode='overwrite', replaceWhere='date >= "2012-01-01"')  

```


# pyspark.pandas.read_parquet — PySpark 4.0.1 documentation
pyspark.pandas.read\_parquet(_path_, _columns\=None_, _index\_col\=None_, _pandas\_metadata\=False_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_parquet)
[#](#pyspark.pandas.read_parquet "Permalink to this definition")

Load a parquet object from the file path, returning a DataFrame.

Parameters

**path**string

File path

**columns**list, default=None

If not None, only these columns will be read from the file.

**index\_col**str or list of str, optional, default: None

Index column of table in Spark.

**pandas\_metadata**bool, default: False

If True, try to respect the metadata if the Parquet file is written from pandas.

**options**dict

All other options passed directly into Spark’s data source.

Returns

DataFrame

Examples

```
>>> ps.range(1).to_parquet('%s/read_spark_io/data.parquet' % path)
>>> ps.read_parquet('%s/read_spark_io/data.parquet' % path, columns=['id'])
   id
0   0

```


You can preserve the index in the roundtrip as below.

```
>>> ps.range(1).to_parquet('%s/read_spark_io/data.parquet' % path, index_col="index")
>>> ps.read_parquet('%s/read_spark_io/data.parquet' % path, columns=['id'], index_col="index")
... 
       id
index
0       0

```


# pyspark.pandas.DataFrame.to_parquet — PySpark 4.0.1 documentation
DataFrame.to\_parquet(_path_, _mode\='w'_, _partition\_cols\=None_, _compression\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_parquet)
[#](#pyspark.pandas.DataFrame.to_parquet "Permalink to this definition")

Write the DataFrame out as a Parquet file or directory.

Parameters

**path**str, required

Path to write to.

**mode**str

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**compression**str {‘none’, ‘uncompressed’, ‘snappy’, ‘gzip’, ‘lzo’, ‘brotli’, ‘lz4’, ‘zstd’}

Compression codec to use when saving to file. If None is set, it uses the value specified in spark.sql.parquet.compression.codec.

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default the index is always lost.

**options**dict

All other options passed directly into Spark’s data source.

Notes

pandas API on Spark writes Parquet files into the directory, path, and writes multiple part files in the directory unlike pandas. pandas API on Spark respects HDFS’s property such as ‘fs.default.name’.

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_parquet('%s/to_parquet/foo.parquet' % path, partition_cols='date')

```


```
>>> df.to_parquet(
...     '%s/to_parquet/foo.parquet' % path,
...     mode = 'overwrite',
...     partition_cols=['date', 'country'])

```


# pyspark.pandas.read_orc — PySpark 4.0.1 documentation
pyspark.pandas.read\_orc(_path_, _columns\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_orc)
[#](#pyspark.pandas.read_orc "Permalink to this definition")

Load an ORC object from the file path, returning a DataFrame.

Parameters

**path**str

The path string storing the ORC file to be read.

**columns**list, default None

If not None, only these columns will be read from the file.

**index\_col**str or list of str, optional, default: None

Index column of table in Spark.

**options**dict

All other options passed directly into Spark’s data source.

Returns

DataFrame

Examples

```
>>> ps.range(1).to_orc('%s/read_spark_io/data.orc' % path)
>>> ps.read_orc('%s/read_spark_io/data.orc' % path, columns=['id'])
   id
0   0

```


You can preserve the index in the roundtrip as below.

```
>>> ps.range(1).to_orc('%s/read_spark_io/data.orc' % path, index_col="index")
>>> ps.read_orc('%s/read_spark_io/data.orc' % path, columns=['id'], index_col="index")
... 
       id
index
0       0

```


# pyspark.pandas.DataFrame.to_orc — PySpark 4.0.1 documentation
DataFrame.to\_orc(_path_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_orc)
[#](#pyspark.pandas.DataFrame.to_orc "Permalink to this definition")

Write a DataFrame to the ORC format.

Parameters

**path**str

Path to write to.

**mode**str

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default the index is always lost.

**options**dict

All other options passed directly into Spark’s data source.

Notes

pandas API on Spark writes ORC files into the directory, path, and writes multiple part files in the directory unlike pandas. pandas API on Spark respects HDFS’s property such as ‘fs.default.name’.

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_orc('%s/to_orc/foo.orc' % path, partition_cols='date')

```


```
>>> df.to_orc(
...     '%s/to_orc/foo.orc' % path,
...     mode = 'overwrite',
...     partition_cols=['date', 'country'])

```


# pyspark.pandas.read_spark_io — PySpark 4.0.1 documentation
pyspark.pandas.read\_spark\_io(_path\=None_, _format\=None_, _schema\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_spark_io)
[#](#pyspark.pandas.read_spark_io "Permalink to this definition")

Load a DataFrame from a Spark data source.

Parameters

**path**string, optional

Path to the data source.

**format**string, optional

Specifies the output data source format. Some common ones are:

*   ‘delta’
    
*   ‘parquet’
    
*   ‘orc’
    
*   ‘json’
    
*   ‘csv’
    

**schema**string or StructType, optional

Input schema. If none, Spark tries to infer the schema automatically. The schema can either be a Spark StructType, or a DDL-formatted string like col0 INT, col1 DOUBLE.

**index\_col**str or list of str, optional, default: None

Index column of table in Spark.

**options**dict

All other options passed directly into Spark’s data source.

See also

`DataFrame.read_table`

`DataFrame.read_delta`

`DataFrame.read_parquet`

Examples

```
>>> ps.range(1).spark.to_spark_io('%s/read_spark_io/data.parquet' % path)
>>> ps.read_spark_io(
...     '%s/read_spark_io/data.parquet' % path, format='parquet', schema='id long')
   id
0   0

```


```
>>> ps.range(10, 15, num_partitions=1).spark.to_spark_io('%s/read_spark_io/data.json' % path,
...                                                format='json', lineSep='__')
>>> ps.read_spark_io(
...     '%s/read_spark_io/data.json' % path, format='json', schema='id long', lineSep='__')
   id
0  10
1  11
2  12
3  13
4  14

```


You can preserve the index in the roundtrip as below.

```
>>> ps.range(10, 15, num_partitions=1).spark.to_spark_io('%s/read_spark_io/data.orc' % path,
...                                                format='orc', index_col="index")
>>> ps.read_spark_io(
...     path=r'%s/read_spark_io/data.orc' % path, format="orc", index_col="index")
... 
       id
index
0      10
1      11
2      12
3      13
4      14

```

# pyspark.pandas.DataFrame.spark.to_spark_io — PySpark 4.0.1 documentation
spark.to\_spark\_io(_path\=None_, _format\=None_, _mode\='overwrite'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.spark.to_spark_io "Permalink to this definition")

Write the DataFrame out to a Spark data source.

Parameters

**path**string, optional

Path to the data source.

**format**string, optional

Specifies the output data source format. Some common ones are:

*   ‘delta’
    
*   ‘parquet’
    
*   ‘orc’
    
*   ‘json’
    
*   ‘csv’
    

**mode**str {‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’}, default

‘overwrite’. Specifies the behavior of the save operation when data already exists.

*   ‘append’: Append the new data to existing data.
    
*   ‘overwrite’: Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options**dict

All other options passed directly into Spark’s data source.

Returns

None

See also

`read_spark_io`

`DataFrame.to_delta`

`DataFrame.to_parquet`

`DataFrame.to_table`

`DataFrame.spark.to_spark_io`

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.spark.to_spark_io(path='%s/to_spark_io/foo.json' % path, format='json')

```



# pyspark.pandas.read_csv — PySpark 4.0.1 documentation
pyspark.pandas.read\_csv(_path_, _sep\=','_, _header\='infer'_, _names\=None_, _index\_col\=None_, _usecols\=None_, _dtype\=None_, _nrows\=None_, _parse\_dates\=False_, _quotechar\=None_, _escapechar\=None_, _comment\=None_, _encoding\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_csv)
[#](#pyspark.pandas.read_csv "Permalink to this definition")

Read CSV (comma-separated) file into DataFrame or Series.

Parameters

**path**str or list

Path(s) of the CSV file(s) to be read.

**sep**str, default ‘,’

Delimiter to use. Non empty string.

**header**int, default ‘infer’

Whether to use the column names, and the start of the data. Default behavior is to infer the column names: if no names are passed the behavior is identical to header=0 and column names are inferred from the first line of the file, if column names are passed explicitly then the behavior is identical to header=None. Explicitly pass header=0 to be able to replace existing names

**names**str or array-like, optional

List of column names to use. If file contains no header row, then you should explicitly pass header=None. Duplicates in this list will cause an error to be issued. If a string is given, it should be a DDL-formatted string in Spark SQL, which is preferred to avoid schema inference for better performance.

**index\_col: str or list of str, optional, default: None**

Index column of table in Spark.

**usecols**list-like or callable, optional

Return a subset of the columns. If list-like, all elements must either be positional (i.e. integer indices into the document columns) or strings that correspond to column names provided either by the user in names or inferred from the document header row(s). If callable, the callable function will be evaluated against the column names, returning names where the callable function evaluates to True.

**dtype**Type name or dict of column -> type, default None

Data type for data or columns. E.g. {‘a’: np.float64, ‘b’: np.int32} Use str or object together with suitable na\_values settings to preserve and not interpret dtype.

**nrows**int, default None

Number of rows to read from the CSV file.

**parse\_dates**boolean or list of ints or names or list of lists or dict, default False.

Currently only False is allowed.

**quotechar**str (length 1), optional

The character used to denote the start and end of a quoted item. Quoted items can include the delimiter and it will be ignored.

**escapechar**str (length 1), default None

One-character string used to escape other characters.

**comment: str, optional**

Indicates the line should not be parsed.

**encoding: str, optional**

Indicates the encoding to read file

**options**dict

All other options passed directly into Spark’s data source.

Returns

DataFrame or Series

See also

[`DataFrame.to_csv`](about:blank/pyspark.pandas.DataFrame.to_csv.html#pyspark.pandas.DataFrame.to_csv "pyspark.pandas.DataFrame.to_csv")

Write DataFrame to a comma-separated values (csv) file.

Examples

```
>>> ps.read_csv('data.csv')  

```


Load multiple CSV files as a single DataFrame:

```
>>> ps.read_csv(['data-01.csv', 'data-02.csv'])  

```


# pyspark.pandas.DataFrame.to_csv — PySpark 4.0.1 documentation
DataFrame.to\_csv(_path\=None_, _sep\=','_, _na\_rep\=''_, _columns\=None_, _header\=True_, _quotechar\='"'_, _date\_format\=None_, _escapechar\=None_, _num\_files\=None_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.to_csv "Permalink to this definition")

Write object to a comma-separated values (csv) file.

Note

pandas-on-Spark to\_csv writes files to a path or URI. Unlike pandas’, pandas-on-Spark respects HDFS’s property such as ‘fs.default.name’.

Note

pandas-on-Spark writes CSV files into the directory, path, and writes multiple part-… files in the directory when path is specified. This behavior was inherited from Apache Spark. The number of partitions can be controlled by num\_files. This is deprecated. Use DataFrame.spark.repartition instead.

Parameters

**path: str, default None**

File path. If None is provided the result is returned as a string.

**sep: str, default ‘,’**

String of length 1. Field delimiter for the output file.

**na\_rep: str, default ‘’**

Missing data representation.

**columns: sequence, optional**

Columns to write.

**header: bool or list of str, default True**

Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.

**quotechar: str, default ‘"’**

String of length 1. Character used to quote fields.

**date\_format: str, default None**

Format string for datetime objects.

**escapechar: str, default None**

String of length 1. Character used to escape sep and quotechar when appropriate.

**num\_files: the number of partitions to be written in \`path\` directory when**

this is a path. This is deprecated. Use DataFrame.spark.repartition instead.

**mode: str**

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols: str or list of str, optional, default None**

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options: keyword arguments for additional options specific to PySpark.**

These kwargs are specific to PySpark’s CSV options to pass. Check the options in PySpark’s API documentation for spark.write.csv(…). It has higher priority and overwrites all other options. This parameter only works when path is specified.

Returns

str or None

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df.sort_values(by="date")  
                   date country  code
... 2012-01-31 12:00:00      KR     1
... 2012-02-29 12:00:00      US     2
... 2012-03-31 12:00:00      JP     3

```


```
>>> print(df.to_csv())  
date,country,code
2012-01-31 12:00:00,KR,1
2012-02-29 12:00:00,US,2
2012-03-31 12:00:00,JP,3

```


```
>>> df.cummax().to_csv(path=r'%s/to_csv/foo.csv' % path, num_files=1)
>>> ps.read_csv(
...    path=r'%s/to_csv/foo.csv' % path
... ).sort_values(by="date")  
                   date country  code
... 2012-01-31 12:00:00      KR     1
... 2012-02-29 12:00:00      US     2
... 2012-03-31 12:00:00      US     3

```


In case of Series,

```
>>> print(df.date.to_csv())  
date
2012-01-31 12:00:00
2012-02-29 12:00:00
2012-03-31 12:00:00

```


```
>>> df.date.to_csv(path=r'%s/to_csv/foo.csv' % path, num_files=1)
>>> ps.read_csv(
...     path=r'%s/to_csv/foo.csv' % path
... ).sort_values(by="date")  
                   date
... 2012-01-31 12:00:00
... 2012-02-29 12:00:00
... 2012-03-31 12:00:00

```


You can preserve the index in the roundtrip as below.

```
>>> df.set_index("country", append=True, inplace=True)
>>> df.date.to_csv(
...     path=r'%s/to_csv/bar.csv' % path,
...     num_files=1,
...     index_col=["index1", "index2"])
>>> ps.read_csv(
...     path=r'%s/to_csv/bar.csv' % path, index_col=["index1", "index2"]
... ).sort_values(by="date")  
                             date
index1 index2
...    ...    2012-01-31 12:00:00
...    ...    2012-02-29 12:00:00
...    ...    2012-03-31 12:00:00

```


# pyspark.pandas.read_clipboard — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Input/Output](../io.html)
*   pyspark.pandas.read\_clipboard

pyspark.pandas.read\_clipboard(_sep\='\\\\s+'_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_clipboard)
[#](#pyspark.pandas.read_clipboard "Permalink to this definition")

Read text from clipboard and pass to read\_csv. See read\_csv for the full argument list

Parameters

**sep**str, default ‘s+’

A string or regex delimiter. The default of ‘s+’ denotes one or more whitespace characters.

Returns

**parsed**DataFrame

# pyspark.pandas.DataFrame.to_clipboard — PySpark 4.0.1 documentation
DataFrame.to\_clipboard(_excel\=True_, _sep\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_clipboard)
[#](#pyspark.pandas.DataFrame.to_clipboard "Permalink to this definition")

Copy object to the system clipboard.

Write a text representation of object to the system clipboard. This can be pasted into Excel, for example.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

Parameters

**excel**bool, default True

*   True, use the provided separator, writing in a csv format for allowing easy pasting into excel.
    
*   False, write a string representation of the object to the clipboard.
    

**sep**str, default `'\t'`

Field delimiter.

**\*\*kwargs**

These parameters will be passed to DataFrame.to\_csv.

Notes

Requirements for your platform.

> *   Linux : xclip, or xsel (with gtk or PyQt4 modules)
>     
> *   Windows : none
>     
> *   OS X : none
>     

Examples

Copy the contents of a DataFrame to the clipboard.

```
>>> df = ps.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])  
>>> df.to_clipboard(sep=',')  
... # Wrote the following to the system clipboard:
... # ,A,B,C
... # 0,1,2,3
... # 1,4,5,6

```


We can omit the index by passing the keyword index and setting it to false.

```
>>> df.to_clipboard(sep=',', index=False)  
... # Wrote the following to the system clipboard:
... # A,B,C
... # 1,2,3
... # 4,5,6

```


This function also works for Series:

```
>>> df = ps.Series([1, 2, 3, 4, 5, 6, 7], name='x')  
>>> df.to_clipboard(sep=',')  
... # Wrote the following to the system clipboard:
... # 0, 1
... # 1, 2
... # 2, 3
... # 3, 4
... # 4, 5
... # 5, 6
... # 6, 7

```




# pyspark.pandas.read_excel — PySpark 4.0.1 documentation
pyspark.pandas.read\_excel(_io_, _sheet\_name\=0_, _header\=0_, _names\=None_, _index\_col\=None_, _usecols\=None_, _dtype\=None_, _engine\=None_, _converters\=None_, _true\_values\=None_, _false\_values\=None_, _skiprows\=None_, _nrows\=None_, _na\_values\=None_, _keep\_default\_na\=True_, _verbose\=False_, _parse\_dates\=False_, _date\_parser\=None_, _thousands\=None_, _comment\=None_, _skipfooter\=0_, _\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_excel)
[#](#pyspark.pandas.read_excel "Permalink to this definition")

Read an Excel file into a pandas-on-Spark DataFrame or Series.

Support both xls and xlsx file extensions from a local filesystem or URL. Support an option to read a single sheet or a list of sheets.

Parameters

**io**str, file descriptor, pathlib.Path, ExcelFile or xlrd.Book

The string could be a URL. The value URL must be available in Spark’s DataFrameReader.

Note

If the underlying Spark is below 3.0, the parameter as a string is not supported. You can use ps.from\_pandas(pd.read\_excel(…)) as a workaround.

**sheet\_name**str, int, list, or None, default 0

Strings are used for sheet names. Integers are used in zero-indexed sheet positions. Lists of strings/integers are used to request multiple sheets. Specify None to get all sheets.

Available cases:

*   Defaults to `0`: 1st sheet as a DataFrame
    
*   `1`: 2nd sheet as a DataFrame
    
*   `"Sheet1"`: Load sheet with name “Sheet1”
    
*   `[0, 1, "Sheet5"]`: Load first, second and sheet named “Sheet5” as a dict of DataFrame
    
*   None: All sheets.
    

**header**int, list of int, default 0

Row (0-indexed) to use for the column labels of the parsed DataFrame. If a list of integers is passed those row positions will be combined into a `MultiIndex`. Use None if there is no header.

**names**array-like, default None

List of column names to use. If file contains no header row, then you should explicitly pass header=None.

**index\_col**int, list of int, default None

Column (0-indexed) to use as the row labels of the DataFrame. Pass None if there is no such column. If a list is passed, those columns will be combined into a `MultiIndex`. If a subset of data is selected with `usecols`, index\_col is based on the subset.

**usecols**int, str, list-like, or callable default None

Return a subset of the columns.

*   If None, then parse all columns.
    
*   If str, then indicates comma separated list of Excel column letters and column ranges (e.g. “A:E” or “A,C,E:F”). Ranges are inclusive of both sides.
    
*   If list of int, then indicates list of column numbers to be parsed.
    
*   If list of string, then indicates list of column names to be parsed.
    
*   If callable, then evaluate each column name against it and parse the column if the callable returns `True`.
    

**dtype**Type name or dict of column -> type, default None

Data type for data or columns. E.g. {‘a’: np.float64, ‘b’: np.int32} Use object to preserve data as stored in Excel and not interpret dtype. If converters are specified, they will be applied INSTEAD of dtype conversion.

**engine**str, default None

If io is not a buffer or path, this must be set to identify io. Acceptable values are None or xlrd.

**converters**dict, default None

Dict of functions for converting values in certain columns. Keys can either be integers or column labels, values are functions that take one input argument, the Excel cell content, and return the transformed content.

**true\_values**list, default None

Values to consider as True.

**false\_values**list, default None

Values to consider as False.

**skiprows**list-like

Rows to skip at the beginning (0-indexed).

**nrows**int, default None

Number of rows to parse.

**na\_values**scalar, str, list-like, or dict, default None

Additional strings to recognize as NA/NaN. If dict passed, specific per-column NA values. By default the following values are interpreted as NaN.

**keep\_default\_na**bool, default True

If na\_values are specified and keep\_default\_na is False the default NaN values are overridden, otherwise they’re appended to.

**verbose**bool, default False

Indicate number of NA values placed in non-numeric columns.

**parse\_dates**bool, list-like, or dict, default False

The behavior is as follows:

*   bool. If True -> try parsing the index.
    
*   list of int or names. e.g. If \[1, 2, 3\] -> try parsing columns 1, 2, 3 each as a separate date column.
    
*   list of lists. e.g. If \[\[1, 3\]\] -> combine columns 1 and 3 and parse as a single date column.
    
*   dict, e.g. {{‘foo’ : \[1, 3\]}} -> parse columns 1, 3 as date and call result ‘foo’
    

If a column or index contains an unparseable date, the entire column or index will be returned unaltered as an object data type. For non-standard datetime parsing, use `pd.to_datetime` after `pd.read_csv`

Note: A fast-path exists for iso8601-formatted dates.

**date\_parser**function, optional

Function to use for converting a sequence of string columns to an array of datetime instances. The default uses `dateutil.parser.parser` to do the conversion. pandas-on-Spark will try to call date\_parser in three different ways, advancing to the next if an exception occurs: 1) Pass one or more arrays (as defined by parse\_dates) as arguments; 2) concatenate (row-wise) the string values from the columns defined by parse\_dates into a single array and pass that; and 3) call date\_parser once for each row using one or more strings (corresponding to the columns defined by parse\_dates) as arguments.

**thousands**str, default None

Thousands separator for parsing string columns to numeric. Note that this parameter is only necessary for columns stored as TEXT in Excel, any numeric columns will automatically be parsed, regardless of display format.

**comment**str, default None

Comments out remainder of line. Pass a character or characters to this argument to indicate comments in the input file. Any data between the comment string and the end of the current line is ignored.

**skipfooter**int, default 0

Rows at the end to skip (0-indexed).

**\*\*kwds**optional

Optional keyword arguments can be passed to `TextFileReader`.

Returns

DataFrame or dict of DataFrames

DataFrame from the passed in Excel file. See notes in sheet\_name argument for more information on when a dict of DataFrames is returned.

Examples

The file can be read using the file name as string or an open file object:

```
>>> ps.read_excel('tmp.xlsx', index_col=0)  
       Name  Value
0   string1      1
1   string2      2
2  #Comment      3

```


```
>>> ps.read_excel(open('tmp.xlsx', 'rb'),
...               sheet_name='Sheet3')  
   Unnamed: 0      Name  Value
0           0   string1      1
1           1   string2      2
2           2  #Comment      3

```


Index and header can be specified via the index\_col and header arguments

```
>>> ps.read_excel('tmp.xlsx', index_col=None, header=None)  
     0         1      2
0  NaN      Name  Value
1  0.0   string1      1
2  1.0   string2      2
3  2.0  #Comment      3

```


Column types are inferred but can be explicitly specified

```
>>> ps.read_excel('tmp.xlsx', index_col=0,
...               dtype={'Name': str, 'Value': float})  
       Name  Value
0   string1    1.0
1   string2    2.0
2  #Comment    3.0

```


True, False, and NA values, and thousands separators have defaults, but can be explicitly specified, too. Supply the values you would like as strings or lists of strings!

```
>>> ps.read_excel('tmp.xlsx', index_col=0,
...               na_values=['string1', 'string2'])  
       Name  Value
0      None      1
1      None      2
2  #Comment      3

```


Comment lines in the excel input file can be skipped using the comment kwarg

```
>>> ps.read_excel('tmp.xlsx', index_col=0, comment='#')  
      Name  Value
0  string1    1.0
1  string2    2.0
2     None    NaN

```



# pyspark.pandas.DataFrame.to_excel — PySpark 4.0.1 documentation
DataFrame.to\_excel(_excel\_writer_, _sheet\_name\='Sheet1'_, _na\_rep\=''_, _float\_format\=None_, _columns\=None_, _header\=True_, _index\=True_, _index\_label\=None_, _startrow\=0_, _startcol\=0_, _engine\=None_, _merge\_cells\=True_, _inf\_rep\='inf'_, _freeze\_panes\=None_)
[#](#pyspark.pandas.DataFrame.to_excel "Permalink to this definition")

Write object to an Excel sheet.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

To write a single object to an Excel .xlsx file it is only necessary to specify a target file name. To write to multiple sheets it is necessary to create an ExcelWriter object with a target file name, and specify a sheet in the file to write to.

Multiple sheets may be written to by specifying unique sheet\_name. With all data written to the file it is necessary to save the changes. Note that creating an ExcelWriter object with a file name that already exists will result in the contents of the existing file being erased.

Parameters

**excel\_writer: str or ExcelWriter object**

File path or existing ExcelWriter.

**sheet\_name: str, default ‘Sheet1’**

Name of sheet which will contain DataFrame.

**na\_rep: str, default ‘’**

Missing data representation.

**float\_format: str, optional**

Format string for floating point numbers. For example `float_format="%%.2f"` will format 0.1234 to 0.12.

**columns: sequence or list of str, optional**

Columns to write.

**header: bool or list of str, default True**

Write out the column names. If a list of string is given it is assumed to be aliases for the column names.

**index: bool, default True**

Write row names (index).

**index\_label: str or sequence, optional**

Column label for index column(s) if desired. If not specified, and header and index are True, then the index names are used. A sequence should be given if the DataFrame uses MultiIndex.

**startrow: int, default 0**

Upper left cell row to dump data frame.

**startcol: int, default 0**

Upper left cell column to dump data frame.

**engine: str, optional**

Write engine to use, ‘openpyxl’ or ‘xlsxwriter’. You can also set this via the options `io.excel.xlsx.writer`, `io.excel.xls.writer`, and `io.excel.xlsm.writer`.

**merge\_cells: bool, default True**

Write MultiIndex and Hierarchical Rows as merged cells.

**inf\_rep: str, default ‘inf’**

Representation for infinity (there is no native representation for infinity in Excel).

**freeze\_panes: tuple of int (length 2), optional**

Specifies the one-based bottommost row and rightmost column that is to be frozen.

Notes

Once a workbook has been saved it is not possible write further data without rewriting the whole workbook.

Examples

Create, write to, and save a workbook:

```
>>> df1 = ps.DataFrame([['a', 'b'], ['c', 'd']],
...                    index=['row 1', 'row 2'],
...                    columns=['col 1', 'col 2'])
>>> df1.to_excel("output.xlsx")  

```


To specify the sheet name:

```
>>> df1.to_excel("output.xlsx")  
>>> df1.to_excel("output.xlsx",
...              sheet_name='Sheet_name_1')  

```


If you wish to write to more than one sheet in the workbook, it is necessary to specify an ExcelWriter object:

```
>>> with pd.ExcelWriter('output.xlsx') as writer:  
...      df1.to_excel(writer, sheet_name='Sheet_name_1')
...      df2.to_excel(writer, sheet_name='Sheet_name_2')

```


To set the library that is used to write the Excel file, you can pass the engine keyword (the default engine is automatically chosen depending on the file extension):

```
>>> df1.to_excel('output1.xlsx', engine='xlsxwriter')  

```


# pyspark.pandas.json_normalize — PySpark 4.0.1 documentation
pyspark.pandas.json\_normalize(_data_, _sep\='.'_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#json_normalize)
[#](#pyspark.pandas.json_normalize "Permalink to this definition")

Normalize semi-structured JSON data into a flat table.

New in version 4.0.0.

Parameters

**data**dict or list of dicts

Unserialized JSON objects.

**sep**str, default ‘.’

Nested records will generate names separated by sep.

Returns

DataFrame

Examples

```
>>> data = [
...     {"id": 1, "name": "Alice", "address": {"city": "NYC", "zipcode": "10001"}},
...     {"id": 2, "name": "Bob", "address": {"city": "SF", "zipcode": "94105"}},
... ]
>>> ps.json_normalize(data)
   id   name address.city address.zipcode
0   1  Alice          NYC           10001
1   2    Bob           SF           94105

```


# pyspark.pandas.read_json — PySpark 4.0.1 documentation
pyspark.pandas.read\_json(_path_, _lines\=True_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_json)
[#](#pyspark.pandas.read_json "Permalink to this definition")

Convert a JSON string to DataFrame.

Parameters

**path**string

File path

**lines**bool, default True

Read the file as a JSON object per line. It should be always True for now.

**index\_col**str or list of str, optional, default: None

Index column of table in Spark.

**options**dict

All other options passed directly into Spark’s data source.

Examples

```
>>> df = ps.DataFrame([['a', 'b'], ['c', 'd']],
...                   columns=['col 1', 'col 2'])

```


```
>>> df.to_json(path=r'%s/read_json/foo.json' % path, num_files=1)
>>> ps.read_json(
...     path=r'%s/read_json/foo.json' % path
... ).sort_values(by="col 1")
  col 1 col 2
0     a     b
1     c     d

```


```
>>> df.to_json(path=r'%s/read_json/foo.json' % path, num_files=1, lineSep='___')
>>> ps.read_json(
...     path=r'%s/read_json/foo.json' % path, lineSep='___'
... ).sort_values(by="col 1")
  col 1 col 2
0     a     b
1     c     d

```


You can preserve the index in the roundtrip as below.

```
>>> df.to_json(path=r'%s/read_json/bar.json' % path, num_files=1, index_col="index")
>>> ps.read_json(
...     path=r'%s/read_json/bar.json' % path, index_col="index"
... ).sort_values(by="col 1")  
      col 1 col 2
index
0         a     b
1         c     d

```


# pyspark.pandas.DataFrame.to_json — PySpark 4.0.1 documentation
DataFrame.to\_json(_path\=None_, _compression\='uncompressed'_, _num\_files\=None_, _mode\='w'_, _orient\='records'_, _lines\=True_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.to_json "Permalink to this definition")

Convert the object to a JSON string.

Note

pandas-on-Spark to\_json writes files to a path or URI. Unlike pandas’, pandas-on-Spark respects HDFS’s property such as ‘fs.default.name’.

Note

pandas-on-Spark writes JSON files into the directory, path, and writes multiple part-… files in the directory when path is specified. This behavior was inherited from Apache Spark. The number of partitions can be controlled by num\_files. This is deprecated. Use DataFrame.spark.repartition instead.

Note

output JSON format is different from pandas’. It always uses orient=’records’ for its output. This behavior might have to change soon.

Note

Set ignoreNullFields keyword argument to True to omit None or NaN values when writing JSON objects. It works only when path is provided.

Note NaN’s and None will be converted to null and datetime objects will be converted to UNIX timestamps.

Parameters

**path: string, optional**

File path. If not specified, the result is returned as a string.

**lines: bool, default True**

If ‘orient’ is ‘records’ write out line delimited JSON format. Will throw ValueError if incorrect ‘orient’ since others are not list like. It should be always True for now.

**orient: str, default ‘records’**

It should be always ‘records’ for now.

**compression: {‘gzip’, ‘bz2’, ‘xz’, None}**

A string representing the compression to use in the output file, only used when the first argument is a filename. By default, the compression is inferred from the filename.

**num\_files: the number of partitions to be written in \`path\` directory when**

this is a path. This is deprecated. Use DataFrame.spark.repartition instead.

**mode: str**

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols: str or list of str, optional, default None**

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options: keyword arguments for additional options specific to PySpark.**

It is specific to PySpark’s JSON options to pass. Check the options in PySpark’s API documentation for spark.write.json(…). It has a higher priority and overwrites all other options. This parameter only works when path is specified.

Returns

str or None

Examples

```
>>> df = ps.DataFrame([['a', 'b'], ['c', 'd']],
...                   columns=['col 1', 'col 2'])
>>> df.to_json()
'[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'

```


```
>>> df['col 1'].to_json()
'[{"col 1":"a"},{"col 1":"c"}]'

```


```
>>> df.to_json(path=r'%s/to_json/foo.json' % path, num_files=1)
>>> ps.read_json(
...     path=r'%s/to_json/foo.json' % path
... ).sort_values(by="col 1")
  col 1 col 2
0     a     b
1     c     d

```


```
>>> df['col 1'].to_json(path=r'%s/to_json/foo.json' % path, num_files=1, index_col="index")
>>> ps.read_json(
...     path=r'%s/to_json/foo.json' % path, index_col="index"
... ).sort_values(by="col 1")  
      col 1
index
0         a
1         c

```

# pyspark.pandas.read_html — PySpark 4.0.1 documentation
pyspark.pandas.read\_html(_io_, _match\='.+'_, _flavor\=None_, _header\=None_, _index\_col\=None_, _skiprows\=None_, _attrs\=None_, _parse\_dates\=False_, _thousands\=','_, _encoding\=None_, _decimal\='.'_, _converters\=None_, _na\_values\=None_, _keep\_default\_na\=True_, _displayed\_only\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_html)
[#](#pyspark.pandas.read_html "Permalink to this definition")

Read HTML tables into a `list` of `DataFrame` objects.

Parameters

**io**str or file-like

A URL, a file-like object, or a raw string containing HTML. Note that lxml only accepts the http, FTP and file URL protocols. If you have a URL that starts with `'https'` you might try removing the `'s'`.

Deprecated since version 4.0.0: Passing html literal strings is deprecated. Wrap literal string/bytes input in io.StringIO/io.BytesIO instead.

**match**str or compiled regular expression, optional

The set of tables containing text matching this regex or string will be returned. Unless the HTML is extremely simple you will probably need to pass a non-empty string here. Defaults to ‘.+’ (match any non-empty string). The default value will return all tables contained on a page. This value is converted to a regular expression so that there is consistent behavior between Beautiful Soup and lxml.

**flavor**str or None, container of strings

The parsing engine to use. ‘bs4’ and ‘html5lib’ are synonymous with each other, they are both there for backwards compatibility. The default of `None` tries to use `lxml` to parse and if that fails it falls back on `bs4` + `html5lib`.

**header**int or list-like or None, optional

The row (or list of rows for a `MultiIndex`) to use to make the columns headers.

**index\_col**int or list-like or None, optional

The column (or list of columns) to use to create the index.

**skiprows**int or list-like or slice or None, optional

0-based. Number of rows to skip after parsing the column integer. If a sequence of integers or a slice is given, will skip the rows indexed by that sequence. Note that a single element sequence means ‘skip the nth row’ whereas an integer means ‘skip n rows’.

**attrs**dict or None, optional

This is a dictionary of attributes that you can pass to use to identify the table in the HTML. These are not checked for validity before being passed to lxml or Beautiful Soup. However, these attributes must be valid HTML table attributes to work correctly. For example,

is a valid attribute dictionary because the ‘id’ HTML tag attribute is a valid HTML attribute for _any_ HTML tag as per [this document](http://www.w3.org/TR/html-markup/global-attributes.html).

```
attrs = {'asdf': 'table'}

```


is _not_ a valid attribute dictionary because ‘asdf’ is not a valid HTML attribute even if it is a valid XML attribute. Valid HTML 4.01 table attributes can be found [here](http://www.w3.org/TR/REC-html40/struct/tables.html#h-11.2). A working draft of the HTML 5 spec can be found [here](http://www.w3.org/TR/html-markup/table.html). It contains the latest information on table attributes for the modern web.

**parse\_dates**bool, optional

See `read_csv()` for more details.

**thousands**str, optional

Separator to use to parse thousands. Defaults to `','`.

**encoding**str or None, optional

The encoding used to decode the web page. Defaults to `None`.\`\`None\`\` preserves the previous encoding behavior, which depends on the underlying parser library (e.g., the parser library will try to use the encoding provided by the document).

**decimal**str, default ‘.’

Character to recognize as decimal point (example: use ‘,’ for European data).

**converters**dict, default None

Dict of functions for converting values in certain columns. Keys can either be integers or column labels, values are functions that take one input argument, the cell (not column) content, and return the transformed content.

**na\_values**iterable, default None

Custom NA values

**keep\_default\_na**bool, default True

If na\_values are specified and keep\_default\_na is False the default NaN values are overridden, otherwise they’re appended to

**displayed\_only**bool, default True

Whether elements with “display: none” should be parsed

Returns

**dfs**list of DataFrames



# pyspark.pandas.DataFrame.to_html — PySpark 4.0.1 documentation
DataFrame.to\_html(_buf\=None_, _columns\=None_, _col\_space\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _justify\=None_, _max\_rows\=None_, _max\_cols\=None_, _show\_dimensions\=False_, _decimal\='.'_, _bold\_rows\=True_, _classes\=None_, _escape\=True_, _notebook\=False_, _border\=None_, _table\_id\=None_, _render\_links\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_html)
[#](#pyspark.pandas.DataFrame.to_html "Permalink to this definition")

Render a DataFrame as an HTML table.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory. If the input is large, set max\_rows parameter.

Parameters

**buf**StringIO-like, optional

Buffer to write to.

**columns**sequence, optional, default None

The subset of columns to write. Writes all columns by default.

**col\_space**int, optional

The minimum width of each column.

**header**bool, optional

Write out the column names. If a list of strings is given, it is assumed to be aliases for the column names

**index**bool, optional, default True

Whether to print index (row) labels.

**na\_rep**str, optional, default ‘NaN’

String representation of NAN to use.

**formatters**list or dict of one-param. functions, optional

Formatter functions to apply to columns’ elements by position or name. The result of each function must be a Unicode string. List must be of length equal to the number of columns.

**float\_format**one-parameter function, optional, default None

Formatter function to apply to columns’ elements if they are floats. The result of this function must be a Unicode string.

**sparsify**bool, optional, default True

Set to False for a DataFrame with a hierarchical index to print every multiindex key at each row.

**index\_names**bool, optional, default True

Prints the names of the indexes.

**justify**str, default None

How to justify the column labels. If None uses the option from the print configuration (controlled by set\_option), ‘right’ out of the box. Valid values are

*   left
    
*   right
    
*   center
    
*   justify
    
*   justify-all
    
*   start
    
*   end
    
*   inherit
    
*   match-parent
    
*   initial
    
*   unset.
    

**max\_rows**int, optional

Maximum number of rows to display in the console.

**max\_cols**int, optional

Maximum number of columns to display in the console.

**show\_dimensions**bool, default False

Display DataFrame dimensions (number of rows by number of columns).

**decimal**str, default ‘.’

Character recognized as decimal separator, e.g. ‘,’ in Europe.

**bold\_rows**bool, default True

Make the row labels bold in the output.

**classes**str or list or tuple, default None

CSS class(es) to apply to the resulting html table.

**escape**bool, default True

Convert the characters <, >, and & to HTML-safe sequences.

**notebook**{True, False}, default False

Whether the generated HTML is for IPython Notebook.

**border**int

A `border=border` attribute is included in the opening <table> tag. By default `pd.options.html.border`.

**table\_id**str, optional

A css id is included in the opening <table> tag if specified.

**render\_links**bool, default False

Convert URLs to HTML links (only works with pandas 0.24+).

Returns

str (or Unicode, depending on data and options)

String representation of the dataframe.

See also

[`to_string`](about:blank/pyspark.pandas.DataFrame.to_string.html#pyspark.pandas.DataFrame.to_string "pyspark.pandas.DataFrame.to_string")

Convert DataFrame to a string.

# pyspark.pandas.read_sql_table — PySpark 4.0.1 documentation
pyspark.pandas.read\_sql\_table(_table\_name_, _con_, _schema\=None_, _index\_col\=None_, _columns\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_sql_table)
[#](#pyspark.pandas.read_sql_table "Permalink to this definition")

Read SQL database table into a DataFrame.

Given a table name and a JDBC URI, returns a DataFrame.

Parameters

**table\_name**str

Name of SQL table in database.

**con**str

A JDBC URI could be provided as str.

Note

The URI must be JDBC URI instead of Python’s database URI.

**schema**str, default None

Name of SQL schema in database to query (if database flavor supports this). Uses default schema if None (default).

**index\_col**str or list of str, optional, default: None

Column(s) to set as index(MultiIndex).

**columns**list, default None

List of column names to select from SQL table.

**options**dict

All other options passed directly into Spark’s JDBC data source.

Returns

DataFrame

A SQL table is returned as two-dimensional data structure with labeled axes.

See also

[`read_sql_query`](about:blank/pyspark.pandas.read_sql_query.html#pyspark.pandas.read_sql_query "pyspark.pandas.read_sql_query")

Read SQL query into a DataFrame.

[`read_sql`](about:blank/pyspark.pandas.read_sql.html#pyspark.pandas.read_sql "pyspark.pandas.read_sql")

Read SQL query or database table into a DataFrame.

Examples

```
>>> ps.read_sql_table('table_name', 'jdbc:postgresql:db_name')  

```


# pyspark.pandas.read_sql_query — PySpark 4.0.1 documentation
pyspark.pandas.read\_sql\_query(_sql_, _con_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_sql_query)
[#](#pyspark.pandas.read_sql_query "Permalink to this definition")

Read SQL query into a DataFrame.

Returns a DataFrame corresponding to the result set of the query string. Optionally provide an index\_col parameter to use one of the columns as the index, otherwise default index will be used.

Note

Some database might hit the issue of Spark: SPARK-27596

Parameters

**sql**string SQL query

SQL query to be executed.

**con**str

A JDBC URI could be provided as str.

Note

The URI must be JDBC URI instead of Python’s database URI.

**index\_col**string or list of strings, optional, default: None

Column(s) to set as index(MultiIndex).

**options**dict

All other options passed directly into Spark’s JDBC data source.

Returns

DataFrame

Examples

```
>>> ps.read_sql_query('SELECT * FROM table_name', 'jdbc:postgresql:db_name')  

```


# pyspark.pandas.read_sql — PySpark 4.0.1 documentation
pyspark.pandas.read\_sql(_sql_, _con_, _index\_col\=None_, _columns\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#read_sql)
[#](#pyspark.pandas.read_sql "Permalink to this definition")

Read SQL query or database table into a DataFrame.

This function is a convenience wrapper around `read_sql_table` and `read_sql_query` (for backward compatibility). It will delegate to the specific function depending on the provided input. A SQL query will be routed to `read_sql_query`, while a database table name will be routed to `read_sql_table`. Note that the delegated function might have more specific notes about their functionality not listed here.

Note

Some database might hit the issue of Spark: SPARK-27596

Parameters

**sql**string

SQL query to be executed or a table name.

**con**str

A JDBC URI could be provided as str.

Note

The URI must be JDBC URI instead of Python’s database URI.

**index\_col**string or list of strings, optional, default: None

Column(s) to set as index(MultiIndex).

**columns**list, default: None

List of column names to select from SQL table (only used when reading a table).

**options**dict

All other options passed directly into Spark’s JDBC data source.

Returns

DataFrame

Examples

```
>>> ps.read_sql('table_name', 'jdbc:postgresql:db_name')  
>>> ps.read_sql('SELECT * FROM table_name', 'jdbc:postgresql:db_name')  

```


