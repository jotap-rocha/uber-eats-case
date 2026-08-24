# Quickstart: Pandas API on Spark — PySpark 4.0.1 documentation
Quickstart: Pandas API on Spark[#](#Quickstart:-Pandas-API-on-Spark "Permalink to this headline")
-------------------------------------------------------------------------------------------------

This is a short introduction to pandas API on Spark, geared mainly for new users. This notebook shows you some key differences between pandas and pandas API on Spark. You can run this examples by yourself in ‘Live Notebook: pandas API on Spark’ at [the quickstart page](https://spark.apache.org/docs/latest/api/python/getting_started/index.html).

Customarily, we import pandas API on Spark as follows:

```
import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession

```


Object Creation[#](#Object-Creation "Permalink to this headline")
-----------------------------------------------------------------

Creating a pandas-on-Spark Series by passing a list of values, letting pandas API on Spark create a default integer index:

```
s = ps.Series([1, 3, 5, np.nan, 6, 8])

```


```
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64

```


Creating a pandas-on-Spark DataFrame by passing a dict of objects that can be converted to series-like.

```
psdf = ps.DataFrame(
    {'a': [1, 2, 3, 4, 5, 6],
     'b': [100, 200, 300, 400, 500, 600],
     'c': ["one", "two", "three", "four", "five", "six"]},
    index=[10, 20, 30, 40, 50, 60])

```



|   |a  |b  |c    |
|---|---|---|-----|
|10 |1  |100|one  |
|20 |2  |200|two  |
|30 |3  |300|three|
|40 |4  |400|four |
|50 |5  |500|five |
|60 |6  |600|six  |


Creating a pandas DataFrame by passing a numpy array, with a datetime index and labeled columns:

```
dates = pd.date_range('20130101', periods=6)

```


```
DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
               '2013-01-05', '2013-01-06'],
              dtype='datetime64[ns]', freq='D')

```


```
pdf = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

```



|          |A        |B        |C        |D        |
|----------|---------|---------|---------|---------|
|2013-01-01|0.912558 |-0.795645|-0.289115|0.187606 |
|2013-01-02|-0.059703|-1.233897|0.316625 |-1.226828|
|2013-01-03|0.332871 |-1.262010|-0.434844|-0.579920|
|2013-01-04|0.924016 |-1.022019|-0.405249|-1.036021|
|2013-01-05|-0.772209|-1.228099|0.068901 |0.896679 |
|2013-01-06|1.485582 |-0.709306|-0.202637|-0.248766|


Now, this pandas DataFrame can be converted to a pandas-on-Spark DataFrame

```
psdf = ps.from_pandas(pdf)

```


```
pyspark.pandas.frame.DataFrame

```


It looks and behaves the same as a pandas DataFrame.


|          |A        |B        |C        |D        |
|----------|---------|---------|---------|---------|
|2013-01-01|0.912558 |-0.795645|-0.289115|0.187606 |
|2013-01-02|-0.059703|-1.233897|0.316625 |-1.226828|
|2013-01-03|0.332871 |-1.262010|-0.434844|-0.579920|
|2013-01-04|0.924016 |-1.022019|-0.405249|-1.036021|
|2013-01-05|-0.772209|-1.228099|0.068901 |0.896679 |
|2013-01-06|1.485582 |-0.709306|-0.202637|-0.248766|


Also, it is possible to create a pandas-on-Spark DataFrame from Spark DataFrame easily.

Creating a Spark DataFrame from pandas DataFrame

```
spark = SparkSession.builder.getOrCreate()

```


```
sdf = spark.createDataFrame(pdf)

```


```
+--------------------+-------------------+--------------------+--------------------+
|                   A|                  B|                   C|                   D|
+--------------------+-------------------+--------------------+--------------------+
|    0.91255803205208|-0.7956452608556638|-0.28911463069772175| 0.18760566615081622|
|-0.05970271470242...| -1.233896949308984|  0.3166246451758431| -1.2268284000402265|
| 0.33287106947536615|-1.2620100816441786| -0.4348444277082644| -0.5799199651437185|
|  0.9240158461589916|-1.0220190956326003| -0.4052488880650239| -1.0360212104348547|
| -0.7722090016558953|-1.2280986385313222|  0.0689011451939635|  0.8966790729426755|
|  1.4855822995785612|-0.7093056426018517| -0.2026366848847041|-0.24876619876451092|
+--------------------+-------------------+--------------------+--------------------+


```


Creating pandas-on-Spark DataFrame from Spark DataFrame.


|   |A        |B        |C        |D        |
|---|---------|---------|---------|---------|
|0  |0.912558 |-0.795645|-0.289115|0.187606 |
|1  |-0.059703|-1.233897|0.316625 |-1.226828|
|2  |0.332871 |-1.262010|-0.434844|-0.579920|
|3  |0.924016 |-1.022019|-0.405249|-1.036021|
|4  |-0.772209|-1.228099|0.068901 |0.896679 |
|5  |1.485582 |-0.709306|-0.202637|-0.248766|


Having specific [dtypes](http://pandas.pydata.org/pandas-docs/stable/basics.html#basics-dtypes) . Types that are common to both Spark and pandas are currently supported.

```
A    float64
B    float64
C    float64
D    float64
dtype: object

```


Here is how to show top rows from the frame below.

Note that the data in a Spark dataframe does not preserve the natural order by default. The natural order can be preserved by setting `compute.ordered_head` option but it causes a performance overhead with sorting internally.


|   |A        |B        |C        |D        |
|---|---------|---------|---------|---------|
|0  |0.912558 |-0.795645|-0.289115|0.187606 |
|1  |-0.059703|-1.233897|0.316625 |-1.226828|
|2  |0.332871 |-1.262010|-0.434844|-0.579920|
|3  |0.924016 |-1.022019|-0.405249|-1.036021|
|4  |-0.772209|-1.228099|0.068901 |0.896679 |


Displaying the index, columns, and the underlying numpy data.

```
Index([0, 1, 2, 3, 4, 5], dtype='int64')

```


```
Index(['A', 'B', 'C', 'D'], dtype='object')

```


```
array([[ 0.91255803, -0.79564526, -0.28911463,  0.18760567],
       [-0.05970271, -1.23389695,  0.31662465, -1.2268284 ],
       [ 0.33287107, -1.26201008, -0.43484443, -0.57991997],
       [ 0.92401585, -1.0220191 , -0.40524889, -1.03602121],
       [-0.772209  , -1.22809864,  0.06890115,  0.89667907],
       [ 1.4855823 , -0.70930564, -0.20263668, -0.2487662 ]])

```


Showing a quick statistic summary of your data


|     |A        |B        |C        |D        |
|-----|---------|---------|---------|---------|
|count|6.000000 |6.000000 |6.000000 |6.000000 |
|mean |0.470519 |-1.041829|-0.157720|-0.334542|
|std  |0.809428 |0.241511 |0.294520 |0.793014 |
|min  |-0.772209|-1.262010|-0.434844|-1.226828|
|25%  |-0.059703|-1.233897|-0.405249|-1.036021|
|50%  |0.332871 |-1.228099|-0.289115|-0.579920|
|75%  |0.924016 |-0.795645|0.068901 |0.187606 |
|max  |1.485582 |-0.709306|0.316625 |0.896679 |


Transposing your data


|   |0        |1        |2        |3        |4        |5        |
|---|---------|---------|---------|---------|---------|---------|
|A  |0.912558 |-0.059703|0.332871 |0.924016 |-0.772209|1.485582 |
|B  |-0.795645|-1.233897|-1.262010|-1.022019|-1.228099|-0.709306|
|C  |-0.289115|0.316625 |-0.434844|-0.405249|0.068901 |-0.202637|
|D  |0.187606 |-1.226828|-0.579920|-1.036021|0.896679 |-0.248766|


Sorting by its index

```
psdf.sort_index(ascending=False)

```



|   |A        |B        |C        |D        |
|---|---------|---------|---------|---------|
|5  |1.485582 |-0.709306|-0.202637|-0.248766|
|4  |-0.772209|-1.228099|0.068901 |0.896679 |
|3  |0.924016 |-1.022019|-0.405249|-1.036021|
|2  |0.332871 |-1.262010|-0.434844|-0.579920|
|1  |-0.059703|-1.233897|0.316625 |-1.226828|
|0  |0.912558 |-0.795645|-0.289115|0.187606 |


Sorting by value


|   |A        |B        |C        |D        |
|---|---------|---------|---------|---------|
|2  |0.332871 |-1.262010|-0.434844|-0.579920|
|1  |-0.059703|-1.233897|0.316625 |-1.226828|
|4  |-0.772209|-1.228099|0.068901 |0.896679 |
|3  |0.924016 |-1.022019|-0.405249|-1.036021|
|0  |0.912558 |-0.795645|-0.289115|0.187606 |
|5  |1.485582 |-0.709306|-0.202637|-0.248766|


Missing Data[#](#Missing-Data "Permalink to this headline")
-----------------------------------------------------------

Pandas API on Spark primarily uses the value `np.nan` to represent missing data. It is by default not included in computations.

```
pdf1 = pdf.reindex(index=dates[0:4], columns=list(pdf.columns) + ['E'])

```


```
pdf1.loc[dates[0]:dates[1], 'E'] = 1

```


```
psdf1 = ps.from_pandas(pdf1)

```



|          |A        |B        |C        |D        |E  |
|----------|---------|---------|---------|---------|---|
|2013-01-01|0.912558 |-0.795645|-0.289115|0.187606 |1.0|
|2013-01-02|-0.059703|-1.233897|0.316625 |-1.226828|1.0|
|2013-01-03|0.332871 |-1.262010|-0.434844|-0.579920|NaN|
|2013-01-04|0.924016 |-1.022019|-0.405249|-1.036021|NaN|


To drop any rows that have missing data.


|          |A        |B        |C        |D        |E  |
|----------|---------|---------|---------|---------|---|
|2013-01-01|0.912558 |-0.795645|-0.289115|0.187606 |1.0|
|2013-01-02|-0.059703|-1.233897|0.316625 |-1.226828|1.0|


Filling missing data.


|          |A        |B        |C        |D        |E  |
|----------|---------|---------|---------|---------|---|
|2013-01-01|0.912558 |-0.795645|-0.289115|0.187606 |1.0|
|2013-01-02|-0.059703|-1.233897|0.316625 |-1.226828|1.0|
|2013-01-03|0.332871 |-1.262010|-0.434844|-0.579920|5.0|
|2013-01-04|0.924016 |-1.022019|-0.405249|-1.036021|5.0|


Operations[#](#Operations "Permalink to this headline")
-------------------------------------------------------

### Stats[#](#Stats "Permalink to this headline")

Performing a descriptive statistic:

```
A    0.470519
B   -1.041829
C   -0.157720
D   -0.334542
dtype: float64

```


### Spark Configurations[#](#Spark-Configurations "Permalink to this headline")

Various configurations in PySpark could be applied internally in pandas API on Spark. For example, you can enable Arrow optimization to hugely speed up internal pandas conversion. See also PySpark Usage Guide for Pandas with Apache Arrow in PySpark documentation.

```
prev = spark.conf.get("spark.sql.execution.arrow.pyspark.enabled")  # Keep its default value.
ps.set_option("compute.default_index_type", "distributed")  # Use default index prevent overhead.
import warnings
warnings.filterwarnings("ignore")  # Ignore warnings coming from Arrow optimizations.

```


```
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", True)
%timeit ps.range(300000).to_pandas()

```


```
900 ms ± 186 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

```


```
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", False)
%timeit ps.range(300000).to_pandas()

```


```
3.08 s ± 227 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

```


```
ps.reset_option("compute.default_index_type")
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", prev)  # Set its default value back.

```


Grouping[#](#Grouping "Permalink to this headline")
---------------------------------------------------

By “group by” we are referring to a process involving one or more of the following steps:

*   Splitting the data into groups based on some criteria
    
*   Applying a function to each group independently
    
*   Combining the results into a data structure
    

```
psdf = ps.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                    'B': ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                    'C': np.random.randn(8),
                    'D': np.random.randn(8)})

```



|   |A  |B    |C        |D        |
|---|---|-----|---------|---------|
|0  |foo|one  |1.039632 |-0.571950|
|1  |bar|one  |0.972089 |1.085353 |
|2  |foo|two  |-1.931621|-2.579164|
|3  |bar|three|-0.654371|-0.340704|
|4  |foo|two  |-0.157080|0.893736 |
|5  |bar|two  |0.882795 |0.024978 |
|6  |foo|one  |-0.149384|0.201667 |
|7  |foo|three|-1.355136|0.693883 |


Grouping and then applying the [sum()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sum.html) function to the resulting groups.


|   |B                |C        |D        |
|---|-----------------|---------|---------|
|A  |                 |         |         |
|bar|onethreetwo      |1.200513 |0.769627 |
|foo|onetwotwoonethree|-2.553589|-1.361828|


Grouping by multiple columns forms a hierarchical index, and again we can apply the sum function.

```
psdf.groupby(['A', 'B']).sum()

```



|   |         |C        |D        |
|---|---------|---------|---------|
|A  |B        |         |         |
|foo|one      |0.890248 |-0.370283|
|two|-2.088701|-1.685428|         |
|bar|three    |-0.654371|-0.340704|
|foo|three    |-1.355136|0.693883 |
|bar|two      |0.882795 |0.024978 |
|one|0.972089 |1.085353 |         |


Plotting[#](#Plotting "Permalink to this headline")
---------------------------------------------------

```
pser = pd.Series(np.random.randn(1000),
                 index=pd.date_range('1/1/2000', periods=1000))

```


On a DataFrame, the [plot()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.plot.html) method is a convenience to plot all of the columns with labels:

```
pdf = pd.DataFrame(np.random.randn(1000, 4), index=pser.index,
                   columns=['A', 'B', 'C', 'D'])

```


```
psdf = ps.from_pandas(pdf)

```


For more details, [Plotting](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/frame.html#plotting) documentation.

Getting data in/out[#](#Getting-data-in/out "Permalink to this headline")
-------------------------------------------------------------------------

### CSV[#](#CSV "Permalink to this headline")

CSV is straightforward and easy to use. See [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_csv.html) to write a CSV file and [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.read_csv.html) to read a CSV file.

```
psdf.to_csv('foo.csv')
ps.read_csv('foo.csv').head(10)

```



|   |A        |B        |C       |D        |
|---|---------|---------|--------|---------|
|0  |-1.187097|-0.134645|0.377094|-0.627217|
|1  |0.331741 |0.166218 |0.377094|-0.627217|
|2  |0.331741 |0.439450 |0.377094|0.365970 |
|3  |0.621620 |0.439450 |1.190180|0.365970 |
|4  |0.621620 |0.439450 |1.190180|0.365970 |
|5  |2.169198 |1.069183 |1.395642|0.365970 |
|6  |2.755738 |1.069183 |1.395642|1.045868 |
|7  |2.755738 |1.069183 |1.395642|1.045868 |
|8  |2.755738 |1.069183 |1.395642|1.045868 |
|9  |2.755738 |1.508732 |1.395642|1.556933 |


### Parquet[#](#Parquet "Permalink to this headline")

Parquet is an efficient and compact file format to read and write faster. See [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_parquet.html) to write a Parquet file and [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.read_parquet.html) to read a Parquet file.

```
psdf.to_parquet('bar.parquet')
ps.read_parquet('bar.parquet').head(10)

```



|   |A        |B        |C       |D        |
|---|---------|---------|--------|---------|
|0  |-1.187097|-0.134645|0.377094|-0.627217|
|1  |0.331741 |0.166218 |0.377094|-0.627217|
|2  |0.331741 |0.439450 |0.377094|0.365970 |
|3  |0.621620 |0.439450 |1.190180|0.365970 |
|4  |0.621620 |0.439450 |1.190180|0.365970 |
|5  |2.169198 |1.069183 |1.395642|0.365970 |
|6  |2.755738 |1.069183 |1.395642|1.045868 |
|7  |2.755738 |1.069183 |1.395642|1.045868 |
|8  |2.755738 |1.069183 |1.395642|1.045868 |
|9  |2.755738 |1.508732 |1.395642|1.556933 |


### Spark IO[#](#Spark-IO "Permalink to this headline")

In addition, pandas API on Spark fully supports Spark’s various datasources such as ORC and an external datasource. See [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_orc.html) to write it to the specified datasource and [here](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.read_orc.html) to read it from the datasource.

```
psdf.spark.to_spark_io('zoo.orc', format="orc")
ps.read_spark_io('zoo.orc', format="orc").head(10)

```



|   |A        |B        |C       |D        |
|---|---------|---------|--------|---------|
|0  |-1.187097|-0.134645|0.377094|-0.627217|
|1  |0.331741 |0.166218 |0.377094|-0.627217|
|2  |0.331741 |0.439450 |0.377094|0.365970 |
|3  |0.621620 |0.439450 |1.190180|0.365970 |
|4  |0.621620 |0.439450 |1.190180|0.365970 |
|5  |2.169198 |1.069183 |1.395642|0.365970 |
|6  |2.755738 |1.069183 |1.395642|1.045868 |
|7  |2.755738 |1.069183 |1.395642|1.045868 |
|8  |2.755738 |1.069183 |1.395642|1.045868 |
|9  |2.755738 |1.508732 |1.395642|1.556933 |


See the [Input/Output](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/io.html) documentation for more details.