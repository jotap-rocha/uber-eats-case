# Chapter 5: Unleashing UDFs & UDTFs — PySpark 4.0.1 documentation
Chapter 5: Unleashing UDFs & UDTFs[#](#Chapter-5:-Unleashing-UDFs-&-UDTFs "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

In large-scale data processing, customization is often necessary to extend the native capabilities of Spark. _Python User-Defined Functions (UDFs)_ and _User-Defined Table Functions (UDTFs)_ offer a way to perform complex transformations and computations using Python, seamlessly integrating them into Spark’s distributed environment.

In this section, we’ll explore how to write and use UDFs and UDTFs in Python, leveraging PySpark to perform complex data transformations that go beyond Spark’s built-in functions.

Python UDFs[#](#Python-UDFs "Permalink to this headline")
---------------------------------------------------------

### Categories of Python UDFs[#](#Categories-of-Python-UDFs "Permalink to this headline")

There are two main categories of UDFs supported in PySpark: Scalar Python UDFs and Pandas UDFs.

*   _Scalar Python UDFs_ are user-defined scalar functions that take or return Python objects serialized/deserialized by [pickle](https://python.readthedocs.io/en/latest/library/pickle.html) or [Arrow](https://arrow.readthedocs.io/en/latest/) and operate one row at a time
    
*   _Pandas UDFs_ (a.k.a. Vectorized UDFs) are UDFs that take/return pandas Series or DataFrame serialized/deserialized by Apache Arrow and operate block by block. Pandas UDFs have some variations categorized by usage, with specific input and output types: Series to Series, Series to Scalar, and Iterator to Iterator.
    

Based on Pandas UDFs implementation, there are also _Pandas Function APIs_: Map (i.e., `mapInPandas`) and (Co)Grouped Map (i.e., `applyInPandas`), as well as an Arrow Function API - `mapInArrow`.

### To create a Scalar Python UDF[#](#To-create-a-Scalar-Python-UDF "Permalink to this headline")

In the code below, we’ve created a simple scalar Python UDF.

```
from pyspark.sql.functions import udf

@udf(returnType='int')
def slen(s: str):
    return len(s)

```


#### Arrow optimization[#](#Arrow-optimization "Permalink to this headline")

Scalar Python UDFs rely on [cloudpickle](https://pypi.org/project/cloudpickle/) for serialization and deserialization, and encounter performance bottlenecks, particularly when dealing with large data inputs and outputs. We introduce Arrow-optimized Python UDFs to significantly improve performance.

At the core of this optimization lies Apache Arrow, a standardized cross-language columnar in-memory data representation. By harnessing Arrow, these UDFs bypass the traditional, slower methods of data (de)serialization, leading to swift data exchange between JVM and Python processes. With Apache Arrow’s rich type system, these optimized UDFs offer a more consistent and standardized way to handle type coercion.

We can control whether or not to enable Arrow optimization for individual UDFs by using the `useArrow` boolean parameter of `functions.udf`. An example is as shown below:

```
from pyspark.sql.functions import udf

@udf(returnType='int', useArrow=True)  # An Arrow Python UDF
def arrow_slen(s: str):
    ...

```


In addition, we can enable Arrow optimization for all UDFs of an entire SparkSession via a Spark configuration: `spark.sql.execution.pythonUDF.arrow.enabled`, as shown below:

```
spark.conf.set("spark.sql.execution.pythonUDF.arrow.enabled", True)

@udf(returnType='int')  # An Arrow Python UDF
def arrow_slen(s: str):
    ...

```


### To use a Scalar Python UDF[#](#To-use-a-Scalar-Python-UDF "Permalink to this headline")

In Python, we can invoke a UDF directly on column(s), just like a built-in Spark function, as shown below.

```
data = [("Alice",), ("Bob",), ("Charlie",)]
df = spark.createDataFrame(data, ["name"])
df.withColumn("name_length", slen(df["name"])).show()

```


```
+-------+-----------+
|   name|name_length|
+-------+-----------+
|  Alice|          5|
|    Bob|          3|
|Charlie|          7|
+-------+-----------+


```


### To create a Pandas UDF[#](#To-create-a-Pandas-UDF "Permalink to this headline")

In the code below, we’ve created a Pandas UDF which takes one `pandas.Series` and outputs one `pandas.Series`

```
import pandas as pd
from pyspark.sql.functions import pandas_udf

@pandas_udf("string")
def to_upper(s: pd.Series) -> pd.Series:
    return s.str.upper()

df = spark.createDataFrame([("John Doe",)], ("name",))
df.select(to_upper("name")).show()


```


```
+--------------+
|to_upper(name)|
+--------------+
|      JOHN DOE|
+--------------+


```


### To use a Pandas UDF[#](#To-use-a-Pandas-UDF "Permalink to this headline")

Similar to a Scalar Python UDF, we can also invoke a pandas UDF directly on column(s):

```
data = [("Alice",), ("Bob",), ("Charlie",)]
df = spark.createDataFrame(data, ["name"])
df.withColumn("name_length", to_upper(df["name"])).show()

```


```
+-------+-----------+
|   name|name_length|
+-------+-----------+
|  Alice|      ALICE|
|    Bob|        BOB|
|Charlie|    CHARLIE|
+-------+-----------+


```


### More Examples[#](#More-Examples "Permalink to this headline")

#### Example 1: Python UDF to Process DataFrame with String and List Columns[#](#Example-1:-Python-UDF-to-Process-DataFrame-with-String-and-List-Columns "Permalink to this headline")

```
from pyspark.sql.types import ArrayType, IntegerType, StringType
from pyspark.sql.functions import udf

data = [
    ("Hello World", [1, 2, 3]),
    ("PySpark is Fun", [4, 5, 6]),
    ("PySpark Rocks", [7, 8, 9])
]
df = spark.createDataFrame(data, ["text_column", "list_column"])

@udf(returnType="string")
def process_row(text: str, numbers):
    vowels_count = sum(1 for char in text if char in "aeiouAEIOU")
    doubled = [x * 2 for x in numbers]
    return f"Vowels: {vowels_count}, Doubled: {doubled}"

df.withColumn("process_row", process_row(df["text_column"], df["list_column"])).show(truncate=False)

```


```
+--------------+-----------+--------------------------------+
|text_column   |list_column|process_row                     |
+--------------+-----------+--------------------------------+
|Hello World   |[1, 2, 3]  |Vowels: 3, Doubled: [2, 4, 6]   |
|PySpark is Fun|[4, 5, 6]  |Vowels: 3, Doubled: [8, 10, 12] |
|PySpark Rocks |[7, 8, 9]  |Vowels: 2, Doubled: [14, 16, 18]|
+--------------+-----------+--------------------------------+


```


#### Example 2: Pandas UDF for Statistical Computations and Complex Transformation[#](#Example-2:-Pandas-UDF-for-Statistical-Computations-and-Complex-Transformation "Permalink to this headline")

```
from pyspark.sql import SparkSession
from pyspark.sql.functions import pandas_udf
from pyspark.sql.types import StructType, StructField, DoubleType, StringType
import pandas as pd

data = [
    (10.0, "Spark"),
    (20.0, "Big Data"),
    (30.0, "AI"),
    (40.0, "Machine Learning"),
    (50.0, "Deep Learning")
]
df = spark.createDataFrame(data, ["numeric_column", "text_column"])

# Schema for the result
schema = StructType([
    StructField("mean_value", DoubleType(), True),
    StructField("sum_value", DoubleType(), True),
    StructField("processed_text", StringType(), True)
])

@pandas_udf(schema)
def compute_stats_and_transform_string(numeric_col: pd.Series, text_col: pd.Series) -> pd.DataFrame:
    mean_value = numeric_col.mean()
    sum_value = numeric_col.sum()

    # Reverse the string if its length is greater than 5, otherwise capitalize it
    processed_text = text_col.apply(lambda x: x[::-1] if len(x) > 5 else x.upper())

    result_df = pd.DataFrame({
        "mean_value": [mean_value] * len(text_col),
        "sum_value": [sum_value] * len(text_col),
        "processed_text": processed_text
    })

    return result_df

df.withColumn("result", compute_stats_and_transform_string(df["numeric_column"], df["text_column"])).show(truncate=False)

```


```
+--------------+----------------+------------------------------+
|numeric_column|text_column     |result                        |
+--------------+----------------+------------------------------+
|10.0          |Spark           |{10.0, 10.0, SPARK}           |
|20.0          |Big Data        |{20.0, 20.0, ataD giB}        |
|30.0          |AI              |{30.0, 30.0, AI}              |
|40.0          |Machine Learning|{40.0, 40.0, gninraeL enihcaM}|
|50.0          |Deep Learning   |{50.0, 50.0, gninraeL peeD}   |
+--------------+----------------+------------------------------+


```


Python UDTFs[#](#Python-UDTFs "Permalink to this headline")
-----------------------------------------------------------

A Python user-defined table function (UDTF) is a new kind of function that returns a table as output instead of a single scalar result value. Once registered, they can appear in the FROM clause of a SQL query.

### When to use Python UDTFs[#](#When-to-use-Python-UDTFs "Permalink to this headline")

In short, if you want a function that generates multiple rows and columns, and want to leverage the rich Python ecosystem, Python UDTFs are for you.

*   **Python UDTFs vs Python UDFs**: While Python UDFs in Spark are designed to each accept zero or more scalar values as input, and return a single value as output, UDTFs offer more flexibility. They can return multiple rows and columns, extending the capabilities of UDFs. Here are a few scenarios where UDTFs are particularly helpful:
    
    *   Exploding nested data types like arrays or structs, transforming it into multiple rows
        
    *   Dealing with string data that needs to be split into multiple parts, each represented as a separate row or multiple columns
        
    *   Generating rows based on input ranges, such as creating sequences of numbers, timestamps, or records for different dates
        
*   **Python UDTFs vs SQL UDTFs**: SQL UDTFs are efficient and versatile, but Python offers a richer set of libraries and tools. Compared to SQL, Python provides tools to enable advanced transformations or computations (e.g. statistical functions or machine learning inferences).
    

### To create a Python UDTF[#](#To-create-a-Python-UDTF "Permalink to this headline")

In the code below, we’ve created a simple UDTF that takes two integers as inputs and produces two columns as output: the original number and its square.

Note the use of the `yield` statement; A Python UDTF requires the return type to be either a tuple or a Row object so that the results can be processed properly.

Also note the return type must be a `StructType`with block-formatting or DDL string representing a `StructType` with block-formatting in Spark.

```
from pyspark.sql.functions import udtf

@udtf(returnType="num: int, squared: int")
class SquareNumbers:
    def eval(self, start: int, end: int):
        for num in range(start, end + 1):
            yield (num, num * num)

```


#### Arrow optimization[#](#id1 "Permalink to this headline")

Apache Arrow is an in-memory columnar data format that allows for efficient data transfers between Java and Python processes. It can significantly boost performance when the UDTF outputs many rows. Arrow-optimization can be enabled using `useArrow=True`, for example,

```
from pyspark.sql.functions import udtf

@udtf(returnType="num: int, squared: int", useArrow=True)
class SquareNumbers:
    ...

```


### To use a Python UDTF[#](#To-use-a-Python-UDTF "Permalink to this headline")

In Python, we can invoke a UDTF directly using the class name, as shown below.

```
from pyspark.sql.functions import lit

SquareNumbers(lit(1), lit(3)).show()

```


```
+---+-------+
|num|squared|
+---+-------+
|  1|      1|
|  2|      4|
|  3|      9|
+---+-------+


```


In SQL, we can register the Python UDTF and then use it in SQL as a table-valued function in the FROM clause of a query.

```
spark.sql("SELECT * FROM square_numbers(1, 3)").show()

```


### More Examples[#](#id2 "Permalink to this headline")

#### Example 1: Generating Numbers, Their Squares, Cubes, and Factorials for a Range[#](#Example-1:-Generating-Numbers,-Their-Squares,-Cubes,-and-Factorials-for-a-Range "Permalink to this headline")

```
from pyspark.sql.functions import lit, udtf
import math

@udtf(returnType="num: int, square: int, cube: int, factorial: int")
class GenerateComplexNumbers:
    def eval(self, start: int, end: int):
        for num in range(start, end + 1):
            yield (num, num ** 2, num ** 3, math.factorial(num))

GenerateComplexNumbers(lit(1), lit(5)).show()

```


```
+---+------+----+---------+
|num|square|cube|factorial|
+---+------+----+---------+
|  1|     1|   1|        1|
|  2|     4|   8|        2|
|  3|     9|  27|        6|
|  4|    16|  64|       24|
|  5|    25| 125|      120|
+---+------+----+---------+


```


#### Example 2: Splitting a Sentence into Words and Performing Multiple Operations[#](#Example-2:-Splitting-a-Sentence-into-Words-and-Performing-Multiple-Operations "Permalink to this headline")

```
from pyspark.sql.functions import lit, udtf

@udtf(returnType="word: string, length: int, is_palindrome: boolean")
class ProcessWords:
    def eval(self, sentence: str):
        words = sentence.split()  # Split sentence into words
        for word in words:
            is_palindrome = word == word[::-1]  # Check if the word is a palindrome
            yield (word, len(word), is_palindrome)

ProcessWords(lit("hello world")).show()

```


```
+-----+------+-------------+
| word|length|is_palindrome|
+-----+------+-------------+
|hello|     5|        false|
|world|     5|        false|
+-----+------+-------------+


```


#### Example 3: Parsing JSON String into Key-Value Pairs with Data Types[#](#Example-3:-Parsing-JSON-String-into-Key-Value-Pairs-with-Data-Types "Permalink to this headline")

```
import json
from pyspark.sql.functions import lit, udtf

@udtf(returnType="key: string, value: string, value_type: string")
class ParseJSON:
    def eval(self, json_str: str):
        try:
            json_data = json.loads(json_str)
            for key, value in json_data.items():
                value_type = type(value).__name__
                yield (key, str(value), value_type)
        except json.JSONDecodeError:
            yield ("Invalid JSON", "", "")

ParseJSON(lit('{"name": "Alice", "age": 25, "is_student": false}')).show()

```


```
+----------+-----+----------+
|       key|value|value_type|
+----------+-----+----------+
|      name|Alice|       str|
|       age|   25|       int|
|is_student|False|      bool|
+----------+-----+----------+


```
