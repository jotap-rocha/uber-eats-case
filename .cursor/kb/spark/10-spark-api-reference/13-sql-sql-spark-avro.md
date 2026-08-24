# Avro — PySpark 4.0.1 documentation
*   [](../../index.html)
*   [API Reference](../index.html)
*   [Spark SQL](index.html)
*   Avro



* from_avro(data, jsonFormatSchema[, options]): to_avro(data[, jsonFormatSchema])
  * Converts a binary column of Avro format into its corresponding catalyst value.: Converts a column into binary of avro format.


# pyspark.sql.avro.functions.from_avro — PySpark 4.0.1 documentation
pyspark.sql.avro.functions.from\_avro(_data_, _jsonFormatSchema_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/avro/functions.html#from_avro)
[#](#pyspark.sql.avro.functions.from_avro "Permalink to this definition")

Converts a binary column of Avro format into its corresponding catalyst value. The specified schema must match the read data, otherwise the behavior is undefined: it may fail or return arbitrary result. To deserialize the data with a compatible and evolved schema, the expected Avro schema can be set via the option avroSchema.

New in version 3.0.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters

**data**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

the binary column.

**jsonFormatSchema**str

the avro schema in JSON string format.

**options**dict, optional

options to control how the Avro record is parsed.

Notes

Avro is built-in but external data source module since Spark 2.4. Please deploy the application as per the deployment section of “Apache Avro Data Source Guide”.

Examples

```
>>> from pyspark.sql import Row
>>> from pyspark.sql.avro.functions import from_avro, to_avro
>>> data = [(1, Row(age=2, name='Alice'))]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> avroDf = df.select(to_avro(df.value).alias("avro"))
>>> avroDf.collect()
[Row(avro=bytearray(b'\x00\x00\x04\x00\nAlice'))]

```


```
>>> jsonFormatSchema = '''{"type":"record","name":"topLevelRecord","fields":
...     [{"name":"avro","type":[{"type":"record","name":"value","namespace":"topLevelRecord",
...     "fields":[{"name":"age","type":["long","null"]},
...     {"name":"name","type":["string","null"]}]},"null"]}]}'''
>>> avroDf.select(from_avro(avroDf.avro, jsonFormatSchema).alias("value")).collect()
[Row(value=Row(avro=Row(age=2, name='Alice')))]

```


# pyspark.sql.avro.functions.to_avro — PySpark 4.0.1 documentation
pyspark.sql.avro.functions.to\_avro(_data_, _jsonFormatSchema\=''_)
[\[source\]](about:blank/_modules/pyspark/sql/avro/functions.html#to_avro)
[#](#pyspark.sql.avro.functions.to_avro "Permalink to this definition")

Converts a column into binary of avro format.

New in version 3.0.0.

Changed in version 3.5.0: Supports Spark Connect.

Parameters

**data**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

the data column.

**jsonFormatSchema**str, optional

user-specified output avro schema in JSON string format.

Notes

Avro is built-in but external data source module since Spark 2.4. Please deploy the application as per the deployment section of “Apache Avro Data Source Guide”.

Examples

```
>>> from pyspark.sql import Row
>>> from pyspark.sql.avro.functions import to_avro
>>> data = ['SPADES']
>>> df = spark.createDataFrame(data, "string")
>>> df.select(to_avro(df.value).alias("suite")).collect()
[Row(suite=bytearray(b'\x00\x0cSPADES'))]

```


```
>>> jsonFormatSchema = '''["null", {"type": "enum", "name": "value",
...     "symbols": ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]}]'''
>>> df.select(to_avro(df.value, jsonFormatSchema).alias("suite")).collect()
[Row(suite=bytearray(b'\x02\x00'))]

```


