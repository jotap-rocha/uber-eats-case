# Chapter 7: Load and Behold - Data loading, storage, file formats — PySpark 4.0.1 documentation
Chapter 7: Load and Behold - Data loading, storage, file formats[#](#Chapter-7:-Load-and-Behold---Data-loading,-storage,-file-formats "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

```
!pip install pyspark==4.0.0.dev2

```


```
Requirement already satisfied: pyspark==4.0.0.dev2 in /Users/amanda.liu/anaconda3/envs/llm-spark/lib/python3.11/site-packages (4.0.0.dev2)
Requirement already satisfied: py4j==0.10.9.7 in /Users/amanda.liu/anaconda3/envs/llm-spark/lib/python3.11/site-packages (from pyspark==4.0.0.dev2) (0.10.9.7)

```


```
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Data Loading and Storage Example") \
    .getOrCreate()

```


This section covers how to read and write data in various formats using PySpark. You’ll learn how to load data from common file types (e.g., CSV, JSON, Parquet, ORC) and store data efficiently.

Reading Data[#](#Reading-Data "Permalink to this headline")
-----------------------------------------------------------

### 1.1 Reading CSV Files[#](#1.1-Reading-CSV-Files "Permalink to this headline")

CSV is one of the most common formats for data exchange. Here’s how to load a CSV file into a DataFrame:

```
csv_df = spark.read.csv("../data/employees.csv", header=True, inferSchema=True)
csv_df.show()

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


**Explanation:** - `header=True`: Treats the first line as column names. - `inferSchema=True`: Automatically infers data types of columns.

### 1.2 Reading JSON Files[#](#1.2-Reading-JSON-Files "Permalink to this headline")

Loading JSON files is simple and allows you to handle both single-line and multi-line JSON structures:

```
json_df = spark.read.option("multiline", "true").json("../data/employees.json")
json_df.show()

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


**Explanation:** - `multiline="true"`: Allows reading multi-line JSON structures.

### 1.3 Reading Parquet Files[#](#1.3-Reading-Parquet-Files "Permalink to this headline")

Parquet is a columnar format that supports efficient data compression and encoding:

```
parquet_df = spark.read.parquet("../data/employees.parquet")
parquet_df.show()

```


```
+-----------+-----------------+-----------------+
|Employee ID|         Location|             Role|
+-----------+-----------------+-----------------+
|      19239|      Seattle, WA|Software Engineer|
|      19243|     New York, NY|  Product Manager|
|      19242|San Francisco, CA|        Recruiter|
|      19241|     New York, NY|     Data Analyst|
|      19240|      Seattle, WA|    IT Specialist|
|      19238|      Seattle, WA|     Data Analyst|
+-----------+-----------------+-----------------+


```


**Tip:** Parquet files are highly efficient for storing data due to columnar storage and compression.

### 1.4 Reading ORC Files[#](#1.4-Reading-ORC-Files "Permalink to this headline")

ORC is another columnar file format, often used in Hadoop environments:

```
orc_df = spark.read.orc("../data/employees.orc")
orc_df.show()

```


```
+-----------+-----------------+-----------------+
|Employee ID|         Location|             Role|
+-----------+-----------------+-----------------+
|      19242|San Francisco, CA|        Recruiter|
|      19239|      Seattle, WA|Software Engineer|
|      19240|      Seattle, WA|    IT Specialist|
|      19243|     New York, NY|  Product Manager|
|      19238|      Seattle, WA|     Data Analyst|
|      19241|     New York, NY|     Data Analyst|
+-----------+-----------------+-----------------+


```


Writing Data[#](#Writing-Data "Permalink to this headline")
-----------------------------------------------------------

### 2.1 Writing Data as CSV[#](#2.1-Writing-Data-as-CSV "Permalink to this headline")

```
csv_df.write.csv("../data/employees_out.csv", mode="overwrite", header=True)

```


**Explanation:** - `mode="overwrite"`: If the directory exists, it will be replaced. - `header=True`: Writes the column names as the first line.

### 2.2 Writing Data as Parquet[#](#2.2-Writing-Data-as-Parquet "Permalink to this headline")

Parquet format is recommended for large datasets:

```
parquet_df.write.parquet("../data/employees_out.parquet", mode="overwrite")

```


### 2.3 Writing Data as ORC[#](#2.3-Writing-Data-as-ORC "Permalink to this headline")

```
json_df.write.orc("../data/employees_out.orc", mode="overwrite")

```


**Tip:** Parquet and ORC formats are best for efficient storage and quick reads.

Additional Options and Configurations[#](#Additional-Options-and-Configurations "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------

You can customize how data is read and written by using additional options. Here are a few examples:

### Custom Delimiter in CSV:[#](#Custom-Delimiter-in-CSV: "Permalink to this headline")

```
spark.read.option("delimiter", ";").csv("../data/employees.csv").show(truncate=False)

```


```
+-------------------------------------+
|_c0                                  |
+-------------------------------------+
|Employee ID,Role,Location            |
|19238,Data Analyst,"Seattle, WA"     |
|19239,Software Engineer,"Seattle, WA"|
|19240,IT Specialist,"Seattle, WA"    |
|19241,Data Analyst,"New York, NY"    |
|19242,Recruiter,"San Francisco, CA"  |
|19243,Product Manager,"New York, NY" |
+-------------------------------------+


```


### Handling Null Values:[#](#Handling-Null-Values: "Permalink to this headline")

```
spark.read.option("nullValue", "NULL").csv("../data/employees.csv").show(truncate=False)

```


```
+-----------+-----------------+-----------------+
|_c0        |_c1              |_c2              |
+-----------+-----------------+-----------------+
|Employee ID|Role             |Location         |
|19238      |Data Analyst     |Seattle, WA      |
|19239      |Software Engineer|Seattle, WA      |
|19240      |IT Specialist    |Seattle, WA      |
|19241      |Data Analyst     |New York, NY     |
|19242      |Recruiter        |San Francisco, CA|
|19243      |Product Manager  |New York, NY     |
+-----------+-----------------+-----------------+


```


### Compression Options:[#](#Compression-Options: "Permalink to this headline")

```
parquet_df.write.option("compression", "gzip").parquet("../data/employees_out.parquet", mode="overwrite")

```


See the [PySpark API reference](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/io.html) for Input/Output to check all supported functions and options.