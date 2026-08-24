# Window — PySpark 4.0.1 documentation


* Window.currentRow: Window.orderBy(*cols)
  * Creates a WindowSpec with the ordering defined.
* Window.currentRow: Window.partitionBy(*cols)
  * Creates a WindowSpec with the partitioning defined.
* Window.currentRow: Window.rangeBetween(start, end)
  * Creates a WindowSpec with the frame boundaries defined, from start (inclusive) to end (inclusive).
* Window.currentRow: Window.rowsBetween(start, end)
  * Creates a WindowSpec with the frame boundaries defined, from start (inclusive) to end (inclusive).
* Window.currentRow: Window.unboundedFollowing
* Window.currentRow: Window.unboundedPreceding
* Window.currentRow: WindowSpec.orderBy(*cols)
  * Defines the ordering columns in a WindowSpec.
* Window.currentRow: WindowSpec.partitionBy(*cols)
  * Defines the partitioning columns in a WindowSpec.
* Window.currentRow: WindowSpec.rangeBetween(start, end)
  * Defines the frame boundaries, from start (inclusive) to end (inclusive).
* Window.currentRow: WindowSpec.rowsBetween(start, end)
  * Defines the frame boundaries, from start (inclusive) to end (inclusive).


# pyspark.sql.Window.currentRow — PySpark 4.0.1 documentation

Window.currentRow = 0

next

pyspark.sql.Window.orderBy


# pyspark.sql.Window.orderBy — PySpark 4.0.1 documentation
_static_ Window.orderBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#Window.orderBy)
[#](#pyspark.sql.Window.orderBy "Permalink to this definition")

Creates a `WindowSpec` with the ordering defined.

New in version 1.4.0.

Parameters

**cols**str, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or list

names of columns or expressions

Returns

class

WindowSpec A `WindowSpec` with the ordering defined.

Examples

```
>>> from pyspark.sql import Window
>>> from pyspark.sql.functions import row_number
>>> df = spark.createDataFrame(
...      [(1, "a"), (1, "a"), (2, "a"), (1, "b"), (2, "b"), (3, "b")], ["id", "category"])
>>> df.show()
+---+--------+
| id|category|
+---+--------+
|  1|       a|
|  1|       a|
|  2|       a|
|  1|       b|
|  2|       b|
|  3|       b|
+---+--------+

```


Show row number order by `category` in partition `id`.

```
>>> window = Window.partitionBy("id").orderBy("category")
>>> df.withColumn("row_number", row_number().over(window)).show()
+---+--------+----------+
| id|category|row_number|
+---+--------+----------+
|  1|       a|         1|
|  1|       a|         2|
|  1|       b|         3|
|  2|       a|         1|
|  2|       b|         2|
|  3|       b|         1|
+---+--------+----------+

```
# pyspark.sql.Window.partitionBy — PySpark 4.0.1 documentation
_static_ Window.partitionBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#Window.partitionBy)
[#](#pyspark.sql.Window.partitionBy "Permalink to this definition")

Creates a `WindowSpec` with the partitioning defined.

New in version 1.4.0.

Parameters

**cols**str, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or list

names of columns or expressions

Returns

class

WindowSpec A `WindowSpec` with the partitioning defined.

Examples

```
>>> from pyspark.sql import Window
>>> from pyspark.sql.functions import row_number
>>> df = spark.createDataFrame(
...      [(1, "a"), (1, "a"), (2, "a"), (1, "b"), (2, "b"), (3, "b")], ["id", "category"])
>>> df.show()
+---+--------+
| id|category|
+---+--------+
|  1|       a|
|  1|       a|
|  2|       a|
|  1|       b|
|  2|       b|
|  3|       b|
+---+--------+

```


Show row number order by `id` in partition `category`.

```
>>> window = Window.partitionBy("category").orderBy("id")
>>> df.withColumn("row_number", row_number().over(window)).show()
+---+--------+----------+
| id|category|row_number|
+---+--------+----------+
|  1|       a|         1|
|  1|       a|         2|
|  2|       a|         3|
|  1|       b|         1|
|  2|       b|         2|
|  3|       b|         3|
+---+--------+----------+

```



# pyspark.sql.Window.rangeBetween — PySpark 4.0.1 documentation
_static_ Window.rangeBetween(_start_, _end_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#Window.rangeBetween)
[#](#pyspark.sql.Window.rangeBetween "Permalink to this definition")

Creates a `WindowSpec` with the frame boundaries defined, from start (inclusive) to end (inclusive).

Both start and end are relative from the current row. For example, “0” means “current row”, while “-1” means one off before the current row, and “5” means the five off after the current row.

We recommend users use `Window.unboundedPreceding`, `Window.unboundedFollowing`, and `Window.currentRow` to specify special boundary values, rather than using integral values directly.

A range-based boundary is based on the actual value of the ORDER BY expression(s). An offset is used to alter the value of the ORDER BY expression, for instance if the current ORDER BY expression has a value of 10 and the lower bound offset is -3, the resulting lower bound for the current row will be 10 - 3 = 7. This however puts a number of constraints on the ORDER BY expressions: there can be only one expression and this expression must have a numerical data type. An exception can be made when the offset is unbounded, because no value modification is needed, in this case multiple and non-numeric ORDER BY expression are allowed.

New in version 2.1.0.

Parameters

**start**int

boundary start, inclusive. The frame is unbounded if this is `Window.unboundedPreceding`, or any value less than or equal to max(-sys.maxsize, -9223372036854775808).

**end**int

boundary end, inclusive. The frame is unbounded if this is `Window.unboundedFollowing`, or any value greater than or equal to min(sys.maxsize, 9223372036854775807).

Returns

class

WindowSpec A `WindowSpec` with the frame boundaries defined, from start (inclusive) to end (inclusive).

Examples

```
>>> from pyspark.sql import Window
>>> from pyspark.sql import functions as func
>>> df = spark.createDataFrame(
...      [(1, "a"), (1, "a"), (2, "a"), (1, "b"), (2, "b"), (3, "b")], ["id", "category"])
>>> df.show()
+---+--------+
| id|category|
+---+--------+
|  1|       a|
|  1|       a|
|  2|       a|
|  1|       b|
|  2|       b|
|  3|       b|
+---+--------+

```


Calculate sum of `id` in the range from `id` of currentRow to `id` of currentRow + 1 in partition `category`

```
>>> window = Window.partitionBy("category").orderBy("id").rangeBetween(Window.currentRow, 1)
>>> df.withColumn("sum", func.sum("id").over(window)).sort("id", "category").show()
+---+--------+---+
| id|category|sum|
+---+--------+---+
|  1|       a|  4|
|  1|       a|  4|
|  1|       b|  3|
|  2|       a|  2|
|  2|       b|  5|
|  3|       b|  3|
+---+--------+---+

```


# pyspark.sql.Window.rowsBetween — PySpark 4.0.1 documentation
_static_ Window.rowsBetween(_start_, _end_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#Window.rowsBetween)
[#](#pyspark.sql.Window.rowsBetween "Permalink to this definition")

Creates a `WindowSpec` with the frame boundaries defined, from start (inclusive) to end (inclusive).

Both start and end are relative positions from the current row. For example, “0” means “current row”, while “-1” means the row before the current row, and “5” means the fifth row after the current row.

We recommend users use `Window.unboundedPreceding`, `Window.unboundedFollowing`, and `Window.currentRow` to specify special boundary values, rather than using integral values directly.

A row based boundary is based on the position of the row within the partition. An offset indicates the number of rows above or below the current row, the frame for the current row starts or ends. For instance, given a row based sliding frame with a lower bound offset of -1 and a upper bound offset of +2. The frame for row with index 5 would range from index 4 to index 7.

New in version 2.1.0.

Parameters

**start**int

boundary start, inclusive. The frame is unbounded if this is `Window.unboundedPreceding`, or any value less than or equal to -9223372036854775808.

**end**int

boundary end, inclusive. The frame is unbounded if this is `Window.unboundedFollowing`, or any value greater than or equal to 9223372036854775807.

Returns

class

WindowSpec A `WindowSpec` with the frame boundaries defined, from start (inclusive) to end (inclusive).

Examples

```
>>> from pyspark.sql import Window
>>> from pyspark.sql import functions as func
>>> df = spark.createDataFrame(
...      [(1, "a"), (1, "a"), (2, "a"), (1, "b"), (2, "b"), (3, "b")], ["id", "category"])
>>> df.show()
+---+--------+
| id|category|
+---+--------+
|  1|       a|
|  1|       a|
|  2|       a|
|  1|       b|
|  2|       b|
|  3|       b|
+---+--------+

```


Calculate sum of `id` in the range from currentRow to currentRow + 1 in partition `category`

```
>>> window = Window.partitionBy("category").orderBy("id").rowsBetween(Window.currentRow, 1)
>>> df.withColumn("sum", func.sum("id").over(window)).sort("id", "category", "sum").show()
+---+--------+---+
| id|category|sum|
+---+--------+---+
|  1|       a|  2|
|  1|       a|  3|
|  1|       b|  3|
|  2|       a|  2|
|  2|       b|  5|
|  3|       b|  3|
+---+--------+---+

```


# pyspark.sql.Window.unboundedFollowing — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Window](../window.html)
*   pyspark.sql.Window.unboundedFollowing

Window.unboundedFollowing _\= 9223372036854775807_[#](#pyspark.sql.Window.unboundedFollowing "Permalink to this definition")

# pyspark.sql.Window.unboundedPreceding — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Window](../window.html)
*   pyspark.sql.Window.unboundedPreceding

Window.unboundedPreceding _\= \-9223372036854775808_[#](#pyspark.sql.Window.unboundedPreceding "Permalink to this definition")

# pyspark.sql.WindowSpec.orderBy — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Window](../window.html)
*   pyspark.sql.WindowSpec.orderBy

WindowSpec.orderBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#WindowSpec.orderBy)
[#](#pyspark.sql.WindowSpec.orderBy "Permalink to this definition")

Defines the ordering columns in a `WindowSpec`.

New in version 1.4.0.

Parameters

**cols**str, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or list

names of columns or expressions

# pyspark.sql.WindowSpec.partitionBy — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Window](../window.html)
*   pyspark.sql.WindowSpec.partitionBy

WindowSpec.partitionBy(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#WindowSpec.partitionBy)
[#](#pyspark.sql.WindowSpec.partitionBy "Permalink to this definition")

Defines the partitioning columns in a `WindowSpec`.

New in version 1.4.0.

Parameters

**cols**str, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or list

names of columns or expressions

# pyspark.sql.WindowSpec.rangeBetween — PySpark 4.0.1 documentation
WindowSpec.rangeBetween(_start_, _end_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#WindowSpec.rangeBetween)
[#](#pyspark.sql.WindowSpec.rangeBetween "Permalink to this definition")

Defines the frame boundaries, from start (inclusive) to end (inclusive).

Both start and end are relative from the current row. For example, “0” means “current row”, while “-1” means one off before the current row, and “5” means the five off after the current row.

We recommend users use `Window.unboundedPreceding`, `Window.unboundedFollowing`, and `Window.currentRow` to specify special boundary values, rather than using integral values directly.

New in version 1.4.0.

Parameters

**start**int

boundary start, inclusive. The frame is unbounded if this is `Window.unboundedPreceding`, or any value less than or equal to max(-sys.maxsize, -9223372036854775808).

**end**int

boundary end, inclusive. The frame is unbounded if this is `Window.unboundedFollowing`, or any value greater than or equal to min(sys.maxsize, 9223372036854775807).

# pyspark.sql.WindowSpec.rowsBetween — PySpark 4.0.1 documentation
WindowSpec.rowsBetween(_start_, _end_)
[\[source\]](about:blank/_modules/pyspark/sql/window.html#WindowSpec.rowsBetween)
[#](#pyspark.sql.WindowSpec.rowsBetween "Permalink to this definition")

Defines the frame boundaries, from start (inclusive) to end (inclusive).

Both start and end are relative positions from the current row. For example, “0” means “current row”, while “-1” means the row before the current row, and “5” means the fifth row after the current row.

We recommend users use `Window.unboundedPreceding`, `Window.unboundedFollowing`, and `Window.currentRow` to specify special boundary values, rather than using integral values directly.

New in version 1.4.0.

Parameters

**start**int

boundary start, inclusive. The frame is unbounded if this is `Window.unboundedPreceding`, or any value less than or equal to max(-sys.maxsize, -9223372036854775808).

**end**int

boundary end, inclusive. The frame is unbounded if this is `Window.unboundedFollowing`, or any value greater than or equal to min(sys.maxsize, 9223372036854775807).