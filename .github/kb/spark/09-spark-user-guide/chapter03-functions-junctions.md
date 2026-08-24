# Chapter 3: Function Junction - Data manipulation with PySpark — PySpark 4.0.1 documentation
Clean data[#](#Clean-data "Permalink to this headline")
-------------------------------------------------------

In data science, `garbage in, garbage out` (GIGO) is the concept that flawed, biased or poor quality information or input produces a result or output of similar quality. To improve the analysis quality, we need data cleaning, the process to turn garbage into gold, it is composed of identifying, correcting, or removing errors and inconsistencies in data to improve its quality and usability.

Let’s start with a Dataframe containing bad values:

```
!pip install pyspark==4.0.0.dev2

```


```
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Data Loading and Storage Example") \
    .getOrCreate()

```


```
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(age=10, height=80.0, NAME="Alice"),
    Row(age=10, height=80.0, NAME="Alice"),
    Row(age=5, height=float("nan"), NAME="BOB"),
    Row(age=None, height=None, NAME="Tom"),
    Row(age=None, height=float("nan"), NAME=None),
    Row(age=9, height=78.9, NAME="josh"),
    Row(age=18, height=1802.3, NAME="bush"),
    Row(age=7, height=75.3, NAME="jerry"),
])

df.show()

```


```
+----+------+-----+
| age|height| NAME|
+----+------+-----+
|  10|  80.0|Alice|
|  10|  80.0|Alice|
|   5|   NaN|  BOB|
|NULL|  NULL|  Tom|
|NULL|   NaN| NULL|
|   9|  78.9| josh|
|  18|1802.3| bush|
|   7|  75.3|jerry|
+----+------+-----+


```


### Rename columns[#](#Rename-columns "Permalink to this headline")

At first glance, we find that column `NAME` is upper case. For consistency, we can use `DataFrame.withColumnRenamed` to rename columns.

```
df2 = df.withColumnRenamed("NAME", "name")

df2.show()

```


```
+----+------+-----+
| age|height| name|
+----+------+-----+
|  10|  80.0|Alice|
|  10|  80.0|Alice|
|   5|   NaN|  BOB|
|NULL|  NULL|  Tom|
|NULL|   NaN| NULL|
|   9|  78.9| josh|
|  18|1802.3| bush|
|   7|  75.3|jerry|
+----+------+-----+


```


### Drop null values[#](#Drop-null-values "Permalink to this headline")

Then we can notice that there are two kinds of missing data:

*   the `NULL` values in all three columns;
    
*   the `NaN` values which means `Not a Number` for a numeric column;
    

The records without a valid `name` are likely useless, so let’s drop them first. There are a group of functions in `DataFrameNaFunctions` for missing value handling, we can use `DataFrame.na.drop` or `DataFrame.dropna` to omit rows with `NULL` or `NaN` values.

After the step `df2.na.drop(subset="name")`, invalid record `(age=None, height=NaN, name=None)` is discarded.

```
df3 = df2.na.drop(subset="name")

df3.show()

```


```
+----+------+-----+
| age|height| name|
+----+------+-----+
|  10|  80.0|Alice|
|  10|  80.0|Alice|
|   5|   NaN|  BOB|
|NULL|  NULL|  Tom|
|   9|  78.9| josh|
|  18|1802.3| bush|
|   7|  75.3|jerry|
+----+------+-----+


```


### Fill values[#](#Fill-values "Permalink to this headline")

For the remaining missing values, we can use `DataFrame.na.fill` or `DataFrame.fillna` to fill them.

With a `Dict` input `{'age': 10, 'height': 80.1}`, we can specify the values for columns `age` and `height` together.

```
df4 = df3.na.fill({'age': 10, 'height': 80.1})

df4.show()

```


```
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
| 10|  80.0|Alice|
|  5|  80.1|  BOB|
| 10|  80.1|  Tom|
|  9|  78.9| josh|
| 18|1802.3| bush|
|  7|  75.3|jerry|
+---+------+-----+


```


### Remove outliers[#](#Remove-outliers "Permalink to this headline")

After above steps, all missing values are dropped or filled. However, we can find that `height=1802.3` seems unreasonable, to remove this kind of outliers, we can filter the DataFrame with a valid range like `(65, 85)`.

```
df5 = df4.where(df4.height.between(65, 85))

df5.show()

```


```
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
| 10|  80.0|Alice|
|  5|  80.1|  BOB|
| 10|  80.1|  Tom|
|  9|  78.9| josh|
|  7|  75.3|jerry|
+---+------+-----+


```


### Remove duplicates[#](#Remove-duplicates "Permalink to this headline")

Now, all invalid records have been handled. But we notice that record `(age=10, height=80.0, name=Alice)` has been duplicated. To remove such duplicates, we can simply apply `DataFrame.distinct`.

```
df6 = df5.distinct()

df6.show()

```


```
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
|  5|  80.1|  BOB|
| 10|  80.1|  Tom|
|  9|  78.9| josh|
|  7|  75.3|jerry|
+---+------+-----+


```


### String manipulation[#](#String-manipulation "Permalink to this headline")

Column `name` contains both lower case and upper case letters. We can apply `lower()` function to convert all letters to lower case.

```
from pyspark.sql import functions as sf

df7 = df6.withColumn("name", sf.lower("name"))
df7.show()

```


```
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|alice|
|  5|  80.1|  bob|
| 10|  80.1|  tom|
|  9|  78.9| josh|
|  7|  75.3|jerry|
+---+------+-----+


```


For more complicated string manipulations, we can also use `udf` to utilize Python’s power functions.

```
from pyspark.sql import functions as sf

capitalize = sf.udf(lambda s: s.capitalize())

df8 = df6.withColumn("name", capitalize("name"))
df8.show()

```


```
+---+------+-----+
|age|height| name|
+---+------+-----+
| 10|  80.0|Alice|
|  5|  80.1|  Bob|
| 10|  80.1|  Tom|
|  9|  78.9| Josh|
|  7|  75.3|Jerry|
+---+------+-----+


```


### Reorder columns[#](#Reorder-columns "Permalink to this headline")

After above process, the data is clean and we want to reorder the columns before saving the DataFrame to some storage. You can refer to previous chapter `Load and Behold: Data loading, storage, file formats` for more details.

Normally, we use `DataFrame.select` for this purpose.

```
df9 = df7.select("name", "age", "height")

df9.show()

```


```
+-----+---+------+
| name|age|height|
+-----+---+------+
|alice| 10|  80.0|
|  bob|  5|  80.1|
|  tom| 10|  80.1|
| josh|  9|  78.9|
|jerry|  7|  75.3|
+-----+---+------+


```


Transform data[#](#Transform-data "Permalink to this headline")
---------------------------------------------------------------

The main part of a data engineering project is transformation. We create new dataframes from old ones.

### Select columns with select()
[#](#Select-columns-with-select\(\) "Permalink to this headline")

The input table may contains hundreds of columns, but for a specific project we likly are interested only in a small subset of them.

```
from pyspark.sql import functions as sf
df = spark.range(10)

for i in range(20):
  df = df.withColumn(f"col_{i}", sf.lit(i))

df.show()

```


```
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+------+------+------+------+
| id|col_0|col_1|col_2|col_3|col_4|col_5|col_6|col_7|col_8|col_9|col_10|col_11|col_12|col_13|col_14|col_15|col_16|col_17|col_18|col_19|
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+------+------+------+------+
|  0|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  1|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  2|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  3|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  4|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  5|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  6|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  7|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  8|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
|  9|    0|    1|    2|    3|    4|    5|    6|    7|    8|    9|    10|    11|    12|    13|    14|    15|    16|    17|    18|    19|
+---+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+------+------+------+------+------+------+------+------+------+


```


We create a DataFrame with 21 columns via a `for` loop, then we only select 4 columns by `select`. Columns `id`, `col_2` and `col_3` are directly selected from previous DataFrame, while column `sqrt_col_4_plus_5` is generated by the math functions.

We have hundreds of functions for column manipulation in `pyspark.sql.function` and `pyspark.sql.Column`.

```

df2 = df.select("id", "col_2", "col_3", sf.sqrt(sf.col("col_4") + sf.col("col_5")).alias("sqrt_col_4_plus_5"))

df2.show()

```


```
+---+-----+-----+-----------------+
| id|col_2|col_3|sqrt_col_4_plus_5|
+---+-----+-----+-----------------+
|  0|    2|    3|              3.0|
|  1|    2|    3|              3.0|
|  2|    2|    3|              3.0|
|  3|    2|    3|              3.0|
|  4|    2|    3|              3.0|
|  5|    2|    3|              3.0|
|  6|    2|    3|              3.0|
|  7|    2|    3|              3.0|
|  8|    2|    3|              3.0|
|  9|    2|    3|              3.0|
+---+-----+-----+-----------------+


```


### Filter rows with where()
[#](#Filter-rows-with-where\(\) "Permalink to this headline")

The input table may be super huge and contains billions of rows, and we may also be interested in only a small subset.

We can use `where` or `filter` with sepcified conditions to filter the rows.

For example, we can select rows with odd `id` values.

```
df3 = df2.where(sf.col("id") % 2 == 1)

df3.show()

```


```
+---+-----+-----+-----------------+
| id|col_2|col_3|sqrt_col_4_plus_5|
+---+-----+-----+-----------------+
|  1|    2|    3|              3.0|
|  3|    2|    3|              3.0|
|  5|    2|    3|              3.0|
|  7|    2|    3|              3.0|
|  9|    2|    3|              3.0|
+---+-----+-----+-----------------+


```


Summarizing data[#](#Summarizing-data "Permalink to this headline")
-------------------------------------------------------------------

In data analysis, we normally end up with summarizing data to a chart or table.

```
from pyspark.sql import Row

df = spark.createDataFrame([
    Row(incomes=[123.0, 456.0, 789.0], NAME="Alice"),
    Row(incomes=[234.0, 567.0], NAME="BOB"),
    Row(incomes=[100.0, 200.0, 100.0], NAME="Tom"),
    Row(incomes=[79.0, 128.0], NAME="josh"),
    Row(incomes=[123.0, 145.0, 178.0], NAME="bush"),
    Row(incomes=[111.0, 187.0, 451.0, 188.0, 199.0], NAME="jerry"),
])

df.show()

```


```
+--------------------+-----+
|             incomes| NAME|
+--------------------+-----+
|[123.0, 456.0, 78...|Alice|
|      [234.0, 567.0]|  BOB|
|[100.0, 200.0, 10...|  Tom|
|       [79.0, 128.0]| josh|
|[123.0, 145.0, 17...| bush|
|[111.0, 187.0, 45...|jerry|
+--------------------+-----+


```


For example, given the income per month, we want to find the average income for each name.

```
from pyspark.sql import functions as sf

df2 = df.select(sf.lower("NAME").alias("name"), "incomes")

df2.show(truncate=False)

```


```
+-----+-----------------------------------+
|name |incomes                            |
+-----+-----------------------------------+
|alice|[123.0, 456.0, 789.0]              |
|bob  |[234.0, 567.0]                     |
|tom  |[100.0, 200.0, 100.0]              |
|josh |[79.0, 128.0]                      |
|bush |[123.0, 145.0, 178.0]              |
|jerry|[111.0, 187.0, 451.0, 188.0, 199.0]|
+-----+-----------------------------------+


```


### Reshape data using explode()
[#](#Reshape-data-using-explode\(\) "Permalink to this headline")

To make the data easier for aggregation, we can use `explode()` function to reshape the data

```
df3 = df2.select("name", sf.explode("incomes").alias("income"))

df3.show()

```


```
+-----+------+
| name|income|
+-----+------+
|alice| 123.0|
|alice| 456.0|
|alice| 789.0|
|  bob| 234.0|
|  bob| 567.0|
|  tom| 100.0|
|  tom| 200.0|
|  tom| 100.0|
| josh|  79.0|
| josh| 128.0|
| bush| 123.0|
| bush| 145.0|
| bush| 178.0|
|jerry| 111.0|
|jerry| 187.0|
|jerry| 451.0|
|jerry| 188.0|
|jerry| 199.0|
+-----+------+


```


### Summarizing via groupBy() and agg()
[#](#Summarizing-via-groupBy\(\)-and-agg\(\) "Permalink to this headline")

Then we normally use `DataFrame.groupBy(...).agg(...)` to aggreate the data. To compute the average income, we can apply aggration function `avg`

```
df4 = df3.groupBy("name").agg(sf.avg("income").alias("avg_income"))

df4.show()

```


```
+-----+------------------+
| name|        avg_income|
+-----+------------------+
|alice|             456.0|
|  bob|             400.5|
|  tom|133.33333333333334|
| josh|             103.5|
| bush|148.66666666666666|
|jerry|             227.2|
+-----+------------------+


```


### Orderby[#](#Orderby "Permalink to this headline")

For final analysis, we normally want to order the data. In this case, we can order the data by `name`.

```
df5 = df4.orderBy("name")

df5.show()

```


```
+-----+------------------+
| name|        avg_income|
+-----+------------------+
|alice|             456.0|
|  bob|             400.5|
| bush|148.66666666666666|
|jerry|             227.2|
| josh|             103.5|
|  tom|133.33333333333334|
+-----+------------------+


```


When DataFrames Collide: The Art of Joining[#](#When-DataFrames-Collide:-The-Art-of-Joining "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

When dealing with multiple dataframe, we likely need to combine them together in some way. The most frequently used approach is joining.

For example, given the `incomes` data and `height` data, we can use `DataFrame.join` to join them together by `name`.

We can see that only `alice`, `josh` and `bush` are in the final results, because they appear in both DataFrames.

```
from pyspark.sql import Row

df1 = spark.createDataFrame([
    Row(age=10, height=80.0, name="alice"),
    Row(age=9, height=78.9, name="josh"),
    Row(age=18, height=82.3, name="bush"),
    Row(age=7, height=75.3, name="tom"),
])

df2 = spark.createDataFrame([
    Row(incomes=[123.0, 456.0, 789.0], name="alice"),
    Row(incomes=[234.0, 567.0], name="bob"),
    Row(incomes=[79.0, 128.0], name="josh"),
    Row(incomes=[123.0, 145.0, 178.0], name="bush"),
    Row(incomes=[111.0, 187.0, 451.0, 188.0, 199.0], name="jerry"),
])

```


```
df3 = df1.join(df2, on="name")

df3.show(truncate=False)

```


```
+-----+---+------+---------------------+
|name |age|height|incomes              |
+-----+---+------+---------------------+
|alice|10 |80.0  |[123.0, 456.0, 789.0]|
|bush |18 |82.3  |[123.0, 145.0, 178.0]|
|josh |9  |78.9  |[79.0, 128.0]        |
+-----+---+------+---------------------+


```


There are seven join methods: - `INNER` - `LEFT` - `RIGHT` - `FULL` - `CROSS` - `LEFTSEMI` - `LEFTANTI`

And the default one is `INNER`.

Let’s take `LEFT` join as another example. A left join includes all of the records from the first (left) of two tables, even if there are no matching values for records in the second (right) table.

```
df4 = df1.join(df2, on="name", how="left")

df4.show(truncate=False)

```


```
+-----+---+------+---------------------+
|name |age|height|incomes              |
+-----+---+------+---------------------+
|alice|10 |80.0  |[123.0, 456.0, 789.0]|
|josh |9  |78.9  |[79.0, 128.0]        |
|bush |18 |82.3  |[123.0, 145.0, 178.0]|
|tom  |7  |75.3  |NULL                 |
+-----+---+------+---------------------+


```


And a `RIGHT` join keeps all of the records from the right table.

```
df5 = df1.join(df2, on="name", how="right")

df5.show(truncate=False)

```


```
+-----+----+------+-----------------------------------+
|name |age |height|incomes                            |
+-----+----+------+-----------------------------------+
|alice|10  |80.0  |[123.0, 456.0, 789.0]              |
|bob  |NULL|NULL  |[234.0, 567.0]                     |
|josh |9   |78.9  |[79.0, 128.0]                      |
|bush |18  |82.3  |[123.0, 145.0, 178.0]              |
|jerry|NULL|NULL  |[111.0, 187.0, 451.0, 188.0, 199.0]|
+-----+----+------+-----------------------------------+


```
