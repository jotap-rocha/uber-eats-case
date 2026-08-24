# 📘 PySpark Pandas Window Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/window.html

# Window#

Rolling objects are returned by `.rolling` calls: [`pyspark.pandas.DataFrame.rolling()`](api/pyspark.pandas.DataFrame.rolling.html#pyspark.pandas.DataFrame.rolling "pyspark.pandas.DataFrame.rolling"), [`pyspark.pandas.Series.rolling()`](api/pyspark.pandas.Series.rolling.html#pyspark.pandas.Series.rolling "pyspark.pandas.Series.rolling"), etc.

Expanding objects are returned by `.expanding` calls: [`pyspark.pandas.DataFrame.expanding()`](api/pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding"), [`pyspark.pandas.Series.expanding()`](api/pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding"), etc.

ExponentialMoving objects are returned by `.ewm` calls: [`pyspark.pandas.DataFrame.ewm()`](api/pyspark.pandas.DataFrame.ewm.html#pyspark.pandas.DataFrame.ewm "pyspark.pandas.DataFrame.ewm"), [`pyspark.pandas.Series.ewm()`](api/pyspark.pandas.Series.ewm.html#pyspark.pandas.Series.ewm "pyspark.pandas.Series.ewm"), etc.

## Standard moving window functions#

[`Rolling.count`](api/pyspark.pandas.window.Rolling.count.html#pyspark.pandas.window.Rolling.count "pyspark.pandas.window.Rolling.count")() | The rolling count of any non-NaN observations inside the window.  
---|---  
[`Rolling.sum`](api/pyspark.pandas.window.Rolling.sum.html#pyspark.pandas.window.Rolling.sum "pyspark.pandas.window.Rolling.sum")() | Calculate rolling summation of given DataFrame or Series.  
[`Rolling.min`](api/pyspark.pandas.window.Rolling.min.html#pyspark.pandas.window.Rolling.min "pyspark.pandas.window.Rolling.min")() | Calculate the rolling minimum.  
[`Rolling.max`](api/pyspark.pandas.window.Rolling.max.html#pyspark.pandas.window.Rolling.max "pyspark.pandas.window.Rolling.max")() | Calculate the rolling maximum.  
[`Rolling.mean`](api/pyspark.pandas.window.Rolling.mean.html#pyspark.pandas.window.Rolling.mean "pyspark.pandas.window.Rolling.mean")() | Calculate the rolling mean of the values.  
[`Rolling.quantile`](api/pyspark.pandas.window.Rolling.quantile.html#pyspark.pandas.window.Rolling.quantile "pyspark.pandas.window.Rolling.quantile")(quantile[,Â accuracy]) | Calculate the rolling quantile of the values.  
  
## Standard expanding window functions#

[`Expanding.count`](api/pyspark.pandas.window.Expanding.count.html#pyspark.pandas.window.Expanding.count "pyspark.pandas.window.Expanding.count")() | The expanding count of any non-NaN observations inside the window.  
---|---  
[`Expanding.sum`](api/pyspark.pandas.window.Expanding.sum.html#pyspark.pandas.window.Expanding.sum "pyspark.pandas.window.Expanding.sum")() | Calculate expanding summation of given DataFrame or Series.  
[`Expanding.min`](api/pyspark.pandas.window.Expanding.min.html#pyspark.pandas.window.Expanding.min "pyspark.pandas.window.Expanding.min")() | Calculate the expanding minimum.  
[`Expanding.max`](api/pyspark.pandas.window.Expanding.max.html#pyspark.pandas.window.Expanding.max "pyspark.pandas.window.Expanding.max")() | Calculate the expanding maximum.  
[`Expanding.mean`](api/pyspark.pandas.window.Expanding.mean.html#pyspark.pandas.window.Expanding.mean "pyspark.pandas.window.Expanding.mean")() | Calculate the expanding mean of the values.  
[`Expanding.quantile`](api/pyspark.pandas.window.Expanding.quantile.html#pyspark.pandas.window.Expanding.quantile "pyspark.pandas.window.Expanding.quantile")(quantile[,Â accuracy]) | Calculate the expanding quantile of the values.  
  
## Exponential moving window functions#

[`ExponentialMoving.mean`](api/pyspark.pandas.window.ExponentialMoving.mean.html#pyspark.pandas.window.ExponentialMoving.mean "pyspark.pandas.window.ExponentialMoving.mean")() | Calculate an online exponentially weighted mean.  
---|---  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/window.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.count.html

# pyspark.pandas.window.Rolling.count#

Rolling.count()[[source]](../../../_modules/pyspark/pandas/window.html#Rolling.count)#
    

The rolling count of any non-NaN observations inside the window.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Return type is the same as the original object with np.float64 dtype.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.count`](pyspark.pandas.Series.count.html#pyspark.pandas.Series.count "pyspark.pandas.Series.count")
    

Count of the full Series.

[`pyspark.pandas.DataFrame.count`](pyspark.pandas.DataFrame.count.html#pyspark.pandas.DataFrame.count "pyspark.pandas.DataFrame.count")
    

Count of the full DataFrame.

Examples
    
    
    >>> s = ps.Series([2, 3, float("nan"), 10])
    >>> s.rolling(1).count()
    0    1.0
    1    1.0
    2    0.0
    3    1.0
    dtype: float64
    
    
    
    >>> s.rolling(3).count()
    0    1.0
    1    2.0
    2    2.0
    3    2.0
    dtype: float64
    
    
    
    >>> s.to_frame().rolling(1).count()
         0
    0  1.0
    1  1.0
    2  0.0
    3  1.0
    
    
    
    >>> s.to_frame().rolling(3).count()
         0
    0  1.0
    1  2.0
    2  2.0
    3  2.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.count.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.sum.html

# pyspark.pandas.window.Rolling.sum#

Rolling.sum()[[source]](../../../_modules/pyspark/pandas/window.html#Rolling.sum)#
    

Calculate rolling summation of given DataFrame or Series.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Same type as the input, with the same index, containing the rolling summation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.sum`](pyspark.pandas.Series.sum.html#pyspark.pandas.Series.sum "pyspark.pandas.Series.sum")
    

Reducing sum for Series.

[`pyspark.pandas.DataFrame.sum`](pyspark.pandas.DataFrame.sum.html#pyspark.pandas.DataFrame.sum "pyspark.pandas.DataFrame.sum")
    

Reducing sum for DataFrame.

Examples
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s
    0    4
    1    3
    2    5
    3    2
    4    6
    dtype: int64
    
    
    
    >>> s.rolling(2).sum()
    0    NaN
    1    7.0
    2    8.0
    3    7.0
    4    8.0
    dtype: float64
    
    
    
    >>> s.rolling(3).sum()
    0     NaN
    1     NaN
    2    12.0
    3    10.0
    4    13.0
    dtype: float64
    

For DataFrame, each rolling summation is computed column-wise.
    
    
    >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
    >>> df
       A   B
    0  4  16
    1  3   9
    2  5  25
    3  2   4
    4  6  36
    
    
    
    >>> df.rolling(2).sum()
         A     B
    0  NaN   NaN
    1  7.0  25.0
    2  8.0  34.0
    3  7.0  29.0
    4  8.0  40.0
    
    
    
    >>> df.rolling(3).sum()
          A     B
    0   NaN   NaN
    1   NaN   NaN
    2  12.0  50.0
    3  10.0  38.0
    4  13.0  65.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.sum.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.min.html

# pyspark.pandas.window.Rolling.min#

Rolling.min()[[source]](../../../_modules/pyspark/pandas/window.html#Rolling.min)#
    

Calculate the rolling minimum.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the rolling calculation.

See also

[`pyspark.pandas.Series.rolling`](pyspark.pandas.Series.rolling.html#pyspark.pandas.Series.rolling "pyspark.pandas.Series.rolling")
    

Calling object with a Series.

[`pyspark.pandas.DataFrame.rolling`](pyspark.pandas.DataFrame.rolling.html#pyspark.pandas.DataFrame.rolling "pyspark.pandas.DataFrame.rolling")
    

Calling object with a DataFrame.

[`pyspark.pandas.Series.min`](pyspark.pandas.Series.min.html#pyspark.pandas.Series.min "pyspark.pandas.Series.min")
    

Similar method for Series.

[`pyspark.pandas.DataFrame.min`](pyspark.pandas.DataFrame.min.html#pyspark.pandas.DataFrame.min "pyspark.pandas.DataFrame.min")
    

Similar method for DataFrame.

Examples
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s
    0    4
    1    3
    2    5
    3    2
    4    6
    dtype: int64
    
    
    
    >>> s.rolling(2).min()
    0    NaN
    1    3.0
    2    3.0
    3    2.0
    4    2.0
    dtype: float64
    
    
    
    >>> s.rolling(3).min()
    0    NaN
    1    NaN
    2    3.0
    3    2.0
    4    2.0
    dtype: float64
    

For DataFrame, each rolling minimum is computed column-wise.
    
    
    >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
    >>> df
       A   B
    0  4  16
    1  3   9
    2  5  25
    3  2   4
    4  6  36
    
    
    
    >>> df.rolling(2).min()
         A    B
    0  NaN  NaN
    1  3.0  9.0
    2  3.0  9.0
    3  2.0  4.0
    4  2.0  4.0
    
    
    
    >>> df.rolling(3).min()
         A    B
    0  NaN  NaN
    1  NaN  NaN
    2  3.0  9.0
    3  2.0  4.0
    4  2.0  4.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.min.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.max.html

# pyspark.pandas.window.Rolling.max#

Rolling.max()[[source]](../../../_modules/pyspark/pandas/window.html#Rolling.max)#
    

Calculate the rolling maximum.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Return type is determined by the caller.

See also

[`pyspark.pandas.Series.rolling`](pyspark.pandas.Series.rolling.html#pyspark.pandas.Series.rolling "pyspark.pandas.Series.rolling")
    

Series rolling.

[`pyspark.pandas.DataFrame.rolling`](pyspark.pandas.DataFrame.rolling.html#pyspark.pandas.DataFrame.rolling "pyspark.pandas.DataFrame.rolling")
    

DataFrame rolling.

[`pyspark.pandas.Series.max`](pyspark.pandas.Series.max.html#pyspark.pandas.Series.max "pyspark.pandas.Series.max")
    

Similar method for Series.

[`pyspark.pandas.DataFrame.max`](pyspark.pandas.DataFrame.max.html#pyspark.pandas.DataFrame.max "pyspark.pandas.DataFrame.max")
    

Similar method for DataFrame.

Examples
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s
    0    4
    1    3
    2    5
    3    2
    4    6
    dtype: int64
    
    
    
    >>> s.rolling(2).max()
    0    NaN
    1    4.0
    2    5.0
    3    5.0
    4    6.0
    dtype: float64
    
    
    
    >>> s.rolling(3).max()
    0    NaN
    1    NaN
    2    5.0
    3    5.0
    4    6.0
    dtype: float64
    

For DataFrame, each rolling maximum is computed column-wise.
    
    
    >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
    >>> df
       A   B
    0  4  16
    1  3   9
    2  5  25
    3  2   4
    4  6  36
    
    
    
    >>> df.rolling(2).max()
         A     B
    0  NaN   NaN
    1  4.0  16.0
    2  5.0  25.0
    3  5.0  25.0
    4  6.0  36.0
    
    
    
    >>> df.rolling(3).max()
         A     B
    0  NaN   NaN
    1  NaN   NaN
    2  5.0  25.0
    3  5.0  25.0
    4  6.0  36.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.max.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.mean.html

# pyspark.pandas.window.Rolling.mean#

Rolling.mean()[[source]](../../../_modules/pyspark/pandas/window.html#Rolling.mean)#
    

Calculate the rolling mean of the values.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the rolling calculation.

See also

[`pyspark.pandas.Series.rolling`](pyspark.pandas.Series.rolling.html#pyspark.pandas.Series.rolling "pyspark.pandas.Series.rolling")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.rolling`](pyspark.pandas.DataFrame.rolling.html#pyspark.pandas.DataFrame.rolling "pyspark.pandas.DataFrame.rolling")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.mean`](pyspark.pandas.Series.mean.html#pyspark.pandas.Series.mean "pyspark.pandas.Series.mean")
    

Equivalent method for Series.

[`pyspark.pandas.DataFrame.mean`](pyspark.pandas.DataFrame.mean.html#pyspark.pandas.DataFrame.mean "pyspark.pandas.DataFrame.mean")
    

Equivalent method for DataFrame.

Examples
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s
    0    4
    1    3
    2    5
    3    2
    4    6
    dtype: int64
    
    
    
    >>> s.rolling(2).mean()
    0    NaN
    1    3.5
    2    4.0
    3    3.5
    4    4.0
    dtype: float64
    
    
    
    >>> s.rolling(3).mean()
    0         NaN
    1         NaN
    2    4.000000
    3    3.333333
    4    4.333333
    dtype: float64
    

For DataFrame, each rolling mean is computed column-wise.
    
    
    >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
    >>> df
       A   B
    0  4  16
    1  3   9
    2  5  25
    3  2   4
    4  6  36
    
    
    
    >>> df.rolling(2).mean()
         A     B
    0  NaN   NaN
    1  3.5  12.5
    2  4.0  17.0
    3  3.5  14.5
    4  4.0  20.0
    
    
    
    >>> df.rolling(3).mean()
              A          B
    0       NaN        NaN
    1       NaN        NaN
    2  4.000000  16.666667
    3  3.333333  12.666667
    4  4.333333  21.666667
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.mean.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.quantile.html

# pyspark.pandas.window.Rolling.quantile#

Rolling.quantile(_quantile_ , _accuracy =10000_)[[source]](../../../_modules/pyspark/pandas/window.html#Rolling.quantile)#
    

Calculate the rolling quantile of the values.

New in version 3.4.0.

Parameters
    

**quantile** float
    

Value between 0 and 1 providing the quantile to compute.

Deprecated since version 4.0.0: This will be renamed to âqâ in a future version.

**accuracy** int, optional
    

Default accuracy of approximation. Larger value means better accuracy. The relative error can be deduced by 1.0 / accuracy. This is a panda-on-Spark specific parameter.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the rolling calculation.

See also

[`pyspark.pandas.Series.rolling`](pyspark.pandas.Series.rolling.html#pyspark.pandas.Series.rolling "pyspark.pandas.Series.rolling")
    

Calling rolling with Series data.

[`pyspark.pandas.DataFrame.rolling`](pyspark.pandas.DataFrame.rolling.html#pyspark.pandas.DataFrame.rolling "pyspark.pandas.DataFrame.rolling")
    

Calling rolling with DataFrames.

[`pyspark.pandas.Series.quantile`](pyspark.pandas.Series.quantile.html#pyspark.pandas.Series.quantile "pyspark.pandas.Series.quantile")
    

Aggregating quantile for Series.

[`pyspark.pandas.DataFrame.quantile`](pyspark.pandas.DataFrame.quantile.html#pyspark.pandas.DataFrame.quantile "pyspark.pandas.DataFrame.quantile")
    

Aggregating quantile for DataFrame.

Notes

quantile in pandas-on-Spark are using distributed percentile approximation algorithm unlike pandas, the result might be different with pandas, also interpolation parameter is not supported yet.

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Examples
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s
    0    4
    1    3
    2    5
    3    2
    4    6
    dtype: int64
    
    
    
    >>> s.rolling(2).quantile(0.5)
    0    NaN
    1    3.0
    2    3.0
    3    2.0
    4    2.0
    dtype: float64
    
    
    
    >>> s.rolling(3).quantile(0.5)
    0    NaN
    1    NaN
    2    4.0
    3    3.0
    4    5.0
    dtype: float64
    

For DataFrame, each rolling quantile is computed column-wise.
    
    
    >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
    >>> df
       A   B
    0  4  16
    1  3   9
    2  5  25
    3  2   4
    4  6  36
    
    
    
    >>> df.rolling(2).quantile(0.5)
         A    B
    0  NaN  NaN
    1  3.0  9.0
    2  3.0  9.0
    3  2.0  4.0
    4  2.0  4.0
    
    
    
    >>> df.rolling(3).quantile(0.5)
         A     B
    0  NaN   NaN
    1  NaN   NaN
    2  4.0  16.0
    3  3.0   9.0
    4  5.0  25.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Rolling.quantile.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.count.html

# pyspark.pandas.window.Expanding.count#

Expanding.count()[[source]](../../../_modules/pyspark/pandas/window.html#Expanding.count)#
    

The expanding count of any non-NaN observations inside the window.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the expanding calculation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.count`](pyspark.pandas.Series.count.html#pyspark.pandas.Series.count "pyspark.pandas.Series.count")
    

Count of the full Series.

[`pyspark.pandas.DataFrame.count`](pyspark.pandas.DataFrame.count.html#pyspark.pandas.DataFrame.count "pyspark.pandas.DataFrame.count")
    

Count of the full DataFrame.

Examples
    
    
    >>> s = ps.Series([2, 3, float("nan"), 10])
    >>> s.expanding().count()
    0    1.0
    1    2.0
    2    2.0
    3    3.0
    dtype: float64
    
    
    
    >>> s.to_frame().expanding().count()
         0
    0  1.0
    1  2.0
    2  2.0
    3  3.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.count.rst.txt)


---

## 🔹 009. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.sum.html

# pyspark.pandas.window.Expanding.sum#

Expanding.sum()[[source]](../../../_modules/pyspark/pandas/window.html#Expanding.sum)#
    

Calculate expanding summation of given DataFrame or Series.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Same type as the input, with the same index, containing the expanding summation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.sum`](pyspark.pandas.Series.sum.html#pyspark.pandas.Series.sum "pyspark.pandas.Series.sum")
    

Reducing sum for Series.

[`pyspark.pandas.DataFrame.sum`](pyspark.pandas.DataFrame.sum.html#pyspark.pandas.DataFrame.sum "pyspark.pandas.DataFrame.sum")
    

Reducing sum for DataFrame.

Examples
    
    
    >>> s = ps.Series([1, 2, 3, 4, 5])
    >>> s
    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64
    
    
    
    >>> s.expanding(3).sum()
    0     NaN
    1     NaN
    2     6.0
    3    10.0
    4    15.0
    dtype: float64
    

For DataFrame, each expanding summation is computed column-wise.
    
    
    >>> df = ps.DataFrame({"A": s.to_numpy(), "B": s.to_numpy() ** 2})
    >>> df
       A   B
    0  1   1
    1  2   4
    2  3   9
    3  4  16
    4  5  25
    
    
    
    >>> df.expanding(3).sum()
          A     B
    0   NaN   NaN
    1   NaN   NaN
    2   6.0  14.0
    3  10.0  30.0
    4  15.0  55.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.sum.rst.txt)


---

## 🔹 010. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.min.html

# pyspark.pandas.window.Expanding.min#

Expanding.min()[[source]](../../../_modules/pyspark/pandas/window.html#Expanding.min)#
    

Calculate the expanding minimum.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the expanding calculation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with a Series.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with a DataFrame.

[`pyspark.pandas.Series.min`](pyspark.pandas.Series.min.html#pyspark.pandas.Series.min "pyspark.pandas.Series.min")
    

Similar method for Series.

[`pyspark.pandas.DataFrame.min`](pyspark.pandas.DataFrame.min.html#pyspark.pandas.DataFrame.min "pyspark.pandas.DataFrame.min")
    

Similar method for DataFrame.

Examples

Performing a expanding minimum with a window size of 3.
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s.expanding(3).min()
    0    NaN
    1    NaN
    2    3.0
    3    2.0
    4    2.0
    dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.min.rst.txt)


---

## 🔹 011. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.max.html

# pyspark.pandas.window.Expanding.max#

Expanding.max()[[source]](../../../_modules/pyspark/pandas/window.html#Expanding.max)#
    

Calculate the expanding maximum.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Return type is determined by the caller.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.max`](pyspark.pandas.Series.max.html#pyspark.pandas.Series.max "pyspark.pandas.Series.max")
    

Similar method for Series.

[`pyspark.pandas.DataFrame.max`](pyspark.pandas.DataFrame.max.html#pyspark.pandas.DataFrame.max "pyspark.pandas.DataFrame.max")
    

Similar method for DataFrame.

Examples

Performing a expanding minimum with a window size of 3.
    
    
    >>> s = ps.Series([4, 3, 5, 2, 6])
    >>> s.expanding(3).max()
    0    NaN
    1    NaN
    2    5.0
    3    5.0
    4    6.0
    dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.max.rst.txt)


---

## 🔹 012. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.mean.html

# pyspark.pandas.window.Expanding.mean#

Expanding.mean()[[source]](../../../_modules/pyspark/pandas/window.html#Expanding.mean)#
    

Calculate the expanding mean of the values.

Note

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the expanding calculation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.mean`](pyspark.pandas.Series.mean.html#pyspark.pandas.Series.mean "pyspark.pandas.Series.mean")
    

Equivalent method for Series.

[`pyspark.pandas.DataFrame.mean`](pyspark.pandas.DataFrame.mean.html#pyspark.pandas.DataFrame.mean "pyspark.pandas.DataFrame.mean")
    

Equivalent method for DataFrame.

Examples

The below examples will show expanding mean calculations with window sizes of two and three, respectively.
    
    
    >>> s = ps.Series([1, 2, 3, 4])
    >>> s.expanding(2).mean()
    0    NaN
    1    1.5
    2    2.0
    3    2.5
    dtype: float64
    
    
    
    >>> s.expanding(3).mean()
    0    NaN
    1    NaN
    2    2.0
    3    2.5
    dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.mean.rst.txt)


---

## 🔹 013. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.quantile.html

# pyspark.pandas.window.Expanding.quantile#

Expanding.quantile(_quantile_ , _accuracy =10000_)[[source]](../../../_modules/pyspark/pandas/window.html#Expanding.quantile)#
    

Calculate the expanding quantile of the values.

Parameters
    

**quantile** float
    

Value between 0 and 1 providing the quantile to compute.

**accuracy** int, optional
    

Default accuracy of approximation. Larger value means better accuracy. The relative error can be deduced by 1.0 / accuracy. This is a panda-on-Spark specific parameter.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the expanding calculation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling expanding with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling expanding with DataFrames.

[`pyspark.pandas.Series.quantile`](pyspark.pandas.Series.quantile.html#pyspark.pandas.Series.quantile "pyspark.pandas.Series.quantile")
    

Aggregating quantile for Series.

[`pyspark.pandas.DataFrame.quantile`](pyspark.pandas.DataFrame.quantile.html#pyspark.pandas.DataFrame.quantile "pyspark.pandas.DataFrame.quantile")
    

Aggregating quantile for DataFrame.

Notes

quantile in pandas-on-Spark are using distributed percentile approximation algorithm unlike pandas, the result might be different with pandas (the result is similar to the interpolation set to lower), also interpolation parameter is not supported yet.

the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.

Examples

The below examples will show expanding quantile calculations with window sizes of two and three, respectively.
    
    
    >>> s = ps.Series([1, 2, 3, 4])
    >>> s.expanding(2).quantile(0.5)
    0    NaN
    1    1.0
    2    2.0
    3    2.0
    dtype: float64
    
    
    
    >>> s.expanding(3).quantile(0.5)
    0    NaN
    1    NaN
    2    2.0
    3    2.0
    dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.Expanding.quantile.rst.txt)


---

## 🔹 014. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.window.ExponentialMoving.mean.html

# pyspark.pandas.window.ExponentialMoving.mean#

ExponentialMoving.mean()[[source]](../../../_modules/pyspark/pandas/window.html#ExponentialMoving.mean)#
    

Calculate an online exponentially weighted mean.

Returns
    

Series or DataFrame
    

Returned object type is determined by the caller of the exponentially calculation.

See also

[`pyspark.pandas.Series.expanding`](pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")
    

Calling object with Series data.

[`pyspark.pandas.DataFrame.expanding`](pyspark.pandas.DataFrame.expanding.html#pyspark.pandas.DataFrame.expanding "pyspark.pandas.DataFrame.expanding")
    

Calling object with DataFrames.

[`pyspark.pandas.Series.mean`](pyspark.pandas.Series.mean.html#pyspark.pandas.Series.mean "pyspark.pandas.Series.mean")
    

Equivalent method for Series.

[`pyspark.pandas.DataFrame.mean`](pyspark.pandas.DataFrame.mean.html#pyspark.pandas.DataFrame.mean "pyspark.pandas.DataFrame.mean")
    

Equivalent method for DataFrame.

Notes

There are behavior differences between pandas-on-Spark and pandas.

  * the current implementation of this API uses Sparkâs Window without specifying partition specification. This leads to move all data into single partition in single machine and could cause serious performance degradation. Avoid this method against very large dataset.




Examples

The below examples will show computing exponentially weighted moving average.
    
    
    >>> df = ps.DataFrame({'s1': [.2, .0, .6, .2, .4, .5, .6], 's2': [2, 1, 3, 1, 0, 0, 0]})
    >>> df.ewm(com=0.1).mean()
             s1        s2
    0  0.200000  2.000000
    1  0.016667  1.083333
    2  0.547368  2.827068
    3  0.231557  1.165984
    4  0.384688  0.105992
    5  0.489517  0.009636
    6  0.589956  0.000876
    
    
    
    >>> df.s2.ewm(halflife=1.5, min_periods=3).mean()
    0         NaN
    1         NaN
    2    2.182572
    3    1.663174
    4    0.979949
    5    0.593155
    6    0.364668
    Name: s2, dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.window.ExponentialMoving.mean.rst.txt)
