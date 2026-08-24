# Row — PySpark 4.0.1 documentation
Copyright @ 2025 The Apache Software Foundation, Licensed under the [Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0).

Created using [Sphinx](https://www.sphinx-doc.org/) 4.5.0.


# pyspark.sql.Row.asDict — PySpark 4.0.1 documentation
Row.asDict(_recursive\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#Row.asDict)
[#](#pyspark.sql.Row.asDict "Permalink to this definition")

Return as a dict

Parameters

**recursive**bool, optional

turns the nested Rows to dict (default: False).

Notes

If a row contains duplicate field names, e.g., the rows of a join between two [`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame") that both have the fields of same names, one of the duplicate fields will be selected by `asDict`. `__getitem__` will also return one of the duplicate fields, however returned value might be different to `asDict`.

Examples

```
>>> from pyspark.sql import Row
>>> Row(name="Alice", age=11).asDict() == {'name': 'Alice', 'age': 11}
True
>>> row = Row(key=1, value=Row(name='a', age=2))
>>> row.asDict() == {'key': 1, 'value': Row(name='a', age=2)}
True
>>> row.asDict(True) == {'key': 1, 'value': {'name': 'a', 'age': 2}}
True

```
