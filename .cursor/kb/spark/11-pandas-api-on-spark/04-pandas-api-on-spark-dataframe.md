# DataFrame — PySpark 4.0.1 documentation
Constructor[#](#constructor "Permalink to this headline")
---------------------------------------------------------



Attributes and underlying data[#](#attributes-and-underlying-data "Permalink to this headline")
-----------------------------------------------------------------------------------------------


|DataFrame.index                              |The index (row labels) Column of the DataFrame.|
|---------------------------------------------|-----------------------------------------------|
|DataFrame.info([verbose, buf, max_cols, ...])|Print a concise summary of a DataFrame.        |
|DataFrame.columns                            |The column labels of the DataFrame.            |
|DataFrame.empty                              |Returns true if the current DataFrame is empty.|




* DataFrame.dtypes: DataFrame.shape
  * Return the dtypes in the DataFrame.: Return a tuple representing the dimensionality of the DataFrame.
* DataFrame.dtypes: DataFrame.axes
  * Return the dtypes in the DataFrame.: Return a list representing the axes of the DataFrame.
* DataFrame.dtypes: DataFrame.ndim
  * Return the dtypes in the DataFrame.: Return an int representing the number of array dimensions.
* DataFrame.dtypes: DataFrame.size
  * Return the dtypes in the DataFrame.: Return an int representing the number of elements in this object.
* DataFrame.dtypes: DataFrame.select_dtypes([include, exclude])
  * Return the dtypes in the DataFrame.: Return a subset of the DataFrame's columns based on the column dtypes.
* DataFrame.dtypes: DataFrame.values
  * Return the dtypes in the DataFrame.: Return a Numpy representation of the DataFrame or the Series.


Conversion[#](#conversion "Permalink to this headline")
-------------------------------------------------------


|DataFrame.copy([deep]) |Make a copy of this object's indices and data.                |
|-----------------------|--------------------------------------------------------------|
|DataFrame.isna()       |Detects missing values for items in the current Dataframe.    |
|DataFrame.astype(dtype)|Cast a pandas-on-Spark object to a specified dtype dtype.     |
|DataFrame.isnull()     |Detects missing values for items in the current Dataframe.    |
|DataFrame.notna()      |Detects non-missing values for items in the current Dataframe.|
|DataFrame.notnull()    |Detects non-missing values for items in the current Dataframe.|
|DataFrame.bool()       |Return the bool of a single element in the current object.    |


Indexing, iteration[#](#indexing-iteration "Permalink to this headline")
------------------------------------------------------------------------



* DataFrame.at: DataFrame.iat
  * Access a single value for a row/column label pair.: Access a single value for a row/column pair by integer position.
* DataFrame.at: DataFrame.head([n])
  * Access a single value for a row/column label pair.: Return the first n rows.
* DataFrame.at: DataFrame.idxmax([axis])
  * Access a single value for a row/column label pair.: Return index of first occurrence of maximum over requested axis.
* DataFrame.at: DataFrame.idxmin([axis])
  * Access a single value for a row/column label pair.: Return index of first occurrence of minimum over requested axis.
* DataFrame.at: DataFrame.loc
  * Access a single value for a row/column label pair.: Access a group of rows and columns by label(s) or a boolean Series.
* DataFrame.at: DataFrame.iloc
  * Access a single value for a row/column label pair.: Purely integer-location based indexing for selection by position.
* DataFrame.at: DataFrame.insert(loc, column, value[, ...])
  * Access a single value for a row/column label pair.: Insert column into DataFrame at specified location.
* DataFrame.at: DataFrame.items()
  * Access a single value for a row/column label pair.: Iterator over (column name, Series) pairs.
* DataFrame.at: DataFrame.iterrows()
  * Access a single value for a row/column label pair.: Iterate over DataFrame rows as (index, Series) pairs.
* DataFrame.at: DataFrame.itertuples([index, name])
  * Access a single value for a row/column label pair.: Iterate over DataFrame rows as namedtuples.
* DataFrame.at: DataFrame.keys()
  * Access a single value for a row/column label pair.: Return alias for columns.
* DataFrame.at: DataFrame.pop(item)
  * Access a single value for a row/column label pair.: Return item and drop from frame.
* DataFrame.at: DataFrame.tail([n])
  * Access a single value for a row/column label pair.: Return the last n rows.
* DataFrame.at: DataFrame.xs(key[, axis, level])
  * Access a single value for a row/column label pair.: Return cross-section from the DataFrame.
* DataFrame.at: DataFrame.get(key[, default])
  * Access a single value for a row/column label pair.: Get item from object for given key (DataFrame column, Panel slice, etc.).
* DataFrame.at: DataFrame.where(cond[, other, axis])
  * Access a single value for a row/column label pair.: Replace values where the condition is False.
* DataFrame.at: DataFrame.mask(cond[, other])
  * Access a single value for a row/column label pair.: Replace values where the condition is True.
* DataFrame.at: DataFrame.query(expr[, inplace])
  * Access a single value for a row/column label pair.: Query the columns of a DataFrame with a boolean expression.


Binary operator functions[#](#binary-operator-functions "Permalink to this headline")
-------------------------------------------------------------------------------------



* DataFrame.add(other): DataFrame.radd(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Addition of dataframe and other, element-wise (binary operator +).
* DataFrame.add(other): DataFrame.div(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Floating division of dataframe and other, element-wise (binary operator /).
* DataFrame.add(other): DataFrame.rdiv(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Floating division of dataframe and other, element-wise (binary operator /).
* DataFrame.add(other): DataFrame.truediv(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Floating division of dataframe and other, element-wise (binary operator /).
* DataFrame.add(other): DataFrame.rtruediv(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Floating division of dataframe and other, element-wise (binary operator /).
* DataFrame.add(other): DataFrame.mul(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Multiplication of dataframe and other, element-wise (binary operator *).
* DataFrame.add(other): DataFrame.rmul(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Multiplication of dataframe and other, element-wise (binary operator *).
* DataFrame.add(other): DataFrame.sub(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Subtraction of dataframe and other, element-wise (binary operator -).
* DataFrame.add(other): DataFrame.rsub(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Subtraction of dataframe and other, element-wise (binary operator -).
* DataFrame.add(other): DataFrame.pow(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Exponential power of series of dataframe and other, element-wise (binary operator **).
* DataFrame.add(other): DataFrame.rpow(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Exponential power of dataframe and other, element-wise (binary operator **).
* DataFrame.add(other): DataFrame.mod(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Modulo of dataframe and other, element-wise (binary operator %).
* DataFrame.add(other): DataFrame.rmod(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Modulo of dataframe and other, element-wise (binary operator %).
* DataFrame.add(other): DataFrame.floordiv(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Integer division of dataframe and other, element-wise (binary operator //).
* DataFrame.add(other): DataFrame.rfloordiv(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Get Integer division of dataframe and other, element-wise (binary operator //).
* DataFrame.add(other): DataFrame.lt(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compare if the current value is less than the other.
* DataFrame.add(other): DataFrame.gt(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compare if the current value is greater than the other.
* DataFrame.add(other): DataFrame.le(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compare if the current value is less than or equal to the other.
* DataFrame.add(other): DataFrame.ge(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compare if the current value is greater than or equal to the other.
* DataFrame.add(other): DataFrame.ne(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compare if the current value is not equal to the other.
* DataFrame.add(other): DataFrame.eq(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compare if the current value is equal to the other.
* DataFrame.add(other): DataFrame.dot(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Compute the matrix multiplication between the DataFrame and others.
* DataFrame.add(other): DataFrame.combine_first(other)
  * Get Addition of dataframe and other, element-wise (binary operator +).: Update null elements with value in the same location in other.


Function application, GroupBy & Window[#](#function-application-groupby-window "Permalink to this headline")
------------------------------------------------------------------------------------------------------------



* DataFrame.apply(func[, axis, args]): DataFrame.applymap(func)
  * Apply a function along an axis of the DataFrame.: Apply a function to a Dataframe elementwise.
* DataFrame.apply(func[, axis, args]): DataFrame.map(func)
  * Apply a function along an axis of the DataFrame.: Apply a function to a Dataframe elementwise.
* DataFrame.apply(func[, axis, args]): DataFrame.pipe(func, *args, **kwargs)
  * Apply a function along an axis of the DataFrame.: Apply func(self, *args, **kwargs).
* DataFrame.apply(func[, axis, args]): DataFrame.agg(func)
  * Apply a function along an axis of the DataFrame.: Aggregate using one or more operations over the specified axis.
* DataFrame.apply(func[, axis, args]): DataFrame.aggregate(func)
  * Apply a function along an axis of the DataFrame.: Aggregate using one or more operations over the specified axis.
* DataFrame.apply(func[, axis, args]): DataFrame.groupby(by[, axis, as_index, dropna])
  * Apply a function along an axis of the DataFrame.: Group DataFrame or Series using one or more columns.
* DataFrame.apply(func[, axis, args]): DataFrame.rolling(window[, min_periods])
  * Apply a function along an axis of the DataFrame.: Provide rolling transformations.
* DataFrame.apply(func[, axis, args]): DataFrame.expanding([min_periods])
  * Apply a function along an axis of the DataFrame.: Provide expanding transformations.
* DataFrame.apply(func[, axis, args]): DataFrame.transform(func[, axis])
  * Apply a function along an axis of the DataFrame.: Call func on self producing a Series with transformed values and that has the same length as its input.


Computations / Descriptive Stats[#](#computations-descriptive-stats "Permalink to this headline")
-------------------------------------------------------------------------------------------------



* DataFrame.abs(): DataFrame.all([axis, bool_only, skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return whether all elements are True.
* DataFrame.abs(): DataFrame.any([axis, bool_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return whether any element is True.
* DataFrame.abs(): DataFrame.clip([lower, upper])
  * Return a Series/DataFrame with absolute numeric value of each element.: Trim values at input threshold(s).
* DataFrame.abs(): DataFrame.corr([method, min_periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute pairwise correlation of columns, excluding NA/null values.
* DataFrame.abs(): DataFrame.corrwith(other[, axis, drop, method])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute pairwise correlation.
* DataFrame.abs(): DataFrame.count([axis, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Count non-NA cells for each column.
* DataFrame.abs(): DataFrame.cov([min_periods, ddof])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute pairwise covariance of columns, excluding NA/null values.
* DataFrame.abs(): DataFrame.describe([percentiles])
  * Return a Series/DataFrame with absolute numeric value of each element.: Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding NaN values.
* DataFrame.abs(): DataFrame.ewm([com, span, halflife, alpha, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Provide exponentially weighted window transformations.
* DataFrame.abs(): DataFrame.kurt([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
* DataFrame.abs(): DataFrame.kurtosis([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
* DataFrame.abs(): DataFrame.max([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the maximum of the values.
* DataFrame.abs(): DataFrame.mean([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the mean of the values.
* DataFrame.abs(): DataFrame.min([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the minimum of the values.
* DataFrame.abs(): DataFrame.median([axis, skipna, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the median of the values for the requested axis.
* DataFrame.abs(): DataFrame.mode([axis, numeric_only, dropna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Get the mode(s) of each element along the selected axis.
* DataFrame.abs(): DataFrame.pct_change([periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Percentage change between the current and a prior element.
* DataFrame.abs(): DataFrame.prod([axis, skipna, numeric_only, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the product of the values.
* DataFrame.abs(): DataFrame.product([axis, skipna, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the product of the values.
* DataFrame.abs(): DataFrame.quantile([q, axis, numeric_only, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return value at the given quantile.
* DataFrame.abs(): DataFrame.rank([method, ascending, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute numerical data ranks (1 through n) along axis.
* DataFrame.abs(): DataFrame.nunique([axis, dropna, approx, rsd])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return number of unique elements in the object.
* DataFrame.abs(): DataFrame.sem([axis, skipna, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased standard error of the mean over requested axis.
* DataFrame.abs(): DataFrame.skew([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased skew normalized by N-1.
* DataFrame.abs(): DataFrame.sum([axis, skipna, numeric_only, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the sum of the values.
* DataFrame.abs(): DataFrame.std([axis, skipna, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return sample standard deviation.
* DataFrame.abs(): DataFrame.var([axis, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased variance.
* DataFrame.abs(): DataFrame.cummin([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative minimum over a DataFrame or Series axis.
* DataFrame.abs(): DataFrame.cummax([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative maximum over a DataFrame or Series axis.
* DataFrame.abs(): DataFrame.cumsum([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative sum over a DataFrame or Series axis.
* DataFrame.abs(): DataFrame.cumprod([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative product over a DataFrame or Series axis.
* DataFrame.abs(): DataFrame.round([decimals])
  * Return a Series/DataFrame with absolute numeric value of each element.: Round a DataFrame to a variable number of decimal places.
* DataFrame.abs(): DataFrame.diff([periods, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: First discrete difference of element.
* DataFrame.abs(): DataFrame.eval(expr[, inplace])
  * Return a Series/DataFrame with absolute numeric value of each element.: Evaluate a string describing operations on DataFrame columns.


Reindexing / Selection / Label manipulation[#](#reindexing-selection-label-manipulation "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------------



* DataFrame.add_prefix(prefix): DataFrame.add_suffix(suffix)
  * Prefix labels with string prefix.: Suffix labels with string suffix.
* DataFrame.add_prefix(prefix): DataFrame.align(other[, join, axis, copy])
  * Prefix labels with string prefix.: Align two objects on their axes with the specified join method.
* DataFrame.add_prefix(prefix): DataFrame.at_time(time[, asof, axis])
  * Prefix labels with string prefix.: Select values at particular time of day (example: 9:30AM).
* DataFrame.add_prefix(prefix): DataFrame.between_time(start_time, end_time)
  * Prefix labels with string prefix.: Select values between particular times of the day (example: 9:00-9:30 AM).
* DataFrame.add_prefix(prefix): DataFrame.drop([labels, axis, index, columns])
  * Prefix labels with string prefix.: Drop specified labels from columns.
* DataFrame.add_prefix(prefix): DataFrame.droplevel(level[, axis])
  * Prefix labels with string prefix.: Return DataFrame with requested index / column level(s) removed.
* DataFrame.add_prefix(prefix): DataFrame.drop_duplicates([subset, keep, ...])
  * Prefix labels with string prefix.: Return DataFrame with duplicate rows removed, optionally only considering certain columns.
* DataFrame.add_prefix(prefix): DataFrame.duplicated([subset, keep])
  * Prefix labels with string prefix.: Return boolean Series denoting duplicate rows, optionally only considering certain columns.
* DataFrame.add_prefix(prefix): DataFrame.equals(other)
  * Prefix labels with string prefix.: Compare if the current value is equal to the other.
* DataFrame.add_prefix(prefix): DataFrame.filter([items, like, regex, axis])
  * Prefix labels with string prefix.: Subset rows or columns of dataframe according to labels in the specified index.
* DataFrame.add_prefix(prefix): DataFrame.first(offset)
  * Prefix labels with string prefix.: Select first periods of time series data based on a date offset.
* DataFrame.add_prefix(prefix): DataFrame.head([n])
  * Prefix labels with string prefix.: Return the first n rows.
* DataFrame.add_prefix(prefix): DataFrame.last(offset)
  * Prefix labels with string prefix.: Select final periods of time series data based on a date offset.
* DataFrame.add_prefix(prefix): DataFrame.reindex([labels, index, columns, ...])
  * Prefix labels with string prefix.: Conform DataFrame to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.
* DataFrame.add_prefix(prefix): DataFrame.reindex_like(other[, copy])
  * Prefix labels with string prefix.: Return a DataFrame with matching indices as other object.
* DataFrame.add_prefix(prefix): DataFrame.rename([mapper, index, columns, ...])
  * Prefix labels with string prefix.: Alter axes labels.
* DataFrame.add_prefix(prefix): DataFrame.rename_axis([mapper, index, ...])
  * Prefix labels with string prefix.: Set the name of the axis for the index or columns.
* DataFrame.add_prefix(prefix): DataFrame.reset_index([level, drop, ...])
  * Prefix labels with string prefix.: Reset the index, or a level of it.
* DataFrame.add_prefix(prefix): DataFrame.set_index(keys[, drop, append, ...])
  * Prefix labels with string prefix.: Set the DataFrame index (row labels) using one or more existing columns.
* DataFrame.add_prefix(prefix): DataFrame.swapaxes(i, j[, copy])
  * Prefix labels with string prefix.: Interchange axes and swap values axes appropriately.
* DataFrame.add_prefix(prefix): DataFrame.swaplevel([i, j, axis])
  * Prefix labels with string prefix.: Swap levels i and j in a MultiIndex on a particular axis.
* DataFrame.add_prefix(prefix): DataFrame.take(indices[, axis])
  * Prefix labels with string prefix.: Return the elements in the given positional indices along an axis.
* DataFrame.add_prefix(prefix): DataFrame.isin(values)
  * Prefix labels with string prefix.: Whether each element in the DataFrame is contained in values.
* DataFrame.add_prefix(prefix): DataFrame.sample([n, frac, replace, ...])
  * Prefix labels with string prefix.: Return a random sample of items from an axis of object.
* DataFrame.add_prefix(prefix): DataFrame.truncate([before, after, axis, copy])
  * Prefix labels with string prefix.: Truncate a Series or DataFrame before and after some index value.


Missing data handling[#](#missing-data-handling "Permalink to this headline")
-----------------------------------------------------------------------------



* DataFrame.backfill([axis, inplace, limit]): DataFrame.dropna([axis, how, thresh, ...])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Remove missing values.
* DataFrame.backfill([axis, inplace, limit]): DataFrame.fillna([value, method, axis, ...])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Fill NA/NaN values.
* DataFrame.backfill([axis, inplace, limit]): DataFrame.replace([to_replace, value, ...])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Returns a new DataFrame replacing a value with another value.
* DataFrame.backfill([axis, inplace, limit]): DataFrame.bfill([axis, inplace, limit])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.
* DataFrame.backfill([axis, inplace, limit]): DataFrame.ffill([axis, inplace, limit])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Synonym for DataFrame.fillna() or Series.fillna() with method=`ffill`.
* DataFrame.backfill([axis, inplace, limit]): DataFrame.interpolate([method, limit, ...])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Fill NaN values using an interpolation method.
* DataFrame.backfill([axis, inplace, limit]): DataFrame.pad([axis, inplace, limit])
  * Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.: Synonym for DataFrame.fillna() or Series.fillna() with method=`ffill`.


Reshaping, sorting, transposing[#](#reshaping-sorting-transposing "Permalink to this headline")
-----------------------------------------------------------------------------------------------



* DataFrame.pivot_table([values, index, ...]): DataFrame.pivot([index, columns, values])
  * Create a spreadsheet-style pivot table as a DataFrame.: Return reshaped DataFrame organized by given index / column values.
* DataFrame.pivot_table([values, index, ...]): DataFrame.sort_index([axis, level, ...])
  * Create a spreadsheet-style pivot table as a DataFrame.: Sort object by labels (along an axis)
* DataFrame.pivot_table([values, index, ...]): DataFrame.sort_values(by[, ascending, ...])
  * Create a spreadsheet-style pivot table as a DataFrame.: Sort by the values along either axis.
* DataFrame.pivot_table([values, index, ...]): DataFrame.nlargest(n, columns[, keep])
  * Create a spreadsheet-style pivot table as a DataFrame.: Return the first n rows ordered by columns in descending order.
* DataFrame.pivot_table([values, index, ...]): DataFrame.nsmallest(n, columns[, keep])
  * Create a spreadsheet-style pivot table as a DataFrame.: Return the first n rows ordered by columns in ascending order.
* DataFrame.pivot_table([values, index, ...]): DataFrame.stack()
  * Create a spreadsheet-style pivot table as a DataFrame.: Stack the prescribed level(s) from columns to index.
* DataFrame.pivot_table([values, index, ...]): DataFrame.unstack()
  * Create a spreadsheet-style pivot table as a DataFrame.: Pivot the (necessarily hierarchical) index labels.
* DataFrame.pivot_table([values, index, ...]): DataFrame.melt([id_vars, value_vars, ...])
  * Create a spreadsheet-style pivot table as a DataFrame.: Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.
* DataFrame.pivot_table([values, index, ...]): DataFrame.explode(column[, ignore_index])
  * Create a spreadsheet-style pivot table as a DataFrame.: Transform each element of a list-like to a row, replicating index values.
* DataFrame.pivot_table([values, index, ...]): DataFrame.squeeze([axis])
  * Create a spreadsheet-style pivot table as a DataFrame.: Squeeze 1 dimensional axis objects into scalars.
* DataFrame.pivot_table([values, index, ...]): DataFrame.T
  * Create a spreadsheet-style pivot table as a DataFrame.: Transpose index and columns.
* DataFrame.pivot_table([values, index, ...]): DataFrame.transpose()
  * Create a spreadsheet-style pivot table as a DataFrame.: Transpose index and columns.


Combining / joining / merging[#](#combining-joining-merging "Permalink to this headline")
-----------------------------------------------------------------------------------------



* DataFrame.assign(**kwargs): DataFrame.merge(right[, how, on, left_on, ...])
  * Assign new columns to a DataFrame.: Merge DataFrame objects with a database-style join.
* DataFrame.assign(**kwargs): DataFrame.join(right[, on, how, lsuffix, ...])
  * Assign new columns to a DataFrame.: Join columns of another DataFrame.
* DataFrame.assign(**kwargs): DataFrame.update(other[, join, overwrite])
  * Assign new columns to a DataFrame.: Modify in place using non-NA values from another DataFrame.


Serialization / IO / Conversion[#](#serialization-io-conversion "Permalink to this headline")
---------------------------------------------------------------------------------------------



* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.from_records(data[, index, ...])
  * Construct DataFrame from dict of array-like or dicts.: Convert structured or recorded ndarray to DataFrame.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_table(name[, format, mode, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write the DataFrame into a Spark table.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_delta(path[, mode, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write the DataFrame out as a Delta Lake table.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_parquet(path[, mode, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write the DataFrame out as a Parquet file or directory.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_csv([path, sep, na_rep, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write object to a comma-separated values (csv) file.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_orc(path[, mode, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write a DataFrame to the ORC format.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_pandas()
  * Construct DataFrame from dict of array-like or dicts.: Return a pandas DataFrame.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_html([buf, columns, col_space, ...])
  * Construct DataFrame from dict of array-like or dicts.: Render a DataFrame as an HTML table.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_numpy()
  * Construct DataFrame from dict of array-like or dicts.: A NumPy ndarray representing the values in this DataFrame or Series.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_spark([index_col])
  * Construct DataFrame from dict of array-like or dicts.: Spark related features.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_string([buf, columns, ...])
  * Construct DataFrame from dict of array-like or dicts.: Render a DataFrame to a console-friendly tabular output.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_feather(path, **kwargs)
  * Construct DataFrame from dict of array-like or dicts.: Write a DataFrame to the binary Feather format.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_stata(path, *[, convert_dates, ...])
  * Construct DataFrame from dict of array-like or dicts.: Export DataFrame object to Stata dta format.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_json([path, compression, ...])
  * Construct DataFrame from dict of array-like or dicts.: Convert the object to a JSON string.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_dict([orient, into])
  * Construct DataFrame from dict of array-like or dicts.: Convert the DataFrame to a dictionary.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_excel(excel_writer[, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write object to an Excel sheet.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_hdf(path_or_buf, key[, mode, ...])
  * Construct DataFrame from dict of array-like or dicts.: Write the contained data to an HDF5 file using HDFStore.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_clipboard([excel, sep])
  * Construct DataFrame from dict of array-like or dicts.: Copy object to the system clipboard.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_markdown([buf, mode])
  * Construct DataFrame from dict of array-like or dicts.: Print Series or DataFrame in Markdown-friendly format.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_records([index, column_dtypes, ...])
  * Construct DataFrame from dict of array-like or dicts.: Convert DataFrame to a NumPy record array.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.to_latex([buf, columns, header, ...])
  * Construct DataFrame from dict of array-like or dicts.: Render an object to a LaTeX tabular environment table.
* DataFrame.from_dict(data[, orient, dtype, ...]): DataFrame.style
  * Construct DataFrame from dict of array-like or dicts.: Property returning a Styler object containing methods for building a styled HTML representation for the DataFrame.


Plotting[#](#plotting "Permalink to this headline")
---------------------------------------------------

`DataFrame.plot` is both a callable method and a namespace attribute for specific plotting methods of the form `DataFrame.plot.<kind>`.



* DataFrame.plot.area([x, y]): DataFrame.plot.bar([x, y])
  * Draw a stacked area plot.: Vertical bar plot.
* DataFrame.plot.area([x, y]): DataFrame.plot.barh([x, y])
  * Draw a stacked area plot.: Make a horizontal bar plot.
* DataFrame.plot.area([x, y]): DataFrame.plot.box(**kwds)
  * Draw a stacked area plot.: Make a box plot of the DataFrame columns.
* DataFrame.plot.area([x, y]): DataFrame.plot.density([bw_method, ind])
  * Draw a stacked area plot.: Generate Kernel Density Estimate plot using Gaussian kernels.
* DataFrame.plot.area([x, y]): DataFrame.plot.hist([bins])
  * Draw a stacked area plot.: Draw one histogram of the DataFrame’s columns.
* DataFrame.plot.area([x, y]): DataFrame.plot.kde([bw_method, ind])
  * Draw a stacked area plot.: Generate Kernel Density Estimate plot using Gaussian kernels.
* DataFrame.plot.area([x, y]): DataFrame.plot.line([x, y])
  * Draw a stacked area plot.: Plot DataFrame/Series as lines.
* DataFrame.plot.area([x, y]): DataFrame.plot.pie(**kwds)
  * Draw a stacked area plot.: Generate a pie plot.
* DataFrame.plot.area([x, y]): DataFrame.plot.scatter(x, y, **kwds)
  * Draw a stacked area plot.: Create a scatter plot with varying marker point size and color.



|DataFrame.hist([bins])         |Draw one histogram of the DataFrame’s columns.               |
|-------------------------------|-------------------------------------------------------------|
|DataFrame.boxplot(**kwds)      |Make a box plot of the DataFrame columns.                    |
|DataFrame.kde([bw_method, ind])|Generate Kernel Density Estimate plot using Gaussian kernels.|


Pandas-on-Spark specific[#](#pandas-on-spark-specific "Permalink to this headline")
-----------------------------------------------------------------------------------

`DataFrame.pandas_on_spark` provides pandas-on-Spark specific features that exists only in pandas API on Spark. These can be accessed by `DataFrame.pandas_on_spark.<function/property>`.



* DataFrame.pandas_on_spark.apply_batch(func): DataFrame.pandas_on_spark.transform_batch(...)
  * Apply a function that takes pandas DataFrame and outputs pandas DataFrame.: Transform chunks with a function that takes pandas DataFrame and outputs pandas DataFrame.


# pyspark.pandas.DataFrame — PySpark 4.0.1 documentation
pandas-on-Spark DataFrame that corresponds to pandas DataFrame logically. This holds Spark DataFrame internally.

Variables

**\_internal** – an internal immutable Frame to manage metadata.

Parameters

**data**numpy ndarray (structured or homogeneous), dict, pandas DataFrame,

Spark DataFrame, pandas-on-Spark DataFrame or pandas-on-Spark Series. Dict can contain Series, arrays, constants, or list-like objects

**index**Index or array-like

Index to use for the resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided

**columns**Index or array-like

Column labels to use for the resulting frame. Will default to RangeIndex (0, 1, 2, …, n) if no column labels are provided

**dtype**dtype, default None

Data type to force. Only a single dtype is allowed. If None, infer

**copy**boolean, default False

Copy data from inputs. Only affects DataFrame / 2d ndarray input

**.. versionchanged:: 3.4.0**

Since 3.4.0, it deals with data and index in this approach: 1, when data is a distributed dataset (Internal DataFrame/Spark DataFrame/ pandas-on-Spark DataFrame/pandas-on-Spark Series), it will first parallelize the index if necessary, and then try to combine the data and index; Note that if data and index doesn’t have the same anchor, then compute.ops\_on\_diff\_frames should be turned on; 2, when data is a local dataset (Pandas DataFrame/numpy ndarray/list/etc), it will first collect the index to driver if necessary, and then apply the pandas.DataFrame(…) creation internally;

Examples

Constructing DataFrame from a dictionary.

```
>>> d = {'col1': [1, 2], 'col2': [3, 4]}
>>> df = ps.DataFrame(data=d, columns=['col1', 'col2'])
>>> df
   col1  col2
0     1     3
1     2     4

```


Constructing DataFrame from pandas DataFrame

```
>>> df = ps.DataFrame(pd.DataFrame(data=d, columns=['col1', 'col2']))
>>> df
   col1  col2
0     1     3
1     2     4

```


Notice that the inferred dtype is int64.

```
>>> df.dtypes
col1    int64
col2    int64
dtype: object

```


To enforce a single dtype:

```
>>> df = ps.DataFrame(data=d, dtype=np.int8)
>>> df.dtypes
col1    int8
col2    int8
dtype: object

```


Constructing DataFrame from numpy ndarray:

```
>>> import numpy as np
>>> ps.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
...     columns=['a', 'b', 'c', 'd', 'e'])
   a  b  c  d  e
0  1  2  3  4  5
1  6  7  8  9  0

```


Constructing DataFrame from numpy ndarray with Pandas index:

```
>>> import numpy as np
>>> import pandas as pd

```


```
>>> ps.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
...     index=pd.Index([1, 4]), columns=['a', 'b', 'c', 'd', 'e'])
   a  b  c  d  e
1  1  2  3  4  5
4  6  7  8  9  0

```


Constructing DataFrame from numpy ndarray with pandas-on-Spark index:

```
>>> import numpy as np
>>> import pandas as pd
>>> ps.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
...     index=ps.Index([1, 4]), columns=['a', 'b', 'c', 'd', 'e'])
   a  b  c  d  e
1  1  2  3  4  5
4  6  7  8  9  0

```


Constructing DataFrame from Pandas DataFrame with Pandas index:

```
>>> import numpy as np
>>> import pandas as pd
>>> pdf = pd.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
...     columns=['a', 'b', 'c', 'd', 'e'])
>>> ps.DataFrame(data=pdf, index=pd.Index([1, 4]))
     a    b    c    d    e
1  6.0  7.0  8.0  9.0  0.0
4  NaN  NaN  NaN  NaN  NaN

```


Constructing DataFrame from Pandas DataFrame with pandas-on-Spark index:

```
>>> import numpy as np
>>> import pandas as pd
>>> pdf = pd.DataFrame(data=np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 0]]),
...     columns=['a', 'b', 'c', 'd', 'e'])
>>> ps.DataFrame(data=pdf, index=ps.Index([1, 4]))
     a    b    c    d    e
1  6.0  7.0  8.0  9.0  0.0
4  NaN  NaN  NaN  NaN  NaN

```


Constructing DataFrame from Spark DataFrame with Pandas index:

```
>>> import pandas as pd
>>> sdf = spark.createDataFrame([("Data", 1), ("Bricks", 2)], ["x", "y"])
>>> with ps.option_context("compute.ops_on_diff_frames", False):
...     ps.DataFrame(data=sdf, index=pd.Index([0, 1, 2]))
Traceback (most recent call last):
  ...
ValueError: Cannot combine the series or dataframe...'compute.ops_on_diff_frames' option.

```


Enable ‘compute.ops\_on\_diff\_frames’ to combine SparkDataFrame and Pandas index

```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     ps.DataFrame(data=sdf, index=pd.Index([0, 1, 2]))
        x    y
0    Data  1.0
1  Bricks  2.0
2    None  NaN

```


Constructing DataFrame from Spark DataFrame with pandas-on-Spark index:

```
>>> import pandas as pd
>>> sdf = spark.createDataFrame([("Data", 1), ("Bricks", 2)], ["x", "y"])
>>> with ps.option_context("compute.ops_on_diff_frames", False):
...     ps.DataFrame(data=sdf, index=ps.Index([0, 1, 2]))
Traceback (most recent call last):
  ...
ValueError: Cannot combine the series or dataframe...'compute.ops_on_diff_frames' option.

```


Enable ‘compute.ops\_on\_diff\_frames’ to combine Spark DataFrame and pandas-on-Spark index

```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     ps.DataFrame(data=sdf, index=ps.Index([0, 1, 2]))
        x    y
0    Data  1.0
1  Bricks  2.0
2    None  NaN

```


Methods



* abs(): add(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Addition of dataframe and other, element-wise (binary operator +).
* abs(): add_prefix(prefix)
  * Return a Series/DataFrame with absolute numeric value of each element.: Prefix labels with string prefix.
* abs(): add_suffix(suffix)
  * Return a Series/DataFrame with absolute numeric value of each element.: Suffix labels with string suffix.
* abs(): agg(func)
  * Return a Series/DataFrame with absolute numeric value of each element.: Aggregate using one or more operations over the specified axis.
* abs(): aggregate(func)
  * Return a Series/DataFrame with absolute numeric value of each element.: Aggregate using one or more operations over the specified axis.
* abs(): align(other[, join, axis, copy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Align two objects on their axes with the specified join method.
* abs(): all([axis, bool_only, skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return whether all elements are True.
* abs(): any([axis, bool_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return whether any element is True.
* abs(): apply(func[, axis, args])
  * Return a Series/DataFrame with absolute numeric value of each element.: Apply a function along an axis of the DataFrame.
* abs(): applymap(func)
  * Return a Series/DataFrame with absolute numeric value of each element.: Apply a function to a Dataframe elementwise.
* abs(): assign(**kwargs)
  * Return a Series/DataFrame with absolute numeric value of each element.: Assign new columns to a DataFrame.
* abs(): astype(dtype)
  * Return a Series/DataFrame with absolute numeric value of each element.: Cast a pandas-on-Spark object to a specified dtype dtype.
* abs(): at_time(time[, asof, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Select values at particular time of day (example: 9:30AM).
* abs(): backfill([axis, inplace, limit])
  * Return a Series/DataFrame with absolute numeric value of each element.: Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.
* abs(): between_time(start_time, end_time[, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Select values between particular times of the day (example: 9:00-9:30 AM).
* abs(): bfill([axis, inplace, limit])
  * Return a Series/DataFrame with absolute numeric value of each element.: Synonym for DataFrame.fillna() or Series.fillna() with method=`bfill`.
* abs(): bool()
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the bool of a single element in the current object.
* abs(): boxplot(**kwds)
  * Return a Series/DataFrame with absolute numeric value of each element.: Make a box plot of the DataFrame columns.
* abs(): clip([lower, upper])
  * Return a Series/DataFrame with absolute numeric value of each element.: Trim values at input threshold(s).
* abs(): combine_first(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Update null elements with value in the same location in other.
* abs(): copy([deep])
  * Return a Series/DataFrame with absolute numeric value of each element.: Make a copy of this object's indices and data.
* abs(): corr([method, min_periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute pairwise correlation of columns, excluding NA/null values.
* abs(): corrwith(other[, axis, drop, method])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute pairwise correlation.
* abs(): count([axis, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Count non-NA cells for each column.
* abs(): cov([min_periods, ddof])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute pairwise covariance of columns, excluding NA/null values.
* abs(): cummax([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative maximum over a DataFrame or Series axis.
* abs(): cummin([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative minimum over a DataFrame or Series axis.
* abs(): cumprod([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative product over a DataFrame or Series axis.
* abs(): cumsum([skipna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cumulative sum over a DataFrame or Series axis.
* abs(): describe([percentiles])
  * Return a Series/DataFrame with absolute numeric value of each element.: Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding NaN values.
* abs(): diff([periods, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: First discrete difference of element.
* abs(): div(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Floating division of dataframe and other, element-wise (binary operator /).
* abs(): divide(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Floating division of dataframe and other, element-wise (binary operator /).
* abs(): dot(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute the matrix multiplication between the DataFrame and others.
* abs(): drop([labels, axis, index, columns])
  * Return a Series/DataFrame with absolute numeric value of each element.: Drop specified labels from columns.
* abs(): drop_duplicates([subset, keep, inplace, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return DataFrame with duplicate rows removed, optionally only considering certain columns.
* abs(): droplevel(level[, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return DataFrame with requested index / column level(s) removed.
* abs(): dropna([axis, how, thresh, subset, inplace])
  * Return a Series/DataFrame with absolute numeric value of each element.: Remove missing values.
* abs(): duplicated([subset, keep])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return boolean Series denoting duplicate rows, optionally only considering certain columns.
* abs(): eq(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is equal to the other.
* abs(): equals(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is equal to the other.
* abs(): eval(expr[, inplace])
  * Return a Series/DataFrame with absolute numeric value of each element.: Evaluate a string describing operations on DataFrame columns.
* abs(): ewm([com, span, halflife, alpha, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Provide exponentially weighted window transformations.
* abs(): expanding([min_periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Provide expanding transformations.
* abs(): explode(column[, ignore_index])
  * Return a Series/DataFrame with absolute numeric value of each element.: Transform each element of a list-like to a row, replicating index values.
* abs(): ffill([axis, inplace, limit])
  * Return a Series/DataFrame with absolute numeric value of each element.: Synonym for DataFrame.fillna() or Series.fillna() with method=`ffill`.
* abs(): fillna([value, method, axis, inplace, limit])
  * Return a Series/DataFrame with absolute numeric value of each element.: Fill NA/NaN values.
* abs(): filter([items, like, regex, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Subset rows or columns of dataframe according to labels in the specified index.
* abs(): first(offset)
  * Return a Series/DataFrame with absolute numeric value of each element.: Select first periods of time series data based on a date offset.
* abs(): first_valid_index()
  * Return a Series/DataFrame with absolute numeric value of each element.: Retrieves the index of the first valid value.
* abs(): floordiv(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Integer division of dataframe and other, element-wise (binary operator //).
* abs(): from_dict(data[, orient, dtype, columns])
  * Return a Series/DataFrame with absolute numeric value of each element.: Construct DataFrame from dict of array-like or dicts.
* abs(): from_records(data[, index, exclude, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Convert structured or recorded ndarray to DataFrame.
* abs(): ge(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is greater than or equal to the other.
* abs(): get(key[, default])
  * Return a Series/DataFrame with absolute numeric value of each element.: Get item from object for given key (DataFrame column, Panel slice, etc.).
* abs(): groupby(by[, axis, as_index, dropna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Group DataFrame or Series using one or more columns.
* abs(): gt(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is greater than the other.
* abs(): head([n])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the first n rows.
* abs(): hist([bins])
  * Return a Series/DataFrame with absolute numeric value of each element.: Draw one histogram of the DataFrame’s columns.
* abs(): idxmax([axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return index of first occurrence of maximum over requested axis.
* abs(): idxmin([axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return index of first occurrence of minimum over requested axis.
* abs(): info([verbose, buf, max_cols, show_counts])
  * Return a Series/DataFrame with absolute numeric value of each element.: Print a concise summary of a DataFrame.
* abs(): insert(loc, column, value[, allow_duplicates])
  * Return a Series/DataFrame with absolute numeric value of each element.: Insert column into DataFrame at specified location.
* abs(): interpolate([method, limit, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Fill NaN values using an interpolation method.
* abs(): isin(values)
  * Return a Series/DataFrame with absolute numeric value of each element.: Whether each element in the DataFrame is contained in values.
* abs(): isna()
  * Return a Series/DataFrame with absolute numeric value of each element.: Detects missing values for items in the current Dataframe.
* abs(): isnull()
  * Return a Series/DataFrame with absolute numeric value of each element.: Detects missing values for items in the current Dataframe.
* abs(): items()
  * Return a Series/DataFrame with absolute numeric value of each element.: Iterator over (column name, Series) pairs.
* abs(): iterrows()
  * Return a Series/DataFrame with absolute numeric value of each element.: Iterate over DataFrame rows as (index, Series) pairs.
* abs(): itertuples([index, name])
  * Return a Series/DataFrame with absolute numeric value of each element.: Iterate over DataFrame rows as namedtuples.
* abs(): join(right[, on, how, lsuffix, rsuffix])
  * Return a Series/DataFrame with absolute numeric value of each element.: Join columns of another DataFrame.
* abs(): kde([bw_method, ind])
  * Return a Series/DataFrame with absolute numeric value of each element.: Generate Kernel Density Estimate plot using Gaussian kernels.
* abs(): keys()
  * Return a Series/DataFrame with absolute numeric value of each element.: Return alias for columns.
* abs(): kurt([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
* abs(): kurtosis([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased kurtosis using Fisher’s definition of kurtosis (kurtosis of normal == 0.0).
* abs(): last(offset)
  * Return a Series/DataFrame with absolute numeric value of each element.: Select final periods of time series data based on a date offset.
* abs(): last_valid_index()
  * Return a Series/DataFrame with absolute numeric value of each element.: Return index for last non-NA/null value.
* abs(): le(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is less than or equal to the other.
* abs(): lt(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is less than the other.
* abs(): map(func)
  * Return a Series/DataFrame with absolute numeric value of each element.: Apply a function to a Dataframe elementwise.
* abs(): mask(cond[, other])
  * Return a Series/DataFrame with absolute numeric value of each element.: Replace values where the condition is True.
* abs(): max([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the maximum of the values.
* abs(): mean([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the mean of the values.
* abs(): median([axis, skipna, numeric_only, accuracy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the median of the values for the requested axis.
* abs(): melt([id_vars, value_vars, var_name, value_name])
  * Return a Series/DataFrame with absolute numeric value of each element.: Unpivot a DataFrame from wide format to long format, optionally leaving identifier variables set.
* abs(): merge(right[, how, on, left_on, right_on, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Merge DataFrame objects with a database-style join.
* abs(): min([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the minimum of the values.
* abs(): mod(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Modulo of dataframe and other, element-wise (binary operator %).
* abs(): mode([axis, numeric_only, dropna])
  * Return a Series/DataFrame with absolute numeric value of each element.: Get the mode(s) of each element along the selected axis.
* abs(): mul(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Multiplication of dataframe and other, element-wise (binary operator *).
* abs(): multiply(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Multiplication of dataframe and other, element-wise (binary operator *).
* abs(): ne(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Compare if the current value is not equal to the other.
* abs(): nlargest(n, columns[, keep])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the first n rows ordered by columns in descending order.
* abs(): notna()
  * Return a Series/DataFrame with absolute numeric value of each element.: Detects non-missing values for items in the current Dataframe.
* abs(): notnull()
  * Return a Series/DataFrame with absolute numeric value of each element.: Detects non-missing values for items in the current Dataframe.
* abs(): nsmallest(n, columns[, keep])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the first n rows ordered by columns in ascending order.
* abs(): nunique([axis, dropna, approx, rsd])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return number of unique elements in the object.
* abs(): pad([axis, inplace, limit])
  * Return a Series/DataFrame with absolute numeric value of each element.: Synonym for DataFrame.fillna() or Series.fillna() with method=`ffill`.
* abs(): pct_change([periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Percentage change between the current and a prior element.
* abs(): pipe(func, *args, **kwargs)
  * Return a Series/DataFrame with absolute numeric value of each element.: Apply func(self, *args, **kwargs).
* abs(): pivot([index, columns, values])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return reshaped DataFrame organized by given index / column values.
* abs(): pivot_table([values, index, columns, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Create a spreadsheet-style pivot table as a DataFrame.
* abs(): pop(item)
  * Return a Series/DataFrame with absolute numeric value of each element.: Return item and drop from frame.
* abs(): pow(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Exponential power of series of dataframe and other, element-wise (binary operator **).
* abs(): prod([axis, skipna, numeric_only, min_count])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the product of the values.
* abs(): product([axis, skipna, numeric_only, min_count])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the product of the values.
* abs(): quantile([q, axis, numeric_only, accuracy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return value at the given quantile.
* abs(): query(expr[, inplace])
  * Return a Series/DataFrame with absolute numeric value of each element.: Query the columns of a DataFrame with a boolean expression.
* abs(): radd(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Addition of dataframe and other, element-wise (binary operator +).
* abs(): rank([method, ascending, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Compute numerical data ranks (1 through n) along axis.
* abs(): rdiv(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Floating division of dataframe and other, element-wise (binary operator /).
* abs(): reindex([labels, index, columns, axis, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Conform DataFrame to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index.
* abs(): reindex_like(other[, copy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return a DataFrame with matching indices as other object.
* abs(): rename([mapper, index, columns, axis, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Alter axes labels.
* abs(): rename_axis([mapper, index, columns, axis, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Set the name of the axis for the index or columns.
* abs(): replace([to_replace, value, inplace, limit, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Returns a new DataFrame replacing a value with another value.
* abs(): resample(rule[, closed, label, on])
  * Return a Series/DataFrame with absolute numeric value of each element.: Resample time-series data.
* abs(): reset_index([level, drop, inplace, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Reset the index, or a level of it.
* abs(): rfloordiv(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Integer division of dataframe and other, element-wise (binary operator //).
* abs(): rmod(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Modulo of dataframe and other, element-wise (binary operator %).
* abs(): rmul(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Multiplication of dataframe and other, element-wise (binary operator *).
* abs(): rolling(window[, min_periods])
  * Return a Series/DataFrame with absolute numeric value of each element.: Provide rolling transformations.
* abs(): round([decimals])
  * Return a Series/DataFrame with absolute numeric value of each element.: Round a DataFrame to a variable number of decimal places.
* abs(): rpow(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Exponential power of dataframe and other, element-wise (binary operator **).
* abs(): rsub(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Subtraction of dataframe and other, element-wise (binary operator -).
* abs(): rtruediv(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Floating division of dataframe and other, element-wise (binary operator /).
* abs(): sample([n, frac, replace, random_state, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return a random sample of items from an axis of object.
* abs(): select_dtypes([include, exclude])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return a subset of the DataFrame's columns based on the column dtypes.
* abs(): sem([axis, skipna, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased standard error of the mean over requested axis.
* abs(): set_index(keys[, drop, append, inplace])
  * Return a Series/DataFrame with absolute numeric value of each element.: Set the DataFrame index (row labels) using one or more existing columns.
* abs(): shift([periods, fill_value])
  * Return a Series/DataFrame with absolute numeric value of each element.: Shift DataFrame by desired number of periods.
* abs(): skew([axis, skipna, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased skew normalized by N-1.
* abs(): sort_index([axis, level, ascending, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Sort object by labels (along an axis)
* abs(): sort_values(by[, ascending, inplace, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Sort by the values along either axis.
* abs(): squeeze([axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Squeeze 1 dimensional axis objects into scalars.
* abs(): stack()
  * Return a Series/DataFrame with absolute numeric value of each element.: Stack the prescribed level(s) from columns to index.
* abs(): std([axis, skipna, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return sample standard deviation.
* abs(): sub(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Subtraction of dataframe and other, element-wise (binary operator -).
* abs(): subtract(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Subtraction of dataframe and other, element-wise (binary operator -).
* abs(): sum([axis, skipna, numeric_only, min_count])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the sum of the values.
* abs(): swapaxes(i, j[, copy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Interchange axes and swap values axes appropriately.
* abs(): swaplevel([i, j, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Swap levels i and j in a MultiIndex on a particular axis.
* abs(): tail([n])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the last n rows.
* abs(): take(indices[, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return the elements in the given positional indices along an axis.
* abs(): to_clipboard([excel, sep])
  * Return a Series/DataFrame with absolute numeric value of each element.: Copy object to the system clipboard.
* abs(): to_csv([path, sep, na_rep, columns, header, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write object to a comma-separated values (csv) file.
* abs(): to_delta(path[, mode, partition_cols, index_col])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write the DataFrame out as a Delta Lake table.
* abs(): to_dict([orient, into])
  * Return a Series/DataFrame with absolute numeric value of each element.: Convert the DataFrame to a dictionary.
* abs(): to_excel(excel_writer[, sheet_name, na_rep, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write object to an Excel sheet.
* abs(): to_feather(path, **kwargs)
  * Return a Series/DataFrame with absolute numeric value of each element.: Write a DataFrame to the binary Feather format.
* abs(): to_hdf(path_or_buf, key[, mode, complevel, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write the contained data to an HDF5 file using HDFStore.
* abs(): to_html([buf, columns, col_space, header, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Render a DataFrame as an HTML table.
* abs(): to_json([path, compression, num_files, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Convert the object to a JSON string.
* abs(): to_latex([buf, columns, header, index, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Render an object to a LaTeX tabular environment table.
* abs(): to_markdown([buf, mode])
  * Return a Series/DataFrame with absolute numeric value of each element.: Print Series or DataFrame in Markdown-friendly format.
* abs(): to_numpy()
  * Return a Series/DataFrame with absolute numeric value of each element.: A NumPy ndarray representing the values in this DataFrame or Series.
* abs(): to_orc(path[, mode, partition_cols, index_col])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write a DataFrame to the ORC format.
* abs(): to_pandas()
  * Return a Series/DataFrame with absolute numeric value of each element.: Return a pandas DataFrame.
* abs(): to_parquet(path[, mode, partition_cols, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write the DataFrame out as a Parquet file or directory.
* abs(): to_records([index, column_dtypes, index_dtypes])
  * Return a Series/DataFrame with absolute numeric value of each element.: Convert DataFrame to a NumPy record array.
* abs(): to_spark([index_col])
  * Return a Series/DataFrame with absolute numeric value of each element.: Spark related features.
* abs(): to_stata(path, *[, convert_dates, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Export DataFrame object to Stata dta format.
* abs(): to_string([buf, columns, col_space, header, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Render a DataFrame to a console-friendly tabular output.
* abs(): to_table(name[, format, mode, ...])
  * Return a Series/DataFrame with absolute numeric value of each element.: Write the DataFrame into a Spark table.
* abs(): transform(func[, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Call func on self producing a Series with transformed values and that has the same length as its input.
* abs(): transpose()
  * Return a Series/DataFrame with absolute numeric value of each element.: Transpose index and columns.
* abs(): truediv(other)
  * Return a Series/DataFrame with absolute numeric value of each element.: Get Floating division of dataframe and other, element-wise (binary operator /).
* abs(): truncate([before, after, axis, copy])
  * Return a Series/DataFrame with absolute numeric value of each element.: Truncate a Series or DataFrame before and after some index value.
* abs(): unstack()
  * Return a Series/DataFrame with absolute numeric value of each element.: Pivot the (necessarily hierarchical) index labels.
* abs(): update(other[, join, overwrite])
  * Return a Series/DataFrame with absolute numeric value of each element.: Modify in place using non-NA values from another DataFrame.
* abs(): var([axis, ddof, numeric_only])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return unbiased variance.
* abs(): where(cond[, other, axis])
  * Return a Series/DataFrame with absolute numeric value of each element.: Replace values where the condition is False.
* abs(): xs(key[, axis, level])
  * Return a Series/DataFrame with absolute numeric value of each element.: Return cross-section from the DataFrame.


Attributes



* T: at
  * Transpose index and columns.: Access a single value for a row/column label pair.
* T: axes
  * Transpose index and columns.: Return a list representing the axes of the DataFrame.
* T: columns
  * Transpose index and columns.: The column labels of the DataFrame.
* T: dtypes
  * Transpose index and columns.: Return the dtypes in the DataFrame.
* T: empty
  * Transpose index and columns.: Returns true if the current DataFrame is empty.
* T: iat
  * Transpose index and columns.: Access a single value for a row/column pair by integer position.
* T: iloc
  * Transpose index and columns.: Purely integer-location based indexing for selection by position.
* T: index
  * Transpose index and columns.: The index (row labels) Column of the DataFrame.
* T: loc
  * Transpose index and columns.: Access a group of rows and columns by label(s) or a boolean Series.
* T: ndim
  * Transpose index and columns.: Return an int representing the number of array dimensions.
* T: shape
  * Transpose index and columns.: Return a tuple representing the dimensionality of the DataFrame.
* T: size
  * Transpose index and columns.: Return an int representing the number of elements in this object.
* T: style
  * Transpose index and columns.: Property returning a Styler object containing methods for building a styled HTML representation for the DataFrame.
* T: values
  * Transpose index and columns.: Return a Numpy representation of the DataFrame or the Series.


# pyspark.pandas.DataFrame.index — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.index

_property_ DataFrame.index[#](#pyspark.pandas.DataFrame.index "Permalink to this definition")

The index (row labels) Column of the DataFrame.

Currently not supported when the DataFrame has no index.

# pyspark.pandas.DataFrame.info — PySpark 4.0.1 documentation
DataFrame.info(_verbose\=None_, _buf\=None_, _max\_cols\=None_, _show\_counts\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.info)
[#](#pyspark.pandas.DataFrame.info "Permalink to this definition")

Print a concise summary of a DataFrame.

This method prints information about a DataFrame including the index dtype and column dtypes, non-null values and memory usage.

Parameters

**verbose**bool, optional

Whether to print the full summary.

**buf**writable buffer, defaults to sys.stdout

Where to send the output. By default the output is printed to sys.stdout. Pass a writable buffer if you need to further process the output.

**max\_cols**int, optional

When to switch from the verbose to the truncated output. If the DataFrame has more than max\_cols columns, the truncated output is used.

**show\_counts**bool, optional

Whether to show the non-null counts.

New in version 4.0.0.

Returns

None

This method prints a summary of a DataFrame and returns None.

Examples

```
>>> int_values = [1, 2, 3, 4, 5]
>>> text_values = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']
>>> float_values = [0.0, 0.25, 0.5, 0.75, 1.0]
>>> df = ps.DataFrame(
...     {"int_col": int_values, "text_col": text_values, "float_col": float_values},
...     columns=['int_col', 'text_col', 'float_col'])
>>> df
   int_col text_col  float_col
0        1    alpha       0.00
1        2     beta       0.25
2        3    gamma       0.50
3        4    delta       0.75
4        5  epsilon       1.00

```


Prints information of all columns:

```
>>> df.info(verbose=True)  
<class 'pyspark.pandas.frame.DataFrame'>
Index: 5 entries, 0 to 4
Data columns (total 3 columns):
 #   Column     Non-Null Count  Dtype
---  ------     --------------  -----
 0   int_col    5 non-null      int64
 1   text_col   5 non-null      object
 2   float_col  5 non-null      float64
dtypes: float64(1), int64(1), object(1)

```


Prints a summary of columns count and its dtypes but not per column information:

```
>>> df.info(verbose=False)  
<class 'pyspark.pandas.frame.DataFrame'>
Index: 5 entries, 0 to 4
Columns: 3 entries, int_col to float_col
dtypes: float64(1), int64(1), object(1)

```


Pipe output of DataFrame.info to buffer instead of sys.stdout, get buffer content and writes to a text file:

```
>>> import io
>>> buffer = io.StringIO()
>>> df.info(buf=buffer)
>>> s = buffer.getvalue()
>>> with open('%s/info.txt' % path, "w",
...           encoding="utf-8") as f:
...     _ = f.write(s)
>>> with open('%s/info.txt' % path) as f:
...     f.readlines()  
["<class 'pyspark.pandas.frame.DataFrame'>\n",
'Index: 5 entries, 0 to 4\n',
'Data columns (total 3 columns):\n',
' #   Column     Non-Null Count  Dtype  \n',
'---  ------     --------------  -----  \n',
' 0   int_col    5 non-null      int64  \n',
' 1   text_col   5 non-null      object \n',
' 2   float_col  5 non-null      float64\n',
'dtypes: float64(1), int64(1), object(1)']

```


# pyspark.pandas.DataFrame.columns — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.columns

_property_ DataFrame.columns[#](#pyspark.pandas.DataFrame.columns "Permalink to this definition")

The column labels of the DataFrame.

# pyspark.pandas.DataFrame.empty — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.empty

_property_ DataFrame.empty[#](#pyspark.pandas.DataFrame.empty "Permalink to this definition")

Returns true if the current DataFrame is empty. Otherwise, returns false.

Examples

```
>>> ps.range(10).empty
False

```


```
>>> ps.range(0).empty
True

```


```
>>> ps.DataFrame({}, index=list('abc')).empty
True

```


# pyspark.pandas.DataFrame.dtypes — PySpark 4.0.1 documentation
_property_ DataFrame.dtypes[#](#pyspark.pandas.DataFrame.dtypes "Permalink to this definition")

Return the dtypes in the DataFrame.

This returns a Series with the data type of each column. The result’s index is the original DataFrame’s columns. Columns with mixed types are stored with the object dtype.

Returns

pd.Series

The data type of each column.

Examples

```
>>> df = ps.DataFrame({'a': list('abc'),
...                    'b': list(range(1, 4)),
...                    'c': np.arange(3, 6).astype('i1'),
...                    'd': np.arange(4.0, 7.0, dtype='float64'),
...                    'e': [True, False, True],
...                    'f': pd.date_range('20130101', periods=3)},
...                   columns=['a', 'b', 'c', 'd', 'e', 'f'])
>>> df.dtypes
a            object
b             int64
c              int8
d           float64
e              bool
f    datetime64[ns]
dtype: object

```


# pyspark.pandas.DataFrame.shape — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.shape

_property_ DataFrame.shape[#](#pyspark.pandas.DataFrame.shape "Permalink to this definition")

Return a tuple representing the dimensionality of the DataFrame.

Examples

```
>>> df = ps.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
>>> df.shape
(2, 2)

```


```
>>> df = ps.DataFrame({'col1': [1, 2], 'col2': [3, 4],
...                    'col3': [5, 6]})
>>> df.shape
(2, 3)

```

# pyspark.pandas.DataFrame.axes — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.axes

_property_ DataFrame.axes[#](#pyspark.pandas.DataFrame.axes "Permalink to this definition")

Return a list representing the axes of the DataFrame.

It has the row axis labels and column axis labels as the only members. They are returned in that order.

Examples

```
>>> df = ps.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
>>> df.axes
[Index([0, 1], dtype='int64'), Index(['col1', 'col2'], dtype='object')]

```

# pyspark.pandas.DataFrame.ndim — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.ndim

_property_ DataFrame.ndim[#](#pyspark.pandas.DataFrame.ndim "Permalink to this definition")

Return an int representing the number of array dimensions.

return 2 for DataFrame.

Examples

```
>>> df = ps.DataFrame([[1, 2], [4, 5], [7, 8]],
...                   index=['cobra', 'viper', None],
...                   columns=['max_speed', 'shield'])
>>> df  
       max_speed  shield
cobra          1       2
viper          4       5
None           7       8
>>> df.ndim
2

```


# pyspark.pandas.DataFrame.size — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.size

_property_ DataFrame.size[#](#pyspark.pandas.DataFrame.size "Permalink to this definition")

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


# pyspark.pandas.DataFrame.select_dtypes — PySpark 4.0.1 documentation
DataFrame.select\_dtypes(_include\=None_, _exclude\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.select_dtypes)
[#](#pyspark.pandas.DataFrame.select_dtypes "Permalink to this definition")

Return a subset of the DataFrame’s columns based on the column dtypes.

Parameters

**include, exclude**scalar or list-like

A selection of dtypes or strings to be included/excluded. At least one of these parameters must be supplied. It also takes Spark SQL DDL type strings, for instance, ‘string’ and ‘date’.

Returns

DataFrame

The subset of the frame including the dtypes in `include` and excluding the dtypes in `exclude`.

Raises

ValueError

*   If both of `include` and `exclude` are empty
    
    ```
>>> df = ps.DataFrame({'a': [1, 2] * 3,
...                    'b': [True, False] * 3,
...                    'c': [1.0, 2.0] * 3})
>>> df.select_dtypes()
Traceback (most recent call last):
...
ValueError: at least one of include or exclude must be nonempty

```

    
*   If `include` and `exclude` have overlapping elements
    
    ```
>>> df = ps.DataFrame({'a': [1, 2] * 3,
...                    'b': [True, False] * 3,
...                    'c': [1.0, 2.0] * 3})
>>> df.select_dtypes(include='a', exclude='a')
Traceback (most recent call last):
...
ValueError: include and exclude overlap on {'a'}

```

    

Notes

*   To select datetimes, use `np.datetime64`, `'datetime'` or `'datetime64'`
    

Examples

```
>>> df = ps.DataFrame({'a': [1, 2] * 3,
...                    'b': [True, False] * 3,
...                    'c': [1.0, 2.0] * 3,
...                    'd': ['a', 'b'] * 3}, columns=['a', 'b', 'c', 'd'])
>>> df
   a      b    c  d
0  1   True  1.0  a
1  2  False  2.0  b
2  1   True  1.0  a
3  2  False  2.0  b
4  1   True  1.0  a
5  2  False  2.0  b

```


```
>>> df.select_dtypes(include='bool')
       b
0   True
1  False
2   True
3  False
4   True
5  False

```


```
>>> df.select_dtypes(include=['float64'], exclude=['int'])
     c
0  1.0
1  2.0
2  1.0
3  2.0
4  1.0
5  2.0

```


```
>>> df.select_dtypes(include=['int'], exclude=['float64'])
   a
0  1
1  2
2  1
3  2
4  1
5  2

```


```
>>> df.select_dtypes(exclude=['int'])
       b    c  d
0   True  1.0  a
1  False  2.0  b
2   True  1.0  a
3  False  2.0  b
4   True  1.0  a
5  False  2.0  b

```


Spark SQL DDL type strings can be used as well.

```
>>> df.select_dtypes(exclude=['string'])
   a      b    c
0  1   True  1.0
1  2  False  2.0
2  1   True  1.0
3  2  False  2.0
4  1   True  1.0
5  2  False  2.0

```


# pyspark.pandas.DataFrame.values — PySpark 4.0.1 documentation
_property_ DataFrame.values[#](#pyspark.pandas.DataFrame.values "Permalink to this definition")

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


# pyspark.pandas.DataFrame.copy — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.copy

DataFrame.copy(_deep\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.copy)
[#](#pyspark.pandas.DataFrame.copy "Permalink to this definition")

Make a copy of this object’s indices and data.

Parameters

**deep**bool, default True

this parameter is not supported but just dummy parameter to match pandas.

Returns

**copy**DataFrame

Examples

```
>>> df = ps.DataFrame({'x': [1, 2], 'y': [3, 4], 'z': [5, 6], 'w': [7, 8]},
...                   columns=['x', 'y', 'z', 'w'])
>>> df
   x  y  z  w
0  1  3  5  7
1  2  4  6  8
>>> df_copy = df.copy()
>>> df_copy
   x  y  z  w
0  1  3  5  7
1  2  4  6  8

```


# pyspark.pandas.DataFrame.isna — PySpark 4.0.1 documentation
DataFrame.isna()
[#](#pyspark.pandas.DataFrame.isna "Permalink to this definition")

Detects missing values for items in the current Dataframe.

Return a boolean same-sized Dataframe indicating if the values are NA. NA values, such as None or numpy.NaN, gets mapped to True values. Everything else gets mapped to False values.

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, None), (.6, None), (.2, .1)])
>>> df.isnull()
       0      1
0  False  False
1  False   True
2  False   True
3  False  False

```


```
>>> df = ps.DataFrame([[None, 'bee', None], ['dog', None, 'fly']])
>>> df.isnull()
       0      1      2
0   True  False   True
1  False   True  False

```


# pyspark.pandas.DataFrame.astype — PySpark 4.0.1 documentation
DataFrame.astype(_dtype_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.astype)
[#](#pyspark.pandas.DataFrame.astype "Permalink to this definition")

Cast a pandas-on-Spark object to a specified dtype `dtype`.

Parameters

**dtype**data type, or dict of column name -> data type

Use a numpy.dtype or Python type to cast entire pandas-on-Spark object to the same type. Alternatively, use {col: dtype, …}, where col is a column label and dtype is a numpy.dtype or Python type to cast one or more of the DataFrame’s columns to column-specific types.

Returns

**casted**same type as caller

Examples

```
>>> df = ps.DataFrame({'a': [1, 2, 3], 'b': [1, 2, 3]}, dtype='int64')
>>> df
   a  b
0  1  1
1  2  2
2  3  3

```


Convert to float type:

```
>>> df.astype('float')
     a    b
0  1.0  1.0
1  2.0  2.0
2  3.0  3.0

```


Convert to int64 type back:

```
>>> df.astype('int64')
   a  b
0  1  1
1  2  2
2  3  3

```


Convert column a to float type:

```
>>> df.astype({'a': float})
     a  b
0  1.0  1
1  2.0  2
2  3.0  3

```


# pyspark.pandas.DataFrame.isnull — PySpark 4.0.1 documentation
DataFrame.isnull()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.isnull)
[#](#pyspark.pandas.DataFrame.isnull "Permalink to this definition")

Detects missing values for items in the current Dataframe.

Return a boolean same-sized Dataframe indicating if the values are NA. NA values, such as None or numpy.NaN, gets mapped to True values. Everything else gets mapped to False values.

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, None), (.6, None), (.2, .1)])
>>> df.isnull()
       0      1
0  False  False
1  False   True
2  False   True
3  False  False

```


```
>>> df = ps.DataFrame([[None, 'bee', None], ['dog', None, 'fly']])
>>> df.isnull()
       0      1      2
0   True  False   True
1  False   True  False

```


# pyspark.pandas.DataFrame.notna — PySpark 4.0.1 documentation
DataFrame.notna()
[#](#pyspark.pandas.DataFrame.notna "Permalink to this definition")

Detects non-missing values for items in the current Dataframe.

This function takes a dataframe and indicates whether it’s values are valid (not missing, which is `NaN` in numeric datatypes, `None` or `NaN` in objects and `NaT` in datetimelike).

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, None), (.6, None), (.2, .1)])
>>> df.notnull()
      0      1
0  True   True
1  True  False
2  True  False
3  True   True

```


```
>>> df = ps.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
>>> df.notnull()
      0      1     2
0  True   True  True
1  True  False  True

```



# pyspark.pandas.DataFrame.notnull — PySpark 4.0.1 documentation
DataFrame.notnull()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.notnull)
[#](#pyspark.pandas.DataFrame.notnull "Permalink to this definition")

Detects non-missing values for items in the current Dataframe.

This function takes a dataframe and indicates whether it’s values are valid (not missing, which is `NaN` in numeric datatypes, `None` or `NaN` in objects and `NaT` in datetimelike).

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, None), (.6, None), (.2, .1)])
>>> df.notnull()
      0      1
0  True   True
1  True  False
2  True  False
3  True   True

```


```
>>> df = ps.DataFrame([['ant', 'bee', 'cat'], ['dog', None, 'fly']])
>>> df.notnull()
      0      1     2
0  True   True  True
1  True  False  True

```


# pyspark.pandas.DataFrame.bool — PySpark 4.0.1 documentation
DataFrame.bool()
[#](#pyspark.pandas.DataFrame.bool "Permalink to this definition")

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


# pyspark.pandas.DataFrame.at — PySpark 4.0.1 documentation
_property_ DataFrame.at[#](#pyspark.pandas.DataFrame.at "Permalink to this definition")

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

# pyspark.pandas.DataFrame.iat — PySpark 4.0.1 documentation
_property_ DataFrame.iat[#](#pyspark.pandas.DataFrame.iat "Permalink to this definition")

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


# pyspark.pandas.DataFrame.head — PySpark 4.0.1 documentation
DataFrame.head(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.head)
[#](#pyspark.pandas.DataFrame.head "Permalink to this definition")

Return the first n rows.

This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.

Parameters

**n**int, default 5

Number of rows to select.

Returns

**obj\_head**same type as caller

The first n rows of the caller object.

Examples

```
>>> df = ps.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

```


Viewing the first 5 lines

```
>>> df.head()
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey

```


Viewing the first n lines (three in this case)

```
>>> df.head(3)
      animal
0  alligator
1        bee
2     falcon

```

# pyspark.pandas.DataFrame.idxmax — PySpark 4.0.1 documentation
DataFrame.idxmax(_axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.idxmax)
[#](#pyspark.pandas.DataFrame.idxmax "Permalink to this definition")

Return index of first occurrence of maximum over requested axis. NA/null values are excluded.

Note

This API collect all rows with maximum value using to\_pandas() because we suppose the number of rows with max values are usually small in general.

Parameters

**axis**0 or ‘index’

Can only be set to 0 now.

Returns

Series

Examples

```
>>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
...                     'b': [4.0, 2.0, 3.0, 1.0],
...                     'c': [300, 200, 400, 200]})
>>> psdf
   a    b    c
0  1  4.0  300
1  2  2.0  200
2  3  3.0  400
3  2  1.0  200

```


```
>>> psdf.idxmax()
a    2
b    0
c    2
dtype: int64

```


For Multi-column Index

```
>>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
...                     'b': [4.0, 2.0, 3.0, 1.0],
...                     'c': [300, 200, 400, 200]})
>>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
>>> psdf
   a    b    c
   x    y    z
0  1  4.0  300
1  2  2.0  200
2  3  3.0  400
3  2  1.0  200

```


```
>>> psdf.idxmax()
a  x    2
b  y    0
c  z    2
dtype: int64

```

# pyspark.pandas.DataFrame.idxmin — PySpark 4.0.1 documentation
DataFrame.idxmin(_axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.idxmin)
[#](#pyspark.pandas.DataFrame.idxmin "Permalink to this definition")

Return index of first occurrence of minimum over requested axis. NA/null values are excluded.

Note

This API collect all rows with minimum value using to\_pandas() because we suppose the number of rows with min values are usually small in general.

Parameters

**axis**0 or ‘index’

Can only be set to 0 now.

Returns

Series

Examples

```
>>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
...                     'b': [4.0, 2.0, 3.0, 1.0],
...                     'c': [300, 200, 400, 200]})
>>> psdf
   a    b    c
0  1  4.0  300
1  2  2.0  200
2  3  3.0  400
3  2  1.0  200

```


```
>>> psdf.idxmin()
a    0
b    3
c    1
dtype: int64

```


For Multi-column Index

```
>>> psdf = ps.DataFrame({'a': [1, 2, 3, 2],
...                     'b': [4.0, 2.0, 3.0, 1.0],
...                     'c': [300, 200, 400, 200]})
>>> psdf.columns = pd.MultiIndex.from_tuples([('a', 'x'), ('b', 'y'), ('c', 'z')])
>>> psdf
   a    b    c
   x    y    z
0  1  4.0  300
1  2  2.0  200
2  3  3.0  400
3  2  1.0  200

```


```
>>> psdf.idxmin()
a  x    0
b  y    3
c  z    1
dtype: int64

```
# pyspark.pandas.DataFrame.loc — PySpark 4.0.1 documentation
_property_ DataFrame.loc[#](#pyspark.pandas.DataFrame.loc "Permalink to this definition")

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

[`Series.loc`](about:blank/pyspark.pandas.Series.loc.html#pyspark.pandas.Series.loc "pyspark.pandas.Series.loc")

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


# pyspark.pandas.DataFrame.iloc — PySpark 4.0.1 documentation
_property_ DataFrame.iloc[#](#pyspark.pandas.DataFrame.iloc "Permalink to this definition")

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

[`Series.iloc`](about:blank/pyspark.pandas.Series.iloc.html#pyspark.pandas.Series.iloc "pyspark.pandas.Series.iloc")

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


# pyspark.pandas.DataFrame.insert — PySpark 4.0.1 documentation
DataFrame.insert(_loc_, _column_, _value_, _allow\_duplicates\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.insert)
[#](#pyspark.pandas.DataFrame.insert "Permalink to this definition")

Insert column into DataFrame at specified location.

Raises a ValueError if column is already contained in the DataFrame, unless allow\_duplicates is set to True.

Parameters

**loc**int

Insertion index. Must verify 0 <= loc <= len(columns).

**column**str, number, or hashable object

Label of the inserted column.

**value**int, Series, or array-like

**allow\_duplicates**bool, optional

Examples

```
>>> psdf = ps.DataFrame([1, 2, 3])
>>> psdf.sort_index()
   0
0  1
1  2
2  3
>>> psdf.insert(0, 'x', 4)
>>> psdf.sort_index()
   x  0
0  4  1
1  4  2
2  4  3

```


```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)

```


```
>>> psdf.insert(1, 'y', [5, 6, 7])
>>> psdf.sort_index()
   x  y  0
0  4  5  1
1  4  6  2
2  4  7  3

```


```
>>> psdf.insert(2, 'z', ps.Series([8, 9, 10]))
>>> psdf.sort_index()
   x  y   z  0
0  4  5   8  1
1  4  6   9  2
2  4  7  10  3

```


```
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.DataFrame.items — PySpark 4.0.1 documentation
DataFrame.items()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.items)
[#](#pyspark.pandas.DataFrame.items "Permalink to this definition")

Iterator over (column name, Series) pairs.

Iterates over the DataFrame columns, returning a tuple with the column name and the content as a Series.

Returns

**label**object

The column names for the DataFrame being iterated over.

**content**Series

The column entries belonging to each label, as a Series.

Examples

```
>>> df = ps.DataFrame({'species': ['bear', 'bear', 'marsupial'],
...                    'population': [1864, 22000, 80000]},
...                   index=['panda', 'polar', 'koala'],
...                   columns=['species', 'population'])
>>> df
         species  population
panda       bear        1864
polar       bear       22000
koala  marsupial       80000

```


```
>>> for label, content in df.items():
...    print('label:', label)
...    print('content:', content.to_string())
label: species
content: panda         bear
polar         bear
koala    marsupial
label: population
content: panda     1864
polar    22000
koala    80000

```


# pyspark.pandas.DataFrame.iterrows — PySpark 4.0.1 documentation
DataFrame.iterrows()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.iterrows)
[#](#pyspark.pandas.DataFrame.iterrows "Permalink to this definition")

Iterate over DataFrame rows as (index, Series) pairs.

Yields

**index**label or tuple of label

The index of the row. A tuple for a MultiIndex.

**data**pandas.Series

The data of the row as a Series.

**it**generator

A generator that iterates over the rows of the frame.

Notes

1.  Because `iterrows` returns a Series for each row, it does **not** preserve dtypes across the rows (dtypes are preserved across columns for DataFrames). For example,
    
    ```
>>> df = ps.DataFrame([[1, 1.5]], columns=['int', 'float'])
>>> row = next(df.iterrows())
[1]
>>> row
int      1.0
float    1.5
Name: 0, dtype: float64
>>> print(row['int'].dtype)
float64
>>> print(df['int'].dtype)
int64

```

    
    To preserve dtypes while iterating over the rows, it is better to use [`itertuples()`](about:blank/pyspark.pandas.DataFrame.itertuples.html#pyspark.pandas.DataFrame.itertuples "pyspark.pandas.DataFrame.itertuples") which returns namedtuples of the values and which is generally faster than `iterrows`.
    
2.  You should **never modify** something you are iterating over. This is not guaranteed to work in all cases. Depending on the data types, the iterator returns a copy and not a view, and writing to it will have no effect.


# pyspark.pandas.DataFrame.itertuples — PySpark 4.0.1 documentation
DataFrame.itertuples(_index\=True_, _name\='PandasOnSpark'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.itertuples)
[#](#pyspark.pandas.DataFrame.itertuples "Permalink to this definition")

Iterate over DataFrame rows as namedtuples.

Parameters

**index**bool, default True

If True, return the index as the first element of the tuple.

**name**str or None, default “PandasOnSpark”

The name of the returned namedtuples or None to return regular tuples.

Returns

iterator

An object to iterate over namedtuples for each row in the DataFrame with the first field possibly being the index and following fields being the column values.

Notes

The column names will be renamed to positional names if they are invalid Python identifiers, repeated, or start with an underscore.

Examples

```
>>> df = ps.DataFrame({'num_legs': [4, 2], 'num_wings': [0, 2]},
...                   index=['dog', 'hawk'])
>>> df
      num_legs  num_wings
dog          4          0
hawk         2          2

```


```
>>> for row in df.itertuples():
...     print(row)
...
PandasOnSpark(Index='dog', num_legs=4, num_wings=0)
PandasOnSpark(Index='hawk', num_legs=2, num_wings=2)

```


By setting the index parameter to False we can remove the index as the first element of the tuple:

```
>>> for row in df.itertuples(index=False):
...     print(row)
...
PandasOnSpark(num_legs=4, num_wings=0)
PandasOnSpark(num_legs=2, num_wings=2)

```


With the name parameter set we set a custom name for the yielded namedtuples:

```
>>> for row in df.itertuples(name='Animal'):
...     print(row)
...
Animal(Index='dog', num_legs=4, num_wings=0)
Animal(Index='hawk', num_legs=2, num_wings=2)

```


# pyspark.pandas.DataFrame.keys — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.keys

DataFrame.keys()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.keys)
[#](#pyspark.pandas.DataFrame.keys "Permalink to this definition")

Return alias for columns.

Returns

Index

Columns of the DataFrame.

Examples

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


```
>>> df.keys()
Index(['max_speed', 'shield'], dtype='object')

```
# pyspark.pandas.DataFrame.pop — PySpark 4.0.1 documentation
DataFrame.pop(_item_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.pop)
[#](#pyspark.pandas.DataFrame.pop "Permalink to this definition")

Return item and drop from frame. Raise KeyError if not found.

Parameters

**item**str

Label of column to be popped.

Returns

Series

Examples

```
>>> df = ps.DataFrame([('falcon', 'bird', 389.0),
...                    ('parrot', 'bird', 24.0),
...                    ('lion', 'mammal', 80.5),
...                    ('monkey','mammal', np.nan)],
...                   columns=('name', 'class', 'max_speed'))

```


```
>>> df
     name   class  max_speed
0  falcon    bird      389.0
1  parrot    bird       24.0
2    lion  mammal       80.5
3  monkey  mammal        NaN

```


```
>>> df.pop('class')
0      bird
1      bird
2    mammal
3    mammal
Name: class, dtype: object

```


```
>>> df
     name  max_speed
0  falcon      389.0
1  parrot       24.0
2    lion       80.5
3  monkey        NaN

```


Also support for MultiIndex

```
>>> df = ps.DataFrame([('falcon', 'bird', 389.0),
...                    ('parrot', 'bird', 24.0),
...                    ('lion', 'mammal', 80.5),
...                    ('monkey','mammal', np.nan)],
...                   columns=('name', 'class', 'max_speed'))
>>> columns = [('a', 'name'), ('a', 'class'), ('b', 'max_speed')]
>>> df.columns = pd.MultiIndex.from_tuples(columns)
>>> df
        a                 b
     name   class max_speed
0  falcon    bird     389.0
1  parrot    bird      24.0
2    lion  mammal      80.5
3  monkey  mammal       NaN

```


```
>>> df.pop('a')
     name   class
0  falcon    bird
1  parrot    bird
2    lion  mammal
3  monkey  mammal

```


```
>>> df
          b
  max_speed
0     389.0
1      24.0
2      80.5
3       NaN

```

# pyspark.pandas.DataFrame.tail — PySpark 4.0.1 documentation
DataFrame.tail(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.tail)
[#](#pyspark.pandas.DataFrame.tail "Permalink to this definition")

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
>>> df = ps.DataFrame({'animal': ['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

```


Viewing the last 5 lines

```
>>> df.tail()  
   animal
4  monkey
5  parrot
6   shark
7   whale
8   zebra

```


Viewing the last n lines (three in this case)

```
>>> df.tail(3)  
  animal
6  shark
7  whale
8  zebra

```


For negative values of n

```
>>> df.tail(-3)  
   animal
3    lion
4  monkey
5  parrot
6   shark
7   whale
8   zebra

```


# pyspark.pandas.DataFrame.xs — PySpark 4.0.1 documentation
DataFrame.xs(_key_, _axis\=0_, _level\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.xs)
[#](#pyspark.pandas.DataFrame.xs "Permalink to this definition")

Return cross-section from the DataFrame.

This method takes a key argument to select data at a particular level of a MultiIndex.

Parameters

**key**label or tuple of label

Label contained in the index, or partially in a MultiIndex.

**axis**0 or ‘index’, default 0

Axis to retrieve cross-section on. currently only support 0 or ‘index’

**level**object, defaults to first n levels (n=1 or len(key))

In case of a key partially contained in a MultiIndex, indicate which levels are used. Levels can be referred by label or position.

Returns

DataFrame or Series

Cross-section from the original DataFrame corresponding to the selected index levels.

See also

[`DataFrame.loc`](about:blank/pyspark.pandas.DataFrame.loc.html#pyspark.pandas.DataFrame.loc "pyspark.pandas.DataFrame.loc")

Access a group of rows and columns by label(s) or a boolean array.

[`DataFrame.iloc`](about:blank/pyspark.pandas.DataFrame.iloc.html#pyspark.pandas.DataFrame.iloc "pyspark.pandas.DataFrame.iloc")

Purely integer-location based indexing for selection by position.

Examples

```
>>> d = {'num_legs': [4, 4, 2, 2],
...      'num_wings': [0, 0, 2, 2],
...      'class': ['mammal', 'mammal', 'mammal', 'bird'],
...      'animal': ['cat', 'dog', 'bat', 'penguin'],
...      'locomotion': ['walks', 'walks', 'flies', 'walks']}
>>> df = ps.DataFrame(data=d)
>>> df = df.set_index(['class', 'animal', 'locomotion'])
>>> df  
                           num_legs  num_wings
class  animal  locomotion
mammal cat     walks              4          0
       dog     walks              4          0
       bat     flies              2          2
bird   penguin walks              2          2

```


Get values at specified index

```
>>> df.xs('mammal')  
                   num_legs  num_wings
animal locomotion
cat    walks              4          0
dog    walks              4          0
bat    flies              2          2

```


Get values at several indexes

```
>>> df.xs(('mammal', 'dog'))  
            num_legs  num_wings
locomotion
walks              4          0

```


```
>>> df.xs(('mammal', 'dog', 'walks'))  
num_legs     4
num_wings    0
Name: (mammal, dog, walks), dtype: int64

```


Get values at specified index and level

```
>>> df.xs('cat', level=1)  
                   num_legs  num_wings
class  locomotion
mammal walks              4          0

```

# pyspark.pandas.DataFrame.get — PySpark 4.0.1 documentation
DataFrame.get(_key_, _default\=None_)
[#](#pyspark.pandas.DataFrame.get "Permalink to this definition")

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

# pyspark.pandas.DataFrame.where — PySpark 4.0.1 documentation
DataFrame.where(_cond_, _other\=nan_, _axis\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.where)
[#](#pyspark.pandas.DataFrame.where "Permalink to this definition")

Replace values where the condition is False.

Parameters

**cond**boolean DataFrame

Where cond is True, keep the original value. Where False, replace with corresponding value from other.

**other**scalar, DataFrame

Entries where cond is False are replaced with corresponding value from other.

**axis**int, default None

Can only be set to 0 now for compatibility with pandas.

Returns

DataFrame

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({'A': [0, 1, 2, 3, 4], 'B':[100, 200, 300, 400, 500]})
>>> df2 = ps.DataFrame({'A': [0, -1, -2, -3, -4], 'B':[-100, -200, -300, -400, -500]})
>>> df1
   A    B
0  0  100
1  1  200
2  2  300
3  3  400
4  4  500
>>> df2
   A    B
0  0 -100
1 -1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> df1.where(df1 > 0).sort_index()
     A      B
0  NaN  100.0
1  1.0  200.0
2  2.0  300.0
3  3.0  400.0
4  4.0  500.0

```


```
>>> df1.where(df1 > 1, 10).sort_index()
    A    B
0  10  100
1  10  200
2   2  300
3   3  400
4   4  500

```


```
>>> df1.where(df1 > 1, df1 + 100).sort_index()
     A    B
0  100  100
1  101  200
2    2  300
3    3  400
4    4  500

```


```
>>> df1.where(df1 > 1, df2).sort_index()
   A    B
0  0  100
1 -1  200
2  2  300
3  3  400
4  4  500

```


When the column name of cond is different from self, it treats all values are False

```
>>> cond = ps.DataFrame({'C': [0, -1, -2, -3, -4], 'D':[4, 3, 2, 1, 0]}) % 3 == 0
>>> cond
       C      D
0   True  False
1  False   True
2  False  False
3   True  False
4  False   True

```


```
>>> df1.where(cond).sort_index()
    A   B
0 NaN NaN
1 NaN NaN
2 NaN NaN
3 NaN NaN
4 NaN NaN

```


When the type of cond is Series, it just check boolean regardless of column name

```
>>> cond = ps.Series([1, 2]) > 1
>>> cond
0    False
1     True
dtype: bool

```


```
>>> df1.where(cond).sort_index()
     A      B
0  NaN    NaN
1  1.0  200.0
2  NaN    NaN
3  NaN    NaN
4  NaN    NaN

```


```
>>> reset_option("compute.ops_on_diff_frames")

```




# pyspark.pandas.DataFrame.mask — PySpark 4.0.1 documentation
DataFrame.mask(_cond_, _other\=nan_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mask)
[#](#pyspark.pandas.DataFrame.mask "Permalink to this definition")

Replace values where the condition is True.

Parameters

**cond**boolean DataFrame

Where cond is False, keep the original value. Where True, replace with corresponding value from other.

**other**scalar, DataFrame

Entries where cond is True are replaced with corresponding value from other.

Returns

DataFrame

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({'A': [0, 1, 2, 3, 4], 'B':[100, 200, 300, 400, 500]})
>>> df2 = ps.DataFrame({'A': [0, -1, -2, -3, -4], 'B':[-100, -200, -300, -400, -500]})
>>> df1
   A    B
0  0  100
1  1  200
2  2  300
3  3  400
4  4  500
>>> df2
   A    B
0  0 -100
1 -1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> df1.mask(df1 > 0).sort_index()
     A   B
0  0.0 NaN
1  NaN NaN
2  NaN NaN
3  NaN NaN
4  NaN NaN

```


```
>>> df1.mask(df1 > 1, 10).sort_index()
    A   B
0   0  10
1   1  10
2  10  10
3  10  10
4  10  10

```


```
>>> df1.mask(df1 > 1, df1 + 100).sort_index()
     A    B
0    0  200
1    1  300
2  102  400
3  103  500
4  104  600

```


```
>>> df1.mask(df1 > 1, df2).sort_index()
   A    B
0  0 -100
1  1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> reset_option("compute.ops_on_diff_frames")

```



# pyspark.pandas.DataFrame.mask — PySpark 4.0.1 documentation
DataFrame.mask(_cond_, _other\=nan_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mask)
[#](#pyspark.pandas.DataFrame.mask "Permalink to this definition")

Replace values where the condition is True.

Parameters

**cond**boolean DataFrame

Where cond is False, keep the original value. Where True, replace with corresponding value from other.

**other**scalar, DataFrame

Entries where cond is True are replaced with corresponding value from other.

Returns

DataFrame

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({'A': [0, 1, 2, 3, 4], 'B':[100, 200, 300, 400, 500]})
>>> df2 = ps.DataFrame({'A': [0, -1, -2, -3, -4], 'B':[-100, -200, -300, -400, -500]})
>>> df1
   A    B
0  0  100
1  1  200
2  2  300
3  3  400
4  4  500
>>> df2
   A    B
0  0 -100
1 -1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> df1.mask(df1 > 0).sort_index()
     A   B
0  0.0 NaN
1  NaN NaN
2  NaN NaN
3  NaN NaN
4  NaN NaN

```


```
>>> df1.mask(df1 > 1, 10).sort_index()
    A   B
0   0  10
1   1  10
2  10  10
3  10  10
4  10  10

```


```
>>> df1.mask(df1 > 1, df1 + 100).sort_index()
     A    B
0    0  200
1    1  300
2  102  400
3  103  500
4  104  600

```


```
>>> df1.mask(df1 > 1, df2).sort_index()
   A    B
0  0 -100
1  1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> reset_option("compute.ops_on_diff_frames")

```

# pyspark.pandas.DataFrame.mask — PySpark 4.0.1 documentation
DataFrame.mask(_cond_, _other\=nan_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mask)
[#](#pyspark.pandas.DataFrame.mask "Permalink to this definition")

Replace values where the condition is True.

Parameters

**cond**boolean DataFrame

Where cond is False, keep the original value. Where True, replace with corresponding value from other.

**other**scalar, DataFrame

Entries where cond is True are replaced with corresponding value from other.

Returns

DataFrame

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({'A': [0, 1, 2, 3, 4], 'B':[100, 200, 300, 400, 500]})
>>> df2 = ps.DataFrame({'A': [0, -1, -2, -3, -4], 'B':[-100, -200, -300, -400, -500]})
>>> df1
   A    B
0  0  100
1  1  200
2  2  300
3  3  400
4  4  500
>>> df2
   A    B
0  0 -100
1 -1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> df1.mask(df1 > 0).sort_index()
     A   B
0  0.0 NaN
1  NaN NaN
2  NaN NaN
3  NaN NaN
4  NaN NaN

```


```
>>> df1.mask(df1 > 1, 10).sort_index()
    A   B
0   0  10
1   1  10
2  10  10
3  10  10
4  10  10

```


```
>>> df1.mask(df1 > 1, df1 + 100).sort_index()
     A    B
0    0  200
1    1  300
2  102  400
3  103  500
4  104  600

```


```
>>> df1.mask(df1 > 1, df2).sort_index()
   A    B
0  0 -100
1  1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.DataFrame.mask — PySpark 4.0.1 documentation
DataFrame.mask(_cond_, _other\=nan_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mask)
[#](#pyspark.pandas.DataFrame.mask "Permalink to this definition")

Replace values where the condition is True.

Parameters

**cond**boolean DataFrame

Where cond is False, keep the original value. Where True, replace with corresponding value from other.

**other**scalar, DataFrame

Entries where cond is True are replaced with corresponding value from other.

Returns

DataFrame

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({'A': [0, 1, 2, 3, 4], 'B':[100, 200, 300, 400, 500]})
>>> df2 = ps.DataFrame({'A': [0, -1, -2, -3, -4], 'B':[-100, -200, -300, -400, -500]})
>>> df1
   A    B
0  0  100
1  1  200
2  2  300
3  3  400
4  4  500
>>> df2
   A    B
0  0 -100
1 -1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> df1.mask(df1 > 0).sort_index()
     A   B
0  0.0 NaN
1  NaN NaN
2  NaN NaN
3  NaN NaN
4  NaN NaN

```


```
>>> df1.mask(df1 > 1, 10).sort_index()
    A   B
0   0  10
1   1  10
2  10  10
3  10  10
4  10  10

```


```
>>> df1.mask(df1 > 1, df1 + 100).sort_index()
     A    B
0    0  200
1    1  300
2  102  400
3  103  500
4  104  600

```


```
>>> df1.mask(df1 > 1, df2).sort_index()
   A    B
0  0 -100
1  1 -200
2 -2 -300
3 -3 -400
4 -4 -500

```


```
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.DataFrame.query — PySpark 4.0.1 documentation
DataFrame.query(_expr_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.query)
[#](#pyspark.pandas.DataFrame.query "Permalink to this definition")

Query the columns of a DataFrame with a boolean expression.

Note

Internal columns that starting with a ‘\_\_’ prefix are able to access, however, they are not supposed to be accessed.

Note

This API delegates to Spark SQL so the syntax follows Spark SQL. Therefore, the pandas specific syntax such as @ is not supported. If you want the pandas syntax, you can work around with [`DataFrame.pandas_on_spark.apply_batch()`](about:blank/pyspark.pandas.DataFrame.pandas_on_spark.apply_batch.html#pyspark.pandas.DataFrame.pandas_on_spark.apply_batch "pyspark.pandas.DataFrame.pandas_on_spark.apply_batch"), but you should be aware that query\_func will be executed at different nodes in a distributed manner. So, for example to use @ syntax, make sure the variable is serialized by putting it within the closure as below.

```
>>> df = ps.DataFrame({'A': range(2000), 'B': range(2000)})
>>> def query_func(pdf):
...     num = 1995
...     return pdf.query('A > @num')
>>> df.pandas_on_spark.apply_batch(query_func)
         A     B
1996  1996  1996
1997  1997  1997
1998  1998  1998
1999  1999  1999

```


Parameters

**expr**str

The query string to evaluate.

You can refer to column names that contain spaces by surrounding them in backticks.

For example, if one of your columns is called `a a` and you want to sum it with `b`, your query should be `` `a a` + b ``.

**inplace**bool

Whether the query should modify the data in place or return a modified copy.

Returns

DataFrame

DataFrame resulting from the provided query expression.

Examples

```
>>> df = ps.DataFrame({'A': range(1, 6),
...                    'B': range(10, 0, -2),
...                    'C C': range(10, 5, -1)})
>>> df
   A   B  C C
0  1  10   10
1  2   8    9
2  3   6    8
3  4   4    7
4  5   2    6

```


```
>>> df.query('A > B')
   A  B  C C
4  5  2    6

```


The previous expression is equivalent to

```
>>> df[df.A > df.B]
   A  B  C C
4  5  2    6

```


For columns with spaces in their name, you can use backtick quoting.

```
>>> df.query('B == `C C`')
   A   B  C C
0  1  10   10

```


The previous expression is equivalent to

```
>>> df[df.B == df['C C']]
   A   B  C C
0  1  10   10

```
# pyspark.pandas.DataFrame.rdiv — PySpark 4.0.1 documentation
DataFrame.rdiv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rdiv)
[#](#pyspark.pandas.DataFrame.rdiv "Permalink to this definition")

Get Floating division of dataframe and other, element-wise (binary operator /).

Equivalent to `other / dataframe`. With the reverse version, div.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.truediv — PySpark 4.0.1 documentation
DataFrame.truediv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.truediv)
[#](#pyspark.pandas.DataFrame.truediv "Permalink to this definition")

Get Floating division of dataframe and other, element-wise (binary operator /).

Equivalent to `dataframe / other`. With the reverse version, rtruediv.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.rtruediv — PySpark 4.0.1 documentation
DataFrame.rtruediv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rtruediv)
[#](#pyspark.pandas.DataFrame.rtruediv "Permalink to this definition")

Get Floating division of dataframe and other, element-wise (binary operator /).

Equivalent to `other / dataframe`. With the reverse version, truediv.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.mul — PySpark 4.0.1 documentation
DataFrame.mul(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mul)
[#](#pyspark.pandas.DataFrame.mul "Permalink to this definition")

Get Multiplication of dataframe and other, element-wise (binary operator \*).

Equivalent to `dataframe * other`. With the reverse version, rmul.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```

# pyspark.pandas.DataFrame.rmul — PySpark 4.0.1 documentation
DataFrame.rmul(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rmul)
[#](#pyspark.pandas.DataFrame.rmul "Permalink to this definition")

Get Multiplication of dataframe and other, element-wise (binary operator \*).

Equivalent to `other * dataframe`. With the reverse version, mul.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```

# pyspark.pandas.DataFrame.sub — PySpark 4.0.1 documentation
DataFrame.sub(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.sub)
[#](#pyspark.pandas.DataFrame.sub "Permalink to this definition")

Get Subtraction of dataframe and other, element-wise (binary operator \-).

Equivalent to `dataframe - other`. With the reverse version, rsub.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```

# pyspark.pandas.DataFrame.rsub — PySpark 4.0.1 documentation
DataFrame.rsub(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rsub)
[#](#pyspark.pandas.DataFrame.rsub "Permalink to this definition")

Get Subtraction of dataframe and other, element-wise (binary operator \-).

Equivalent to `other - dataframe`. With the reverse version, sub.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```

# pyspark.pandas.DataFrame.pow — PySpark 4.0.1 documentation
DataFrame.pow(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.pow)
[#](#pyspark.pandas.DataFrame.pow "Permalink to this definition")

Get Exponential power of series of dataframe and other, element-wise (binary operator \*\*).

Equivalent to `dataframe ** other`. With the reverse version, rpow.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```



# pyspark.pandas.DataFrame.rpow — PySpark 4.0.1 documentation
DataFrame.rpow(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rpow)
[#](#pyspark.pandas.DataFrame.rpow "Permalink to this definition")

Get Exponential power of dataframe and other, element-wise (binary operator \*\*).

Equivalent to `other ** dataframe`. With the reverse version, pow.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.mod — PySpark 4.0.1 documentation
DataFrame.mod(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mod)
[#](#pyspark.pandas.DataFrame.mod "Permalink to this definition")

Get Modulo of dataframe and other, element-wise (binary operator %).

Equivalent to `dataframe % other`. With the reverse version, rmod.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```

# pyspark.pandas.DataFrame.rmod — PySpark 4.0.1 documentation
DataFrame.rmod(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rmod)
[#](#pyspark.pandas.DataFrame.rmod "Permalink to this definition")

Get Modulo of dataframe and other, element-wise (binary operator %).

Equivalent to `other % dataframe`. With the reverse version, mod.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.floordiv — PySpark 4.0.1 documentation
DataFrame.floordiv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.floordiv)
[#](#pyspark.pandas.DataFrame.floordiv "Permalink to this definition")

Get Integer division of dataframe and other, element-wise (binary operator //).

Equivalent to `dataframe // other`. With the reverse version, rfloordiv.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.rfloordiv — PySpark 4.0.1 documentation
DataFrame.rfloordiv(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rfloordiv)
[#](#pyspark.pandas.DataFrame.rfloordiv "Permalink to this definition")

Get Integer division of dataframe and other, element-wise (binary operator //).

Equivalent to `other // dataframe`. With the reverse version, floordiv.

Among flexible wrappers (add, sub, mul, div) to arithmetic operators: +, \-, \*, /, //.

Parameters

**other**scalar

Any single data

Returns

DataFrame

Result of the arithmetic operation.

Examples

```
>>> df = ps.DataFrame({'angles': [0, 3, 4],
...                    'degrees': [360, 180, 360]},
...                   index=['circle', 'triangle', 'rectangle'],
...                   columns=['angles', 'degrees'])
>>> df
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Add a scalar with operator version which returns the same results. Also, the reverse version.

```
>>> df + 1
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


```
>>> df.add(df)
           angles  degrees
circle          0      720
triangle        6      360
rectangle       8      720

```


```
>>> df + df + df
           angles  degrees
circle          0     1080
triangle        9      540
rectangle      12     1080

```


```
>>> df.radd(1)
           angles  degrees
circle          1      361
triangle        4      181
rectangle       5      361

```


Divide and true divide by constant with reverse version.

```
>>> df / 10
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.div(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rdiv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


```
>>> df.truediv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.3     18.0
rectangle     0.4     36.0

```


```
>>> df.rtruediv(10)
             angles   degrees
circle          inf  0.027778
triangle   3.333333  0.055556
rectangle  2.500000  0.027778

```


Subtract by constant with reverse version.

```
>>> df - 1
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.sub(1)
           angles  degrees
circle         -1      359
triangle        2      179
rectangle       3      359

```


```
>>> df.rsub(1)
           angles  degrees
circle          1     -359
triangle       -2     -179
rectangle      -3     -359

```


Multiply by constant with the reverse version.

```
>>> df * 1
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.mul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


```
>>> df.rmul(1)
           angles  degrees
circle          0      360
triangle        3      180
rectangle       4      360

```


Floor Divide by constant with reverse version.

```
>>> df // 10
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.floordiv(10)
           angles  degrees
circle        0.0     36.0
triangle      0.0     18.0
rectangle     0.0     36.0

```


```
>>> df.rfloordiv(10)  
           angles  degrees
circle        inf      0.0
triangle      3.0      0.0
rectangle     2.0      0.0

```


Mod by constant with reverse version.

```
>>> df % 2
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.mod(2)
           angles  degrees
circle          0        0
triangle        1        0
rectangle       0        0

```


```
>>> df.rmod(2)
           angles  degrees
circle        NaN        2
triangle      2.0        2
rectangle     2.0        2

```


Power by constant with reverse version.

```
>>> df ** 2
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.pow(2)
           angles   degrees
circle        0.0  129600.0
triangle      9.0   32400.0
rectangle    16.0  129600.0

```


```
>>> df.rpow(2)
           angles        degrees
circle        1.0  2.348543e+108
triangle      8.0   1.532496e+54
rectangle    16.0  2.348543e+108

```


# pyspark.pandas.DataFrame.lt — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.lt

DataFrame.lt(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.lt)
[#](#pyspark.pandas.DataFrame.lt "Permalink to this definition")

Compare if the current value is less than the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.lt(1)
       a      b
a  False  False
b  False  False
c  False  False
d  False  False

```


# pyspark.pandas.DataFrame.gt — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.gt

DataFrame.gt(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.gt)
[#](#pyspark.pandas.DataFrame.gt "Permalink to this definition")

Compare if the current value is greater than the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.gt(2)
       a      b
a  False  False
b  False  False
c   True  False
d   True  False

```


# pyspark.pandas.DataFrame.le — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.le

DataFrame.le(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.le)
[#](#pyspark.pandas.DataFrame.le "Permalink to this definition")

Compare if the current value is less than or equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.le(2)
       a      b
a   True   True
b   True  False
c  False   True
d  False  False

```
# pyspark.pandas.DataFrame.ge — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.ge

DataFrame.ge(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.ge)
[#](#pyspark.pandas.DataFrame.ge "Permalink to this definition")

Compare if the current value is greater than or equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.ge(1)
      a      b
a  True   True
b  True  False
c  True   True
d  True  False

```

# pyspark.pandas.DataFrame.ne — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.ne

DataFrame.ne(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.ne)
[#](#pyspark.pandas.DataFrame.ne "Permalink to this definition")

Compare if the current value is not equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.ne(1)
       a      b
a  False  False
b   True   True
c   True  False
d   True   True

```


# pyspark.pandas.DataFrame.eq — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.eq

DataFrame.eq(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.eq)
[#](#pyspark.pandas.DataFrame.eq "Permalink to this definition")

Compare if the current value is equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.eq(1)
       a      b
a   True   True
b  False  False
c  False   True
d  False  False

```


# pyspark.pandas.DataFrame.dot — PySpark 4.0.1 documentation
DataFrame.dot(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.dot)
[#](#pyspark.pandas.DataFrame.dot "Permalink to this definition")

Compute the matrix multiplication between the DataFrame and others.

This method computes the matrix product between the DataFrame and the values of an other Series

It can also be called using `self @ other` in Python >= 3.5.

Note

This method is based on an expensive operation due to the nature of big data. Internally it needs to generate each row for each value, and then group twice - it is a huge operation. To prevent misuse, this method has the ‘compute.max\_rows’ default limit of input length and raises a ValueError.

```
>>> from pyspark.pandas.config import option_context
>>> with option_context(
...     'compute.max_rows', 1000, "compute.ops_on_diff_frames", True
... ):  
...     psdf = ps.DataFrame({'a': range(1001)})
...     psser = ps.Series([2], index=['a'])
...     psdf.dot(psser)
Traceback (most recent call last):
  ...
ValueError: Current DataFrame's length exceeds the given limit of 1000 rows.
Please set 'compute.max_rows' by using 'pyspark.pandas.config.set_option'
to retrieve more than 1000 rows. Note that, before changing the
'compute.max_rows', this operation is considerably expensive.

```


Parameters

**other**Series

The other object to compute the matrix product with.

Returns

Series

Return the matrix product between self and other as a Series.

Notes

The dimensions of DataFrame and other must be compatible to compute the matrix multiplication. In addition, the column names of DataFrame and the index of other must contain the same values, as they will be aligned prior to the multiplication.

The dot method for Series computes the inner product, instead of the matrix product here.

Examples

```
>>> from pyspark.pandas.config import set_option, reset_option
>>> set_option("compute.ops_on_diff_frames", True)
>>> psdf = ps.DataFrame([[0, 1, -2, -1], [1, 1, 1, 1]])
>>> psser = ps.Series([1, 1, 2, 1])
>>> psdf.dot(psser)
0   -4
1    5
dtype: int64

```


Note how shuffling of the objects does not change the result.

```
>>> psser2 = psser.reindex([1, 0, 2, 3])
>>> psdf.dot(psser2)
0   -4
1    5
dtype: int64
>>> psdf @ psser2
0   -4
1    5
dtype: int64
>>> reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.DataFrame.combine_first — PySpark 4.0.1 documentation
DataFrame.combine\_first(_other_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.combine_first)
[#](#pyspark.pandas.DataFrame.combine_first "Permalink to this definition")

Update null elements with value in the same location in other.

Combine two DataFrame objects by filling null values in one DataFrame with non-null values from other DataFrame. The row and column indexes of the resulting DataFrame will be the union of the two.

New in version 3.3.0.

Parameters

**other**DataFrame

Provided DataFrame to use to fill null values.

Returns

DataFrame

Examples

```
>>> ps.set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({'A': [None, 0], 'B': [None, 4]})
>>> df2 = ps.DataFrame({'A': [1, 1], 'B': [3, 3]})

```


```
>>> df1.combine_first(df2).sort_index()
     A    B
0  1.0  3.0
1  0.0  4.0

```


Null values persist if the location of that null value does not exist in other

```
>>> df1 = ps.DataFrame({'A': [None, 0], 'B': [4, None]})
>>> df2 = ps.DataFrame({'B': [3, 3], 'C': [1, 1]}, index=[1, 2])

```


```
>>> df1.combine_first(df2).sort_index()
     A    B    C
0  NaN  4.0  NaN
1  0.0  3.0  1.0
2  NaN  3.0  1.0
>>> ps.reset_option("compute.ops_on_diff_frames")

```


# pyspark.pandas.DataFrame.apply — PySpark 4.0.1 documentation
DataFrame.apply(_func_, _axis\=0_, _args\=()_, _\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.apply)
[#](#pyspark.pandas.DataFrame.apply "Permalink to this definition")

Apply a function along an axis of the DataFrame.

Objects passed to the function are Series objects whose index is either the DataFrame’s index (`axis=0`) or the DataFrame’s columns (`axis=1`).

See also [Transform and apply a function](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/transform_apply.html).

Note

when axis is 0 or ‘index’, the func is unable to access to the whole input series. pandas-on-Spark internally splits the input series into multiple batches and calls func with each batch multiple times. Therefore, operations such as global aggregations are impossible. See the example below.

```
>>> # This case does not return the length of whole series but of the batch internally
... # used.
... def length(s) -> int:
...     return len(s)
...
>>> df = ps.DataFrame({'A': range(1000)})
>>> df.apply(length, axis=0)  
0     83
1     83
2     83
...
10    83
11    83
dtype: int32

```


Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify the return type as Series or scalar value in `func`, for instance, as below:

```
>>> def square(s) -> ps.Series[np.int32]:
...     return s ** 2

```


pandas-on-Spark uses return type hints and does not try to infer the type.

In case when axis is 1, it requires to specify DataFrame or scalar value with type hints as below:

```
>>> def plus_one(x) -> ps.DataFrame[int, [float, float]]:
...     return x + 1

```


If the return type is specified as DataFrame, the output column names become c0, c1, c2 … cn. These names are positionally mapped to the returned DataFrame in `func`.

To specify the column names, you can assign them in a pandas style as below:

```
>>> def plus_one(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
...     return x + 1

```


```
>>> pdf = pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
>>> def plus_one(x) -> ps.DataFrame[
...         (pdf.index.name, pdf.index.dtype), zip(pdf.dtypes, pdf.columns)]:
...     return x + 1

```


Parameters

**func**function

Function to apply to each column or row.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Axis along which the function is applied:

*   0 or ‘index’: apply function to each column.
    
*   1 or ‘columns’: apply function to each row.
    

**args**tuple

Positional arguments to pass to func in addition to the array/series.

**\*\*kwds**

Additional keyword arguments to pass as keywords arguments to func.

Returns

Series or DataFrame

Result of applying `func` along the given axis of the DataFrame.

Examples

```
>>> df = ps.DataFrame([[4, 9]] * 3, columns=['A', 'B'])
>>> df
   A  B
0  4  9
1  4  9
2  4  9

```


Using a numpy universal function (in this case the same as `np.sqrt(df)`):

```
>>> def sqrt(x) -> ps.Series[float]:
...     return np.sqrt(x)
...
>>> df.apply(sqrt, axis=0)
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0

```


You can omit type hints and let pandas-on-Spark infer its type.

```
>>> df.apply(np.sqrt, axis=0)
     A    B
0  2.0  3.0
1  2.0  3.0
2  2.0  3.0

```


When axis is 1 or ‘columns’, it applies the function for each row.

```
>>> def summation(x) -> np.int64:
...     return np.sum(x)
...
>>> df.apply(summation, axis=1)
0    13
1    13
2    13
dtype: int64

```


You can omit type hints and let pandas-on-Spark infer its type.

```
>>> df.apply(np.sum, axis=1)
0    13
1    13
2    13
dtype: int64

```


```
>>> df.apply(max, axis=1)
0    9
1    9
2    9
dtype: int64

```


Returning a list-like will result in a Series

```
>>> df.apply(lambda x: [1, 2], axis=1)
0    [1, 2]
1    [1, 2]
2    [1, 2]
dtype: object

```


To specify the types when axis is ‘1’, it should use DataFrame\[…\] annotation. In this case, the column names are automatically generated.

```
>>> def identify(x) -> ps.DataFrame[('index', int), [('A', np.int64), ('B', np.int64)]]:
...     return x
...
>>> df.apply(identify, axis=1)  
       A  B
index
0      4  9
1      4  9
2      4  9

```


You can also specify extra arguments.

```
>>> def plus_two(a, b, c) -> ps.DataFrame[np.int64, [np.int64, np.int64]]:
...     return a + b + c
...
>>> df.apply(plus_two, axis=1, args=(1,), c=3)
   c0  c1
0   8  13
1   8  13
2   8  13

```


# pyspark.pandas.DataFrame.applymap — PySpark 4.0.1 documentation
DataFrame.applymap(_func_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.applymap)
[#](#pyspark.pandas.DataFrame.applymap "Permalink to this definition")

Apply a function to a Dataframe elementwise.

This method applies a function that accepts and returns a scalar to every element of a DataFrame.

Deprecated since version 4.0.0.

Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def square(x) -> np.int32:
...     return x ** 2

```


pandas-on-Spark uses return type hints and does not try to infer the type.

Parameters

**func**callable

Python function returns a single value from a single value.

Returns

DataFrame

Transformed DataFrame.

Examples

```
>>> df = ps.DataFrame([[1, 2.12], [3.356, 4.567]])
>>> df
       0      1
0  1.000  2.120
1  3.356  4.567

```


```
>>> def str_len(x) -> int:
...     return len(str(x))
>>> df.applymap(str_len)
   0  1
0  3  4
1  5  5

```


```
>>> def power(x) -> float:
...     return x ** 2
>>> df.applymap(power)
           0          1
0   1.000000   4.494400
1  11.262736  20.857489

```


You can omit type hints and let pandas-on-Spark infer its type.

```
>>> df.applymap(lambda x: x ** 2)
           0          1
0   1.000000   4.494400
1  11.262736  20.857489

```


# pyspark.pandas.DataFrame.map — PySpark 4.0.1 documentation
DataFrame.map(_func_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.map)
[#](#pyspark.pandas.DataFrame.map "Permalink to this definition")

Apply a function to a Dataframe elementwise.

This method applies a function that accepts and returns a scalar to every element of a DataFrame.

New in version 4.0.0: DataFrame.applymap was deprecated and renamed to DataFrame.map.

Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def square(x) -> np.int32:
...     return x ** 2

```


pandas-on-Spark uses return type hints and does not try to infer the type.

Parameters

**func**callable

Python function returns a single value from a single value.

Returns

DataFrame

Transformed DataFrame.

Examples

```
>>> df = ps.DataFrame([[1, 2.12], [3.356, 4.567]])
>>> df
       0      1
0  1.000  2.120
1  3.356  4.567

```


```
>>> def str_len(x) -> int:
...     return len(str(x))
>>> df.map(str_len)
   0  1
0  3  4
1  5  5

```


```
>>> def power(x) -> float:
...     return x ** 2
>>> df.map(power)
           0          1
0   1.000000   4.494400
1  11.262736  20.857489

```


You can omit type hints and let pandas-on-Spark infer its type.

```
>>> df.map(lambda x: x ** 2)
           0          1
0   1.000000   4.494400
1  11.262736  20.857489

```


# pyspark.pandas.DataFrame.pipe — PySpark 4.0.1 documentation
DataFrame.pipe(_func_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.DataFrame.pipe "Permalink to this definition")

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
# pyspark.pandas.DataFrame.agg — PySpark 4.0.1 documentation
DataFrame.agg(_func_)
[#](#pyspark.pandas.DataFrame.agg "Permalink to this definition")

Aggregate using one or more operations over the specified axis.

Parameters

**func**dict or a list

a dict mapping from column name (string) to aggregate functions (list of strings). If a list is given, the aggregation is performed against all columns.

Returns

DataFrame

Notes

agg is an alias for aggregate. Use the alias.

Examples

```
>>> df = ps.DataFrame([[1, 2, 3],
...                    [4, 5, 6],
...                    [7, 8, 9],
...                    [np.nan, np.nan, np.nan]],
...                   columns=['A', 'B', 'C'])

```


```
>>> df
     A    B    C
0  1.0  2.0  3.0
1  4.0  5.0  6.0
2  7.0  8.0  9.0
3  NaN  NaN  NaN

```


Aggregate these functions over the rows.

```
>>> df.agg(['sum', 'min'])
[['A', 'B', 'C']].sort_index()
        A     B     C
min   1.0   2.0   3.0
sum  12.0  15.0  18.0

```


Different aggregations per column.

```
>>> df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
[['A', 'B']].sort_index()
        A    B
max   NaN  8.0
min   1.0  2.0
sum  12.0  NaN

```


For multi-index columns:

```
>>> df.columns = pd.MultiIndex.from_tuples([("X", "A"), ("X", "B"), ("Y", "C")])
>>> df.agg(['sum', 'min'])
[[("X", "A"), ("X", "B"), ("Y", "C")]].sort_index()
        X           Y
        A     B     C
min   1.0   2.0   3.0
sum  12.0  15.0  18.0

```


```
>>> aggregated = df.agg({("X", "A") : ['sum', 'min'], ("X", "B") : ['min', 'max']})
>>> aggregated[[("X", "A"), ("X", "B")]].sort_index()  
        X
        A    B
max   NaN  8.0
min   1.0  2.0
sum  12.0  NaN

```

# pyspark.pandas.DataFrame.aggregate — PySpark 4.0.1 documentation
DataFrame.aggregate(_func_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.aggregate)
[#](#pyspark.pandas.DataFrame.aggregate "Permalink to this definition")

Aggregate using one or more operations over the specified axis.

Parameters

**func**dict or a list

a dict mapping from column name (string) to aggregate functions (list of strings). If a list is given, the aggregation is performed against all columns.

Returns

DataFrame

Notes

agg is an alias for aggregate. Use the alias.

Examples

```
>>> df = ps.DataFrame([[1, 2, 3],
...                    [4, 5, 6],
...                    [7, 8, 9],
...                    [np.nan, np.nan, np.nan]],
...                   columns=['A', 'B', 'C'])

```


```
>>> df
     A    B    C
0  1.0  2.0  3.0
1  4.0  5.0  6.0
2  7.0  8.0  9.0
3  NaN  NaN  NaN

```


Aggregate these functions over the rows.

```
>>> df.agg(['sum', 'min'])
[['A', 'B', 'C']].sort_index()
        A     B     C
min   1.0   2.0   3.0
sum  12.0  15.0  18.0

```


Different aggregations per column.

```
>>> df.agg({'A' : ['sum', 'min'], 'B' : ['min', 'max']})
[['A', 'B']].sort_index()
        A    B
max   NaN  8.0
min   1.0  2.0
sum  12.0  NaN

```


For multi-index columns:

```
>>> df.columns = pd.MultiIndex.from_tuples([("X", "A"), ("X", "B"), ("Y", "C")])
>>> df.agg(['sum', 'min'])
[[("X", "A"), ("X", "B"), ("Y", "C")]].sort_index()
        X           Y
        A     B     C
min   1.0   2.0   3.0
sum  12.0  15.0  18.0

```


```
>>> aggregated = df.agg({("X", "A") : ['sum', 'min'], ("X", "B") : ['min', 'max']})
>>> aggregated[[("X", "A"), ("X", "B")]].sort_index()  
        X
        A    B
max   NaN  8.0
min   1.0  2.0
sum  12.0  NaN

```


# pyspark.pandas.DataFrame.groupby — PySpark 4.0.1 documentation
DataFrame.groupby(_by_, _axis\=0_, _as\_index\=True_, _dropna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.groupby)
[#](#pyspark.pandas.DataFrame.groupby "Permalink to this definition")

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

# pyspark.pandas.DataFrame.rolling — PySpark 4.0.1 documentation
DataFrame.rolling(_window_, _min\_periods\=None_)
[#](#pyspark.pandas.DataFrame.rolling "Permalink to this definition")

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

# pyspark.pandas.DataFrame.expanding — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.expanding

DataFrame.expanding(_min\_periods\=1_)
[#](#pyspark.pandas.DataFrame.expanding "Permalink to this definition")

Provide expanding transformations.

Note

‘min\_periods’ in pandas-on-Spark works as a fixed window size unlike pandas. Unlike pandas, NA is also counted as the period. This might be changed soon.

Parameters

**min\_periods: int, default 1**

Minimum number of observations in window required to have a value (otherwise result is NA).

Returns

a Window sub-classed for the operation


# pyspark.pandas.DataFrame.transform — PySpark 4.0.1 documentation
DataFrame.transform(_func_, _axis\=0_, _\*args_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.transform)
[#](#pyspark.pandas.DataFrame.transform "Permalink to this definition")

Call `func` on self producing a Series with transformed values and that has the same length as its input.

See also [Transform and apply a function](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/transform_apply.html).

Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def square(x) -> ps.Series[np.int32]:
...     return x ** 2

```


pandas-on-Spark uses return type hints and does not try to infer the type.

Note

the series within `func` is actually multiple pandas series as the segments of the whole pandas-on-Spark series; therefore, the length of each series is not guaranteed. As an example, an aggregation against each series does work as a global aggregation but an aggregation of each segment. See below:

```
>>> def func(x) -> ps.Series[np.int32]:
...     return x + sum(x)

```


Parameters

**func**function

Function to use for transforming the data. It must work when pandas Series is passed.

**axis**int, default 0 or ‘index’

Can only be set to 0 now.

**\*args**

Positional arguments to pass to func.

**\*\*kwargs**

Keyword arguments to pass to func.

Returns

DataFrame

A DataFrame that must have the same length as self.

Raises

**Exception**If the returned DataFrame has a different length than self.

Examples

```
>>> df = ps.DataFrame({'A': range(3), 'B': range(1, 4)}, columns=['A', 'B'])
>>> df
   A  B
0  0  1
1  1  2
2  2  3

```


```
>>> def square(x) -> ps.Series[np.int32]:
...     return x ** 2
>>> df.transform(square)
   A  B
0  0  1
1  1  4
2  4  9

```


You can omit type hints and let pandas-on-Spark infer its type.

```
>>> df.transform(lambda x: x ** 2)
   A  B
0  0  1
1  1  4
2  4  9

```


For multi-index columns:

```
>>> df.columns = [('X', 'A'), ('X', 'B')]
>>> df.transform(square)  
   X
   A  B
0  0  1
1  1  4
2  4  9

```


```
>>> (df * -1).transform(abs)  
   X
   A  B
0  0  1
1  1  2
2  2  3

```


You can also specify extra arguments.

```
>>> def calculation(x, y, z) -> ps.Series[int]:
...     return x ** y + z
>>> df.transform(calculation, y=10, z=20)  
      X
      A      B
0    20     21
1    21   1044
2  1044  59069

```

# pyspark.pandas.DataFrame.abs — PySpark 4.0.1 documentation
DataFrame.abs()
[#](#pyspark.pandas.DataFrame.abs "Permalink to this definition")

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



# pyspark.pandas.DataFrame.all — PySpark 4.0.1 documentation
DataFrame.all(_axis\=0_, _bool\_only\=None_, _skipna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.all)
[#](#pyspark.pandas.DataFrame.all "Permalink to this definition")

Return whether all elements are True.

Returns True unless there is at least one element within a series that is False or equivalent (e.g. zero or empty)

Parameters

**axis**{0 or ‘index’}, default 0

Indicate which axis or axes should be reduced.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    

**bool\_only**bool, default None

Include only boolean columns. If None, will attempt to use everything, then use only boolean data.

**skipna**boolean, default True

Exclude NA values, such as None or numpy.NaN. If an entire row/column is NA values and skipna is True, then the result will be True, as for an empty row/column. If skipna is False, numpy.NaNs are treated as True because these are not equal to zero, Nones are treated as False.

Returns

Series

Examples

Create a dataframe from a dictionary.

```
>>> df = ps.DataFrame({
...    'col1': [True, True, True],
...    'col2': [True, False, False],
...    'col3': [0, 0, 0],
...    'col4': [1, 2, 3],
...    'col5': [True, True, None],
...    'col6': [True, False, None]},
...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

```


Default behavior checks if column-wise values all return True.

```
>>> df.all()
col1     True
col2    False
col3    False
col4     True
col5     True
col6    False
dtype: bool

```


Include NA values when set skipna=False.

```
>>> df[['col5', 'col6']].all(skipna=False)
col5    False
col6    False
dtype: bool

```


Include only boolean columns when set bool\_only=True.

```
>>> df.all(bool_only=True)
col1     True
col2    False
dtype: bool

```


# pyspark.pandas.DataFrame.any — PySpark 4.0.1 documentation
DataFrame.any(_axis\=0_, _bool\_only\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.any)
[#](#pyspark.pandas.DataFrame.any "Permalink to this definition")

Return whether any element is True.

Returns False unless there is at least one element within a series that is True or equivalent (e.g. non-zero or non-empty).

Parameters

**axis**{0 or ‘index’}, default 0

Indicate which axis or axes should be reduced.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    

**bool\_only**bool, default None

Include only boolean columns. If None, will attempt to use everything, then use only boolean data.

Returns

Series

Examples

Create a dataframe from a dictionary.

```
>>> df = ps.DataFrame({
...    'col1': [False, False, False],
...    'col2': [True, False, False],
...    'col3': [0, 0, 1],
...    'col4': [0, 1, 2],
...    'col5': [False, False, None],
...    'col6': [True, False, None]},
...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

```


Default behavior checks if column-wise values all return True.

```
>>> df.any()
col1    False
col2     True
col3     True
col4     True
col5    False
col6     True
dtype: bool

```


Include only boolean columns when set bool\_only=True.

```
>>> df.any(bool_only=True)
col1    False
col2     True
dtype: bool

```


Returns empty Series when the DataFrame is empty. >>> df\[\[\]\].any() Series(\[\], dtype: bool)

# pyspark.pandas.DataFrame.any — PySpark 4.0.1 documentation
DataFrame.any(_axis\=0_, _bool\_only\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.any)
[#](#pyspark.pandas.DataFrame.any "Permalink to this definition")

Return whether any element is True.

Returns False unless there is at least one element within a series that is True or equivalent (e.g. non-zero or non-empty).

Parameters

**axis**{0 or ‘index’}, default 0

Indicate which axis or axes should be reduced.

*   0 / ‘index’ : reduce the index, return a Series whose index is the original column labels.
    

**bool\_only**bool, default None

Include only boolean columns. If None, will attempt to use everything, then use only boolean data.

Returns

Series

Examples

Create a dataframe from a dictionary.

```
>>> df = ps.DataFrame({
...    'col1': [False, False, False],
...    'col2': [True, False, False],
...    'col3': [0, 0, 1],
...    'col4': [0, 1, 2],
...    'col5': [False, False, None],
...    'col6': [True, False, None]},
...    columns=['col1', 'col2', 'col3', 'col4', 'col5', 'col6'])

```


Default behavior checks if column-wise values all return True.

```
>>> df.any()
col1    False
col2     True
col3     True
col4     True
col5    False
col6     True
dtype: bool

```


Include only boolean columns when set bool\_only=True.

```
>>> df.any(bool_only=True)
col1    False
col2     True
dtype: bool

```


Returns empty Series when the DataFrame is empty. >>> df\[\[\]\].any() Series(\[\], dtype: bool)

# pyspark.pandas.DataFrame.clip — PySpark 4.0.1 documentation
DataFrame.clip(_lower\=None_, _upper\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.clip)
[#](#pyspark.pandas.DataFrame.clip "Permalink to this definition")

Trim values at input threshold(s).

Assigns values outside boundary-to-boundary values.

Parameters

**lower**float or int, default None

Minimum threshold value. All values below this threshold will be set to it.

**upper**float or int, default None

Maximum threshold value. All values above this threshold will be set to it.

Returns

DataFrame

DataFrame with the values outside the clip boundaries replaced.

Notes

One difference between this implementation and pandas is that running pd.DataFrame({‘A’: \[‘a’, ‘b’\]}).clip(0, 1) will crash with “TypeError: ‘<=’ not supported between instances of ‘str’ and ‘int’” while ps.DataFrame({‘A’: \[‘a’, ‘b’\]}).clip(0, 1) will output the original DataFrame, simply ignoring the incompatible types.

Examples

```
>>> ps.DataFrame({'A': [0, 2, 4]}).clip(1, 3)
   A
0  1
1  2
2  3

```


# pyspark.pandas.DataFrame.corr — PySpark 4.0.1 documentation
DataFrame.corr(_method\='pearson'_, _min\_periods\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.corr)
[#](#pyspark.pandas.DataFrame.corr "Permalink to this definition")

Compute pairwise correlation of columns, excluding NA/null values.

New in version 3.3.0.

Parameters

**method**{‘pearson’, ‘spearman’, ‘kendall’}

*   pearson : standard correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   kendall : Kendall Tau correlation coefficient
    

Changed in version 3.4.0: support ‘kendall’ for method parameter

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result.

New in version 3.4.0.

Returns

DataFrame

Notes

1.  Pearson, Kendall and Spearman correlation are currently computed using pairwise complete observations.
    
2.  The complexity of Kendall correlation is O(#row \* #row), if the dataset is too large, sampling ahead of correlation computation is recommended.
    

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
...                   columns=['dogs', 'cats'])
>>> df.corr('pearson')
          dogs      cats
dogs  1.000000 -0.851064
cats -0.851064  1.000000

```


```
>>> df.corr('spearman')
          dogs      cats
dogs  1.000000 -0.948683
cats -0.948683  1.000000

```


```
>>> df.corr('kendall')
          dogs      cats
dogs  1.000000 -0.912871
cats -0.912871  1.000000

```

# pyspark.pandas.DataFrame.corrwith — PySpark 4.0.1 documentation
DataFrame.corrwith(_other_, _axis\=0_, _drop\=False_, _method\='pearson'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.corrwith)
[#](#pyspark.pandas.DataFrame.corrwith "Permalink to this definition")

Compute pairwise correlation.

Pairwise correlation is computed between rows or columns of DataFrame with rows or columns of Series or DataFrame. DataFrames are first aligned along both axes before computing the correlations.

New in version 3.4.0.

Parameters

**other**DataFrame, Series

Object with which to compute correlations.

**axis**int, default 0 or ‘index’

Can only be set to 0 now.

**drop**bool, default False

Drop missing indices from result.

**method**{‘pearson’, ‘spearman’, ‘kendall’}

*   pearson : standard correlation coefficient
    
*   spearman : Spearman rank correlation
    
*   kendall : Kendall Tau correlation coefficient
    

Returns

Series

Pairwise correlations.

Examples

```
>>> df1 = ps.DataFrame({
...         "A":[1, 5, 7, 8],
...         "X":[5, 8, 4, 3],
...         "C":[10, 4, 9, 3]})
>>> df1.corrwith(df1[["X", "C"]]).sort_index()
A    NaN
C    1.0
X    1.0
dtype: float64

```


```
>>> df2 = ps.DataFrame({
...         "A":[5, 3, 6, 4],
...         "B":[11, 2, 4, 3],
...         "C":[4, 3, 8, 5]})

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     df1.corrwith(df2).sort_index()
A   -0.041703
B         NaN
C    0.395437
X         NaN
dtype: float64

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     df1.corrwith(df2, method="kendall").sort_index()
A    0.0
B    NaN
C    0.0
X    NaN
dtype: float64

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     df1.corrwith(df2.B, method="spearman").sort_index()
A   -0.4
C    0.8
X   -0.2
dtype: float64

```


```
>>> with ps.option_context("compute.ops_on_diff_frames", True):
...     df2.corrwith(df1.X).sort_index()
A   -0.597614
B   -0.151186
C   -0.642857
dtype: float64

```


# pyspark.pandas.DataFrame.count — PySpark 4.0.1 documentation
DataFrame.count(_axis\=None_, _numeric\_only\=False_)
[#](#pyspark.pandas.DataFrame.count "Permalink to this definition")

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


# pyspark.pandas.DataFrame.cov — PySpark 4.0.1 documentation
DataFrame.cov(_min\_periods\=None_, _ddof\=1_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.cov)
[#](#pyspark.pandas.DataFrame.cov "Permalink to this definition")

Compute pairwise covariance of columns, excluding NA/null values.

Compute the pairwise covariance among the series of a DataFrame. The returned data frame is the [covariance matrix](https://en.wikipedia.org/wiki/Covariance_matrix) of the columns of the DataFrame.

Both NA and null values are automatically excluded from the calculation. (See the note below about bias from missing values.) A threshold can be set for the minimum number of observations for each value created. Comparisons with observations below this threshold will be returned as `NaN`.

This method is generally used for the analysis of time series data to understand the relationship between different measures across time.

New in version 3.3.0.

Parameters

**min\_periods**int, optional

Minimum number of observations required per pair of columns to have a valid result.

**ddof**int, default 1

Delta degrees of freedom. The divisor used in calculations is `N - ddof`, where `N` represents the number of elements.

New in version 3.4.0.

Returns

DataFrame

The covariance matrix of the series of the DataFrame.

See also

[`Series.cov`](about:blank/pyspark.pandas.Series.cov.html#pyspark.pandas.Series.cov "pyspark.pandas.Series.cov")

Compute covariance with another Series.

Examples

```
>>> df = ps.DataFrame([(1, 2), (0, 3), (2, 0), (1, 1)],
...                   columns=['dogs', 'cats'])
>>> df.cov()
          dogs      cats
dogs  0.666667 -1.000000
cats -1.000000  1.666667

```


```
>>> np.random.seed(42)
>>> df = ps.DataFrame(np.random.randn(1000, 5),
...                   columns=['a', 'b', 'c', 'd', 'e'])
>>> df.cov()
          a         b         c         d         e
a  0.998438 -0.020161  0.059277 -0.008943  0.014144
b -0.020161  1.059352 -0.008543 -0.024738  0.009826
c  0.059277 -0.008543  1.010670 -0.001486 -0.000271
d -0.008943 -0.024738 -0.001486  0.921297 -0.013692
e  0.014144  0.009826 -0.000271 -0.013692  0.977795
>>> df.cov(ddof=2)
          a         b         c         d         e
a  0.999439 -0.020181  0.059336 -0.008952  0.014159
b -0.020181  1.060413 -0.008551 -0.024762  0.009836
c  0.059336 -0.008551  1.011683 -0.001487 -0.000271
d -0.008952 -0.024762 -0.001487  0.922220 -0.013705
e  0.014159  0.009836 -0.000271 -0.013705  0.978775
>>> df.cov(ddof=-1)
  a         b         c         d         e
a  0.996444 -0.020121  0.059158 -0.008926  0.014116
b -0.020121  1.057235 -0.008526 -0.024688  0.009807
c  0.059158 -0.008526  1.008650 -0.001483 -0.000270
d -0.008926 -0.024688 -0.001483  0.919456 -0.013664
e  0.014116  0.009807 -0.000270 -0.013664  0.975842

```


**Minimum number of periods**

This method also supports an optional `min_periods` keyword that specifies the required minimum number of non-NA observations for each column pair to have a valid result:

```
>>> np.random.seed(42)
>>> df = pd.DataFrame(np.random.randn(20, 3),
...                   columns=['a', 'b', 'c'])
>>> df.loc[df.index[:5], 'a'] = np.nan
>>> df.loc[df.index[5:10], 'b'] = np.nan
>>> sdf = ps.from_pandas(df)
>>> sdf.cov(min_periods=12)
          a         b         c
a  0.316741       NaN -0.150812
b       NaN  1.248003  0.191417
c -0.150812  0.191417  0.895202

```


# pyspark.pandas.DataFrame.describe — PySpark 4.0.1 documentation
DataFrame.describe(_percentiles\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.describe)
[#](#pyspark.pandas.DataFrame.describe "Permalink to this definition")

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

# pyspark.pandas.DataFrame.ewm — PySpark 4.0.1 documentation
DataFrame.ewm(_com\=None_, _span\=None_, _halflife\=None_, _alpha\=None_, _min\_periods\=None_, _ignore\_na\=False_)
[#](#pyspark.pandas.DataFrame.ewm "Permalink to this definition")

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

# pyspark.pandas.DataFrame.kurt — PySpark 4.0.1 documentation
DataFrame.kurt(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.kurt "Permalink to this definition")

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


# pyspark.pandas.DataFrame.kurtosis — PySpark 4.0.1 documentation
DataFrame.kurtosis(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.kurtosis "Permalink to this definition")

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
# pyspark.pandas.DataFrame.max — PySpark 4.0.1 documentation
DataFrame.max(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.max "Permalink to this definition")

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

# pyspark.pandas.DataFrame.mean — PySpark 4.0.1 documentation
DataFrame.mean(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.mean "Permalink to this definition")

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


# pyspark.pandas.DataFrame.min — PySpark 4.0.1 documentation
DataFrame.min(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.min "Permalink to this definition")

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


# pyspark.pandas.DataFrame.median — PySpark 4.0.1 documentation
DataFrame.median(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _accuracy\=10000_)
[#](#pyspark.pandas.DataFrame.median "Permalink to this definition")

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


# pyspark.pandas.DataFrame.mode — PySpark 4.0.1 documentation
DataFrame.mode(_axis\=0_, _numeric\_only\=False_, _dropna\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.mode)
[#](#pyspark.pandas.DataFrame.mode "Permalink to this definition")

Get the mode(s) of each element along the selected axis.

The mode of a set of values is the value that appears most often. It can be multiple values.

New in version 3.4.0.

Parameters

**axis**{0 or ‘index’}, default 0

Axis for the function to be applied on.

**numeric\_only**bool, default False

If True, only apply to numeric columns.

**dropna**bool, default True

Don’t consider counts of NaN/NaT.

Returns

DataFrame

The modes of each column or row.

Examples

```
>>> df = ps.DataFrame([('bird', 2, 2),
...                    ('mammal', 4, np.nan),
...                    ('arthropod', 8, 0),
...                    ('bird', 2, np.nan)],
...                   index=('falcon', 'horse', 'spider', 'ostrich'),
...                   columns=('species', 'legs', 'wings'))
>>> df
           species  legs  wings
falcon        bird     2    2.0
horse       mammal     4    NaN
spider   arthropod     8    0.0
ostrich       bird     2    NaN

```


By default missing values are not considered, and the mode of wings are both 0 and 2. Because the resulting DataFrame has two rows, the second row of `species` and `legs` contains `NaN`.

```
>>> df.mode()
  species  legs  wings
0    bird   2.0    0.0
1    None   NaN    2.0

```


Setting `dropna=False` `NaN` values are considered and they can be the mode (like for wings).

```
>>> df.mode(dropna=False)
  species  legs  wings
0    bird     2    NaN

```


Setting `numeric_only=True`, only the mode of numeric columns is computed, and columns of other types are ignored.

```
>>> df.mode(numeric_only=True)
   legs  wings
0   2.0    0.0
1   NaN    2.0

```


# pyspark.pandas.DataFrame.pct_change — PySpark 4.0.1 documentation
DataFrame.pct\_change(_periods\=1_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.pct_change)
[#](#pyspark.pandas.DataFrame.pct_change "Permalink to this definition")

Percentage change between the current and a prior element.

Note

the current implementation of this API uses Spark’s Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**periods**int, default 1

Periods to shift for forming percent change.

Returns

DataFrame

Examples

Percentage change in French franc, Deutsche Mark, and Italian lira from 1980-01-01 to 1980-03-01.

```
>>> df = ps.DataFrame({
...     'FR': [4.0405, 4.0963, 4.3149],
...     'GR': [1.7246, 1.7482, 1.8519],
...     'IT': [804.74, 810.01, 860.13]},
...     index=['1980-01-01', '1980-02-01', '1980-03-01'])
>>> df
                FR      GR      IT
1980-01-01  4.0405  1.7246  804.74
1980-02-01  4.0963  1.7482  810.01
1980-03-01  4.3149  1.8519  860.13

```


```
>>> df.pct_change()
                  FR        GR        IT
1980-01-01       NaN       NaN       NaN
1980-02-01  0.013810  0.013684  0.006549
1980-03-01  0.053365  0.059318  0.061876

```


You can set periods to shift for forming percent change

```
>>> df.pct_change(2)
                  FR        GR       IT
1980-01-01       NaN       NaN      NaN
1980-02-01       NaN       NaN      NaN
1980-03-01  0.067912  0.073814  0.06883

```

# pyspark.pandas.DataFrame.prod — PySpark 4.0.1 documentation
DataFrame.prod(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _min\_count\=0_)
[#](#pyspark.pandas.DataFrame.prod "Permalink to this definition")

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


# pyspark.pandas.DataFrame.product — PySpark 4.0.1 documentation
DataFrame.product(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _min\_count\=0_)
[#](#pyspark.pandas.DataFrame.product "Permalink to this definition")

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

# pyspark.pandas.DataFrame.quantile — PySpark 4.0.1 documentation
DataFrame.quantile(_q\=0.5_, _axis\=0_, _numeric\_only\=False_, _accuracy\=10000_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.quantile)
[#](#pyspark.pandas.DataFrame.quantile "Permalink to this definition")

Return value at the given quantile.

Note

Unlike pandas’, the quantile in pandas-on-Spark is an approximated quantile based upon approximate percentile computation because computing quantile across a large dataset is extremely expensive.

Parameters

**q**float or array-like, default 0.5 (50% quantile)

0 <= q <= 1, the quantile(s) to compute.

**axis**int or str, default 0 or ‘index’

Can only be set to 0 now.

**numeric\_only**bool, default False

Include only float, int or boolean data.

Changed in version 4.0.0: The default value of `numeric_only` is now `False`.

**accuracy**int, optional

Default accuracy of approximation. Larger value means better accuracy. The relative error can be deduced by 1.0 / accuracy.

Returns

Series or DataFrame

If q is an array, a DataFrame will be returned where the index is q, the columns are the columns of self, and the values are the quantiles. If q is a float, a Series will be returned where the index is the columns of self and the values are the quantiles.

Examples

```
>>> psdf = ps.DataFrame({'a': [1, 2, 3, 4, 5], 'b': [6, 7, 8, 9, 0]})
>>> psdf
   a  b
0  1  6
1  2  7
2  3  8
3  4  9
4  5  0

```


```
>>> psdf.quantile(.5)
a    3.0
b    7.0
Name: 0.5, dtype: float64

```


```
>>> psdf.quantile([.25, .5, .75])
        a    b
0.25  2.0  6.0
0.50  3.0  7.0
0.75  4.0  8.0

```

# pyspark.pandas.DataFrame.rank — PySpark 4.0.1 documentation
DataFrame.rank(_method\='average'_, _ascending\=True_, _numeric\_only\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rank)
[#](#pyspark.pandas.DataFrame.rank "Permalink to this definition")

Compute numerical data ranks (1 through n) along axis. Equal values are assigned a rank that is the average of the ranks of those values.

Note

the current implementation of rank uses Spark’s Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

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
>>> df = ps.DataFrame({'A': [1, 2, 2, 3], 'B': [4, 3, 2, 1]}, columns=['A', 'B'])
>>> df
   A  B
0  1  4
1  2  3
2  2  2
3  3  1

```


```
>>> df.rank().sort_index()
     A    B
0  1.0  4.0
1  2.5  3.0
2  2.5  2.0
3  4.0  1.0

```


If method is set to ‘min’, it uses lowest rank in group.

```
>>> df.rank(method='min').sort_index()
     A    B
0  1.0  4.0
1  2.0  3.0
2  2.0  2.0
3  4.0  1.0

```


If method is set to ‘max’, it uses highest rank in group.

```
>>> df.rank(method='max').sort_index()
     A    B
0  1.0  4.0
1  3.0  3.0
2  3.0  2.0
3  4.0  1.0

```


If method is set to ‘dense’, it leaves no gaps in group.

```
>>> df.rank(method='dense').sort_index()
     A    B
0  1.0  4.0
1  2.0  3.0
2  2.0  2.0
3  3.0  1.0

```


If numeric\_only is set to ‘True’, rank only numeric columns.

```
>>> df = ps.DataFrame({'A': [1, 2, 2, 3], 'B': ['a', 'b', 'd', 'c']}, columns= ['A', 'B'])
>>> df
   A  B
0  1  a
1  2  b
2  2  d
3  3  c
>>> df.rank(numeric_only=True)
     A
0  1.0
1  2.5
2  2.5
3  4.0

```


# pyspark.pandas.DataFrame.nunique — PySpark 4.0.1 documentation
DataFrame.nunique(_axis\=0_, _dropna\=True_, _approx\=False_, _rsd\=0.05_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.nunique)
[#](#pyspark.pandas.DataFrame.nunique "Permalink to this definition")

Return number of unique elements in the object.

Excludes NA values by default.

Parameters

**axis**int, default 0 or ‘index’

Can only be set to 0 now.

**dropna**bool, default True

Don’t include NaN in the count.

**approx: bool, default False**

If False, will use the exact algorithm and return the exact number of unique. If True, it uses the HyperLogLog approximate algorithm, which is significantly faster for large amounts of data. Note: This parameter is specific to pandas-on-Spark and is not found in pandas.

**rsd: float, default 0.05**

Maximum estimation error allowed in the HyperLogLog algorithm. Note: Just like `approx` this parameter is specific to pandas-on-Spark.

Returns

The number of unique values per column as a pandas-on-Spark Series.

Examples

```
>>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [np.nan, 3, np.nan]})
>>> df.nunique()
A    3
B    1
dtype: int64

```


```
>>> df.nunique(dropna=False)
A    3
B    2
dtype: int64

```


On big data, we recommend using the approximate algorithm to speed up this function. The result will be very close to the exact unique count.

```
>>> df.nunique(approx=True)
A    3
B    1
dtype: int64

```

# pyspark.pandas.DataFrame.sem — PySpark 4.0.1 documentation
DataFrame.sem(_axis\=None_, _skipna\=True_, _ddof\=1_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.sem "Permalink to this definition")

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



# pyspark.pandas.DataFrame.skew — PySpark 4.0.1 documentation
DataFrame.skew(_axis\=None_, _skipna\=True_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.skew "Permalink to this definition")

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

# pyspark.pandas.DataFrame.sum — PySpark 4.0.1 documentation
DataFrame.sum(_axis\=None_, _skipna\=True_, _numeric\_only\=None_, _min\_count\=0_)
[#](#pyspark.pandas.DataFrame.sum "Permalink to this definition")

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


# pyspark.pandas.DataFrame.std — PySpark 4.0.1 documentation
DataFrame.std(_axis\=None_, _skipna\=True_, _ddof\=1_, _numeric\_only\=None_)
[#](#pyspark.pandas.DataFrame.std "Permalink to this definition")

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

# pyspark.pandas.DataFrame.cummin — PySpark 4.0.1 documentation
DataFrame.cummin(_skipna\=True_)
[#](#pyspark.pandas.DataFrame.cummin "Permalink to this definition")

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



# pyspark.pandas.DataFrame.cummax — PySpark 4.0.1 documentation
DataFrame.cummax(_skipna\=True_)
[#](#pyspark.pandas.DataFrame.cummax "Permalink to this definition")

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

# pyspark.pandas.DataFrame.cumsum — PySpark 4.0.1 documentation
DataFrame.cumsum(_skipna\=True_)
[#](#pyspark.pandas.DataFrame.cumsum "Permalink to this definition")

Return cumulative sum over a DataFrame or Series axis.

Returns a DataFrame or Series of the same size containing the cumulative sum.

Note

the current implementation of cumsum uses Spark’s Window without specifying partition specification. This leads to moveing all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

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


By default, iterates over rows and finds the sum in each column.

```
>>> df.cumsum()
     A    B
0  2.0  1.0
1  5.0  NaN
2  6.0  1.0

```


It works identically in Series.

```
>>> df.A.cumsum()
0    2.0
1    5.0
2    6.0
Name: A, dtype: float64

```

# pyspark.pandas.DataFrame.cumprod — PySpark 4.0.1 documentation
DataFrame.cumprod(_skipna\=True_)
[#](#pyspark.pandas.DataFrame.cumprod "Permalink to this definition")

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
# pyspark.pandas.DataFrame.round — PySpark 4.0.1 documentation
DataFrame.round(_decimals\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.round)
[#](#pyspark.pandas.DataFrame.round "Permalink to this definition")

Round a DataFrame to a variable number of decimal places.

Parameters

**decimals**int, dict, Series

Number of decimal places to round each column to. If an int is given, round each column to the same number of places. Otherwise dict and Series round to variable numbers of places. Column names should be in the keys if decimals is a dict-like, or in the index if decimals is a Series. Any columns not included in decimals will be left as is. Elements of decimals which are not columns of the input will be ignored.

Note

If decimals is a Series, it is expected to be small, as all the data is loaded into the driver’s memory.

Returns

DataFrame

Examples

```
>>> df = ps.DataFrame({'A':[0.028208, 0.038683, 0.877076],
...                    'B':[0.992815, 0.645646, 0.149370],
...                    'C':[0.173891, 0.577595, 0.491027]},
...                    columns=['A', 'B', 'C'],
...                    index=['first', 'second', 'third'])
>>> df
               A         B         C
first   0.028208  0.992815  0.173891
second  0.038683  0.645646  0.577595
third   0.877076  0.149370  0.491027

```


```
>>> df.round(2)
           A     B     C
first   0.03  0.99  0.17
second  0.04  0.65  0.58
third   0.88  0.15  0.49

```


```
>>> df.round({'A': 1, 'C': 2})
          A         B     C
first   0.0  0.992815  0.17
second  0.0  0.645646  0.58
third   0.9  0.149370  0.49

```


```
>>> decimals = ps.Series([1, 0, 2], index=['A', 'B', 'C'])
>>> df.round(decimals)
          A    B     C
first   0.0  1.0  0.17
second  0.0  1.0  0.58
third   0.9  0.0  0.49

```
# pyspark.pandas.DataFrame.diff — PySpark 4.0.1 documentation
DataFrame.diff(_periods\=1_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.diff)
[#](#pyspark.pandas.DataFrame.diff "Permalink to this definition")

First discrete difference of element.

Calculates the difference of a DataFrame element compared with another element in the DataFrame (default is the element in the same column of the previous row).

Note

the current implementation of diff uses Spark’s Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**periods**int, default 1

Periods to shift for calculating difference, accepts negative values.

**axis**int, default 0 or ‘index’

Can only be set to 0 now.

Returns

**diffed**DataFrame

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
>>> df.diff()
     a    b     c
0  NaN  NaN   NaN
1  1.0  0.0   3.0
2  1.0  1.0   5.0
3  1.0  1.0   7.0
4  1.0  2.0   9.0
5  1.0  3.0  11.0

```


Difference with previous column

```
>>> df.diff(periods=3)
     a    b     c
0  NaN  NaN   NaN
1  NaN  NaN   NaN
2  NaN  NaN   NaN
3  3.0  2.0  15.0
4  3.0  4.0  21.0
5  3.0  6.0  27.0

```


Difference with following row

```
>>> df.diff(periods=-1)
     a    b     c
0 -1.0  0.0  -3.0
1 -1.0 -1.0  -5.0
2 -1.0 -1.0  -7.0
3 -1.0 -2.0  -9.0
4 -1.0 -3.0 -11.0
5  NaN  NaN   NaN

```
# pyspark.pandas.DataFrame.eval — PySpark 4.0.1 documentation
DataFrame.eval(_expr_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.eval)
[#](#pyspark.pandas.DataFrame.eval "Permalink to this definition")

Evaluate a string describing operations on DataFrame columns.

Operates on columns only, not specific rows or elements. This allows eval to run arbitrary code, which can make you vulnerable to code injection if you pass user input to this function.

Parameters

**expr**str

The expression string to evaluate.

**inplace**bool, default False

If the expression contains an assignment, whether to perform the operation inplace and mutate the existing DataFrame. Otherwise, a new DataFrame is returned.

Returns

The result of the evaluation.

See also

[`DataFrame.query`](about:blank/pyspark.pandas.DataFrame.query.html#pyspark.pandas.DataFrame.query "pyspark.pandas.DataFrame.query")

Evaluates a boolean expression to query the columns of a frame.

[`DataFrame.assign`](about:blank/pyspark.pandas.DataFrame.assign.html#pyspark.pandas.DataFrame.assign "pyspark.pandas.DataFrame.assign")

Can evaluate an expression or function to create new values for a column.

[`eval`](#pyspark.pandas.DataFrame.eval "pyspark.pandas.DataFrame.eval")

Evaluate a Python expression as a string using various backends.

Examples

```
>>> df = ps.DataFrame({'A': range(1, 6), 'B': range(10, 0, -2)})
>>> df
   A   B
0  1  10
1  2   8
2  3   6
3  4   4
4  5   2
>>> df.eval('A + B')
0    11
1    10
2     9
3     8
4     7
dtype: int64

```


Assignment is allowed though by default the original DataFrame is not modified.

```
>>> df.eval('C = A + B')
   A   B   C
0  1  10  11
1  2   8  10
2  3   6   9
3  4   4   8
4  5   2   7
>>> df
   A   B
0  1  10
1  2   8
2  3   6
3  4   4
4  5   2

```


Use `inplace=True` to modify the original DataFrame.

```
>>> df.eval('C = A + B', inplace=True)
>>> df
   A   B   C
0  1  10  11
1  2   8  10
2  3   6   9
3  4   4   8
4  5   2   7

```
# pyspark.pandas.DataFrame.add_prefix — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.add\_prefix

DataFrame.add\_prefix(_prefix_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.add_prefix)
[#](#pyspark.pandas.DataFrame.add_prefix "Permalink to this definition")

Prefix labels with string prefix.

For Series, the row labels are prefixed. For DataFrame, the column labels are prefixed.

Parameters

**prefix**str

The string to add before each label.

Returns

DataFrame

New DataFrame with updated labels.

Examples

```
>>> df = ps.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]}, columns=['A', 'B'])
>>> df
   A  B
0  1  3
1  2  4
2  3  5
3  4  6

```


```
>>> df.add_prefix('col_')
   col_A  col_B
0      1      3
1      2      4
2      3      5
3      4      6

```
# pyspark.pandas.DataFrame.add_suffix — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.add\_suffix

DataFrame.add\_suffix(_suffix_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.add_suffix)
[#](#pyspark.pandas.DataFrame.add_suffix "Permalink to this definition")

Suffix labels with string suffix.

For Series, the row labels are suffixed. For DataFrame, the column labels are suffixed.

Parameters

**suffix**str

The string to add before each label.

Returns

DataFrame

New DataFrame with updated labels.

Examples

```
>>> df = ps.DataFrame({'A': [1, 2, 3, 4], 'B': [3, 4, 5, 6]}, columns=['A', 'B'])
>>> df
   A  B
0  1  3
1  2  4
2  3  5
3  4  6

```


```
>>> df.add_suffix('_col')
   A_col  B_col
0      1      3
1      2      4
2      3      5
3      4      6

```
# pyspark.pandas.DataFrame.align — PySpark 4.0.1 documentation
DataFrame.align(_other_, _join\='outer'_, _axis\=None_, _copy\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.align)
[#](#pyspark.pandas.DataFrame.align "Permalink to this definition")

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

**(left, right)**(DataFrame, type of other)

Aligned objects.

Examples

```
>>> ps.set_option("compute.ops_on_diff_frames", True)
>>> df1 = ps.DataFrame({"a": [1, 2, 3], "b": ["a", "b", "c"]}, index=[10, 20, 30])
>>> df2 = ps.DataFrame({"a": [4, 5, 6], "c": ["d", "e", "f"]}, index=[10, 11, 12])

```


Align both axis:

```
>>> aligned_l, aligned_r = df1.align(df2)
>>> aligned_l.sort_index()
      a     b   c
10  1.0     a NaN
11  NaN  None NaN
12  NaN  None NaN
20  2.0     b NaN
30  3.0     c NaN
>>> aligned_r.sort_index()
      a   b     c
10  4.0 NaN     d
11  5.0 NaN     e
12  6.0 NaN     f
20  NaN NaN  None
30  NaN NaN  None

```


Align only axis=0 (index):

```
>>> aligned_l, aligned_r = df1.align(df2, axis=0)
>>> aligned_l.sort_index()
      a     b
10  1.0     a
11  NaN  None
12  NaN  None
20  2.0     b
30  3.0     c
>>> aligned_r.sort_index()
      a     c
10  4.0     d
11  5.0     e
12  6.0     f
20  NaN  None
30  NaN  None

```


Align only axis=1 (column):

```
>>> aligned_l, aligned_r = df1.align(df2, axis=1)
>>> aligned_l.sort_index()
    a  b   c
10  1  a NaN
20  2  b NaN
30  3  c NaN
>>> aligned_r.sort_index()
    a   b  c
10  4 NaN  d
11  5 NaN  e
12  6 NaN  f

```


Align with the join type “inner”:

```
>>> aligned_l, aligned_r = df1.align(df2, join="inner")
>>> aligned_l.sort_index()
    a
10  1
>>> aligned_r.sort_index()
    a
10  4

```


Align with a Series:

```
>>> s = ps.Series([7, 8, 9], index=[10, 11, 12])
>>> aligned_l, aligned_r = df1.align(s, axis=0)
>>> aligned_l.sort_index()
      a     b
10  1.0     a
11  NaN  None
12  NaN  None
20  2.0     b
30  3.0     c
>>> aligned_r.sort_index()
10    7.0
11    8.0
12    9.0
20    NaN
30    NaN
dtype: float64

```


```
>>> ps.reset_option("compute.ops_on_diff_frames")

```
# pyspark.pandas.DataFrame.at_time — PySpark 4.0.1 documentation
DataFrame.at\_time(_time_, _asof\=False_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.at_time)
[#](#pyspark.pandas.DataFrame.at_time "Permalink to this definition")

Select values at particular time of day (example: 9:30AM).

Parameters

**time**datetime.time or str

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Returns

DataFrame

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

Examples

```
>>> idx = pd.date_range('2018-04-09', periods=4, freq='12H')
>>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=idx)
>>> psdf
                     A
2018-04-09 00:00:00  1
2018-04-09 12:00:00  2
2018-04-10 00:00:00  3
2018-04-10 12:00:00  4

```


```
>>> psdf.at_time('12:00')
                     A
2018-04-09 12:00:00  2
2018-04-10 12:00:00  4

```
# pyspark.pandas.DataFrame.between_time — PySpark 4.0.1 documentation
DataFrame.between\_time(_start\_time_, _end\_time_, _inclusive\='both'_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.between_time)
[#](#pyspark.pandas.DataFrame.between_time "Permalink to this definition")

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

DataFrame

Data from the original object filtered to the specified dates range.

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

See also

[`at_time`](about:blank/pyspark.pandas.DataFrame.at_time.html#pyspark.pandas.DataFrame.at_time "pyspark.pandas.DataFrame.at_time")

Select values at a particular time of the day.

[`first`](about:blank/pyspark.pandas.DataFrame.first.html#pyspark.pandas.DataFrame.first "pyspark.pandas.DataFrame.first")

Select initial periods of time series based on a date offset.

[`last`](about:blank/pyspark.pandas.DataFrame.last.html#pyspark.pandas.DataFrame.last "pyspark.pandas.DataFrame.last")

Select final periods of time series based on a date offset.

[`DatetimeIndex.indexer_between_time`](about:blank/pyspark.pandas.DatetimeIndex.indexer_between_time.html#pyspark.pandas.DatetimeIndex.indexer_between_time "pyspark.pandas.DatetimeIndex.indexer_between_time")

Get just the index locations for values between particular times of the day.

Examples

```
>>> idx = pd.date_range('2018-04-09', periods=4, freq='1D20min')
>>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=idx)
>>> psdf
                     A
2018-04-09 00:00:00  1
2018-04-10 00:20:00  2
2018-04-11 00:40:00  3
2018-04-12 01:00:00  4

```


```
>>> psdf.between_time('0:15', '0:45')  
                     A
2018-04-10 00:20:00  2
2018-04-11 00:40:00  3

```


You get the times that are _not_ between two times by setting `start_time` later than `end_time`:

```
>>> psdf.between_time('0:45', '0:15')  
                     A
2018-04-09 00:00:00  1
2018-04-12 01:00:00  4

```
# pyspark.pandas.DataFrame.drop — PySpark 4.0.1 documentation
DataFrame.drop(_labels\=None_, _axis\=0_, _index\=None_, _columns\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.drop)
[#](#pyspark.pandas.DataFrame.drop "Permalink to this definition")

Drop specified labels from columns.

Remove rows and/or columns by specifying label names and corresponding axis, or by specifying directly index and/or column names. Drop rows of a MultiIndex DataFrame is not supported yet.

Parameters

**labels**single label or list-like

Column labels to drop.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Changed in version 3.3: Set dropping by index is default.

**index**single label or list-like

Alternative to specifying axis (`labels, axis=0` is equivalent to `index=columns`).

Changed in version 3.3: Added dropping rows by ‘index’.

**columns**single label or list-like

Alternative to specifying axis (`labels, axis=1` is equivalent to `columns=labels`).

Returns

**dropped**DataFrame

Notes

Currently, dropping rows of a MultiIndex DataFrame is not supported yet.

Examples

```
>>> df = ps.DataFrame(np.arange(12).reshape(3, 4), columns=['A', 'B', 'C', 'D'])
>>> df
   A  B   C   D
0  0  1   2   3
1  4  5   6   7
2  8  9  10  11

```


Drop columns

```
>>> df.drop(['B', 'C'], axis=1)
   A   D
0  0   3
1  4   7
2  8  11

```


```
>>> df.drop(columns=['B', 'C'])
   A   D
0  0   3
1  4   7
2  8  11

```


Drop a row by index

```
>>> df.drop([0, 1])
   A  B   C   D
2  8  9  10  11

```


```
>>> df.drop(index=[0, 1], columns='A')
   B   C   D
2  9  10  11

```


Also support dropping columns for MultiIndex

```
>>> df = ps.DataFrame({'x': [1, 2], 'y': [3, 4], 'z': [5, 6], 'w': [7, 8]},
...                   columns=['x', 'y', 'z', 'w'])
>>> columns = [('a', 'x'), ('a', 'y'), ('b', 'z'), ('b', 'w')]
>>> df.columns = pd.MultiIndex.from_tuples(columns)
>>> df  
   a     b
   x  y  z  w
0  1  3  5  7
1  2  4  6  8
>>> df.drop(labels='a', axis=1)  
   b
   z  w
0  5  7
1  6  8

```
# pyspark.pandas.DataFrame.droplevel — PySpark 4.0.1 documentation
DataFrame.droplevel(_level_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.droplevel)
[#](#pyspark.pandas.DataFrame.droplevel "Permalink to this definition")

Return DataFrame with requested index / column level(s) removed.

Parameters

**level: int, str, or list-like**

If a string is given, must be the name of a level If list-like, elements must be names or positional indexes of levels.

**axis: {0 or ‘index’, 1 or ‘columns’}, default 0**

Returns

DataFrame with requested index / column level(s) removed.

Examples

```
>>> df = ps.DataFrame(
...     [[3, 4], [7, 8], [11, 12]],
...     index=pd.MultiIndex.from_tuples([(1, 2), (5, 6), (9, 10)], names=["a", "b"]),
... )

```


```
>>> df.columns = pd.MultiIndex.from_tuples([
...   ('c', 'e'), ('d', 'f')
... ], names=['level_1', 'level_2'])

```


```
>>> df  
level_1   c   d
level_2   e   f
a b
1 2      3   4
5 6      7   8
9 10    11  12

```


```
>>> df.droplevel('a')  
level_1   c   d
level_2   e   f
b
2        3   4
6        7   8
10      11  12

```


```
>>> df.droplevel('level_2', axis=1)  
level_1   c   d
a b
1 2      3   4
5 6      7   8
9 10    11  12

```
# pyspark.pandas.DataFrame.drop_duplicates — PySpark 4.0.1 documentation
DataFrame.drop\_duplicates(_subset\=None_, _keep\='first'_, _inplace\=False_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.drop_duplicates)
[#](#pyspark.pandas.DataFrame.drop_duplicates "Permalink to this definition")

Return DataFrame with duplicate rows removed, optionally only considering certain columns.

Parameters

**subset**column label or sequence of labels, optional

Only consider certain columns for identifying duplicates, by default use all the columns.

**keep**{‘first’, ‘last’, False}, default ‘first’

Determines which duplicates (if any) to keep. - `first` : Drop duplicates except for the first occurrence. - `last` : Drop duplicates except for the last occurrence. - False : Drop all duplicates.

**inplace**boolean, default False

Whether to drop duplicates in place or to return a copy.

**ignore\_index**boolean, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

Returns

DataFrame

DataFrame with duplicates removed or None if `inplace=True`.

```
>>> df = ps.DataFrame(
    ..

```


… {‘a’: \[1, 2, 2, 2, 3\], ‘b’: \[‘a’, ‘a’, ‘a’, ‘c’, ‘d’\]}, columns = \[‘a’, ‘b’\])

0 1 a

1 2 a

2 2 a

3 2 c

4 3 d

```
>>> df.drop_duplicates().sort_index()
    a  b

```


0 1 a

1 2 a

3 2 c

4 3 d

```
>>> df.drop_duplicates(ignore_index=True).sort_index()
    a  b

```


0 1 a

1 2 a

2 2 c

3 3 d

```
>>> df.drop_duplicates('a').sort_index()
    a  b

```


0 1 a

1 2 a

4 3 d

```
>>> df.drop_duplicates(['a', 'b']).sort_index()
    a  b

```


0 1 a

1 2 a

3 2 c

4 3 d

```
>>> df.drop_duplicates(keep='last').sort_index()
    a  b

```


0 1 a

2 2 a

3 2 c

4 3 d

```
>>> df.drop_duplicates(keep=False).sort_index()
    a  b

```


0 1 a

3 2 c

4 3 d

# pyspark.pandas.DataFrame.duplicated — PySpark 4.0.1 documentation
DataFrame.duplicated(_subset\=None_, _keep\='first'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.duplicated)
[#](#pyspark.pandas.DataFrame.duplicated "Permalink to this definition")

Return boolean Series denoting duplicate rows, optionally only considering certain columns.

Parameters

**subset**column label or sequence of labels, optional

Only consider certain columns for identifying duplicates, default use all of the columns

**keep**{‘first’, ‘last’, False}, default ‘first’

*   `first` : Mark duplicates as `True` except for the first occurrence.
    
*   `last` : Mark duplicates as `True` except for the last occurrence.
    
*   False : Mark all duplicates as `True`.
    

Returns

**duplicated**Series

Examples

```
>>> df = ps.DataFrame({'a': [1, 1, 1, 3], 'b': [1, 1, 1, 4], 'c': [1, 1, 1, 5]},
...                   columns = ['a', 'b', 'c'])
>>> df
   a  b  c
0  1  1  1
1  1  1  1
2  1  1  1
3  3  4  5

```


```
>>> df.duplicated().sort_index()
0    False
1     True
2     True
3    False
dtype: bool

```


Mark duplicates as `True` except for the last occurrence.

```
>>> df.duplicated(keep='last').sort_index()
0     True
1     True
2    False
3    False
dtype: bool

```


Mark all duplicates as `True`.

```
>>> df.duplicated(keep=False).sort_index()
0     True
1     True
2     True
3    False
dtype: bool

```

# pyspark.pandas.DataFrame.equals — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.equals

DataFrame.equals(_other_)
[#](#pyspark.pandas.DataFrame.equals "Permalink to this definition")

Compare if the current value is equal to the other.

```
>>> df = ps.DataFrame({'a': [1, 2, 3, 4],
...                    'b': [1, np.nan, 1, np.nan]},
...                   index=['a', 'b', 'c', 'd'], columns=['a', 'b'])

```


```
>>> df.eq(1)
       a      b
a   True   True
b  False  False
c  False   True
d  False  False

```


# pyspark.pandas.DataFrame.filter — PySpark 4.0.1 documentation
DataFrame.filter(_items\=None_, _like\=None_, _regex\=None_, _axis\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.filter)
[#](#pyspark.pandas.DataFrame.filter "Permalink to this definition")

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


urltomarkdowncodeblockplaceholder30.843850660231092

For a Series,

urltomarkdowncodeblockplaceholder40.9813817971492913

urltomarkdowncodeblockplaceholder50.008435145525377274

urltomarkdowncodeblockplaceholder60.3525073096071758)
mouse    1
Name: one, dtype: int64

```


urltomarkdowncodeblockplaceholder60.3525073096071758, axis=1)
        one  three
mouse     1      3
rabbit    4      6

```


urltomarkdowncodeblockplaceholder30.843850660231092

For a Series,

urltomarkdowncodeblockplaceholder40.9813817971492913

urltomarkdowncodeblockplaceholder50.008435145525377274

urltomarkdowncodeblockplaceholder60.3525073096071758

# pyspark.pandas.DataFrame.first — PySpark 4.0.1 documentation
DataFrame.first(_offset_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.first)
[#](#pyspark.pandas.DataFrame.first "Permalink to this definition")

Select first periods of time series data based on a date offset.

When having a DataFrame with dates as index, this function can select the first few rows based on a date offset.

Deprecated since version 4.0.0.

Parameters

**offset**str or DateOffset

The offset length of the data that will be selected. For instance, ‘3D’ will display all the rows having their index within the first 3 days.

Returns

DataFrame

A subset of the caller.

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

Examples

```
>>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
>>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=index)
>>> psdf
            A
2018-04-09  1
2018-04-11  2
2018-04-13  3
2018-04-15  4

```


Get the rows for the last 3 days:

```
>>> psdf.first('3D')
            A
2018-04-09  1
2018-04-11  2

```


Notice the data for 3 first calendar days were returned, not the first 3 observed days in the dataset, and therefore data for 2018-04-13 was not returned.


# pyspark.pandas.DataFrame.head — PySpark 4.0.1 documentation
DataFrame.head(_n\=5_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.head)
[#](#pyspark.pandas.DataFrame.head "Permalink to this definition")

Return the first n rows.

This function returns the first n rows for the object based on position. It is useful for quickly testing if your object has the right type of data in it.

Parameters

**n**int, default 5

Number of rows to select.

Returns

**obj\_head**same type as caller

The first n rows of the caller object.

Examples

```
>>> df = ps.DataFrame({'animal':['alligator', 'bee', 'falcon', 'lion',
...                    'monkey', 'parrot', 'shark', 'whale', 'zebra']})
>>> df
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey
5     parrot
6      shark
7      whale
8      zebra

```


Viewing the first 5 lines

```
>>> df.head()
      animal
0  alligator
1        bee
2     falcon
3       lion
4     monkey

```


Viewing the first n lines (three in this case)

```
>>> df.head(3)
      animal
0  alligator
1        bee
2     falcon

```


# pyspark.pandas.DataFrame.last — PySpark 4.0.1 documentation
DataFrame.last(_offset_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.last)
[#](#pyspark.pandas.DataFrame.last "Permalink to this definition")

Select final periods of time series data based on a date offset.

When having a DataFrame with dates as index, this function can select the last few rows based on a date offset.

Deprecated since version 4.0.0.

Parameters

**offset**str or DateOffset

The offset length of the data that will be selected. For instance, ‘3D’ will display all the rows having their index within the last 3 days.

Returns

DataFrame

A subset of the caller.

Raises

TypeError

If the index is not a [`DatetimeIndex`](about:blank/pyspark.pandas.DatetimeIndex.html#pyspark.pandas.DatetimeIndex "pyspark.pandas.DatetimeIndex")

Examples

```
>>> index = pd.date_range('2018-04-09', periods=4, freq='2D')
>>> psdf = ps.DataFrame({'A': [1, 2, 3, 4]}, index=index)
>>> psdf
            A
2018-04-09  1
2018-04-11  2
2018-04-13  3
2018-04-15  4

```


Get the rows for the last 3 days:

```
>>> psdf.last('3D')
            A
2018-04-13  3
2018-04-15  4

```


Notice the data for 3 last calendar days were returned, not the last 3 observed days in the dataset, and therefore data for 2018-04-11 was not returned.


# pyspark.pandas.DataFrame.reindex — PySpark 4.0.1 documentation
DataFrame.reindex(_labels\=None_, _index\=None_, _columns\=None_, _axis\=None_, _copy\=True_, _fill\_value\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.reindex)
[#](#pyspark.pandas.DataFrame.reindex "Permalink to this definition")

Conform DataFrame to new index with optional filling logic, placing NA/NaN in locations having no value in the previous index. A new object is produced unless the new index is equivalent to the current one and `copy=False`.

Parameters

**labels: array-like, optional**

New labels / index to conform the axis specified by ‘axis’ to.

**index, columns: array-like, optional**

New labels / index to conform to, should be specified using keywords. Preferably an Index object to avoid duplicating data

**axis: int or str, optional**

Axis to target. Can be either the axis name (‘index’, ‘columns’) or number (0, 1).

**copy**bool, default True

Return a new object, even if the passed indexes are the same.

**fill\_value**scalar, default np.nan

Value to use for missing values. Defaults to NaN, but can be any “compatible” value.

Returns

DataFrame with changed index.

Examples

`DataFrame.reindex` supports two calling conventions

*   `(index=index_labels, columns=column_labels, ...)`
    
*   `(labels, axis={'index', 'columns'}, ...)`
    

We _highly_ recommend using keyword arguments to clarify your intent.

Create a dataframe with some fictional data.

```
>>> index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
>>> df = ps.DataFrame({
...      'http_status': [200, 200, 404, 404, 301],
...      'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]},
...       index=index,
...       columns=['http_status', 'response_time'])
>>> df
           http_status  response_time
Firefox            200           0.04
Chrome             200           0.02
Safari             404           0.07
IE10               404           0.08
Konqueror          301           1.00

```


Create a new index and reindex the dataframe. By default values in the new index that do not have corresponding records in the dataframe are assigned `NaN`.

```
>>> new_index= ['Safari', 'Iceweasel', 'Comodo Dragon', 'IE10',
...             'Chrome']
>>> df.reindex(new_index).sort_index()
               http_status  response_time
Chrome               200.0           0.02
Comodo Dragon          NaN            NaN
IE10                 404.0           0.08
Iceweasel              NaN            NaN
Safari               404.0           0.07

```


We can fill in the missing values by passing a value to the keyword `fill_value`.

```
>>> df.reindex(new_index, fill_value=0, copy=False).sort_index()
               http_status  response_time
Chrome                 200           0.02
Comodo Dragon            0           0.00
IE10                   404           0.08
Iceweasel                0           0.00
Safari                 404           0.07

```


We can also reindex the columns.

```
>>> df.reindex(columns=['http_status', 'user_agent']).sort_index()
           http_status  user_agent
Chrome             200         NaN
Firefox            200         NaN
IE10               404         NaN
Konqueror          301         NaN
Safari             404         NaN

```


Or we can use “axis-style” keyword arguments

```
>>> df.reindex(['http_status', 'user_agent'], axis="columns").sort_index()
           http_status  user_agent
Chrome             200         NaN
Firefox            200         NaN
IE10               404         NaN
Konqueror          301         NaN
Safari             404         NaN

```


To further illustrate the filling functionality in `reindex`, we will create a dataframe with a monotonically increasing index (for example, a sequence of dates).

```
>>> date_index = pd.date_range('1/1/2010', periods=6, freq='D')
>>> df2 = ps.DataFrame({"prices": [100, 101, np.nan, 100, 89, 88]},
...                    index=date_index)
>>> df2.sort_index()
            prices
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0

```


Suppose we decide to expand the dataframe to cover a wider date range.

```
>>> date_index2 = pd.date_range('12/29/2009', periods=10, freq='D')
>>> df2.reindex(date_index2).sort_index()
            prices
2009-12-29     NaN
2009-12-30     NaN
2009-12-31     NaN
2010-01-01   100.0
2010-01-02   101.0
2010-01-03     NaN
2010-01-04   100.0
2010-01-05    89.0
2010-01-06    88.0
2010-01-07     NaN

```


# pyspark.pandas.DataFrame.reindex_like — PySpark 4.0.1 documentation
DataFrame.reindex\_like(_other_, _copy\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.reindex_like)
[#](#pyspark.pandas.DataFrame.reindex_like "Permalink to this definition")

Return a DataFrame with matching indices as other object.

Conform the object to the same index on all axes. Places NA/NaN in locations having no value in the previous index. A new object is produced unless the new index is equivalent to the current one and copy=False.

Parameters

**other**DataFrame

Its row and column indices are used to define the new indices of this object.

**copy**bool, default True

Return a new object, even if the passed indexes are the same.

Returns

DataFrame

DataFrame with changed indices on each axis.

Notes

Same as calling `.reindex(index=other.index, columns=other.columns,...)`.

Examples

```
>>> df1 = ps.DataFrame([[24.3, 75.7, 'high'],
...                     [31, 87.8, 'high'],
...                     [22, 71.6, 'medium'],
...                     [35, 95, 'medium']],
...                    columns=['temp_celsius', 'temp_fahrenheit',
...                             'windspeed'],
...                    index=pd.date_range(start='2014-02-12',
...                                        end='2014-02-15', freq='D'))
>>> df1
            temp_celsius  temp_fahrenheit windspeed
2014-02-12          24.3             75.7      high
2014-02-13          31.0             87.8      high
2014-02-14          22.0             71.6    medium
2014-02-15          35.0             95.0    medium

```


```
>>> df2 = ps.DataFrame([[28, 'low'],
...                     [30, 'low'],
...                     [35.1, 'medium']],
...                    columns=['temp_celsius', 'windspeed'],
...                    index=pd.DatetimeIndex(['2014-02-12', '2014-02-13',
...                                            '2014-02-15']))
>>> df2
            temp_celsius windspeed
2014-02-12          28.0       low
2014-02-13          30.0       low
2014-02-15          35.1    medium

```


```
>>> df2.reindex_like(df1).sort_index() 
            temp_celsius  temp_fahrenheit windspeed
2014-02-12          28.0              NaN       low
2014-02-13          30.0              NaN       low
2014-02-14           NaN              NaN       None
2014-02-15          35.1              NaN    medium

```


# pyspark.pandas.DataFrame.rename — PySpark 4.0.1 documentation
DataFrame.rename(_mapper\=None_, _index\=None_, _columns\=None_, _axis\='index'_, _inplace\=False_, _level\=None_, _errors\='ignore'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rename)
[#](#pyspark.pandas.DataFrame.rename "Permalink to this definition")

Alter axes labels. Function / dict values must be unique (1-to-1). Labels not contained in a dict / Series will be left as-is. Extra labels listed don’t throw an error.

Parameters

**mapper**dict-like or function

Dict-like or functions transformations to apply to that axis’ values. Use either mapper and axis to specify the axis to target with mapper, or index and columns.

**index**dict-like or function

Alternative to specifying axis (“mapper, axis=0” is equivalent to “index=mapper”).

**columns**dict-like or function

Alternative to specifying axis (“mapper, axis=1” is equivalent to “columns=mapper”).

**axis**int or str, default ‘index’

Axis to target with mapper. Can be either the axis name (‘index’, ‘columns’) or number (0, 1).

**inplace**bool, default False

Whether to return a new DataFrame.

**level**int or level name, default None

In case of a MultiIndex, only rename labels in the specified level.

**errors**{‘ignore’, ‘raise’}, default ‘ignore’

If ‘raise’, raise a KeyError when a dict-like mapper, index, or columns contains labels that are not present in the Index being transformed. If ‘ignore’, existing keys will be renamed, and extra keys will be ignored.

Returns

DataFrame with the renamed axis labels.

Raises

KeyError

If any of the labels is not found in the selected axis and “errors=’raise’”.

Examples

```
>>> psdf1 = ps.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
>>> psdf1.rename(columns={"A": "a", "B": "c"})  
   a  c
0  1  4
1  2  5
2  3  6

```


```
>>> psdf1.rename(index={1: 10, 2: 20})  
    A  B
0   1  4
10  2  5
20  3  6

```


```
>>> psdf1.rename(columns={"A": "a", "C": "c"}, errors="raise")
Traceback (most recent call last):
    ...
KeyError: 'Index include value which is not in the `mapper`'

```


```
>>> def str_lower(s) -> str:
...     return str.lower(s)
>>> psdf1.rename(str_lower, axis='columns')  
   a  b
0  1  4
1  2  5
2  3  6

```


```
>>> def mul10(x) -> int:
...     return x * 10
>>> psdf1.rename(mul10, axis='index')  
    A  B
0   1  4
10  2  5
20  3  6

```


```
>>> idx = pd.MultiIndex.from_tuples([('X', 'A'), ('X', 'B'), ('Y', 'C'), ('Y', 'D')])
>>> psdf2 = ps.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]], columns=idx)
>>> psdf2.rename(columns=str_lower, level=0)  
   x     y
   A  B  C  D
0  1  2  3  4
1  5  6  7  8

```


```
>>> psdf3 = ps.DataFrame([[1, 2], [3, 4], [5, 6], [7, 8]], index=idx, columns=list('ab'))
>>> psdf3.rename(index=str_lower)  
     a  b
x a  1  2
  b  3  4
y c  5  6
  d  7  8

```

# pyspark.pandas.DataFrame.rename_axis — PySpark 4.0.1 documentation
DataFrame.rename\_axis(_mapper\=None_, _index\=None_, _columns\=None_, _axis\=0_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.rename_axis)
[#](#pyspark.pandas.DataFrame.rename_axis "Permalink to this definition")

Set the name of the axis for the index or columns.

Parameters

**mapper**scalar, list-like, optional

A scalar, list-like, dict-like or functions transformations to apply to the axis name attribute.

**index, columns**scalar, list-like, dict-like or function, optional

A scalar, list-like, dict-like or functions transformations to apply to that axis’ values.

Use either `mapper` and `axis` to specify the axis to target with `mapper`, or `index` and/or `columns`.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to rename.

**inplace**bool, default False

Modifies the object directly, instead of creating a new DataFrame.

Returns

DataFrame, or None if inplace is True.

Notes

`DataFrame.rename_axis` supports two calling conventions

*   `(index=index_mapper, columns=columns_mapper, ...)`
    
*   `(mapper, axis={'index', 'columns'}, ...)`
    

The first calling convention will only modify the names of the index and/or the names of the Index object that is the columns.

The second calling convention will modify the names of the corresponding index specified by axis.

We _highly_ recommend using keyword arguments to clarify your intent.

Examples

```
>>> df = ps.DataFrame({"num_legs": [4, 4, 2],
...                    "num_arms": [0, 0, 2]},
...                   index=["dog", "cat", "monkey"],
...                   columns=["num_legs", "num_arms"])
>>> df
        num_legs  num_arms
dog            4         0
cat            4         0
monkey         2         2

```


```
>>> df = df.rename_axis("animal").sort_index()
>>> df  
        num_legs  num_arms
animal
cat            4         0
dog            4         0
monkey         2         2

```


```
>>> df = df.rename_axis("limbs", axis="columns").sort_index()
>>> df 
limbs   num_legs  num_arms
animal
cat            4         0
dog            4         0
monkey         2         2

```


**MultiIndex**

```
>>> index = pd.MultiIndex.from_product([['mammal'],
...                                     ['dog', 'cat', 'monkey']],
...                                    names=['type', 'name'])
>>> df = ps.DataFrame({"num_legs": [4, 4, 2],
...                    "num_arms": [0, 0, 2]},
...                   index=index,
...                   columns=["num_legs", "num_arms"])
>>> df  
               num_legs  num_arms
type   name
mammal dog            4         0
       cat            4         0
       monkey         2         2

```


```
>>> df.rename_axis(index={'type': 'class'}).sort_index()  
               num_legs  num_arms
class  name
mammal cat            4         0
       dog            4         0
       monkey         2         2

```


```
>>> df.rename_axis(index=str.upper).sort_index()  
               num_legs  num_arms
TYPE   NAME
mammal cat            4         0
       dog            4         0
       monkey         2         2

```


# pyspark.pandas.DataFrame.reset_index — PySpark 4.0.1 documentation
DataFrame.reset\_index(_level\=None_, _drop\=False_, _inplace\=False_, _col\_level\=0_, _col\_fill\=''_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.reset_index)
[#](#pyspark.pandas.DataFrame.reset_index "Permalink to this definition")

Reset the index, or a level of it.

For DataFrame with multi-level index, return new DataFrame with labeling information in the columns under the index names, defaulting to ‘level\_0’, ‘level\_1’, etc. if any are None. For a standard index, the index name will be used (if set), otherwise a default ‘index’ or ‘level\_0’ (if ‘index’ is already taken) will be used.

Parameters

**level**int, str, tuple, or list, default None

Only remove the given levels from the index. Removes all levels by default.

**drop**bool, default False

Do not try to insert index into dataframe columns. This reset the index to the default integer index.

**inplace**bool, default False

Modify the DataFrame in place (do not create a new object).

**col\_level**int or str, default 0

If the columns have multiple levels, determines which level the labels are inserted into. By default it is inserted into the first level.

**col\_fill**object, default ‘’

If the columns have multiple levels, determines how the other levels are named. If None then the index name is repeated.

Returns

DataFrame

DataFrame with the new index.

Examples

```
>>> df = ps.DataFrame([('bird', 389.0),
...                    ('bird', 24.0),
...                    ('mammal', 80.5),
...                    ('mammal', np.nan)],
...                   index=['falcon', 'parrot', 'lion', 'monkey'],
...                   columns=('class', 'max_speed'))
>>> df
         class  max_speed
falcon    bird      389.0
parrot    bird       24.0
lion    mammal       80.5
monkey  mammal        NaN

```


When we reset the index, the old index is added as a column. Unlike pandas, pandas-on-Spark does not automatically add a sequential index. The following 0, 1, 2, 3 are only there when we display the DataFrame.

```
>>> df.reset_index()
    index   class  max_speed
0  falcon    bird      389.0
1  parrot    bird       24.0
2    lion  mammal       80.5
3  monkey  mammal        NaN

```


We can use the drop parameter to avoid the old index being added as a column:

```
>>> df.reset_index(drop=True)
    class  max_speed
0    bird      389.0
1    bird       24.0
2  mammal       80.5
3  mammal        NaN

```


You can also use reset\_index with MultiIndex.

```
>>> index = pd.MultiIndex.from_tuples([('bird', 'falcon'),
...                                    ('bird', 'parrot'),
...                                    ('mammal', 'lion'),
...                                    ('mammal', 'monkey')],
...                                   names=['class', 'name'])
>>> columns = pd.MultiIndex.from_tuples([('speed', 'max'),
...                                      ('species', 'type')])
>>> df = ps.DataFrame([(389.0, 'fly'),
...                    ( 24.0, 'fly'),
...                    ( 80.5, 'run'),
...                    (np.nan, 'jump')],
...                   index=index,
...                   columns=columns)
>>> df  
               speed species
                 max    type
class  name
bird   falcon  389.0     fly
       parrot   24.0     fly
mammal lion     80.5     run
       monkey    NaN    jump

```


If the index has multiple levels, we can reset a subset of them:

```
>>> df.reset_index(level='class')  
         class  speed species
                  max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump

```


If we are not dropping the index, by default, it is placed in the top level. We can place it in another level:

```
>>> df.reset_index(level='class', col_level=1)  
                speed species
         class    max    type
name
falcon    bird  389.0     fly
parrot    bird   24.0     fly
lion    mammal   80.5     run
monkey  mammal    NaN    jump

```


When the index is inserted under another level, we can specify under which one with the parameter col\_fill:

```
>>> df.reset_index(level='class', col_level=1,
...                col_fill='species')  
              species  speed species
                class    max    type
name
falcon           bird  389.0     fly
parrot           bird   24.0     fly
lion           mammal   80.5     run
monkey         mammal    NaN    jump

```


If we specify a nonexistent level for col\_fill, it is created:

```
>>> df.reset_index(level='class', col_level=1,
...                col_fill='genus')  
                genus  speed species
                class    max    type
name
falcon           bird  389.0     fly
parrot           bird   24.0     fly
lion           mammal   80.5     run
monkey         mammal    NaN    jump

```


# pyspark.pandas.DataFrame.set_index — PySpark 4.0.1 documentation
DataFrame.set\_index(_keys_, _drop\=True_, _append\=False_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.set_index)
[#](#pyspark.pandas.DataFrame.set_index "Permalink to this definition")

Set the DataFrame index (row labels) using one or more existing columns.

Set the DataFrame index (row labels) using one or more existing columns or arrays (of the correct length). The index can replace the existing index or expand on it.

Parameters

**keys**label or array-like or list of labels/arrays

This parameter can be either a single column key, a single array of the same length as the calling DataFrame, or a list containing an arbitrary combination of column keys and arrays. Here, “array” encompasses [`Series`](about:blank/pyspark.pandas.Series.html#pyspark.pandas.Series "pyspark.pandas.Series"), [`Index`](about:blank/pyspark.pandas.Index.html#pyspark.pandas.Index "pyspark.pandas.Index") and `np.ndarray`.

**drop**bool, default True

Delete columns to be used as the new index.

**append**bool, default False

Whether to append columns to existing index.

**inplace**bool, default False

Modify the DataFrame in place (do not create a new object).

Returns

DataFrame

Changed row labels.

Examples

```
>>> df = ps.DataFrame({'month': [1, 4, 7, 10],
...                    'year': [2012, 2014, 2013, 2014],
...                    'sale': [55, 40, 84, 31]},
...                   columns=['month', 'year', 'sale'])
>>> df
   month  year  sale
0      1  2012    55
1      4  2014    40
2      7  2013    84
3     10  2014    31

```


Set the index to become the ‘month’ column:

```
>>> df.set_index('month')  
       year  sale
month
1      2012    55
4      2014    40
7      2013    84
10     2014    31

```


Create a MultiIndex using columns ‘year’ and ‘month’:

```
>>> df.set_index(['year', 'month'])  
            sale
year  month
2012  1     55
2014  4     40
2013  7     84
2014  10    31

```


# pyspark.pandas.DataFrame.swapaxes — PySpark 4.0.1 documentation
DataFrame.swapaxes(_i_, _j_, _copy\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.swapaxes)
[#](#pyspark.pandas.DataFrame.swapaxes "Permalink to this definition")

Interchange axes and swap values axes appropriately.

Note

This method is based on an expensive operation due to the nature of big data. Internally it needs to generate each row for each value, and then group twice - it is a huge operation. To prevent misuse, this method has the ‘compute.max\_rows’ default limit of input length and raises a ValueError.

```
>>> from pyspark.pandas.config import option_context
>>> with option_context('compute.max_rows', 1000):  
...     ps.DataFrame({'a': range(1001)}).swapaxes(i=0, j=1)
Traceback (most recent call last):
  ...
ValueError: Current DataFrame's length exceeds the given limit of 1000 rows.
Please set 'compute.max_rows' by using 'pyspark.pandas.config.set_option'
to retrieve more than 1000 rows. Note that, before changing the
'compute.max_rows', this operation is considerably expensive.

```


Parameters

**i: {0 or ‘index’, 1 or ‘columns’}. The axis to swap.**

**j: {0 or ‘index’, 1 or ‘columns’}. The axis to swap.**

**copy**bool, default True.

Returns

DataFrame

Examples

```
>>> psdf = ps.DataFrame(
...     [[1, 2, 3], [4, 5, 6], [7, 8, 9]], index=['x', 'y', 'z'], columns=['a', 'b', 'c']
... )
>>> psdf
   a  b  c
x  1  2  3
y  4  5  6
z  7  8  9
>>> psdf.swapaxes(i=1, j=0)
   x  y  z
a  1  4  7
b  2  5  8
c  3  6  9
>>> psdf.swapaxes(i=1, j=1)
   a  b  c
x  1  2  3
y  4  5  6
z  7  8  9

```


# pyspark.pandas.DataFrame.swaplevel — PySpark 4.0.1 documentation
DataFrame.swaplevel(_i\=\- 2_, _j\=\- 1_, _axis\=0_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.swaplevel)
[#](#pyspark.pandas.DataFrame.swaplevel "Permalink to this definition")

Swap levels i and j in a MultiIndex on a particular axis.

Parameters

**i, j**int or str

Levels of the indices to be swapped. Can pass level name as string.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

The axis to swap levels on. 0 or ‘index’ for row-wise, 1 or ‘columns’ for column-wise.

Returns

DataFrame

DataFrame with levels swapped in MultiIndex.

Examples

```
>>> midx = pd.MultiIndex.from_arrays(
...     [['red', 'blue'], [1, 2], ['s', 'm']], names = ['color', 'number', 'size'])
>>> midx  
MultiIndex([( 'red', 1, 's'),
            ('blue', 2, 'm')],
           names=['color', 'number', 'size'])

```


Swap levels in a MultiIndex on index.

```
>>> psdf = ps.DataFrame({'x': [5, 6], 'y':[5, 6]}, index=midx)
>>> psdf  
                   x  y
color number size
red   1      s     5  5
blue  2      m     6  6

```


```
>>> psdf.swaplevel()  
                   x  y
color size number
red   s    1       5  5
blue  m    2       6  6

```


```
>>> psdf.swaplevel(0, 1)  
                   x  y
number color size
1      red   s     5  5
2      blue  m     6  6

```


```
>>> psdf.swaplevel('number', 'size')  
                   x  y
color size number
red   s    1       5  5
blue  m    2       6  6

```


Swap levels in a MultiIndex on columns.

```
>>> psdf = ps.DataFrame({'x': [5, 6], 'y':[5, 6]})
>>> psdf.columns = midx
>>> psdf
color  red blue
number   1    2
size     s    m
0        5    5
1        6    6

```


```
>>> psdf.swaplevel(axis=1)
color  red blue
size     s    m
number   1    2
0        5    5
1        6    6

```


```
>>> psdf.swaplevel(axis=1)
color  red blue
size     s    m
number   1    2
0        5    5
1        6    6

```


```
>>> psdf.swaplevel(0, 1, axis=1)
number   1    2
color  red blue
size     s    m
0        5    5
1        6    6

```


```
>>> psdf.swaplevel('number', 'color', axis=1)
number   1    2
color  red blue
size     s    m
0        5    5
1        6    6

```


# pyspark.pandas.DataFrame.take — PySpark 4.0.1 documentation
DataFrame.take(_indices_, _axis\=0_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.take)
[#](#pyspark.pandas.DataFrame.take "Permalink to this definition")

Return the elements in the given _positional_ indices along an axis.

This means that we are not indexing according to actual values in the index attribute of the object. We are indexing according to the actual position of the element in the object.

Parameters

**indices**array-like

An array of ints indicating which positions to take.

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default 0

The axis on which to select elements. `0` means that we are selecting rows, `1` means that we are selecting columns.

**\*\*kwargs**

For compatibility with `numpy.take()`. Has no effect on the output.

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

```
>>> df = ps.DataFrame([('falcon', 'bird', 389.0),
...                    ('parrot', 'bird', 24.0),
...                    ('lion', 'mammal', 80.5),
...                    ('monkey', 'mammal', np.nan)],
...                   columns=['name', 'class', 'max_speed'],
...                   index=[0, 2, 3, 1])
>>> df
     name   class  max_speed
0  falcon    bird      389.0
2  parrot    bird       24.0
3    lion  mammal       80.5
1  monkey  mammal        NaN

```


Take elements at positions 0 and 3 along the axis 0 (default).

Note how the actual indices selected (0 and 1) do not correspond to our selected indices 0 and 3. That’s because we are selecting the 0th and 3rd rows, not rows whose indices equal 0 and 3.

```
>>> df.take([0, 3]).sort_index()
     name   class  max_speed
0  falcon    bird      389.0
1  monkey  mammal        NaN

```


Take elements at indices 1 and 2 along the axis 1 (column selection).

```
>>> df.take([1, 2], axis=1)
    class  max_speed
0    bird      389.0
2    bird       24.0
3  mammal       80.5
1  mammal        NaN

```


We may take elements using negative integers for positive indices, starting from the end of the object, just like with Python lists.

```
>>> df.take([-1, -2]).sort_index()
     name   class  max_speed
1  monkey  mammal        NaN
3    lion  mammal       80.5

```

# pyspark.pandas.DataFrame.isin — PySpark 4.0.1 documentation
DataFrame.isin(_values_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.isin)
[#](#pyspark.pandas.DataFrame.isin "Permalink to this definition")

Whether each element in the DataFrame is contained in values.

Parameters

**values**iterable or dict

The sequence of values to test. If values are a dict, the keys must be the column names, which must match. Series and DataFrame are not supported.

Returns

DataFrame

DataFrame of booleans showing whether each element in the DataFrame is contained in values.

Examples

```
>>> df = ps.DataFrame({'num_legs': [2, 4], 'num_wings': [2, 0]},
...                   index=['falcon', 'dog'],
...                   columns=['num_legs', 'num_wings'])
>>> df
        num_legs  num_wings
falcon         2          2
dog            4          0

```


When `values` is a list check whether every value in the DataFrame is present in the list (which animals have 0 or 2 legs or wings)

```
>>> df.isin([0, 2])
        num_legs  num_wings
falcon      True       True
dog        False       True

```


When `values` is a dict, we can pass values to check for each column separately:

```
>>> df.isin({'num_wings': [0, 3]})
        num_legs  num_wings
falcon     False      False
dog        False       True

```


# pyspark.pandas.DataFrame.sample — PySpark 4.0.1 documentation
DataFrame.sample(_n\=None_, _frac\=None_, _replace\=False_, _random\_state\=None_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.sample)
[#](#pyspark.pandas.DataFrame.sample "Permalink to this definition")

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




# pyspark.pandas.DataFrame.truncate — PySpark 4.0.1 documentation
DataFrame.truncate(_before\=None_, _after\=None_, _axis\=None_, _copy\=True_)
[#](#pyspark.pandas.DataFrame.truncate "Permalink to this definition")

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

# pyspark.pandas.DataFrame.backfill — PySpark 4.0.1 documentation
DataFrame.backfill(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.DataFrame.backfill "Permalink to this definition")

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


# pyspark.pandas.DataFrame.dropna — PySpark 4.0.1 documentation
DataFrame.dropna(_axis\=0_, _how\='any'_, _thresh\=None_, _subset\=None_, _inplace\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.dropna)
[#](#pyspark.pandas.DataFrame.dropna "Permalink to this definition")

Remove missing values.

Parameters

**axis**{0 or ‘index’}, default 0

Determine if rows or columns which contain missing values are removed.

*   0, or ‘index’ : Drop rows which contain missing values.
    

**how**{‘any’, ‘all’}, default ‘any’

Determine if row or column is removed from DataFrame, when we have at least one NA or all NA.

*   ‘any’ : If any NA values are present, drop that row or column.
    
*   ‘all’ : If all values are NA, drop that row or column.
    

**thresh**int, optional

Require that many non-NA values.

**subset**array-like, optional

Labels along other axis to consider, e.g. if you are dropping rows these would be a list of columns to include.

**inplace**bool, default False

If True, do operation inplace and return None.

Returns

DataFrame

DataFrame with NA entries dropped from it.

Examples

```
>>> df = ps.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
...                    "toy": [None, 'Batmobile', 'Bullwhip'],
...                    "born": [None, "1940-04-25", None]},
...                   columns=['name', 'toy', 'born'])
>>> df
       name        toy        born
0    Alfred       None        None
1    Batman  Batmobile  1940-04-25
2  Catwoman   Bullwhip        None

```


Drop the rows where at least one element is missing.

```
>>> df.dropna()
     name        toy        born
1  Batman  Batmobile  1940-04-25

```


Drop the columns where at least one element is missing.

```
>>> df.dropna(axis='columns')
       name
0    Alfred
1    Batman
2  Catwoman

```


Drop the rows where all elements are missing.

```
>>> df.dropna(how='all')
       name        toy        born
0    Alfred       None        None
1    Batman  Batmobile  1940-04-25
2  Catwoman   Bullwhip        None

```


Keep only the rows with at least 2 non-NA values.

```
>>> df.dropna(thresh=2)
       name        toy        born
1    Batman  Batmobile  1940-04-25
2  Catwoman   Bullwhip        None

```


Define in which columns to look for missing values.

```
>>> df.dropna(subset=['name', 'born'])
     name        toy        born
1  Batman  Batmobile  1940-04-25

```


Keep the DataFrame with valid entries in the same variable.

```
>>> df.dropna(inplace=True)
>>> df
     name        toy        born
1  Batman  Batmobile  1940-04-25

```


# pyspark.pandas.DataFrame.fillna — PySpark 4.0.1 documentation
DataFrame.fillna(_value\=None_, _method\=None_, _axis\=None_, _inplace\=False_, _limit\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.fillna)
[#](#pyspark.pandas.DataFrame.fillna "Permalink to this definition")

Fill NA/NaN values.

Note

the current implementation of ‘method’ parameter in fillna uses Spark’s Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

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

DataFrame

DataFrame with NA entries filled.

Examples

```
>>> df = ps.DataFrame({
...     'A': [None, 3, None, None],
...     'B': [2, 4, None, 3],
...     'C': [None, None, None, 1],
...     'D': [0, 1, 5, 4]
...     },
...     columns=['A', 'B', 'C', 'D'])
>>> df
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  NaN  NaN  NaN  5
3  NaN  3.0  1.0  4

```


Replace all NaN elements with 0s.

```
>>> df.fillna(0)
     A    B    C  D
0  0.0  2.0  0.0  0
1  3.0  4.0  0.0  1
2  0.0  0.0  0.0  5
3  0.0  3.0  1.0  4

```


We can also propagate non-null values forward or backward.

```
>>> df.fillna(method='ffill')
     A    B    C  D
0  NaN  2.0  NaN  0
1  3.0  4.0  NaN  1
2  3.0  4.0  NaN  5
3  3.0  3.0  1.0  4

```


Replace all NaN elements in column ‘A’, ‘B’, ‘C’, and ‘D’, with 0, 1, 2, and 3 respectively.

```
>>> values = {'A': 0, 'B': 1, 'C': 2, 'D': 3}
>>> df.fillna(value=values)
     A    B    C  D
0  0.0  2.0  2.0  0
1  3.0  4.0  2.0  1
2  0.0  1.0  2.0  5
3  0.0  3.0  1.0  4

```


# pyspark.pandas.DataFrame.replace — PySpark 4.0.1 documentation
DataFrame.replace(_to\_replace\=None_, _value\=None_, _inplace\=False_, _limit\=None_, _regex\=False_, _method\='pad'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.replace)
[#](#pyspark.pandas.DataFrame.replace "Permalink to this definition")

Returns a new DataFrame replacing a value with another value.

Parameters

**to\_replace**int, float, string, list, tuple or dict

Value to be replaced.

**value**int, float, string, list or tuple

Value to use to replace holes. The replacement value must be an int, float, or string. If value is a list or tuple, value should be of the same length with to\_replace.

**inplace**boolean, default False

Fill in place (do not create a new object)

**limit**int, default None

Maximum size gap to forward or backward fill.

Deprecated since version 4.0.0.

**regex**bool or str, default False

Whether to interpret to\_replace and/or value as regular expressions. If this is True then to\_replace must be a string. Alternatively, this could be a regular expression in which case to\_replace must be None.

**method**‘pad’, default None

The method to use when for replacement, when to\_replace is a scalar, list or tuple and value is None.

Deprecated since version 4.0.0.

Returns

DataFrame

Object after replacement.

Examples

```
>>> df = ps.DataFrame({"name": ['Ironman', 'Captain America', 'Thor', 'Hulk'],
...                    "weapon": ['Mark-45', 'Shield', 'Mjolnir', 'Smash']},
...                   columns=['name', 'weapon'])
>>> df
              name   weapon
0          Ironman  Mark-45
1  Captain America   Shield
2             Thor  Mjolnir
3             Hulk    Smash

```


Scalar to\_replace and value

```
>>> df.replace('Ironman', 'War-Machine')
              name   weapon
0      War-Machine  Mark-45
1  Captain America   Shield
2             Thor  Mjolnir
3             Hulk    Smash

```


List like to\_replace and value

```
>>> df.replace(['Ironman', 'Captain America'], ['Rescue', 'Hawkeye'], inplace=True)
>>> df
      name   weapon
0   Rescue  Mark-45
1  Hawkeye   Shield
2     Thor  Mjolnir
3     Hulk    Smash

```


Dicts can be used to specify different replacement values for different existing values To use a dict in this way the value parameter should be None

```
>>> df.replace({'Mjolnir': 'Stormbuster'})
      name       weapon
0   Rescue      Mark-45
1  Hawkeye       Shield
2     Thor  Stormbuster
3     Hulk        Smash

```


Dict can specify that different values should be replaced in different columns The value parameter should not be None in this case

```
>>> df.replace({'weapon': 'Mjolnir'}, 'Stormbuster')
      name       weapon
0   Rescue      Mark-45
1  Hawkeye       Shield
2     Thor  Stormbuster
3     Hulk        Smash

```


Nested dictionaries The value parameter should be None to use a nested dict in this way

```
>>> df.replace({'weapon': {'Mjolnir': 'Stormbuster'}})
      name       weapon
0   Rescue      Mark-45
1  Hawkeye       Shield
2     Thor  Stormbuster
3     Hulk        Smash

```


# pyspark.pandas.DataFrame.bfill — PySpark 4.0.1 documentation
DataFrame.bfill(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.DataFrame.bfill "Permalink to this definition")

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


# pyspark.pandas.DataFrame.ffill — PySpark 4.0.1 documentation
DataFrame.ffill(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.DataFrame.ffill "Permalink to this definition")

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


# pyspark.pandas.DataFrame.interpolate — PySpark 4.0.1 documentation
DataFrame.interpolate(_method\='linear'_, _limit\=None_, _limit\_direction\=None_, _limit\_area\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.interpolate)
[#](#pyspark.pandas.DataFrame.interpolate "Permalink to this definition")

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

[`fillna`](about:blank/pyspark.pandas.DataFrame.fillna.html#pyspark.pandas.DataFrame.fillna "pyspark.pandas.DataFrame.fillna")

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


# pyspark.pandas.DataFrame.pad — PySpark 4.0.1 documentation
DataFrame.pad(_axis\=None_, _inplace\=False_, _limit\=None_)
[#](#pyspark.pandas.DataFrame.pad "Permalink to this definition")

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

# pyspark.pandas.DataFrame.pivot_table — PySpark 4.0.1 documentation
DataFrame.pivot\_table(_values\=None_, _index\=None_, _columns\=None_, _aggfunc\='mean'_, _fill\_value\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.pivot_table)
[#](#pyspark.pandas.DataFrame.pivot_table "Permalink to this definition")

Create a spreadsheet-style pivot table as a DataFrame. The levels in the pivot table will be stored in MultiIndex objects (hierarchical indexes) on the index and columns of the result DataFrame.

Parameters

**values**column to aggregate.

They should be either a list less than three or a string.

**index**column (string) or list of columns

If an array is passed, it must be the same length as the data. The list should contain string.

**columns**column

Columns used in the pivot operation. Only one column is supported and it should be a string.

**aggfunc**function (string), dict, default mean

If dict is passed, the key is column to aggregate and value is function or list of functions.

**fill\_value**scalar, default None

Value to replace missing values with.

Returns

**table**DataFrame

Examples

```
>>> df = ps.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
...                          "bar", "bar", "bar", "bar"],
...                    "B": ["one", "one", "one", "two", "two",
...                          "one", "one", "two", "two"],
...                    "C": ["small", "large", "large", "small",
...                          "small", "large", "small", "small",
...                          "large"],
...                    "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
...                    "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]},
...                   columns=['A', 'B', 'C', 'D', 'E'])
>>> df
     A    B      C  D  E
0  foo  one  small  1  2
1  foo  one  large  2  4
2  foo  one  large  2  5
3  foo  two  small  3  5
4  foo  two  small  3  6
5  bar  one  large  4  6
6  bar  one  small  5  8
7  bar  two  small  6  9
8  bar  two  large  7  9

```


This first example aggregates values by taking the sum.

```
>>> table = df.pivot_table(values='D', index=['A', 'B'],
...                        columns='C', aggfunc='sum')
>>> table.sort_index()  
C        large  small
A   B
bar one    4.0      5
    two    7.0      6
foo one    4.0      1
    two    NaN      6

```


We can also fill missing values using the fill\_value parameter.

```
>>> table = df.pivot_table(values='D', index=['A', 'B'],
...                        columns='C', aggfunc='sum', fill_value=0)
>>> table.sort_index()  
C        large  small
A   B
bar one      4      5
    two      7      6
foo one      4      1
    two      0      6

```


We can also calculate multiple types of aggregations for any given value column.

```
>>> table = df.pivot_table(values=['D'], index =['C'],
...                        columns="A", aggfunc={'D': 'mean'})
>>> table.sort_index()  
         D
A      bar       foo
C
large  5.5  2.000000
small  5.5  2.333333

```


The next example aggregates on multiple values.

```
>>> table = df.pivot_table(index=['C'], columns="A", values=['D', 'E'],
...                         aggfunc={'D': 'mean', 'E': 'sum'})
>>> table.sort_index() 
         D             E
A      bar       foo bar foo
C
large  5.5  2.000000  15   9
small  5.5  2.333333  17  13

```



# pyspark.pandas.DataFrame.pivot — PySpark 4.0.1 documentation
DataFrame.pivot(_index\=None_, _columns\=None_, _values\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.pivot)
[#](#pyspark.pandas.DataFrame.pivot "Permalink to this definition")

Return reshaped DataFrame organized by given index / column values.

Reshape data (produce a “pivot” table) based on column values. Uses unique values from specified index / columns to form axes of the resulting DataFrame. This function does not support data aggregation.

Parameters

**index**string, optional

Column to use to make new frame’s index. If None, uses existing index.

**columns**string

Column to use to make new frame’s columns.

**values**string, object or a list of the previous

Column(s) to use for populating new frame’s values.

Returns

DataFrame

Returns reshaped DataFrame.

See also

[`DataFrame.pivot_table`](about:blank/pyspark.pandas.DataFrame.pivot_table.html#pyspark.pandas.DataFrame.pivot_table "pyspark.pandas.DataFrame.pivot_table")

Generalization of pivot that can handle duplicate values for one index/column pair.

Examples

```
>>> df = ps.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
...                            'two'],
...                    'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
...                    'baz': [1, 2, 3, 4, 5, 6],
...                    'zoo': ['x', 'y', 'z', 'q', 'w', 't']},
...                   columns=['foo', 'bar', 'baz', 'zoo'])
>>> df
   foo bar  baz zoo
0  one   A    1   x
1  one   B    2   y
2  one   C    3   z
3  two   A    4   q
4  two   B    5   w
5  two   C    6   t

```


```
>>> df.pivot(index='foo', columns='bar', values='baz').sort_index()
... 
bar  A  B  C
foo
one  1  2  3
two  4  5  6

```


```
>>> df.pivot(columns='bar', values='baz').sort_index()  
bar  A    B    C
0  1.0  NaN  NaN
1  NaN  2.0  NaN
2  NaN  NaN  3.0
3  4.0  NaN  NaN
4  NaN  5.0  NaN
5  NaN  NaN  6.0

```


Notice that, unlike pandas raises an ValueError when duplicated values are found. Pandas-on-Spark’s pivot still works with its first value it meets during operation because pivot is an expensive operation, and it is preferred to permissively execute over failing fast when processing large data.

```
>>> df = ps.DataFrame({"foo": ['one', 'one', 'two', 'two'],
...                    "bar": ['A', 'A', 'B', 'C'],
...                    "baz": [1, 2, 3, 4]}, columns=['foo', 'bar', 'baz'])
>>> df
   foo bar  baz
0  one   A    1
1  one   A    2
2  two   B    3
3  two   C    4

```


```
>>> df.pivot(index='foo', columns='bar', values='baz').sort_index()
... 
bar    A    B    C
foo
one  1.0  NaN  NaN
two  NaN  3.0  4.0

```


It also supports multi-index and multi-index column. >>> df.columns = pd.MultiIndex.from\_tuples(\[(‘a’, ‘foo’), (‘a’, ‘bar’), (‘b’, ‘baz’)\])

```
>>> df = df.set_index(('a', 'bar'), append=True)
>>> df  
              a   b
            foo baz
  (a, bar)
0 A         one   1
1 A         one   2
2 B         two   3
3 C         two   4

```


```
>>> df.pivot(columns=('a', 'foo'), values=('b', 'baz')).sort_index()
... 
('a', 'foo')  one  two
  (a, bar)
0 A           1.0  NaN
1 A           2.0  NaN
2 B           NaN  3.0
3 C           NaN  4.0

```
# pyspark.pandas.DataFrame.sort_index — PySpark 4.0.1 documentation
DataFrame.sort\_index(_axis\=0_, _level\=None_, _ascending\=True_, _inplace\=False_, _kind\=None_, _na\_position\='last'_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.sort_index)
[#](#pyspark.pandas.DataFrame.sort_index "Permalink to this definition")

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

**sorted\_obj**DataFrame

Examples

```
>>> df = ps.DataFrame({'A': [2, 1, np.nan]}, index=['b', 'a', np.nan])

```


```
>>> df.sort_index()  
        A
a     1.0
b     2.0
None  NaN

```


```
>>> df.sort_index(ascending=False)  
        A
b     2.0
a     1.0
None  NaN

```


```
>>> df.sort_index(na_position='first')  
        A
None  NaN
a     1.0
b     2.0

```


```
>>> df.sort_index(ignore_index=True)
     A
0  1.0
1  2.0
2  NaN

```


```
>>> df.sort_index(inplace=True)
>>> df  
        A
a     1.0
b     2.0
None  NaN

```


```
>>> df = ps.DataFrame({'A': range(4), 'B': range(4)
[::-1]},
...                   index=[['b', 'b', 'a', 'a'], [1, 0, 1, 0]],
...                   columns=['A', 'B'])

```


```
>>> df.sort_index()
     A  B
a 0  3  0
  1  2  1
b 0  1  2
  1  0  3

```


```
>>> df.sort_index(level=1)
     A  B
b 0  1  2
a 0  3  0
b 1  0  3
a 1  2  1

```


```
>>> df.sort_index(level=[1, 0])
     A  B
a 0  3  0
b 0  1  2
a 1  2  1
b 1  0  3

```


```
>>> df.sort_index(ignore_index=True)
   A  B
0  3  0
1  2  1
2  1  2
3  0  3

```

# pyspark.pandas.DataFrame.sort_values — PySpark 4.0.1 documentation
DataFrame.sort\_values(_by_, _ascending\=True_, _inplace\=False_, _na\_position\='last'_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.sort_values)
[#](#pyspark.pandas.DataFrame.sort_values "Permalink to this definition")

Sort by the values along either axis.

Parameters

**by**str or list of str

**ascending**bool or list of bool, default True

Sort ascending vs. descending. Specify list for multiple sort orders. If this is a list of bools, must match the length of the by.

**inplace**bool, default False

if True, perform operation in-place

**na\_position**{‘first’, ‘last’}, default ‘last’

first puts NaNs at the beginning, last puts NaNs at the end

**ignore\_index**bool, default False

If True, the resulting axis will be labeled 0, 1, …, n - 1.

Returns

**sorted\_obj**DataFrame

Examples

```
>>> df = ps.DataFrame({
...     'col1': ['A', 'B', None, 'D', 'C'],
...     'col2': [2, 9, 8, 7, 4],
...     'col3': [0, 9, 4, 2, 3],
...   },
...   columns=['col1', 'col2', 'col3'],
...   index=['a', 'b', 'c', 'd', 'e'])
>>> df
   col1  col2  col3
a     A     2     0
b     B     9     9
c  None     8     4
d     D     7     2
e     C     4     3

```


Sort by col1

```
>>> df.sort_values(by=['col1'])
   col1  col2  col3
a     A     2     0
b     B     9     9
e     C     4     3
d     D     7     2
c  None     8     4

```


Ignore index for the resulting axis

```
>>> df.sort_values(by=['col1'], ignore_index=True)
   col1  col2  col3
0     A     2     0
1     B     9     9
2     C     4     3
3     D     7     2
4  None     8     4

```


Sort Descending

```
>>> df.sort_values(by='col1', ascending=False)
   col1  col2  col3
d     D     7     2
e     C     4     3
b     B     9     9
a     A     2     0
c  None     8     4

```


Sort by multiple columns

```
>>> df = ps.DataFrame({
...     'col1': ['A', 'A', 'B', None, 'D', 'C'],
...     'col2': [2, 1, 9, 8, 7, 4],
...     'col3': [0, 1, 9, 4, 2, 3],
...   },
...   columns=['col1', 'col2', 'col3'])
>>> df.sort_values(by=['col1', 'col2'])
   col1  col2  col3
1     A     1     1
0     A     2     0
2     B     9     9
5     C     4     3
4     D     7     2
3  None     8     4

```

# pyspark.pandas.DataFrame.nlargest — PySpark 4.0.1 documentation
DataFrame.nlargest(_n_, _columns_, _keep\='first'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.nlargest)
[#](#pyspark.pandas.DataFrame.nlargest "Permalink to this definition")

Return the first n rows ordered by columns in descending order.

Return the first n rows with the largest values in columns, in descending order. The columns that are not specified are returned as well, but not used for ordering.

This method is equivalent to `df.sort_values(columns, ascending=False).head(n)`, but more performant in pandas. In pandas-on-Spark, thanks to Spark’s lazy execution and query optimizer, the two would have same performance.

Parameters

**n**int

Number of rows to return.

**columns**label or list of labels

Column label(s) to order by.

**keep**{‘first’, ‘last’}, default ‘first’. ‘all’ is not implemented yet.

Determines which duplicates (if any) to keep. - `first` : Keep the first occurrence. - `last` : Keep the last occurrence.

Returns

DataFrame

The first n rows ordered by the given columns in descending order.

Notes

This function cannot be used with all column types. For example, when specifying columns with object or category dtypes, `TypeError` is raised.

Examples

```
>>> df = ps.DataFrame({'X': [1, 2, 3, 5, 6, 7, np.nan],
...                    'Y': [6, 7, 8, 9, 10, 11, 12]})
>>> df
     X   Y
0  1.0   6
1  2.0   7
2  3.0   8
3  5.0   9
4  6.0  10
5  7.0  11
6  NaN  12

```


In the following example, we will use `nlargest` to select the three rows having the largest values in column “X”.

```
>>> df.nlargest(n=3, columns='X')
     X   Y
5  7.0  11
4  6.0  10
3  5.0   9

```


To order by the largest values in column “Y” and then “X”, we can specify multiple columns like in the next example.

```
>>> df.nlargest(n=3, columns=['Y', 'X'])
     X   Y
6  NaN  12
5  7.0  11
4  6.0  10

```


The examples below show how ties are resolved, which is decided by keep.

```
>>> tied_df = ps.DataFrame({'X': [1, 2, 2, 3, 3]}, index=['a', 'b', 'c', 'd', 'e'])
>>> tied_df
   X
a  1
b  2
c  2
d  3
e  3

```


When using keep=’first’ (default), ties are resolved in order:

```
>>> tied_df.nlargest(3, 'X')
   X
d  3
e  3
b  2

```


```
>>> tied_df.nlargest(3, 'X', keep='first')
   X
d  3
e  3
b  2

```


When using keep=’last’, ties are resolved in reverse order:

```
>>> tied_df.nlargest(3, 'X', keep='last')
   X
e  3
d  3
c  2

```



# pyspark.pandas.DataFrame.nsmallest — PySpark 4.0.1 documentation
DataFrame.nsmallest(_n_, _columns_, _keep\='first'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.nsmallest)
[#](#pyspark.pandas.DataFrame.nsmallest "Permalink to this definition")

Return the first n rows ordered by columns in ascending order.

Return the first n rows with the smallest values in columns, in ascending order. The columns that are not specified are returned as well, but not used for ordering.

This method is equivalent to `df.sort_values(columns, ascending=True).head(n)`, but more performant. In pandas-on-Spark, thanks to Spark’s lazy execution and query optimizer, the two would have same performance.

Parameters

**n**int

Number of items to retrieve.

**columns**list or str

Column name or names to order by.

**keep**{‘first’, ‘last’}, default ‘first’. ‘all’ is not implemented yet.

Determines which duplicates (if any) to keep. - `first` : Keep the first occurrence. - `last` : Keep the last occurrence.

Returns

DataFrame

Examples

```
>>> df = ps.DataFrame({'X': [1, 2, 3, 5, 6, 7, np.nan],
...                    'Y': [6, 7, 8, 9, 10, 11, 12]})
>>> df
     X   Y
0  1.0   6
1  2.0   7
2  3.0   8
3  5.0   9
4  6.0  10
5  7.0  11
6  NaN  12

```


In the following example, we will use `nsmallest` to select the three rows having the smallest values in column “X”.

```
>>> df.nsmallest(n=3, columns='X') 
     X   Y
0  1.0   6
1  2.0   7
2  3.0   8

```


To order by the smallest values in column “Y” and then “X”, we can specify multiple columns like in the next example.

```
>>> df.nsmallest(n=3, columns=['Y', 'X']) 
     X   Y
0  1.0   6
1  2.0   7
2  3.0   8

```


The examples below show how ties are resolved, which is decided by keep.

```
>>> tied_df = ps.DataFrame({'X': [1, 1, 2, 2, 3]}, index=['a', 'b', 'c', 'd', 'e'])
>>> tied_df
   X
a  1
b  1
c  2
d  2
e  3

```


When using keep=’first’ (default), ties are resolved in order:

```
>>> tied_df.nsmallest(3, 'X')
   X
a  1
b  1
c  2

```


```
>>> tied_df.nsmallest(3, 'X', keep='first')
   X
a  1
b  1
c  2

```


When using keep=’last’, ties are resolved in reverse order:

```
>>> tied_df.nsmallest(3, 'X', keep='last')
   X
b  1
a  1
d  2

```


# pyspark.pandas.DataFrame.stack — PySpark 4.0.1 documentation
DataFrame.stack()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.stack)
[#](#pyspark.pandas.DataFrame.stack "Permalink to this definition")

Stack the prescribed level(s) from columns to index.

Return a reshaped DataFrame or Series having a multi-level index with one or more new inner-most levels compared to the current DataFrame. The new inner-most levels are created by pivoting the columns of the current dataframe:

> *   if the columns have a single level, the output is a Series
>     
> *   if the columns have multiple levels, the new index level(s) is (are) taken from the prescribed level(s) and the output is a DataFrame.
>     

The new index levels are sorted.

Returns

DataFrame or Series

Stacked dataframe or series.

Notes

The function is named by analogy with a collection of books being reorganized from being side by side on a horizontal position (the columns of the dataframe) to being stacked vertically on top of each other (in the index of the dataframe).

Examples

**Single level columns**

```
>>> df_single_level_cols = ps.DataFrame([[0, 1], [2, 3]],
...                                     index=['cat', 'dog'],
...                                     columns=['weight', 'height'])

```


Stacking a dataframe with a single level column axis returns a Series:

```
>>> df_single_level_cols
     weight  height
cat       0       1
dog       2       3
>>> df_single_level_cols.stack().sort_index()
cat  height    1
     weight    0
dog  height    3
     weight    2
dtype: int64

```


**Multi level columns: simple case**

```
>>> multicol1 = pd.MultiIndex.from_tuples([('weight', 'kg'),
...                                        ('weight', 'pounds')])
>>> df_multi_level_cols1 = ps.DataFrame([[1, 2], [2, 4]],
...                                     index=['cat', 'dog'],
...                                     columns=multicol1)

```


Stacking a dataframe with a multi-level column axis:

```
>>> df_multi_level_cols1  
    weight
        kg pounds
cat      1      2
dog      2      4
>>> df_multi_level_cols1.stack().sort_index()
            weight
cat kg           1
    pounds       2
dog kg           2
    pounds       4

```


**Missing values**

```
>>> multicol2 = pd.MultiIndex.from_tuples([('weight', 'kg'),
...                                        ('height', 'm')])
>>> df_multi_level_cols2 = ps.DataFrame([[1.0, 2.0], [3.0, 4.0]],
...                                     index=['cat', 'dog'],
...                                     columns=multicol2)

```


It is common to have missing values when stacking a dataframe with multi-level columns, as the stacked dataframe typically has more values than the original dataframe. Missing values are filled with NaNs:

```
>>> df_multi_level_cols2
    weight height
        kg      m
cat    1.0    2.0
dog    3.0    4.0
>>> df_multi_level_cols2.stack().sort_index()
        weight  height
cat kg     1.0     NaN
    m      NaN     2.0
dog kg     3.0     NaN
    m      NaN     4.0

```


# pyspark.pandas.DataFrame.unstack — PySpark 4.0.1 documentation
DataFrame.unstack()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.unstack)
[#](#pyspark.pandas.DataFrame.unstack "Permalink to this definition")

Pivot the (necessarily hierarchical) index labels.

Returns a DataFrame having a new level of column labels whose inner-most level consists of the pivoted index labels.

If the index is not a MultiIndex, the output will be a Series.

Note

If the index is a MultiIndex, the output DataFrame could be very wide, and it could cause a serious performance degradation since Spark partitions its row based.

Returns

Series or DataFrame

Examples

```
>>> df = ps.DataFrame({"A": {"0": "a", "1": "b", "2": "c"},
...                    "B": {"0": "1", "1": "3", "2": "5"},
...                    "C": {"0": "2", "1": "4", "2": "6"}},
...                   columns=["A", "B", "C"])
>>> df
   A  B  C
0  a  1  2
1  b  3  4
2  c  5  6

```


```
>>> df.unstack().sort_index()
A  0    a
   1    b
   2    c
B  0    1
   1    3
   2    5
C  0    2
   1    4
   2    6
dtype: object

```


```
>>> df.columns = pd.MultiIndex.from_tuples([('X', 'A'), ('X', 'B'), ('Y', 'C')])
>>> df.unstack().sort_index()
X  A  0    a
      1    b
      2    c
   B  0    1
      1    3
      2    5
Y  C  0    2
      1    4
      2    6
dtype: object

```


For MultiIndex case:

```
>>> df = ps.DataFrame({"A": ["a", "b", "c"],
...                    "B": [1, 3, 5],
...                    "C": [2, 4, 6]},
...                   columns=["A", "B", "C"])
>>> df = df.set_index('A', append=True)
>>> df  
     B  C
  A
0 a  1  2
1 b  3  4
2 c  5  6
>>> df.unstack().sort_index()  
     B              C
A    a    b    c    a    b    c
0  1.0  NaN  NaN  2.0  NaN  NaN
1  NaN  3.0  NaN  NaN  4.0  NaN
2  NaN  NaN  5.0  NaN  NaN  6.0

```


# pyspark.pandas.DataFrame.melt — PySpark 4.0.1 documentation
DataFrame.melt(_id\_vars\=None_, _value\_vars\=None_, _var\_name\=None_, _value\_name\='value'_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.melt)
[#](#pyspark.pandas.DataFrame.melt "Permalink to this definition")

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


# pyspark.pandas.DataFrame.explode — PySpark 4.0.1 documentation
DataFrame.explode(_column_, _ignore\_index\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.explode)
[#](#pyspark.pandas.DataFrame.explode "Permalink to this definition")

Transform each element of a list-like to a row, replicating index values.

Parameters

**column**str or tuple

Column to explode.

**ignore\_index**bool, default False

If True, the resulting index will be labeled 0, 1, …, n - 1.

Returns

DataFrame

Exploded lists to rows of the subset columns; index will be duplicated for these rows.

Examples

```
>>> df = ps.DataFrame({'A': [[1, 2, 3], [], [3, 4]], 'B': 1})
>>> df
           A  B
0  [1, 2, 3]  1
1         []  1
2     [3, 4]  1

```


```
>>> df.explode('A')
     A  B
0  1.0  1
0  2.0  1
0  3.0  1
1  NaN  1
2  3.0  1
2  4.0  1

```


```
>>> df.explode('A', ignore_index=True)
     A  B
0  1.0  1
1  2.0  1
2  3.0  1
3  NaN  1
4  3.0  1
5  4.0  1

```


# pyspark.pandas.DataFrame.squeeze — PySpark 4.0.1 documentation
DataFrame.squeeze(_axis\=None_)
[#](#pyspark.pandas.DataFrame.squeeze "Permalink to this definition")

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

# pyspark.pandas.DataFrame.T — PySpark 4.0.1 documentation
_property_ DataFrame.T[#](#pyspark.pandas.DataFrame.T "Permalink to this definition")

Transpose index and columns.

Reflect the DataFrame over its main diagonal by writing rows as columns and vice-versa. The property [`T`](#pyspark.pandas.DataFrame.T "pyspark.pandas.DataFrame.T") is an accessor to the method [`transpose()`](about:blank/pyspark.pandas.DataFrame.transpose.html#pyspark.pandas.DataFrame.transpose "pyspark.pandas.DataFrame.transpose").

Note

This method is based on an expensive operation due to the nature of big data. Internally it needs to generate each row for each value, and then group twice - it is a huge operation. To prevent misuse, this method has the ‘compute.max\_rows’ default limit of input length and raises a ValueError.

```
>>> from pyspark.pandas.config import option_context
>>> with option_context('compute.max_rows', 1000):  
...     ps.DataFrame({'a': range(1001)}).transpose()
Traceback (most recent call last):
  ...
ValueError: Current DataFrame's length exceeds the given limit of 1000 rows.
Please set 'compute.max_rows' by using 'pyspark.pandas.config.set_option'
to retrieve more than 1000 rows. Note that, before changing the
'compute.max_rows', this operation is considerably expensive.

```


Returns

DataFrame

The transposed DataFrame.

Notes

Transposing a DataFrame with mixed dtypes will result in a homogeneous DataFrame with the coerced dtype. For instance, if int and float have to be placed in same column, it becomes float. If type coercion is not possible, it fails.

Also, note that the values in index should be unique because they become unique column names.

In addition, if Spark 2.3 is used, the types should always be exactly same.

Examples

**Square DataFrame with homogeneous dtype**

```
>>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
>>> df1 = ps.DataFrame(data=d1, columns=['col1', 'col2'])
>>> df1
   col1  col2
0     1     3
1     2     4

```


```
>>> df1_transposed = df1.T.sort_index()
>>> df1_transposed
      0  1
col1  1  2
col2  3  4

```


When the dtype is homogeneous in the original DataFrame, we get a transposed DataFrame with the same dtype:

```
>>> df1.dtypes
col1    int64
col2    int64
dtype: object
>>> df1_transposed.dtypes
0    int64
1    int64
dtype: object

```


**Non-square DataFrame with mixed dtypes**

```
>>> d2 = {'score': [9.5, 8],
...       'kids': [0, 0],
...       'age': [12, 22]}
>>> df2 = ps.DataFrame(data=d2, columns=['score', 'kids', 'age'])
>>> df2
   score  kids  age
0    9.5     0   12
1    8.0     0   22

```


```
>>> df2_transposed = df2.T.sort_index()
>>> df2_transposed
          0     1
age    12.0  22.0
kids    0.0   0.0
score   9.5   8.0

```


When the DataFrame has mixed dtypes, we get a transposed DataFrame with the coerced dtype:

```
>>> df2.dtypes
score    float64
kids       int64
age        int64
dtype: object

```


```
>>> df2_transposed.dtypes
0    float64
1    float64
dtype: object

```



# pyspark.pandas.DataFrame.transpose — PySpark 4.0.1 documentation
DataFrame.transpose()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.transpose)
[#](#pyspark.pandas.DataFrame.transpose "Permalink to this definition")

Transpose index and columns.

Reflect the DataFrame over its main diagonal by writing rows as columns and vice-versa. The property [`T`](about:blank/pyspark.pandas.DataFrame.T.html#pyspark.pandas.DataFrame.T "pyspark.pandas.DataFrame.T") is an accessor to the method [`transpose()`](#pyspark.pandas.DataFrame.transpose "pyspark.pandas.DataFrame.transpose").

Note

This method is based on an expensive operation due to the nature of big data. Internally it needs to generate each row for each value, and then group twice - it is a huge operation. To prevent misuse, this method has the ‘compute.max\_rows’ default limit of input length and raises a ValueError.

```
>>> from pyspark.pandas.config import option_context
>>> with option_context('compute.max_rows', 1000):  
...     ps.DataFrame({'a': range(1001)}).transpose()
Traceback (most recent call last):
  ...
ValueError: Current DataFrame's length exceeds the given limit of 1000 rows.
Please set 'compute.max_rows' by using 'pyspark.pandas.config.set_option'
to retrieve more than 1000 rows. Note that, before changing the
'compute.max_rows', this operation is considerably expensive.

```


Returns

DataFrame

The transposed DataFrame.

Notes

Transposing a DataFrame with mixed dtypes will result in a homogeneous DataFrame with the coerced dtype. For instance, if int and float have to be placed in same column, it becomes float. If type coercion is not possible, it fails.

Also, note that the values in index should be unique because they become unique column names.

In addition, if Spark 2.3 is used, the types should always be exactly same.

Examples

**Square DataFrame with homogeneous dtype**

```
>>> d1 = {'col1': [1, 2], 'col2': [3, 4]}
>>> df1 = ps.DataFrame(data=d1, columns=['col1', 'col2'])
>>> df1
   col1  col2
0     1     3
1     2     4

```


```
>>> df1_transposed = df1.T.sort_index()
>>> df1_transposed
      0  1
col1  1  2
col2  3  4

```


When the dtype is homogeneous in the original DataFrame, we get a transposed DataFrame with the same dtype:

```
>>> df1.dtypes
col1    int64
col2    int64
dtype: object
>>> df1_transposed.dtypes
0    int64
1    int64
dtype: object

```


**Non-square DataFrame with mixed dtypes**

```
>>> d2 = {'score': [9.5, 8],
...       'kids': [0, 0],
...       'age': [12, 22]}
>>> df2 = ps.DataFrame(data=d2, columns=['score', 'kids', 'age'])
>>> df2
   score  kids  age
0    9.5     0   12
1    8.0     0   22

```


```
>>> df2_transposed = df2.T.sort_index()
>>> df2_transposed
          0     1
age    12.0  22.0
kids    0.0   0.0
score   9.5   8.0

```


When the DataFrame has mixed dtypes, we get a transposed DataFrame with the coerced dtype:

```
>>> df2.dtypes
score    float64
kids       int64
age        int64
dtype: object

```


```
>>> df2_transposed.dtypes
0    float64
1    float64
dtype: object

```
# pyspark.pandas.DataFrame.assign — PySpark 4.0.1 documentation
DataFrame.assign(_\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.assign)
[#](#pyspark.pandas.DataFrame.assign "Permalink to this definition")

Assign new columns to a DataFrame.

Returns a new object with all original columns in addition to new ones. Existing columns that are re-assigned will be overwritten.

Parameters

**\*\*kwargs**dict of {str: callable, Series or Index}

The column names are keywords. If the values are callable, they are computed on the DataFrame and assigned to the new columns. The callable must not change input DataFrame (though pandas-on-Spark doesn’t check it). If the values are not callable, (e.g. a Series or a literal), they are simply assigned.

Returns

DataFrame

A new DataFrame with the new columns in addition to all the existing columns.

Notes

Assigning multiple columns within the same `assign` is possible but you cannot refer to newly created or modified columns. This feature is supported in pandas for Python 3.6 and later but not in pandas-on-Spark. In pandas-on-Spark, all items are computed first, and then assigned.

Examples

```
>>> df = ps.DataFrame({'temp_c': [17.0, 25.0]},
...                   index=['Portland', 'Berkeley'])
>>> df
          temp_c
Portland    17.0
Berkeley    25.0

```


Where the value is a callable, evaluated on df:

```
>>> df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
          temp_c  temp_f
Portland    17.0    62.6
Berkeley    25.0    77.0

```


Alternatively, the same behavior can be achieved by directly referencing an existing Series or sequence and you can also create multiple columns within the same assign.

```
>>> assigned = df.assign(temp_f=df['temp_c'] * 9 / 5 + 32,
...                      temp_k=df['temp_c'] + 273.15,
...                      temp_idx=df.index)
>>> assigned[['temp_c', 'temp_f', 'temp_k', 'temp_idx']]
          temp_c  temp_f  temp_k  temp_idx
Portland    17.0    62.6  290.15  Portland
Berkeley    25.0    77.0  298.15  Berkeley

```

# pyspark.pandas.DataFrame.merge — PySpark 4.0.1 documentation
DataFrame.merge(_right_, _how\='inner'_, _on\=None_, _left\_on\=None_, _right\_on\=None_, _left\_index\=False_, _right\_index\=False_, _suffixes\=('\_x', '\_y')_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.merge)
[#](#pyspark.pandas.DataFrame.merge "Permalink to this definition")

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

left: use only keys from left frame, like a SQL left outer join; not preserve

key order unlike pandas.

right: use only keys from right frame, like a SQL right outer join; not preserve

key order unlike pandas.

outer: use union of keys from both frames, like a SQL full outer join; sort keys

lexicographically.

inner: use intersection of keys from both frames, like a SQL inner join;

not preserve the order of the left keys unlike pandas.

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

See also

[`DataFrame.join`](about:blank/pyspark.pandas.DataFrame.join.html#pyspark.pandas.DataFrame.join "pyspark.pandas.DataFrame.join")

Join columns of another DataFrame.

[`DataFrame.update`](about:blank/pyspark.pandas.DataFrame.update.html#pyspark.pandas.DataFrame.update "pyspark.pandas.DataFrame.update")

Modify in place using non-NA values from another DataFrame.

`DataFrame.hint`

Specifies some hint on the current DataFrame.

[`broadcast`](about:blank/pyspark.pandas.broadcast.html#pyspark.pandas.broadcast "pyspark.pandas.broadcast")

Marks a DataFrame as small enough for use in broadcast joins.

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
>>> merged = df1.merge(df2, left_on='lkey', right_on='rkey')
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
>>> left_psdf.merge(right_psdf, left_index=True, right_index=True).sort_index()
   A  B
1  2  x

```


```
>>> left_psdf.merge(right_psdf, left_index=True, right_index=True, how='left').sort_index()
   A     B
0  1  None
1  2     x

```


```
>>> left_psdf.merge(right_psdf, left_index=True, right_index=True, how='right').sort_index()
     A  B
1  2.0  x
2  NaN  y

```


```
>>> left_psdf.merge(right_psdf, left_index=True, right_index=True, how='outer').sort_index()
     A     B
0  1.0  None
1  2.0     x
2  NaN     y

```

# pyspark.pandas.DataFrame.join — PySpark 4.0.1 documentation
DataFrame.join(_right_, _on\=None_, _how\='left'_, _lsuffix\=''_, _rsuffix\=''_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.join)
[#](#pyspark.pandas.DataFrame.join "Permalink to this definition")

Join columns of another DataFrame.

Join columns with right DataFrame either on index or on a key column. Efficiently join multiple DataFrame objects by index at once by passing a list.

Parameters

**right: DataFrame, Series**

**on: str, list of str, or array-like, optional**

Column or index level name(s) in the caller to join on the index in right, otherwise joins index-on-index. If multiple values given, the right DataFrame must have a MultiIndex. Can pass an array as the join key if it is not already contained in the calling DataFrame. Like an Excel VLOOKUP operation.

**how: {‘left’, ‘right’, ‘outer’, ‘inner’}, default ‘left’**

How to handle the operation of the two objects.

*   left: use left frame’s index (or column if on is specified).
    
*   right: use right’s index.
    
*   outer: form union of left frame’s index (or column if on is specified) with right’s index, and sort it. lexicographically.
    
*   inner: form intersection of left frame’s index (or column if on is specified) with right’s index, preserving the order of the left’s one.
    

**lsuffix**str, default ‘’

Suffix to use from left frame’s overlapping columns.

**rsuffix**str, default ‘’

Suffix to use from right frame’s overlapping columns.

Returns

DataFrame

A dataframe containing columns from both the left and right.

See also

[`DataFrame.merge`](about:blank/pyspark.pandas.DataFrame.merge.html#pyspark.pandas.DataFrame.merge "pyspark.pandas.DataFrame.merge")

For column(s)-on-columns(s) operations.

[`DataFrame.update`](about:blank/pyspark.pandas.DataFrame.update.html#pyspark.pandas.DataFrame.update "pyspark.pandas.DataFrame.update")

Modify in place using non-NA values from another DataFrame.

`DataFrame.hint`

Specifies some hint on the current DataFrame.

[`broadcast`](about:blank/pyspark.pandas.broadcast.html#pyspark.pandas.broadcast "pyspark.pandas.broadcast")

Marks a DataFrame as small enough for use in broadcast joins.

Notes

Parameters on, lsuffix, and rsuffix are not supported when passing a list of DataFrame objects.

Examples

```
>>> psdf1 = ps.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
...                      'A': ['A0', 'A1', 'A2', 'A3']},
...                     columns=['key', 'A'])
>>> psdf2 = ps.DataFrame({'key': ['K0', 'K1', 'K2'],
...                      'B': ['B0', 'B1', 'B2']},
...                     columns=['key', 'B'])
>>> psdf1
  key   A
0  K0  A0
1  K1  A1
2  K2  A2
3  K3  A3
>>> psdf2
  key   B
0  K0  B0
1  K1  B1
2  K2  B2

```


Join DataFrames using their indexes.

```
>>> join_psdf = psdf1.join(psdf2, lsuffix='_left', rsuffix='_right')
>>> join_psdf.sort_values(by=join_psdf.columns)
  key_left   A key_right     B
0       K0  A0        K0    B0
1       K1  A1        K1    B1
2       K2  A2        K2    B2
3       K3  A3      None  None

```


If we want to join using the key columns, we need to set key to be the index in both df and right. The joined DataFrame will have key as its index.

```
>>> join_psdf = psdf1.set_index('key').join(psdf2.set_index('key'))
>>> join_psdf.sort_values(by=join_psdf.columns) 
      A     B
key
K0   A0    B0
K1   A1    B1
K2   A2    B2
K3   A3  None

```


Another option to join using the key columns is to use the on parameter. DataFrame.join always uses right’s index but we can use any column in df. This method does not preserve the original DataFrame’s index in the result unlike pandas.

```
>>> join_psdf = psdf1.join(psdf2.set_index('key'), on='key')
>>> join_psdf.index
Index([0, 1, 2, 3], dtype='int64')

```


# pyspark.pandas.DataFrame.update — PySpark 4.0.1 documentation
DataFrame.update(_other_, _join\='left'_, _overwrite\=True_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.update)
[#](#pyspark.pandas.DataFrame.update "Permalink to this definition")

Modify in place using non-NA values from another DataFrame. Aligns on indices. There is no return value.

Parameters

**other**DataFrame, or Series

**join**‘left’, default ‘left’

Only left join is implemented, keeping the index and columns of the original object.

**overwrite**bool, default True

How to handle non-NA values for overlapping keys:

*   True: overwrite original DataFrame’s values with values from other.
    
*   False: only update values that are NA in the original DataFrame.
    

Returns

**None**method directly changes calling object

See also

[`DataFrame.merge`](about:blank/pyspark.pandas.DataFrame.merge.html#pyspark.pandas.DataFrame.merge "pyspark.pandas.DataFrame.merge")

For column(s)-on-columns(s) operations.

[`DataFrame.join`](about:blank/pyspark.pandas.DataFrame.join.html#pyspark.pandas.DataFrame.join "pyspark.pandas.DataFrame.join")

Join columns of another DataFrame.

`DataFrame.hint`

Specifies some hint on the current DataFrame.

[`broadcast`](about:blank/pyspark.pandas.broadcast.html#pyspark.pandas.broadcast "pyspark.pandas.broadcast")

Marks a DataFrame as small enough for use in broadcast joins.

Examples

```
>>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [400, 500, 600]}, columns=['A', 'B'])
>>> new_df = ps.DataFrame({'B': [4, 5, 6], 'C': [7, 8, 9]}, columns=['B', 'C'])
>>> df.update(new_df)
>>> df.sort_index()
   A  B
0  1  4
1  2  5
2  3  6

```


The DataFrame’s length does not increase because of the update, only values at matching index/column labels are updated.

```
>>> df = ps.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']}, columns=['A', 'B'])
>>> new_df = ps.DataFrame({'B': ['d', 'e', 'f', 'g', 'h', 'i']}, columns=['B'])
>>> df.update(new_df)
>>> df.sort_index()
   A  B
0  a  d
1  b  e
2  c  f

```


For Series, its name attribute must be set.

```
>>> df = ps.DataFrame({'A': ['a', 'b', 'c'], 'B': ['x', 'y', 'z']}, columns=['A', 'B'])
>>> new_column = ps.Series(['d', 'e'], name='B', index=[0, 2])
>>> df.update(new_column)
>>> df.sort_index()
   A  B
0  a  d
1  b  y
2  c  e

```


If other contains None the corresponding values are not updated in the original dataframe.

```
>>> df = ps.DataFrame({'A': [1, 2, 3], 'B': [400, 500, 600]}, columns=['A', 'B'])
>>> new_df = ps.DataFrame({'B': [4, None, 6]}, columns=['B'])
>>> df.update(new_df)
>>> df.sort_index()
   A      B
0  1    4.0
1  2  500.0
2  3    6.0

```



# pyspark.pandas.DataFrame.resample — PySpark 4.0.1 documentation
DataFrame.resample(_rule_, _closed\=None_, _label\=None_, _on\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.resample)
[#](#pyspark.pandas.DataFrame.resample "Permalink to this definition")

Resample time-series data.

Convenience method for frequency conversion and resampling of time series. The object must have a datetime-like index (only support DatetimeIndex for now), or the caller must pass the label of a datetime-like series/index to the `on` keyword parameter.

New in version 3.4.0.

Parameters

**rule**str

The offset string or object representing target conversion. Currently, supported units are {‘Y’, ‘A’, ‘M’, ‘D’, ‘H’, ‘T’, ‘MIN’, ‘S’}.

**closed**{{‘right’, ‘left’}}, default None

Which side of bin interval is closed. The default is ‘left’ for all frequency offsets except for ‘A’, ‘Y’ and ‘M’ which all have a default of ‘right’.

**label**{{‘right’, ‘left’}}, default None

Which bin edge label to label bucket with. The default is ‘left’ for all frequency offsets except for ‘A’, ‘Y’ and ‘M’ which all have a default of ‘right’.

**on**Series, optional

For a DataFrame, column to use instead of index for resampling. Column must be datetime-like.

Returns

DataFrameResampler


# pyspark.pandas.DataFrame.shift — PySpark 4.0.1 documentation
DataFrame.shift(_periods\=1_, _fill\_value\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.shift)
[#](#pyspark.pandas.DataFrame.shift "Permalink to this definition")

Shift DataFrame by desired number of periods.

Note

the current implementation of shift uses Spark’s Window without specifying partition specification. This leads to moving all data into a single partition in a single machine and could cause serious performance degradation. Avoid this method with very large datasets.

Parameters

**periods**int

Number of periods to shift. Can be positive or negative.

**fill\_value**object, optional

The scalar value to use for newly introduced missing values. The default depends on the dtype of self. For numeric data, np.nan is used.

Returns

Copy of input DataFrame, shifted.

Examples

```
>>> df = ps.DataFrame({'Col1': [10, 20, 15, 30, 45],
...                    'Col2': [13, 23, 18, 33, 48],
...                    'Col3': [17, 27, 22, 37, 52]},
...                   columns=['Col1', 'Col2', 'Col3'])

```


```
>>> df.shift(periods=3)
   Col1  Col2  Col3
0   NaN   NaN   NaN
1   NaN   NaN   NaN
2   NaN   NaN   NaN
3  10.0  13.0  17.0
4  20.0  23.0  27.0

```


```
>>> df.shift(periods=3, fill_value=0)
   Col1  Col2  Col3
0     0     0     0
1     0     0     0
2     0     0     0
3    10    13    17
4    20    23    27

```


# pyspark.pandas.DataFrame.first_valid_index — PySpark 4.0.1 documentation
DataFrame.first\_valid\_index()
[#](#pyspark.pandas.DataFrame.first_valid_index "Permalink to this definition")

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


# pyspark.pandas.DataFrame.last_valid_index — PySpark 4.0.1 documentation
DataFrame.last\_valid\_index()
[#](#pyspark.pandas.DataFrame.last_valid_index "Permalink to this definition")

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


# pyspark.pandas.DataFrame.from_dict — PySpark 4.0.1 documentation
_static_ DataFrame.from\_dict(_data_, _orient\='columns'_, _dtype\=None_, _columns\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.from_dict)
[#](#pyspark.pandas.DataFrame.from_dict "Permalink to this definition")

Construct DataFrame from dict of array-like or dicts.

Creates DataFrame object from dictionary by columns or by index allowing dtype specification.

Parameters

**data**dict

Of the form {field : array-like} or {field : dict}.

**orient**{‘columns’, ‘index’}, default ‘columns’

The “orientation” of the data. If the keys of the passed dict should be the columns of the resulting DataFrame, pass ‘columns’ (default). Otherwise, if the keys should be rows, pass ‘index’.

**dtype**dtype, default None

Data type to force, otherwise infer.

**columns**list, default None

Column labels to use when `orient='index'`. Raises a ValueError if used with `orient='columns'`.

Returns

DataFrame

See also

[`DataFrame.from_records`](about:blank/pyspark.pandas.DataFrame.from_records.html#pyspark.pandas.DataFrame.from_records "pyspark.pandas.DataFrame.from_records")

DataFrame from structured ndarray, sequence of tuples or dicts, or DataFrame.

[`DataFrame`](about:blank/pyspark.pandas.DataFrame.html#pyspark.pandas.DataFrame "pyspark.pandas.DataFrame")

DataFrame object creation using constructor.

Examples

By default the keys of the dict become the DataFrame columns:

```
>>> data = {'col_1': [3, 2, 1, 0], 'col_2': [10, 20, 30, 40]}
>>> ps.DataFrame.from_dict(data)
   col_1  col_2
0      3     10
1      2     20
2      1     30
3      0     40

```


Specify `orient='index'` to create the DataFrame using dictionary keys as rows:

```
>>> data = {'row_1': [3, 2, 1, 0], 'row_2': [10, 20, 30, 40]}
>>> ps.DataFrame.from_dict(data, orient='index').sort_index()
        0   1   2   3
row_1   3   2   1   0
row_2  10  20  30  40

```


When using the ‘index’ orientation, the column names can be specified manually:

```
>>> ps.DataFrame.from_dict(data, orient='index',
...                        columns=['A', 'B', 'C', 'D']).sort_index()
        A   B   C   D
row_1   3   2   1   0
row_2  10  20  30  40

```


# pyspark.pandas.DataFrame.from_records — PySpark 4.0.1 documentation
_static_ DataFrame.from\_records(_data_, _index\=None_, _exclude\=None_, _columns\=None_, _coerce\_float\=False_, _nrows\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.from_records)
[#](#pyspark.pandas.DataFrame.from_records "Permalink to this definition")

Convert structured or recorded ndarray to DataFrame.

Parameters

**data**ndarray (structured dtype), list of tuples, dict, or DataFrame

Deprecated since version 4.0.0: Passing a DataFrame is deprecated.

**index**string, list of fields, array-like

Field of array to use as the index, alternately a specific set of input labels to use

**exclude**sequence, default None

Columns or fields to exclude

**columns**sequence, default None

Column names to use. If the passed data do not have names associated with them, this argument provides names for the columns. Otherwise this argument indicates the order of the columns in the result (any names not found in the data will become all-NA columns)

**coerce\_float**boolean, default False

Attempt to convert values of non-string, non-numeric objects (like decimal.Decimal) to floating point, useful for SQL result sets

**nrows**int, default None

Number of rows to read if data is an iterator

Returns

**df**DataFrame

Examples

Use dict as input

```
>>> ps.DataFrame.from_records({'A': [1, 2, 3]})
   A
0  1
1  2
2  3

```


Use list of tuples as input

```
>>> ps.DataFrame.from_records([(1, 2), (3, 4)])
   0  1
0  1  2
1  3  4

```


Use NumPy array as input

```
>>> ps.DataFrame.from_records(np.eye(3))
     0    1    2
0  1.0  0.0  0.0
1  0.0  1.0  0.0
2  0.0  0.0  1.0

```


# pyspark.pandas.DataFrame.to_table — PySpark 4.0.1 documentation
DataFrame.to\_table(_name_, _format\=None_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_table)
[#](#pyspark.pandas.DataFrame.to_table "Permalink to this definition")

Write the DataFrame into a Spark table. [`DataFrame.spark.to_table()`](about:blank/pyspark.pandas.DataFrame.spark.to_table.html#pyspark.pandas.DataFrame.spark.to_table "pyspark.pandas.DataFrame.spark.to_table") is an alias of [`DataFrame.to_table()`](#pyspark.pandas.DataFrame.to_table "pyspark.pandas.DataFrame.to_table").

Parameters

**name**str, required

Table name in Spark.

**format**string, optional

Specifies the output data source format. Some common ones are:

*   ‘delta’
    
*   ‘parquet’
    
*   ‘orc’
    
*   ‘json’
    
*   ‘csv’
    

**mode**str {‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’}, default

‘overwrite’. Specifies the behavior of the save operation when the table exists already.

*   ‘append’: Append the new data to existing data.
    
*   ‘overwrite’: Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options**

Additional options passed directly to Spark.

Returns

None

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_table('%s.my_table' % db, partition_cols='date')

```


# pyspark.pandas.DataFrame.to_delta — PySpark 4.0.1 documentation
DataFrame.to\_delta(_path_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_delta)
[#](#pyspark.pandas.DataFrame.to_delta "Permalink to this definition")

Write the DataFrame out as a Delta Lake table.

Parameters

**path**str, required

Path to write to.

**mode**str

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default the index is always lost.

**options**dict

All other options passed directly into Delta Lake.

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


Create a new Delta Lake table, partitioned by one column:

```
>>> df.to_delta('%s/to_delta/foo' % path, partition_cols='date')  

```


Partitioned by two columns:

```
>>> df.to_delta('%s/to_delta/bar' % path,
...             partition_cols=['date', 'country'])  

```


Overwrite an existing table’s partitions, using the ‘replaceWhere’ capability in Delta:

```
>>> df.to_delta('%s/to_delta/bar' % path,
...             mode='overwrite', replaceWhere='date >= "2012-01-01"')  

```

# pyspark.pandas.DataFrame.to_parquet — PySpark 4.0.1 documentation
DataFrame.to\_parquet(_path_, _mode\='w'_, _partition\_cols\=None_, _compression\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_parquet)
[#](#pyspark.pandas.DataFrame.to_parquet "Permalink to this definition")

Write the DataFrame out as a Parquet file or directory.

Parameters

**path**str, required

Path to write to.

**mode**str

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**compression**str {‘none’, ‘uncompressed’, ‘snappy’, ‘gzip’, ‘lzo’, ‘brotli’, ‘lz4’, ‘zstd’}

Compression codec to use when saving to file. If None is set, it uses the value specified in spark.sql.parquet.compression.codec.

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default the index is always lost.

**options**dict

All other options passed directly into Spark’s data source.

Notes

pandas API on Spark writes Parquet files into the directory, path, and writes multiple part files in the directory unlike pandas. pandas API on Spark respects HDFS’s property such as ‘fs.default.name’.

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_parquet('%s/to_parquet/foo.parquet' % path, partition_cols='date')

```


```
>>> df.to_parquet(
...     '%s/to_parquet/foo.parquet' % path,
...     mode = 'overwrite',
...     partition_cols=['date', 'country'])

```


# pyspark.pandas.DataFrame.to_csv — PySpark 4.0.1 documentation
DataFrame.to\_csv(_path\=None_, _sep\=','_, _na\_rep\=''_, _columns\=None_, _header\=True_, _quotechar\='"'_, _date\_format\=None_, _escapechar\=None_, _num\_files\=None_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.to_csv "Permalink to this definition")

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


# pyspark.pandas.DataFrame.to_orc — PySpark 4.0.1 documentation
DataFrame.to\_orc(_path_, _mode\='w'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_orc)
[#](#pyspark.pandas.DataFrame.to_orc "Permalink to this definition")

Write a DataFrame to the ORC format.

Parameters

**path**str

Path to write to.

**mode**str

Python write mode, default ‘w’.

Note

mode can accept the strings for Spark writing mode. Such as ‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’.

*   ‘append’ (equivalent to ‘a’): Append the new data to existing data.
    
*   ‘overwrite’ (equivalent to ‘w’): Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default the index is always lost.

**options**dict

All other options passed directly into Spark’s data source.

Notes

pandas API on Spark writes ORC files into the directory, path, and writes multiple part files in the directory unlike pandas. pandas API on Spark respects HDFS’s property such as ‘fs.default.name’.

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_orc('%s/to_orc/foo.orc' % path, partition_cols='date')

```


```
>>> df.to_orc(
...     '%s/to_orc/foo.orc' % path,
...     mode = 'overwrite',
...     partition_cols=['date', 'country'])

```

# pyspark.pandas.DataFrame.to_pandas — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.to\_pandas

DataFrame.to\_pandas()
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_pandas)
[#](#pyspark.pandas.DataFrame.to_pandas "Permalink to this definition")

Return a pandas DataFrame.

Note

This method should only be used if the resulting pandas DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
...                   columns=['dogs', 'cats'])
>>> df.to_pandas()
   dogs  cats
0   0.2   0.3
1   0.0   0.6
2   0.6   0.0
3   0.2   0.1

```

# pyspark.pandas.DataFrame.to_html — PySpark 4.0.1 documentation
DataFrame.to\_html(_buf\=None_, _columns\=None_, _col\_space\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _justify\=None_, _max\_rows\=None_, _max\_cols\=None_, _show\_dimensions\=False_, _decimal\='.'_, _bold\_rows\=True_, _classes\=None_, _escape\=True_, _notebook\=False_, _border\=None_, _table\_id\=None_, _render\_links\=False_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_html)
[#](#pyspark.pandas.DataFrame.to_html "Permalink to this definition")

Render a DataFrame as an HTML table.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory. If the input is large, set max\_rows parameter.

Parameters

**buf**StringIO-like, optional

Buffer to write to.

**columns**sequence, optional, default None

The subset of columns to write. Writes all columns by default.

**col\_space**int, optional

The minimum width of each column.

**header**bool, optional

Write out the column names. If a list of strings is given, it is assumed to be aliases for the column names

**index**bool, optional, default True

Whether to print index (row) labels.

**na\_rep**str, optional, default ‘NaN’

String representation of NAN to use.

**formatters**list or dict of one-param. functions, optional

Formatter functions to apply to columns’ elements by position or name. The result of each function must be a Unicode string. List must be of length equal to the number of columns.

**float\_format**one-parameter function, optional, default None

Formatter function to apply to columns’ elements if they are floats. The result of this function must be a Unicode string.

**sparsify**bool, optional, default True

Set to False for a DataFrame with a hierarchical index to print every multiindex key at each row.

**index\_names**bool, optional, default True

Prints the names of the indexes.

**justify**str, default None

How to justify the column labels. If None uses the option from the print configuration (controlled by set\_option), ‘right’ out of the box. Valid values are

*   left
    
*   right
    
*   center
    
*   justify
    
*   justify-all
    
*   start
    
*   end
    
*   inherit
    
*   match-parent
    
*   initial
    
*   unset.
    

**max\_rows**int, optional

Maximum number of rows to display in the console.

**max\_cols**int, optional

Maximum number of columns to display in the console.

**show\_dimensions**bool, default False

Display DataFrame dimensions (number of rows by number of columns).

**decimal**str, default ‘.’

Character recognized as decimal separator, e.g. ‘,’ in Europe.

**bold\_rows**bool, default True

Make the row labels bold in the output.

**classes**str or list or tuple, default None

CSS class(es) to apply to the resulting html table.

**escape**bool, default True

Convert the characters <, >, and & to HTML-safe sequences.

**notebook**{True, False}, default False

Whether the generated HTML is for IPython Notebook.

**border**int

A `border=border` attribute is included in the opening <table> tag. By default `pd.options.html.border`.

**table\_id**str, optional

A css id is included in the opening <table> tag if specified.

**render\_links**bool, default False

Convert URLs to HTML links (only works with pandas 0.24+).

Returns

str (or Unicode, depending on data and options)

String representation of the dataframe.

See also

[`to_string`](about:blank/pyspark.pandas.DataFrame.to_string.html#pyspark.pandas.DataFrame.to_string "pyspark.pandas.DataFrame.to_string")

Convert DataFrame to a string.


# pyspark.pandas.DataFrame.to_numpy — PySpark 4.0.1 documentation
DataFrame.to\_numpy()
[#](#pyspark.pandas.DataFrame.to_numpy "Permalink to this definition")

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


# pyspark.pandas.DataFrame.to_spark — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.to\_spark

DataFrame.to\_spark(_index\_col\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_spark)
[#](#pyspark.pandas.DataFrame.to_spark "Permalink to this definition")

Spark related features. Usually, the features here are missing in pandas but Spark has it.

# pyspark.pandas.DataFrame.to_string — PySpark 4.0.1 documentation
DataFrame.to\_string(_buf\=None_, _columns\=None_, _col\_space\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _justify\=None_, _max\_rows\=None_, _max\_cols\=None_, _show\_dimensions\=False_, _decimal\='.'_, _line\_width\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_string)
[#](#pyspark.pandas.DataFrame.to_string "Permalink to this definition")

Render a DataFrame to a console-friendly tabular output.

Note

This method should only be used if the resulting pandas object is expected to be small, as all the data is loaded into the driver’s memory. If the input is large, set max\_rows parameter.

Parameters

**buf**StringIO-like, optional

Buffer to write to.

**columns**sequence, optional, default None

The subset of columns to write. Writes all columns by default.

**col\_space**int, optional

The minimum width of each column.

**header**bool, optional

Write out the column names. If a list of strings is given, it is assumed to be aliases for the column names

**index**bool, optional, default True

Whether to print index (row) labels.

**na\_rep**str, optional, default ‘NaN’

String representation of NAN to use.

**formatters**list or dict of one-param. functions, optional

Formatter functions to apply to columns’ elements by position or name. The result of each function must be a Unicode string. List must be of length equal to the number of columns.

**float\_format**one-parameter function, optional, default None

Formatter function to apply to columns’ elements if they are floats. The result of this function must be a Unicode string.

**sparsify**bool, optional, default True

Set to False for a DataFrame with a hierarchical index to print every multiindex key at each row.

**index\_names**bool, optional, default True

Prints the names of the indexes.

**justify**str, default None

How to justify the column labels. If None uses the option from the print configuration (controlled by set\_option), ‘right’ out of the box. Valid values are

*   left
    
*   right
    
*   center
    
*   justify
    
*   justify-all
    
*   start
    
*   end
    
*   inherit
    
*   match-parent
    
*   initial
    
*   unset.
    

**max\_rows**int, optional

Maximum number of rows to display in the console.

**max\_cols**int, optional

Maximum number of columns to display in the console.

**show\_dimensions**bool, default False

Display DataFrame dimensions (number of rows by number of columns).

**decimal**str, default ‘.’

Character recognized as decimal separator, e.g. ‘,’ in Europe.

**line\_width**int, optional

Width to wrap a line in characters.

Returns

str (or Unicode, depending on data and options)

String representation of the dataframe.

See also

[`to_html`](about:blank/pyspark.pandas.DataFrame.to_html.html#pyspark.pandas.DataFrame.to_html "pyspark.pandas.DataFrame.to_html")

Convert DataFrame to HTML.

Examples

```
>>> df = ps.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]}, columns=['col1', 'col2'])
>>> print(df.to_string())
   col1  col2
0     1     4
1     2     5
2     3     6

```


```
>>> print(df.to_string(max_rows=2))
   col1  col2
0     1     4
1     2     5

```

# pyspark.pandas.DataFrame.to_feather — PySpark 4.0.1 documentation
DataFrame.to\_feather(_path_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_feather)
[#](#pyspark.pandas.DataFrame.to_feather "Permalink to this definition")

Write a DataFrame to the binary Feather format.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

New in version 4.0.0.

Parameters

**path**str, path object, file-like object

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `write()` function.

**\*\*kwargs**

Additional keywords passed to `pyarrow.feather.write_feather()`. This includes the compression, compression\_level, chunksize and version keywords.

Examples

```
>>> df = ps.DataFrame([[1, 2, 3], [4, 5, 6]])
>>> df.to_feather("file.feather")  

```

# pyspark.pandas.DataFrame.to_stata — PySpark 4.0.1 documentation
DataFrame.to\_stata(_path_, _\*_, _convert\_dates\=None_, _write\_index\=True_, _byteorder\=None_, _time\_stamp\=None_, _data\_label\=None_, _variable\_labels\=None_, _version\=114_, _convert\_strl\=None_, _compression\='infer'_, _storage\_options\=None_, _value\_labels\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_stata)
[#](#pyspark.pandas.DataFrame.to_stata "Permalink to this definition")

Export DataFrame object to Stata dta format.

Note

This method should only be used if the resulting DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

New in version 4.0.0.

Parameters

**path**str, path object, or buffer

String, path object (implementing `os.PathLike[str]`), or file-like object implementing a binary `write()` function.

**convert\_dates**dict

Dictionary mapping columns containing datetime types to stata internal format to use when writing the dates. Options are ‘tc’, ‘td’, ‘tm’, ‘tw’, ‘th’, ‘tq’, ‘ty’. Column can be either an integer or a name. Datetime columns that do not have a conversion type specified will be converted to ‘tc’. Raises NotImplementedError if a datetime column has timezone information.

**write\_index**bool

Write the index to Stata dataset.

**byteorder**str

Can be “>”, “<”, “little”, or “big”. default is sys.byteorder.

**time\_stamp**datetime

A datetime to use as file creation date. Default is the current time.

**data\_label**str, optional

A label for the data set. Must be 80 characters or smaller.

**variable\_labels**dict

Dictionary containing columns as keys and variable labels as values. Each label must be 80 characters or smaller.

**version**{{114, 117, 118, 119, None}}, default 114

Version to use in the output dta file. Set to None to let pandas decide between 118 or 119 formats depending on the number of columns in the frame. Version 114 can be read by Stata 10 and later. Version 117 can be read by Stata 13 or later. Version 118 is supported in Stata 14 and later. Version 119 is supported in Stata 15 and later. Version 114 limits string variables to 244 characters or fewer while versions 117 and later allow strings with lengths up to 2,000,000 characters. Versions 118 and 119 support Unicode characters, and version 119 supports more than 32,767 variables.

**convert\_strl**list, optional

List of column names to convert to string columns to Stata StrL format. Only available if version is 117. Storing strings in the StrL format can produce smaller dta files if strings have more than 8 characters and values are repeated.

**value\_labels**dict of dicts

Dictionary containing columns as keys and dictionaries of column value to labels as values. Labels for a single variable must be 32,000 characters or smaller.

Examples

```
>>> df = ps.DataFrame({'animal': ['falcon', 'parrot', 'falcon', 'parrot'],
...                    'speed': [350, 18, 361, 15]})
>>> df.to_stata('animals.dta')  

```


# pyspark.pandas.DataFrame.to_json — PySpark 4.0.1 documentation
DataFrame.to\_json(_path\=None_, _compression\='uncompressed'_, _num\_files\=None_, _mode\='w'_, _orient\='records'_, _lines\=True_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.to_json "Permalink to this definition")

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



# pyspark.pandas.DataFrame.to_dict — PySpark 4.0.1 documentation
DataFrame.to\_dict(_orient='dict'_, _into=<class 'dict'>_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_dict)
[#](#pyspark.pandas.DataFrame.to_dict "Permalink to this definition")

Convert the DataFrame to a dictionary.

The type of the key-value pairs can be customized with the parameters (see below).

Note

This method should only be used if the resulting pandas DataFrame is expected to be small, as all the data is loaded into the driver’s memory.

Parameters

**orient**str {‘dict’, ‘list’, ‘series’, ‘split’, ‘records’, ‘index’}

Determines the type of the values of the dictionary.

*   ‘dict’ (default) : dict like {column -> {index -> value}}
    
*   ‘list’ : dict like {column -> \[values\]}
    
*   ‘series’ : dict like {column -> Series(values)}
    
*   ‘split’ : dict like {‘index’ -> \[index\], ‘columns’ -> \[columns\], ‘data’ -> \[values\]}
    
*   ‘records’ : list like \[{column -> value}, … , {column -> value}\]
    
*   ‘index’ : dict like {index -> {column -> value}}
    

Abbreviations are allowed. s indicates series and sp indicates split.

**into**class, default dict

The collections.abc.Mapping subclass used for all Mappings in the return value. Can be the actual class or an empty instance of the mapping type you want. If you want a collections.defaultdict, you must pass it initialized.

Returns

dict, list or collections.abc.Mapping

Return a collections.abc.Mapping object representing the DataFrame. The resulting transformation depends on the orient parameter.

Examples

```
>>> df = ps.DataFrame({'col1': [1, 2],
...                    'col2': [0.5, 0.75]},
...                   index=['row1', 'row2'],
...                   columns=['col1', 'col2'])
>>> df
      col1  col2
row1     1  0.50
row2     2  0.75

```


```
>>> df_dict = df.to_dict()
>>> sorted([(key, sorted(values.items())) for key, values in df_dict.items()])
[('col1', [('row1', 1), ('row2', 2)]), ('col2', [('row1', 0.5), ('row2', 0.75)])]

```


You can specify the return orientation.

```
>>> df_dict = df.to_dict('series')
>>> sorted(df_dict.items())
[('col1', row1    1
row2    2
Name: col1, dtype: int64), ('col2', row1    0.50
row2    0.75
Name: col2, dtype: float64)]

```


```
>>> df_dict = df.to_dict('split')
>>> sorted(df_dict.items())  
[('columns', ['col1', 'col2']), ('data', [[1..., 0.75]]), ('index', ['row1', 'row2'])]

```


```
>>> df_dict = df.to_dict('records')
>>> [sorted(values.items()) for values in df_dict]  
[[('col1', 1...), ('col2', 0.5)], [('col1', 2...), ('col2', 0.75)]]

```


```
>>> df_dict = df.to_dict('index')
>>> sorted([(key, sorted(values.items())) for key, values in df_dict.items()])
[('row1', [('col1', 1), ('col2', 0.5)]), ('row2', [('col1', 2), ('col2', 0.75)])]

```


You can also specify the mapping type.

```
>>> from collections import OrderedDict, defaultdict
>>> df.to_dict(into=OrderedDict)  
OrderedDict(...)

```


If you want a defaultdict, you need to initialize it:

```
>>> dd = defaultdict(list)
>>> df.to_dict('records', into=dd)  
[defaultdict(<class 'list'>, {'col..., 'col...}), defaultdict(<class 'list'>, {'col..., 'col...})]

```
# pyspark.pandas.DataFrame.to_excel — PySpark 4.0.1 documentation
DataFrame.to\_excel(_excel\_writer_, _sheet\_name\='Sheet1'_, _na\_rep\=''_, _float\_format\=None_, _columns\=None_, _header\=True_, _index\=True_, _index\_label\=None_, _startrow\=0_, _startcol\=0_, _engine\=None_, _merge\_cells\=True_, _inf\_rep\='inf'_, _freeze\_panes\=None_)
[#](#pyspark.pandas.DataFrame.to_excel "Permalink to this definition")

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

# pyspark.pandas.DataFrame.to_hdf — PySpark 4.0.1 documentation
DataFrame.to\_hdf(_path\_or\_buf_, _key_, _mode\='a'_, _complevel\=None_, _complib\=None_, _append\=False_, _format\=None_, _index\=True_, _min\_itemsize\=None_, _nan\_rep\=None_, _dropna\=None_, _data\_columns\=None_, _errors\='strict'_, _encoding\='UTF-8'_)
[#](#pyspark.pandas.DataFrame.to_hdf "Permalink to this definition")

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


# pyspark.pandas.DataFrame.to_clipboard — PySpark 4.0.1 documentation
DataFrame.to\_clipboard(_excel\=True_, _sep\=None_, _\*\*kwargs_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_clipboard)
[#](#pyspark.pandas.DataFrame.to_clipboard "Permalink to this definition")

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

# pyspark.pandas.DataFrame.to_markdown — PySpark 4.0.1 documentation
DataFrame.to\_markdown(_buf\=None_, _mode\=None_)
[#](#pyspark.pandas.DataFrame.to_markdown "Permalink to this definition")

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


# pyspark.pandas.DataFrame.to_records — PySpark 4.0.1 documentation
DataFrame.to\_records(_index\=True_, _column\_dtypes\=None_, _index\_dtypes\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_records)
[#](#pyspark.pandas.DataFrame.to_records "Permalink to this definition")

Convert DataFrame to a NumPy record array.

Index will be included as the first field of the record array if requested.

Note

This method should only be used if the resulting NumPy ndarray is expected to be small, as all the data is loaded into the driver’s memory.

Parameters

**index**bool, default True

Include index in resulting record array, stored in ‘index’ field or using the index label, if set.

**column\_dtypes**str, type, dict, default None

If a string or type, the data type to store all columns. If a dictionary, a mapping of column names and indices (zero-indexed) to specific data types.

**index\_dtypes**str, type, dict, default None

If a string or type, the data type to store all index levels. If a dictionary, a mapping of index level names and indices (zero-indexed) to specific data types. This mapping is applied only if index=True.

Returns

numpy.recarray

NumPy ndarray with the DataFrame labels as fields and each row of the DataFrame as entries.

See also

[`DataFrame.from_records`](about:blank/pyspark.pandas.DataFrame.from_records.html#pyspark.pandas.DataFrame.from_records "pyspark.pandas.DataFrame.from_records")

Convert structured or record ndarray to DataFrame.

`numpy.recarray`

An ndarray that allows field access using attributes, analogous to typed columns in a spreadsheet.

Examples

```
>>> df = ps.DataFrame({'A': [1, 2], 'B': [0.5, 0.75]},
...                   index=['a', 'b'])
>>> df
   A     B
a  1  0.50
b  2  0.75

```


```
>>> df.to_records() 
rec.array([('a', 1, 0.5 ), ('b', 2, 0.75)],
          dtype=[('index', 'O'), ('A', '<i8'), ('B', '<f8')])

```


The index can be excluded from the record array:

```
>>> df.to_records(index=False) 
rec.array([(1, 0.5 ), (2, 0.75)],
          dtype=[('A', '<i8'), ('B', '<f8')])

```


Specification of dtype for columns is new in pandas 0.24.0. Data types can be specified for the columns:

```
>>> df.to_records(column_dtypes={"A": "int32"}) 
rec.array([('a', 1, 0.5 ), ('b', 2, 0.75)],
          dtype=[('index', 'O'), ('A', '<i4'), ('B', '<f8')])

```


Specification of dtype for index is new in pandas 0.24.0. Data types can also be specified for the index:

```
>>> df.to_records(index_dtypes="<S2") 
rec.array([(b'a', 1, 0.5 ), (b'b', 2, 0.75)],
          dtype=[('index', 'S2'), ('A', '<i8'), ('B', '<f8')])

```


# pyspark.pandas.DataFrame.to_latex — PySpark 4.0.1 documentation
DataFrame.to\_latex(_buf\=None_, _columns\=None_, _header\=True_, _index\=True_, _na\_rep\='NaN'_, _formatters\=None_, _float\_format\=None_, _sparsify\=None_, _index\_names\=True_, _bold\_rows\=False_, _column\_format\=None_, _longtable\=None_, _escape\=None_, _encoding\=None_, _decimal\='.'_, _multicolumn\=None_, _multicolumn\_format\=None_, _multirow\=None_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.to_latex)
[#](#pyspark.pandas.DataFrame.to_latex "Permalink to this definition")

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


# pyspark.pandas.DataFrame.style — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [DataFrame](../frame.html)
*   pyspark.pandas.DataFrame.style

_property_ DataFrame.style[#](#pyspark.pandas.DataFrame.style "Permalink to this definition")

Property returning a Styler object containing methods for building a styled HTML representation for the DataFrame.

Examples

```
>>> ps.range(1001).style  
<pandas.io.formats.style.Styler object at ...>

```


# pyspark.pandas.DataFrame.spark.frame — PySpark 4.0.1 documentation
spark.frame(_index\_col\=None_)
[#](#pyspark.pandas.DataFrame.spark.frame "Permalink to this definition")

Return the current DataFrame as a Spark DataFrame. `DataFrame.spark.frame()` is an alias of `DataFrame.to_spark()`.

Parameters

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

See also

`DataFrame.to_spark`

`DataFrame.pandas_api`

`DataFrame.spark.frame`

Examples

By default, this method loses the index as below.

```
>>> df = ps.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
>>> df.to_spark().show()  
+---+---+---+
|  a|  b|  c|
+---+---+---+
|  1|  4|  7|
|  2|  5|  8|
|  3|  6|  9|
+---+---+---+

```


```
>>> df = ps.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
>>> df.spark.frame().show()  
+---+---+---+
|  a|  b|  c|
+---+---+---+
|  1|  4|  7|
|  2|  5|  8|
|  3|  6|  9|
+---+---+---+

```


If index\_col is set, it keeps the index column as specified.

```
>>> df.to_spark(index_col="index").show()  
+-----+---+---+---+
|index|  a|  b|  c|
+-----+---+---+---+
|    0|  1|  4|  7|
|    1|  2|  5|  8|
|    2|  3|  6|  9|
+-----+---+---+---+

```


Keeping an index column is useful when you want to call some Spark APIs and convert it back to pandas-on-Spark DataFrame without creating a default index, which can affect performance.

```
>>> spark_df = df.to_spark(index_col="index")
>>> spark_df = spark_df.filter("a == 2")
>>> spark_df.pandas_api(index_col="index")  
       a  b  c
index
1      2  5  8

```


In case of multi-index, specify a list to index\_col.

```
>>> new_df = df.set_index("a", append=True)
>>> new_spark_df = new_df.to_spark(index_col=["index_1", "index_2"])
>>> new_spark_df.show()  
+-------+-------+---+---+
|index_1|index_2|  b|  c|
+-------+-------+---+---+
|      0|      1|  4|  7|
|      1|      2|  5|  8|
|      2|      3|  6|  9|
+-------+-------+---+---+

```


Can be converted back to pandas-on-Spark DataFrame.

```
>>> new_spark_df.pandas_api(
...     index_col=["index_1", "index_2"])  
                 b  c
index_1 index_2
0       1        4  7
1       2        5  8
2       3        6  9

```


# pyspark.pandas.DataFrame.spark.cache — PySpark 4.0.1 documentation
spark.cache()
[#](#pyspark.pandas.DataFrame.spark.cache "Permalink to this definition")

Yields and caches the current DataFrame.

The pandas-on-Spark DataFrame is yielded as a protected resource and its corresponding data is cached which gets uncached after execution goes off the context.

If you want to specify the StorageLevel manually, use `DataFrame.spark.persist()`

See also

`DataFrame.spark.persist`

Examples

```
>>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
...                   columns=['dogs', 'cats'])
>>> df
   dogs  cats
0   0.2   0.3
1   0.0   0.6
2   0.6   0.0
3   0.2   0.1

```


```
>>> with df.spark.cache() as cached_df:
...     print(cached_df.count())
...
dogs    4
cats    4
dtype: int64

```


```
>>> df = df.spark.cache()
>>> df.to_pandas().mean(axis=1)
0    0.25
1    0.30
2    0.30
3    0.15
dtype: float64

```


To uncache the dataframe, use unpersist function

# pyspark.pandas.DataFrame.spark.persist — PySpark 4.0.1 documentation
spark.persist(_storage\_level\=StorageLevel(True, True, False, False, 1)_)
[#](#pyspark.pandas.DataFrame.spark.persist "Permalink to this definition")

Yields and caches the current DataFrame with a specific StorageLevel. If a StorageLevel is not given, the MEMORY\_AND\_DISK level is used by default like PySpark.

The pandas-on-Spark DataFrame is yielded as a protected resource and its corresponding data is cached which gets uncached after execution goes off the context.

See also

`DataFrame.spark.cache`

Examples

```
>>> import pyspark
>>> df = ps.DataFrame([(.2, .3), (.0, .6), (.6, .0), (.2, .1)],
...                   columns=['dogs', 'cats'])
>>> df
   dogs  cats
0   0.2   0.3
1   0.0   0.6
2   0.6   0.0
3   0.2   0.1

```


Set the StorageLevel to MEMORY\_ONLY.

```
>>> with df.spark.persist(pyspark.StorageLevel.MEMORY_ONLY) as cached_df:
...     print(cached_df.spark.storage_level)
...     print(cached_df.count())
...
Memory Serialized 1x Replicated
dogs    4
cats    4
dtype: int64

```


Set the StorageLevel to DISK\_ONLY.

```
>>> with df.spark.persist(pyspark.StorageLevel.DISK_ONLY) as cached_df:
...     print(cached_df.spark.storage_level)
...     print(cached_df.count())
...
Disk Serialized 1x Replicated
dogs    4
cats    4
dtype: int64

```


If a StorageLevel is not given, it uses MEMORY\_AND\_DISK by default.

```
>>> with df.spark.persist() as cached_df:
...     print(cached_df.spark.storage_level)
...     print(cached_df.count())
...
Disk Memory Serialized 1x Replicated
dogs    4
cats    4
dtype: int64

```


```
>>> df = df.spark.persist()
>>> df.to_pandas().mean(axis=1)
0    0.25
1    0.30
2    0.30
3    0.15
dtype: float64

```


To uncache the dataframe, use unpersist function


# pyspark.pandas.DataFrame.spark.hint — PySpark 4.0.1 documentation
spark.hint(_name_, _\*parameters_)
[#](#pyspark.pandas.DataFrame.spark.hint "Permalink to this definition")

Specifies some hint on the current DataFrame.

Parameters

**name**A name of the hint.

**parameters**Optional parameters.

Returns

**ret**DataFrame with the hint.

See also

`broadcast`

Marks a DataFrame as small enough for use in broadcast joins.

Examples

```
>>> df1 = ps.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [1, 2, 3, 5]},
...                    columns=['lkey', 'value']).set_index('lkey')
>>> df2 = ps.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
...                     'value': [5, 6, 7, 8]},
...                    columns=['rkey', 'value']).set_index('rkey')
>>> merged = df1.merge(df2.spark.hint("broadcast"), left_index=True, right_index=True)
>>> merged.spark.explain()  
== Physical Plan ==
...
...BroadcastHashJoin...
...

```

# pyspark.pandas.DataFrame.spark.to_table — PySpark 4.0.1 documentation
spark.to\_table(_name_, _format\=None_, _mode\='overwrite'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.spark.to_table "Permalink to this definition")

Write the DataFrame into a Spark table. `DataFrame.spark.to_table()` is an alias of `DataFrame.to_table()`.

Parameters

**name**str, required

Table name in Spark.

**format**string, optional

Specifies the output data source format. Some common ones are:

*   ‘delta’
    
*   ‘parquet’
    
*   ‘orc’
    
*   ‘json’
    
*   ‘csv’
    

**mode**str {‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’}, default

‘overwrite’. Specifies the behavior of the save operation when the table exists already.

*   ‘append’: Append the new data to existing data.
    
*   ‘overwrite’: Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional, default None

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options**

Additional options passed directly to Spark.

Returns

None

See also

`read_table`

`DataFrame.spark.to_spark_io`

`DataFrame.to_parquet`

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.to_table('%s.my_table' % db, partition_cols='date')

```



# pyspark.pandas.DataFrame.spark.to_spark_io — PySpark 4.0.1 documentation
spark.to\_spark\_io(_path\=None_, _format\=None_, _mode\='overwrite'_, _partition\_cols\=None_, _index\_col\=None_, _\*\*options_)
[#](#pyspark.pandas.DataFrame.spark.to_spark_io "Permalink to this definition")

Write the DataFrame out to a Spark data source.

Parameters

**path**string, optional

Path to the data source.

**format**string, optional

Specifies the output data source format. Some common ones are:

*   ‘delta’
    
*   ‘parquet’
    
*   ‘orc’
    
*   ‘json’
    
*   ‘csv’
    

**mode**str {‘append’, ‘overwrite’, ‘ignore’, ‘error’, ‘errorifexists’}, default

‘overwrite’. Specifies the behavior of the save operation when data already exists.

*   ‘append’: Append the new data to existing data.
    
*   ‘overwrite’: Overwrite existing data.
    
*   ‘ignore’: Silently ignore this operation if data already exists.
    
*   ‘error’ or ‘errorifexists’: Throw an exception if data already exists.
    

**partition\_cols**str or list of str, optional

Names of partitioning columns

**index\_col: str or list of str, optional, default: None**

Column names to be used in Spark to represent pandas-on-Spark’s index. The index name in pandas-on-Spark is ignored. By default, the index is always lost.

**options**dict

All other options passed directly into Spark’s data source.

Returns

None

See also

`read_spark_io`

`DataFrame.to_delta`

`DataFrame.to_parquet`

`DataFrame.to_table`

`DataFrame.spark.to_spark_io`

Examples

```
>>> df = ps.DataFrame(dict(
...    date=list(pd.date_range('2012-1-1 12:00:00', periods=3, freq='ME')),
...    country=['KR', 'US', 'JP'],
...    code=[1, 2 ,3]), columns=['date', 'country', 'code'])
>>> df
                 date country  code
0 2012-01-31 12:00:00      KR     1
1 2012-02-29 12:00:00      US     2
2 2012-03-31 12:00:00      JP     3

```


```
>>> df.spark.to_spark_io(path='%s/to_spark_io/foo.json' % path, format='json')

```


# pyspark.pandas.DataFrame.spark.apply — PySpark 4.0.1 documentation
spark.apply(_func_, _index\_col\=None_)
[#](#pyspark.pandas.DataFrame.spark.apply "Permalink to this definition")

Applies a function that takes and returns a Spark DataFrame. It allows natively apply a Spark function and column APIs with the Spark column internally used in Series or Index.

Note

set index\_col and keep the column named as so in the output Spark DataFrame to avoid using the default index to prevent performance penalty. If you omit index\_col, it will use default index which is potentially expensive in general.

Note

it will lose column labels. This is a synonym of `func(psdf.to_spark(index_col)).pandas_api(index_col)`.

Parameters

**func**function

Function to apply the function against the data by using Spark DataFrame.

Returns

DataFrame

Raises

**ValueError**If the output from the function is not a Spark DataFrame.

Examples

```
>>> psdf = ps.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}, columns=["a", "b"])
>>> psdf
   a  b
0  1  4
1  2  5
2  3  6

```


```
>>> psdf.spark.apply(
...     lambda sdf: sdf.selectExpr("a + b as c", "index"), index_col="index")
... 
       c
index
0      5
1      7
2      9

```


The case below ends up with using the default index, which should be avoided if possible.

```
>>> psdf.spark.apply(lambda sdf: sdf.groupby("a").count().sort("a"))
   a  count
0  1      1
1  2      1
2  3      1

```


# pyspark.pandas.DataFrame.spark.repartition — PySpark 4.0.1 documentation
spark.repartition(_num\_partitions_)
[#](#pyspark.pandas.DataFrame.spark.repartition "Permalink to this definition")

Returns a new DataFrame partitioned by the given partitioning expressions. The resulting DataFrame is hash partitioned.

Parameters

**num\_partitions**int

The target number of partitions.

Returns

DataFrame

Examples

```
>>> psdf = ps.DataFrame({"age": [5, 5, 2, 2],
...         "name": ["Bob", "Bob", "Alice", "Alice"]}).set_index("age")
>>> psdf.sort_index()  
      name
age
2    Alice
2    Alice
5      Bob
5      Bob
>>> new_psdf = psdf.spark.repartition(7)
>>> new_psdf.to_spark().rdd.getNumPartitions()
7
>>> new_psdf.sort_index()   
      name
age
2    Alice
2    Alice
5      Bob
5      Bob

```



# pyspark.pandas.DataFrame.spark.coalesce — PySpark 4.0.1 documentation
spark.coalesce(_num\_partitions_)
[#](#pyspark.pandas.DataFrame.spark.coalesce "Permalink to this definition")

Returns a new DataFrame that has exactly num\_partitions partitions.

Note

This operation results in a narrow dependency, e.g. if you go from 1000 partitions to 100 partitions, there will not be a shuffle, instead each of the 100 new partitions will claim 10 of the current partitions. If a larger number of partitions is requested, it will stay at the current number of partitions. However, if you’re doing a drastic coalesce, e.g. to num\_partitions = 1, this may result in your computation taking place on fewer nodes than you like (e.g. one node in the case of num\_partitions = 1). To avoid this, you can call repartition(). This will add a shuffle step, but means the current upstream partitions will be executed in parallel (per whatever the current partitioning is).

Parameters

**num\_partitions**int

The target number of partitions.

Returns

DataFrame

Examples

```
>>> psdf = ps.DataFrame({"age": [5, 5, 2, 2],
...         "name": ["Bob", "Bob", "Alice", "Alice"]}).set_index("age")
>>> psdf.sort_index()  
      name
age
2    Alice
2    Alice
5      Bob
5      Bob
>>> new_psdf = psdf.spark.coalesce(1)
>>> new_psdf.to_spark().rdd.getNumPartitions()
1
>>> new_psdf.sort_index()   
      name
age
2    Alice
2    Alice
5      Bob
5      Bob

```



# pyspark.pandas.DataFrame.plot.area — PySpark 4.0.1 documentation
plot.area(_x\=None_, _y\=None_, _\*\*kwds_)
[#](#pyspark.pandas.DataFrame.plot.area "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.bar — PySpark 4.0.1 documentation
plot.bar(_x\=None_, _y\=None_, _\*\*kwds_)
[#](#pyspark.pandas.DataFrame.plot.bar "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.barh — PySpark 4.0.1 documentation
plot.barh(_x\=None_, _y\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.DataFrame.plot.barh "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.box — PySpark 4.0.1 documentation
plot.box(_\*\*kwds_)
[#](#pyspark.pandas.DataFrame.plot.box "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.density — PySpark 4.0.1 documentation
plot.density(_bw\_method\=None_, _ind\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.DataFrame.plot.density "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.hist — PySpark 4.0.1 documentation
plot.hist(_bins\=10_, _\*\*kwds_)
[#](#pyspark.pandas.DataFrame.plot.hist "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.kde — PySpark 4.0.1 documentation
plot.kde(_bw\_method\=None_, _ind\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.DataFrame.plot.kde "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.line — PySpark 4.0.1 documentation
plot.line(_x\=None_, _y\=None_, _\*\*kwargs_)
[#](#pyspark.pandas.DataFrame.plot.line "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.pie — PySpark 4.0.1 documentation
plot.pie(_\*\*kwds_)
[#](#pyspark.pandas.DataFrame.plot.pie "Permalink to this definition")

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


# pyspark.pandas.DataFrame.plot.scatter — PySpark 4.0.1 documentation
plot.scatter(_x_, _y_, _\*\*kwds_)
[#](#pyspark.pandas.DataFrame.plot.scatter "Permalink to this definition")

Create a scatter plot with varying marker point size and color.

The coordinates of each point are defined by two dataframe columns and filled circles are used to represent each point. This kind of plot is useful to see complex correlations between two variables. Points could be for instance natural 2D coordinates like longitude and latitude in a map or, in general, any pair of metrics that can be plotted against each other.

Parameters

**x**int or str

The column name or column position to be used as horizontal coordinates for each point.

**y**int or str

The column name or column position to be used as vertical coordinates for each point.

**s**scalar or array\_like, optional

(matplotlib-only).

**c**str, int or array\_like, optional

(matplotlib-only).

**\*\*kwds: Optional**

Keyword arguments to pass on to `pyspark.pandas.DataFrame.plot()`.

Returns

`plotly.graph_objs.Figure`

Return an custom object when `backend!=plotly`. Return an ndarray when `subplots=True` (matplotlib-only).

See also

`plotly.express.scatter`

Scatter plot using multiple input data formats (plotly).

`matplotlib.pyplot.scatter`

Scatter plot using multiple input data formats (matplotlib).

Examples

Let’s see how to draw a scatter plot using coordinates from the values in a DataFrame’s columns.

```
>>> df = ps.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
...                    [6.4, 3.2, 1], [5.9, 3.0, 2]],
...                   columns=['length', 'width', 'species'])
>>> df.plot.scatter(x='length', y='width')  

```


And now with dark scheme:

```
>>> df = ps.DataFrame([[5.1, 3.5, 0], [4.9, 3.0, 0], [7.0, 3.2, 1],
...                    [6.4, 3.2, 1], [5.9, 3.0, 2]],
...                   columns=['length', 'width', 'species'])
>>> fig = df.plot.scatter(x='length', y='width')
>>> fig.update_layout(template="plotly_dark")  

```


# pyspark.pandas.DataFrame.hist — PySpark 4.0.1 documentation
DataFrame.hist(_bins\=10_, _\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.hist)
[#](#pyspark.pandas.DataFrame.hist "Permalink to this definition")

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


# pyspark.pandas.DataFrame.boxplot — PySpark 4.0.1 documentation
DataFrame.boxplot(_\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.boxplot)
[#](#pyspark.pandas.DataFrame.boxplot "Permalink to this definition")

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

# pyspark.pandas.DataFrame.kde — PySpark 4.0.1 documentation
DataFrame.kde(_bw\_method\=None_, _ind\=None_, _\*\*kwds_)
[\[source\]](about:blank/_modules/pyspark/pandas/frame.html#DataFrame.kde)
[#](#pyspark.pandas.DataFrame.kde "Permalink to this definition")

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


# pyspark.pandas.DataFrame.pandas_on_spark.apply_batch — PySpark 4.0.1 documentation
pandas\_on\_spark.apply\_batch(_func_, _args\=()_, _\*\*kwds_)
[#](#pyspark.pandas.DataFrame.pandas_on_spark.apply_batch "Permalink to this definition")

Apply a function that takes pandas DataFrame and outputs pandas DataFrame. The pandas DataFrame given to the function is of a batch used internally.

See also [Transform and apply a function](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/transform_apply.html).

Note

the func is unable to access the whole input frame. pandas-on-Spark internally splits the input series into multiple batches and calls func with each batch multiple times. Therefore, operations such as global aggregations are impossible. See the example below.

```
>>> # This case does not return the length of whole frame but of the batch internally
... # used.
... def length(pdf) -> ps.DataFrame[int, [int]]:
...     return pd.DataFrame([len(pdf)])
...
>>> df = ps.DataFrame({'A': range(1000)})
>>> df.pandas_on_spark.apply_batch(length)  
    c0
0   83
1   83
2   83
...
10  83
11  83

```


Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:

```
>>> def plus_one(x) -> ps.DataFrame[int, [float, float]]:
...     return x + 1

```


If the return type is specified, the output column names become c0, c1, c2 … cn. These names are positionally mapped to the returned DataFrame in `func`.

To specify the column names, you can assign them in a NumPy compound type style as below:

```
>>> def plus_one(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
...     return x + 1

```


```
>>> pdf = pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
>>> def plus_one(x) -> ps.DataFrame[
...         (pdf.index.name, pdf.index.dtype), zip(pdf.dtypes, pdf.columns)]:
...     return x + 1

```


Parameters

**func**function

Function to apply to each pandas frame.

**args**tuple

Positional arguments to pass to func in addition to the array/series.

**\*\*kwds**

Additional keyword arguments to pass as keywords arguments to func.

Returns

DataFrame

See also

`DataFrame.apply`

For row/columnwise operations.

`DataFrame.applymap`

For elementwise operations.

`DataFrame.aggregate`

Only perform aggregating type operations.

`DataFrame.transform`

Only perform transforming type operations.

`Series.pandas_on_spark.transform_batch`

transform the search as each pandas chunks.

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
>>> def query_func(pdf) -> ps.DataFrame[int, [int, int]]:
...     return pdf.query('A == 1')
>>> df.pandas_on_spark.apply_batch(query_func)
   c0  c1
0   1   2

```


```
>>> def query_func(pdf) -> ps.DataFrame[("idx", int), [("A", int), ("B", int)]]:
...     return pdf.query('A == 1')
>>> df.pandas_on_spark.apply_batch(query_func)  
     A  B
idx
0    1  2

```


You can also omit the type hints so pandas-on-Spark infers the return schema as below:

```
>>> df.pandas_on_spark.apply_batch(lambda pdf: pdf.query('A == 1'))
   A  B
0  1  2

```


You can also specify extra arguments.

```
>>> def calculation(pdf, y, z) -> ps.DataFrame[int, [int, int]]:
...     return pdf ** y + z
>>> df.pandas_on_spark.apply_batch(calculation, args=(10,), z=20)
        c0        c1
0       21      1044
1    59069   1048596
2  9765645  60466196

```


You can also use `np.ufunc` and built-in functions as input.

```
>>> df.pandas_on_spark.apply_batch(np.add, args=(10,))
    A   B
0  11  12
1  13  14
2  15  16

```


```
>>> (df * -1).pandas_on_spark.apply_batch(abs)
   A  B
0  1  2
1  3  4
2  5  6

```


# pyspark.pandas.DataFrame.pandas_on_spark.transform_batch — PySpark 4.0.1 documentation
pandas\_on\_spark.transform\_batch(_func_, _\*args_, _\*\*kwargs_)
[#](#pyspark.pandas.DataFrame.pandas_on_spark.transform_batch "Permalink to this definition")

Transform chunks with a function that takes pandas DataFrame and outputs pandas DataFrame. The pandas DataFrame given to the function is of a batch used internally. The length of each input and output should be the same.

See also [Transform and apply a function](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/transform_apply.html).

Note

the func is unable to access the whole input frame. pandas-on-Spark internally splits the input series into multiple batches and calls func with each batch multiple times. Therefore, operations such as global aggregations are impossible. See the example below.

```
>>> # This case does not return the length of whole frame but of the batch internally
... # used.
... def length(pdf) -> ps.DataFrame[int]:
...     return pd.DataFrame([len(pdf)] * len(pdf))
...
>>> df = ps.DataFrame({'A': range(1000)})
>>> df.pandas_on_spark.transform_batch(length)  
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
>>> def plus_one(x) -> ps.DataFrame[int, [float, float]]:
...     return x + 1

```


If the return type is specified, the output column names become c0, c1, c2 … cn. These names are positionally mapped to the returned DataFrame in `func`.

To specify the column names, you can assign them in a NumPy compound type style as below:

```
>>> def plus_one(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
...     return x + 1

```


```
>>> pdf = pd.DataFrame({'a': [1, 2, 3], 'b': [3, 4, 5]})
>>> def plus_one(x) -> ps.DataFrame[
...         (pdf.index.name, pdf.index.dtype), zip(pdf.dtypes, pdf.columns)]:
...     return x + 1

```


Parameters

**func**function

Function to transform each pandas frame.

**\*args**

Positional arguments to pass to func.

**\*\*kwargs**

Keyword arguments to pass to func.

Returns

DataFrame or Series

See also

`DataFrame.pandas_on_spark.apply_batch`

For row/columnwise operations.

`Series.pandas_on_spark.transform_batch`

transform the search as each pandas chunks.

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
>>> def plus_one_func(pdf) -> ps.DataFrame[int, [int, int]]:
...     return pdf + 1
>>> df.pandas_on_spark.transform_batch(plus_one_func)
   c0  c1
0   2   3
1   4   5
2   6   7

```


```
>>> def plus_one_func(pdf) -> ps.DataFrame[("index", int), [('A', int), ('B', int)]]:
...     return pdf + 1
>>> df.pandas_on_spark.transform_batch(plus_one_func)  
       A  B
index
0      2  3
1      4  5
2      6  7

```


```
>>> def plus_one_func(pdf) -> ps.Series[int]:
...     return pdf.B + 1
>>> df.pandas_on_spark.transform_batch(plus_one_func)
0    3
1    5
2    7
dtype: int64

```


You can also omit the type hints so pandas-on-Spark infers the return schema as below:

```
>>> df.pandas_on_spark.transform_batch(lambda pdf: pdf + 1)
   A  B
0  2  3
1  4  5
2  6  7

```


```
>>> (df * -1).pandas_on_spark.transform_batch(abs)
   A  B
0  1  2
1  3  4
2  5  6

```


Note that you should not transform the index. The index information will not change.

```
>>> df.pandas_on_spark.transform_batch(lambda pdf: pdf.B + 1)
0    3
1    5
2    7
Name: B, dtype: int64

```


You can also specify extra arguments as below.

```
>>> df.pandas_on_spark.transform_batch(lambda pdf, a, b, c: pdf.B + a + b + c, 1, 2, c=3)
0     8
1    10
2    12
Name: B, dtype: int64

```
