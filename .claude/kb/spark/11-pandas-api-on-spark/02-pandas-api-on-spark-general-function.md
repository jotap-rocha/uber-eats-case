# General functions — PySpark 4.0.1 documentation
Data manipulations and SQL[#](#data-manipulations-and-sql "Permalink to this headline")
---------------------------------------------------------------------------------------



* melt(frame[, id_vars, value_vars, var_name, ...]): merge(obj, right[, how, on, left_on, ...])
  * Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.: Merge DataFrame objects with a database-style join.
* melt(frame[, id_vars, value_vars, var_name, ...]): merge_asof(left, right[, on, left_on, ...])
  * Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.: Perform an asof merge.
* melt(frame[, id_vars, value_vars, var_name, ...]): get_dummies(data[, prefix, prefix_sep, ...])
  * Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.: Convert categorical variable into dummy/indicator variables, also known as one hot encoding.
* melt(frame[, id_vars, value_vars, var_name, ...]): concat(objs[, axis, join, ignore_index, sort])
  * Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.: Concatenate pandas-on-Spark objects along a particular axis with optional set logic along the other axes.
* melt(frame[, id_vars, value_vars, var_name, ...]): sql(query[, index_col, args])
  * Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.: Execute a SQL query and return the result as a pandas-on-Spark DataFrame.
* melt(frame[, id_vars, value_vars, var_name, ...]): broadcast(obj)
  * Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.: Marks a DataFrame as small enough for use in broadcast joins.


Top-level missing data[#](#top-level-missing-data "Permalink to this headline")
-------------------------------------------------------------------------------


|isna(obj)   |Detect missing values for an array-like object.|
|------------|-----------------------------------------------|
|isnull(obj) |Detect missing values for an array-like object.|
|notna(obj)  |Detect existing (non-missing) values.          |
|notnull(obj)|Detect existing (non-missing) values.          |


Top-level dealing with numeric data[#](#top-level-dealing-with-numeric-data "Permalink to this headline")
---------------------------------------------------------------------------------------------------------



Top-level dealing with datetimelike data[#](#top-level-dealing-with-datetimelike-data "Permalink to this headline")
-------------------------------------------------------------------------------------------------------------------



* to_datetime(arg[, errors, format, unit, ...]): date_range([start, end, periods, freq, tz, ...])
  * Convert argument to datetime.: Return a fixed frequency DatetimeIndex.
* to_datetime(arg[, errors, format, unit, ...]): to_timedelta(arg[, unit, errors])
  * Convert argument to datetime.: Convert argument to timedelta.
* to_datetime(arg[, errors, format, unit, ...]): timedelta_range([start, end, periods, freq, ...])
  * Convert argument to datetime.: Return a fixed frequency TimedeltaIndex, with day as the default frequency.

# pyspark.pandas.melt — PySpark 4.0.1 documentation
pyspark.pandas.melt(_frame_, _id\_vars\=None_, _value\_vars\=None_, _var\_name\=None_, _value\_name\='value'_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#melt)
[#](#pyspark.pandas.melt "Permalink to this definition")

Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.

This function is useful to massage a DataFrame into a format where one or more columns are identifier variables (id\_vars), while all other columns, considered measured variables (value\_vars), are “unpivoted” to the row axis, leaving just two non-identifier columns, ‘variable’ and ‘value’.

Parameters

**frame**DataFrame

**id\_vars**tuple, list, or ndarray, optional

Column(s) to use as identifier variables.

**value\_vars**tuple, list, or ndarray, optional

Column(s) to unpivot. If not specified, uses all columns that are not set as id\_vars.

**var\_name**scalar, default ‘variable’

Name to use for the ‘variable’ column. If None it uses frame.columns.name or ‘variable’.

**value\_name**scalar, default ‘value’

Name to use for the ‘value’ column.

Returns

DataFrame

Unpivoted DataFrame.

Examples

```
>>> df = ps.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
...                    'B': {0: 1, 1: 3, 2: 5},
...                    'C': {0: 2, 1: 4, 2: 6}},
...                   columns=['A', 'B', 'C'])
>>> df
   A  B  C
0  a  1  2
1  b  3  4
2  c  5  6

```


```
>>> ps.melt(df)
  variable value
0        A     a
1        B     1
2        C     2
3        A     b
4        B     3
5        C     4
6        A     c
7        B     5
8        C     6

```


```
>>> df.melt(id_vars='A')
   A variable  value
0  a        B      1
1  a        C      2
2  b        B      3
3  b        C      4
4  c        B      5
5  c        C      6

```


```
>>> df.melt(value_vars='A')
  variable value
0        A     a
1        A     b
2        A     c

```


```
>>> ps.melt(df, id_vars=['A', 'B'])
   A  B variable  value
0  a  1        C      2
1  b  3        C      4
2  c  5        C      6

```


```
>>> df.melt(id_vars=['A'], value_vars=['C'])
   A variable  value
0  a        C      2
1  b        C      4
2  c        C      6

```


The names of ‘variable’ and ‘value’ columns can be customized:

```
>>> ps.melt(df, id_vars=['A'], value_vars=['B'],
...         var_name='myVarname', value_name='myValname')
   A myVarname  myValname
0  a         B          1
1  b         B          3
2  c         B          5

```

# pyspark.pandas.merge — PySpark 4.0.1 documentation
pyspark.pandas.merge(_obj_, _right_, _how\='inner'_, _on\=None_, _left\_on\=None_, _right\_on\=None_, _left\_index\=False_, _right\_index\=False_, _suffixes\=('\_x', '\_y')_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#merge)
[#](#pyspark.pandas.merge "Permalink to this definition")

Merge DataFrame objects with a database-style join.

The index of the resulting DataFrame will be one of the following:

*   0…n if no index is used for merging
    
*   Index of the left DataFrame if merged only on the index of the right DataFrame
    
*   Index of the right DataFrame if merged only on the index of the left DataFrame
    
*   All involved indices if merged using the indices of both DataFrames
    
    e.g. if left with indices (a, x) and right with indices (b, x), the result will be an index (x, a, b)
    

Parameters

**right: Object to merge with.**

**how: Type of merge to be performed.**

{‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘inner’

left: use only keys from left frame, like a SQL left outer join; preserve key

order.

right: use only keys from right frame, like a SQL right outer join; preserve key

order.

outer: use union of keys from both frames, like a SQL full outer join; sort keys

lexicographically.

inner: use intersection of keys from both frames, like a SQL inner join;

preserve the order of the left keys.

**on: Column or index level names to join on. These must be found in both DataFrames. If on**

is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames.

**left\_on: Column or index level names to join on in the left DataFrame. Can also**

be an array or list of arrays of the length of the left DataFrame. These arrays are treated as if they are columns.

**right\_on: Column or index level names to join on in the right DataFrame. Can also**

be an array or list of arrays of the length of the right DataFrame. These arrays are treated as if they are columns.

**left\_index: Use the index from the left DataFrame as the join key(s). If it is a**

MultiIndex, the number of keys in the other DataFrame (either the index or a number of columns) must match the number of levels.

**right\_index: Use the index from the right DataFrame as the join key. Same caveats as**

left\_index.

**suffixes: Suffix to apply to overlapping column names in the left and right side,**

respectively.

Returns

DataFrame

A DataFrame of the two merged objects.

Notes

As described in #263, joining string columns currently returns None for missing values

instead of NaN.

Examples

```
>>> df1 = ps.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [1, 2, 3, 5]},
...                    columns=['lkey', 'value'])
>>> df2 = ps.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [5, 6, 7, 8]},
...                    columns=['rkey', 'value'])
>>> df1
  lkey  value
0  foo      1
1  bar      2
2  baz      3
3  foo      5
>>> df2
  rkey  value
0  foo      5
1  bar      6
2  baz      7
3  foo      8

```


Merge df1 and df2 on the lkey and rkey columns. The value columns have the default suffixes, \_x and \_y, appended.

```
>>> merged = ps.merge(df1, df2, left_on='lkey', right_on='rkey')
>>> merged.sort_values(by=['lkey', 'value_x', 'rkey', 'value_y'])  
  lkey  value_x rkey  value_y
...bar        2  bar        6
...baz        3  baz        7
...foo        1  foo        5
...foo        1  foo        8
...foo        5  foo        5
...foo        5  foo        8

```


```
>>> left_psdf = ps.DataFrame({'A': [1, 2]})
>>> right_psdf = ps.DataFrame({'B': ['x', 'y']}, index=[1, 2])

```


```
>>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True).sort_index()
   A  B
1  2  x

```


```
>>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True, how='left').sort_index()
   A     B
0  1  None
1  2     x

```


```
>>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True, how='right').sort_index()
     A  B
1  2.0  x
2  NaN  y

```


```
>>> ps.merge(left_psdf, right_psdf, left_index=True, right_index=True, how='outer').sort_index()
     A     B
0  1.0  None
1  2.0     x
2  NaN     y

```


# pyspark.pandas.merge_asof — PySpark 4.0.1 documentation
pyspark.pandas.merge\_asof(_left_, _right_, _on\=None_, _left\_on\=None_, _right\_on\=None_, _left\_index\=False_, _right\_index\=False_, _by\=None_, _left\_by\=None_, _right\_by\=None_, _suffixes\=('\_x', '\_y')_, _tolerance\=None_, _allow\_exact\_matches\=True_, _direction\='backward'_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#merge_asof)
[#](#pyspark.pandas.merge_asof "Permalink to this definition")

Perform an asof merge.

This is like a left-join except that we match on nearest key rather than equal keys.

For each row in the left DataFrame:

> *   A “backward” search selects the last row in the right DataFrame whose ‘on’ key is less than or equal to the left’s key.
>     
> *   A “forward” search selects the first row in the right DataFrame whose ‘on’ key is greater than or equal to the left’s key.
>     
> *   A “nearest” search selects the row in the right DataFrame who’s ‘on’ key is closest in absolute distance to the left’s key.
>     

Optionally match on equivalent keys with ‘by’ before searching with ‘on’.

New in version 3.3.0.

Parameters

**left**DataFrame or named Series

**right**DataFrame or named Series

**on**label

Field name to join on. Must be found in both DataFrames. The data MUST be ordered. This must be a numeric column, such as datetimelike, integer, or float. On or left\_on/right\_on must be given.

**left\_on**label

Field name to join on in left DataFrame.

**right\_on**label

Field name to join on in right DataFrame.

**left\_index**bool

Use the index of the left DataFrame as the join key.

**right\_index**bool

Use the index of the right DataFrame as the join key.

**by**column name or list of column names

Match on these columns before performing merge operation.

**left\_by**column name

Field names to match on in the left DataFrame.

**right\_by**column name

Field names to match on in the right DataFrame.

**suffixes**2-length sequence (tuple, list, …)

Suffix to apply to overlapping column names in the left and right side, respectively.

**tolerance**int or Timedelta, optional, default None

Select asof tolerance within this range; must be compatible with the merge index.

**allow\_exact\_matches**bool, default True

*   If True, allow matching with the same ‘on’ value (i.e. less-than-or-equal-to / greater-than-or-equal-to)
    
*   If False, don’t match the same ‘on’ value (i.e., strictly less-than / strictly greater-than).
    

**direction**‘backward’ (default), ‘forward’, or ‘nearest’

Whether to search for prior, subsequent, or closest matches.

Returns

**merged**DataFrame

See also

[`merge`](about:blank/pyspark.pandas.merge.html#pyspark.pandas.merge "pyspark.pandas.merge")

Merge with a database-style join.

`merge_ordered`

Merge with optional filling/interpolation.

Examples

```
>>> left = ps.DataFrame({"a": [1, 5, 10], "left_val": ["a", "b", "c"]})
>>> left
    a left_val
0   1        a
1   5        b
2  10        c

```


```
>>> right = ps.DataFrame({"a": [1, 2, 3, 6, 7], "right_val": [1, 2, 3, 6, 7]})
>>> right
   a  right_val
0  1          1
1  2          2
2  3          3
3  6          6
4  7          7

```


```
>>> ps.merge_asof(left, right, on="a").sort_values("a").reset_index(drop=True)
    a left_val  right_val
0   1        a          1
1   5        b          3
2  10        c          7

```


```
>>> ps.merge_asof(
...     left,
...     right,
...     on="a",
...     allow_exact_matches=False
... ).sort_values("a").reset_index(drop=True)
    a left_val  right_val
0   1        a        NaN
1   5        b        3.0
2  10        c        7.0

```


```
>>> ps.merge_asof(
...     left,
...     right,
...     on="a",
...     direction="forward"
... ).sort_values("a").reset_index(drop=True)
    a left_val  right_val
0   1        a        1.0
1   5        b        6.0
2  10        c        NaN

```


```
>>> ps.merge_asof(
...     left,
...     right,
...     on="a",
...     direction="nearest"
... ).sort_values("a").reset_index(drop=True)
    a left_val  right_val
0   1        a          1
1   5        b          6
2  10        c          7

```


We can use indexed DataFrames as well.

```
>>> left = ps.DataFrame({"left_val": ["a", "b", "c"]}, index=[1, 5, 10])
>>> left
   left_val
1         a
5         b
10        c

```


```
>>> right = ps.DataFrame({"right_val": [1, 2, 3, 6, 7]}, index=[1, 2, 3, 6, 7])
>>> right
   right_val
1          1
2          2
3          3
6          6
7          7

```


```
>>> ps.merge_asof(left, right, left_index=True, right_index=True).sort_index()
   left_val  right_val
1         a          1
5         b          3
10        c          7

```


Here is a real-world times-series example

```
>>> quotes = ps.DataFrame(
...     {
...         "time": [
...             pd.Timestamp("2016-05-25 13:30:00.023"),
...             pd.Timestamp("2016-05-25 13:30:00.023"),
...             pd.Timestamp("2016-05-25 13:30:00.030"),
...             pd.Timestamp("2016-05-25 13:30:00.041"),
...             pd.Timestamp("2016-05-25 13:30:00.048"),
...             pd.Timestamp("2016-05-25 13:30:00.049"),
...             pd.Timestamp("2016-05-25 13:30:00.072"),
...             pd.Timestamp("2016-05-25 13:30:00.075")
...         ],
...         "ticker": [
...                "GOOG",
...                "MSFT",
...                "MSFT",
...                "MSFT",
...                "GOOG",
...                "AAPL",
...                "GOOG",
...                "MSFT"
...            ],
...            "bid": [720.50, 51.95, 51.97, 51.99, 720.50, 97.99, 720.50, 52.01],
...            "ask": [720.93, 51.96, 51.98, 52.00, 720.93, 98.01, 720.88, 52.03]
...     }
... )
>>> quotes
                     time ticker     bid     ask
0 2016-05-25 13:30:00.023   GOOG  720.50  720.93
1 2016-05-25 13:30:00.023   MSFT   51.95   51.96
2 2016-05-25 13:30:00.030   MSFT   51.97   51.98
3 2016-05-25 13:30:00.041   MSFT   51.99   52.00
4 2016-05-25 13:30:00.048   GOOG  720.50  720.93
5 2016-05-25 13:30:00.049   AAPL   97.99   98.01
6 2016-05-25 13:30:00.072   GOOG  720.50  720.88
7 2016-05-25 13:30:00.075   MSFT   52.01   52.03

```


```
>>> trades = ps.DataFrame(
...        {
...            "time": [
...                pd.Timestamp("2016-05-25 13:30:00.023"),
...                pd.Timestamp("2016-05-25 13:30:00.038"),
...                pd.Timestamp("2016-05-25 13:30:00.048"),
...                pd.Timestamp("2016-05-25 13:30:00.048"),
...                pd.Timestamp("2016-05-25 13:30:00.048")
...            ],
...            "ticker": ["MSFT", "MSFT", "GOOG", "GOOG", "AAPL"],
...            "price": [51.95, 51.95, 720.77, 720.92, 98.0],
...            "quantity": [75, 155, 100, 100, 100]
...        }
...    )
>>> trades
                     time ticker   price  quantity
0 2016-05-25 13:30:00.023   MSFT   51.95        75
1 2016-05-25 13:30:00.038   MSFT   51.95       155
2 2016-05-25 13:30:00.048   GOOG  720.77       100
3 2016-05-25 13:30:00.048   GOOG  720.92       100
4 2016-05-25 13:30:00.048   AAPL   98.00       100

```


By default we are taking the asof of the quotes

```
>>> ps.merge_asof(
...    trades, quotes, on="time", by="ticker"
... ).sort_values(["time", "ticker", "price"]).reset_index(drop=True)
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
2 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
3 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
4 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93

```


We only asof within 2ms between the quote time and the trade time

```
>>> ps.merge_asof(
...     trades,
...     quotes,
...     on="time",
...     by="ticker",
...     tolerance=sf.expr("INTERVAL 2 MILLISECONDS")  # pd.Timedelta("2ms")
... ).sort_values(["time", "ticker", "price"]).reset_index(drop=True)
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75   51.95   51.96
1 2016-05-25 13:30:00.038   MSFT   51.95       155     NaN     NaN
2 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
3 2016-05-25 13:30:00.048   GOOG  720.77       100  720.50  720.93
4 2016-05-25 13:30:00.048   GOOG  720.92       100  720.50  720.93

```


We only asof within 10ms between the quote time and the trade time and we exclude exact matches on time. However _prior_ data will propagate forward

```
>>> ps.merge_asof(
...     trades,
...     quotes,
...     on="time",
...     by="ticker",
...     tolerance=sf.expr("INTERVAL 10 MILLISECONDS"),  # pd.Timedelta("10ms")
...     allow_exact_matches=False
... ).sort_values(["time", "ticker", "price"]).reset_index(drop=True)
                     time ticker   price  quantity     bid     ask
0 2016-05-25 13:30:00.023   MSFT   51.95        75     NaN     NaN
1 2016-05-25 13:30:00.038   MSFT   51.95       155   51.97   51.98
2 2016-05-25 13:30:00.048   AAPL   98.00       100     NaN     NaN
3 2016-05-25 13:30:00.048   GOOG  720.77       100     NaN     NaN
4 2016-05-25 13:30:00.048   GOOG  720.92       100     NaN     NaN

```

# pyspark.pandas.get_dummies — PySpark 4.0.1 documentation
pyspark.pandas.get\_dummies(_data_, _prefix\=None_, _prefix\_sep\='\_'_, _dummy\_na\=False_, _columns\=None_, _sparse\=False_, _drop\_first\=False_, _dtype\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#get_dummies)
[#](#pyspark.pandas.get_dummies "Permalink to this definition")

Convert categorical variable into dummy/indicator variables, also known as one hot encoding.

Parameters

**data**array-like, Series, or DataFrame

**prefix**string, list of strings, or dict of strings, default None

String to append DataFrame column names. Pass a list with length equal to the number of columns when calling get\_dummies on a DataFrame. Alternatively, prefix can be a dictionary mapping column names to prefixes.

**prefix\_sep**string, default ‘\_’

If appending prefix, separator/delimiter to use. Or pass a list or dictionary as with prefix.

**dummy\_na**bool, default False

Add a column to indicate NaNs, if False NaNs are ignored.

**columns**list-like, default None

Column names in the DataFrame to be encoded. If columns is None then all the columns with object or category dtype will be converted.

**sparse**bool, default False

Whether the dummy-encoded columns should be be backed by a `SparseArray` (True) or a regular NumPy array (False). In pandas-on-Spark, this value must be “False”.

**drop\_first**bool, default False

Whether to get k-1 dummies out of k categorical levels by removing the first level.

**dtype**dtype, default np.uint8

Data type for new columns. Only a single dtype is allowed.

Returns

**dummies**DataFrame

Examples

```
>>> s = ps.Series(list('abca'))

```


```
>>> ps.get_dummies(s)
   a  b  c
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0

```


```
>>> df = ps.DataFrame({'A': ['a', 'b', 'a'], 'B': ['b', 'a', 'c'],
...                    'C': [1, 2, 3]},
...                   columns=['A', 'B', 'C'])

```


```
>>> ps.get_dummies(df, prefix=['col1', 'col2'])
   C  col1_a  col1_b  col2_a  col2_b  col2_c
0  1       1       0       0       1       0
1  2       0       1       1       0       0
2  3       1       0       0       0       1

```


```
>>> ps.get_dummies(ps.Series(list('abcaa')))
   a  b  c
0  1  0  0
1  0  1  0
2  0  0  1
3  1  0  0
4  1  0  0

```


```
>>> ps.get_dummies(ps.Series(list('abcaa')), drop_first=True)
   b  c
0  0  0
1  1  0
2  0  1
3  0  0
4  0  0

```


```
>>> ps.get_dummies(ps.Series(list('abc')), dtype=float)
     a    b    c
0  1.0  0.0  0.0
1  0.0  1.0  0.0
2  0.0  0.0  1.0

```


# pyspark.pandas.concat — PySpark 4.0.1 documentation
pyspark.pandas.concat(_objs_, _axis\=0_, _join\='outer'_, _ignore\_index\=False_, _sort\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#concat)
[#](#pyspark.pandas.concat "Permalink to this definition")

Concatenate pandas-on-Spark objects along a particular axis with optional set logic along the other axes.

Parameters

**objs**a sequence of Series or DataFrame

Any None objects will be dropped silently unless they are all None in which case a ValueError will be raised

**axis**{0/’index’, 1/’columns’}, default 0

The axis to concatenate along.

**join**{‘inner’, ‘outer’}, default ‘outer’

How to handle indexes on other axis (or axes).

**ignore\_index**bool, default False

If True, do not use the index values along the concatenation axis. The resulting axis will be labeled 0, …, n - 1. This is useful if you are concatenating objects where the concatenation axis does not have meaningful indexing information. Note the index values on the other axes are still respected in the join.

**sort**bool, default False

Sort non-concatenation axis if it is not already aligned.

Returns

object, type of objs

When concatenating all `Series` along the index (axis=0), a `Series` is returned. When `objs` contains at least one `DataFrame`, a `DataFrame` is returned. When concatenating along the columns (axis=1), a `DataFrame` is returned.

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)

```


Combine two `Series`.

```
>>> s1 = ps.Series(['a', 'b'])
>>> s2 = ps.Series(['c', 'd'])
>>> ps.concat([s1, s2])
0    a
1    b
0    c
1    d
dtype: object

```


Clear the existing index and reset it in the result by setting the `ignore_index` option to `True`.

```
>>> ps.concat([s1, s2], ignore_index=True)
0    a
1    b
2    c
3    d
dtype: object

```


Combine two `DataFrame` objects with identical columns.

```
>>> df1 = ps.DataFrame([['a', 1], ['b', 2]],
...                    columns=['letter', 'number'])
>>> df1
  letter  number
0      a       1
1      b       2
>>> df2 = ps.DataFrame([['c', 3], ['d', 4]],
...                    columns=['letter', 'number'])
>>> df2
  letter  number
0      c       3
1      d       4

```


```
>>> ps.concat([df1, df2])
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4

```


Combine `DataFrame` and `Series` objects with different columns.

```
>>> ps.concat([df2, s1])
  letter  number     0
0      c     3.0  None
1      d     4.0  None
0   None     NaN     a
1   None     NaN     b

```


Combine `DataFrame` objects with overlapping columns and return everything. Columns outside the intersection will be filled with `None` values.

```
>>> df3 = ps.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],
...                    columns=['letter', 'number', 'animal'])
>>> df3
  letter  number animal
0      c       3    cat
1      d       4    dog

```


```
>>> ps.concat([df1, df3])
  letter  number animal
0      a       1   None
1      b       2   None
0      c       3    cat
1      d       4    dog

```


Sort the columns.

```
>>> ps.concat([df1, df3], sort=True)
  animal letter  number
0   None      a       1
1   None      b       2
0    cat      c       3
1    dog      d       4

```


Combine `DataFrame` objects with overlapping columns and return only those that are shared by passing `inner` to the `join` keyword argument.

```
>>> ps.concat([df1, df3], join="inner")
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4

```


```
>>> df4 = ps.DataFrame([['bird', 'polly'], ['monkey', 'george']],
...                    columns=['animal', 'name'])

```


Combine with column axis.

```
>>> ps.concat([df1, df4], axis=1)
  letter  number  animal    name
0      a       1    bird   polly
1      b       2  monkey  george

```


```
>>> reset_option("compute.ops_on_diff_frames")

```



# pyspark.pandas.sql — PySpark 4.0.1 documentation
pyspark.pandas.sql(_query_, _index\_col\=None_, _args\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/sql_formatter.html#sql)
[#](#pyspark.pandas.sql "Permalink to this definition")

Execute a SQL query and return the result as a pandas-on-Spark DataFrame.

This function acts as a standard Python string formatter with understanding the following variable types:

> *   pandas-on-Spark DataFrame
>     
> *   pandas-on-Spark Series
>     
> *   pandas DataFrame
>     
> *   pandas Series
>     
> *   string
>     

Also the method can bind named parameters to SQL literals from args.

Note

pandas-on-Spark DataFrame is not supported for Spark Connect.

Parameters

**query**str

the SQL query

**index\_col**str or list of str, optional

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

Note

If you want to preserve the index, explicitly use [`DataFrame.reset_index()`](about:blank/pyspark.pandas.DataFrame.reset_index.html#pyspark.pandas.DataFrame.reset_index "pyspark.pandas.DataFrame.reset_index"), and pass it to the SQL statement with index\_col parameter.

For example,

```
>>> psdf = ps.DataFrame({"A": [1, 2, 3], "B":[4, 5, 6]}, index=['a', 'b', 'c'])
>>> new_psdf = psdf.reset_index()
>>> ps.sql("SELECT * FROM {new_psdf}", index_col="index", new_psdf=new_psdf)
... 
       A  B
index
a      1  4
b      2  5
c      3  6

```


For MultiIndex,

```
>>> psdf = ps.DataFrame(
...     {"A": [1, 2, 3], "B": [4, 5, 6]},
...     index=pd.MultiIndex.from_tuples(
...         [("a", "b"), ("c", "d"), ("e", "f")], names=["index1", "index2"]
...     ),
... )
>>> new_psdf = psdf.reset_index()
>>> ps.sql(
...     "SELECT * FROM {new_psdf}", index_col=["index1", "index2"], new_psdf=new_psdf)
... 
               A  B
index1 index2
a      b       1  4
c      d       2  5
e      f       3  6

```


Also note that the index name(s) should be matched to the existing name.

**args**dict or list

A dictionary of parameter names to Python objects or a list of Python objects that can be converted to SQL literal expressions. See [Supported Data Types](https://spark.apache.org/docs/latest/sql-ref-datatypes.html) for supported value types in Python. For example, dictionary keys: “rank”, “name”, “birthdate”; dictionary values: 1, “Steven”, datetime.date(2023, 4, 2). A value can be also a Column of a literal or collection constructor functions such as map(), array(), struct(), in that case it is taken as is.

New in version 3.4.0.

Changed in version 3.5.0: Added positional parameters.

**kwargs**

other variables that the user want to set that can be referenced in the query

Returns

pandas-on-Spark DataFrame

Examples

Calling a built-in SQL function.

```
>>> ps.sql("SELECT * FROM range(10) where id > 7")
   id
0   8
1   9

```


```
>>> ps.sql("SELECT * FROM range(10) WHERE id > {bound1} AND id < {bound2}", bound1=7, bound2=9)
   id
0   8

```


```
>>> mydf = ps.range(10)
>>> x = tuple(range(4))
>>> ps.sql("SELECT {ser} FROM {mydf} WHERE id IN {x}", ser=mydf.id, mydf=mydf, x=x)
   id
0   0
1   1
2   2
3   3

```


Mixing pandas-on-Spark and pandas DataFrames in a join operation. Note that the index is dropped.

```
>>> ps.sql('''
...   SELECT m1.a, m2.b
...   FROM {table1} m1 INNER JOIN {table2} m2
...   ON m1.key = m2.key
...   ORDER BY m1.a, m2.b''',
...   table1=ps.DataFrame({"a": [1,2], "key": ["a", "b"]}),
...   table2=pd.DataFrame({"b": [3,4,5], "key": ["a", "b", "b"]}))
   a  b
0  1  3
1  2  4
2  2  5

```


Also, it is possible to query using Series.

```
>>> psdf = ps.DataFrame({"A": [1, 2, 3], "B":[4, 5, 6]}, index=['a', 'b', 'c'])
>>> ps.sql("SELECT {mydf.A} FROM {mydf}", mydf=psdf)
   A
0  1
1  2
2  3

```


And substitute named parameters with the : prefix by SQL literals.

```
>>> ps.sql("SELECT * FROM range(10) WHERE id > :bound1", args={"bound1":7})
   id
0   8
1   9

```


Or positional parameters marked by ? in the SQL query by SQL literals.

```
>>> ps.sql("SELECT * FROM range(10) WHERE id > ?", args=[7])
   id
0   8
1   9

```

# pyspark.pandas.broadcast — PySpark 4.0.1 documentation
pyspark.pandas.broadcast(_obj_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#broadcast)
[#](#pyspark.pandas.broadcast "Permalink to this definition")

Marks a DataFrame as small enough for use in broadcast joins.

Parameters

**obj**DataFrame

Returns

**ret**DataFrame with broadcast hint.

See also

[`DataFrame.merge`](about:blank/pyspark.pandas.DataFrame.merge.html#pyspark.pandas.DataFrame.merge "pyspark.pandas.DataFrame.merge")

Merge DataFrame objects with a database-style join.

[`DataFrame.join`](about:blank/pyspark.pandas.DataFrame.join.html#pyspark.pandas.DataFrame.join "pyspark.pandas.DataFrame.join")

Join columns of another DataFrame.

[`DataFrame.update`](about:blank/pyspark.pandas.DataFrame.update.html#pyspark.pandas.DataFrame.update "pyspark.pandas.DataFrame.update")

Modify in place using non-NA values from another DataFrame.

`DataFrame.hint`

Specifies some hint on the current DataFrame.

Examples

```
>>> df1 = ps.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [1, 2, 3, 5]},
...                    columns=['lkey', 'value']).set_index('lkey')
>>> df2 = ps.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [5, 6, 7, 8]},
...                    columns=['rkey', 'value']).set_index('rkey')
>>> merged = df1.merge(ps.broadcast(df2), left_index=True, right_index=True)
>>> merged.spark.explain()  
== Physical Plan ==
...
...BroadcastHashJoin...
...

```

# pyspark.pandas.isna — PySpark 4.0.1 documentation
pyspark.pandas.isna(_obj_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#isna)
[#](#pyspark.pandas.isna "Permalink to this definition")

Detect missing values for an array-like object.

This function takes a scalar or array-like object and indicates whether values are missing (`NaN` in numeric arrays, `None` or `NaN` in object arrays).

Parameters

**obj**scalar or array-like

Object to check for null or missing values.

Returns

bool or array-like of bool

For scalar input, returns a scalar boolean. For array input, returns an array of boolean indicating whether each corresponding element is missing.

Examples

Scalar arguments (including strings) result in a scalar boolean.

ndarrays result in an ndarray of booleans.

```
>>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
>>> array
array([[ 1., nan,  3.],
       [ 4.,  5., nan]])
>>> ps.isna(array)
array([[False,  True, False],
       [False, False,  True]])

```


For Series and DataFrame, the same type is returned, containing booleans.

```
>>> df = ps.DataFrame({'a': ['ant', 'bee', 'cat'], 'b': ['dog', None, 'fly']})
>>> df
     a     b
0  ant   dog
1  bee  None
2  cat   fly

```


```
>>> ps.isna(df)
       a      b
0  False  False
1  False   True
2  False  False

```


```
>>> ps.isnull(df.b)
0    False
1     True
2    False
Name: b, dtype: bool

```


# pyspark.pandas.isnull — PySpark 4.0.1 documentation
pyspark.pandas.isnull(_obj_)
[#](#pyspark.pandas.isnull "Permalink to this definition")

Detect missing values for an array-like object.

This function takes a scalar or array-like object and indicates whether values are missing (`NaN` in numeric arrays, `None` or `NaN` in object arrays).

Parameters

**obj**scalar or array-like

Object to check for null or missing values.

Returns

bool or array-like of bool

For scalar input, returns a scalar boolean. For array input, returns an array of boolean indicating whether each corresponding element is missing.

Examples

Scalar arguments (including strings) result in a scalar boolean.

ndarrays result in an ndarray of booleans.

```
>>> array = np.array([[1, np.nan, 3], [4, 5, np.nan]])
>>> array
array([[ 1., nan,  3.],
       [ 4.,  5., nan]])
>>> ps.isna(array)
array([[False,  True, False],
       [False, False,  True]])

```


For Series and DataFrame, the same type is returned, containing booleans.

```
>>> df = ps.DataFrame({'a': ['ant', 'bee', 'cat'], 'b': ['dog', None, 'fly']})
>>> df
     a     b
0  ant   dog
1  bee  None
2  cat   fly

```


```
>>> ps.isna(df)
       a      b
0  False  False
1  False   True
2  False  False

```


```
>>> ps.isnull(df.b)
0    False
1     True
2    False
Name: b, dtype: bool

```


# pyspark.pandas.notna — PySpark 4.0.1 documentation
pyspark.pandas.notna(_obj_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#notna)
[#](#pyspark.pandas.notna "Permalink to this definition")

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. NA values, such as None or `numpy.NaN`, get mapped to False values.

Returns

bool or array-like of bool

Mask of bool values for each element that indicates whether an element is not an NA value.

Examples

Show which entries in a DataFrame are not NA.

```
>>> df = ps.DataFrame({'age': [5, 6, np.nan],
...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
...                             pd.Timestamp('1940-04-25')],
...                    'name': ['Alfred', 'Batman', ''],
...                    'toy': [None, 'Batmobile', 'Joker']})
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

```


```
>>> df.notnull()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

```


Show which entries in a Series are not NA.

```
>>> ser = ps.Series([5, 6, np.nan])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

```


```
>>> ps.notna(ser)
0     True
1     True
2    False
dtype: bool

```


```
>>> ps.notna(ser.index)
True

```


# pyspark.pandas.notnull — PySpark 4.0.1 documentation
pyspark.pandas.notnull(_obj_)
[#](#pyspark.pandas.notnull "Permalink to this definition")

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. NA values, such as None or `numpy.NaN`, get mapped to False values.

Returns

bool or array-like of bool

Mask of bool values for each element that indicates whether an element is not an NA value.

Examples

Show which entries in a DataFrame are not NA.

```
>>> df = ps.DataFrame({'age': [5, 6, np.nan],
...                    'born': [pd.NaT, pd.Timestamp('1939-05-27'),
...                             pd.Timestamp('1940-04-25')],
...                    'name': ['Alfred', 'Batman', ''],
...                    'toy': [None, 'Batmobile', 'Joker']})
>>> df
   age       born    name        toy
0  5.0        NaT  Alfred       None
1  6.0 1939-05-27  Batman  Batmobile
2  NaN 1940-04-25              Joker

```


```
>>> df.notnull()
     age   born  name    toy
0   True  False  True  False
1   True   True  True   True
2  False   True  True   True

```


Show which entries in a Series are not NA.

```
>>> ser = ps.Series([5, 6, np.nan])
>>> ser
0    5.0
1    6.0
2    NaN
dtype: float64

```


```
>>> ps.notna(ser)
0     True
1     True
2    False
dtype: bool

```


```
>>> ps.notna(ser.index)
True

```




# pyspark.pandas.to_numeric — PySpark 4.0.1 documentation
pyspark.pandas.to\_numeric(_arg_, _errors\='raise'_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#to_numeric)
[#](#pyspark.pandas.to_numeric "Permalink to this definition")

Convert argument to a numeric type.

Parameters

**arg**scalar, list, tuple, 1-d array, or Series

Argument to be converted.

**errors**{‘raise’, ‘coerce’}, default ‘raise’

*   If ‘coerce’, then invalid parsing will be set as NaN.
    
*   If ‘raise’, then invalid parsing will raise an exception.
    
*   If ‘ignore’, then invalid parsing will return the input.
    

Note

‘ignore’ doesn’t work yet when arg is pandas-on-Spark Series.

Returns

**ret**numeric if parsing succeeded.

See also

[`DataFrame.astype`](about:blank/pyspark.pandas.DataFrame.astype.html#pyspark.pandas.DataFrame.astype "pyspark.pandas.DataFrame.astype")

Cast argument to a specified dtype.

[`to_datetime`](about:blank/pyspark.pandas.to_datetime.html#pyspark.pandas.to_datetime "pyspark.pandas.to_datetime")

Convert argument to datetime.

[`to_timedelta`](about:blank/pyspark.pandas.to_timedelta.html#pyspark.pandas.to_timedelta "pyspark.pandas.to_timedelta")

Convert argument to timedelta.

`numpy.ndarray.astype`

Cast a numpy array to a specified type.

Examples

```
>>> psser = ps.Series(['1.0', '2', '-3'])
>>> psser
0    1.0
1      2
2     -3
dtype: object

```


```
>>> ps.to_numeric(psser)
0    1.0
1    2.0
2   -3.0
dtype: float32

```


If given Series contains invalid value to cast float, just cast it to np.nan when errors is set to “coerce”.

```
>>> psser = ps.Series(['apple', '1.0', '2', '-3'])
>>> psser
0    apple
1      1.0
2        2
3       -3
dtype: object

```


```
>>> ps.to_numeric(psser, errors="coerce")
0    NaN
1    1.0
2    2.0
3   -3.0
dtype: float32

```


Also support for list, tuple, np.array, or a scalar

```
>>> ps.to_numeric(['1.0', '2', '-3'])
array([ 1.,  2., -3.])

```


```
>>> ps.to_numeric(('1.0', '2', '-3'))
array([ 1.,  2., -3.])

```


```
>>> ps.to_numeric(np.array(['1.0', '2', '-3']))
array([ 1.,  2., -3.])

```


```
>>> ps.to_numeric('1.0')
1.0

```



# pyspark.pandas.to_datetime — PySpark 4.0.1 documentation
pyspark.pandas.to\_datetime(_arg_, _errors\='raise'_, _format\=None_, _unit\=None_, _infer\_datetime\_format\=False_, _origin\='unix'_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#to_datetime)
[#](#pyspark.pandas.to_datetime "Permalink to this definition")

Convert argument to datetime.

Parameters

**arg**integer, float, string, datetime, list, tuple, 1-d array, Series

or DataFrame/dict-like

**errors**{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’

*   If ‘raise’, then invalid parsing will raise an exception
    
*   If ‘coerce’, then invalid parsing will be set as NaT
    
*   If ‘ignore’, then invalid parsing will return the input
    

**format**string, default None

strftime to parse time, eg “%d/%m/%Y”, note that “%f” will parse all the way up to nanoseconds.

**unit**string, default None

unit of the arg (D,s,ms,us,ns) denote the unit, which is an integer or float number. This will be based off the origin. Example, with unit=’ms’ and origin=’unix’ (the default), this would calculate the number of milliseconds to the unix epoch start.

**infer\_datetime\_format**boolean, default False

If True and no format is given, attempt to infer the format of the datetime strings, and if it can be inferred, switch to a faster method of parsing them. In some cases this can increase the parsing speed by ~5-10x.

**origin**scalar, default ‘unix’

Define the reference date. The numeric values would be parsed as number of units (defined by unit) since this reference date.

*   If ‘unix’ (or POSIX) time; origin is set to 1970-01-01.
    
*   If ‘julian’, unit must be ‘D’, and origin is set to beginning of Julian Calendar. Julian day number 0 is assigned to the day starting at noon on January 1, 4713 BC.
    
*   If Timestamp convertible, origin is set to Timestamp identified by origin.
    

Returns

**ret**datetime if parsing succeeded.

Return type depends on input:

*   list-like: DatetimeIndex
    
*   Series: Series of datetime64 dtype
    
*   scalar: Timestamp
    

In case when it is not possible to return designated types (e.g. when any element of input is before Timestamp.min or after Timestamp.max) return will have datetime.datetime type (or corresponding array/Series).

Examples

Assembling a datetime from multiple columns of a DataFrame. The keys can be common abbreviations like \[‘year’, ‘month’, ‘day’, ‘minute’, ‘second’, ‘ms’, ‘us’, ‘ns’\]) or plurals of the same

```
>>> df = ps.DataFrame({'year': [2015, 2016],
...                    'month': [2, 3],
...                    'day': [4, 5]})
>>> ps.to_datetime(df)
0   2015-02-04
1   2016-03-05
dtype: datetime64[ns]

```


If a date does not meet the [timestamp limitations](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#timeseries-timestamp-limits), passing errors=’ignore’ will return the original input instead of raising any exception.

Passing errors=’coerce’ will force an out-of-bounds date to NaT, in addition to forcing non-dates (or non-parseable dates) to NaT.

```
>>> ps.to_datetime('13000101', format='%Y%m%d', errors='ignore')  
datetime.datetime(1300, 1, 1, 0, 0)
>>> ps.to_datetime('13000101', format='%Y%m%d', errors='coerce')
NaT

```


Passing infer\_datetime\_format=True can often-times speedup a parsing if its not an ISO8601 format exactly, but in a regular format.

```
>>> s = ps.Series(['3/11/2000', '3/12/2000', '3/13/2000'] * 1000)
>>> s.head()
0    3/11/2000
1    3/12/2000
2    3/13/2000
3    3/11/2000
4    3/12/2000
dtype: object

```


```
>>> import timeit
>>> timeit.timeit(
...    lambda: repr(ps.to_datetime(s, infer_datetime_format=True)),
...    number = 1)  
0.35832712500000063

```


```
>>> timeit.timeit(
...    lambda: repr(ps.to_datetime(s, infer_datetime_format=False)),
...    number = 1)  
0.8895321660000004

```


Using a unix epoch time

```
>>> ps.to_datetime(1490195805, unit='s')
Timestamp('2017-03-22 15:16:45')
>>> ps.to_datetime(1490195805433502912, unit='ns')
Timestamp('2017-03-22 15:16:45.433502912')

```


Using a non-unix epoch origin

```
>>> ps.to_datetime([1, 2, 3], unit='D', origin=pd.Timestamp('1960-01-01'))
DatetimeIndex(['1960-01-02', '1960-01-03', '1960-01-04'], dtype='datetime64[ns]', freq=None)

```



# pyspark.pandas.date_range — PySpark 4.0.1 documentation
pyspark.pandas.date\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\=None_, _tz\=None_, _normalize\=False_, _name\=None_, _inclusive\='both'_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#date_range)
[#](#pyspark.pandas.date_range "Permalink to this definition")

Return a fixed frequency DatetimeIndex.

Parameters

**start**str or datetime-like, optional

Left bound for generating dates.

**end**str or datetime-like, optional

Right bound for generating dates.

**periods**int, optional

Number of periods to generate.

**freq**str or DateOffset, default ‘D’

Frequency strings can have multiples, e.g. ‘5H’.

**tz**str or tzinfo, optional

Time zone name for returning localized DatetimeIndex, for example ‘Asia/Hong\_Kong’. By default, the resulting DatetimeIndex is time zone naive.

**normalize**bool, default False

Normalize start/end dates to midnight before generating date range.

**name**str, default None

Name of the resulting DatetimeIndex.

**inclusive**{“both”, “neither”, “left”, “right”}, default “both”

Include boundaries; Whether to set each bound as closed or open.

New in version 4.0.0.

**\*\*kwargs**

For compatibility. Has no effect on the result.

Returns

**rng**DatetimeIndex

Notes

Of the four parameters `start`, `end`, `periods`, and `freq`, exactly three must be specified. If `freq` is omitted, the resulting `DatetimeIndex` will have `periods` linearly spaced elements between `start` and `end` (closed on both sides).

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases).

Examples

**Specifying the values**

The next four examples generate the same DatetimeIndex, but vary the combination of start, end and periods.

Specify start and end, with the default daily frequency.

```
>>> ps.date_range(start='1/1/2018', end='1/08/2018')  
DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
              dtype='datetime64[ns]', freq=None)

```


Specify start and periods, the number of periods (days).

```
>>> ps.date_range(start='1/1/2018', periods=8)  
DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
               '2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08'],
              dtype='datetime64[ns]', freq=None)

```


Specify end and periods, the number of periods (days).

```
>>> ps.date_range(end='1/1/2018', periods=8)  
DatetimeIndex(['2017-12-25', '2017-12-26', '2017-12-27', '2017-12-28',
               '2017-12-29', '2017-12-30', '2017-12-31', '2018-01-01'],
              dtype='datetime64[ns]', freq=None)

```


Specify start, end, and periods; the frequency is generated automatically (linearly spaced).

```
>>> ps.date_range(
...     start='2018-04-24', end='2018-04-27', periods=3
... )  
DatetimeIndex(['2018-04-24 00:00:00', '2018-04-25 12:00:00',
               '2018-04-27 00:00:00'],
              dtype='datetime64[ns]', freq=None)

```


**Other Parameters**

Changed the freq (frequency) to `'M'` (month end frequency).

```
>>> ps.date_range(start='1/1/2018', periods=5, freq='ME')  
DatetimeIndex(['2018-01-31', '2018-02-28', '2018-03-31', '2018-04-30',
               '2018-05-31'],
              dtype='datetime64[ns]', freq=None)

```


Multiples are allowed

```
>>> ps.date_range(start='1/1/2018', periods=5, freq='3M')  
DatetimeIndex(['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',
               '2019-01-31'],
              dtype='datetime64[ns]', freq=None)

```


freq can also be specified as an Offset object.

```
>>> ps.date_range(
...     start='1/1/2018', periods=5, freq=pd.offsets.MonthEnd(3)
... )  
DatetimeIndex(['2018-01-31', '2018-04-30', '2018-07-31', '2018-10-31',
               '2019-01-31'],
              dtype='datetime64[ns]', freq=None)

```


inclusive controls whether to include start and end that are on the boundary. The default includes boundary points on either end.

```
>>> ps.date_range(
...     start='2017-01-01', end='2017-01-04', inclusive="both"
... )  
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04'],
               dtype='datetime64[ns]', freq=None)

```


Use `inclusive='left'` to exclude end if it falls on the boundary.

```
>>> ps.date_range(
...     start='2017-01-01', end='2017-01-04', inclusive='left'
... )  
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03'], dtype='datetime64[ns]', freq=None)

```


Use `inclusive='right'` to exclude start if it falls on the boundary.

```
>>> ps.date_range(
...     start='2017-01-01', end='2017-01-04', inclusive='right'
... )  
DatetimeIndex(['2017-01-02', '2017-01-03', '2017-01-04'], dtype='datetime64[ns]', freq=None)

```



# pyspark.pandas.to_timedelta — PySpark 4.0.1 documentation
pyspark.pandas.to\_timedelta(_arg_, _unit\=None_, _errors\='raise'_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#to_timedelta)
[#](#pyspark.pandas.to_timedelta "Permalink to this definition")

Convert argument to timedelta.

Parameters

**arg**str, timedelta, list-like or Series

The data to be converted to timedelta.

**unit**str, optional

Denotes the unit of the arg for numeric arg. Defaults to `"ns"`.

Possible values: \* ‘W’ \* ‘D’ / ‘days’ / ‘day’ \* ‘hours’ / ‘hour’ / ‘hr’ / ‘h’ \* ‘m’ / ‘minute’ / ‘min’ / ‘minutes’ / ‘T’ \* ‘S’ / ‘seconds’ / ‘sec’ / ‘second’ \* ‘ms’ / ‘milliseconds’ / ‘millisecond’ / ‘milli’ / ‘millis’ / ‘L’ \* ‘us’ / ‘microseconds’ / ‘microsecond’ / ‘micro’ / ‘micros’ / ‘U’ \* ‘ns’ / ‘nanoseconds’ / ‘nano’ / ‘nanos’ / ‘nanosecond’ / ‘N’

Must not be specified when arg context strings and `errors="raise"`.

Deprecated since version 4.0.0: Units ‘T’ and ‘L’ are deprecated and will be removed in a future version.

**errors**{‘ignore’, ‘raise’, ‘coerce’}, default ‘raise’

*   If ‘raise’, then invalid parsing will raise an exception.
    
*   If ‘coerce’, then invalid parsing will be set as NaT.
    
*   If ‘ignore’, then invalid parsing will return the input.
    

Returns

**ret**timedelta64, TimedeltaIndex or Series of timedelta64 if parsing succeeded.

Notes

If the precision is higher than nanoseconds, the precision of the duration is truncated to nanoseconds for string inputs.

Examples

Parsing a single string to a Timedelta:

```
>>> ps.to_timedelta('1 days 06:05:01.00003')
Timedelta('1 days 06:05:01.000030')
>>> ps.to_timedelta('15.5us')  
Timedelta('0 days 00:00:00.000015500')

```


Parsing a list or array of strings:

```
>>> ps.to_timedelta(['1 days 06:05:01.00003', '15.5us', 'nan'])  
TimedeltaIndex(['1 days 06:05:01.000030', '0 days 00:00:00.000015500', NaT],
               dtype='timedelta64[ns]', freq=None)

```


Converting numbers by specifying the unit keyword argument:

```
>>> ps.to_timedelta(np.arange(5), unit='s')  
TimedeltaIndex(['0 days 00:00:00', '0 days 00:00:01', '0 days 00:00:02',
                '0 days 00:00:03', '0 days 00:00:04'],
               dtype='timedelta64[ns]', freq=None)
>>> ps.to_timedelta(np.arange(5), unit='d')  
TimedeltaIndex(['0 days', '1 days', '2 days', '3 days', '4 days'],
               dtype='timedelta64[ns]', freq=None)

```


# pyspark.pandas.timedelta_range — PySpark 4.0.1 documentation
pyspark.pandas.timedelta\_range(_start\=None_, _end\=None_, _periods\=None_, _freq\=None_, _name\=None_, _closed\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/namespace.html#timedelta_range)
[#](#pyspark.pandas.timedelta_range "Permalink to this definition")

Return a fixed frequency TimedeltaIndex, with day as the default frequency.

Parameters

**start**str or timedelta-like, optional

Left bound for generating timedeltas.

**end**str or timedelta-like, optional

Right bound for generating timedeltas.

**periods**int, optional

Number of periods to generate.

**freq**str or DateOffset, default ‘D’

Frequency strings can have multiples, e.g. ‘5H’.

**name**str, default None

Name of the resulting TimedeltaIndex.

**closed**{None, ‘left’, ‘right’}, optional

Make the interval closed with respect to the given frequency to the ‘left’, ‘right’, or both sides (None, the default).

Returns

TimedeltaIndex

Notes

Of the four parameters `start`, `end`, `periods`, and `freq`, exactly three must be specified. If `freq` is omitted, the resulting `TimedeltaIndex` will have `periods` linearly spaced elements between `start` and `end` (closed on both sides).

To learn more about the frequency strings, please see [this link](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases).

Examples

```
>>> ps.timedelta_range(start='1 day', periods=4)  
TimedeltaIndex(['1 days', '2 days', '3 days', '4 days'], dtype='timedelta64[ns]', freq=None)

```


The closed parameter specifies which endpoint is included. The default behavior is to include both endpoints.

```
>>> ps.timedelta_range(start='1 day', periods=4, closed='right')
... 
TimedeltaIndex(['2 days', '3 days', '4 days'], dtype='timedelta64[ns]', freq=None)

```


The freq parameter specifies the frequency of the TimedeltaIndex. Only fixed frequencies can be passed, non-fixed frequencies such as ‘M’ (month end) will raise.

```
>>> ps.timedelta_range(start='1 day', end='2 days', freq='6H')
... 
TimedeltaIndex(['1 days 00:00:00', '1 days 06:00:00', '1 days 12:00:00',
                '1 days 18:00:00', '2 days 00:00:00'],
               dtype='timedelta64[ns]', freq=None)

```


Specify start, end, and periods; the frequency is generated automatically (linearly spaced).

```
>>> ps.timedelta_range(start='1 day', end='5 days', periods=4)
... 
TimedeltaIndex(['1 days 00:00:00', '2 days 08:00:00', '3 days 16:00:00',
                '5 days 00:00:00'],
               dtype='timedelta64[ns]', freq=None)

```
