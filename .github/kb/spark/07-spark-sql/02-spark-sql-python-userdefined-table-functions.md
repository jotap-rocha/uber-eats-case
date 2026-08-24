# Python User-defined Table Functions (UDTFs) — PySpark 4.0.1 documentation
Spark 3.5 introduces the Python user-defined table function (UDTF), a new type of user-defined function. Unlike scalar functions that return a single result value from each call, each UDTF is invoked in the `FROM` clause of a query and returns an entire table as output. Each UDTF call can accept zero or more arguments. These arguments can either be scalar expressions or table arguments that represent entire input tables.

Implementing a Python UDTF[#](#implementing-a-python-udtf "Permalink to this headline")
---------------------------------------------------------------------------------------

To implement a Python UDTF, you first need to define a class implementing the methods:

```
class PythonUDTF:

    def __init__(self) -> None:
        """
        Initializes the user-defined table function (UDTF). This is optional.

        This method serves as the default constructor and is called once when the
        UDTF is instantiated on the executor side.

        Any class fields assigned in this method will be available for subsequent
        calls to the `eval` and `terminate` methods. This class instance will remain
        alive until all rows in the current partition have been consumed by the `eval`
        method.

        Notes
        -----
        - You cannot create or reference the Spark session within the UDTF. Any
          attempt to do so will result in a serialization error.
        - If the below `analyze` method is implemented, it is also possible to define this
          method as: `__init__(self, analyze_result: AnalyzeResult)`. In this case, the result
          of the `analyze` method is passed into all future instantiations of this UDTF class.
          In this way, the UDTF may inspect the schema and metadata of the output table as
          needed during execution of other methods in this class. Note that it is possible to
          create a subclass of the `AnalyzeResult` class if desired for purposes of passing
          custom information generated just once during UDTF analysis to other method calls;
          this can be especially useful if this initialization is expensive.
        """
        ...

    @staticmethod
    def analyze(self, *args: AnalyzeArgument) -> AnalyzeResult:
        """
        Static method to compute the output schema of a particular call to this function in
        response to the arguments provided.

        This method is optional and only needed if the registration of the UDTF did not provide
        a static output schema to be use for all calls to the function. In this context,
        `output schema` refers to the ordered list of the names and types of the columns in the
        function's result table.

        This method accepts zero or more parameters mapping 1:1 with the arguments provided to
        the particular UDTF call under consideration. Each parameter is an instance of the
        `AnalyzeArgument` class.

        `AnalyzeArgument` fields
        ------------------------
        dataType: DataType
            Indicates the type of the provided input argument to this particular UDTF call.
            For input table arguments, this is a StructType representing the table's columns.
        value: Optional[Any]
            The value of the provided input argument to this particular UDTF call. This is
            `None` for table arguments, or for literal scalar arguments that are not constant.
        isTable: bool
            This is true if the provided input argument to this particular UDTF call is a
            table argument.
        isConstantExpression: bool
            This is true if the provided input argument to this particular UDTF call is either a
            literal or other constant-foldable scalar expression.

        This method returns an instance of the `AnalyzeResult` class which includes the result
        table's schema as a StructType. If the UDTF accepts an input table argument, then the
        `AnalyzeResult` can also include a requested way to partition and order the rows of
        the input table across several UDTF calls. See below for more information about UDTF
        table arguments and how to call them in SQL queries, including the WITH SINGLE
        PARTITION clause (corresponding to the `withSinglePartition` field here), PARTITION BY
        clause (corresponding to the `partitionBy` field here), ORDER BY clause (corresponding
        to the `orderBy` field here), and passing table subqueries as arguments (corresponding
        to the `select` field here).

        `AnalyzeResult` fields
        ----------------------
        schema: StructType
            The schema of the result table.
        withSinglePartition: bool = False
            If True, the query planner will arrange a repartitioning operation from the previous
            execution stage such that all rows of the input table are consumed by the `eval`
            method from exactly one instance of the UDTF class.
        partitionBy: Sequence[PartitioningColumn] = field(default_factory=tuple)
            If non-empty, the query planner will arrange a repartitioning such that all rows
            with each unique combination of values of the partitioning expressions are consumed
            by a separate unique instance of the UDTF class.
        orderBy: Sequence[OrderingColumn] = field(default_factory=tuple)
            If non-empty, this specifies the requested ordering of rows within each partition.
        select: Sequence[SelectedColumn] = field(default_factory=tuple)
            If non-empty, this is a sequence of expressions that the UDTF is specifying for
            Catalyst to evaluate against the columns in the input TABLE argument. The UDTF then
            receives one input attribute for each name in the list, in the order they are
            listed.

        Notes
        -----
        - It is possible for the `analyze` method to accept the exact arguments expected,
          mapping 1:1 with the arguments provided to the UDTF call.
        - The `analyze` method can instead choose to accept positional arguments if desired
          (using `*args`) or keyword arguments (using `**kwargs`).

        Examples
        --------
        This is an `analyze` implementation that returns one output column for each word in the
        input string argument.

        >>> @staticmethod
        ... def analyze(text: str) -> AnalyzeResult:
        ...     schema = StructType()
        ...     for index, word in enumerate(text.split(" ")):
        ...         schema = schema.add(f"word_{index}")
        ...     return AnalyzeResult(schema=schema)

        Same as above, but using *args to accept the arguments.

        >>> @staticmethod
        ... def analyze(*args) -> AnalyzeResult:
        ...     assert len(args) == 1, "This function accepts one argument only"
        ...     assert args[0].dataType == StringType(), "Only string arguments are supported"
        ...     text = args[0]
        ...     schema = StructType()
        ...     for index, word in enumerate(text.split(" ")):
        ...         schema = schema.add(f"word_{index}")
        ...     return AnalyzeResult(schema=schema)

        Same as above, but using **kwargs to accept the arguments.

        >>> @staticmethod
        ... def analyze(**kwargs) -> AnalyzeResult:
        ...     assert len(kwargs) == 1, "This function accepts one argument only"
        ...     assert "text" in kwargs, "An argument named 'text' is required"
        ...     assert kwargs["text"].dataType == StringType(), "Only strings are supported"
        ...     text = args["text"]
        ...     schema = StructType()
        ...     for index, word in enumerate(text.split(" ")):
        ...         schema = schema.add(f"word_{index}")
        ...     return AnalyzeResult(schema=schema)

        This is an `analyze` implementation that returns a constant output schema, but add
        custom information in the result metadata to be consumed by future __init__ method
        calls:

        >>> @staticmethod
        ... def analyze(text: str) -> AnalyzeResult:
        ...     @dataclass
        ...     class AnalyzeResultWithOtherMetadata(AnalyzeResult):
        ...         num_words: int
        ...         num_articles: int
        ...     words = text.split(" ")
        ...     return AnalyzeResultWithOtherMetadata(
        ...         schema=StructType()
        ...             .add("word", StringType())
        ...             .add('total", IntegerType()),
        ...         num_words=len(words),
        ...         num_articles=len((
        ...             word for word in words
        ...             if word == 'a' or word == 'an' or word == 'the')))

        This is an `analyze` implementation that returns a constant output schema, and also
        requests to select a subset of columns from the input table and for the input table to
        be partitioned across several UDTF calls based on the values of the `date` column.
        A SQL query may this UDTF passing a table argument like "SELECT * FROM udtf(TABLE(t))".
        Then this `analyze` method specifies additional constraints on the input table:
        (1) The input table must be partitioned across several UDTF calls based on the values of
            the month value of each `date` column.
        (2) The rows within each partition will arrive ordered by the `date` column.
        (3) The UDTF will only receive the `date` and `word` columns from the input table.

        >>> @staticmethod
        ... def analyze(*args) -> AnalyzeResult:
        ...     assert len(args) == 1, "This function accepts one argument only"
        ...     assert args[0].isTable, "Only table arguments are supported"
        ...     return AnalyzeResult(
        ...         schema=StructType()
        ...             .add("month", DateType())
        ...             .add('longest_word", IntegerType()),
        ...         partitionBy=[
        ...             PartitioningColumn("extract(month from date)")],
        ...         orderBy=[
        ...             OrderingColumn("date")],
        ...         select=[
        ...             SelectedColumn("date"),
        ...             SelectedColumn(
        ...               name="length(word),
        ...               alias="length_word")])
        """
        ...

    def eval(self, *args: Any) -> Iterator[Any]:
        """
        Evaluates the function using the given input arguments.

        This method is required and must be implemented.

        Argument Mapping:
        - Each provided scalar expression maps to exactly one value in the
          `*args` list.
        - Each provided table argument maps to a pyspark.sql.Row object containing
          the columns in the order they appear in the provided input table,
          and with the names computed by the query analyzer.

        This method is called on every input row, and can produce zero or more
        output rows. Each element in the output tuple corresponds to one column
        specified in the return type of the UDTF.

        Parameters
        ----------
        *args : Any
            Arbitrary positional arguments representing the input to the UDTF.

        Yields
        ------
        tuple
            A tuple, list, or pyspark.sql.Row object representing a single row in the UDTF
            result table. Yield as many times as needed to produce multiple rows.

        Notes
        -----
        - It is also possible for UDTFs to accept the exact arguments expected, along with
          their types.
        - UDTFs can instead accept keyword arguments during the function call if needed.
        - The `eval` method can raise a `SkipRestOfInputTableException` to indicate that the
          UDTF wants to skip consuming all remaining rows from the current partition of the
          input table. This will cause the UDTF to proceed directly to the `terminate` method.
        - The `eval` method can raise any other exception to indicate that the UDTF should be
          aborted entirely. This will cause the UDTF to skip the `terminate` method and proceed
          directly to the `cleanup` method, and then the exception will be propagated to the
          query processor causing the invoking query to fail.

        Examples
        --------
        This `eval` method returns one row and one column for each input.

        >>> def eval(self, x: int):
        ...     yield (x, )

        This `eval` method returns two rows and two columns for each input.

        >>> def eval(self, x: int, y: int):
        ...     yield (x + y, x - y)
        ...     yield (y + x, y - x)

        Same as above, but using *args to accept the arguments:

        >>> def eval(self, *args):
        ...     assert len(args) == 2, "This function accepts two integer arguments only"
        ...     x = args[0]
        ...     y = args[1]
        ...     yield (x + y, x - y)
        ...     yield (y + x, y - x)

        Same as above, but using **kwargs to accept the arguments:

        >>> def eval(self, **kwargs):
        ...     assert len(kwargs) == 2, "This function accepts two integer arguments only"
        ...     x = kwargs["x"]
        ...     y = kwargs["y"]
        ...     yield (x + y, x - y)
        ...     yield (y + x, y - x)
        """
        ...

    def terminate(self) -> Iterator[Any]:
        """
        Called when the UDTF has successfully processed all input rows.

        This method is optional to implement and is useful for performing any
        finalization operations after the UDTF has finished processing
        all rows. It can also be used to yield additional rows if needed.
        Table functions that consume all rows in the entire input partition
        and then compute and return the entire output table can do so from
        this method as well (please be mindful of memory usage when doing
        this).

        If any exceptions occur during input row processing, this method
        won't be called.

        Yields
        ------
        tuple
            A tuple representing a single row in the UDTF result table.
            Yield this if you want to return additional rows during termination.

        Examples
        --------
        >>> def terminate(self) -> Iterator[Any]:
        >>>     yield "done", None
        """
        ...

    def cleanup(self) -> None:
        """
        Invoked after the UDTF completes processing input rows.

        This method is optional to implement and is useful for final cleanup
        regardless of whether the UDTF processed all input rows successfully
        or was aborted due to exceptions.

        Examples
        --------
        >>> def cleanup(self) -> None:
        >>>     self.conn.close()
        """
        ...

```


Defining the Output Schema[#](#defining-the-output-schema "Permalink to this headline")
---------------------------------------------------------------------------------------

The return type of the UDTF defines the schema of the table it outputs.

You can specify it either after the `@udtf` decorator or as a result from the `analyze` method.

It must be either a `StructType`:

```
StructType().add("c1", StringType())

```


or a DDL string representing a struct type:

Emitting Output Rows[#](#emitting-output-rows "Permalink to this headline")
---------------------------------------------------------------------------

The eval and terminate methods then emit zero or more output rows conforming to this schema by yielding tuples, lists, or `pyspark.sql.Row` objects.

For example, here we return a row by providing a tuple of three elements:

```
def eval(self, x, y, z):
    yield (x, y, z)

```


It is also acceptable to omit the parentheses:

```
def eval(self, x, y, z):
    yield x, y, z

```


Remember to add a trailing comma if returning a row with only one column!

```
def eval(self, x, y, z):
    yield x,

```


It is also possible to yield a `pyspark.sql.Row` object.

```
def eval(self, x, y, z)
    from pyspark.sql.types import Row
    yield Row(x, y, z)

```


This is an example of yielding output rows from the terminate method using a Python list. Usually it makes sense to store state inside the class for this purpose from earlier steps in the UDTF evaluation.

```
def terminate(self):
    yield [self.x, self.y, self.z]

```


Registering and Using Python UDTFs in SQL[#](#registering-and-using-python-udtfs-in-sql "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------

Python UDTFs can be registered and used in SQL queries.

```
from pyspark.sql.functions import udtf

@udtf(returnType="word: string")
class WordSplitter:
    def eval(self, text: str):
        for word in text.split(" "):
            yield (word.strip(),)

# Register the UDTF for use in Spark SQL.
spark.udtf.register("split_words", WordSplitter)

# Example: Using the UDTF in SQL.
spark.sql("SELECT * FROM split_words('hello world')").show()
# +-----+
# | word|
# +-----+
# |hello|
# |world|
# +-----+

# Example: Using the UDTF with a lateral join in SQL.
# The lateral join allows us to reference the columns and aliases
# in the previous FROM clause items as inputs to the UDTF.
spark.sql(
    "SELECT * FROM VALUES ('Hello World'), ('Apache Spark') t(text), "
    "LATERAL split_words(text)"
).show()
# +------------+------+
# |        text|  word|
# +------------+------+
# | Hello World| Hello|
# | Hello World| World|
# |Apache Spark|Apache|
# |Apache Spark| Spark|
# +------------+------+

```


Arrow Optimization[#](#arrow-optimization "Permalink to this headline")
-----------------------------------------------------------------------

Apache Arrow is an in-memory columnar data format used in Spark to efficiently transfer data between Java and Python processes. Apache Arrow is disabled by default for Python UDTFs.

Arrow can improve performance when each input row generates a large result table from the UDTF.

To enable Arrow optimization, set the `spark.sql.execution.pythonUDTF.arrow.enabled` configuration to `true`. You can also enable it by specifying the `useArrow` parameter when declaring the UDTF.

```
from pyspark.sql.functions import udtf

@udtf(returnType="c1: int, c2: int", useArrow=True)
class PlusOne:
    def eval(self, x: int):
        yield x, x + 1

```


For more details, please see [Apache Arrow in PySpark](../arrow_pandas.html).

UDTF Examples with Scalar Arguments[#](#udtf-examples-with-scalar-arguments "Permalink to this headline")
---------------------------------------------------------------------------------------------------------

Here is a simple example of a UDTF class implementation:

```
# Define the UDTF class and implement the required `eval` method.
class SquareNumbers:
    def eval(self, start: int, end: int):
        for num in range(start, end + 1):
            yield (num, num * num)

```


To make use of the UDTF, you’ll first need to instantiate it using the `@udtf` decorator:

```
from pyspark.sql.functions import lit, udtf

# Create a UDTF using the class definition and the `udtf` function.
square_num = udtf(SquareNumbers, returnType="num: int, squared: int")

# Invoke the UDTF in PySpark.
square_num(lit(1), lit(3)).show()
# +---+-------+
# |num|squared|
# +---+-------+
# |  1|      1|
# |  2|      4|
# |  3|      9|
# +---+-------+

```


An alternative way to create a UDTF is to use the [`udtf()`](about:blank/reference/pyspark.sql/api/pyspark.sql.functions.udtf.html#pyspark.sql.functions.udtf "pyspark.sql.functions.udtf") function:

```
from pyspark.sql.functions import lit, udtf

# Define a UDTF using the `udtf` decorator directly on the class.
@udtf(returnType="num: int, squared: int")
class SquareNumbers:
    def eval(self, start: int, end: int):
        for num in range(start, end + 1):
            yield (num, num * num)

# Invoke the UDTF in PySpark using the SquareNumbers class directly.
SquareNumbers(lit(1), lit(3)).show()
# +---+-------+
# |num|squared|
# +---+-------+
# |  1|      1|
# |  2|      4|
# |  3|      9|
# +---+-------+

```


Here is a Python UDTF that expands date ranges into individual dates:

```
from datetime import datetime, timedelta
from pyspark.sql.functions import lit, udtf

@udtf(returnType="date: string")
class DateExpander:
    def eval(self, start_date: str, end_date: str):
        current = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        while current <= end:
            yield (current.strftime('%Y-%m-%d'),)
            current += timedelta(days=1)

DateExpander(lit("2023-02-25"), lit("2023-03-01")).show()
# +----------+
# |      date|
# +----------+
# |2023-02-25|
# |2023-02-26|
# |2023-02-27|
# |2023-02-28|
# |2023-03-01|
# +----------+

```


Here is a Python UDTF with `__init__` and `terminate`:

```
from pyspark.sql.functions import udtf

@udtf(returnType="cnt: int")
class CountUDTF:
    def __init__(self):
        # Initialize the counter to 0 when an instance of the class is created.
        self.count = 0

    def eval(self, x: int):
        # Increment the counter by 1 for each input value received.
        self.count += 1

    def terminate(self):
        # Yield the final count when the UDTF is done processing.
        yield self.count,

spark.udtf.register("count_udtf", CountUDTF)
spark.sql("SELECT * FROM range(0, 10, 1, 1), LATERAL count_udtf(id)").show()
# +---+---+
# | id|cnt|
# +---+---+
# |  9| 10|
# +---+---+
spark.sql("SELECT * FROM range(0, 10, 1, 2), LATERAL count_udtf(id)").show()
# +---+---+
# | id|cnt|
# +---+---+
# |  4|  5|
# |  9|  5|
# +---+---+

```


Accepting an Input Table Argument[#](#accepting-an-input-table-argument "Permalink to this headline")
-----------------------------------------------------------------------------------------------------

The UDTF examples above show functions that accept scalar input arguments, such as integers or strings.

However, any Python UDTF can also accept an input table as an argument, and this can work in conjunction with scalar input argument(s) for the same function definition. You are allowed to have only one such table argument as input.

Then any SQL query can provide an input table using the `TABLE` keyword followed by parentheses surrounding an appropriate table identifier, like `TABLE(t)`. Alternatively, you can pass a table subquery, like `TABLE(SELECT a, b, c FROM t)` or `TABLE(SELECT t1.a, t2.b FROM t1 INNER JOIN t2 USING (key))`.

The input table argument is then represented as a `pyspark.sql.Row` argument to the `eval` method, with one call to the `eval` method for each row in the input table.

For example:

```
from pyspark.sql.functions import udtf
from pyspark.sql.types import Row

@udtf(returnType="id: int")
class FilterUDTF:
    def eval(self, row: Row):
        if row["id"] > 5:
            yield row["id"],

spark.udtf.register("filter_udtf", FilterUDTF)

spark.sql("SELECT * FROM filter_udtf(TABLE(SELECT * FROM range(10)))").show()
# +---+
# | id|
# +---+
# |  6|
# |  7|
# |  8|
# |  9|
# +---+

```


When calling a UDTF with a table argument, any SQL query can request that the input table be partitioned across several UDTF calls based on the values of one or more columns of the input table. To do so, specify the `PARTITION BY` clause in the function call after the `TABLE` argument. This provides a guaranteee that all input rows with each unique combination of values of the partitioning columns will get consumed by exactly one instance of the UDTF class.

Note that in addition to simple column references, the `PARTITION BY` clause also accepts arbitrary expressions based on columns of the input table. For example, you can specify the `LENGTH` of a string, extract a month from a date, or concatenate two values.

It is also possible to specify `WITH SINGLE PARTITION` instead of `PARTITION BY` to request only one partition wherein all input rows must be consumed by exactly one instance of the UDTF class.

Within each partition, you can optionally specify a required ordering of the input rows as the UDTF’s `eval` method consumes them. To do so, provide an `ORDER BY` clause after the `PARTITION BY` or `WITH SINGLE PARTITION` clause described above.

For example:

```
from pyspark.sql.functions import udtf
from pyspark.sql.types import Row

# Define and register a UDTF.
@udtf(returnType="a: string, b: int")
class FilterUDTF:
    def __init__(self):
        self.key = ""
        self.max = 0

    def eval(self, row: Row):
        self.key = row["a"]
        self.max = max(self.max, row["b"])

    def terminate(self):
        yield self.key, self.max

spark.udtf.register("filter_udtf", FilterUDTF)

# Create an input table with some example values.
spark.sql("DROP TABLE IF EXISTS values_table")
spark.sql("CREATE TABLE values_table (a STRING, b INT)")
spark.sql("INSERT INTO values_table VALUES ('abc', 2), ('abc', 4), ('def', 6), ('def', 8)")
spark.table("values_table").show()
# +-------+----+
# |     a |  b |
# +-------+----+
# | "abc" | 2  |
# | "abc" | 4  |
# | "def" | 6  |
# | "def" | 8  |
# +-------+----+

# Query the UDTF with the input table as an argument, and a directive to partition the input
# rows such that all rows with each unique value of the `a` column are processed by the same
# instance of the UDTF class. Within each partition, the rows are ordered by the `b` column.
spark.sql("""
    SELECT * FROM filter_udtf(TABLE(values_table) PARTITION BY a ORDER BY b) ORDER BY 1
    """).show()
# +-------+----+
# |     a |  b |
# +-------+----+
# | "abc" | 4  |
# | "def" | 8  |
# +-------+----+

# Query the UDTF with the input table as an argument, and a directive to partition the input
# rows such that all rows with each unique result of evaluating the "LENGTH(a)" expression are
# processed by the same instance of the UDTF class. Within each partition, the rows are ordered
# by the `b` column.
spark.sql("""
    SELECT * FROM filter_udtf(TABLE(values_table) PARTITION BY LENGTH(a) ORDER BY b) ORDER BY 1
    """).show()
# +-------+---+
# |     a | b |
# +-------+---+
# | "def" | 8 |
# +-------+---+

# Query the UDTF with the input table as an argument, and a directive to consider all the input
# rows in one single partition such that exactly once instance of the UDTF class consumes all of
# the input rows. Within each partition, the rows are ordered by the `b` column.
spark.sql("""
    SELECT * FROM filter_udtf(TABLE(values_table) WITH SINGLE PARTITION ORDER BY b) ORDER BY 1
    """).show()
# +-------+----+
# |     a |  b |
# +-------+----+
# | "def" | 8 |
# +-------+----+

# Clean up.
spark.sql("DROP TABLE values_table")

```


Note that in for each of these ways of partitioning the input table when calling UDTFs in SQL queries, there is a corresponding way for the UDTF’s `analyze` method to specify the same partitioning method automatically instead.

For example, instead of calling a UDTF as `SELECT * FROM udtf(TABLE(t) PARTITION BY a)`, you can update the `analyze` method to set the field `partitionBy=[PartitioningColumn("a")]` and simply call the function like `SELECT * FROM udtf(TABLE(t))`.

By the same token, instead of specifying `TABLE(t) WITH SINGLE PARTITION` in the SQL query, make `analyze` set the field `withSinglePartition=true` and then just pass `TABLE(t)`.

Instead of passing `TABLE(t) ORDER BY b` in the SQL query, you can make `analyze` set `orderBy=[OrderingColumn("b")]` and then just pass `TABLE(t)`.

Instead of passing `TABLE(SELECT a FROM t)` in the SQL query, you can make `analyze` set `select=[SelectedColumn("a")]` and then just pass `TABLE(t)`.