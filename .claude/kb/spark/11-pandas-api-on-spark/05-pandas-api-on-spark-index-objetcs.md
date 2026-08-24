# pyspark.pandas.Index — PySpark 4.0.1 documentation
_class_ pyspark.pandas.Index(_data\=None_, _dtype\=None_, _copy\=False_, _name\=None_, _tupleize\_cols\=True_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/indexes/base.html#Index)
[#](#pyspark.pandas.Index "Permalink to this definition")

pandas-on-Spark Index that corresponds to pandas Index logically. This might hold Spark Column internally.

Parameters

**data**array-like (1-dimensional)

**dtype**dtype, default None

If dtype is None, we find the dtype that best fits the data. If an actual dtype is provided, we coerce to that dtype if it’s safe. Otherwise, an error will be raised.

**copy**bool

Make a copy of input ndarray.

**name**object

Name to be stored in the index.

**tupleize\_cols**bool (default: True)

When True, attempt to create a MultiIndex if possible.

Examples

```
>>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[1, 2, 3]).index
Index([1, 2, 3], dtype='int64')

```


```
>>> ps.DataFrame({'a': [1, 2, 3]}, index=list('abc')).index
Index(['a', 'b', 'c'], dtype='object')

```


```
>>> ps.Index([1, 2, 3])
Index([1, 2, 3], dtype='int64')

```


```
>>> ps.Index(list('abc'))
Index(['a', 'b', 'c'], dtype='object')

```


From a Series:

```
>>> s = ps.Series([1, 2, 3], index=[10, 20, 30])
>>> ps.Index(s)
Index([1, 2, 3], dtype='int64')

```


From an Index:

```
>>> idx = ps.Index([1, 2, 3])
>>> ps.Index(idx)
Index([1, 2, 3], dtype='int64')

```


Methods



* all([axis, skipna]): any([axis])
  * Return whether all elements are True.: Return whether any element is True.
* all([axis, skipna]): append(other)
  * Return whether all elements are True.: Append a collection of Index options together.
* all([axis, skipna]): argmax()
  * Return whether all elements are True.: Return a maximum argument indexer.
* all([axis, skipna]): argmin()
  * Return whether all elements are True.: Return a minimum argument indexer.
* all([axis, skipna]): asof(label)
  * Return whether all elements are True.: Return the label from the index, or, if not present, the previous one.
* all([axis, skipna]): astype(dtype)
  * Return whether all elements are True.: Cast a pandas-on-Spark object to a specified dtype dtype.
* all([axis, skipna]): copy([name, deep])
  * Return whether all elements are True.: Make a copy of this object.
* all([axis, skipna]): delete(loc)
  * Return whether all elements are True.: Make new Index with passed location(-s) deleted.
* all([axis, skipna]): difference(other[, sort])
  * Return whether all elements are True.: Return a new Index with elements from the index that are not in other.
* all([axis, skipna]): drop(labels)
  * Return whether all elements are True.: Make new Index with passed list of labels deleted.
* all([axis, skipna]): drop_duplicates([keep])
  * Return whether all elements are True.: Return Index with duplicate values removed.
* all([axis, skipna]): droplevel(level)
  * Return whether all elements are True.: Return index with requested level(s) removed.
* all([axis, skipna]): dropna([how])
  * Return whether all elements are True.: Return Index or MultiIndex without NA/NaN values
* all([axis, skipna]): equals(other)
  * Return whether all elements are True.: Determine if two Index objects contain the same elements.
* all([axis, skipna]): factorize([sort, use_na_sentinel])
  * Return whether all elements are True.: Encode the object as an enumerated type or categorical variable.
* all([axis, skipna]): fillna(value)
  * Return whether all elements are True.: Fill NA/NaN values with the specified value.
* all([axis, skipna]): get_level_values(level)
  * Return whether all elements are True.: Return Index if a valid level is given.
* all([axis, skipna]): holds_integer()
  * Return whether all elements are True.: Whether the type is an integer type.
* all([axis, skipna]): identical(other)
  * Return whether all elements are True.: Similar to equals, but check that other comparable attributes are also equal.
* all([axis, skipna]): insert(loc, item)
  * Return whether all elements are True.: Make new Index inserting new item at location.
* all([axis, skipna]): intersection(other)
  * Return whether all elements are True.: Form the intersection of two Index objects.
* all([axis, skipna]): is_boolean()
  * Return whether all elements are True.: Return if the current index type is a boolean type.
* all([axis, skipna]): is_categorical()
  * Return whether all elements are True.: Return if the current index type is a categorical type.
* all([axis, skipna]): is_floating()
  * Return whether all elements are True.: Return if the current index type is a floating type.
* all([axis, skipna]): is_integer()
  * Return whether all elements are True.: Return if the current index type is an integer type.
* all([axis, skipna]): is_interval()
  * Return whether all elements are True.: Return if the current index type is an interval type.
* all([axis, skipna]): is_numeric()
  * Return whether all elements are True.: Return if the current index type is a numeric type.
* all([axis, skipna]): is_object()
  * Return whether all elements are True.: Return if the current index type is an object type.
* all([axis, skipna]): isin(values)
  * Return whether all elements are True.: Check whether values are contained in Series or Index.
* all([axis, skipna]): isna()
  * Return whether all elements are True.: Detect existing (non-missing) values.
* all([axis, skipna]): isnull()
  * Return whether all elements are True.: Detect existing (non-missing) values.
* all([axis, skipna]): item()
  * Return whether all elements are True.: Return the first element of the underlying data as a python scalar.
* all([axis, skipna]): map(mapper[, na_action])
  * Return whether all elements are True.: Map values using input correspondence (a dict, Series, or function).
* all([axis, skipna]): max()
  * Return whether all elements are True.: Return the maximum value of the Index.
* all([axis, skipna]): min()
  * Return whether all elements are True.: Return the minimum value of the Index.
* all([axis, skipna]): notna()
  * Return whether all elements are True.: Detect existing (non-missing) values.
* all([axis, skipna]): notnull()
  * Return whether all elements are True.: Detect existing (non-missing) values.
* all([axis, skipna]): nunique([dropna, approx, rsd])
  * Return whether all elements are True.: Return number of unique elements in the object.
* all([axis, skipna]): rename(name[, inplace])
  * Return whether all elements are True.: Alter Index or MultiIndex name.
* all([axis, skipna]): repeat(repeats)
  * Return whether all elements are True.: Repeat elements of a Index/MultiIndex.
* all([axis, skipna]): set_names(names[, level, inplace])
  * Return whether all elements are True.: Set Index or MultiIndex name.
* all([axis, skipna]): shift([periods, fill_value])
  * Return whether all elements are True.: Shift Series/Index by desired number of periods.
* all([axis, skipna]): sort(*args, **kwargs)
  * Return whether all elements are True.: Use sort_values instead.
* all([axis, skipna]): sort_values([return_indexer, ascending])
  * Return whether all elements are True.: Return a sorted copy of the index, and optionally return the indices that sorted the index itself.
* all([axis, skipna]): symmetric_difference(other[, result_name, sort])
  * Return whether all elements are True.: Compute the symmetric difference of two Index objects.
* all([axis, skipna]): take(indices)
  * Return whether all elements are True.: Return the elements in the given positional indices along an axis.
* all([axis, skipna]): to_frame([index, name])
  * Return whether all elements are True.: Create a DataFrame with a column containing the Index.
* all([axis, skipna]): to_list()
  * Return whether all elements are True.: Return a list of the values.
* all([axis, skipna]): to_numpy([dtype, copy])
  * Return whether all elements are True.: A NumPy ndarray representing the values in this Index or MultiIndex.
* all([axis, skipna]): to_pandas()
  * Return whether all elements are True.: Return a pandas Index.
* all([axis, skipna]): to_series([name])
  * Return whether all elements are True.: Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.
* all([axis, skipna]): tolist()
  * Return whether all elements are True.: Return a list of the values.
* all([axis, skipna]): transpose()
  * Return whether all elements are True.: Return the transpose, For index, It will be index itself.
* all([axis, skipna]): union(other[, sort])
  * Return whether all elements are True.: Form the union of two Index objects.
* all([axis, skipna]): unique([level])
  * Return whether all elements are True.: Return unique values in the index.
* all([axis, skipna]): value_counts([normalize, sort, ascending, ...])
  * Return whether all elements are True.: Return a Series containing counts of unique values.
* all([axis, skipna]): view()
  * Return whether all elements are True.: this is defined as a copy with the same identity


Attributes


|T                      |Return the transpose, For index, It will be index itself.           |
|-----------------------|--------------------------------------------------------------------|
|dtype                  |Return the dtype object of the underlying data.                     |
|empty                  |Returns true if the current object is empty.                        |
|has_duplicates         |If index has duplicates, return True, otherwise False.              |
|hasnans                |Return True if it has any missing values.                           |
|inferred_type          |Return a string of the type inferred from the values.               |
|is_monotonic_decreasing|Return boolean if values in the object are monotonically decreasing.|
|is_monotonic_increasing|Return boolean if values in the object are monotonically increasing.|
|is_unique              |Return if the index has unique values.                              |
|name                   |Return name of the Index.                                           |
|names                  |Return names of the Index.                                          |
|ndim                   |Return an int representing the number of array dimensions.          |
|nlevels                |Number of levels in Index & MultiIndex.                             |
|shape                  |Return a tuple of the shape of the underlying data.                 |
|size                   |Return an int representing the number of elements in this object.   |
|values                 |Return an array representing the data in the Index.                 |



# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_monotonic_increasing.html

# pyspark.pandas.Index.is_monotonic_increasing#

_property _Index.is_monotonic_increasing#
    

Return boolean if values in the object are monotonically increasing.

Note

the current implementation of is_monotonic_increasing requires to shuffle and aggregate multiple times to check the order locally and globally, which is potentially expensive. In case of multi-index, all data is transferred to a single node which can easily cause out-of-memory errors.

Note

Disable the Spark config spark.sql.optimizer.nestedSchemaPruning.enabled for multi-index if youâre using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

Returns
    

**is_monotonic** bool
    

Examples
    
    
    >>> ser = ps.Series(['1/1/2018', '3/1/2018', '4/1/2018'])
    >>> ser.is_monotonic_increasing
    True
    
    
    
    >>> df = ps.DataFrame({'dates': [None, '1/1/2018', '2/1/2018', '3/1/2018']})
    >>> df.dates.is_monotonic_increasing
    False
    
    
    
    >>> df.index.is_monotonic_increasing
    True
    
    
    
    >>> ser = ps.Series([1])
    >>> ser.is_monotonic_increasing
    True
    
    
    
    >>> ser = ps.Series([])
    >>> ser.is_monotonic_increasing
    True
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.is_monotonic_increasing
    True
    
    
    
    >>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
    >>> ser.is_monotonic_increasing
    False
    
    
    
    >>> ser.index.is_monotonic_increasing
    True
    

Support for MultiIndex
    
    
    >>> midx = ps.MultiIndex.from_tuples(
    ... [('x', 'a'), ('x', 'b'), ('y', 'c'), ('y', 'd'), ('z', 'e')])
    >>> midx  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('y', 'c'),
                ('y', 'd'),
                ('z', 'e')],
               )
    >>> midx.is_monotonic_increasing
    True
    
    
    
    >>> midx = ps.MultiIndex.from_tuples(
    ... [('z', 'a'), ('z', 'b'), ('y', 'c'), ('y', 'd'), ('x', 'e')])
    >>> midx  
    MultiIndex([('z', 'a'),
                ('z', 'b'),
                ('y', 'c'),
                ('y', 'd'),
                ('x', 'e')],
               )
    >>> midx.is_monotonic_increasing
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_monotonic_increasing.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_monotonic_decreasing.html

# pyspark.pandas.Index.is_monotonic_decreasing#

_property _Index.is_monotonic_decreasing#
    

Return boolean if values in the object are monotonically decreasing.

Note

the current implementation of is_monotonic_decreasing requires to shuffle and aggregate multiple times to check the order locally and globally, which is potentially expensive. In case of multi-index, all data is transferred to a single node which can easily cause out-of-memory errors.

Note

Disable the Spark config spark.sql.optimizer.nestedSchemaPruning.enabled for multi-index if youâre using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

Returns
    

**is_monotonic** bool
    

Examples
    
    
    >>> ser = ps.Series(['4/1/2018', '3/1/2018', '1/1/2018'])
    >>> ser.is_monotonic_decreasing
    True
    
    
    
    >>> df = ps.DataFrame({'dates': [None, '3/1/2018', '2/1/2018', '1/1/2018']})
    >>> df.dates.is_monotonic_decreasing
    False
    
    
    
    >>> df.index.is_monotonic_decreasing
    False
    
    
    
    >>> ser = ps.Series([1])
    >>> ser.is_monotonic_decreasing
    True
    
    
    
    >>> ser = ps.Series([])
    >>> ser.is_monotonic_decreasing
    True
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.is_monotonic_decreasing
    True
    
    
    
    >>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
    >>> ser.is_monotonic_decreasing
    True
    
    
    
    >>> ser.index.is_monotonic_decreasing
    False
    

Support for MultiIndex
    
    
    >>> midx = ps.MultiIndex.from_tuples(
    ... [('x', 'a'), ('x', 'b'), ('y', 'c'), ('y', 'd'), ('z', 'e')])
    >>> midx  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('y', 'c'),
                ('y', 'd'),
                ('z', 'e')],
               )
    >>> midx.is_monotonic_decreasing
    False
    
    
    
    >>> midx = ps.MultiIndex.from_tuples(
    ... [('z', 'e'), ('z', 'd'), ('y', 'c'), ('y', 'b'), ('x', 'a')])
    >>> midx  
    MultiIndex([('z', 'a'),
                ('z', 'b'),
                ('y', 'c'),
                ('y', 'd'),
                ('x', 'e')],
               )
    >>> midx.is_monotonic_decreasing
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_monotonic_decreasing.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_unique.html

# pyspark.pandas.Index.is_unique#

_property _Index.is_unique#
    

Return if the index has unique values.

Examples
    
    
    >>> idx = ps.Index([1, 5, 7, 7])
    >>> idx.is_unique
    False
    
    
    
    >>> idx = ps.Index([1, 5, 7])
    >>> idx.is_unique
    True
    
    
    
    >>> idx = ps.Index(["Watermelon", "Orange", "Apple",
    ...                 "Watermelon"])
    >>> idx.is_unique
    False
    
    
    
    >>> idx = ps.Index(["Orange", "Apple",
    ...                 "Watermelon"])
    >>> idx.is_unique
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_unique.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.has_duplicates.html

# pyspark.pandas.Index.has_duplicates#

_property _Index.has_duplicates#
    

If index has duplicates, return True, otherwise False.

Examples
    
    
    >>> idx = ps.Index([1, 5, 7, 7])
    >>> idx.has_duplicates
    True
    
    
    
    >>> idx = ps.Index([1, 5, 7])
    >>> idx.has_duplicates
    False
    
    
    
    >>> idx = ps.Index(["Watermelon", "Orange", "Apple",
    ...                 "Watermelon"])
    >>> idx.has_duplicates
    True
    
    
    
    >>> idx = ps.Index(["Orange", "Apple",
    ...                 "Watermelon"])
    >>> idx.has_duplicates
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.has_duplicates.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.hasnans.html

# pyspark.pandas.Index.hasnans#

_property _Index.hasnans#
    

Return True if it has any missing values. Otherwise, it returns False.
    
    
    >>> ps.DataFrame({}, index=list('abc')).index.hasnans
    False
    
    
    
    >>> ps.Series(['a', None]).hasnans
    True
    
    
    
    >>> ps.Series([1.0, 2.0, np.nan]).hasnans
    True
    
    
    
    >>> ps.Series([1, 2, 3]).hasnans
    False
    
    
    
    >>> (ps.Series([1.0, 2.0, np.nan]) + 1).hasnans
    True
    
    
    
    >>> ps.Series([1, 2, 3]).rename("a").to_frame().set_index("a").index.hasnans
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.hasnans.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.dtype.html

# pyspark.pandas.Index.dtype#

_property _Index.dtype#
    

Return the dtype object of the underlying data.

Examples
    
    
    >>> s = ps.Series([1, 2, 3])
    >>> s.dtype
    dtype('int64')
    
    
    
    >>> s = ps.Series(list('abc'))
    >>> s.dtype
    dtype('O')
    
    
    
    >>> s = ps.Series(pd.date_range('20130101', periods=3))
    >>> s.dtype
    dtype('<M8[ns]')
    
    
    
    >>> s.rename("a").to_frame().set_index("a").index.dtype
    dtype('<M8[ns]')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.dtype.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.inferred_type.html

# pyspark.pandas.Index.inferred_type#

_property _Index.inferred_type#
    

Return a string of the type inferred from the values.

Examples
    
    
    >>> from datetime import datetime
    >>> ps.Index([1, 2, 3]).inferred_type
    'integer'
    
    
    
    >>> ps.Index([1.0, 2.0, 3.0]).inferred_type
    'floating'
    
    
    
    >>> ps.Index(['a', 'b', 'c']).inferred_type
    'string'
    
    
    
    >>> ps.Index([True, False, True, False]).inferred_type
    'boolean'
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.inferred_type.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.shape.html

# pyspark.pandas.Index.shape#

_property _Index.shape#
    

Return a tuple of the shape of the underlying data.

Examples
    
    
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx
    Index(['a', 'b', 'c'], dtype='object')
    >>> idx.shape
    (3,)
    
    
    
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    >>> midx.shape
    (3,)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.shape.rst.txt)


---

## 🔹 009. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.name.html

# pyspark.pandas.Index.name#

_property _Index.name#
    

Return name of the Index.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.name.rst.txt)


---

## 🔹 010. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.names.html

# pyspark.pandas.Index.names#

_property _Index.names#
    

Return names of the Index.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.names.rst.txt)


---

## 🔹 011. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.ndim.html

# pyspark.pandas.Index.ndim#

_property _Index.ndim#
    

Return an int representing the number of array dimensions.

Return 1 for Series / Index / MultiIndex.

Examples

For Series
    
    
    >>> s = ps.Series([None, 1, 2, 3, 4], index=[4, 5, 2, 1, 8])
    >>> s.ndim
    1
    

For Index
    
    
    >>> s.index.ndim
    1
    

For MultiIndex
    
    
    >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
    ...                       ['speed', 'weight', 'length']],
    ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
    >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
    >>> s.index.ndim
    1
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.ndim.rst.txt)


---

## 🔹 012. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.size.html

# pyspark.pandas.Index.size#

_property _Index.size#
    

Return an int representing the number of elements in this object.

Examples
    
    
    >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
    ...                   columns=['dogs', 'cats'],
    ...                   index=list('abcd'))
    >>> df.index.size
    4
    
    
    
    >>> df.set_index('dogs', append=True).index.size
    4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.size.rst.txt)


---

## 🔹 013. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.nlevels.html

# pyspark.pandas.Index.nlevels#

_property _Index.nlevels#
    

Number of levels in Index & MultiIndex.

Examples
    
    
    >>> psdf = ps.DataFrame({"a": [1, 2, 3]}, index=pd.Index(['a', 'b', 'c'], name="idx"))
    >>> psdf.index.nlevels
    1
    
    
    
    >>> psdf = ps.DataFrame({'a': [1, 2, 3]}, index=[list('abc'), list('def')])
    >>> psdf.index.nlevels
    2
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.nlevels.rst.txt)


---

## 🔹 014. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.empty.html

# pyspark.pandas.Index.empty#

_property _Index.empty#
    

Returns true if the current object is empty. Otherwise, it returns false.
    
    
    >>> ps.range(10).id.empty
    False
    
    
    
    >>> ps.range(0).id.empty
    True
    
    
    
    >>> ps.DataFrame({}, index=list('abc')).index.empty
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.empty.rst.txt)


---

## 🔹 015. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.T.html

# pyspark.pandas.Index.T#

_property _Index.T#
    

Return the transpose, For index, It will be index itself.

Examples
    
    
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx
    Index(['a', 'b', 'c'], dtype='object')
    
    
    
    >>> idx.transpose()
    Index(['a', 'b', 'c'], dtype='object')
    

For MultiIndex
    
    
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    
    
    
    >>> midx.transpose()  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.T.rst.txt)


---

## 🔹 016. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.values.html

# pyspark.pandas.Index.values#

_property _Index.values#
    

Return an array representing the data in the Index.

Warning

We recommend using Index.to_numpy() instead.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driverâs memory.

Returns
    

numpy.ndarray
    

Examples
    
    
    >>> ps.Series([1, 2, 3, 4]).index.values
    array([0, 1, 2, 3])
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index.values
    array([(1, 4), (2, 5), (3, 6)], dtype=object)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.values.rst.txt)


---

## 🔹 017. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.all.html

# pyspark.pandas.Index.all#

Index.all(_axis =0_, _skipna =True_)#
    

Return whether all elements are True.

Returns True unless there at least one element within a series that is False or equivalent (e.g. zero or empty)

Parameters
    

**axis**{0 or âindexâ}, default 0
    

Indicate which axis or axes should be reduced.

  * 0 / âindexâ : reduce the index, return a Series whose index is the original column labels.



**skipna** boolean, default True
    

Exclude NA values, such as None or numpy.NaN. If an entire row/column is NA values and skipna is True, then the result will be True, as for an empty row/column. If skipna is False, numpy.NaNs are treated as True because these are not equal to zero, Nones are treated as False.

Examples
    
    
    >>> ps.Series([True, True]).all()
    True
    
    
    
    >>> ps.Series([True, False]).all()
    False
    
    
    
    >>> ps.Series([0, 1]).all()
    False
    
    
    
    >>> ps.Series([1, 2, 3]).all()
    True
    
    
    
    >>> ps.Series([True, True, None]).all()
    True
    
    
    
    >>> ps.Series([True, True, None]).all(skipna=False)
    False
    
    
    
    >>> ps.Series([True, False, None]).all()
    False
    
    
    
    >>> ps.Series([]).all()
    True
    
    
    
    >>> ps.Series([np.nan]).all()
    True
    
    
    
    >>> ps.Series([np.nan]).all(skipna=False)
    True
    
    
    
    >>> ps.Series([None]).all()
    True
    
    
    
    >>> ps.Series([None]).all(skipna=False)
    False
    
    
    
    >>> df = ps.Series([True, False, None]).rename("a").to_frame()
    >>> df.set_index("a").index.all()
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.all.rst.txt)


---

## 🔹 018. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.any.html

# pyspark.pandas.Index.any#

Index.any(_axis =0_)#
    

Return whether any element is True.

Returns False unless there is at least one element within a series that is True or equivalent (e.g. non-zero or non-empty).

Parameters
    

**axis**{0 or âindexâ}, default 0
    

Indicate which axis or axes should be reduced.

  * 0 / âindexâ : reduce the index, return a Series whose index is the original column labels.




Examples
    
    
    >>> ps.Series([False, False]).any()
    False
    
    
    
    >>> ps.Series([True, False]).any()
    True
    
    
    
    >>> ps.Series([0, 0]).any()
    False
    
    
    
    >>> ps.Series([0, 1, 2]).any()
    True
    
    
    
    >>> ps.Series([False, False, None]).any()
    False
    
    
    
    >>> ps.Series([True, False, None]).any()
    True
    
    
    
    >>> ps.Series([]).any()
    False
    
    
    
    >>> ps.Series([np.nan]).any()
    False
    
    
    
    >>> df = ps.Series([True, False, None]).rename("a").to_frame()
    >>> df.set_index("a").index.any()
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.any.rst.txt)


---

## 🔹 019. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.argmin.html

# pyspark.pandas.Index.argmin#

Index.argmin()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.argmin)#
    

Return a minimum argument indexer.

Parameters
    

**skipna** bool, default True
    
Returns
    

minimum argument indexer
    

Examples
    
    
    >>> psidx = ps.Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3])
    >>> psidx
    Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3], dtype='int64')
    
    
    
    >>> psidx.argmin()
    7
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.argmin.rst.txt)


---

## 🔹 020. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.argmax.html

# pyspark.pandas.Index.argmax#

Index.argmax()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.argmax)#
    

Return a maximum argument indexer.

Parameters
    

**skipna** bool, default True
    
Returns
    

maximum argument indexer
    

Examples
    
    
    >>> psidx = ps.Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3])
    >>> psidx
    Index([10, 9, 8, 7, 100, 5, 4, 3, 100, 3], dtype='int64')
    
    
    
    >>> psidx.argmax()
    4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.argmax.rst.txt)


---

## 🔹 021. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.copy.html

# pyspark.pandas.Index.copy#

Index.copy(_name =None_, _deep =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.copy)#
    

Make a copy of this object. name sets those attributes on the new object.

Parameters
    

**name** string, optional
    

to set name of index

**deep** None
    

this parameter is not supported but just dummy parameter to match pandas.

Examples
    
    
    >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
    ...                   index=['cobra', 'viper', 'sidewinder'],
    ...                   columns=['max_speed', 'shield'])
    >>> df
                max_speed  shield
    cobra               1       2
    viper               4       5
    sidewinder          7       8
    >>> df.index
    Index(['cobra', 'viper', 'sidewinder'], dtype='object')
    

Copy index
    
    
    >>> df.index.copy()
    Index(['cobra', 'viper', 'sidewinder'], dtype='object')
    

Copy index with name
    
    
    >>> df.index.copy(name='snake')
    Index(['cobra', 'viper', 'sidewinder'], dtype='object', name='snake')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.copy.rst.txt)


---

## 🔹 022. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.delete.html

# pyspark.pandas.Index.delete#

Index.delete(_loc_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.delete)#
    

Make new Index with passed location(-s) deleted.

Note

this API can be pretty expensive since it is based on a global sequence internally.

Returns
    

**new_index** Index
    

Examples
    
    
    >>> psidx = ps.Index([10, 10, 9, 8, 4, 2, 4, 4, 2, 2, 10, 10])
    >>> psidx
    Index([10, 10, 9, 8, 4, 2, 4, 4, 2, 2, 10, 10], dtype='int64')
    
    
    
    >>> psidx.delete(0).sort_values()
    Index([2, 2, 2, 4, 4, 4, 8, 9, 10, 10, 10], dtype='int64')
    
    
    
    >>> psidx.delete([0, 1, 2, 3, 10, 11]).sort_values()
    Index([2, 2, 2, 4, 4, 4], dtype='int64')
    

MultiIndex
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)])
    >>> psidx  
    MultiIndex([('a', 'x', 1),
                ('b', 'y', 2),
                ('c', 'z', 3)],
               )
    
    
    
    >>> psidx.delete([0, 2]).sort_values()  
    MultiIndex([('b', 'y', 2)],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.delete.rst.txt)


---

## 🔹 023. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.equals.html

# pyspark.pandas.Index.equals#

Index.equals(_other_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.equals)#
    

Determine if two Index objects contain the same elements.

Returns
    

bool
    

True if âotherâ is an Index and it has the same elements as calling index; False otherwise.

Examples
    
    
    >>> from pyspark.pandas.config import option_context
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx.name = "name"
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx.names = ("nameA", "nameB")
    

For Index
    
    
    >>> idx.equals(idx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.equals(ps.Index(['a', 'b', 'c']))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.equals(ps.Index(['b', 'b', 'a']))
    False
    >>> idx.equals(midx)
    False
    

For MultiIndex
    
    
    >>> midx.equals(midx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.equals(ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.equals(ps.MultiIndex.from_tuples([('c', 'z'), ('b', 'y'), ('a', 'x')]))
    False
    >>> midx.equals(idx)
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.equals.rst.txt)


---

## 🔹 024. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.factorize.html

# pyspark.pandas.Index.factorize#

Index.factorize(_sort =True_, _use_na_sentinel =True_)#
    

Encode the object as an enumerated type or categorical variable.

This method is useful for obtaining a numeric representation of an array when all that matters is identifying distinct values.

Parameters
    

**sort** bool, default True
    
**use_na_sentinel** bool, default True
    

If True, the sentinel -1 will be used for NaN values, effectively assigning them a distinct category. If False, NaN values will be encoded as non-negative integers, treating them as unique categories in the encoding process and retaining them in the set of unique categories in the data.

Returns
    

**codes** Series or Index
    

A Series or Index thatâs an indexer into uniques. `uniques.take(codes)` will have the same values as values.

**uniques** pd.Index
    

The unique valid values.

Note

Even if thereâs a missing value in values, uniques will _not_ contain an entry for it.

Examples
    
    
    >>> psser = ps.Series(['b', None, 'a', 'c', 'b'])
    >>> codes, uniques = psser.factorize()
    >>> codes
    0    1
    1   -1
    2    0
    3    2
    4    1
    dtype: int32
    >>> uniques
    Index(['a', 'b', 'c'], dtype='object')
    
    
    
    >>> codes, uniques = psser.factorize(use_na_sentinel=False)
    >>> codes
    0    1
    1    3
    2    0
    3    2
    4    1
    dtype: int32
    >>> uniques
    Index(['a', 'b', 'c', None], dtype='object')
    

For Index:
    
    
    >>> psidx = ps.Index(['b', None, 'a', 'c', 'b'])
    >>> codes, uniques = psidx.factorize()
    >>> codes
    Index([1, -1, 0, 2, 1], dtype='int32')
    >>> uniques
    Index(['a', 'b', 'c'], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.factorize.rst.txt)


---

## 🔹 025. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.identical.html

# pyspark.pandas.Index.identical#

Index.identical(_other_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.identical)#
    

Similar to equals, but check that other comparable attributes are also equal.

Returns
    

bool
    

If two Index objects have equal elements and same type True, otherwise False.

Examples
    
    
    >>> from pyspark.pandas.config import option_context
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    

For Index
    
    
    >>> idx.identical(idx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.identical(ps.Index(['a', 'b', 'c']))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.identical(ps.Index(['b', 'b', 'a']))
    False
    >>> idx.identical(midx)
    False
    

For MultiIndex
    
    
    >>> midx.identical(midx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.identical(ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.identical(ps.MultiIndex.from_tuples([('c', 'z'), ('b', 'y'), ('a', 'x')]))
    False
    >>> midx.identical(idx)
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.identical.rst.txt)


---

## 🔹 026. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.insert.html

# pyspark.pandas.Index.insert#

Index.insert(_loc_ , _item_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.insert)#
    

Make new Index inserting new item at location.

Follows Python list.append semantics for negative values.

Changed in version 3.4.0: Raise IndexError when loc is out of bounds to follow Pandas 1.4+ behavior

Parameters
    

**loc** int
    
**item** object
    
Returns
    

**new_index** Index
    

Examples
    
    
    >>> psidx = ps.Index([1, 2, 3, 4, 5])
    >>> psidx.insert(3, 100)
    Index([1, 2, 3, 100, 4, 5], dtype='int64')
    

For negative values
    
    
    >>> psidx = ps.Index([1, 2, 3, 4, 5])
    >>> psidx.insert(-3, 100)
    Index([1, 2, 100, 3, 4, 5], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.insert.rst.txt)


---

## 🔹 027. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_boolean.html

# pyspark.pandas.Index.is_boolean#

Index.is_boolean()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_boolean)#
    

Return if the current index type is a boolean type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=[True]).index.is_boolean()
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_boolean.rst.txt)


---

## 🔹 028. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_categorical.html

# pyspark.pandas.Index.is_categorical#

Index.is_categorical()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_categorical)#
    

Return if the current index type is a categorical type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_categorical()
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_categorical.rst.txt)


---

## 🔹 029. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_floating.html

# pyspark.pandas.Index.is_floating#

Index.is_floating()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_floating)#
    

Return if the current index type is a floating type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_floating()
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_floating.rst.txt)


---

## 🔹 030. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_integer.html

# pyspark.pandas.Index.is_integer#

Index.is_integer()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_integer)#
    

Return if the current index type is an integer type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_integer()
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_integer.rst.txt)


---

## 🔹 031. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_interval.html

# pyspark.pandas.Index.is_interval#

Index.is_interval()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_interval)#
    

Return if the current index type is an interval type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_interval()
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_interval.rst.txt)


---

## 🔹 032. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_numeric.html

# pyspark.pandas.Index.is_numeric#

Index.is_numeric()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_numeric)#
    

Return if the current index type is a numeric type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=[1]).index.is_numeric()
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_numeric.rst.txt)


---

## 🔹 033. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.is_object.html

# pyspark.pandas.Index.is_object#

Index.is_object()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.is_object)#
    

Return if the current index type is an object type.

Examples
    
    
    >>> ps.DataFrame({'a': [1]}, index=["a"]).index.is_object()
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.is_object.rst.txt)


---

## 🔹 034. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.drop.html

# pyspark.pandas.Index.drop#

Index.drop(_labels_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.drop)#
    

Make new Index with passed list of labels deleted.

Parameters
    

**labels** array-like
    
Returns
    

**dropped** Index
    

Examples
    
    
    >>> index = ps.Index([1, 2, 3])
    >>> index
    Index([1, 2, 3], dtype='int64')
    
    
    
    >>> index.drop([1])
    Index([2, 3], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.drop.rst.txt)


---

## 🔹 035. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.drop_duplicates.html

# pyspark.pandas.Index.drop_duplicates#

Index.drop_duplicates(_keep ='first'_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.drop_duplicates)#
    

Return Index with duplicate values removed.

Parameters
    

**keep**{âfirstâ, âlastâ, `False`}, default âfirstâ
    

Method to handle dropping duplicates: \- âfirstâ : Drop duplicates except for the first occurrence. \- âlastâ : Drop duplicates except for the last occurrence. \- `False` : Drop all duplicates.

Returns
    

**deduplicated** Index
    

See also

[`Series.drop_duplicates`](pyspark.pandas.Series.drop_duplicates.html#pyspark.pandas.Series.drop_duplicates "pyspark.pandas.Series.drop_duplicates")
    

Equivalent method on Series.

[`DataFrame.drop_duplicates`](pyspark.pandas.DataFrame.drop_duplicates.html#pyspark.pandas.DataFrame.drop_duplicates "pyspark.pandas.DataFrame.drop_duplicates")
    

Equivalent method on DataFrame.

Examples

Generate an Index with duplicate values.
    
    
    >>> idx = ps.Index(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'])
    
    
    
    >>> idx.drop_duplicates().sort_values()
    Index(['beetle', 'cow', 'hippo', 'lama'], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.drop_duplicates.rst.txt)


---

## 🔹 036. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.min.html

# pyspark.pandas.Index.min#

Index.min()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.min)#
    

Return the minimum value of the Index.

Returns
    

scalar
    

Minimum value.

See also

[`Index.max`](pyspark.pandas.Index.max.html#pyspark.pandas.Index.max "pyspark.pandas.Index.max")
    

Return the maximum value of the object.

[`Series.min`](pyspark.pandas.Series.min.html#pyspark.pandas.Series.min "pyspark.pandas.Series.min")
    

Return the minimum value in a Series.

[`DataFrame.min`](pyspark.pandas.DataFrame.min.html#pyspark.pandas.DataFrame.min "pyspark.pandas.DataFrame.min")
    

Return the minimum values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([3, 2, 1])
    >>> idx.min()
    1
    
    
    
    >>> idx = ps.Index(['c', 'b', 'a'])
    >>> idx.min()
    'a'
    

For a MultiIndex, the maximum is determined lexicographically.
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
    >>> idx.min()
    ('a', 'x', 1)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.min.rst.txt)


---

## 🔹 037. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.max.html

# pyspark.pandas.Index.max#

Index.max()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.max)#
    

Return the maximum value of the Index.

Returns
    

scalar
    

Maximum value.

See also

[`Index.min`](pyspark.pandas.Index.min.html#pyspark.pandas.Index.min "pyspark.pandas.Index.min")
    

Return the minimum value in an Index.

[`Series.max`](pyspark.pandas.Series.max.html#pyspark.pandas.Series.max "pyspark.pandas.Series.max")
    

Return the maximum value in a Series.

[`DataFrame.max`](pyspark.pandas.DataFrame.max.html#pyspark.pandas.DataFrame.max "pyspark.pandas.DataFrame.max")
    

Return the maximum values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([3, 2, 1])
    >>> idx.max()
    3
    
    
    
    >>> idx = ps.Index(['c', 'b', 'a'])
    >>> idx.max()
    'c'
    

For a MultiIndex, the maximum is determined lexicographically.
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
    >>> idx.max()
    ('b', 'y', 2)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.max.rst.txt)


---

## 🔹 038. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.map.html

# pyspark.pandas.Index.map#

Index.map(_mapper_ , _na_action =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.map)#
    

Map values using input correspondence (a dict, Series, or function).

Parameters
    

**mapper** function, dict, or pd.Series
    

Mapping correspondence.

**na_action**{None, âignoreâ}
    

If âignoreâ, propagate NA values, without passing them to the mapping correspondence.

Returns
    

**applied** Index, inferred
    

The output of the mapping function applied to the index.

Examples
    
    
    >>> psidx = ps.Index([1, 2, 3])
    
    
    
    >>> psidx.map({1: "one", 2: "two", 3: "three"})
    Index(['one', 'two', 'three'], dtype='object')
    
    
    
    >>> psidx.map(lambda id: "{id} + 1".format(id=id))
    Index(['1 + 1', '2 + 1', '3 + 1'], dtype='object')
    
    
    
    >>> pser = pd.Series(["one", "two", "three"], index=[1, 2, 3])
    >>> psidx.map(pser)
    Index(['one', 'two', 'three'], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.map.rst.txt)


---

## 🔹 039. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.rename.html

# pyspark.pandas.Index.rename#

Index.rename(_name_ , _inplace =False_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.rename)#
    

Alter Index or MultiIndex name. Able to set new names without level. Defaults to returning a new index.

Parameters
    

**name** label or list of labels
    

Name(s) to set.

**inplace** boolean, default False
    

Modifies the object directly, instead of creating a new Index or MultiIndex.

Returns
    

Index or MultiIndex
    

The same type as the caller or None if inplace is True.

Examples
    
    
    >>> df = ps.DataFrame({'a': ['A', 'C'], 'b': ['A', 'B']}, columns=['a', 'b'])
    >>> df.index.rename("c")
    Index([0, 1], dtype='int64', name='c')
    
    
    
    >>> df.set_index("a", inplace=True)
    >>> df.index.rename("d")
    Index(['A', 'C'], dtype='object', name='d')
    

You can also change the index name in place.
    
    
    >>> df.index.rename("e", inplace=True)
    >>> df.index
    Index(['A', 'C'], dtype='object', name='e')
    
    
    
    >>> df  
       b
    e
    A  A
    C  B
    

Support for MultiIndex
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
    >>> psidx.names = ['hello', 'pandas-on-Spark']
    >>> psidx  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               names=['hello', 'pandas-on-Spark'])
    
    
    
    >>> psidx.rename(['aloha', 'databricks'])  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               names=['aloha', 'databricks'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.rename.rst.txt)


---

## 🔹 040. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.repeat.html

# pyspark.pandas.Index.repeat#

Index.repeat(_repeats_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.repeat)#
    

Repeat elements of a Index/MultiIndex.

Returns a new Index/MultiIndex where each element of the current Index/MultiIndex is repeated consecutively a given number of times.

Parameters
    

**repeats** int
    

The number of repetitions for each element. This should be a non-negative integer. Repeating 0 times will return an empty Index.

Returns
    

**repeated_index** Index/MultiIndex
    

Newly created Index/MultiIndex with repeated elements.

See also

[`Series.repeat`](pyspark.pandas.Series.repeat.html#pyspark.pandas.Series.repeat "pyspark.pandas.Series.repeat")
    

Equivalent function for Series.

Examples
    
    
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx
    Index(['a', 'b', 'c'], dtype='object')
    >>> idx.repeat(2)
    Index(['a', 'b', 'c', 'a', 'b', 'c'], dtype='object')
    

For MultiIndex,
    
    
    >>> midx = ps.MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'c')])
    >>> midx  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('y', 'c')],
               )
    >>> midx.repeat(2)  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('y', 'c'),
                ('x', 'a'),
                ('x', 'b'),
                ('y', 'c')],
               )
    >>> midx.repeat(0)  
    MultiIndex([], )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.repeat.rst.txt)


---

## 🔹 041. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.take.html

# pyspark.pandas.Index.take#

Index.take(_indices_)#
    

Return the elements in the given _positional_ indices along an axis.

This means that we are not indexing according to actual values in the index attribute of the object. We are indexing according to the actual position of the element in the object.

Parameters
    

**indices** array-like
    

An array of ints indicating which positions to take.

Returns
    

**taken** same type as caller
    

An array-like containing the elements taken from the object.

See also

[`DataFrame.loc`](pyspark.pandas.DataFrame.loc.html#pyspark.pandas.DataFrame.loc "pyspark.pandas.DataFrame.loc")
    

Select a subset of a DataFrame by labels.

[`DataFrame.iloc`](pyspark.pandas.DataFrame.iloc.html#pyspark.pandas.DataFrame.iloc "pyspark.pandas.DataFrame.iloc")
    

Select a subset of a DataFrame by positions.

`numpy.take`
    

Take elements from an array along an axis.

Examples

Series
    
    
    >>> psser = ps.Series([100, 200, 300, 400, 500])
    >>> psser
    0    100
    1    200
    2    300
    3    400
    4    500
    dtype: int64
    
    
    
    >>> psser.take([0, 2, 4]).sort_index()
    0    100
    2    300
    4    500
    dtype: int64
    

Index
    
    
    >>> psidx = ps.Index([100, 200, 300, 400, 500])
    >>> psidx
    Index([100, 200, 300, 400, 500], dtype='int64')
    
    
    
    >>> psidx.take([0, 2, 4]).sort_values()
    Index([100, 300, 500], dtype='int64')
    

MultiIndex
    
    
    >>> psmidx = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c")])
    >>> psmidx  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('x', 'c')],
               )
    
    
    
    >>> psmidx.take([0, 2])  
    MultiIndex([('x', 'a'),
                ('x', 'c')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.take.rst.txt)


---

## 🔹 042. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.unique.html

# pyspark.pandas.Index.unique#

Index.unique(_level =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.unique)#
    

Return unique values in the index.

Be aware the order of unique values might be different than pandas.Index.unique

Parameters
    

**level** int or str, optional, default is None
    
Returns
    

Index without duplicates
    

See also

[`Series.unique`](pyspark.pandas.Series.unique.html#pyspark.pandas.Series.unique "pyspark.pandas.Series.unique")
    
[`groupby.SeriesGroupBy.unique`](pyspark.pandas.groupby.SeriesGroupBy.unique.html#pyspark.pandas.groupby.SeriesGroupBy.unique "pyspark.pandas.groupby.SeriesGroupBy.unique")
    

Examples
    
    
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[1, 1, 3]).index.unique().sort_values()
    Index([1, 3], dtype='int64')
    
    
    
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=['d', 'e', 'e']).index.unique().sort_values()
    Index(['d', 'e'], dtype='object')
    

MultiIndex
    
    
    >>> ps.MultiIndex.from_tuples([("A", "X"), ("A", "Y"), ("A", "X")]).unique()
    ... 
    MultiIndex([('A', 'X'),
                ('A', 'Y')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.unique.rst.txt)


---

## 🔹 043. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.nunique.html

# pyspark.pandas.Index.nunique#

Index.nunique(_dropna =True_, _approx =False_, _rsd =0.05_)#
    

Return number of unique elements in the object. Excludes NA values by default.

Parameters
    

**dropna** bool, default True
    

Donât include NaN in the count.

**approx: bool, default False**
    

If False, will use the exact algorithm and return the exact number of unique. If True, it uses the HyperLogLog approximate algorithm, which is significantly faster for large amount of data. Note: This parameter is specific to pandas-on-Spark and is not found in pandas.

**rsd: float, default 0.05**
    

Maximum estimation error allowed in the HyperLogLog algorithm. Note: Just like `approx` this parameter is specific to pandas-on-Spark.

Returns
    

int
    

See also

[`DataFrame.nunique`](pyspark.pandas.DataFrame.nunique.html#pyspark.pandas.DataFrame.nunique "pyspark.pandas.DataFrame.nunique")
    

Method nunique for DataFrame.

[`Series.count`](pyspark.pandas.Series.count.html#pyspark.pandas.Series.count "pyspark.pandas.Series.count")
    

Count non-NA/null observations in the Series.

Examples
    
    
    >>> ps.Series([1, 2, 3, np.nan]).nunique()
    3
    
    
    
    >>> ps.Series([1, 2, 3, np.nan]).nunique(dropna=False)
    4
    

On big data, we recommend using the approximate algorithm to speed up this function. The result will be very close to the exact unique count.
    
    
    >>> ps.Series([1, 2, 3, np.nan]).nunique(approx=True)
    3
    
    
    
    >>> idx = ps.Index([1, 1, 2, None])
    >>> idx
    Index([1.0, 1.0, 2.0, nan], dtype='float64')
    
    
    
    >>> idx.nunique()
    2
    
    
    
    >>> idx.nunique(dropna=False)
    3
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.nunique.rst.txt)


---

## 🔹 044. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.value_counts.html

# pyspark.pandas.Index.value_counts#

Index.value_counts(_normalize =False_, _sort =True_, _ascending =False_, _bins =None_, _dropna =True_)#
    

Return a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

Parameters
    

**normalize** boolean, default False
    

If True then the object returned will contain the relative frequencies of the unique values.

**sort** boolean, default True
    

Sort by values.

**ascending** boolean, default False
    

Sort in ascending order.

**bins** Not Yet Supported
    
**dropna** boolean, default True
    

Donât include counts of NaN.

Returns
    

**counts** Series
    

See also

[`Series.count`](pyspark.pandas.Series.count.html#pyspark.pandas.Series.count "pyspark.pandas.Series.count")
    

Number of non-NA elements in a Series.

Examples

For Series
    
    
    >>> df = ps.DataFrame({'x':[0, 0, 1, 1, 1, np.nan]})
    >>> df.x.value_counts()  
    x
    1.0    3
    0.0    2
    Name: count, dtype: int64
    

With normalize set to True, returns the relative frequency by dividing all values by the sum of values.
    
    
    >>> df.x.value_counts(normalize=True)  
    x
    1.0    0.6
    0.0    0.4
    Name: proportion, dtype: float64
    

**dropna** With dropna set to False we can also see NaN index values.
    
    
    >>> df.x.value_counts(dropna=False)  
    x
    1.0    3
    0.0    2
    NaN    1
    Name: count, dtype: int64
    

For Index
    
    
    >>> idx = ps.Index([3, 1, 2, 3, 4, np.nan])
    >>> idx
    Index([3.0, 1.0, 2.0, 3.0, 4.0, nan], dtype='float64')
    
    
    
    >>> idx.value_counts().sort_index()
    1.0    1
    2.0    1
    3.0    2
    4.0    1
    Name: count, dtype: int64
    

**sort**

With sort set to False, the result wouldnât be sorted by number of count.
    
    
    >>> idx.value_counts(sort=True).sort_index()
    1.0    1
    2.0    1
    3.0    2
    4.0    1
    Name: count, dtype: int64
    

**normalize**

With normalize set to True, returns the relative frequency by dividing all values by the sum of values.
    
    
    >>> idx.value_counts(normalize=True).sort_index()
    1.0    0.2
    2.0    0.2
    3.0    0.4
    4.0    0.2
    Name: proportion, dtype: float64
    

**dropna**

With dropna set to False we can also see NaN index values.
    
    
    >>> idx.value_counts(dropna=False).sort_index()  
    1.0    1
    2.0    1
    3.0    2
    4.0    1
    NaN    1
    dtype: int64
    

For MultiIndex.
    
    
    >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
    ...                       ['speed', 'weight', 'length']],
    ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
    >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
    >>> s.index  
    MultiIndex([(  'lama', 'weight'),
                (  'lama', 'weight'),
                (  'lama', 'weight'),
                (   'cow', 'weight'),
                (   'cow', 'weight'),
                (   'cow', 'length'),
                ('falcon', 'weight'),
                ('falcon', 'length'),
                ('falcon', 'length')],
               )
    
    
    
    >>> s.index.value_counts().sort_index()
    (cow, length)       1
    (cow, weight)       2
    (falcon, length)    2
    (falcon, weight)    1
    (lama, weight)      3
    Name: count, dtype: int64
    
    
    
    >>> s.index.value_counts(normalize=True).sort_index()
    (cow, length)       0.111111
    (cow, weight)       0.222222
    (falcon, length)    0.222222
    (falcon, weight)    0.111111
    (lama, weight)      0.333333
    Name: proportion, dtype: float64
    

If Index has name, keep the name up.
    
    
    >>> idx = ps.Index([0, 0, 0, 1, 1, 2, 3], name='pandas-on-Spark')
    >>> idx.value_counts().sort_index()
    pandas-on-Spark
    0    3
    1    2
    2    1
    3    1
    Name: count, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.value_counts.rst.txt)


---

## 🔹 045. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.set_names.html

# pyspark.pandas.Index.set_names#

Index.set_names(_names_ , _level =None_, _inplace =False_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.set_names)#
    

Set Index or MultiIndex name. Able to set new names partially and by level.

Parameters
    

**names** label or list of label
    

Name(s) to set.

**level** int, label or list of int or label, optional
    

If the index is a MultiIndex, level(s) to set (None for all levels). Otherwise level must be None.

**inplace** bool, default False
    

Modifies the object directly, instead of creating a new Index or MultiIndex.

Returns
    

Index
    

The same type as the caller or None if inplace is True.

See also

[`Index.rename`](pyspark.pandas.Index.rename.html#pyspark.pandas.Index.rename "pyspark.pandas.Index.rename")
    

Able to set new names without level.

Examples
    
    
    >>> idx = ps.Index([1, 2, 3, 4])
    >>> idx
    Index([1, 2, 3, 4], dtype='int64')
    
    
    
    >>> idx.set_names('quarter')
    Index([1, 2, 3, 4], dtype='int64', name='quarter')
    

For MultiIndex
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
    >>> idx  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               )
    
    
    
    >>> idx.set_names(['kind', 'year'], inplace=True)
    >>> idx  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               names=['kind', 'year'])
    
    
    
    >>> idx.set_names('species', level=0)  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               names=['species', 'year'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.set_names.rst.txt)


---

## 🔹 046. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.droplevel.html

# pyspark.pandas.Index.droplevel#

Index.droplevel(_level_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.droplevel)#
    

Return index with requested level(s) removed. If resulting index has only 1 level left, the result will be of Index type, not MultiIndex.

Parameters
    

**level** int, str, tuple, or list-like, default 0
    

If a string is given, must be the name of a level If list-like, elements must be names or indexes of levels.

Returns
    

Index or MultiIndex
    

Examples
    
    
    >>> midx = ps.DataFrame({'a': ['a', 'b']}, index=[['a', 'x'], ['b', 'y'], [1, 2]]).index
    >>> midx  
    MultiIndex([('a', 'b', 1),
                ('x', 'y', 2)],
               )
    >>> midx.droplevel([0, 1])
    Index([1, 2], dtype='int64')
    >>> midx.droplevel(0)  
    MultiIndex([('b', 1),
                ('y', 2)],
               )
    >>> midx.names = [("a", "b"), "b", "c"]
    >>> midx.droplevel([('a', 'b')])  
    MultiIndex([('b', 1),
                ('y', 2)],
               names=['b', 'c'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.droplevel.rst.txt)


---

## 🔹 047. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.fillna.html

# pyspark.pandas.Index.fillna#

Index.fillna(_value_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.fillna)#
    

Fill NA/NaN values with the specified value.

Parameters
    

**value** scalar
    

Scalar value to use to fill holes (example: 0). This value cannot be a list-likes.

Returns
    

Index
    

filled with value

Examples
    
    
    >>> idx = ps.Index([1, 2, None])
    >>> idx
    Index([1.0, 2.0, nan], dtype='float64')
    
    
    
    >>> idx.fillna(0)
    Index([1.0, 2.0, 0.0], dtype='float64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.fillna.rst.txt)


---

## 🔹 048. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.dropna.html

# pyspark.pandas.Index.dropna#

Index.dropna(_how ='any'_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.dropna)#
    

Return Index or MultiIndex without NA/NaN values

Parameters
    

**how**{âanyâ, âallâ}, default âanyâ
    

If the Index is a MultiIndex, drop the value when any or all levels are NaN.

Returns
    

Index or MultiIndex
    

Examples
    
    
    >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
    ...                   index=['cobra', 'viper', None],
    ...                   columns=['max_speed', 'shield'])
    >>> df  
           max_speed  shield
    cobra          1       2
    viper          4       5
    None           7       8
    
    
    
    >>> df.index.dropna()
    Index(['cobra', 'viper'], dtype='object')
    

Also support for MultiIndex
    
    
    >>> tuples = [(np.nan, 1.0), (2.0, 2.0), (np.nan, np.nan), (3.0, np.nan)]
    >>> midx = ps.MultiIndex.from_tuples(tuples)
    >>> midx  
    MultiIndex([(nan, 1.0),
                (2.0, 2.0),
                (nan, nan),
                (3.0, nan)],
               )
    
    
    
    >>> midx.dropna()  
    MultiIndex([(2.0, 2.0)],
               )
    
    
    
    >>> midx.dropna(how="all")  
    MultiIndex([(nan, 1.0),
                (2.0, 2.0),
                (3.0, nan)],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.dropna.rst.txt)


---

## 🔹 049. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.isna.html

# pyspark.pandas.Index.isna#

Index.isna()#
    

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, get mapped to True values. Everything else gets mapped to False values. Characters such as empty strings ââ or numpy.inf are not considered NA values

Returns
    

**Series or Index** Mask of bool values for each element in Series
    

that indicates whether an element is not an NA value.

Examples
    
    
    >>> ser = ps.Series([5, 6, np.nan])
    >>> ser.isna()  
    0    False
    1    False
    2     True
    dtype: bool
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.isna()  
    Index([False, False, True], dtype='bool', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.isna.rst.txt)


---

## 🔹 050. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.isnull.html

# pyspark.pandas.Index.isnull#

Index.isnull()#
    

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, get mapped to True values. Everything else gets mapped to False values. Characters such as empty strings ââ or numpy.inf are not considered NA values

Returns
    

**Series or Index** Mask of bool values for each element in Series
    

that indicates whether an element is not an NA value.

Examples
    
    
    >>> ser = ps.Series([5, 6, np.nan])
    >>> ser.isna()  
    0    False
    1    False
    2     True
    dtype: bool
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.isna()  
    Index([False, False, True], dtype='bool', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.isnull.rst.txt)


---

## 🔹 051. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.notna.html

# pyspark.pandas.Index.notna#

Index.notna()#
    

Detect existing (non-missing) values. Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. Characters such as empty strings ââ or numpy.inf are not considered NA values NA values, such as None or numpy.NaN, get mapped to False values.

Returns
    

**Series or Index** Mask of bool values for each element in Series
    

that indicates whether an element is not an NA value.

Examples

Show which entries in a Series are not NA.
    
    
    >>> ser = ps.Series([5, 6, np.nan])
    >>> ser
    0    5.0
    1    6.0
    2    NaN
    dtype: float64
    
    
    
    >>> ser.notna()
    0     True
    1     True
    2    False
    dtype: bool
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.notna()  
    Index([True, True, False], dtype='bool', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.notna.rst.txt)


---

## 🔹 052. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.notnull.html

# pyspark.pandas.Index.notnull#

Index.notnull()#
    

Detect existing (non-missing) values. Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. Characters such as empty strings ââ or numpy.inf are not considered NA values NA values, such as None or numpy.NaN, get mapped to False values.

Returns
    

**Series or Index** Mask of bool values for each element in Series
    

that indicates whether an element is not an NA value.

Examples

Show which entries in a Series are not NA.
    
    
    >>> ser = ps.Series([5, 6, np.nan])
    >>> ser
    0    5.0
    1    6.0
    2    NaN
    dtype: float64
    
    
    
    >>> ser.notna()
    0     True
    1     True
    2    False
    dtype: bool
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.notna()  
    Index([True, True, False], dtype='bool', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.notnull.rst.txt)


---

## 🔹 053. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.astype.html

# pyspark.pandas.Index.astype#

Index.astype(_dtype_)#
    

Cast a pandas-on-Spark object to a specified dtype `dtype`.

Parameters
    

**dtype** data type
    

Use a numpy.dtype or Python type to cast entire pandas object to the same type.

Returns
    

**casted** same type as caller
    

See also

[`to_datetime`](pyspark.pandas.to_datetime.html#pyspark.pandas.to_datetime "pyspark.pandas.to_datetime")
    

Convert argument to datetime.

Examples
    
    
    >>> ser = ps.Series([1, 2], dtype='int32')
    >>> ser
    0    1
    1    2
    dtype: int32
    
    
    
    >>> ser.astype('int64')
    0    1
    1    2
    dtype: int64
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.astype('int64')
    Index([1, 2], dtype='int64', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.astype.rst.txt)


---

## 🔹 054. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.item.html

# pyspark.pandas.Index.item#

Index.item()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.item)#
    

Return the first element of the underlying data as a python scalar.

Returns
    

scalar
    

The first element of Index.

Raises
    

ValueError
    

If the data is not length-1.

Examples
    
    
    >>> psidx = ps.Index([10])
    >>> psidx.item()
    10
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.item.rst.txt)


---

## 🔹 055. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.to_list.html

# pyspark.pandas.Index.to_list#

Index.to_list()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.to_list)#
    

Return a list of the values.

These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)

Note

This method should only be used if the resulting list is expected to be small, as all the data is loaded into the driverâs memory.

Examples

Index
    
    
    >>> idx = ps.Index([1, 2, 3, 4, 5])
    >>> idx.to_list()
    [1, 2, 3, 4, 5]
    

MultiIndex
    
    
    >>> tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
    >>> midx = ps.MultiIndex.from_tuples(tuples)
    >>> midx.to_list()
    [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.to_list.rst.txt)


---

## 🔹 056. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.to_series.html

# pyspark.pandas.Index.to_series#

Index.to_series(_name =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.to_series)#
    

Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.

Parameters
    

**name** string, optional
    

name of resulting Series. If None, defaults to name of original index

Returns
    

**Series** dtype will be based on the type of the Index values.
    

Examples
    
    
    >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
    ...                   columns=['dogs', 'cats'],
    ...                   index=list('abcd'))
    >>> df['dogs'].index.to_series()
    a    a
    b    b
    c    c
    d    d
    dtype: object
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.to_series.rst.txt)


---

## 🔹 057. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.to_frame.html

# pyspark.pandas.Index.to_frame#

Index.to_frame(_index =True_, _name =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.to_frame)#
    

Create a DataFrame with a column containing the Index.

Parameters
    

**index** boolean, default True
    

Set the index of the returned DataFrame as the original Index.

**name** object, default None
    

The passed name should substitute for the index name (if it has one).

Returns
    

DataFrame
    

DataFrame containing the original Index data.

See also

[`Index.to_series`](pyspark.pandas.Index.to_series.html#pyspark.pandas.Index.to_series "pyspark.pandas.Index.to_series")
    

Convert an Index to a Series.

[`Series.to_frame`](pyspark.pandas.Series.to_frame.html#pyspark.pandas.Series.to_frame "pyspark.pandas.Series.to_frame")
    

Convert Series to DataFrame.

Examples
    
    
    >>> idx = ps.Index(['Ant', 'Bear', 'Cow'], name='animal')
    >>> idx.to_frame()  
           animal
    animal
    Ant       Ant
    Bear     Bear
    Cow       Cow
    

By default, the original Index is reused. To enforce a new Index:
    
    
    >>> idx.to_frame(index=False)
      animal
    0    Ant
    1   Bear
    2    Cow
    

To override the name of the resulting column, specify name:
    
    
    >>> idx.to_frame(name='zoo')  
             zoo
    animal
    Ant      Ant
    Bear    Bear
    Cow      Cow
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.to_frame.rst.txt)


---

## 🔹 058. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.view.html

# pyspark.pandas.Index.view#

Index.view()[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.view)#
    

this is defined as a copy with the same identity

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.view.rst.txt)


---

## 🔹 059. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.to_numpy.html

# pyspark.pandas.Index.to_numpy#

Index.to_numpy(_dtype =None_, _copy =False_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.to_numpy)#
    

A NumPy ndarray representing the values in this Index or MultiIndex.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driverâs memory.

Parameters
    

**dtype** str or numpy.dtype, optional
    

The dtype to pass to `numpy.asarray()`

**copy** bool, default False
    

Whether to ensure that the returned value is not a view on another array. Note that `copy=False` does not _ensure_ that `to_numpy()` is no-copy. Rather, `copy=True` ensures that a copy is made, even if not strictly necessary.

Returns
    

numpy.ndarray
    

Examples
    
    
    >>> ps.Series([1, 2, 3, 4]).index.to_numpy()
    array([0, 1, 2, 3])
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index.to_numpy()
    array([(1, 4), (2, 5), (3, 6)], dtype=object)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.to_numpy.rst.txt)


---

## 🔹 060. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.spark.column.html

# pyspark.pandas.Index.spark.column#

spark.column#
    

Spark Column object representing the Series/Index.

Note

This Spark Column object is strictly stick to its base DataFrame the Series/Index was derived from.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.spark.column.rst.txt)


---

## 🔹 061. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.spark.transform.html

# pyspark.pandas.Index.spark.transform#

spark.transform(_func_)#
    

Applies a function that takes and returns a Spark column. It allows natively applying a Spark function and column APIs with the Spark column internally used in Series or Index. The output length of the Spark column should be the same as inputâs.

Note

It requires to have the same input and output length; therefore, the aggregate Spark functions such as count does not work.

Parameters
    

**func** function
    

Function to use for transforming the data by using Spark columns.

Returns
    

Series or Index
    
Raises
    

**ValueError** If the output from the function is not a Spark column.
    

Examples
    
    
    >>> from pyspark.sql.functions import log
    >>> df = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, columns=["a", "b"])
    >>> df
       a  b
    0  1  4
    1  2  5
    2  3  6
    
    
    
    >>> df.a.spark.transform(lambda c: log(c))
    0    0.000000
    1    0.693147
    2    1.098612
    Name: a, dtype: float64
    
    
    
    >>> df.index.spark.transform(lambda c: c + 10)
    Index([10, 11, 12], dtype='int64')
    
    
    
    >>> df.a.spark.transform(lambda c: c + df.b.spark.column)
    0    5
    1    7
    2    9
    Name: a, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.spark.transform.rst.txt)


---

## 🔹 062. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.sort_values.html

# pyspark.pandas.Index.sort_values#

Index.sort_values(_return_indexer =False_, _ascending =True_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.sort_values)#
    

Return a sorted copy of the index, and optionally return the indices that sorted the index itself.

Note

This method is not supported for pandas when index has NaN value. pandas raises unexpected TypeError, but we support treating NaN as the smallest value. This method returns indexer as a pandas-on-Spark index while pandas returns it as a list. Thatâs because indexer in pandas-on-Spark may not fit in memory.

Parameters
    

**return_indexer** bool, default False
    

Should the indices that would sort the index be returned.

**ascending** bool, default True
    

Should the index values be sorted in an ascending order.

Returns
    

**sorted_index** ps.Index or ps.MultiIndex
    

Sorted copy of the index.

**indexer** ps.Index
    

The indices that the index itself was sorted by.

See also

[`Series.sort_values`](pyspark.pandas.Series.sort_values.html#pyspark.pandas.Series.sort_values "pyspark.pandas.Series.sort_values")
    

Sort values of a Series.

[`DataFrame.sort_values`](pyspark.pandas.DataFrame.sort_values.html#pyspark.pandas.DataFrame.sort_values "pyspark.pandas.DataFrame.sort_values")
    

Sort values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([10, 100, 1, 1000])
    >>> idx
    Index([10, 100, 1, 1000], dtype='int64')
    

Sort values in ascending order (default behavior).
    
    
    >>> idx.sort_values()
    Index([1, 10, 100, 1000], dtype='int64')
    

Sort values in descending order.
    
    
    >>> idx.sort_values(ascending=False)
    Index([1000, 100, 10, 1], dtype='int64')
    

Sort values in descending order, and also get the indices idx was sorted by.
    
    
    >>> idx.sort_values(ascending=False, return_indexer=True)
    (Index([1000, 100, 10, 1], dtype='int64'), Index([3, 1, 0, 2], dtype='int64'))
    

Support for MultiIndex.
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('c', 'y', 2), ('b', 'z', 3)])
    >>> psidx  
    MultiIndex([('a', 'x', 1),
                ('c', 'y', 2),
                ('b', 'z', 3)],
               )
    
    
    
    >>> psidx.sort_values()  
    MultiIndex([('a', 'x', 1),
                ('b', 'z', 3),
                ('c', 'y', 2)],
               )
    
    
    
    >>> psidx.sort_values(ascending=False)  
    MultiIndex([('c', 'y', 2),
                ('b', 'z', 3),
                ('a', 'x', 1)],
               )
    
    
    
    >>> psidx.sort_values(ascending=False, return_indexer=True)
    (MultiIndex([('c', 'y', 2),
                ('b', 'z', 3),
                ('a', 'x', 1)],
               ), Index([1, 2, 0], dtype='int64'))
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.sort_values.rst.txt)


---

## 🔹 063. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.shift.html

# pyspark.pandas.Index.shift#

Index.shift(_periods =1_, _fill_value =None_)#
    

Shift Series/Index by desired number of periods.

Note

the current implementation of shift uses Sparkâs Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters
    

**periods** int
    

Number of periods to shift. Can be positive or negative.

**fill_value** object, optional
    

The scalar value to use for newly introduced missing values. The default depends on the dtype of self. For numeric data, np.nan is used.

Returns
    

Copy of input Series/Index, shifted.
    

Examples
    
    
    >>> df = ps.DataFrame({'Col1': [10, 20, 15, 30, 45],
    ...                    'Col2': [13, 23, 18, 33, 48],
    ...                    'Col3': [17, 27, 22, 37, 52]},
    ...                   columns=['Col1', 'Col2', 'Col3'])
    
    
    
    >>> df.Col1.shift(periods=3)
    0     NaN
    1     NaN
    2     NaN
    3    10.0
    4    20.0
    Name: Col1, dtype: float64
    
    
    
    >>> df.Col2.shift(periods=3, fill_value=0)
    0     0
    1     0
    2     0
    3    13
    4    23
    Name: Col2, dtype: int64
    
    
    
    >>> df.index.shift(periods=3, fill_value=0)
    Index([0, 0, 0, 0, 1], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.shift.rst.txt)


---

## 🔹 064. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.append.html

# pyspark.pandas.Index.append#

Index.append(_other_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.append)#
    

Append a collection of Index options together.

Parameters
    

**other** Index
    
Returns
    

**appended** Index
    

Examples
    
    
    >>> psidx = ps.Index([10, 5, 0, 5, 10, 5, 0, 10])
    >>> psidx
    Index([10, 5, 0, 5, 10, 5, 0, 10], dtype='int64')
    
    
    
    >>> psidx.append(psidx)
    Index([10, 5, 0, 5, 10, 5, 0, 10, 10, 5, 0, 5, 10, 5, 0, 10], dtype='int64')
    

Support for MiltiIndex
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
    >>> psidx  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               )
    
    
    
    >>> psidx.append(psidx)  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('a', 'x'),
                ('b', 'y')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.append.rst.txt)


---

## 🔹 065. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.intersection.html

# pyspark.pandas.Index.intersection#

Index.intersection(_other_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.intersection)#
    

Form the intersection of two Index objects.

This returns a new Index with elements common to the index and other.

Parameters
    

**other** Index or array-like
    
Returns
    

**intersection** Index
    

Examples
    
    
    >>> idx1 = ps.Index([1, 2, 3, 4])
    >>> idx2 = ps.Index([3, 4, 5, 6])
    >>> idx1.intersection(idx2).sort_values()
    Index([3, 4], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.intersection.rst.txt)


---

## 🔹 066. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.union.html

# pyspark.pandas.Index.union#

Index.union(_other_ , _sort =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.union)#
    

Form the union of two Index objects.

Parameters
    

**other** Index or array-like
    
**sort** bool or None, default None
    

Whether to sort the resulting Index.

Returns
    

**union** Index
    

Examples

Index
    
    
    >>> idx1 = ps.Index([1, 2, 3, 4])
    >>> idx2 = ps.Index([3, 4, 5, 6])
    >>> idx1.union(idx2).sort_values()
    Index([1, 2, 3, 4, 5, 6], dtype='int64')
    

MultiIndex
    
    
    >>> midx1 = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c"), ("x", "d")])
    >>> midx2 = ps.MultiIndex.from_tuples([("x", "c"), ("x", "d"), ("x", "e"), ("x", "f")])
    >>> midx1.union(midx2).sort_values()  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('x', 'c'),
                ('x', 'd'),
                ('x', 'e'),
                ('x', 'f')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.union.rst.txt)


---

## 🔹 067. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.difference.html

# pyspark.pandas.Index.difference#

Index.difference(_other_ , _sort =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.difference)#
    

Return a new Index with elements from the index that are not in other.

This is the set difference of two Index objects.

Parameters
    

**other** Index or array-like
    
**sort** True or None, default None
    

Whether to sort the resulting index. * True : Attempt to sort the result. * None : Do not sort the result.

Returns
    

**difference** Index
    

Examples
    
    
    >>> idx1 = ps.Index([2, 1, 3, 4])
    >>> idx2 = ps.Index([3, 4, 5, 6])
    >>> idx1.difference(idx2, sort=True)
    Index([1, 2], dtype='int64')
    

MultiIndex
    
    
    >>> midx1 = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)])
    >>> midx2 = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'z', 2), ('k', 'z', 3)])
    >>> midx1.difference(midx2)  
    MultiIndex([('b', 'y', 2),
                ('c', 'z', 3)],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.difference.rst.txt)


---

## 🔹 068. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.symmetric_difference.html

# pyspark.pandas.Index.symmetric_difference#

Index.symmetric_difference(_other_ , _result_name =None_, _sort =None_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.symmetric_difference)#
    

Compute the symmetric difference of two Index objects.

Parameters
    

**other** Index or array-like
    
**result_name** str
    
**sort** True or None, default None
    

Whether to sort the resulting index. * True : Attempt to sort the result. * None : Do not sort the result.

Returns
    

**symmetric_difference** Index
    

Notes

`symmetric_difference` contains elements that appear in either `idx1` or `idx2` but not both. Equivalent to the Index created by `idx1.difference(idx2) | idx2.difference(idx1)` with duplicates dropped.

Examples
    
    
    >>> s1 = ps.Series([1, 2, 3, 4], index=[1, 2, 3, 4])
    >>> s2 = ps.Series([1, 2, 3, 4], index=[2, 3, 4, 5])
    
    
    
    >>> s1.index.symmetric_difference(s2.index)
    Index([1, 5], dtype='int64')
    

You can set name of result Index.
    
    
    >>> s1.index.symmetric_difference(s2.index, result_name='pandas-on-Spark')
    Index([1, 5], dtype='int64', name='pandas-on-Spark')
    

You can set sort to True, if you want to sort the resulting index.
    
    
    >>> s1.index.symmetric_difference(s2.index, sort=True)
    Index([1, 5], dtype='int64')
    

You can also use the `^` operator:
    
    
    >>> (s1.index ^ s2.index)
    Index([1, 5], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.symmetric_difference.rst.txt)


---

## 🔹 069. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.asof.html

# pyspark.pandas.Index.asof#

Index.asof(_label_)[[source]](../../../_modules/pyspark/pandas/indexes/base.html#Index.asof)#
    

Return the label from the index, or, if not present, the previous one.

Assuming that the index is sorted, return the passed index label if it is in the index, or return the previous index label if the passed one is not in the index.

Note

This API is dependent on [`Index.is_monotonic_increasing()`](pyspark.pandas.Index.is_monotonic_increasing.html#pyspark.pandas.Index.is_monotonic_increasing "pyspark.pandas.Index.is_monotonic_increasing") which can be expensive.

Parameters
    

**label** object
    

The label up to which the method returns the latest index label.

Returns
    

object
    

The passed label if it is in the index. The previous label if the passed label is not in the sorted index or NaN if there is no such label.

Examples

Index.asof returns the latest index label up to the passed label.
    
    
    >>> idx = ps.Index(['2013-12-31', '2014-01-02', '2014-01-03'])
    >>> idx.asof('2014-01-01')
    '2013-12-31'
    

If the label is in the index, the method returns the passed label.
    
    
    >>> idx.asof('2014-01-02')
    '2014-01-02'
    

If all of the labels in the index are later than the passed label, NaN is returned.
    
    
    >>> idx.asof('1999-01-02')
    nan
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.asof.rst.txt)


---

## 🔹 070. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.Index.isin.html

# pyspark.pandas.Index.isin#

Index.isin(_values_)#
    

Check whether values are contained in Series or Index.

Return a boolean Series or Index showing whether each element in the Series matches an element in the passed sequence of values exactly.

Parameters
    

**values** set or list-like
    

The sequence of values to test.

Returns
    

**isin** Series (bool dtype) or Index (bool dtype)
    

Examples
    
    
    >>> s = ps.Series(['lama', 'cow', 'lama', 'beetle', 'lama',
    ...                'hippo'], name='animal')
    >>> s.isin(['cow', 'lama'])
    0     True
    1     True
    2     True
    3    False
    4     True
    5    False
    Name: animal, dtype: bool
    

Passing a single string as `s.isin('lama')` will raise an error. Use a list of one element instead:
    
    
    >>> s.isin(['lama'])
    0     True
    1    False
    2     True
    3    False
    4     True
    5    False
    Name: animal, dtype: bool
    
    
    
    >>> s.rename("a").to_frame().set_index("a").index.isin(['lama'])  
    Index([True, False, True, False, True, False], dtype='bool', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Index.isin.rst.txt)


---

## 🔹 071. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.html

# pyspark.pandas.CategoricalIndex#

_class _pyspark.pandas.CategoricalIndex(_data =None_, _categories =None_, _ordered =None_, _dtype =None_, _copy =False_, _name =None_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex)#
    

Index based on an underlying Categorical.

CategoricalIndex can only take on a limited, and usually fixed, number of possible values (categories). Also, it might have an order, but numerical operations (additions, divisions, â¦) are not possible.

Parameters
    

**data** array-like (1-dimensional)
    

The values of the categorical. If categories are given, values not in categories will be replaced with NaN.

**categories** index-like, optional
    

The categories for the categorical. Items need to be unique. If the categories are not given here (and also not in dtype), they will be inferred from the data.

**ordered** bool, optional
    

Whether or not this categorical is treated as an ordered categorical. If not given here or in dtype, the resulting categorical will be unordered.

**dtype** CategoricalDtype or âcategoryâ, optional
    

If `CategoricalDtype`, cannot be used together with categories or ordered.

**copy** bool, default False
    

Make a copy of input ndarray.

**name** object, optional
    

Name to be stored in the index.

See also

[`Index`](pyspark.pandas.Index.html#pyspark.pandas.Index "pyspark.pandas.Index")
    

The base pandas-on-Spark Index type.

Examples
    
    
    >>> ps.CategoricalIndex(["a", "b", "c", "a", "b", "c"])  
    CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    

`CategoricalIndex` can also be instantiated from a `Categorical`:
    
    
    >>> c = pd.Categorical(["a", "b", "c", "a", "b", "c"])
    >>> ps.CategoricalIndex(c)  
    CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    

Ordered `CategoricalIndex` can have a min and max value.
    
    
    >>> ci = ps.CategoricalIndex(
    ...     ["a", "b", "c", "a", "b", "c"], ordered=True, categories=["c", "b", "a"]
    ... )
    >>> ci  
    CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c'],
                     categories=['c', 'b', 'a'], ordered=True, dtype='category')
    

From a Series:
    
    
    >>> s = ps.Series(["a", "b", "c", "a", "b", "c"], index=[10, 20, 30, 40, 50, 60])
    >>> ps.CategoricalIndex(s)  
    CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    

From an Index:
    
    
    >>> idx = ps.Index(["a", "b", "c", "a", "b", "c"])
    >>> ps.CategoricalIndex(idx)  
    CategoricalIndex(['a', 'b', 'c', 'a', 'b', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    

Methods

[`add_categories`](pyspark.pandas.CategoricalIndex.add_categories.html#pyspark.pandas.CategoricalIndex.add_categories "pyspark.pandas.CategoricalIndex.add_categories")(new_categories) | Add new categories.  
---|---  
`all`(*args,Â **kwargs) | Return whether all elements are True.  
`any`([axis]) | Return whether any element is True.  
`append`(other) | Append a collection of Index options together.  
`argmax`() | Return a maximum argument indexer.  
`argmin`() | Return a minimum argument indexer.  
[`as_ordered`](pyspark.pandas.CategoricalIndex.as_ordered.html#pyspark.pandas.CategoricalIndex.as_ordered "pyspark.pandas.CategoricalIndex.as_ordered")() | Set the Categorical to be ordered.  
[`as_unordered`](pyspark.pandas.CategoricalIndex.as_unordered.html#pyspark.pandas.CategoricalIndex.as_unordered "pyspark.pandas.CategoricalIndex.as_unordered")() | Set the Categorical to be unordered.  
`asof`(label) | Return the label from the index, or, if not present, the previous one.  
`astype`(dtype) | Cast a pandas-on-Spark object to a specified dtype `dtype`.  
`copy`([name,Â deep]) | Make a copy of this object.  
`delete`(loc) | Make new Index with passed location(-s) deleted.  
`difference`(other[,Â sort]) | Return a new Index with elements from the index that are not in other.  
`drop`(labels) | Make new Index with passed list of labels deleted.  
`drop_duplicates`([keep]) | Return Index with duplicate values removed.  
`droplevel`(level) | Return index with requested level(s) removed.  
`dropna`([how]) | Return Index or MultiIndex without NA/NaN values  
[`equals`](pyspark.pandas.CategoricalIndex.equals.html#pyspark.pandas.CategoricalIndex.equals "pyspark.pandas.CategoricalIndex.equals")(other) | Determine if two Index objects contain the same elements.  
`factorize`([sort,Â use_na_sentinel]) | Encode the object as an enumerated type or categorical variable.  
`fillna`(value) | Fill NA/NaN values with the specified value.  
`get_level_values`(level) | Return Index if a valid level is given.  
`holds_integer`() | Whether the type is an integer type.  
`identical`(other) | Similar to equals, but check that other comparable attributes are also equal.  
`insert`(loc,Â item) | Make new Index inserting new item at location.  
`intersection`(other) | Form the intersection of two Index objects.  
`is_boolean`() | Return if the current index type is a boolean type.  
`is_categorical`() | Return if the current index type is a categorical type.  
`is_floating`() | Return if the current index type is a floating type.  
`is_integer`() | Return if the current index type is an integer type.  
`is_interval`() | Return if the current index type is an interval type.  
`is_numeric`() | Return if the current index type is a numeric type.  
`is_object`() | Return if the current index type is an object type.  
`isin`(values) | Check whether values are contained in Series or Index.  
`isna`() | Detect existing (non-missing) values.  
`isnull`() | Detect existing (non-missing) values.  
`item`() | Return the first element of the underlying data as a python scalar.  
[`map`](pyspark.pandas.CategoricalIndex.map.html#pyspark.pandas.CategoricalIndex.map "pyspark.pandas.CategoricalIndex.map")(mapper) | Map values using input correspondence (a dict, Series, or function).  
[`max`](pyspark.pandas.CategoricalIndex.max.html#pyspark.pandas.CategoricalIndex.max "pyspark.pandas.CategoricalIndex.max")() | Return the maximum value of the Index.  
[`min`](pyspark.pandas.CategoricalIndex.min.html#pyspark.pandas.CategoricalIndex.min "pyspark.pandas.CategoricalIndex.min")() | Return the minimum value of the Index.  
`notna`() | Detect existing (non-missing) values.  
`notnull`() | Detect existing (non-missing) values.  
`nunique`([dropna,Â approx,Â rsd]) | Return number of unique elements in the object.  
[`remove_categories`](pyspark.pandas.CategoricalIndex.remove_categories.html#pyspark.pandas.CategoricalIndex.remove_categories "pyspark.pandas.CategoricalIndex.remove_categories")(removals) | Remove the specified categories.  
[`remove_unused_categories`](pyspark.pandas.CategoricalIndex.remove_unused_categories.html#pyspark.pandas.CategoricalIndex.remove_unused_categories "pyspark.pandas.CategoricalIndex.remove_unused_categories")() | Remove categories which are not used.  
`rename`(name[,Â inplace]) | Alter Index or MultiIndex name.  
[`rename_categories`](pyspark.pandas.CategoricalIndex.rename_categories.html#pyspark.pandas.CategoricalIndex.rename_categories "pyspark.pandas.CategoricalIndex.rename_categories")(new_categories) | Rename categories.  
[`reorder_categories`](pyspark.pandas.CategoricalIndex.reorder_categories.html#pyspark.pandas.CategoricalIndex.reorder_categories "pyspark.pandas.CategoricalIndex.reorder_categories")(new_categories[,Â ordered]) | Reorder categories as specified in new_categories.  
`repeat`(repeats) | Repeat elements of a Index/MultiIndex.  
[`set_categories`](pyspark.pandas.CategoricalIndex.set_categories.html#pyspark.pandas.CategoricalIndex.set_categories "pyspark.pandas.CategoricalIndex.set_categories")(new_categories[,Â ordered,Â rename]) | Set the categories to the specified new_categories.  
`set_names`(names[,Â level,Â inplace]) | Set Index or MultiIndex name.  
`shift`([periods,Â fill_value]) | Shift Series/Index by desired number of periods.  
`sort`(*args,Â **kwargs) | Use sort_values instead.  
`sort_values`([return_indexer,Â ascending]) | Return a sorted copy of the index, and optionally return the indices that sorted the index itself.  
`symmetric_difference`(other[,Â result_name,Â sort]) | Compute the symmetric difference of two Index objects.  
`take`(indices) | Return the elements in the given _positional_ indices along an axis.  
`to_frame`([index,Â name]) | Create a DataFrame with a column containing the Index.  
`to_list`() | Return a list of the values.  
`to_numpy`([dtype,Â copy]) | A NumPy ndarray representing the values in this Index or MultiIndex.  
`to_pandas`() | Return a pandas Index.  
`to_series`([name]) | Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.  
[`tolist`](pyspark.pandas.CategoricalIndex.tolist.html#pyspark.pandas.CategoricalIndex.tolist "pyspark.pandas.CategoricalIndex.tolist")() | Return a list of the values.  
`transpose`() | Return the transpose, For index, It will be index itself.  
`union`(other[,Â sort]) | Form the union of two Index objects.  
`unique`([level]) | Return unique values in the index.  
`value_counts`([normalize,Â sort,Â ascending,Â ...]) | Return a Series containing counts of unique values.  
`view`() | this is defined as a copy with the same identity  
  
Attributes

`T` | Return the transpose, For index, It will be index itself.  
---|---  
[`categories`](pyspark.pandas.CategoricalIndex.categories.html#pyspark.pandas.CategoricalIndex.categories "pyspark.pandas.CategoricalIndex.categories") | The categories of this categorical.  
[`codes`](pyspark.pandas.CategoricalIndex.codes.html#pyspark.pandas.CategoricalIndex.codes "pyspark.pandas.CategoricalIndex.codes") | The category codes of this categorical.  
`dtype` | Return the dtype object of the underlying data.  
`empty` | Returns true if the current object is empty.  
`has_duplicates` | If index has duplicates, return True, otherwise False.  
`hasnans` | Return True if it has any missing values.  
`inferred_type` | Return a string of the type inferred from the values.  
`is_monotonic_decreasing` | Return boolean if values in the object are monotonically decreasing.  
`is_monotonic_increasing` | Return boolean if values in the object are monotonically increasing.  
`is_unique` | Return if the index has unique values.  
`name` | Return name of the Index.  
`names` | Return names of the Index.  
`ndim` | Return an int representing the number of array dimensions.  
`nlevels` | Number of levels in Index & MultiIndex.  
[`ordered`](pyspark.pandas.CategoricalIndex.ordered.html#pyspark.pandas.CategoricalIndex.ordered "pyspark.pandas.CategoricalIndex.ordered") | Whether the categories have an ordered relationship.  
`shape` | Return a tuple of the shape of the underlying data.  
`size` | Return an int representing the number of elements in this object.  
`values` | Return an array representing the data in the Index.  
  
[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.rst.txt)


---

## 🔹 072. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.codes.html

# pyspark.pandas.CategoricalIndex.codes#

_property _CategoricalIndex.codes#
    

The category codes of this categorical.

Codes are an Index of integers which are the positions of the actual values in the categories Index.

There is no setter, use the other categorical methods and the normal item setter to change values in the categorical.

Returns
    

Index
    

A non-writable view of the codes Index.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.codes
    Index([0, 1, 1, 2, 2, 2], dtype='int8')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.codes.rst.txt)


---

## 🔹 073. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.categories.html

# pyspark.pandas.CategoricalIndex.categories#

_property _CategoricalIndex.categories#
    

The categories of this categorical.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.categories
    Index(['a', 'b', 'c'], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.categories.rst.txt)


---

## 🔹 074. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.ordered.html

# pyspark.pandas.CategoricalIndex.ordered#

_property _CategoricalIndex.ordered#
    

Whether the categories have an ordered relationship.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.ordered
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.ordered.rst.txt)


---

## 🔹 075. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.rename_categories.html

# pyspark.pandas.CategoricalIndex.rename_categories#

CategoricalIndex.rename_categories(_new_categories_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.rename_categories)#
    

Rename categories.

Parameters
    

**new_categories** list-like, dict-like or callable
    

New categories which will replace old categories.

  * list-like: all items must be unique and the number of items in the new categories must match the existing number of categories.

  * dict-like: specifies a mapping from old categories to new. Categories not contained in the mapping are passed through and extra categories in the mapping are ignored.

  * callable : a callable that is called on all items in the old categories and whose return values comprise the new categories.



Returns
    

**cat** CategoricalIndex
    

Categorical with removed categories or None

Raises
    

ValueError
    

If new categories are list-like and do not have the same number of items than the current categories or do not validate as categories

See also

[`reorder_categories`](pyspark.pandas.CategoricalIndex.reorder_categories.html#pyspark.pandas.CategoricalIndex.reorder_categories "pyspark.pandas.CategoricalIndex.reorder_categories")
    

Reorder categories.

[`add_categories`](pyspark.pandas.CategoricalIndex.add_categories.html#pyspark.pandas.CategoricalIndex.add_categories "pyspark.pandas.CategoricalIndex.add_categories")
    

Add new categories.

[`remove_categories`](pyspark.pandas.CategoricalIndex.remove_categories.html#pyspark.pandas.CategoricalIndex.remove_categories "pyspark.pandas.CategoricalIndex.remove_categories")
    

Remove the specified categories.

[`remove_unused_categories`](pyspark.pandas.CategoricalIndex.remove_unused_categories.html#pyspark.pandas.CategoricalIndex.remove_unused_categories "pyspark.pandas.CategoricalIndex.remove_unused_categories")
    

Remove categories which are not used.

[`set_categories`](pyspark.pandas.CategoricalIndex.set_categories.html#pyspark.pandas.CategoricalIndex.set_categories "pyspark.pandas.CategoricalIndex.set_categories")
    

Set the categories to the specified ones.

Examples
    
    
    >>> idx = ps.CategoricalIndex(["a", "a", "b"])
    >>> idx.rename_categories([0, 1])
    CategoricalIndex([0, 0, 1], categories=[0, 1], ordered=False, dtype='category')
    

For dict-like `new_categories`, extra keys are ignored and categories not in the dictionary are passed through
    
    
    >>> idx.rename_categories({'a': 'A', 'c': 'C'})
    CategoricalIndex(['A', 'A', 'b'], categories=['A', 'b'], ordered=False, dtype='category')
    

You may also provide a callable to create the new categories
    
    
    >>> idx.rename_categories(lambda x: x.upper())
    CategoricalIndex(['A', 'A', 'B'], categories=['A', 'B'], ordered=False, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.rename_categories.rst.txt)


---

## 🔹 076. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.reorder_categories.html

# pyspark.pandas.CategoricalIndex.reorder_categories#

CategoricalIndex.reorder_categories(_new_categories_ , _ordered =None_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.reorder_categories)#
    

Reorder categories as specified in new_categories.

new_categories needs to include all old categories and no new category items.

Parameters
    

**new_categories** Index-like
    

The categories in new order.

**ordered** bool, optional
    

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

Returns
    

**cat** CategoricalIndex
    

Categorical with removed categories

Raises
    

ValueError
    

If the new categories do not contain all old category items or any new ones

See also

[`rename_categories`](pyspark.pandas.CategoricalIndex.rename_categories.html#pyspark.pandas.CategoricalIndex.rename_categories "pyspark.pandas.CategoricalIndex.rename_categories")
    

Rename categories.

[`add_categories`](pyspark.pandas.CategoricalIndex.add_categories.html#pyspark.pandas.CategoricalIndex.add_categories "pyspark.pandas.CategoricalIndex.add_categories")
    

Add new categories.

[`remove_categories`](pyspark.pandas.CategoricalIndex.remove_categories.html#pyspark.pandas.CategoricalIndex.remove_categories "pyspark.pandas.CategoricalIndex.remove_categories")
    

Remove the specified categories.

[`remove_unused_categories`](pyspark.pandas.CategoricalIndex.remove_unused_categories.html#pyspark.pandas.CategoricalIndex.remove_unused_categories "pyspark.pandas.CategoricalIndex.remove_unused_categories")
    

Remove categories which are not used.

[`set_categories`](pyspark.pandas.CategoricalIndex.set_categories.html#pyspark.pandas.CategoricalIndex.set_categories "pyspark.pandas.CategoricalIndex.set_categories")
    

Set the categories to the specified ones.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.reorder_categories(['c', 'b', 'a'])  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['c', 'b', 'a'], ordered=False, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.reorder_categories.rst.txt)


---

## 🔹 077. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.add_categories.html

# pyspark.pandas.CategoricalIndex.add_categories#

CategoricalIndex.add_categories(_new_categories_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.add_categories)#
    

Add new categories.

new_categories will be included at the last/highest place in the categories and will be unused directly after this call.

Parameters
    

**new_categories** category or list-like of category
    

The new categories to be included.

Returns
    

CategoricalIndex
    

Categorical with new categories added

Raises
    

ValueError
    

If the new categories include old categories or do not validate as categories

See also

[`rename_categories`](pyspark.pandas.CategoricalIndex.rename_categories.html#pyspark.pandas.CategoricalIndex.rename_categories "pyspark.pandas.CategoricalIndex.rename_categories")
    

Rename categories.

[`reorder_categories`](pyspark.pandas.CategoricalIndex.reorder_categories.html#pyspark.pandas.CategoricalIndex.reorder_categories "pyspark.pandas.CategoricalIndex.reorder_categories")
    

Reorder categories.

[`remove_categories`](pyspark.pandas.CategoricalIndex.remove_categories.html#pyspark.pandas.CategoricalIndex.remove_categories "pyspark.pandas.CategoricalIndex.remove_categories")
    

Remove the specified categories.

[`remove_unused_categories`](pyspark.pandas.CategoricalIndex.remove_unused_categories.html#pyspark.pandas.CategoricalIndex.remove_unused_categories "pyspark.pandas.CategoricalIndex.remove_unused_categories")
    

Remove categories which are not used.

[`set_categories`](pyspark.pandas.CategoricalIndex.set_categories.html#pyspark.pandas.CategoricalIndex.set_categories "pyspark.pandas.CategoricalIndex.set_categories")
    

Set the categories to the specified ones.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.add_categories('x')  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c', 'x'], ordered=False, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.add_categories.rst.txt)


---

## 🔹 078. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.remove_categories.html

# pyspark.pandas.CategoricalIndex.remove_categories#

CategoricalIndex.remove_categories(_removals_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.remove_categories)#
    

Remove the specified categories.

removals must be included in the old categories. Values which were in the removed categories will be set to NaN

Parameters
    

**removals** category or list of categories
    

The categories which should be removed.

Returns
    

CategoricalIndex
    

Categorical with removed categories

Raises
    

ValueError
    

If the removals are not contained in the categories

See also

[`rename_categories`](pyspark.pandas.CategoricalIndex.rename_categories.html#pyspark.pandas.CategoricalIndex.rename_categories "pyspark.pandas.CategoricalIndex.rename_categories")
    

Rename categories.

[`reorder_categories`](pyspark.pandas.CategoricalIndex.reorder_categories.html#pyspark.pandas.CategoricalIndex.reorder_categories "pyspark.pandas.CategoricalIndex.reorder_categories")
    

Reorder categories.

[`add_categories`](pyspark.pandas.CategoricalIndex.add_categories.html#pyspark.pandas.CategoricalIndex.add_categories "pyspark.pandas.CategoricalIndex.add_categories")
    

Add new categories.

[`remove_unused_categories`](pyspark.pandas.CategoricalIndex.remove_unused_categories.html#pyspark.pandas.CategoricalIndex.remove_unused_categories "pyspark.pandas.CategoricalIndex.remove_unused_categories")
    

Remove categories which are not used.

[`set_categories`](pyspark.pandas.CategoricalIndex.set_categories.html#pyspark.pandas.CategoricalIndex.set_categories "pyspark.pandas.CategoricalIndex.set_categories")
    

Set the categories to the specified ones.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.remove_categories('b')  
    CategoricalIndex(['a', nan, nan, 'c', 'c', 'c'],
                     categories=['a', 'c'], ordered=False, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.remove_categories.rst.txt)


---

## 🔹 079. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.remove_unused_categories.html

# pyspark.pandas.CategoricalIndex.remove_unused_categories#

CategoricalIndex.remove_unused_categories()[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.remove_unused_categories)#
    

Remove categories which are not used.

Returns
    

**cat** CategoricalIndex
    

Categorical with unused categories dropped

See also

[`rename_categories`](pyspark.pandas.CategoricalIndex.rename_categories.html#pyspark.pandas.CategoricalIndex.rename_categories "pyspark.pandas.CategoricalIndex.rename_categories")
    

Rename categories.

[`reorder_categories`](pyspark.pandas.CategoricalIndex.reorder_categories.html#pyspark.pandas.CategoricalIndex.reorder_categories "pyspark.pandas.CategoricalIndex.reorder_categories")
    

Reorder categories.

[`add_categories`](pyspark.pandas.CategoricalIndex.add_categories.html#pyspark.pandas.CategoricalIndex.add_categories "pyspark.pandas.CategoricalIndex.add_categories")
    

Add new categories.

[`remove_categories`](pyspark.pandas.CategoricalIndex.remove_categories.html#pyspark.pandas.CategoricalIndex.remove_categories "pyspark.pandas.CategoricalIndex.remove_categories")
    

Remove the specified categories.

[`set_categories`](pyspark.pandas.CategoricalIndex.set_categories.html#pyspark.pandas.CategoricalIndex.set_categories "pyspark.pandas.CategoricalIndex.set_categories")
    

Set the categories to the specified ones.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"), categories=['a', 'b', 'c', 'd'])
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c', 'd'], ordered=False, dtype='category')
    
    
    
    >>> idx.remove_unused_categories()  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.remove_unused_categories.rst.txt)


---

## 🔹 080. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.set_categories.html

# pyspark.pandas.CategoricalIndex.set_categories#

CategoricalIndex.set_categories(_new_categories_ , _ordered =None_, _rename =False_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.set_categories)#
    

Set the categories to the specified new_categories.

new_categories can include new categories (which will result in unused categories) or remove old categories (which results in values set to NaN). If rename==True, the categories will simply be renamed (less or more items than in old categories will result in values set to NaN or in unused categories respectively).

This method can be used to perform more than one action of adding, removing, and reordering simultaneously and is therefore faster than performing the individual steps via the more specialised methods.

On the other hand this methods does not do checks (e.g., whether the old categories are included in the new categories on a reorder), which can result in surprising changes, for example when using special string dtypes, which does not consider a S1 string equal to a single char python string.

Parameters
    

**new_categories** Index-like
    

The categories in new order.

**ordered** bool, default False
    

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

**rename** bool, default False
    

Whether or not the new_categories should be considered as a rename of the old categories or as reordered categories.

Returns
    

CategoricalIndex with reordered categories
    
Raises
    

ValueError
    

If new_categories does not validate as categories

See also

[`rename_categories`](pyspark.pandas.CategoricalIndex.rename_categories.html#pyspark.pandas.CategoricalIndex.rename_categories "pyspark.pandas.CategoricalIndex.rename_categories")
    

Rename categories.

[`reorder_categories`](pyspark.pandas.CategoricalIndex.reorder_categories.html#pyspark.pandas.CategoricalIndex.reorder_categories "pyspark.pandas.CategoricalIndex.reorder_categories")
    

Reorder categories.

[`add_categories`](pyspark.pandas.CategoricalIndex.add_categories.html#pyspark.pandas.CategoricalIndex.add_categories "pyspark.pandas.CategoricalIndex.add_categories")
    

Add new categories.

[`remove_categories`](pyspark.pandas.CategoricalIndex.remove_categories.html#pyspark.pandas.CategoricalIndex.remove_categories "pyspark.pandas.CategoricalIndex.remove_categories")
    

Remove the specified categories.

[`remove_unused_categories`](pyspark.pandas.CategoricalIndex.remove_unused_categories.html#pyspark.pandas.CategoricalIndex.remove_unused_categories "pyspark.pandas.CategoricalIndex.remove_unused_categories")
    

Remove categories which are not used.

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.set_categories(['b', 'c'])  
    CategoricalIndex([nan, 'b', 'b', 'c', 'c', 'c'],
                     categories=['b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.set_categories([1, 2, 3], rename=True)
    CategoricalIndex([1, 2, 2, 3, 3, 3], categories=[1, 2, 3], ordered=False, dtype='category')
    
    
    
    >>> idx.set_categories([1, 2, 3], rename=True, ordered=True)
    CategoricalIndex([1, 2, 2, 3, 3, 3], categories=[1, 2, 3], ordered=True, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.set_categories.rst.txt)


---

## 🔹 081. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.as_ordered.html

# pyspark.pandas.CategoricalIndex.as_ordered#

CategoricalIndex.as_ordered()[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.as_ordered)#
    

Set the Categorical to be ordered.

Returns
    

CategoricalIndex
    

Ordered Categorical

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc"))
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.as_ordered()  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=True, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.as_ordered.rst.txt)


---

## 🔹 082. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.as_unordered.html

# pyspark.pandas.CategoricalIndex.as_unordered#

CategoricalIndex.as_unordered()[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.as_unordered)#
    

Set the Categorical to be unordered.

Returns
    

CategoricalIndex
    

Unordered Categorical

Examples
    
    
    >>> idx = ps.CategoricalIndex(list("abbccc")).as_ordered()
    >>> idx  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=True, dtype='category')
    
    
    
    >>> idx.as_unordered()  
    CategoricalIndex(['a', 'b', 'b', 'c', 'c', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.as_unordered.rst.txt)


---

## 🔹 083. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.map.html

# pyspark.pandas.CategoricalIndex.map#

CategoricalIndex.map(_mapper_)[[source]](../../../_modules/pyspark/pandas/indexes/category.html#CategoricalIndex.map)#
    

Map values using input correspondence (a dict, Series, or function).

Maps the values (their categories, not the codes) of the index to new categories. If the mapping correspondence is one-to-one the result is a CategoricalIndex which has the same order property as the original, otherwise an Index is returned.

If a dict or Series is used any unmapped category is mapped to missing values. Note that if this happens an Index will be returned.

Parameters
    

**mapper** function, dict, or Series
    

Mapping correspondence.

Returns
    

CategoricalIndex or Index
    

Mapped index.

See also

[`Index.map`](pyspark.pandas.Index.map.html#pyspark.pandas.Index.map "pyspark.pandas.Index.map")
    

Apply a mapping correspondence on an Index.

[`Series.map`](pyspark.pandas.Series.map.html#pyspark.pandas.Series.map "pyspark.pandas.Series.map")
    

Apply a mapping correspondence on a Series

[`Series.apply`](pyspark.pandas.Series.apply.html#pyspark.pandas.Series.apply "pyspark.pandas.Series.apply")
    

Apply more complex functions on a Series

Examples
    
    
    >>> idx = ps.CategoricalIndex(['a', 'b', 'c'])
    >>> idx  
    CategoricalIndex(['a', 'b', 'c'],
                     categories=['a', 'b', 'c'], ordered=False, dtype='category')
    
    
    
    >>> idx.map(lambda x: x.upper())  
    CategoricalIndex(['A', 'B', 'C'],
                     categories=['A', 'B', 'C'], ordered=False, dtype='category')
    
    
    
    >>> pser = pd.Series([1, 2, 3], index=pd.CategoricalIndex(['a', 'b', 'c'], ordered=True))
    >>> idx.map(pser)  
    CategoricalIndex([1, 2, 3],
                     categories=[1, 2, 3], ordered=False, dtype='category')
    
    
    
    >>> idx.map({'a': 'first', 'b': 'second', 'c': 'third'})  
    CategoricalIndex(['first', 'second', 'third'],
                     categories=['first', 'second', 'third'], ordered=False, dtype='category')
    

If the mapping is one-to-one the ordering of the categories is preserved:
    
    
    >>> idx = ps.CategoricalIndex(['a', 'b', 'c'], ordered=True)
    >>> idx  
    CategoricalIndex(['a', 'b', 'c'],
                     categories=['a', 'b', 'c'], ordered=True, dtype='category')
    
    
    
    >>> idx.map({'a': 3, 'b': 2, 'c': 1})  
    CategoricalIndex([3, 2, 1],
                     categories=[3, 2, 1], ordered=True, dtype='category')
    

If the mapping is not one-to-one an Index is returned:
    
    
    >>> idx.map({'a': 'first', 'b': 'second', 'c': 'first'})
    Index(['first', 'second', 'first'], dtype='object')
    

If a dict is used, all unmapped categories are mapped to None and the result is an Index:
    
    
    >>> idx.map({'a': 'first', 'b': 'second'})
    Index(['first', 'second', None], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.map.rst.txt)


---

## 🔹 084. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.equals.html

# pyspark.pandas.CategoricalIndex.equals#

CategoricalIndex.equals(_other_)#
    

Determine if two Index objects contain the same elements.

Returns
    

bool
    

True if âotherâ is an Index and it has the same elements as calling index; False otherwise.

Examples
    
    
    >>> from pyspark.pandas.config import option_context
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx.name = "name"
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx.names = ("nameA", "nameB")
    

For Index
    
    
    >>> idx.equals(idx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.equals(ps.Index(['a', 'b', 'c']))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.equals(ps.Index(['b', 'b', 'a']))
    False
    >>> idx.equals(midx)
    False
    

For MultiIndex
    
    
    >>> midx.equals(midx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.equals(ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.equals(ps.MultiIndex.from_tuples([('c', 'z'), ('b', 'y'), ('a', 'x')]))
    False
    >>> midx.equals(idx)
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.equals.rst.txt)


---

## 🔹 085. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.max.html

# pyspark.pandas.CategoricalIndex.max#

CategoricalIndex.max()#
    

Return the maximum value of the Index.

Returns
    

scalar
    

Maximum value.

See also

[`Index.min`](pyspark.pandas.Index.min.html#pyspark.pandas.Index.min "pyspark.pandas.Index.min")
    

Return the minimum value in an Index.

[`Series.max`](pyspark.pandas.Series.max.html#pyspark.pandas.Series.max "pyspark.pandas.Series.max")
    

Return the maximum value in a Series.

[`DataFrame.max`](pyspark.pandas.DataFrame.max.html#pyspark.pandas.DataFrame.max "pyspark.pandas.DataFrame.max")
    

Return the maximum values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([3, 2, 1])
    >>> idx.max()
    3
    
    
    
    >>> idx = ps.Index(['c', 'b', 'a'])
    >>> idx.max()
    'c'
    

For a MultiIndex, the maximum is determined lexicographically.
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
    >>> idx.max()
    ('b', 'y', 2)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.max.rst.txt)


---

## 🔹 086. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.min.html

# pyspark.pandas.CategoricalIndex.min#

CategoricalIndex.min()#
    

Return the minimum value of the Index.

Returns
    

scalar
    

Minimum value.

See also

[`Index.max`](pyspark.pandas.Index.max.html#pyspark.pandas.Index.max "pyspark.pandas.Index.max")
    

Return the maximum value of the object.

[`Series.min`](pyspark.pandas.Series.min.html#pyspark.pandas.Series.min "pyspark.pandas.Series.min")
    

Return the minimum value in a Series.

[`DataFrame.min`](pyspark.pandas.DataFrame.min.html#pyspark.pandas.DataFrame.min "pyspark.pandas.DataFrame.min")
    

Return the minimum values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([3, 2, 1])
    >>> idx.min()
    1
    
    
    
    >>> idx = ps.Index(['c', 'b', 'a'])
    >>> idx.min()
    'a'
    

For a MultiIndex, the maximum is determined lexicographically.
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
    >>> idx.min()
    ('a', 'x', 1)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.min.rst.txt)


---

## 🔹 087. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.tolist.html

# pyspark.pandas.CategoricalIndex.tolist#

CategoricalIndex.tolist()#
    

Return a list of the values.

These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)

Note

This method should only be used if the resulting list is expected to be small, as all the data is loaded into the driverâs memory.

Examples

Index
    
    
    >>> idx = ps.Index([1, 2, 3, 4, 5])
    >>> idx.to_list()
    [1, 2, 3, 4, 5]
    

MultiIndex
    
    
    >>> tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
    >>> midx = ps.MultiIndex.from_tuples(tuples)
    >>> midx.to_list()
    [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.CategoricalIndex.tolist.rst.txt)


---

## 🔹 088. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.html

# pyspark.pandas.MultiIndex#

_class _pyspark.pandas.MultiIndex(_levels =None_, _codes =None_, _sortorder =None_, _names =None_, _dtype =None_, _copy =False_, _name =None_, _verify_integrity =True_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex)#
    

pandas-on-Spark MultiIndex that corresponds to pandas MultiIndex logically. This might hold Spark Column internally.

Parameters
    

**levels** sequence of arrays
    

The unique labels for each level.

**codes** sequence of arrays
    

Integers for each level designating which label at each location.

**sortorder** optional int
    

Level of sortedness (must be lexicographically sorted by that level).

**names** optional sequence of objects
    

Names for each of the index levels. (name is accepted for compat).

**copy** bool, default False
    

Copy the meta-data.

**verify_integrity** bool, default True
    

Check that the levels/codes are consistent and valid.

See also

[`MultiIndex.from_arrays`](pyspark.pandas.MultiIndex.from_arrays.html#pyspark.pandas.MultiIndex.from_arrays "pyspark.pandas.MultiIndex.from_arrays")
    

Convert list of arrays to MultiIndex.

[`MultiIndex.from_product`](pyspark.pandas.MultiIndex.from_product.html#pyspark.pandas.MultiIndex.from_product "pyspark.pandas.MultiIndex.from_product")
    

Create a MultiIndex from the cartesian product of iterables.

[`MultiIndex.from_tuples`](pyspark.pandas.MultiIndex.from_tuples.html#pyspark.pandas.MultiIndex.from_tuples "pyspark.pandas.MultiIndex.from_tuples")
    

Convert list of tuples to a MultiIndex.

[`MultiIndex.from_frame`](pyspark.pandas.MultiIndex.from_frame.html#pyspark.pandas.MultiIndex.from_frame "pyspark.pandas.MultiIndex.from_frame")
    

Make a MultiIndex from a DataFrame.

[`Index`](pyspark.pandas.Index.html#pyspark.pandas.Index "pyspark.pandas.Index")
    

A single-level Index.

Examples
    
    
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index  
    MultiIndex([(1, 4),
                (2, 5),
                (3, 6)],
               )
    
    
    
    >>> ps.DataFrame({'a': [1, 2, 3]}, index=[list('abc'), list('def')]).index  
    MultiIndex([('a', 'd'),
                ('b', 'e'),
                ('c', 'f')],
               )
    

Methods

`all`(*args,Â **kwargs) | Return whether all elements are True.  
---|---  
`any`(*args,Â **kwargs) | Return whether any element is True.  
[`append`](pyspark.pandas.MultiIndex.append.html#pyspark.pandas.MultiIndex.append "pyspark.pandas.MultiIndex.append")(other) | Append a collection of Index options together.  
`argmax`() | Return a maximum argument indexer.  
`argmin`() | Return a minimum argument indexer.  
`asof`(label) | Return the label from the index, or, if not present, the previous one.  
[`astype`](pyspark.pandas.MultiIndex.astype.html#pyspark.pandas.MultiIndex.astype "pyspark.pandas.MultiIndex.astype")(dtype) | Cast a pandas-on-Spark object to a specified dtype `dtype`.  
[`copy`](pyspark.pandas.MultiIndex.copy.html#pyspark.pandas.MultiIndex.copy "pyspark.pandas.MultiIndex.copy")([deep]) | Make a copy of this object.  
[`delete`](pyspark.pandas.MultiIndex.delete.html#pyspark.pandas.MultiIndex.delete "pyspark.pandas.MultiIndex.delete")(loc) | Make new Index with passed location(-s) deleted.  
[`difference`](pyspark.pandas.MultiIndex.difference.html#pyspark.pandas.MultiIndex.difference "pyspark.pandas.MultiIndex.difference")(other[,Â sort]) | Return a new Index with elements from the index that are not in other.  
[`drop`](pyspark.pandas.MultiIndex.drop.html#pyspark.pandas.MultiIndex.drop "pyspark.pandas.MultiIndex.drop")(codes[,Â level]) | Make new MultiIndex with passed list of labels deleted  
`drop_duplicates`([keep]) | Return MultiIndex with duplicate values removed.  
[`droplevel`](pyspark.pandas.MultiIndex.droplevel.html#pyspark.pandas.MultiIndex.droplevel "pyspark.pandas.MultiIndex.droplevel")(level) | Return index with requested level(s) removed.  
[`dropna`](pyspark.pandas.MultiIndex.dropna.html#pyspark.pandas.MultiIndex.dropna "pyspark.pandas.MultiIndex.dropna")([how]) | Return Index or MultiIndex without NA/NaN values  
[`equal_levels`](pyspark.pandas.MultiIndex.equal_levels.html#pyspark.pandas.MultiIndex.equal_levels "pyspark.pandas.MultiIndex.equal_levels")(other) | Return True if the levels of both MultiIndex objects are the same  
[`equals`](pyspark.pandas.MultiIndex.equals.html#pyspark.pandas.MultiIndex.equals "pyspark.pandas.MultiIndex.equals")(other) | Determine if two Index objects contain the same elements.  
`factorize`([sort,Â na_sentinel]) | Encode the object as an enumerated type or categorical variable.  
[`fillna`](pyspark.pandas.MultiIndex.fillna.html#pyspark.pandas.MultiIndex.fillna "pyspark.pandas.MultiIndex.fillna")(value) | Fill NA/NaN values with the specified value.  
[`from_arrays`](pyspark.pandas.MultiIndex.from_arrays.html#pyspark.pandas.MultiIndex.from_arrays "pyspark.pandas.MultiIndex.from_arrays")(arrays[,Â sortorder,Â names]) | Convert arrays to MultiIndex.  
[`from_frame`](pyspark.pandas.MultiIndex.from_frame.html#pyspark.pandas.MultiIndex.from_frame "pyspark.pandas.MultiIndex.from_frame")(df[,Â names]) | Make a MultiIndex from a DataFrame.  
[`from_product`](pyspark.pandas.MultiIndex.from_product.html#pyspark.pandas.MultiIndex.from_product "pyspark.pandas.MultiIndex.from_product")(iterables[,Â sortorder,Â names]) | Make a MultiIndex from the cartesian product of multiple iterables.  
[`from_tuples`](pyspark.pandas.MultiIndex.from_tuples.html#pyspark.pandas.MultiIndex.from_tuples "pyspark.pandas.MultiIndex.from_tuples")(tuples[,Â sortorder,Â names]) | Convert list of tuples to MultiIndex.  
`get_level_values`(level) | Return vector of label values for requested level, equal to the length of the index.  
`holds_integer`() | Whether the type is an integer type.  
[`identical`](pyspark.pandas.MultiIndex.identical.html#pyspark.pandas.MultiIndex.identical "pyspark.pandas.MultiIndex.identical")(other) | Similar to equals, but check that other comparable attributes are also equal.  
[`insert`](pyspark.pandas.MultiIndex.insert.html#pyspark.pandas.MultiIndex.insert "pyspark.pandas.MultiIndex.insert")(loc,Â item) | Make new MultiIndex inserting new item at location.  
[`intersection`](pyspark.pandas.MultiIndex.intersection.html#pyspark.pandas.MultiIndex.intersection "pyspark.pandas.MultiIndex.intersection")(other) | Form the intersection of two Index objects.  
`is_boolean`() | Return if the current index type is a boolean type.  
`is_categorical`() | Return if the current index type is a categorical type.  
`is_floating`() | Return if the current index type is a floating type.  
`is_integer`() | Return if the current index type is an integer type.  
`is_interval`() | Return if the current index type is an interval type.  
`is_numeric`() | Return if the current index type is a numeric type.  
`is_object`() | Return if the current index type is an object type.  
`isin`(values) | Check whether values are contained in Series or Index.  
`isna`() | Detect existing (non-missing) values.  
`isnull`() | Detect existing (non-missing) values.  
[`item`](pyspark.pandas.MultiIndex.item.html#pyspark.pandas.MultiIndex.item "pyspark.pandas.MultiIndex.item")() | Return the first element of the underlying data as a python tuple.  
`map`([mapper,Â na_action]) | Map values using input correspondence (a dict, Series, or function).  
[`max`](pyspark.pandas.MultiIndex.max.html#pyspark.pandas.MultiIndex.max "pyspark.pandas.MultiIndex.max")() | Return the maximum value of the Index.  
[`min`](pyspark.pandas.MultiIndex.min.html#pyspark.pandas.MultiIndex.min "pyspark.pandas.MultiIndex.min")() | Return the minimum value of the Index.  
`notna`() | Detect existing (non-missing) values.  
`notnull`() | Detect existing (non-missing) values.  
`nunique`([dropna,Â approx,Â rsd]) | Return number of unique elements in the object.  
[`rename`](pyspark.pandas.MultiIndex.rename.html#pyspark.pandas.MultiIndex.rename "pyspark.pandas.MultiIndex.rename")(name[,Â inplace]) | Alter Index or MultiIndex name.  
[`repeat`](pyspark.pandas.MultiIndex.repeat.html#pyspark.pandas.MultiIndex.repeat "pyspark.pandas.MultiIndex.repeat")(repeats) | Repeat elements of a Index/MultiIndex.  
`set_names`(names[,Â level,Â inplace]) | Set Index or MultiIndex name.  
`shift`([periods,Â fill_value]) | Shift Series/Index by desired number of periods.  
`sort`(*args,Â **kwargs) | Use sort_values instead.  
[`sort_values`](pyspark.pandas.MultiIndex.sort_values.html#pyspark.pandas.MultiIndex.sort_values "pyspark.pandas.MultiIndex.sort_values")([return_indexer,Â ascending]) | Return a sorted copy of the index, and optionally return the indices that sorted the index itself.  
[`swaplevel`](pyspark.pandas.MultiIndex.swaplevel.html#pyspark.pandas.MultiIndex.swaplevel "pyspark.pandas.MultiIndex.swaplevel")([i,Â j]) | Swap level i with level j.  
[`symmetric_difference`](pyspark.pandas.MultiIndex.symmetric_difference.html#pyspark.pandas.MultiIndex.symmetric_difference "pyspark.pandas.MultiIndex.symmetric_difference")(other[,Â result_name,Â sort]) | Compute the symmetric difference of two MultiIndex objects.  
[`take`](pyspark.pandas.MultiIndex.take.html#pyspark.pandas.MultiIndex.take "pyspark.pandas.MultiIndex.take")(indices) | Return the elements in the given _positional_ indices along an axis.  
[`to_frame`](pyspark.pandas.MultiIndex.to_frame.html#pyspark.pandas.MultiIndex.to_frame "pyspark.pandas.MultiIndex.to_frame")([index,Â name]) | Create a DataFrame with the levels of the MultiIndex as columns.  
[`to_list`](pyspark.pandas.MultiIndex.to_list.html#pyspark.pandas.MultiIndex.to_list "pyspark.pandas.MultiIndex.to_list")() | Return a list of the values.  
[`to_numpy`](pyspark.pandas.MultiIndex.to_numpy.html#pyspark.pandas.MultiIndex.to_numpy "pyspark.pandas.MultiIndex.to_numpy")([dtype,Â copy]) | A NumPy ndarray representing the values in this Index or MultiIndex.  
`to_pandas`() | Return a pandas MultiIndex.  
[`to_series`](pyspark.pandas.MultiIndex.to_series.html#pyspark.pandas.MultiIndex.to_series "pyspark.pandas.MultiIndex.to_series")([name]) | Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.  
`tolist`() | Return a list of the values.  
`transpose`() | Return the transpose, For index, It will be index itself.  
[`union`](pyspark.pandas.MultiIndex.union.html#pyspark.pandas.MultiIndex.union "pyspark.pandas.MultiIndex.union")(other[,Â sort]) | Form the union of two Index objects.  
[`unique`](pyspark.pandas.MultiIndex.unique.html#pyspark.pandas.MultiIndex.unique "pyspark.pandas.MultiIndex.unique")([level]) | Return unique values in the index.  
[`value_counts`](pyspark.pandas.MultiIndex.value_counts.html#pyspark.pandas.MultiIndex.value_counts "pyspark.pandas.MultiIndex.value_counts")([normalize,Â sort,Â ascending,Â ...]) | Return a Series containing counts of unique values.  
[`view`](pyspark.pandas.MultiIndex.view.html#pyspark.pandas.MultiIndex.view "pyspark.pandas.MultiIndex.view")() | this is defined as a copy with the same identity  
  
Attributes

[`T`](pyspark.pandas.MultiIndex.T.html#pyspark.pandas.MultiIndex.T "pyspark.pandas.MultiIndex.T") | Return the transpose, For index, It will be index itself.  
---|---  
`dtype` | Return the dtype object of the underlying data.  
[`dtypes`](pyspark.pandas.MultiIndex.dtypes.html#pyspark.pandas.MultiIndex.dtypes "pyspark.pandas.MultiIndex.dtypes") | Return the dtypes as a Series for the underlying MultiIndex.  
[`empty`](pyspark.pandas.MultiIndex.empty.html#pyspark.pandas.MultiIndex.empty "pyspark.pandas.MultiIndex.empty") | Returns true if the current object is empty.  
[`has_duplicates`](pyspark.pandas.MultiIndex.has_duplicates.html#pyspark.pandas.MultiIndex.has_duplicates "pyspark.pandas.MultiIndex.has_duplicates") | If index has duplicates, return True, otherwise False.  
[`hasnans`](pyspark.pandas.MultiIndex.hasnans.html#pyspark.pandas.MultiIndex.hasnans "pyspark.pandas.MultiIndex.hasnans") | Return True if it has any missing values.  
[`inferred_type`](pyspark.pandas.MultiIndex.inferred_type.html#pyspark.pandas.MultiIndex.inferred_type "pyspark.pandas.MultiIndex.inferred_type") | Return a string of the type inferred from the values.  
`is_monotonic_decreasing` | Return boolean if values in the object are monotonically decreasing.  
`is_monotonic_increasing` | Return boolean if values in the object are monotonically increasing.  
`is_unique` | Return if the index has unique values.  
[`levshape`](pyspark.pandas.MultiIndex.levshape.html#pyspark.pandas.MultiIndex.levshape "pyspark.pandas.MultiIndex.levshape") | A tuple with the length of each level.  
`name` | Return name of the Index.  
[`names`](pyspark.pandas.MultiIndex.names.html#pyspark.pandas.MultiIndex.names "pyspark.pandas.MultiIndex.names") | Return names of the Index.  
[`ndim`](pyspark.pandas.MultiIndex.ndim.html#pyspark.pandas.MultiIndex.ndim "pyspark.pandas.MultiIndex.ndim") | Return an int representing the number of array dimensions.  
[`nlevels`](pyspark.pandas.MultiIndex.nlevels.html#pyspark.pandas.MultiIndex.nlevels "pyspark.pandas.MultiIndex.nlevels") | Number of levels in Index & MultiIndex.  
[`shape`](pyspark.pandas.MultiIndex.shape.html#pyspark.pandas.MultiIndex.shape "pyspark.pandas.MultiIndex.shape") | Return a tuple of the shape of the underlying data.  
[`size`](pyspark.pandas.MultiIndex.size.html#pyspark.pandas.MultiIndex.size "pyspark.pandas.MultiIndex.size") | Return an int representing the number of elements in this object.  
[`values`](pyspark.pandas.MultiIndex.values.html#pyspark.pandas.MultiIndex.values "pyspark.pandas.MultiIndex.values") | Return an array representing the data in the Index.  
  
[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.rst.txt)


---

## 🔹 089. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_arrays.html

# pyspark.pandas.MultiIndex.from_arrays#

_static _MultiIndex.from_arrays(_arrays_ , _sortorder =None_, _names =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.from_arrays)#
    

Convert arrays to MultiIndex.

Parameters
    

**arrays: list / sequence of array-likes**
    

Each array-like gives one levelâs value for each data point. len(arrays) is the number of levels.

**sortorder: int or None**
    

Level of sortedness (must be lexicographically sorted by that level).

**names: list / sequence of str, optional**
    

Names for the levels in the index.

Returns
    

index: MultiIndex
    

Examples
    
    
    >>> arrays = [[1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
    >>> ps.MultiIndex.from_arrays(arrays, names=('number', 'color'))  
    MultiIndex([(1,  'red'),
                (1, 'blue'),
                (2,  'red'),
                (2, 'blue')],
               names=['number', 'color'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_arrays.rst.txt)


---

## 🔹 090. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_tuples.html

# pyspark.pandas.MultiIndex.from_tuples#

_static _MultiIndex.from_tuples(_tuples_ , _sortorder =None_, _names =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.from_tuples)#
    

Convert list of tuples to MultiIndex.

Parameters
    

**tuples** list / sequence of tuple-likes
    

Each tuple is the index of one row/column.

**sortorder** int or None
    

Level of sortedness (must be lexicographically sorted by that level).

**names** list / sequence of str, optional
    

Names for the levels in the index.

Returns
    

**index** MultiIndex
    

Examples
    
    
    >>> tuples = [(1, 'red'), (1, 'blue'),
    ...           (2, 'red'), (2, 'blue')]
    >>> ps.MultiIndex.from_tuples(tuples, names=('number', 'color'))  
    MultiIndex([(1,  'red'),
                (1, 'blue'),
                (2,  'red'),
                (2, 'blue')],
               names=['number', 'color'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_tuples.rst.txt)


---

## 🔹 091. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_product.html

# pyspark.pandas.MultiIndex.from_product#

_static _MultiIndex.from_product(_iterables_ , _sortorder =None_, _names =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.from_product)#
    

Make a MultiIndex from the cartesian product of multiple iterables.

Parameters
    

**iterables** list / sequence of iterables
    

Each iterable has unique labels for each level of the index.

**sortorder** int or None
    

Level of sortedness (must be lexicographically sorted by that level).

**names** list / sequence of str, optional
    

Names for the levels in the index.

Returns
    

**index** MultiIndex
    

See also

[`MultiIndex.from_arrays`](pyspark.pandas.MultiIndex.from_arrays.html#pyspark.pandas.MultiIndex.from_arrays "pyspark.pandas.MultiIndex.from_arrays")
    

Convert list of arrays to MultiIndex.

[`MultiIndex.from_tuples`](pyspark.pandas.MultiIndex.from_tuples.html#pyspark.pandas.MultiIndex.from_tuples "pyspark.pandas.MultiIndex.from_tuples")
    

Convert list of tuples to MultiIndex.

Examples
    
    
    >>> numbers = [0, 1, 2]
    >>> colors = ['green', 'purple']
    >>> ps.MultiIndex.from_product([numbers, colors],
    ...                            names=['number', 'color'])  
    MultiIndex([(0,  'green'),
                (0, 'purple'),
                (1,  'green'),
                (1, 'purple'),
                (2,  'green'),
                (2, 'purple')],
               names=['number', 'color'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_product.rst.txt)


---

## 🔹 092. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_frame.html

# pyspark.pandas.MultiIndex.from_frame#

_static _MultiIndex.from_frame(_df_ , _names =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.from_frame)#
    

Make a MultiIndex from a DataFrame.

Parameters
    

**df** DataFrame
    

DataFrame to be converted to MultiIndex.

**names** list-like, optional
    

If no names are provided, use the column names, or tuple of column names if the column is a MultiIndex. If a sequence, overwrite names with the given sequence.

Returns
    

MultiIndex
    

The MultiIndex representation of the given DataFrame.

See also

[`MultiIndex.from_arrays`](pyspark.pandas.MultiIndex.from_arrays.html#pyspark.pandas.MultiIndex.from_arrays "pyspark.pandas.MultiIndex.from_arrays")
    

Convert list of arrays to MultiIndex.

[`MultiIndex.from_tuples`](pyspark.pandas.MultiIndex.from_tuples.html#pyspark.pandas.MultiIndex.from_tuples "pyspark.pandas.MultiIndex.from_tuples")
    

Convert list of tuples to MultiIndex.

[`MultiIndex.from_product`](pyspark.pandas.MultiIndex.from_product.html#pyspark.pandas.MultiIndex.from_product "pyspark.pandas.MultiIndex.from_product")
    

Make a MultiIndex from cartesian product of iterables.

Examples
    
    
    >>> df = ps.DataFrame([['HI', 'Temp'], ['HI', 'Precip'],
    ...                    ['NJ', 'Temp'], ['NJ', 'Precip']],
    ...                   columns=['a', 'b'])
    >>> df  
          a       b
    0    HI    Temp
    1    HI  Precip
    2    NJ    Temp
    3    NJ  Precip
    
    
    
    >>> ps.MultiIndex.from_frame(df)  
    MultiIndex([('HI',   'Temp'),
                ('HI', 'Precip'),
                ('NJ',   'Temp'),
                ('NJ', 'Precip')],
               names=['a', 'b'])
    

Using explicit names, instead of the column names
    
    
    >>> ps.MultiIndex.from_frame(df, names=['state', 'observation'])  
    MultiIndex([('HI',   'Temp'),
                ('HI', 'Precip'),
                ('NJ',   'Temp'),
                ('NJ', 'Precip')],
               names=['state', 'observation'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.from_frame.rst.txt)


---

## 🔹 093. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.has_duplicates.html

# pyspark.pandas.MultiIndex.has_duplicates#

_property _MultiIndex.has_duplicates#
    

If index has duplicates, return True, otherwise False.

Examples
    
    
    >>> idx = ps.Index([1, 5, 7, 7])
    >>> idx.has_duplicates
    True
    
    
    
    >>> idx = ps.Index([1, 5, 7])
    >>> idx.has_duplicates
    False
    
    
    
    >>> idx = ps.Index(["Watermelon", "Orange", "Apple",
    ...                 "Watermelon"])
    >>> idx.has_duplicates
    True
    
    
    
    >>> idx = ps.Index(["Orange", "Apple",
    ...                 "Watermelon"])
    >>> idx.has_duplicates
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.has_duplicates.rst.txt)


---

## 🔹 094. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.hasnans.html

# pyspark.pandas.MultiIndex.hasnans#

_property _MultiIndex.hasnans#
    

Return True if it has any missing values. Otherwise, it returns False.
    
    
    >>> ps.DataFrame({}, index=list('abc')).index.hasnans
    False
    
    
    
    >>> ps.Series(['a', None]).hasnans
    True
    
    
    
    >>> ps.Series([1.0, 2.0, np.nan]).hasnans
    True
    
    
    
    >>> ps.Series([1, 2, 3]).hasnans
    False
    
    
    
    >>> (ps.Series([1.0, 2.0, np.nan]) + 1).hasnans
    True
    
    
    
    >>> ps.Series([1, 2, 3]).rename("a").to_frame().set_index("a").index.hasnans
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.hasnans.rst.txt)


---

## 🔹 095. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.inferred_type.html

# pyspark.pandas.MultiIndex.inferred_type#

_property _MultiIndex.inferred_type#
    

Return a string of the type inferred from the values.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.inferred_type.rst.txt)


---

## 🔹 096. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.shape.html

# pyspark.pandas.MultiIndex.shape#

_property _MultiIndex.shape#
    

Return a tuple of the shape of the underlying data.

Examples
    
    
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx
    Index(['a', 'b', 'c'], dtype='object')
    >>> idx.shape
    (3,)
    
    
    
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    >>> midx.shape
    (3,)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.shape.rst.txt)


---

## 🔹 097. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.names.html

# pyspark.pandas.MultiIndex.names#

_property _MultiIndex.names#
    

Return names of the Index.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.names.rst.txt)


---

## 🔹 098. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.ndim.html

# pyspark.pandas.MultiIndex.ndim#

_property _MultiIndex.ndim#
    

Return an int representing the number of array dimensions.

Return 1 for Series / Index / MultiIndex.

Examples

For Series
    
    
    >>> s = ps.Series([None, 1, 2, 3, 4], index=[4, 5, 2, 1, 8])
    >>> s.ndim
    1
    

For Index
    
    
    >>> s.index.ndim
    1
    

For MultiIndex
    
    
    >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
    ...                       ['speed', 'weight', 'length']],
    ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
    >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
    >>> s.index.ndim
    1
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.ndim.rst.txt)


---

## 🔹 099. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.empty.html

# pyspark.pandas.MultiIndex.empty#

_property _MultiIndex.empty#
    

Returns true if the current object is empty. Otherwise, it returns false.
    
    
    >>> ps.range(10).id.empty
    False
    
    
    
    >>> ps.range(0).id.empty
    True
    
    
    
    >>> ps.DataFrame({}, index=list('abc')).index.empty
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.empty.rst.txt)


---

## 🔹 100. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.T.html

# pyspark.pandas.MultiIndex.T#

_property _MultiIndex.T#
    

Return the transpose, For index, It will be index itself.

Examples
    
    
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx
    Index(['a', 'b', 'c'], dtype='object')
    
    
    
    >>> idx.transpose()
    Index(['a', 'b', 'c'], dtype='object')
    

For MultiIndex
    
    
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    
    
    
    >>> midx.transpose()  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.T.rst.txt)


---

## 🔹 101. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.size.html

# pyspark.pandas.MultiIndex.size#

_property _MultiIndex.size#
    

Return an int representing the number of elements in this object.

Examples
    
    
    >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
    ...                   columns=['dogs', 'cats'],
    ...                   index=list('abcd'))
    >>> df.index.size
    4
    
    
    
    >>> df.set_index('dogs', append=True).index.size
    4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.size.rst.txt)


---

## 🔹 102. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.nlevels.html

# pyspark.pandas.MultiIndex.nlevels#

_property _MultiIndex.nlevels#
    

Number of levels in Index & MultiIndex.

Examples
    
    
    >>> psdf = ps.DataFrame({"a": [1, 2, 3]}, index=pd.Index(['a', 'b', 'c'], name="idx"))
    >>> psdf.index.nlevels
    1
    
    
    
    >>> psdf = ps.DataFrame({'a': [1, 2, 3]}, index=[list('abc'), list('def')])
    >>> psdf.index.nlevels
    2
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.nlevels.rst.txt)


---

## 🔹 103. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.levshape.html

# pyspark.pandas.MultiIndex.levshape#

_property _MultiIndex.levshape#
    

A tuple with the length of each level.

Examples
    
    
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    
    
    
    >>> midx.levshape
    (3, 3)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.levshape.rst.txt)


---

## 🔹 104. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.values.html

# pyspark.pandas.MultiIndex.values#

_property _MultiIndex.values#
    

Return an array representing the data in the Index.

Warning

We recommend using Index.to_numpy() instead.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driverâs memory.

Returns
    

numpy.ndarray
    

Examples
    
    
    >>> ps.Series([1, 2, 3, 4]).index.values
    array([0, 1, 2, 3])
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index.values
    array([(1, 4), (2, 5), (3, 6)], dtype=object)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.values.rst.txt)


---

## 🔹 105. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.dtypes.html

# pyspark.pandas.MultiIndex.dtypes#

_property _MultiIndex.dtypes#
    

Return the dtypes as a Series for the underlying MultiIndex.

New in version 3.3.0.

Returns
    

pd.Series
    

The data type of each level.

Examples
    
    
    >>> psmidx = ps.MultiIndex.from_arrays(
    ...     [[0, 1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    ...     names=("zero", "one"),
    ... )
    >>> psmidx.dtypes
    zero    int64
    one     int64
    dtype: object
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.dtypes.rst.txt)


---

## 🔹 106. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.swaplevel.html

# pyspark.pandas.MultiIndex.swaplevel#

MultiIndex.swaplevel(_i =- 2_, _j =- 1_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.swaplevel)#
    

Swap level i with level j. Calling this method does not change the ordering of the values.

Parameters
    

**i** int, str, default -2
    

First level of index to be swapped. Can pass level name as string. Parameter types can be mixed.

**j** int, str, default -1
    

Second level of index to be swapped. Can pass level name as string. Parameter types can be mixed.

Returns
    

MultiIndex
    

A new MultiIndex.

Examples
    
    
    >>> midx = ps.MultiIndex.from_arrays([['a', 'b'], [1, 2]], names = ['word', 'number'])
    >>> midx  
    MultiIndex([('a', 1),
                ('b', 2)],
               names=['word', 'number'])
    
    
    
    >>> midx.swaplevel(0, 1)  
    MultiIndex([(1, 'a'),
                (2, 'b')],
               names=['number', 'word'])
    
    
    
    >>> midx.swaplevel('number', 'word')  
    MultiIndex([(1, 'a'),
                (2, 'b')],
               names=['number', 'word'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.swaplevel.rst.txt)


---

## 🔹 107. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.droplevel.html

# pyspark.pandas.MultiIndex.droplevel#

MultiIndex.droplevel(_level_)#
    

Return index with requested level(s) removed. If resulting index has only 1 level left, the result will be of Index type, not MultiIndex.

Parameters
    

**level** int, str, tuple, or list-like, default 0
    

If a string is given, must be the name of a level If list-like, elements must be names or indexes of levels.

Returns
    

Index or MultiIndex
    

Examples
    
    
    >>> midx = ps.DataFrame({'a': ['a', 'b']}, index=[['a', 'x'], ['b', 'y'], [1, 2]]).index
    >>> midx  
    MultiIndex([('a', 'b', 1),
                ('x', 'y', 2)],
               )
    >>> midx.droplevel([0, 1])
    Index([1, 2], dtype='int64')
    >>> midx.droplevel(0)  
    MultiIndex([('b', 1),
                ('y', 2)],
               )
    >>> midx.names = [("a", "b"), "b", "c"]
    >>> midx.droplevel([('a', 'b')])  
    MultiIndex([('b', 1),
                ('y', 2)],
               names=['b', 'c'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.droplevel.rst.txt)


---

## 🔹 108. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.fillna.html

# pyspark.pandas.MultiIndex.fillna#

MultiIndex.fillna(_value_)#
    

Fill NA/NaN values with the specified value.

Parameters
    

**value** scalar
    

Scalar value to use to fill holes (example: 0). This value cannot be a list-likes.

Returns
    

Index
    

filled with value

Examples
    
    
    >>> idx = ps.Index([1, 2, None])
    >>> idx
    Index([1.0, 2.0, nan], dtype='float64')
    
    
    
    >>> idx.fillna(0)
    Index([1.0, 2.0, 0.0], dtype='float64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.fillna.rst.txt)


---

## 🔹 109. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.dropna.html

# pyspark.pandas.MultiIndex.dropna#

MultiIndex.dropna(_how ='any'_)#
    

Return Index or MultiIndex without NA/NaN values

Parameters
    

**how**{âanyâ, âallâ}, default âanyâ
    

If the Index is a MultiIndex, drop the value when any or all levels are NaN.

Returns
    

Index or MultiIndex
    

Examples
    
    
    >>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
    ...                   index=['cobra', 'viper', None],
    ...                   columns=['max_speed', 'shield'])
    >>> df  
           max_speed  shield
    cobra          1       2
    viper          4       5
    None           7       8
    
    
    
    >>> df.index.dropna()
    Index(['cobra', 'viper'], dtype='object')
    

Also support for MultiIndex
    
    
    >>> tuples = [(np.nan, 1.0), (2.0, 2.0), (np.nan, np.nan), (3.0, np.nan)]
    >>> midx = ps.MultiIndex.from_tuples(tuples)
    >>> midx  
    MultiIndex([(nan, 1.0),
                (2.0, 2.0),
                (nan, nan),
                (3.0, nan)],
               )
    
    
    
    >>> midx.dropna()  
    MultiIndex([(2.0, 2.0)],
               )
    
    
    
    >>> midx.dropna(how="all")  
    MultiIndex([(nan, 1.0),
                (2.0, 2.0),
                (3.0, nan)],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.dropna.rst.txt)


---

## 🔹 110. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.equals.html

# pyspark.pandas.MultiIndex.equals#

MultiIndex.equals(_other_)#
    

Determine if two Index objects contain the same elements.

Returns
    

bool
    

True if âotherâ is an Index and it has the same elements as calling index; False otherwise.

Examples
    
    
    >>> from pyspark.pandas.config import option_context
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx.name = "name"
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> midx.names = ("nameA", "nameB")
    

For Index
    
    
    >>> idx.equals(idx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.equals(ps.Index(['a', 'b', 'c']))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.equals(ps.Index(['b', 'b', 'a']))
    False
    >>> idx.equals(midx)
    False
    

For MultiIndex
    
    
    >>> midx.equals(midx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.equals(ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.equals(ps.MultiIndex.from_tuples([('c', 'z'), ('b', 'y'), ('a', 'x')]))
    False
    >>> midx.equals(idx)
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.equals.rst.txt)


---

## 🔹 111. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.equal_levels.html

# pyspark.pandas.MultiIndex.equal_levels#

MultiIndex.equal_levels(_other_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.equal_levels)#
    

Return True if the levels of both MultiIndex objects are the same

New in version 3.3.0.

Examples
    
    
    >>> psmidx1 = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "z")])
    >>> psmidx2 = ps.MultiIndex.from_tuples([("b", "y"), ("a", "x"), ("c", "z")])
    >>> psmidx1.equal_levels(psmidx2)
    True
    
    
    
    >>> psmidx2 = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "j")])
    >>> psmidx1.equal_levels(psmidx2)
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.equal_levels.rst.txt)


---

## 🔹 112. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.identical.html

# pyspark.pandas.MultiIndex.identical#

MultiIndex.identical(_other_)#
    

Similar to equals, but check that other comparable attributes are also equal.

Returns
    

bool
    

If two Index objects have equal elements and same type True, otherwise False.

Examples
    
    
    >>> from pyspark.pandas.config import option_context
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> midx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    

For Index
    
    
    >>> idx.identical(idx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.identical(ps.Index(['a', 'b', 'c']))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     idx.identical(ps.Index(['b', 'b', 'a']))
    False
    >>> idx.identical(midx)
    False
    

For MultiIndex
    
    
    >>> midx.identical(midx)
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.identical(ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')]))
    True
    >>> with option_context('compute.ops_on_diff_frames', True):
    ...     midx.identical(ps.MultiIndex.from_tuples([('c', 'z'), ('b', 'y'), ('a', 'x')]))
    False
    >>> midx.identical(idx)
    False
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.identical.rst.txt)


---

## 🔹 113. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.insert.html

# pyspark.pandas.MultiIndex.insert#

MultiIndex.insert(_loc_ , _item_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.insert)#
    

Make new MultiIndex inserting new item at location.

Follows Python list.append semantics for negative values.

Changed in version 3.4.0: Raise IndexError when loc is out of bounds to follow Pandas 1.4+ behavior

Parameters
    

**loc** int
    
**item** object
    
Returns
    

**new_index** MultiIndex
    

Examples
    
    
    >>> psmidx = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "z")])
    >>> psmidx.insert(3, ("h", "j"))  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z'),
                ('h', 'j')],
               )
    

For negative values
    
    
    >>> psmidx.insert(-2, ("h", "j"))  
    MultiIndex([('a', 'x'),
                ('h', 'j'),
                ('b', 'y'),
                ('c', 'z')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.insert.rst.txt)


---

## 🔹 114. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.drop.html

# pyspark.pandas.MultiIndex.drop#

MultiIndex.drop(_codes_ , _level =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.drop)#
    

Make new MultiIndex with passed list of labels deleted

Parameters
    

**codes** array-like
    

Must be a list of tuples

**level** int or level name, default None
    
Returns
    

**dropped** MultiIndex
    

Examples
    
    
    >>> index = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
    >>> index 
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('c', 'z')],
               )
    
    
    
    >>> index.drop(['a']) 
    MultiIndex([('b', 'y'),
                ('c', 'z')],
               )
    
    
    
    >>> index.drop(['x', 'y'], level=1) 
    MultiIndex([('c', 'z')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.drop.rst.txt)


---

## 🔹 115. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.copy.html

# pyspark.pandas.MultiIndex.copy#

MultiIndex.copy(_deep =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.copy)#
    

Make a copy of this object.

Parameters
    

**deep** None
    

this parameter is not supported but just dummy parameter to match pandas.

Examples
    
    
    >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
    ...                   columns=['dogs', 'cats'],
    ...                   index=[list('abcd'), list('efgh')])
    >>> df['dogs'].index  
    MultiIndex([('a', 'e'),
                ('b', 'f'),
                ('c', 'g'),
                ('d', 'h')],
               )
    

Copy index
    
    
    >>> df.index.copy()  
    MultiIndex([('a', 'e'),
                ('b', 'f'),
                ('c', 'g'),
                ('d', 'h')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.copy.rst.txt)


---

## 🔹 116. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.delete.html

# pyspark.pandas.MultiIndex.delete#

MultiIndex.delete(_loc_)#
    

Make new Index with passed location(-s) deleted.

Note

this API can be pretty expensive since it is based on a global sequence internally.

Returns
    

**new_index** Index
    

Examples
    
    
    >>> psidx = ps.Index([10, 10, 9, 8, 4, 2, 4, 4, 2, 2, 10, 10])
    >>> psidx
    Index([10, 10, 9, 8, 4, 2, 4, 4, 2, 2, 10, 10], dtype='int64')
    
    
    
    >>> psidx.delete(0).sort_values()
    Index([2, 2, 2, 4, 4, 4, 8, 9, 10, 10, 10], dtype='int64')
    
    
    
    >>> psidx.delete([0, 1, 2, 3, 10, 11]).sort_values()
    Index([2, 2, 2, 4, 4, 4], dtype='int64')
    

MultiIndex
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)])
    >>> psidx  
    MultiIndex([('a', 'x', 1),
                ('b', 'y', 2),
                ('c', 'z', 3)],
               )
    
    
    
    >>> psidx.delete([0, 2]).sort_values()  
    MultiIndex([('b', 'y', 2)],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.delete.rst.txt)


---

## 🔹 117. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.rename.html

# pyspark.pandas.MultiIndex.rename#

MultiIndex.rename(_name_ , _inplace =False_)#
    

Alter Index or MultiIndex name. Able to set new names without level. Defaults to returning a new index.

Parameters
    

**name** label or list of labels
    

Name(s) to set.

**inplace** boolean, default False
    

Modifies the object directly, instead of creating a new Index or MultiIndex.

Returns
    

Index or MultiIndex
    

The same type as the caller or None if inplace is True.

Examples
    
    
    >>> df = ps.DataFrame({'a': ['A', 'C'], 'b': ['A', 'B']}, columns=['a', 'b'])
    >>> df.index.rename("c")
    Index([0, 1], dtype='int64', name='c')
    
    
    
    >>> df.set_index("a", inplace=True)
    >>> df.index.rename("d")
    Index(['A', 'C'], dtype='object', name='d')
    

You can also change the index name in place.
    
    
    >>> df.index.rename("e", inplace=True)
    >>> df.index
    Index(['A', 'C'], dtype='object', name='e')
    
    
    
    >>> df  
       b
    e
    A  A
    C  B
    

Support for MultiIndex
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
    >>> psidx.names = ['hello', 'pandas-on-Spark']
    >>> psidx  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               names=['hello', 'pandas-on-Spark'])
    
    
    
    >>> psidx.rename(['aloha', 'databricks'])  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               names=['aloha', 'databricks'])
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.rename.rst.txt)


---

## 🔹 118. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.repeat.html

# pyspark.pandas.MultiIndex.repeat#

MultiIndex.repeat(_repeats_)#
    

Repeat elements of a Index/MultiIndex.

Returns a new Index/MultiIndex where each element of the current Index/MultiIndex is repeated consecutively a given number of times.

Parameters
    

**repeats** int
    

The number of repetitions for each element. This should be a non-negative integer. Repeating 0 times will return an empty Index.

Returns
    

**repeated_index** Index/MultiIndex
    

Newly created Index/MultiIndex with repeated elements.

See also

[`Series.repeat`](pyspark.pandas.Series.repeat.html#pyspark.pandas.Series.repeat "pyspark.pandas.Series.repeat")
    

Equivalent function for Series.

Examples
    
    
    >>> idx = ps.Index(['a', 'b', 'c'])
    >>> idx
    Index(['a', 'b', 'c'], dtype='object')
    >>> idx.repeat(2)
    Index(['a', 'b', 'c', 'a', 'b', 'c'], dtype='object')
    

For MultiIndex,
    
    
    >>> midx = ps.MultiIndex.from_tuples([('x', 'a'), ('x', 'b'), ('y', 'c')])
    >>> midx  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('y', 'c')],
               )
    >>> midx.repeat(2)  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('y', 'c'),
                ('x', 'a'),
                ('x', 'b'),
                ('y', 'c')],
               )
    >>> midx.repeat(0)  
    MultiIndex([], )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.repeat.rst.txt)


---

## 🔹 119. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.take.html

# pyspark.pandas.MultiIndex.take#

MultiIndex.take(_indices_)#
    

Return the elements in the given _positional_ indices along an axis.

This means that we are not indexing according to actual values in the index attribute of the object. We are indexing according to the actual position of the element in the object.

Parameters
    

**indices** array-like
    

An array of ints indicating which positions to take.

Returns
    

**taken** same type as caller
    

An array-like containing the elements taken from the object.

See also

[`DataFrame.loc`](pyspark.pandas.DataFrame.loc.html#pyspark.pandas.DataFrame.loc "pyspark.pandas.DataFrame.loc")
    

Select a subset of a DataFrame by labels.

[`DataFrame.iloc`](pyspark.pandas.DataFrame.iloc.html#pyspark.pandas.DataFrame.iloc "pyspark.pandas.DataFrame.iloc")
    

Select a subset of a DataFrame by positions.

`numpy.take`
    

Take elements from an array along an axis.

Examples

Series
    
    
    >>> psser = ps.Series([100, 200, 300, 400, 500])
    >>> psser
    0    100
    1    200
    2    300
    3    400
    4    500
    dtype: int64
    
    
    
    >>> psser.take([0, 2, 4]).sort_index()
    0    100
    2    300
    4    500
    dtype: int64
    

Index
    
    
    >>> psidx = ps.Index([100, 200, 300, 400, 500])
    >>> psidx
    Index([100, 200, 300, 400, 500], dtype='int64')
    
    
    
    >>> psidx.take([0, 2, 4]).sort_values()
    Index([100, 300, 500], dtype='int64')
    

MultiIndex
    
    
    >>> psmidx = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c")])
    >>> psmidx  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('x', 'c')],
               )
    
    
    
    >>> psmidx.take([0, 2])  
    MultiIndex([('x', 'a'),
                ('x', 'c')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.take.rst.txt)


---

## 🔹 120. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.unique.html

# pyspark.pandas.MultiIndex.unique#

MultiIndex.unique(_level =None_)#
    

Return unique values in the index.

Be aware the order of unique values might be different than pandas.Index.unique

Parameters
    

**level** int or str, optional, default is None
    
Returns
    

Index without duplicates
    

See also

[`Series.unique`](pyspark.pandas.Series.unique.html#pyspark.pandas.Series.unique "pyspark.pandas.Series.unique")
    
[`groupby.SeriesGroupBy.unique`](pyspark.pandas.groupby.SeriesGroupBy.unique.html#pyspark.pandas.groupby.SeriesGroupBy.unique "pyspark.pandas.groupby.SeriesGroupBy.unique")
    

Examples
    
    
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[1, 1, 3]).index.unique().sort_values()
    Index([1, 3], dtype='int64')
    
    
    
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=['d', 'e', 'e']).index.unique().sort_values()
    Index(['d', 'e'], dtype='object')
    

MultiIndex
    
    
    >>> ps.MultiIndex.from_tuples([("A", "X"), ("A", "Y"), ("A", "X")]).unique()
    ... 
    MultiIndex([('A', 'X'),
                ('A', 'Y')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.unique.rst.txt)


---

## 🔹 121. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.min.html

# pyspark.pandas.MultiIndex.min#

MultiIndex.min()#
    

Return the minimum value of the Index.

Returns
    

scalar
    

Minimum value.

See also

[`Index.max`](pyspark.pandas.Index.max.html#pyspark.pandas.Index.max "pyspark.pandas.Index.max")
    

Return the maximum value of the object.

[`Series.min`](pyspark.pandas.Series.min.html#pyspark.pandas.Series.min "pyspark.pandas.Series.min")
    

Return the minimum value in a Series.

[`DataFrame.min`](pyspark.pandas.DataFrame.min.html#pyspark.pandas.DataFrame.min "pyspark.pandas.DataFrame.min")
    

Return the minimum values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([3, 2, 1])
    >>> idx.min()
    1
    
    
    
    >>> idx = ps.Index(['c', 'b', 'a'])
    >>> idx.min()
    'a'
    

For a MultiIndex, the maximum is determined lexicographically.
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
    >>> idx.min()
    ('a', 'x', 1)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.min.rst.txt)


---

## 🔹 122. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.max.html

# pyspark.pandas.MultiIndex.max#

MultiIndex.max()#
    

Return the maximum value of the Index.

Returns
    

scalar
    

Maximum value.

See also

[`Index.min`](pyspark.pandas.Index.min.html#pyspark.pandas.Index.min "pyspark.pandas.Index.min")
    

Return the minimum value in an Index.

[`Series.max`](pyspark.pandas.Series.max.html#pyspark.pandas.Series.max "pyspark.pandas.Series.max")
    

Return the maximum value in a Series.

[`DataFrame.max`](pyspark.pandas.DataFrame.max.html#pyspark.pandas.DataFrame.max "pyspark.pandas.DataFrame.max")
    

Return the maximum values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([3, 2, 1])
    >>> idx.max()
    3
    
    
    
    >>> idx = ps.Index(['c', 'b', 'a'])
    >>> idx.max()
    'c'
    

For a MultiIndex, the maximum is determined lexicographically.
    
    
    >>> idx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2)])
    >>> idx.max()
    ('b', 'y', 2)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.max.rst.txt)


---

## 🔹 123. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.value_counts.html

# pyspark.pandas.MultiIndex.value_counts#

MultiIndex.value_counts(_normalize =False_, _sort =True_, _ascending =False_, _bins =None_, _dropna =True_)#
    

Return a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

Parameters
    

**normalize** boolean, default False
    

If True then the object returned will contain the relative frequencies of the unique values.

**sort** boolean, default True
    

Sort by values.

**ascending** boolean, default False
    

Sort in ascending order.

**bins** Not Yet Supported
    
**dropna** boolean, default True
    

Donât include counts of NaN.

Returns
    

**counts** Series
    

See also

[`Series.count`](pyspark.pandas.Series.count.html#pyspark.pandas.Series.count "pyspark.pandas.Series.count")
    

Number of non-NA elements in a Series.

Examples

For Series
    
    
    >>> df = ps.DataFrame({'x':[0, 0, 1, 1, 1, np.nan]})
    >>> df.x.value_counts()  
    x
    1.0    3
    0.0    2
    Name: count, dtype: int64
    

With normalize set to True, returns the relative frequency by dividing all values by the sum of values.
    
    
    >>> df.x.value_counts(normalize=True)  
    x
    1.0    0.6
    0.0    0.4
    Name: proportion, dtype: float64
    

**dropna** With dropna set to False we can also see NaN index values.
    
    
    >>> df.x.value_counts(dropna=False)  
    x
    1.0    3
    0.0    2
    NaN    1
    Name: count, dtype: int64
    

For Index
    
    
    >>> idx = ps.Index([3, 1, 2, 3, 4, np.nan])
    >>> idx
    Index([3.0, 1.0, 2.0, 3.0, 4.0, nan], dtype='float64')
    
    
    
    >>> idx.value_counts().sort_index()
    1.0    1
    2.0    1
    3.0    2
    4.0    1
    Name: count, dtype: int64
    

**sort**

With sort set to False, the result wouldnât be sorted by number of count.
    
    
    >>> idx.value_counts(sort=True).sort_index()
    1.0    1
    2.0    1
    3.0    2
    4.0    1
    Name: count, dtype: int64
    

**normalize**

With normalize set to True, returns the relative frequency by dividing all values by the sum of values.
    
    
    >>> idx.value_counts(normalize=True).sort_index()
    1.0    0.2
    2.0    0.2
    3.0    0.4
    4.0    0.2
    Name: proportion, dtype: float64
    

**dropna**

With dropna set to False we can also see NaN index values.
    
    
    >>> idx.value_counts(dropna=False).sort_index()  
    1.0    1
    2.0    1
    3.0    2
    4.0    1
    NaN    1
    dtype: int64
    

For MultiIndex.
    
    
    >>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
    ...                       ['speed', 'weight', 'length']],
    ...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
    >>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
    >>> s.index  
    MultiIndex([(  'lama', 'weight'),
                (  'lama', 'weight'),
                (  'lama', 'weight'),
                (   'cow', 'weight'),
                (   'cow', 'weight'),
                (   'cow', 'length'),
                ('falcon', 'weight'),
                ('falcon', 'length'),
                ('falcon', 'length')],
               )
    
    
    
    >>> s.index.value_counts().sort_index()
    (cow, length)       1
    (cow, weight)       2
    (falcon, length)    2
    (falcon, weight)    1
    (lama, weight)      3
    Name: count, dtype: int64
    
    
    
    >>> s.index.value_counts(normalize=True).sort_index()
    (cow, length)       0.111111
    (cow, weight)       0.222222
    (falcon, length)    0.222222
    (falcon, weight)    0.111111
    (lama, weight)      0.333333
    Name: proportion, dtype: float64
    

If Index has name, keep the name up.
    
    
    >>> idx = ps.Index([0, 0, 0, 1, 1, 2, 3], name='pandas-on-Spark')
    >>> idx.value_counts().sort_index()
    pandas-on-Spark
    0    3
    1    2
    2    1
    3    1
    Name: count, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.value_counts.rst.txt)


---

## 🔹 124. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.append.html

# pyspark.pandas.MultiIndex.append#

MultiIndex.append(_other_)#
    

Append a collection of Index options together.

Parameters
    

**other** Index
    
Returns
    

**appended** Index
    

Examples
    
    
    >>> psidx = ps.Index([10, 5, 0, 5, 10, 5, 0, 10])
    >>> psidx
    Index([10, 5, 0, 5, 10, 5, 0, 10], dtype='int64')
    
    
    
    >>> psidx.append(psidx)
    Index([10, 5, 0, 5, 10, 5, 0, 10, 10, 5, 0, 5, 10, 5, 0, 10], dtype='int64')
    

Support for MiltiIndex
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x'), ('b', 'y')])
    >>> psidx  
    MultiIndex([('a', 'x'),
                ('b', 'y')],
               )
    
    
    
    >>> psidx.append(psidx)  
    MultiIndex([('a', 'x'),
                ('b', 'y'),
                ('a', 'x'),
                ('b', 'y')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.append.rst.txt)


---

## 🔹 125. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.intersection.html

# pyspark.pandas.MultiIndex.intersection#

MultiIndex.intersection(_other_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.intersection)#
    

Form the intersection of two Index objects.

This returns a new Index with elements common to the index and other.

Parameters
    

**other** Index or array-like
    
Returns
    

**intersection** MultiIndex
    

Examples
    
    
    >>> midx1 = ps.MultiIndex.from_tuples([("a", "x"), ("b", "y"), ("c", "z")])
    >>> midx2 = ps.MultiIndex.from_tuples([("c", "z"), ("d", "w")])
    >>> midx1.intersection(midx2).sort_values()  
    MultiIndex([('c', 'z')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.intersection.rst.txt)


---

## 🔹 126. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.union.html

# pyspark.pandas.MultiIndex.union#

MultiIndex.union(_other_ , _sort =None_)#
    

Form the union of two Index objects.

Parameters
    

**other** Index or array-like
    
**sort** bool or None, default None
    

Whether to sort the resulting Index.

Returns
    

**union** Index
    

Examples

Index
    
    
    >>> idx1 = ps.Index([1, 2, 3, 4])
    >>> idx2 = ps.Index([3, 4, 5, 6])
    >>> idx1.union(idx2).sort_values()
    Index([1, 2, 3, 4, 5, 6], dtype='int64')
    

MultiIndex
    
    
    >>> midx1 = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c"), ("x", "d")])
    >>> midx2 = ps.MultiIndex.from_tuples([("x", "c"), ("x", "d"), ("x", "e"), ("x", "f")])
    >>> midx1.union(midx2).sort_values()  
    MultiIndex([('x', 'a'),
                ('x', 'b'),
                ('x', 'c'),
                ('x', 'd'),
                ('x', 'e'),
                ('x', 'f')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.union.rst.txt)


---

## 🔹 127. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.difference.html

# pyspark.pandas.MultiIndex.difference#

MultiIndex.difference(_other_ , _sort =None_)#
    

Return a new Index with elements from the index that are not in other.

This is the set difference of two Index objects.

Parameters
    

**other** Index or array-like
    
**sort** True or None, default None
    

Whether to sort the resulting index. * True : Attempt to sort the result. * None : Do not sort the result.

Returns
    

**difference** Index
    

Examples
    
    
    >>> idx1 = ps.Index([2, 1, 3, 4])
    >>> idx2 = ps.Index([3, 4, 5, 6])
    >>> idx1.difference(idx2, sort=True)
    Index([1, 2], dtype='int64')
    

MultiIndex
    
    
    >>> midx1 = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'y', 2), ('c', 'z', 3)])
    >>> midx2 = ps.MultiIndex.from_tuples([('a', 'x', 1), ('b', 'z', 2), ('k', 'z', 3)])
    >>> midx1.difference(midx2)  
    MultiIndex([('b', 'y', 2),
                ('c', 'z', 3)],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.difference.rst.txt)


---

## 🔹 128. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.symmetric_difference.html

# pyspark.pandas.MultiIndex.symmetric_difference#

MultiIndex.symmetric_difference(_other_ , _result_name =None_, _sort =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.symmetric_difference)#
    

Compute the symmetric difference of two MultiIndex objects.

Parameters
    

**other** Index or array-like
    
**result_name** list
    
**sort** True or None, default None
    

Whether to sort the resulting index. * True : Attempt to sort the result. * None : Do not sort the result.

Returns
    

**symmetric_difference** MultiIndex
    

Notes

`symmetric_difference` contains elements that appear in either `idx1` or `idx2` but not both. Equivalent to the Index created by `idx1.difference(idx2) | idx2.difference(idx1)` with duplicates dropped.

Examples
    
    
    >>> midx1 = pd.MultiIndex([['lama', 'cow', 'falcon'],
    ...                        ['speed', 'weight', 'length']],
    ...                       [[0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...                        [0, 0, 0, 0, 1, 2, 0, 1, 2]])
    >>> midx2 = pd.MultiIndex([['pandas-on-Spark', 'cow', 'falcon'],
    ...                        ['speed', 'weight', 'length']],
    ...                       [[0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...                        [0, 0, 0, 0, 1, 2, 0, 1, 2]])
    >>> s1 = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
    ...                index=midx1)
    >>> s2 = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
    ...              index=midx2)
    
    
    
    >>> s1.index.symmetric_difference(s2.index)  
    MultiIndex([('pandas-on-Spark', 'speed'),
                (  'lama', 'speed')],
               )
    

You can set names of the result Index.
    
    
    >>> s1.index.symmetric_difference(s2.index, result_name=['a', 'b'])  
    MultiIndex([('pandas-on-Spark', 'speed'),
                (  'lama', 'speed')],
               names=['a', 'b'])
    

You can set sort to True, if you want to sort the resulting index.
    
    
    >>> s1.index.symmetric_difference(s2.index, sort=True)  
    MultiIndex([('pandas-on-Spark', 'speed'),
                (  'lama', 'speed')],
               )
    

You can also use the `^` operator:
    
    
    >>> s1.index ^ s2.index  
    MultiIndex([('pandas-on-Spark', 'speed'),
                (  'lama', 'speed')],
               )
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.symmetric_difference.rst.txt)


---

## 🔹 129. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.astype.html

# pyspark.pandas.MultiIndex.astype#

MultiIndex.astype(_dtype_)#
    

Cast a pandas-on-Spark object to a specified dtype `dtype`.

Parameters
    

**dtype** data type
    

Use a numpy.dtype or Python type to cast entire pandas object to the same type.

Returns
    

**casted** same type as caller
    

See also

[`to_datetime`](pyspark.pandas.to_datetime.html#pyspark.pandas.to_datetime "pyspark.pandas.to_datetime")
    

Convert argument to datetime.

Examples
    
    
    >>> ser = ps.Series([1, 2], dtype='int32')
    >>> ser
    0    1
    1    2
    dtype: int32
    
    
    
    >>> ser.astype('int64')
    0    1
    1    2
    dtype: int64
    
    
    
    >>> ser.rename("a").to_frame().set_index("a").index.astype('int64')
    Index([1, 2], dtype='int64', name='a')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.astype.rst.txt)


---

## 🔹 130. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.item.html

# pyspark.pandas.MultiIndex.item#

MultiIndex.item()[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.item)#
    

Return the first element of the underlying data as a python tuple.

Returns
    

tuple
    

The first element of MultiIndex.

Raises
    

ValueError
    

If the data is not length-1.

Examples
    
    
    >>> psmidx = ps.MultiIndex.from_tuples([('a', 'x')])
    >>> psmidx.item()
    ('a', 'x')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.item.rst.txt)


---

## 🔹 131. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_list.html

# pyspark.pandas.MultiIndex.to_list#

MultiIndex.to_list()#
    

Return a list of the values.

These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)

Note

This method should only be used if the resulting list is expected to be small, as all the data is loaded into the driverâs memory.

Examples

Index
    
    
    >>> idx = ps.Index([1, 2, 3, 4, 5])
    >>> idx.to_list()
    [1, 2, 3, 4, 5]
    

MultiIndex
    
    
    >>> tuples = [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
    >>> midx = ps.MultiIndex.from_tuples(tuples)
    >>> midx.to_list()
    [(1, 'red'), (1, 'blue'), (2, 'red'), (2, 'green')]
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_list.rst.txt)


---

## 🔹 132. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_series.html

# pyspark.pandas.MultiIndex.to_series#

MultiIndex.to_series(_name =None_)#
    

Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.

Parameters
    

**name** string, optional
    

name of resulting Series. If None, defaults to name of original index

Returns
    

**Series** dtype will be based on the type of the Index values.
    

Examples
    
    
    >>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
    ...                   columns=['dogs', 'cats'],
    ...                   index=list('abcd'))
    >>> df['dogs'].index.to_series()
    a    a
    b    b
    c    c
    d    d
    dtype: object
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_series.rst.txt)


---

## 🔹 133. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_frame.html

# pyspark.pandas.MultiIndex.to_frame#

MultiIndex.to_frame(_index =True_, _name =None_)[[source]](../../../_modules/pyspark/pandas/indexes/multi.html#MultiIndex.to_frame)#
    

Create a DataFrame with the levels of the MultiIndex as columns. Column ordering is determined by the DataFrame constructor with data as a dict.

Parameters
    

**index** boolean, default True
    

Set the index of the returned DataFrame as the original MultiIndex.

**name** list / sequence of strings, optional
    

The passed names should substitute index level names.

Returns
    

**DataFrame** a DataFrame containing the original MultiIndex data.
    

See also

[`DataFrame`](pyspark.pandas.DataFrame.html#pyspark.pandas.DataFrame "pyspark.pandas.DataFrame")
    

Examples
    
    
    >>> tuples = [(1, 'red'), (1, 'blue'),
    ...           (2, 'red'), (2, 'blue')]
    >>> idx = ps.MultiIndex.from_tuples(tuples, names=('number', 'color'))
    >>> idx  
    MultiIndex([(1,  'red'),
                (1, 'blue'),
                (2,  'red'),
                (2, 'blue')],
               names=['number', 'color'])
    >>> idx.to_frame()  
                  number color
    number color
    1      red         1   red
           blue        1  blue
    2      red         2   red
           blue        2  blue
    

By default, the original Index is reused. To enforce a new Index:
    
    
    >>> idx.to_frame(index=False)
       number color
    0       1   red
    1       1  blue
    2       2   red
    3       2  blue
    

To override the name of the resulting column, specify name:
    
    
    >>> idx.to_frame(name=['n', 'c'])  
                  n     c
    number color
    1      red    1   red
           blue   1  blue
    2      red    2   red
           blue   2  blue
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_frame.rst.txt)


---

## 🔹 134. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.view.html

# pyspark.pandas.MultiIndex.view#

MultiIndex.view()#
    

this is defined as a copy with the same identity

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.view.rst.txt)


---

## 🔹 135. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_numpy.html

# pyspark.pandas.MultiIndex.to_numpy#

MultiIndex.to_numpy(_dtype =None_, _copy =False_)#
    

A NumPy ndarray representing the values in this Index or MultiIndex.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driverâs memory.

Parameters
    

**dtype** str or numpy.dtype, optional
    

The dtype to pass to `numpy.asarray()`

**copy** bool, default False
    

Whether to ensure that the returned value is not a view on another array. Note that `copy=False` does not _ensure_ that `to_numpy()` is no-copy. Rather, `copy=True` ensures that a copy is made, even if not strictly necessary.

Returns
    

numpy.ndarray
    

Examples
    
    
    >>> ps.Series([1, 2, 3, 4]).index.to_numpy()
    array([0, 1, 2, 3])
    >>> ps.DataFrame({'a': ['a', 'b', 'c']}, index=[[1, 2, 3], [4, 5, 6]]).index.to_numpy()
    array([(1, 4), (2, 5), (3, 6)], dtype=object)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.to_numpy.rst.txt)


---

## 🔹 136. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.spark.data_type.html

# pyspark.pandas.MultiIndex.spark.data_type#

spark.data_type#
    

Returns the data type as defined by Spark, as a Spark DataType object.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.spark.data_type.rst.txt)


---

## 🔹 137. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.spark.column.html

# pyspark.pandas.MultiIndex.spark.column#

spark.column#
    

Spark Column object representing the Series/Index.

Note

This Spark Column object is strictly stick to its base DataFrame the Series/Index was derived from.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.spark.column.rst.txt)


---

## 🔹 138. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.spark.transform.html

# pyspark.pandas.MultiIndex.spark.transform#

spark.transform(_func_)#
    

Applies a function that takes and returns a Spark column. It allows natively applying a Spark function and column APIs with the Spark column internally used in Series or Index. The output length of the Spark column should be the same as inputâs.

Note

It requires to have the same input and output length; therefore, the aggregate Spark functions such as count does not work.

Parameters
    

**func** function
    

Function to use for transforming the data by using Spark columns.

Returns
    

Series or Index
    
Raises
    

**ValueError** If the output from the function is not a Spark column.
    

Examples
    
    
    >>> from pyspark.sql.functions import log
    >>> df = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, columns=["a", "b"])
    >>> df
       a  b
    0  1  4
    1  2  5
    2  3  6
    
    
    
    >>> df.a.spark.transform(lambda c: log(c))
    0    0.000000
    1    0.693147
    2    1.098612
    Name: a, dtype: float64
    
    
    
    >>> df.index.spark.transform(lambda c: c + 10)
    Index([10, 11, 12], dtype='int64')
    
    
    
    >>> df.a.spark.transform(lambda c: c + df.b.spark.column)
    0    5
    1    7
    2    9
    Name: a, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.spark.transform.rst.txt)


---

## 🔹 139. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.sort_values.html

# pyspark.pandas.MultiIndex.sort_values#

MultiIndex.sort_values(_return_indexer =False_, _ascending =True_)#
    

Return a sorted copy of the index, and optionally return the indices that sorted the index itself.

Note

This method is not supported for pandas when index has NaN value. pandas raises unexpected TypeError, but we support treating NaN as the smallest value. This method returns indexer as a pandas-on-Spark index while pandas returns it as a list. Thatâs because indexer in pandas-on-Spark may not fit in memory.

Parameters
    

**return_indexer** bool, default False
    

Should the indices that would sort the index be returned.

**ascending** bool, default True
    

Should the index values be sorted in an ascending order.

Returns
    

**sorted_index** ps.Index or ps.MultiIndex
    

Sorted copy of the index.

**indexer** ps.Index
    

The indices that the index itself was sorted by.

See also

[`Series.sort_values`](pyspark.pandas.Series.sort_values.html#pyspark.pandas.Series.sort_values "pyspark.pandas.Series.sort_values")
    

Sort values of a Series.

[`DataFrame.sort_values`](pyspark.pandas.DataFrame.sort_values.html#pyspark.pandas.DataFrame.sort_values "pyspark.pandas.DataFrame.sort_values")
    

Sort values in a DataFrame.

Examples
    
    
    >>> idx = ps.Index([10, 100, 1, 1000])
    >>> idx
    Index([10, 100, 1, 1000], dtype='int64')
    

Sort values in ascending order (default behavior).
    
    
    >>> idx.sort_values()
    Index([1, 10, 100, 1000], dtype='int64')
    

Sort values in descending order.
    
    
    >>> idx.sort_values(ascending=False)
    Index([1000, 100, 10, 1], dtype='int64')
    

Sort values in descending order, and also get the indices idx was sorted by.
    
    
    >>> idx.sort_values(ascending=False, return_indexer=True)
    (Index([1000, 100, 10, 1], dtype='int64'), Index([3, 1, 0, 2], dtype='int64'))
    

Support for MultiIndex.
    
    
    >>> psidx = ps.MultiIndex.from_tuples([('a', 'x', 1), ('c', 'y', 2), ('b', 'z', 3)])
    >>> psidx  
    MultiIndex([('a', 'x', 1),
                ('c', 'y', 2),
                ('b', 'z', 3)],
               )
    
    
    
    >>> psidx.sort_values()  
    MultiIndex([('a', 'x', 1),
                ('b', 'z', 3),
                ('c', 'y', 2)],
               )
    
    
    
    >>> psidx.sort_values(ascending=False)  
    MultiIndex([('c', 'y', 2),
                ('b', 'z', 3),
                ('a', 'x', 1)],
               )
    
    
    
    >>> psidx.sort_values(ascending=False, return_indexer=True)
    (MultiIndex([('c', 'y', 2),
                ('b', 'z', 3),
                ('a', 'x', 1)],
               ), Index([1, 2, 0], dtype='int64'))
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.MultiIndex.sort_values.rst.txt)


---

## 🔹 140. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.html

# pyspark.pandas.DatetimeIndex#

_class _pyspark.pandas.DatetimeIndex(_data=None_ , _freq= <no value>_, _normalize=False_ , _closed=None_ , _ambiguous='raise'_ , _dayfirst=False_ , _yearfirst=False_ , _dtype=None_ , _copy=False_ , _name=None_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex)#
    

Immutable ndarray-like of datetime64 data.

Parameters
    

**data** array-like (1-dimensional), optional
    

Optional datetime-like data to construct index with.

**freq** str or pandas offset object, optional
    

One of pandas date offset strings or corresponding objects. The string âinferâ can be passed in order to set the frequency of the index as the inferred frequency upon creation.

**normalize** bool, default False
    

Normalize start/end dates to midnight before generating date range.

Deprecated since version 4.0.0.

**closed**{âleftâ, ârightâ}, optional
    

Set whether to include start and end that are on the boundary. The default includes boundary points on either end.

Deprecated since version 4.0.0.

**ambiguous** âinferâ, bool-ndarray, âNaTâ, default âraiseâ
    

When clocks moved backward due to DST, ambiguous times may arise. For example in Central European Time (UTC+01), when going from 03:00 DST to 02:00 non-DST, 02:30:00 local time occurs both at 00:30:00 UTC and at 01:30:00 UTC. In such a situation, the ambiguous parameter dictates how ambiguous times should be handled.

  * âinferâ will attempt to infer fall dst-transition hours based on order

  * bool-ndarray where True signifies a DST time, False signifies a non-DST time (note that this flag is only applicable for ambiguous times)

  * âNaTâ will return NaT where there are ambiguous times

  * âraiseâ will raise an AmbiguousTimeError if there are ambiguous times.



**dayfirst** bool, default False
    

If True, parse dates in data with the day first order.

**yearfirst** bool, default False
    

If True parse dates in data with the year first order.

**dtype** numpy.dtype or str, default None
    

Note that the only NumPy dtype allowed is âdatetime64[ns]â.

**copy** bool, default False
    

Make a copy of input ndarray.

**name** label, default None
    

Name to be stored in the index.

See also

[`Index`](pyspark.pandas.Index.html#pyspark.pandas.Index "pyspark.pandas.Index")
    

The base pandas Index type.

[`to_datetime`](pyspark.pandas.to_datetime.html#pyspark.pandas.to_datetime "pyspark.pandas.to_datetime")
    

Convert argument to datetime.

Examples
    
    
    >>> ps.DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'])
    DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'], dtype='datetime64[ns]', freq=None)
    

From a Series:
    
    
    >>> from datetime import datetime
    >>> s = ps.Series([datetime(2021, 3, 1), datetime(2021, 3, 2)], index=[10, 20])
    >>> ps.DatetimeIndex(s)
    DatetimeIndex(['2021-03-01', '2021-03-02'], dtype='datetime64[ns]', freq=None)
    

From an Index:
    
    
    >>> idx = ps.DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'])
    >>> ps.DatetimeIndex(idx)
    DatetimeIndex(['1970-01-01', '1970-01-01', '1970-01-01'], dtype='datetime64[ns]', freq=None)
    

Methods

`all`(*args,Â **kwargs) | Return whether all elements are True.  
---|---  
`any`([axis]) | Return whether any element is True.  
`append`(other) | Append a collection of Index options together.  
`argmax`() | Return a maximum argument indexer.  
`argmin`() | Return a minimum argument indexer.  
`asof`(label) | Return the label from the index, or, if not present, the previous one.  
`astype`(dtype) | Cast a pandas-on-Spark object to a specified dtype `dtype`.  
[`ceil`](pyspark.pandas.DatetimeIndex.ceil.html#pyspark.pandas.DatetimeIndex.ceil "pyspark.pandas.DatetimeIndex.ceil")(freq,Â *args,Â **kwargs) | Perform ceil operation on the data to the specified freq.  
`copy`([name,Â deep]) | Make a copy of this object.  
[`day_name`](pyspark.pandas.DatetimeIndex.day_name.html#pyspark.pandas.DatetimeIndex.day_name "pyspark.pandas.DatetimeIndex.day_name")([locale]) | Return the day names of the series with specified locale.  
`delete`(loc) | Make new Index with passed location(-s) deleted.  
`difference`(other[,Â sort]) | Return a new Index with elements from the index that are not in other.  
`drop`(labels) | Make new Index with passed list of labels deleted.  
`drop_duplicates`([keep]) | Return Index with duplicate values removed.  
`droplevel`(level) | Return index with requested level(s) removed.  
`dropna`([how]) | Return Index or MultiIndex without NA/NaN values  
`equals`(other) | Determine if two Index objects contain the same elements.  
`factorize`([sort,Â use_na_sentinel]) | Encode the object as an enumerated type or categorical variable.  
`fillna`(value) | Fill NA/NaN values with the specified value.  
[`floor`](pyspark.pandas.DatetimeIndex.floor.html#pyspark.pandas.DatetimeIndex.floor "pyspark.pandas.DatetimeIndex.floor")(freq,Â *args,Â **kwargs) | Perform floor operation on the data to the specified freq.  
`get_level_values`(level) | Return Index if a valid level is given.  
`holds_integer`() | Whether the type is an integer type.  
`identical`(other) | Similar to equals, but check that other comparable attributes are also equal.  
[`indexer_at_time`](pyspark.pandas.DatetimeIndex.indexer_at_time.html#pyspark.pandas.DatetimeIndex.indexer_at_time "pyspark.pandas.DatetimeIndex.indexer_at_time")(time[,Â asof]) | Return index locations of values at particular time of day (example: 9:30AM).  
[`indexer_between_time`](pyspark.pandas.DatetimeIndex.indexer_between_time.html#pyspark.pandas.DatetimeIndex.indexer_between_time "pyspark.pandas.DatetimeIndex.indexer_between_time")(start_time,Â end_time[,Â ...]) | Return index locations of values between particular times of day (example: 9:00-9:30AM).  
`insert`(loc,Â item) | Make new Index inserting new item at location.  
`intersection`(other) | Form the intersection of two Index objects.  
`is_boolean`() | Return if the current index type is a boolean type.  
`is_categorical`() | Return if the current index type is a categorical type.  
`is_floating`() | Return if the current index type is a floating type.  
`is_integer`() | Return if the current index type is an integer type.  
`is_interval`() | Return if the current index type is an interval type.  
`is_numeric`() | Return if the current index type is a numeric type.  
`is_object`() | Return if the current index type is an object type.  
`isin`(values) | Check whether values are contained in Series or Index.  
`isna`() | Detect existing (non-missing) values.  
`isnull`() | Detect existing (non-missing) values.  
[`isocalendar`](pyspark.pandas.DatetimeIndex.isocalendar.html#pyspark.pandas.DatetimeIndex.isocalendar "pyspark.pandas.DatetimeIndex.isocalendar")() | Calculate year, week, and day according to the ISO 8601 standard.  
`item`() | Return the first element of the underlying data as a python scalar.  
`map`(mapper[,Â na_action]) | Map values using input correspondence (a dict, Series, or function).  
`max`() | Return the maximum value of the Index.  
`min`() | Return the minimum value of the Index.  
[`month_name`](pyspark.pandas.DatetimeIndex.month_name.html#pyspark.pandas.DatetimeIndex.month_name "pyspark.pandas.DatetimeIndex.month_name")([locale]) | Return the month names of the DatetimeIndex with specified locale.  
[`normalize`](pyspark.pandas.DatetimeIndex.normalize.html#pyspark.pandas.DatetimeIndex.normalize "pyspark.pandas.DatetimeIndex.normalize")() | Convert times to midnight.  
`notna`() | Detect existing (non-missing) values.  
`notnull`() | Detect existing (non-missing) values.  
`nunique`([dropna,Â approx,Â rsd]) | Return number of unique elements in the object.  
`rename`(name[,Â inplace]) | Alter Index or MultiIndex name.  
`repeat`(repeats) | Repeat elements of a Index/MultiIndex.  
[`round`](pyspark.pandas.DatetimeIndex.round.html#pyspark.pandas.DatetimeIndex.round "pyspark.pandas.DatetimeIndex.round")(freq,Â *args,Â **kwargs) | Perform round operation on the data to the specified freq.  
`set_names`(names[,Â level,Â inplace]) | Set Index or MultiIndex name.  
`shift`([periods,Â fill_value]) | Shift Series/Index by desired number of periods.  
`sort`(*args,Â **kwargs) | Use sort_values instead.  
`sort_values`([return_indexer,Â ascending]) | Return a sorted copy of the index, and optionally return the indices that sorted the index itself.  
[`strftime`](pyspark.pandas.DatetimeIndex.strftime.html#pyspark.pandas.DatetimeIndex.strftime "pyspark.pandas.DatetimeIndex.strftime")(date_format) | Convert to a string Index using specified date_format.  
`symmetric_difference`(other[,Â result_name,Â sort]) | Compute the symmetric difference of two Index objects.  
`take`(indices) | Return the elements in the given _positional_ indices along an axis.  
`to_frame`([index,Â name]) | Create a DataFrame with a column containing the Index.  
`to_list`() | Return a list of the values.  
`to_numpy`([dtype,Â copy]) | A NumPy ndarray representing the values in this Index or MultiIndex.  
`to_pandas`() | Return a pandas Index.  
`to_series`([name]) | Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.  
`tolist`() | Return a list of the values.  
`transpose`() | Return the transpose, For index, It will be index itself.  
`union`(other[,Â sort]) | Form the union of two Index objects.  
`unique`([level]) | Return unique values in the index.  
`value_counts`([normalize,Â sort,Â ascending,Â ...]) | Return a Series containing counts of unique values.  
`view`() | this is defined as a copy with the same identity  
  
Attributes

`T` | Return the transpose, For index, It will be index itself.  
---|---  
[`day`](pyspark.pandas.DatetimeIndex.day.html#pyspark.pandas.DatetimeIndex.day "pyspark.pandas.DatetimeIndex.day") | The days of the datetime.  
[`day_of_week`](pyspark.pandas.DatetimeIndex.day_of_week.html#pyspark.pandas.DatetimeIndex.day_of_week "pyspark.pandas.DatetimeIndex.day_of_week") | The day of the week with Monday=0, Sunday=6.  
[`day_of_year`](pyspark.pandas.DatetimeIndex.day_of_year.html#pyspark.pandas.DatetimeIndex.day_of_year "pyspark.pandas.DatetimeIndex.day_of_year") | The ordinal day of the year.  
[`dayofweek`](pyspark.pandas.DatetimeIndex.dayofweek.html#pyspark.pandas.DatetimeIndex.dayofweek "pyspark.pandas.DatetimeIndex.dayofweek") | The day of the week with Monday=0, Sunday=6.  
[`dayofyear`](pyspark.pandas.DatetimeIndex.dayofyear.html#pyspark.pandas.DatetimeIndex.dayofyear "pyspark.pandas.DatetimeIndex.dayofyear") | The ordinal day of the year.  
[`days_in_month`](pyspark.pandas.DatetimeIndex.days_in_month.html#pyspark.pandas.DatetimeIndex.days_in_month "pyspark.pandas.DatetimeIndex.days_in_month") | The number of days in the month.  
[`daysinmonth`](pyspark.pandas.DatetimeIndex.daysinmonth.html#pyspark.pandas.DatetimeIndex.daysinmonth "pyspark.pandas.DatetimeIndex.daysinmonth") | The number of days in the month.  
`dtype` | Return the dtype object of the underlying data.  
`empty` | Returns true if the current object is empty.  
`has_duplicates` | If index has duplicates, return True, otherwise False.  
`hasnans` | Return True if it has any missing values.  
[`hour`](pyspark.pandas.DatetimeIndex.hour.html#pyspark.pandas.DatetimeIndex.hour "pyspark.pandas.DatetimeIndex.hour") | The hours of the datetime.  
`inferred_type` | Return a string of the type inferred from the values.  
[`is_leap_year`](pyspark.pandas.DatetimeIndex.is_leap_year.html#pyspark.pandas.DatetimeIndex.is_leap_year "pyspark.pandas.DatetimeIndex.is_leap_year") | Boolean indicator if the date belongs to a leap year.  
`is_monotonic_decreasing` | Return boolean if values in the object are monotonically decreasing.  
`is_monotonic_increasing` | Return boolean if values in the object are monotonically increasing.  
[`is_month_end`](pyspark.pandas.DatetimeIndex.is_month_end.html#pyspark.pandas.DatetimeIndex.is_month_end "pyspark.pandas.DatetimeIndex.is_month_end") | Indicates whether the date is the last day of the month.  
[`is_month_start`](pyspark.pandas.DatetimeIndex.is_month_start.html#pyspark.pandas.DatetimeIndex.is_month_start "pyspark.pandas.DatetimeIndex.is_month_start") | Indicates whether the date is the first day of the month.  
[`is_quarter_end`](pyspark.pandas.DatetimeIndex.is_quarter_end.html#pyspark.pandas.DatetimeIndex.is_quarter_end "pyspark.pandas.DatetimeIndex.is_quarter_end") | Indicator for whether the date is the last day of a quarter.  
[`is_quarter_start`](pyspark.pandas.DatetimeIndex.is_quarter_start.html#pyspark.pandas.DatetimeIndex.is_quarter_start "pyspark.pandas.DatetimeIndex.is_quarter_start") | Indicator for whether the date is the first day of a quarter.  
`is_unique` | Return if the index has unique values.  
[`is_year_end`](pyspark.pandas.DatetimeIndex.is_year_end.html#pyspark.pandas.DatetimeIndex.is_year_end "pyspark.pandas.DatetimeIndex.is_year_end") | Indicate whether the date is the last day of the year.  
[`is_year_start`](pyspark.pandas.DatetimeIndex.is_year_start.html#pyspark.pandas.DatetimeIndex.is_year_start "pyspark.pandas.DatetimeIndex.is_year_start") | Indicate whether the date is the first day of a year.  
[`microsecond`](pyspark.pandas.DatetimeIndex.microsecond.html#pyspark.pandas.DatetimeIndex.microsecond "pyspark.pandas.DatetimeIndex.microsecond") | The microseconds of the datetime.  
[`minute`](pyspark.pandas.DatetimeIndex.minute.html#pyspark.pandas.DatetimeIndex.minute "pyspark.pandas.DatetimeIndex.minute") | The minutes of the datetime.  
[`month`](pyspark.pandas.DatetimeIndex.month.html#pyspark.pandas.DatetimeIndex.month "pyspark.pandas.DatetimeIndex.month") | The month of the timestamp as January = 1 December = 12.  
`name` | Return name of the Index.  
`names` | Return names of the Index.  
`ndim` | Return an int representing the number of array dimensions.  
`nlevels` | Number of levels in Index & MultiIndex.  
[`quarter`](pyspark.pandas.DatetimeIndex.quarter.html#pyspark.pandas.DatetimeIndex.quarter "pyspark.pandas.DatetimeIndex.quarter") | The quarter of the date.  
[`second`](pyspark.pandas.DatetimeIndex.second.html#pyspark.pandas.DatetimeIndex.second "pyspark.pandas.DatetimeIndex.second") | The seconds of the datetime.  
`shape` | Return a tuple of the shape of the underlying data.  
`size` | Return an int representing the number of elements in this object.  
`values` | Return an array representing the data in the Index.  
[`weekday`](pyspark.pandas.DatetimeIndex.weekday.html#pyspark.pandas.DatetimeIndex.weekday "pyspark.pandas.DatetimeIndex.weekday") | The day of the week with Monday=0, Sunday=6.  
[`year`](pyspark.pandas.DatetimeIndex.year.html#pyspark.pandas.DatetimeIndex.year "pyspark.pandas.DatetimeIndex.year") | The year of the datetime.  
  
[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.rst.txt)


---

## 🔹 141. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.year.html

# pyspark.pandas.DatetimeIndex.year#

_property _DatetimeIndex.year#
    

The year of the datetime.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.year.rst.txt)


---

## 🔹 142. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.month.html

# pyspark.pandas.DatetimeIndex.month#

_property _DatetimeIndex.month#
    

The month of the timestamp as January = 1 December = 12.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.month.rst.txt)


---

## 🔹 143. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day.html

# pyspark.pandas.DatetimeIndex.day#

_property _DatetimeIndex.day#
    

The days of the datetime.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day.rst.txt)


---

## 🔹 144. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.hour.html

# pyspark.pandas.DatetimeIndex.hour#

_property _DatetimeIndex.hour#
    

The hours of the datetime.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.hour.rst.txt)


---

## 🔹 145. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.minute.html

# pyspark.pandas.DatetimeIndex.minute#

_property _DatetimeIndex.minute#
    

The minutes of the datetime.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.minute.rst.txt)


---

## 🔹 146. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.second.html

# pyspark.pandas.DatetimeIndex.second#

_property _DatetimeIndex.second#
    

The seconds of the datetime.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.second.rst.txt)


---

## 🔹 147. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.microsecond.html

# pyspark.pandas.DatetimeIndex.microsecond#

_property _DatetimeIndex.microsecond#
    

The microseconds of the datetime.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.microsecond.rst.txt)


---

## 🔹 148. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.isocalendar.html

# pyspark.pandas.DatetimeIndex.isocalendar#

DatetimeIndex.isocalendar()[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.isocalendar)#
    

Calculate year, week, and day according to the ISO 8601 standard.

> New in version 4.0.0.

Returns
    

DataFrame
    

With columns year, week and day.

Note

Returns have int64 type instead of UInt32 as is in pandas due to UInt32 is not supported by spark

Examples
    
    
    >>> psidxs = ps.from_pandas(
    ...     pd.DatetimeIndex(["2019-12-29", "2019-12-30", "2019-12-31", "2020-01-01"])
    ... )
    >>> psidxs.isocalendar()
                year  week  day
    2019-12-29  2019    52    7
    2019-12-30  2020     1    1
    2019-12-31  2020     1    2
    2020-01-01  2020     1    3
    
    
    
    >>> psidxs.isocalendar().week
    2019-12-29    52
    2019-12-30     1
    2019-12-31     1
    2020-01-01     1
    Name: week, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.isocalendar.rst.txt)


---

## 🔹 149. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.dayofweek.html

# pyspark.pandas.DatetimeIndex.dayofweek#

_property _DatetimeIndex.dayofweek#
    

The day of the week with Monday=0, Sunday=6. Return the day of the week. It is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6. This method is available on both Series with datetime values (using the dt accessor) or DatetimeIndex.

Returns
    

Series or Index
    

Containing integers indicating the day number.

See also

[`Series.dt.dayofweek`](pyspark.pandas.Series.dt.dayofweek.html#pyspark.pandas.Series.dt.dayofweek "pyspark.pandas.Series.dt.dayofweek")
    

Alias.

[`Series.dt.weekday`](pyspark.pandas.Series.dt.weekday.html#pyspark.pandas.Series.dt.weekday "pyspark.pandas.Series.dt.weekday")
    

Alias.

[`Series.dt.day_name`](pyspark.pandas.Series.dt.day_name.html#pyspark.pandas.Series.dt.day_name "pyspark.pandas.Series.dt.day_name")
    

Returns the name of the day of the week.

Examples
    
    
    >>> idx = ps.date_range('2016-12-31', '2017-01-08', freq='D')  
    >>> idx.dayofweek  
    Index([5, 6, 0, 1, 2, 3, 4, 5, 6], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.dayofweek.rst.txt)


---

## 🔹 150. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day_of_week.html

# pyspark.pandas.DatetimeIndex.day_of_week#

_property _DatetimeIndex.day_of_week#
    

The day of the week with Monday=0, Sunday=6. Return the day of the week. It is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6. This method is available on both Series with datetime values (using the dt accessor) or DatetimeIndex.

Returns
    

Series or Index
    

Containing integers indicating the day number.

See also

[`Series.dt.dayofweek`](pyspark.pandas.Series.dt.dayofweek.html#pyspark.pandas.Series.dt.dayofweek "pyspark.pandas.Series.dt.dayofweek")
    

Alias.

[`Series.dt.weekday`](pyspark.pandas.Series.dt.weekday.html#pyspark.pandas.Series.dt.weekday "pyspark.pandas.Series.dt.weekday")
    

Alias.

[`Series.dt.day_name`](pyspark.pandas.Series.dt.day_name.html#pyspark.pandas.Series.dt.day_name "pyspark.pandas.Series.dt.day_name")
    

Returns the name of the day of the week.

Examples
    
    
    >>> idx = ps.date_range('2016-12-31', '2017-01-08', freq='D')  
    >>> idx.dayofweek  
    Index([5, 6, 0, 1, 2, 3, 4, 5, 6], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day_of_week.rst.txt)


---

## 🔹 151. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.weekday.html

# pyspark.pandas.DatetimeIndex.weekday#

_property _DatetimeIndex.weekday#
    

The day of the week with Monday=0, Sunday=6. Return the day of the week. It is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6. This method is available on both Series with datetime values (using the dt accessor) or DatetimeIndex.

Returns
    

Series or Index
    

Containing integers indicating the day number.

See also

[`Series.dt.dayofweek`](pyspark.pandas.Series.dt.dayofweek.html#pyspark.pandas.Series.dt.dayofweek "pyspark.pandas.Series.dt.dayofweek")
    

Alias.

[`Series.dt.weekday`](pyspark.pandas.Series.dt.weekday.html#pyspark.pandas.Series.dt.weekday "pyspark.pandas.Series.dt.weekday")
    

Alias.

[`Series.dt.day_name`](pyspark.pandas.Series.dt.day_name.html#pyspark.pandas.Series.dt.day_name "pyspark.pandas.Series.dt.day_name")
    

Returns the name of the day of the week.

Examples
    
    
    >>> idx = ps.date_range('2016-12-31', '2017-01-08', freq='D')  
    >>> idx.dayofweek  
    Index([5, 6, 0, 1, 2, 3, 4, 5, 6], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.weekday.rst.txt)


---

## 🔹 152. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.dayofyear.html

# pyspark.pandas.DatetimeIndex.dayofyear#

_property _DatetimeIndex.dayofyear#
    

The ordinal day of the year.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.dayofyear.rst.txt)


---

## 🔹 153. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day_of_year.html

# pyspark.pandas.DatetimeIndex.day_of_year#

_property _DatetimeIndex.day_of_year#
    

The ordinal day of the year.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day_of_year.rst.txt)


---

## 🔹 154. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.quarter.html

# pyspark.pandas.DatetimeIndex.quarter#

_property _DatetimeIndex.quarter#
    

The quarter of the date.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.quarter.rst.txt)


---

## 🔹 155. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_month_start.html

# pyspark.pandas.DatetimeIndex.is_month_start#

_property _DatetimeIndex.is_month_start#
    

Indicates whether the date is the first day of the month.

Returns
    

Index
    

Returns a Index with boolean values

See also

[`is_month_end`](pyspark.pandas.DatetimeIndex.is_month_end.html#pyspark.pandas.DatetimeIndex.is_month_end "pyspark.pandas.DatetimeIndex.is_month_end")
    

Return a boolean indicating whether the date is the last day of the month.

Examples
    
    
    >>> idx = ps.date_range("2018-02-27", periods=3)  
    >>> idx.is_month_start  
    Index([False, False, True], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_month_start.rst.txt)


---

## 🔹 156. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_month_end.html

# pyspark.pandas.DatetimeIndex.is_month_end#

_property _DatetimeIndex.is_month_end#
    

Indicates whether the date is the last day of the month.

Returns
    

Index
    

Returns an Index with boolean values.

See also

[`is_month_start`](pyspark.pandas.DatetimeIndex.is_month_start.html#pyspark.pandas.DatetimeIndex.is_month_start "pyspark.pandas.DatetimeIndex.is_month_start")
    

Return a boolean indicating whether the date is the first day of the month.

Examples
    
    
    >>> idx = ps.date_range("2018-02-27", periods=3)  
    >>> idx.is_month_end  
    Index([False, True, False], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_month_end.rst.txt)


---

## 🔹 157. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_quarter_start.html

# pyspark.pandas.DatetimeIndex.is_quarter_start#

_property _DatetimeIndex.is_quarter_start#
    

Indicator for whether the date is the first day of a quarter.

Returns
    

**is_quarter_start** Index
    

Returns an Index with boolean values.

See also

[`quarter`](pyspark.pandas.DatetimeIndex.quarter.html#pyspark.pandas.DatetimeIndex.quarter "pyspark.pandas.DatetimeIndex.quarter")
    

Return the quarter of the date.

[`is_quarter_end`](pyspark.pandas.DatetimeIndex.is_quarter_end.html#pyspark.pandas.DatetimeIndex.is_quarter_end "pyspark.pandas.DatetimeIndex.is_quarter_end")
    

Similar property for indicating the quarter start.

Examples
    
    
    >>> idx = ps.date_range('2017-03-30', periods=4)  
    >>> idx.is_quarter_start  
    Index([False, False, True, False], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_quarter_start.rst.txt)


---

## 🔹 158. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_quarter_end.html

# pyspark.pandas.DatetimeIndex.is_quarter_end#

_property _DatetimeIndex.is_quarter_end#
    

Indicator for whether the date is the last day of a quarter.

Returns
    

**is_quarter_end** Index
    

Returns an Index with boolean values.

See also

[`quarter`](pyspark.pandas.DatetimeIndex.quarter.html#pyspark.pandas.DatetimeIndex.quarter "pyspark.pandas.DatetimeIndex.quarter")
    

Return the quarter of the date.

[`is_quarter_start`](pyspark.pandas.DatetimeIndex.is_quarter_start.html#pyspark.pandas.DatetimeIndex.is_quarter_start "pyspark.pandas.DatetimeIndex.is_quarter_start")
    

Similar property indicating the quarter start.

Examples
    
    
    >>> idx = ps.date_range('2017-03-30', periods=4)  
    >>> idx.is_quarter_end  
    Index([False, True, False, False], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_quarter_end.rst.txt)


---

## 🔹 159. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_year_start.html

# pyspark.pandas.DatetimeIndex.is_year_start#

_property _DatetimeIndex.is_year_start#
    

Indicate whether the date is the first day of a year.

Returns
    

Index
    

Returns an Index with boolean values.

See also

[`is_year_end`](pyspark.pandas.DatetimeIndex.is_year_end.html#pyspark.pandas.DatetimeIndex.is_year_end "pyspark.pandas.DatetimeIndex.is_year_end")
    

Similar property indicating the last day of the year.

Examples
    
    
    >>> idx = ps.date_range("2017-12-30", periods=3)  
    >>> idx.is_year_start  
    Index([False, False, True], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_year_start.rst.txt)


---

## 🔹 160. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_year_end.html

# pyspark.pandas.DatetimeIndex.is_year_end#

_property _DatetimeIndex.is_year_end#
    

Indicate whether the date is the last day of the year.

Returns
    

Index
    

Returns an Index with boolean values.

See also

[`is_year_start`](pyspark.pandas.DatetimeIndex.is_year_start.html#pyspark.pandas.DatetimeIndex.is_year_start "pyspark.pandas.DatetimeIndex.is_year_start")
    

Similar property indicating the start of the year.

Examples
    
    
    >>> idx = ps.date_range("2017-12-30", periods=3)  
    >>> idx.is_year_end  
    Index([False, True, False], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_year_end.rst.txt)


---

## 🔹 161. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_leap_year.html

# pyspark.pandas.DatetimeIndex.is_leap_year#

_property _DatetimeIndex.is_leap_year#
    

Boolean indicator if the date belongs to a leap year.

A leap year is a year, which has 366 days (instead of 365) including 29th of February as an intercalary day. Leap years are years which are multiples of four with the exception of years divisible by 100 but not by 400.

Returns
    

Index
    

Booleans indicating if dates belong to a leap year.

Examples
    
    
    >>> idx = ps.date_range("2012-01-01", "2015-01-01", freq="Y")  
    >>> idx.is_leap_year  
    Index([True, False, False], dtype='bool')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.is_leap_year.rst.txt)


---

## 🔹 162. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.daysinmonth.html

# pyspark.pandas.DatetimeIndex.daysinmonth#

_property _DatetimeIndex.daysinmonth#
    

The number of days in the month.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.daysinmonth.rst.txt)


---

## 🔹 163. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.days_in_month.html

# pyspark.pandas.DatetimeIndex.days_in_month#

_property _DatetimeIndex.days_in_month#
    

The number of days in the month.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.days_in_month.rst.txt)


---

## 🔹 164. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.indexer_between_time.html

# pyspark.pandas.DatetimeIndex.indexer_between_time#

DatetimeIndex.indexer_between_time(_start_time_ , _end_time_ , _include_start =True_, _include_end =True_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.indexer_between_time)#
    

Return index locations of values between particular times of day (example: 9:00-9:30AM).

Parameters
    

**start_time, end_time** datetime.time, str
    

Time passed either as object (datetime.time) or as string in appropriate format (â%H:%Mâ, â%H%Mâ, â%I:%M%pâ, â%I%M%pâ, â%H:%M:%Sâ, â%H%M%Sâ, â%I:%M:%S%pâ,â%I%M%S%pâ).

**include_start** bool, default True
    
**include_end** bool, default True
    
Returns
    

**values_between_time** Index of integers
    

Examples
    
    
    >>> psidx = ps.date_range("2000-01-01", periods=3, freq="T")
    >>> psidx
    DatetimeIndex(['2000-01-01 00:00:00', '2000-01-01 00:01:00',
                   '2000-01-01 00:02:00'],
                  dtype='datetime64[ns]', freq=None)
    
    
    
    >>> psidx.indexer_between_time("00:01", "00:02").sort_values()
    Index([1, 2], dtype='int64')
    
    
    
    >>> psidx.indexer_between_time("00:01", "00:02", include_end=False)
    Index([1], dtype='int64')
    
    
    
    >>> psidx.indexer_between_time("00:01", "00:02", include_start=False)
    Index([2], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.indexer_between_time.rst.txt)


---

## 🔹 165. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.indexer_at_time.html

# pyspark.pandas.DatetimeIndex.indexer_at_time#

DatetimeIndex.indexer_at_time(_time_ , _asof =False_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.indexer_at_time)#
    

Return index locations of values at particular time of day (example: 9:30AM).

Parameters
    

**time** datetime.time or str
    

Time passed in either as object (datetime.time) or as string in appropriate format (â%H:%Mâ, â%H%Mâ, â%I:%M%pâ, â%I%M%pâ, â%H:%M:%Sâ, â%H%M%Sâ, â%I:%M:%S%pâ, â%I%M%S%pâ).

Returns
    

**values_at_time** Index of integers
    

Examples
    
    
    >>> psidx = ps.date_range("2000-01-01", periods=3, freq="T")  
    >>> psidx  
    DatetimeIndex(['2000-01-01 00:00:00', '2000-01-01 00:01:00',
                   '2000-01-01 00:02:00'],
                  dtype='datetime64[ns]', freq=None)
    
    
    
    >>> psidx.indexer_at_time("00:00")  
    Index([0], dtype='int64')
    
    
    
    >>> psidx.indexer_at_time("00:01")  
    Index([1], dtype='int64')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.indexer_at_time.rst.txt)


---

## 🔹 166. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.normalize.html

# pyspark.pandas.DatetimeIndex.normalize#

DatetimeIndex.normalize()[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.normalize)#
    

Convert times to midnight.

The time component of the date-time is converted to midnight i.e. 00:00:00. This is useful in cases, when the time does not matter. Length is unaltered. The time zones are unaffected.

This method is available on Series with datetime values under the `.dt` accessor.

Returns
    

DatetimeIndex
    

The same type as the original data.

See also

[`floor`](pyspark.pandas.DatetimeIndex.floor.html#pyspark.pandas.DatetimeIndex.floor "pyspark.pandas.DatetimeIndex.floor")
    

Floor the series to the specified freq.

[`ceil`](pyspark.pandas.DatetimeIndex.ceil.html#pyspark.pandas.DatetimeIndex.ceil "pyspark.pandas.DatetimeIndex.ceil")
    

Ceil the series to the specified freq.

[`round`](pyspark.pandas.DatetimeIndex.round.html#pyspark.pandas.DatetimeIndex.round "pyspark.pandas.DatetimeIndex.round")
    

Round the series to the specified freq.

Examples
    
    
    >>> idx = ps.date_range(start='2014-08-01 10:00', freq='H', periods=3)  
    >>> idx.normalize()  
    DatetimeIndex(['2014-08-01', '2014-08-01', '2014-08-01'], dtype='datetime64[ns]', freq=None)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.normalize.rst.txt)


---

## 🔹 167. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.strftime.html

# pyspark.pandas.DatetimeIndex.strftime#

DatetimeIndex.strftime(_date_format_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.strftime)#
    

Convert to a string Index using specified date_format.

Return an Index of formatted strings specified by date_format, which supports the same string format as the python standard library. Details of the string format can be found in the python string format doc.

Parameters
    

**date_format** str
    

Date format string (example: â%%Y-%%m-%%dâ).

Returns
    

Index
    

Index of formatted strings.

See also

[`normalize`](pyspark.pandas.DatetimeIndex.normalize.html#pyspark.pandas.DatetimeIndex.normalize "pyspark.pandas.DatetimeIndex.normalize")
    

Return series with times to midnight.

[`round`](pyspark.pandas.DatetimeIndex.round.html#pyspark.pandas.DatetimeIndex.round "pyspark.pandas.DatetimeIndex.round")
    

Round the series to the specified freq.

[`floor`](pyspark.pandas.DatetimeIndex.floor.html#pyspark.pandas.DatetimeIndex.floor "pyspark.pandas.DatetimeIndex.floor")
    

Floor the series to the specified freq.

Examples
    
    
    >>> idx = ps.date_range(pd.Timestamp("2018-03-10 09:00"), periods=3, freq='s')
    ... 
    >>> idx.strftime('%B %d, %Y, %r')  
    Index(['March 10, 2018, 09:00:00 AM', 'March 10, 2018, 09:00:01 AM',
           'March 10, 2018, 09:00:02 AM'],
          dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.strftime.rst.txt)


---

## 🔹 168. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.round.html

# pyspark.pandas.DatetimeIndex.round#

DatetimeIndex.round(_freq_ , _* args_, _** kwargs_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.round)#
    

Perform round operation on the data to the specified freq.

Parameters
    

**freq** str or Offset
    

The frequency level to round the index to. Must be a fixed frequency like âSâ (second) not âMEâ (month end).

Returns
    

DatetimeIndex
    
Raises
    

ValueError if the freq cannot be converted.
    

Examples
    
    
    >>> rng = ps.date_range('1/1/2018 11:59:00', periods=3, freq='min')  
    >>> rng.round("H")  
    DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',
                   '2018-01-01 12:00:00'],
                  dtype='datetime64[ns]', freq=None)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.round.rst.txt)


---

## 🔹 169. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.floor.html

# pyspark.pandas.DatetimeIndex.floor#

DatetimeIndex.floor(_freq_ , _* args_, _** kwargs_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.floor)#
    

Perform floor operation on the data to the specified freq.

Parameters
    

**freq** str or Offset
    

The frequency level to floor the index to. Must be a fixed frequency like âSâ (second) not âMEâ (month end).

Returns
    

DatetimeIndex
    
Raises
    

ValueError if the freq cannot be converted.
    

Examples
    
    
    >>> rng = ps.date_range('1/1/2018 11:59:00', periods=3, freq='min')  
    >>> rng.floor("H")  
    DatetimeIndex(['2018-01-01 11:00:00', '2018-01-01 12:00:00',
                   '2018-01-01 12:00:00'],
                  dtype='datetime64[ns]', freq=None)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.floor.rst.txt)


---

## 🔹 170. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.ceil.html

# pyspark.pandas.DatetimeIndex.ceil#

DatetimeIndex.ceil(_freq_ , _* args_, _** kwargs_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.ceil)#
    

Perform ceil operation on the data to the specified freq.

Parameters
    

**freq** str or Offset
    

The frequency level to ceil the index to. Must be a fixed frequency like âSâ (second) not âMEâ (month end).

Returns
    

DatetimeIndex
    
Raises
    

ValueError if the freq cannot be converted.
    

Examples
    
    
    >>> rng = ps.date_range('1/1/2018 11:59:00', periods=3, freq='min')  
    >>> rng.ceil('H')  
    DatetimeIndex(['2018-01-01 12:00:00', '2018-01-01 12:00:00',
                   '2018-01-01 13:00:00'],
                  dtype='datetime64[ns]', freq=None)
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.ceil.rst.txt)


---

## 🔹 171. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.month_name.html

# pyspark.pandas.DatetimeIndex.month_name#

DatetimeIndex.month_name(_locale =None_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.month_name)#
    

Return the month names of the DatetimeIndex with specified locale.

Parameters
    

**locale** str, optional
    

Locale determining the language in which to return the month name. Default is English locale.

Returns
    

Index
    

Index of month names.

Examples
    
    
    >>> idx = ps.date_range(start='2018-01', freq='ME', periods=3)  
    >>> idx.month_name()  
    Index(['January', 'February', 'March'], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.month_name.rst.txt)


---

## 🔹 172. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day_name.html

# pyspark.pandas.DatetimeIndex.day_name#

DatetimeIndex.day_name(_locale =None_)[[source]](../../../_modules/pyspark/pandas/indexes/datetimes.html#DatetimeIndex.day_name)#
    

Return the day names of the series with specified locale.

Parameters
    

**locale** str, optional
    

Locale determining the language in which to return the day name. Default is English locale.

Returns
    

Index
    

Index of day names.

Examples
    
    
    >>> idx = ps.date_range(start='2018-01-01', freq='D', periods=3)  
    >>> idx.day_name()  
    Index(['Monday', 'Tuesday', 'Wednesday'], dtype='object')
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.DatetimeIndex.day_name.rst.txt)


---

## 🔹 173. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.html

# pyspark.pandas.TimedeltaIndex#

_class _pyspark.pandas.TimedeltaIndex(_data=None_ , _unit=None_ , _freq= <no value>_, _closed=None_ , _dtype=None_ , _copy=False_ , _name=None_)[[source]](../../../_modules/pyspark/pandas/indexes/timedelta.html#TimedeltaIndex)#
    

Immutable ndarray-like of timedelta64 data, represented internally as int64, and which can be boxed to timedelta objects.

Parameters
    

**data** array-like (1-dimensional), optional
    

Optional timedelta-like data to construct index with.

**unit** unit of the arg (D,h,m,s,ms,us,ns) denote the unit, optional
    

Which is an integer/float number.

**freq** str or pandas offset object, optional
    

One of pandas date offset strings or corresponding objects. The string âinferâ can be passed in order to set the frequency of the index as the inferred frequency upon creation.

**copy** bool
    

Make a copy of input ndarray.

**name** object
    

Name to be stored in the index.

See also

[`Index`](pyspark.pandas.Index.html#pyspark.pandas.Index "pyspark.pandas.Index")
    

The base pandas Index type.

Examples
    
    
    >>> from datetime import timedelta
    >>> ps.TimedeltaIndex([timedelta(1), timedelta(microseconds=2)])
    ... 
    TimedeltaIndex(['1 days 00:00:00', '0 days 00:00:00.000002'],
    dtype='timedelta64[ns]', freq=None)
    

From an Series:
    
    
    >>> s = ps.Series([timedelta(1), timedelta(microseconds=2)], index=[10, 20])
    >>> ps.TimedeltaIndex(s)
    ... 
    TimedeltaIndex(['1 days 00:00:00', '0 days 00:00:00.000002'],
    dtype='timedelta64[ns]', freq=None)
    

From an Index:
    
    
    >>> idx = ps.TimedeltaIndex([timedelta(1), timedelta(microseconds=2)])
    >>> ps.TimedeltaIndex(idx)
    ... 
    TimedeltaIndex(['1 days 00:00:00', '0 days 00:00:00.000002'],
    dtype='timedelta64[ns]', freq=None)
    

Methods

`all`(*args,Â **kwargs) | Return whether all elements are True.  
---|---  
`any`([axis]) | Return whether any element is True.  
`append`(other) | Append a collection of Index options together.  
`argmax`() | Return a maximum argument indexer.  
`argmin`() | Return a minimum argument indexer.  
`asof`(label) | Return the label from the index, or, if not present, the previous one.  
`astype`(dtype) | Cast a pandas-on-Spark object to a specified dtype `dtype`.  
`copy`([name,Â deep]) | Make a copy of this object.  
`delete`(loc) | Make new Index with passed location(-s) deleted.  
`difference`(other[,Â sort]) | Return a new Index with elements from the index that are not in other.  
`drop`(labels) | Make new Index with passed list of labels deleted.  
`drop_duplicates`([keep]) | Return Index with duplicate values removed.  
`droplevel`(level) | Return index with requested level(s) removed.  
`dropna`([how]) | Return Index or MultiIndex without NA/NaN values  
`equals`(other) | Determine if two Index objects contain the same elements.  
`factorize`([sort,Â use_na_sentinel]) | Encode the object as an enumerated type or categorical variable.  
`fillna`(value) | Fill NA/NaN values with the specified value.  
`get_level_values`(level) | Return Index if a valid level is given.  
`holds_integer`() | Whether the type is an integer type.  
`identical`(other) | Similar to equals, but check that other comparable attributes are also equal.  
`insert`(loc,Â item) | Make new Index inserting new item at location.  
`intersection`(other) | Form the intersection of two Index objects.  
`is_boolean`() | Return if the current index type is a boolean type.  
`is_categorical`() | Return if the current index type is a categorical type.  
`is_floating`() | Return if the current index type is a floating type.  
`is_integer`() | Return if the current index type is an integer type.  
`is_interval`() | Return if the current index type is an interval type.  
`is_numeric`() | Return if the current index type is a numeric type.  
`is_object`() | Return if the current index type is an object type.  
`isin`(values) | Check whether values are contained in Series or Index.  
`isna`() | Detect existing (non-missing) values.  
`isnull`() | Detect existing (non-missing) values.  
`item`() | Return the first element of the underlying data as a python scalar.  
`map`(mapper[,Â na_action]) | Map values using input correspondence (a dict, Series, or function).  
`max`() | Return the maximum value of the Index.  
`min`() | Return the minimum value of the Index.  
`notna`() | Detect existing (non-missing) values.  
`notnull`() | Detect existing (non-missing) values.  
`nunique`([dropna,Â approx,Â rsd]) | Return number of unique elements in the object.  
`rename`(name[,Â inplace]) | Alter Index or MultiIndex name.  
`repeat`(repeats) | Repeat elements of a Index/MultiIndex.  
`set_names`(names[,Â level,Â inplace]) | Set Index or MultiIndex name.  
`shift`([periods,Â fill_value]) | Shift Series/Index by desired number of periods.  
`sort`(*args,Â **kwargs) | Use sort_values instead.  
`sort_values`([return_indexer,Â ascending]) | Return a sorted copy of the index, and optionally return the indices that sorted the index itself.  
`symmetric_difference`(other[,Â result_name,Â sort]) | Compute the symmetric difference of two Index objects.  
`take`(indices) | Return the elements in the given _positional_ indices along an axis.  
`to_frame`([index,Â name]) | Create a DataFrame with a column containing the Index.  
`to_list`() | Return a list of the values.  
`to_numpy`([dtype,Â copy]) | A NumPy ndarray representing the values in this Index or MultiIndex.  
`to_pandas`() | Return a pandas Index.  
`to_series`([name]) | Create a Series with both index and values equal to the index keys useful with map for returning an indexer based on an index.  
`tolist`() | Return a list of the values.  
`transpose`() | Return the transpose, For index, It will be index itself.  
`union`(other[,Â sort]) | Form the union of two Index objects.  
`unique`([level]) | Return unique values in the index.  
`value_counts`([normalize,Â sort,Â ascending,Â ...]) | Return a Series containing counts of unique values.  
`view`() | this is defined as a copy with the same identity  
  
Attributes

`T` | Return the transpose, For index, It will be index itself.  
---|---  
[`days`](pyspark.pandas.TimedeltaIndex.days.html#pyspark.pandas.TimedeltaIndex.days "pyspark.pandas.TimedeltaIndex.days") | Number of days for each element.  
`dtype` | Return the dtype object of the underlying data.  
`empty` | Returns true if the current object is empty.  
`has_duplicates` | If index has duplicates, return True, otherwise False.  
`hasnans` | Return True if it has any missing values.  
`inferred_type` | Return a string of the type inferred from the values.  
`is_monotonic_decreasing` | Return boolean if values in the object are monotonically decreasing.  
`is_monotonic_increasing` | Return boolean if values in the object are monotonically increasing.  
`is_unique` | Return if the index has unique values.  
[`microseconds`](pyspark.pandas.TimedeltaIndex.microseconds.html#pyspark.pandas.TimedeltaIndex.microseconds "pyspark.pandas.TimedeltaIndex.microseconds") | Number of microseconds (>= 0 and less than 1 second) for each element.  
`name` | Return name of the Index.  
`names` | Return names of the Index.  
`ndim` | Return an int representing the number of array dimensions.  
`nlevels` | Number of levels in Index & MultiIndex.  
[`seconds`](pyspark.pandas.TimedeltaIndex.seconds.html#pyspark.pandas.TimedeltaIndex.seconds "pyspark.pandas.TimedeltaIndex.seconds") | Number of seconds (>= 0 and less than 1 day) for each element.  
`shape` | Return a tuple of the shape of the underlying data.  
`size` | Return an int representing the number of elements in this object.  
`values` | Return an array representing the data in the Index.  
  
[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.rst.txt)


---

## 🔹 174. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.days.html

# pyspark.pandas.TimedeltaIndex.days#

_property _TimedeltaIndex.days#
    

Number of days for each element.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.days.rst.txt)


---

## 🔹 175. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.seconds.html

# pyspark.pandas.TimedeltaIndex.seconds#

_property _TimedeltaIndex.seconds#
    

Number of seconds (>= 0 and less than 1 day) for each element.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.seconds.rst.txt)


---

## 🔹 176. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.microseconds.html

# pyspark.pandas.TimedeltaIndex.microseconds#

_property _TimedeltaIndex.microseconds#
    

Number of microseconds (>= 0 and less than 1 second) for each element.

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.TimedeltaIndex.microseconds.rst.txt)
