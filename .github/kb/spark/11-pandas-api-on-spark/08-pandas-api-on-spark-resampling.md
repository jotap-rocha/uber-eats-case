# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/resampling.html

# Resampling#

Resampler objects are returned by `.resample` calls: [`DataFrame.resample()`](api/pyspark.pandas.DataFrame.resample.html#pyspark.pandas.DataFrame.resample "pyspark.pandas.DataFrame.resample"), [`Series.resample()`](api/pyspark.pandas.Series.resample.html#pyspark.pandas.Series.resample "pyspark.pandas.Series.resample"), etc.

## Computations / descriptive stats#

[`Resampler.max`](api/pyspark.pandas.resample.Resampler.max.html#pyspark.pandas.resample.Resampler.max "pyspark.pandas.resample.Resampler.max")() | Compute max of resampled values.  
---|---  
[`Resampler.mean`](api/pyspark.pandas.resample.Resampler.mean.html#pyspark.pandas.resample.Resampler.mean "pyspark.pandas.resample.Resampler.mean")() | Compute mean of resampled values.  
[`Resampler.min`](api/pyspark.pandas.resample.Resampler.min.html#pyspark.pandas.resample.Resampler.min "pyspark.pandas.resample.Resampler.min")() | Compute min of resampled values.  
[`Resampler.std`](api/pyspark.pandas.resample.Resampler.std.html#pyspark.pandas.resample.Resampler.std "pyspark.pandas.resample.Resampler.std")() | Compute std of resampled values.  
[`Resampler.sum`](api/pyspark.pandas.resample.Resampler.sum.html#pyspark.pandas.resample.Resampler.sum "pyspark.pandas.resample.Resampler.sum")() | Compute sum of resampled values.  
[`Resampler.var`](api/pyspark.pandas.resample.Resampler.var.html#pyspark.pandas.resample.Resampler.var "pyspark.pandas.resample.Resampler.var")() | Compute var of resampled values.  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/resampling.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.max.html

# pyspark.pandas.resample.Resampler.max#

Resampler.max()[[source]](../../../_modules/pyspark/pandas/resample.html#Resampler.max)#
    

Compute max of resampled values.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> from datetime import datetime
    >>> np.random.seed(22)
    >>> dates = [
    ...    datetime(2022, 5, 1, 4, 5, 6),
    ...    datetime(2022, 5, 3),
    ...    datetime(2022, 5, 3, 23, 59, 59),
    ...    datetime(2022, 5, 4),
    ...    pd.NaT,
    ...    datetime(2022, 5, 4, 0, 0, 1),
    ...    datetime(2022, 5, 11),
    ... ]
    >>> df = ps.DataFrame(
    ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
    ... )
    >>> df
                                A         B
    2022-05-01 04:05:06  0.208461  0.481681
    2022-05-03 00:00:00  0.420538  0.859182
    2022-05-03 23:59:59  0.171162  0.338864
    2022-05-04 00:00:00  0.270533  0.691041
    NaT                  0.220405  0.811951
    2022-05-04 00:00:01  0.010527  0.561204
    2022-05-11 00:00:00  0.813726  0.745100
    >>> df.resample("3D").max().sort_index()
                       A         B
    2022-05-01  0.420538  0.859182
    2022-05-04  0.270533  0.691041
    2022-05-07       NaN       NaN
    2022-05-10  0.813726  0.745100
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.max.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.mean.html

# pyspark.pandas.resample.Resampler.mean#

Resampler.mean()[[source]](../../../_modules/pyspark/pandas/resample.html#Resampler.mean)#
    

Compute mean of resampled values.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> from datetime import datetime
    >>> np.random.seed(22)
    >>> dates = [
    ...    datetime(2022, 5, 1, 4, 5, 6),
    ...    datetime(2022, 5, 3),
    ...    datetime(2022, 5, 3, 23, 59, 59),
    ...    datetime(2022, 5, 4),
    ...    pd.NaT,
    ...    datetime(2022, 5, 4, 0, 0, 1),
    ...    datetime(2022, 5, 11),
    ... ]
    >>> df = ps.DataFrame(
    ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
    ... )
    >>> df
                                A         B
    2022-05-01 04:05:06  0.208461  0.481681
    2022-05-03 00:00:00  0.420538  0.859182
    2022-05-03 23:59:59  0.171162  0.338864
    2022-05-04 00:00:00  0.270533  0.691041
    NaT                  0.220405  0.811951
    2022-05-04 00:00:01  0.010527  0.561204
    2022-05-11 00:00:00  0.813726  0.745100
    >>> df.resample("3D").mean().sort_index()
                       A         B
    2022-05-01  0.266720  0.559909
    2022-05-04  0.140530  0.626123
    2022-05-07       NaN       NaN
    2022-05-10  0.813726  0.745100
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.mean.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.min.html

# pyspark.pandas.resample.Resampler.min#

Resampler.min()[[source]](../../../_modules/pyspark/pandas/resample.html#Resampler.min)#
    

Compute min of resampled values.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> from datetime import datetime
    >>> np.random.seed(22)
    >>> dates = [
    ...    datetime(2022, 5, 1, 4, 5, 6),
    ...    datetime(2022, 5, 3),
    ...    datetime(2022, 5, 3, 23, 59, 59),
    ...    datetime(2022, 5, 4),
    ...    pd.NaT,
    ...    datetime(2022, 5, 4, 0, 0, 1),
    ...    datetime(2022, 5, 11),
    ... ]
    >>> df = ps.DataFrame(
    ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
    ... )
    >>> df
                                A         B
    2022-05-01 04:05:06  0.208461  0.481681
    2022-05-03 00:00:00  0.420538  0.859182
    2022-05-03 23:59:59  0.171162  0.338864
    2022-05-04 00:00:00  0.270533  0.691041
    NaT                  0.220405  0.811951
    2022-05-04 00:00:01  0.010527  0.561204
    2022-05-11 00:00:00  0.813726  0.745100
    >>> df.resample("3D").min().sort_index()
                       A         B
    2022-05-01  0.171162  0.338864
    2022-05-04  0.010527  0.561204
    2022-05-07       NaN       NaN
    2022-05-10  0.813726  0.745100
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.min.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.std.html

# pyspark.pandas.resample.Resampler.std#

Resampler.std()[[source]](../../../_modules/pyspark/pandas/resample.html#Resampler.std)#
    

Compute std of resampled values.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> from datetime import datetime
    >>> np.random.seed(22)
    >>> dates = [
    ...    datetime(2022, 5, 1, 4, 5, 6),
    ...    datetime(2022, 5, 3),
    ...    datetime(2022, 5, 3, 23, 59, 59),
    ...    datetime(2022, 5, 4),
    ...    pd.NaT,
    ...    datetime(2022, 5, 4, 0, 0, 1),
    ...    datetime(2022, 5, 11),
    ... ]
    >>> df = ps.DataFrame(
    ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
    ... )
    >>> df
                                A         B
    2022-05-01 04:05:06  0.208461  0.481681
    2022-05-03 00:00:00  0.420538  0.859182
    2022-05-03 23:59:59  0.171162  0.338864
    2022-05-04 00:00:00  0.270533  0.691041
    NaT                  0.220405  0.811951
    2022-05-04 00:00:01  0.010527  0.561204
    2022-05-11 00:00:00  0.813726  0.745100
    >>> df.resample("3D").std().sort_index()
                       A         B
    2022-05-01  0.134509  0.268835
    2022-05-04  0.183852  0.091809
    2022-05-07       NaN       NaN
    2022-05-10       NaN       NaN
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.std.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.sum.html

# pyspark.pandas.resample.Resampler.sum#

Resampler.sum()[[source]](../../../_modules/pyspark/pandas/resample.html#Resampler.sum)#
    

Compute sum of resampled values.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> from datetime import datetime
    >>> np.random.seed(22)
    >>> dates = [
    ...    datetime(2022, 5, 1, 4, 5, 6),
    ...    datetime(2022, 5, 3),
    ...    datetime(2022, 5, 3, 23, 59, 59),
    ...    datetime(2022, 5, 4),
    ...    pd.NaT,
    ...    datetime(2022, 5, 4, 0, 0, 1),
    ...    datetime(2022, 5, 11),
    ... ]
    >>> df = ps.DataFrame(
    ...    np.random.rand(len(dates), 2), index=pd.DatetimeIndex(dates), columns=["A", "B"]
    ... )
    >>> df
                                A         B
    2022-05-01 04:05:06  0.208461  0.481681
    2022-05-03 00:00:00  0.420538  0.859182
    2022-05-03 23:59:59  0.171162  0.338864
    2022-05-04 00:00:00  0.270533  0.691041
    NaT                  0.220405  0.811951
    2022-05-04 00:00:01  0.010527  0.561204
    2022-05-11 00:00:00  0.813726  0.745100
    >>> df.resample("3D").sum().sort_index()
                       A         B
    2022-05-01  0.800160  1.679727
    2022-05-04  0.281060  1.252245
    2022-05-07  0.000000  0.000000
    2022-05-10  0.813726  0.745100
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.resample.Resampler.sum.rst.txt)
