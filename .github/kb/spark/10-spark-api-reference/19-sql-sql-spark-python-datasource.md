# Python Data Source — PySpark 4.0.1 documentation


* DataSource.name(): DataSource.reader(schema)
  * Returns a string represents the format name of this data source.: Returns a DataSourceReader instance for reading data.
* DataSource.name(): DataSource.schema()
  * Returns a string represents the format name of this data source.: Returns the schema of the data source.
* DataSource.name(): DataSource.streamReader(schema)
  * Returns a string represents the format name of this data source.: Returns a DataSourceStreamReader instance for reading streaming data.
* DataSource.name(): DataSource.writer(schema, overwrite)
  * Returns a string represents the format name of this data source.: Returns a DataSourceWriter instance for writing data.
* DataSource.name(): DataSourceReader.partitions()
  * Returns a string represents the format name of this data source.: Returns an iterator of partitions for this data source.
* DataSource.name(): DataSourceReader.read(partition)
  * Returns a string represents the format name of this data source.: Generates data for a given partition and returns an iterator of tuples or rows.
* DataSource.name(): DataSourceRegistration.register(dataSource)
  * Returns a string represents the format name of this data source.: Register a Python user-defined data source.
* DataSource.name(): DataSourceStreamReader.commit(end)
  * Returns a string represents the format name of this data source.: Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.
* DataSource.name(): DataSourceStreamReader.initialOffset()
  * Returns a string represents the format name of this data source.: Return the initial offset of the streaming data source.
* DataSource.name(): DataSourceStreamReader.latestOffset()
  * Returns a string represents the format name of this data source.: Returns the most recent offset available.
* DataSource.name(): DataSourceStreamReader.partitions(start, end)
  * Returns a string represents the format name of this data source.: Returns a list of InputPartition given the start and end offsets.
* DataSource.name(): DataSourceStreamReader.read(partition)
  * Returns a string represents the format name of this data source.: Generates data for a given partition and returns an iterator of tuples or rows.
* DataSource.name(): DataSourceStreamReader.stop()
  * Returns a string represents the format name of this data source.: Stop this source and free any resources it has allocated.
* DataSource.name(): DataSourceWriter.abort(messages)
  * Returns a string represents the format name of this data source.: Aborts this writing job due to task failures.
* DataSource.name(): DataSourceWriter.commit(messages)
  * Returns a string represents the format name of this data source.: Commits this writing job with a list of commit messages.
* DataSource.name(): DataSourceWriter.write(iterator)
  * Returns a string represents the format name of this data source.: Writes data into the data source.


# pyspark.sql.datasource.DataSource.name — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSource.name

_classmethod_ DataSource.name()
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSource.name)
[#](#pyspark.sql.datasource.DataSource.name "Permalink to this definition")

Returns a string represents the format name of this data source.

By default, it is the class name of the data source. It can be overridden to provide a customized short name for the data source.

Examples

```
>>> def name(cls):
...     return "my_data_source"

```


# pyspark.sql.datasource.DataSource.reader — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSource.reader

DataSource.reader(_schema_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSource.reader)
[#](#pyspark.sql.datasource.DataSource.reader "Permalink to this definition")

Returns a [`DataSourceReader`](about:blank/pyspark.sql.datasource.DataSourceReader.html#pyspark.sql.datasource.DataSourceReader "pyspark.sql.datasource.DataSourceReader") instance for reading data.

The implementation is required for readable data sources.

Parameters

**schema**`StructType`

The schema of the data to be read.

Returns

**reader**[`DataSourceReader`](about:blank/pyspark.sql.datasource.DataSourceReader.html#pyspark.sql.datasource.DataSourceReader "pyspark.sql.datasource.DataSourceReader")

A reader instance for this data source.

# pyspark.sql.datasource.DataSource.schema — PySpark 4.0.1 documentation
DataSource.schema()
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSource.schema)
[#](#pyspark.sql.datasource.DataSource.schema "Permalink to this definition")

Returns the schema of the data source.

It can refer any field initialized in the `DataSource.__init__()` method to infer the data source’s schema when users do not explicitly specify it. This method is invoked once when calling `spark.read.format(...).load()` to get the schema for a data source read operation. If this method is not implemented, and a user does not provide a schema when reading the data source, an exception will be thrown.

Returns

**schema**`StructType` or str

The schema of this data source or a DDL string represents the schema

Examples

Returns a DDL string:

```
>>> def schema(self):
...    return "a INT, b STRING"

```


Returns a `StructType`:

```
>>> def schema(self):
...   return StructType().add("a", "int").add("b", "string")

```


# pyspark.sql.datasource.DataSource.streamReader — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSource.streamReader

DataSource.streamReader(_schema_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSource.streamReader)
[#](#pyspark.sql.datasource.DataSource.streamReader "Permalink to this definition")

Returns a [`DataSourceStreamReader`](about:blank/pyspark.sql.datasource.DataSourceStreamReader.html#pyspark.sql.datasource.DataSourceStreamReader "pyspark.sql.datasource.DataSourceStreamReader") instance for reading streaming data.

One of simpleStreamReader() and streamReader() must be implemented for readable streaming data source.

Parameters

**schema**`StructType`

The schema of the data to be read.

Returns

**reader**[`DataSourceStreamReader`](about:blank/pyspark.sql.datasource.DataSourceStreamReader.html#pyspark.sql.datasource.DataSourceStreamReader "pyspark.sql.datasource.DataSourceStreamReader")

A reader instance for this streaming data source.

# pyspark.sql.datasource.DataSource.writer — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSource.writer

DataSource.writer(_schema_, _overwrite_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSource.writer)
[#](#pyspark.sql.datasource.DataSource.writer "Permalink to this definition")

Returns a [`DataSourceWriter`](about:blank/pyspark.sql.datasource.DataSourceWriter.html#pyspark.sql.datasource.DataSourceWriter "pyspark.sql.datasource.DataSourceWriter") instance for writing data.

The implementation is required for writable data sources.

Parameters

**schema**`StructType`

The schema of the data to be written.

**overwrite**bool

A flag indicating whether to overwrite existing data when writing to the data source.

Returns

**writer**[`DataSourceWriter`](about:blank/pyspark.sql.datasource.DataSourceWriter.html#pyspark.sql.datasource.DataSourceWriter "pyspark.sql.datasource.DataSourceWriter")

A writer instance for this data source.

# pyspark.sql.datasource.DataSourceReader.partitions — PySpark 4.0.1 documentation
DataSourceReader.partitions()
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceReader.partitions)
[#](#pyspark.sql.datasource.DataSourceReader.partitions "Permalink to this definition")

Returns an iterator of partitions for this data source.

Partitions are used to split data reading operations into parallel tasks. If this method returns N partitions, the query planner will create N tasks. Each task will execute [`DataSourceReader.read()`](about:blank/pyspark.sql.datasource.DataSourceReader.read.html#pyspark.sql.datasource.DataSourceReader.read "pyspark.sql.datasource.DataSourceReader.read") in parallel, using the respective partition value to read the data.

This method is called once during query planning. By default, it returns a single partition with the value `None`. Subclasses can override this method to return multiple partitions.

It’s recommended to override this method for better performance when reading large datasets.

Returns

sequence of [`InputPartition`](about:blank/pyspark.sql.datasource.InputPartition.html#pyspark.sql.datasource.InputPartition "pyspark.sql.datasource.InputPartition")s

A sequence of partitions for this data source. Each partition value must be an instance of InputPartition or a subclass of it.

Notes

All partition values must be picklable objects.

Examples

Returns a list of integers:

```
>>> def partitions(self):
...     return [InputPartition(1), InputPartition(2), InputPartition(3)]

```


Returns a list of string:

```
>>> def partitions(self):
...     return [InputPartition("a"), InputPartition("b"), InputPartition("c")]

```


Returns a list of ranges:

```
>>> class RangeInputPartition(InputPartition):
...    def __init__(self, start, end):
...        self.start = start
...        self.end = end

```


```
>>> def partitions(self):
...     return [RangeInputPartition(1, 3), RangeInputPartition(5, 10)]

```


# pyspark.sql.datasource.DataSourceReader.read — PySpark 4.0.1 documentation
_abstract_ DataSourceReader.read(_partition_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceReader.read)
[#](#pyspark.sql.datasource.DataSourceReader.read "Permalink to this definition")

Generates data for a given partition and returns an iterator of tuples or rows.

This method is invoked once per partition to read the data. Implementing this method is required for readable data sources. You can initialize any non-serializable resources required for reading data from the data source within this method.

Parameters

**partition**object

The partition to read. It must be one of the partition values returned by [`DataSourceReader.partitions()`](about:blank/pyspark.sql.datasource.DataSourceReader.partitions.html#pyspark.sql.datasource.DataSourceReader.partitions "pyspark.sql.datasource.DataSourceReader.partitions").

Returns

iterator of tuples or PyArrow’s RecordBatch

An iterator of tuples or rows. Each tuple or row will be converted to a row in the final DataFrame. It can also return an iterator of PyArrow’s RecordBatch if the data source supports it.

Examples

Yields a list of tuples:

```
>>> def read(self, partition: InputPartition):
...     yield (partition.value, 0)
...     yield (partition.value, 1)

```


Yields a list of rows:

```
>>> def read(self, partition: InputPartition):
...     yield Row(partition=partition.value, value=0)
...     yield Row(partition=partition.value, value=1)

```


# pyspark.sql.datasource.DataSourceRegistration.register — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSourceRegistration.register

DataSourceRegistration.register(_dataSource_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceRegistration.register)
[#](#pyspark.sql.datasource.DataSourceRegistration.register "Permalink to this definition")

Register a Python user-defined data source.

Parameters

**dataSource**type

The data source class to be registered. It should be a subclass of DataSource.

# pyspark.sql.datasource.DataSourceStreamReader.commit — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSourceStreamReader.commit

DataSourceStreamReader.commit(_end_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader.commit)
[#](#pyspark.sql.datasource.DataSourceStreamReader.commit "Permalink to this definition")

Informs the source that Spark has completed processing all data for offsets less than or equal to end and will only request offsets greater than end in the future.

Parameters

**end**dict

The latest offset that the streaming query has processed for this source.

# pyspark.sql.datasource.DataSourceStreamReader.initialOffset — PySpark 4.0.1 documentation
DataSourceStreamReader.initialOffset()
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader.initialOffset)
[#](#pyspark.sql.datasource.DataSourceStreamReader.initialOffset "Permalink to this definition")

Return the initial offset of the streaming data source. A new streaming query starts reading data from the initial offset. If Spark is restarting an existing query, it will restart from the check-pointed offset rather than the initial one.

Returns

dict

A dict or recursive dict whose key and value are primitive types, which includes Integer, String and Boolean.

Examples

```
>>> def initialOffset(self):
...     return {"parititon-1": {"index": 3, "closed": True}, "partition-2": {"index": 5}}

```


# pyspark.sql.datasource.DataSourceStreamReader.latestOffset — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSourceStreamReader.latestOffset

DataSourceStreamReader.latestOffset()
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader.latestOffset)
[#](#pyspark.sql.datasource.DataSourceStreamReader.latestOffset "Permalink to this definition")

Returns the most recent offset available.

Returns

dict

A dict or recursive dict whose key and value are primitive types, which includes Integer, String and Boolean.

Examples

```
>>> def latestOffset(self):
...     return {"parititon-1": {"index": 3, "closed": True}, "partition-2": {"index": 5}}

```


# pyspark.sql.datasource.DataSourceStreamReader.partitions — PySpark 4.0.1 documentation
DataSourceStreamReader.partitions(_start_, _end_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader.partitions)
[#](#pyspark.sql.datasource.DataSourceStreamReader.partitions "Permalink to this definition")

Returns a list of InputPartition given the start and end offsets. Each InputPartition represents a data split that can be processed by one Spark task. This may be called with an empty offset range when start == end, in that case the method should return an empty sequence of InputPartition.

Parameters

**start**dict

The start offset of the microbatch to plan partitioning.

**end**dict

The end offset of the microbatch to plan partitioning.

Returns

sequence of [`InputPartition`](about:blank/pyspark.sql.datasource.InputPartition.html#pyspark.sql.datasource.InputPartition "pyspark.sql.datasource.InputPartition")s

A sequence of partitions for this data source. Each partition value must be an instance of InputPartition or a subclass of it.

# pyspark.sql.datasource.DataSourceStreamReader.read — PySpark 4.0.1 documentation
_abstract_ DataSourceStreamReader.read(_partition_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader.read)
[#](#pyspark.sql.datasource.DataSourceStreamReader.read "Permalink to this definition")

Generates data for a given partition and returns an iterator of tuples or rows.

This method is invoked once per partition to read the data. Implementing this method is required for stream reader. You can initialize any non-serializable resources required for reading data from the data source within this method.

Parameters

**partition**[`InputPartition`](about:blank/pyspark.sql.datasource.InputPartition.html#pyspark.sql.datasource.InputPartition "pyspark.sql.datasource.InputPartition")

The partition to read. It must be one of the partition values returned by [`DataSourceStreamReader.partitions()`](about:blank/pyspark.sql.datasource.DataSourceStreamReader.partitions.html#pyspark.sql.datasource.DataSourceStreamReader.partitions "pyspark.sql.datasource.DataSourceStreamReader.partitions").

Returns

iterator of tuples or PyArrow’s RecordBatch

An iterator of tuples or rows. Each tuple or row will be converted to a row in the final DataFrame. It can also return an iterator of PyArrow’s RecordBatch if the data source supports it.

Notes

This method is static and stateless. You shouldn’t access mutable class member or keep in memory state between different invocations of read().

# pyspark.sql.datasource.DataSourceStreamReader.stop — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Python Data Source](../datasource.html)
*   pyspark.sql.datasource.DataSourceStreamReader.stop

DataSourceStreamReader.stop()
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceStreamReader.stop)
[#](#pyspark.sql.datasource.DataSourceStreamReader.stop "Permalink to this definition")

Stop this source and free any resources it has allocated. Invoked when the streaming query terminated.


# pyspark.sql.datasource.DataSourceWriter.abort — PySpark 4.0.1 documentation
DataSourceWriter.abort(_messages_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceWriter.abort)
[#](#pyspark.sql.datasource.DataSourceWriter.abort "Permalink to this definition")

Aborts this writing job due to task failures.

This method is invoked on the driver when one or more tasks failed. The commit messages are collected from the [`DataSourceWriter.write()`](about:blank/pyspark.sql.datasource.DataSourceWriter.write.html#pyspark.sql.datasource.DataSourceWriter.write "pyspark.sql.datasource.DataSourceWriter.write") method call from each task, and are passed to this method. The implementation should use the commit messages to abort the writing job to the data source.

Parameters

**messages**list of [`WriterCommitMessage`](about:blank/pyspark.sql.datasource.WriterCommitMessage.html#pyspark.sql.datasource.WriterCommitMessage "pyspark.sql.datasource.WriterCommitMessage")s

A list of commit messages. If a write task fails, the commit message will be None.


# pyspark.sql.datasource.DataSourceWriter.commit — PySpark 4.0.1 documentation
DataSourceWriter.commit(_messages_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceWriter.commit)
[#](#pyspark.sql.datasource.DataSourceWriter.commit "Permalink to this definition")

Commits this writing job with a list of commit messages.

This method is invoked on the driver when all tasks run successfully. The commit messages are collected from the [`DataSourceWriter.write()`](about:blank/pyspark.sql.datasource.DataSourceWriter.write.html#pyspark.sql.datasource.DataSourceWriter.write "pyspark.sql.datasource.DataSourceWriter.write") method call from each task, and are passed to this method. The implementation should use the commit messages to commit the writing job to the data source.

Parameters

**messages**list of [`WriterCommitMessage`](about:blank/pyspark.sql.datasource.WriterCommitMessage.html#pyspark.sql.datasource.WriterCommitMessage "pyspark.sql.datasource.WriterCommitMessage")s

A list of commit messages. If a write task fails, the commit message will be None.


# pyspark.sql.datasource.DataSourceWriter.write — PySpark 4.0.1 documentation
_abstract_ DataSourceWriter.write(_iterator_)
[\[source\]](about:blank/_modules/pyspark/sql/datasource.html#DataSourceWriter.write)
[#](#pyspark.sql.datasource.DataSourceWriter.write "Permalink to this definition")

Writes data into the data source.

This method is called once on each executor to write data to the data source. It accepts an iterator of input data and returns a single row representing a commit message, or None if there is no commit message.

The driver collects commit messages, if any, from all executors and passes them to the [`DataSourceWriter.commit`](about:blank/pyspark.sql.datasource.DataSourceWriter.commit.html#pyspark.sql.datasource.DataSourceWriter.commit "pyspark.sql.datasource.DataSourceWriter.commit") method if all tasks run successfully. If any task fails, the [`DataSourceWriter.abort`](about:blank/pyspark.sql.datasource.DataSourceWriter.abort.html#pyspark.sql.datasource.DataSourceWriter.abort "pyspark.sql.datasource.DataSourceWriter.abort") method will be called with the collected commit messages.

Parameters

**iterator**iterator of `Row`s

An iterator of input data.

Returns

[`WriterCommitMessage`](about:blank/pyspark.sql.datasource.WriterCommitMessage.html#pyspark.sql.datasource.WriterCommitMessage "pyspark.sql.datasource.WriterCommitMessage")

a serializable commit message

