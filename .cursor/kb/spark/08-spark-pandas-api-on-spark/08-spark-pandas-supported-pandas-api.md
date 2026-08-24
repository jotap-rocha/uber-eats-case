# Supported pandas API — PySpark 4.0.1 documentation
The following table shows the pandas APIs that implemented or non-implemented from pandas API on Spark. Some pandas API do not implement full parameters, so the third column shows missing parameters for each API.

*   ‘Y’ in the second column means it’s implemented including its whole parameter.
    
*   ‘N’ means it’s not implemented yet.
    
*   ‘P’ means it’s partially implemented with the missing of some parameters.
    

All API in the list below computes the data with distributed execution except the ones that require the local execution by design. For example, [DataFrame.to\_numpy()](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.DataFrame.to_numpy.html) requires to collect the data to the driver side.

If there is non-implemented pandas API or parameter you want, you can create an [Apache Spark JIRA](https://issues.apache.org/jira/projects/SPARK/summary) to request or to contribute by your own.

The API list is updated based on the [latest pandas official API reference](https://pandas.pydata.org/docs/reference/index.html#).

CategoricalIndex API[#](#categoricalindex-api "Permalink to this headline")
---------------------------------------------------------------------------


|API                       |Implemented|Missing parameters            |
|--------------------------|-----------|------------------------------|
|add_categories()          |Y          |                              |
|all()                     |Y          |                              |
|any()                     |Y          |                              |
|append()                  |Y          |                              |
|argmax()                  |P          |axis , skipna                 |
|argmin()                  |P          |axis , skipna                 |
|argsort                   |N          |                              |
|as_ordered()              |Y          |                              |
|as_unordered()            |Y          |                              |
|asof()                    |Y          |                              |
|asof_locs                 |N          |                              |
|astype()                  |P          |copy                          |
|copy()                    |Y          |                              |
|delete()                  |Y          |                              |
|diff                      |N          |                              |
|difference()              |Y          |                              |
|drop()                    |P          |errors                        |
|drop_duplicates()         |Y          |                              |
|droplevel()               |Y          |                              |
|dropna()                  |Y          |                              |
|duplicated                |N          |                              |
|equals()                  |Y          |                              |
|factorize()               |Y          |                              |
|fillna()                  |P          |downcast                      |
|format                    |N          |                              |
|get_indexer               |N          |                              |
|get_indexer_for           |N          |                              |
|get_indexer_non_unique    |N          |                              |
|get_level_values()        |Y          |                              |
|get_loc                   |N          |                              |
|get_slice_bound           |N          |                              |
|groupby                   |N          |                              |
|holds_integer()           |Y          |                              |
|identical()               |Y          |                              |
|infer_objects             |N          |                              |
|insert()                  |Y          |                              |
|intersection()            |P          |sort                          |
|is_                       |N          |                              |
|is_boolean()              |Y          |                              |
|is_categorical()          |Y          |                              |
|is_floating()             |Y          |                              |
|is_integer()              |Y          |                              |
|is_interval()             |Y          |                              |
|is_numeric()              |Y          |                              |
|is_object()               |Y          |                              |
|isin()                    |P          |level                         |
|isna()                    |Y          |                              |
|isnull()                  |Y          |                              |
|item()                    |Y          |                              |
|join                      |N          |                              |
|map()                     |P          |na_action                     |
|max()                     |Y          |                              |
|memory_usage              |N          |                              |
|min()                     |Y          |                              |
|notna()                   |Y          |                              |
|notnull()                 |Y          |                              |
|nunique()                 |Y          |                              |
|putmask                   |N          |                              |
|ravel                     |N          |                              |
|reindex                   |N          |                              |
|remove_categories()       |Y          |                              |
|remove_unused_categories()|Y          |                              |
|rename()                  |Y          |                              |
|rename_categories()       |Y          |                              |
|reorder_categories()      |Y          |                              |
|repeat()                  |P          |axis                          |
|round                     |N          |                              |
|searchsorted              |N          |                              |
|set_categories()          |Y          |                              |
|set_names()               |Y          |                              |
|shift()                   |P          |freq                          |
|slice_indexer             |N          |                              |
|slice_locs                |N          |                              |
|sort()                    |Y          |                              |
|sort_values()             |P          |key , na_position             |
|sortlevel                 |N          |                              |
|symmetric_difference()    |Y          |                              |
|take()                    |P          |allow_fill , axis , fill_value|
|to_flat_index             |N          |                              |
|to_frame()                |Y          |                              |
|to_list()                 |Y          |                              |
|to_numpy()                |P          |na_value                      |
|to_series()               |P          |index                         |
|tolist()                  |Y          |                              |
|transpose()               |Y          |                              |
|union()                   |Y          |                              |
|unique()                  |Y          |                              |
|value_counts()            |Y          |                              |
|view()                    |Y          |                              |
|where                     |N          |                              |


DataFrame API[#](#dataframe-api "Permalink to this headline")
-------------------------------------------------------------



* API: abs()
  * Implemented: Y
  * Missing parameters: 
* API: add()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: add_prefix()
  * Implemented: P
  * Missing parameters: axis
* API: add_suffix()
  * Implemented: P
  * Missing parameters: axis
* API: agg()
  * Implemented: P
  * Missing parameters: axis
* API: aggregate()
  * Implemented: P
  * Missing parameters: axis
* API: align()
  * Implemented: P
  * Missing parameters: broadcast_axis , fill_axis , fill_value , level , limit and more. See the pandas.DataFrame.align and pyspark.pandas.DataFrame.align for detail.
* API: all()
  * Implemented: Y
  * Missing parameters: 
* API: any()
  * Implemented: P
  * Missing parameters: skipna
* API: apply()
  * Implemented: P
  * Missing parameters: by_row , engine , engine_kwargs , raw , result_type
* API: applymap()
  * Implemented: P
  * Missing parameters: na_action
* API: asfreq
  * Implemented: N
  * Missing parameters: 
* API: asof
  * Implemented: N
  * Missing parameters: 
* API: assign()
  * Implemented: Y
  * Missing parameters: 
* API: astype()
  * Implemented: P
  * Missing parameters: copy , errors
* API: at_time()
  * Implemented: Y
  * Missing parameters: 
* API: backfill()
  * Implemented: P
  * Missing parameters: downcast
* API: between_time()
  * Implemented: Y
  * Missing parameters: 
* API: bfill()
  * Implemented: P
  * Missing parameters: downcast , limit_area
* API: bool()
  * Implemented: Y
  * Missing parameters: 
* API: boxplot()
  * Implemented: P
  * Missing parameters: ax , backend , by , column , figsize and more. See the pandas.DataFrame.boxplot and pyspark.pandas.DataFrame.boxplot for detail.
* API: clip()
  * Implemented: P
  * Missing parameters: axis , inplace
* API: combine
  * Implemented: N
  * Missing parameters: 
* API: combine_first()
  * Implemented: Y
  * Missing parameters: 
* API: compare
  * Implemented: N
  * Missing parameters: 
* API: convert_dtypes
  * Implemented: N
  * Missing parameters: 
* API: copy()
  * Implemented: Y
  * Missing parameters: 
* API: corr()
  * Implemented: P
  * Missing parameters: numeric_only
* API: corrwith()
  * Implemented: P
  * Missing parameters: numeric_only
* API: count()
  * Implemented: Y
  * Missing parameters: 
* API: cov()
  * Implemented: P
  * Missing parameters: numeric_only
* API: cummax()
  * Implemented: P
  * Missing parameters: axis
* API: cummin()
  * Implemented: P
  * Missing parameters: axis
* API: cumprod()
  * Implemented: P
  * Missing parameters: axis
* API: cumsum()
  * Implemented: P
  * Missing parameters: axis
* API: describe()
  * Implemented: P
  * Missing parameters: exclude , include
* API: diff()
  * Implemented: Y
  * Missing parameters: 
* API: div()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: divide()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: dot()
  * Implemented: Y
  * Missing parameters: 
* API: drop()
  * Implemented: P
  * Missing parameters: errors , inplace , level
* API: drop_duplicates()
  * Implemented: Y
  * Missing parameters: 
* API: droplevel()
  * Implemented: Y
  * Missing parameters: 
* API: dropna()
  * Implemented: P
  * Missing parameters: ignore_index
* API: duplicated()
  * Implemented: Y
  * Missing parameters: 
* API: eq()
  * Implemented: P
  * Missing parameters: axis , level
* API: equals()
  * Implemented: Y
  * Missing parameters: 
* API: eval()
  * Implemented: Y
  * Missing parameters: 
* API: ewm()
  * Implemented: P
  * Missing parameters: adjust , axis , method , times
* API: expanding()
  * Implemented: P
  * Missing parameters: axis , method
* API: explode()
  * Implemented: Y
  * Missing parameters: 
* API: ffill()
  * Implemented: P
  * Missing parameters: downcast , limit_area
* API: fillna()
  * Implemented: P
  * Missing parameters: downcast
* API: filter()
  * Implemented: Y
  * Missing parameters: 
* API: first()
  * Implemented: Y
  * Missing parameters: 
* API: first_valid_index()
  * Implemented: Y
  * Missing parameters: 
* API: floordiv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: ge()
  * Implemented: P
  * Missing parameters: axis , level
* API: get()
  * Implemented: Y
  * Missing parameters: 
* API: groupby()
  * Implemented: P
  * Missing parameters: group_keys , level , observed , sort
* API: gt()
  * Implemented: P
  * Missing parameters: axis , level
* API: head()
  * Implemented: Y
  * Missing parameters: 
* API: hist()
  * Implemented: P
  * Missing parameters: ax , backend , by , column , data and more. See the pandas.DataFrame.hist and pyspark.pandas.DataFrame.hist for detail.
* API: idxmax()
  * Implemented: P
  * Missing parameters: numeric_only , skipna
* API: idxmin()
  * Implemented: P
  * Missing parameters: numeric_only , skipna
* API: infer_objects
  * Implemented: N
  * Missing parameters: 
* API: info()
  * Implemented: P
  * Missing parameters: memory_usage
* API: insert()
  * Implemented: Y
  * Missing parameters: 
* API: interpolate()
  * Implemented: P
  * Missing parameters: axis , downcast , inplace
* API: isetitem
  * Implemented: N
  * Missing parameters: 
* API: isin()
  * Implemented: Y
  * Missing parameters: 
* API: isna()
  * Implemented: Y
  * Missing parameters: 
* API: isnull()
  * Implemented: Y
  * Missing parameters: 
* API: items()
  * Implemented: Y
  * Missing parameters: 
* API: iterrows()
  * Implemented: Y
  * Missing parameters: 
* API: itertuples()
  * Implemented: Y
  * Missing parameters: 
* API: join()
  * Implemented: P
  * Missing parameters: other , sort , validate
* API: keys()
  * Implemented: Y
  * Missing parameters: 
* API: kurt()
  * Implemented: Y
  * Missing parameters: 
* API: kurtosis()
  * Implemented: Y
  * Missing parameters: 
* API: last()
  * Implemented: Y
  * Missing parameters: 
* API: last_valid_index()
  * Implemented: Y
  * Missing parameters: 
* API: le()
  * Implemented: P
  * Missing parameters: axis , level
* API: lt()
  * Implemented: P
  * Missing parameters: axis , level
* API: map()
  * Implemented: P
  * Missing parameters: na_action
* API: mask()
  * Implemented: P
  * Missing parameters: axis , inplace , level
* API: max()
  * Implemented: Y
  * Missing parameters: 
* API: mean()
  * Implemented: Y
  * Missing parameters: 
* API: median()
  * Implemented: Y
  * Missing parameters: 
* API: melt()
  * Implemented: P
  * Missing parameters: col_level , ignore_index
* API: memory_usage
  * Implemented: N
  * Missing parameters: 
* API: merge()
  * Implemented: P
  * Missing parameters: copy , indicator , sort , validate
* API: min()
  * Implemented: Y
  * Missing parameters: 
* API: mod()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: mode()
  * Implemented: Y
  * Missing parameters: 
* API: mul()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: multiply()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: ne()
  * Implemented: P
  * Missing parameters: axis , level
* API: nlargest()
  * Implemented: Y
  * Missing parameters: 
* API: notna()
  * Implemented: Y
  * Missing parameters: 
* API: notnull()
  * Implemented: Y
  * Missing parameters: 
* API: nsmallest()
  * Implemented: Y
  * Missing parameters: 
* API: nunique()
  * Implemented: Y
  * Missing parameters: 
* API: pad()
  * Implemented: P
  * Missing parameters: downcast
* API: pct_change()
  * Implemented: P
  * Missing parameters: fill_method , freq , limit
* API: pipe()
  * Implemented: Y
  * Missing parameters: 
* API: pivot()
  * Implemented: Y
  * Missing parameters: 
* API: pivot_table()
  * Implemented: P
  * Missing parameters: dropna , margins , margins_name , observed , sort
* API: pop()
  * Implemented: Y
  * Missing parameters: 
* API: pow()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: prod()
  * Implemented: Y
  * Missing parameters: 
* API: product()
  * Implemented: Y
  * Missing parameters: 
* API: quantile()
  * Implemented: P
  * Missing parameters: interpolation , method
* API: query()
  * Implemented: Y
  * Missing parameters: 
* API: radd()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rank()
  * Implemented: P
  * Missing parameters: axis , na_option , pct
* API: rdiv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: reindex()
  * Implemented: P
  * Missing parameters: level , limit , method , tolerance
* API: reindex_like()
  * Implemented: P
  * Missing parameters: limit , method , tolerance
* API: rename()
  * Implemented: P
  * Missing parameters: copy
* API: rename_axis()
  * Implemented: P
  * Missing parameters: copy
* API: reorder_levels
  * Implemented: N
  * Missing parameters: 
* API: replace()
  * Implemented: Y
  * Missing parameters: 
* API: resample()
  * Implemented: P
  * Missing parameters: axis , convention , group_keys , kind , level and more. See the pandas.DataFrame.resample and pyspark.pandas.DataFrame.resample for detail.
* API: reset_index()
  * Implemented: P
  * Missing parameters: allow_duplicates , names
* API: rfloordiv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rmod()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rmul()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rolling()
  * Implemented: P
  * Missing parameters: axis , center , closed , method , on and more. See the pandas.DataFrame.rolling and pyspark.pandas.DataFrame.rolling for detail.
* API: round()
  * Implemented: Y
  * Missing parameters: 
* API: rpow()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rsub()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rtruediv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: sample()
  * Implemented: P
  * Missing parameters: axis , weights
* API: select_dtypes()
  * Implemented: Y
  * Missing parameters: 
* API: sem()
  * Implemented: Y
  * Missing parameters: 
* API: set_axis
  * Implemented: N
  * Missing parameters: 
* API: set_flags
  * Implemented: N
  * Missing parameters: 
* API: set_index()
  * Implemented: P
  * Missing parameters: verify_integrity
* API: shift()
  * Implemented: P
  * Missing parameters: axis , freq , suffix
* API: skew()
  * Implemented: Y
  * Missing parameters: 
* API: sort_index()
  * Implemented: P
  * Missing parameters: key , sort_remaining
* API: sort_values()
  * Implemented: P
  * Missing parameters: axis , key , kind
* API: squeeze()
  * Implemented: Y
  * Missing parameters: 
* API: stack()
  * Implemented: P
  * Missing parameters: dropna , future_stack , level , sort
* API: std()
  * Implemented: Y
  * Missing parameters: 
* API: sub()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: subtract()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: sum()
  * Implemented: Y
  * Missing parameters: 
* API: swapaxes()
  * Implemented: P
  * Missing parameters: axis1 , axis2
* API: swaplevel()
  * Implemented: Y
  * Missing parameters: 
* API: tail()
  * Implemented: Y
  * Missing parameters: 
* API: take()
  * Implemented: Y
  * Missing parameters: 
* API: to_clipboard()
  * Implemented: Y
  * Missing parameters: 
* API: to_csv()
  * Implemented: P
  * Missing parameters: chunksize , compression , decimal , doublequote , encoding and more. See the pandas.DataFrame.to_csv and pyspark.pandas.DataFrame.to_csv for detail.
* API: to_dict()
  * Implemented: P
  * Missing parameters: index
* API: to_excel()
  * Implemented: P
  * Missing parameters: engine_kwargs , storage_options
* API: to_feather()
  * Implemented: Y
  * Missing parameters: 
* API: to_gbq
  * Implemented: N
  * Missing parameters: 
* API: to_hdf()
  * Implemented: Y
  * Missing parameters: 
* API: to_html()
  * Implemented: P
  * Missing parameters: encoding
* API: to_json()
  * Implemented: P
  * Missing parameters: date_format , date_unit , default_handler , double_precision , force_ascii and more. See the pandas.DataFrame.to_json and pyspark.pandas.DataFrame.to_json for detail.
* API: to_latex()
  * Implemented: P
  * Missing parameters: caption , label , position
* API: to_markdown()
  * Implemented: P
  * Missing parameters: index , storage_options
* API: to_numpy()
  * Implemented: P
  * Missing parameters: copy , dtype , na_value
* API: to_orc()
  * Implemented: P
  * Missing parameters: engine , engine_kwargs , index
* API: to_parquet()
  * Implemented: P
  * Missing parameters: engine , index , storage_options
* API: to_period
  * Implemented: N
  * Missing parameters: 
* API: to_pickle
  * Implemented: N
  * Missing parameters: 
* API: to_records()
  * Implemented: Y
  * Missing parameters: 
* API: to_sql
  * Implemented: N
  * Missing parameters: 
* API: to_stata()
  * Implemented: Y
  * Missing parameters: 
* API: to_string()
  * Implemented: P
  * Missing parameters: encoding , max_colwidth , min_rows
* API: to_timestamp
  * Implemented: N
  * Missing parameters: 
* API: to_xarray
  * Implemented: N
  * Missing parameters: 
* API: to_xml
  * Implemented: N
  * Missing parameters: 
* API: transform()
  * Implemented: Y
  * Missing parameters: 
* API: transpose()
  * Implemented: P
  * Missing parameters: copy
* API: truediv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: truncate()
  * Implemented: Y
  * Missing parameters: 
* API: tz_convert
  * Implemented: N
  * Missing parameters: 
* API: tz_localize
  * Implemented: N
  * Missing parameters: 
* API: unstack()
  * Implemented: P
  * Missing parameters: fill_value , level , sort
* API: update()
  * Implemented: P
  * Missing parameters: errors , filter_func
* API: value_counts
  * Implemented: N
  * Missing parameters: 
* API: var()
  * Implemented: P
  * Missing parameters: skipna
* API: where()
  * Implemented: P
  * Missing parameters: inplace , level
* API: xs()
  * Implemented: P
  * Missing parameters: drop_level


DatetimeIndex API[#](#datetimeindex-api "Permalink to this headline")
---------------------------------------------------------------------


|API                   |Implemented|Missing parameters            |
|----------------------|-----------|------------------------------|
|all()                 |Y          |                              |
|any()                 |Y          |                              |
|append()              |Y          |                              |
|argmax()              |P          |axis , skipna                 |
|argmin()              |P          |axis , skipna                 |
|argsort               |N          |                              |
|as_unit               |N          |                              |
|asof()                |Y          |                              |
|asof_locs             |N          |                              |
|astype()              |P          |copy                          |
|ceil()                |Y          |                              |
|copy()                |Y          |                              |
|day_name()            |Y          |                              |
|delete()              |Y          |                              |
|diff                  |N          |                              |
|difference()          |Y          |                              |
|drop()                |P          |errors                        |
|drop_duplicates()     |Y          |                              |
|droplevel()           |Y          |                              |
|dropna()              |Y          |                              |
|duplicated            |N          |                              |
|equals()              |Y          |                              |
|factorize()           |Y          |                              |
|fillna()              |P          |downcast                      |
|floor()               |Y          |                              |
|format                |N          |                              |
|get_indexer           |N          |                              |
|get_indexer_for       |N          |                              |
|get_indexer_non_unique|N          |                              |
|get_level_values()    |Y          |                              |
|get_loc               |N          |                              |
|get_slice_bound       |N          |                              |
|groupby               |N          |                              |
|holds_integer()       |Y          |                              |
|identical()           |Y          |                              |
|indexer_at_time()     |Y          |                              |
|indexer_between_time()|Y          |                              |
|infer_objects         |N          |                              |
|insert()              |Y          |                              |
|intersection()        |P          |sort                          |
|is_                   |N          |                              |
|is_boolean()          |Y          |                              |
|is_categorical()      |Y          |                              |
|is_floating()         |Y          |                              |
|is_integer()          |Y          |                              |
|is_interval()         |Y          |                              |
|is_numeric()          |Y          |                              |
|is_object()           |Y          |                              |
|isin()                |P          |level                         |
|isna()                |Y          |                              |
|isnull()              |Y          |                              |
|isocalendar()         |Y          |                              |
|item()                |Y          |                              |
|join                  |N          |                              |
|map()                 |Y          |                              |
|max()                 |P          |axis , skipna                 |
|mean                  |N          |                              |
|memory_usage          |N          |                              |
|min()                 |P          |axis , skipna                 |
|month_name()          |Y          |                              |
|normalize()           |Y          |                              |
|notna()               |Y          |                              |
|notnull()             |Y          |                              |
|nunique()             |Y          |                              |
|putmask               |N          |                              |
|ravel                 |N          |                              |
|reindex               |N          |                              |
|rename()              |Y          |                              |
|repeat()              |P          |axis                          |
|round()               |Y          |                              |
|searchsorted          |N          |                              |
|set_names()           |Y          |                              |
|shift()               |P          |freq                          |
|slice_indexer         |N          |                              |
|slice_locs            |N          |                              |
|snap                  |N          |                              |
|sort()                |Y          |                              |
|sort_values()         |P          |key , na_position             |
|sortlevel             |N          |                              |
|std                   |N          |                              |
|strftime()            |Y          |                              |
|symmetric_difference()|Y          |                              |
|take()                |P          |allow_fill , axis , fill_value|
|to_flat_index         |N          |                              |
|to_frame()            |Y          |                              |
|to_julian_date        |N          |                              |
|to_list()             |Y          |                              |
|to_numpy()            |P          |na_value                      |
|to_period             |N          |                              |
|to_pydatetime         |N          |                              |
|to_series()           |P          |index                         |
|tolist()              |Y          |                              |
|transpose()           |Y          |                              |
|tz_convert            |N          |                              |
|tz_localize           |N          |                              |
|union()               |Y          |                              |
|unique()              |Y          |                              |
|value_counts()        |Y          |                              |
|view()                |Y          |                              |
|where                 |N          |                              |


Index API[#](#index-api "Permalink to this headline")
-----------------------------------------------------


|API                   |Implemented|Missing parameters            |
|----------------------|-----------|------------------------------|
|all()                 |Y          |                              |
|any()                 |Y          |                              |
|append()              |Y          |                              |
|argmax()              |P          |axis , skipna                 |
|argmin()              |P          |axis , skipna                 |
|argsort               |N          |                              |
|asof()                |Y          |                              |
|asof_locs             |N          |                              |
|astype()              |P          |copy                          |
|copy()                |Y          |                              |
|delete()              |Y          |                              |
|diff                  |N          |                              |
|difference()          |Y          |                              |
|drop()                |P          |errors                        |
|drop_duplicates()     |Y          |                              |
|droplevel()           |Y          |                              |
|dropna()              |Y          |                              |
|duplicated            |N          |                              |
|equals()              |Y          |                              |
|factorize()           |Y          |                              |
|fillna()              |P          |downcast                      |
|format                |N          |                              |
|get_indexer           |N          |                              |
|get_indexer_for       |N          |                              |
|get_indexer_non_unique|N          |                              |
|get_level_values()    |Y          |                              |
|get_loc               |N          |                              |
|get_slice_bound       |N          |                              |
|groupby               |N          |                              |
|holds_integer()       |Y          |                              |
|identical()           |Y          |                              |
|infer_objects         |N          |                              |
|insert()              |Y          |                              |
|intersection()        |P          |sort                          |
|is_                   |N          |                              |
|is_boolean()          |Y          |                              |
|is_categorical()      |Y          |                              |
|is_floating()         |Y          |                              |
|is_integer()          |Y          |                              |
|is_interval()         |Y          |                              |
|is_numeric()          |Y          |                              |
|is_object()           |Y          |                              |
|isin()                |P          |level                         |
|isna()                |Y          |                              |
|isnull()              |Y          |                              |
|item()                |Y          |                              |
|join                  |N          |                              |
|map()                 |Y          |                              |
|max()                 |P          |axis , skipna                 |
|memory_usage          |N          |                              |
|min()                 |P          |axis , skipna                 |
|notna()               |Y          |                              |
|notnull()             |Y          |                              |
|nunique()             |Y          |                              |
|putmask               |N          |                              |
|ravel                 |N          |                              |
|reindex               |N          |                              |
|rename()              |Y          |                              |
|repeat()              |P          |axis                          |
|round                 |N          |                              |
|searchsorted          |N          |                              |
|set_names()           |Y          |                              |
|shift()               |P          |freq                          |
|slice_indexer         |N          |                              |
|slice_locs            |N          |                              |
|sort()                |Y          |                              |
|sort_values()         |P          |key , na_position             |
|sortlevel             |N          |                              |
|symmetric_difference()|Y          |                              |
|take()                |P          |allow_fill , axis , fill_value|
|to_flat_index         |N          |                              |
|to_frame()            |Y          |                              |
|to_list()             |Y          |                              |
|to_numpy()            |P          |na_value                      |
|to_series()           |P          |index                         |
|tolist()              |Y          |                              |
|transpose()           |Y          |                              |
|union()               |Y          |                              |
|unique()              |Y          |                              |
|value_counts()        |Y          |                              |
|view()                |Y          |                              |
|where                 |N          |                              |


MultiIndex API[#](#multiindex-api "Permalink to this headline")
---------------------------------------------------------------


|API                   |Implemented|Missing parameters            |
|----------------------|-----------|------------------------------|
|all()                 |Y          |                              |
|any()                 |Y          |                              |
|append()              |Y          |                              |
|argmax()              |P          |axis , skipna                 |
|argmin()              |P          |axis , skipna                 |
|argsort               |N          |                              |
|asof()                |Y          |                              |
|asof_locs             |N          |                              |
|astype()              |P          |copy                          |
|copy()                |P          |name , names                  |
|delete()              |Y          |                              |
|diff                  |N          |                              |
|difference()          |Y          |                              |
|drop()                |P          |errors                        |
|drop_duplicates()     |Y          |                              |
|droplevel()           |Y          |                              |
|dropna()              |Y          |                              |
|duplicated            |N          |                              |
|equal_levels()        |Y          |                              |
|equals()              |Y          |                              |
|factorize()           |P          |use_na_sentinel               |
|fillna()              |P          |downcast                      |
|format                |N          |                              |
|get_indexer           |N          |                              |
|get_indexer_for       |N          |                              |
|get_indexer_non_unique|N          |                              |
|get_level_values()    |Y          |                              |
|get_loc               |N          |                              |
|get_loc_level         |N          |                              |
|get_locs              |N          |                              |
|get_slice_bound       |N          |                              |
|groupby               |N          |                              |
|holds_integer()       |Y          |                              |
|identical()           |Y          |                              |
|infer_objects         |N          |                              |
|insert()              |Y          |                              |
|intersection()        |P          |sort                          |
|is_                   |N          |                              |
|is_boolean()          |Y          |                              |
|is_categorical()      |Y          |                              |
|is_floating()         |Y          |                              |
|is_integer()          |Y          |                              |
|is_interval()         |Y          |                              |
|is_numeric()          |Y          |                              |
|is_object()           |Y          |                              |
|isin()                |P          |level                         |
|isna()                |Y          |                              |
|isnull()              |Y          |                              |
|item()                |Y          |                              |
|join                  |N          |                              |
|map()                 |Y          |                              |
|max()                 |P          |axis , skipna                 |
|memory_usage          |N          |                              |
|min()                 |P          |axis , skipna                 |
|notna()               |Y          |                              |
|notnull()             |Y          |                              |
|nunique()             |Y          |                              |
|putmask               |N          |                              |
|ravel                 |N          |                              |
|reindex               |N          |                              |
|remove_unused_levels  |N          |                              |
|rename()              |P          |level , names                 |
|reorder_levels        |N          |                              |
|repeat()              |P          |axis                          |
|round                 |N          |                              |
|searchsorted          |N          |                              |
|set_codes             |N          |                              |
|set_levels            |N          |                              |
|set_names()           |Y          |                              |
|shift()               |P          |freq                          |
|slice_indexer         |N          |                              |
|slice_locs            |N          |                              |
|sort()                |Y          |                              |
|sort_values()         |P          |key , na_position             |
|sortlevel             |N          |                              |
|swaplevel()           |Y          |                              |
|symmetric_difference()|Y          |                              |
|take()                |P          |allow_fill , axis , fill_value|
|to_flat_index         |N          |                              |
|to_frame()            |P          |allow_duplicates              |
|to_list()             |Y          |                              |
|to_numpy()            |P          |na_value                      |
|to_series()           |P          |index                         |
|tolist()              |Y          |                              |
|transpose()           |Y          |                              |
|truncate              |N          |                              |
|union()               |Y          |                              |
|unique()              |Y          |                              |
|value_counts()        |Y          |                              |
|view()                |Y          |                              |
|where                 |N          |                              |


Series API[#](#series-api "Permalink to this headline")
-------------------------------------------------------



* API: abs()
  * Implemented: Y
  * Missing parameters: 
* API: add()
  * Implemented: P
  * Missing parameters: axis , level
* API: add_prefix()
  * Implemented: P
  * Missing parameters: axis
* API: add_suffix()
  * Implemented: P
  * Missing parameters: axis
* API: agg()
  * Implemented: P
  * Missing parameters: axis
* API: aggregate()
  * Implemented: P
  * Missing parameters: axis
* API: align()
  * Implemented: P
  * Missing parameters: broadcast_axis , fill_axis , fill_value , level , limit and more. See the pandas.Series.align and pyspark.pandas.Series.align for detail.
* API: all()
  * Implemented: P
  * Missing parameters: bool_only
* API: any()
  * Implemented: P
  * Missing parameters: bool_only , skipna
* API: apply()
  * Implemented: P
  * Missing parameters: by_row , convert_dtype
* API: argmax()
  * Implemented: Y
  * Missing parameters: 
* API: argmin()
  * Implemented: Y
  * Missing parameters: 
* API: argsort()
  * Implemented: P
  * Missing parameters: axis , kind , order , stable
* API: asfreq
  * Implemented: N
  * Missing parameters: 
* API: asof()
  * Implemented: P
  * Missing parameters: subset
* API: astype()
  * Implemented: P
  * Missing parameters: copy , errors
* API: at_time()
  * Implemented: Y
  * Missing parameters: 
* API: autocorr()
  * Implemented: Y
  * Missing parameters: 
* API: backfill()
  * Implemented: P
  * Missing parameters: downcast
* API: between()
  * Implemented: Y
  * Missing parameters: 
* API: between_time()
  * Implemented: Y
  * Missing parameters: 
* API: bfill()
  * Implemented: P
  * Missing parameters: downcast , limit_area
* API: bool()
  * Implemented: Y
  * Missing parameters: 
* API: case_when
  * Implemented: N
  * Missing parameters: 
* API: clip()
  * Implemented: P
  * Missing parameters: axis
* API: combine
  * Implemented: N
  * Missing parameters: 
* API: combine_first()
  * Implemented: Y
  * Missing parameters: 
* API: compare()
  * Implemented: P
  * Missing parameters: align_axis , result_names
* API: convert_dtypes
  * Implemented: N
  * Missing parameters: 
* API: copy()
  * Implemented: Y
  * Missing parameters: 
* API: corr()
  * Implemented: Y
  * Missing parameters: 
* API: count()
  * Implemented: Y
  * Missing parameters: 
* API: cov()
  * Implemented: Y
  * Missing parameters: 
* API: cummax()
  * Implemented: P
  * Missing parameters: axis
* API: cummin()
  * Implemented: P
  * Missing parameters: axis
* API: cumprod()
  * Implemented: P
  * Missing parameters: axis
* API: cumsum()
  * Implemented: P
  * Missing parameters: axis
* API: describe()
  * Implemented: P
  * Missing parameters: exclude , include
* API: diff()
  * Implemented: Y
  * Missing parameters: 
* API: div()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: divide()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: divmod()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: dot()
  * Implemented: Y
  * Missing parameters: 
* API: drop()
  * Implemented: P
  * Missing parameters: axis , errors
* API: drop_duplicates()
  * Implemented: P
  * Missing parameters: ignore_index
* API: droplevel()
  * Implemented: P
  * Missing parameters: axis
* API: dropna()
  * Implemented: P
  * Missing parameters: how , ignore_index
* API: duplicated()
  * Implemented: Y
  * Missing parameters: 
* API: eq()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: equals()
  * Implemented: Y
  * Missing parameters: 
* API: ewm()
  * Implemented: P
  * Missing parameters: adjust , axis , method , times
* API: expanding()
  * Implemented: P
  * Missing parameters: axis , method
* API: explode()
  * Implemented: P
  * Missing parameters: ignore_index
* API: factorize()
  * Implemented: Y
  * Missing parameters: 
* API: ffill()
  * Implemented: P
  * Missing parameters: downcast , limit_area
* API: fillna()
  * Implemented: P
  * Missing parameters: downcast
* API: filter()
  * Implemented: Y
  * Missing parameters: 
* API: first()
  * Implemented: Y
  * Missing parameters: 
* API: first_valid_index()
  * Implemented: Y
  * Missing parameters: 
* API: floordiv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: ge()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: get()
  * Implemented: Y
  * Missing parameters: 
* API: groupby()
  * Implemented: P
  * Missing parameters: group_keys , level , observed , sort
* API: gt()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: head()
  * Implemented: Y
  * Missing parameters: 
* API: hist()
  * Implemented: P
  * Missing parameters: ax , backend , by , figsize , grid and more. See the pandas.Series.hist and pyspark.pandas.Series.hist for detail.
* API: idxmax()
  * Implemented: P
  * Missing parameters: axis
* API: idxmin()
  * Implemented: P
  * Missing parameters: axis
* API: infer_objects
  * Implemented: N
  * Missing parameters: 
* API: info
  * Implemented: N
  * Missing parameters: 
* API: interpolate()
  * Implemented: P
  * Missing parameters: axis , downcast , inplace
* API: isin()
  * Implemented: Y
  * Missing parameters: 
* API: isna()
  * Implemented: Y
  * Missing parameters: 
* API: isnull()
  * Implemented: Y
  * Missing parameters: 
* API: item()
  * Implemented: Y
  * Missing parameters: 
* API: items()
  * Implemented: Y
  * Missing parameters: 
* API: keys()
  * Implemented: Y
  * Missing parameters: 
* API: kurt()
  * Implemented: Y
  * Missing parameters: 
* API: kurtosis()
  * Implemented: Y
  * Missing parameters: 
* API: last()
  * Implemented: Y
  * Missing parameters: 
* API: last_valid_index()
  * Implemented: Y
  * Missing parameters: 
* API: le()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: lt()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: map()
  * Implemented: Y
  * Missing parameters: 
* API: mask()
  * Implemented: P
  * Missing parameters: axis , inplace , level
* API: max()
  * Implemented: Y
  * Missing parameters: 
* API: mean()
  * Implemented: Y
  * Missing parameters: 
* API: median()
  * Implemented: Y
  * Missing parameters: 
* API: memory_usage
  * Implemented: N
  * Missing parameters: 
* API: min()
  * Implemented: Y
  * Missing parameters: 
* API: mod()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: mode()
  * Implemented: Y
  * Missing parameters: 
* API: mul()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: multiply()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: ne()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: nlargest()
  * Implemented: P
  * Missing parameters: keep
* API: notna()
  * Implemented: Y
  * Missing parameters: 
* API: notnull()
  * Implemented: Y
  * Missing parameters: 
* API: nsmallest()
  * Implemented: P
  * Missing parameters: keep
* API: nunique()
  * Implemented: Y
  * Missing parameters: 
* API: pad()
  * Implemented: P
  * Missing parameters: downcast
* API: pct_change()
  * Implemented: P
  * Missing parameters: fill_method , freq , limit
* API: pipe()
  * Implemented: Y
  * Missing parameters: 
* API: pop()
  * Implemented: Y
  * Missing parameters: 
* API: pow()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: prod()
  * Implemented: Y
  * Missing parameters: 
* API: product()
  * Implemented: Y
  * Missing parameters: 
* API: quantile()
  * Implemented: P
  * Missing parameters: interpolation
* API: radd()
  * Implemented: P
  * Missing parameters: axis , level
* API: rank()
  * Implemented: P
  * Missing parameters: axis , na_option , pct
* API: ravel
  * Implemented: N
  * Missing parameters: 
* API: rdiv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rdivmod()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: reindex()
  * Implemented: P
  * Missing parameters: axis , copy , level , limit , method and more. See the pandas.Series.reindex and pyspark.pandas.Series.reindex for detail.
* API: reindex_like()
  * Implemented: P
  * Missing parameters: copy , limit , method , tolerance
* API: rename()
  * Implemented: P
  * Missing parameters: axis , copy , errors , inplace , level
* API: rename_axis()
  * Implemented: P
  * Missing parameters: axis , copy
* API: reorder_levels
  * Implemented: N
  * Missing parameters: 
* API: repeat()
  * Implemented: P
  * Missing parameters: axis
* API: replace()
  * Implemented: P
  * Missing parameters: inplace , limit , method
* API: resample()
  * Implemented: P
  * Missing parameters: axis , convention , group_keys , kind , level and more. See the pandas.Series.resample and pyspark.pandas.Series.resample for detail.
* API: reset_index()
  * Implemented: P
  * Missing parameters: allow_duplicates
* API: rfloordiv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rmod()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rmul()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rolling()
  * Implemented: P
  * Missing parameters: axis , center , closed , method , on and more. See the pandas.Series.rolling and pyspark.pandas.Series.rolling for detail.
* API: round()
  * Implemented: Y
  * Missing parameters: 
* API: rpow()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rsub()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: rtruediv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: sample()
  * Implemented: P
  * Missing parameters: axis , weights
* API: searchsorted()
  * Implemented: P
  * Missing parameters: sorter
* API: sem()
  * Implemented: Y
  * Missing parameters: 
* API: set_axis
  * Implemented: N
  * Missing parameters: 
* API: set_flags
  * Implemented: N
  * Missing parameters: 
* API: shift()
  * Implemented: P
  * Missing parameters: axis , freq , suffix
* API: skew()
  * Implemented: Y
  * Missing parameters: 
* API: sort_index()
  * Implemented: P
  * Missing parameters: key , sort_remaining
* API: sort_values()
  * Implemented: P
  * Missing parameters: axis , key , kind
* API: squeeze()
  * Implemented: Y
  * Missing parameters: 
* API: std()
  * Implemented: Y
  * Missing parameters: 
* API: sub()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: subtract()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: sum()
  * Implemented: Y
  * Missing parameters: 
* API: swapaxes()
  * Implemented: P
  * Missing parameters: axis1 , axis2
* API: swaplevel()
  * Implemented: Y
  * Missing parameters: 
* API: tail()
  * Implemented: Y
  * Missing parameters: 
* API: take()
  * Implemented: P
  * Missing parameters: axis
* API: to_clipboard()
  * Implemented: Y
  * Missing parameters: 
* API: to_csv()
  * Implemented: P
  * Missing parameters: chunksize , compression , decimal , doublequote , encoding and more. See the pandas.Series.to_csv and pyspark.pandas.Series.to_csv for detail.
* API: to_dict()
  * Implemented: Y
  * Missing parameters: 
* API: to_excel()
  * Implemented: P
  * Missing parameters: engine_kwargs , storage_options
* API: to_frame()
  * Implemented: Y
  * Missing parameters: 
* API: to_hdf()
  * Implemented: Y
  * Missing parameters: 
* API: to_json()
  * Implemented: P
  * Missing parameters: date_format , date_unit , default_handler , double_precision , force_ascii and more. See the pandas.Series.to_json and pyspark.pandas.Series.to_json for detail.
* API: to_latex()
  * Implemented: P
  * Missing parameters: caption , label , position
* API: to_list()
  * Implemented: Y
  * Missing parameters: 
* API: to_markdown()
  * Implemented: P
  * Missing parameters: index , storage_options
* API: to_numpy()
  * Implemented: P
  * Missing parameters: copy , dtype , na_value
* API: to_period
  * Implemented: N
  * Missing parameters: 
* API: to_pickle
  * Implemented: N
  * Missing parameters: 
* API: to_sql
  * Implemented: N
  * Missing parameters: 
* API: to_string()
  * Implemented: P
  * Missing parameters: min_rows
* API: to_timestamp
  * Implemented: N
  * Missing parameters: 
* API: to_xarray
  * Implemented: N
  * Missing parameters: 
* API: tolist()
  * Implemented: Y
  * Missing parameters: 
* API: transform()
  * Implemented: Y
  * Missing parameters: 
* API: transpose()
  * Implemented: Y
  * Missing parameters: 
* API: truediv()
  * Implemented: P
  * Missing parameters: axis , fill_value , level
* API: truncate()
  * Implemented: Y
  * Missing parameters: 
* API: tz_convert
  * Implemented: N
  * Missing parameters: 
* API: tz_localize
  * Implemented: N
  * Missing parameters: 
* API: unique()
  * Implemented: Y
  * Missing parameters: 
* API: unstack()
  * Implemented: P
  * Missing parameters: fill_value , sort
* API: update()
  * Implemented: Y
  * Missing parameters: 
* API: value_counts()
  * Implemented: Y
  * Missing parameters: 
* API: var()
  * Implemented: P
  * Missing parameters: skipna
* API: view
  * Implemented: N
  * Missing parameters: 
* API: where()
  * Implemented: P
  * Missing parameters: axis , inplace , level
* API: xs()
  * Implemented: P
  * Missing parameters: axis , drop_level


TimedeltaIndex API[#](#timedeltaindex-api "Permalink to this headline")
-----------------------------------------------------------------------


|API                   |Implemented|Missing parameters            |
|----------------------|-----------|------------------------------|
|all()                 |Y          |                              |
|any()                 |Y          |                              |
|append()              |Y          |                              |
|argmax()              |P          |axis , skipna                 |
|argmin()              |P          |axis , skipna                 |
|argsort               |N          |                              |
|as_unit               |N          |                              |
|asof()                |Y          |                              |
|asof_locs             |N          |                              |
|astype()              |P          |copy                          |
|ceil                  |N          |                              |
|copy()                |Y          |                              |
|delete()              |Y          |                              |
|diff                  |N          |                              |
|difference()          |Y          |                              |
|drop()                |P          |errors                        |
|drop_duplicates()     |Y          |                              |
|droplevel()           |Y          |                              |
|dropna()              |Y          |                              |
|duplicated            |N          |                              |
|equals()              |Y          |                              |
|factorize()           |Y          |                              |
|fillna()              |P          |downcast                      |
|floor                 |N          |                              |
|format                |N          |                              |
|get_indexer           |N          |                              |
|get_indexer_for       |N          |                              |
|get_indexer_non_unique|N          |                              |
|get_level_values()    |Y          |                              |
|get_loc               |N          |                              |
|get_slice_bound       |N          |                              |
|groupby               |N          |                              |
|holds_integer()       |Y          |                              |
|identical()           |Y          |                              |
|infer_objects         |N          |                              |
|insert()              |Y          |                              |
|intersection()        |P          |sort                          |
|is_                   |N          |                              |
|is_boolean()          |Y          |                              |
|is_categorical()      |Y          |                              |
|is_floating()         |Y          |                              |
|is_integer()          |Y          |                              |
|is_interval()         |Y          |                              |
|is_numeric()          |Y          |                              |
|is_object()           |Y          |                              |
|isin()                |P          |level                         |
|isna()                |Y          |                              |
|isnull()              |Y          |                              |
|item()                |Y          |                              |
|join                  |N          |                              |
|map()                 |Y          |                              |
|max()                 |P          |axis , skipna                 |
|mean                  |N          |                              |
|median                |N          |                              |
|memory_usage          |N          |                              |
|min()                 |P          |axis , skipna                 |
|notna()               |Y          |                              |
|notnull()             |Y          |                              |
|nunique()             |Y          |                              |
|putmask               |N          |                              |
|ravel                 |N          |                              |
|reindex               |N          |                              |
|rename()              |Y          |                              |
|repeat()              |P          |axis                          |
|round                 |N          |                              |
|searchsorted          |N          |                              |
|set_names()           |Y          |                              |
|shift()               |P          |freq                          |
|slice_indexer         |N          |                              |
|slice_locs            |N          |                              |
|sort()                |Y          |                              |
|sort_values()         |P          |key , na_position             |
|sortlevel             |N          |                              |
|std                   |N          |                              |
|sum                   |N          |                              |
|symmetric_difference()|Y          |                              |
|take()                |P          |allow_fill , axis , fill_value|
|to_flat_index         |N          |                              |
|to_frame()            |Y          |                              |
|to_list()             |Y          |                              |
|to_numpy()            |P          |na_value                      |
|to_pytimedelta        |N          |                              |
|to_series()           |P          |index                         |
|tolist()              |Y          |                              |
|total_seconds         |N          |                              |
|transpose()           |Y          |                              |
|union()               |Y          |                              |
|unique()              |Y          |                              |
|value_counts()        |Y          |                              |
|view()                |Y          |                              |
|where                 |N          |                              |


General Function API[#](#general-function-api "Permalink to this headline")
---------------------------------------------------------------------------



* API: array
  * Implemented: N
  * Missing parameters: 
* API: bdate_range
  * Implemented: N
  * Missing parameters: 
* API: concat()
  * Implemented: P
  * Missing parameters: copy , keys , levels , names , verify_integrity
* API: crosstab
  * Implemented: N
  * Missing parameters: 
* API: cut
  * Implemented: N
  * Missing parameters: 
* API: date_range()
  * Implemented: P
  * Missing parameters: unit
* API: eval
  * Implemented: N
  * Missing parameters: 
* API: factorize
  * Implemented: N
  * Missing parameters: 
* API: from_dummies
  * Implemented: N
  * Missing parameters: 
* API: get_dummies()
  * Implemented: Y
  * Missing parameters: 
* API: infer_freq
  * Implemented: N
  * Missing parameters: 
* API: interval_range
  * Implemented: N
  * Missing parameters: 
* API: isna()
  * Implemented: Y
  * Missing parameters: 
* API: isnull()
  * Implemented: Y
  * Missing parameters: 
* API: json_normalize()
  * Implemented: P
  * Missing parameters: errors , max_level , meta , meta_prefix , record_path and more. See the pandas.json_normalize and pyspark.pandas.json_normalize for detail.
* API: lreshape
  * Implemented: N
  * Missing parameters: 
* API: melt()
  * Implemented: P
  * Missing parameters: col_level , ignore_index
* API: merge()
  * Implemented: P
  * Missing parameters: copy , indicator , left , sort , validate
* API: merge_asof()
  * Implemented: Y
  * Missing parameters: 
* API: merge_ordered
  * Implemented: N
  * Missing parameters: 
* API: notna()
  * Implemented: Y
  * Missing parameters: 
* API: notnull()
  * Implemented: Y
  * Missing parameters: 
* API: period_range
  * Implemented: N
  * Missing parameters: 
* API: pivot
  * Implemented: N
  * Missing parameters: 
* API: pivot_table
  * Implemented: N
  * Missing parameters: 
* API: qcut
  * Implemented: N
  * Missing parameters: 
* API: read_clipboard()
  * Implemented: P
  * Missing parameters: dtype_backend
* API: read_csv()
  * Implemented: P
  * Missing parameters: cache_dates , chunksize , compression , converters , date_format and more. See the pandas.read_csv and pyspark.pandas.read_csv for detail.
* API: read_excel()
  * Implemented: P
  * Missing parameters: date_format , decimal , dtype_backend , engine_kwargs , na_filter and more. See the pandas.read_excel and pyspark.pandas.read_excel for detail.
* API: read_feather
  * Implemented: N
  * Missing parameters: 
* API: read_fwf
  * Implemented: N
  * Missing parameters: 
* API: read_gbq
  * Implemented: N
  * Missing parameters: 
* API: read_hdf
  * Implemented: N
  * Missing parameters: 
* API: read_html()
  * Implemented: P
  * Missing parameters: dtype_backend , extract_links , storage_options
* API: read_json()
  * Implemented: P
  * Missing parameters: chunksize , compression , convert_axes , convert_dates , date_unit and more. See the pandas.read_json and pyspark.pandas.read_json for detail.
* API: read_orc()
  * Implemented: P
  * Missing parameters: dtype_backend , filesystem
* API: read_parquet()
  * Implemented: P
  * Missing parameters: dtype_backend , engine , filesystem , filters , storage_options and more. See the pandas.read_parquet and pyspark.pandas.read_parquet for detail.
* API: read_pickle
  * Implemented: N
  * Missing parameters: 
* API: read_sas
  * Implemented: N
  * Missing parameters: 
* API: read_spss
  * Implemented: N
  * Missing parameters: 
* API: read_sql()
  * Implemented: P
  * Missing parameters: chunksize , coerce_float , dtype , dtype_backend , params and more. See the pandas.read_sql and pyspark.pandas.read_sql for detail.
* API: read_sql_query()
  * Implemented: P
  * Missing parameters: chunksize , coerce_float , dtype , dtype_backend , params and more. See the pandas.read_sql_query and pyspark.pandas.read_sql_query for detail.
* API: read_sql_table()
  * Implemented: P
  * Missing parameters: chunksize , coerce_float , dtype_backend , parse_dates
* API: read_stata
  * Implemented: N
  * Missing parameters: 
* API: read_table()
  * Implemented: P
  * Missing parameters: cache_dates , chunksize , comment , compression , converters and more. See the pandas.read_table and pyspark.pandas.read_table for detail.
* API: read_xml
  * Implemented: N
  * Missing parameters: 
* API: set_eng_float_format
  * Implemented: N
  * Missing parameters: 
* API: show_versions
  * Implemented: N
  * Missing parameters: 
* API: test
  * Implemented: N
  * Missing parameters: 
* API: timedelta_range()
  * Implemented: P
  * Missing parameters: unit
* API: to_datetime()
  * Implemented: P
  * Missing parameters: cache , dayfirst , exact , utc , yearfirst
* API: to_numeric()
  * Implemented: P
  * Missing parameters: downcast , dtype_backend
* API: to_pickle
  * Implemented: N
  * Missing parameters: 
* API: to_timedelta()
  * Implemented: Y
  * Missing parameters: 
* API: unique
  * Implemented: N
  * Missing parameters: 
* API: value_counts
  * Implemented: N
  * Missing parameters: 
* API: wide_to_long
  * Implemented: N
  * Missing parameters: 


Expanding API[#](#expanding-api "Permalink to this headline")
-------------------------------------------------------------


|API       |Implemented|Missing parameters                          |
|----------|-----------|--------------------------------------------|
|agg       |N          |                                            |
|aggregate |N          |                                            |
|apply     |N          |                                            |
|corr      |N          |                                            |
|count()   |P          |numeric_only                                |
|cov       |N          |                                            |
|kurt()    |P          |numeric_only                                |
|max()     |P          |engine , engine_kwargs , numeric_only       |
|mean()    |P          |engine , engine_kwargs , numeric_only       |
|median    |N          |                                            |
|min()     |P          |engine , engine_kwargs , numeric_only       |
|quantile()|P          |interpolation , numeric_only , q            |
|rank      |N          |                                            |
|sem       |N          |                                            |
|skew()    |P          |numeric_only                                |
|std()     |P          |ddof , engine , engine_kwargs , numeric_only|
|sum()     |P          |engine , engine_kwargs , numeric_only       |
|var()     |P          |ddof , engine , engine_kwargs , numeric_only|


ExpandingGroupby API[#](#expandinggroupby-api "Permalink to this headline")
---------------------------------------------------------------------------


|API       |Implemented|Missing parameters                          |
|----------|-----------|--------------------------------------------|
|agg       |N          |                                            |
|aggregate |N          |                                            |
|apply     |N          |                                            |
|corr      |N          |                                            |
|count()   |P          |numeric_only                                |
|cov       |N          |                                            |
|kurt()    |P          |numeric_only                                |
|max()     |P          |engine , engine_kwargs , numeric_only       |
|mean()    |P          |engine , engine_kwargs , numeric_only       |
|median    |N          |                                            |
|min()     |P          |engine , engine_kwargs , numeric_only       |
|quantile()|P          |interpolation , numeric_only , q            |
|rank      |N          |                                            |
|sem       |N          |                                            |
|skew()    |P          |numeric_only                                |
|std()     |P          |ddof , engine , engine_kwargs , numeric_only|
|sum()     |P          |engine , engine_kwargs , numeric_only       |
|var()     |P          |ddof , engine , engine_kwargs , numeric_only|


Rolling API[#](#rolling-api "Permalink to this headline")
---------------------------------------------------------


|API       |Implemented|Missing parameters                          |
|----------|-----------|--------------------------------------------|
|agg       |N          |                                            |
|aggregate |N          |                                            |
|apply     |N          |                                            |
|corr      |N          |                                            |
|count()   |P          |numeric_only                                |
|cov       |N          |                                            |
|kurt()    |P          |numeric_only                                |
|max()     |P          |engine , engine_kwargs , numeric_only       |
|mean()    |P          |engine , engine_kwargs , numeric_only       |
|median    |N          |                                            |
|min()     |P          |engine , engine_kwargs , numeric_only       |
|quantile()|P          |interpolation , numeric_only , q            |
|rank      |N          |                                            |
|sem       |N          |                                            |
|skew()    |P          |numeric_only                                |
|std()     |P          |ddof , engine , engine_kwargs , numeric_only|
|sum()     |P          |engine , engine_kwargs , numeric_only       |
|var()     |P          |ddof , engine , engine_kwargs , numeric_only|


RollingGroupby API[#](#rollinggroupby-api "Permalink to this headline")
-----------------------------------------------------------------------


|API       |Implemented|Missing parameters                          |
|----------|-----------|--------------------------------------------|
|agg       |N          |                                            |
|aggregate |N          |                                            |
|apply     |N          |                                            |
|corr      |N          |                                            |
|count()   |P          |numeric_only                                |
|cov       |N          |                                            |
|kurt()    |P          |numeric_only                                |
|max()     |P          |engine , engine_kwargs , numeric_only       |
|mean()    |P          |engine , engine_kwargs , numeric_only       |
|median    |N          |                                            |
|min()     |P          |engine , engine_kwargs , numeric_only       |
|quantile()|P          |interpolation , numeric_only , q            |
|rank      |N          |                                            |
|sem       |N          |                                            |
|skew()    |P          |numeric_only                                |
|std()     |P          |ddof , engine , engine_kwargs , numeric_only|
|sum()     |P          |engine , engine_kwargs , numeric_only       |
|var()     |P          |ddof , engine , engine_kwargs , numeric_only|


Window API[#](#window-api "Permalink to this headline")
-------------------------------------------------------


|API      |Implemented|Missing parameters|
|---------|-----------|------------------|
|agg      |N          |                  |
|aggregate|N          |                  |
|mean     |N          |                  |
|std      |N          |                  |
|sum      |N          |                  |
|var      |N          |                  |


DataFrameGroupBy API[#](#dataframegroupby-api "Permalink to this headline")
---------------------------------------------------------------------------


|API         |Implemented|Missing parameters                   |
|------------|-----------|-------------------------------------|
|agg()       |P          |engine , engine_kwargs , func        |
|aggregate() |P          |engine , engine_kwargs , func        |
|all()       |Y          |                                     |
|any()       |P          |skipna                               |
|apply()     |P          |include_groups                       |
|bfill()     |Y          |                                     |
|boxplot     |N          |                                     |
|corr()      |Y          |                                     |
|corrwith    |N          |                                     |
|count()     |Y          |                                     |
|cov         |N          |                                     |
|cumcount()  |Y          |                                     |
|cummax()    |P          |axis , numeric_only                  |
|cummin()    |P          |axis , numeric_only                  |
|cumprod()   |P          |axis                                 |
|cumsum()    |P          |axis                                 |
|describe()  |P          |exclude , include , percentiles      |
|diff()      |P          |axis                                 |
|ewm()       |Y          |                                     |
|expanding() |Y          |                                     |
|ffill()     |Y          |                                     |
|fillna()    |P          |downcast                             |
|filter()    |P          |dropna                               |
|first()     |P          |skipna                               |
|get_group() |P          |obj                                  |
|head()      |Y          |                                     |
|hist        |N          |                                     |
|idxmax()    |P          |axis , numeric_only                  |
|idxmin()    |P          |axis , numeric_only                  |
|last()      |P          |skipna                               |
|max()       |P          |engine , engine_kwargs               |
|mean()      |P          |engine , engine_kwargs               |
|median()    |Y          |                                     |
|min()       |P          |engine , engine_kwargs               |
|ngroup      |N          |                                     |
|nunique()   |Y          |                                     |
|ohlc        |N          |                                     |
|pct_change  |N          |                                     |
|pipe        |N          |                                     |
|prod()      |Y          |                                     |
|quantile()  |P          |interpolation , numeric_only         |
|rank()      |P          |axis , na_option , pct               |
|resample    |N          |                                     |
|rolling()   |Y          |                                     |
|sample      |N          |                                     |
|sem()       |P          |numeric_only                         |
|shift()     |P          |axis , freq , suffix                 |
|size()      |Y          |                                     |
|skew()      |P          |axis , numeric_only , skipna         |
|std()       |P          |engine , engine_kwargs , numeric_only|
|sum()       |P          |engine , engine_kwargs               |
|tail()      |Y          |                                     |
|take        |N          |                                     |
|transform() |P          |engine , engine_kwargs               |
|value_counts|N          |                                     |
|var()       |P          |engine , engine_kwargs               |


GroupBy API[#](#groupby-api "Permalink to this headline")
---------------------------------------------------------


|API        |Implemented|Missing parameters                   |
|-----------|-----------|-------------------------------------|
|agg()      |P          |func                                 |
|aggregate()|P          |func                                 |
|all()      |Y          |                                     |
|any()      |P          |skipna                               |
|apply()    |P          |include_groups                       |
|bfill()    |Y          |                                     |
|count()    |Y          |                                     |
|cumcount() |Y          |                                     |
|cummax()   |P          |axis , numeric_only                  |
|cummin()   |P          |axis , numeric_only                  |
|cumprod()  |P          |axis                                 |
|cumsum()   |P          |axis                                 |
|describe   |N          |                                     |
|diff()     |P          |axis                                 |
|ewm()      |Y          |                                     |
|expanding()|Y          |                                     |
|ffill()    |Y          |                                     |
|first()    |P          |skipna                               |
|get_group()|P          |obj                                  |
|head()     |Y          |                                     |
|last()     |P          |skipna                               |
|max()      |P          |engine , engine_kwargs               |
|mean()     |P          |engine , engine_kwargs               |
|median()   |Y          |                                     |
|min()      |P          |engine , engine_kwargs               |
|ngroup     |N          |                                     |
|ohlc       |N          |                                     |
|pct_change |N          |                                     |
|pipe       |N          |                                     |
|prod()     |Y          |                                     |
|quantile() |P          |interpolation , numeric_only         |
|rank()     |P          |axis , na_option , pct               |
|resample   |N          |                                     |
|rolling()  |Y          |                                     |
|sample     |N          |                                     |
|sem()      |P          |numeric_only                         |
|shift()    |P          |axis , freq , suffix                 |
|size()     |Y          |                                     |
|std()      |P          |engine , engine_kwargs , numeric_only|
|sum()      |P          |engine , engine_kwargs               |
|tail()     |Y          |                                     |
|var()      |P          |engine , engine_kwargs               |


SeriesGroupBy API[#](#seriesgroupby-api "Permalink to this headline")
---------------------------------------------------------------------


|API           |Implemented|Missing parameters                   |
|--------------|-----------|-------------------------------------|
|agg()         |P          |engine , engine_kwargs , func        |
|aggregate()   |P          |engine , engine_kwargs , func        |
|all()         |Y          |                                     |
|any()         |P          |skipna                               |
|apply()       |Y          |                                     |
|bfill()       |Y          |                                     |
|corr          |N          |                                     |
|count()       |Y          |                                     |
|cov           |N          |                                     |
|cumcount()    |Y          |                                     |
|cummax()      |P          |axis , numeric_only                  |
|cummin()      |P          |axis , numeric_only                  |
|cumprod()     |P          |axis                                 |
|cumsum()      |P          |axis                                 |
|describe      |N          |                                     |
|diff()        |P          |axis                                 |
|ewm()         |Y          |                                     |
|expanding()   |Y          |                                     |
|ffill()       |Y          |                                     |
|fillna()      |P          |downcast                             |
|filter()      |P          |dropna                               |
|first()       |P          |skipna                               |
|get_group()   |P          |obj                                  |
|head()        |Y          |                                     |
|hist          |N          |                                     |
|idxmax()      |P          |axis                                 |
|idxmin()      |P          |axis                                 |
|last()        |P          |skipna                               |
|max()         |P          |engine , engine_kwargs               |
|mean()        |P          |engine , engine_kwargs               |
|median()      |Y          |                                     |
|min()         |P          |engine , engine_kwargs               |
|ngroup        |N          |                                     |
|nlargest()    |P          |keep                                 |
|nsmallest()   |P          |keep                                 |
|nunique()     |Y          |                                     |
|ohlc          |N          |                                     |
|pct_change    |N          |                                     |
|pipe          |N          |                                     |
|prod()        |Y          |                                     |
|quantile()    |P          |interpolation , numeric_only         |
|rank()        |P          |axis , na_option , pct               |
|resample      |N          |                                     |
|rolling()     |Y          |                                     |
|sample        |N          |                                     |
|sem()         |P          |numeric_only                         |
|shift()       |P          |axis , freq , suffix                 |
|size()        |Y          |                                     |
|skew()        |P          |axis , numeric_only , skipna         |
|std()         |P          |engine , engine_kwargs , numeric_only|
|sum()         |P          |engine , engine_kwargs               |
|tail()        |Y          |                                     |
|take          |N          |                                     |
|transform()   |P          |engine , engine_kwargs               |
|unique()      |Y          |                                     |
|value_counts()|P          |bins , normalize                     |
|var()         |P          |engine , engine_kwargs               |
