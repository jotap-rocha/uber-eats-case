# Options and settings — PySpark 4.0.1 documentation
Pandas API on Spark has an options system that lets you customize some aspects of its behaviour, display-related options being those the user is most likely to adjust.

Options have a full “dotted-style”, case-insensitive name (e.g. `display.max_rows`). You can get/set options directly as attributes of the top-level `options` attribute:

```
>>> import pyspark.pandas as ps
>>> ps.options.display.max_rows
1000
>>> ps.options.display.max_rows = 10
>>> ps.options.display.max_rows
10

```


The API is composed of 3 relevant functions, available directly from the `pandas_on_spark` namespace:

*   [`get_option()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.get_option.html#pyspark.pandas.get_option "pyspark.pandas.get_option") / [`set_option()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.set_option.html#pyspark.pandas.set_option "pyspark.pandas.set_option") - get/set the value of a single option.
    
*   [`reset_option()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.reset_option.html#pyspark.pandas.reset_option "pyspark.pandas.reset_option") - reset one or more options to their default value.
    

**Note:** Developers can check out [pyspark.pandas/config.py](https://github.com/apache/spark/blob/master/python/pyspark/pandas/config.py) for more information.

```
>>> import pyspark.pandas as ps
>>> ps.get_option("display.max_rows")
1000
>>> ps.set_option("display.max_rows", 101)
>>> ps.get_option("display.max_rows")
101

```


Getting and setting options[#](#getting-and-setting-options "Permalink to this headline")
-----------------------------------------------------------------------------------------

As described above, [`get_option()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.get_option.html#pyspark.pandas.get_option "pyspark.pandas.get_option") and [`set_option()`](about:blank/reference/pyspark.pandas/api/pyspark.pandas.set_option.html#pyspark.pandas.set_option "pyspark.pandas.set_option") are available from the `pandas_on_spark` namespace. To change an option, call `set_option('option name', new_value)`.

```
>>> import pyspark.pandas as ps
>>> ps.get_option('compute.max_rows')
1000
>>> ps.set_option('compute.max_rows', 2000)
>>> ps.get_option('compute.max_rows')
2000

```


All options also have a default value, and you can use `reset_option` to do just that:

```
>>> import pyspark.pandas as ps
>>> ps.reset_option("display.max_rows")

```


```
>>> import pyspark.pandas as ps
>>> ps.get_option("display.max_rows")
1000
>>> ps.set_option("display.max_rows", 999)
>>> ps.get_option("display.max_rows")
999
>>> ps.reset_option("display.max_rows")
>>> ps.get_option("display.max_rows")
1000

```


`option_context` context manager has been exposed through the top-level API, allowing you to execute code with given option values. Option values are restored automatically when you exit the with block:

```
>>> with ps.option_context("display.max_rows", 10, "compute.max_rows", 5):
...    print(ps.get_option("display.max_rows"))
...    print(ps.get_option("compute.max_rows"))
10
5
>>> print(ps.get_option("display.max_rows"))
>>> print(ps.get_option("compute.max_rows"))
1000
1000

```


Operations on different DataFrames[#](#operations-on-different-dataframes "Permalink to this headline")
-------------------------------------------------------------------------------------------------------

Pandas API on Spark disallows the operations on different DataFrames (or Series) by default to prevent expensive operations. It internally performs a join operation which can be expensive in general.

This can be enabled by setting compute.ops\_on\_diff\_frames to True to allow such cases. See the examples below.

```
>>> import pyspark.pandas as ps
>>> ps.set_option('compute.ops_on_diff_frames', True)
>>> psdf1 = ps.range(5)
>>> psdf2 = ps.DataFrame({'id': [5, 4, 3]})
>>> (psdf1 - psdf2).sort_index()
    id
0 -5.0
1 -3.0
2 -1.0
3  NaN
4  NaN
>>> ps.reset_option('compute.ops_on_diff_frames')

```


```
>>> import pyspark.pandas as ps
>>> ps.set_option('compute.ops_on_diff_frames', True)
>>> psdf = ps.range(5)
>>> psser_a = ps.Series([1, 2, 3, 4])
>>> # 'psser_a' is not from 'psdf' DataFrame. So it is considered as a Series not from 'psdf'.
>>> psdf['new_col'] = psser_a
>>> psdf
   id  new_col
0   0      1.0
1   1      2.0
3   3      4.0
2   2      3.0
4   4      NaN
>>> ps.reset_option('compute.ops_on_diff_frames')

```


Default Index type[#](#default-index-type "Permalink to this headline")
-----------------------------------------------------------------------

In the pandas API on Spark, the default index is used in several cases, for instance, when Spark DataFrame is converted into pandas-on-Spark DataFrame. In this case, internally pandas API on Spark attaches a default index into pandas-on-Spark DataFrame.

There are several types of the default index that can be configured by compute.default\_index\_type as below:

**sequence**: It implements a sequence that increases one by one, by PySpark’s Window function without specifying a partition. Therefore, it can end up with a whole partition in a single node. This index type should be avoided when the data is large. See the example below:

```
>>> import pyspark.pandas as ps
>>> ps.set_option('compute.default_index_type', 'sequence')
>>> psdf = ps.range(3)
>>> ps.reset_option('compute.default_index_type')
>>> psdf.index
Index([0, 1, 2], dtype='int64')

```


This is conceptually equivalent to the PySpark example as below:

```
>>> from pyspark.sql import functions as sf, Window
>>> import pyspark.pandas as ps
>>> spark_df = ps.range(3).to_spark()
>>> sequential_index = sf.row_number().over(
...    Window.orderBy(sf.monotonically_increasing_id().asc())) - 1
>>> spark_df.select(sequential_index).rdd.map(lambda r: r[0]).collect()
[0, 1, 2]

```


**distributed-sequence** (default): It implements a sequence that increases one by one, by group-by and group-map approach in a distributed manner. It still generates the sequential index globally. If the default index must be the sequence in a large dataset, this index has to be used. See the example below:

```
>>> import pyspark.pandas as ps
>>> ps.set_option('compute.default_index_type', 'distributed-sequence')
>>> psdf = ps.range(3)
>>> ps.reset_option('compute.default_index_type')
>>> psdf.index
Index([0, 1, 2], dtype='int64')

```


This is conceptually equivalent to the PySpark example as below:

```
>>> import pyspark.pandas as ps
>>> spark_df = ps.range(3).to_spark()
>>> spark_df.rdd.zipWithIndex().map(lambda p: p[1]).collect()
[0, 1, 2]

```


Warning

Unlike `sequence`, since `distributed-sequence` is executed in a distributed environment, the rows corresponding to each index may vary although the index itself still remains globally sequential.

This happens because the rows are distributed across multiple partitions and nodes, leading to indeterministic row-to-index mappings when the data is loaded.

Additionally, when using operations such as `apply()`, `groupby()`, or `transform()`, a new `distributed-sequence` index may be generated, which does not necessarily match the original index of the DataFrame. This can result in misaligned row-to-index mappings, leading to incorrect calculations.

To avoid this issue, see [Handling index misalignment with distributed-sequence](about:blank/best_practices.html#handling-index-misalignment-with-distributed-sequence)

**distributed**: It implements a monotonically increasing sequence simply by using PySpark’s monotonically\_increasing\_id function in a fully distributed manner. The values are indeterministic. If the index does not have to be a sequence that increases one by one, this index should be used. Performance-wise, this index almost does not have any penalty compared to other index types. See the example below:

```
>>> import pyspark.pandas as ps
>>> ps.set_option('compute.default_index_type', 'distributed')
>>> psdf = ps.range(3)
>>> ps.reset_option('compute.default_index_type')
>>> psdf.index
Index([25769803776, 60129542144, 94489280512], dtype='int64')

```


This is conceptually equivalent to the PySpark example as below:

```
>>> from pyspark.sql import functions as sf
>>> import pyspark.pandas as ps
>>> spark_df = ps.range(3).to_spark()
>>> spark_df.select(sf.monotonically_increasing_id()) \
...     .rdd.map(lambda r: r[0]).collect()
[25769803776, 60129542144, 94489280512]

```


Warning

It is very unlikely for this type of index to be used for computing two different dataframes because it is not guaranteed to have the same indexes in two dataframes. If you use this default index and turn on compute.ops\_on\_diff\_frames, the result from the operations between two different DataFrames will likely be an unexpected output due to the indeterministic index values.

Available options[#](#available-options "Permalink to this headline")
---------------------------------------------------------------------



* Option: display.max_rows
  * Default: 1000
  * Description: This sets the maximum number of rows pandas-on-Sparkshould output when printing out various output. Forexample, this value determines the number of rows tobe shown at the repr() in a dataframe. Set None tounlimit the input length. Default is 1000.
* Option: compute.max_rows
  * Default: 1000
  * Description: ‘compute.max_rows’ sets the limit of the currentpandas-on-Spark DataFrame. Set None to unlimit theinput length. When the limit is set, it is executedby the shortcut by collecting the data into thedriver, and then using the pandas API. If the limitis unset, the operation is executed by PySpark.Default is 1000.
* Option: compute.shortcut_limit
  * Default: 1000
  * Description: ‘compute.shortcut_limit’ sets the limit for ashortcut. It computes the specified number of rowsand uses its schema. When the dataframe length islarger than this limit, pandas-on-Spark uses PySparkto compute.
* Option: compute.ops_on_diff_frames
  * Default: True
  * Description: This determines whether or not to operate between twodifferent dataframes. For example, ‘combine_frames’function internally performs a join operation whichcan be expensive in general. So, ifcompute.ops_on_diff_frames variable is not True,that method throws an exception.
* Option: compute.default_index_type
  * Default: ‘distributed-sequence’
  * Description: This sets the default index type: sequence,distributed and distributed-sequence.
* Option: compute.default_index_cache
  * Default: ‘MEMORY_AND_DISK_SER’
  * Description: This sets the default storage level for temporaryRDDs cached in distributed-sequence indexing: ‘NONE’,‘DISK_ONLY’, ‘DISK_ONLY_2’, ‘DISK_ONLY_3’,‘MEMORY_ONLY’, ‘MEMORY_ONLY_2’, ‘MEMORY_ONLY_SER’,‘MEMORY_ONLY_SER_2’, ‘MEMORY_AND_DISK’,‘MEMORY_AND_DISK_2’, ‘MEMORY_AND_DISK_SER’,‘MEMORY_AND_DISK_SER_2’, ‘OFF_HEAP’,‘LOCAL_CHECKPOINT’.
* Option: compute.ordered_head
  * Default: False
  * Description: ‘compute.ordered_head’ sets whether or not to operatehead with natural ordering. pandas-on-Spark does notguarantee the row ordering so head could returnsome rows from distributed partitions. If‘compute.ordered_head’ is set to True, pandas-on-Spark performs natural ordering beforehand, but itwill cause a performance overhead.
* Option: compute.eager_check
  * Default: True
  * Description: ‘compute.eager_check’ sets whether or not to launchsome Spark jobs just for the sake of validation. If‘compute.eager_check’ is set to True, pandas-on-Sparkperforms the validation beforehand, but it will causea performance overhead. Otherwise, pandas-on-Sparkskip the validation and will be slightly differentfrom pandas. Affected APIs: Series.dot,Series.asof, Series.compare,FractionalExtensionOps.astype,IntegralExtensionOps.astype,FractionalOps.astype, DecimalOps.astype, skipnaof statistical functions.
* Option: compute.isin_limit
  * Default: 80
  * Description: ‘compute.isin_limit’ sets the limit for filtering by‘Column.isin(list)’. If the length of the ‘list’ isabove the limit, broadcast join is used instead forbetter performance.
* Option: compute.pandas_fallback
  * Default: False
  * Description: ‘compute.pandas_fallback’ sets whether or not tofallback automatically to Pandas’ implementation.
* Option: compute.fail_on_ansi_mode
  * Default: True
  * Description: ‘compute.fail_on_ansi_mode’ sets whether or not workwith ANSI mode. If True, pandas API on Spark raisesan exception if the underlying Spark is working withANSI mode enabled; otherwise, it forces to workalthough it can cause unexpected behavior.
* Option: plotting.max_rows
  * Default: 1000
  * Description: ‘plotting.max_rows’ sets the visual limit on top-n-based plots such as plot.bar and plot.pie. If itis set to 1000, the first 1000 data points will beused for plotting. Default is 1000.
* Option: plotting.sample_ratio
  * Default: None
  * Description: ‘plotting.sample_ratio’ sets the proportion of datathat will be plotted for sample-based plots such asplot.line and plot.area. If not set, it isderived from ‘plotting.max_rows’, by calculating theratio of ‘plotting.max_rows’ to the total data size.
* Option: plotting.backend
  * Default: ‘plotly’
  * Description: Backend to use for plotting. Default is plotly.Supports any package that has a top-level .plotmethod. Known options are: [matplotlib, plotly].
