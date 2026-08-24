# Data Types — PySpark 4.0.1 documentation


* ArrayType(elementType[, containsNull]): BinaryType()
  * Array data type.: Binary (byte array) data type.
* ArrayType(elementType[, containsNull]): BooleanType()
  * Array data type.: Boolean data type.
* ArrayType(elementType[, containsNull]): ByteType()
  * Array data type.: Byte data type, representing signed 8-bit integers.
* ArrayType(elementType[, containsNull]): DataType()
  * Array data type.: Base class for data types.
* ArrayType(elementType[, containsNull]): DateType()
  * Array data type.: Date (datetime.date) data type.
* ArrayType(elementType[, containsNull]): DecimalType([precision, scale])
  * Array data type.: Decimal (decimal.Decimal) data type.
* ArrayType(elementType[, containsNull]): DoubleType()
  * Array data type.: Double data type, representing double precision floats.
* ArrayType(elementType[, containsNull]): FloatType()
  * Array data type.: Float data type, representing single precision floats.
* ArrayType(elementType[, containsNull]): IntegerType()
  * Array data type.: Int data type, representing signed 32-bit integers.
* ArrayType(elementType[, containsNull]): LongType()
  * Array data type.: Long data type, representing signed 64-bit integers.
* ArrayType(elementType[, containsNull]): MapType(keyType, valueType[, valueContainsNull])
  * Array data type.: Map data type.
* ArrayType(elementType[, containsNull]): NullType()
  * Array data type.: Null type.
* ArrayType(elementType[, containsNull]): ShortType()
  * Array data type.: Short data type, representing signed 16-bit integers.
* ArrayType(elementType[, containsNull]): StringType([collation])
  * Array data type.: String data type.
* ArrayType(elementType[, containsNull]): CharType(length)
  * Array data type.: Char data type
* ArrayType(elementType[, containsNull]): VarcharType(length)
  * Array data type.: Varchar data type
* ArrayType(elementType[, containsNull]): StructField(name, dataType[, nullable, metadata])
  * Array data type.: A field in StructType.
* ArrayType(elementType[, containsNull]): StructType([fields])
  * Array data type.: Struct type, consisting of a list of StructField.
* ArrayType(elementType[, containsNull]): VariantType()
  * Array data type.: Variant data type, representing semi-structured values.
* ArrayType(elementType[, containsNull]): TimestampType()
  * Array data type.: Timestamp (datetime.datetime) data type.
* ArrayType(elementType[, containsNull]): TimestampNTZType()
  * Array data type.: Timestamp (datetime.datetime) data type without timezone information.
* ArrayType(elementType[, containsNull]): DayTimeIntervalType([startField, endField])
  * Array data type.: DayTimeIntervalType (datetime.timedelta).
* ArrayType(elementType[, containsNull]): YearMonthIntervalType([startField, endField])
  * Array data type.: YearMonthIntervalType, represents year-month intervals of the SQL standard
* ArrayType(elementType[, containsNull]): CalendarIntervalType()
  * Array data type.: The data type representing calendar intervals.


# ArrayType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.ArrayType(_elementType_, _containsNull\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType)
[#](#pyspark.sql.types.ArrayType "Permalink to this definition")

Array data type.

Parameters

**elementType**[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") of each element in the array.

**containsNull**bool, optional

whether the array can contain null (None) values.

Examples

```
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType

```


The below example demonstrates how to create class:ArrayType:

```
>>> arr = ArrayType(StringType())

```


The array can contain null (None) values by default:

```
>>> ArrayType(StringType()) == ArrayType(StringType(), True)
True
>>> ArrayType(StringType(), False) == ArrayType(StringType())
False

```


Methods



* fromDDL(ddl): fromInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts an internal SQL object into a native Python object.
* fromDDL(ddl): fromJson(json[, fieldPath, collationsMap])
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): json()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): jsonValue()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): needConversion()
  * Creates DataType for a given DDL-formatted string.: Does this type needs conversion between Python object and internal SQL object.
* fromDDL(ddl): simpleString()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): toInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts a Python object into an internal SQL object.
* fromDDL(ddl): toNullable()
  * Creates DataType for a given DDL-formatted string.: Returns the same data type but set all nullability fields are true (StructField.nullable, ArrayType.containsNull, and MapType.valueContainsNull).
* fromDDL(ddl): typeName()
  * Creates DataType for a given DDL-formatted string.: 


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.ArrayType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.fromInternal)
[#](#pyspark.sql.types.ArrayType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

_classmethod_ fromJson(_json_, _fieldPath\=''_, _collationsMap\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.fromJson)
[#](#pyspark.sql.types.ArrayType.fromJson "Permalink to this definition")

json()
[#](#pyspark.sql.types.ArrayType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.jsonValue)
[#](#pyspark.sql.types.ArrayType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.needConversion)
[#](#pyspark.sql.types.ArrayType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.simpleString)
[#](#pyspark.sql.types.ArrayType.simpleString "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.toInternal)
[#](#pyspark.sql.types.ArrayType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

toNullable()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ArrayType.toNullable)
[#](#pyspark.sql.types.ArrayType.toNullable "Permalink to this definition")

Returns the same data type but set all nullability fields are true (StructField.nullable, ArrayType.containsNull, and MapType.valueContainsNull).

New in version 4.0.0.

Returns

[`ArrayType`](#pyspark.sql.types.ArrayType "pyspark.sql.types.ArrayType")

Examples

Example 1: Simple nullability conversion

```
>>> ArrayType(IntegerType(), containsNull=False).toNullable()
ArrayType(IntegerType(), True)

```


Example 2: Nested nullability conversion

```
>>> ArrayType(
...     StructType([
...         StructField("b", IntegerType(), nullable=False),
...         StructField("c", ArrayType(IntegerType(), containsNull=False))
...     ]),
...     containsNull=False
... ).toNullable()
ArrayType(StructType([StructField('b', IntegerType(), True),
StructField('c', ArrayType(IntegerType(), True), True)]), True)

```


_classmethod_ typeName()
[#](#pyspark.sql.types.ArrayType.typeName "Permalink to this definition")

# BinaryType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.BinaryType[\[source\]](about:blank/_modules/pyspark/sql/types.html#BinaryType)
[#](#pyspark.sql.types.BinaryType "Permalink to this definition")

Binary (byte array) data type.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.BinaryType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.BinaryType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.BinaryType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.BinaryType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.BinaryType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.BinaryType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.BinaryType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.BinaryType.typeName "Permalink to this definition")

# BooleanType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.BooleanType[\[source\]](about:blank/_modules/pyspark/sql/types.html#BooleanType)
[#](#pyspark.sql.types.BooleanType "Permalink to this definition")

Boolean data type.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.BooleanType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.BooleanType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.BooleanType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.BooleanType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.BooleanType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.BooleanType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.BooleanType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.BooleanType.typeName "Permalink to this definition")

# ByteType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.ByteType[\[source\]](about:blank/_modules/pyspark/sql/types.html#ByteType)
[#](#pyspark.sql.types.ByteType "Permalink to this definition")

Byte data type, representing signed 8-bit integers.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.ByteType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.ByteType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.ByteType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.ByteType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.ByteType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ByteType.simpleString)
[#](#pyspark.sql.types.ByteType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.ByteType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.ByteType.typeName "Permalink to this definition")


# DataType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.DataType[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType)
[#](#pyspark.sql.types.DataType "Permalink to this definition")

Base class for data types.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.fromDDL)
[#](#pyspark.sql.types.DataType.fromDDL "Permalink to this definition")

Creates [`DataType`](#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.fromInternal)
[#](#pyspark.sql.types.DataType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.json)
[#](#pyspark.sql.types.DataType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.jsonValue)
[#](#pyspark.sql.types.DataType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.needConversion)
[#](#pyspark.sql.types.DataType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.simpleString)
[#](#pyspark.sql.types.DataType.simpleString "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.toInternal)
[#](#pyspark.sql.types.DataType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DataType.typeName)
[#](#pyspark.sql.types.DataType.typeName "Permalink to this definition")

# DateType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.DateType[\[source\]](about:blank/_modules/pyspark/sql/types.html#DateType)
[#](#pyspark.sql.types.DateType "Permalink to this definition")

Date (datetime.date) data type.

Methods


|fromDDL(ddl)    |Creates DataType for a given DDL-formatted string.                            |
|----------------|------------------------------------------------------------------------------|
|fromInternal(v) |Converts an internal SQL object into a native Python object.                  |
|json()          |                                                                              |
|jsonValue()     |                                                                              |
|needConversion()|Does this type needs conversion between Python object and internal SQL object.|
|simpleString()  |                                                                              |
|toInternal(d)   |Converts a Python object into an internal SQL object.                         |
|typeName()      |                                                                              |


Attributes



Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.DateType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_v_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DateType.fromInternal)
[#](#pyspark.sql.types.DateType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.DateType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.DateType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DateType.needConversion)
[#](#pyspark.sql.types.DateType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.DateType.simpleString "Permalink to this definition")

toInternal(_d_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DateType.toInternal)
[#](#pyspark.sql.types.DateType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.DateType.typeName "Permalink to this definition")

Attributes Documentation

EPOCH\_ORDINAL _\= 719163_[#](#pyspark.sql.types.DateType.EPOCH_ORDINAL "Permalink to this definition")

# DecimalType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.DecimalType(_precision\=10_, _scale\=0_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DecimalType)
[#](#pyspark.sql.types.DecimalType "Permalink to this definition")

Decimal (decimal.Decimal) data type.

The DecimalType must have fixed precision (the maximum total number of digits) and scale (the number of digits on the right of dot). For example, (5, 2) can support the value from \[-999.99 to 999.99\].

The precision can be up to 38, the scale must be less or equal to precision.

When creating a DecimalType, the default precision and scale is (10, 0). When inferring schema from decimal.Decimal objects, it will be DecimalType(38, 18).

Parameters

**precision**int, optional

the maximum (i.e. total) number of digits (default: 10)

**scale**int, optional

the number of digits on right side of dot. (default: 0)

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.DecimalType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.DecimalType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.DecimalType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DecimalType.jsonValue)
[#](#pyspark.sql.types.DecimalType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.DecimalType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DecimalType.simpleString)
[#](#pyspark.sql.types.DecimalType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.DecimalType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.DecimalType.typeName "Permalink to this definition")

# DoubleType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.DoubleType[\[source\]](about:blank/_modules/pyspark/sql/types.html#DoubleType)
[#](#pyspark.sql.types.DoubleType "Permalink to this definition")

Double data type, representing double precision floats.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.DoubleType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.DoubleType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.DoubleType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.DoubleType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.DoubleType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.DoubleType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.DoubleType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.DoubleType.typeName "Permalink to this definition")


# FloatType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.FloatType[\[source\]](about:blank/_modules/pyspark/sql/types.html#FloatType)
[#](#pyspark.sql.types.FloatType "Permalink to this definition")

Float data type, representing single precision floats.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.FloatType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.FloatType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.FloatType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.FloatType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.FloatType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.FloatType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.FloatType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.FloatType.typeName "Permalink to this definition")



# IntegerType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.IntegerType[\[source\]](about:blank/_modules/pyspark/sql/types.html#IntegerType)
[#](#pyspark.sql.types.IntegerType "Permalink to this definition")

Int data type, representing signed 32-bit integers.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.IntegerType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.IntegerType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.IntegerType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.IntegerType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.IntegerType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#IntegerType.simpleString)
[#](#pyspark.sql.types.IntegerType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.IntegerType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.IntegerType.typeName "Permalink to this definition")


# LongType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.LongType[\[source\]](about:blank/_modules/pyspark/sql/types.html#LongType)
[#](#pyspark.sql.types.LongType "Permalink to this definition")

Long data type, representing signed 64-bit integers.

If the values are beyond the range of \[-9223372036854775808, 9223372036854775807\], please use [`DecimalType`](about:blank/pyspark.sql.types.DecimalType.html#pyspark.sql.types.DecimalType "pyspark.sql.types.DecimalType").

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.LongType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.LongType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.LongType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.LongType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.LongType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#LongType.simpleString)
[#](#pyspark.sql.types.LongType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.LongType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.LongType.typeName "Permalink to this definition")



# MapType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.MapType(_keyType_, _valueType_, _valueContainsNull\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType)
[#](#pyspark.sql.types.MapType "Permalink to this definition")

Map data type.

Parameters

**keyType**[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") of the keys in the map.

**valueType**[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") of the values in the map.

**valueContainsNull**bool, optional

indicates whether values can contain null (None) values.

Notes

Keys in a map data type are not allowed to be null (None).

Examples

```
>>> from pyspark.sql.types import IntegerType, FloatType, MapType, StringType

```


The below example demonstrates how to create class:MapType:

```
>>> map_type = MapType(StringType(), IntegerType())

```


The values of the map can contain null (`None`) values by default:

```
>>> (MapType(StringType(), IntegerType())
...        == MapType(StringType(), IntegerType(), True))
True
>>> (MapType(StringType(), IntegerType(), False)
...        == MapType(StringType(), FloatType()))
False

```


Methods



* fromDDL(ddl): fromInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts an internal SQL object into a native Python object.
* fromDDL(ddl): fromJson(json[, fieldPath, collationsMap])
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): json()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): jsonValue()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): needConversion()
  * Creates DataType for a given DDL-formatted string.: Does this type needs conversion between Python object and internal SQL object.
* fromDDL(ddl): simpleString()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): toInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts a Python object into an internal SQL object.
* fromDDL(ddl): toNullable()
  * Creates DataType for a given DDL-formatted string.: Returns the same data type but set all nullability fields are true (StructField.nullable, ArrayType.containsNull, and MapType.valueContainsNull).
* fromDDL(ddl): typeName()
  * Creates DataType for a given DDL-formatted string.: 


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.MapType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.fromInternal)
[#](#pyspark.sql.types.MapType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

_classmethod_ fromJson(_json_, _fieldPath\=''_, _collationsMap\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.fromJson)
[#](#pyspark.sql.types.MapType.fromJson "Permalink to this definition")

json()
[#](#pyspark.sql.types.MapType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.jsonValue)
[#](#pyspark.sql.types.MapType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.needConversion)
[#](#pyspark.sql.types.MapType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.simpleString)
[#](#pyspark.sql.types.MapType.simpleString "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.toInternal)
[#](#pyspark.sql.types.MapType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

toNullable()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#MapType.toNullable)
[#](#pyspark.sql.types.MapType.toNullable "Permalink to this definition")

Returns the same data type but set all nullability fields are true (StructField.nullable, ArrayType.containsNull, and MapType.valueContainsNull).

New in version 4.0.0.

Returns

[`MapType`](#pyspark.sql.types.MapType "pyspark.sql.types.MapType")

Examples

Example 1: Simple nullability conversion

```
>>> MapType(IntegerType(), StringType(), valueContainsNull=False).toNullable()
MapType(IntegerType(), StringType(), True)

```


Example 2: Nested nullability conversion

```
>>> MapType(
...     StringType(),
...     MapType(
...         IntegerType(),
...         ArrayType(IntegerType(), containsNull=False),
...         valueContainsNull=False
...     ),
...     valueContainsNull=False
... ).toNullable()
MapType(StringType(), MapType(IntegerType(), ArrayType(IntegerType(), True), True), True)

```


_classmethod_ typeName()
[#](#pyspark.sql.types.MapType.typeName "Permalink to this definition")



# NullType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.NullType[\[source\]](about:blank/_modules/pyspark/sql/types.html#NullType)
[#](#pyspark.sql.types.NullType "Permalink to this definition")

Null type.

The data type representing None, used for the types that cannot be inferred.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.NullType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.NullType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.NullType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.NullType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.NullType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.NullType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.NullType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#NullType.typeName)
[#](#pyspark.sql.types.NullType.typeName "Permalink to this definition")



# ShortType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.ShortType[\[source\]](about:blank/_modules/pyspark/sql/types.html#ShortType)
[#](#pyspark.sql.types.ShortType "Permalink to this definition")

Short data type, representing signed 16-bit integers.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.ShortType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.ShortType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.ShortType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.ShortType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.ShortType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#ShortType.simpleString)
[#](#pyspark.sql.types.ShortType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.ShortType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.ShortType.typeName "Permalink to this definition")


# StringType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.StringType(_collation\='UTF8\_BINARY'_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StringType)
[#](#pyspark.sql.types.StringType "Permalink to this definition")

String data type.

Parameters

**collation**str

name of the collation, default is UTF8\_BINARY.

Methods



* collationProvider(collationName): fromDDL(ddl)
  * Creates DataType for a given DDL-formatted string.
* collationProvider(collationName): fromInternal(obj)
  * Converts an internal SQL object into a native Python object.
* collationProvider(collationName): isUTF8BinaryCollation()
* collationProvider(collationName): json()
* collationProvider(collationName): jsonValue()
* collationProvider(collationName): needConversion()
  * Does this type needs conversion between Python object and internal SQL object.
* collationProvider(collationName): simpleString()
* collationProvider(collationName): toInternal(obj)
  * Converts a Python object into an internal SQL object.
* collationProvider(collationName): typeName()


Attributes


|providerICU  |   |
|-------------|---|
|providerSpark|   |
|providers    |   |


Methods Documentation

_classmethod_ collationProvider(_collationName_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StringType.collationProvider)
[#](#pyspark.sql.types.StringType.collationProvider "Permalink to this definition")

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.StringType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.StringType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

isUTF8BinaryCollation()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StringType.isUTF8BinaryCollation)
[#](#pyspark.sql.types.StringType.isUTF8BinaryCollation "Permalink to this definition")

json()
[#](#pyspark.sql.types.StringType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StringType.jsonValue)
[#](#pyspark.sql.types.StringType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.StringType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StringType.simpleString)
[#](#pyspark.sql.types.StringType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.StringType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.StringType.typeName "Permalink to this definition")

Attributes Documentation

providerICU _\= 'icu'_[#](#pyspark.sql.types.StringType.providerICU "Permalink to this definition")

providerSpark _\= 'spark'_[#](#pyspark.sql.types.StringType.providerSpark "Permalink to this definition")

providers _\= \['spark', 'icu'\]_[#](#pyspark.sql.types.StringType.providers "Permalink to this definition")


# CharType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.CharType(_length_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CharType)
[#](#pyspark.sql.types.CharType "Permalink to this definition")

Char data type

Parameters

**length**int

the length limitation.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.CharType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.CharType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.CharType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CharType.jsonValue)
[#](#pyspark.sql.types.CharType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.CharType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CharType.simpleString)
[#](#pyspark.sql.types.CharType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.CharType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.CharType.typeName "Permalink to this definition")


# VarcharType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.VarcharType(_length_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VarcharType)
[#](#pyspark.sql.types.VarcharType "Permalink to this definition")

Varchar data type

Parameters

**length**int

the length limitation.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.VarcharType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[#](#pyspark.sql.types.VarcharType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.VarcharType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VarcharType.jsonValue)
[#](#pyspark.sql.types.VarcharType.jsonValue "Permalink to this definition")

needConversion()
[#](#pyspark.sql.types.VarcharType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VarcharType.simpleString)
[#](#pyspark.sql.types.VarcharType.simpleString "Permalink to this definition")

toInternal(_obj_)
[#](#pyspark.sql.types.VarcharType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.VarcharType.typeName "Permalink to this definition")


# StructField — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.StructField(_name_, _dataType_, _nullable\=True_, _metadata\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField)
[#](#pyspark.sql.types.StructField "Permalink to this definition")

A field in [`StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType").

Parameters

**name**str

name of the field.

**dataType**[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") of the field.

**nullable**bool, optional

whether the field can be null (None) or not.

**metadata**dict, optional

a dict from string to simple type that can be toInternald to JSON automatically

Examples

```
>>> from pyspark.sql.types import StringType, StructField
>>> (StructField("f1", StringType(), True)
...      == StructField("f1", StringType(), True))
True
>>> (StructField("f1", StringType(), True)
...      == StructField("f2", StringType(), True))
False

```


Methods



* fromDDL(ddl): fromInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts an internal SQL object into a native Python object.
* fromDDL(ddl): fromJson(json)
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): getCollationMetadata()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): getCollationsMap(metadata)
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): json()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): jsonValue()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): needConversion()
  * Creates DataType for a given DDL-formatted string.: Does this type needs conversion between Python object and internal SQL object.
* fromDDL(ddl): schemaCollationValue(dt)
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): simpleString()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): toInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts a Python object into an internal SQL object.
* fromDDL(ddl): typeName()
  * Creates DataType for a given DDL-formatted string.: 


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.StructField.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.fromInternal)
[#](#pyspark.sql.types.StructField.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

_classmethod_ fromJson(_json_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.fromJson)
[#](#pyspark.sql.types.StructField.fromJson "Permalink to this definition")

getCollationMetadata()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.getCollationMetadata)
[#](#pyspark.sql.types.StructField.getCollationMetadata "Permalink to this definition")

getCollationsMap(_metadata_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.getCollationsMap)
[#](#pyspark.sql.types.StructField.getCollationsMap "Permalink to this definition")

json()
[#](#pyspark.sql.types.StructField.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.jsonValue)
[#](#pyspark.sql.types.StructField.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.needConversion)
[#](#pyspark.sql.types.StructField.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

schemaCollationValue(_dt_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.schemaCollationValue)
[#](#pyspark.sql.types.StructField.schemaCollationValue "Permalink to this definition")

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.simpleString)
[#](#pyspark.sql.types.StructField.simpleString "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.toInternal)
[#](#pyspark.sql.types.StructField.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

typeName()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructField.typeName)
[#](#pyspark.sql.types.StructField.typeName "Permalink to this definition")


# StructType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.StructType(_fields\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType)
[#](#pyspark.sql.types.StructType "Permalink to this definition")

Struct type, consisting of a list of [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField").

This is the data type representing a [`Row`](about:blank/pyspark.sql.Row.html#pyspark.sql.Row "pyspark.sql.types.Row").

Iterating a [`StructType`](#pyspark.sql.types.StructType "pyspark.sql.types.StructType") will iterate over its [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField")s. A contained [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField") can be accessed by its name or position.

Examples

```
>>> from pyspark.sql.types import *
>>> struct1 = StructType([StructField("f1", StringType(), True)])
>>> struct1["f1"]
StructField('f1', StringType(), True)
>>> struct1[0]
StructField('f1', StringType(), True)

```


```
>>> struct1 = StructType([StructField("f1", StringType(), True)])
>>> struct2 = StructType([StructField("f1", StringType(), True)])
>>> struct1 == struct2
True
>>> struct1 = StructType([StructField("f1", CharType(10), True)])
>>> struct2 = StructType([StructField("f1", CharType(10), True)])
>>> struct1 == struct2
True
>>> struct1 = StructType([StructField("f1", VarcharType(10), True)])
>>> struct2 = StructType([StructField("f1", VarcharType(10), True)])
>>> struct1 == struct2
True
>>> struct1 = StructType([StructField("f1", StringType(), True)])
>>> struct2 = StructType([StructField("f1", StringType(), True),
...     StructField("f2", IntegerType(), False)])
>>> struct1 == struct2
False

```


The below example demonstrates how to create a DataFrame based on a struct created using class:StructType and class:StructField:

```
>>> data = [("Alice", ["Java", "Scala"]), ("Bob", ["Python", "Scala"])]
>>> schema = StructType([
...     StructField("name", StringType()),
...     StructField("languagesSkills", ArrayType(StringType())),
... ])
>>> df = spark.createDataFrame(data=data, schema=schema)
>>> df.printSchema()
root
 |-- name: string (nullable = true)
 |-- languagesSkills: array (nullable = true)
 |    |-- element: string (containsNull = true)
>>> df.show()
+-----+---------------+
| name|languagesSkills|
+-----+---------------+
|Alice|  [Java, Scala]|
|  Bob|[Python, Scala]|
+-----+---------------+

```


Methods



* add(field[, data_type, nullable, metadata]): fieldNames()
  * Construct a StructType by adding new elements to it, to define the schema.: Returns all field names in a list.
* add(field[, data_type, nullable, metadata]): fromDDL(ddl)
  * Construct a StructType by adding new elements to it, to define the schema.: Creates DataType for a given DDL-formatted string.
* add(field[, data_type, nullable, metadata]): fromInternal(obj)
  * Construct a StructType by adding new elements to it, to define the schema.: Converts an internal SQL object into a native Python object.
* add(field[, data_type, nullable, metadata]): fromJson(json)
  * Construct a StructType by adding new elements to it, to define the schema.: Constructs StructType from a schema defined in JSON format.
* add(field[, data_type, nullable, metadata]): json()
  * Construct a StructType by adding new elements to it, to define the schema.: 
* add(field[, data_type, nullable, metadata]): jsonValue()
  * Construct a StructType by adding new elements to it, to define the schema.: 
* add(field[, data_type, nullable, metadata]): needConversion()
  * Construct a StructType by adding new elements to it, to define the schema.: Does this type needs conversion between Python object and internal SQL object.
* add(field[, data_type, nullable, metadata]): simpleString()
  * Construct a StructType by adding new elements to it, to define the schema.: 
* add(field[, data_type, nullable, metadata]): toDDL()
  * Construct a StructType by adding new elements to it, to define the schema.: 
* add(field[, data_type, nullable, metadata]): toInternal(obj)
  * Construct a StructType by adding new elements to it, to define the schema.: Converts a Python object into an internal SQL object.
* add(field[, data_type, nullable, metadata]): toNullable()
  * Construct a StructType by adding new elements to it, to define the schema.: Returns the same data type but set all nullability fields are true (StructField.nullable, ArrayType.containsNull, and MapType.valueContainsNull).
* add(field[, data_type, nullable, metadata]): treeString([maxDepth])
  * Construct a StructType by adding new elements to it, to define the schema.: 
* add(field[, data_type, nullable, metadata]): typeName()
  * Construct a StructType by adding new elements to it, to define the schema.: 


Methods Documentation

add(_field_, _data\_type\=None_, _nullable\=True_, _metadata\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.add)
[#](#pyspark.sql.types.StructType.add "Permalink to this definition")

Construct a [`StructType`](#pyspark.sql.types.StructType "pyspark.sql.types.StructType") by adding new elements to it, to define the schema. The method accepts either:

> 1.  A single parameter which is a [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField") object.
>     
> 2.  Between 2 and 4 parameters as (name, data\_type, nullable (optional), metadata(optional). The data\_type parameter may be either a String or a [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object.
>     

Parameters

**field**str or [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField")

Either the name of the field or a [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField") object

**data\_type**[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType"), optional

If present, the DataType of the [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField") to create

**nullable**bool, optional

Whether the field to add should be nullable (default True)

**metadata**dict, optional

Any additional metadata (default None)

Returns

[`StructType`](#pyspark.sql.types.StructType "pyspark.sql.types.StructType")

Examples

```
>>> from pyspark.sql.types import IntegerType, StringType, StructField, StructType
>>> struct1 = StructType().add("f1", StringType(), True).add("f2", StringType(), True, None)
>>> struct2 = StructType([StructField("f1", StringType(), True),
...     StructField("f2", StringType(), True, None)])
>>> struct1 == struct2
True
>>> struct1 = StructType().add(StructField("f1", StringType(), True))
>>> struct2 = StructType([StructField("f1", StringType(), True)])
>>> struct1 == struct2
True
>>> struct1 = StructType().add("f1", "string", True)
>>> struct2 = StructType([StructField("f1", StringType(), True)])
>>> struct1 == struct2
True

```


fieldNames()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.fieldNames)
[#](#pyspark.sql.types.StructType.fieldNames "Permalink to this definition")

Returns all field names in a list.

Examples

```
>>> from pyspark.sql.types import StringType, StructField, StructType
>>> struct = StructType([StructField("f1", StringType(), True)])
>>> struct.fieldNames()
['f1']

```


_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.StructType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.fromInternal)
[#](#pyspark.sql.types.StructType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

_classmethod_ fromJson(_json_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.fromJson)
[#](#pyspark.sql.types.StructType.fromJson "Permalink to this definition")

Constructs [`StructType`](#pyspark.sql.types.StructType "pyspark.sql.types.StructType") from a schema defined in JSON format.

Below is a JSON schema it must adhere to:

```
 {
   "title":"StructType",
   "description":"Schema of StructType in json format",
   "type":"object",
   "properties":{
      "fields":{
         "description":"Array of struct fields",
         "type":"array",
         "items":{
             "type":"object",
             "properties":{
                "name":{
                   "description":"Name of the field",
                   "type":"string"
                },
                "type":{
                   "description": "Type of the field. Can either be
                                   another nested StructType or primitive type",
                   "type":"object/string"
                },
                "nullable":{
                   "description":"If nulls are allowed",
                   "type":"boolean"
                },
                "metadata":{
                   "description":"Additional metadata to supply",
                   "type":"object"
                },
                "required":[
                   "name",
                   "type",
                   "nullable",
                   "metadata"
                ]
             }
        }
     }
  }
}

```


Parameters

**json**dict or a dict-like object e.g. JSON object

This “dict” must have “fields” key that returns an array of fields each of which must have specific keys (name, type, nullable, metadata).

Returns

[`StructType`](#pyspark.sql.types.StructType "pyspark.sql.types.StructType")

Examples

```
>>> json_str = '''
...  {
...      "fields": [
...          {
...              "metadata": {},
...              "name": "Person",
...              "nullable": true,
...              "type": {
...                  "fields": [
...                      {
...                          "metadata": {},
...                          "name": "name",
...                          "nullable": false,
...                          "type": "string"
...                      },
...                      {
...                          "metadata": {},
...                          "name": "surname",
...                          "nullable": false,
...                          "type": "string"
...                      }
...                  ],
...                  "type": "struct"
...              }
...          }
...      ],
...      "type": "struct"
...  }
...  '''
>>> import json
>>> scheme = StructType.fromJson(json.loads(json_str))
>>> scheme.simpleString()
'struct<Person:struct<name:string,surname:string>>'

```


json()
[#](#pyspark.sql.types.StructType.json "Permalink to this definition")

jsonValue()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.jsonValue)
[#](#pyspark.sql.types.StructType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.needConversion)
[#](#pyspark.sql.types.StructType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.simpleString)
[#](#pyspark.sql.types.StructType.simpleString "Permalink to this definition")

toDDL()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.toDDL)
[#](#pyspark.sql.types.StructType.toDDL "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.toInternal)
[#](#pyspark.sql.types.StructType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

toNullable()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.toNullable)
[#](#pyspark.sql.types.StructType.toNullable "Permalink to this definition")

Returns the same data type but set all nullability fields are true (StructField.nullable, ArrayType.containsNull, and MapType.valueContainsNull).

New in version 4.0.0.

Returns

[`StructType`](#pyspark.sql.types.StructType "pyspark.sql.types.StructType")

Examples

Example 1: Simple nullability conversion

```
>>> StructType([StructField("a", IntegerType(), nullable=False)]).toNullable()
StructType([StructField('a', IntegerType(), True)])

```


Example 2: Nested nullability conversion

```
>>> StructType([
...     StructField("a",
...         StructType([
...             StructField("b", IntegerType(), nullable=False),
...             StructField("c", StructType([
...                 StructField("d", IntegerType(), nullable=False)
...             ]))
...         ]),
...         nullable=False)
... ]).toNullable()
StructType([StructField('a', StructType([StructField('b', IntegerType(), True),
StructField('c', StructType([StructField('d', IntegerType(), True)]), True)]), True)])

```


treeString(_maxDepth\=2147483647_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#StructType.treeString)
[#](#pyspark.sql.types.StructType.treeString "Permalink to this definition")

_classmethod_ typeName()
[#](#pyspark.sql.types.StructType.typeName "Permalink to this definition")



# VariantType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.VariantType[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantType)
[#](#pyspark.sql.types.VariantType "Permalink to this definition")

Variant data type, representing semi-structured values.

New in version 4.0.0.

Methods



* fromDDL(ddl): fromInternal(obj)
  * Creates DataType for a given DDL-formatted string.: Converts an internal SQL object into a native Python object.
* fromDDL(ddl): json()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): jsonValue()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): needConversion()
  * Creates DataType for a given DDL-formatted string.: Does this type needs conversion between Python object and internal SQL object.
* fromDDL(ddl): simpleString()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): toInternal(variant)
  * Creates DataType for a given DDL-formatted string.: Converts a Python object into an internal SQL object.
* fromDDL(ddl): typeName()
  * Creates DataType for a given DDL-formatted string.: 


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.VariantType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantType.fromInternal)
[#](#pyspark.sql.types.VariantType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.VariantType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.VariantType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantType.needConversion)
[#](#pyspark.sql.types.VariantType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.VariantType.simpleString "Permalink to this definition")

toInternal(_variant_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantType.toInternal)
[#](#pyspark.sql.types.VariantType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.VariantType.typeName "Permalink to this definition")



# TimestampType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.TimestampType[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampType)
[#](#pyspark.sql.types.TimestampType "Permalink to this definition")

Timestamp (datetime.datetime) data type.

Methods


|fromDDL(ddl)    |Creates DataType for a given DDL-formatted string.                            |
|----------------|------------------------------------------------------------------------------|
|fromInternal(ts)|Converts an internal SQL object into a native Python object.                  |
|json()          |                                                                              |
|jsonValue()     |                                                                              |
|needConversion()|Does this type needs conversion between Python object and internal SQL object.|
|simpleString()  |                                                                              |
|toInternal(dt)  |Converts a Python object into an internal SQL object.                         |
|typeName()      |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.TimestampType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_ts_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampType.fromInternal)
[#](#pyspark.sql.types.TimestampType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.TimestampType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.TimestampType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampType.needConversion)
[#](#pyspark.sql.types.TimestampType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.TimestampType.simpleString "Permalink to this definition")

toInternal(_dt_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampType.toInternal)
[#](#pyspark.sql.types.TimestampType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.TimestampType.typeName "Permalink to this definition")



# TimestampNTZType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.TimestampNTZType[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampNTZType)
[#](#pyspark.sql.types.TimestampNTZType "Permalink to this definition")

Timestamp (datetime.datetime) data type without timezone information.

Methods


|fromDDL(ddl)    |Creates DataType for a given DDL-formatted string.                            |
|----------------|------------------------------------------------------------------------------|
|fromInternal(ts)|Converts an internal SQL object into a native Python object.                  |
|json()          |                                                                              |
|jsonValue()     |                                                                              |
|needConversion()|Does this type needs conversion between Python object and internal SQL object.|
|simpleString()  |                                                                              |
|toInternal(dt)  |Converts a Python object into an internal SQL object.                         |
|typeName()      |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.TimestampNTZType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_ts_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampNTZType.fromInternal)
[#](#pyspark.sql.types.TimestampNTZType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.TimestampNTZType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.TimestampNTZType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampNTZType.needConversion)
[#](#pyspark.sql.types.TimestampNTZType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.TimestampNTZType.simpleString "Permalink to this definition")

toInternal(_dt_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampNTZType.toInternal)
[#](#pyspark.sql.types.TimestampNTZType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#TimestampNTZType.typeName)
[#](#pyspark.sql.types.TimestampNTZType.typeName "Permalink to this definition")



# DayTimeIntervalType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.DayTimeIntervalType(_startField\=None_, _endField\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DayTimeIntervalType)
[#](#pyspark.sql.types.DayTimeIntervalType "Permalink to this definition")

DayTimeIntervalType (datetime.timedelta).

Methods



* fromDDL(ddl): fromInternal(micros)
  * Creates DataType for a given DDL-formatted string.: Converts an internal SQL object into a native Python object.
* fromDDL(ddl): json()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): jsonValue()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): needConversion()
  * Creates DataType for a given DDL-formatted string.: Does this type needs conversion between Python object and internal SQL object.
* fromDDL(ddl): simpleString()
  * Creates DataType for a given DDL-formatted string.: 
* fromDDL(ddl): toInternal(dt)
  * Creates DataType for a given DDL-formatted string.: Converts a Python object into an internal SQL object.
* fromDDL(ddl): typeName()
  * Creates DataType for a given DDL-formatted string.: 


Attributes


|DAY   |   |
|------|---|
|HOUR  |   |
|MINUTE|   |
|SECOND|   |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.DayTimeIntervalType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_micros_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DayTimeIntervalType.fromInternal)
[#](#pyspark.sql.types.DayTimeIntervalType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.DayTimeIntervalType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.DayTimeIntervalType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DayTimeIntervalType.needConversion)
[#](#pyspark.sql.types.DayTimeIntervalType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.DayTimeIntervalType.simpleString "Permalink to this definition")

toInternal(_dt_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#DayTimeIntervalType.toInternal)
[#](#pyspark.sql.types.DayTimeIntervalType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.DayTimeIntervalType.typeName "Permalink to this definition")

Attributes Documentation

DAY _\= 0_[#](#pyspark.sql.types.DayTimeIntervalType.DAY "Permalink to this definition")

HOUR _\= 1_[#](#pyspark.sql.types.DayTimeIntervalType.HOUR "Permalink to this definition")

MINUTE _\= 2_[#](#pyspark.sql.types.DayTimeIntervalType.MINUTE "Permalink to this definition")

SECOND _\= 3_[#](#pyspark.sql.types.DayTimeIntervalType.SECOND "Permalink to this definition")



# YearMonthIntervalType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.YearMonthIntervalType(_startField\=None_, _endField\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#YearMonthIntervalType)
[#](#pyspark.sql.types.YearMonthIntervalType "Permalink to this definition")

YearMonthIntervalType, represents year-month intervals of the SQL standard

Notes

This data type doesn’t support collection: df.collect/take/head.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Attributes


|MONTH|   |
|-----|---|
|YEAR |   |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.YearMonthIntervalType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#YearMonthIntervalType.fromInternal)
[#](#pyspark.sql.types.YearMonthIntervalType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.YearMonthIntervalType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.YearMonthIntervalType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#YearMonthIntervalType.needConversion)
[#](#pyspark.sql.types.YearMonthIntervalType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.YearMonthIntervalType.simpleString "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#YearMonthIntervalType.toInternal)
[#](#pyspark.sql.types.YearMonthIntervalType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[#](#pyspark.sql.types.YearMonthIntervalType.typeName "Permalink to this definition")

Attributes Documentation

MONTH _\= 1_[#](#pyspark.sql.types.YearMonthIntervalType.MONTH "Permalink to this definition")

YEAR _\= 0_[#](#pyspark.sql.types.YearMonthIntervalType.YEAR "Permalink to this definition")


# CalendarIntervalType — PySpark 4.0.1 documentation
_class_ pyspark.sql.types.CalendarIntervalType[\[source\]](about:blank/_modules/pyspark/sql/types.html#CalendarIntervalType)
[#](#pyspark.sql.types.CalendarIntervalType "Permalink to this definition")

The data type representing calendar intervals.

The calendar interval is stored internally in three components: - an integer value representing the number of months in this interval. - an integer value representing the number of days in this interval. - a long value representing the number of microseconds in this interval.

Methods


|fromDDL(ddl)     |Creates DataType for a given DDL-formatted string.                            |
|-----------------|------------------------------------------------------------------------------|
|fromInternal(obj)|Converts an internal SQL object into a native Python object.                  |
|json()           |                                                                              |
|jsonValue()      |                                                                              |
|needConversion() |Does this type needs conversion between Python object and internal SQL object.|
|simpleString()   |                                                                              |
|toInternal(obj)  |Converts a Python object into an internal SQL object.                         |
|typeName()       |                                                                              |


Methods Documentation

_classmethod_ fromDDL(_ddl_)
[#](#pyspark.sql.types.CalendarIntervalType.fromDDL "Permalink to this definition")

Creates [`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") for a given DDL-formatted string.

New in version 4.0.0.

Parameters

**ddl**str

DDL-formatted string representation of types, e.g. [`pyspark.sql.types.DataType.simpleString`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType.simpleString "pyspark.sql.types.DataType.simpleString"), except that top level struct type can omit the `struct<>` for the compatibility reason with `spark.createDataFrame` and Python UDFs.

Returns

[`DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType")

Examples

Create a StructType by the corresponding DDL formatted string.

```
>>> from pyspark.sql.types import DataType
>>> DataType.fromDDL("b string, a int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


Create a single DataType by the corresponding DDL formatted string.

```
>>> DataType.fromDDL("decimal(10,10)")
DecimalType(10,10)

```


Create a StructType by the legacy string format.

```
>>> DataType.fromDDL("b: string, a: int")
StructType([StructField('b', StringType(), True), StructField('a', IntegerType(), True)])

```


fromInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CalendarIntervalType.fromInternal)
[#](#pyspark.sql.types.CalendarIntervalType.fromInternal "Permalink to this definition")

Converts an internal SQL object into a native Python object.

json()
[#](#pyspark.sql.types.CalendarIntervalType.json "Permalink to this definition")

jsonValue()
[#](#pyspark.sql.types.CalendarIntervalType.jsonValue "Permalink to this definition")

needConversion()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CalendarIntervalType.needConversion)
[#](#pyspark.sql.types.CalendarIntervalType.needConversion "Permalink to this definition")

Does this type needs conversion between Python object and internal SQL object.

This is used to avoid the unnecessary conversion for ArrayType/MapType/StructType.

simpleString()
[#](#pyspark.sql.types.CalendarIntervalType.simpleString "Permalink to this definition")

toInternal(_obj_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CalendarIntervalType.toInternal)
[#](#pyspark.sql.types.CalendarIntervalType.toInternal "Permalink to this definition")

Converts a Python object into an internal SQL object.

_classmethod_ typeName()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#CalendarIntervalType.typeName)
[#](#pyspark.sql.types.CalendarIntervalType.typeName "Permalink to this definition")


