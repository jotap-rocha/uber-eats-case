# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/extensions.html

# Extensions#

## Accessors#

Accessors can be written and registered with pandas-on-Spark Dataframes, Series, and Index objects. Accessors allow developers to extend the functionality of pandas-on-Spark objects seamlessly by writing arbitrary classes and methods which are then wrapped in one of the following decorators.

[`register_dataframe_accessor`](api/pyspark.pandas.extensions.register_dataframe_accessor.html#pyspark.pandas.extensions.register_dataframe_accessor "pyspark.pandas.extensions.register_dataframe_accessor")(name) | Register a custom accessor with a DataFrame  
---|---  
[`register_series_accessor`](api/pyspark.pandas.extensions.register_series_accessor.html#pyspark.pandas.extensions.register_series_accessor "pyspark.pandas.extensions.register_series_accessor")(name) | Register a custom accessor with a Series object  
[`register_index_accessor`](api/pyspark.pandas.extensions.register_index_accessor.html#pyspark.pandas.extensions.register_index_accessor "pyspark.pandas.extensions.register_index_accessor")(name) | Register a custom accessor with an Index  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/extensions.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.extensions.register_dataframe_accessor.html

# pyspark.pandas.extensions.register_dataframe_accessor#

pyspark.pandas.extensions.register_dataframe_accessor(_name_)[[source]](../../../_modules/pyspark/pandas/extensions.html#register_dataframe_accessor)#
    

Register a custom accessor with a DataFrame

Parameters
    

**name** str
    

name used when calling the accessor after its registered

Returns
    

callable
    

A class decorator.

See also

[`register_series_accessor`](pyspark.pandas.extensions.register_series_accessor.html#pyspark.pandas.extensions.register_series_accessor "pyspark.pandas.extensions.register_series_accessor")
    

Register a custom accessor on Series objects

[`register_index_accessor`](pyspark.pandas.extensions.register_index_accessor.html#pyspark.pandas.extensions.register_index_accessor "pyspark.pandas.extensions.register_index_accessor")
    

Register a custom accessor on Index objects

Notes

When accessed, your accessor will be initialized with the pandas-on-Spark object the user is interacting with. The accessorâs init method should always ingest the object being accessed. See the examples for the init signature.

In the pandas API, if data passed to your accessor has an incorrect dtype, itâs recommended to raise an `AttributeError` for consistency purposes. In pandas-on-Spark, `ValueError` is more frequently used to annotate when a valueâs datatype is unexpected for a given method/function.

Ultimately, you can structure this however you like, but pandas-on-Spark would likely do something like this:
    
    
    >>> ps.Series(['a', 'b']).dt
    ...
    Traceback (most recent call last):
        ...
    ValueError: Cannot call DatetimeMethods on type StringType()
    

Examples

In your library code:
    
    
    from pyspark.pandas.extensions import register_dataframe_accessor
    
    @register_dataframe_accessor("geo")
    class GeoAccessor:
    
        def __init__(self, pandas_on_spark_obj):
            self._obj = pandas_on_spark_obj
            # other constructor logic
    
        @property
        def center(self):
            # return the geographic center point of this DataFrame
            lat = self._obj.latitude
            lon = self._obj.longitude
            return (float(lon.mean()), float(lat.mean()))
    
        def plot(self):
            # plot this array's data on a map
            pass
    

Then, in an ipython session:
    
    
    >>> ## Import if the accessor is in the other file.
    >>> # from my_ext_lib import GeoAccessor
    >>> psdf = ps.DataFrame({"longitude": np.linspace(0,10),
    ...                     "latitude": np.linspace(0, 20)})
    >>> psdf.geo.center  
    (5.0, 10.0)
    
    >>> psdf.geo.plot()  
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.extensions.register_dataframe_accessor.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.extensions.register_series_accessor.html

# pyspark.pandas.extensions.register_series_accessor#

pyspark.pandas.extensions.register_series_accessor(_name_)[[source]](../../../_modules/pyspark/pandas/extensions.html#register_series_accessor)#
    

Register a custom accessor with a Series object

Parameters
    

**name** str
    

name used when calling the accessor after its registered

Returns
    

callable
    

A class decorator.

See also

[`register_dataframe_accessor`](pyspark.pandas.extensions.register_dataframe_accessor.html#pyspark.pandas.extensions.register_dataframe_accessor "pyspark.pandas.extensions.register_dataframe_accessor")
    

Register a custom accessor on DataFrame objects

[`register_index_accessor`](pyspark.pandas.extensions.register_index_accessor.html#pyspark.pandas.extensions.register_index_accessor "pyspark.pandas.extensions.register_index_accessor")
    

Register a custom accessor on Index objects

Notes

When accessed, your accessor will be initialized with the pandas-on-Spark object the user is interacting with. The code signature must be:
    
    
    def __init__(self, pandas_on_spark_obj):
        # constructor logic
    ...
    

In the pandas API, if data passed to your accessor has an incorrect dtype, itâs recommended to raise an `AttributeError` for consistency purposes. In pandas-on-Spark, `ValueError` is more frequently used to annotate when a valueâs datatype is unexpected for a given method/function.

Ultimately, you can structure this however you like, but pandas-on-Spark would likely do something like this:
    
    
    >>> ps.Series(['a', 'b']).dt
    ...
    Traceback (most recent call last):
        ...
    ValueError: Cannot call DatetimeMethods on type StringType()
    

Examples

In your library code:
    
    
    from pyspark.pandas.extensions import register_series_accessor
    
    @register_series_accessor("geo")
    class GeoAccessor:
    
        def __init__(self, pandas_on_spark_obj):
            self._obj = pandas_on_spark_obj
    
        @property
        def is_valid(self):
            # boolean check to see if series contains valid geometry
            return True
    

Then, in an ipython session:
    
    
    >>> ## Import if the accessor is in the other file.
    >>> # from my_ext_lib import GeoAccessor
    >>> psdf = ps.DataFrame({"longitude": np.linspace(0,10),
    ...                     "latitude": np.linspace(0, 20)})
    >>> psdf.longitude.geo.is_valid  
    True
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.extensions.register_series_accessor.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.extensions.register_index_accessor.html

# pyspark.pandas.extensions.register_index_accessor#

pyspark.pandas.extensions.register_index_accessor(_name_)[[source]](../../../_modules/pyspark/pandas/extensions.html#register_index_accessor)#
    

Register a custom accessor with an Index

Parameters
    

**name** str
    

name used when calling the accessor after its registered

Returns
    

callable
    

A class decorator.

See also

[`register_dataframe_accessor`](pyspark.pandas.extensions.register_dataframe_accessor.html#pyspark.pandas.extensions.register_dataframe_accessor "pyspark.pandas.extensions.register_dataframe_accessor")
    

Register a custom accessor on DataFrame objects

[`register_series_accessor`](pyspark.pandas.extensions.register_series_accessor.html#pyspark.pandas.extensions.register_series_accessor "pyspark.pandas.extensions.register_series_accessor")
    

Register a custom accessor on Series objects

Notes

When accessed, your accessor will be initialized with the pandas-on-Spark object the user is interacting with. The code signature must be:
    
    
    def __init__(self, pandas_on_spark_obj):
        # constructor logic
    ...
    

In the pandas API, if data passed to your accessor has an incorrect dtype, itâs recommended to raise an `AttributeError` for consistency purposes. In pandas-on-Spark, `ValueError` is more frequently used to annotate when a valueâs datatype is unexpected for a given method/function.

Ultimately, you can structure this however you like, but pandas-on-Spark would likely do something like this:
    
    
    >>> ps.Series(['a', 'b']).dt
    ...
    Traceback (most recent call last):
        ...
    ValueError: Cannot call DatetimeMethods on type StringType()
    

Examples

In your library code:
    
    
    from pyspark.pandas.extensions import register_index_accessor
    
    @register_index_accessor("foo")
    class CustomAccessor:
    
        def __init__(self, pandas_on_spark_obj):
            self._obj = pandas_on_spark_obj
            self.item = "baz"
    
        @property
        def bar(self):
            # return item value
            return self.item
    

Then, in an ipython session:
    
    
    >>> ## Import if the accessor is in the other file.
    >>> # from my_ext_lib import CustomAccessor
    >>> psdf = ps.DataFrame({"longitude": np.linspace(0,10),
    ...                     "latitude": np.linspace(0, 20)})
    >>> psdf.index.foo.bar  
    'baz'
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.extensions.register_index_accessor.rst.txt)
