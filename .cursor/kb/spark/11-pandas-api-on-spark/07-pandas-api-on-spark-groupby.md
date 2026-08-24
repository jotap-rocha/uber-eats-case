# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/groupby.html

# GroupBy#

GroupBy objects are returned by groupby calls: [`DataFrame.groupby()`](api/pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby"), [`Series.groupby()`](api/pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby"), etc.

## Indexing, iteration#

[`GroupBy.get_group`](api/pyspark.pandas.groupby.GroupBy.get_group.html#pyspark.pandas.groupby.GroupBy.get_group "pyspark.pandas.groupby.GroupBy.get_group")(name) | Construct DataFrame from group with provided name.  
---|---  
  
## Function application#

[`GroupBy.apply`](api/pyspark.pandas.groupby.GroupBy.apply.html#pyspark.pandas.groupby.GroupBy.apply "pyspark.pandas.groupby.GroupBy.apply")(func,Â *args,Â **kwargs) | Apply function func group-wise and combine the results together.  
---|---  
[`GroupBy.transform`](api/pyspark.pandas.groupby.GroupBy.transform.html#pyspark.pandas.groupby.GroupBy.transform "pyspark.pandas.groupby.GroupBy.transform")(func,Â *args,Â **kwargs) | Apply function column-by-column to the GroupBy object.  
  
The following methods are available only for DataFrameGroupBy objects.

[`DataFrameGroupBy.agg`](api/pyspark.pandas.groupby.DataFrameGroupBy.agg.html#pyspark.pandas.groupby.DataFrameGroupBy.agg "pyspark.pandas.groupby.DataFrameGroupBy.agg")([func_or_funcs]) | Aggregate using one or more operations over the specified axis.  
---|---  
[`DataFrameGroupBy.aggregate`](api/pyspark.pandas.groupby.DataFrameGroupBy.aggregate.html#pyspark.pandas.groupby.DataFrameGroupBy.aggregate "pyspark.pandas.groupby.DataFrameGroupBy.aggregate")([func_or_funcs]) | Aggregate using one or more operations over the specified axis.  
  
## Computations / Descriptive Stats#

[`GroupBy.all`](api/pyspark.pandas.groupby.GroupBy.all.html#pyspark.pandas.groupby.GroupBy.all "pyspark.pandas.groupby.GroupBy.all")([skipna]) | Returns True if all values in the group are truthful, else False.  
---|---  
[`GroupBy.any`](api/pyspark.pandas.groupby.GroupBy.any.html#pyspark.pandas.groupby.GroupBy.any "pyspark.pandas.groupby.GroupBy.any")() | Returns True if any value in the group is truthful, else False.  
[`GroupBy.count`](api/pyspark.pandas.groupby.GroupBy.count.html#pyspark.pandas.groupby.GroupBy.count "pyspark.pandas.groupby.GroupBy.count")() | Compute count of group, excluding missing values.  
[`GroupBy.cumcount`](api/pyspark.pandas.groupby.GroupBy.cumcount.html#pyspark.pandas.groupby.GroupBy.cumcount "pyspark.pandas.groupby.GroupBy.cumcount")([ascending]) | Number each item in each group from 0 to the length of that group - 1.  
[`GroupBy.cummax`](api/pyspark.pandas.groupby.GroupBy.cummax.html#pyspark.pandas.groupby.GroupBy.cummax "pyspark.pandas.groupby.GroupBy.cummax")() | Cumulative max for each group.  
[`GroupBy.cummin`](api/pyspark.pandas.groupby.GroupBy.cummin.html#pyspark.pandas.groupby.GroupBy.cummin "pyspark.pandas.groupby.GroupBy.cummin")() | Cumulative min for each group.  
[`GroupBy.cumprod`](api/pyspark.pandas.groupby.GroupBy.cumprod.html#pyspark.pandas.groupby.GroupBy.cumprod "pyspark.pandas.groupby.GroupBy.cumprod")() | Cumulative product for each group.  
[`GroupBy.cumsum`](api/pyspark.pandas.groupby.GroupBy.cumsum.html#pyspark.pandas.groupby.GroupBy.cumsum "pyspark.pandas.groupby.GroupBy.cumsum")() | Cumulative sum for each group.  
[`GroupBy.ewm`](api/pyspark.pandas.groupby.GroupBy.ewm.html#pyspark.pandas.groupby.GroupBy.ewm "pyspark.pandas.groupby.GroupBy.ewm")([com,Â span,Â halflife,Â alpha,Â ...]) | Return an ewm grouper, providing ewm functionality per group.  
[`GroupBy.filter`](api/pyspark.pandas.groupby.GroupBy.filter.html#pyspark.pandas.groupby.GroupBy.filter "pyspark.pandas.groupby.GroupBy.filter")(func) | Return a copy of a DataFrame excluding elements from groups that do not satisfy the boolean criterion specified by func.  
[`GroupBy.first`](api/pyspark.pandas.groupby.GroupBy.first.html#pyspark.pandas.groupby.GroupBy.first "pyspark.pandas.groupby.GroupBy.first")([numeric_only,Â min_count]) | Compute first of group values.  
[`GroupBy.last`](api/pyspark.pandas.groupby.GroupBy.last.html#pyspark.pandas.groupby.GroupBy.last "pyspark.pandas.groupby.GroupBy.last")([numeric_only,Â min_count]) | Compute last of group values.  
[`GroupBy.max`](api/pyspark.pandas.groupby.GroupBy.max.html#pyspark.pandas.groupby.GroupBy.max "pyspark.pandas.groupby.GroupBy.max")([numeric_only,Â min_count]) | Compute max of group values.  
[`GroupBy.mean`](api/pyspark.pandas.groupby.GroupBy.mean.html#pyspark.pandas.groupby.GroupBy.mean "pyspark.pandas.groupby.GroupBy.mean")([numeric_only]) | Compute mean of groups, excluding missing values.  
[`GroupBy.median`](api/pyspark.pandas.groupby.GroupBy.median.html#pyspark.pandas.groupby.GroupBy.median "pyspark.pandas.groupby.GroupBy.median")([numeric_only,Â accuracy]) | Compute median of groups, excluding missing values.  
[`GroupBy.min`](api/pyspark.pandas.groupby.GroupBy.min.html#pyspark.pandas.groupby.GroupBy.min "pyspark.pandas.groupby.GroupBy.min")([numeric_only,Â min_count]) | Compute min of group values.  
[`GroupBy.nth`](api/pyspark.pandas.groupby.GroupBy.nth.html#pyspark.pandas.groupby.GroupBy.nth "pyspark.pandas.groupby.GroupBy.nth")(n) | Take the nth row from each group.  
[`GroupBy.prod`](api/pyspark.pandas.groupby.GroupBy.prod.html#pyspark.pandas.groupby.GroupBy.prod "pyspark.pandas.groupby.GroupBy.prod")([numeric_only,Â min_count]) | Compute prod of groups.  
[`GroupBy.rank`](api/pyspark.pandas.groupby.GroupBy.rank.html#pyspark.pandas.groupby.GroupBy.rank "pyspark.pandas.groupby.GroupBy.rank")([method,Â ascending]) | Provide the rank of values within each group.  
[`GroupBy.sem`](api/pyspark.pandas.groupby.GroupBy.sem.html#pyspark.pandas.groupby.GroupBy.sem "pyspark.pandas.groupby.GroupBy.sem")([ddof]) | Compute standard error of the mean of groups, excluding missing values.  
[`GroupBy.std`](api/pyspark.pandas.groupby.GroupBy.std.html#pyspark.pandas.groupby.GroupBy.std "pyspark.pandas.groupby.GroupBy.std")([ddof]) | Compute standard deviation of groups, excluding missing values.  
[`GroupBy.sum`](api/pyspark.pandas.groupby.GroupBy.sum.html#pyspark.pandas.groupby.GroupBy.sum "pyspark.pandas.groupby.GroupBy.sum")([numeric_only,Â min_count]) | Compute sum of group values  
[`GroupBy.var`](api/pyspark.pandas.groupby.GroupBy.var.html#pyspark.pandas.groupby.GroupBy.var "pyspark.pandas.groupby.GroupBy.var")([ddof,Â numeric_only]) | Compute variance of groups, excluding missing values.  
[`GroupBy.nunique`](api/pyspark.pandas.groupby.GroupBy.nunique.html#pyspark.pandas.groupby.GroupBy.nunique "pyspark.pandas.groupby.GroupBy.nunique")([dropna]) | Return DataFrame with number of distinct observations per group for each column.  
[`GroupBy.quantile`](api/pyspark.pandas.groupby.GroupBy.quantile.html#pyspark.pandas.groupby.GroupBy.quantile "pyspark.pandas.groupby.GroupBy.quantile")([q,Â accuracy]) | Return group values at the given quantile.  
[`GroupBy.size`](api/pyspark.pandas.groupby.GroupBy.size.html#pyspark.pandas.groupby.GroupBy.size "pyspark.pandas.groupby.GroupBy.size")() | Compute group sizes.  
[`GroupBy.diff`](api/pyspark.pandas.groupby.GroupBy.diff.html#pyspark.pandas.groupby.GroupBy.diff "pyspark.pandas.groupby.GroupBy.diff")([periods]) | First discrete difference of element.  
[`GroupBy.idxmax`](api/pyspark.pandas.groupby.GroupBy.idxmax.html#pyspark.pandas.groupby.GroupBy.idxmax "pyspark.pandas.groupby.GroupBy.idxmax")([skipna]) | Return index of first occurrence of maximum over requested axis in group.  
[`GroupBy.idxmin`](api/pyspark.pandas.groupby.GroupBy.idxmin.html#pyspark.pandas.groupby.GroupBy.idxmin "pyspark.pandas.groupby.GroupBy.idxmin")([skipna]) | Return index of first occurrence of minimum over requested axis in group.  
[`GroupBy.fillna`](api/pyspark.pandas.groupby.GroupBy.fillna.html#pyspark.pandas.groupby.GroupBy.fillna "pyspark.pandas.groupby.GroupBy.fillna")([value,Â method,Â axis,Â ...]) | Fill NA/NaN values in group.  
[`GroupBy.bfill`](api/pyspark.pandas.groupby.GroupBy.bfill.html#pyspark.pandas.groupby.GroupBy.bfill "pyspark.pandas.groupby.GroupBy.bfill")([limit]) | Synonym for DataFrame.fillna() with `method=`bfill``.  
[`GroupBy.ffill`](api/pyspark.pandas.groupby.GroupBy.ffill.html#pyspark.pandas.groupby.GroupBy.ffill "pyspark.pandas.groupby.GroupBy.ffill")([limit]) | Synonym for DataFrame.fillna() with `method=`ffill``.  
[`GroupBy.head`](api/pyspark.pandas.groupby.GroupBy.head.html#pyspark.pandas.groupby.GroupBy.head "pyspark.pandas.groupby.GroupBy.head")([n]) | Return first n rows of each group.  
[`GroupBy.shift`](api/pyspark.pandas.groupby.GroupBy.shift.html#pyspark.pandas.groupby.GroupBy.shift "pyspark.pandas.groupby.GroupBy.shift")([periods,Â fill_value]) | Shift each group by periods observations.  
[`GroupBy.tail`](api/pyspark.pandas.groupby.GroupBy.tail.html#pyspark.pandas.groupby.GroupBy.tail "pyspark.pandas.groupby.GroupBy.tail")([n]) | Return last n rows of each group.  
  
The following methods are available only for DataFrameGroupBy objects.

[`DataFrameGroupBy.describe`](api/pyspark.pandas.groupby.DataFrameGroupBy.describe.html#pyspark.pandas.groupby.DataFrameGroupBy.describe "pyspark.pandas.groupby.DataFrameGroupBy.describe")() | Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding `NaN` values.  
---|---  
  
The following methods are available only for SeriesGroupBy objects.

[`SeriesGroupBy.nsmallest`](api/pyspark.pandas.groupby.SeriesGroupBy.nsmallest.html#pyspark.pandas.groupby.SeriesGroupBy.nsmallest "pyspark.pandas.groupby.SeriesGroupBy.nsmallest")([n]) | Return the smallest n elements.  
---|---  
[`SeriesGroupBy.nlargest`](api/pyspark.pandas.groupby.SeriesGroupBy.nlargest.html#pyspark.pandas.groupby.SeriesGroupBy.nlargest "pyspark.pandas.groupby.SeriesGroupBy.nlargest")([n]) | Return the first n rows ordered by columns in descending order in group.  
[`SeriesGroupBy.value_counts`](api/pyspark.pandas.groupby.SeriesGroupBy.value_counts.html#pyspark.pandas.groupby.SeriesGroupBy.value_counts "pyspark.pandas.groupby.SeriesGroupBy.value_counts")([sort,Â ...]) | Compute group sizes.  
[`SeriesGroupBy.unique`](api/pyspark.pandas.groupby.SeriesGroupBy.unique.html#pyspark.pandas.groupby.SeriesGroupBy.unique "pyspark.pandas.groupby.SeriesGroupBy.unique")() | Return unique values in group.  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/groupby.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/groupby.html

# GroupBy#

GroupBy objects are returned by groupby calls: [`DataFrame.groupby()`](api/pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby"), [`Series.groupby()`](api/pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby"), etc.

## Indexing, iteration#

[`GroupBy.get_group`](api/pyspark.pandas.groupby.GroupBy.get_group.html#pyspark.pandas.groupby.GroupBy.get_group "pyspark.pandas.groupby.GroupBy.get_group")(name) | Construct DataFrame from group with provided name.  
---|---  
  
## Function application#

[`GroupBy.apply`](api/pyspark.pandas.groupby.GroupBy.apply.html#pyspark.pandas.groupby.GroupBy.apply "pyspark.pandas.groupby.GroupBy.apply")(func,Â *args,Â **kwargs) | Apply function func group-wise and combine the results together.  
---|---  
[`GroupBy.transform`](api/pyspark.pandas.groupby.GroupBy.transform.html#pyspark.pandas.groupby.GroupBy.transform "pyspark.pandas.groupby.GroupBy.transform")(func,Â *args,Â **kwargs) | Apply function column-by-column to the GroupBy object.  
  
The following methods are available only for DataFrameGroupBy objects.

[`DataFrameGroupBy.agg`](api/pyspark.pandas.groupby.DataFrameGroupBy.agg.html#pyspark.pandas.groupby.DataFrameGroupBy.agg "pyspark.pandas.groupby.DataFrameGroupBy.agg")([func_or_funcs]) | Aggregate using one or more operations over the specified axis.  
---|---  
[`DataFrameGroupBy.aggregate`](api/pyspark.pandas.groupby.DataFrameGroupBy.aggregate.html#pyspark.pandas.groupby.DataFrameGroupBy.aggregate "pyspark.pandas.groupby.DataFrameGroupBy.aggregate")([func_or_funcs]) | Aggregate using one or more operations over the specified axis.  
  
## Computations / Descriptive Stats#

[`GroupBy.all`](api/pyspark.pandas.groupby.GroupBy.all.html#pyspark.pandas.groupby.GroupBy.all "pyspark.pandas.groupby.GroupBy.all")([skipna]) | Returns True if all values in the group are truthful, else False.  
---|---  
[`GroupBy.any`](api/pyspark.pandas.groupby.GroupBy.any.html#pyspark.pandas.groupby.GroupBy.any "pyspark.pandas.groupby.GroupBy.any")() | Returns True if any value in the group is truthful, else False.  
[`GroupBy.count`](api/pyspark.pandas.groupby.GroupBy.count.html#pyspark.pandas.groupby.GroupBy.count "pyspark.pandas.groupby.GroupBy.count")() | Compute count of group, excluding missing values.  
[`GroupBy.cumcount`](api/pyspark.pandas.groupby.GroupBy.cumcount.html#pyspark.pandas.groupby.GroupBy.cumcount "pyspark.pandas.groupby.GroupBy.cumcount")([ascending]) | Number each item in each group from 0 to the length of that group - 1.  
[`GroupBy.cummax`](api/pyspark.pandas.groupby.GroupBy.cummax.html#pyspark.pandas.groupby.GroupBy.cummax "pyspark.pandas.groupby.GroupBy.cummax")() | Cumulative max for each group.  
[`GroupBy.cummin`](api/pyspark.pandas.groupby.GroupBy.cummin.html#pyspark.pandas.groupby.GroupBy.cummin "pyspark.pandas.groupby.GroupBy.cummin")() | Cumulative min for each group.  
[`GroupBy.cumprod`](api/pyspark.pandas.groupby.GroupBy.cumprod.html#pyspark.pandas.groupby.GroupBy.cumprod "pyspark.pandas.groupby.GroupBy.cumprod")() | Cumulative product for each group.  
[`GroupBy.cumsum`](api/pyspark.pandas.groupby.GroupBy.cumsum.html#pyspark.pandas.groupby.GroupBy.cumsum "pyspark.pandas.groupby.GroupBy.cumsum")() | Cumulative sum for each group.  
[`GroupBy.ewm`](api/pyspark.pandas.groupby.GroupBy.ewm.html#pyspark.pandas.groupby.GroupBy.ewm "pyspark.pandas.groupby.GroupBy.ewm")([com,Â span,Â halflife,Â alpha,Â ...]) | Return an ewm grouper, providing ewm functionality per group.  
[`GroupBy.filter`](api/pyspark.pandas.groupby.GroupBy.filter.html#pyspark.pandas.groupby.GroupBy.filter "pyspark.pandas.groupby.GroupBy.filter")(func) | Return a copy of a DataFrame excluding elements from groups that do not satisfy the boolean criterion specified by func.  
[`GroupBy.first`](api/pyspark.pandas.groupby.GroupBy.first.html#pyspark.pandas.groupby.GroupBy.first "pyspark.pandas.groupby.GroupBy.first")([numeric_only,Â min_count]) | Compute first of group values.  
[`GroupBy.last`](api/pyspark.pandas.groupby.GroupBy.last.html#pyspark.pandas.groupby.GroupBy.last "pyspark.pandas.groupby.GroupBy.last")([numeric_only,Â min_count]) | Compute last of group values.  
[`GroupBy.max`](api/pyspark.pandas.groupby.GroupBy.max.html#pyspark.pandas.groupby.GroupBy.max "pyspark.pandas.groupby.GroupBy.max")([numeric_only,Â min_count]) | Compute max of group values.  
[`GroupBy.mean`](api/pyspark.pandas.groupby.GroupBy.mean.html#pyspark.pandas.groupby.GroupBy.mean "pyspark.pandas.groupby.GroupBy.mean")([numeric_only]) | Compute mean of groups, excluding missing values.  
[`GroupBy.median`](api/pyspark.pandas.groupby.GroupBy.median.html#pyspark.pandas.groupby.GroupBy.median "pyspark.pandas.groupby.GroupBy.median")([numeric_only,Â accuracy]) | Compute median of groups, excluding missing values.  
[`GroupBy.min`](api/pyspark.pandas.groupby.GroupBy.min.html#pyspark.pandas.groupby.GroupBy.min "pyspark.pandas.groupby.GroupBy.min")([numeric_only,Â min_count]) | Compute min of group values.  
[`GroupBy.nth`](api/pyspark.pandas.groupby.GroupBy.nth.html#pyspark.pandas.groupby.GroupBy.nth "pyspark.pandas.groupby.GroupBy.nth")(n) | Take the nth row from each group.  
[`GroupBy.prod`](api/pyspark.pandas.groupby.GroupBy.prod.html#pyspark.pandas.groupby.GroupBy.prod "pyspark.pandas.groupby.GroupBy.prod")([numeric_only,Â min_count]) | Compute prod of groups.  
[`GroupBy.rank`](api/pyspark.pandas.groupby.GroupBy.rank.html#pyspark.pandas.groupby.GroupBy.rank "pyspark.pandas.groupby.GroupBy.rank")([method,Â ascending]) | Provide the rank of values within each group.  
[`GroupBy.sem`](api/pyspark.pandas.groupby.GroupBy.sem.html#pyspark.pandas.groupby.GroupBy.sem "pyspark.pandas.groupby.GroupBy.sem")([ddof]) | Compute standard error of the mean of groups, excluding missing values.  
[`GroupBy.std`](api/pyspark.pandas.groupby.GroupBy.std.html#pyspark.pandas.groupby.GroupBy.std "pyspark.pandas.groupby.GroupBy.std")([ddof]) | Compute standard deviation of groups, excluding missing values.  
[`GroupBy.sum`](api/pyspark.pandas.groupby.GroupBy.sum.html#pyspark.pandas.groupby.GroupBy.sum "pyspark.pandas.groupby.GroupBy.sum")([numeric_only,Â min_count]) | Compute sum of group values  
[`GroupBy.var`](api/pyspark.pandas.groupby.GroupBy.var.html#pyspark.pandas.groupby.GroupBy.var "pyspark.pandas.groupby.GroupBy.var")([ddof,Â numeric_only]) | Compute variance of groups, excluding missing values.  
[`GroupBy.nunique`](api/pyspark.pandas.groupby.GroupBy.nunique.html#pyspark.pandas.groupby.GroupBy.nunique "pyspark.pandas.groupby.GroupBy.nunique")([dropna]) | Return DataFrame with number of distinct observations per group for each column.  
[`GroupBy.quantile`](api/pyspark.pandas.groupby.GroupBy.quantile.html#pyspark.pandas.groupby.GroupBy.quantile "pyspark.pandas.groupby.GroupBy.quantile")([q,Â accuracy]) | Return group values at the given quantile.  
[`GroupBy.size`](api/pyspark.pandas.groupby.GroupBy.size.html#pyspark.pandas.groupby.GroupBy.size "pyspark.pandas.groupby.GroupBy.size")() | Compute group sizes.  
[`GroupBy.diff`](api/pyspark.pandas.groupby.GroupBy.diff.html#pyspark.pandas.groupby.GroupBy.diff "pyspark.pandas.groupby.GroupBy.diff")([periods]) | First discrete difference of element.  
[`GroupBy.idxmax`](api/pyspark.pandas.groupby.GroupBy.idxmax.html#pyspark.pandas.groupby.GroupBy.idxmax "pyspark.pandas.groupby.GroupBy.idxmax")([skipna]) | Return index of first occurrence of maximum over requested axis in group.  
[`GroupBy.idxmin`](api/pyspark.pandas.groupby.GroupBy.idxmin.html#pyspark.pandas.groupby.GroupBy.idxmin "pyspark.pandas.groupby.GroupBy.idxmin")([skipna]) | Return index of first occurrence of minimum over requested axis in group.  
[`GroupBy.fillna`](api/pyspark.pandas.groupby.GroupBy.fillna.html#pyspark.pandas.groupby.GroupBy.fillna "pyspark.pandas.groupby.GroupBy.fillna")([value,Â method,Â axis,Â ...]) | Fill NA/NaN values in group.  
[`GroupBy.bfill`](api/pyspark.pandas.groupby.GroupBy.bfill.html#pyspark.pandas.groupby.GroupBy.bfill "pyspark.pandas.groupby.GroupBy.bfill")([limit]) | Synonym for DataFrame.fillna() with `method=`bfill``.  
[`GroupBy.ffill`](api/pyspark.pandas.groupby.GroupBy.ffill.html#pyspark.pandas.groupby.GroupBy.ffill "pyspark.pandas.groupby.GroupBy.ffill")([limit]) | Synonym for DataFrame.fillna() with `method=`ffill``.  
[`GroupBy.head`](api/pyspark.pandas.groupby.GroupBy.head.html#pyspark.pandas.groupby.GroupBy.head "pyspark.pandas.groupby.GroupBy.head")([n]) | Return first n rows of each group.  
[`GroupBy.shift`](api/pyspark.pandas.groupby.GroupBy.shift.html#pyspark.pandas.groupby.GroupBy.shift "pyspark.pandas.groupby.GroupBy.shift")([periods,Â fill_value]) | Shift each group by periods observations.  
[`GroupBy.tail`](api/pyspark.pandas.groupby.GroupBy.tail.html#pyspark.pandas.groupby.GroupBy.tail "pyspark.pandas.groupby.GroupBy.tail")([n]) | Return last n rows of each group.  
  
The following methods are available only for DataFrameGroupBy objects.

[`DataFrameGroupBy.describe`](api/pyspark.pandas.groupby.DataFrameGroupBy.describe.html#pyspark.pandas.groupby.DataFrameGroupBy.describe "pyspark.pandas.groupby.DataFrameGroupBy.describe")() | Generate descriptive statistics that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding `NaN` values.  
---|---  
  
The following methods are available only for SeriesGroupBy objects.

[`SeriesGroupBy.nsmallest`](api/pyspark.pandas.groupby.SeriesGroupBy.nsmallest.html#pyspark.pandas.groupby.SeriesGroupBy.nsmallest "pyspark.pandas.groupby.SeriesGroupBy.nsmallest")([n]) | Return the smallest n elements.  
---|---  
[`SeriesGroupBy.nlargest`](api/pyspark.pandas.groupby.SeriesGroupBy.nlargest.html#pyspark.pandas.groupby.SeriesGroupBy.nlargest "pyspark.pandas.groupby.SeriesGroupBy.nlargest")([n]) | Return the first n rows ordered by columns in descending order in group.  
[`SeriesGroupBy.value_counts`](api/pyspark.pandas.groupby.SeriesGroupBy.value_counts.html#pyspark.pandas.groupby.SeriesGroupBy.value_counts "pyspark.pandas.groupby.SeriesGroupBy.value_counts")([sort,Â ...]) | Compute group sizes.  
[`SeriesGroupBy.unique`](api/pyspark.pandas.groupby.SeriesGroupBy.unique.html#pyspark.pandas.groupby.SeriesGroupBy.unique "pyspark.pandas.groupby.SeriesGroupBy.unique")() | Return unique values in group.  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/groupby.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.get_group.html

# pyspark.pandas.groupby.GroupBy.get_group#

GroupBy.get_group(_name_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.get_group)#
    

Construct DataFrame from group with provided name.

Parameters
    

**name** object
    

The name of the group to get as a DataFrame.

Returns
    

**group** same type as obj
    

Examples
    
    
    >>> psdf = ps.DataFrame([('falcon', 'bird', 389.0),
    ...                     ('parrot', 'bird', 24.0),
    ...                     ('lion', 'mammal', 80.5),
    ...                     ('monkey', 'mammal', np.nan)],
    ...                    columns=['name', 'class', 'max_speed'],
    ...                    index=[0, 2, 3, 1])
    >>> psdf
         name   class  max_speed
    0  falcon    bird      389.0
    2  parrot    bird       24.0
    3    lion  mammal       80.5
    1  monkey  mammal        NaN
    
    
    
    >>> psdf.groupby("class").get_group("bird").sort_index()
         name class  max_speed
    0  falcon  bird      389.0
    2  parrot  bird       24.0
    
    
    
    >>> psdf.groupby("class").get_group("mammal").sort_index()
         name   class  max_speed
    1  monkey  mammal        NaN
    3    lion  mammal       80.5
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.get_group.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.apply.html

# pyspark.pandas.groupby.GroupBy.apply#

GroupBy.apply(_func_ , _* args_, _** kwargs_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.apply)#
    

Apply function func group-wise and combine the results together.

The function passed to apply must take a DataFrame as its first argument and return a DataFrame. apply will then take care of combining the results back together into a single dataframe. apply is therefore a highly flexible grouping method.

While apply is a very flexible method, its downside is that using it can be quite a bit slower than using more specific methods like agg or transform. pandas-on-Spark offers a wide range of method that will be much faster than using apply for their specific purposes, so try to use them before reaching for apply.

Note

this API executes the function once to infer the type which is potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:
    
    
    >>> def pandas_div(x) -> ps.DataFrame[int, [float, float]]:
    ...     return x[['B', 'C']] / x[['B', 'C']]
    

If the return type is specified, the output column names become c0, c1, c2 â¦ cn. These names are positionally mapped to the returned DataFrame in `func`.

To specify the column names, you can assign them in a NumPy compound type style as below:
    
    
    >>> def pandas_div(x) -> ps.DataFrame[("index", int), [("a", float), ("b", float)]]:
    ...     return x[['B', 'C']] / x[['B', 'C']]
    
    
    
    >>> pdf = pd.DataFrame({'B': [1.], 'C': [3.]})
    >>> def plus_one(x) -> ps.DataFrame[
    ...         (pdf.index.name, pdf.index.dtype), zip(pdf.columns, pdf.dtypes)]:
    ...     return x[['B', 'C']] / x[['B', 'C']]
    

Note

the dataframe within `func` is actually a pandas dataframe. Therefore, any pandas API within this function is allowed.

Parameters
    

**func** callable
    

A callable that takes a DataFrame as its first argument, and returns a dataframe.

***args**
    

Positional arguments to pass to func.

****kwargs**
    

Keyword arguments to pass to func.

Returns
    

**applied** DataFrame or Series
    

See also

`aggregate`
    

Apply aggregate function to the GroupBy object.

`DataFrame.apply`
    

Apply a function to a DataFrame.

`Series.apply`
    

Apply a function to a Series.

Examples
    
    
    >>> df = ps.DataFrame({'A': 'a a b'.split(),
    ...                    'B': [1, 2, 3],
    ...                    'C': [4, 6, 5]}, columns=['A', 'B', 'C'])
    >>> g = df.groupby('A')
    

Notice that `g` has two groups, `a` and `b`. Calling apply in various ways, we can get different grouping results:

Below the functions passed to apply takes a DataFrame as its argument and returns a DataFrame. apply combines the result for each group together into a new DataFrame:
    
    
    >>> def plus_min(x):
    ...     return x + x.min()
    >>> g.apply(plus_min).sort_index()  
        A  B   C
    0  aa  2   8
    1  aa  3  10
    2  bb  6  10
    
    
    
    >>> g.apply(sum).sort_index()  
        A  B   C
    A
    a  aa  3  10
    b   b  3   5
    
    
    
    >>> g.apply(len).sort_index()  
    A
    a    2
    b    1
    dtype: int64
    

You can specify the type hint and prevent schema inference for better performance.
    
    
    >>> def pandas_div(x) -> ps.DataFrame[int, [float, float]]:
    ...     return x[['B', 'C']] / x[['B', 'C']]
    >>> g.apply(pandas_div).sort_index()  
        c0   c1
    0  1.0  1.0
    1  1.0  1.0
    2  1.0  1.0
    
    
    
    >>> def pandas_div(x) -> ps.DataFrame[("index", int), [("f1", float), ("f2", float)]]:
    ...     return x[['B', 'C']] / x[['B', 'C']]
    >>> g.apply(pandas_div).sort_index()  
            f1   f2
    index
    0      1.0  1.0
    1      1.0  1.0
    2      1.0  1.0
    

In case of Series, it works as below.
    
    
    >>> def plus_max(x) -> ps.Series[int]:
    ...     return x + x.max()
    >>> df.B.groupby(df.A).apply(plus_max).sort_index()  
    0    6
    1    3
    2    4
    Name: B, dtype: int64
    
    
    
    >>> def plus_min(x):
    ...     return x + x.min()
    >>> df.B.groupby(df.A).apply(plus_min).sort_index()  
    0    2
    1    3
    2    6
    Name: B, dtype: int64
    

You can also return a scalar value as an aggregated value of the group:
    
    
    >>> def plus_length(x) -> int:
    ...     return len(x)
    >>> df.B.groupby(df.A).apply(plus_length).sort_index()  
    0    1
    1    2
    Name: B, dtype: int64
    

The extra arguments to the function can be passed as below.
    
    
    >>> def calculation(x, y, z) -> int:
    ...     return len(x) + y * z
    >>> df.B.groupby(df.A).apply(calculation, 5, z=10).sort_index()  
    0    51
    1    52
    Name: B, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.apply.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.transform.html

# pyspark.pandas.groupby.GroupBy.transform#

GroupBy.transform(_func_ , _* args_, _** kwargs_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.transform)#
    

Apply function column-by-column to the GroupBy object.

The function passed to transform must take a Series as its first argument and return a Series. The given function is executed for each series in each grouped data.

While transform is a very flexible method, its downside is that using it can be quite a bit slower than using more specific methods like agg or transform. pandas-on-Spark offers a wide range of method that will be much faster than using transform for their specific purposes, so try to use them before reaching for transform.

Note

this API executes the function once to infer the type which is
    

potentially expensive, for instance, when the dataset is created after aggregations or sorting.

To avoid this, specify return type in `func`, for instance, as below:
    
    
    >>> def convert_to_string(x) -> ps.Series[str]:
    ...     return x.apply("a string {}".format)
    

When the given function has the return type annotated, the original index of the GroupBy object will be lost, and a default index will be attached to the result. Please be careful about configuring the default index. See also [Default Index Type](https://spark.apache.org/docs/latest/api/python/tutorial/pandas_on_spark/options.html#default-index-type).

Note

the series within `func` is actually a pandas series. Therefore, any pandas API within this function is allowed.

Parameters
    

**func** callable
    

A callable that takes a Series as its first argument, and returns a Series.

***args**
    

Positional arguments to pass to func.

****kwargs**
    

Keyword arguments to pass to func.

Returns
    

**applied** DataFrame
    

See also

`aggregate`
    

Apply aggregate function to the GroupBy object.

`Series.apply`
    

Apply a function to a Series.

Examples
    
    
    >>> df = ps.DataFrame({'A': [0, 0, 1],
    ...                    'B': [1, 2, 3],
    ...                    'C': [4, 6, 5]}, columns=['A', 'B', 'C'])
    
    
    
    >>> g = df.groupby('A')
    

Notice that `g` has two groups, `0` and `1`. Calling transform in various ways, we can get different grouping results: Below the functions passed to transform takes a Series as its argument and returns a Series. transform applies the function on each series in each grouped data, and combine them into a new DataFrame:
    
    
    >>> def convert_to_string(x) -> ps.Series[str]:
    ...     return x.apply("a string {}".format)
    >>> g.transform(convert_to_string)  
                B           C
    0  a string 1  a string 4
    1  a string 2  a string 6
    2  a string 3  a string 5
    
    
    
    >>> def plus_max(x) -> ps.Series[int]:
    ...     return x + x.max()
    >>> g.transform(plus_max)  
       B   C
    0  3  10
    1  4  12
    2  6  10
    

You can omit the type hint and let pandas-on-Spark infer its type.
    
    
    >>> def plus_min(x):
    ...     return x + x.min()
    >>> g.transform(plus_min)  
       B   C
    0  2   8
    1  3  10
    2  6  10
    

In case of Series, it works as below.
    
    
    >>> df.B.groupby(df.A).transform(plus_max)
    0    3
    1    4
    2    6
    Name: B, dtype: int64
    
    
    
    >>> (df * -1).B.groupby(df.A).transform(abs)
    0    1
    1    2
    2    3
    Name: B, dtype: int64
    

You can also specify extra arguments to pass to the function.
    
    
    >>> def calculation(x, y, z) -> ps.Series[int]:
    ...     return x + x.min() + y + z
    >>> g.transform(calculation, 5, z=20)  
        B   C
    0  27  33
    1  28  35
    2  31  35
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.transform.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.DataFrameGroupBy.agg.html

# pyspark.pandas.groupby.DataFrameGroupBy.agg#

DataFrameGroupBy.agg(_func_or_funcs =None_, _* args_, _** kwargs_)#
    

Aggregate using one or more operations over the specified axis.

Parameters
    

**func_or_funcs** dict, str or list
    

a dict mapping from column name (string) to aggregate functions (string or list of strings).

Returns
    

Series or DataFrame
    

The return can be:

  * Series : when DataFrame.agg is called with a single function

  * DataFrame : when DataFrame.agg is called with several functions




Return Series or DataFrame.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Notes

agg is an alias for aggregate. Use the alias.

Examples
    
    
    >>> df = ps.DataFrame({'A': [1, 1, 2, 2],
    ...                    'B': [1, 2, 3, 4],
    ...                    'C': [0.362, 0.227, 1.267, -0.562]},
    ...                   columns=['A', 'B', 'C'])
    
    
    
    >>> df
       A  B      C
    0  1  1  0.362
    1  1  2  0.227
    2  2  3  1.267
    3  2  4 -0.562
    

Different aggregations per column
    
    
    >>> aggregated = df.groupby('A').agg({'B': 'min', 'C': 'sum'})
    >>> aggregated[['B', 'C']].sort_index()  
       B      C
    A
    1  1  0.589
    2  3  0.705
    
    
    
    >>> aggregated = df.groupby('A').agg({'B': ['min', 'max']})
    >>> aggregated.sort_index()  
         B
       min  max
    A
    1    1    2
    2    3    4
    
    
    
    >>> aggregated = df.groupby('A').agg('min')
    >>> aggregated.sort_index()  
         B      C
    A
    1    1  0.227
    2    3 -0.562
    
    
    
    >>> aggregated = df.groupby('A').agg(['min', 'max'])
    >>> aggregated.sort_index()  
         B           C
       min  max    min    max
    A
    1    1    2  0.227  0.362
    2    3    4 -0.562  1.267
    

To control the output names with different aggregations per column, pandas-on-Spark also supports ânamed aggregationâ or nested renaming in .agg. It can also be used when applying multiple aggregation functions to specific columns.
    
    
    >>> aggregated = df.groupby('A').agg(b_max=ps.NamedAgg(column='B', aggfunc='max'))
    >>> aggregated.sort_index()  
         b_max
    A
    1        2
    2        4
    
    
    
    >>> aggregated = df.groupby('A').agg(b_max=('B', 'max'), b_min=('B', 'min'))
    >>> aggregated.sort_index()  
         b_max   b_min
    A
    1        2       1
    2        4       3
    
    
    
    >>> aggregated = df.groupby('A').agg(b_max=('B', 'max'), c_min=('C', 'min'))
    >>> aggregated.sort_index()  
         b_max   c_min
    A
    1        2   0.227
    2        4  -0.562
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.DataFrameGroupBy.agg.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.DataFrameGroupBy.aggregate.html

# pyspark.pandas.groupby.DataFrameGroupBy.aggregate#

DataFrameGroupBy.aggregate(_func_or_funcs =None_, _* args_, _** kwargs_)#
    

Aggregate using one or more operations over the specified axis.

Parameters
    

**func_or_funcs** dict, str or list
    

a dict mapping from column name (string) to aggregate functions (string or list of strings).

Returns
    

Series or DataFrame
    

The return can be:

  * Series : when DataFrame.agg is called with a single function

  * DataFrame : when DataFrame.agg is called with several functions




Return Series or DataFrame.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Notes

agg is an alias for aggregate. Use the alias.

Examples
    
    
    >>> df = ps.DataFrame({'A': [1, 1, 2, 2],
    ...                    'B': [1, 2, 3, 4],
    ...                    'C': [0.362, 0.227, 1.267, -0.562]},
    ...                   columns=['A', 'B', 'C'])
    
    
    
    >>> df
       A  B      C
    0  1  1  0.362
    1  1  2  0.227
    2  2  3  1.267
    3  2  4 -0.562
    

Different aggregations per column
    
    
    >>> aggregated = df.groupby('A').agg({'B': 'min', 'C': 'sum'})
    >>> aggregated[['B', 'C']].sort_index()  
       B      C
    A
    1  1  0.589
    2  3  0.705
    
    
    
    >>> aggregated = df.groupby('A').agg({'B': ['min', 'max']})
    >>> aggregated.sort_index()  
         B
       min  max
    A
    1    1    2
    2    3    4
    
    
    
    >>> aggregated = df.groupby('A').agg('min')
    >>> aggregated.sort_index()  
         B      C
    A
    1    1  0.227
    2    3 -0.562
    
    
    
    >>> aggregated = df.groupby('A').agg(['min', 'max'])
    >>> aggregated.sort_index()  
         B           C
       min  max    min    max
    A
    1    1    2  0.227  0.362
    2    3    4 -0.562  1.267
    

To control the output names with different aggregations per column, pandas-on-Spark also supports ânamed aggregationâ or nested renaming in .agg. It can also be used when applying multiple aggregation functions to specific columns.
    
    
    >>> aggregated = df.groupby('A').agg(b_max=ps.NamedAgg(column='B', aggfunc='max'))
    >>> aggregated.sort_index()  
         b_max
    A
    1        2
    2        4
    
    
    
    >>> aggregated = df.groupby('A').agg(b_max=('B', 'max'), b_min=('B', 'min'))
    >>> aggregated.sort_index()  
         b_max   b_min
    A
    1        2       1
    2        4       3
    
    
    
    >>> aggregated = df.groupby('A').agg(b_max=('B', 'max'), c_min=('C', 'min'))
    >>> aggregated.sort_index()  
         b_max   c_min
    A
    1        2   0.227
    2        4  -0.562
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.DataFrameGroupBy.aggregate.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.min.html

# pyspark.pandas.groupby.GroupBy.min#

GroupBy.min(_numeric_only =False_, _min_count =- 1_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.min)#
    

Compute min of group values.

New in version 3.3.0.

Parameters
    

**numeric_only** bool, default False
    

Include only float, int, boolean columns. If None, will attempt to use everything, then use only numeric data.

New in version 3.4.0.

**min_count** bool, default -1
    

The required number of valid values to perform the operation. If fewer than min_count non-NA values are present the result will be NA.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
    ...                    "C": [3, 4, 3, 4], "D": ["a", "a", "b", "a"]})
    >>> df.groupby("A").min().sort_index()
           B  C  D
    A
    1  False  3  a
    2  False  4  a
    

Include only float, int, boolean columns when set numeric_only True.
    
    
    >>> df.groupby("A").min(numeric_only=True).sort_index()
           B  C
    A
    1  False  3
    2  False  4
    
    
    
    >>> df.groupby("D").min().sort_index()
       A      B  C
    D
    a  1  False  3
    b  1  False  3
    
    
    
    >>> df.groupby("D").min(min_count=3).sort_index()
         A      B    C
    D
    a  1.0  False  3.0
    b  NaN   None  NaN
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.min.rst.txt)


---

## 🔹 009. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nth.html

# pyspark.pandas.groupby.GroupBy.nth#

GroupBy.nth(_n_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.nth)#
    

Take the nth row from each group.

New in version 3.4.0.

Parameters
    

**n** int
    

A single nth value for the row

Returns
    

Series or DataFrame
    

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Notes

There is a behavior difference between pandas-on-Spark and pandas:

  * when there is no aggregation column, and n not equal to 0 or -1,
    

the returned empty dataframe may have an index with different lenght __len__.




Examples
    
    
    >>> import numpy as np
    >>> df = ps.DataFrame({'A': [1, 1, 2, 1, 2],
    ...                    'B': [np.nan, 2, 3, 4, 5]}, columns=['A', 'B'])
    >>> g = df.groupby('A')
    >>> g.nth(0)
       A    B
    0  1  NaN
    2  2  3.0
    >>> g.nth(1)
       A    B
    1  1  2.0
    4  2  5.0
    >>> g.nth(-1)
       A    B
    3  1  4.0
    4  2  5.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nth.rst.txt)


---

## 🔹 010. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.prod.html

# pyspark.pandas.groupby.GroupBy.prod#

GroupBy.prod(_numeric_only =False_, _min_count =0_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.prod)#
    

Compute prod of groups.

New in version 3.4.0.

Parameters
    

**numeric_only** bool, default False
    

Include only float, int, boolean columns.

Changed in version 4.0.0.

**min_count** int, default 0
    

The required number of valid values to perform the operation. If fewer than min_count non-NA values are present the result will be NA.

Returns
    

Series or DataFrame
    

Computed prod of values within each group.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> df = ps.DataFrame(
    ...     {
    ...         "A": [1, 1, 2, 1, 2],
    ...         "B": [np.nan, 2, 3, 4, 5],
    ...         "C": [1, 2, 1, 1, 2],
    ...         "D": [True, False, True, False, True],
    ...     }
    ... )
    

Groupby one column and return the prod of the remaining columns in each group.
    
    
    >>> df.groupby('A').prod().sort_index()
         B  C  D
    A
    1  8.0  2  0
    2  15.0 2  1
    
    
    
    >>> df.groupby('A').prod(min_count=3).sort_index()
         B  C   D
    A
    1  NaN  2.0  0.0
    2  NaN NaN  NaN
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.prod.rst.txt)


---

## 🔹 011. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.rank.html

# pyspark.pandas.groupby.GroupBy.rank#

GroupBy.rank(_method ='average'_, _ascending =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.rank)#
    

Provide the rank of values within each group.

Parameters
    

**method**{âaverageâ, âminâ, âmaxâ, âfirstâ, âdenseâ}, default âaverageâ
    

  * average: average rank of group

  * min: lowest rank in group

  * max: highest rank in group

  * first: ranks assigned in order they appear in the array

  * dense: like âminâ, but rank always increases by 1 between groups



**ascending** boolean, default True
    

False for ranks by high (1) to low (N)

Returns
    

DataFrame with ranking of values within each group
    

Examples
    
    
    >>> df = ps.DataFrame({
    ...     'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...     'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
    >>> df
       a  b
    0  1  1
    1  1  2
    2  1  2
    3  2  2
    4  2  3
    5  2  3
    6  3  3
    7  3  4
    8  3  4
    
    
    
    >>> df.groupby("a").rank().sort_index()
         b
    0  1.0
    1  2.5
    2  2.5
    3  1.0
    4  2.5
    5  2.5
    6  1.0
    7  2.5
    8  2.5
    
    
    
    >>> df.b.groupby(df.a).rank(method='max').sort_index()
    0    1.0
    1    3.0
    2    3.0
    3    1.0
    4    3.0
    5    3.0
    6    1.0
    7    3.0
    8    3.0
    Name: b, dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.rank.rst.txt)


---

## 🔹 012. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sem.html

# pyspark.pandas.groupby.GroupBy.sem#

GroupBy.sem(_ddof =1_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.sem)#
    

Compute standard error of the mean of groups, excluding missing values.

New in version 3.4.0.

Parameters
    

**ddof** int, default 1
    

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

See also

[`pyspark.pandas.Series.sem`](pyspark.pandas.Series.sem.html#pyspark.pandas.Series.sem "pyspark.pandas.Series.sem")
    
[`pyspark.pandas.DataFrame.sem`](pyspark.pandas.DataFrame.sem.html#pyspark.pandas.DataFrame.sem "pyspark.pandas.DataFrame.sem")
    

Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 1], "B": [True, False, False, True],
    ...                    "C": [3, None, 3, 4], "D": ["a", "b", "b", "a"]})
    
    
    
    >>> df.groupby("A").sem()
              B         C
    A
    1  0.333333  0.333333
    2       NaN       NaN
    
    
    
    >>> df.groupby("D").sem(ddof=1)
         A    B    C
    D
    a  0.0  0.0  0.5
    b  0.5  0.0  NaN
    
    
    
    >>> df.B.groupby(df.A).sem()
    A
    1    0.333333
    2         NaN
    Name: B, dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sem.rst.txt)


---

## 🔹 013. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.std.html

# pyspark.pandas.groupby.GroupBy.std#

GroupBy.std(_ddof =1_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.std)#
    

Compute standard deviation of groups, excluding missing values.

New in version 3.3.0.

Parameters
    

**ddof** int, default 1
    

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

Changed in version 3.4.0: Supported including arbitary integers.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
    ...                    "C": [3, 4, 3, 4], "D": ["a", "b", "b", "a"]})
    
    
    
    >>> df.groupby("A").std()
              B    C
    A
    1  0.707107  0.0
    2  0.707107  0.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.std.rst.txt)


---

## 🔹 014. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sum.html

# pyspark.pandas.groupby.GroupBy.sum#

GroupBy.sum(_numeric_only =False_, _min_count =0_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.sum)#
    

Compute sum of group values

New in version 3.3.0.

Parameters
    

**numeric_only** bool, default False
    

Include only float, int, boolean columns.

New in version 3.4.0.

Changed in version 4.0.0.

**min_count** int, default 0
    

The required number of valid values to perform the operation. If fewer than min_count non-NA values are present the result will be NA.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Notes

There is a behavior difference between pandas-on-Spark and pandas:

  * when there is a non-numeric aggregation column, it will be ignored
    

even if numeric_only is False.




Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
    ...                    "C": [3, 4, 3, 4], "D": ["a", "a", "b", "a"]})
    
    
    
    >>> df.groupby("A").sum().sort_index()
       B  C   D
    A
    1  1  6  ab
    2  1  8  aa
    
    
    
    >>> df.groupby("D").sum().sort_index()
       A  B   C
    D
    a  5  2  11
    b  1  0   3
    
    
    
    >>> df.groupby("D").sum(min_count=3).sort_index()
         A    B     C
    D
    a  5.0  2.0  11.0
    b  NaN  NaN   NaN
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sum.rst.txt)


---

## 🔹 015. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nunique.html

# pyspark.pandas.groupby.GroupBy.nunique#

GroupBy.nunique(_dropna =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.nunique)#
    

Return DataFrame with number of distinct observations per group for each column.

Parameters
    

**dropna** boolean, default True
    

Donât include NaN in the counts.

Returns
    

**nunique** DataFrame or Series
    

Examples
    
    
    >>> df = ps.DataFrame({'id': ['spam', 'egg', 'egg', 'spam',
    ...                           'ham', 'ham'],
    ...                    'value1': [1, 5, 5, 2, 5, 5],
    ...                    'value2': list('abbaxy')}, columns=['id', 'value1', 'value2'])
    >>> df
         id  value1 value2
    0  spam       1      a
    1   egg       5      b
    2   egg       5      b
    3  spam       2      a
    4   ham       5      x
    5   ham       5      y
    
    
    
    >>> df.groupby('id').nunique().sort_index() 
          value1  value2
    id
    egg        1       1
    ham        1       2
    spam       2       1
    
    
    
    >>> df.groupby('id')['value1'].nunique().sort_index() 
    id
    egg     1
    ham     1
    spam    2
    Name: value1, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nunique.rst.txt)


---

## 🔹 016. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nth.html

# pyspark.pandas.groupby.GroupBy.nth#

GroupBy.nth(_n_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.nth)#
    

Take the nth row from each group.

New in version 3.4.0.

Parameters
    

**n** int
    

A single nth value for the row

Returns
    

Series or DataFrame
    

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Notes

There is a behavior difference between pandas-on-Spark and pandas:

  * when there is no aggregation column, and n not equal to 0 or -1,
    

the returned empty dataframe may have an index with different lenght __len__.




Examples
    
    
    >>> import numpy as np
    >>> df = ps.DataFrame({'A': [1, 1, 2, 1, 2],
    ...                    'B': [np.nan, 2, 3, 4, 5]}, columns=['A', 'B'])
    >>> g = df.groupby('A')
    >>> g.nth(0)
       A    B
    0  1  NaN
    2  2  3.0
    >>> g.nth(1)
       A    B
    1  1  2.0
    4  2  5.0
    >>> g.nth(-1)
       A    B
    3  1  4.0
    4  2  5.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nth.rst.txt)


---

## 🔹 017. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.prod.html

# pyspark.pandas.groupby.GroupBy.prod#

GroupBy.prod(_numeric_only =False_, _min_count =0_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.prod)#
    

Compute prod of groups.

New in version 3.4.0.

Parameters
    

**numeric_only** bool, default False
    

Include only float, int, boolean columns.

Changed in version 4.0.0.

**min_count** int, default 0
    

The required number of valid values to perform the operation. If fewer than min_count non-NA values are present the result will be NA.

Returns
    

Series or DataFrame
    

Computed prod of values within each group.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> import numpy as np
    >>> df = ps.DataFrame(
    ...     {
    ...         "A": [1, 1, 2, 1, 2],
    ...         "B": [np.nan, 2, 3, 4, 5],
    ...         "C": [1, 2, 1, 1, 2],
    ...         "D": [True, False, True, False, True],
    ...     }
    ... )
    

Groupby one column and return the prod of the remaining columns in each group.
    
    
    >>> df.groupby('A').prod().sort_index()
         B  C  D
    A
    1  8.0  2  0
    2  15.0 2  1
    
    
    
    >>> df.groupby('A').prod(min_count=3).sort_index()
         B  C   D
    A
    1  NaN  2.0  0.0
    2  NaN NaN  NaN
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.prod.rst.txt)


---

## 🔹 018. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.rank.html

# pyspark.pandas.groupby.GroupBy.rank#

GroupBy.rank(_method ='average'_, _ascending =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.rank)#
    

Provide the rank of values within each group.

Parameters
    

**method**{âaverageâ, âminâ, âmaxâ, âfirstâ, âdenseâ}, default âaverageâ
    

  * average: average rank of group

  * min: lowest rank in group

  * max: highest rank in group

  * first: ranks assigned in order they appear in the array

  * dense: like âminâ, but rank always increases by 1 between groups



**ascending** boolean, default True
    

False for ranks by high (1) to low (N)

Returns
    

DataFrame with ranking of values within each group
    

Examples
    
    
    >>> df = ps.DataFrame({
    ...     'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...     'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
    >>> df
       a  b
    0  1  1
    1  1  2
    2  1  2
    3  2  2
    4  2  3
    5  2  3
    6  3  3
    7  3  4
    8  3  4
    
    
    
    >>> df.groupby("a").rank().sort_index()
         b
    0  1.0
    1  2.5
    2  2.5
    3  1.0
    4  2.5
    5  2.5
    6  1.0
    7  2.5
    8  2.5
    
    
    
    >>> df.b.groupby(df.a).rank(method='max').sort_index()
    0    1.0
    1    3.0
    2    3.0
    3    1.0
    4    3.0
    5    3.0
    6    1.0
    7    3.0
    8    3.0
    Name: b, dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.rank.rst.txt)


---

## 🔹 019. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sem.html

# pyspark.pandas.groupby.GroupBy.sem#

GroupBy.sem(_ddof =1_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.sem)#
    

Compute standard error of the mean of groups, excluding missing values.

New in version 3.4.0.

Parameters
    

**ddof** int, default 1
    

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

See also

[`pyspark.pandas.Series.sem`](pyspark.pandas.Series.sem.html#pyspark.pandas.Series.sem "pyspark.pandas.Series.sem")
    
[`pyspark.pandas.DataFrame.sem`](pyspark.pandas.DataFrame.sem.html#pyspark.pandas.DataFrame.sem "pyspark.pandas.DataFrame.sem")
    

Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 1], "B": [True, False, False, True],
    ...                    "C": [3, None, 3, 4], "D": ["a", "b", "b", "a"]})
    
    
    
    >>> df.groupby("A").sem()
              B         C
    A
    1  0.333333  0.333333
    2       NaN       NaN
    
    
    
    >>> df.groupby("D").sem(ddof=1)
         A    B    C
    D
    a  0.0  0.0  0.5
    b  0.5  0.0  NaN
    
    
    
    >>> df.B.groupby(df.A).sem()
    A
    1    0.333333
    2         NaN
    Name: B, dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sem.rst.txt)


---

## 🔹 020. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.std.html

# pyspark.pandas.groupby.GroupBy.std#

GroupBy.std(_ddof =1_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.std)#
    

Compute standard deviation of groups, excluding missing values.

New in version 3.3.0.

Parameters
    

**ddof** int, default 1
    

Delta Degrees of Freedom. The divisor used in calculations is N - ddof, where N represents the number of elements.

Changed in version 3.4.0: Supported including arbitary integers.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
    ...                    "C": [3, 4, 3, 4], "D": ["a", "b", "b", "a"]})
    
    
    
    >>> df.groupby("A").std()
              B    C
    A
    1  0.707107  0.0
    2  0.707107  0.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.std.rst.txt)


---

## 🔹 021. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sum.html

# pyspark.pandas.groupby.GroupBy.sum#

GroupBy.sum(_numeric_only =False_, _min_count =0_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.sum)#
    

Compute sum of group values

New in version 3.3.0.

Parameters
    

**numeric_only** bool, default False
    

Include only float, int, boolean columns.

New in version 3.4.0.

Changed in version 4.0.0.

**min_count** int, default 0
    

The required number of valid values to perform the operation. If fewer than min_count non-NA values are present the result will be NA.

New in version 3.4.0.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Notes

There is a behavior difference between pandas-on-Spark and pandas:

  * when there is a non-numeric aggregation column, it will be ignored
    

even if numeric_only is False.




Examples
    
    
    >>> df = ps.DataFrame({"A": [1, 2, 1, 2], "B": [True, False, False, True],
    ...                    "C": [3, 4, 3, 4], "D": ["a", "a", "b", "a"]})
    
    
    
    >>> df.groupby("A").sum().sort_index()
       B  C   D
    A
    1  1  6  ab
    2  1  8  aa
    
    
    
    >>> df.groupby("D").sum().sort_index()
       A  B   C
    D
    a  5  2  11
    b  1  0   3
    
    
    
    >>> df.groupby("D").sum(min_count=3).sort_index()
         A    B     C
    D
    a  5.0  2.0  11.0
    b  NaN  NaN   NaN
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.sum.rst.txt)


---

## 🔹 022. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nunique.html

# pyspark.pandas.groupby.GroupBy.nunique#

GroupBy.nunique(_dropna =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.nunique)#
    

Return DataFrame with number of distinct observations per group for each column.

Parameters
    

**dropna** boolean, default True
    

Donât include NaN in the counts.

Returns
    

**nunique** DataFrame or Series
    

Examples
    
    
    >>> df = ps.DataFrame({'id': ['spam', 'egg', 'egg', 'spam',
    ...                           'ham', 'ham'],
    ...                    'value1': [1, 5, 5, 2, 5, 5],
    ...                    'value2': list('abbaxy')}, columns=['id', 'value1', 'value2'])
    >>> df
         id  value1 value2
    0  spam       1      a
    1   egg       5      b
    2   egg       5      b
    3  spam       2      a
    4   ham       5      x
    5   ham       5      y
    
    
    
    >>> df.groupby('id').nunique().sort_index() 
          value1  value2
    id
    egg        1       1
    ham        1       2
    spam       2       1
    
    
    
    >>> df.groupby('id')['value1'].nunique().sort_index() 
    id
    egg     1
    ham     1
    spam    2
    Name: value1, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.nunique.rst.txt)


---

## 🔹 023. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.quantile.html

# pyspark.pandas.groupby.GroupBy.quantile#

GroupBy.quantile(_q =0.5_, _accuracy =10000_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.quantile)#
    

Return group values at the given quantile.

New in version 3.4.0.

Parameters
    

**q** float, default 0.5 (50% quantile)
    

Value between 0 and 1 providing the quantile to compute.

**accuracy** int, optional
    

Default accuracy of approximation. Larger value means better accuracy. The relative error can be deduced by 1.0 / accuracy. This is a panda-on-Spark specific parameter.

Returns
    

pyspark.pandas.Series or pyspark.pandas.DataFrame
    

Return type determined by caller of GroupBy object.

See also

[`pyspark.pandas.Series.quantile`](pyspark.pandas.Series.quantile.html#pyspark.pandas.Series.quantile "pyspark.pandas.Series.quantile")
    
[`pyspark.pandas.DataFrame.quantile`](pyspark.pandas.DataFrame.quantile.html#pyspark.pandas.DataFrame.quantile "pyspark.pandas.DataFrame.quantile")
    
[`pyspark.sql.functions.percentile_approx`](../../pyspark.sql/api/pyspark.sql.functions.percentile_approx.html#pyspark.sql.functions.percentile_approx "pyspark.sql.functions.percentile_approx")
    

Notes

quantile in pandas-on-Spark are using distributed percentile approximation algorithm unlike pandas, the result might be different with pandas, also interpolation parameter is not supported yet.

Examples
    
    
    >>> df = ps.DataFrame([
    ...     ['a', 1], ['a', 2], ['a', 3],
    ...     ['b', 1], ['b', 3], ['b', 5]
    ... ], columns=['key', 'val'])
    

Groupby one column and return the quantile of the remaining columns in each group.
    
    
    >>> df.groupby('key').quantile()
         val
    key
    a    2.0
    b    3.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.quantile.rst.txt)


---

## 🔹 024. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.size.html

# pyspark.pandas.groupby.GroupBy.size#

GroupBy.size()[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.size)#
    

Compute group sizes.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({'A': [1, 2, 2, 3, 3, 3],
    ...                    'B': [1, 1, 2, 3, 3, 3]},
    ...                   columns=['A', 'B'])
    >>> df
       A  B
    0  1  1
    1  2  1
    2  2  2
    3  3  3
    4  3  3
    5  3  3
    
    
    
    >>> df.groupby('A').size().sort_index()
    A
    1    1
    2    2
    3    3
    dtype: int64
    
    
    
    >>> df.groupby(['A', 'B']).size().sort_index()
    A  B
    1  1    1
    2  1    1
       2    1
    3  3    3
    dtype: int64
    

For Series,
    
    
    >>> df.B.groupby(df.A).size().sort_index()
    A
    1    1
    2    2
    3    3
    Name: B, dtype: int64
    
    
    
    >>> df.groupby(df.A).B.size().sort_index()
    A
    1    1
    2    2
    3    3
    Name: B, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.size.rst.txt)


---

## 🔹 025. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.diff.html

# pyspark.pandas.groupby.GroupBy.diff#

GroupBy.diff(_periods =1_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.diff)#
    

First discrete difference of element.

Calculates the difference of a DataFrame element compared with another element in the DataFrame group (default is the element in the same column of the previous row).

Parameters
    

**periods** int, default 1
    

Periods to shift for calculating difference, accepts negative values.

Returns
    

**diffed** DataFrame or Series
    

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
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
    
    
    
    >>> df.groupby(['b']).diff().sort_index()
         a    c
    0  NaN  NaN
    1  1.0  3.0
    2  NaN  NaN
    3  NaN  NaN
    4  NaN  NaN
    5  NaN  NaN
    

Difference with previous column in a group.
    
    
    >>> df.groupby(['b'])['a'].diff().sort_index()
    0    NaN
    1    1.0
    2    NaN
    3    NaN
    4    NaN
    5    NaN
    Name: a, dtype: float64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.diff.rst.txt)


---

## 🔹 026. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.idxmax.html

# pyspark.pandas.groupby.GroupBy.idxmax#

GroupBy.idxmax(_skipna =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.idxmax)#
    

Return index of first occurrence of maximum over requested axis in group. NA/null values are excluded.

Parameters
    

**skipna** boolean, default True
    

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

See also

`Series.idxmax`
    
`DataFrame.idxmax`
    
[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 2, 2, 3],
    ...                    'b': [1, 2, 3, 4, 5],
    ...                    'c': [5, 4, 3, 2, 1]}, columns=['a', 'b', 'c'])
    
    
    
    >>> df.groupby(['a'])['b'].idxmax().sort_index() 
    a
    1  1
    2  3
    3  4
    Name: b, dtype: int64
    
    
    
    >>> df.groupby(['a']).idxmax().sort_index() 
       b  c
    a
    1  1  0
    2  3  2
    3  4  4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.idxmax.rst.txt)


---

## 🔹 027. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.idxmin.html

# pyspark.pandas.groupby.GroupBy.idxmin#

GroupBy.idxmin(_skipna =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.idxmin)#
    

Return index of first occurrence of minimum over requested axis in group. NA/null values are excluded.

Parameters
    

**skipna** boolean, default True
    

Exclude NA/null values. If an entire row/column is NA, the result will be NA.

See also

`Series.idxmin`
    
`DataFrame.idxmin`
    
[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 2, 2, 3],
    ...                    'b': [1, 2, 3, 4, 5],
    ...                    'c': [5, 4, 3, 2, 1]}, columns=['a', 'b', 'c'])
    
    
    
    >>> df.groupby(['a'])['b'].idxmin().sort_index() 
    a
    1    0
    2    2
    3    4
    Name: b, dtype: int64
    
    
    
    >>> df.groupby(['a']).idxmin().sort_index() 
       b  c
    a
    1  0  1
    2  2  3
    3  4  4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.idxmin.rst.txt)


---

## 🔹 028. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.fillna.html

# pyspark.pandas.groupby.GroupBy.fillna#

GroupBy.fillna(_value =None_, _method =None_, _axis =None_, _inplace =False_, _limit =None_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.fillna)#
    

Fill NA/NaN values in group.

Parameters
    

**value** scalar, dict, Series
    

Value to use to fill holes. alternately a dict/Series of values specifying which value to use for each column. DataFrame is not supported.

**method**{âbackfillâ, âbfillâ, âpadâ, âffillâ, None}, default None
    

Method to use for filling holes in reindexed Series pad / ffill: propagate last valid observation forward to next valid backfill / bfill: use NEXT valid observation to fill gap

Deprecated since version 4.0.0.

**axis**{0 or index}
    

1 and columns are not supported.

Deprecated since version 4.0.0: For axis=1, operate on the underlying object instead. Otherwise the axis keyword is not necessary.

**inplace** boolean, default False
    

Fill in place (do not create a new object)

**limit** int, default None
    

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Deprecated since version 4.0.0.

Returns
    

DataFrame
    

DataFrame with NA entries filled.

Examples
    
    
    >>> df = ps.DataFrame({
    ...     'A': [1, 1, 2, 2],
    ...     'B': [2, 4, None, 3],
    ...     'C': [None, None, None, 1],
    ...     'D': [0, 1, 5, 4]
    ...     },
    ...     columns=['A', 'B', 'C', 'D'])
    >>> df
       A    B    C  D
    0  1  2.0  NaN  0
    1  1  4.0  NaN  1
    2  2  NaN  NaN  5
    3  2  3.0  1.0  4
    

We can also propagate non-null values forward or backward in group.
    
    
    >>> df.groupby(['A'])['B'].fillna(method='ffill').sort_index()
    0    2.0
    1    4.0
    2    NaN
    3    3.0
    Name: B, dtype: float64
    
    
    
    >>> df.groupby(['A']).fillna(method='bfill').sort_index()
         B    C  D
    0  2.0  NaN  0
    1  4.0  NaN  1
    2  3.0  1.0  5
    3  3.0  1.0  4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.fillna.rst.txt)


---

## 🔹 029. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.bfill.html

# pyspark.pandas.groupby.GroupBy.bfill#

GroupBy.bfill(_limit =None_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.bfill)#
    

Synonym for DataFrame.fillna() with `method=`bfill``.

Parameters
    

**axis**{0 or index}
    

1 and columns are not supported.

**inplace** boolean, default False
    

Fill in place (do not create a new object)

**limit** int, default None
    

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Returns
    

DataFrame
    

DataFrame with NA entries filled.

Examples
    
    
    >>> df = ps.DataFrame({
    ...     'A': [1, 1, 2, 2],
    ...     'B': [2, 4, None, 3],
    ...     'C': [None, None, None, 1],
    ...     'D': [0, 1, 5, 4]
    ...     },
    ...     columns=['A', 'B', 'C', 'D'])
    >>> df
       A    B    C  D
    0  1  2.0  NaN  0
    1  1  4.0  NaN  1
    2  2  NaN  NaN  5
    3  2  3.0  1.0  4
    

Propagate non-null values backward.
    
    
    >>> df.groupby(['A']).bfill().sort_index()
         B    C  D
    0  2.0  NaN  0
    1  4.0  NaN  1
    2  3.0  1.0  5
    3  3.0  1.0  4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.bfill.rst.txt)


---

## 🔹 030. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.ffill.html

# pyspark.pandas.groupby.GroupBy.ffill#

GroupBy.ffill(_limit =None_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.ffill)#
    

Synonym for DataFrame.fillna() with `method=`ffill``.

Parameters
    

**axis**{0 or index}
    

1 and columns are not supported.

**inplace** boolean, default False
    

Fill in place (do not create a new object)

**limit** int, default None
    

If method is specified, this is the maximum number of consecutive NaN values to forward/backward fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled. If method is not specified, this is the maximum number of entries along the entire axis where NaNs will be filled. Must be greater than 0 if not None

Returns
    

DataFrame
    

DataFrame with NA entries filled.

Examples
    
    
    >>> df = ps.DataFrame({
    ...     'A': [1, 1, 2, 2],
    ...     'B': [2, 4, None, 3],
    ...     'C': [None, None, None, 1],
    ...     'D': [0, 1, 5, 4]
    ...     },
    ...     columns=['A', 'B', 'C', 'D'])
    >>> df
       A    B    C  D
    0  1  2.0  NaN  0
    1  1  4.0  NaN  1
    2  2  NaN  NaN  5
    3  2  3.0  1.0  4
    

Propagate non-null values forward.
    
    
    >>> df.groupby(['A']).ffill().sort_index()
         B    C  D
    0  2.0  NaN  0
    1  4.0  NaN  1
    2  NaN  NaN  5
    3  3.0  1.0  4
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.ffill.rst.txt)


---

## 🔹 031. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.head.html

# pyspark.pandas.groupby.GroupBy.head#

GroupBy.head(_n =5_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.head)#
    

Return first n rows of each group.

Returns
    

DataFrame or Series
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...                    'b': [2, 3, 1, 4, 6, 9, 8, 10, 7, 5],
    ...                    'c': [3, 5, 2, 5, 1, 2, 6, 4, 3, 6]},
    ...                   columns=['a', 'b', 'c'],
    ...                   index=[7, 2, 4, 1, 3, 4, 9, 10, 5, 6])
    >>> df
        a   b  c
    7   1   2  3
    2   1   3  5
    4   1   1  2
    1   1   4  5
    3   2   6  1
    4   2   9  2
    9   2   8  6
    10  3  10  4
    5   3   7  3
    6   3   5  6
    
    
    
    >>> df.groupby('a').head(2).sort_index()
        a   b  c
    2   1   3  5
    3   2   6  1
    4   2   9  2
    5   3   7  3
    7   1   2  3
    10  3  10  4
    
    
    
    >>> df.groupby('a')['b'].head(2).sort_index()
    2      3
    3      6
    4      9
    5      7
    7      2
    10    10
    Name: b, dtype: int64
    

Supports Groupby positional indexing Since pandas on Spark 3.4 (with pandas 1.4+):
    
    
    >>> df = ps.DataFrame([["g", "g0"],
    ...                   ["g", "g1"],
    ...                   ["g", "g2"],
    ...                   ["g", "g3"],
    ...                   ["h", "h0"],
    ...                   ["h", "h1"]], columns=["A", "B"])
    >>> df.groupby("A").head(-1) 
       A   B
    0  g  g0
    1  g  g1
    2  g  g2
    4  h  h0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.head.rst.txt)


---

## 🔹 032. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.shift.html

# pyspark.pandas.groupby.GroupBy.shift#

GroupBy.shift(_periods =1_, _fill_value =None_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.shift)#
    

Shift each group by periods observations.

Parameters
    

**periods** integer, default 1
    

number of periods to shift

**fill_value** optional
    
Returns
    

Series or DataFrame
    

Object shifted within each group.

Examples
    
    
    >>> df = ps.DataFrame({
    ...     'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...     'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
    >>> df
       a  b
    0  1  1
    1  1  2
    2  1  2
    3  2  2
    4  2  3
    5  2  3
    6  3  3
    7  3  4
    8  3  4
    
    
    
    >>> df.groupby('a').shift().sort_index()  
         b
    0  NaN
    1  1.0
    2  2.0
    3  NaN
    4  2.0
    5  3.0
    6  NaN
    7  3.0
    8  4.0
    
    
    
    >>> df.groupby('a').shift(periods=-1, fill_value=0).sort_index()  
       b
    0  2
    1  2
    2  0
    3  3
    4  3
    5  0
    6  4
    7  4
    8  0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.shift.rst.txt)


---

## 🔹 033. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.tail.html

# pyspark.pandas.groupby.GroupBy.tail#

GroupBy.tail(_n =5_)[[source]](../../../_modules/pyspark/pandas/groupby.html#GroupBy.tail)#
    

Return last n rows of each group.

Similar to .apply(lambda x: x.tail(n)), but it returns a subset of rows from the original DataFrame with original index and order preserved (as_index flag is ignored).

Does not work for negative values of n.

Returns
    

DataFrame or Series
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...                    'b': [2, 3, 1, 4, 6, 9, 8, 10, 7, 5],
    ...                    'c': [3, 5, 2, 5, 1, 2, 6, 4, 3, 6]},
    ...                   columns=['a', 'b', 'c'],
    ...                   index=[7, 2, 3, 1, 3, 4, 9, 10, 5, 6])
    >>> df
        a   b  c
    7   1   2  3
    2   1   3  5
    3   1   1  2
    1   1   4  5
    3   2   6  1
    4   2   9  2
    9   2   8  6
    10  3  10  4
    5   3   7  3
    6   3   5  6
    
    
    
    >>> df.groupby('a').tail(2).sort_index()
       a  b  c
    1  1  4  5
    3  1  1  2
    4  2  9  2
    5  3  7  3
    6  3  5  6
    9  2  8  6
    
    
    
    >>> df.groupby('a')['b'].tail(2).sort_index()
    1    4
    3    1
    4    9
    5    7
    6    5
    9    8
    Name: b, dtype: int64
    

Supports Groupby positional indexing Since pandas on Spark 3.4 (with pandas 1.4+):
    
    
    >>> df = ps.DataFrame([["g", "g0"],
    ...                   ["g", "g1"],
    ...                   ["g", "g2"],
    ...                   ["g", "g3"],
    ...                   ["h", "h0"],
    ...                   ["h", "h1"]], columns=["A", "B"])
    >>> df.groupby("A").tail(-1) 
       A   B
    3  g  g3
    2  g  g2
    1  g  g1
    5  h  h1
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.GroupBy.tail.rst.txt)


---

## 🔹 034. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.DataFrameGroupBy.describe.html

# pyspark.pandas.groupby.DataFrameGroupBy.describe#

DataFrameGroupBy.describe()[[source]](../../../_modules/pyspark/pandas/groupby.html#DataFrameGroupBy.describe)#
    

Generate descriptive statistics that summarize the central tendency, dispersion and shape of a datasetâs distribution, excluding `NaN` values.

Analyzes both numeric and object series, as well as `DataFrame` column sets of mixed data types. The output will vary depending on what is provided. Refer to the notes below for more detail.

Note

Unlike pandas, the percentiles in pandas-on-Spark are based upon approximate percentile computation because computing percentiles across a large dataset is extremely expensive.

Returns
    

DataFrame
    

Summary statistics of the DataFrame provided.

See also

`DataFrame.count`
    
`DataFrame.max`
    
`DataFrame.min`
    
`DataFrame.mean`
    
`DataFrame.std`
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]})
    >>> df
       a  b  c
    0  1  4  7
    1  1  5  8
    2  3  6  9
    

Describing a `DataFrame`. By default only numeric fields are returned.
    
    
    >>> described = df.groupby('a').describe()
    >>> described.sort_index()  
          b                                        c
      count mean       std min 25% 50% 75% max count mean       std min 25% 50% 75% max
    a
    1   2.0  4.5  0.707107 4.0 4.0 4.0 5.0 5.0   2.0  7.5  0.707107 7.0 7.0 7.0 8.0 8.0
    3   1.0  6.0       NaN 6.0 6.0 6.0 6.0 6.0   1.0  9.0       NaN 9.0 9.0 9.0 9.0 9.0
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.DataFrameGroupBy.describe.rst.txt)


---

## 🔹 035. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.nsmallest.html

# pyspark.pandas.groupby.SeriesGroupBy.nsmallest#

SeriesGroupBy.nsmallest(_n =5_)[[source]](../../../_modules/pyspark/pandas/groupby.html#SeriesGroupBy.nsmallest)#
    

Return the smallest n elements.

Parameters
    

**n** int
    

Number of items to retrieve.

See also

[`pyspark.pandas.Series.nsmallest`](pyspark.pandas.Series.nsmallest.html#pyspark.pandas.Series.nsmallest "pyspark.pandas.Series.nsmallest")
    
[`pyspark.pandas.DataFrame.nsmallest`](pyspark.pandas.DataFrame.nsmallest.html#pyspark.pandas.DataFrame.nsmallest "pyspark.pandas.DataFrame.nsmallest")
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...                    'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
    
    
    
    >>> df.groupby(['a'])['b'].nsmallest(1).sort_index()  
    a
    1  0    1
    2  3    2
    3  6    3
    Name: b, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.nsmallest.rst.txt)


---

## 🔹 036. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.nlargest.html

# pyspark.pandas.groupby.SeriesGroupBy.nlargest#

SeriesGroupBy.nlargest(_n =5_)[[source]](../../../_modules/pyspark/pandas/groupby.html#SeriesGroupBy.nlargest)#
    

Return the first n rows ordered by columns in descending order in group.

Return the first n rows with the smallest values in columns, in descending order. The columns that are not specified are returned as well, but not used for ordering.

Parameters
    

**n** int
    

Number of items to retrieve.

See also

[`pyspark.pandas.Series.nlargest`](pyspark.pandas.Series.nlargest.html#pyspark.pandas.Series.nlargest "pyspark.pandas.Series.nlargest")
    
[`pyspark.pandas.DataFrame.nlargest`](pyspark.pandas.DataFrame.nlargest.html#pyspark.pandas.DataFrame.nlargest "pyspark.pandas.DataFrame.nlargest")
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...                    'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
    
    
    
    >>> df.groupby(['a'])['b'].nlargest(1).sort_index()  
    a
    1  1    2
    2  4    3
    3  7    4
    Name: b, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.nlargest.rst.txt)


---

## 🔹 037. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.value_counts.html

# pyspark.pandas.groupby.SeriesGroupBy.value_counts#

SeriesGroupBy.value_counts(_sort =None_, _ascending =None_, _dropna =True_)[[source]](../../../_modules/pyspark/pandas/groupby.html#SeriesGroupBy.value_counts)#
    

Compute group sizes.

Parameters
    

**sort** boolean, default None
    

Sort by frequencies.

**ascending** boolean, default False
    

Sort in ascending order.

**dropna** boolean, default True
    

Donât include counts of NaN.

See also

[`pyspark.pandas.Series.groupby`](pyspark.pandas.Series.groupby.html#pyspark.pandas.Series.groupby "pyspark.pandas.Series.groupby")
    
[`pyspark.pandas.DataFrame.groupby`](pyspark.pandas.DataFrame.groupby.html#pyspark.pandas.DataFrame.groupby "pyspark.pandas.DataFrame.groupby")
    

Examples
    
    
    >>> df = ps.DataFrame({'A': [1, 2, 2, 3, 3, 3],
    ...                    'B': [1, 1, 2, 3, 3, np.nan]},
    ...                   columns=['A', 'B'])
    >>> df
       A    B
    0  1  1.0
    1  2  1.0
    2  2  2.0
    3  3  3.0
    4  3  3.0
    5  3  NaN
    
    
    
    >>> df.groupby('A')['B'].value_counts().sort_index()  
    A  B
    1  1.0    1
    2  1.0    1
       2.0    1
    3  3.0    2
    Name: count, dtype: int64
    

Donât include counts of NaN when dropna is False.
    
    
    >>> df.groupby('A')['B'].value_counts(
    ...   dropna=False).sort_index()  
    A  B
    1  1.0    1
    2  1.0    1
       2.0    1
    3  3.0    2
       NaN    1
    Name: count, dtype: int64
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.value_counts.rst.txt)


---

## 🔹 038. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.unique.html

# pyspark.pandas.groupby.SeriesGroupBy.unique#

SeriesGroupBy.unique()[[source]](../../../_modules/pyspark/pandas/groupby.html#SeriesGroupBy.unique)#
    

Return unique values in group.

Unique is returned in order of unknown. It does NOT sort.

See also

[`pyspark.pandas.Series.unique`](pyspark.pandas.Series.unique.html#pyspark.pandas.Series.unique "pyspark.pandas.Series.unique")
    
[`pyspark.pandas.Index.unique`](pyspark.pandas.Index.unique.html#pyspark.pandas.Index.unique "pyspark.pandas.Index.unique")
    

Examples
    
    
    >>> df = ps.DataFrame({'a': [1, 1, 1, 2, 2, 2, 3, 3, 3],
    ...                    'b': [1, 2, 2, 2, 3, 3, 3, 4, 4]}, columns=['a', 'b'])
    
    
    
    >>> df.groupby(['a'])['b'].unique().sort_index()  
    a
    1    [1, 2]
    2    [2, 3]
    3    [3, 4]
    Name: b, dtype: object
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.groupby.SeriesGroupBy.unique.rst.txt)
