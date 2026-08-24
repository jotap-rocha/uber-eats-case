# Series — PySpark 4.0.1 documentation
Constructor[#](#constructor "Permalink to this headline")
---------------------------------------------------------



Attributes[#](#attributes "Permalink to this headline")
-------------------------------------------------------


|Series.index  |The index (axis labels) Column of the Series.                    |
|--------------|-----------------------------------------------------------------|
|Series.dtype  |Return the dtype object of the underlying data.                  |
|Series.dtypes |Return the dtype object of the underlying data.                  |
|Series.ndim   |Return an int representing the number of array dimensions.       |
|Series.name   |Return name of the Series.                                       |
|Series.shape  |Return a tuple of the shape of the underlying data.              |
|Series.axes   |Return a list of the row axis labels.                            |
|Series.size   |Return an int representing the number of elements in this object.|
|Series.empty  |Returns true if the current object is empty.                     |
|Series.T      |Return the transpose, which is self.                             |
|Series.hasnans|Return True if it has any missing values.                        |
|Series.values |Return a Numpy representation of the DataFrame or the Series.    |


Conversion[#](#conversion "Permalink to this headline")
-------------------------------------------------------


|Series.astype(dtype)|Cast a pandas-on-Spark object to a specified dtype dtype. |
|--------------------|----------------------------------------------------------|
|Series.copy([deep]) |Make a copy of this object's indices and data.            |
|Series.bool()       |Return the bool of a single element in the current object.|


Indexing, iteration[#](#indexing-iteration "Permalink to this headline")
------------------------------------------------------------------------



* Series.at: Series.iat
  * Access a single value for a row/column label pair.: Access a single value for a row/column pair by integer position.
* Series.at: Series.loc
  * Access a single value for a row/column label pair.: Access a group of rows and columns by label(s) or a boolean Series.
* Series.at: Series.iloc
  * Access a single value for a row/column label pair.: Purely integer-location based indexing for selection by position.
* Series.at: Series.keys()
  * Access a single value for a row/column label pair.: Return alias for index.
* Series.at: Series.pop(item)
  * Access a single value for a row/column label pair.: Return item and drop from series.
* Series.at: Series.items()
  * Access a single value for a row/column label pair.: Lazily iterate over (index, value) tuples.
* Series.at: Series.item()
  * Access a single value for a row/column label pair.: Return the first element of the underlying data as a Python scalar.
* Series.at: Series.xs(key[, level])
  * Access a single value for a row/column label pair.: Return cross-section from the Series.
* Series.at: Series.get(key[, default])
  * Access a single value for a row/column label pair.: Get item from object for given key (DataFrame column, Panel slice, etc.).


Binary operator functions[#](#binary-operator-functions "Permalink to this headline")
-------------------------------------------------------------------------------------



* Series.add(other[, fill_value]): Series.div(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Floating division of series and other, element-wise (binary operator /).
* Series.add(other[, fill_value]): Series.mul(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Multiplication of series and other, element-wise (binary operator *).
* Series.add(other[, fill_value]): Series.radd(other[, fill_value])
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Addition of series and other, element-wise (binary operator +).
* Series.add(other[, fill_value]): Series.rdiv(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Floating division of series and other, element-wise (binary operator /).
* Series.add(other[, fill_value]): Series.rmul(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Multiplication of series and other, element-wise (binary operator *).
* Series.add(other[, fill_value]): Series.rsub(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Subtraction of series and other, element-wise (binary operator -).
* Series.add(other[, fill_value]): Series.rtruediv(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Floating division of series and other, element-wise (binary operator /).
* Series.add(other[, fill_value]): Series.sub(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Subtraction of series and other, element-wise (binary operator -).
* Series.add(other[, fill_value]): Series.truediv(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Floating division of series and other, element-wise (binary operator /).
* Series.add(other[, fill_value]): Series.pow(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Exponential power of series of series and other, element-wise (binary operator **).
* Series.add(other[, fill_value]): Series.rpow(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Exponential power of series and other, element-wise (binary operator **).
* Series.add(other[, fill_value]): Series.mod(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Modulo of series and other, element-wise (binary operator %).
* Series.add(other[, fill_value]): Series.rmod(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Modulo of series and other, element-wise (binary operator %).
* Series.add(other[, fill_value]): Series.floordiv(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Integer division of series and other, element-wise (binary operator //).
* Series.add(other[, fill_value]): Series.rfloordiv(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Reverse Integer division of series and other, element-wise (binary operator //).
* Series.add(other[, fill_value]): Series.divmod(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Integer division and modulo of series and other, element-wise (binary operator divmod).
* Series.add(other[, fill_value]): Series.rdivmod(other)
  * Return Addition of series and other, element-wise (binary operator +).: Return Integer division and modulo of series and other, element-wise (binary operator rdivmod).
* Series.add(other[, fill_value]): Series.combine_first(other)
  * Return Addition of series and other, element-wise (binary operator +).: Combine Series values, choosing the calling Series's values first.
* Series.add(other[, fill_value]): Series.lt(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compare if the current value is less than the other.
* Series.add(other[, fill_value]): Series.gt(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compare if the current value is greater than the other.
* Series.add(other[, fill_value]): Series.le(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compare if the current value is less than or equal to the other.
* Series.add(other[, fill_value]): Series.ge(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compare if the current value is greater than or equal to the other.
* Series.add(other[, fill_value]): Series.ne(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compare if the current value is not equal to the other.
* Series.add(other[, fill_value]): Series.eq(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compare if the current value is equal to the other.
* Series.add(other[, fill_value]): Series.product([axis, skipna, numeric_only, ...])
  * Return Addition of series and other, element-wise (binary operator +).: Return the product of the values.
* Series.add(other[, fill_value]): Series.dot(other)
  * Return Addition of series and other, element-wise (binary operator +).: Compute the dot product between the Series and the columns of other.


Function application, GroupBy & Window[#](#function-application-groupby-window "Permalink to this headline")
------------------------------------------------------------------------------------------------------------



* Series.apply(func[, args]): Series.agg(func)
  * Invoke function on values of Series.: Aggregate using one or more operations over the specified axis.
* Series.apply(func[, args]): Series.aggregate(func)
  * Invoke function on values of Series.: Aggregate using one or more operations over the specified axis.
* Series.apply(func[, args]): Series.transform(func[, axis])
  * Invoke function on values of Series.: Call func producing the same type as self with transformed values and that has the same axis length as input.
* Series.apply(func[, args]): Series.map(arg[, na_action])
  * Invoke function on values of Series.: Map values of Series according to input correspondence.
* Series.apply(func[, args]): Series.groupby(by[, axis, as_index, dropna])
  * Invoke function on values of Series.: Group DataFrame or Series using one or more columns.
* Series.apply(func[, args]): Series.rolling(window[, min_periods])
  * Invoke function on values of Series.: Provide rolling transformations.
* Series.apply(func[, args]): Series.expanding([min_periods])
  * Invoke function on values of Series.: Provide expanding transformations.
* Series.apply(func[, args]): Series.pipe(func, *args, **kwargs)
  * Invoke function on values of Series.: Apply func(self, *args, **kwargs).


Computations / Descriptive Stats[#](#computations-descriptive-stats "Permalink to this headline")
-------------------------------------------------------------------------------------------------



* Series.abs(): Series.all([axis, skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return whether all elements are True.
* Series.abs(): Series.any([axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return whether any element is True.
* Series.abs(): Series.autocorr([lag])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute the lag-N autocorrelation.
* Series.abs(): Series.between(left, right[, inclusive])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return boolean Series equivalent to left <= series <= right.
* Series.abs(): Series.clip([lower, upper, inplace])
  * Return a Series/DataFrame with absolute numeric value of each element.: Trim values at input threshold(s).
* Series.abs(): Series.corr(other[, method, min_periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute correlation with other Series, excluding missing values.
* Series.abs(): Series.count([axis, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Count non-NA cells for each column.
* Series.abs(): Series.cov(other[, min_periods, ddof])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute covariance with Series, excluding missing values.
* Series.abs(): Series.cummax([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative maximum over a DataFrame or Series axis.
* Series.abs(): Series.cummin([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative minimum over a DataFrame or Series axis.
* Series.abs(): Series.cumsum([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative sum over a DataFrame or Series axis.
* Series.abs(): Series.cumprod([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative product over a DataFrame or Series axis.
* Series.abs(): Series.describe([percentiles])
  * Return a Series/DataFrame with absolute numeric value of each element.: Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding NaN values.
* Series.abs(): Series.ewm([com, span, halflife, alpha, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Provide exponentially weighted window transformations.
* Series.abs(): Series.filter([items, like, regex, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Subset rows or columns of dataframe according to labels in the specified index.
* Series.abs(): Series.kurt([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
* Series.abs(): Series.max([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the maximum of the values.
* Series.abs(): Series.mean([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the mean of the values.
* Series.abs(): Series.min([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the minimum of the values.
* Series.abs(): Series.mode([dropna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the mode(s) of the dataset.
* Series.abs(): Series.nlargest([n])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the largest n elements.
* Series.abs(): Series.nsmallest([n])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the smallest n elements.
* Series.abs(): Series.pct_change([periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Percentage change between the current and a prior element.
* Series.abs(): Series.prod([axis, skipna, numeric_only, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the product of the values.
* Series.abs(): Series.nunique([dropna, approx, rsd])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return number of unique elements in the object.
* Series.abs(): Series.is_unique
  * Return a Series/DataFrame with absolute numeric value of each element.: Return boolean if values in the object are unique
* Series.abs(): Series.quantile([q, accuracy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return value at the given quantile.
* Series.abs(): Series.rank([method, ascending, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute numerical data ranks (1 through n) along axis.
* Series.abs(): Series.sem([axis, skipna, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased standard error of the mean over requested axis.
* Series.abs(): Series.skew([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased skew normalized by N-1.
* Series.abs(): Series.std([axis, skipna, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return sample standard deviation.
* Series.abs(): Series.sum([axis, skipna, numeric_only, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the sum of the values.
* Series.abs(): Series.median([axis, skipna, numeric_only, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the median of the values for the requested axis.
* Series.abs(): Series.var([axis, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased variance.
* Series.abs(): Series.kurtosis([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
* Series.abs(): Series.unique()
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unique values of Series object.
* Series.abs(): Series.value_counts([normalize, sort, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return a Series containing counts of unique values.
* Series.abs(): Series.round([decimals])
  * Return a Series/DataFrame with absolute numeric value of each element.: Round each value in a Series to the given number of decimals.
* Series.abs(): Series.diff([periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: First discrete difference of element.
* Series.abs(): Series.is_monotonic_increasing
  * Return a Series/DataFrame with absolute numeric value of each element.: Return boolean if values in the object are monotonically increasing.
* Series.abs(): Series.is_monotonic_decreasing
  * Return a Series/DataFrame with absolute numeric value of each element.: Return boolean if values in the object are monotonically decreasing.


Reindexing / Selection / Label manipulation[#](#reindexing-selection-label-manipulation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------



* Series.align(other[, join, axis, copy]): Series.drop([labels, index, columns, level, ...])
  * Align two objects on their axes with the specified join method.: Return Series with specified index labels removed.
* Series.align(other[, join, axis, copy]): Series.droplevel(level)
  * Align two objects on their axes with the specified join method.: Return Series with requested index level(s) removed.
* Series.align(other[, join, axis, copy]): Series.drop_duplicates([keep, inplace])
  * Align two objects on their axes with the specified join method.: Return Series with duplicate values removed.
* Series.align(other[, join, axis, copy]): Series.duplicated([keep])
  * Align two objects on their axes with the specified join method.: Indicate duplicate Series values.
* Series.align(other[, join, axis, copy]): Series.equals(other)
  * Align two objects on their axes with the specified join method.: Compare if the current value is equal to the other.
* Series.align(other[, join, axis, copy]): Series.add_prefix(prefix)
  * Align two objects on their axes with the specified join method.: Prefix labels with string prefix.
* Series.align(other[, join, axis, copy]): Series.add_suffix(suffix)
  * Align two objects on their axes with the specified join method.: Suffix labels with string suffix.
* Series.align(other[, join, axis, copy]): Series.first(offset)
  * Align two objects on their axes with the specified join method.: Select first periods of time series data based on a date offset.
* Series.align(other[, join, axis, copy]): Series.head([n])
  * Align two objects on their axes with the specified join method.: Return the first n rows.
* Series.align(other[, join, axis, copy]): Series.idxmax([skipna])
  * Align two objects on their axes with the specified join method.: Return the row label of the maximum value.
* Series.align(other[, join, axis, copy]): Series.idxmin([skipna])
  * Align two objects on their axes with the specified join method.: Return the row label of the minimum value.
* Series.align(other[, join, axis, copy]): Series.isin(values)
  * Align two objects on their axes with the specified join method.: Check whether values are contained in Series or Index.
* Series.align(other[, join, axis, copy]): Series.last(offset)
  * Align two objects on their axes with the specified join method.: Select final periods of time series data based on a date offset.
* Series.align(other[, join, axis, copy]): Series.rename([index])
  * Align two objects on their axes with the specified join method.: Alter Series index labels or name.
* Series.align(other[, join, axis, copy]): Series.rename_axis([mapper, index, inplace])
  * Align two objects on their axes with the specified join method.: Set the name of the axis for the index or columns.
* Series.align(other[, join, axis, copy]): Series.reindex([index, fill_value])
  * Align two objects on their axes with the specified join method.: Conform Series to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.
* Series.align(other[, join, axis, copy]): Series.reindex_like(other)
  * Align two objects on their axes with the specified join method.: Return a Series with matching indices as other object.
* Series.align(other[, join, axis, copy]): Series.reset_index([level, drop, name, inplace])
  * Align two objects on their axes with the specified join method.: Generate a new DataFrame or Series with the index reset.
* Series.align(other[, join, axis, copy]): Series.sample([n, frac, replace, ...])
  * Align two objects on their axes with the specified join method.: Return a random sample of items from an axis of object.
* Series.align(other[, join, axis, copy]): Series.searchsorted(value[, side])
  * Align two objects on their axes with the specified join method.: Find indices where elements should be inserted to maintain order.
* Series.align(other[, join, axis, copy]): Series.swaplevel([i, j, copy])
  * Align two objects on their axes with the specified join method.: Swap levels i and j in a MultiIndex.
* Series.align(other[, join, axis, copy]): Series.swapaxes(i, j[, copy])
  * Align two objects on their axes with the specified join method.: Interchange axes and swap values axes appropriately.
* Series.align(other[, join, axis, copy]): Series.take(indices)
  * Align two objects on their axes with the specified join method.: Return the elements in the given positional indices along an axis.
* Series.align(other[, join, axis, copy]): Series.tail([n])
  * Align two objects on their axes with the specified join method.: Return the last n rows.
* Series.align(other[, join, axis, copy]): Series.where(cond[, other])
  * Align two objects on their axes with the specified join method.: Replace values where the condition is False.
* Series.align(other[, join, axis, copy]): Series.mask(cond[, other])
  * Align two objects on their axes with the specified join method.: Replace values where the condition is True.
* Series.align(other[, join, axis, copy]): Series.truncate([before, after, axis, copy])
  * Align two objects on their axes with the specified join method.: Truncate a Series or DataFrame before and after some index value.


Missing data handling[#](#missing-data-handling "Permalink to this headline")
-----------------------------------------------------------------------------



* Series.backfill([axis, inplace, limit]): Series.bfill([axis, inplace, limit])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.
* Series.backfill([axis, inplace, limit]): Series.ffill([axis, inplace, limit])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Synonym for DataFrame.fillna() or Series.fillna() with method=`ffill`.
* Series.backfill([axis, inplace, limit]): Series.isna()
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Detect existing (non-missing) values.
* Series.backfill([axis, inplace, limit]): Series.isnull()
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Detect existing (non-missing) values.
* Series.backfill([axis, inplace, limit]): Series.notna()
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Detect existing (non-missing) values.
* Series.backfill([axis, inplace, limit]): Series.notnull()
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Detect existing (non-missing) values.
* Series.backfill([axis, inplace, limit]): Series.pad([axis, inplace, limit])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Synonym for DataFrame.fillna() or Series.fillna() with method=`ffill`.
* Series.backfill([axis, inplace, limit]): Series.dropna([axis, inplace])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Return a new Series with missing values removed.
* Series.backfill([axis, inplace, limit]): Series.fillna([value, method, axis, ...])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Fill NA/NaN values.
* Series.backfill([axis, inplace, limit]): Series.interpolate([method, limit, ...])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Fill NaN values using an interpolation method.


Reshaping, sorting, transposing[#](#reshaping-sorting-transposing "Permalink to this headline")
-----------------------------------------------------------------------------------------------



* Series.argsort(): Series.argmin([axis, skipna])
  * Return the integer indices that would sort the Series values.: Return int position of the smallest value in the Series.
* Series.argsort(): Series.argmax([axis, skipna])
  * Return the integer indices that would sort the Series values.: Return int position of the largest value in the Series.
* Series.argsort(): Series.sort_index([axis, level, ascending, ...])
  * Return the integer indices that would sort the Series values.: Sort object by labels (along an axis)
* Series.argsort(): Series.sort_values([ascending, inplace, ...])
  * Return the integer indices that would sort the Series values.: Sort by the values.
* Series.argsort(): Series.unstack([level])
  * Return the integer indices that would sort the Series values.: Unstack, a.k.a.
* Series.argsort(): Series.explode()
  * Return the integer indices that would sort the Series values.: Transform each element of a list-like to a row.
* Series.argsort(): Series.repeat(repeats)
  * Return the integer indices that would sort the Series values.: Repeat elements of a Series.
* Series.argsort(): Series.squeeze([axis])
  * Return the integer indices that would sort the Series values.: Squeeze 1 dimensional axis objects into scalars.
* Series.argsort(): Series.factorize([sort, use_na_sentinel])
  * Return the integer indices that would sort the Series values.: Encode the object as an enumerated type or categorical variable.


Combining / joining / merging[#](#combining-joining-merging "Permalink to this headline")
-----------------------------------------------------------------------------------------



* Series.compare(other[, keep_shape, keep_equal]): Series.replace([to_replace, value, regex])
  * Compare to another Series and show the differences.: Replace values given in to_replace with value.
* Series.compare(other[, keep_shape, keep_equal]): Series.update(other)
  * Compare to another Series and show the differences.: Modify Series in place using non-NA values from passed Series.


Accessors[#](#accessors "Permalink to this headline")
-----------------------------------------------------

Pandas API on Spark provides dtype-specific methods under various accessors. These are separate namespaces within [`Series`](about:blank/api/pyspark.pandas.Series.html#pyspark.pandas.Series "pyspark.pandas.Series") that only apply to specific data types.


|Data Type  |Accessor|
|-----------|--------|
|Datetime   |dt      |
|String     |str     |
|Categorical|cat     |


Date Time Handling[#](#date-time-handling "Permalink to this headline")
-----------------------------------------------------------------------

`Series.dt` can be used to access the values of the series as datetimelike and return several properties. These can be accessed like `Series.dt.<property>`.

### Datetime Properties[#](#datetime-properties "Permalink to this headline")



* Series.dt.date: Series.dt.year
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The year of the datetime.
* Series.dt.date: Series.dt.month
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The month of the timestamp as January = 1 December = 12.
* Series.dt.date: Series.dt.day
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The days of the datetime.
* Series.dt.date: Series.dt.hour
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The hours of the datetime.
* Series.dt.date: Series.dt.minute
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The minutes of the datetime.
* Series.dt.date: Series.dt.second
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The seconds of the datetime.
* Series.dt.date: Series.dt.microsecond
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The microseconds of the datetime.
* Series.dt.date: Series.dt.isocalendar()
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Calculate year, week, and day according to the ISO 8601 standard.
* Series.dt.date: Series.dt.dayofweek
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The day of the week with Monday=0, Sunday=6.
* Series.dt.date: Series.dt.weekday
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The day of the week with Monday=0, Sunday=6.
* Series.dt.date: Series.dt.dayofyear
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The ordinal day of the year.
* Series.dt.date: Series.dt.quarter
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The quarter of the date.
* Series.dt.date: Series.dt.is_month_start
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Indicates whether the date is the first day of the month.
* Series.dt.date: Series.dt.is_month_end
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Indicates whether the date is the last day of the month.
* Series.dt.date: Series.dt.is_quarter_start
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Indicator for whether the date is the first day of a quarter.
* Series.dt.date: Series.dt.is_quarter_end
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Indicator for whether the date is the last day of a quarter.
* Series.dt.date: Series.dt.is_year_start
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Indicate whether the date is the first day of a year.
* Series.dt.date: Series.dt.is_year_end
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Indicate whether the date is the last day of the year.
* Series.dt.date: Series.dt.is_leap_year
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: Boolean indicator if the date belongs to a leap year.
* Series.dt.date: Series.dt.daysinmonth
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The number of days in the month.
* Series.dt.date: Series.dt.days_in_month
  * Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).: The number of days in the month.


### Datetime Methods[#](#datetime-methods "Permalink to this headline")



* Series.dt.normalize(): Series.dt.strftime(date_format)
  * Convert times to midnight.: Convert to a string Series using specified date_format.
* Series.dt.normalize(): Series.dt.round(freq, *args, **kwargs)
  * Convert times to midnight.: Perform round operation on the data to the specified freq.
* Series.dt.normalize(): Series.dt.floor(freq, *args, **kwargs)
  * Convert times to midnight.: Perform floor operation on the data to the specified freq.
* Series.dt.normalize(): Series.dt.ceil(freq, *args, **kwargs)
  * Convert times to midnight.: Perform ceil operation on the data to the specified freq.
* Series.dt.normalize(): Series.dt.month_name([locale])
  * Convert times to midnight.: Return the month names of the series with specified locale.
* Series.dt.normalize(): Series.dt.day_name([locale])
  * Convert times to midnight.: Return the day names of the series with specified locale.


String Handling[#](#string-handling "Permalink to this headline")
-----------------------------------------------------------------

`Series.str` can be used to access the values of the series as strings and apply several methods to it. These can be accessed like `Series.str.<function/property>`.



* Series.str.capitalize(): Series.str.cat([others, sep, na_rep, join])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.center(width[, fillchar])
  * Convert Strings in the series to be capitalized.: Filling left and right side of strings in the Series/Index with an additional character.
* Series.str.capitalize(): Series.str.contains(pat[, case, flags, na, ...])
  * Convert Strings in the series to be capitalized.: Test if pattern or regex is contained within a string of a Series.
* Series.str.capitalize(): Series.str.count(pat[, flags])
  * Convert Strings in the series to be capitalized.: Count occurrences of pattern in each string of the Series.
* Series.str.capitalize(): Series.str.decode(encoding[, errors])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.encode(encoding[, errors])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.endswith(pattern[, na])
  * Convert Strings in the series to be capitalized.: Test if the end of each string element matches a pattern.
* Series.str.capitalize(): Series.str.extract(pat[, flags, expand])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.extractall(pat[, flags])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.find(sub[, start, end])
  * Convert Strings in the series to be capitalized.: Return lowest indexes in each string in the Series where the substring is fully contained between [start:end].
* Series.str.capitalize(): Series.str.findall(pat[, flags])
  * Convert Strings in the series to be capitalized.: Find all occurrences of pattern or regular expression in the Series.
* Series.str.capitalize(): Series.str.get(i)
  * Convert Strings in the series to be capitalized.: Extract element from each string or string list/tuple in the Series at the specified position.
* Series.str.capitalize(): Series.str.get_dummies([sep])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.index(sub[, start, end])
  * Convert Strings in the series to be capitalized.: Return lowest indexes in each string where the substring is fully contained between [start:end].
* Series.str.capitalize(): Series.str.isalnum()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are alphanumeric.
* Series.str.capitalize(): Series.str.isalpha()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are alphabetic.
* Series.str.capitalize(): Series.str.isdigit()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are digits.
* Series.str.capitalize(): Series.str.isspace()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are whitespaces.
* Series.str.capitalize(): Series.str.islower()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are lowercase.
* Series.str.capitalize(): Series.str.isupper()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are uppercase.
* Series.str.capitalize(): Series.str.istitle()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are title case.
* Series.str.capitalize(): Series.str.isnumeric()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are numeric.
* Series.str.capitalize(): Series.str.isdecimal()
  * Convert Strings in the series to be capitalized.: Check whether all characters in each string are decimals.
* Series.str.capitalize(): Series.str.join(sep)
  * Convert Strings in the series to be capitalized.: Join lists contained as elements in the Series with passed delimiter.
* Series.str.capitalize(): Series.str.len()
  * Convert Strings in the series to be capitalized.: Computes the length of each element in the Series.
* Series.str.capitalize(): Series.str.ljust(width[, fillchar])
  * Convert Strings in the series to be capitalized.: Filling right side of strings in the Series with an additional character.
* Series.str.capitalize(): Series.str.lower()
  * Convert Strings in the series to be capitalized.: Convert strings in the Series/Index to all lowercase.
* Series.str.capitalize(): Series.str.lstrip([to_strip])
  * Convert Strings in the series to be capitalized.: Remove leading characters.
* Series.str.capitalize(): Series.str.match(pat[, case, flags, na])
  * Convert Strings in the series to be capitalized.: Determine if each string matches a regular expression.
* Series.str.capitalize(): Series.str.normalize(form)
  * Convert Strings in the series to be capitalized.: Return the Unicode normal form for the strings in the Series.
* Series.str.capitalize(): Series.str.pad(width[, side, fillchar])
  * Convert Strings in the series to be capitalized.: Pad strings in the Series up to width.
* Series.str.capitalize(): Series.str.partition([sep, expand])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.repeat(repeats)
  * Convert Strings in the series to be capitalized.: Duplicate each string in the Series.
* Series.str.capitalize(): Series.str.replace(pat, repl[, n, case, ...])
  * Convert Strings in the series to be capitalized.: Replace occurrences of pattern/regex in the Series with some other string.
* Series.str.capitalize(): Series.str.rfind(sub[, start, end])
  * Convert Strings in the series to be capitalized.: Return highest indexes in each string in the Series where the substring is fully contained between [start:end].
* Series.str.capitalize(): Series.str.rindex(sub[, start, end])
  * Convert Strings in the series to be capitalized.: Return highest indexes in each string where the substring is fully contained between [start:end].
* Series.str.capitalize(): Series.str.rjust(width[, fillchar])
  * Convert Strings in the series to be capitalized.: Filling left side of strings in the Series with an additional character.
* Series.str.capitalize(): Series.str.rpartition([sep, expand])
  * Convert Strings in the series to be capitalized.: Not supported.
* Series.str.capitalize(): Series.str.rsplit([pat, n, expand])
  * Convert Strings in the series to be capitalized.: Split strings around given separator/delimiter.
* Series.str.capitalize(): Series.str.rstrip([to_strip])
  * Convert Strings in the series to be capitalized.: Remove trailing characters.
* Series.str.capitalize(): Series.str.slice([start, stop, step])
  * Convert Strings in the series to be capitalized.: Slice substrings from each element in the Series.
* Series.str.capitalize(): Series.str.slice_replace([start, stop, repl])
  * Convert Strings in the series to be capitalized.: Slice substrings from each element in the Series.
* Series.str.capitalize(): Series.str.split([pat, n, expand])
  * Convert Strings in the series to be capitalized.: Split strings around given separator/delimiter.
* Series.str.capitalize(): Series.str.startswith(pattern[, na])
  * Convert Strings in the series to be capitalized.: Test if the start of each string element matches a pattern.
* Series.str.capitalize(): Series.str.strip([to_strip])
  * Convert Strings in the series to be capitalized.: Remove leading and trailing characters.
* Series.str.capitalize(): Series.str.swapcase()
  * Convert Strings in the series to be capitalized.: Convert strings in the Series/Index to be swap cased.
* Series.str.capitalize(): Series.str.title()
  * Convert Strings in the series to be capitalized.: Convert Strings in the series to be title case.
* Series.str.capitalize(): Series.str.translate(table)
  * Convert Strings in the series to be capitalized.: Map all characters in the string through the given mapping table.
* Series.str.capitalize(): Series.str.upper()
  * Convert Strings in the series to be capitalized.: Convert strings in the Series/Index to all uppercase.
* Series.str.capitalize(): Series.str.wrap(width, **kwargs)
  * Convert Strings in the series to be capitalized.: Wrap long strings in the Series to be formatted in paragraphs with length less than a given width.
* Series.str.capitalize(): Series.str.zfill(width)
  * Convert Strings in the series to be capitalized.: Pad strings in the Series by prepending ‘0’ characters.


Categorical accessor[#](#categorical-accessor "Permalink to this headline")
---------------------------------------------------------------------------

Categorical-dtype specific methods and attributes are available under the `Series.cat` accessor.


|Series.cat.categories|The categories of this categorical.                 |
|---------------------|----------------------------------------------------|
|Series.cat.ordered   |Whether the categories have an ordered relationship.|
|Series.cat.codes     |Return Series of codes as well as the index.        |




* Series.cat.rename_categories(new_categories): Series.cat.reorder_categories(new_categories)
  * Rename categories.: Reorder categories as specified in new_categories.
* Series.cat.rename_categories(new_categories): Series.cat.add_categories(new_categories)
  * Rename categories.: Add new categories.
* Series.cat.rename_categories(new_categories): Series.cat.remove_categories(removals)
  * Rename categories.: Remove the specified categories.
* Series.cat.rename_categories(new_categories): Series.cat.remove_unused_categories()
  * Rename categories.: Remove categories which are not used.
* Series.cat.rename_categories(new_categories): Series.cat.set_categories(new_categories[, ...])
  * Rename categories.: Set the categories to the specified new_categories.
* Series.cat.rename_categories(new_categories): Series.cat.as_ordered()
  * Rename categories.: Set the Categorical to be ordered.
* Series.cat.rename_categories(new_categories): Series.cat.as_unordered()
  * Rename categories.: Set the Categorical to be unordered.


Plotting[#](#plotting "Permalink to this headline")
---------------------------------------------------

`Series.plot` is both a callable method and a namespace attribute for specific plotting methods of the form `Series.plot.<kind>`.



* Series.plot.area([x, y]): Series.plot.bar([x, y])
  * Draw a stacked area plot.: Vertical bar plot.
* Series.plot.area([x, y]): Series.plot.barh([x, y])
  * Draw a stacked area plot.: Make a horizontal bar plot.
* Series.plot.area([x, y]): Series.plot.box(**kwds)
  * Draw a stacked area plot.: Make a box plot of the DataFrame columns.
* Series.plot.area([x, y]): Series.plot.density([bw_method, ind])
  * Draw a stacked area plot.: Generate Kernel Density Estimate plot using Gaussian kernels.
* Series.plot.area([x, y]): Series.plot.hist([bins])
  * Draw a stacked area plot.: Draw one histogram of the DataFrame’s columns.
* Series.plot.area([x, y]): Series.plot.kde([bw_method, ind])
  * Draw a stacked area plot.: Generate Kernel Density Estimate plot using Gaussian kernels.
* Series.plot.area([x, y]): Series.plot.line([x, y])
  * Draw a stacked area plot.: Plot DataFrame/Series as lines.
* Series.plot.area([x, y]): Series.plot.pie(**kwds)
  * Draw a stacked area plot.: Generate a pie plot.




Serialization / IO / Conversion[#](#serialization-io-conversion "Permalink to this headline")
---------------------------------------------------------------------------------------------



* Series.to_pandas(): Series.to_numpy()
  * Return a pandas Series.: A NumPy ndarray representing the values in this DataFrame or Series.
* Series.to_pandas(): Series.to_list()
  * Return a pandas Series.: Return a list of the values.
* Series.to_pandas(): Series.to_string([buf, na_rep, ...])
  * Return a pandas Series.: Render a string representation of the Series.
* Series.to_pandas(): Series.to_dict([into])
  * Return a pandas Series.: Convert Series to {label -> value} dict or dict-like object.
* Series.to_pandas(): Series.to_clipboard([excel, sep])
  * Return a pandas Series.: Copy object to the system clipboard.
* Series.to_pandas(): Series.to_latex([buf, columns, header, ...])
  * Return a pandas Series.: Render an object to a LaTeX tabular environment table.
* Series.to_pandas(): Series.to_markdown([buf, mode])
  * Return a pandas Series.: Print Series or DataFrame in Markdown-friendly format.
* Series.to_pandas(): Series.to_json([path, compression, ...])
  * Return a pandas Series.: Convert the object to a JSON string.
* Series.to_pandas(): Series.to_csv([path, sep, na_rep, columns, ...])
  * Return a pandas Series.: Write object to a comma-separated values (csv) file.
* Series.to_pandas(): Series.to_excel(excel_writer[, sheet_name, ...])
  * Return a pandas Series.: Write object to an Excel sheet.
* Series.to_pandas(): Series.to_hdf(path_or_buf, key[, mode, ...])
  * Return a pandas Series.: Write the contained data to an HDF5 file using HDFStore.
* Series.to_pandas(): Series.to_frame([name])
  * Return a pandas Series.: Convert Series to DataFrame.


Pandas-on-Spark specific[#](#pandas-on-spark-specific "Permalink to this headline")
-----------------------------------------------------------------------------------

`Series.pandas_on_spark` provides pandas-on-Spark specific features that exists only in pandas API on Spark. These can be accessed by `Series.pandas_on_spark.<function/property>`.


# pyspark.pandas.Series — PySpark 4.0.1 documentation
[`abs`](about:blank/pyspark.pandas.Series.abs.html#pyspark.pandas.Series.abs "pyspark.pandas.Series.abs")()

Return a Series/DataFrame with absolute numeric value of each element.

[`add`](about:blank/pyspark.pandas.Series.add.html#pyspark.pandas.Series.add "pyspark.pandas.Series.add")(other\[, fill\_value\])

Return Addition of series and other, element-wise (binary operator +).

[`add_prefix`](about:blank/pyspark.pandas.Series.add_prefix.html#pyspark.pandas.Series.add_prefix "pyspark.pandas.Series.add_prefix")(prefix)

Prefix labels with string prefix.

[`add_suffix`](about:blank/pyspark.pandas.Series.add_suffix.html#pyspark.pandas.Series.add_suffix "pyspark.pandas.Series.add_suffix")(suffix)

Suffix labels with string suffix.

[`agg`](about:blank/pyspark.pandas.Series.agg.html#pyspark.pandas.Series.agg "pyspark.pandas.Series.agg")(func)

Aggregate using one or more operations over the specified axis.

[`aggregate`](about:blank/pyspark.pandas.Series.aggregate.html#pyspark.pandas.Series.aggregate "pyspark.pandas.Series.aggregate")(func)

Aggregate using one or more operations over the specified axis.

[`align`](about:blank/pyspark.pandas.Series.align.html#pyspark.pandas.Series.align "pyspark.pandas.Series.align")(other\[, join, axis, copy\])

Align two objects on their axes with the specified join method.

[`all`](about:blank/pyspark.pandas.Series.all.html#pyspark.pandas.Series.all "pyspark.pandas.Series.all")(\[axis, skipna\])

Return whether all elements are True.

[`any`](about:blank/pyspark.pandas.Series.any.html#pyspark.pandas.Series.any "pyspark.pandas.Series.any")(\[axis\])

Return whether any element is True.

[`apply`](about:blank/pyspark.pandas.Series.apply.html#pyspark.pandas.Series.apply "pyspark.pandas.Series.apply")(func\[, args\])

Invoke function on values of Series.

[`argmax`](about:blank/pyspark.pandas.Series.argmax.html#pyspark.pandas.Series.argmax "pyspark.pandas.Series.argmax")(\[axis, skipna\])

Return int position of the largest value in the Series.

[`argmin`](about:blank/pyspark.pandas.Series.argmin.html#pyspark.pandas.Series.argmin "pyspark.pandas.Series.argmin")(\[axis, skipna\])

Return int position of the smallest value in the Series.

[`argsort`](about:blank/pyspark.pandas.Series.argsort.html#pyspark.pandas.Series.argsort "pyspark.pandas.Series.argsort")()

Return the integer indices that would sort the Series values.

[`asof`](about:blank/pyspark.pandas.Series.asof.html#pyspark.pandas.Series.asof "pyspark.pandas.Series.asof")(where)

Return the last row(s) without any NaNs before where.

[`astype`](about:blank/pyspark.pandas.Series.astype.html#pyspark.pandas.Series.astype "pyspark.pandas.Series.astype")(dtype)

Cast a pandas-on-Spark object to a specified dtype `dtype`.

[`at_time`](about:blank/pyspark.pandas.Series.at_time.html#pyspark.pandas.Series.at_time "pyspark.pandas.Series.at_time")(time\[, asof, axis\])

Select values at particular time of day (example: 9:30AM).

[`autocorr`](about:blank/pyspark.pandas.Series.autocorr.html#pyspark.pandas.Series.autocorr "pyspark.pandas.Series.autocorr")(\[lag\])

Compute the lag-N autocorrelation.

[`backfill`](about:blank/pyspark.pandas.Series.backfill.html#pyspark.pandas.Series.backfill "pyspark.pandas.Series.backfill")(\[axis, inplace, limit\])

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`bfill` ``.

[`between`](about:blank/pyspark.pandas.Series.between.html#pyspark.pandas.Series.between "pyspark.pandas.Series.between")(left, right\[, inclusive\])

Return boolean Series equivalent to left <= series <= right.

[`between_time`](about:blank/pyspark.pandas.Series.between_time.html#pyspark.pandas.Series.between_time "pyspark.pandas.Series.between_time")(start\_time, end\_time\[, ...\])

Select values between particular times of the day (example: 9:00-9:30 AM).

[`bfill`](about:blank/pyspark.pandas.Series.bfill.html#pyspark.pandas.Series.bfill "pyspark.pandas.Series.bfill")(\[axis, inplace, limit\])

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`bfill` ``.

[`bool`](about:blank/pyspark.pandas.Series.bool.html#pyspark.pandas.Series.bool "pyspark.pandas.Series.bool")()

Return the bool of a single element in the current object.

[`clip`](about:blank/pyspark.pandas.Series.clip.html#pyspark.pandas.Series.clip "pyspark.pandas.Series.clip")(\[lower, upper, inplace\])

Trim values at input threshold(s).

[`combine_first`](about:blank/pyspark.pandas.Series.combine_first.html#pyspark.pandas.Series.combine_first "pyspark.pandas.Series.combine_first")(other)

Combine Series values, choosing the calling Series's values first.

[`compare`](about:blank/pyspark.pandas.Series.compare.html#pyspark.pandas.Series.compare "pyspark.pandas.Series.compare")(other\[, keep\_shape, keep\_equal\])

Compare to another Series and show the differences.

[`copy`](about:blank/pyspark.pandas.Series.copy.html#pyspark.pandas.Series.copy "pyspark.pandas.Series.copy")(\[deep\])

Make a copy of this object's indices and data.

[`corr`](about:blank/pyspark.pandas.Series.corr.html#pyspark.pandas.Series.corr "pyspark.pandas.Series.corr")(other\[, method, min\_periods\])

Compute correlation with other Series, excluding missing values.

[`count`](about:blank/pyspark.pandas.Series.count.html#pyspark.pandas.Series.count "pyspark.pandas.Series.count")(\[axis, numeric\_only\])

Count non-NA cells for each column.

[`cov`](about:blank/pyspark.pandas.Series.cov.html#pyspark.pandas.Series.cov "pyspark.pandas.Series.cov")(other\[, min\_periods, ddof\])

Compute covariance with Series, excluding missing values.

[`cummax`](about:blank/pyspark.pandas.Series.cummax.html#pyspark.pandas.Series.cummax "pyspark.pandas.Series.cummax")(\[skipna\])

Return cumulative maximum over a DataFrame or Series axis.

[`cummin`](about:blank/pyspark.pandas.Series.cummin.html#pyspark.pandas.Series.cummin "pyspark.pandas.Series.cummin")(\[skipna\])

Return cumulative minimum over a DataFrame or Series axis.

[`cumprod`](about:blank/pyspark.pandas.Series.cumprod.html#pyspark.pandas.Series.cumprod "pyspark.pandas.Series.cumprod")(\[skipna\])

Return cumulative product over a DataFrame or Series axis.

[`cumsum`](about:blank/pyspark.pandas.Series.cumsum.html#pyspark.pandas.Series.cumsum "pyspark.pandas.Series.cumsum")(\[skipna\])

Return cumulative sum over a DataFrame or Series axis.

[`describe`](about:blank/pyspark.pandas.Series.describe.html#pyspark.pandas.Series.describe "pyspark.pandas.Series.describe")(\[percentiles\])

Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding `NaN` values.

[`diff`](about:blank/pyspark.pandas.Series.diff.html#pyspark.pandas.Series.diff "pyspark.pandas.Series.diff")(\[periods\])

First discrete difference of element.

[`div`](about:blank/pyspark.pandas.Series.div.html#pyspark.pandas.Series.div "pyspark.pandas.Series.div")(other)

Return Floating division of series and other, element-wise (binary operator /).

`divide`(other)

Return Floating division of series and other, element-wise (binary operator /).

[`divmod`](about:blank/pyspark.pandas.Series.divmod.html#pyspark.pandas.Series.divmod "pyspark.pandas.Series.divmod")(other)

Return Integer division and modulo of series and other, element-wise (binary operator divmod).

[`dot`](about:blank/pyspark.pandas.Series.dot.html#pyspark.pandas.Series.dot "pyspark.pandas.Series.dot")(other)

Compute the dot product between the Series and the columns of other.

[`drop`](about:blank/pyspark.pandas.Series.drop.html#pyspark.pandas.Series.drop "pyspark.pandas.Series.drop")(\[labels, index, columns, level, inplace\])

Return Series with specified index labels removed.

[`drop_duplicates`](about:blank/pyspark.pandas.Series.drop_duplicates.html#pyspark.pandas.Series.drop_duplicates "pyspark.pandas.Series.drop_duplicates")(\[keep, inplace\])

Return Series with duplicate values removed.

[`droplevel`](about:blank/pyspark.pandas.Series.droplevel.html#pyspark.pandas.Series.droplevel "pyspark.pandas.Series.droplevel")(level)

Return Series with requested index level(s) removed.

[`dropna`](about:blank/pyspark.pandas.Series.dropna.html#pyspark.pandas.Series.dropna "pyspark.pandas.Series.dropna")(\[axis, inplace\])

Return a new Series with missing values removed.

[`duplicated`](about:blank/pyspark.pandas.Series.duplicated.html#pyspark.pandas.Series.duplicated "pyspark.pandas.Series.duplicated")(\[keep\])

Indicate duplicate Series values.

[`eq`](about:blank/pyspark.pandas.Series.eq.html#pyspark.pandas.Series.eq "pyspark.pandas.Series.eq")(other)

Compare if the current value is equal to the other.

[`equals`](about:blank/pyspark.pandas.Series.equals.html#pyspark.pandas.Series.equals "pyspark.pandas.Series.equals")(other)

Compare if the current value is equal to the other.

[`ewm`](about:blank/pyspark.pandas.Series.ewm.html#pyspark.pandas.Series.ewm "pyspark.pandas.Series.ewm")(\[com, span, halflife, alpha, ...\])

Provide exponentially weighted window transformations.

[`expanding`](about:blank/pyspark.pandas.Series.expanding.html#pyspark.pandas.Series.expanding "pyspark.pandas.Series.expanding")(\[min\_periods\])

Provide expanding transformations.

[`explode`](about:blank/pyspark.pandas.Series.explode.html#pyspark.pandas.Series.explode "pyspark.pandas.Series.explode")()

Transform each element of a list-like to a row.

[`factorize`](about:blank/pyspark.pandas.Series.factorize.html#pyspark.pandas.Series.factorize "pyspark.pandas.Series.factorize")(\[sort, use\_na\_sentinel\])

Encode the object as an enumerated type or categorical variable.

[`ffill`](about:blank/pyspark.pandas.Series.ffill.html#pyspark.pandas.Series.ffill "pyspark.pandas.Series.ffill")(\[axis, inplace, limit\])

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`ffill` ``.

[`fillna`](about:blank/pyspark.pandas.Series.fillna.html#pyspark.pandas.Series.fillna "pyspark.pandas.Series.fillna")(\[value, method, axis, inplace, limit\])

Fill NA/NaN values.

[`filter`](about:blank/pyspark.pandas.Series.filter.html#pyspark.pandas.Series.filter "pyspark.pandas.Series.filter")(\[items, like, regex, axis\])

Subset rows or columns of dataframe according to labels in the specified index.

[`first`](about:blank/pyspark.pandas.Series.first.html#pyspark.pandas.Series.first "pyspark.pandas.Series.first")(offset)

Select first periods of time series data based on a date offset.

[`first_valid_index`](about:blank/pyspark.pandas.Series.first_valid_index.html#pyspark.pandas.Series.first_valid_index "pyspark.pandas.Series.first_valid_index")()

Retrieves the index of the first valid value.

[`floordiv`](about:blank/pyspark.pandas.Series.floordiv.html#pyspark.pandas.Series.floordiv "pyspark.pandas.Series.floordiv")(other)

Return Integer division of series and other, element-wise (binary operator //).

[`ge`](about:blank/pyspark.pandas.Series.ge.html#pyspark.pandas.Series.ge "pyspark.pandas.Series.ge")(other)

Compare if the current value is greater than or equal to the other.

[`get`](about:blank/pyspark.pandas.Series.get.html#pyspark.pandas.Series.get "pyspark.pandas.Series.get")(key\[, default\])

Get item from object for given key (DataFrame column, Panel slice, etc.).

[`groupby`](about:blank/pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")(by\[, axis, as\_index, dropna\])

Group DataFrame or Series using one or more columns.

[`gt`](about:blank/pyspark.pandas.Series.gt.html#pyspark.pandas.Series.gt "pyspark.pandas.Series.gt")(other)

Compare if the current value is greater than the other.

[`head`](about:blank/pyspark.pandas.Series.head.html#pyspark.pandas.Series.head "pyspark.pandas.Series.head")(\[n\])

Return the first n rows.

[`hist`](about:blank/pyspark.pandas.Series.hist.html#pyspark.pandas.Series.hist "pyspark.pandas.Series.hist")(\[bins\])

Draw one histogram of the DataFrame’s columns.

[`idxmax`](about:blank/pyspark.pandas.Series.idxmax.html#pyspark.pandas.Series.idxmax "pyspark.pandas.Series.idxmax")(\[skipna\])

Return the row label of the maximum value.

[`idxmin`](about:blank/pyspark.pandas.Series.idxmin.html#pyspark.pandas.Series.idxmin "pyspark.pandas.Series.idxmin")(\[skipna\])

Return the row label of the minimum value.

[`interpolate`](about:blank/pyspark.pandas.Series.interpolate.html#pyspark.pandas.Series.interpolate "pyspark.pandas.Series.interpolate")(\[method, limit, ...\])

Fill NaN values using an interpolation method.

[`isin`](about:blank/pyspark.pandas.Series.isin.html#pyspark.pandas.Series.isin "pyspark.pandas.Series.isin")(values)

Check whether values are contained in Series or Index.

[`isna`](about:blank/pyspark.pandas.Series.isna.html#pyspark.pandas.Series.isna "pyspark.pandas.Series.isna")()

Detect existing (non-missing) values.

[`isnull`](about:blank/pyspark.pandas.Series.isnull.html#pyspark.pandas.Series.isnull "pyspark.pandas.Series.isnull")()

Detect existing (non-missing) values.

[`item`](about:blank/pyspark.pandas.Series.item.html#pyspark.pandas.Series.item "pyspark.pandas.Series.item")()

Return the first element of the underlying data as a Python scalar.

[`items`](about:blank/pyspark.pandas.Series.items.html#pyspark.pandas.Series.items "pyspark.pandas.Series.items")()

Lazily iterate over (index, value) tuples.

[`keys`](about:blank/pyspark.pandas.Series.keys.html#pyspark.pandas.Series.keys "pyspark.pandas.Series.keys")()

Return alias for index.

[`kurt`](about:blank/pyspark.pandas.Series.kurt.html#pyspark.pandas.Series.kurt "pyspark.pandas.Series.kurt")(\[axis, skipna, numeric\_only\])

Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).

[`kurtosis`](about:blank/pyspark.pandas.Series.kurtosis.html#pyspark.pandas.Series.kurtosis "pyspark.pandas.Series.kurtosis")(\[axis, skipna, numeric\_only\])

Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).

[`last`](about:blank/pyspark.pandas.Series.last.html#pyspark.pandas.Series.last "pyspark.pandas.Series.last")(offset)

Select final periods of time series data based on a date offset.

[`last_valid_index`](about:blank/pyspark.pandas.Series.last_valid_index.html#pyspark.pandas.Series.last_valid_index "pyspark.pandas.Series.last_valid_index")()

Return index for last non-NA/null value.

[`le`](about:blank/pyspark.pandas.Series.le.html#pyspark.pandas.Series.le "pyspark.pandas.Series.le")(other)

Compare if the current value is less than or equal to the other.

[`lt`](about:blank/pyspark.pandas.Series.lt.html#pyspark.pandas.Series.lt "pyspark.pandas.Series.lt")(other)

Compare if the current value is less than the other.

[`map`](about:blank/pyspark.pandas.Series.map.html#pyspark.pandas.Series.map "pyspark.pandas.Series.map")(arg\[, na\_action\])

Map values of Series according to input correspondence.

[`mask`](about:blank/pyspark.pandas.Series.mask.html#pyspark.pandas.Series.mask "pyspark.pandas.Series.mask")(cond\[, other\])

Replace values where the condition is True.

[`max`](about:blank/pyspark.pandas.Series.max.html#pyspark.pandas.Series.max "pyspark.pandas.Series.max")(\[axis, skipna, numeric\_only\])

Return the maximum of the values.

[`mean`](about:blank/pyspark.pandas.Series.mean.html#pyspark.pandas.Series.mean "pyspark.pandas.Series.mean")(\[axis, skipna, numeric\_only\])

Return the mean of the values.

[`median`](about:blank/pyspark.pandas.Series.median.html#pyspark.pandas.Series.median "pyspark.pandas.Series.median")(\[axis, skipna, numeric\_only, accuracy\])

Return the median of the values for the requested axis.

[`min`](about:blank/pyspark.pandas.Series.min.html#pyspark.pandas.Series.min "pyspark.pandas.Series.min")(\[axis, skipna, numeric\_only\])

Return the minimum of the values.

[`mod`](about:blank/pyspark.pandas.Series.mod.html#pyspark.pandas.Series.mod "pyspark.pandas.Series.mod")(other)

Return Modulo of series and other, element-wise (binary operator %).

[`mode`](about:blank/pyspark.pandas.Series.mode.html#pyspark.pandas.Series.mode "pyspark.pandas.Series.mode")(\[dropna\])

Return the mode(s) of the dataset.

[`mul`](about:blank/pyspark.pandas.Series.mul.html#pyspark.pandas.Series.mul "pyspark.pandas.Series.mul")(other)

Return Multiplication of series and other, element-wise (binary operator \*).

`multiply`(other)

Return Multiplication of series and other, element-wise (binary operator \*).

[`ne`](about:blank/pyspark.pandas.Series.ne.html#pyspark.pandas.Series.ne "pyspark.pandas.Series.ne")(other)

Compare if the current value is not equal to the other.

[`nlargest`](about:blank/pyspark.pandas.Series.nlargest.html#pyspark.pandas.Series.nlargest "pyspark.pandas.Series.nlargest")(\[n\])

Return the largest n elements.

[`notna`](about:blank/pyspark.pandas.Series.notna.html#pyspark.pandas.Series.notna "pyspark.pandas.Series.notna")()

Detect existing (non-missing) values.

[`notnull`](about:blank/pyspark.pandas.Series.notnull.html#pyspark.pandas.Series.notnull "pyspark.pandas.Series.notnull")()

Detect existing (non-missing) values.

[`nsmallest`](about:blank/pyspark.pandas.Series.nsmallest.html#pyspark.pandas.Series.nsmallest "pyspark.pandas.Series.nsmallest")(\[n\])

Return the smallest n elements.

[`nunique`](about:blank/pyspark.pandas.Series.nunique.html#pyspark.pandas.Series.nunique "pyspark.pandas.Series.nunique")(\[dropna, approx, rsd\])

Return number of unique elements in the object.

[`pad`](about:blank/pyspark.pandas.Series.pad.html#pyspark.pandas.Series.pad "pyspark.pandas.Series.pad")(\[axis, inplace, limit\])

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`ffill` ``.

[`pct_change`](about:blank/pyspark.pandas.Series.pct_change.html#pyspark.pandas.Series.pct_change "pyspark.pandas.Series.pct_change")(\[periods\])

Percentage change between the current and a prior element.

[`pipe`](about:blank/pyspark.pandas.Series.pipe.html#pyspark.pandas.Series.pipe "pyspark.pandas.Series.pipe")(func, \*args, \*\*kwargs)

Apply func(self, \*args, \*\*kwargs).

[`pop`](about:blank/pyspark.pandas.Series.pop.html#pyspark.pandas.Series.pop "pyspark.pandas.Series.pop")(item)

Return item and drop from series.

[`pow`](about:blank/pyspark.pandas.Series.pow.html#pyspark.pandas.Series.pow "pyspark.pandas.Series.pow")(other)

Return Exponential power of series of series and other, element-wise (binary operator \*\*).

[`prod`](about:blank/pyspark.pandas.Series.prod.html#pyspark.pandas.Series.prod "pyspark.pandas.Series.prod")(\[axis, skipna, numeric\_only, min\_count\])

Return the product of the values.

[`product`](about:blank/pyspark.pandas.Series.product.html#pyspark.pandas.Series.product "pyspark.pandas.Series.product")(\[axis, skipna, numeric\_only, min\_count\])

Return the product of the values.

[`quantile`](about:blank/pyspark.pandas.Series.quantile.html#pyspark.pandas.Series.quantile "pyspark.pandas.Series.quantile")(\[q, accuracy\])

Return value at the given quantile.

[`radd`](about:blank/pyspark.pandas.Series.radd.html#pyspark.pandas.Series.radd "pyspark.pandas.Series.radd")(other\[, fill\_value\])

Return Reverse Addition of series and other, element-wise (binary operator +).

[`rank`](about:blank/pyspark.pandas.Series.rank.html#pyspark.pandas.Series.rank "pyspark.pandas.Series.rank")(\[method, ascending, numeric\_only\])

Compute numerical data ranks (1 through n) along axis.

[`rdiv`](about:blank/pyspark.pandas.Series.rdiv.html#pyspark.pandas.Series.rdiv "pyspark.pandas.Series.rdiv")(other)

Return Reverse Floating division of series and other, element-wise (binary operator /).

[`rdivmod`](about:blank/pyspark.pandas.Series.rdivmod.html#pyspark.pandas.Series.rdivmod "pyspark.pandas.Series.rdivmod")(other)

Return Integer division and modulo of series and other, element-wise (binary operator rdivmod).

[`reindex`](about:blank/pyspark.pandas.Series.reindex.html#pyspark.pandas.Series.reindex "pyspark.pandas.Series.reindex")(\[index, fill\_value\])

Conform Series to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.

[`reindex_like`](about:blank/pyspark.pandas.Series.reindex_like.html#pyspark.pandas.Series.reindex_like "pyspark.pandas.Series.reindex_like")(other)

Return a Series with matching indices as other object.

[`rename`](about:blank/pyspark.pandas.Series.rename.html#pyspark.pandas.Series.rename "pyspark.pandas.Series.rename")(\[index\])

Alter Series index labels or name.

[`rename_axis`](about:blank/pyspark.pandas.Series.rename_axis.html#pyspark.pandas.Series.rename_axis "pyspark.pandas.Series.rename_axis")(\[mapper, index, inplace\])

Set the name of the axis for the index or columns.

[`repeat`](about:blank/pyspark.pandas.Series.repeat.html#pyspark.pandas.Series.repeat "pyspark.pandas.Series.repeat")(repeats)

Repeat elements of a Series.

[`replace`](about:blank/pyspark.pandas.Series.replace.html#pyspark.pandas.Series.replace "pyspark.pandas.Series.replace")(\[to\_replace, value, regex\])

Replace values given in to\_replace with value.

[`resample`](about:blank/pyspark.pandas.Series.resample.html#pyspark.pandas.Series.resample "pyspark.pandas.Series.resample")(rule\[, closed, label, on\])

Resample time-series data.

[`reset_index`](about:blank/pyspark.pandas.Series.reset_index.html#pyspark.pandas.Series.reset_index "pyspark.pandas.Series.reset_index")(\[level, drop, name, inplace\])

Generate a new DataFrame or Series with the index reset.

[`rfloordiv`](about:blank/pyspark.pandas.Series.rfloordiv.html#pyspark.pandas.Series.rfloordiv "pyspark.pandas.Series.rfloordiv")(other)

Return Reverse Integer division of series and other, element-wise (binary operator //).

[`rmod`](about:blank/pyspark.pandas.Series.rmod.html#pyspark.pandas.Series.rmod "pyspark.pandas.Series.rmod")(other)

Return Reverse Modulo of series and other, element-wise (binary operator %).

[`rmul`](about:blank/pyspark.pandas.Series.rmul.html#pyspark.pandas.Series.rmul "pyspark.pandas.Series.rmul")(other)

Return Reverse Multiplication of series and other, element-wise (binary operator \*).

[`rolling`](about:blank/pyspark.pandas.Series.rolling.html#pyspark.pandas.Series.rolling "pyspark.pandas.Series.rolling")(window\[, min\_periods\])

Provide rolling transformations.

[`round`](about:blank/pyspark.pandas.Series.round.html#pyspark.pandas.Series.round "pyspark.pandas.Series.round")(\[decimals\])

Round each value in a Series to the given number of decimals.

[`rpow`](about:blank/pyspark.pandas.Series.rpow.html#pyspark.pandas.Series.rpow "pyspark.pandas.Series.rpow")(other)

Return Reverse Exponential power of series and other, element-wise (binary operator \*\*).

[`rsub`](about:blank/pyspark.pandas.Series.rsub.html#pyspark.pandas.Series.rsub "pyspark.pandas.Series.rsub")(other)

Return Reverse Subtraction of series and other, element-wise (binary operator \-).

[`rtruediv`](about:blank/pyspark.pandas.Series.rtruediv.html#pyspark.pandas.Series.rtruediv "pyspark.pandas.Series.rtruediv")(other)

Return Reverse Floating division of series and other, element-wise (binary operator /).

[`sample`](about:blank/pyspark.pandas.Series.sample.html#pyspark.pandas.Series.sample "pyspark.pandas.Series.sample")(\[n, frac, replace, random\_state, ...\])

Return a random sample of items from an axis of object.

[`searchsorted`](about:blank/pyspark.pandas.Series.searchsorted.html#pyspark.pandas.Series.searchsorted "pyspark.pandas.Series.searchsorted")(value\[, side\])

Find indices where elements should be inserted to maintain order.

[`sem`](about:blank/pyspark.pandas.Series.sem.html#pyspark.pandas.Series.sem "pyspark.pandas.Series.sem")(\[axis, skipna, ddof, numeric\_only\])

Return unbiased standard error of the mean over requested axis.

[`shift`](about:blank/pyspark.pandas.Series.shift.html#pyspark.pandas.Series.shift "pyspark.pandas.Series.shift")(\[periods, fill\_value\])

Shift Series/Index by desired number of periods.

[`skew`](about:blank/pyspark.pandas.Series.skew.html#pyspark.pandas.Series.skew "pyspark.pandas.Series.skew")(\[axis, skipna, numeric\_only\])

Return unbiased skew normalized by N-1.

[`sort_index`](about:blank/pyspark.pandas.Series.sort_index.html#pyspark.pandas.Series.sort_index "pyspark.pandas.Series.sort_index")(\[axis, level, ascending, ...\])

Sort object by labels (along an axis)

[`sort_values`](about:blank/pyspark.pandas.Series.sort_values.html#pyspark.pandas.Series.sort_values "pyspark.pandas.Series.sort_values")(\[ascending, inplace, ...\])

Sort by the values.

[`squeeze`](about:blank/pyspark.pandas.Series.squeeze.html#pyspark.pandas.Series.squeeze "pyspark.pandas.Series.squeeze")(\[axis\])

Squeeze 1 dimensional axis objects into scalars.

[`std`](about:blank/pyspark.pandas.Series.std.html#pyspark.pandas.Series.std "pyspark.pandas.Series.std")(\[axis, skipna, ddof, numeric\_only\])

Return sample standard deviation.

[`sub`](about:blank/pyspark.pandas.Series.sub.html#pyspark.pandas.Series.sub "pyspark.pandas.Series.sub")(other)

Return Subtraction of series and other, element-wise (binary operator \-).

`subtract`(other)

Return Subtraction of series and other, element-wise (binary operator \-).

[`sum`](about:blank/pyspark.pandas.Series.sum.html#pyspark.pandas.Series.sum "pyspark.pandas.Series.sum")(\[axis, skipna, numeric\_only, min\_count\])

Return the sum of the values.

[`swapaxes`](about:blank/pyspark.pandas.Series.swapaxes.html#pyspark.pandas.Series.swapaxes "pyspark.pandas.Series.swapaxes")(i, j\[, copy\])

Interchange axes and swap values axes appropriately.

[`swaplevel`](about:blank/pyspark.pandas.Series.swaplevel.html#pyspark.pandas.Series.swaplevel "pyspark.pandas.Series.swaplevel")(\[i, j, copy\])

Swap levels i and j in a MultiIndex.

[`tail`](about:blank/pyspark.pandas.Series.tail.html#pyspark.pandas.Series.tail "pyspark.pandas.Series.tail")(\[n\])

Return the last n rows.

[`take`](about:blank/pyspark.pandas.Series.take.html#pyspark.pandas.Series.take "pyspark.pandas.Series.take")(indices)

Return the elements in the given _positional_ indices along an axis.

[`to_clipboard`](about:blank/pyspark.pandas.Series.to_clipboard.html#pyspark.pandas.Series.to_clipboard "pyspark.pandas.Series.to_clipboard")(\[excel, sep\])

Copy object to the system clipboard.

[`to_csv`](about:blank/pyspark.pandas.Series.to_csv.html#pyspark.pandas.Series.to_csv "pyspark.pandas.Series.to_csv")(\[path, sep, na\_rep, columns, header, ...\])

Write object to a comma-separated values (csv) file.

`to_dataframe`(\[name\])

Convert Series to DataFrame.

[`to_dict`](about:blank/pyspark.pandas.Series.to_dict.html#pyspark.pandas.Series.to_dict "pyspark.pandas.Series.to_dict")(\[into\])

Convert Series to {label -> value} dict or dict-like object.

[`to_excel`](about:blank/pyspark.pandas.Series.to_excel.html#pyspark.pandas.Series.to_excel "pyspark.pandas.Series.to_excel")(excel\_writer\[, sheet\_name, na\_rep, ...\])

Write object to an Excel sheet.

[`to_frame`](about:blank/pyspark.pandas.Series.to_frame.html#pyspark.pandas.Series.to_frame "pyspark.pandas.Series.to_frame")(\[name\])

Convert Series to DataFrame.

[`to_hdf`](about:blank/pyspark.pandas.Series.to_hdf.html#pyspark.pandas.Series.to_hdf "pyspark.pandas.Series.to_hdf")(path\_or\_buf, key\[, mode, complevel, ...\])

Write the contained data to an HDF5 file using HDFStore.

[`to_json`](about:blank/pyspark.pandas.Series.to_json.html#pyspark.pandas.Series.to_json "pyspark.pandas.Series.to_json")(\[path, compression, num\_files, ...\])

Convert the object to a JSON string.

[`to_latex`](about:blank/pyspark.pandas.Series.to_latex.html#pyspark.pandas.Series.to_latex "pyspark.pandas.Series.to_latex")(\[buf, columns, header, index, ...\])

Render an object to a LaTeX tabular environment table.

[`to_list`](about:blank/pyspark.pandas.Series.to_list.html#pyspark.pandas.Series.to_list "pyspark.pandas.Series.to_list")()

Return a list of the values.

[`to_markdown`](about:blank/pyspark.pandas.Series.to_markdown.html#pyspark.pandas.Series.to_markdown "pyspark.pandas.Series.to_markdown")(\[buf, mode\])

Print Series or DataFrame in Markdown-friendly format.

[`to_numpy`](about:blank/pyspark.pandas.Series.to_numpy.html#pyspark.pandas.Series.to_numpy "pyspark.pandas.Series.to_numpy")()

A NumPy ndarray representing the values in this DataFrame or Series.

[`to_pandas`](about:blank/pyspark.pandas.Series.to_pandas.html#pyspark.pandas.Series.to_pandas "pyspark.pandas.Series.to_pandas")()

Return a pandas Series.

[`to_string`](about:blank/pyspark.pandas.Series.to_string.html#pyspark.pandas.Series.to_string "pyspark.pandas.Series.to_string")(\[buf, na\_rep, float\_format, ...\])

Render a string representation of the Series.

`tolist`()

Return a list of the values.

[`transform`](about:blank/pyspark.pandas.Series.transform.html#pyspark.pandas.Series.transform "pyspark.pandas.Series.transform")(func\[, axis\])

Call `func` producing the same type as self with transformed values and that has the same axis length as input.

`transpose`(\*args, \*\*kwargs)

Return the transpose, which is self.

[`truediv`](about:blank/pyspark.pandas.Series.truediv.html#pyspark.pandas.Series.truediv "pyspark.pandas.Series.truediv")(other)

Return Floating division of series and other, element-wise (binary operator /).

[`truncate`](about:blank/pyspark.pandas.Series.truncate.html#pyspark.pandas.Series.truncate "pyspark.pandas.Series.truncate")(\[before, after, axis, copy\])

Truncate a Series or DataFrame before and after some index value.

[`unique`](about:blank/pyspark.pandas.Series.unique.html#pyspark.pandas.Series.unique "pyspark.pandas.Series.unique")()

Return unique values of Series object.

[`unstack`](about:blank/pyspark.pandas.Series.unstack.html#pyspark.pandas.Series.unstack "pyspark.pandas.Series.unstack")(\[level\])

Unstack, a.k.a.

[`update`](about:blank/pyspark.pandas.Series.update.html#pyspark.pandas.Series.update "pyspark.pandas.Series.update")(other)

Modify Series in place using non-NA values from passed Series.

[`value_counts`](about:blank/pyspark.pandas.Series.value_counts.html#pyspark.pandas.Series.value_counts "pyspark.pandas.Series.value_counts")(\[normalize, sort, ascending, ...\])

Return a Series containing counts of unique values.

[`var`](about:blank/pyspark.pandas.Series.var.html#pyspark.pandas.Series.var "pyspark.pandas.Series.var")(\[axis, ddof, numeric\_only\])

Return unbiased variance.

[`where`](about:blank/pyspark.pandas.Series.where.html#pyspark.pandas.Series.where "pyspark.pandas.Series.where")(cond\[, other\])

Replace values where the condition is False.

[`xs`](about:blank/pyspark.pandas.Series.xs.html#pyspark.pandas.Series.xs "pyspark.pandas.Series.xs")(key\[, level\])

Return cross-section from the Series.


# pyspark.pandas.Series.index — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.index

_property_ Series.index[#](#pyspark.pandas.Series.index "Permalink to this definition")

The index (axis labels) Column of the Series.

# pyspark.pandas.Series.dtype — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dtype

_property_ Series.dtype[#](#pyspark.pandas.Series.dtype "Permalink to this definition")

Return the dtype object of the underlying data.

Examples

```
>>> s = ps.Series([1, 2, 3])
>>> s.dtype
dtype('int64')

```


```
>>> s = ps.Series(list('abc'))
>>> s.dtype
dtype('O')

```


```
>>> s = ps.Series(pd.date_range('20130101', periods=3))
>>> s.dtype
dtype('<M8[ns]')

```


```
>>> s.rename("a").to_frame().set_index("a").index.dtype
dtype('<M8[ns]')

```


# pyspark.pandas.Series.dtypes — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dtypes

_property_ Series.dtypes[#](#pyspark.pandas.Series.dtypes "Permalink to this definition")

Return the dtype object of the underlying data.

```
>>> s = ps.Series(list('abc'))
>>> s.dtype == s.dtypes
True

```

# pyspark.pandas.Series.ndim — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.ndim

_property_ Series.ndim[#](#pyspark.pandas.Series.ndim "Permalink to this definition")

Return an int representing the number of array dimensions.

Return 1 for Series / Index / MultiIndex.

Examples

For Series

```
>>> s = ps.Series([None, 1, 2, 3, 4], index=[4, 5, 2, 1, 8])
>>> s.ndim
1

```


For Index

For MultiIndex

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [1, 1, 1, 1, 1, 2, 1, 2, 2]])
>>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)
>>> s.index.ndim
1

```


# pyspark.pandas.Series.name — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.name

_property_ Series.name[#](#pyspark.pandas.Series.name "Permalink to this definition")

Return name of the Series.


# pyspark.pandas.Series.shape — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.shape

_property_ Series.shape[#](#pyspark.pandas.Series.shape "Permalink to this definition")

Return a tuple of the shape of the underlying data.

# pyspark.pandas.Series.axes — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.axes

_property_ Series.axes[#](#pyspark.pandas.Series.axes "Permalink to this definition")

Return a list of the row axis labels.

Examples

```
>>> psser = ps.Series([1, 2, 3])
>>> psser.axes
[Index([0, 1, 2], dtype='int64')]

```


# pyspark.pandas.Series.size — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.size

_property_ Series.size[#](#pyspark.pandas.Series.size "Permalink to this definition")

Return an int representing the number of elements in this object.

Return the number of rows if Series. Otherwise return the number of rows times number of columns if DataFrame.

Examples

```
>>> s = ps.Series({'a': 1, 'b': 2, 'c': None})
>>> s.size
3

```


```
>>> df = ps.DataFrame({'col1': [1, 2, None], 'col2': [3, 4, None]})
>>> df.size
6

```


```
>>> df = ps.DataFrame(index=[1, 2, None])
>>> df.size
0

```

# pyspark.pandas.Series.empty — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.empty

_property_ Series.empty[#](#pyspark.pandas.Series.empty "Permalink to this definition")

Returns true if the current object is empty. Otherwise, it returns false.

```
>>> ps.range(10).id.empty
False

```


```
>>> ps.range(0).id.empty
True

```


```
>>> ps.DataFrame({}, index=list('abc')).index.empty
False

```



# pyspark.pandas.Series.T — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.T

_property_ Series.T[#](#pyspark.pandas.Series.T "Permalink to this definition")

Return the transpose, which is self.

Examples

It returns the same object as the transpose of the given series object, which is by definition self.

```
>>> s = ps.Series([1, 2, 3])
>>> s
0    1
1    2
2    3
dtype: int64

```


```
>>> s.transpose()
0    1
1    2
2    3
dtype: int64

```


# pyspark.pandas.Series.hasnans — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.hasnans

_property_ Series.hasnans[#](#pyspark.pandas.Series.hasnans "Permalink to this definition")

Return True if it has any missing values. Otherwise, it returns False.

```
>>> ps.DataFrame({}, index=list('abc')).index.hasnans
False

```


```
>>> ps.Series(['a', None]).hasnans
True

```


```
>>> ps.Series([1.0, 2.0, np.nan]).hasnans
True

```


```
>>> ps.Series([1, 2, 3]).hasnans
False

```


```
>>> (ps.Series([1.0, 2.0, np.nan]) + 1).hasnans
True

```


```
>>> ps.Series([1, 2, 3]).rename("a").to_frame().set_index("a").index.hasnans
False

```

# pyspark.pandas.Series.values — PySpark 4.0.1 documentation
_property_ Series.values[#](#pyspark.pandas.Series.values "Permalink to this definition")

Return a Numpy representation of the DataFrame or the Series.

Warning

We recommend using DataFrame.to\_numpy() or Series.to\_numpy() instead.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driver’s memory.

Returns

numpy.ndarray

Examples

A DataFrame where all columns are the same type (e.g., int64) results in an array of the same type.

```
>>> df = ps.DataFrame({'age':    [ 3,  29],
...                    'height': [94, 170],
...                    'weight': [31, 115]})
>>> df
   age  height  weight
0    3      94      31
1   29     170     115
>>> df.dtypes
age       int64
height    int64
weight    int64
dtype: object
>>> df.values
array([[  3,  94,  31],
       [ 29, 170, 115]])

```


A DataFrame with mixed type columns(e.g., str/object, int64, float32) results in an ndarray of the broadest type that accommodates these mixed types (e.g., object).

```
>>> df2 = ps.DataFrame([('parrot',   24.0, 'second'),
...                     ('lion',     80.5, 'first'),
...                     ('monkey', np.nan, None)],
...                   columns=('name', 'max_speed', 'rank'))
>>> df2.dtypes
name          object
max_speed    float64
rank          object
dtype: object
>>> df2.values
array([['parrot', 24.0, 'second'],
       ['lion', 80.5, 'first'],
       ['monkey', nan, None]], dtype=object)

```


For Series,

```
>>> ps.Series([1, 2, 3]).values
array([1, 2, 3])

```


```
>>> ps.Series(list('aabc')).values
array(['a', 'a', 'b', 'c'], dtype=object)

```

# pyspark.pandas.Series.astype — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.astype

Series.astype(_dtype_)
[#](#pyspark.pandas.Series.astype "Permalink to this definition")

Cast a pandas-on-Spark object to a specified dtype `dtype`.

Parameters

**dtype**data type

Use a numpy.dtype or Python type to cast entire pandas object to the same type.

Returns

**casted**same type as caller

Examples

```
>>> ser = ps.Series([1, 2], dtype='int32')
>>> ser
0    1
1    2
dtype: int32

```


```
>>> ser.astype('int64')
0    1
1    2
dtype: int64

```


```
>>> ser.rename("a").to_frame().set_index("a").index.astype('int64')
Index([1, 2], dtype='int64', name='a')

```


# pyspark.pandas.Series.copy — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.copy

Series.copy(_deep\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.copy)
[#](#pyspark.pandas.Series.copy "Permalink to this definition")

Make a copy of this object’s indices and data.

Parameters

**deep**bool, default True

this parameter is not supported but just dummy parameter to match pandas.

Returns

**copy**Series

Examples

```
>>> s = ps.Series([1, 2], index=["a", "b"])
>>> s
a    1
b    2
dtype: int64
>>> s_copy = s.copy()
>>> s_copy
a    1
b    2
dtype: int64

```


# pyspark.pandas.Series.bool — PySpark 4.0.1 documentation
Series.bool()
[#](#pyspark.pandas.Series.bool "Permalink to this definition")

Return the bool of a single element in the current object.

This must be a boolean scalar value, either True or False. Raise a ValueError if the object does not have exactly 1 element, or that element is not boolean

Deprecated since version 4.0.0.

Returns

bool

Examples

```
>>> ps.DataFrame({'a': [True]}).bool()
True

```


```
>>> ps.Series([False]).bool()
False

```


If there are non-boolean or multiple values exist, it raises an exception in all cases as below.

```
>>> ps.DataFrame({'a': ['a']}).bool()
Traceback (most recent call last):
  ...
ValueError: bool cannot act on a non-boolean single element DataFrame

```


```
>>> ps.DataFrame({'a': [True], 'b': [False]}).bool()  
Traceback (most recent call last):
  ...
ValueError: The truth value of a DataFrame is ambiguous. Use a.empty, a.bool(),
a.item(), a.any() or a.all().

```


```
>>> ps.Series([1]).bool()
Traceback (most recent call last):
  ...
ValueError: bool cannot act on a non-boolean single element DataFrame

```


# pyspark.pandas.Series.at — PySpark 4.0.1 documentation
_property_ Series.at[#](#pyspark.pandas.Series.at "Permalink to this definition")

Access a single value for a row/column label pair. If the index is not unique, all matching pairs are returned as an array. Like `loc`, in that both provide label-based lookups. Use `at` if you only need to get a single value in a DataFrame or Series.

Note

Unlike pandas, pandas-on-Spark only allows using `at` to get values but not to set them.

Note

Warning: If `row_index` matches a lot of rows, large amounts of data will be fetched, potentially causing your machine to run out of memory.

Raises

KeyError

When label does not exist in DataFrame

Examples

```
>>> psdf = ps.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
...                    index=[4, 5, 5], columns=['A', 'B', 'C'])
>>> psdf
    A   B   C
4   0   2   3
5   0   4   1
5  10  20  30

```


Get value at specified row/column pair

```
>>> int(psdf.at[4, 'B'])
2

```


Get array if an index occurs multiple times

```
>>> psdf.at[5, 'B']
array([ 4, 20])

```


# pyspark.pandas.Series.iat — PySpark 4.0.1 documentation
_property_ Series.iat[#](#pyspark.pandas.Series.iat "Permalink to this definition")

Access a single value for a row/column pair by integer position.

Like `iloc`, in that both provide integer-based lookups. Use `iat` if you only need to get or set a single value in a DataFrame or Series.

Raises

KeyError

When label does not exist in DataFrame

Examples

```
>>> df = ps.DataFrame([[0, 2, 3], [0, 4, 1], [10, 20, 30]],
...                   columns=['A', 'B', 'C'])
>>> df
    A   B   C
0   0   2   3
1   0   4   1
2  10  20  30

```


Get value at specified row/column pair

Get value within a series

```
>>> psser = ps.Series([1, 2, 3], index=[10, 20, 30])
>>> psser
10    1
20    2
30    3
dtype: int64

```
# pyspark.pandas.Series.loc — PySpark 4.0.1 documentation
_property_ Series.loc[#](#pyspark.pandas.Series.loc "Permalink to this definition")

Access a group of rows and columns by label(s) or a boolean Series.

`.loc[]` is primarily label based, but may also be used with a conditional boolean Series derived from the DataFrame or Series.

Allowed inputs are:

*   A single label, e.g. `5` or `'a'`, (note that `5` is interpreted as a _label_ of the index, and **never** as an integer position along the index) for column selection.
    
*   A list or array of labels, e.g. `['a', 'b', 'c']`.
    
*   A slice object with labels, e.g. `'a':'f'`.
    
*   A conditional boolean Series derived from the DataFrame or Series
    
*   A boolean array of the same length as the column axis being sliced, e.g. `[True, False, True]`.
    
*   An alignable boolean pandas Series to the column axis being sliced. The index of the key will be aligned before masking.
    

Not allowed inputs which pandas allows are:

*   A boolean array of the same length as the row axis being sliced, e.g. `[True, False, True]`.
    
*   A `callable` function with one argument (the calling Series, DataFrame or Panel) and that returns valid output for indexing (one of the above)
    

Note

MultiIndex is not supported yet.

Note

Note that contrary to usual python slices, **both** the start and the stop are included, and the step of the slice is not allowed.

Note

With a list or array of labels for row selection, pandas-on-Spark behaves as a filter without reordering by the labels.

See also

[`Series.loc`](#pyspark.pandas.Series.loc "pyspark.pandas.Series.loc")

Access group of values using labels.

Examples

**Getting values**

```
>>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
...                   index=['cobra', 'viper', 'sidewinder'],
...                   columns=['max_speed', 'shield'])
>>> df
            max_speed  shield
cobra               1       2
viper               4       5
sidewinder          7       8

```


Single label. Note this returns the row as a Series.

```
>>> df.loc['viper']
max_speed    4
shield       5
Name: viper, dtype: int64

```


List of labels. Note using `[[]]` returns a DataFrame. Also note that pandas-on-Spark behaves just a filter without reordering by the labels.

```
>>> df.loc[['viper', 'sidewinder']]
            max_speed  shield
viper               4       5
sidewinder          7       8

```


```
>>> df.loc[['sidewinder', 'viper']]
            max_speed  shield
viper               4       5
sidewinder          7       8

```


Single label for column.

```
>>> int(df.loc['cobra', 'shield'])
2

```


List of labels for row.

```
>>> df.loc[['cobra'], 'shield']
cobra    2
Name: shield, dtype: int64

```


List of labels for column.

```
>>> df.loc['cobra', ['shield']]
shield    2
Name: cobra, dtype: int64

```


List of labels for both row and column.

```
>>> df.loc[['cobra'], ['shield']]
       shield
cobra       2

```


Slice with labels for row and single label for column. Note that both the start and stop of the slice are included.

```
>>> df.loc['cobra':'viper', 'max_speed']
cobra    1
viper    4
Name: max_speed, dtype: int64

```


Conditional that returns a boolean Series

```
>>> df.loc[df['shield'] > 6]
            max_speed  shield
sidewinder          7       8

```


Conditional that returns a boolean Series with column labels specified

```
>>> df.loc[df['shield'] > 6, ['max_speed']]
            max_speed
sidewinder          7

```


A boolean array of the same length as the column axis being sliced.

```
>>> df.loc[:, [False, True]]
            shield
cobra            2
viper            5
sidewinder       8

```


An alignable boolean Series to the column axis being sliced.

```
>>> df.loc[:, pd.Series([False, True], index=['max_speed', 'shield'])]
            shield
cobra            2
viper            5
sidewinder       8

```


**Setting values**

Setting value for all items matching the list of labels.

```
>>> df.loc[['viper', 'sidewinder'], ['shield']] = 50
>>> df
            max_speed  shield
cobra               1       2
viper               4      50
sidewinder          7      50

```


Setting value for an entire row

```
>>> df.loc['cobra'] = 10
>>> df
            max_speed  shield
cobra              10      10
viper               4      50
sidewinder          7      50

```


Set value for an entire column

```
>>> df.loc[:, 'max_speed'] = 30
>>> df
            max_speed  shield
cobra              30      10
viper              30      50
sidewinder         30      50

```


Set value for an entire list of columns

```
>>> df.loc[:, ['max_speed', 'shield']] = 100
>>> df
            max_speed  shield
cobra             100     100
viper             100     100
sidewinder        100     100

```


Set value with Series

```
>>> df.loc[:, 'shield'] = df['shield'] * 2
>>> df
            max_speed  shield
cobra             100     200
viper             100     200
sidewinder        100     200

```


**Getting values on a DataFrame with an index that has integer labels**

Another example using integers for the index

```
>>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
...                   index=[7, 8, 9],
...                   columns=['max_speed', 'shield'])
>>> df
   max_speed  shield
7          1       2
8          4       5
9          7       8

```


Slice with integer labels for rows. Note that both the start and stop of the slice are included.

```
>>> df.loc[7:9]
   max_speed  shield
7          1       2
8          4       5
9          7       8

```

# pyspark.pandas.Series.iloc — PySpark 4.0.1 documentation
_property_ Series.iloc[#](#pyspark.pandas.Series.iloc "Permalink to this definition")

Purely integer-location based indexing for selection by position.

`.iloc[]` is primarily integer position based (from `0` to `length-1` of the axis), but may also be used with a conditional boolean Series.

Allowed inputs are:

*   An integer for column selection, e.g. `5`.
    
*   A list or array of integers for row selection with distinct index values, e.g. `[3, 4, 0]`
    
*   A list or array of integers for column selection, e.g. `[4, 3, 0]`.
    
*   A boolean array for column selection.
    
*   A slice object with ints for row and column selection, e.g. `1:7`.
    

Not allowed inputs which pandas allows are:

*   A list or array of integers for row selection with duplicated indexes, e.g. `[4, 4, 0]`.
    
*   A boolean array for row selection.
    
*   A `callable` function with one argument (the calling Series, DataFrame or Panel) and that returns valid output for indexing (one of the above). This is useful in method chains when you don’t have a reference to the calling object but would like to base your selection on some value.
    

`.iloc` will raise `IndexError` if a requested indexer is out-of-bounds, except _slice_ indexers which allow out-of-bounds indexing (this conforms with python/numpy _slice_ semantics).

See also

[`DataFrame.loc`](about:blank/pyspark.pandas.DataFrame.loc.html#pyspark.pandas.DataFrame.loc "pyspark.pandas.DataFrame.loc")

Purely label-location based indexer for selection by label.

[`Series.iloc`](#pyspark.pandas.Series.iloc "pyspark.pandas.Series.iloc")

Purely integer-location based indexing for selection by position.

Examples

```
>>> mydict = [{'a': 1, 'b': 2, 'c': 3, 'd': 4},
...           {'a': 100, 'b': 200, 'c': 300, 'd': 400},
...           {'a': 1000, 'b': 2000, 'c': 3000, 'd': 4000 }]
>>> df = ps.DataFrame(mydict, columns=['a', 'b', 'c', 'd'])
>>> df
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

```


**Indexing just the rows**

A scalar integer for row selection.

```
>>> df.iloc[1]
a    100
b    200
c    300
d    400
Name: 1, dtype: int64

```


```
>>> df.iloc[[0]]
   a  b  c  d
0  1  2  3  4

```


With a slice object.

```
>>> df.iloc[:3]
      a     b     c     d
0     1     2     3     4
1   100   200   300   400
2  1000  2000  3000  4000

```


**Indexing both axes**

You can mix the indexer types for the index and columns. Use `:` to select the entire axis.

With scalar integers.

```
>>> df.iloc[:1, 1]
0    2
Name: b, dtype: int64

```


With lists of integers.

```
>>> df.iloc[:2, [1, 3]]
     b    d
0    2    4
1  200  400

```


With slice objects.

```
>>> df.iloc[:2, 0:3]
     a    b    c
0    1    2    3
1  100  200  300

```


With a boolean array whose length matches the columns.

```
>>> df.iloc[:, [True, False, True, False]]
      a     c
0     1     3
1   100   300
2  1000  3000

```


**Setting values**

Setting value for all items matching the list of labels.

```
>>> df.iloc[[1, 2], [1]] = 50
>>> df
      a   b     c     d
0     1   2     3     4
1   100  50   300   400
2  1000  50  3000  4000

```


Setting value for an entire row

```
>>> df.iloc[0] = 10
>>> df
      a   b     c     d
0    10  10    10    10
1   100  50   300   400
2  1000  50  3000  4000

```


Set value for an entire column

```
>>> df.iloc[:, 2] = 30
>>> df
      a   b   c     d
0    10  10  30    10
1   100  50  30   400
2  1000  50  30  4000

```


Set value for an entire list of columns

```
>>> df.iloc[:, [2, 3]] = 100
>>> df
      a   b    c    d
0    10  10  100  100
1   100  50  100  100
2  1000  50  100  100

```


Set value with Series

```
>>> df.iloc[:, 3] = df.iloc[:, 3] * 2
>>> df
      a   b    c    d
0    10  10  100  200
1   100  50  100  200
2  1000  50  100  200

```


# pyspark.pandas.Series.keys — PySpark 4.0.1 documentation
Series.keys()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.keys)
[#](#pyspark.pandas.Series.keys "Permalink to this definition")

Return alias for index.

Returns

Index

Index of the Series.

Examples

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> psser = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3], index=midx)

```


```
>>> psser.keys()  
MultiIndex([(  'lama',  'speed'),
            (  'lama', 'weight'),
            (  'lama', 'length'),
            (   'cow',  'speed'),
            (   'cow', 'weight'),
            (   'cow', 'length'),
            ('falcon',  'speed'),
            ('falcon', 'weight'),
            ('falcon', 'length')],
           )

```



# pyspark.pandas.Series.pop — PySpark 4.0.1 documentation
Series.pop(_item_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.pop)
[#](#pyspark.pandas.Series.pop "Permalink to this definition")

Return item and drop from series.

Parameters

**item**label

Label of index to be popped.

Returns

Value that is popped from series.

Examples

```
>>> s = ps.Series(data=np.arange(3), index=['A', 'B', 'C'])
>>> s
A    0
B    1
C    2
dtype: int64

```


```
>>> s
B    1
C    2
dtype: int64

```


```
>>> s = ps.Series(data=np.arange(3), index=['A', 'A', 'C'])
>>> s
A    0
A    1
C    2
dtype: int64

```


```
>>> s.pop('A')
A    0
A    1
dtype: int64

```


Also support for MultiIndex

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
...               index=midx)
>>> s
lama    speed      45.0
        weight    200.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.pop('lama')
speed      45.0
weight    200.0
length      1.2
dtype: float64

```


```
>>> s
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


Also support for MultiIndex with several indexes.

```
>>> midx = pd.MultiIndex([['a', 'b', 'c'],
...                       ['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 0, 0, 0, 1, 1, 1],
...                       [0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 0, 2]]
...  )
>>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
...              index=midx)
>>> s
a  lama    speed      45.0
           weight    200.0
           length      1.2
   cow     speed      30.0
           weight    250.0
           length      1.5
b  falcon  speed     320.0
           speed       1.0
           length      0.3
dtype: float64

```


```
>>> s.pop(('a', 'lama'))
speed      45.0
weight    200.0
length      1.2
dtype: float64

```


```
>>> s
a  cow     speed      30.0
           weight    250.0
           length      1.5
b  falcon  speed     320.0
           speed       1.0
           length      0.3
dtype: float64

```


```
>>> s.pop(('b', 'falcon', 'speed'))
(b, falcon, speed)    320.0
(b, falcon, speed)      1.0
dtype: float64

```


# pyspark.pandas.Series.items — PySpark 4.0.1 documentation
Series.items()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.items)
[#](#pyspark.pandas.Series.items "Permalink to this definition")

Lazily iterate over (index, value) tuples.

This method returns an iterable tuple (index, value). This is convenient if you want to create a lazy iterator.

Note

Unlike pandas’, the itmes in pandas-on-Spark returns generator rather zip object

Returns

iterable

Iterable of tuples containing the (index, value) pairs from a Series.

Examples

```
>>> s = ps.Series(['A', 'B', 'C'])
>>> for index, value in s.items():
...     print("Index : {}, Value : {}".format(index, value))
Index : 0, Value : A
Index : 1, Value : B
Index : 2, Value : C

```


# pyspark.pandas.Series.item — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.item

Series.item()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.item)
[#](#pyspark.pandas.Series.item "Permalink to this definition")

Return the first element of the underlying data as a Python scalar.

Returns

scalar

The first element of Series.

Raises

ValueError

If the data is not length-1.

Examples

```
>>> psser = ps.Series([10])
>>> psser.item()
10

```

# pyspark.pandas.Series.xs — PySpark 4.0.1 documentation
Series.xs(_key_, _level\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.xs)
[#](#pyspark.pandas.Series.xs "Permalink to this definition")

Return cross-section from the Series.

This method takes a key argument to select data at a particular level of a MultiIndex.

Parameters

**key**label or tuple of label

Label contained in the index, or partially in a MultiIndex.

**level**object, defaults to first n levels (n=1 or len(key))

In case of a key partially contained in a MultiIndex, indicate which levels are used. Levels can be referred by label or position.

Returns

Series

Cross-section from the original Series corresponding to the selected index levels.

Examples

```
>>> midx = pd.MultiIndex([['a', 'b', 'c'],
...                       ['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
...               index=midx)
>>> s
a  lama    speed      45.0
           weight    200.0
           length      1.2
b  cow     speed      30.0
           weight    250.0
           length      1.5
c  falcon  speed     320.0
           weight      1.0
           length      0.3
dtype: float64

```


Get values at specified index

```
>>> s.xs('a')
lama  speed      45.0
      weight    200.0
      length      1.2
dtype: float64

```


Get values at several indexes

```
>>> s.xs(('a', 'lama'))
speed      45.0
weight    200.0
length      1.2
dtype: float64

```


Get values at specified index and level

```
>>> s.xs('lama', level=1)
a  speed      45.0
   weight    200.0
   length      1.2
dtype: float64

```


# pyspark.pandas.Series.get — PySpark 4.0.1 documentation
Series.get(_key_, _default\=None_)
[#](#pyspark.pandas.Series.get "Permalink to this definition")

Get item from object for given key (DataFrame column, Panel slice, etc.). Returns default value if not found.

Parameters

**key: object**

Returns

value: same type as items contained in object

Examples

```
>>> df = ps.DataFrame({'x':range(3), 'y':['a','b','b'], 'z':['a','b','b']},
...                   columns=['x', 'y', 'z'], index=[10, 20, 20])
>>> df
    x  y  z
10  0  a  a
20  1  b  b
20  2  b  b

```


```
>>> df.get('x')
10    0
20    1
20    2
Name: x, dtype: int64

```


```
>>> df.get(['x', 'y'])
    x  y
10  0  a
20  1  b
20  2  b

```


```
>>> df.x.get(20)
20    1
20    2
Name: x, dtype: int64

```



# pyspark.pandas.Series.add — PySpark 4.0.1 documentation
Series.add(_other_, _fill\_value\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.add)
[#](#pyspark.pandas.Series.add "Permalink to this definition")

Return Addition of series and other, element-wise (binary operator +).

Equivalent to `series + other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.add(df.b)
a    4.0
b    NaN
c    6.0
d    NaN
dtype: float64

```


```
>>> df.a.radd(df.b)
a    4.0
b    NaN
c    6.0
d    NaN
dtype: float64

```

# pyspark.pandas.Series.div — PySpark 4.0.1 documentation
Series.div(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.div)
[#](#pyspark.pandas.Series.div "Permalink to this definition")

Return Floating division of series and other, element-wise (binary operator /).

Equivalent to `series / other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.divide(df.b)
a    1.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rdiv(df.b)
a    1.0
b    NaN
c    0.5
d    NaN
dtype: float64

```



# pyspark.pandas.Series.mul — PySpark 4.0.1 documentation
Series.mul(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.mul)
[#](#pyspark.pandas.Series.mul "Permalink to this definition")

Return Multiplication of series and other, element-wise (binary operator \*).

Equivalent to `series * other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.multiply(df.b)
a    4.0
b    NaN
c    8.0
d    NaN
dtype: float64

```


```
>>> df.a.rmul(df.b)
a    4.0
b    NaN
c    8.0
d    NaN
dtype: float64

```


# pyspark.pandas.Series.radd — PySpark 4.0.1 documentation
Series.radd(_other_, _fill\_value\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.radd)
[#](#pyspark.pandas.Series.radd "Permalink to this definition")

Return Reverse Addition of series and other, element-wise (binary operator +).

Equivalent to `other + series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.add(df.b)
a    4.0
b    NaN
c    6.0
d    NaN
dtype: float64

```


```
>>> df.a.radd(df.b)
a    4.0
b    NaN
c    6.0
d    NaN
dtype: float64

```


# pyspark.pandas.Series.rdiv — PySpark 4.0.1 documentation
Series.rdiv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rdiv)
[#](#pyspark.pandas.Series.rdiv "Permalink to this definition")

Return Reverse Floating division of series and other, element-wise (binary operator /).

Equivalent to `other / series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.divide(df.b)
a    1.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rdiv(df.b)
a    1.0
b    NaN
c    0.5
d    NaN
dtype: float64

```



# pyspark.pandas.Series.rmul — PySpark 4.0.1 documentation
Series.rmul(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rmul)
[#](#pyspark.pandas.Series.rmul "Permalink to this definition")

Return Reverse Multiplication of series and other, element-wise (binary operator \*).

Equivalent to `other * series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.multiply(df.b)
a    4.0
b    NaN
c    8.0
d    NaN
dtype: float64

```


```
>>> df.a.rmul(df.b)
a    4.0
b    NaN
c    8.0
d    NaN
dtype: float64

```



# pyspark.pandas.Series.rsub — PySpark 4.0.1 documentation
Series.rsub(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rsub)
[#](#pyspark.pandas.Series.rsub "Permalink to this definition")

Return Reverse Subtraction of series and other, element-wise (binary operator \-).

Equivalent to `other - series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.subtract(df.b)
a    0.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rsub(df.b)
a    0.0
b    NaN
c   -2.0
d    NaN
dtype: float64

```
# pyspark.pandas.Series.rtruediv — PySpark 4.0.1 documentation
Series.rtruediv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rtruediv)
[#](#pyspark.pandas.Series.rtruediv "Permalink to this definition")

Return Reverse Floating division of series and other, element-wise (binary operator /).

Equivalent to `other / series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.divide(df.b)
a    1.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rdiv(df.b)
a    1.0
b    NaN
c    0.5
d    NaN
dtype: float64

```

# pyspark.pandas.Series.sub — PySpark 4.0.1 documentation
Series.sub(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.sub)
[#](#pyspark.pandas.Series.sub "Permalink to this definition")

Return Subtraction of series and other, element-wise (binary operator \-).

Equivalent to `series - other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.subtract(df.b)
a    0.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rsub(df.b)
a    0.0
b    NaN
c   -2.0
d    NaN
dtype: float64

```


# pyspark.pandas.Series.truediv — PySpark 4.0.1 documentation
Series.truediv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.truediv)
[#](#pyspark.pandas.Series.truediv "Permalink to this definition")

Return Floating division of series and other, element-wise (binary operator /).

Equivalent to `series / other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.divide(df.b)
a    1.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rdiv(df.b)
a    1.0
b    NaN
c    0.5
d    NaN
dtype: float64

```


# pyspark.pandas.Series.pow — PySpark 4.0.1 documentation
Series.pow(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.pow)
[#](#pyspark.pandas.Series.pow "Permalink to this definition")

Return Exponential power of series of series and other, element-wise (binary operator \*\*).

Equivalent to `series ** other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.pow(df.b)
a     4.0
b     NaN
c    16.0
d     NaN
dtype: float64

```


```
>>> df.a.rpow(df.b)
a     4.0
b     NaN
c    16.0
d     NaN
dtype: float64

```

# pyspark.pandas.Series.rpow — PySpark 4.0.1 documentation
Series.rpow(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rpow)
[#](#pyspark.pandas.Series.rpow "Permalink to this definition")

Return Reverse Exponential power of series and other, element-wise (binary operator \*\*).

Equivalent to `other ** series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.pow(df.b)
a     4.0
b     NaN
c    16.0
d     NaN
dtype: float64

```


```
>>> df.a.rpow(df.b)
a     4.0
b     NaN
c    16.0
d     NaN
dtype: float64

```


# pyspark.pandas.Series.mod — PySpark 4.0.1 documentation
Series.mod(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.mod)
[#](#pyspark.pandas.Series.mod "Permalink to this definition")

Return Modulo of series and other, element-wise (binary operator %).

Equivalent to `series % other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.mod(df.b)
a    0.0
b    NaN
c    0.0
d    NaN
dtype: float64

```


```
>>> df.a.rmod(df.b)
a    0.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


# pyspark.pandas.Series.mod — PySpark 4.0.1 documentation
Series.mod(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.mod)
[#](#pyspark.pandas.Series.mod "Permalink to this definition")

Return Modulo of series and other, element-wise (binary operator %).

Equivalent to `series % other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.mod(df.b)
a    0.0
b    NaN
c    0.0
d    NaN
dtype: float64

```


```
>>> df.a.rmod(df.b)
a    0.0
b    NaN
c    2.0
d    NaN
dtype: float64

```



# pyspark.pandas.Series.floordiv — PySpark 4.0.1 documentation
Series.floordiv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.floordiv)
[#](#pyspark.pandas.Series.floordiv "Permalink to this definition")

Return Integer division of series and other, element-wise (binary operator //).

Equivalent to `series // other`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.floordiv(df.b)
a    1.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rfloordiv(df.b)
a    1.0
b    NaN
c    0.0
d    NaN
dtype: float64

```

# pyspark.pandas.Series.rfloordiv — PySpark 4.0.1 documentation
Series.rfloordiv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rfloordiv)
[#](#pyspark.pandas.Series.rfloordiv "Permalink to this definition")

Return Reverse Integer division of series and other, element-wise (binary operator //).

Equivalent to `other // series`

Parameters

**other**Series or scalar value

**fill\_value**Scalar value, default None

Returns

Series

The result of the operation.

Examples

```
>>> df = ps.DataFrame({'a': [2, 2, 4, np.nan],
...                    'b': [2, np.nan, 2, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])
>>> df
     a    b
a  2.0  2.0
b  2.0  NaN
c  4.0  2.0
d  NaN  NaN

```


```
>>> df.a.floordiv(df.b)
a    1.0
b    NaN
c    2.0
d    NaN
dtype: float64

```


```
>>> df.a.rfloordiv(df.b)
a    1.0
b    NaN
c    0.0
d    NaN
dtype: float64

```

# pyspark.pandas.Series.divmod — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.divmod

Series.divmod(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.divmod)
[#](#pyspark.pandas.Series.divmod "Permalink to this definition")

Return Integer division and modulo of series and other, element-wise (binary operator divmod).

Parameters

**other**Series or scalar value

Returns

2-Tuple of Series

The result of the operation.



# pyspark.pandas.Series.rdivmod — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.rdivmod

Series.rdivmod(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rdivmod)
[#](#pyspark.pandas.Series.rdivmod "Permalink to this definition")

Return Integer division and modulo of series and other, element-wise (binary operator rdivmod).

Parameters

**other**Series or scalar value

Returns

2-Tuple of Series

The result of the operation.



# pyspark.pandas.Series.combine_first — PySpark 4.0.1 documentation
Series.combine\_first(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.combine_first)
[#](#pyspark.pandas.Series.combine_first "Permalink to this definition")

Combine Series values, choosing the calling Series’s values first.

Parameters

**other**Series

The value(s) to be combined with the Series.

Returns

Series

The result of combining the Series with the other object.

See also

`Series.combine`

Perform element-wise operation on two Series using a given function.

Notes

Result index will be the union of the two indexes.

Examples

```
>>> s1 = ps.Series([1, np.nan])
>>> s2 = ps.Series([3, 4])
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.combine_first(s2)
0    1.0
1    4.0
dtype: float64

```

# pyspark.pandas.Series.lt — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.lt

Series.lt(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.lt)
[#](#pyspark.pandas.Series.lt "Permalink to this definition")

Compare if the current value is less than the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a < 1
a    False
b    False
c    False
d    False
Name: a, dtype: bool

```


```
>>> df.b.lt(2)
a     True
b    False
c     True
d    False
Name: b, dtype: bool

```



# pyspark.pandas.Series.gt — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.gt

Series.gt(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.gt)
[#](#pyspark.pandas.Series.gt "Permalink to this definition")

Compare if the current value is greater than the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a > 1
a    False
b     True
c     True
d     True
Name: a, dtype: bool

```


```
>>> df.b.gt(1)
a    False
b    False
c    False
d    False
Name: b, dtype: bool

```

# pyspark.pandas.Series.le — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.le

Series.le(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.le)
[#](#pyspark.pandas.Series.le "Permalink to this definition")

Compare if the current value is less than or equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a <= 2
a     True
b     True
c    False
d    False
Name: a, dtype: bool

```


```
>>> df.b.le(2)
a     True
b    False
c     True
d    False
Name: b, dtype: bool

```

# pyspark.pandas.Series.ge — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.ge

Series.ge(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.ge)
[#](#pyspark.pandas.Series.ge "Permalink to this definition")

Compare if the current value is greater than or equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a >= 2
a    False
b     True
c     True
d     True
Name: a, dtype: bool

```


```
>>> df.b.ge(2)
a    False
b    False
c    False
d    False
Name: b, dtype: bool

```



# pyspark.pandas.Series.ne — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.ne

Series.ne(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.ne)
[#](#pyspark.pandas.Series.ne "Permalink to this definition")

Compare if the current value is not equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a != 1
a    False
b     True
c     True
d     True
Name: a, dtype: bool

```


```
>>> df.b.ne(1)
a    False
b     True
c    False
d     True
Name: b, dtype: bool

```


# pyspark.pandas.Series.eq — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.eq

Series.eq(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.eq)
[#](#pyspark.pandas.Series.eq "Permalink to this definition")

Compare if the current value is equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a == 1
a     True
b    False
c    False
d    False
Name: a, dtype: bool

```


```
>>> df.b.eq(1)
a     True
b    False
c     True
d    False
Name: b, dtype: bool

```

# pyspark.pandas.Series.product — PySpark 4.0.1 documentation
Series.product(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _min\_count\=0_)
[#](#pyspark.pandas.Series.product "Permalink to this definition")

Return the product of the values.

Note

unlike pandas’, pandas-on-Spark’s emulates product by `exp(sum(log(...)))` trick. Therefore, it only works for positive numbers.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

**min\_count: int, default 0**

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

Examples

On a DataFrame:

Non-numeric type column is not included to the result.

```
>>> psdf = ps.DataFrame({'A': [1, 2, 3, 4, 5],
...                     'B': [10, 20, 30, 40, 50],
...                     'C': ['a', 'b', 'c', 'd', 'e']})
>>> psdf
   A   B  C
0  1  10  a
1  2  20  b
2  3  30  c
3  4  40  d
4  5  50  e

```


```
>>> psdf.prod()
A         120
B    12000000
dtype: int64

```


If there is no numeric type columns, returns empty Series.

```
>>> ps.DataFrame({"key": ['a', 'b', 'c'], "val": ['x', 'y', 'z']}).prod()  
Series([], dtype: float64)

```


On a Series:

```
>>> ps.Series([1, 2, 3, 4, 5]).prod()
120

```


By default, the product of an empty or all-NA Series is `1`

```
>>> ps.Series([]).prod()  
1.0

```


This can be controlled with the `min_count` parameter

```
>>> ps.Series([]).prod(min_count=1)  
nan

```


# pyspark.pandas.Series.dot — PySpark 4.0.1 documentation
Series.dot(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.dot)
[#](#pyspark.pandas.Series.dot "Permalink to this definition")

Compute the dot product between the Series and the columns of other.

This method computes the dot product between the Series and another one, or the Series and each columns of a DataFrame.

It can also be called using self @ other in Python >= 3.5.

Note

This API is slightly different from pandas when indexes from both Series are not aligned and config ‘compute.eager\_check’ is False. pandas raise an exception; however, pandas-on-Spark just proceeds and performs by ignoring mismatches with NaN permissively.

```
>>> pdf1 = pd.Series([1, 2, 3], index=[0, 1, 2])
>>> pdf2 = pd.Series([1, 2, 3], index=[0, 1, 3])
>>> pdf1.dot(pdf2)  
...
ValueError: matrices are not aligned

```


```
>>> psdf1 = ps.Series([1, 2, 3], index=[0, 1, 2])
>>> psdf2 = ps.Series([1, 2, 3], index=[0, 1, 3])
>>> with ps.option_context("compute.eager_check", False):
...     psdf1.dot(psdf2)  
...
5

```


Parameters

**other**Series, DataFrame.

The other object to compute the dot product with its columns.

Returns

scalar, Series

Return the dot product of the Series and other if other is a Series, the Series of the dot product of Series and each row of other if other is a DataFrame.

Notes

The Series and other must share the same index if other are a Series or a DataFrame.

Examples

```
>>> s = ps.Series([0, 1, 2, 3])

```


```
>>> psdf = ps.DataFrame({'x': [0, 1, 2, 3], 'y': [0, -1, -2, -3]})
>>> psdf
   x  y
0  0  0
1  1 -1
2  2 -2
3  3 -3

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s.dot(psdf)
...
x    14
y   -14
dtype: int64

```


# pyspark.pandas.Series.apply — PySpark 4.0.1 documentation
Series.apply(_func_, _args\=()_, _\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.apply)
[#](#pyspark.pandas.Series.apply "Permalink to this definition")

Invoke function on values of Series.

Can be a Python function that only works on the Series.

Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def square(x) -> np.int32:
...     return x ** 2

```


pandas-on-Spark uses return type hint and does not try to infer the type.

Parameters

**func**function

Python function to apply. Note that type hint for return type is required.

**args**tuple

Positional arguments passed to func after the series value.

**\*\*kwds**

Additional keyword arguments passed to func.

Returns

Series

Examples

Create a Series with typical summer temperatures for each city.

```
>>> s = ps.Series([20, 21, 12],
...               index=['London', 'New York', 'Helsinki'])
>>> s
London      20
New York    21
Helsinki    12
dtype: int64

```


Square the values by defining a function and passing it as an argument to `apply()`.

```
>>> def square(x) -> np.int64:
...     return x ** 2
>>> s.apply(square)
London      400
New York    441
Helsinki    144
dtype: int64

```


Define a custom function that needs additional positional arguments and pass these additional arguments using the `args` keyword

```
>>> def subtract_custom_value(x, custom_value) -> np.int64:
...     return x - custom_value

```


```
>>> s.apply(subtract_custom_value, args=(5,))
London      15
New York    16
Helsinki     7
dtype: int64

```


Define a custom function that takes keyword arguments and pass these arguments to `apply`

```
>>> def add_custom_values(x, **kwargs) -> np.int64:
...     for month in kwargs:
...         x += kwargs[month]
...     return x

```


```
>>> s.apply(add_custom_values, june=30, july=20, august=25)
London      95
New York    96
Helsinki    87
dtype: int64

```


Use a function from the Numpy library

```
>>> def numpy_log(col) -> np.float64:
...     return np.log(col)
>>> s.apply(numpy_log)
London      2.995732
New York    3.044522
Helsinki    2.484907
dtype: float64

```


You can omit the type hint and let pandas-on-Spark infer its type.

```
>>> s.apply(np.log)
London      2.995732
New York    3.044522
Helsinki    2.484907
dtype: float64

```



# pyspark.pandas.Series.agg — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.agg

Series.agg(_func_)
[#](#pyspark.pandas.Series.agg "Permalink to this definition")

Aggregate using one or more operations over the specified axis.

Parameters

**func**str or a list of str

function name(s) as string apply to series.

Returns

scalar, Series

The return can be: - scalar : when Series.agg is called with single function - Series : when Series.agg is called with several functions

Notes

agg is an alias for aggregate. Use the alias.

Examples

```
>>> s = ps.Series([1, 2, 3, 4])
>>> s.agg('min')
1

```


```
>>> s.agg(['min', 'max']).sort_index()
max    4
min    1
dtype: int64

```


# pyspark.pandas.Series.aggregate — PySpark 4.0.1 documentation
Series.aggregate(_func_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.aggregate)
[#](#pyspark.pandas.Series.aggregate "Permalink to this definition")

Aggregate using one or more operations over the specified axis.

Parameters

**func**str or a list of str

function name(s) as string apply to series.

Returns

scalar, Series

The return can be: - scalar : when Series.agg is called with single function - Series : when Series.agg is called with several functions

Notes

agg is an alias for aggregate. Use the alias.

Examples

```
>>> s = ps.Series([1, 2, 3, 4])
>>> s.agg('min')
1

```


```
>>> s.agg(['min', 'max']).sort_index()
max    4
min    1
dtype: int64

```




# pyspark.pandas.Series.transform — PySpark 4.0.1 documentation
Series.transform(_func_, _axis\=0_, _\*args_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.transform)
[#](#pyspark.pandas.Series.transform "Permalink to this definition")

Call `func` producing the same type as self with transformed values and that has the same axis length as input.

Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def square(x) -> np.int32:
...     return x ** 2

```


pandas-on-Spark uses return type hint and does not try to infer the type.

Parameters

**func**function or list

A function or a list of functions to use for transforming the data.

**axis**int, default 0 or ‘index’

Can only be set to 0 now.

**\*args**

Positional arguments to pass to func.

**\*\*kwargs**

Keyword arguments to pass to func.

Returns

An instance of the same type with self that must have the same length as input.

Examples

```
>>> s = ps.Series(range(3))
>>> s
0    0
1    1
2    2
dtype: int64

```


```
>>> def sqrt(x) -> float:
...     return np.sqrt(x)
>>> s.transform(sqrt)
0    0.000000
1    1.000000
2    1.414214
dtype: float64

```


Even though the resulting instance must have the same length as the input, it is possible to provide several input functions:

```
>>> def exp(x) -> float:
...     return np.exp(x)
>>> s.transform([sqrt, exp])
       sqrt       exp
0  0.000000  1.000000
1  1.000000  2.718282
2  1.414214  7.389056

```


You can omit the type hint and let pandas-on-Spark infer its type.

```
>>> s.transform([np.sqrt, np.exp])
       sqrt       exp
0  0.000000  1.000000
1  1.000000  2.718282
2  1.414214  7.389056

```


# pyspark.pandas.Series.map — PySpark 4.0.1 documentation
Series.map(_arg_, _na\_action\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.map)
[#](#pyspark.pandas.Series.map "Permalink to this definition")

Map values of Series according to input correspondence.

Used for substituting each value in a Series with another value, that may be derived from a function, a `dict`.

Note

make sure the size of the dictionary is not huge because it could downgrade the performance or throw OutOfMemoryError due to a huge expression within Spark. Consider the input as a function as an alternative instead in this case.

Parameters

**arg**function, dict or pd.Series

Mapping correspondence.

**na\_action**

If ignore, propagate NA values, without passing them to the mapping correspondence.

Returns

Series

Same index as caller.

Notes

When `arg` is a dictionary, values in Series that are not in the dictionary (as keys) is converted to `None`. However, if the dictionary is a `dict` subclass that defines `__missing__` (i.e. provides a method for default values), then this default is used rather than `None`.

Examples

```
>>> s = ps.Series(['cat', 'dog', None, 'rabbit'])
>>> s
0       cat
1       dog
2      None
3    rabbit
dtype: object

```


`map` accepts a `dict`. Values that are not found in the `dict` are converted to `None`, unless the dict has a default value (e.g. `defaultdict`):

```
>>> s.map({'cat': 'kitten', 'dog': 'puppy'})
0    kitten
1     puppy
2      None
3      None
dtype: object

```


It also accepts a pandas Series:

```
>>> pser = pd.Series(['kitten', 'puppy'], index=['cat', 'dog'])
>>> s.map(pser)
0    kitten
1     puppy
2      None
3      None
dtype: object

```


It also accepts a function:

```
>>> def format(x) -> str:
...     return 'I am a {}'.format(x)

```


```
>>> s.map(format)
0       I am a cat
1       I am a dog
2      I am a None
3    I am a rabbit
dtype: object

```


To avoid applying the function to missing values (and keep them as NaN) na\_action=’ignore’ can be used:

```
>>> s.map('I am a {}'.format, na_action='ignore')
0       I am a cat
1       I am a dog
2             None
3    I am a rabbit
dtype: object

```


# pyspark.pandas.Series.groupby — PySpark 4.0.1 documentation
Series.groupby(_by_, _axis\=0_, _as\_index\=True_, _dropna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.groupby)
[#](#pyspark.pandas.Series.groupby "Permalink to this definition")

Group DataFrame or Series using one or more columns.

A groupby operation involves some combination of splitting the object, applying a function, and combining the results. This can be used to group large amounts of data and compute operations on these groups.

Parameters

**by: Series, label, or list of labels**

Used to determine the groups for the groupby. If Series is passed, the Series or dict VALUES will be used to determine the groups. A label or list of labels may be passed to group by the columns in `self`.

**axis: int, default 0 or ‘index’**

Can only be set to 0 now.

**as\_index: bool, default True**

For aggregated output, return object with group labels as the index. Only relevant for DataFrame input. as\_index=False is effectively “SQL-style” grouped output.

**dropna: bool, default True**

If True, and if group keys contain NA values, NA values together with row/column will be dropped. If False, NA values will also be treated as the key in groups.

Returns

DataFrameGroupBy or SeriesGroupBy

Depends on the calling object and returns groupby object that contains information about the groups.

See also

`pyspark.pandas.groupby.GroupBy`

Examples

```
>>> df = ps.DataFrame({'Animal': ['Falcon', 'Falcon',
...                               'Parrot', 'Parrot'],
...                    'Max Speed': [380., 370., 24., 26.]},
...                   columns=['Animal', 'Max Speed'])
>>> df
   Animal  Max Speed
0  Falcon      380.0
1  Falcon      370.0
2  Parrot       24.0
3  Parrot       26.0

```


```
>>> df.groupby(['Animal']).mean().sort_index()  
        Max Speed
Animal
Falcon      375.0
Parrot       25.0

```


```
>>> df.groupby(['Animal'], as_index=False).mean().sort_values('Animal')
... 
   Animal  Max Speed
...Falcon      375.0
...Parrot       25.0

```


We can also choose to include NA in group keys or not by setting dropna parameter, the default setting is True:

```
>>> l = [[1, 2, 3], [1, None, 4], [2, 1, 3], [1, 2, 2]]
>>> df = ps.DataFrame(l, columns=["a", "b", "c"])
>>> df.groupby(by=["b"]).sum().sort_index()  
     a  c
b
1.0  2  3
2.0  2  5

```


```
>>> df.groupby(by=["b"], dropna=False).sum().sort_index()  
     a  c
b
1.0  2  3
2.0  2  5
NaN  1  4

```


# pyspark.pandas.Series.rolling — PySpark 4.0.1 documentation
Series.rolling(_window_, _min\_periods\=None_)
[#](#pyspark.pandas.Series.rolling "Permalink to this definition")

Provide rolling transformations.

Note

‘min\_periods’ in pandas-on-Spark works as a fixed window size unlike pandas. Unlike pandas, NA is also counted as the period. This might be changed soon.

Parameters

**window: int, or offset**

Size of the moving window. This is the number of observations used for calculating the statistic. Each window will be a fixed size.

**min\_periods: int, default None**

Minimum number of observations in window required to have a value (otherwise result is NA). For a window that is specified by an offset, min\_periods will default to 1. Otherwise, min\_periods will default to the size of the window.

Returns

a Window sub-classed for the operation

# pyspark.pandas.Series.expanding — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.expanding

Series.expanding(_min\_periods\=1_)
[#](#pyspark.pandas.Series.expanding "Permalink to this definition")

Provide expanding transformations.

Note

‘min\_periods’ in pandas-on-Spark works as a fixed window size unlike pandas. Unlike pandas, NA is also counted as the period. This might be changed soon.

Parameters

**min\_periods: int, default 1**

Minimum number of observations in window required to have a value (otherwise result is NA).

Returns

a Window sub-classed for the operation


# pyspark.pandas.Series.pipe — PySpark 4.0.1 documentation
Series.pipe(_func_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.pipe "Permalink to this definition")

Apply func(self, \*args, \*\*kwargs).

Parameters

**func: function**

function to apply to the DataFrame. `args`, and `kwargs` are passed into `func`. Alternatively a `(callable, data_keyword)` tuple where `data_keyword` is a string indicating the keyword of `callable` that expects the DataFrames.

**args: iterable, optional**

positional arguments passed into `func`.

**kwargs: mapping, optional**

a dictionary of keyword arguments passed into `func`.

Returns

object: the return type of `func`.

Notes

Use `.pipe` when chaining together functions that expect Series, DataFrames or GroupBy objects. For example, given

```
>>> df = ps.DataFrame({'category': ['A', 'A', 'B'],
...                    'col1': [1, 2, 3],
...                    'col2': [4, 5, 6]},
...                   columns=['category', 'col1', 'col2'])
>>> def keep_category_a(df):
...     return df[df['category'] == 'A']
>>> def add_one(df, column):
...     return df.assign(col3=df[column] + 1)
>>> def multiply(df, column1, column2):
...     return df.assign(col4=df[column1] * df[column2])

```


instead of writing

```
>>> multiply(add_one(keep_category_a(df), column="col1"), column1="col2", column2="col3")
  category  col1  col2  col3  col4
0        A     1     4     2     8
1        A     2     5     3    15

```


You can write

```
>>> (df.pipe(keep_category_a)
...    .pipe(add_one, column="col1")
...    .pipe(multiply, column1="col2", column2="col3")
... )
  category  col1  col2  col3  col4
0        A     1     4     2     8
1        A     2     5     3    15

```


If you have a function that takes the data as the second argument, pass a tuple indicating which keyword expects the data. For example, suppose `f` takes its data as `df`:

```
>>> def multiply_2(column1, df, column2):
...     return df.assign(col4=df[column1] * df[column2])

```


Then you can write

```
>>> (df.pipe(keep_category_a)
...    .pipe(add_one, column="col1")
...    .pipe((multiply_2, 'df'), column1="col2", column2="col3")
... )
  category  col1  col2  col3  col4
0        A     1     4     2     8
1        A     2     5     3    15

```


You can use lambda as well

```
>>> ps.Series([1, 2, 3]).pipe(lambda x: (x + 1).rename("value"))
0    2
1    3
2    4
Name: value, dtype: int64

```


# pyspark.pandas.Series.abs — PySpark 4.0.1 documentation
Series.abs()
[#](#pyspark.pandas.Series.abs "Permalink to this definition")

Return a Series/DataFrame with absolute numeric value of each element.

Returns

abs: Series/DataFrame containing the absolute value of each element.

Examples

Absolute numeric values in a Series.

```
>>> s = ps.Series([-1.10, 2, -3.33, 4])
>>> s.abs()
0    1.10
1    2.00
2    3.33
3    4.00
dtype: float64

```


Absolute numeric values in a DataFrame.

```
>>> df = ps.DataFrame({
...     'a': [4, 5, 6, 7],
...     'b': [10, 20, 30, 40],
...     'c': [100, 50, -30, -50]
...   },
...   columns=['a', 'b', 'c'])
>>> df.abs()
   a   b    c
0  4  10  100
1  5  20   50
2  6  30   30
3  7  40   50

```


# pyspark.pandas.Series.all — PySpark 4.0.1 documentation
Series.all(_axis\=0_, _skipna\=True_)
[#](#pyspark.pandas.Series.all "Permalink to this definition")

Return whether all elements are True.

Returns True unless there at least one element within a series that is False or equivalent (e.g. zero or empty)

Parameters

**axis**{0 or ‘index’}, default 0

Indicate which axis or axes should be reduced.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    

**skipna**boolean, default True

Exclude NA values, such as None or numpy.NaN. If an entire row/column is NA values and skipna is True, then the result will be True, as for an empty row/column. If skipna is False, numpy.NaNs are treated as True because these are not equal to zero, Nones are treated as False.

Examples

```
>>> ps.Series([True, True]).all()
True

```


```
>>> ps.Series([True, False]).all()
False

```


```
>>> ps.Series([0, 1]).all()
False

```


```
>>> ps.Series([1, 2, 3]).all()
True

```


```
>>> ps.Series([True, True, None]).all()
True

```


```
>>> ps.Series([True, True, None]).all(skipna=False)
False

```


```
>>> ps.Series([True, False, None]).all()
False

```


```
>>> ps.Series([]).all()
True

```


```
>>> ps.Series([np.nan]).all()
True

```


```
>>> ps.Series([np.nan]).all(skipna=False)
True

```


```
>>> ps.Series([None]).all()
True

```


```
>>> ps.Series([None]).all(skipna=False)
False

```


```
>>> df = ps.Series([True, False, None]).rename("a").to_frame()
>>> df.set_index("a").index.all()
False

```


# pyspark.pandas.Series.any — PySpark 4.0.1 documentation
Series.any(_axis\=0_)
[#](#pyspark.pandas.Series.any "Permalink to this definition")

Return whether any element is True.

Returns False unless there is at least one element within a series that is True or equivalent (e.g. non-zero or non-empty).

Parameters

**axis**{0 or ‘index’}, default 0

Indicate which axis or axes should be reduced.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    

Examples

```
>>> ps.Series([False, False]).any()
False

```


```
>>> ps.Series([True, False]).any()
True

```


```
>>> ps.Series([0, 0]).any()
False

```


```
>>> ps.Series([0, 1, 2]).any()
True

```


```
>>> ps.Series([False, False, None]).any()
False

```


```
>>> ps.Series([True, False, None]).any()
True

```


```
>>> ps.Series([]).any()
False

```


```
>>> ps.Series([np.nan]).any()
False

```


```
>>> df = ps.Series([True, False, None]).rename("a").to_frame()
>>> df.set_index("a").index.any()
True

```


# pyspark.pandas.Series.autocorr — PySpark 4.0.1 documentation
Series.autocorr(_lag\=1_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.autocorr)
[#](#pyspark.pandas.Series.autocorr "Permalink to this definition")

Compute the lag-N autocorrelation.

This method computes the Pearson correlation between the Series and its shifted self.

Note

the current implementation of rank uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

New in version 3.4.0.

Parameters

**lag**int, default 1

Number of lags to apply before performing autocorrelation.

Returns

float

The Pearson correlation between self and self.shift(lag).

Notes

If the Pearson correlation is not well defined return ‘NaN’.

Examples

```
>>> s = ps.Series([.2, .0, .6, .2, np.nan, .5, .6])
>>> s.autocorr()  
-0.141219...
>>> s.autocorr(0)  
1.0...
>>> s.autocorr(2)  
0.970725...
>>> s.autocorr(-3)  
0.277350...
>>> s.autocorr(5)  
-1.000000...
>>> s.autocorr(6)  
nan

```


If the Pearson correlation is not well defined, then ‘NaN’ is returned.

```
>>> s = ps.Series([1, 0, 0, 0])
>>> s.autocorr()
nan

```

# pyspark.pandas.Series.between — PySpark 4.0.1 documentation
Series.between(_left_, _right_, _inclusive\='both'_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.between)
[#](#pyspark.pandas.Series.between "Permalink to this definition")

Return boolean Series equivalent to left <= series <= right. This function returns a boolean vector containing True wherever the corresponding Series element is between the boundary values left and right. NA values are treated as False.

Parameters

**left**scalar or list-like

Left boundary.

**right**scalar or list-like

Right boundary.

**inclusive**{“both”, “neither”, “left”, “right”}

Include boundaries. Whether to set each bound as closed or open.

Changed in version 4.0.0.

Returns

Series

Series representing whether each element is between left and right (inclusive).

See also

[`Series.gt`](about:blank/pyspark.pandas.Series.gt.html#pyspark.pandas.Series.gt "pyspark.pandas.Series.gt")

Greater than of series and other.

[`Series.lt`](about:blank/pyspark.pandas.Series.lt.html#pyspark.pandas.Series.lt "pyspark.pandas.Series.lt")

Less than of series and other.

Notes

This function is equivalent to `(left <= ser) & (ser <= right)`

Examples

```
>>> s = ps.Series([2, 0, 4, 8, np.nan])

```


Boundary values are included by default:

```
>>> s.between(0, 4)
0     True
1     True
2     True
3    False
4    False
dtype: bool

```


With inclusive set to “neither” boundary values are excluded:

```
>>> s.between(0, 4, inclusive="neither")
0     True
1    False
2    False
3    False
4    False
dtype: bool

```


With inclusive set to “right” only right boundary value is included:

```
>>> s.between(0, 4, inclusive="right")
0     True
1    False
2     True
3    False
4    False
dtype: bool

```


With inclusive set to “left” only left boundary value is included:

```
>>> s.between(0, 4, inclusive="left")
0     True
1     True
2    False
3    False
4    False
dtype: bool

```


left and right can be any scalar value:

```
>>> s = ps.Series(['Alice', 'Bob', 'Carol', 'Eve'])
>>> s.between('Anna', 'Daniel')
0    False
1     True
2     True
3    False
dtype: bool

```

# pyspark.pandas.Series.clip — PySpark 4.0.1 documentation
Series.clip(_lower\=None_, _upper\=None_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.clip)
[#](#pyspark.pandas.Series.clip "Permalink to this definition")

Trim values at input threshold(s).

Assigns values outside boundary-to-boundary values.

Parameters

**lower**float or int, default None

Minimum threshold value. All values below this threshold will be set to it.

**upper**float or int, default None

Maximum threshold value. All values above this threshold will be set to it.

**inplace**bool, default False

if True, perform operation in-place

Returns

Series

Series with the values outside the clip boundaries replaced

Notes

One difference between this implementation and pandas is that running pd.Series(\[‘a’, ‘b’\]).clip(0, 1) will crash with “TypeError: ‘<=’ not supported between instances of ‘str’ and ‘int’” while ps.Series(\[‘a’, ‘b’\]).clip(0, 1) will output the original Series, simply ignoring the incompatible types.

Examples

```
>>> psser = ps.Series([0, 2, 4])
>>> psser
0    0
1    2
2    4
dtype: int64

```


```
>>> psser.clip(1, 3)
0    1
1    2
2    3
dtype: int64

```


Clip can be performed in-place.

```
>>> psser.clip(2, 3, inplace=True)
>>> psser
0    2
1    2
2    3
dtype: int64

```


# pyspark.pandas.Series.corr — PySpark 4.0.1 documentation
Series.corr(_other_, _method\='pearson'_, _min\_periods\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.corr)
[#](#pyspark.pandas.Series.corr "Permalink to this definition")

Compute correlation with other Series, excluding missing values.

New in version 3.3.0.

Parameters

**other**Series

**method**{‘pearson’, ‘spearman’, ‘kendall’}

*   pearson : standard correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   kendall : Kendall Tau correlation coefficient
    

Changed in version 3.4.0: support ‘kendall’ for method parameter

**min\_periods**int, optional

Minimum number of observations needed to have a valid result.

New in version 3.4.0.

Returns

**correlation**float

Notes

The complexity of Kendall correlation is O(#row \* #row), if the dataset is too large, sampling ahead of correlation computation is recommended.

Examples

```
>>> df = ps.DataFrame({'s1': [.2, .0, .6, .2],
...                    's2': [.3, .6, .0, .1]})
>>> s1 = df.s1
>>> s2 = df.s2
>>> s1.corr(s2, method='pearson')
-0.85106...

```


```
>>> s1.corr(s2, method='spearman')
-0.94868...

```


```
>>> s1.corr(s2, method='kendall')
-0.91287...

```


```
>>> s1 = ps.Series([1, np.nan, 2, 1, 1, 2, 3])
>>> s2 = ps.Series([3, 4, 1, 1, 5])

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.corr(s2, method="pearson")
-0.52223...

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.corr(s2, method="spearman")
-0.54433...

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.corr(s2, method="kendall")
-0.51639...

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.corr(s2, method="kendall", min_periods=5)
nan

```


# pyspark.pandas.Series.count — PySpark 4.0.1 documentation
Series.count(_axis\=None_, _numeric\_only\=False_)
[#](#pyspark.pandas.Series.count "Permalink to this definition")

Count non-NA cells for each column.

The values None, NaN are considered NA.

Parameters

**axis: {0 or ‘index’, 1 or ‘columns’}, default 0**

If 0 or ‘index’ counts are generated for each column. If 1 or ‘columns’ counts are generated for each row.

**numeric\_only: bool, default False**

If True, include only float, int, boolean columns. This parameter is mainly for pandas compatibility.

Returns

max: scalar for a Series, and a Series for a DataFrame.

See also

[`DataFrame.shape`](about:blank/pyspark.pandas.DataFrame.shape.html#pyspark.pandas.DataFrame.shape "pyspark.pandas.DataFrame.shape")

Number of DataFrame rows and columns (including NA elements).

[`DataFrame.isna`](about:blank/pyspark.pandas.DataFrame.isna.html#pyspark.pandas.DataFrame.isna "pyspark.pandas.DataFrame.isna")

Boolean same-sized DataFrame showing places of NA elements.

Examples

Constructing DataFrame from a dictionary:

```
>>> df = ps.DataFrame({"Person":
...                    ["John", "Myla", "Lewis", "John", "Myla"],
...                    "Age": [24., np.nan, 21., 33, 26],
...                    "Single": [False, True, True, True, False]},
...                   columns=["Person", "Age", "Single"])
>>> df
  Person   Age  Single
0   John  24.0   False
1   Myla   NaN    True
2  Lewis  21.0    True
3   John  33.0    True
4   Myla  26.0   False

```


Notice the uncounted NA values:

```
>>> df.count()
Person    5
Age       4
Single    5
dtype: int64

```


```
>>> df.count(axis=1)
0    3
1    2
2    3
3    3
4    3
dtype: int64

```


On a Series:

```
>>> df['Person'].count()
5

```


# pyspark.pandas.Series.cov — PySpark 4.0.1 documentation
Series.cov(_other_, _min\_periods\=None_, _ddof\=1_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.cov)
[#](#pyspark.pandas.Series.cov "Permalink to this definition")

Compute covariance with Series, excluding missing values.

New in version 3.3.0.

Parameters

**other**Series

Series with which to compute the covariance.

**min\_periods**int, optional

Minimum number of observations needed to have a valid result.

**ddof**int, default 1

Delta degrees of freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

New in version 3.4.0.

Returns

float

Covariance between Series and other

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> s1 = ps.Series([0.90010907, 0.13484424, 0.62036035])
>>> s2 = ps.Series([0.12528585, 0.26962463, 0.51111198])
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.cov(s2)
-0.016857...
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     s1.cov(s2, ddof=2)
-0.033715...

```

# pyspark.pandas.Series.cummax — PySpark 4.0.1 documentation
Series.cummax(_skipna\=True_)
[#](#pyspark.pandas.Series.cummax "Permalink to this definition")

Return cumulative maximum over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative maximum.

Note

the current implementation of cummax uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**skipna: boolean, default True**

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

Returns

DataFrame or Series

Examples

```
>>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [1.0, 0.0]], columns=list('AB'))
>>> df
     A    B
0  2.0  1.0
1  3.0  NaN
2  1.0  0.0

```


By default, iterates over rows and finds the maximum in each column.

```
>>> df.cummax()
     A    B
0  2.0  1.0
1  3.0  NaN
2  3.0  1.0

```


It works identically in Series.

```
>>> df.B.cummax()
0    1.0
1    NaN
2    1.0
Name: B, dtype: float64

```


# pyspark.pandas.Series.cummin — PySpark 4.0.1 documentation
Series.cummin(_skipna\=True_)
[#](#pyspark.pandas.Series.cummin "Permalink to this definition")

Return cumulative minimum over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative minimum.

Note

the current implementation of cummin uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**skipna: boolean, default True**

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

Returns

DataFrame or Series

Examples

```
>>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [1.0, 0.0]], columns=list('AB'))
>>> df
     A    B
0  2.0  1.0
1  3.0  NaN
2  1.0  0.0

```


By default, iterates over rows and finds the minimum in each column.

```
>>> df.cummin()
     A    B
0  2.0  1.0
1  2.0  NaN
2  1.0  0.0

```


It works identically in Series.

```
>>> df.A.cummin()
0    2.0
1    2.0
2    1.0
Name: A, dtype: float64

```


# pyspark.pandas.Series.cumprod — PySpark 4.0.1 documentation
Series.cumprod(_skipna\=True_)
[#](#pyspark.pandas.Series.cumprod "Permalink to this definition")

Return cumulative product over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative product.

Note

the current implementation of cumprod uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Note

unlike pandas’, pandas-on-Spark’s emulates cumulative product by `exp(sum(log(...)))` trick. Therefore, it only works for positive numbers.

Parameters

**skipna: boolean, default True**

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

Returns

DataFrame or Series

Raises

Exception: If the values is equal to or lower than 0.

Examples

```
>>> df = ps.DataFrame([[2.0, 1.0], [3.0, None], [4.0, 10.0]], columns=list('AB'))
>>> df
     A     B
0  2.0   1.0
1  3.0   NaN
2  4.0  10.0

```


By default, iterates over rows and finds the sum in each column.

```
>>> df.cumprod()
      A     B
0   2.0   1.0
1   6.0   NaN
2  24.0  10.0

```


It works identically in Series.

```
>>> df.A.cumprod()
0     2.0
1     6.0
2    24.0
Name: A, dtype: float64

```


# pyspark.pandas.Series.describe — PySpark 4.0.1 documentation
Series.describe(_percentiles\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.describe)
[#](#pyspark.pandas.Series.describe "Permalink to this definition")

Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset’s distribution, excluding `NaN` values.

Analyzes both numeric and object series, as well as `DataFrame` column sets of mixed data types. The output will vary depending on what is provided. Refer to the notes below for more detail.

Parameters

**percentiles**list of `float` in range \[0.0, 1.0\], default \[0.25, 0.5, 0.75\]

A list of percentiles to be computed.

Returns

DataFrame

Summary statistics of the Dataframe provided.

Notes

For numeric data, the result’s index will include `count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max`.

For object data (e.g. strings or timestamps), the result’s index will include `count`, `unique`, `top`, and `freq`. The `top` is the most common value. The `freq` is the most common value’s frequency. Timestamps also include the `first` and `last` items.

Examples

Describing a numeric `Series`.

```
>>> s = ps.Series([1, 2, 3])
>>> s.describe()
count    3.0
mean     2.0
std      1.0
min      1.0
25%      1.0
50%      2.0
75%      3.0
max      3.0
dtype: float64

```


Describing a `DataFrame`. Only numeric fields are returned.

```
>>> df = ps.DataFrame({'numeric1': [1, 2, 3],
...                    'numeric2': [4.0, 5.0, 6.0],
...                    'object': ['a', 'b', 'c']
...                   },
...                   columns=['numeric1', 'numeric2', 'object'])
>>> df.describe()
       numeric1  numeric2
count       3.0       3.0
mean        2.0       5.0
std         1.0       1.0
min         1.0       4.0
25%         1.0       4.0
50%         2.0       5.0
75%         3.0       6.0
max         3.0       6.0

```


For multi-index columns:

```
>>> df.columns = [('num', 'a'), ('num', 'b'), ('obj', 'c')]
>>> df.describe()  
       num
         a    b
count  3.0  3.0
mean   2.0  5.0
std    1.0  1.0
min    1.0  4.0
25%    1.0  4.0
50%    2.0  5.0
75%    3.0  6.0
max    3.0  6.0

```


```
>>> df[('num', 'b')].describe()
count    3.0
mean     5.0
std      1.0
min      4.0
25%      4.0
50%      5.0
75%      6.0
max      6.0
Name: (num, b), dtype: float64

```


Describing a `DataFrame` and selecting custom percentiles.

```
>>> df = ps.DataFrame({'numeric1': [1, 2, 3],
...                    'numeric2': [4.0, 5.0, 6.0]
...                   },
...                   columns=['numeric1', 'numeric2'])
>>> df.describe(percentiles = [0.85, 0.15])
       numeric1  numeric2
count       3.0       3.0
mean        2.0       5.0
std         1.0       1.0
min         1.0       4.0
15%         1.0       4.0
50%         2.0       5.0
85%         3.0       6.0
max         3.0       6.0

```


Describing a column from a `DataFrame` by accessing it as an attribute.

```
>>> df.numeric1.describe()
count    3.0
mean     2.0
std      1.0
min      1.0
25%      1.0
50%      2.0
75%      3.0
max      3.0
Name: numeric1, dtype: float64

```


Describing a column from a `DataFrame` by accessing it as an attribute and selecting custom percentiles.

```
>>> df.numeric1.describe(percentiles = [0.85, 0.15])
count    3.0
mean     2.0
std      1.0
min      1.0
15%      1.0
50%      2.0
85%      3.0
max      3.0
Name: numeric1, dtype: float64

```

# pyspark.pandas.Series.ewm — PySpark 4.0.1 documentation
Series.ewm(_com\=None_, _span\=None_, _halflife\=None_, _alpha\=None_, _min\_periods\=None_, _ignore\_na\=False_)
[#](#pyspark.pandas.Series.ewm "Permalink to this definition")

Provide exponentially weighted window transformations.

Note

‘min\_periods’ in pandas-on-Spark works as a fixed window size unlike pandas. Unlike pandas, NA is also counted as the period. This might be changed soon.

New in version 3.4.0.

Parameters

**com: float, optional**

Specify decay in terms of center of mass. alpha = 1 / (1 + com), for com >= 0.

**span: float, optional**

Specify decay in terms of span. alpha = 2 / (span + 1), for span >= 1.

**halflife: float, optional**

Specify decay in terms of half-life. alpha = 1 - exp(-ln(2) / halflife), for halflife > 0.

**alpha: float, optional**

Specify smoothing factor alpha directly. 0 < alpha <= 1.

**min\_periods: int, default None**

Minimum number of observations in window required to have a value (otherwise result is NA).

**ignore\_na: bool, default False**

Ignore missing values when calculating weights.

*   When `ignore_na=False` (default), weights are based on absolute positions. For example, the weights of \\(x\_0\\) and \\(x\_2\\) used in calculating the final weighted average of \[\\(x\_0\\), None, \\(x\_2\\)\] are \\((1-lpha)^2\\) and \\(1\\) if `adjust=True`, and \\((1-lpha)^2\\) and \\(lpha\\) if `adjust=False`.
    
*   When `ignore_na=True`, weights are based on relative positions. For example, the weights of \\(x\_0\\) and \\(x\_2\\) used in calculating the final weighted average of \[\\(x\_0\\), None, \\(x\_2\\)\] are \\(1-lpha\\) and \\(1\\) if `adjust=True`, and \\(1-lpha\\) and \\(lpha\\) if `adjust=False`.
    

Returns

a Window sub-classed for the operation

# pyspark.pandas.Series.filter — PySpark 4.0.1 documentation
Series.filter(_items\=None_, _like\=None_, _regex\=None_, _axis\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.filter)
[#](#pyspark.pandas.Series.filter "Permalink to this definition")

Subset rows or columns of dataframe according to labels in the specified index.

Note that this routine does not filter a dataframe on its contents. The filter is applied to the labels of the index.

Parameters

**items**list-like

Keep labels from axis which are in items.

**like**string

Keep labels from axis for which “like in label == True”.

**regex**string (regular expression)

Keep labels from axis for which re.search(regex, label) == True.

**axis**int or string axis name

The axis to filter on. By default this is the info axis, ‘index’ for Series, ‘columns’ for DataFrame.

Returns

same type as input object

Notes

The `items`, `like`, and `regex` parameters are enforced to be mutually exclusive.

`axis` defaults to the info axis that is used when indexing with `[]`.

Examples

```
>>> df = ps.DataFrame(np.array(([1, 2, 3], [4, 5, 6])),
...                   index=['mouse', 'rabbit'],
...                   columns=['one', 'two', 'three'])

```


```
>>> # select columns by name
>>> df.filter(items=['one', 'three'])
        one  three
mouse     1      3
rabbit    4      6

```


```
>>> # select columns by regular expression
>>> df.filter(regex='e

```
>>> # select rows containing 'bbi'
>>> df.filter(like='bbi', axis=0)
        one  two  three
rabbit    4    5      6

```


For a Series,

```
>>> # select rows by name
>>> df.one.filter(items=['rabbit'])
rabbit    4
Name: one, dtype: int64

```


```
>>> # select rows by regular expression
>>> df.one.filter(regex='e

```
>>> # select rows containing 'bbi'
>>> df.one.filter(like='bbi')
rabbit    4
Name: one, dtype: int64

```
, axis=1)
        one  three
mouse     1      3
rabbit    4      6

```


urltomarkdowncodeblockplaceholder30.4681240095164714

For a Series,

urltomarkdowncodeblockplaceholder40.2920421569226237

urltomarkdowncodeblockplaceholder50.5540843833256888

urltomarkdowncodeblockplaceholder60.6131508778419752)
mouse    1
Name: one, dtype: int64

```


urltomarkdowncodeblockplaceholder60.6131508778419752, axis=1)
        one  three
mouse     1      3
rabbit    4      6

```


urltomarkdowncodeblockplaceholder30.4681240095164714

For a Series,

urltomarkdowncodeblockplaceholder40.2920421569226237

urltomarkdowncodeblockplaceholder50.5540843833256888

urltomarkdowncodeblockplaceholder60.6131508778419752


# pyspark.pandas.Series.kurt — PySpark 4.0.1 documentation
Series.kurt(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.kurt "Permalink to this definition")

Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0). Normalized by N-1.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

Returns

kurt: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan, 6], 'b': [0.1, 0.2, 0.3, np.nan, 0.8]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.kurtosis()
a    1.500000
b    2.703924
dtype: float64

```


On a Series:

```
>>> df['a'].kurtosis()
1.5

```


# pyspark.pandas.Series.max — PySpark 4.0.1 documentation
Series.max(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.max "Permalink to this definition")

Return the maximum of the values.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

If True, include only float, int, boolean columns. This parameter is mainly for pandas compatibility. False is supported; however, the columns should be all numeric or all non-numeric.

Returns

max: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.max()
a    3.0
b    0.3
dtype: float64

```


```
>>> df.max(axis=1)
0    1.0
1    2.0
2    3.0
3    NaN
dtype: float64

```


On a Series:


# pyspark.pandas.Series.mean — PySpark 4.0.1 documentation
Series.mean(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.mean "Permalink to this definition")

Return the mean of the values.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

Returns

mean: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.mean()
a    2.0
b    0.2
dtype: float64

```


```
>>> df.mean(axis=1)
0    0.55
1    1.10
2    1.65
3     NaN
dtype: float64

```


On a Series:


# pyspark.pandas.Series.min — PySpark 4.0.1 documentation
Series.min(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.min "Permalink to this definition")

Return the minimum of the values.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

If True, include only float, int, boolean columns. This parameter is mainly for pandas compatibility. False is supported; however, the columns should be all numeric or all non-numeric.

Returns

min: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.min()
a    1.0
b    0.1
dtype: float64

```


```
>>> df.min(axis=1)
0    0.1
1    0.2
2    0.3
3    NaN
dtype: float64

```


On a Series:



# pyspark.pandas.Series.mode — PySpark 4.0.1 documentation
Series.mode(_dropna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.mode)
[#](#pyspark.pandas.Series.mode "Permalink to this definition")

Return the mode(s) of the dataset.

Always returns Series even if only one value is returned.

Changed in version 3.4.0: Series name is preserved to follow pandas 1.4+ behavior.

Parameters

**dropna**bool, default True

Don’t consider counts of NaN/NaT.

Returns

Series

Modes of the Series.

Examples

```
>>> s = ps.Series([0, 0, 1, 1, 1, np.nan, np.nan, np.nan])
>>> s
0    0.0
1    0.0
2    1.0
3    1.0
4    1.0
5    NaN
6    NaN
7    NaN
dtype: float64

```


```
>>> s.mode()
0    1.0
dtype: float64

```


If there are several same modes, all items are shown

```
>>> s = ps.Series([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3,
...                np.nan, np.nan, np.nan])
>>> s
0     0.0
1     0.0
2     1.0
3     1.0
4     1.0
5     2.0
6     2.0
7     2.0
8     3.0
9     3.0
10    3.0
11    NaN
12    NaN
13    NaN
dtype: float64

```


```
>>> s.mode().sort_values()
0    1.0
1    2.0
2    3.0
dtype: float64

```


With ‘dropna’ set to ‘False’, we can also see NaN in the result

```
>>> s.mode(False).sort_values()
0    1.0
1    2.0
2    3.0
3    NaN
dtype: float64

```


# pyspark.pandas.Series.nlargest — PySpark 4.0.1 documentation
Series.nlargest(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.nlargest)
[#](#pyspark.pandas.Series.nlargest "Permalink to this definition")

Return the largest n elements.

Parameters

**n**int, default 5

Returns

Series

The n largest values in the Series, sorted in decreasing order.

Notes

Faster than `.sort_values(ascending=False).head(n)` for small n relative to the size of the `Series` object.

In pandas-on-Spark, thanks to Spark’s lazy execution and query optimizer, the two would have same performance.

Examples

```
>>> data = [1, 2, 3, 4, np.nan ,6, 7, 8]
>>> s = ps.Series(data)
>>> s
0    1.0
1    2.0
2    3.0
3    4.0
4    NaN
5    6.0
6    7.0
7    8.0
dtype: float64

```


The n largest elements where `n=5` by default.

```
>>> s.nlargest()
7    8.0
6    7.0
5    6.0
3    4.0
2    3.0
dtype: float64

```


```
>>> s.nlargest(n=3)
7    8.0
6    7.0
5    6.0
dtype: float64

```


# pyspark.pandas.Series.nsmallest — PySpark 4.0.1 documentation
Series.nsmallest(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.nsmallest)
[#](#pyspark.pandas.Series.nsmallest "Permalink to this definition")

Return the smallest n elements.

Parameters

**n**int, default 5

Return this many ascending sorted values.

Returns

Series

The n smallest values in the Series, sorted in increasing order.

Notes

Faster than `.sort_values().head(n)` for small n relative to the size of the `Series` object. In pandas-on-Spark, thanks to Spark’s lazy execution and query optimizer, the two would have same performance.

Examples

```
>>> data = [1, 2, 3, 4, np.nan ,6, 7, 8]
>>> s = ps.Series(data)
>>> s
0    1.0
1    2.0
2    3.0
3    4.0
4    NaN
5    6.0
6    7.0
7    8.0
dtype: float64

```


The n largest elements where `n=5` by default.

```
>>> s.nsmallest()
0    1.0
1    2.0
2    3.0
3    4.0
5    6.0
dtype: float64

```


```
>>> s.nsmallest(3)
0    1.0
1    2.0
2    3.0
dtype: float64

```


# pyspark.pandas.Series.pct_change — PySpark 4.0.1 documentation
Series.pct\_change(_periods\=1_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.pct_change)
[#](#pyspark.pandas.Series.pct_change "Permalink to this definition")

Percentage change between the current and a prior element.

Note

the current implementation of this API uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**periods**int, default 1

Periods to shift for forming percent change.

Returns

Series

Examples

```
>>> psser = ps.Series([90, 91, 85], index=[2, 4, 1])
>>> psser
2    90
4    91
1    85
dtype: int64

```


```
>>> psser.pct_change()
2         NaN
4    0.011111
1   -0.065934
dtype: float64

```


```
>>> psser.sort_index().pct_change()
1         NaN
2    0.058824
4    0.011111
dtype: float64

```


```
>>> psser.pct_change(periods=2)
2         NaN
4         NaN
1   -0.055556
dtype: float64

```


# pyspark.pandas.Series.prod — PySpark 4.0.1 documentation
Series.prod(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _min\_count\=0_)
[#](#pyspark.pandas.Series.prod "Permalink to this definition")

Return the product of the values.

Note

unlike pandas’, pandas-on-Spark’s emulates product by `exp(sum(log(...)))` trick. Therefore, it only works for positive numbers.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

**min\_count: int, default 0**

The required number of valid values to perform the operation. If fewer than `min_count` non-NA values are present the result will be NA.

Examples

On a DataFrame:

Non-numeric type column is not included to the result.

```
>>> psdf = ps.DataFrame({'A': [1, 2, 3, 4, 5],
...                     'B': [10, 20, 30, 40, 50],
...                     'C': ['a', 'b', 'c', 'd', 'e']})
>>> psdf
   A   B  C
0  1  10  a
1  2  20  b
2  3  30  c
3  4  40  d
4  5  50  e

```


```
>>> psdf.prod()
A         120
B    12000000
dtype: int64

```


If there is no numeric type columns, returns empty Series.

```
>>> ps.DataFrame({"key": ['a', 'b', 'c'], "val": ['x', 'y', 'z']}).prod()  
Series([], dtype: float64)

```


On a Series:

```
>>> ps.Series([1, 2, 3, 4, 5]).prod()
120

```


By default, the product of an empty or all-NA Series is `1`

```
>>> ps.Series([]).prod()  
1.0

```


This can be controlled with the `min_count` parameter

```
>>> ps.Series([]).prod(min_count=1)  
nan

```


# pyspark.pandas.Series.nunique — PySpark 4.0.1 documentation
Series.nunique(_dropna\=True_, _approx\=False_, _rsd\=0.05_)
[#](#pyspark.pandas.Series.nunique "Permalink to this definition")

Return number of unique elements in the object. Excludes NA values by default.

Parameters

**dropna**bool, default True

Don’t include NaN in the count.

**approx: bool, default False**

If False, will use the exact algorithm and return the exact number of unique. If True, it uses the HyperLogLog approximate algorithm, which is significantly faster for large amount of data. Note: This parameter is specific to pandas-on-Spark and is not found in pandas.

**rsd: float, default 0.05**

Maximum estimation error allowed in the HyperLogLog algorithm. Note: Just like `approx` this parameter is specific to pandas-on-Spark.

Returns

int

Examples

```
>>> ps.Series([1, 2, 3, np.nan]).nunique()
3

```


```
>>> ps.Series([1, 2, 3, np.nan]).nunique(dropna=False)
4

```


On big data, we recommend using the approximate algorithm to speed up this function. The result will be very close to the exact unique count.

```
>>> ps.Series([1, 2, 3, np.nan]).nunique(approx=True)
3

```


```
>>> idx = ps.Index([1, 1, 2, None])
>>> idx
Index([1.0, 1.0, 2.0, nan], dtype='float64')

```


```
>>> idx.nunique(dropna=False)
3

```


# pyspark.pandas.Series.is_unique — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.is\_unique

_property_ Series.is\_unique[#](#pyspark.pandas.Series.is_unique "Permalink to this definition")

Return boolean if values in the object are unique

Returns

**is\_unique**boolean

```
>>> ps.Series([1, 2, 3]).is_unique
    ..

```


True

```
>>> ps.Series([1, 2, 2]).is_unique
    ..

```


False

```
>>> ps.Series([1, 2, 3, None]).is_unique
    ..

```


True


# pyspark.pandas.Series.quantile — PySpark 4.0.1 documentation
Series.quantile(_q\=0.5_, _accuracy\=10000_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.quantile)
[#](#pyspark.pandas.Series.quantile "Permalink to this definition")

Return value at the given quantile.

Note

Unlike pandas’, the quantile in pandas-on-Spark is an approximated quantile based upon approximate percentile computation because computing quantile across a large dataset is extremely expensive.

Parameters

**q**float or array-like, default 0.5 (50% quantile)

0 <= q <= 1, the quantile(s) to compute.

**accuracy**int, optional

Default accuracy of approximation. Larger value means better accuracy. The relative error can be deduced by 1.0 / accuracy.

Returns

float or Series

If the current object is a Series and `q` is an array, a Series will be returned where the index is `q` and the values are the quantiles, otherwise a float will be returned.

Examples

```
>>> s = ps.Series([1, 2, 3, 4, 5])
>>> s.quantile(.5)
3.0

```


```
>>> (s + 1).quantile(.5)
4.0

```


```
>>> s.quantile([.25, .5, .75])
0.25    2.0
0.50    3.0
0.75    4.0
dtype: float64

```


```
>>> (s + 1).quantile([.25, .5, .75])
0.25    3.0
0.50    4.0
0.75    5.0
dtype: float64

```


# pyspark.pandas.Series.rank — PySpark 4.0.1 documentation
Series.rank(_method\='average'_, _ascending\=True_, _numeric\_only\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rank)
[#](#pyspark.pandas.Series.rank "Permalink to this definition")

Compute numerical data ranks (1 through n) along axis. Equal values are assigned a rank that is the average of the ranks of those values.

Note

the current implementation of rank uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**method**{‘average’, ‘min’, ‘max’, ‘first’, ‘dense’}

*   average: average rank of group
    
*   min: lowest rank in group
    
*   max: highest rank in group
    
*   first: ranks assigned in order they appear in the array
    
*   dense: like ‘min’, but rank always increases by 1 between groups
    

**ascending**boolean, default True

False for ranks by high (1) to low (N)

**numeric\_only**bool, default False

For DataFrame objects, rank only numeric columns if set to True.

Changed in version 4.0.0: The default value of `numeric_only` is now `False`.

Returns

**ranks**same type as caller

Examples

```
>>> s = ps.Series([1, 2, 2, 3], name='A')
>>> s
0    1
1    2
2    2
3    3
Name: A, dtype: int64

```


```
>>> s.rank()
0    1.0
1    2.5
2    2.5
3    4.0
Name: A, dtype: float64

```


If method is set to ‘min’, it uses lowest rank in group.

```
>>> s.rank(method='min')
0    1.0
1    2.0
2    2.0
3    4.0
Name: A, dtype: float64

```


If method is set to ‘max’, it uses highest rank in group.

```
>>> s.rank(method='max')
0    1.0
1    3.0
2    3.0
3    4.0
Name: A, dtype: float64

```


If method is set to ‘first’, it is assigned rank in order without groups.

```
>>> s.rank(method='first')
0    1.0
1    2.0
2    3.0
3    4.0
Name: A, dtype: float64

```


If method is set to ‘dense’, it leaves no gaps in group.

```
>>> s.rank(method='dense')
0    1.0
1    2.0
2    2.0
3    3.0
Name: A, dtype: float64

```


If numeric\_only is set to ‘True’, rank only numeric Series, return an empty Series otherwise.

```
>>> s = ps.Series(['a', 'b', 'c'], name='A', index=['x', 'y', 'z'])
>>> s
x    a
y    b
z    c
Name: A, dtype: object

```


# pyspark.pandas.Series.sem — PySpark 4.0.1 documentation
Series.sem(_axis\=None_, _skipna\=True_, _ddof\=1_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.sem "Permalink to this definition")

Return unbiased standard error of the mean over requested axis.

New in version 3.3.0.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**ddof: int, default 1**

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

Changed in version 3.4.0: Supported including arbitary integers.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

Returns

scalar(for Series) or Series(for DataFrame)

Examples

```
>>> psdf = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
>>> psdf
   a  b
0  1  4
1  2  5
2  3  6

```


```
>>> psdf.sem()
a    0.57735
b    0.57735
dtype: float64

```


```
>>> psdf.sem(ddof=0)
a    0.471405
b    0.471405
dtype: float64

```


```
>>> psdf.sem(ddof=2)
a    0.816497
b    0.816497
dtype: float64

```


```
>>> psdf.sem(axis=1)
0    1.5
1    1.5
2    1.5
dtype: float64

```


Support for Series

```
>>> psser = psdf.a
>>> psser
0    1
1    2
2    3
Name: a, dtype: int64

```


```
>>> psser.sem()
0.5773502691896258

```


```
>>> psser.sem(ddof=0)
0.47140452079103173

```


# pyspark.pandas.Series.skew — PySpark 4.0.1 documentation
Series.skew(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.skew "Permalink to this definition")

Return unbiased skew normalized by N-1.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

Returns

skew: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.skew()
a    0.0
b    0.0
dtype: float64

```


On a Series:


# pyspark.pandas.Series.std — PySpark 4.0.1 documentation
Series.std(_axis\=None_, _skipna\=True_, _ddof\=1_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.std "Permalink to this definition")

Return sample standard deviation.

New in version 3.3.0.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**ddof: int, default 1**

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

Changed in version 3.4.0: Supported including arbitary integers.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

Returns

std: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, 0.2, 0.3, np.nan]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.std()
a    1.0
b    0.1
dtype: float64

```


```
>>> df.std(ddof=2)
a    1.414214
b    0.141421
dtype: float64

```


```
>>> df.std(axis=1)
0    0.636396
1    1.272792
2    1.909188
3         NaN
dtype: float64

```


```
>>> df.std(ddof=0)
a    0.816497
b    0.081650
dtype: float64

```


On a Series:

```
>>> df['a'].std(ddof=0)
0.816496580927726

```


```
>>> df['a'].std(ddof=-1)
0.707106...

```


# pyspark.pandas.Series.sum — PySpark 4.0.1 documentation
Series.sum(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _min\_count\=0_)
[#](#pyspark.pandas.Series.sum "Permalink to this definition")

Return the sum of the values.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Added _skipna_ to exclude.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

**min\_count: int, default 0**

The required number of valid values to perform the operation. If fewer than

`min_count` non-NA values are present the result will be NA.

Returns

sum: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan], 'b': [0.1, np.nan, 0.3, np.nan]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.sum()
a    6.0
b    0.4
dtype: float64

```


```
>>> df.sum(axis=1)
0    1.1
1    2.0
2    3.3
3    0.0
dtype: float64

```


```
>>> df.sum(min_count=3)
a    6.0
b    NaN
dtype: float64

```


```
>>> df.sum(axis=1, min_count=1)
0    1.1
1    2.0
2    3.3
3    NaN
dtype: float64

```


On a Series:

```
>>> df['a'].sum(min_count=3)
6.0
>>> df['b'].sum(min_count=3)
nan

```


# pyspark.pandas.Series.median — PySpark 4.0.1 documentation
Series.median(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _accuracy\=10000_)
[#](#pyspark.pandas.Series.median "Permalink to this definition")

Return the median of the values for the requested axis.

Note

Unlike pandas’, the median in pandas-on-Spark is an approximated median based upon approximate percentile computation because computing median across a large dataset is extremely expensive.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

**accuracy: int, optional**

Default accuracy of approximation. Larger value means better accuracy. The relative error can be deduced by 1.0 / accuracy.

Returns

median: scalar or Series

Examples

```
>>> df = ps.DataFrame({
...     'a': [24., 21., 25., 33., 26.], 'b': [1, 2, 3, 4, 5]}, columns=['a', 'b'])
>>> df
      a  b
0  24.0  1
1  21.0  2
2  25.0  3
3  33.0  4
4  26.0  5

```


On a DataFrame:

```
>>> df.median()
a    25.0
b     3.0
dtype: float64

```


On a Series:

```
>>> df['a'].median()
25.0
>>> (df['b'] + 100).median()
103.0

```


For multi-index columns,

```
>>> df.columns = pd.MultiIndex.from_tuples([('x', 'a'), ('y', 'b')])
>>> df
      x  y
      a  b
0  24.0  1
1  21.0  2
2  25.0  3
3  33.0  4
4  26.0  5

```


On a DataFrame:

```
>>> df.median()
x  a    25.0
y  b     3.0
dtype: float64

```


```
>>> df.median(axis=1)
0    12.5
1    11.5
2    14.0
3    18.5
4    15.5
dtype: float64

```


On a Series:

```
>>> df[('x', 'a')].median()
25.0
>>> (df[('y', 'b')] + 100).median()
103.0

```


# pyspark.pandas.Series.kurtosis — PySpark 4.0.1 documentation
Series.kurtosis(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.Series.kurtosis "Permalink to this definition")

Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0). Normalized by N-1.

Parameters

**axis: {index (0), columns (1)}**

Axis for the function to be applied on.

**skipna: bool, default True**

Exclude NA/null values when computing the result.

Changed in version 3.4.0: Supported including NA/null values.

**numeric\_only: bool, default None**

Include only float, int, boolean columns. False is not supported. This parameter is mainly for pandas compatibility.

Returns

kurt: scalar for a Series, and a Series for a DataFrame.

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, np.nan, 6], 'b': [0.1, 0.2, 0.3, np.nan, 0.8]},
...                   columns=['a', 'b'])

```


On a DataFrame:

```
>>> df.kurtosis()
a    1.500000
b    2.703924
dtype: float64

```


On a Series:

```
>>> df['a'].kurtosis()
1.5

```


# pyspark.pandas.Series.unique — PySpark 4.0.1 documentation
Series.unique()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.unique)
[#](#pyspark.pandas.Series.unique "Permalink to this definition")

Return unique values of Series object.

Uniques are returned in order of appearance. Hash table-based unique, therefore does NOT sort.

Note

This method returns newly created Series whereas pandas returns the unique values as a NumPy array.

Returns

Returns the unique values as a Series.

Examples

```
>>> psser = ps.Series([2, 1, 3, 3], name='A')
>>> psser.unique().sort_values()
1    1
0    2
2    3
Name: A, dtype: int64

```


```
>>> ps.Series([pd.Timestamp('2016-01-01') for _ in range(3)]).unique()
0   2016-01-01
dtype: datetime64[ns]

```


```
>>> psser.name = ('x', 'a')
>>> psser.unique().sort_values()
1    1
0    2
2    3
Name: (x, a), dtype: int64

```


# pyspark.pandas.Series.value_counts — PySpark 4.0.1 documentation
Series.value\_counts(_normalize\=False_, _sort\=True_, _ascending\=False_, _bins\=None_, _dropna\=True_)
[#](#pyspark.pandas.Series.value_counts "Permalink to this definition")

Return a Series containing counts of unique values. The resulting object will be in descending order so that the first element is the most frequently-occurring element. Excludes NA values by default.

Parameters

**normalize**boolean, default False

If True then the object returned will contain the relative frequencies of the unique values.

**sort**boolean, default True

Sort by values.

**ascending**boolean, default False

Sort in ascending order.

**bins**Not Yet Supported

**dropna**boolean, default True

Don’t include counts of NaN.

Returns

**counts**Series

Examples

For Series

```
>>> df = ps.DataFrame({'x':[0, 0, 1, 1, 1, np.nan]})
>>> df.x.value_counts()  
x
1.0    3
0.0    2
Name: count, dtype: int64

```


With normalize set to True, returns the relative frequency by dividing all values by the sum of values.

```
>>> df.x.value_counts(normalize=True)  
x
1.0    0.6
0.0    0.4
Name: proportion, dtype: float64

```


**dropna** With dropna set to False we can also see NaN index values.

```
>>> df.x.value_counts(dropna=False)  
x
1.0    3
0.0    2
NaN    1
Name: count, dtype: int64

```


For Index

```
>>> idx = ps.Index([3, 1, 2, 3, 4, np.nan])
>>> idx
Index([3.0, 1.0, 2.0, 3.0, 4.0, nan], dtype='float64')

```


```
>>> idx.value_counts().sort_index()
1.0    1
2.0    1
3.0    2
4.0    1
Name: count, dtype: int64

```


**sort**

With sort set to False, the result wouldn’t be sorted by number of count.

```
>>> idx.value_counts(sort=True).sort_index()
1.0    1
2.0    1
3.0    2
4.0    1
Name: count, dtype: int64

```


**normalize**

With normalize set to True, returns the relative frequency by dividing all values by the sum of values.

```
>>> idx.value_counts(normalize=True).sort_index()
1.0    0.2
2.0    0.2
3.0    0.4
4.0    0.2
Name: proportion, dtype: float64

```


**dropna**

With dropna set to False we can also see NaN index values.

```
>>> idx.value_counts(dropna=False).sort_index()  
1.0    1
2.0    1
3.0    2
4.0    1
NaN    1
dtype: int64

```


For MultiIndex.

```
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

```


```
>>> s.index.value_counts().sort_index()
(cow, length)       1
(cow, weight)       2
(falcon, length)    2
(falcon, weight)    1
(lama, weight)      3
Name: count, dtype: int64

```


```
>>> s.index.value_counts(normalize=True).sort_index()
(cow, length)       0.111111
(cow, weight)       0.222222
(falcon, length)    0.222222
(falcon, weight)    0.111111
(lama, weight)      0.333333
Name: proportion, dtype: float64

```


If Index has name, keep the name up.

```
>>> idx = ps.Index([0, 0, 0, 1, 1, 2, 3], name='pandas-on-Spark')
>>> idx.value_counts().sort_index()
pandas-on-Spark
0    3
1    2
2    1
3    1
Name: count, dtype: int64

```


# pyspark.pandas.Series.round — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.round

Series.round(_decimals\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.round)
[#](#pyspark.pandas.Series.round "Permalink to this definition")

Round each value in a Series to the given number of decimals.

Parameters

**decimals**int

Number of decimal places to round to (default: 0). If decimals are negative, it specifies the number of positions to the left of the decimal point.

Returns

Series object

Examples

```
>>> df = ps.Series([0.028208, 0.038683, 0.877076], name='x')
>>> df
0    0.028208
1    0.038683
2    0.877076
Name: x, dtype: float64

```


```
>>> df.round(2)
0    0.03
1    0.04
2    0.88
Name: x, dtype: float64

```


# pyspark.pandas.Series.diff — PySpark 4.0.1 documentation
Series.diff(_periods\=1_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.diff)
[#](#pyspark.pandas.Series.diff "Permalink to this definition")

First discrete difference of element.

Calculates the difference of a Series element compared with another element in the DataFrame (default is the element in the same column of the previous row).

Note

the current implementation of diff uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**periods**int, default 1

Periods to shift for calculating difference, accepts negative values.

Returns

**diffed**Series

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4, 5, 6],
...                    'b': [1, 1, 2, 3, 5, 8],
...                    'c': [1, 4, 9, 16, 25, 36]}, columns=['a', 'b', 'c'])
>>> df
   a  b   c
0  1  1   1
1  2  1   4
2  3  2   9
3  4  3  16
4  5  5  25
5  6  8  36

```


```
>>> df.b.diff()
0    NaN
1    0.0
2    1.0
3    1.0
4    2.0
5    3.0
Name: b, dtype: float64

```


Difference with previous value

```
>>> df.c.diff(periods=3)
0     NaN
1     NaN
2     NaN
3    15.0
4    21.0
5    27.0
Name: c, dtype: float64

```


Difference with following value

```
>>> df.c.diff(periods=-1)
0    -3.0
1    -5.0
2    -7.0
3    -9.0
4   -11.0
5     NaN
Name: c, dtype: float64

```


# pyspark.pandas.Series.is_monotonic_increasing — PySpark 4.0.1 documentation
_property_ Series.is\_monotonic\_increasing[#](#pyspark.pandas.Series.is_monotonic_increasing "Permalink to this definition")

Return boolean if values in the object are monotonically increasing.

Note

the current implementation of is\_monotonic\_increasing requires to shuffle and aggregate multiple times to check the order locally and globally, which is potentially expensive. In case of multi-index, all data is transferred to a single node which can easily cause out-of-memory errors.

Note

Disable the Spark config spark.sql.optimizer.nestedSchemaPruning.enabled for multi-index if you’re using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

Returns

**is\_monotonic**bool

Examples

```
>>> ser = ps.Series(['1/1/2018', '3/1/2018', '4/1/2018'])
>>> ser.is_monotonic_increasing
True

```


```
>>> df = ps.DataFrame({'dates': [None, '1/1/2018', '2/1/2018', '3/1/2018']})
>>> df.dates.is_monotonic_increasing
False

```


```
>>> df.index.is_monotonic_increasing
True

```


```
>>> ser = ps.Series([1])
>>> ser.is_monotonic_increasing
True

```


```
>>> ser = ps.Series([])
>>> ser.is_monotonic_increasing
True

```


```
>>> ser.rename("a").to_frame().set_index("a").index.is_monotonic_increasing
True

```


```
>>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
>>> ser.is_monotonic_increasing
False

```


```
>>> ser.index.is_monotonic_increasing
True

```


Support for MultiIndex

```
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

```


```
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

```


# pyspark.pandas.Series.is_monotonic_decreasing — PySpark 4.0.1 documentation
_property_ Series.is\_monotonic\_decreasing[#](#pyspark.pandas.Series.is_monotonic_decreasing "Permalink to this definition")

Return boolean if values in the object are monotonically decreasing.

Note

the current implementation of is\_monotonic\_decreasing requires to shuffle and aggregate multiple times to check the order locally and globally, which is potentially expensive. In case of multi-index, all data is transferred to a single node which can easily cause out-of-memory errors.

Note

Disable the Spark config spark.sql.optimizer.nestedSchemaPruning.enabled for multi-index if you’re using pandas-on-Spark < 1.7.0 with PySpark 3.1.1.

Returns

**is\_monotonic**bool

Examples

```
>>> ser = ps.Series(['4/1/2018', '3/1/2018', '1/1/2018'])
>>> ser.is_monotonic_decreasing
True

```


```
>>> df = ps.DataFrame({'dates': [None, '3/1/2018', '2/1/2018', '1/1/2018']})
>>> df.dates.is_monotonic_decreasing
False

```


```
>>> df.index.is_monotonic_decreasing
False

```


```
>>> ser = ps.Series([1])
>>> ser.is_monotonic_decreasing
True

```


```
>>> ser = ps.Series([])
>>> ser.is_monotonic_decreasing
True

```


```
>>> ser.rename("a").to_frame().set_index("a").index.is_monotonic_decreasing
True

```


```
>>> ser = ps.Series([5, 4, 3, 2, 1], index=[1, 2, 3, 4, 5])
>>> ser.is_monotonic_decreasing
True

```


```
>>> ser.index.is_monotonic_decreasing
False

```


Support for MultiIndex

```
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

```


```
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

```


# pyspark.pandas.Series.align — PySpark 4.0.1 documentation
Series.align(_other_, _join\='outer'_, _axis\=None_, _copy\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.align)
[#](#pyspark.pandas.Series.align "Permalink to this definition")

Align two objects on their axes with the specified join method.

Join method is specified for each axis Index.

Parameters

**other**DataFrame or Series

**join**{{‘outer’, ‘inner’, ‘left’, ‘right’}}, default ‘outer’

**axis**allowed axis of the other object, default None

Align on index (0), columns (1), or both (None).

**copy**bool, default True

Always returns new objects. If copy=False and no reindexing is required then original objects are returned.

Returns

**(left, right)**(Series, type of other)

Aligned objects.

Examples

```
>>> ps.set_option("compute.ops_on_diff_frames", True)
>>> s1 = ps.Series([7, 8, 9], index=[10, 11, 12])
>>> s2 = ps.Series(["g", "h", "i"], index=[10, 20, 30])

```


```
>>> aligned_l, aligned_r = s1.align(s2)
>>> aligned_l.sort_index()
10    7.0
11    8.0
12    9.0
20    NaN
30    NaN
dtype: float64
>>> aligned_r.sort_index()
10       g
11    None
12    None
20       h
30       i
dtype: object

```


Align with the join type “inner”:

```
>>> aligned_l, aligned_r = s1.align(s2, join="inner")
>>> aligned_l.sort_index()
10    7
dtype: int64
>>> aligned_r.sort_index()
10    g
dtype: object

```


Align with a DataFrame:

```
>>> df = ps.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]}, index=[10, 20, 30])
>>> aligned_l, aligned_r = s1.align(df)
>>> aligned_l.sort_index()
10    7.0
11    8.0
12    9.0
20    NaN
30    NaN
dtype: float64
>>> aligned_r.sort_index()
      a     b
10  1.0     a
11  NaN  None
12  NaN  None
20  2.0     b
30  3.0     c

```


```
>>> ps.reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.Series.drop — PySpark 4.0.1 documentation
Series.drop(_labels\=None_, _index\=None_, _columns\=None_, _level\=None_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.drop)
[#](#pyspark.pandas.Series.drop "Permalink to this definition")

Return Series with specified index labels removed.

Remove elements of a Series based on specifying the index labels. When using a multi-index, labels on different levels can be removed by specifying the level.

Parameters

**labels**single label or list-like

Index labels to drop.

**index**single label or list-like

Redundant for application on Series, but index can be used instead of labels.

**columns**single label or list-like

No change is made to the Series; use ‘index’ or ‘labels’ instead.

New in version 3.4.0.

**level**int or level name, optional

For MultiIndex, level for which the labels will be removed.

**inplace: bool, default False**

If True, do operation inplace and return None

New in version 3.4.0.

Returns

Series

Series with specified index labels removed.

Examples

```
>>> s = ps.Series(data=np.arange(3), index=['A', 'B', 'C'])
>>> s
A    0
B    1
C    2
dtype: int64

```


Drop single label A

```
>>> s.drop('A')
B    1
C    2
dtype: int64

```


Drop labels B and C

```
>>> s.drop(labels=['B', 'C'])
A    0
dtype: int64

```


With ‘index’ rather than ‘labels’ returns exactly same result.

```
>>> s.drop(index='A')
B    1
C    2
dtype: int64

```


```
>>> s.drop(index=['B', 'C'])
A    0
dtype: int64

```


With ‘columns’, no change is made to the Series.

```
>>> s.drop(columns=['A'])
A    0
B    1
C    2
dtype: int64

```


With ‘inplace=True’, do operation inplace and return None.

```
>>> s.drop(index=['B', 'C'], inplace=True)
>>> s
A    0
dtype: int64

```


Also support for MultiIndex

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
...               index=midx)
>>> s
lama    speed      45.0
        weight    200.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.drop(labels='weight', level=1)
lama    speed      45.0
        length      1.2
cow     speed      30.0
        length      1.5
falcon  speed     320.0
        length      0.3
dtype: float64

```


```
>>> s.drop(('lama', 'weight'))
lama    speed      45.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.drop([('lama', 'speed'), ('falcon', 'weight')])
lama    weight    200.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        length      0.3
dtype: float64

```


# pyspark.pandas.Series.droplevel — PySpark 4.0.1 documentation
Series.droplevel(_level_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.droplevel)
[#](#pyspark.pandas.Series.droplevel "Permalink to this definition")

Return Series with requested index level(s) removed.

Parameters

**level**int, str, or list-like

If a string is given, must be the name of a level If list-like, elements must be names or positional indexes of levels.

Returns

Series

Series with requested index level(s) removed.

Examples

```
>>> psser = ps.Series(
...     [1, 2, 3],
...     index=pd.MultiIndex.from_tuples(
...         [("x", "a"), ("x", "b"), ("y", "c")], names=["level_1", "level_2"]
...     ),
... )
>>> psser
level_1  level_2
x        a          1
         b          2
y        c          3
dtype: int64

```


Removing specific index level by level

```
>>> psser.droplevel(0)
level_2
a    1
b    2
c    3
dtype: int64

```


Removing specific index level by name

```
>>> psser.droplevel("level_2")
level_1
x    1
x    2
y    3
dtype: int64

```


# pyspark.pandas.Series.drop_duplicates — PySpark 4.0.1 documentation
Series.drop\_duplicates(_keep\='first'_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.drop_duplicates)
[#](#pyspark.pandas.Series.drop_duplicates "Permalink to this definition")

Return Series with duplicate values removed.

Parameters

**keep**{‘first’, ‘last’, `False`}, default ‘first’

Method to handle dropping duplicates: - ‘first’ : Drop duplicates except for the first occurrence. - ‘last’ : Drop duplicates except for the last occurrence. - `False` : Drop all duplicates.

**inplace**bool, default `False`

If `True`, performs operation inplace and returns None.

Returns

Series

Series with duplicates dropped.

Examples

Generate a Series with duplicated entries.

```
>>> s = ps.Series(['lama', 'cow', 'lama', 'beetle', 'lama', 'hippo'],
...               name='animal')
>>> s.sort_index()
0      lama
1       cow
2      lama
3    beetle
4      lama
5     hippo
Name: animal, dtype: object

```


With the ‘keep’ parameter, the selection behavior of duplicated values can be changed. The value ‘first’ keeps the first occurrence for each set of duplicated entries. The default value of keep is ‘first’.

```
>>> s.drop_duplicates().sort_index()
0      lama
1       cow
3    beetle
5     hippo
Name: animal, dtype: object

```


The value ‘last’ for parameter ‘keep’ keeps the last occurrence for each set of duplicated entries.

```
>>> s.drop_duplicates(keep='last').sort_index()
1       cow
3    beetle
4      lama
5     hippo
Name: animal, dtype: object

```


The value `False` for parameter ‘keep’ discards all sets of duplicated entries. Setting the value of ‘inplace’ to `True` performs the operation inplace and returns `None`.

```
>>> s.drop_duplicates(keep=False, inplace=True)
>>> s.sort_index()
1       cow
3    beetle
5     hippo
Name: animal, dtype: object

```


# pyspark.pandas.Series.duplicated — PySpark 4.0.1 documentation
Series.duplicated(_keep\='first'_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.duplicated)
[#](#pyspark.pandas.Series.duplicated "Permalink to this definition")

Indicate duplicate Series values.

Duplicated values are indicated as `True` values in the resulting Series. Either all duplicates, all except the first or all except the last occurrence of duplicates can be indicated.

New in version 3.4.0.

Parameters

**keep**{‘first’, ‘last’, False}, default ‘first’

Method to handle marking duplicates: - ‘first’ : Mark duplicates as `True` except for the first occurrence. - ‘last’ : Mark duplicates as `True` except for the last occurrence. - `False` : Mark all duplicates as `True`.

Returns

Series

Series indicating whether each value has occurred in the preceding values

Examples

By default, for each set of duplicated values, the first occurrence is set on False and all others on True:

```
>>> animals = ps.Series(['lama', 'cow', 'lama', 'beetle', 'lama'])
>>> animals.duplicated().sort_index()
0    False
1    False
2     True
3    False
4     True
dtype: bool

```


which is equivalent to

```
>>> animals.duplicated(keep='first').sort_index()
0    False
1    False
2     True
3    False
4     True
dtype: bool

```


By using ‘last’, the last occurrence of each set of duplicated values is set on False and all others on True:

```
>>> animals.duplicated(keep='last').sort_index()
0     True
1    False
2     True
3    False
4    False
dtype: bool

```


By setting keep on `False`, all duplicates are True:

```
>>> animals.duplicated(keep=False).sort_index()
0     True
1    False
2     True
3    False
4     True
dtype: bool

```


# pyspark.pandas.Series.equals — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.equals

Series.equals(_other_)
[#](#pyspark.pandas.Series.equals "Permalink to this definition")

Compare if the current value is equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.a == 1
a     True
b    False
c    False
d    False
Name: a, dtype: bool

```


```
>>> df.b.eq(1)
a     True
b    False
c     True
d    False
Name: b, dtype: bool

```



# pyspark.pandas.Series.add_prefix — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.add\_prefix

Series.add\_prefix(_prefix_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.add_prefix)
[#](#pyspark.pandas.Series.add_prefix "Permalink to this definition")

Prefix labels with string prefix.

For Series, the row labels are prefixed. For DataFrame, the column labels are prefixed.

Parameters

**prefix**str

The string to add before each label.

Returns

Series

New Series with updated labels.

See also

[`Series.add_suffix`](about:blank/pyspark.pandas.Series.add_suffix.html#pyspark.pandas.Series.add_suffix "pyspark.pandas.Series.add_suffix")

Suffix column labels with string suffix.

[`DataFrame.add_suffix`](about:blank/pyspark.pandas.DataFrame.add_suffix.html#pyspark.pandas.DataFrame.add_suffix "pyspark.pandas.DataFrame.add_suffix")

Suffix column labels with string suffix.

[`DataFrame.add_prefix`](about:blank/pyspark.pandas.DataFrame.add_prefix.html#pyspark.pandas.DataFrame.add_prefix "pyspark.pandas.DataFrame.add_prefix")

Prefix column labels with string prefix.

Examples

```
>>> s = ps.Series([1, 2, 3, 4])
>>> s
0    1
1    2
2    3
3    4
dtype: int64

```


```
>>> s.add_prefix('item_')
item_0    1
item_1    2
item_2    3
item_3    4
dtype: int64

```


[Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Series.add_prefix.rst.txt)


# pyspark.pandas.Series.first — PySpark 4.0.1 documentation
Series.first(_offset_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.first)
[#](#pyspark.pandas.Series.first "Permalink to this definition")

Select first periods of time series data based on a date offset.

When having a Series with dates as index, this function can select the first few elements based on a date offset.

Deprecated since version 4.0.0.

Parameters

**offset**str or DateOffset

The offset length of the data that will be selected. For instance, ‘3D’ will display all the rows having their index within the first 3 days.

Returns

Series

A subset of the caller.

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

Examples

```
>>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
>>> psser = ps.Series([1, 2, 3, 4], index=index)
>>> psser
2018-04-09    1
2018-04-11    2
2018-04-13    3
2018-04-15    4
dtype: int64

```


Get the rows for the first 3 days:

```
>>> psser.first('3D')
2018-04-09    1
2018-04-11    2
dtype: int64

```


Notice the data for 3 first calendar days were returned, not the first 3 observed days in the dataset, and therefore data for 2018-04-13 was not returned.


# pyspark.pandas.Series.head — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.head

Series.head(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.head)
[#](#pyspark.pandas.Series.head "Permalink to this definition")

Return the first n rows.

This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.

Parameters

**n**Integer, default = 5

Returns

The first n rows of the caller object.

Examples

```
>>> df = ps.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion']})
>>> df.animal.head(2)  
0     alligator
1     bee
Name: animal, dtype: object

```


# pyspark.pandas.Series.idxmax — PySpark 4.0.1 documentation
Series.idxmax(_skipna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.idxmax)
[#](#pyspark.pandas.Series.idxmax "Permalink to this definition")

Return the row label of the maximum value.

If multiple values equal the maximum, the first row label with that value is returned.

Parameters

**skipna**bool, default True

Exclude NA/null values. If the entire Series is NA, the result will be NA.

Returns

Index

Label of the maximum value.

Raises

ValueError

If the Series is empty.

See also

[`Series.idxmin`](about:blank/pyspark.pandas.Series.idxmin.html#pyspark.pandas.Series.idxmin "pyspark.pandas.Series.idxmin")

Return index _label_ of the first occurrence of minimum of values.

Examples

```
>>> s = ps.Series(data=[1, None, 4, 3, 5],
...               index=['A', 'B', 'C', 'D', 'E'])
>>> s
A    1.0
B    NaN
C    4.0
D    3.0
E    5.0
dtype: float64

```


If skipna is False and there is an NA value in the data, the function returns `nan`.

```
>>> s.idxmax(skipna=False)
nan

```


In case of multi-index, you get a tuple:

```
>>> index = pd.MultiIndex.from_arrays([
...     ['a', 'a', 'b', 'b'], ['c', 'd', 'e', 'f']], names=('first', 'second'))
>>> s = ps.Series(data=[1, None, 4, 5], index=index)
>>> s
first  second
a      c         1.0
       d         NaN
b      e         4.0
       f         5.0
dtype: float64

```


```
>>> s.idxmax()
('b', 'f')

```


If multiple values equal the maximum, the first row label with that value is returned.

```
>>> s = ps.Series([1, 100, 1, 100, 1, 100], index=[10, 3, 5, 2, 1, 8])
>>> s
10      1
3     100
5       1
2     100
1       1
8     100
dtype: int64

```


# pyspark.pandas.Series.idxmin — PySpark 4.0.1 documentation
Series.idxmin(_skipna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.idxmin)
[#](#pyspark.pandas.Series.idxmin "Permalink to this definition")

Return the row label of the minimum value.

If multiple values equal the minimum, the first row label with that value is returned.

Parameters

**skipna**bool, default True

Exclude NA/null values. If the entire Series is NA, the result will be NA.

Returns

Index

Label of the minimum value.

Raises

ValueError

If the Series is empty.

See also

[`Series.idxmax`](about:blank/pyspark.pandas.Series.idxmax.html#pyspark.pandas.Series.idxmax "pyspark.pandas.Series.idxmax")

Return index _label_ of the first occurrence of maximum of values.

Notes

This method is the Series version of `ndarray.argmin`. This method returns the label of the minimum, while `ndarray.argmin` returns the position. To get the position, use `series.values.argmin()`.

Examples

```
>>> s = ps.Series(data=[1, None, 4, 0],
...               index=['A', 'B', 'C', 'D'])
>>> s
A    1.0
B    NaN
C    4.0
D    0.0
dtype: float64

```


If skipna is False and there is an NA value in the data, the function returns `nan`.

```
>>> s.idxmin(skipna=False)
nan

```


In case of multi-index, you get a tuple:

```
>>> index = pd.MultiIndex.from_arrays([
...     ['a', 'a', 'b', 'b'], ['c', 'd', 'e', 'f']], names=('first', 'second'))
>>> s = ps.Series(data=[1, None, 4, 0], index=index)
>>> s
first  second
a      c         1.0
       d         NaN
b      e         4.0
       f         0.0
dtype: float64

```


```
>>> s.idxmin()
('b', 'f')

```


If multiple values equal the minimum, the first row label with that value is returned.

```
>>> s = ps.Series([1, 100, 1, 100, 1, 100], index=[10, 3, 5, 2, 1, 8])
>>> s
10      1
3     100
5       1
2     100
1       1
8     100
dtype: int64

```


# pyspark.pandas.Series.isin — PySpark 4.0.1 documentation
Series.isin(_values_)
[#](#pyspark.pandas.Series.isin "Permalink to this definition")

Check whether values are contained in Series or Index.

Return a boolean Series or Index showing whether each element in the Series matches an element in the passed sequence of values exactly.

Parameters

**values**set or list-like

The sequence of values to test.

Returns

**isin**Series (bool dtype) or Index (bool dtype)

Examples

```
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

```


Passing a single string as `s.isin('lama')` will raise an error. Use a list of one element instead:

```
>>> s.isin(['lama'])
0     True
1    False
2     True
3    False
4     True
5    False
Name: animal, dtype: bool

```


```
>>> s.rename("a").to_frame().set_index("a").index.isin(['lama'])  
Index([True, False, True, False, True, False], dtype='bool', name='a')

```


# pyspark.pandas.Series.last — PySpark 4.0.1 documentation
Series.last(_offset_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.last)
[#](#pyspark.pandas.Series.last "Permalink to this definition")

Select final periods of time series data based on a date offset.

When having a Series with dates as index, this function can select the last few elements based on a date offset.

Deprecated since version 4.0.0.

Parameters

**offset**str or DateOffset

The offset length of the data that will be selected. For instance, ‘3D’ will display all the rows having their index within the last 3 days.

Returns

Series

A subset of the caller.

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

Examples

```
>>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
>>> psser = ps.Series([1, 2, 3, 4], index=index)
>>> psser
2018-04-09    1
2018-04-11    2
2018-04-13    3
2018-04-15    4
dtype: int64

```


Get the rows for the last 3 days:

```
>>> psser.last('3D')
2018-04-13    3
2018-04-15    4
dtype: int64

```


Notice the data for 3 last calendar days were returned, not the last 3 observed days in the dataset, and therefore data for 2018-04-11 was not returned.


# pyspark.pandas.Series.rename — PySpark 4.0.1 documentation
Series.rename(_index\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rename)
[#](#pyspark.pandas.Series.rename "Permalink to this definition")

Alter Series index labels or name.

Parameters

**index**scalar or function, optional

Functions are transformations to apply to the index. Scalar will alter the Series.name attribute.

**inplace**bool, default False

Whether to return a new Series. If True then value of copy is ignored.

Returns

Series

Series with index labels or name altered.

Examples

```
>>> s = ps.Series([1, 2, 3])
>>> s
0    1
1    2
2    3
dtype: int64

```


```
>>> s.rename("my_name")  # scalar, changes Series.name
0    1
1    2
2    3
Name: my_name, dtype: int64

```


```
>>> s.rename(lambda x: x ** 2)  # function, changes labels
0    1
1    2
4    3
dtype: int64

```


# pyspark.pandas.Series.rename_axis — PySpark 4.0.1 documentation
Series.rename\_axis(_mapper\=None_, _index\=None_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.rename_axis)
[#](#pyspark.pandas.Series.rename_axis "Permalink to this definition")

Set the name of the axis for the index or columns.

Parameters

**mapper, index**scalar, list-like, dict-like or function, optional

A scalar, list-like, dict-like or functions transformations to apply to the index values.

**inplace**bool, default False

Modifies the object directly, instead of creating a new Series.

Returns

Series, or None if inplace is True.

Examples

```
>>> s = ps.Series(["dog", "cat", "monkey"], name="animal")
>>> s  
0       dog
1       cat
2    monkey
Name: animal, dtype: object
>>> s.rename_axis("index").sort_index()  
index
0       dog
1       cat
2    monkey
Name: animal, dtype: object

```


**MultiIndex**

```
>>> index = pd.MultiIndex.from_product([['mammal'],
...                                        ['dog', 'cat', 'monkey']],
...                                       names=['type', 'name'])
>>> s = ps.Series([4, 4, 2], index=index, name='num_legs')
>>> s  
type    name
mammal  dog       4
        cat       4
        monkey    2
Name: num_legs, dtype: int64
>>> s.rename_axis(index={'type': 'class'}).sort_index()  
class   name
mammal  cat       4
        dog       4
        monkey    2
Name: num_legs, dtype: int64
>>> s.rename_axis(index=str.upper).sort_index()  
TYPE    NAME
mammal  cat       4
        dog       4
        monkey    2
Name: num_legs, dtype: int64

```


# pyspark.pandas.Series.reindex — PySpark 4.0.1 documentation
Series.reindex(_index\=None_, _fill\_value\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.reindex)
[#](#pyspark.pandas.Series.reindex "Permalink to this definition")

Conform Series to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index. A new object is produced.

Parameters

**index: array-like, optional**

New labels / index to conform to, should be specified using keywords. Preferably an Index object to avoid duplicating data

**fill\_value**scalar, default np.nan

Value to use for missing values. Defaults to NaN, but can be any “compatible” value.

Returns

Series with changed index.

Examples

Create a series with some fictional data.

```
>>> index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
>>> ser = ps.Series([200, 200, 404, 404, 301],
...                 index=index, name='http_status')
>>> ser
Firefox      200
Chrome       200
Safari       404
IE10         404
Konqueror    301
Name: http_status, dtype: int64

```


Create a new index and reindex the Series. By default values in the new index that do not have corresponding records in the Series are assigned `NaN`.

```
>>> new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10',
...             'Chrome']
>>> ser.reindex(new_index).sort_index()
Chrome           200.0
Comodo Dragon      NaN
IE10             404.0
Iceweasel          NaN
Safari           404.0
Name: http_status, dtype: float64

```


We can fill in the missing values by passing a value to the keyword `fill_value`.

```
>>> ser.reindex(new_index, fill_value=0).sort_index()
Chrome           200
Comodo Dragon      0
IE10             404
Iceweasel          0
Safari           404
Name: http_status, dtype: int64

```


To further illustrate the filling functionality in `reindex`, we will create a Series with a monotonically increasing index (for example, a sequence of dates).

```
>>> date_index = pd.date_range('1/1/2010', periods=6, freq='D')
>>> ser2 = ps.Series([100, 101, np.nan, 100, 89, 88],
...                  name='prices', index=date_index)
>>> ser2.sort_index()
2010-01-01    100.0
2010-01-02    101.0
2010-01-03      NaN
2010-01-04    100.0
2010-01-05     89.0
2010-01-06     88.0
Name: prices, dtype: float64

```


Suppose we decide to expand the series to cover a wider date range.

```
>>> date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
>>> ser2.reindex(date_index2).sort_index()
2009-12-29      NaN
2009-12-30      NaN
2009-12-31      NaN
2010-01-01    100.0
2010-01-02    101.0
2010-01-03      NaN
2010-01-04    100.0
2010-01-05     89.0
2010-01-06     88.0
2010-01-07      NaN
Name: prices, dtype: float64

```


# pyspark.pandas.Series.reindex_like — PySpark 4.0.1 documentation
Series.reindex\_like(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.reindex_like)
[#](#pyspark.pandas.Series.reindex_like "Permalink to this definition")

Return a Series with matching indices as other object.

Conform the object to the same index on all axes. Places NA/NaN in locations having no value in the previous index.

Parameters

**other**Series or DataFrame

Its row and column indices are used to define the new indices of this object.

Returns

Series

Series with changed indices on each axis.

Notes

Same as calling `.reindex(index=other.index, ...)`.

Examples

```
>>> s1 = ps.Series([24.3, 31.0, 22.0, 35.0],
...                index=pd.date_range(start='2014-02-12',
...                                    end='2014-02-15', freq='D'),
...                name="temp_celsius")
>>> s1
2014-02-12    24.3
2014-02-13    31.0
2014-02-14    22.0
2014-02-15    35.0
Name: temp_celsius, dtype: float64

```


```
>>> s2 = ps.Series(["low", "low", "medium"],
...                index=pd.DatetimeIndex(['2014-02-12', '2014-02-13',
...                                        '2014-02-15']),
...                name="winspeed")
>>> s2
2014-02-12       low
2014-02-13       low
2014-02-15    medium
Name: winspeed, dtype: object

```


```
>>> s2.reindex_like(s1).sort_index()
2014-02-12       low
2014-02-13       low
2014-02-14      None
2014-02-15    medium
Name: winspeed, dtype: object

```

# pyspark.pandas.Series.sample — PySpark 4.0.1 documentation
Series.sample(_n\=None_, _frac\=None_, _replace\=False_, _random\_state\=None_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.sample)
[#](#pyspark.pandas.Series.sample "Permalink to this definition")

Return a random sample of items from an axis of object.

Please call this function using named argument by specifying the `frac` argument.

You can use random\_state for reproducibility. However, note that different from pandas, specifying a seed in pandas-on-Spark/Spark does not guarantee the sampled rows will be fixed. The result set depends on not only the seed, but also how the data is distributed across machines and to some extent network randomness when shuffle operations are involved. Even in the simplest case, the result set will depend on the system’s CPU core count.

Parameters

**n**int, optional

Number of items to return. This is currently NOT supported. Use frac instead.

**frac**float, optional

Fraction of axis items to return.

**replace**bool, default False

Sample with or without replacement.

**random\_state**int, optional

Seed for the random number generator (if int).

**ignore\_index**bool, default False

If True, the resulting index will be labeled 0, 1, …, n - 1.

New in version 3.4.0.

Returns

Series or DataFrame

A new object of same type as caller containing the sampled items.

Examples

```
>>> df = ps.DataFrame({'num_legs': [2, 4, 8, 0],
...                    'num_wings': [2, 0, 0, 0],
...                    'num_specimen_seen': [10, 2, 1, 8]},
...                   index=['falcon', 'dog', 'spider', 'fish'],
...                   columns=['num_legs', 'num_wings', 'num_specimen_seen'])
>>> df  
        num_legs  num_wings  num_specimen_seen
falcon         2          2                 10
dog            4          0                  2
spider         8          0                  1
fish           0          0                  8

```


A random 25% sample of the `DataFrame`. Note that we use random\_state to ensure the reproducibility of the examples.

```
>>> df.sample(frac=0.25, random_state=1)  
        num_legs  num_wings  num_specimen_seen
falcon         2          2                 10
fish           0          0                  8

```


A random 50% sample of the `DataFrame`, while ignoring the index.

```
>>> df.sample(frac=0.5, random_state=1, ignore_index=True)  
   num_legs  num_wings  num_specimen_seen
0         4          0                  2
1         8          0                  1
2         0          0                  8

```


Extract 25% random elements from the `Series` `df['num_legs']` with replacement so, the same items could appear more than once.

```
>>> df['num_legs'].sample(frac=0.4, replace=True, random_state=1)  
falcon    2
spider    8
spider    8
Name: num_legs, dtype: int64

```


Specifying the exact number of items to return is not supported now.

```
>>> df.sample(n=5)  
Traceback (most recent call last):
    ...
NotImplementedError: Function sample currently does not support specifying ...

```


# pyspark.pandas.Series.searchsorted — PySpark 4.0.1 documentation
Series.searchsorted(_value_, _side\='left'_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.searchsorted)
[#](#pyspark.pandas.Series.searchsorted "Permalink to this definition")

Find indices where elements should be inserted to maintain order.

Find the indices into a sorted Series self such that, if the corresponding elements in value were inserted before the indices, the order of self would be preserved.

New in version 3.4.0.

Parameters

**value**scalar

Values to insert into self.

**side**{‘left’, ‘right’}, optional

If ‘left’, the index of the first suitable location found is given. If ‘right’, return the last such index. If there is no suitable index, return either 0 or N (where N is the length of self).

Returns

int

insertion point

Notes

The Series must be monotonically sorted, otherwise wrong locations will likely be returned.

Examples

```
>>> ser = ps.Series([1, 2, 2, 3])
>>> ser.searchsorted(0)
0
>>> ser.searchsorted(1)
0
>>> ser.searchsorted(2)
1
>>> ser.searchsorted(5)
4
>>> ser.searchsorted(0, side="right")
0
>>> ser.searchsorted(1, side="right")
1
>>> ser.searchsorted(2, side="right")
3
>>> ser.searchsorted(5, side="right")
4

```


# pyspark.pandas.Series.swaplevel — PySpark 4.0.1 documentation
Series.swaplevel(_i\=\- 2_, _j\=\- 1_, _copy\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.swaplevel)
[#](#pyspark.pandas.Series.swaplevel "Permalink to this definition")

Swap levels i and j in a MultiIndex. Default is to swap the two innermost levels of the index.

Parameters

**i, j**int, str

Level of the indices to be swapped. Can pass level name as string.

**copy**bool, default True

Whether to copy underlying data. Must be True.

Returns

Series

Series with levels swapped in MultiIndex.

Examples

```
>>> midx = pd.MultiIndex.from_arrays([['a', 'b'], [1, 2]], names = ['word', 'number'])
>>> midx  
MultiIndex([('a', 1),
            ('b', 2)],
           names=['word', 'number'])
>>> psser = ps.Series(['x', 'y'], index=midx)
>>> psser
word  number
a     1         x
b     2         y
dtype: object
>>> psser.swaplevel()
number  word
1       a       x
2       b       y
dtype: object
>>> psser.swaplevel(0, 1)
number  word
1       a       x
2       b       y
dtype: object
>>> psser.swaplevel('number', 'word')
number  word
1       a       x
2       b       y
dtype: object

```


# pyspark.pandas.Series.swapaxes — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.swapaxes

Series.swapaxes(_i_, _j_, _copy\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.swapaxes)
[#](#pyspark.pandas.Series.swapaxes "Permalink to this definition")

Interchange axes and swap values axes appropriately.

Deprecated since version 4.0.0.

Parameters

**i: {0 or ‘index’, 1 or ‘columns’}. The axis to swap.**

**j: {0 or ‘index’, 1 or ‘columns’}. The axis to swap.**

**copy**bool, default True.

Returns

Series

Examples

```
>>> psser = ps.Series([1, 2, 3], index=["x", "y", "z"])
>>> psser
x    1
y    2
z    3
dtype: int64
>>>
>>> psser.swapaxes(0, 0)
x    1
y    2
z    3
dtype: int64

```


# pyspark.pandas.Series.take — PySpark 4.0.1 documentation
Series.take(_indices_)
[#](#pyspark.pandas.Series.take "Permalink to this definition")

Return the elements in the given _positional_ indices along an axis.

This means that we are not indexing according to actual values in the index attribute of the object. We are indexing according to the actual position of the element in the object.

Parameters

**indices**array-like

An array of ints indicating which positions to take.

Returns

**taken**same type as caller

An array-like containing the elements taken from the object.

See also

[`DataFrame.loc`](about:blank/pyspark.pandas.DataFrame.loc.html#pyspark.pandas.DataFrame.loc "pyspark.pandas.DataFrame.loc")

Select a subset of a DataFrame by labels.

[`DataFrame.iloc`](about:blank/pyspark.pandas.DataFrame.iloc.html#pyspark.pandas.DataFrame.iloc "pyspark.pandas.DataFrame.iloc")

Select a subset of a DataFrame by positions.

`numpy.take`

Take elements from an array along an axis.

Examples

Series

```
>>> psser = ps.Series([100, 200, 300, 400, 500])
>>> psser
0    100
1    200
2    300
3    400
4    500
dtype: int64

```


```
>>> psser.take([0, 2, 4]).sort_index()
0    100
2    300
4    500
dtype: int64

```


Index

```
>>> psidx = ps.Index([100, 200, 300, 400, 500])
>>> psidx
Index([100, 200, 300, 400, 500], dtype='int64')

```


```
>>> psidx.take([0, 2, 4]).sort_values()
Index([100, 300, 500], dtype='int64')

```


MultiIndex

```
>>> psmidx = ps.MultiIndex.from_tuples([("x", "a"), ("x", "b"), ("x", "c")])
>>> psmidx  
MultiIndex([('x', 'a'),
            ('x', 'b'),
            ('x', 'c')],
           )

```


```
>>> psmidx.take([0, 2])  
MultiIndex([('x', 'a'),
            ('x', 'c')],
           )

```


# pyspark.pandas.Series.tail — PySpark 4.0.1 documentation
Series.tail(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.tail)
[#](#pyspark.pandas.Series.tail "Permalink to this definition")

Return the last n rows.

This function returns last n rows from the object based on position. It is useful for quickly verifying data, for example, after sorting or appending rows.

For negative values of n, this function returns all rows except the first n rows, equivalent to `df[n:]`.

Parameters

**n**int, default 5

Number of rows to select.

Returns

type of caller

The last n rows of the caller object.

Examples

```
>>> psser = ps.Series([1, 2, 3, 4, 5])
>>> psser
0    1
1    2
2    3
3    4
4    5
dtype: int64

```


```
>>> psser.tail(3)  
2    3
3    4
4    5
dtype: int64

```


# pyspark.pandas.Series.where — PySpark 4.0.1 documentation
Series.where(_cond_, _other\=nan_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.where)
[#](#pyspark.pandas.Series.where "Permalink to this definition")

Replace values where the condition is False.

Parameters

**cond**boolean Series

Where cond is True, keep the original value. Where False, replace with corresponding value from other.

**other**scalar, Series

Entries where cond is False are replaced with corresponding value from other.

Returns

Series

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> s1 = ps.Series([0, 1, 2, 3, 4])
>>> s2 = ps.Series([100, 200, 300, 400, 500])
>>> s1.where(s1 > 0).sort_index()
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64

```


```
>>> s1.where(s1 > 1, 10).sort_index()
0    10
1    10
2     2
3     3
4     4
dtype: int64

```


```
>>> s1.where(s1 > 1, s1 + 100).sort_index()
0    100
1    101
2      2
3      3
4      4
dtype: int64

```


```
>>> s1.where(s1 > 1, s2).sort_index()
0    100
1    200
2      2
3      3
4      4
dtype: int64

```


```
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.Series.mask — PySpark 4.0.1 documentation
Series.mask(_cond_, _other\=nan_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.mask)
[#](#pyspark.pandas.Series.mask "Permalink to this definition")

Replace values where the condition is True.

Parameters

**cond**boolean Series

Where cond is False, keep the original value. Where True, replace with corresponding value from other.

**other**scalar, Series

Entries where cond is True are replaced with corresponding value from other.

Returns

Series

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> s1 = ps.Series([0, 1, 2, 3, 4])
>>> s2 = ps.Series([100, 200, 300, 400, 500])
>>> s1.mask(s1 > 0).sort_index()
0    0.0
1    NaN
2    NaN
3    NaN
4    NaN
dtype: float64

```


```
>>> s1.mask(s1 > 1, 10).sort_index()
0     0
1     1
2    10
3    10
4    10
dtype: int64

```


```
>>> s1.mask(s1 > 1, s1 + 100).sort_index()
0      0
1      1
2    102
3    103
4    104
dtype: int64

```


```
>>> s1.mask(s1 > 1, s2).sort_index()
0      0
1      1
2    300
3    400
4    500
dtype: int64

```


```
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.Series.truncate — PySpark 4.0.1 documentation
Series.truncate(_before\=None_, _after\=None_, _axis\=None_, _copy\=True_)
[#](#pyspark.pandas.Series.truncate "Permalink to this definition")

Truncate a Series or DataFrame before and after some index value.

This is a useful shorthand for boolean indexing based on index values above or below certain thresholds.

Parameters

**before: date, str, int**

Truncate all rows before this index value.

**after: date, str, int**

Truncate all rows after this index value.

**axis: {0 or ‘index’, 1 or ‘columns’}, optional**

Axis to truncate. Truncates the index (rows) by default.

**copy: bool, default is True,**

Return a copy of the truncated section.

Returns

type of caller

The truncated Series or DataFrame.

Examples

```
>>> df = ps.DataFrame({'A': ['a', 'b', 'c', 'd', 'e'],
...                    'B': ['f', 'g', 'h', 'i', 'j'],
...                    'C': ['k', 'l', 'm', 'n', 'o']},
...                   index=[1, 2, 3, 4, 5])
>>> df
   A  B  C
1  a  f  k
2  b  g  l
3  c  h  m
4  d  i  n
5  e  j  o

```


```
>>> df.truncate(before=2, after=4)
   A  B  C
2  b  g  l
3  c  h  m
4  d  i  n

```


The columns of a DataFrame can be truncated.

```
>>> df.truncate(before="A", after="B", axis="columns")
   A  B
1  a  f
2  b  g
3  c  h
4  d  i
5  e  j

```


For Series, only rows can be truncated.

```
>>> df['A'].truncate(before=2, after=4)
2    b
3    c
4    d
Name: A, dtype: object

```


A Series has index that sorted integers.

```
>>> s = ps.Series([10, 20, 30, 40, 50, 60, 70],
...               index=[1, 2, 3, 4, 5, 6, 7])
>>> s
1    10
2    20
3    30
4    40
5    50
6    60
7    70
dtype: int64

```


```
>>> s.truncate(2, 5)
2    20
3    30
4    40
5    50
dtype: int64

```


A Series has index that sorted strings.

```
>>> s = ps.Series([10, 20, 30, 40, 50, 60, 70],
...               index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
>>> s
a    10
b    20
c    30
d    40
e    50
f    60
g    70
dtype: int64

```


```
>>> s.truncate('b', 'e')
b    20
c    30
d    40
e    50
dtype: int64

```


# pyspark.pandas.Series.backfill — PySpark 4.0.1 documentation
Series.backfill(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.Series.backfill "Permalink to this definition")

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`bfill` ``.

Note

the current implementation of ‘bfill’ uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**axis: {0 or \`index\`}**

1 and columns are not supported.

**inplace: boolean, default False**

Fill in place (do not create a new object)

**limit: int, default None**

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Returns

DataFrame or Series

DataFrame or Series with NA entries filled.

Examples

```
>>> psdf = ps.DataFrame({
...     'A': [None, 3, None, None],
...     'B': [2, 4, None, 3],
...     'C': [None, None, None, 1],
...     'D': [0, 1, 5, 4]
...     },
...     columns=['A', 'B', 'C', 'D'])
>>> psdf
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  NaN  NaN  NaN  5
3  NaN  3.0  1.0  4

```


Propagate non-null values backward.

```
>>> psdf.bfill()
     A    B    C  D
0  3.0  2.0  1.0  0
1  3.0  4.0  1.0  1
2  NaN  3.0  1.0  5
3  NaN  3.0  1.0  4

```


For Series

```
>>> psser = ps.Series([None, None, None, 1])
>>> psser
0    NaN
1    NaN
2    NaN
3    1.0
dtype: float64

```


```
>>> psser.bfill()
0    1.0
1    1.0
2    1.0
3    1.0
dtype: float64

```


# pyspark.pandas.Series.bfill — PySpark 4.0.1 documentation
Series.bfill(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.Series.bfill "Permalink to this definition")

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`bfill` ``.

Note

the current implementation of ‘bfill’ uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**axis: {0 or \`index\`}**

1 and columns are not supported.

**inplace: boolean, default False**

Fill in place (do not create a new object)

**limit: int, default None**

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Returns

DataFrame or Series

DataFrame or Series with NA entries filled.

Examples

```
>>> psdf = ps.DataFrame({
...     'A': [None, 3, None, None],
...     'B': [2, 4, None, 3],
...     'C': [None, None, None, 1],
...     'D': [0, 1, 5, 4]
...     },
...     columns=['A', 'B', 'C', 'D'])
>>> psdf
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  NaN  NaN  NaN  5
3  NaN  3.0  1.0  4

```


Propagate non-null values backward.

```
>>> psdf.bfill()
     A    B    C  D
0  3.0  2.0  1.0  0
1  3.0  4.0  1.0  1
2  NaN  3.0  1.0  5
3  NaN  3.0  1.0  4

```


For Series

```
>>> psser = ps.Series([None, None, None, 1])
>>> psser
0    NaN
1    NaN
2    NaN
3    1.0
dtype: float64

```


```
>>> psser.bfill()
0    1.0
1    1.0
2    1.0
3    1.0
dtype: float64

```


# pyspark.pandas.Series.ffill — PySpark 4.0.1 documentation
Series.ffill(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.Series.ffill "Permalink to this definition")

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`ffill` ``.

Note

the current implementation of ‘ffill’ uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single a partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**axis: {0 or \`index\`}**

1 and columns are not supported.

**inplace: boolean, default False**

Fill in place (do not create a new object)

**limit: int, default None**

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Returns

DataFrame or Series

DataFrame or Series with NA entries filled.

Examples

```
>>> psdf = ps.DataFrame({
...     'A': [None, 3, None, None],
...     'B': [2, 4, None, 3],
...     'C': [None, None, None, 1],
...     'D': [0, 1, 5, 4]
...     },
...     columns=['A', 'B', 'C', 'D'])
>>> psdf
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  NaN  NaN  NaN  5
3  NaN  3.0  1.0  4

```


Propagate non-null values forward.

```
>>> psdf.ffill()
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  3.0  4.0  NaN  5
3  3.0  3.0  1.0  4

```


For Series

```
>>> psser = ps.Series([2, 4, None, 3])
>>> psser
0    2.0
1    4.0
2    NaN
3    3.0
dtype: float64

```


```
>>> psser.ffill()
0    2.0
1    4.0
2    4.0
3    3.0
dtype: float64

```


# pyspark.pandas.Series.isna — PySpark 4.0.1 documentation
Series.isna()
[#](#pyspark.pandas.Series.isna "Permalink to this definition")

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, get mapped to True values. Everything else gets mapped to False values. Characters such as empty strings ‘’ or numpy.inf are not considered NA values

Returns

**Series or Index**Mask of bool values for each element in Series

that indicates whether an element is not an NA value.

Examples

```
>>> ser = ps.Series([5, 6, np.nan])
>>> ser.isna()  
0    False
1    False
2     True
dtype: bool

```


```
>>> ser.rename("a").to_frame().set_index("a").index.isna()  
Index([False, False, True], dtype='bool', name='a')

```


# pyspark.pandas.Series.isnull — PySpark 4.0.1 documentation
Series.isnull()
[#](#pyspark.pandas.Series.isnull "Permalink to this definition")

Detect existing (non-missing) values.

Return a boolean same-sized object indicating if the values are NA. NA values, such as None or numpy.NaN, get mapped to True values. Everything else gets mapped to False values. Characters such as empty strings ‘’ or numpy.inf are not considered NA values

Returns

**Series or Index**Mask of bool values for each element in Series

that indicates whether an element is not an NA value.

Examples

```
>>> ser = ps.Series([5, 6, np.nan])
>>> ser.isna()  
0    False
1    False
2     True
dtype: bool

```


```
>>> ser.rename("a").to_frame().set_index("a").index.isna()  
Index([False, False, True], dtype='bool', name='a')

```


# pyspark.pandas.Series.notna — PySpark 4.0.1 documentation
Series.notna()
[#](#pyspark.pandas.Series.notna "Permalink to this definition")

Detect existing (non-missing) values. Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. Characters such as empty strings ‘’ or numpy.inf are not considered NA values NA values, such as None or numpy.NaN, get mapped to False values.

Returns

**Series or Index**Mask of bool values for each element in Series

that indicates whether an element is not an NA value.

Examples

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
>>> ser.notna()
0     True
1     True
2    False
dtype: bool

```


```
>>> ser.rename("a").to_frame().set_index("a").index.notna()  
Index([True, True, False], dtype='bool', name='a')

```


# pyspark.pandas.Series.notnull — PySpark 4.0.1 documentation
Series.notnull()
[#](#pyspark.pandas.Series.notnull "Permalink to this definition")

Detect existing (non-missing) values. Return a boolean same-sized object indicating if the values are not NA. Non-missing values get mapped to True. Characters such as empty strings ‘’ or numpy.inf are not considered NA values NA values, such as None or numpy.NaN, get mapped to False values.

Returns

**Series or Index**Mask of bool values for each element in Series

that indicates whether an element is not an NA value.

Examples

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
>>> ser.notna()
0     True
1     True
2    False
dtype: bool

```


```
>>> ser.rename("a").to_frame().set_index("a").index.notna()  
Index([True, True, False], dtype='bool', name='a')

```


# pyspark.pandas.Series.pad — PySpark 4.0.1 documentation
Series.pad(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.Series.pad "Permalink to this definition")

Synonym for DataFrame.fillna() or Series.fillna() with `` method=`ffill` ``.

Note

the current implementation of ‘ffill’ uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single a partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**axis: {0 or \`index\`}**

1 and columns are not supported.

**inplace: boolean, default False**

Fill in place (do not create a new object)

**limit: int, default None**

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Returns

DataFrame or Series

DataFrame or Series with NA entries filled.

Examples

```
>>> psdf = ps.DataFrame({
...     'A': [None, 3, None, None],
...     'B': [2, 4, None, 3],
...     'C': [None, None, None, 1],
...     'D': [0, 1, 5, 4]
...     },
...     columns=['A', 'B', 'C', 'D'])
>>> psdf
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  NaN  NaN  NaN  5
3  NaN  3.0  1.0  4

```


Propagate non-null values forward.

```
>>> psdf.ffill()
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  3.0  4.0  NaN  5
3  3.0  3.0  1.0  4

```


For Series

```
>>> psser = ps.Series([2, 4, None, 3])
>>> psser
0    2.0
1    4.0
2    NaN
3    3.0
dtype: float64

```


```
>>> psser.ffill()
0    2.0
1    4.0
2    4.0
3    3.0
dtype: float64

```

# pyspark.pandas.Series.dropna — PySpark 4.0.1 documentation
Series.dropna(_axis\=0_, _inplace\=False_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.dropna)
[#](#pyspark.pandas.Series.dropna "Permalink to this definition")

Return a new Series with missing values removed.

Parameters

**axis**{0 or ‘index’}, default 0

There is only one axis to drop values from.

**inplace**bool, default False

If True, do operation inplace and return None.

**\*\*kwargs**

Not in use.

Returns

Series

Series with NA entries dropped from it.

Examples

```
>>> ser = ps.Series([1., 2., np.nan])
>>> ser
0    1.0
1    2.0
2    NaN
dtype: float64

```


Drop NA values from a Series.

```
>>> ser.dropna()
0    1.0
1    2.0
dtype: float64

```


Keep the Series with valid entries in the same variable.

```
>>> ser.dropna(inplace=True)
>>> ser
0    1.0
1    2.0
dtype: float64

```


# pyspark.pandas.Series.fillna — PySpark 4.0.1 documentation
Series.fillna(_value\=None_, _method\=None_, _axis\=None_, _inplace\=False_, _limit\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.fillna)
[#](#pyspark.pandas.Series.fillna "Permalink to this definition")

Fill NA/NaN values.

Note

the current implementation of ‘method’ parameter in fillna uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**value**scalar, dict, Series

Value to use to fill holes. alternately a dict/Series of values specifying which value to use for each column. DataFrame is not supported.

**method**{‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}, default None

Method to use for filling holes in reindexed Series pad / ffill: propagate last valid observation forward to next valid backfill / bfill: use NEXT valid observation to fill gap

Deprecated since version 4.0.0.

**axis**{0 or index}

1 and columns are not supported.

**inplace**boolean, default False

Fill in place (do not create a new object)

**limit**int, default None

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Deprecated since version 4.0.0.

Returns

Series

Series with NA entries filled.

Examples

```
>>> s = ps.Series([np.nan, 2, 3, 4, np.nan, 6], name='x')
>>> s
0    NaN
1    2.0
2    3.0
3    4.0
4    NaN
5    6.0
Name: x, dtype: float64

```


Replace all NaN elements with 0s.

```
>>> s.fillna(0)
0    0.0
1    2.0
2    3.0
3    4.0
4    0.0
5    6.0
Name: x, dtype: float64

```


We can also propagate non-null values forward or backward.

```
>>> s.fillna(method='ffill')
0    NaN
1    2.0
2    3.0
3    4.0
4    4.0
5    6.0
Name: x, dtype: float64

```


```
>>> s = ps.Series([np.nan, 'a', 'b', 'c', np.nan], name='x')
>>> s.fillna(method='ffill')
0    None
1       a
2       b
3       c
4       c
Name: x, dtype: object

```

# pyspark.pandas.Series.interpolate — PySpark 4.0.1 documentation
Series.interpolate(_method\='linear'_, _limit\=None_, _limit\_direction\=None_, _limit\_area\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.interpolate)
[#](#pyspark.pandas.Series.interpolate "Permalink to this definition")

Fill NaN values using an interpolation method.

Note

the current implementation of interpolate uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

New in version 3.4.0.

Parameters

**method: str, default ‘linear’**

Interpolation technique to use. One of:

*   ‘linear’: Ignore the index and treat the values as equally spaced.
    

**limit: int, optional**

Maximum number of consecutive NaNs to fill. Must be greater than 0.

**limit\_direction: str, default None**

Consecutive NaNs will be filled in this direction. One of {{‘forward’, ‘backward’, ‘both’}}.

**limit\_area: str, default None**

If limit is specified, consecutive NaNs will be filled with this restriction. One of:

*   None: No fill restriction.
    
*   ‘inside’: Only fill NaNs surrounded by valid values (interpolate).
    
*   ‘outside’: Only fill NaNs outside valid values (extrapolate).
    

Returns

Series or DataFrame or None

Returns the same object type as the caller, interpolated at some or all NA values.

See also

[`fillna`](about:blank/pyspark.pandas.Series.fillna.html#pyspark.pandas.Series.fillna "pyspark.pandas.Series.fillna")

Fill missing values using different methods.

Examples

Filling in NA via linear interpolation.

```
>>> s = ps.Series([0, 1, np.nan, 3])
>>> s
0    0.0
1    1.0
2    NaN
3    3.0
dtype: float64
>>> s.interpolate()
0    0.0
1    1.0
2    2.0
3    3.0
dtype: float64

```


Fill the DataFrame forward (that is, going down) along each column using linear interpolation.

Note how the last entry in column ‘a’ is interpolated differently, because there is no entry after it to use for interpolation. Note how the first entry in column ‘b’ remains NA, because there is no entry before it to use for interpolation.

```
>>> df = ps.DataFrame([(0.0, np.nan, -1.0, 1.0),
...                    (np.nan, 2.0, np.nan, np.nan),
...                    (2.0, 3.0, np.nan, 9.0),
...                    (np.nan, 4.0, -4.0, 16.0)],
...                   columns=list('abcd'))
>>> df
     a    b    c     d
0  0.0  NaN -1.0   1.0
1  NaN  2.0  NaN   NaN
2  2.0  3.0  NaN   9.0
3  NaN  4.0 -4.0  16.0
>>> df.interpolate(method='linear')
     a    b    c     d
0  0.0  NaN -1.0   1.0
1  1.0  2.0 -2.0   5.0
2  2.0  3.0 -3.0   9.0
3  2.0  4.0 -4.0  16.0

```



# pyspark.pandas.Series.argsort — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.argsort

Series.argsort()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.argsort)
[#](#pyspark.pandas.Series.argsort "Permalink to this definition")

Return the integer indices that would sort the Series values. Unlike pandas, the index order is not preserved in the result.

Returns

Series

Positions of values within the sort order with -1 indicating nan values.

Examples

```
>>> psser = ps.Series([3, 3, 4, 1, 6, 2, 3, 7, 8, 7, 10])
>>> psser
0      3
1      3
2      4
3      1
4      6
5      2
6      3
7      7
8      8
9      7
10    10
dtype: int64

```


```
>>> psser.argsort().sort_index()
0      3
1      5
2      0
3      1
4      6
5      2
6      4
7      7
8      9
9      8
10    10
dtype: int64

```


# pyspark.pandas.Series.argmin — PySpark 4.0.1 documentation
Series.argmin(_axis\=None_, _skipna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.argmin)
[#](#pyspark.pandas.Series.argmin "Permalink to this definition")

Return int position of the smallest value in the Series.

If the minimum is achieved in multiple locations, the first row position is returned.

Parameters

**axis**None

Dummy argument for consistency with Series.

**skipna**bool, default True

Exclude NA/null values.

Returns

int

Row position of the minimum value.

Examples

Consider dataset containing cereal calories

```
>>> s = ps.Series({'Corn Flakes': 100.0, 'Almond Delight': 110.0,
...                'Cinnamon Toast Crunch': 120.0, 'Cocoa Puff': 110.0})
>>> s  
Corn Flakes              100.0
Almond Delight           110.0
Cinnamon Toast Crunch    120.0
Cocoa Puff               110.0
dtype: float64

```

# pyspark.pandas.Series.argmax — PySpark 4.0.1 documentation
Series.argmax(_axis\=None_, _skipna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.argmax)
[#](#pyspark.pandas.Series.argmax "Permalink to this definition")

Return int position of the largest value in the Series.

If the maximum is achieved in multiple locations, the first row position is returned.

Parameters

**axis**None

Dummy argument for consistency with Series.

**skipna**bool, default True

Exclude NA/null values.

Returns

int

Row position of the maximum value.

Examples

Consider dataset containing cereal calories

```
>>> s = ps.Series({'Corn Flakes': 100.0, 'Almond Delight': 110.0, 'Unknown': np.nan,
...                'Cinnamon Toast Crunch': 120.0, 'Cocoa Puff': 110.0})
>>> s
Corn Flakes              100.0
Almond Delight           110.0
Unknown                    NaN
Cinnamon Toast Crunch    120.0
Cocoa Puff               110.0
dtype: float64

```


# pyspark.pandas.Series.sort_index — PySpark 4.0.1 documentation
Series.sort\_index(_axis\=0_, _level\=None_, _ascending\=True_, _inplace\=False_, _kind\=None_, _na\_position\='last'_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.sort_index)
[#](#pyspark.pandas.Series.sort_index "Permalink to this definition")

Sort object by labels (along an axis)

Parameters

**axis**index, columns to direct sorting. Currently, only axis = 0 is supported.

**level**int or level name or list of ints or list of level names

if not None, sort on values in specified index level(s)

**ascending**boolean, default True

Sort ascending vs. descending

**inplace**bool, default False

if True, perform operation in-place

**kind**str, default None

pandas-on-Spark does not allow specifying the sorting algorithm now, default None

**na\_position**{‘first’, ‘last’}, default ‘last’

first puts NaNs at the beginning, last puts NaNs at the end. Not implemented for MultiIndex.

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

New in version 3.4.0.

Returns

**sorted\_obj**Series

Examples

```
>>> s = ps.Series([2, 1, np.nan], index=['b', 'a', np.nan])

```


```
>>> s.sort_index()  
a       1.0
b       2.0
None    NaN
dtype: float64

```


```
>>> s.sort_index(ignore_index=True)
0    1.0
1    2.0
2    NaN
dtype: float64

```


```
>>> s.sort_index(ascending=False)  
b       2.0
a       1.0
None    NaN
dtype: float64

```


```
>>> s.sort_index(na_position='first')  
None    NaN
a       1.0
b       2.0
dtype: float64

```


```
>>> s.sort_index(inplace=True)
>>> s  
a       1.0
b       2.0
None    NaN
dtype: float64

```


Multi-index series.

```
>>> s = ps.Series(range(4), index=[['b', 'b', 'a', 'a'], [1, 0, 1, 0]], name='0')

```


```
>>> s.sort_index()
a  0    3
   1    2
b  0    1
   1    0
Name: 0, dtype: int64

```


```
>>> s.sort_index(level=1)  
a  0    3
b  0    1
a  1    2
b  1    0
Name: 0, dtype: int64

```


```
>>> s.sort_index(level=[1, 0])
a  0    3
b  0    1
a  1    2
b  1    0
Name: 0, dtype: int64

```


# pyspark.pandas.Series.sort_values — PySpark 4.0.1 documentation
Series.sort\_values(_ascending\=True_, _inplace\=False_, _na\_position\='last'_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.sort_values)
[#](#pyspark.pandas.Series.sort_values "Permalink to this definition")

Sort by the values.

Sort a Series in ascending or descending order by some criterion.

Parameters

**ascending**bool or list of bool, default True

Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the by.

**inplace**bool, default False

if True, perform operation in-place

**na\_position**{‘first’, ‘last’}, default ‘last’

first puts NaNs at the beginning, last puts NaNs at the end

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

New in version 3.4.0.

Returns

**sorted\_obj**Series ordered by values.

Examples

```
>>> s = ps.Series([np.nan, 1, 3, 10, 5])
>>> s
0     NaN
1     1.0
2     3.0
3    10.0
4     5.0
dtype: float64

```


Sort values ascending order (default behaviour)

```
>>> s.sort_values(ascending=True)
1     1.0
2     3.0
4     5.0
3    10.0
0     NaN
dtype: float64

```


Sort values descending order

```
>>> s.sort_values(ascending=False)
3    10.0
4     5.0
2     3.0
1     1.0
0     NaN
dtype: float64

```


Sort values descending order and ignoring index

```
>>> s.sort_values(ascending=False, ignore_index=True)
0    10.0
1     5.0
2     3.0
3     1.0
4     NaN
dtype: float64

```


Sort values inplace

```
>>> s.sort_values(ascending=False, inplace=True)
>>> s
3    10.0
4     5.0
2     3.0
1     1.0
0     NaN
dtype: float64

```


Sort values putting NAs first

```
>>> s.sort_values(na_position='first')
0     NaN
1     1.0
2     3.0
4     5.0
3    10.0
dtype: float64

```


Sort a series of strings

```
>>> s = ps.Series(['z', 'b', 'd', 'a', 'c'])
>>> s
0    z
1    b
2    d
3    a
4    c
dtype: object

```


```
>>> s.sort_values()
3    a
1    b
4    c
2    d
0    z
dtype: object

```

# pyspark.pandas.Series.unstack — PySpark 4.0.1 documentation
Series.unstack(_level\=\- 1_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.unstack)
[#](#pyspark.pandas.Series.unstack "Permalink to this definition")

Unstack, a.k.a. pivot, Series with MultiIndex to produce DataFrame. The level involved will automatically get sorted.

Parameters

**level**int, str, or list of these, default last level

Level(s) to unstack, can pass level name.

Returns

DataFrame

Unstacked Series.

Notes

Unlike pandas, pandas-on-Spark doesn’t check whether an index is duplicated or not because the checking of duplicated index requires scanning whole data which can be quite expensive.

Examples

```
>>> s = ps.Series([1, 2, 3, 4],
...               index=pd.MultiIndex.from_product([['one', 'two'],
...                                                 ['a', 'b']]))
>>> s
one  a    1
     b    2
two  a    3
     b    4
dtype: int64

```


```
>>> s.unstack(level=-1).sort_index()
     a  b
one  1  2
two  3  4

```


```
>>> s.unstack(level=0).sort_index()
   one  two
a    1    3
b    2    4

```


# pyspark.pandas.Series.explode — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.explode

Series.explode()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.explode)
[#](#pyspark.pandas.Series.explode "Permalink to this definition")

Transform each element of a list-like to a row.

Returns

Series

Exploded lists to rows; index will be duplicated for these rows.

Examples

```
>>> psser = ps.Series([[1, 2, 3], [], [3, 4]])
>>> psser
0    [1, 2, 3]
1           []
2       [3, 4]
dtype: object

```


```
>>> psser.explode()  
0    1.0
0    2.0
0    3.0
1    NaN
2    3.0
2    4.0
dtype: float64

```


# pyspark.pandas.Series.repeat — PySpark 4.0.1 documentation
Series.repeat(_repeats_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.repeat)
[#](#pyspark.pandas.Series.repeat "Permalink to this definition")

Repeat elements of a Series.

Returns a new Series where each element of the current Series is repeated consecutively a given number of times.

Parameters

**repeats**int or Series

The number of repetitions for each element. This should be a non-negative integer. Repeating 0 times will return an empty Series.

Returns

Series

Newly created Series with repeated elements.

Examples

```
>>> s = ps.Series(['a', 'b', 'c'])
>>> s
0    a
1    b
2    c
dtype: object
>>> s.repeat(2)
0    a
1    b
2    c
0    a
1    b
2    c
dtype: object
>>> ps.Series([1, 2, 3]).repeat(0)
Series([], dtype: int64)

```


# pyspark.pandas.Series.squeeze — PySpark 4.0.1 documentation
Series.squeeze(_axis\=None_)
[#](#pyspark.pandas.Series.squeeze "Permalink to this definition")

Squeeze 1 dimensional axis objects into scalars.

Series or DataFrames with a single element are squeezed to a scalar. DataFrames with a single column or a single row are squeezed to a Series. Otherwise the object is unchanged.

This method is most useful when you don’t know if your object is a Series or DataFrame, but you do know it has just a single column. In that case you can safely call squeeze to ensure you have a Series.

Parameters

**axis: {0 or ‘index’, 1 or ‘columns’, None}, default None**

A specific axis to squeeze. By default, all length-1 axes are squeezed.

Returns

DataFrame, Series, or scalar

The projection after squeezing axis or all the axes.

See also

[`Series.iloc`](about:blank/pyspark.pandas.Series.iloc.html#pyspark.pandas.Series.iloc "pyspark.pandas.Series.iloc")

Integer-location based indexing for selecting scalars.

[`DataFrame.iloc`](about:blank/pyspark.pandas.DataFrame.iloc.html#pyspark.pandas.DataFrame.iloc "pyspark.pandas.DataFrame.iloc")

Integer-location based indexing for selecting Series.

[`Series.to_frame`](about:blank/pyspark.pandas.Series.to_frame.html#pyspark.pandas.Series.to_frame "pyspark.pandas.Series.to_frame")

Inverse of DataFrame.squeeze for a single-column DataFrame.

Examples

```
>>> primes = ps.Series([2, 3, 5, 7])

```


Slicing might produce a Series with a single value:

```
>>> even_primes = primes[primes % 2 == 0]
>>> even_primes
0    2
dtype: int64

```


```
>>> int(even_primes.squeeze())
2

```


Squeezing objects with more than one value in every axis does nothing:

```
>>> odd_primes = primes[primes % 2 == 1]
>>> odd_primes
1    3
2    5
3    7
dtype: int64

```


```
>>> odd_primes.squeeze()
1    3
2    5
3    7
dtype: int64

```


Squeezing is even more effective when used with DataFrames.

```
>>> df = ps.DataFrame([[1, 2], [3, 4]], columns=['a', 'b'])
>>> df
   a  b
0  1  2
1  3  4

```


Slicing a single column will produce a DataFrame with the columns having only one value:

```
>>> df_a = df[['a']]
>>> df_a
   a
0  1
1  3

```


The columns can be squeezed down, resulting in a Series:

```
>>> df_a.squeeze('columns')
0    1
1    3
Name: a, dtype: int64

```


Slicing a single row from a single column will produce a single scalar DataFrame:

```
>>> df_1a = df.loc[[1], ['a']]
>>> df_1a
   a
1  3

```


Squeezing the rows produces a single scalar Series:

```
>>> df_1a.squeeze('rows')
a    3
Name: 1, dtype: int64

```


Squeezing all axes will project directly into a scalar:

```
>>> int(df_1a.squeeze())
3

```


# pyspark.pandas.Series.factorize — PySpark 4.0.1 documentation
Series.factorize(_sort\=True_, _use\_na\_sentinel\=True_)
[#](#pyspark.pandas.Series.factorize "Permalink to this definition")

Encode the object as an enumerated type or categorical variable.

This method is useful for obtaining a numeric representation of an array when all that matters is identifying distinct values.

Parameters

**sort**bool, default True

**use\_na\_sentinel**bool, default True

If True, the sentinel -1 will be used for NaN values, effectively assigning them a distinct category. If False, NaN values will be encoded as non-negative integers, treating them as unique categories in the encoding process and retaining them in the set of unique categories in the data.

Returns

**codes**Series or Index

A Series or Index that’s an indexer into uniques. `uniques.take(codes)` will have the same values as values.

**uniques**pd.Index

The unique valid values.

Note

Even if there’s a missing value in values, uniques will _not_ contain an entry for it.

Examples

```
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

```


```
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

```


For Index:

```
>>> psidx = ps.Index(['b', None, 'a', 'c', 'b'])
>>> codes, uniques = psidx.factorize()
>>> codes
Index([1, -1, 0, 2, 1], dtype='int32')
>>> uniques
Index(['a', 'b', 'c'], dtype='object')

```


# pyspark.pandas.Series.compare — PySpark 4.0.1 documentation
Series.compare(_other_, _keep\_shape\=False_, _keep\_equal\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.compare)
[#](#pyspark.pandas.Series.compare "Permalink to this definition")

Compare to another Series and show the differences.

Note

This API is slightly different from pandas when indexes from both Series are not identical and config ‘compute.eager\_check’ is False. pandas raise an exception; however, pandas-on-Spark just proceeds and performs by ignoring mismatches.

```
>>> psser1 = ps.Series([1, 2, 3, 4, 5], index=pd.Index([1, 2, 3, 4, 5]))
>>> psser2 = ps.Series([1, 2, 3, 4, 5], index=pd.Index([1, 2, 4, 3, 6]))
>>> psser1.compare(psser2)  
...
ValueError: Can only compare identically-labeled Series objects

```


```
>>> with ps.option_context("compute.eager_check", False):
...     psser1.compare(psser2)  
...
   self  other
3   3.0    4.0
4   4.0    3.0
5   5.0    NaN
6   NaN    5.0

```


Parameters

**other**Series

Object to compare with.

**keep\_shape**bool, default False

If true, all rows and columns are kept. Otherwise, only the ones with different values are kept.

**keep\_equal**bool, default False

If true, the result keeps values that are equal. Otherwise, equal values are shown as NaNs.

Returns

DataFrame

Notes

Matching NaNs will not appear as a difference.

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> s1 = ps.Series(["a", "b", "c", "d", "e"])
>>> s2 = ps.Series(["a", "a", "c", "b", "e"])

```


Align the differences on columns

```
>>> s1.compare(s2).sort_index()
  self other
1    b     a
3    d     b

```


Keep all original rows

```
>>> s1.compare(s2, keep_shape=True).sort_index()
   self other
0  None  None
1     b     a
2  None  None
3     d     b
4  None  None

```


Keep all original rows and all original values

```
>>> s1.compare(s2, keep_shape=True, keep_equal=True).sort_index()
  self other
0    a     a
1    b     a
2    c     c
3    d     b
4    e     e

```


```
>>> reset_option("compute.ops_on_diff_frames")

```



# pyspark.pandas.Series.replace — PySpark 4.0.1 documentation
Series.replace(_to\_replace\=None_, _value\=None_, _regex\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.replace)
[#](#pyspark.pandas.Series.replace "Permalink to this definition")

Replace values given in to\_replace with value. Values of the Series are replaced with other values dynamically.

Note

For partial pattern matching, the replacement is against the whole string, which is different from pandas. That’s by the nature of underlying Spark API.

Parameters

**to\_replace**str, list, tuple, dict, Series, int, float, or None

How to find the values that will be replaced. \* numeric, str:

> *   numeric: numeric values equal to to\_replace will be replaced with value
>     
> *   str: string exactly matching to\_replace will be replaced with value
>     

*   list of str or numeric:
    
    > *   if to\_replace and value are both lists or tuples, they must be the same length.
    >     
    > *   str and numeric rules apply as above.
    >     
    
*   dict:
    
    > *   Dicts can be used to specify different replacement values for different existing values. For example, {‘a’: ‘b’, ‘y’: ‘z’} replaces the value ‘a’ with ‘b’ and ‘y’ with ‘z’. To use a dict in this way the value parameter should be None.
    >     
    > *   For a DataFrame a dict can specify that different values should be replaced in different columns. For example, {‘a’: 1, ‘b’: ‘z’} looks for the value 1 in column ‘a’ and the value ‘z’ in column ‘b’ and replaces these values with whatever is specified in value. The value parameter should not be None in this case. You can treat this as a special case of passing two lists except that you are specifying the column to search in.
    >     
    

See the examples section for examples of each of these.

**value**scalar, dict, list, tuple, str default None

Value to replace any values matching to\_replace with. For a DataFrame a dict of values can be used to specify which value to use for each column (columns not in the dict will not be filled). Regular expressions, strings and lists or dicts of such objects are also allowed.

**regex: bool or str, default False**

Whether to interpret to\_replace and/or value as regular expressions. If this is True then to\_replace must be a string. Alternatively, this could be a regular expression in which case to\_replace must be None.

Returns

Series

Object after replacement.

Examples

Scalar to\_replace and value

```
>>> s = ps.Series([0, 1, 2, 3, 4])
>>> s
0    0
1    1
2    2
3    3
4    4
dtype: int64

```


```
>>> s.replace(0, 5)
0    5
1    1
2    2
3    3
4    4
dtype: int64

```


List-like to\_replace

```
>>> s.replace([0, 4], 5000)
0    5000
1       1
2       2
3       3
4    5000
dtype: int64

```


```
>>> s.replace([1, 2, 3], [10, 20, 30])
0     0
1    10
2    20
3    30
4     4
dtype: int64

```


Dict-like to\_replace

```
>>> s.replace({1: 1000, 2: 2000, 3: 3000, 4: 4000})
0       0
1    1000
2    2000
3    3000
4    4000
dtype: int64

```


Also support for MultiIndex

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> s = ps.Series([45, 200, 1.2, 30, 250, 1.5, 320, 1, 0.3],
...               index=midx)
>>> s
lama    speed      45.0
        weight    200.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.replace(45, 450)
lama    speed     450.0
        weight    200.0
        length      1.2
cow     speed      30.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.replace([45, 30, 320], 500)
lama    speed     500.0
        weight    200.0
        length      1.2
cow     speed     500.0
        weight    250.0
        length      1.5
falcon  speed     500.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.replace({45: 450, 30: 300})
lama    speed     450.0
        weight    200.0
        length      1.2
cow     speed     300.0
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


Regular expression to\_replace

```
>>> psser = ps.Series(['bat', 'foo', 'bait', 'abc', 'bar', 'zoo'])
>>> psser.replace(to_replace=r'^ba.

```
>>> psser.replace(value='new', regex=r'^.oo

For partial pattern matching, the replacement is against the whole string

```
>>> psser.replace('ba', 'xx', regex=True)
0     xx
1    foo
2     xx
3    abc
4     xx
5    zoo
dtype: object

```
, value='new', regex=True)
0     new
1     foo
2    bait
3     abc
4     new
5     zoo
dtype: object

```


urltomarkdowncodeblockplaceholder100.838409354543802

For partial pattern matching, the replacement is against the whole string

urltomarkdowncodeblockplaceholder110.9533654327671703)
0     bat
1     new
2    bait
3     abc
4     bar
5     new
dtype: object

```


For partial pattern matching, the replacement is against the whole string

urltomarkdowncodeblockplaceholder110.9533654327671703, value='new', regex=True)
0     new
1     foo
2    bait
3     abc
4     new
5     zoo
dtype: object

```


urltomarkdowncodeblockplaceholder100.838409354543802

For partial pattern matching, the replacement is against the whole string

urltomarkdowncodeblockplaceholder110.9533654327671703


# pyspark.pandas.Series.update — PySpark 4.0.1 documentation
Series.update(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.update)
[#](#pyspark.pandas.Series.update "Permalink to this definition")

Modify Series in place using non-NA values from passed Series. Aligns on index.

Parameters

**other**Series

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> s = ps.Series([1, 2, 3])
>>> s.update(ps.Series([4, 5, 6]))
>>> s.sort_index()
0    4
1    5
2    6
dtype: int64

```


```
>>> s = ps.Series(['a', 'b', 'c'])
>>> s.update(ps.Series(['d', 'e'], index=[0, 2]))
>>> s.sort_index()
0    d
1    b
2    e
dtype: object

```


```
>>> s = ps.Series([1, 2, 3])
>>> s.update(ps.Series([4, 5, 6, 7, 8]))
>>> s.sort_index()
0    4
1    5
2    6
dtype: int64

```


```
>>> s = ps.Series([1, 2, 3], index=[10, 11, 12])
>>> s
10    1
11    2
12    3
dtype: int64

```


```
>>> s.update(ps.Series([4, 5, 6]))
>>> s.sort_index()
10    1
11    2
12    3
dtype: int64

```


```
>>> s.update(ps.Series([4, 5, 6], index=[11, 12, 13]))
>>> s.sort_index()
10    1
11    4
12    5
dtype: int64

```


If `other` contains NaNs the corresponding values are not updated in the original Series.

```
>>> s = ps.Series([1, 2, 3])
>>> s.update(ps.Series([4, np.nan, 6]))
>>> s.sort_index()
0    4.0
1    2.0
2    6.0
dtype: float64

```


```
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.Series.asof — PySpark 4.0.1 documentation
Series.asof(_where_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.asof)
[#](#pyspark.pandas.Series.asof "Permalink to this definition")

Return the last row(s) without any NaNs before where.

The last row (for each element in where, if list) without any NaN is taken.

If there is no good value, NaN is returned.

Parameters

**where**index or array-like of indices

Returns

scalar or Series

The return can be:

*   scalar : when self is a Series and where is a scalar
    
*   Series: when self is a Series and where is an array-like
    

Return scalar or Series

Notes

Indices are assumed to be sorted. Raises if this is not the case and config ‘compute.eager\_check’ is True. If ‘compute.eager\_check’ is False pandas-on-Spark just proceeds and performs by ignoring the indeces’s order

Examples

```
>>> s = ps.Series([1, 2, np.nan, 4], index=[10, 20, 30, 40])
>>> s
10    1.0
20    2.0
30    NaN
40    4.0
dtype: float64

```


A scalar where.

```
>>> float(s.asof(20))
2.0

```


For a sequence where, a Series is returned. The first value is NaN, because the first element of where is before the first index value.

```
>>> s.asof([5, 20]).sort_index()
5     NaN
20    2.0
dtype: float64

```


Missing values are not considered. The following is `2.0`, not NaN, even though NaN is at the index location for `30`.

```
>>> float(s.asof(30))
2.0

```


```
>>> s = ps.Series([1, 2, np.nan, 4], index=[10, 30, 20, 40])
>>> with ps.option_context("compute.eager_check", False):
...     float(s.asof(20))
...
1.0

```


# pyspark.pandas.Series.resample — PySpark 4.0.1 documentation
Series.resample(_rule_, _closed\=None_, _label\=None_, _on\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.resample)
[#](#pyspark.pandas.Series.resample "Permalink to this definition")

Resample time-series data.

Convenience method for frequency conversion and resampling of time series. The object must have a datetime-like index (only support DatetimeIndex for now), or the caller must pass the label of a datetime-like series/index to the `on` keyword parameter.

New in version 3.4.0.

Parameters

**rule**str

The offset string or object representing target conversion. Currently, supported units are {‘YE’, ‘A’, ‘ME’, ‘D’, ‘h’, ‘min’, ‘MIN’, ‘s’}.

**closed**{{‘right’, ‘left’}}, default None

Which side of bin interval is closed. The default is ‘left’ for all frequency offsets except for ‘A’, ‘YE’ and ‘ME’ which all have a default of ‘right’.

**label**{{‘right’, ‘left’}}, default None

Which bin edge label to label bucket with. The default is ‘left’ for all frequency offsets except for ‘A’, ‘YE’ and ‘ME’ which all have a default of ‘right’.

**on**Series, optional

For a DataFrame, column to use instead of index for resampling. Column must be datetime-like.

Returns

SeriesResampler

Examples

Start by creating a series with 9 one minute timestamps.

```
>>> index = pd.date_range('1/1/2000', periods=9, freq='T')
>>> series = ps.Series(range(9), index=index, name='V')
>>> series
2000-01-01 00:00:00    0
2000-01-01 00:01:00    1
2000-01-01 00:02:00    2
2000-01-01 00:03:00    3
2000-01-01 00:04:00    4
2000-01-01 00:05:00    5
2000-01-01 00:06:00    6
2000-01-01 00:07:00    7
2000-01-01 00:08:00    8
Name: V, dtype: int64

```


Downsample the series into 3 minute bins and sum the values of the timestamps falling into a bin.

```
>>> series.resample('3T').sum().sort_index()
2000-01-01 00:00:00     3.0
2000-01-01 00:03:00    12.0
2000-01-01 00:06:00    21.0
Name: V, dtype: float64

```


Downsample the series into 3 minute bins as above, but label each bin using the right edge instead of the left. Please note that the value in the bucket used as the label is not included in the bucket, which it labels. For example, in the original series the bucket `2000-01-01 00:03:00` contains the value 3, but the summed value in the resampled bucket with the label `2000-01-01 00:03:00` does not include 3 (if it did, the summed value would be 6, not 3). To include this value, close the right side of the bin interval as illustrated in the example below this one.

```
>>> series.resample('3T', label='right').sum().sort_index()
2000-01-01 00:03:00     3.0
2000-01-01 00:06:00    12.0
2000-01-01 00:09:00    21.0
Name: V, dtype: float64

```


Downsample the series into 3 minute bins as above, but close the right side of the bin interval.

```
>>> series.resample('3T', label='right', closed='right').sum().sort_index()
2000-01-01 00:00:00     0.0
2000-01-01 00:03:00     6.0
2000-01-01 00:06:00    15.0
2000-01-01 00:09:00    15.0
Name: V, dtype: float64

```


Upsample the series into 30 second bins.

```
>>> series.resample('30S').sum().sort_index()
[0:5]   # Select first 5 rows
2000-01-01 00:00:00    0.0
2000-01-01 00:00:30    0.0
2000-01-01 00:01:00    1.0
2000-01-01 00:01:30    0.0
2000-01-01 00:02:00    2.0
Name: V, dtype: float64

```


# pyspark.pandas.Series.shift — PySpark 4.0.1 documentation
Series.shift(_periods\=1_, _fill\_value\=None_)
[#](#pyspark.pandas.Series.shift "Permalink to this definition")

Shift Series/Index by desired number of periods.

Note

the current implementation of shift uses Spark’s Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**periods**int

Number of periods to shift. Can be positive or negative.

**fill\_value**object, optional

The scalar value to use for newly introduced missing values. The default depends on the dtype of self. For numeric data, np.nan is used.

Returns

Copy of input Series/Index, shifted.

Examples

```
>>> df = ps.DataFrame({'Col1': [10, 20, 15, 30, 45],
...                    'Col2': [13, 23, 18, 33, 48],
...                    'Col3': [17, 27, 22, 37, 52]},
...                   columns=['Col1', 'Col2', 'Col3'])

```


```
>>> df.Col1.shift(periods=3)
0     NaN
1     NaN
2     NaN
3    10.0
4    20.0
Name: Col1, dtype: float64

```


```
>>> df.Col2.shift(periods=3, fill_value=0)
0     0
1     0
2     0
3    13
4    23
Name: Col2, dtype: int64

```


```
>>> df.index.shift(periods=3, fill_value=0)
Index([0, 0, 0, 0, 1], dtype='int64')

```


# pyspark.pandas.Series.first_valid_index — PySpark 4.0.1 documentation
Series.first\_valid\_index()
[#](#pyspark.pandas.Series.first_valid_index "Permalink to this definition")

Retrieves the index of the first valid value.

Returns

scalar, tuple, or None

Examples

Support for DataFrame

```
>>> psdf = ps.DataFrame({'a': [None, 2, 3, 2],
...                     'b': [None, 2.0, 3.0, 1.0],
...                     'c': [None, 200, 400, 200]},
...                     index=['Q', 'W', 'E', 'R'])
>>> psdf
     a    b      c
Q  NaN  NaN    NaN
W  2.0  2.0  200.0
E  3.0  3.0  400.0
R  2.0  1.0  200.0

```


```
>>> psdf.first_valid_index()
'W'

```


Support for MultiIndex columns

```
>>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
>>> psdf
     a    b      c
     x    y      z
Q  NaN  NaN    NaN
W  2.0  2.0  200.0
E  3.0  3.0  400.0
R  2.0  1.0  200.0

```


```
>>> psdf.first_valid_index()
'W'

```


Support for Series.

```
>>> s = ps.Series([None, None, 3, 4, 5], index=[100, 200, 300, 400, 500])
>>> s
100    NaN
200    NaN
300    3.0
400    4.0
500    5.0
dtype: float64

```


```
>>> int(s.first_valid_index())
300

```


Support for MultiIndex

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> s = ps.Series([None, None, None, None, 250, 1.5, 320, 1, 0.3], index=midx)
>>> s
lama    speed       NaN
        weight      NaN
        length      NaN
cow     speed       NaN
        weight    250.0
        length      1.5
falcon  speed     320.0
        weight      1.0
        length      0.3
dtype: float64

```


```
>>> s.first_valid_index()
('cow', 'weight')

```


# pyspark.pandas.Series.last_valid_index — PySpark 4.0.1 documentation
Series.last\_valid\_index()
[#](#pyspark.pandas.Series.last_valid_index "Permalink to this definition")

Return index for last non-NA/null value.

Returns

scalar, tuple, or None

Notes

This API only works with PySpark >= 3.0.

Examples

Support for DataFrame

```
>>> psdf = ps.DataFrame({'a': [1, 2, 3, None],
...                     'b': [1.0, 2.0, 3.0, None],
...                     'c': [100, 200, 400, None]},
...                     index=['Q', 'W', 'E', 'R'])
>>> psdf
     a    b      c
Q  1.0  1.0  100.0
W  2.0  2.0  200.0
E  3.0  3.0  400.0
R  NaN  NaN    NaN

```


```
>>> psdf.last_valid_index()  
'E'

```


Support for MultiIndex columns

```
>>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
>>> psdf
     a    b      c
     x    y      z
Q  1.0  1.0  100.0
W  2.0  2.0  200.0
E  3.0  3.0  400.0
R  NaN  NaN    NaN

```


```
>>> psdf.last_valid_index()  
'E'

```


Support for Series.

```
>>> s = ps.Series([1, 2, 3, None, None], index=[100, 200, 300, 400, 500])
>>> s
100    1.0
200    2.0
300    3.0
400    NaN
500    NaN
dtype: float64

```


```
>>> s.last_valid_index()  
300

```


Support for MultiIndex

```
>>> midx = pd.MultiIndex([['lama', 'cow', 'falcon'],
...                       ['speed', 'weight', 'length']],
...                      [[0, 0, 0, 1, 1, 1, 2, 2, 2],
...                       [0, 1, 2, 0, 1, 2, 0, 1, 2]])
>>> s = ps.Series([250, 1.5, 320, 1, 0.3, None, None, None, None], index=midx)
>>> s
lama    speed     250.0
        weight      1.5
        length    320.0
cow     speed       1.0
        weight      0.3
        length      NaN
falcon  speed       NaN
        weight      NaN
        length      NaN
dtype: float64

```


```
>>> s.last_valid_index()  
('cow', 'weight')

```


# pyspark.pandas.Series.at_time — PySpark 4.0.1 documentation
Series.at\_time(_time_, _asof\=False_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.at_time)
[#](#pyspark.pandas.Series.at_time "Permalink to this definition")

Select values at particular time of day (example: 9:30AM).

Parameters

**time**datetime.time or str

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Returns

Series

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

Examples

```
>>> idx = pd.date_range('2018-04-09', periods=4, freq='12H')
>>> psser = ps.Series([1, 2, 3, 4], index=idx)
>>> psser
2018-04-09 00:00:00    1
2018-04-09 12:00:00    2
2018-04-10 00:00:00    3
2018-04-10 12:00:00    4
dtype: int64

```


```
>>> psser.at_time('12:00')
2018-04-09 12:00:00    2
2018-04-10 12:00:00    4
dtype: int64

```


# pyspark.pandas.Series.between_time — PySpark 4.0.1 documentation
Series.between\_time(_start\_time_, _end\_time_, _inclusive\='both'_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.between_time)
[#](#pyspark.pandas.Series.between_time "Permalink to this definition")

Select values between particular times of the day (example: 9:00-9:30 AM).

By setting `start_time` to be later than `end_time`, you can get the times that are _not_ between the two times.

Parameters

**start\_time**datetime.time or str

Initial time as a time filter limit.

**end\_time**datetime.time or str

End time as a time filter limit.

**inclusive**{“both”, “neither”, “left”, “right”}, default “both”

Include boundaries; whether to set each bound as closed or open.

New in version 4.0.0.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Determine range time on index or columns value.

Returns

Series

Data from the original object filtered to the specified dates range.

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

See also

[`at_time`](about:blank/pyspark.pandas.Series.at_time.html#pyspark.pandas.Series.at_time "pyspark.pandas.Series.at_time")

Select values at a particular time of the day.

[`last`](about:blank/pyspark.pandas.Series.last.html#pyspark.pandas.Series.last "pyspark.pandas.Series.last")

Select final periods of time series based on a date offset.

[`DatetimeIndex.indexer_between_time`](about:blank/pyspark.pandas.DatetimeIndex.indexer_between_time.html#pyspark.pandas.DatetimeIndex.indexer_between_time "pyspark.pandas.DatetimeIndex.indexer_between_time")

Get just the index locations for values between particular times of the day.

Examples

```
>>> idx = pd.date_range('2018-04-09', periods=4, freq='1D20min')
>>> psser = ps.Series([1, 2, 3, 4], index=idx)
>>> psser
2018-04-09 00:00:00    1
2018-04-10 00:20:00    2
2018-04-11 00:40:00    3
2018-04-12 01:00:00    4
dtype: int64

```


```
>>> psser.between_time('0:15', '0:45')  
2018-04-10 00:20:00    2
2018-04-11 00:40:00    3
dtype: int64

```


# pyspark.pandas.Series.spark.column — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.spark.column

spark.column[#](#pyspark.pandas.Series.spark.column "Permalink to this definition")

Spark Column object representing the Series/Index.

Note

This Spark Column object is strictly stick to its base DataFrame the Series/Index was derived from.


# pyspark.pandas.Series.spark.transform — PySpark 4.0.1 documentation
spark.transform(_func_)
[#](#pyspark.pandas.Series.spark.transform "Permalink to this definition")

Applies a function that takes and returns a Spark column. It allows natively applying a Spark function and column APIs with the Spark column internally used in Series or Index. The output length of the Spark column should be the same as input’s.

Note

It requires to have the same input and output length; therefore, the aggregate Spark functions such as count does not work.

Parameters

**func**function

Function to use for transforming the data by using Spark columns.

Returns

Series or Index

Raises

**ValueError**If the output from the function is not a Spark column.

Examples

```
>>> from pyspark.sql.functions import log
>>> df = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, columns=["a", "b"])
>>> df
   a  b
0  1  4
1  2  5
2  3  6

```


```
>>> df.a.spark.transform(lambda c: log(c))
0    0.000000
1    0.693147
2    1.098612
Name: a, dtype: float64

```


```
>>> df.index.spark.transform(lambda c: c + 10)
Index([10, 11, 12], dtype='int64')

```


```
>>> df.a.spark.transform(lambda c: c + df.b.spark.column)
0    5
1    7
2    9
Name: a, dtype: int64

```


# pyspark.pandas.Series.spark.apply — PySpark 4.0.1 documentation
spark.apply(_func_)
[#](#pyspark.pandas.Series.spark.apply "Permalink to this definition")

Applies a function that takes and returns a Spark column. It allows to natively apply a Spark function and column APIs with the Spark column internally used in Series or Index.

Note

It forces to lose the index and end up using the default index. It is preferred to use `Series.spark.transform()` or :meth:\`DataFrame.spark.apply with specifying the index\_col.

Note

It does not require to have the same length of the input and output. However, it requires to create a new DataFrame internally which will require to set compute.ops\_on\_diff\_frames to compute even with the same origin DataFrame is expensive, whereas `Series.spark.transform()` does not require it.

Parameters

**func**function

Function to apply the function against the data by using Spark columns.

Returns

Series

Raises

**ValueError**If the output from the function is not a Spark column.

Examples

```
>>> from pyspark import pandas as ps
>>> from pyspark.sql.functions import count, lit
>>> df = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, columns=["a", "b"])
>>> df
   a  b
0  1  4
1  2  5
2  3  6

```


```
>>> df.a.spark.apply(lambda c: count(c))
0    3
Name: a, dtype: int64

```


```
>>> df.a.spark.apply(lambda c: c + df.b.spark.column)
0    5
1    7
2    9
Name: a, dtype: int64

```


# pyspark.pandas.Series.dt.date — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.date

dt.date[#](#pyspark.pandas.Series.dt.date "Permalink to this definition")

Returns a Series of python datetime.date objects (namely, the date part of Timestamps without timezone information).


# pyspark.pandas.Series.dt.year — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.year

dt.year[#](#pyspark.pandas.Series.dt.year "Permalink to this definition")

The year of the datetime.


# pyspark.pandas.Series.dt.month — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.month

dt.month[#](#pyspark.pandas.Series.dt.month "Permalink to this definition")

The month of the timestamp as January = 1 December = 12.



# pyspark.pandas.Series.dt.day — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.day

dt.day[#](#pyspark.pandas.Series.dt.day "Permalink to this definition")

The days of the datetime.


# pyspark.pandas.Series.dt.hour — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.hour

dt.hour[#](#pyspark.pandas.Series.dt.hour "Permalink to this definition")

The hours of the datetime.


# pyspark.pandas.Series.dt.minute — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.minute

dt.minute[#](#pyspark.pandas.Series.dt.minute "Permalink to this definition")

The minutes of the datetime.

# pyspark.pandas.Series.dt.second — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.second

dt.second[#](#pyspark.pandas.Series.dt.second "Permalink to this definition")

The seconds of the datetime.


# pyspark.pandas.Series.dt.microsecond — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.microsecond

dt.microsecond[#](#pyspark.pandas.Series.dt.microsecond "Permalink to this definition")

The microseconds of the datetime.

# pyspark.pandas.Series.dt.isocalendar — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.isocalendar

dt.isocalendar _\= <function DatetimeMethods.isocalendar>_[#](#pyspark.pandas.Series.dt.isocalendar "Permalink to this definition")


# pyspark.pandas.Series.dt.dayofweek — PySpark 4.0.1 documentation
dt.dayofweek[#](#pyspark.pandas.Series.dt.dayofweek "Permalink to this definition")

The day of the week with Monday=0, Sunday=6.

Return the day of the week. It is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6. This method is available on both Series with datetime values (using the dt accessor).

Returns

Series

Containing integers indicating the day number.

See also

`Series.dt.dayofweek`

Alias.

`Series.dt.weekday`

Alias.

`Series.dt.day_name`

Returns the name of the day of the week.

Examples

```
>>> s = ps.from_pandas(pd.date_range('2016-12-31', '2017-01-08', freq='D').to_series())
>>> s.dt.dayofweek
2016-12-31    5
2017-01-01    6
2017-01-02    0
2017-01-03    1
2017-01-04    2
2017-01-05    3
2017-01-06    4
2017-01-07    5
2017-01-08    6
dtype: int32

```


# pyspark.pandas.Series.dt.weekday — PySpark 4.0.1 documentation
dt.weekday[#](#pyspark.pandas.Series.dt.weekday "Permalink to this definition")

The day of the week with Monday=0, Sunday=6.

Return the day of the week. It is assumed the week starts on Monday, which is denoted by 0 and ends on Sunday which is denoted by 6. This method is available on both Series with datetime values (using the dt accessor).

Returns

Series

Containing integers indicating the day number.

See also

`Series.dt.dayofweek`

Alias.

`Series.dt.weekday`

Alias.

`Series.dt.day_name`

Returns the name of the day of the week.

Examples

```
>>> s = ps.from_pandas(pd.date_range('2016-12-31', '2017-01-08', freq='D').to_series())
>>> s.dt.dayofweek
2016-12-31    5
2017-01-01    6
2017-01-02    0
2017-01-03    1
2017-01-04    2
2017-01-05    3
2017-01-06    4
2017-01-07    5
2017-01-08    6
dtype: int32

```


# pyspark.pandas.Series.dt.dayofyear — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.dayofyear

dt.dayofyear[#](#pyspark.pandas.Series.dt.dayofyear "Permalink to this definition")

The ordinal day of the year.

# pyspark.pandas.Series.dt.quarter — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.quarter

dt.quarter[#](#pyspark.pandas.Series.dt.quarter "Permalink to this definition")

The quarter of the date.

# pyspark.pandas.Series.dt.is_month_start — PySpark 4.0.1 documentation
dt.is\_month\_start[#](#pyspark.pandas.Series.dt.is_month_start "Permalink to this definition")

Indicates whether the date is the first day of the month.

Returns

Series

For Series, returns a Series with boolean values.

See also

[`is_month_end`](about:blank/pyspark.pandas.Series.dt.is_month_end.html#pyspark.pandas.Series.dt.is_month_end "pyspark.pandas.Series.dt.is_month_end")

Return a boolean indicating whether the date is the last day of the month.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> s = ps.Series(pd.date_range("2018-02-27", periods=3))
>>> s
0   2018-02-27
1   2018-02-28
2   2018-03-01
dtype: datetime64[ns]

```


```
>>> s.dt.is_month_start
0    False
1    False
2     True
dtype: bool

```


# pyspark.pandas.Series.dt.is_month_end — PySpark 4.0.1 documentation
dt.is\_month\_end[#](#pyspark.pandas.Series.dt.is_month_end "Permalink to this definition")

Indicates whether the date is the last day of the month.

Returns

Series

For Series, returns a Series with boolean values.

See also

[`is_month_start`](about:blank/pyspark.pandas.Series.dt.is_month_start.html#pyspark.pandas.Series.dt.is_month_start "pyspark.pandas.Series.dt.is_month_start")

Return a boolean indicating whether the date is the first day of the month.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> s = ps.Series(pd.date_range("2018-02-27", periods=3))
>>> s
0   2018-02-27
1   2018-02-28
2   2018-03-01
dtype: datetime64[ns]

```


```
>>> s.dt.is_month_end
0    False
1     True
2    False
dtype: bool

```


# pyspark.pandas.Series.dt.is_quarter_start — PySpark 4.0.1 documentation
dt.is\_quarter\_start[#](#pyspark.pandas.Series.dt.is_quarter_start "Permalink to this definition")

Indicator for whether the date is the first day of a quarter.

Returns

**is\_quarter\_start**Series

The same type as the original data with boolean values. Series will have the same name and index.

See also

[`quarter`](about:blank/pyspark.pandas.Series.dt.quarter.html#pyspark.pandas.Series.dt.quarter "pyspark.pandas.Series.dt.quarter")

Return the quarter of the date.

[`is_quarter_end`](about:blank/pyspark.pandas.Series.dt.is_quarter_end.html#pyspark.pandas.Series.dt.is_quarter_end "pyspark.pandas.Series.dt.is_quarter_end")

Similar property for indicating the quarter start.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> df = ps.DataFrame({'dates': pd.date_range("2017-03-30",
...                   periods=4)})
>>> df
       dates
0 2017-03-30
1 2017-03-31
2 2017-04-01
3 2017-04-02

```


```
>>> df.dates.dt.quarter
0    1
1    1
2    2
3    2
Name: dates, dtype: int32

```


```
>>> df.dates.dt.is_quarter_start
0    False
1    False
2     True
3    False
Name: dates, dtype: bool

```


# pyspark.pandas.Series.dt.is_quarter_end — PySpark 4.0.1 documentation
dt.is\_quarter\_end[#](#pyspark.pandas.Series.dt.is_quarter_end "Permalink to this definition")

Indicator for whether the date is the last day of a quarter.

Returns

**is\_quarter\_end**Series

The same type as the original data with boolean values. Series will have the same name and index.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> df = ps.DataFrame({'dates': pd.date_range("2017-03-30",
...                   periods=4)})
>>> df
       dates
0 2017-03-30
1 2017-03-31
2 2017-04-01
3 2017-04-02

```


```
>>> df.dates.dt.quarter
0    1
1    1
2    2
3    2
Name: dates, dtype: int32

```


```
>>> df.dates.dt.is_quarter_start
0    False
1    False
2     True
3    False
Name: dates, dtype: bool

```


# pyspark.pandas.Series.dt.is_year_start — PySpark 4.0.1 documentation
dt.is\_year\_start[#](#pyspark.pandas.Series.dt.is_year_start "Permalink to this definition")

Indicate whether the date is the first day of a year.

Returns

Series

The same type as the original data with boolean values. Series will have the same name and index.

See also

[`is_year_end`](about:blank/pyspark.pandas.Series.dt.is_year_end.html#pyspark.pandas.Series.dt.is_year_end "pyspark.pandas.Series.dt.is_year_end")

Similar property indicating the last day of the year.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> dates = ps.Series(pd.date_range("2017-12-30", periods=3))
>>> dates
0   2017-12-30
1   2017-12-31
2   2018-01-01
dtype: datetime64[ns]

```


```
>>> dates.dt.is_year_start
0    False
1    False
2     True
dtype: bool

```


# pyspark.pandas.Series.dt.is_year_end — PySpark 4.0.1 documentation
dt.is\_year\_end[#](#pyspark.pandas.Series.dt.is_year_end "Permalink to this definition")

Indicate whether the date is the last day of the year.

Returns

Series

The same type as the original data with boolean values. Series will have the same name and index.

See also

[`is_year_start`](about:blank/pyspark.pandas.Series.dt.is_year_start.html#pyspark.pandas.Series.dt.is_year_start "pyspark.pandas.Series.dt.is_year_start")

Similar property indicating the start of the year.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> dates = ps.Series(pd.date_range("2017-12-30", periods=3))
>>> dates
0   2017-12-30
1   2017-12-31
2   2018-01-01
dtype: datetime64[ns]

```


```
>>> dates.dt.is_year_end
0    False
1     True
2    False
dtype: bool

```


# pyspark.pandas.Series.dt.is_leap_year — PySpark 4.0.1 documentation
dt.is\_leap\_year[#](#pyspark.pandas.Series.dt.is_leap_year "Permalink to this definition")

Boolean indicator if the date belongs to a leap year.

A leap year is a year, which has 366 days (instead of 365) including 29th of February as an intercalary day. Leap years are years which are multiples of four with the exception of years divisible by 100 but not by 400.

Returns

Series

Booleans indicating if dates belong to a leap year.

Examples

This method is available on Series with datetime values under the `.dt` accessor.

```
>>> dates_series = ps.Series(pd.date_range("2012-01-01", "2015-01-01", freq="Y"))
>>> dates_series
0   2012-12-31
1   2013-12-31
2   2014-12-31
dtype: datetime64[ns]

```


```
>>> dates_series.dt.is_leap_year
0     True
1    False
2    False
dtype: bool

```



# pyspark.pandas.Series.dt.daysinmonth — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.daysinmonth

dt.daysinmonth[#](#pyspark.pandas.Series.dt.daysinmonth "Permalink to this definition")

The number of days in the month.


# pyspark.pandas.Series.dt.days_in_month — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.days\_in\_month

dt.days\_in\_month[#](#pyspark.pandas.Series.dt.days_in_month "Permalink to this definition")

The number of days in the month.


# pyspark.pandas.Series.dt.normalize — PySpark 4.0.1 documentation
dt.normalize()
[#](#pyspark.pandas.Series.dt.normalize "Permalink to this definition")

Convert times to midnight.

The time component of the date-time is converted to midnight i.e. 00:00:00. This is useful in cases, when the time does not matter. Length is unaltered. The time zones are unaffected.

This method is available on Series with datetime values under the `.dt` accessor, and directly on Datetime Array.

Returns

Series

The same type as the original data. Series will have the same name and index.

See also

[`floor`](about:blank/pyspark.pandas.Series.dt.floor.html#pyspark.pandas.Series.dt.floor "pyspark.pandas.Series.dt.floor")

Floor the series to the specified freq.

[`ceil`](about:blank/pyspark.pandas.Series.dt.ceil.html#pyspark.pandas.Series.dt.ceil "pyspark.pandas.Series.dt.ceil")

Ceil the series to the specified freq.

[`round`](about:blank/pyspark.pandas.Series.round.html#pyspark.pandas.Series.round "pyspark.pandas.Series.round")

Round the series to the specified freq.

Examples

```
>>> series = ps.Series(pd.Series(pd.date_range('2012-1-1 12:45:31', periods=3, freq='ME')))
>>> series.dt.normalize()
0   2012-01-31
1   2012-02-29
2   2012-03-31
dtype: datetime64[ns]

```


# pyspark.pandas.Series.dt.strftime — PySpark 4.0.1 documentation
dt.strftime(_date\_format_)
[#](#pyspark.pandas.Series.dt.strftime "Permalink to this definition")

Convert to a string Series using specified date\_format.

Return an series of formatted strings specified by date\_format, which supports the same string format as the python standard library. Details of the string format can be found in the python string format doc.

Parameters

**date\_format**str

Date format string (example: “%%Y-%%m-%%d”).

Returns

Series

Series of formatted strings.

See also

`to_datetime`

Convert the given argument to datetime.

[`normalize`](about:blank/pyspark.pandas.Series.dt.normalize.html#pyspark.pandas.Series.dt.normalize "pyspark.pandas.Series.dt.normalize")

Return series with times to midnight.

[`round`](about:blank/pyspark.pandas.Series.round.html#pyspark.pandas.Series.round "pyspark.pandas.Series.round")

Round the series to the specified freq.

[`floor`](about:blank/pyspark.pandas.Series.dt.floor.html#pyspark.pandas.Series.dt.floor "pyspark.pandas.Series.dt.floor")

Floor the series to the specified freq.

Examples

```
>>> series = ps.Series(pd.date_range(pd.Timestamp("2018-03-10 09:00"),
...                                  periods=3, freq='s'))
>>> series
0   2018-03-10 09:00:00
1   2018-03-10 09:00:01
2   2018-03-10 09:00:02
dtype: datetime64[ns]

```


```
>>> series.dt.strftime('%B %d, %Y, %r')
0    March 10, 2018, 09:00:00 AM
1    March 10, 2018, 09:00:01 AM
2    March 10, 2018, 09:00:02 AM
dtype: object

```


# pyspark.pandas.Series.dt.round — PySpark 4.0.1 documentation
dt.round(_freq_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.dt.round "Permalink to this definition")

Perform round operation on the data to the specified freq.

Parameters

**freq**str or Offset

The frequency level to round the index to. Must be a fixed frequency like ‘S’ (second) not ‘ME’ (month end).

**nonexistent**‘shift\_forward’, ‘shift\_backward, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise an NonExistentTimeError if there are nonexistent times
    

Note

this option only works with pandas 0.24.0+

Returns

Series

a Series with the same index for a Series.

Raises

ValueError if the freq cannot be converted.

Examples

```
>>> series = ps.Series(pd.date_range('1/1/2018 11:59:00', periods=3, freq='min'))
>>> series
0   2018-01-01 11:59:00
1   2018-01-01 12:00:00
2   2018-01-01 12:01:00
dtype: datetime64[ns]

```


```
>>> series.dt.round("H")
0   2018-01-01 12:00:00
1   2018-01-01 12:00:00
2   2018-01-01 12:00:00
dtype: datetime64[ns]

```

# pyspark.pandas.Series.dt.floor — PySpark 4.0.1 documentation
dt.floor(_freq_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.dt.floor "Permalink to this definition")

Perform floor operation on the data to the specified freq.

Parameters

**freq**str or Offset

The frequency level to floor the index to. Must be a fixed frequency like ‘S’ (second) not ‘ME’ (month end).

**nonexistent**‘shift\_forward’, ‘shift\_backward, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise an NonExistentTimeError if there are nonexistent times
    

Note

this option only works with pandas 0.24.0+

Returns

Series

a Series with the same index for a Series.

Raises

ValueError if the freq cannot be converted.

Examples

```
>>> series = ps.Series(pd.date_range('1/1/2018 11:59:00', periods=3, freq='min'))
>>> series
0   2018-01-01 11:59:00
1   2018-01-01 12:00:00
2   2018-01-01 12:01:00
dtype: datetime64[ns]

```


```
>>> series.dt.floor("H")
0   2018-01-01 11:00:00
1   2018-01-01 12:00:00
2   2018-01-01 12:00:00
dtype: datetime64[ns]

```


# pyspark.pandas.Series.dt.ceil — PySpark 4.0.1 documentation
dt.ceil(_freq_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.dt.ceil "Permalink to this definition")

Perform ceil operation on the data to the specified freq.

Parameters

**freq**str or Offset

The frequency level to round the index to. Must be a fixed frequency like ‘S’ (second) not ‘ME’ (month end).

**nonexistent**‘shift\_forward’, ‘shift\_backward, ‘NaT’, timedelta, default ‘raise’

A nonexistent time does not exist in a particular timezone where clocks moved forward due to DST.

*   ‘shift\_forward’ will shift the nonexistent time forward to the closest existing time
    
*   ‘shift\_backward’ will shift the nonexistent time backward to the closest existing time
    
*   ‘NaT’ will return NaT where there are nonexistent times
    
*   timedelta objects will shift nonexistent times by the timedelta
    
*   ‘raise’ will raise an NonExistentTimeError if there are nonexistent times
    

Note

this option only works with pandas 0.24.0+

Returns

Series

a Series with the same index for a Series.

Raises

ValueError if the freq cannot be converted.

Examples

```
>>> series = ps.Series(pd.date_range('1/1/2018 11:59:00', periods=3, freq='min'))
>>> series
0   2018-01-01 11:59:00
1   2018-01-01 12:00:00
2   2018-01-01 12:01:00
dtype: datetime64[ns]

```


```
>>> series.dt.ceil("H")
0   2018-01-01 12:00:00
1   2018-01-01 12:00:00
2   2018-01-01 13:00:00
dtype: datetime64[ns]

```


# pyspark.pandas.Series.dt.month_name — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.month\_name

dt.month\_name(_locale\=None_)
[#](#pyspark.pandas.Series.dt.month_name "Permalink to this definition")

Return the month names of the series with specified locale.

Parameters

**locale**str, optional

Locale determining the language in which to return the month name. Default is English locale.

Returns

Series

Series of month names.

Examples

```
>>> series = ps.Series(pd.date_range(start='2018-01', freq='ME', periods=3))
>>> series
0   2018-01-31
1   2018-02-28
2   2018-03-31
dtype: datetime64[ns]

```


```
>>> series.dt.month_name()
0     January
1    February
2       March
dtype: object

```


# pyspark.pandas.Series.dt.day_name — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.dt.day\_name

dt.day\_name(_locale\=None_)
[#](#pyspark.pandas.Series.dt.day_name "Permalink to this definition")

Return the day names of the series with specified locale.

Parameters

**locale**str, optional

Locale determining the language in which to return the day name. Default is English locale.

Returns

Series

Series of day names.

Examples

```
>>> series = ps.Series(pd.date_range(start='2018-01-01', freq='D', periods=3))
>>> series
0   2018-01-01
1   2018-01-02
2   2018-01-03
dtype: datetime64[ns]

```


```
>>> series.dt.day_name()
0       Monday
1      Tuesday
2    Wednesday
dtype: object

```

# pyspark.pandas.Series.str.capitalize — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.capitalize

str.capitalize()
[#](#pyspark.pandas.Series.str.capitalize "Permalink to this definition")

Convert Strings in the series to be capitalized.

Examples

```
>>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object

```


```
>>> s.str.capitalize()
0                 Lower
1              Capitals
2    This is a sentence
3              Swapcase
dtype: object

```


# pyspark.pandas.Series.str.cat — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.cat

str.cat(_others\=None_, _sep\=None_, _na\_rep\=None_, _join\=None_)
[#](#pyspark.pandas.Series.str.cat "Permalink to this definition")

Not supported.



# pyspark.pandas.Series.str.center — PySpark 4.0.1 documentation
str.center(_width_, _fillchar\=' '_)
[#](#pyspark.pandas.Series.str.center "Permalink to this definition")

Filling left and right side of strings in the Series/Index with an additional character. Equivalent to [`str.center()`](#pyspark.pandas.Series.str.center "pyspark.pandas.Series.str.center").

Parameters

**width**int

Minimum width of resulting string; additional characters will be filled with fillchar.

**fillchar**str

Additional character for filling, default is whitespace.

Returns

Series of objects

Examples

```
>>> s = ps.Series(["caribou", "tiger"])
>>> s
0    caribou
1      tiger
dtype: object

```


```
>>> s.str.center(width=10, fillchar='-')
0    -caribou--
1    --tiger---
dtype: object

```



# pyspark.pandas.Series.str.contains — PySpark 4.0.1 documentation
str.contains(_pat_, _case\=True_, _flags\=0_, _na\=None_, _regex\=True_)
[#](#pyspark.pandas.Series.str.contains "Permalink to this definition")

Test if pattern or regex is contained within a string of a Series.

Return boolean Series based on whether a given pattern or regex is contained within a string of a Series.

Analogous to [`match()`](about:blank/pyspark.pandas.Series.str.match.html#pyspark.pandas.Series.str.match "pyspark.pandas.Series.str.match"), but less strict, relying on `re.search()` instead of `re.match()`.

Parameters

**pat**str

Character sequence or regular expression.

**case**bool, default True

If True, case sensitive.

**flags**int, default 0 (no flags)

Flags to pass through to the re module, e.g. re.IGNORECASE.

**na**default None

Fill value for missing values. NaN converted to None.

**regex**bool, default True

If True, assumes the pat is a regular expression. If False, treats the pat as a literal string.

Returns

Series of boolean values or object

A Series of boolean values indicating whether the given pattern is contained within the string of each element of the Series.

Examples

Returning a Series of booleans using only a literal pattern.

```
>>> s1 = ps.Series(['Mouse', 'dog', 'house and parrot', '23', np.nan])
>>> s1.str.contains('og', regex=False)
0    False
1     True
2    False
3    False
4     None
dtype: object

```


Specifying case sensitivity using case.

```
>>> s1.str.contains('oG', case=True, regex=True)
0    False
1    False
2    False
3    False
4     None
dtype: object

```


Specifying na to be False instead of NaN replaces NaN values with False. If Series does not contain NaN values the resultant dtype will be bool, otherwise, an object dtype.

```
>>> s1.str.contains('og', na=False, regex=True)
0    False
1     True
2    False
3    False
4    False
dtype: bool

```


Returning ‘house’ or ‘dog’ when either expression occurs in a string.

```
>>> s1.str.contains('house|dog', regex=True)
0    False
1     True
2     True
3    False
4     None
dtype: object

```


Ignoring case sensitivity using flags with regex.

```
>>> import re
>>> s1.str.contains('PARROT', flags=re.IGNORECASE, regex=True)
0    False
1    False
2     True
3    False
4     None
dtype: object

```


Returning any digit using regular expression.

```
>>> s1.str.contains('[0-9]', regex=True)
0    False
1    False
2    False
3     True
4     None
dtype: object

```


Ensure pat is a not a literal pattern when regex is set to True. Note in the following example one might expect only s2\[1\] and s2\[3\] to return True. However, ‘.0’ as a regex matches any character followed by a 0.

```
>>> s2 = ps.Series(['40','40.0','41','41.0','35'])
>>> s2.str.contains('.0', regex=True)
0     True
1     True
2    False
3     True
4    False
dtype: bool

```

# pyspark.pandas.Series.str.count — PySpark 4.0.1 documentation
str.count(_pat_, _flags\=0_)
[#](#pyspark.pandas.Series.str.count "Permalink to this definition")

Count occurrences of pattern in each string of the Series.

This function is used to count the number of times a particular regex pattern is repeated in each of the string elements of the Series.

Parameters

**pat**str

Valid regular expression.

**flags**int, default 0 (no flags)

Flags for the re module.

Returns

Series of int

A Series containing the integer counts of pattern matches.

Examples

```
>>> s = ps.Series(['A', 'B', 'Aaba', 'Baca', np.nan, 'CABA', 'cat'])
>>> s.str.count('a')
0    0.0
1    0.0
2    2.0
3    2.0
4    NaN
5    0.0
6    1.0
dtype: float64

```


Escape ‘$’ to find the literal dollar sign.

```
>>> s = ps.Series([', 'B', 'Aab, '$ca', 'C$B, 'cat'])
>>> s.str.count('\)
0    1
1    0
2    1
3    2
4    2
5    0
dtype: int64

```



# pyspark.pandas.Series.str.decode — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.decode

str.decode(_encoding_, _errors\='strict'_)
[#](#pyspark.pandas.Series.str.decode "Permalink to this definition")

Not supported.


# pyspark.pandas.Series.str.endswith — PySpark 4.0.1 documentation
str.endswith(_pattern_, _na\=None_)
[#](#pyspark.pandas.Series.str.endswith "Permalink to this definition")

Test if the end of each string element matches a pattern.

Equivalent to [`str.endswith()`](#pyspark.pandas.Series.str.endswith "pyspark.pandas.Series.str.endswith").

Parameters

**pattern**str

Character sequence. Regular expressions are not accepted.

**na**object, default None

Object shown if element is not a string. NaN converted to None.

Returns

Series of bool or object

pandas-on-Spark Series of booleans indicating whether the given pattern matches the end of each string element.

Examples

```
>>> s = ps.Series(['bat', 'Bear', 'cat', np.nan])
>>> s
0     bat
1    Bear
2     cat
3    None
dtype: object

```


```
>>> s.str.endswith('t')
0     True
1    False
2     True
3     None
dtype: object

```


Specifying na to be False instead of None.

```
>>> s.str.endswith('t', na=False)
0     True
1    False
2     True
3    False
dtype: bool

```


# pyspark.pandas.Series.str.extract — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.extract

str.extract(_pat_, _flags\=0_, _expand\=True_)
[#](#pyspark.pandas.Series.str.extract "Permalink to this definition")

Not supported.

# pyspark.pandas.Series.str.extractall — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.extractall

str.extractall(_pat_, _flags\=0_)
[#](#pyspark.pandas.Series.str.extractall "Permalink to this definition")

Not supported.


# pyspark.pandas.Series.str.find — PySpark 4.0.1 documentation
str.find(_sub_, _start\=0_, _end\=None_)
[#](#pyspark.pandas.Series.str.find "Permalink to this definition")

Return lowest indexes in each string in the Series where the substring is fully contained between \[start:end\].

Return -1 on failure. Equivalent to standard [`str.find()`](#pyspark.pandas.Series.str.find "pyspark.pandas.Series.str.find").

Parameters

**sub**str

Substring being searched.

**start**int

Left edge index.

**end**int

Right edge index.

Returns

Series of int

Series of lowest matching indexes.

Examples

```
>>> s = ps.Series(['apple', 'oranges', 'bananas'])

```


```
>>> s.str.find('a')
0    0
1    2
2    1
dtype: int64

```


```
>>> s.str.find('a', start=2)
0   -1
1    2
2    3
dtype: int64

```


```
>>> s.str.find('a', end=1)
0    0
1   -1
2   -1
dtype: int64

```


```
>>> s.str.find('a', start=2, end=2)
0   -1
1   -1
2   -1
dtype: int64

```


# pyspark.pandas.Series.str.findall — PySpark 4.0.1 documentation
str.findall(_pat_, _flags\=0_)
[#](#pyspark.pandas.Series.str.findall "Permalink to this definition")

Find all occurrences of pattern or regular expression in the Series.

Equivalent to applying `re.findall()` to all the elements in the Series.

Parameters

**pat**str

Pattern or regular expression.

**flags**int, default 0 (no flags)

re module flags, e.g. re.IGNORECASE.

Returns

Series of object

All non-overlapping matches of pattern or regular expression in each string of this Series.

Examples

```
>>> s = ps.Series(['Lion', 'Monkey', 'Rabbit'])

```


The search for the pattern ‘Monkey’ returns one match:

```
>>> s.str.findall('Monkey')
0          []
1    [Monkey]
2          []
dtype: object

```


On the other hand, the search for the pattern ‘MONKEY’ doesn’t return any match:

```
>>> s.str.findall('MONKEY')
0    []
1    []
2    []
dtype: object

```


Flags can be added to the pattern or regular expression. For instance, to find the pattern ‘MONKEY’ ignoring the case:

```
>>> import re
>>> s.str.findall('MONKEY', flags=re.IGNORECASE)
0          []
1    [Monkey]
2          []
dtype: object

```


When the pattern matches more than one string in the Series, all matches are returned:

```
>>> s.str.findall('on')
0    [on]
1    [on]
2      []
dtype: object

```


Regular expressions are supported too. For instance, the search for all the strings ending with the word ‘on’ is shown next:

```
>>> s.str.findall('on

If the pattern is found more than once in the same string, then a list of multiple strings is returned:

```
>>> s.str.findall('b')
0        []
1        []
2    [b, b]
dtype: object

```
)
0    [on]
1      []
2      []
dtype: object

```


If the pattern is found more than once in the same string, then a list of multiple strings is returned:

urltomarkdowncodeblockplaceholder60.09057472087336405


# pyspark.pandas.Series.str.get — PySpark 4.0.1 documentation
str.get(_i_)
[#](#pyspark.pandas.Series.str.get "Permalink to this definition")

Extract element from each string or string list/tuple in the Series at the specified position.

Parameters

**i**int

Position of element to extract.

Returns

Series of objects

Examples

```
>>> s1 = ps.Series(["String", "123"])
>>> s1
0    String
1       123
dtype: object

```


```
>>> s1.str.get(1)
0    t
1    2
dtype: object

```


```
>>> s1.str.get(-1)
0    g
1    3
dtype: object

```


```
>>> s2 = ps.Series([["a", "b", "c"], ["x", "y"]])
>>> s2
0    [a, b, c]
1       [x, y]
dtype: object

```


```
>>> s2.str.get(0)
0    a
1    x
dtype: object

```


```
>>> s2.str.get(2)
0       c
1    None
dtype: object

```


# pyspark.pandas.Series.str.get_dummies — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.get\_dummies

str.get\_dummies(_sep\='|'_)
[#](#pyspark.pandas.Series.str.get_dummies "Permalink to this definition")

Not supported.


# pyspark.pandas.Series.str.index — PySpark 4.0.1 documentation
str.index(_sub_, _start\=0_, _end\=None_)
[#](#pyspark.pandas.Series.str.index "Permalink to this definition")

Return lowest indexes in each string where the substring is fully contained between \[start:end\].

This is the same as [`str.find()`](about:blank/pyspark.pandas.Series.str.find.html#pyspark.pandas.Series.str.find "pyspark.pandas.Series.str.find") except instead of returning -1, it raises a ValueError when the substring is not found. Equivalent to standard [`str.index()`](#pyspark.pandas.Series.str.index "pyspark.pandas.Series.str.index").

Parameters

**sub**str

Substring being searched.

**start**int

Left edge index.

**end**int

Right edge index.

Returns

Series of int

Series of lowest matching indexes.

Examples

```
>>> s = ps.Series(['apple', 'oranges', 'bananas'])

```


```
>>> s.str.index('a')
0    0
1    2
2    1
dtype: int64

```


The following expression throws an exception:

```
>>> s.str.index('a', start=2) 

```


# pyspark.pandas.Series.str.isalnum — PySpark 4.0.1 documentation
str.isalnum()
[#](#pyspark.pandas.Series.str.isalnum "Permalink to this definition")

Check whether all characters in each string are alphanumeric.

This is equivalent to running the Python string method [`str.isalnum()`](#pyspark.pandas.Series.str.isalnum "pyspark.pandas.Series.str.isalnum") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s1 = ps.Series(['one', 'one1', '1', ''])

```


```
>>> s1.str.isalnum()
0     True
1     True
2     True
3    False
dtype: bool

```


Note that checks against characters mixed with any additional punctuation or whitespace will evaluate too false for an alphanumeric check.

```
>>> s2 = ps.Series(['A B', '1.5', '3,000'])
>>> s2.str.isalnum()
0    False
1    False
2    False
dtype: bool

```


# pyspark.pandas.Series.str.isalpha — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.isalpha

str.isalpha()
[#](#pyspark.pandas.Series.str.isalpha "Permalink to this definition")

Check whether all characters in each string are alphabetic.

This is equivalent to running the Python string method [`str.isalpha()`](#pyspark.pandas.Series.str.isalpha "pyspark.pandas.Series.str.isalpha") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s1 = ps.Series(['one', 'one1', '1', ''])

```


```
>>> s1.str.isalpha()
0     True
1    False
2    False
3    False
dtype: bool

```


[Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Series.str.isalpha.rst.txt)



# pyspark.pandas.Series.str.isdigit — PySpark 4.0.1 documentation
str.isdigit()
[#](#pyspark.pandas.Series.str.isdigit "Permalink to this definition")

Check whether all characters in each string are digits.

This is equivalent to running the Python string method [`str.isdigit()`](#pyspark.pandas.Series.str.isdigit "pyspark.pandas.Series.str.isdigit") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s = ps.Series(['23', '³', '⅕', ''])

```


The s.str.isdecimal method checks for characters used to form numbers in base 10.

```
>>> s.str.isdecimal()
0     True
1    False
2    False
3    False
dtype: bool

```


The s.str.isdigit method is the same as s.str.isdecimal but also includes special digits, like superscripted and subscripted digits in Unicode.

```
>>> s.str.isdigit()
0     True
1     True
2    False
3    False
dtype: bool

```


The s.str.isnumeric method is the same as s.str.isdigit but also includes other characters that can represent quantities such as unicode fractions.

```
>>> s.str.isnumeric()
0     True
1     True
2     True
3    False
dtype: bool

```


# pyspark.pandas.Series.str.isspace — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.isspace

str.isspace()
[#](#pyspark.pandas.Series.str.isspace "Permalink to this definition")

Check whether all characters in each string are whitespaces.

This is equivalent to running the Python string method [`str.isspace()`](#pyspark.pandas.Series.str.isspace "pyspark.pandas.Series.str.isspace") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s = ps.Series([' ', '\t\r\n ', ''])
>>> s.str.isspace()
0     True
1     True
2    False
dtype: bool

```


# pyspark.pandas.Series.str.islower — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.islower

str.islower()
[#](#pyspark.pandas.Series.str.islower "Permalink to this definition")

Check whether all characters in each string are lowercase.

This is equivalent to running the Python string method [`str.islower()`](#pyspark.pandas.Series.str.islower "pyspark.pandas.Series.str.islower") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s = ps.Series(['leopard', 'Golden Eagle', 'SNAKE', ''])
>>> s.str.islower()
0     True
1    False
2    False
3    False
dtype: bool

```


# pyspark.pandas.Series.str.isnumeric — PySpark 4.0.1 documentation
str.isnumeric()
[#](#pyspark.pandas.Series.str.isnumeric "Permalink to this definition")

Check whether all characters in each string are numeric.

This is equivalent to running the Python string method [`str.isnumeric()`](#pyspark.pandas.Series.str.isnumeric "pyspark.pandas.Series.str.isnumeric") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s1 = ps.Series(['one', 'one1', '1', ''])
>>> s1.str.isnumeric()
0    False
1    False
2     True
3    False
dtype: bool

```


```
>>> s2 = ps.Series(['23', '³', '⅕', ''])

```


The s2.str.isdecimal method checks for characters used to form numbers in base 10.

```
>>> s2.str.isdecimal()
0     True
1    False
2    False
3    False
dtype: bool

```


The s2.str.isdigit method is the same as s2.str.isdecimal but also includes special digits, like superscripted and subscripted digits in Unicode.

```
>>> s2.str.isdigit()
0     True
1     True
2    False
3    False
dtype: bool

```


The s2.str.isnumeric method is the same as s2.str.isdigit but also includes other characters that can represent quantities such as unicode fractions.

```
>>> s2.str.isnumeric()
0     True
1     True
2     True
3    False
dtype: bool

```


# pyspark.pandas.Series.str.isdecimal — PySpark 4.0.1 documentation
str.isdecimal()
[#](#pyspark.pandas.Series.str.isdecimal "Permalink to this definition")

Check whether all characters in each string are decimals.

This is equivalent to running the Python string method [`str.isdecimal()`](#pyspark.pandas.Series.str.isdecimal "pyspark.pandas.Series.str.isdecimal") for each element of the Series/Index. If a string has zero characters, False is returned for that check.

Examples

```
>>> s = ps.Series(['23', '³', '⅕', ''])

```


The s.str.isdecimal method checks for characters used to form numbers in base 10.

```
>>> s.str.isdecimal()
0     True
1    False
2    False
3    False
dtype: bool

```


The s.str.isdigit method is the same as s.str.isdecimal but also includes special digits, like superscripted and subscripted digits in Unicode.

```
>>> s.str.isdigit()
0     True
1     True
2    False
3    False
dtype: bool

```


The s.str.isnumeric method is the same as s.str.isdigit but also includes other characters that can represent quantities such as unicode fractions.

```
>>> s.str.isnumeric()
0     True
1     True
2     True
3    False
dtype: bool

```

# pyspark.pandas.Series.str.join — PySpark 4.0.1 documentation
str.join(_sep_)
[#](#pyspark.pandas.Series.str.join "Permalink to this definition")

Join lists contained as elements in the Series with passed delimiter.

If the elements of a Series are lists themselves, join the content of these lists using the delimiter passed to the function. This function is an equivalent to calling [`str.join()`](#pyspark.pandas.Series.str.join "pyspark.pandas.Series.str.join") on the lists.

Parameters

**sep**str

Delimiter to use between list entries.

Returns

Series of object

Series with list entries concatenated by intervening occurrences of the delimiter.

See also

[`str.split`](about:blank/pyspark.pandas.Series.str.split.html#pyspark.pandas.Series.str.split "pyspark.pandas.Series.str.split")

Split strings around given separator/delimiter.

[`str.rsplit`](about:blank/pyspark.pandas.Series.str.rsplit.html#pyspark.pandas.Series.str.rsplit "pyspark.pandas.Series.str.rsplit")

Splits string around given separator/delimiter, starting from the right.

Examples

Example with a list that contains a None element.

```
>>> s = ps.Series([['lion', 'elephant', 'zebra'],
...                ['cat', None, 'dog']])
>>> s
0    [lion, elephant, zebra]
1           [cat, None, dog]
dtype: object

```


Join all lists using a ‘-‘. The list containing None will produce None.

```
>>> s.str.join('-')
0    lion-elephant-zebra
1                   None
dtype: object

```


# pyspark.pandas.Series.str.len — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.len

str.len()
[#](#pyspark.pandas.Series.str.len "Permalink to this definition")

Computes the length of each element in the Series.

The element may be a sequence (such as a string, tuple or list).

Returns

Series of int

A Series of integer values indicating the length of each element in the Series.

Examples

Returns the length (number of characters) in a string. Returns the number of entries for lists or tuples.

```
>>> s1 = ps.Series(['dog', 'monkey'])
>>> s1.str.len()
0    3
1    6
dtype: int64

```


```
>>> s2 = ps.Series([["a", "b", "c"], []])
>>> s2.str.len()
0    3
1    0
dtype: int64

```


# pyspark.pandas.Series.str.ljust — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.ljust

str.ljust(_width_, _fillchar\=' '_)
[#](#pyspark.pandas.Series.str.ljust "Permalink to this definition")

Filling right side of strings in the Series with an additional character. Equivalent to [`str.ljust()`](#pyspark.pandas.Series.str.ljust "pyspark.pandas.Series.str.ljust").

Parameters

**width**int

Minimum width of resulting string; additional characters will be filled with fillchar.

**fillchar**str

Additional character for filling, default is whitespace.

Returns

Series of object

Examples

```
>>> s = ps.Series(["caribou", "tiger"])
>>> s
0    caribou
1      tiger
dtype: object

```


```
>>> s.str.ljust(width=10, fillchar='-')
0    caribou---
1    tiger-----
dtype: object

```


# pyspark.pandas.Series.str.lower — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.lower

str.lower()
[#](#pyspark.pandas.Series.str.lower "Permalink to this definition")

Convert strings in the Series/Index to all lowercase.

Examples

```
>>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object

```


```
>>> s.str.lower()
0                 lower
1              capitals
2    this is a sentence
3              swapcase
dtype: object

```


# pyspark.pandas.Series.str.lstrip — PySpark 4.0.1 documentation
str.lstrip(_to\_strip\=None_)
[#](#pyspark.pandas.Series.str.lstrip "Permalink to this definition")

Remove leading characters.

Strip whitespaces (including newlines) or a set of specified characters from each string in the Series/Index from left side. Equivalent to [`str.lstrip()`](#pyspark.pandas.Series.str.lstrip "pyspark.pandas.Series.str.lstrip").

Parameters

**to\_strip**str

Specifying the set of characters to be removed. All combinations of this set of characters will be stripped. If None then whitespaces are removed.

Returns

Series of object

Examples

```
>>> s = ps.Series(['1. Ant.', '2. Bee!\t', None])
>>> s
0      1. Ant.
1    2. Bee!\t
2         None
dtype: object

```


```
>>> s.str.lstrip('12.')
0       Ant.
1     Bee!\t
2       None
dtype: object

```

# pyspark.pandas.Series.str.match — PySpark 4.0.1 documentation
str.match(_pat_, _case\=True_, _flags\=0_, _na\=nan_)
[#](#pyspark.pandas.Series.str.match "Permalink to this definition")

Determine if each string matches a regular expression.

Analogous to [`contains()`](about:blank/pyspark.pandas.Series.str.contains.html#pyspark.pandas.Series.str.contains "pyspark.pandas.Series.str.contains"), but more strict, relying on `re.match()` instead of `re.search()`.

Parameters

**pat**str

Character sequence or regular expression.

**case**bool, default True

If True, case sensitive.

**flags**int, default 0 (no flags)

Flags to pass through to the re module, e.g. re.IGNORECASE.

**na**default NaN

Fill value for missing values.

Returns

Series of boolean values or object

A Series of boolean values indicating whether the given pattern can be matched in the string of each element of the Series.

Examples

```
>>> s = ps.Series(['Mouse', 'dog', 'house and parrot', '23', np.nan])
>>> s.str.match('dog')
0    False
1     True
2    False
3    False
4     None
dtype: object

```


```
>>> s.str.match('mouse|dog', case=False)
0     True
1     True
2    False
3    False
4     None
dtype: object

```


```
>>> s.str.match('.+and.+', na=True)
0    False
1    False
2     True
3    False
4     True
dtype: bool

```


```
>>> import re
>>> s.str.match('MOUSE', flags=re.IGNORECASE)
0     True
1    False
2    False
3    False
4     None
dtype: object

```

# pyspark.pandas.Series.str.normalize — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.normalize

str.normalize(_form_)
[#](#pyspark.pandas.Series.str.normalize "Permalink to this definition")

Return the Unicode normal form for the strings in the Series.

For more information on the forms, see the `unicodedata.normalize()`.

Parameters

**form**{‘NFC’, ‘NFKC’, ‘NFD’, ‘NFKD’}

Unicode form.

Returns

Series of objects

A Series of normalized strings.

[Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.Series.str.normalize.rst.txt)



# pyspark.pandas.Series.str.pad — PySpark 4.0.1 documentation
str.pad(_width_, _side\='left'_, _fillchar\=' '_)
[#](#pyspark.pandas.Series.str.pad "Permalink to this definition")

Pad strings in the Series up to width.

Parameters

**width**int

Minimum width of resulting string; additional characters will be filled with character defined in fillchar.

**side**{‘left’, ‘right’, ‘both’}, default ‘left’

Side from which to fill resulting string.

**fillchar**str, default ‘ ‘

Additional character for filling, default is whitespace.

Returns

Series of object

Returns Series with minimum number of char in object.

Examples

```
>>> s = ps.Series(["caribou", "tiger"])
>>> s
0    caribou
1      tiger
dtype: object

```


```
>>> s.str.pad(width=10)
0       caribou
1         tiger
dtype: object

```


```
>>> s.str.pad(width=10, side='right', fillchar='-')
0    caribou---
1    tiger-----
dtype: object

```


```
>>> s.str.pad(width=10, side='both', fillchar='-')
0    -caribou--
1    --tiger---
dtype: object

```


# pyspark.pandas.Series.str.partition — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.partition

str.partition(_sep\=' '_, _expand\=True_)
[#](#pyspark.pandas.Series.str.partition "Permalink to this definition")

Not supported.

# pyspark.pandas.Series.str.repeat — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.repeat

str.repeat(_repeats_)
[#](#pyspark.pandas.Series.str.repeat "Permalink to this definition")

Duplicate each string in the Series.

Parameters

**repeats**int

Repeat the string given number of times (int). Sequence of int is not supported.

Returns

Series of object

Series or Index of repeated string objects specified by input parameter repeats.

Examples

```
>>> s = ps.Series(['a', 'b', 'c'])
>>> s
0    a
1    b
2    c
dtype: object

```


Single int repeats string in Series

```
>>> s.str.repeat(repeats=2)
0    aa
1    bb
2    cc
dtype: object

```

# pyspark.pandas.Series.str.replace — PySpark 4.0.1 documentation
str.replace(_pat_, _repl_, _n\=\- 1_, _case\=None_, _flags\=0_, _regex\=False_)
[#](#pyspark.pandas.Series.str.replace "Permalink to this definition")

Replace occurrences of pattern/regex in the Series with some other string. Equivalent to [`str.replace()`](#pyspark.pandas.Series.str.replace "pyspark.pandas.Series.str.replace") or `re.sub()`.

Parameters

**pat**str or compiled regex

String can be a character sequence or regular expression.

**repl**str or callable

Replacement string or a callable. The callable is passed the regex match object and must return a replacement string to be used. See `re.sub()`.

**n**int, default -1 (all)

Number of replacements to make from start.

**case**boolean, default None

If True, case sensitive (the default if pat is a string). Set to False for case insensitive. Cannot be set if pat is a compiled regex.

**flags: int, default 0 (no flags)**

re module flags, e.g. re.IGNORECASE. Cannot be set if pat is a compiled regex.

**regex**boolean, default True

If True, assumes the passed-in pattern is a regular expression. If False, treats the pattern as a literal string. Cannot be set to False if pat is a compile regex or repl is a callable.

Returns

Series of object

A copy of the string with all matching occurrences of pat replaced by repl.

Examples

When pat is a string and regex is True (the default), the given pat is compiled as a regex. When repl is a string, it replaces matching regex patterns as with `re.sub()`. NaN value(s) in the Series are changed to None:

```
>>> ps.Series(['foo', 'fuz', np.nan]).str.replace('f.', 'ba', regex=True)
0     bao
1     baz
2    None
dtype: object

```


When pat is a string and regex is False, every pat is replaced with repl as with [`str.replace()`](#pyspark.pandas.Series.str.replace "pyspark.pandas.Series.str.replace"):

```
>>> ps.Series(['f.o', 'fuz', np.nan]).str.replace('f.', 'ba', regex=False)
0     bao
1     fuz
2    None
dtype: object

```


When repl is a callable, it is called on every pat using `re.sub()`. The callable should expect one positional argument (a regex object) and return a string.

Reverse every lowercase alphabetic word:

```
>>> repl = lambda m: m.group(0)
[::-1]
>>> ps.Series(['foo 123', 'bar baz', np.nan]).str.replace('[a-z]+', repl, regex=True)
0    oof 123
1    rab zab
2       None
dtype: object

```


Using regex groups (extract second group and swap case):

```
>>> pat = "(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"
>>> repl = lambda m: m.group('two').swapcase()
>>> ps.Series(['One Two Three', 'Foo Bar Baz']).str.replace(pat, repl, regex=True)
0    tWO
1    bAR
dtype: object

```


Using a compiled regex with flags:

```
>>> import re
>>> regex_pat = re.compile('FUZ', flags=re.IGNORECASE)
>>> ps.Series(['foo', 'fuz', np.nan]).str.replace(regex_pat, 'bar', regex=True)
0     foo
1     bar
2    None
dtype: object

```

# pyspark.pandas.Series.str.rfind — PySpark 4.0.1 documentation
str.rfind(_sub_, _start\=0_, _end\=None_)
[#](#pyspark.pandas.Series.str.rfind "Permalink to this definition")

Return highest indexes in each string in the Series where the substring is fully contained between \[start:end\].

Return -1 on failure. Equivalent to standard [`str.rfind()`](#pyspark.pandas.Series.str.rfind "pyspark.pandas.Series.str.rfind").

Parameters

**sub**str

Substring being searched.

**start**int

Left edge index.

**end**int

Right edge index.

Returns

Series of int

Series of highest matching indexes.

Examples

```
>>> s = ps.Series(['apple', 'oranges', 'bananas'])

```


```
>>> s.str.rfind('a')
0    0
1    2
2    5
dtype: int64

```


```
>>> s.str.rfind('a', start=2)
0   -1
1    2
2    5
dtype: int64

```


```
>>> s.str.rfind('a', end=1)
0    0
1   -1
2   -1
dtype: int64

```


```
>>> s.str.rfind('a', start=2, end=2)
0   -1
1   -1
2   -1
dtype: int64

```


# pyspark.pandas.Series.str.rindex — PySpark 4.0.1 documentation
str.rindex(_sub_, _start\=0_, _end\=None_)
[#](#pyspark.pandas.Series.str.rindex "Permalink to this definition")

Return highest indexes in each string where the substring is fully contained between \[start:end\].

This is the same as [`str.rfind()`](about:blank/pyspark.pandas.Series.str.rfind.html#pyspark.pandas.Series.str.rfind "pyspark.pandas.Series.str.rfind") except instead of returning -1, it raises a ValueError when the substring is not found. Equivalent to standard [`str.rindex()`](#pyspark.pandas.Series.str.rindex "pyspark.pandas.Series.str.rindex").

Parameters

**sub**str

Substring being searched.

**start**int

Left edge index.

**end**int

Right edge index.

Returns

Series of int

Series of highest matching indexes.

Examples

```
>>> s = ps.Series(['apple', 'oranges', 'bananas'])

```


```
>>> s.str.rindex('a')
0    0
1    2
2    5
dtype: int64

```


The following expression throws an exception:

```
>>> s.str.rindex('a', start=2) 

```



# pyspark.pandas.Series.str.rjust — PySpark 4.0.1 documentation
str.rjust(_width_, _fillchar\=' '_)
[#](#pyspark.pandas.Series.str.rjust "Permalink to this definition")

Filling left side of strings in the Series with an additional character. Equivalent to [`str.rjust()`](#pyspark.pandas.Series.str.rjust "pyspark.pandas.Series.str.rjust").

Parameters

**width**int

Minimum width of resulting string; additional characters will be filled with fillchar.

**fillchar**str

Additional character for filling, default is whitespace.

Returns

Series of object

Examples

```
>>> s = ps.Series(["caribou", "tiger"])
>>> s
0    caribou
1      tiger
dtype: object

```


```
>>> s.str.rjust(width=10)
0       caribou
1         tiger
dtype: object

```


```
>>> s.str.rjust(width=10, fillchar='-')
0    ---caribou
1    -----tiger
dtype: object

```


# pyspark.pandas.Series.str.rpartition — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.rpartition

str.rpartition(_sep\=' '_, _expand\=True_)
[#](#pyspark.pandas.Series.str.rpartition "Permalink to this definition")

Not supported.

# pyspark.pandas.Series.str.rsplit — PySpark 4.0.1 documentation
str.rsplit(_pat\=None_, _n\=\- 1_, _expand\=False_)
[#](#pyspark.pandas.Series.str.rsplit "Permalink to this definition")

Split strings around given separator/delimiter.

Splits the string in the Series from the end, at the specified delimiter string. Equivalent to [`str.rsplit()`](#pyspark.pandas.Series.str.rsplit "pyspark.pandas.Series.str.rsplit").

Parameters

**pat**str, optional

String or regular expression to split on. If not specified, split on whitespace.

**n**int, default -1 (all)

Limit number of splits in output. None, 0 and -1 will be interpreted as return all splits.

**expand**bool, default False

Expand the split strings into separate columns.

*   If `True`, n must be a positive integer, and return DataFrame expanding dimensionality.
    
*   If `False`, return Series, containing lists of strings.
    

Returns

Series, DataFrame

Type matches caller unless expand=True (see Notes).

See also

[`str.split`](about:blank/pyspark.pandas.Series.str.split.html#pyspark.pandas.Series.str.split "pyspark.pandas.Series.str.split")

Split strings around given separator/delimiter.

[`str.join`](about:blank/pyspark.pandas.Series.str.join.html#pyspark.pandas.Series.str.join "pyspark.pandas.Series.str.join")

Join lists contained as elements in the Series/Index with passed delimiter.

Notes

The handling of the n keyword depends on the number of found splits:

*   If found splits > n, make first n splits only
    
*   If found splits <= n, make all splits
    
*   If for a certain row the number of found splits < n, append None for padding up to n if `expand=True`
    

If using `expand=True`, Series callers return DataFrame objects with n + 1 columns.

Note

Even if n is much larger than found splits, the number of columns does NOT shrink unlike pandas.

Examples

```
>>> s = ps.Series(["this is a regular sentence",
...                "https://docs.python.org/3/tutorial/index.html",
...                np.nan])

```


In the default setting, the string is split by whitespace.

```
>>> s.str.split()  
0                   [this, is, a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


Without the n parameter, the outputs of rsplit and split are identical.

```
>>> s.str.rsplit()  
0                   [this, is, a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


The n parameter can be used to limit the number of splits on the delimiter. The outputs of split and rsplit are different.

```
>>> s.str.split(n=2)  
0                     [this, is, a regular sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


```
>>> s.str.rsplit(n=2)  
0                     [this is a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


When using `expand=True`, the split elements will expand out into separate columns. If NaN is present, it is propagated throughout the columns during the split.

```
>>> s.str.split(n=4, expand=True)  
                                               0     1     2        3         4
0                                           this    is     a  regular  sentence
1  https://docs.python.org/3/tutorial/index.html  None  None     None      None
2                                           None  None  None     None      None

```


For slightly more complex use cases like splitting the html document name from a url, a combination of parameter settings can be used.

```
>>> s.str.rsplit("/", n=1, expand=True)  
                                    0           1
0          this is a regular sentence        None
1  https://docs.python.org/3/tutorial  index.html
2                                None        None

```


Remember to escape special characters when explicitly using regular expressions.

```
>>> s = ps.Series(["1+1=2"])
>>> s.str.split(r"\+|=", n=2, expand=True)  
   0  1  2
0  1  1  2

```


# pyspark.pandas.Series.str.rstrip — PySpark 4.0.1 documentation
str.rstrip(_to\_strip\=None_)
[#](#pyspark.pandas.Series.str.rstrip "Permalink to this definition")

Remove trailing characters.

Strip whitespaces (including newlines) or a set of specified characters from each string in the Series/Index from right side. Equivalent to [`str.rstrip()`](#pyspark.pandas.Series.str.rstrip "pyspark.pandas.Series.str.rstrip").

Parameters

**to\_strip**str

Specifying the set of characters to be removed. All combinations of this set of characters will be stripped. If None then whitespaces are removed.

Returns

Series of object

Examples

```
>>> s = ps.Series(['1. Ant.', '2. Bee!\t', None])
>>> s
0      1. Ant.
1    2. Bee!\t
2         None
dtype: object

```


```
>>> s.str.rstrip('.!\t')
0    1. Ant
1    2. Bee
2      None
dtype: object

```

# pyspark.pandas.Series.str.slice — PySpark 4.0.1 documentation
str.slice(_start\=None_, _stop\=None_, _step\=None_)
[#](#pyspark.pandas.Series.str.slice "Permalink to this definition")

Slice substrings from each element in the Series.

Parameters

**start**int, optional

Start position for slice operation.

**stop**int, optional

Stop position for slice operation.

**step**int, optional

Step size for slice operation.

Returns

Series of object

Series from sliced substrings from original string objects.

Examples

```
>>> s = ps.Series(["koala", "fox", "chameleon"])
>>> s
0        koala
1          fox
2    chameleon
dtype: object

```


```
>>> s.str.slice(start=1)
0        oala
1          ox
2    hameleon
dtype: object

```


```
>>> s.str.slice(stop=2)
0    ko
1    fo
2    ch
dtype: object

```


```
>>> s.str.slice(step=2)
0      kaa
1       fx
2    caeen
dtype: object

```


```
>>> s.str.slice(start=0, stop=5, step=3)
0    kl
1     f
2    cm
dtype: object

```


# pyspark.pandas.Series.str.slice_replace — PySpark 4.0.1 documentation
str.slice\_replace(_start\=None_, _stop\=None_, _repl\=None_)
[#](#pyspark.pandas.Series.str.slice_replace "Permalink to this definition")

Slice substrings from each element in the Series.

Parameters

**start**int, optional

Start position for slice operation. If not specified (None), the slice is unbounded on the left, i.e. slice from the start of the string.

**stop**int, optional

Stop position for slice operation. If not specified (None), the slice is unbounded on the right, i.e. slice until the end of the string.

**repl**str, optional

String for replacement. If not specified (None), the sliced region is replaced with an empty string.

Returns

Series of object

Series from sliced substrings from original string objects.

Examples

```
>>> s = ps.Series(['a', 'ab', 'abc', 'abdc', 'abcde'])
>>> s
0        a
1       ab
2      abc
3     abdc
4    abcde
dtype: object

```


Specify just start, meaning replace start until the end of the string with repl.

```
>>> s.str.slice_replace(1, repl='X')
0    aX
1    aX
2    aX
3    aX
4    aX
dtype: object

```


Specify just stop, meaning the start of the string to stop is replaced with repl, and the rest of the string is included.

```
>>> s.str.slice_replace(stop=2, repl='X')
0       X
1       X
2      Xc
3     Xdc
4    Xcde
dtype: object

```


Specify start and stop, meaning the slice from start to stop is replaced with repl. Everything before or after start and stop is included as is.

```
>>> s.str.slice_replace(start=1, stop=3, repl='X')
0      aX
1      aX
2      aX
3     aXc
4    aXde
dtype: object

```
# pyspark.pandas.Series.str.split — PySpark 4.0.1 documentation
str.split(_pat\=None_, _n\=\- 1_, _expand\=False_)
[#](#pyspark.pandas.Series.str.split "Permalink to this definition")

Split strings around given separator/delimiter.

Splits the string in the Series from the beginning, at the specified delimiter string. Equivalent to [`str.split()`](#pyspark.pandas.Series.str.split "pyspark.pandas.Series.str.split").

Parameters

**pat**str, optional

String or regular expression to split on. If not specified, split on whitespace.

**n**int, default -1 (all)

Limit number of splits in output. None, 0 and -1 will be interpreted as return all splits.

**expand**bool, default False

Expand the split strings into separate columns.

*   If `True`, n must be a positive integer, and return DataFrame expanding dimensionality.
    
*   If `False`, return Series, containing lists of strings.
    

Returns

Series, DataFrame

Type matches caller unless expand=True (see Notes).

See also

[`str.rsplit`](about:blank/pyspark.pandas.Series.str.rsplit.html#pyspark.pandas.Series.str.rsplit "pyspark.pandas.Series.str.rsplit")

Splits string around given separator/delimiter, starting from the right.

[`str.join`](about:blank/pyspark.pandas.Series.str.join.html#pyspark.pandas.Series.str.join "pyspark.pandas.Series.str.join")

Join lists contained as elements in the Series/Index with passed delimiter.

Notes

The handling of the n keyword depends on the number of found splits:

*   If found splits > n, make first n splits only
    
*   If found splits <= n, make all splits
    
*   If for a certain row the number of found splits < n, append None for padding up to n if `expand=True`
    

If using `expand=True`, Series callers return DataFrame objects with n + 1 columns.

Note

Even if n is much larger than found splits, the number of columns does NOT shrink unlike pandas.

Examples

```
>>> s = ps.Series(["this is a regular sentence",
...                "https://docs.python.org/3/tutorial/index.html",
...                np.nan])

```


In the default setting, the string is split by whitespace.

```
>>> s.str.split()  
0                   [this, is, a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


Without the n parameter, the outputs of rsplit and split are identical.

```
>>> s.str.rsplit()  
0                   [this, is, a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


The n parameter can be used to limit the number of splits on the delimiter. The outputs of split and rsplit are different.

```
>>> s.str.split(n=2)  
0                     [this, is, a regular sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


```
>>> s.str.rsplit(n=2)  
0                     [this is a, regular, sentence]
1    [https://docs.python.org/3/tutorial/index.html]
2                                               None
dtype: object

```


The pat parameter can be used to split by other characters.

```
>>> s.str.split(pat = "/")  
0                         [this is a regular sentence]
1    [https:, , docs.python.org, 3, tutorial, index...
2                                                 None
dtype: object

```


When using `expand=True`, the split elements will expand out into separate columns. If NaN is present, it is propagated throughout the columns during the split.

```
>>> s.str.split(n=4, expand=True)  
                                               0     1     2        3         4
0                                           this    is     a  regular  sentence
1  https://docs.python.org/3/tutorial/index.html  None  None     None      None
2                                           None  None  None     None      None

```


For slightly more complex use cases like splitting the html document name from a url, a combination of parameter settings can be used.

```
>>> s.str.rsplit("/", n=1, expand=True)  
                                    0           1
0          this is a regular sentence        None
1  https://docs.python.org/3/tutorial  index.html
2                                None        None

```


Remember to escape special characters when explicitly using regular expressions.

```
>>> s = ps.Series(["1+1=2"])
>>> s.str.split(r"\+|=", n=2, expand=True)  
   0  1  2
0  1  1  2

```



# pyspark.pandas.Series.str.startswith — PySpark 4.0.1 documentation
str.startswith(_pattern_, _na\=None_)
[#](#pyspark.pandas.Series.str.startswith "Permalink to this definition")

Test if the start of each string element matches a pattern.

Equivalent to [`str.startswith()`](#pyspark.pandas.Series.str.startswith "pyspark.pandas.Series.str.startswith").

Parameters

**pattern**str

Character sequence. Regular expressions are not accepted.

**na**object, default None

Object shown if element is not a string. NaN converted to None.

Returns

Series of bool or object

pandas-on-Spark Series of booleans indicating whether the given pattern matches the start of each string element.

Examples

```
>>> s = ps.Series(['bat', 'Bear', 'cat', np.nan])
>>> s
0     bat
1    Bear
2     cat
3    None
dtype: object

```


```
>>> s.str.startswith('b')
0     True
1    False
2    False
3     None
dtype: object

```


Specifying na to be False instead of None.

```
>>> s.str.startswith('b', na=False)
0     True
1    False
2    False
3    False
dtype: bool

```
# pyspark.pandas.Series.str.strip — PySpark 4.0.1 documentation
str.strip(_to\_strip\=None_)
[#](#pyspark.pandas.Series.str.strip "Permalink to this definition")

Remove leading and trailing characters.

Strip whitespaces (including newlines) or a set of specified characters from each string in the Series/Index from left and right sides. Equivalent to [`str.strip()`](#pyspark.pandas.Series.str.strip "pyspark.pandas.Series.str.strip").

Parameters

**to\_strip**str

Specifying the set of characters to be removed. All combinations of this set of characters will be stripped. If None then whitespaces are removed.

Returns

Series of objects

Examples

```
>>> s = ps.Series(['1. Ant.', '2. Bee!\t', None])
>>> s
0      1. Ant.
1    2. Bee!\t
2         None
dtype: object

```


```
>>> s.str.strip()
0    1. Ant.
1    2. Bee!
2       None
dtype: object

```


```
>>> s.str.strip('12.')
0        Ant
1     Bee!\t
2       None
dtype: object

```


```
>>> s.str.strip('.!\t')
0    1. Ant
1    2. Bee
2      None
dtype: object

```



# pyspark.pandas.Series.str.swapcase — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.swapcase

str.swapcase()
[#](#pyspark.pandas.Series.str.swapcase "Permalink to this definition")

Convert strings in the Series/Index to be swap cased.

Examples

```
>>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object

```


```
>>> s.str.swapcase()
0                 LOWER
1              capitals
2    THIS IS A SENTENCE
3              sWaPcAsE
dtype: object

```

# pyspark.pandas.Series.str.title — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.title

str.title()
[#](#pyspark.pandas.Series.str.title "Permalink to this definition")

Convert Strings in the series to be title case.

Examples

```
>>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object

```


```
>>> s.str.title()
0                 Lower
1              Capitals
2    This Is A Sentence
3              Swapcase
dtype: object

```



# pyspark.pandas.Series.str.translate — PySpark 4.0.1 documentation
str.translate(_table_)
[#](#pyspark.pandas.Series.str.translate "Permalink to this definition")

Map all characters in the string through the given mapping table. Equivalent to standard [`str.translate()`](#pyspark.pandas.Series.str.translate "pyspark.pandas.Series.str.translate").

Parameters

**table**dict

Table is a mapping of Unicode ordinals to Unicode ordinals, strings, or None. Unmapped characters are left untouched. Characters mapped to None are deleted. `str.maketrans()` is a helper function for making translation tables.

Returns

Series of object

Series with translated strings.

Examples

```
>>> s = ps.Series(["dog", "cat", "bird"])
>>> m = str.maketrans({'a': 'X', 'i': 'Y', 'o': None})
>>> s.str.translate(m)
0      dg
1     cXt
2    bYrd
dtype: object

```



# pyspark.pandas.Series.str.upper — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.str.upper

str.upper()
[#](#pyspark.pandas.Series.str.upper "Permalink to this definition")

Convert strings in the Series/Index to all uppercase.

Examples

```
>>> s = ps.Series(['lower', 'CAPITALS', 'this is a sentence', 'SwApCaSe'])
>>> s
0                 lower
1              CAPITALS
2    this is a sentence
3              SwApCaSe
dtype: object

```


```
>>> s.str.upper()
0                 LOWER
1              CAPITALS
2    THIS IS A SENTENCE
3              SWAPCASE
dtype: object

```


# pyspark.pandas.Series.str.wrap — PySpark 4.0.1 documentation
str.wrap(_width_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.str.wrap "Permalink to this definition")

Wrap long strings in the Series to be formatted in paragraphs with length less than a given width.

This method has the same keyword parameters and defaults as `textwrap.TextWrapper`.

Parameters

**width**int

Maximum line-width. Lines separated with newline char.

**expand\_tabs**bool, optional

If true, tab characters will be expanded to spaces (default: True).

**replace\_whitespace**bool, optional

If true, each whitespace character remaining after tab expansion will be replaced by a single space (default: True).

**drop\_whitespace**bool, optional

If true, whitespace that, after wrapping, happens to end up at the beginning or end of a line is dropped (default: True).

**break\_long\_words**bool, optional

If true, then words longer than width will be broken to ensure that no lines are longer than width. If it is false, long words will not be broken, and some lines may be longer than width (default: True).

**break\_on\_hyphens**bool, optional

If true, wrapping will occur preferably on whitespace and right after hyphens in compound words, as it is customary in English. If false, only whitespaces will be considered as potentially good places for line breaks, but you need to set break\_long\_words to false if you want truly insecable words (default: True).

Returns

Series of object

Series with wrapped strings.

Examples

```
>>> s = ps.Series(['line to be wrapped', 'another line to be wrapped'])
>>> s.str.wrap(12)
0             line to be\nwrapped
1    another line\nto be\nwrapped
dtype: object

```


# pyspark.pandas.Series.str.zfill — PySpark 4.0.1 documentation
str.zfill(_width_)
[#](#pyspark.pandas.Series.str.zfill "Permalink to this definition")

Pad strings in the Series by prepending ‘0’ characters.

Strings in the Series are padded with ‘0’ characters on the left of the string to reach a total string length width. Strings in the Series with length greater or equal to width are unchanged.

Differs from [`str.zfill()`](#pyspark.pandas.Series.str.zfill "pyspark.pandas.Series.str.zfill") which has special handling for ‘+’/’-‘ in the string.

Parameters

**width**int

Minimum length of resulting string; strings with length less than width be prepended with ‘0’ characters.

Returns

Series of object

Series with ‘0’ left-padded strings.

Examples

```
>>> s = ps.Series(['-1', '1', '1000', np.nan])
>>> s
0      -1
1       1
2    1000
3    None
dtype: object

```


Note that NaN is not a string, therefore it is converted to NaN. The minus sign in ‘-1’ is treated as a regular character and the zero is added to the left of it ([`str.zfill()`](#pyspark.pandas.Series.str.zfill "pyspark.pandas.Series.str.zfill") would have moved it to the left). 1000 remains unchanged as it is longer than width.

```
>>> s.str.zfill(3)  
0     -01
1     001
2    1000
3    None
dtype: object

```


# pyspark.pandas.Series.cat.categories — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.cat.categories

cat.categories[#](#pyspark.pandas.Series.cat.categories "Permalink to this definition")

The categories of this categorical.

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.categories
Index(['a', 'b', 'c'], dtype='object')

```


# pyspark.pandas.Series.cat.ordered — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.cat.ordered

cat.ordered[#](#pyspark.pandas.Series.cat.ordered "Permalink to this definition")

Whether the categories have an ordered relationship.

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


# pyspark.pandas.Series.cat.codes — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.cat.codes

cat.codes[#](#pyspark.pandas.Series.cat.codes "Permalink to this definition")

Return Series of codes as well as the index.

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.codes
0    0
1    1
2    1
3    2
4    2
5    2
dtype: int8

```


# pyspark.pandas.Series.cat.rename_categories — PySpark 4.0.1 documentation
cat.rename\_categories(_new\_categories_)
[#](#pyspark.pandas.Series.cat.rename_categories "Permalink to this definition")

Rename categories.

Parameters

**new\_categories**list-like, dict-like or callable

New categories which will replace old categories.

*   list-like: all items must be unique and the number of items in the new categories must match the existing number of categories.
    
*   dict-like: specifies a mapping from old categories to new. Categories not contained in the mapping are passed through and extra categories in the mapping are ignored.
    
*   callable : a callable that is called on all items in the old categories and whose return values comprise the new categories.
    

Returns

**cat**Series

Categorical with removed categories

Raises

ValueError

If new categories are list-like and do not have the same number of items than the current categories or do not validate as categories

Examples

```
>>> s = ps.Series(["a", "a", "b"], dtype="category")
>>> s.cat.rename_categories([0, 1])  
0    0
1    0
2    1
dtype: category
Categories (2, int64): [0, 1]

```


For dict-like `new_categories`, extra keys are ignored and categories not in the dictionary are passed through

```
>>> s.cat.rename_categories({'a': 'A', 'c': 'C'})  
0    A
1    A
2    b
dtype: category
Categories (2, object): ['A', 'b']

```


You may also provide a callable to create the new categories

```
>>> s.cat.rename_categories(lambda x: x.upper())  
0    A
1    A
2    B
dtype: category
Categories (2, object): ['A', 'B']

```


# pyspark.pandas.Series.cat.reorder_categories — PySpark 4.0.1 documentation
cat.reorder\_categories(_new\_categories_, _ordered\=None_)
[#](#pyspark.pandas.Series.cat.reorder_categories "Permalink to this definition")

Reorder categories as specified in new\_categories.

new\_categories needs to include all old categories and no new category items.

Parameters

**new\_categories**Index-like

The categories in new order.

**ordered**bool, optional

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

Returns

**cat**Series

Categorical with removed categories

Raises

ValueError

If the new categories do not contain all old category items or any new ones

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.reorder_categories(['c', 'b', 'a'], ordered=True)  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['c' < 'b' < 'a']

```


# pyspark.pandas.Series.cat.add_categories — PySpark 4.0.1 documentation
cat.add\_categories(_new\_categories_)
[#](#pyspark.pandas.Series.cat.add_categories "Permalink to this definition")

Add new categories.

new\_categories will be included at the last/highest place in the categories and will be unused directly after this call.

Parameters

**new\_categories**category or list-like of category

The new categories to be included.

Returns

Series

Categorical with new categories added

Raises

ValueError

If the new categories include old categories or do not validate as categories

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.add_categories('x')  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (4, object): ['a', 'b', 'c', 'x']

```


# pyspark.pandas.Series.cat.remove_categories — PySpark 4.0.1 documentation
cat.remove\_categories(_removals_)
[#](#pyspark.pandas.Series.cat.remove_categories "Permalink to this definition")

Remove the specified categories.

removals must be included in the old categories. Values which were in the removed categories will be set to NaN

Parameters

**removals**category or list of categories

The categories which should be removed.

Returns

Series

Categorical with removed categories

Raises

ValueError

If the removals are not contained in the categories

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.remove_categories('b')  
0      a
1    NaN
2    NaN
3      c
4      c
5      c
dtype: category
Categories (2, object): ['a', 'c']

```

# pyspark.pandas.Series.cat.remove_unused_categories — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.cat.remove\_unused\_categories

cat.remove\_unused\_categories()
[#](#pyspark.pandas.Series.cat.remove_unused_categories "Permalink to this definition")

Remove categories which are not used.

Returns

**cat**Series

Categorical with unused categories dropped

Examples

```
>>> s = ps.Series(pd.Categorical(list("abbccc"), categories=['a', 'b', 'c', 'd']))
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (4, object): ['a', 'b', 'c', 'd']

```


```
>>> s.cat.remove_unused_categories()  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```

# pyspark.pandas.Series.cat.set_categories — PySpark 4.0.1 documentation
cat.set\_categories(_new\_categories_, _ordered\=None_, _rename\=False_)
[#](#pyspark.pandas.Series.cat.set_categories "Permalink to this definition")

Set the categories to the specified new\_categories.

new\_categories can include new categories (which will result in unused categories) or remove old categories (which results in values set to NaN). If rename==True, the categories will simply be renamed (less or more items than in old categories will result in values set to NaN or in unused categories respectively).

This method can be used to perform more than one action of adding, removing, and reordering simultaneously and is therefore faster than performing the individual steps via the more specialised methods.

On the other hand this methods does not do checks (e.g., whether the old categories are included in the new categories on a reorder), which can result in surprising changes, for example when using special string dtypes, which does not consider a S1 string equal to a single char python string.

Parameters

**new\_categories**Index-like

The categories in new order.

**ordered**bool, default False

Whether or not the categorical is treated as an ordered categorical. If not given, do not change the ordered information.

**rename**bool, default False

Whether or not the new\_categories should be considered as a rename of the old categories or as reordered categories.

Returns

Series with reordered categories

Raises

ValueError

If new\_categories does not validate as categories

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.set_categories(['b', 'c'])  
0    NaN
1      b
2      b
3      c
4      c
5      c
dtype: category
Categories (2, object): ['b', 'c']

```


```
>>> s.cat.set_categories([1, 2, 3], rename=True)  
0    1
1    2
2    2
3    3
4    3
5    3
dtype: category
Categories (3, int64): [1, 2, 3]

```


```
>>> s.cat.set_categories([1, 2, 3], rename=True, ordered=True)  
0    1
1    2
2    2
3    3
4    3
5    3
dtype: category
Categories (3, int64): [1 < 2 < 3]

```

# pyspark.pandas.Series.cat.as_ordered — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.cat.as\_ordered

cat.as\_ordered()
[#](#pyspark.pandas.Series.cat.as_ordered "Permalink to this definition")

Set the Categorical to be ordered.

Returns

Series

Ordered Categorical

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category")
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```


```
>>> s.cat.as_ordered()  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a' < 'b' < 'c']

```

# pyspark.pandas.Series.cat.as_unordered — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.cat.as\_unordered

cat.as\_unordered()
[#](#pyspark.pandas.Series.cat.as_unordered "Permalink to this definition")

Set the Categorical to be unordered.

Returns

Series

Unordered Categorical

Examples

```
>>> s = ps.Series(list("abbccc"), dtype="category").cat.as_ordered()
>>> s  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a' < 'b' < 'c']

```


```
>>> s.cat.as_unordered()  
0    a
1    b
2    b
3    c
4    c
5    c
dtype: category
Categories (3, object): ['a', 'b', 'c']

```



# pyspark.pandas.Series.plot.area — PySpark 4.0.1 documentation
plot.area(_x\=None_, _y\=None_, _\*\*kwds_)
[#](#pyspark.pandas.Series.plot.area "Permalink to this definition")

Draw a stacked area plot.

An area plot displays quantitative data visually. This function wraps the plotly area function.

Parameters

**x**label or position, optional

Coordinates for the X axis. By default it uses the index.

**y**label or position, optional

Column to plot. By default it uses all columns.

**stacked**bool, default True

Area plots are stacked by default. Set to False to create an unstacked plot (matplotlib-only).

**\*\*kwds**optional

Additional keyword arguments are documented in `DataFrame.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

For Series

```
>>> df = ps.DataFrame({
...     'sales': [3, 2, 3, 9, 10, 6],
...     'signups': [5, 5, 6, 12, 14, 13],
...     'visits': [20, 42, 28, 62, 81, 50],
... }, index=pd.date_range(start='2018/01/01', end='2018/07/01',
...                        freq='ME'))
>>> df.sales.plot.area()  

```


For DataFrame

```
>>> df = ps.DataFrame({
...     'sales': [3, 2, 3, 9, 10, 6],
...     'signups': [5, 5, 6, 12, 14, 13],
...     'visits': [20, 42, 28, 62, 81, 50],
... }, index=pd.date_range(start='2018/01/01', end='2018/07/01',
...                        freq='ME'))
>>> df.plot.area()  

```



# pyspark.pandas.Series.plot.bar — PySpark 4.0.1 documentation
plot.bar(_x\=None_, _y\=None_, _\*\*kwds_)
[#](#pyspark.pandas.Series.plot.bar "Permalink to this definition")

Vertical bar plot.

A bar plot is a plot that presents categorical data with rectangular bars with lengths proportional to the values that they represent. A bar plot shows comparisons among discrete categories. One axis of the plot shows the specific categories being compared, and the other axis represents a measured value.

Parameters

**x**label or position, optional

Allows plotting of one column versus another. If not specified, the index of the DataFrame is used.

**y**label or position, optional

Allows plotting of one column versus another. If not specified, all numerical columns are used.

**\*\*kwds**optional

Additional keyword arguments are documented in `pyspark.pandas.Series.plot()` or `pyspark.pandas.DataFrame.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

Basic plot.

For Series:

```
>>> s = ps.Series([1, 3, 2])
>>> s.plot.bar()  

```


For DataFrame:

```
>>> df = ps.DataFrame({'lab': ['A', 'B', 'C'], 'val': [10, 30, 20]})
>>> df.plot.bar(x='lab', y='val')  

```


Plot a whole dataframe to a bar plot. Each column is stacked with a distinct color along the horizontal axis.

```
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> df.plot.bar()  

```


Instead of stacking, the figure can be split by column with plotly APIs.

```
>>> from plotly.subplots import make_subplots
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> fig = (make_subplots(rows=2, cols=1)
...        .add_trace(df.plot.bar(y='speed').data[0], row=1, col=1)
...        .add_trace(df.plot.bar(y='speed').data[0], row=1, col=1)
...        .add_trace(df.plot.bar(y='lifespan').data[0], row=2, col=1))
>>> fig  

```


Plot a single column.

```
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> df.plot.bar(y='speed')  

```


Plot only selected categories for the DataFrame.

```
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> df.plot.bar(x='lifespan')  

```


# pyspark.pandas.Series.plot.barh — PySpark 4.0.1 documentation
plot.barh(_x\=None_, _y\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.plot.barh "Permalink to this definition")

Make a horizontal bar plot.

A horizontal bar plot is a plot that presents quantitative data with rectangular bars with lengths proportional to the values that they represent. A bar plot shows comparisons among discrete categories. One axis of the plot shows the specific categories being compared, and the other axis represents a measured value.

Parameters

**x**label or position, default All numeric columns in dataframe

Columns to be plotted from the DataFrame.

**y**label or position, default DataFrame.index

Column to be used for categories.

**\*\*kwds**

Keyword arguments to pass on to `pyspark.pandas.DataFrame.plot()` or `pyspark.pandas.Series.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

See also

`plotly.express.bar`

Plot a vertical bar plot using plotly.

`matplotlib.axes.Axes.bar`

Plot a vertical bar plot using matplotlib.

Notes

In Plotly and Matplotlib, the interpretation of x and y for barh plots differs. In Plotly, x refers to the values and y refers to the categories. In Matplotlib, x refers to the categories and y refers to the values. Ensure correct axis labeling based on the backend used.

Examples

For Series:

```
>>> df = ps.DataFrame({'lab': ['A', 'B', 'C'], 'val': [10, 30, 20]})
>>> df.val.plot.barh()  

```


For DataFrame:

```
>>> df = ps.DataFrame({'lab': ['A', 'B', 'C'], 'val': [10, 30, 20]})
>>> df.plot.barh(x='lab', y='val')  

```


Plot a whole DataFrame to a horizontal bar plot

```
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> df.plot.barh()  

```


Plot a column of the DataFrame to a horizontal bar plot

```
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> df.plot.barh(y='speed')  

```


Plot DataFrame versus the desired column

```
>>> speed = [0.1, 17.5, 40, 48, 52, 69, 88]
>>> lifespan = [2, 8, 70, 1.5, 25, 12, 28]
>>> index = ['snail', 'pig', 'elephant',
...          'rabbit', 'giraffe', 'coyote', 'horse']
>>> df = ps.DataFrame({'speed': speed,
...                    'lifespan': lifespan}, index=index)
>>> df.plot.barh(x='lifespan')  

```


# pyspark.pandas.Series.plot.box — PySpark 4.0.1 documentation
plot.box(_\*\*kwds_)
[#](#pyspark.pandas.Series.plot.box "Permalink to this definition")

Make a box plot of the DataFrame columns.

A box plot is a method for graphically depicting groups of numerical data through their quartiles. The box extends from the Q1 to Q3 quartile values of the data, with a line at the median (Q2). The whiskers extend from the edges of box to show the range of the data. The position of the whiskers is set by default to 1.5\*IQR (IQR = Q3 - Q1) from the edges of the box. Outlier points are those past the end of the whiskers.

A consideration when using this chart is that the box and the whiskers can overlap, which is very common when plotting small sets of data.

Parameters

**\*\*kwds**dict, optional

Extra arguments to precision: refer to a float that is used by pandas-on-Spark to compute approximate statistics for building a boxplot. The default value is 0.01. Use smaller values to get more precise statistics. Additional keyword arguments are documented in `pyspark.pandas.Series.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Notes

There are behavior differences between pandas-on-Spark and pandas.

*   pandas-on-Spark computes approximate statistics - expect differences between pandas and pandas-on-Spark boxplots, especially regarding 1st and 3rd quartiles.
    
*   The whis argument is only supported as a single number.
    
*   pandas-on-Spark doesn’t support the following argument(s) (matplotlib-only).
    
    *   bootstrap argument is not supported
        
    *   autorange argument is not supported
        

Examples

Draw a box plot from a DataFrame with four columns of randomly generated data.

For Series:

```
>>> data = np.random.randn(25, 4)
>>> df = ps.DataFrame(data, columns=list('ABCD'))
>>> df['A'].plot.box()  

```


This is an unsupported function for DataFrame type



# pyspark.pandas.Series.plot.density — PySpark 4.0.1 documentation
plot.density(_bw\_method\=None_, _ind\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.plot.density "Permalink to this definition")

Generate Kernel Density Estimate plot using Gaussian kernels.

In statistics, kernel density estimation (KDE) is a non-parametric way to estimate the probability density function (PDF) of a random variable. This function uses Gaussian kernels and includes automatic bandwidth determination.

Parameters

**bw\_method**scalar

The method used to calculate the estimator bandwidth. See KernelDensity in PySpark for more information.

**ind**NumPy array or integer, optional

Evaluation points for the estimated PDF. If None (default), 1000 equally spaced points are used. If ind is a NumPy array, the KDE is evaluated at the points passed. If ind is an integer, ind number of equally spaced points are used.

**\*\*kwargs**optional

Keyword arguments to pass on to `pandas-on-Spark.Series.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

A scalar bandwidth should be specified. Using a small bandwidth value can lead to over-fitting, while using a large bandwidth value may result in under-fitting:

```
>>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(bw_method=0.3, ind=100)  

```


```
>>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(bw_method=3, ind=100)  

```


The ind parameter determines the evaluation points for the plot of the estimated KDF:

```
>>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(ind=[1, 2, 3, 4, 5], bw_method=0.3)  

```


For DataFrame, it works in the same way as Series:

```
>>> df = ps.DataFrame({
...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
... })
>>> df.plot.kde(bw_method=0.3, ind=100)  

```


```
>>> df = ps.DataFrame({
...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
... })
>>> df.plot.kde(bw_method=3, ind=100)  

```


```
>>> df = ps.DataFrame({
...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
... })
>>> df.plot.kde(ind=[1, 2, 3, 4, 5, 6], bw_method=0.3)  

```


# pyspark.pandas.Series.plot.hist — PySpark 4.0.1 documentation
plot.hist(_bins\=10_, _\*\*kwds_)
[#](#pyspark.pandas.Series.plot.hist "Permalink to this definition")

Draw one histogram of the DataFrame’s columns.

A [histogram](https://en.wikipedia.org/wiki/Histogram) is a representation of the distribution of data. This function calls `plotting.backend.plot()`, on each series in the DataFrame, resulting in one histogram per column. This is useful when the DataFrame’s Series are in a similar scale.

Parameters

**bins**integer or sequence, default 10

Number of histogram bins to be used. If an integer is given, bins + 1 bin edges are calculated and returned. If bins is a sequence, it gives bin edges, including left edge of first bin and right edge of last bin. In this case, bins are returned unmodified.

**\*\*kwds**

All other plotting keyword arguments to be passed to plotting backend.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

Basic plot.

For Series:

```
>>> s = ps.Series([1, 3, 2])
>>> s.plot.hist()  

```


For DataFrame:

```
>>> df = pd.DataFrame(
...     np.random.randint(1, 7, 6000),
...     columns=['one'])
>>> df['two'] = df['one'] + np.random.randint(1, 7, 6000)
>>> df = ps.from_pandas(df)
>>> df.plot.hist(bins=12, alpha=0.5)  

```


# pyspark.pandas.Series.plot.kde — PySpark 4.0.1 documentation
plot.kde(_bw\_method\=None_, _ind\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.plot.kde "Permalink to this definition")

Generate Kernel Density Estimate plot using Gaussian kernels.

In statistics, kernel density estimation (KDE) is a non-parametric way to estimate the probability density function (PDF) of a random variable. This function uses Gaussian kernels and includes automatic bandwidth determination.

Parameters

**bw\_method**scalar

The method used to calculate the estimator bandwidth. See KernelDensity in PySpark for more information.

**ind**NumPy array or integer, optional

Evaluation points for the estimated PDF. If None (default), 1000 equally spaced points are used. If ind is a NumPy array, the KDE is evaluated at the points passed. If ind is an integer, ind number of equally spaced points are used.

**\*\*kwargs**optional

Keyword arguments to pass on to `pandas-on-Spark.Series.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

A scalar bandwidth should be specified. Using a small bandwidth value can lead to over-fitting, while using a large bandwidth value may result in under-fitting:

```
>>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(bw_method=0.3, ind=100)  

```


```
>>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(bw_method=3, ind=100)  

```


The ind parameter determines the evaluation points for the plot of the estimated KDF:

```
>>> s = ps.Series([1, 2, 2.5, 3, 3.5, 4, 5])
>>> s.plot.kde(ind=[1, 2, 3, 4, 5], bw_method=0.3)  

```


For DataFrame, it works in the same way as Series:

```
>>> df = ps.DataFrame({
...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
... })
>>> df.plot.kde(bw_method=0.3, ind=100)  

```


```
>>> df = ps.DataFrame({
...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
... })
>>> df.plot.kde(bw_method=3, ind=100)  

```


```
>>> df = ps.DataFrame({
...     'x': [1, 2, 2.5, 3, 3.5, 4, 5],
...     'y': [4, 4, 4.5, 5, 5.5, 6, 6],
... })
>>> df.plot.kde(ind=[1, 2, 3, 4, 5, 6], bw_method=0.3)  

```

# pyspark.pandas.Series.plot.line — PySpark 4.0.1 documentation
plot.line(_x\=None_, _y\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.plot.line "Permalink to this definition")

Plot DataFrame/Series as lines.

This function is useful to plot lines using DataFrame’s values as coordinates.

Parameters

**x**int or str, optional

Columns to use for the horizontal axis. Either the location or the label of the columns to be used. By default, it will use the DataFrame indices.

**y**int, str, or list of them, optional

The values to be plotted. Either the location or the label of the columns to be used. By default, it will use the remaining DataFrame numeric columns.

**\*\*kwds**

Keyword arguments to pass on to `Series.plot()` or `DataFrame.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

See also

`plotly.express.line`

Plot y versus x as lines and/or markers (plotly).

`matplotlib.pyplot.plot`

Plot y versus x as lines and/or markers (matplotlib).

Examples

Basic plot.

For Series:

```
>>> s = ps.Series([1, 3, 2])
>>> s.plot.line()  

```


For DataFrame:

The following example shows the populations for some animals over the years.

```
>>> df = ps.DataFrame({'pig': [20, 18, 489, 675, 1776],
...                    'horse': [4, 25, 281, 600, 1900]},
...                   index=[1990, 1997, 2003, 2009, 2014])
>>> df.plot.line()  

```


The following example shows the relationship between both populations.

```
>>> df = ps.DataFrame({'pig': [20, 18, 489, 675, 1776],
...                    'horse': [4, 25, 281, 600, 1900]},
...                   index=[1990, 1997, 2003, 2009, 2014])
>>> df.plot.line(x='pig', y='horse')  

```

# pyspark.pandas.Series.plot.pie — PySpark 4.0.1 documentation
plot.pie(_\*\*kwds_)
[#](#pyspark.pandas.Series.plot.pie "Permalink to this definition")

Generate a pie plot.

A pie plot is a proportional representation of the numerical data in a column. This function wraps `plotly.express.pie()` for the specified column.

Parameters

**y**int or label, optional

Label or position of the column to plot. If not provided, `subplots=True` argument must be passed (matplotlib-only).

**\*\*kwds**

Keyword arguments to pass on to `pandas-on-Spark.Series.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

For Series:

```
>>> df = ps.DataFrame({'mass': [0.330, 4.87, 5.97],
...                    'radius': [2439.7, 6051.8, 6378.1]},
...                   index=['Mercury', 'Venus', 'Earth'])
>>> df.mass.plot.pie()  

```


For DataFrame:

```
>>> df = ps.DataFrame({'mass': [0.330, 4.87, 5.97],
...                    'radius': [2439.7, 6051.8, 6378.1]},
...                   index=['Mercury', 'Venus', 'Earth'])
>>> df.plot.pie(y='mass')  

```



# pyspark.pandas.Series.hist — PySpark 4.0.1 documentation
Series.hist(_bins\=10_, _\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.hist)
[#](#pyspark.pandas.Series.hist "Permalink to this definition")

Draw one histogram of the DataFrame’s columns.

A [histogram](https://en.wikipedia.org/wiki/Histogram) is a representation of the distribution of data. This function calls `plotting.backend.plot()`, on each series in the DataFrame, resulting in one histogram per column. This is useful when the DataFrame’s Series are in a similar scale.

Parameters

**bins**integer or sequence, default 10

Number of histogram bins to be used. If an integer is given, bins + 1 bin edges are calculated and returned. If bins is a sequence, it gives bin edges, including left edge of first bin and right edge of last bin. In this case, bins are returned unmodified.

**\*\*kwds**

All other plotting keyword arguments to be passed to plotting backend.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

Examples

Basic plot.

For Series:

```
>>> s = ps.Series([1, 3, 2])
>>> s.plot.hist()  

```


For DataFrame:

```
>>> df = pd.DataFrame(
...     np.random.randint(1, 7, 6000),
...     columns=['one'])
>>> df['two'] = df['one'] + np.random.randint(1, 7, 6000)
>>> df = ps.from_pandas(df)
>>> df.plot.hist(bins=12, alpha=0.5)  

```


# pyspark.pandas.Series.to_pandas — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.to\_pandas

Series.to\_pandas()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_pandas)
[#](#pyspark.pandas.Series.to_pandas "Permalink to this definition")

Return a pandas Series.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory.

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)], columns=['dogs', 'cats'])
>>> df['dogs'].to_pandas()
0    0.2
1    0.0
2    0.6
3    0.2
Name: dogs, dtype: float64

```




# pyspark.pandas.Series.to_numpy — PySpark 4.0.1 documentation
Series.to\_numpy()
[#](#pyspark.pandas.Series.to_numpy "Permalink to this definition")

A NumPy ndarray representing the values in this DataFrame or Series.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driver’s memory.

Returns

numpy.ndarray

Examples

```
>>> ps.DataFrame({"A": [1, 2], "B": [3, 4]}).to_numpy()
array([[1, 3],
       [2, 4]])

```


With heterogeneous data, the lowest common type will have to be used.

```
>>> ps.DataFrame({"A": [1, 2], "B": [3.0, 4.5]}).to_numpy()
array([[1. , 3. ],
       [2. , 4.5]])

```


For a mix of numeric and non-numeric types, the output array will have object dtype.

```
>>> df = ps.DataFrame({"A": [1, 2], "B": [3.0, 4.5], "C": pd.date_range('2000', periods=2)})
>>> df.to_numpy()
array([[1, 3.0, Timestamp('2000-01-01 00:00:00')],
       [2, 4.5, Timestamp('2000-01-02 00:00:00')]], dtype=object)

```


For Series,

```
>>> ps.Series(['a', 'b', 'a']).to_numpy()
array(['a', 'b', 'a'], dtype=object)

```


# pyspark.pandas.Series.to_list — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.to\_list

Series.to\_list()
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_list)
[#](#pyspark.pandas.Series.to_list "Permalink to this definition")

Return a list of the values.

These are each a scalar type, which is a Python scalar (for str, int, float) or a pandas scalar (for Timestamp/Timedelta/Interval/Period)

Note

This method should only be used if the resulting list is expected to be small, as all the data is loaded into the driver’s memory.

# pyspark.pandas.Series.to_string — PySpark 4.0.1 documentation
Series.to\_string(_buf\=None_, _na\_rep\='NaN'_, _float\_format\=None_, _header\=True_, _index\=True_, _length\=False_, _dtype\=False_, _name\=False_, _max\_rows\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_string)
[#](#pyspark.pandas.Series.to_string "Permalink to this definition")

Render a string representation of the Series.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory. If the input is large, set max\_rows parameter.

Parameters

**buf**StringIO-like, optional

buffer to write to

**na\_rep**string, optional

string representation of NAN to use, default ‘NaN’

**float\_format**one-parameter function, optional

formatter function to apply to columns’ elements if they are floats default None

**header**boolean, default True

Add the Series header (index name)

**index**bool, optional

Add index (row) labels, default True

**length**boolean, default False

Add the Series length

**dtype**boolean, default False

Add the Series dtype

**name**boolean, default False

Add the Series name if not None

**max\_rows**int, optional

Maximum number of rows to show before truncating. If None, show all.

Returns

**formatted**string (if not buffer passed)

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)], columns=['dogs', 'cats'])
>>> print(df['dogs'].to_string())
0    0.2
1    0.0
2    0.6
3    0.2

```


```
>>> print(df['dogs'].to_string(max_rows=2))
0    0.2
1    0.0

```


# pyspark.pandas.Series.to_dict — PySpark 4.0.1 documentation
Series.to\_dict(_into=<class 'dict'>_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_dict)
[#](#pyspark.pandas.Series.to_dict "Permalink to this definition")

Convert Series to {label -> value} dict or dict-like object.

Note

This method should only be used if the resulting pandas DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

Parameters

**into**class, default dict

The collections.abc.Mapping subclass to use as the return object. Can be the actual class or an empty instance of the mapping type you want. If you want a collections.defaultdict, you must pass it initialized.

Returns

collections.abc.Mapping

Key-value representation of Series.

Examples

```
>>> s = ps.Series([1, 2, 3, 4])
>>> s_dict = s.to_dict()
>>> sorted(s_dict.items())
[(0, 1), (1, 2), (2, 3), (3, 4)]

```


```
>>> from collections import OrderedDict, defaultdict
>>> s.to_dict(OrderedDict)
OrderedDict(...)

```


```
>>> dd = defaultdict(list)
>>> s.to_dict(dd)  
defaultdict(<class 'list'>, {...})

```


# pyspark.pandas.Series.to_clipboard — PySpark 4.0.1 documentation
Series.to\_clipboard(_excel\=True_, _sep\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_clipboard)
[#](#pyspark.pandas.Series.to_clipboard "Permalink to this definition")

Copy object to the system clipboard.

Write a text representation of object to the system clipboard. This can be pasted into Excel, for example.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

Parameters

**excel**bool, default True

*   True, use the provided separator, writing in a csv format for allowing easy pasting into excel.
    
*   False, write a string representation of the object to the clipboard.
    

**sep**str, default `'\t'`

Field delimiter.

**\*\*kwargs**

These parameters will be passed to DataFrame.to\_csv.

Notes

Requirements for your platform.

> *   Linux : xclip, or xsel (with gtk or PyQt4 modules)
>     
> *   Windows : none
>     
> *   OS X : none
>     

Examples

Copy the contents of a DataFrame to the clipboard.

```
>>> df = ps.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])  
>>> df.to_clipboard(sep=',')  
... # Wrote the following to the system clipboard:
... # ,A,B,C
... # 0,1,2,3
... # 1,4,5,6

```


We can omit the index by passing the keyword index and setting it to false.

```
>>> df.to_clipboard(sep=',', index=False)  
... # Wrote the following to the system clipboard:
... # A,B,C
... # 1,2,3
... # 4,5,6

```


This function also works for Series:

```
>>> df = ps.Series([1, 2, 3, 4, 5, 6, 7], name='x')  
>>> df.to_clipboard(sep=',')  
... # Wrote the following to the system clipboard:
... # 0, 1
... # 1, 2
... # 2, 3
... # 3, 4
... # 4, 5
... # 5, 6
... # 6, 7

```


# pyspark.pandas.Series.to_latex — PySpark 4.0.1 documentation
Series.to\_latex(_buf\=None_, _columns\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _bold\_rows\=False_, _column\_format\=None_, _longtable\=None_, _escape\=None_, _encoding\=None_, _decimal\='.'_, _multicolumn\=None_, _multicolumn\_format\=None_, _multirow\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_latex)
[#](#pyspark.pandas.Series.to_latex "Permalink to this definition")

Render an object to a LaTeX tabular environment table.

Render an object to a tabular environment table. You can splice this into a LaTeX document. Requires usepackage{booktabs}.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory. If the input is large, consider alternative formats.

Parameters

**buf**file descriptor or None

Buffer to write to. If None, the output is returned as a string.

**columns**list of label, optional

The subset of columns to write. Writes all columns by default.

**header**bool or list of str, default True

Write out the column names. If a list of strings is given, it is assumed to be aliases for the column names.

**index**bool, default True

Write row names (index).

**na\_rep**str, default ‘NaN’

Missing data representation.

**formatters**list of functions or dict of {str: function}, optional

Formatter functions to apply to columns’ elements by position or name. The result of each function must be a Unicode string. List must be of length equal to the number of columns.

**float\_format**str, optional

Format string for floating point numbers.

**sparsify**bool, optional

Set to False for a DataFrame with a hierarchical index to print every multiindex key at each row. By default the value will be read from the config module.

**index\_names**bool, default True

Prints the names of the indexes.

**bold\_rows**bool, default False

Make the row labels bold in the output.

**column\_format**str, optional

The columns format as specified in LaTeX table format e.g. ‘rcl’ for 3 columns. By default, ‘l’ will be used for all columns except columns of numbers, which default to ‘r’.

**longtable**bool, optional

By default the value will be read from the pandas config module. Use a longtable environment instead of tabular. Requires adding a usepackage{longtable} to your LaTeX preamble.

**escape**bool, optional

By default the value will be read from the pandas config module. When set to False prevents from escaping latex special characters in column names.

**encoding**str, optional

A string representing the encoding to use in the output file, defaults to ‘ascii’ on Python 2 and ‘utf-8’ on Python 3.

**decimal**str, default ‘.’

Character recognized as decimal separator, e.g. ‘,’ in Europe.

**multicolumn**bool, default True

Use multicolumn to enhance MultiIndex columns. The default will be read from the config module.

**multicolumn\_format**str, default ‘l’

The alignment for multicolumns, similar to column\_format The default will be read from the config module.

**multirow**bool, default False

Use multirow to enhance MultiIndex rows. Requires adding a usepackage{multirow} to your LaTeX preamble. Will print centered labels (instead of top-aligned) across the contained rows, separating groups via clines. The default will be read from the pandas config module.

Returns

str or None

If buf is None, returns the resulting LateX format as a string. Otherwise returns None.

Examples

```
>>> df = ps.DataFrame({'name': ['Raphael', 'Donatello'],
...                    'mask': ['red', 'purple'],
...                    'weapon': ['sai', 'bo staff']},
...                   columns=['name', 'mask', 'weapon'])
>>> print(df.to_latex(index=False))  
\begin{tabular}{lll}
\toprule
      name &    mask &    weapon \\
\midrule
   Raphael &     red &       sai \\
 Donatello &  purple &  bo staff \\
\bottomrule
\end{tabular}

```


# pyspark.pandas.Series.to_markdown — PySpark 4.0.1 documentation
Series.to\_markdown(_buf\=None_, _mode\=None_)
[#](#pyspark.pandas.Series.to_markdown "Permalink to this definition")

Print Series or DataFrame in Markdown-friendly format.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory.

Parameters

**buf: writable buffer, defaults to sys.stdout**

Where to send the output. By default, the output is printed to sys.stdout. Pass a writable buffer if you need to further process the output.

**mode: str, optional**

Mode in which file is opened.

**\*\*kwargs**

These parameters will be passed to tabulate.

Returns

str

Series or DataFrame in Markdown-friendly format.

Notes

Requires the [tabulate](https://pypi.org/project/tabulate) package.

Examples

```
>>> psser = ps.Series(["elk", "pig", "dog", "quetzal"], name="animal")
>>> print(psser.to_markdown())  
|    | animal   |
|---:|:---------|
|  0 | elk      |
|  1 | pig      |
|  2 | dog      |
|  3 | quetzal  |

```


```
>>> psdf = ps.DataFrame(
...     data={"animal_1": ["elk", "pig"], "animal_2": ["dog", "quetzal"]}
... )
>>> print(psdf.to_markdown())  
|    | animal_1   | animal_2   |
|---:|:-----------|:-----------|
|  0 | elk        | dog        |
|  1 | pig        | quetzal    |

```


# pyspark.pandas.Series.to_json — PySpark 4.0.1 documentation
Series.to\_json(_path\=None_, _compression\='uncompressed'_, _num\_files\=None_, _mode\='w'_, _orient\='records'_, _lines\=True_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.Series.to_json "Permalink to this definition")

Convert the object to a JSON string.

Note

pandas-on-Spark to\_json writes files to a path or URI. Unlike pandas’, pandas-on-Spark respects HDFS’s property such as ‘fs.default.name’.

Note

pandas-on-Spark writes JSON files into the directory, path, and writes multiple part-… files in the directory when path is specified. This behavior was inherited from Apache Spark. The number of partitions can be controlled by num\_files. This is deprecated. Use DataFrame.spark.repartition instead.

Note

output JSON format is different from pandas’. It always uses orient=’records’ for its output. This behavior might have to change soon.

Note

Set ignoreNullFields keyword argument to True to omit None or NaN values when writing JSON objects. It works only when path is provided.

Note NaN’s and None will be converted to null and datetime objects will be converted to UNIX timestamps.

Parameters

**path: string, optional**

File path. If not specified, the result is returned as a string.

**lines: bool, default True**

If ‘orient’ is ‘records’ write out line delimited JSON format. Will throw ValueError if incorrect ‘orient’ since others are not list like. It should be always True for now.

**orient: str, default ‘records’**

It should be always ‘records’ for now.

**compression: {‘gzip’, ‘bz2’, ‘xz’, None}**

A string representing the compression to use in the output file, only used when the first argument is a filename. By default, the compression is inferred from the filename.

**num\_files: the number of partitions to be written in \`path\` directory when**

this is a path. This is deprecated. Use DataFrame.spark.repartition instead.

**mode: str**

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols: str or list of str, optional, default None**

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options: keyword arguments for additional options specific to PySpark.**

It is specific to PySpark’s JSON options to pass. Check the options in PySpark’s API documentation for spark.write.json(…). It has a higher priority and overwrites all other options. This parameter only works when path is specified.

Returns

str or None

Examples

```
>>> df = ps.DataFrame([['a', 'b'], ['c', 'd']],
...                   columns=['col 1', 'col 2'])
>>> df.to_json()
'[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]'

```


```
>>> df['col 1'].to_json()
'[{"col 1":"a"},{"col 1":"c"}]'

```


```
>>> df.to_json(path=r'%s/to_json/foo.json' % path, num_files=1)
>>> ps.read_json(
...     path=r'%s/to_json/foo.json' % path
... ).sort_values(by="col 1")
  col 1 col 2
0     a     b
1     c     d

```


```
>>> df['col 1'].to_json(path=r'%s/to_json/foo.json' % path, num_files=1, index_col="index")
>>> ps.read_json(
...     path=r'%s/to_json/foo.json' % path, index_col="index"
... ).sort_values(by="col 1")  
      col 1
index
0         a
1         c

```


# pyspark.pandas.Series.to_csv — PySpark 4.0.1 documentation
Series.to\_csv(_path\=None_, _sep\=','_, _na\_rep\=''_, _columns\=None_, _header\=True_, _quotechar\='"'_, _date\_format\=None_, _escapechar\=None_, _num\_files\=None_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.Series.to_csv "Permalink to this definition")

Write object to a comma-separated values (csv) file.

Note

pandas-on-Spark to\_csv writes files to a path or URI. Unlike pandas’, pandas-on-Spark respects HDFS’s property such as ‘fs.default.name’.

Note

pandas-on-Spark writes CSV files into the directory, path, and writes multiple part-… files in the directory when path is specified. This behavior was inherited from Apache Spark. The number of partitions can be controlled by num\_files. This is deprecated. Use DataFrame.spark.repartition instead.

Parameters

**path: str, default None**

File path. If None is provided the result is returned as a string.

**sep: str, default ‘,’**

String of length 1. Field delimiter for the output file.

**na\_rep: str, default ‘’**

Missing data representation.

**columns: sequence, optional**

Columns to write.

**header: bool or list of str, default True**

Write out the column names. If a list of strings is given it is assumed to be aliases for the column names.

**quotechar: str, default ‘"’**

String of length 1. Character used to quote fields.

**date\_format: str, default None**

Format string for datetime objects.

**escapechar: str, default None**

String of length 1. Character used to escape sep and quotechar when appropriate.

**num\_files: the number of partitions to be written in \`path\` directory when**

this is a path. This is deprecated. Use DataFrame.spark.repartition instead.

**mode: str**

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols: str or list of str, optional, default None**

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options: keyword arguments for additional options specific to PySpark.**

These kwargs are specific to PySpark’s CSV options to pass. Check the options in PySpark’s API documentation for spark.write.csv(…). It has higher priority and overwrites all other options. This parameter only works when path is specified.

Returns

str or None

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df.sort_values(by="date")  
                   date country  code
... 2012-01-31 12:00:00      KR     1
... 2012-02-29 12:00:00      US     2
... 2012-03-31 12:00:00      JP     3

```


```
>>> print(df.to_csv())  
date,country,code
2012-01-31 12:00:00,KR,1
2012-02-29 12:00:00,US,2
2012-03-31 12:00:00,JP,3

```


```
>>> df.cummax().to_csv(path=r'%s/to_csv/foo.csv' % path, num_files=1)
>>> ps.read_csv(
...    path=r'%s/to_csv/foo.csv' % path
... ).sort_values(by="date")  
                   date country  code
... 2012-01-31 12:00:00      KR     1
... 2012-02-29 12:00:00      US     2
... 2012-03-31 12:00:00      US     3

```


In case of Series,

```
>>> print(df.date.to_csv())  
date
2012-01-31 12:00:00
2012-02-29 12:00:00
2012-03-31 12:00:00

```


```
>>> df.date.to_csv(path=r'%s/to_csv/foo.csv' % path, num_files=1)
>>> ps.read_csv(
...     path=r'%s/to_csv/foo.csv' % path
... ).sort_values(by="date")  
                   date
... 2012-01-31 12:00:00
... 2012-02-29 12:00:00
... 2012-03-31 12:00:00

```


You can preserve the index in the roundtrip as below.

```
>>> df.set_index("country", append=True, inplace=True)
>>> df.date.to_csv(
...     path=r'%s/to_csv/bar.csv' % path,
...     num_files=1,
...     index_col=["index1", "index2"])
>>> ps.read_csv(
...     path=r'%s/to_csv/bar.csv' % path, index_col=["index1", "index2"]
... ).sort_values(by="date")  
                             date
index1 index2
...    ...    2012-01-31 12:00:00
...    ...    2012-02-29 12:00:00
...    ...    2012-03-31 12:00:00

```


# pyspark.pandas.Series.to_excel — PySpark 4.0.1 documentation
Series.to\_excel(_excel\_writer_, _sheet\_name\='Sheet1'_, _na\_rep\=''_, _float\_format\=None_, _columns\=None_, _header\=True_, _index\=True_, _index\_label\=None_, _startrow\=0_, _startcol\=0_, _engine\=None_, _merge\_cells\=True_, _inf\_rep\='inf'_, _freeze\_panes\=None_)
[#](#pyspark.pandas.Series.to_excel "Permalink to this definition")

Write object to an Excel sheet.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

To write a single object to an Excel .xlsx file it is only necessary to specify a target file name. To write to multiple sheets it is necessary to create an ExcelWriter object with a target file name, and specify a sheet in the file to write to.

Multiple sheets may be written to by specifying unique sheet\_name. With all data written to the file it is necessary to save the changes. Note that creating an ExcelWriter object with a file name that already exists will result in the contents of the existing file being erased.

Parameters

**excel\_writer: str or ExcelWriter object**

File path or existing ExcelWriter.

**sheet\_name: str, default ‘Sheet1’**

Name of sheet which will contain DataFrame.

**na\_rep: str, default ‘’**

Missing data representation.

**float\_format: str, optional**

Format string for floating point numbers. For example `float_format="%%.2f"` will format 0.1234 to 0.12.

**columns: sequence or list of str, optional**

Columns to write.

**header: bool or list of str, default True**

Write out the column names. If a list of string is given it is assumed to be aliases for the column names.

**index: bool, default True**

Write row names (index).

**index\_label: str or sequence, optional**

Column label for index column(s) if desired. If not specified, and header and index are True, then the index names are used. A sequence should be given if the DataFrame uses MultiIndex.

**startrow: int, default 0**

Upper left cell row to dump data frame.

**startcol: int, default 0**

Upper left cell column to dump data frame.

**engine: str, optional**

Write engine to use, ‘openpyxl’ or ‘xlsxwriter’. You can also set this via the options `io.excel.xlsx.writer`, `io.excel.xls.writer`, and `io.excel.xlsm.writer`.

**merge\_cells: bool, default True**

Write MultiIndex and Hierarchical Rows as merged cells.

**inf\_rep: str, default ‘inf’**

Representation for infinity (there is no native representation for infinity in Excel).

**freeze\_panes: tuple of int (length 2), optional**

Specifies the one-based bottommost row and rightmost column that is to be frozen.

Notes

Once a workbook has been saved it is not possible write further data without rewriting the whole workbook.

Examples

Create, write to, and save a workbook:

```
>>> df1 = ps.DataFrame([['a', 'b'], ['c', 'd']],
...                    index=['row 1', 'row 2'],
...                    columns=['col 1', 'col 2'])
>>> df1.to_excel("output.xlsx")  

```


To specify the sheet name:

```
>>> df1.to_excel("output.xlsx")  
>>> df1.to_excel("output.xlsx",
...              sheet_name='Sheet_name_1')  

```


If you wish to write to more than one sheet in the workbook, it is necessary to specify an ExcelWriter object:

```
>>> with pd.ExcelWriter('output.xlsx') as writer:  
...      df1.to_excel(writer, sheet_name='Sheet_name_1')
...      df2.to_excel(writer, sheet_name='Sheet_name_2')

```


To set the library that is used to write the Excel file, you can pass the engine keyword (the default engine is automatically chosen depending on the file extension):

```
>>> df1.to_excel('output1.xlsx', engine='xlsxwriter')  

```


# pyspark.pandas.Series.to_hdf — PySpark 4.0.1 documentation
Series.to\_hdf(_path\_or\_buf_, _key_, _mode\='a'_, _complevel\=None_, _complib\=None_, _append\=False_, _format\=None_, _index\=True_, _min\_itemsize\=None_, _nan\_rep\=None_, _dropna\=None_, _data\_columns\=None_, _errors\='strict'_, _encoding\='UTF-8'_)
[#](#pyspark.pandas.Series.to_hdf "Permalink to this definition")

Write the contained data to an HDF5 file using HDFStore.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

New in version 4.0.0.

Parameters

**path\_or\_buf**str or pandas.HDFStore

File path or HDFStore object.

**key**str

Identifier for the group in the store.

**mode**{‘a’, ‘w’, ‘r+’}, default ‘a’

Mode to open file:

*   ‘w’: write, a new file is created (an existing file with the same name would be deleted).
    
*   ‘a’: append, an existing file is opened for reading and writing, and if the file does not exist it is created.
    
*   ‘r+’: similar to ‘a’, but the file must already exist.
    

**complevel**{0-9}, default None

Specifies a compression level for data. A value of 0 or None disables compression.

**complib**{‘zlib’, ‘lzo’, ‘bzip2’, ‘blosc’}, default ‘zlib’

Specifies the compression library to be used. These additional compressors for Blosc are supported (default if no compressor specified: ‘blosc:blosclz’): {‘blosc:blosclz’, ‘blosc:lz4’, ‘blosc:lz4hc’, ‘blosc:snappy’, ‘blosc:zlib’, ‘blosc:zstd’}. Specifying a compression library which is not available issues a ValueError.

**append**bool, default False

For Table formats, append the input data to the existing.

**format**{‘fixed’, ‘table’, None}, default ‘fixed’

Possible values:

*   ‘fixed’: Fixed format. Fast writing/reading. Not-appendable, nor searchable.
    
*   ‘table’: Table format. Write as a PyTables Table structure which may perform worse but allow more flexible operations like searching / selecting subsets of the data.
    
*   If None, pd.get\_option(‘io.hdf.default\_format’) is checked, followed by fallback to “fixed”.
    

**index**bool, default True

Write DataFrame index as a column.

**min\_itemsize**dict or int, optional

Map column names to minimum string sizes for columns.

**nan\_rep**Any, optional

How to represent null values as str. Not allowed with append=True.

**dropna**bool, default False, optional

Remove missing values.

**data\_columns**list of columns or True, optional

List of columns to create as indexed data columns for on-disk queries, or True to use all columns. By default only the axes of the object are indexed. Applicable only to format=’table’.

**errors**str, default ‘strict’

Specifies how encoding and decoding errors are to be handled. See the errors argument for `open()` for a full list of options.

**encoding**str, default “UTF-8”

Examples

```
>>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]},
...                   index=['a', 'b', 'c'])  
>>> df.to_hdf('data.h5', key='df', mode='w')  

```


We can add another object to the same file:

```
>>> s = ps.Series([1, 2, 3, 4])  
>>> s.to_hdf('data.h5', key='s')  

```


# pyspark.pandas.Series.to_frame — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Series](../series.html)
*   pyspark.pandas.Series.to\_frame

Series.to\_frame(_name\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/series.html#Series.to_frame)
[#](#pyspark.pandas.Series.to_frame "Permalink to this definition")

Convert Series to DataFrame.

Parameters

**name**object, default None

The passed name should substitute for the series name (if it has one).

Returns

DataFrame

DataFrame representation of Series.

Examples

```
>>> s = ps.Series(["a", "b", "c"])
>>> s.to_frame()
   0
0  a
1  b
2  c

```


```
>>> s = ps.Series(["a", "b", "c"], name="vals")
>>> s.to_frame()
  vals
0    a
1    b
2    c

```


# pyspark.pandas.Series.pandas_on_spark.transform_batch — PySpark 4.0.1 documentation
pandas\_on\_spark.transform\_batch(_func_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.Series.pandas_on_spark.transform_batch "Permalink to this definition")

Transform the data with the function that takes pandas Series and outputs pandas Series. The pandas Series given to the function is of a batch used internally.

See also [Transform and apply a function](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/transform_apply.html).

Note

the func is unable to access the whole input series. pandas-on-Spark internally splits the input series into multiple batches and calls func with each batch multiple times. Therefore, operations such as global aggregations are impossible. See the example below.

```
>>> # This case does not return the length of whole frame but of the batch internally
... # used.
... def length(pser) -> ps.Series[int]:
...     return pd.Series([len(pser)] * len(pser))
...
>>> df = ps.DataFrame({'A': range(1000)})
>>> df.A.pandas_on_spark.transform_batch(length)  
    c0
0   83
1   83
2   83
...

```


Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def plus_one(x) -> ps.Series[int]:
...     return x + 1

```


Parameters

**func**function

Function to apply to each pandas frame.

**\*args**

Positional arguments to pass to func.

**\*\*kwargs**

Keyword arguments to pass to func.

Returns

DataFrame

See also

`DataFrame.pandas_on_spark.apply_batch`

Similar but it takes pandas DataFrame as its internal batch.

Examples

```
>>> df = ps.DataFrame([(1, 2), (3, 4), (5, 6)], columns=['A', 'B'])
>>> df
   A  B
0  1  2
1  3  4
2  5  6

```


```
>>> def plus_one_func(pser) -> ps.Series[np.int64]:
...     return pser + 1
>>> df.A.pandas_on_spark.transform_batch(plus_one_func)
0    2
1    4
2    6
Name: A, dtype: int64

```


You can also omit the type hints so pandas-on-Spark infers the return schema as below:

```
>>> df.A.pandas_on_spark.transform_batch(lambda pser: pser + 1)
0    2
1    4
2    6
Name: A, dtype: int64

```


You can also specify extra arguments.

```
>>> def plus_one_func(pser, a, b, c=3) -> ps.Series[np.int64]:
...     return pser + a + b + c
>>> df.A.pandas_on_spark.transform_batch(plus_one_func, 1, b=2)
0     7
1     9
2    11
Name: A, dtype: int64

```


You can also use `np.ufunc` and built-in functions as input.

```
>>> df.A.pandas_on_spark.transform_batch(np.add, 10)
0    11
1    13
2    15
Name: A, dtype: int64

```


```
>>> (df * -1).A.pandas_on_spark.transform_batch(abs)
0    1
1    3
2    5
Name: A, dtype: int64

```
