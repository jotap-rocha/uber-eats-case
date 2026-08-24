# Stateful Processor — PySpark 4.0.1 documentation


* StatefulProcessor.init(handle): StatefulProcessor.handleInputRows(key, rows, ...)
  * Function that will be invoked as the first method that allows for users to initialize all their state variables and perform other init actions before handling data.: Function that will allow users to interact with input data rows along with the grouping key.
* StatefulProcessor.init(handle): StatefulProcessor.close()
  * Function that will be invoked as the first method that allows for users to initialize all their state variables and perform other init actions before handling data.: Function called as the last method that allows for users to perform any cleanup or teardown operations.
* StatefulProcessor.init(handle): StatefulProcessor.handleInitialState(key, ...)
  * Function that will be invoked as the first method that allows for users to initialize all their state variables and perform other init actions before handling data.: Optional to implement. Will act as no-op if not defined or no initial state input.


# pyspark.sql.streaming.StatefulProcessor.init — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Stateful Processor](../stateful_processor.html)
*   pyspark.sql.streaming.StatefulProcessor.init

_abstract_ StatefulProcessor.init(_handle_)
[\[source\]](about:blank/_modules/pyspark/sql/streaming/stateful_processor.html#StatefulProcessor.init)
[#](#pyspark.sql.streaming.StatefulProcessor.init "Permalink to this definition")

Function that will be invoked as the first method that allows for users to initialize all their state variables and perform other init actions before handling data.

Parameters

**handle**`pyspark.sql.streaming.stateful_processor.StatefulProcessorHandle`

Handle to the stateful processor that provides access to the state store and other stateful processing related APIs.


# pyspark.sql.streaming.StatefulProcessor.handleInputRows — PySpark 4.0.1 documentation
_abstract_ StatefulProcessor.handleInputRows(_key_, _rows_, _timerValues_)
[\[source\]](about:blank/_modules/pyspark/sql/streaming/stateful_processor.html#StatefulProcessor.handleInputRows)
[#](#pyspark.sql.streaming.StatefulProcessor.handleInputRows "Permalink to this definition")

Function that will allow users to interact with input data rows along with the grouping key. It should take parameters (key, Iterator\[pandas.DataFrame\]) and return another Iterator\[pandas.DataFrame\]. For each group, all columns are passed together as pandas.DataFrame to the function, and the returned pandas.DataFrame across all invocations are combined as a `DataFrame`. Note that the function should not make a guess of the number of elements in the iterator. To process all data, the handleInputRows function needs to iterate all elements and process them. On the other hand, the handleInputRows function is not strictly required to iterate through all elements in the iterator if it intends to read a part of data.

Parameters

**key**Any

grouping key.

**rows**iterable of `pandas.DataFrame`

iterator of input rows associated with grouping key

**timerValues: TimerValues**

Timer value for the current batch that process the input rows. Users can get the processing or event time timestamp from TimerValues.


# pyspark.sql.streaming.StatefulProcessor.close — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Stateful Processor](../stateful_processor.html)
*   pyspark.sql.streaming.StatefulProcessor.close

StatefulProcessor.close()
[\[source\]](about:blank/_modules/pyspark/sql/streaming/stateful_processor.html#StatefulProcessor.close)
[#](#pyspark.sql.streaming.StatefulProcessor.close "Permalink to this definition")

Function called as the last method that allows for users to perform any cleanup or teardown operations.

# pyspark.sql.streaming.StatefulProcessor.handleInitialState — PySpark 4.0.1 documentation
StatefulProcessor.handleInitialState(_key_, _initialState_, _timerValues_)
[\[source\]](about:blank/_modules/pyspark/sql/streaming/stateful_processor.html#StatefulProcessor.handleInitialState)
[#](#pyspark.sql.streaming.StatefulProcessor.handleInitialState "Permalink to this definition")

Optional to implement. Will act as no-op if not defined or no initial state input.

Function that will be invoked only in the first batch for users to process initial states.

Parameters

**key**Any

grouping key.

**initialState: :class:\`pandas.DataFrame\`**

One dataframe in the initial state associated with the key.

**timerValues: TimerValues**

Timer value for the current batch that process the input rows. Users can get the processing or event time timestamp from TimerValues.

