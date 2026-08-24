# Chapter 6: Old SQL, New Tricks - Running SQL on PySpark — PySpark 4.0.1 documentation
```
import warnings
warnings.filterwarnings('ignore')

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("error")

```


Chapter 6: Old SQL, New Tricks - Running SQL on PySpark[#](#Chapter-6:-Old-SQL,-New-Tricks---Running-SQL-on-PySpark "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------

Introduction[#](#Introduction "Permalink to this headline")
-----------------------------------------------------------

This section explains how to use the Spark SQL API in PySpark and compare it with the DataFrame API. It also covers how to switch between the two APIs seamlessly, along with some practical tips and tricks.

Running SQL with PySpark[#](#Running-SQL-with-PySpark "Permalink to this headline")
-----------------------------------------------------------------------------------

PySpark offers two main ways to perform SQL operations:

### Using `spark.sql()`[#](#Using-spark.sql\(\) "Permalink to this headline")

The `spark.sql()` function allows you to execute SQL queries directly.

```
# Create a table via spark.sql()
spark.sql("DROP TABLE IF EXISTS people")
spark.sql("""
CREATE TABLE people USING PARQUET
AS SELECT * FROM VALUES (1, 'Alice', 10), (2, 'Bob', 20), (3, 'Charlie', 30) t(id, name, age)
""")

```


```
# Use spark.sql() to select data from a table
spark.sql("SELECT name, age FROM people WHERE age > 21").show()

```


```
+-------+---+
|   name|age|
+-------+---+
|Charlie| 30|
+-------+---+


```


### Using the PySpark DataFrame API[#](#Using-the-PySpark-DataFrame-API "Permalink to this headline")

The PySpark DataFrame API provides equivalent functionality to SQL but with a Pythonic approach.

```
# Read a table using the DataFrame API
people_df = spark.read.table("people")

# Use DataFrame API to select data
people_df.select("name", "age").filter("age > 21").show()

```


```
+-------+---+
|   name|age|
+-------+---+
|Charlie| 30|
+-------+---+


```


SQL vs. DataFrame API in PySpark[#](#SQL-vs.-DataFrame-API-in-PySpark "Permalink to this headline")
---------------------------------------------------------------------------------------------------

When to use which API depends on your background and the specific task:

**SQL API:** - Ideal for users with SQL backgrounds who are more comfortable writing SQL queries.

**DataFrame API:** - Preferred by Python developers as it aligns with Python syntax and idioms. - Provides greater flexibility for complex transformations, especially with user-defined functions (UDFs).

### Code Examples: SQL vs. DataFrame API[#](#Code-Examples:-SQL-vs.-DataFrame-API "Permalink to this headline")

Here are some examples comparing how common tasks are performed using the SQL API and PySpark’s DataFrame API to give you an idea of their differences and when one might be more suitable than the other.

#### Example: SELECT and FILTER Operation[#](#Example:-SELECT-and-FILTER-Operation "Permalink to this headline")

**SQL API:**

```
spark.sql("SELECT name FROM people WHERE age > 21").show()

```


```
+-------+
|   name|
+-------+
|Charlie|
+-------+


```


**DataFrame API:**

```
spark.read.table("people").select("name").filter("age > 21").show()

```


```
+-------+
|   name|
+-------+
|Charlie|
+-------+


```


#### Example: JOIN Operation[#](#Example:-JOIN-Operation "Permalink to this headline")

```
spark.sql("DROP TABLE IF EXISTS orders")
spark.sql("""
CREATE TABLE orders USING PARQUET
AS SELECT * FROM VALUES (101, 1, 200), (102, 2, 150), (103,3, 300) t(order_id, customer_id, amount)
""")

```


**SQL API:**

```
spark.sql("""
SELECT p.name, o.order_id
FROM people p
JOIN orders o ON p.id = o.customer_id
""").show()

```


```
+-------+--------+
|   name|order_id|
+-------+--------+
|Charlie|     103|
|  Alice|     101|
|    Bob|     102|
+-------+--------+


```


**DataFrame API:**

```
people_df = spark.read.table("people")
orders_df = spark.read.table("orders")
(
    people_df
        .join(orders_df, people_df.id == orders_df.customer_id)
        .select(people_df.name, orders_df.order_id)
        .show()
)

```


```
+-------+--------+
|   name|order_id|
+-------+--------+
|Charlie|     103|
|  Alice|     101|
|    Bob|     102|
+-------+--------+


```


#### Example: GROUP BY and Aggregate Operation[#](#Example:-GROUP-BY-and-Aggregate-Operation "Permalink to this headline")

**SQL API:**

```
spark.sql("""
SELECT p.name, SUM(o.amount) AS total_amount
FROM people p
JOIN orders o ON p.id = o.customer_id
GROUP BY p.name
""").show()

```


```
+-------+------------+
|   name|total_amount|
+-------+------------+
|Charlie|         300|
|  Alice|         200|
|    Bob|         150|
+-------+------------+


```


**DataFrame API:**

```
from pyspark.sql.functions import sum

(
    people_df
        .join(orders_df, people_df.id == orders_df.customer_id)
        .groupBy("name")
        .agg(sum("amount").alias("total_amount"))
        .show()
)

```


```
+-------+------------+
|   name|total_amount|
+-------+------------+
|Charlie|         300|
|  Alice|         200|
|    Bob|         150|
+-------+------------+


```


#### Example: Window Operations[#](#Example:-Window-Operations "Permalink to this headline")

**SQL API:**

```
spark.sql("""
SELECT
    p.name,
    o.amount,
    RANK() OVER (PARTITION BY p.name ORDER BY o.amount DESC) AS rank
FROM people p
JOIN orders o ON p.id = o.customer_id
""").show()

```


```
+-------+------+----+
|   name|amount|rank|
+-------+------+----+
|  Alice|   200|   1|
|    Bob|   150|   1|
|Charlie|   300|   1|
+-------+------+----+


```


**DataFrame API:**

```
from pyspark.sql.window import Window
from pyspark.sql.functions import rank

# Define the window specification
window_spec = Window.partitionBy("name").orderBy(orders_df.amount.desc())

# Window operation with RANK
(
    people_df
        .join(orders_df, people_df.id == orders_df.customer_id)
        .withColumn("rank", rank().over(window_spec))
        .select("name", "amount", "rank")
        .show()
)

```


```
+-------+------+----+
|   name|amount|rank|
+-------+------+----+
|  Alice|   200|   1|
|    Bob|   150|   1|
|Charlie|   300|   1|
+-------+------+----+


```


#### Example: UNION Operation[#](#Example:-UNION-Operation "Permalink to this headline")

**SQL API:** - The `UNION` operator combines rows from two queries and removes duplicates by default.

```
spark.sql("CREATE OR REPLACE TEMP VIEW people2 AS SELECT * FROM VALUES (1, 'Alice', 10), (4, 'David', 35) t(id, name, age)")

```


```
spark.sql("""
SELECT * FROM people
UNION
SELECT * FROM people2
""").show()

```


```
+---+-------+---+
| id|   name|age|
+---+-------+---+
|  3|Charlie| 30|
|  1|  Alice| 10|
|  2|    Bob| 20|
|  4|  David| 35|
+---+-------+---+


```


**DataFrame API:** - The `union()` method is used to combine two DataFrames, but it does not remove duplicates by default. - To match the behavior of SQL’s UNION, we use the .dropDuplicates() method to eliminate duplicates after the union operation.

```
people_df = spark.read.table("people")
people2_df = spark.read.table("people2")
# This will have duplicate values.
people_df.union(people2_df).show()

```


```
+---+-------+---+
| id|   name|age|
+---+-------+---+
|  3|Charlie| 30|
|  1|  Alice| 10|
|  2|    Bob| 20|
|  1|  Alice| 10|
|  4|  David| 35|
+---+-------+---+


```


```
# Remove duplicate values
people_df.union(people2_df).dropDuplicates().show()

```


```
+---+-------+---+
| id|   name|age|
+---+-------+---+
|  3|Charlie| 30|
|  1|  Alice| 10|
|  2|    Bob| 20|
|  4|  David| 35|
+---+-------+---+


```


#### Example: SET Configurations[#](#Example:-SET-Configurations "Permalink to this headline")

**SQL API:**

```
spark.sql("SET spark.sql.shuffle.partitions=8")

```


```
DataFrame[key: string, value: string]

```


```
spark.sql("SET spark.sql.shuffle.partitions").show(truncate=False)

```


```
+----------------------------+-----+
|key                         |value|
+----------------------------+-----+
|spark.sql.shuffle.partitions|8    |
+----------------------------+-----+


```


**DataFrame API:**

```
spark.conf.set("spark.sql.shuffle.partitions", 10)

```


```
spark.conf.get("spark.sql.shuffle.partitions")

```


#### Example: Listing Tables and Views[#](#Example:-Listing-Tables-and-Views "Permalink to this headline")

**SQL API:**

```
spark.sql("SHOW TABLES").show()

```


```
+---------+---------+-----------+
|namespace|tableName|isTemporary|
+---------+---------+-----------+
|  default|   orders|      false|
|  default|   people|      false|
|         |  people2|       true|
+---------+---------+-----------+


```


**DataFrame API:**

```
tables = spark.catalog.listTables()
for table in tables:
    print(f"Name: {table.name}, isTemporary: {table.isTemporary}")

```


```
Name: orders, isTemporary: False
Name: people, isTemporary: False
Name: people2, isTemporary: True

```


### DataFrame API Exclusive Functions[#](#DataFrame-API-Exclusive-Functions "Permalink to this headline")

Certain operations are exclusive to the DataFrame API and are not supported in SQL, such as:

**withColumn**: Adds or modifies columns in a DataFrame.

```
people_df.withColumn("new_col", people_df["age"] + 10).show()

```


```
+---+-------+---+-------+
| id|   name|age|new_col|
+---+-------+---+-------+
|  3|Charlie| 30|     40|
|  1|  Alice| 10|     20|
|  2|    Bob| 20|     30|
+---+-------+---+-------+


```


```
people_df.withColumn("age", people_df["age"] + 10).show()

```


```
+---+-------+---+
| id|   name|age|
+---+-------+---+
|  3|Charlie| 40|
|  1|  Alice| 20|
|  2|    Bob| 30|
+---+-------+---+


```


Using SQL and DataFrame API Interchangeably[#](#Using-SQL-and-DataFrame-API-Interchangeably "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------

PySpark supports switching between SQL and DataFrame API, making it easy to mix and match.

### Chaining DataFrame Operations on SQL Outputs[#](#Chaining-DataFrame-Operations-on-SQL-Outputs "Permalink to this headline")

PySpark’s DataFrame API allows you to chain multiple operations together to create efficient and readable transformations.

```
# Chaining DataFrame operations on SQL results
spark.sql("SELECT name, age FROM people").filter("age > 21").show()

```


```
+-------+---+
|   name|age|
+-------+---+
|Charlie| 30|
+-------+---+


```


### Using `selectExpr()`[#](#Using-selectExpr\(\) "Permalink to this headline")

The `selectExpr()` method allows you to run SQL expressions within the DataFrame API.

```
people_df.selectExpr("name", "age + 1 AS age_plus_one").show()

```


```
+-------+------------+
|   name|age_plus_one|
+-------+------------+
|Charlie|          31|
|  Alice|          11|
|    Bob|          21|
+-------+------------+


```


### Querying a DataFrame in SQL[#](#Querying-a-DataFrame-in-SQL "Permalink to this headline")

You can create a temporary view from a DataFrame and run SQL queries on it.

```
# First create a temp view on top of the DataFrame.
people_df.createOrReplaceTempView("people_view")

# Then it can be referenced in SQL.
spark.sql("SELECT * FROM people_view WHERE age > 21").show()

```


```
+---+-------+---+
| id|   name|age|
+---+-------+---+
|  3|Charlie| 30|
+---+-------+---+


```


### Use Python User-Defined Functions in SQL[#](#Use-Python-User-Defined-Functions-in-SQL "Permalink to this headline")

You can register Python user-defined functions (UDFs) for use within SQL queries, enabling custom transformations within SQL syntax.

```
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Define the UDF
@udf("string")
def uppercase_name(name):
    return name.upper()

# Register the UDF
spark.udf.register("uppercase_name", uppercase_name)

# Use it in SQL
spark.sql("SELECT name, uppercase_name(name) FROM people_view WHERE age > 21").show()

```


```
+-------+--------------------+
|   name|uppercase_name(name)|
+-------+--------------------+
|Charlie|             CHARLIE|
+-------+--------------------+


```
