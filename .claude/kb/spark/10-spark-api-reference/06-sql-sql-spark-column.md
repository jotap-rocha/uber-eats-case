# Column — PySpark 4.0.1 documentation
[`Column.__getattr__`](about:blank/api/pyspark.sql.Column.__getattr__.html#pyspark.sql.Column.__getattr__ "pyspark.sql.Column.__getattr__")(item)

An expression that gets an item at position `ordinal` out of a list, or gets an item by key out of a dict.

[`Column.__getitem__`](about:blank/api/pyspark.sql.Column.__getitem__.html#pyspark.sql.Column.__getitem__ "pyspark.sql.Column.__getitem__")(k)

An expression that gets an item at position `ordinal` out of a list, or gets an item by key out of a dict.

[`Column.alias`](about:blank/api/pyspark.sql.Column.alias.html#pyspark.sql.Column.alias "pyspark.sql.Column.alias")(\*alias, \*\*kwargs)

Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).

[`Column.asc`](about:blank/api/pyspark.sql.Column.asc.html#pyspark.sql.Column.asc "pyspark.sql.Column.asc")()

Returns a sort expression based on the ascending order of the column.

[`Column.asc_nulls_first`](about:blank/api/pyspark.sql.Column.asc_nulls_first.html#pyspark.sql.Column.asc_nulls_first "pyspark.sql.Column.asc_nulls_first")()

Returns a sort expression based on ascending order of the column, and null values return before non-null values.

[`Column.asc_nulls_last`](about:blank/api/pyspark.sql.Column.asc_nulls_last.html#pyspark.sql.Column.asc_nulls_last "pyspark.sql.Column.asc_nulls_last")()

Returns a sort expression based on ascending order of the column, and null values appear after non-null values.

[`Column.astype`](about:blank/api/pyspark.sql.Column.astype.html#pyspark.sql.Column.astype "pyspark.sql.Column.astype")(dataType)

`astype()` is an alias for `cast()`.

[`Column.between`](about:blank/api/pyspark.sql.Column.between.html#pyspark.sql.Column.between "pyspark.sql.Column.between")(lowerBound, upperBound)

Check if the current column's values are between the specified lower and upper bounds, inclusive.

[`Column.bitwiseAND`](about:blank/api/pyspark.sql.Column.bitwiseAND.html#pyspark.sql.Column.bitwiseAND "pyspark.sql.Column.bitwiseAND")(other)

Compute bitwise AND of this expression with another expression.

[`Column.bitwiseOR`](about:blank/api/pyspark.sql.Column.bitwiseOR.html#pyspark.sql.Column.bitwiseOR "pyspark.sql.Column.bitwiseOR")(other)

"

[`Column.bitwiseXOR`](about:blank/api/pyspark.sql.Column.bitwiseXOR.html#pyspark.sql.Column.bitwiseXOR "pyspark.sql.Column.bitwiseXOR")(other)

Compute bitwise XOR of this expression with another expression.

[`Column.cast`](about:blank/api/pyspark.sql.Column.cast.html#pyspark.sql.Column.cast "pyspark.sql.Column.cast")(dataType)

Casts the column into type `dataType`.

[`Column.contains`](about:blank/api/pyspark.sql.Column.contains.html#pyspark.sql.Column.contains "pyspark.sql.Column.contains")(other)

Contains the other element.

[`Column.desc`](about:blank/api/pyspark.sql.Column.desc.html#pyspark.sql.Column.desc "pyspark.sql.Column.desc")()

Returns a sort expression based on the descending order of the column.

[`Column.desc_nulls_first`](about:blank/api/pyspark.sql.Column.desc_nulls_first.html#pyspark.sql.Column.desc_nulls_first "pyspark.sql.Column.desc_nulls_first")()

Returns a sort expression based on the descending order of the column, and null values appear before non-null values.

[`Column.desc_nulls_last`](about:blank/api/pyspark.sql.Column.desc_nulls_last.html#pyspark.sql.Column.desc_nulls_last "pyspark.sql.Column.desc_nulls_last")()

Returns a sort expression based on the descending order of the column, and null values appear after non-null values.

[`Column.dropFields`](about:blank/api/pyspark.sql.Column.dropFields.html#pyspark.sql.Column.dropFields "pyspark.sql.Column.dropFields")(\*fieldNames)

An expression that drops fields in `StructType` by name.

[`Column.endswith`](about:blank/api/pyspark.sql.Column.endswith.html#pyspark.sql.Column.endswith "pyspark.sql.Column.endswith")(other)

String ends with.

[`Column.eqNullSafe`](about:blank/api/pyspark.sql.Column.eqNullSafe.html#pyspark.sql.Column.eqNullSafe "pyspark.sql.Column.eqNullSafe")(other)

Equality test that is safe for null values.

[`Column.getField`](about:blank/api/pyspark.sql.Column.getField.html#pyspark.sql.Column.getField "pyspark.sql.Column.getField")(name)

An expression that gets a field by name in a `StructType`.

[`Column.getItem`](about:blank/api/pyspark.sql.Column.getItem.html#pyspark.sql.Column.getItem "pyspark.sql.Column.getItem")(key)

An expression that gets an item at position `ordinal` out of a list, or gets an item by key out of a dict.

[`Column.ilike`](about:blank/api/pyspark.sql.Column.ilike.html#pyspark.sql.Column.ilike "pyspark.sql.Column.ilike")(other)

SQL ILIKE expression (case insensitive LIKE).

[`Column.isNaN`](about:blank/api/pyspark.sql.Column.isNaN.html#pyspark.sql.Column.isNaN "pyspark.sql.Column.isNaN")()

True if the current expression is NaN.

[`Column.isNotNull`](about:blank/api/pyspark.sql.Column.isNotNull.html#pyspark.sql.Column.isNotNull "pyspark.sql.Column.isNotNull")()

True if the current expression is NOT null.

[`Column.isNull`](about:blank/api/pyspark.sql.Column.isNull.html#pyspark.sql.Column.isNull "pyspark.sql.Column.isNull")()

True if the current expression is null.

[`Column.isin`](about:blank/api/pyspark.sql.Column.isin.html#pyspark.sql.Column.isin "pyspark.sql.Column.isin")(\*cols)

A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.

[`Column.like`](about:blank/api/pyspark.sql.Column.like.html#pyspark.sql.Column.like "pyspark.sql.Column.like")(other)

SQL like expression.

[`Column.name`](about:blank/api/pyspark.sql.Column.name.html#pyspark.sql.Column.name "pyspark.sql.Column.name")(\*alias, \*\*kwargs)

`name()` is an alias for `alias()`.

[`Column.otherwise`](about:blank/api/pyspark.sql.Column.otherwise.html#pyspark.sql.Column.otherwise "pyspark.sql.Column.otherwise")(value)

Evaluates a list of conditions and returns one of multiple possible result expressions.

[`Column.outer`](about:blank/api/pyspark.sql.Column.outer.html#pyspark.sql.Column.outer "pyspark.sql.Column.outer")()

Mark this column as an outer column if its expression refers to columns from an outer query.

[`Column.over`](about:blank/api/pyspark.sql.Column.over.html#pyspark.sql.Column.over "pyspark.sql.Column.over")(window)

Define a windowing column.

[`Column.rlike`](about:blank/api/pyspark.sql.Column.rlike.html#pyspark.sql.Column.rlike "pyspark.sql.Column.rlike")(other)

SQL RLIKE expression (LIKE with Regex).

[`Column.startswith`](about:blank/api/pyspark.sql.Column.startswith.html#pyspark.sql.Column.startswith "pyspark.sql.Column.startswith")(other)

String starts with.

[`Column.substr`](about:blank/api/pyspark.sql.Column.substr.html#pyspark.sql.Column.substr "pyspark.sql.Column.substr")(startPos, length)

Return a [`Column`](about:blank/api/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") which is a substring of the column.

[`Column.try_cast`](about:blank/api/pyspark.sql.Column.try_cast.html#pyspark.sql.Column.try_cast "pyspark.sql.Column.try_cast")(dataType)

This is a special version of cast that performs the same operation, but returns a NULL value instead of raising an error if the invoke method throws exception.

[`Column.when`](about:blank/api/pyspark.sql.Column.when.html#pyspark.sql.Column.when "pyspark.sql.Column.when")(condition, value)

Evaluates a list of conditions and returns one of multiple possible result expressions.

[`Column.withField`](about:blank/api/pyspark.sql.Column.withField.html#pyspark.sql.Column.withField "pyspark.sql.Column.withField")(fieldName, col)

An expression that adds/replaces a field in `StructType` by name.


# pyspark.sql.Column.__getattr__ — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.\_\_getattr\_\_

Column.\_\_getattr\_\_(_item_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.__getattr__)
[#](#pyspark.sql.Column.__getattr__ "Permalink to this definition")

An expression that gets an item at position `ordinal` out of a list, or gets an item by key out of a dict.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**item**

a literal value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing the item got by key out of a dict.

Examples

```
>>> df = spark.createDataFrame([('abcedfg', {"key": "value"})], ["l", "d"])
>>> df.select(df.d.key).show()
+------+
|d[key]|
+------+
| value|
+------+

```

# pyspark.sql.Column.__getitem__ — PySpark 4.0.1 documentation
Column.\_\_getitem\_\_(_k_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.__getitem__)
[#](#pyspark.sql.Column.__getitem__ "Permalink to this definition")

An expression that gets an item at position `ordinal` out of a list, or gets an item by key out of a dict.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**k**

a literal value, or a slice object without step.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing the item got by key out of a dict, or substrings sliced by the given slice object.

Examples

```
>>> df = spark.createDataFrame([('abcedfg', {"key": "value"})], ["l", "d"])
>>> df.select(df.l[slice(1, 3)], df.d['key']).show()
+---------------+------+
|substr(l, 1, 3)|d[key]|
+---------------+------+
|            abc| value|
+---------------+------+

```

# pyspark.sql.Column.alias — PySpark 4.0.1 documentation
Column.alias(_\*alias_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.alias)
[#](#pyspark.sql.Column.alias "Permalink to this definition")

Returns this column aliased with a new name or names (in the case of expressions that return more than one column, such as explode).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**alias**str

desired column names (collects all positional arguments passed)

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column is aliased with new name or names.

Other Parameters

**metadata: dict**

a dict of information to be stored in `metadata` attribute of the corresponding [`StructField`](about:blank/pyspark.sql.types.StructField.html#pyspark.sql.types.StructField "pyspark.sql.types.StructField") (optional, keyword only argument)

Changed in version 2.2.0: Added optional `metadata` argument.

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.select(df.age.alias("age2")).collect()
[Row(age2=2), Row(age2=5)]
>>> df.select(df.age.alias("age3", metadata={'max': 99})).schema['age3'].metadata['max']
99

```

# pyspark.sql.Column.asc — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.asc

Column.asc()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.asc)
[#](#pyspark.sql.Column.asc "Permalink to this definition")

Returns a sort expression based on the ascending order of the column.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([('Tom', 80), ('Alice', None)], ["name", "height"])
>>> df.select(df.name).orderBy(df.name.asc()).collect()
[Row(name='Alice'), Row(name='Tom')]

```

# pyspark.sql.Column.asc_nulls_first — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.asc\_nulls\_first

Column.asc\_nulls\_first()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.asc_nulls_first)
[#](#pyspark.sql.Column.asc_nulls_first "Permalink to this definition")

Returns a sort expression based on ascending order of the column, and null values return before non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame(
...     [('Tom', 80), (None, 60), ('Alice', None)], ["name", "height"])
>>> df.select(df.name).orderBy(df.name.asc_nulls_first()).collect()
[Row(name=None), Row(name='Alice'), Row(name='Tom')]

```
# pyspark.sql.Column.asc_nulls_last — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.asc\_nulls\_last

Column.asc\_nulls\_last()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.asc_nulls_last)
[#](#pyspark.sql.Column.asc_nulls_last "Permalink to this definition")

Returns a sort expression based on ascending order of the column, and null values appear after non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame(
...     [('Tom', 80), (None, 60), ('Alice', None)], ["name", "height"])
>>> df.select(df.name).orderBy(df.name.asc_nulls_last()).collect()
[Row(name='Alice'), Row(name='Tom'), Row(name=None)]

```

# pyspark.sql.Column.astype — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.astype

Column.astype(_dataType_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.astype)
[#](#pyspark.sql.Column.astype "Permalink to this definition")

[`astype()`](#pyspark.sql.Column.astype "pyspark.sql.Column.astype") is an alias for [`cast()`](about:blank/pyspark.sql.Column.cast.html#pyspark.sql.Column.cast "pyspark.sql.Column.cast").

New in version 1.4.0.



# pyspark.sql.Column.between — PySpark 4.0.1 documentation
Column.between(_lowerBound_, _upperBound_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.between)
[#](#pyspark.sql.Column.between "Permalink to this definition")

Check if the current column’s values are between the specified lower and upper bounds, inclusive.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**lowerBound**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), int, float, string, bool, datetime, date or Decimal

The lower boundary value, inclusive.

**upperBound**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), int, float, string, bool, datetime, date or Decimal

The upper boundary value, inclusive.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of boolean values indicating whether each element in the original column is within the specified range (inclusive).

Examples

Using between with integer values.

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.select(df.name, df.age.between(2, 4)).show()
+-----+---------------------------+
| name|((age >= 2) AND (age <= 4))|
+-----+---------------------------+
|Alice|                       true|
|  Bob|                      false|
+-----+---------------------------+

```


Using between with string values.

```
>>> df = spark.createDataFrame([("Alice", "A"), ("Bob", "B")], ["name", "initial"])
>>> df.select(df.name, df.initial.between("A", "B")).show()
+-----+-----------------------------------+
| name|((initial >= A) AND (initial <= B))|
+-----+-----------------------------------+
|Alice|                               true|
|  Bob|                               true|
+-----+-----------------------------------+

```


Using between with float values.

```
>>> df = spark.createDataFrame(
...     [(2.5, "Alice"), (5.5, "Bob")], ["height", "name"])
>>> df.select(df.name, df.height.between(2.0, 5.0)).show()
+-----+-------------------------------------+
| name|((height >= 2.0) AND (height <= 5.0))|
+-----+-------------------------------------+
|Alice|                                 true|
|  Bob|                                false|
+-----+-------------------------------------+

```


Using between with date values.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [("Alice", "2023-01-01"), ("Bob", "2023-02-01")], ["name", "date"])
>>> df = df.withColumn("date", sf.to_date(df.date))
>>> df.select(df.name, df.date.between("2023-01-01", "2023-01-15")).show()
+-----+-----------------------------------------------+
| name|((date >= 2023-01-01) AND (date <= 2023-01-15))|
+-----+-----------------------------------------------+
|Alice|                                           true|
|  Bob|                                          false|
+-----+-----------------------------------------------+
>>> from datetime import date
>>> df.select(df.name, df.date.between(date(2023, 1, 1), date(2023, 1, 15))).show()
+-----+-------------------------------------------------------------+
| name|((date >= DATE '2023-01-01') AND (date <= DATE '2023-01-15'))|
+-----+-------------------------------------------------------------+
|Alice|                                                         true|
|  Bob|                                                        false|
+-----+-------------------------------------------------------------+

```


Using between with timestamp values.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [("Alice", "2023-01-01 10:00:00"), ("Bob", "2023-02-01 10:00:00")],
...     schema=["name", "timestamp"])
>>> df = df.withColumn("timestamp", sf.to_timestamp(df.timestamp))
>>> df.select(df.name, df.timestamp.between("2023-01-01", "2023-02-01")).show()
+-----+---------------------------------------------------------+
| name|((timestamp >= 2023-01-01) AND (timestamp <= 2023-02-01))|
+-----+---------------------------------------------------------+
|Alice|                                                     true|
|  Bob|                                                    false|
+-----+---------------------------------------------------------+
>>> df.select(df.name, df.timestamp.between("2023-01-01", "2023-02-01 12:00:00")).show()
+-----+------------------------------------------------------------------+
| name|((timestamp >= 2023-01-01) AND (timestamp <= 2023-02-01 12:00:00))|
+-----+------------------------------------------------------------------+
|Alice|                                                              true|
|  Bob|                                                              true|
+-----+------------------------------------------------------------------+

```


# pyspark.sql.Column.bitwiseAND — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.bitwiseAND

Column.bitwiseAND(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.bitwiseAND)
[#](#pyspark.sql.Column.bitwiseAND "Permalink to this definition")

Compute bitwise AND of this expression with another expression.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**

a value or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") to calculate bitwise and(&) with this [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(a=170, b=75)])
>>> df.select(df.a.bitwiseAND(df.b)).collect()
[Row((a & b)=10)]

```


# pyspark.sql.Column.bitwiseOR — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.bitwiseOR

Column.bitwiseOR(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.bitwiseOR)
[#](#pyspark.sql.Column.bitwiseOR "Permalink to this definition")

” Compute bitwise OR of this expression with another expression.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**

a value or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") to calculate bitwise or(|) with this [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(a=170, b=75)])
>>> df.select(df.a.bitwiseOR(df.b)).collect()
[Row((a | b)=235)]

```


# pyspark.sql.Column.bitwiseXOR — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.bitwiseXOR

Column.bitwiseXOR(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.bitwiseXOR)
[#](#pyspark.sql.Column.bitwiseXOR "Permalink to this definition")

Compute bitwise XOR of this expression with another expression.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**

a value or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") to calculate bitwise xor(^) with this [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(a=170, b=75)])
>>> df.select(df.a.bitwiseXOR(df.b)).collect()
[Row((a ^ b)=225)]

```


# pyspark.sql.Column.cast — PySpark 4.0.1 documentation
Column.cast(_dataType_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.cast)
[#](#pyspark.sql.Column.cast "Permalink to this definition")

Casts the column into type `dataType`.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**dataType**`DataType` or str

a DataType or Python string literal with a DDL-formatted string to use when parsing the column to the same type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column is cast into new type.

Examples

```
>>> from pyspark.sql.types import StringType
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.select(df.age.cast("string").alias('ages')).collect()
[Row(ages='2'), Row(ages='5')]
>>> df.select(df.age.cast(StringType()).alias('ages')).collect()
[Row(ages='2'), Row(ages='5')]

```


# pyspark.sql.Column.contains — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.contains

Column.contains(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.contains)
[#](#pyspark.sql.Column.contains "Permalink to this definition")

Contains the other element. Returns a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on a string match.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**

string in line. A value as a literal or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column").

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.filter(df.name.contains('o')).collect()
[Row(age=5, name='Bob')]

```


# pyspark.sql.Column.desc — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.desc

Column.desc()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.desc)
[#](#pyspark.sql.Column.desc "Permalink to this definition")

Returns a sort expression based on the descending order of the column.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([('Tom', 80), ('Alice', None)], ["name", "height"])
>>> df.select(df.name).orderBy(df.name.desc()).collect()
[Row(name='Tom'), Row(name='Alice')]

```


# pyspark.sql.Column.desc_nulls_first — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.desc\_nulls\_first

Column.desc\_nulls\_first()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.desc_nulls_first)
[#](#pyspark.sql.Column.desc_nulls_first "Permalink to this definition")

Returns a sort expression based on the descending order of the column, and null values appear before non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame(
...     [('Tom', 80), (None, 60), ('Alice', None)], ["name", "height"])
>>> df.select(df.name).orderBy(df.name.desc_nulls_first()).collect()
[Row(name=None), Row(name='Tom'), Row(name='Alice')]

```


# pyspark.sql.Column.desc_nulls_last — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.desc\_nulls\_last

Column.desc\_nulls\_last()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.desc_nulls_last)
[#](#pyspark.sql.Column.desc_nulls_last "Permalink to this definition")

Returns a sort expression based on the descending order of the column, and null values appear after non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame(
...     [('Tom', 80), (None, 60), ('Alice', None)], ["name", "height"])
>>> df.select(df.name).orderBy(df.name.desc_nulls_last()).collect()
[Row(name='Tom'), Row(name='Alice'), Row(name=None)]

```


# pyspark.sql.Column.dropFields — PySpark 4.0.1 documentation
Column.dropFields(_\*fieldNames_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.dropFields)
[#](#pyspark.sql.Column.dropFields "Permalink to this definition")

An expression that drops fields in `StructType` by name. This is a no-op if the schema doesn’t contain field name(s).

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**fieldNames**str

Desired field names (collects all positional arguments passed) The result will drop at a location if any field matches in the Column.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column with field dropped by fieldName.

Examples

```
>>> from pyspark.sql import Row
>>> from pyspark.sql.functions import col, lit
>>> df = spark.createDataFrame([
...     Row(a=Row(b=1, c=2, d=3, e=Row(f=4, g=5, h=6)))])
>>> df.withColumn('a', df['a'].dropFields('b')).show()
+-----------------+
|                a|
+-----------------+
|{2, 3, {4, 5, 6}}|
+-----------------+

```


```
>>> df.withColumn('a', df['a'].dropFields('b', 'c')).show()
+--------------+
|             a|
+--------------+
|{3, {4, 5, 6}}|
+--------------+

```


This method supports dropping multiple nested fields directly e.g.

```
>>> df.withColumn("a", col("a").dropFields("e.g", "e.h")).show()
+--------------+
|             a|
+--------------+
|{1, 2, 3, {4}}|
+--------------+

```


However, if you are going to add/replace multiple nested fields, it is preferred to extract out the nested struct before adding/replacing multiple fields e.g.

```
>>> df.select(col("a").withField(
...     "e", col("a.e").dropFields("g", "h")).alias("a")
... ).show()
+--------------+
|             a|
+--------------+
|{1, 2, 3, {4}}|
+--------------+

```

# pyspark.sql.Column.endswith — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.endswith

Column.endswith(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.endswith)
[#](#pyspark.sql.Column.endswith "Permalink to this definition")

String ends with. Returns a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on a string match.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

string at end of line (do not use a regex $)

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.filter(df.name.endswith('ice')).collect()
[Row(age=2, name='Alice')]
>>> df.filter(df.name.endswith('ice)).collect()
[]

```


# pyspark.sql.Column.eqNullSafe — PySpark 4.0.1 documentation
Column.eqNullSafe(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.eqNullSafe)
[#](#pyspark.sql.Column.eqNullSafe "Permalink to this definition")

Equality test that is safe for null values.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**

a value or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Notes

Unlike Pandas, PySpark doesn’t consider NaN values to be NULL. See the [NaN Semantics](https://spark.apache.org/docs/latest/sql-ref-datatypes.html#nan-semantics) for details.

Examples

```
>>> from pyspark.sql import Row
>>> df1 = spark.createDataFrame([
...     Row(id=1, value='foo'),
...     Row(id=2, value=None)
... ])
>>> df1.select(
...     df1['value'] == 'foo',
...     df1['value'].eqNullSafe('foo'),
...     df1['value'].eqNullSafe(None)
... ).show()
+-------------+---------------+----------------+
|(value = foo)|(value <=> foo)|(value <=> NULL)|
+-------------+---------------+----------------+
|         true|           true|           false|
|         NULL|          false|            true|
+-------------+---------------+----------------+
>>> df2 = spark.createDataFrame([
...     Row(value = 'bar'),
...     Row(value = None)
... ])
>>> df1.join(df2, df1["value"] == df2["value"]).count()
0
>>> df1.join(df2, df1["value"].eqNullSafe(df2["value"])).count()
1
>>> df2 = spark.createDataFrame([
...     Row(id=1, value=float('NaN')),
...     Row(id=2, value=42.0),
...     Row(id=3, value=None)
... ])
>>> df2.select(
...     df2['value'].eqNullSafe(None),
...     df2['value'].eqNullSafe(float('NaN')),
...     df2['value'].eqNullSafe(42.0)
... ).show()
+----------------+---------------+----------------+
|(value <=> NULL)|(value <=> NaN)|(value <=> 42.0)|
+----------------+---------------+----------------+
|           false|           true|           false|
|           false|          false|            true|
|            true|          false|           false|
+----------------+---------------+----------------+

```


# pyspark.sql.Column.getField — PySpark 4.0.1 documentation
Column.getField(_name_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.getField)
[#](#pyspark.sql.Column.getField "Permalink to this definition")

An expression that gets a field by name in a `StructType`.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**name**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression. The result will only be true at a location if the field matches in the Column.

> Deprecated since version 3.0.0: [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") as a parameter is deprecated.

**Returns**

**——-**

**:class:\`Column\`**

Column representing whether each element of Column got by name.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(r=Row(a=1, b="b"))])
>>> df.select(df.r.getField("b")).show()
+---+
|r.b|
+---+
|  b|
+---+
>>> df.select(df.r.a).show()
+---+
|r.a|
+---+
|  1|
+---+

```
# pyspark.sql.Column.getItem — PySpark 4.0.1 documentation
Column.getItem(_key_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.getItem)
[#](#pyspark.sql.Column.getItem "Permalink to this definition")

An expression that gets an item at position `ordinal` out of a list, or gets an item by key out of a dict.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**key**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression. The result will only be true at a location if the item matches in the column.

> Deprecated since version 3.0.0: [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") as a parameter is deprecated.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing the item(s) got at position out of a list or by key out of a dict.

Examples

```
>>> df = spark.createDataFrame([([1, 2], {"key": "value"})], ["l", "d"])
>>> df.select(df.l.getItem(0), df.d.getItem("key")).show()
+----+------+
|l[0]|d[key]|
+----+------+
|   1| value|
+----+------+

```


# pyspark.sql.Column.ilike — PySpark 4.0.1 documentation
Column.ilike(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.ilike)
[#](#pyspark.sql.Column.ilike "Permalink to this definition")

SQL ILIKE expression (case insensitive LIKE). Returns a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on a case insensitive match.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**str

a SQL LIKE pattern

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column of booleans showing whether each element in the Column is matched by SQL LIKE pattern.

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.filter(df.name.ilike('%Ice')).collect()
[Row(age=2, name='Alice')]

```

# pyspark.sql.Column.isNaN — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.isNaN

Column.isNaN()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.isNaN)
[#](#pyspark.sql.Column.isNaN "Permalink to this definition")

True if the current expression is NaN.

New in version 4.0.0.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame(
...     [Row(name='Tom', height=80.0), Row(name='Alice', height=float('nan'))])
>>> df.filter(df.height.isNaN()).collect()
[Row(name='Alice', height=nan)]

```



# pyspark.sql.Column.isNotNull — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.isNotNull

Column.isNotNull()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.isNotNull)
[#](#pyspark.sql.Column.isNotNull "Permalink to this definition")

True if the current expression is NOT null.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(name='Tom', height=80), Row(name='Alice', height=None)])
>>> df.filter(df.height.isNotNull()).collect()
[Row(name='Tom', height=80)]

```




# pyspark.sql.Column.isNull — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.isNull

Column.isNull()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.isNull)
[#](#pyspark.sql.Column.isNull "Permalink to this definition")

True if the current expression is null.

Changed in version 3.4.0: Supports Spark Connect.

Examples

```
>>> from pyspark.sql import Row
>>> df = spark.createDataFrame([Row(name='Tom', height=80), Row(name='Alice', height=None)])
>>> df.filter(df.height.isNull()).collect()
[Row(name='Alice', height=None)]

```


# pyspark.sql.Column.isin — PySpark 4.0.1 documentation
Column.isin(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.isin)
[#](#pyspark.sql.Column.isin "Permalink to this definition")

A boolean expression that is evaluated to true if the value of this expression is contained by the evaluated values of the arguments.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**Any

The values to compare with the column values. The result will only be true at a location if any value matches in the Column.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column of booleans showing whether each element in the Column is contained in cols.

Examples

```
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob"), (8, "Mike")], ["age", "name"])

```


Example 1: Filter rows with names in the specified values

```
>>> df[df.name.isin("Bob", "Mike")].show()
+---+----+
|age|name|
+---+----+
|  5| Bob|
|  8|Mike|
+---+----+

```


Example 2: Filter rows with ages in the specified list

```
>>> df[df.age.isin([1, 2, 3])].show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
+---+-----+

```


Example 3: Filter rows with names not in the specified values

```
>>> df[~df.name.isin("Alice", "Bob")].show()
+---+----+
|age|name|
+---+----+
|  8|Mike|
+---+----+

```


# pyspark.sql.Column.like — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.like

Column.like(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.like)
[#](#pyspark.sql.Column.like "Permalink to this definition")

SQL like expression. Returns a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on a SQL LIKE match.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**str

a SQL LIKE pattern

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column of booleans showing whether each element in the Column is matched by SQL LIKE pattern.

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.filter(df.name.like('Al%')).collect()
[Row(age=2, name='Alice')]

```


# pyspark.sql.Column.name — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.name

Column.name(_\*alias_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.name)
[#](#pyspark.sql.Column.name "Permalink to this definition")

[`name()`](#pyspark.sql.Column.name "pyspark.sql.Column.name") is an alias for [`alias()`](about:blank/pyspark.sql.Column.alias.html#pyspark.sql.Column.alias "pyspark.sql.Column.alias").

New in version 2.0.0.


# pyspark.sql.Column.otherwise — PySpark 4.0.1 documentation
Column.otherwise(_value_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.otherwise)
[#](#pyspark.sql.Column.otherwise "Permalink to this definition")

Evaluates a list of conditions and returns one of multiple possible result expressions. If [`Column.otherwise()`](#pyspark.sql.Column.otherwise "pyspark.sql.Column.otherwise") is not invoked, None is returned for unmatched conditions.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**value**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column is unmatched conditions.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.select(df.name, sf.when(df.age > 3, 1).otherwise(0)).show()
+-----+-------------------------------------+
| name|CASE WHEN (age > 3) THEN 1 ELSE 0 END|
+-----+-------------------------------------+
|Alice|                                    0|
|  Bob|                                    1|
+-----+-------------------------------------+

```


# pyspark.sql.Column.outer — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.outer

Column.outer()
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.outer)
[#](#pyspark.sql.Column.outer "Permalink to this definition")

Mark this column as an outer column if its expression refers to columns from an outer query.

This is used to trigger lazy analysis of Spark Classic DataFrame, so that we can use it to build subquery expressions. Spark Connect DataFrame is always lazily analyzed and does not need to use this function.

New in version 4.0.0.

See also

`pyspark.sql.dataframe.DataFrame.scalar`

`pyspark.sql.dataframe.DataFrame.exists`

# pyspark.sql.Column.over — PySpark 4.0.1 documentation
Column.over(_window_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.over)
[#](#pyspark.sql.Column.over "Permalink to this definition")

Define a windowing column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**window**`WindowSpec`

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Examples

```
>>> from pyspark.sql import Window
>>> window = (
...     Window.partitionBy("name")
...     .orderBy("age")
...     .rowsBetween(Window.unboundedPreceding, Window.currentRow)
... )
>>> from pyspark.sql.functions import rank, min, desc
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.withColumn(
...      "rank", rank().over(window)
... ).withColumn(
...      "min", min('age').over(window)
... ).sort(desc("age")).show()
+---+-----+----+---+
|age| name|rank|min|
+---+-----+----+---+
|  5|  Bob|   1|  5|
|  2|Alice|   1|  2|
+---+-----+----+---+

```

# pyspark.sql.Column.rlike — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.rlike

Column.rlike(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.rlike)
[#](#pyspark.sql.Column.rlike "Permalink to this definition")

SQL RLIKE expression (LIKE with Regex). Returns a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on a regex match.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**str

an extended regex expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column of booleans showing whether each element in the Column is matched by extended regex expression.

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.filter(df.name.rlike('ice)).collect()
[Row(age=2, name='Alice')]

```

# pyspark.sql.Column.startswith — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Column](../column.html)
*   pyspark.sql.Column.startswith

Column.startswith(_other_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.startswith)
[#](#pyspark.sql.Column.startswith "Permalink to this definition")

String starts with. Returns a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on a string match.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**other**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

string at start of line (do not use a regex ^)

Examples

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.filter(df.name.startswith('Al')).collect()
[Row(age=2, name='Alice')]
>>> df.filter(df.name.startswith('^Al')).collect()
[]

```



# pyspark.sql.Column.substr — PySpark 4.0.1 documentation
Column.substr(_startPos_, _length_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.substr)
[#](#pyspark.sql.Column.substr "Permalink to this definition")

Return a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") which is a substring of the column.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**startPos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

start position

**length**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

length of the substring

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column is substr of origin Column.

Examples

Example 1. Using integers for the input arguments.

```
>>> df = spark.createDataFrame(
...      [(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> df.select(df.name.substr(1, 3).alias("col")).collect()
[Row(col='Ali'), Row(col='Bob')]

```


Example 2. Using columns for the input arguments.

```
>>> df = spark.createDataFrame(
...      [(3, 4, "Alice"), (2, 3, "Bob")], ["sidx", "eidx", "name"])
>>> df.select(df.name.substr(df.sidx, df.eidx).alias("col")).collect()
[Row(col='ice'), Row(col='ob')]

```


# pyspark.sql.Column.try_cast — PySpark 4.0.1 documentation
Column.try\_cast(_dataType_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.try_cast)
[#](#pyspark.sql.Column.try_cast "Permalink to this definition")

This is a special version of cast that performs the same operation, but returns a NULL value instead of raising an error if the invoke method throws exception.

New in version 4.0.0.

Parameters

**dataType**`DataType` or str

a DataType or Python string literal with a DDL-formatted string to use when parsing the column to the same type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column is cast into new type.

Examples

Example 1: Cast with a Datatype

```
>>> from pyspark.sql.types import LongType
>>> df = spark.createDataFrame(
...      [(2, "123"), (5, "Bob"), (3, None)], ["age", "name"])
>>> df.select(df.name.try_cast(LongType())).show()
+----+
|name|
+----+
| 123|
|NULL|
|NULL|
+----+

```


Example 2: Cast with a DDL string

```
>>> df = spark.createDataFrame(
...      [(2, "123"), (5, "Bob"), (3, None)], ["age", "name"])
>>> df.select(df.name.try_cast("double")).show()
+-----+
| name|
+-----+
|123.0|
| NULL|
| NULL|
+-----+

```


# pyspark.sql.Column.when — PySpark 4.0.1 documentation
Column.when(_condition_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.when)
[#](#pyspark.sql.Column.when "Permalink to this definition")

Evaluates a list of conditions and returns one of multiple possible result expressions. If [`Column.otherwise()`](about:blank/pyspark.sql.Column.otherwise.html#pyspark.sql.Column.otherwise "pyspark.sql.Column.otherwise") is not invoked, None is returned for unmatched conditions.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**condition**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

**value**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column is in conditions.

Examples

Example 1: Using [`when()`](#pyspark.sql.Column.when "pyspark.sql.Column.when") with conditions and values to create a new Column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> result = df.select(df.name, sf.when(df.age > 4, 1).when(df.age < 3, -1).otherwise(0))
>>> result.show()
+-----+------------------------------------------------------------+
| name|CASE WHEN (age > 4) THEN 1 WHEN (age < 3) THEN -1 ELSE 0 END|
+-----+------------------------------------------------------------+
|Alice|                                                          -1|
|  Bob|                                                           1|
+-----+------------------------------------------------------------+

```


Example 2: Chaining multiple [`when()`](#pyspark.sql.Column.when "pyspark.sql.Column.when") conditions

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "Alice"), (4, "Bob"), (6, "Charlie")], ["age", "name"])
>>> result = df.select(
...     df.name,
...     sf.when(df.age < 3, "Young").when(df.age < 5, "Middle-aged").otherwise("Old")
... )
>>> result.show()
+-------+---------------------------------------------------------------------------+
|   name|CASE WHEN (age < 3) THEN Young WHEN (age < 5) THEN Middle-aged ELSE Old END|
+-------+---------------------------------------------------------------------------+
|  Alice|                                                                      Young|
|    Bob|                                                                Middle-aged|
|Charlie|                                                                        Old|
+-------+---------------------------------------------------------------------------+

```


Example 3: Using literal values as conditions

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2, "Alice"), (5, "Bob")], ["age", "name"])
>>> result = df.select(
...     df.name, sf.when(sf.lit(True), 1).otherwise(
...         sf.raise_error("unreachable")).alias("when"))
>>> result.show()
+-----+----+
| name|when|
+-----+----+
|Alice|   1|
|  Bob|   1|
+-----+----+

```


# pyspark.sql.Column.withField — PySpark 4.0.1 documentation
Column.withField(_fieldName_, _col_)
[\[source\]](about:blank/_modules/pyspark/sql/column.html#Column.withField)
[#](#pyspark.sql.Column.withField "Permalink to this definition")

An expression that adds/replaces a field in `StructType` by name.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**fieldName**str

a literal value. The result will only be true at a location if any field matches in the Column.

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression for the column with fieldName.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column representing whether each element of Column which field was added/replaced by fieldName.

Examples

```
>>> from pyspark.sql import Row
>>> from pyspark.sql.functions import lit
>>> df = spark.createDataFrame([Row(a=Row(b=1, c=2))])
>>> df.withColumn('a', df['a'].withField('b', lit(3))).select('a.b').show()
+---+
|  b|
+---+
|  3|
+---+
>>> df.withColumn('a', df['a'].withField('d', lit(4))).select('a.d').show()
+---+
|  d|
+---+
|  4|
+---+

```

