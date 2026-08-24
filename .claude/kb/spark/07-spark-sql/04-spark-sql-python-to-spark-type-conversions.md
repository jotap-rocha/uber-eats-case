# Python to Spark Type Conversions — PySpark 4.0.1 documentation
When working with PySpark, you will often need to consider the conversions between Python-native objects to their Spark equivalents. For instance, when working with user-defined functions, the function return type will be cast by Spark to an appropriate Spark SQL type. Or, when creating a `DataFrame`, you may supply `numpy` or `pandas` objects as the inputted data. This guide will cover the various conversions between Python and Spark SQL types.

Browsing Type Conversions[#](#browsing-type-conversions "Permalink to this headline")
-------------------------------------------------------------------------------------

Though this document provides a comprehensive list of type conversions, you may find it easier to interactively check the conversion behavior of Spark. To do so, you can test small examples of user-defined functions, and use the `spark.createDataFrame` interface.

All data types of Spark SQL are located in the package of `pyspark.sql.types`. You can access them by doing:

```
from pyspark.sql.types import *

```


Configuration[#](#configuration "Permalink to this headline")
-------------------------------------------------------------

There are several configurations that affect the behavior of type conversions. These configurations are listed below:



* Configuration: spark.sql.execution.pythonUDF.arrow.enabled
  * Description: Enable PyArrow in PySpark. See more here.
  * Default: False
* Configuration: spark.sql.pyspark.inferNestedDictAsStruct.enabled
  * Description: When enabled, nested dictionaries are inferred as StructType. Otherwise, they are inferred as MapType.
  * Default: False
* Configuration: spark.sql.timestampType
  * Description: If set to TIMESTAMP_NTZ, the default timestamp type is TimestampNTZType. Otherwise, the default timestamp type is TimestampType.
  * Default: “”
* Configuration: spark.sql.execution.pandas.inferPandasDictAsMap
  * Description: When enabled, Pandas dictionaries are inferred as MapType. Otherwise, they are inferred as StructType.
  * Default: False


All Conversions[#](#all-conversions "Permalink to this headline")
-----------------------------------------------------------------



* Data type: ByteType
  * Value type in Python: intNoteNumbers will be converted to 1-byte signed integer numbers at runtime. Please make sure that numbers are within the range of -128 to 127.
  * API to access or create a data type: ByteType()
* Data type: ShortType
  * Value type in Python: intNoteNumbers will be converted to 2-byte signed integer numbers at runtime. Please make sure that numbers are within the range of -32768 to 32767.
  * API to access or create a data type: ShortType()
* Data type: IntegerType
  * Value type in Python: int
  * API to access or create a data type: IntegerType()
* Data type: LongType
  * Value type in Python: intNoteNumbers will be converted to 8-byte signed integer numbers at runtime. Please make sure that numbers are within the range of -9223372036854775808 to 9223372036854775807. Otherwise, please convert data to decimal.Decimal and use DecimalType.
  * API to access or create a data type: LongType()
* Data type: FloatType
  * Value type in Python: floatNoteNumbers will be converted to 4-byte single-precision floating point numbers at runtime.
  * API to access or create a data type: FloatType()
* Data type: DoubleType
  * Value type in Python: float
  * API to access or create a data type: DoubleType()
* Data type: DecimalType
  * Value type in Python: decimal.Decimal
  * API to access or create a data type: DecimalType()|
* Data type: StringType
  * Value type in Python: string
  * API to access or create a data type: StringType()
* Data type: BinaryType
  * Value type in Python: bytearray
  * API to access or create a data type: BinaryType()
* Data type: BooleanType
  * Value type in Python: bool
  * API to access or create a data type: BooleanType()
* Data type: TimestampType
  * Value type in Python: datetime.datetime
  * API to access or create a data type: TimestampType()
* Data type: TimestampNTZType
  * Value type in Python: datetime.datetime
  * API to access or create a data type: TimestampNTZType()
* Data type: DateType
  * Value type in Python: datetime.date
  * API to access or create a data type: DateType()
* Data type: DayTimeIntervalType
  * Value type in Python: datetime.timedelta
  * API to access or create a data type: DayTimeIntervalType()
* Data type: ArrayType
  * Value type in Python: list, tuple, or array
  * API to access or create a data type: ArrayType(elementType, [containsNull])NoteThe default value of containsNull is True.
* Data type: MapType
  * Value type in Python: dict
  * API to access or create a data type: MapType(keyType, valueType, [valueContainsNull])NoteThe default value of valueContainsNull is True.
* Data type: StructType
  * Value type in Python: list or tuple
  * API to access or create a data type: StructType(fields)Notefields is a Seq of StructFields. Also, two fields with the same name are not allowed.
* Data type: StructField
  * Value type in Python: The value type in Python of the data type of this field. For example, Int for a StructField with the data type IntegerType.
  * API to access or create a data type: StructField(name, dataType, [nullable])NoteThe default value of nullable is True.


Conversions in Practice - UDFs[#](#conversions-in-practice-udfs "Permalink to this headline")
---------------------------------------------------------------------------------------------

A common conversion case is returning a Python value from a UDF. In this case, the return type of the UDF must match the provided return type.

Note

If the actual return type of your function does not match the provided return type, Spark will implicitly cast the value to null.

```
from pyspark.sql.types import (
    StructType,
    StructField,
    IntegerType,
    StringType,
    FloatType,
)
from pyspark.sql.functions import udf, col

df = spark.createDataFrame(
    [[1]], schema=StructType([StructField("int", IntegerType())])
)

@udf(returnType=StringType())
def to_string(value):
    return str(value)

@udf(returnType=FloatType())
def to_float(value):
    return float(value)

df.withColumn("cast_int", to_float(col("int"))).withColumn(
    "cast_str", to_string(col("int"))
).printSchema()
# root
# |-- int: integer (nullable = true)
# |-- cast_int: float (nullable = true)
# |-- cast_str: string (nullable = true)

```


Conversions in Practice - Creating DataFrames[#](#conversions-in-practice-creating-dataframes "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------------

Another common conversion case is when creating a DataFrame from values in Python. In this case, you can supply a schema, or allow Spark to infer the schema from the provided data.

```
data = [
    ["Wei", "Math", 93.0, 1],
    ["Jerry", "Physics", 85.0, 4],
    ["Katrina", "Geology", 90.0, 2],
]
cols = ["Name", "Subject", "Score", "Period"]

spark.createDataFrame(data, cols).printSchema()
# root
# |-- Name: string (nullable = true)
# |-- Subject: string (nullable = true)
# |-- Score: double (nullable = true)
# |-- Period: long (nullable = true)

import pandas as pd

df = pd.DataFrame(data, columns=cols)
spark.createDataFrame(df).printSchema()
# root
# |-- Name: string (nullable = true)
# |-- Subject: string (nullable = true)
# |-- Score: double (nullable = true)
# |-- Period: long (nullable = true)

import numpy as np

spark.createDataFrame(np.zeros([3, 2], "int8")).printSchema()
# root
# |-- _1: byte (nullable = true)
# |-- _2: byte (nullable = true)

```


Conversions in Practice - Nested Data Types[#](#conversions-in-practice-nested-data-types "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------------

Nested data types will convert to `StructType`, `MapType`, and `ArrayType`, depending on the passed data.

```
data = [
    ["Wei", [[1, 2]], {"RecordType": "Scores", "Math": { "H1": 93.0, "H2": 85.0}}],
]
cols = ["Name", "ActiveHalfs", "Record"]

spark.createDataFrame(data, cols).printSchema()
# root
#  |-- Name: string (nullable = true)
#  |-- ActiveHalfs: array (nullable = true)
#  |    |-- element: array (containsNull = true)
#  |    |    |-- element: long (containsNull = true)
#  |-- Record: map (nullable = true)
#  |    |-- key: string
#  |    |-- value: string (valueContainsNull = true)

spark.conf.set('spark.sql.pyspark.inferNestedDictAsStruct.enabled', True)

spark.createDataFrame(data, cols).printSchema()
# root
#  |-- Name: string (nullable = true)
#  |-- ActiveHalfs: array (nullable = true)
#  |    |-- element: array (containsNull = true)
#  |    |    |-- element: long (containsNull = true)
#  |-- Record: struct (nullable = true)
#  |    |-- RecordType: string (nullable = true)
#  |    |-- Math: struct (nullable = true)
#  |    |    |-- H1: double (nullable = true)
#  |    |    |-- H2: double (nullable = true)

```
