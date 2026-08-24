# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/options.html

# Options and settings#

API for configuring global behavior. See [the User Guide](../../tutorial/pandas_on_spark/options.html#user-guide-options) for more.

## Working with options#

[`reset_option`](api/pyspark.pandas.reset_option.html#pyspark.pandas.reset_option "pyspark.pandas.reset_option")(key) | Reset one option to their default value.  
---|---  
[`get_option`](api/pyspark.pandas.get_option.html#pyspark.pandas.get_option "pyspark.pandas.get_option")(key[,Â default]) | Retrieves the value of the specified option.  
[`set_option`](api/pyspark.pandas.set_option.html#pyspark.pandas.set_option "pyspark.pandas.set_option")(key,Â value) | Sets the value of the specified option.  
[`option_context`](api/pyspark.pandas.option_context.html#pyspark.pandas.option_context "pyspark.pandas.option_context")(*args) | Context manager to temporarily set options in the with statement context.  
  
__On this page

[ __Show Source](../../_sources/reference/pyspark.pandas/options.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.reset_option.html

# pyspark.pandas.reset_option#

pyspark.pandas.reset_option(_key_)[[source]](../../../_modules/pyspark/pandas/config.html#reset_option)#
    

Reset one option to their default value.

Pass âallâ as an argument to reset all options.

Parameters
    

**key** str
    

If specified only option will be reset.

Returns
    

None
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.reset_option.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.get_option.html

# pyspark.pandas.get_option#

pyspark.pandas.get_option(_key_ , _default= <no value>_)[[source]](../../../_modules/pyspark/pandas/config.html#get_option)#
    

Retrieves the value of the specified option.

Parameters
    

**key** str
    

The key which should match a single option.

**default** object
    

The default value if the option is not set yet. The value should be JSON serializable.

Returns
    

**result** the value of the option
    
Raises
    

**OptionError** if no such option exists and the default is not provided
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.get_option.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.set_option.html

# pyspark.pandas.set_option#

pyspark.pandas.set_option(_key_ , _value_)[[source]](../../../_modules/pyspark/pandas/config.html#set_option)#
    

Sets the value of the specified option.

Parameters
    

**key** str
    

The key which should match a single option.

**value** object
    

New value of option. The value should be JSON serializable.

Returns
    

None
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.set_option.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/api/pyspark.pandas.option_context.html

# pyspark.pandas.option_context#

pyspark.pandas.option_context(_* args_)[[source]](../../../_modules/pyspark/pandas/config.html#option_context)#
    

Context manager to temporarily set options in the with statement context.

You need to invoke `option_context(pat, val, [(pat, val), ...])`.

Examples
    
    
    >>> with option_context('display.max_rows', 10, 'compute.max_rows', 5):
    ...     print(get_option('display.max_rows'), get_option('compute.max_rows'))
    10 5
    >>> print(get_option('display.max_rows'), get_option('compute.max_rows'))
    1000 1000
    

[ __Show Source](../../../_sources/reference/pyspark.pandas/api/pyspark.pandas.option_context.rst.txt)
