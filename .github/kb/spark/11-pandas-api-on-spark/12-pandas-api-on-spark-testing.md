# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/testing.html

# Testing#

## Assertion functions#

[`testing.assert_frame_equal`](api/pyspark.pandas.testing.assert_frame_equal.html#pyspark.pandas.testing.assert_frame_equal "pyspark.pandas.testing.assert_frame_equal")(left,Â right[,Â ...]) | Check that left and right DataFrame are equal.  
---|---  
[`testing.assert_series_equal`](api/pyspark.pandas.testing.assert_series_equal.html#pyspark.pandas.testing.assert_series_equal "pyspark.pandas.testing.assert_series_equal")(left,Â right[,Â ...]) | Check that left and right Series are equal.  
[`testing.assert_index_equal`](api/pyspark.pandas.testing.assert_index_equal.html#pyspark.pandas.testing.assert_index_equal "pyspark.pandas.testing.assert_index_equal")(left,Â right[,Â ...]) | Check that left and right Index are equal.  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/testing.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.testing.assert_frame_equal.html

# pyspark.pandas.testing.assert_frame_equal#

pyspark.pandas.testing.assert_frame_equal(_left_ , _right_ , _check_dtype =True_, _check_index_type ='equiv'_, _check_column_type ='equiv'_, _check_frame_type =True_, _check_names =True_, _by_blocks =False_, _check_exact =False_, _check_datetimelike_compat =False_, _check_categorical =True_, _check_like =False_, _check_freq =True_, _check_flags =True_, _rtol =1e-05_, _atol =1e-08_, _obj ='DataFrame'_)[[source]](../../../_modules/pyspark/pandas/testing.html#assert_frame_equal)#
    

Check that left and right DataFrame are equal.

This function is intended to compare two DataFrames and output any differences. It is mostly intended for use in unit tests. Additional parameters allow varying the strictness of the equality checks performed.

New in version 4.0.0.

Parameters
    

**left** DataFrame
    

First DataFrame to compare.

**right** DataFrame
    

Second DataFrame to compare.

**check_dtype** bool, default True
    

Whether to check the DataFrame dtype is identical.

**check_index_type** bool or {âequivâ}, default âequivâ
    

Whether to check the Index class, dtype and inferred_type are identical.

**check_column_type** bool or {âequivâ}, default âequivâ
    

Whether to check the columns class, dtype and inferred_type are identical. Is passed as the `exact` argument of [`assert_index_equal()`](pyspark.pandas.testing.assert_index_equal.html#pyspark.pandas.testing.assert_index_equal "pyspark.pandas.testing.assert_index_equal").

**check_frame_type** bool, default True
    

Whether to check the DataFrame class is identical.

**check_names** bool, default True
    

Whether to check that the names attribute for both the index and column attributes of the DataFrame is identical.

**by_blocks** bool, default False
    

Specify how to compare internal data. If False, compare by columns. If True, compare by blocks.

**check_exact** bool, default False
    

Whether to compare number exactly.

**check_datetimelike_compat** bool, default False
    

Compare datetime-like which is comparable ignoring dtype.

**check_categorical** bool, default True
    

Whether to compare internal Categorical exactly.

**check_like** bool, default False
    

If True, ignore the order of index & columns. Note: index labels must match their respective rows (same as in columns) - same labels must be with the same data.

**check_freq** bool, default True
    

Whether to check the freq attribute on a DatetimeIndex or TimedeltaIndex.

**check_flags** bool, default True
    

Whether to check the flags attribute.

**rtol** float, default 1e-5
    

Relative tolerance. Only used when check_exact is False.

**atol** float, default 1e-8
    

Absolute tolerance. Only used when check_exact is False.

**obj** str, default âDataFrameâ
    

Specify object name being compared, internally used to show appropriate assertion message.

See also

[`assert_series_equal`](pyspark.pandas.testing.assert_series_equal.html#pyspark.pandas.testing.assert_series_equal "pyspark.pandas.testing.assert_series_equal")
    

Equivalent method for asserting Series equality.

`DataFrame.equals`
    

Check DataFrame equality.

Examples

This example shows comparing two DataFrames that are equal but with columns of differing dtypes.
    
    
    >>> from pyspark.pandas.testing import assert_frame_equal
    >>> df1 = ps.DataFrame({'a': [1, 2], 'b': [3, 4]})
    >>> df2 = ps.DataFrame({'a': [1, 2], 'b': [3.0, 4.0]})
    

df1 equals itself.
    
    
    >>> assert_frame_equal(df1, df1)
    

df1 differs from df2 as column âbâ is of a different type.
    
    
    >>> assert_frame_equal(df1, df2)
    Traceback (most recent call last):
    ...
    AssertionError: Attributes of DataFrame.iloc[:, 1] (column name="b") are different
    
    Attribute "dtype" are different
    [left]:  int64
    [right]: float64
    

Ignore differing dtypes in columns with check_dtype.
    
    
    >>> assert_frame_equal(df1, df2, check_dtype=False)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.testing.assert_frame_equal.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.testing.assert_series_equal.html

# pyspark.pandas.testing.assert_series_equal#

pyspark.pandas.testing.assert_series_equal(_left_ , _right_ , _check_dtype =True_, _check_index_type ='equiv'_, _check_series_type =True_, _check_names =True_, _check_exact =False_, _check_datetimelike_compat =False_, _check_categorical =True_, _check_category_order =True_, _check_freq =True_, _check_flags =True_, _rtol =1e-05_, _atol =1e-08_, _obj ='Series'_, _*_ , _check_index =True_, _check_like =False_)[[source]](../../../_modules/pyspark/pandas/testing.html#assert_series_equal)#
    

Check that left and right Series are equal.

New in version 4.0.0.

Parameters
    

**left** Series
    
**right** Series
    
**check_dtype** bool, default True
    

Whether to check the Series dtype is identical.

**check_index_type** bool or {âequivâ}, default âequivâ
    

Whether to check the Index class, dtype and inferred_type are identical.

**check_series_type** bool, default True
    

Whether to check the Series class is identical.

**check_names** bool, default True
    

Whether to check the Series and Index names attribute.

**check_exact** bool, default False
    

Whether to compare number exactly.

**check_datetimelike_compat** bool, default False
    

Compare datetime-like which is comparable ignoring dtype.

**check_categorical** bool, default True
    

Whether to compare internal Categorical exactly.

**check_category_order** bool, default True
    

Whether to compare category order of internal Categoricals.

**check_freq** bool, default True
    

Whether to check the freq attribute on a DatetimeIndex or TimedeltaIndex.

**check_flags** bool, default True
    

Whether to check the flags attribute.

**rtol** float, default 1e-5
    

Relative tolerance. Only used when check_exact is False.

**atol** float, default 1e-8
    

Absolute tolerance. Only used when check_exact is False.

**obj** str, default âSeriesâ
    

Specify object name being compared, internally used to show appropriate assertion message.

**check_index** bool, default True
    

Whether to check index equivalence. If False, then compare only values.

**check_like** bool, default False
    

If True, ignore the order of the index. Must be False if check_index is False. Note: same labels must be with the same data.

Examples
    
    
    >>> from pyspark.pandas import testing as tm
    >>> a = ps.Series([1, 2, 3, 4])
    >>> b = ps.Series([1, 2, 3, 4])
    >>> tm.assert_series_equal(a, b)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.testing.assert_series_equal.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.testing.assert_index_equal.html

# pyspark.pandas.testing.assert_index_equal#

pyspark.pandas.testing.assert_index_equal(_left_ , _right_ , _exact ='equiv'_, _check_names =True_, _check_exact =True_, _check_categorical =True_, _check_order =True_, _rtol =1e-05_, _atol =1e-08_, _obj ='Index'_)[[source]](../../../_modules/pyspark/pandas/testing.html#assert_index_equal)#
    

Check that left and right Index are equal.

New in version 4.0.0.

Parameters
    

**left** Index
    
**right** Index
    
**exact** bool or {âequivâ}, default âequivâ
    

Whether to check the Index class, dtype and inferred_type are identical. If âequivâ, then RangeIndex can be substituted for Index with an int64 dtype as well.

**check_names** bool, default True
    

Whether to check the names attribute.

**check_exact** bool, default True
    

Whether to compare number exactly.

**check_categorical** bool, default True
    

Whether to compare internal Categorical exactly.

**check_order** bool, default True
    

Whether to compare the order of index entries as well as their values. If True, both indexes must contain the same elements, in the same order. If False, both indexes must contain the same elements, but in any order.

**rtol** float, default 1e-5
    

Relative tolerance. Only used when check_exact is False.

**atol** float, default 1e-8
    

Absolute tolerance. Only used when check_exact is False.

**obj** str, default âIndexâ
    

Specify object name being compared, internally used to show appropriate assertion message.

Examples
    
    
    >>> from pyspark.pandas import testing as tm
    >>> a = ps.Index([1, 2, 3])
    >>> b = ps.Index([1, 2, 3])
    >>> tm.assert_index_equal(a, b)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.testing.assert_index_equal.rst.txt)
