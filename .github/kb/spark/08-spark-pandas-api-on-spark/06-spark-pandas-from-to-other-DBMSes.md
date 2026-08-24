# From/to other DBMSes — PySpark 4.0.1 documentation
The APIs interacting with other DBMSes in pandas API on Spark are slightly different from the ones in pandas because pandas API on Spark leverages JDBC APIs in PySpark to read and write from/to other DBMSes.

The APIs to read/write from/to external DBMSes are as follows:



* read_sql_table(table_name, con[, schema, ...]): read_sql_query(sql, con[, index_col])
  * Read SQL database table into a DataFrame.: Read SQL query into a DataFrame.
* read_sql_table(table_name, con[, schema, ...]): read_sql(sql, con[, index_col, columns])
  * Read SQL database table into a DataFrame.: Read SQL query or database table into a DataFrame.


pandas-on-Spark needs a canonical JDBC URL for `con`, and is able to take extra keyword arguments for [the options in PySpark JDBC APIs](https://spark.apache.org/docs/latest/sql-data-sources-jdbc.html):

```
ps.read_sql(..., dbtable="...", driver="", keytab="", ...)

```


Reading and writing DataFrames[#](#reading-and-writing-dataframes "Permalink to this headline")
-----------------------------------------------------------------------------------------------

In the example below, you will read and write a table in SQLite.

Firstly, create the `example` database as below via Python’s SQLite library. This will be read to pandas-on-Spark later:

```
import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()
# Create table
cur.execute(
    '''CREATE TABLE stocks
       (date text, trans text, symbol text, qty real, price real)''')
# Insert a row of data
cur.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")
# Save (commit) the changes
con.commit()
con.close()

```


Pandas API on Spark requires a JDBC driver to read so it requires the driver for your particular database to be on the Spark’s classpath. For SQLite JDBC driver, you can download it, for example, as below:

```
curl -O https://repo1.maven.org/maven2/org/xerial/sqlite-jdbc/3.34.0/sqlite-jdbc-3.34.0.jar

```


After that, you should add it into your Spark session first. Once you add it, pandas API on Spark will automatically detect the Spark session and leverage it.

```
import os

from pyspark.sql import SparkSession

(SparkSession.builder
    .master("local")
    .appName("SQLite JDBC")
    .config(
        "spark.jars",
        "{}/sqlite-jdbc-3.34.0.jar".format(os.getcwd()))
    .config(
        "spark.driver.extraClassPath",
        "{}/sqlite-jdbc-3.34.0.jar".format(os.getcwd()))
    .getOrCreate())

```


Now, you’re ready to read the table:

```
import pyspark.pandas as ps

df = ps.read_sql("stocks", con="jdbc:sqlite:{}/example.db".format(os.getcwd()))
df

```


```
         date trans symbol    qty  price
0  2006-01-05   BUY   RHAT  100.0  35.14

```


You can also write it back to the `stocks` table as below:

```
df.price += 1
df.spark.to_spark_io(
    format="jdbc", mode="append",
    dbtable="stocks", url="jdbc:sqlite:{}/example.db".format(os.getcwd()))
ps.read_sql("stocks", con="jdbc:sqlite:{}/example.db".format(os.getcwd()))

```


```
         date trans symbol    qty  price
0  2006-01-05   BUY   RHAT  100.0  35.14
1  2006-01-05   BUY   RHAT  100.0  36.14

```
