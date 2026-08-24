# Chapter 1: DataFrames - A view into your structured data — PySpark 4.0.1 documentation
```
Requirement already satisfied: pyspark in /Users/amanda.liu/anaconda3/lib/python3.10/site-packages (3.5.0)
Requirement already satisfied: py4j==0.10.9.7 in /Users/amanda.liu/anaconda3/lib/python3.10/site-packages (from pyspark) (0.10.9.7)
Note: you may need to restart the kernel to use updated packages.

```


```
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

```


This section introduces the most fundamental data structure in PySpark: the DataFrame.

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. You can think of a DataFrame like a spreadsheet, a SQL table, or a dictionary of series objects. Apache Spark DataFrames support a rich set of APIs (select columns, filter, join, aggregate, etc.) that allow you to solve common data analysis problems efficiently.

Compared to traditional relational databases, Spark DataFrames offer several key advantages for big data processing and analytics:

*   **Distributed computing**: Spark distributes data across multiple nodes in a cluster, allowing for parallel processing of big data
    
*   **In-memory processing**: Spark performs computations in memory, which can be significantly faster than disk-based processing
    
*   **Schema flexibility**: Unlike traditional databases, PySpark DataFrames support schema evolution and dynamic typing.
    
*   **Fault tolerance**: PySpark DataFrames are built on top of Resilient Distributed Dataset (RDDs), which are inherently fault-tolerant. Spark automatically handles node failures and data replication, ensuring data reliability and integrity.
    

A note on RDDs: Direct use of RDDs are no longer supported on Spark Connect as of Spark 4.0. Interacting directly with Spark DataFrames uses a unified planning and optimization engine, allowing us to get nearly identical performance across all supported languages on Databricks (Python, SQL, Scala, and R).

Create a DataFrame[#](#Create-a-DataFrame "Permalink to this headline")
-----------------------------------------------------------------------

There are several ways to create a DataFrame in PySpark.

### From a list of dictionaries[#](#From-a-list-of-dictionaries "Permalink to this headline")

The simplest way is to use the createDataFrame() method like so:

```
employees = [{"name": "John D.", "age": 30},
  {"name": "Alice G.", "age": 25},
  {"name": "Bob T.", "age": 35},
  {"name": "Eve A.", "age": 28}]

# Create a DataFrame containing the employees data
df = spark.createDataFrame(employees)
df.show()

```


```
+---+--------+
|age|    name|
+---+--------+
| 30| John D.|
| 25|Alice G.|
| 35|  Bob T.|
| 28|  Eve A.|
+---+--------+


```


### From a local file[#](#From-a-local-file "Permalink to this headline")

We can also create a DataFrame from a local CSV file:

```
df = spark.read.csv("../data/employees.csv", header=True, inferSchema=True)
df.show()

```


```
+-----------+-----------------+-----------------+
|Employee ID|             Role|         Location|
+-----------+-----------------+-----------------+
|      19238|     Data Analyst|      Seattle, WA|
|      19239|Software Engineer|      Seattle, WA|
|      19240|    IT Specialist|      Seattle, WA|
|      19241|     Data Analyst|     New York, NY|
|      19242|        Recruiter|San Francisco, CA|
|      19243|  Product Manager|     New York, NY|
+-----------+-----------------+-----------------+


```


Or from a local JSON file:

```
df = spark.read.option("multiline","true").json("../data/employees.json")
df.show()

```


```
+-----------+-----------------+-----------------+
|Employee ID|         Location|             Role|
+-----------+-----------------+-----------------+
|      19238|      Seattle, WA|     Data Analyst|
|      19239|      Seattle, WA|Software Engineer|
|      19240|      Seattle, WA|    IT Specialist|
|      19241|     New York, NY|     Data Analyst|
|      19242|San Francisco, CA|        Recruiter|
|      19243|     New York, NY|  Product Manager|
+-----------+-----------------+-----------------+


```


### From an existing DataFrame[#](#From-an-existing-DataFrame "Permalink to this headline")

We can even create a DataFrame from another existing DataFrame, by selecting certain columns:

```
employees = [
  {"name": "John D.", "age": 30, "department": "HR"},
  {"name": "Alice G.", "age": 25, "department": "Finance"},
  {"name": "Bob T.", "age": 35, "department": "IT"},
  {"name": "Eve A.", "age": 28, "department": "Marketing"}
]
df = spark.createDataFrame(employees)

# Select only the name and age columns
new_df = df.select("name", "age")

```


### From a table[#](#From-a-table "Permalink to this headline")

If you have an existing table `table_name` in your Spark environment, you can create a DataFrame like this:

```
df = spark.read.table("table_name")

```


### From a database[#](#From-a-database "Permalink to this headline")

If your table is in a database, you can use JDBC to read the table into a DataFrame.

```
url = "jdbc:mysql://localhost:3306/mydatabase"
table = "employees"
properties = {
  "user": "username",
  "password": "password"
}

# Read table into DataFrame
df = spark.read.jdbc(url=url, table=table, properties=properties)

```


View the DataFrame[#](#View-the-DataFrame "Permalink to this headline")
-----------------------------------------------------------------------

We can use PySpark to view and interact with our DataFrame.

### Display the DataFrame[#](#Display-the-DataFrame "Permalink to this headline")

`df.show()` displays a basic visualization of the DataFrame’s contents. From our above `createDataFrame()` example:

```
employees = [{"name": "John D.", "age": 30},
  {"name": "Alice G.", "age": 25},
  {"name": "Bob T.", "age": 35},
  {"name": "Eve A.", "age": 28}]

# Create a DataFrame containing the employees data
df = spark.createDataFrame(employees)

```


```
+---+--------+
|age|    name|
+---+--------+
| 30| John D.|
| 25|Alice G.|
| 35|  Bob T.|
| 28|  Eve A.|
+---+--------+


```


`df.show()` has 3 optional arguments: `n`, `truncate`, and `vertical`.

By default, `df.show()` displays up to the first 20 rows of the DataFrame. We can control the number of rows displayed by passing an argument to the show() method:

```
+---+--------+
|age|    name|
+---+--------+
| 30| John D.|
| 25|Alice G.|
+---+--------+
only showing top 2 rows


```


The truncate argument controls the length of displayed column values (default value is 20):

```
+---+----+
|age|name|
+---+----+
| 30| Joh|
| 25| Ali|
| 35| Bob|
| 28| Eve|
+---+----+


```


If we set `vertical` to True, the DataFrame will be displayed vertically with one line per value:

```
-RECORD 0--------
 age  | 30
 name | John D.
-RECORD 1--------
 age  | 25
 name | Alice G.
-RECORD 2--------
 age  | 35
 name | Bob T.
-RECORD 3--------
 age  | 28
 name | Eve A.


```


### Print the DataFrame schema[#](#Print-the-DataFrame-schema "Permalink to this headline")

We can view information about the DataFrame schema using the `printSchema()` method:

```
root
 |-- age: long (nullable = true)
 |-- name: string (nullable = true)


```


DataFrame Manipulation[#](#DataFrame-Manipulation "Permalink to this headline")
-------------------------------------------------------------------------------

Let’s look at some ways we can transform our DataFrames.

For more detailed information, please see the section about data manipulation, [Chapter 6: Function Junction - Data manipulation with PySpark](https://databricks-eng.github.io/pyspark-cookbook/07-dataprep.html).

### Rename columns[#](#Rename-columns "Permalink to this headline")

We can rename DataFrame columns using the `withColumnRenamed()` method:

```
df.show()
df2 = df.withColumnRenamed("name", "full_name")
df2.show()

```


```
+---+--------+
|age|    name|
+---+--------+
| 30| John D.|
| 25|Alice G.|
| 35|  Bob T.|
| 28|  Eve A.|
+---+--------+

+---+---------+
|age|full_name|
+---+---------+
| 30|  John D.|
| 25| Alice G.|
| 35|   Bob T.|
| 28|   Eve A.|
+---+---------+


```


### Filter rows[#](#Filter-rows "Permalink to this headline")

We can filter for employees within a certain age range. The following `df.filter` will create a new DataFrame with rows that match our age condition:

```
filtered_df = df.filter((df["age"] > 26) & (df["age"] < 32))
filtered_df.show()

```


```
+---+-------+
|age|   name|
+---+-------+
| 30|John D.|
| 28| Eve A.|
+---+-------+


```


We can also use `df.where` to get the same result:

```
where_df = df.where((df["age"] > 26) & (df["age"] < 32))
where_df.show()

```


```
+---+-------+
|age|   name|
+---+-------+
| 30|John D.|
| 28| Eve A.|
+---+-------+


```


DataFrames vs. Tables[#](#DataFrames-vs.-Tables "Permalink to this headline")
-----------------------------------------------------------------------------

A DataFrame is an immutable distributed collection of data, only available in the current Spark session.

A table is a persistent data structure that can be accessed across multiple Spark sessions.

If you wish to promote a DataFrame to a table, you can use the `createOrReplaceTempView()` method:

```
df.createOrReplaceTempView("employees")

```


Note that the lifetime of this temporary table is tied to the SparkSession that was used to create this DataFrame. To persist the table beyond this Spark session, you will need to save it to persistent storage.

Save DataFrame to Persistent Storage[#](#Save-DataFrame-to-Persistent-Storage "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------

There are several ways to save a DataFrame to persistent storage in PySpark. For more detailed information about saving data to your local environment, please see the section about Data Loading (TODO: add link).

### Save to file-based data source[#](#Save-to-file-based-data-source "Permalink to this headline")

For file-based data source (text, parquet, json, etc.), you can specify a custom table path like so:

```
df.write.option("path", "../dataout").saveAsTable("dataframes_savetable_example")

```


Even if the table is dropped, the custom table path and table data will still be there.

If no custom table path is specified, Spark will write data to a default table path under the warehouse directory. When the table is dropped, the default table path will be removed too.

### Save to Hive metastore[#](#Save-to-Hive-metastore "Permalink to this headline")

To save to Hive metastore, you can use the following:

```
df.write().mode("overwrite").saveAsTable("schemaName.tableName")

```
