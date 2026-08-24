# Observation — PySpark 4.0.1 documentation
previous

pyspark.sql.avro.functions.to\_avro

# pyspark.sql.Observation.get — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Observation](../observation.html)
*   pyspark.sql.Observation.get

_property_ Observation.get[#](#pyspark.sql.Observation.get "Permalink to this definition")

Get the observed metrics.

Waits until the observed dataset finishes its first action. Only the result of the first action is available. Subsequent actions do not modify the result.

Returns

dict

the observed metrics