# VariantVal — PySpark 4.0.1 documentation


* VariantVal.toPython(): VariantVal.toJson([zone_id])
  * Convert the VariantVal to a Python data structure.: Convert the VariantVal to a JSON string.
* VariantVal.toPython(): VariantVal.parseJson(json_str)
  * Convert the VariantVal to a Python data structure.: Convert the VariantVal to a nested Python object of Python data types.


# pyspark.sql.VariantVal.toPython — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [VariantVal](../variant_val.html)
*   pyspark.sql.VariantVal.toPython

VariantVal.toPython()
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantVal.toPython)
[#](#pyspark.sql.VariantVal.toPython "Permalink to this definition")

Convert the VariantVal to a Python data structure.

Returns

Any

A Python object that represents the Variant.


# pyspark.sql.VariantVal.toJson — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [VariantVal](../variant_val.html)
*   pyspark.sql.VariantVal.toJson

VariantVal.toJson(_zone\_id\='UTC'_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantVal.toJson)
[#](#pyspark.sql.VariantVal.toJson "Permalink to this definition")

Convert the VariantVal to a JSON string. The zone ID represents the time zone that the timestamp should be printed in. It is defaulted to UTC. The list of valid zone IDs can be found by importing the zoneinfo module and running `zoneinfo.available_timezones()`.

Returns

str

A JSON string that represents the Variant.

# pyspark.sql.VariantVal.parseJson — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [VariantVal](../variant_val.html)
*   pyspark.sql.VariantVal.parseJson

_classmethod_ VariantVal.parseJson(_json\_str_)
[\[source\]](about:blank/_modules/pyspark/sql/types.html#VariantVal.parseJson)
[#](#pyspark.sql.VariantVal.parseJson "Permalink to this definition")

Convert the VariantVal to a nested Python object of Python data types. :return: Python representation of the Variant nested structure

