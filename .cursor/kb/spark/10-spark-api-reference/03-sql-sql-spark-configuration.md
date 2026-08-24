# pyspark.sql.conf.RuntimeConfig — PySpark 4.0.1 documentation
_class_ pyspark.sql.conf.RuntimeConfig(_jconf_)
[\[source\]](about:blank/_modules/pyspark/sql/conf.html#RuntimeConfig)
[#](#pyspark.sql.conf.RuntimeConfig "Permalink to this definition")

User-facing configuration API, accessible through SparkSession.conf.

Options set here are automatically propagated to the Hadoop configuration during I/O.

Changed in version 3.4.0: Supports Spark Connect.

Methods



* get(key[, default]): isModifiable(key)
  * Returns the value of Spark runtime configuration property for the given key, assuming it is set.: Indicates whether the configuration property with the given key is modifiable in the current session.
* get(key[, default]): set(key, value)
  * Returns the value of Spark runtime configuration property for the given key, assuming it is set.: Sets the given Spark runtime configuration property.
* get(key[, default]): unset(key)
  * Returns the value of Spark runtime configuration property for the given key, assuming it is set.: Resets the configuration property for the given key.


Attributes

