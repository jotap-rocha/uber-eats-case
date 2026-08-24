# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.logger.html

# Logger#

## Classes#

[`PySparkLogger`](api/pyspark.logger.PySparkLogger.html#pyspark.logger.PySparkLogger "pyspark.logger.PySparkLogger")([name]) | Custom logging.Logger wrapper for PySpark that logs messages in a structured JSON format.  
---|---  
  
## Methods#

[`PySparkLogger.getLogger`](api/pyspark.logger.PySparkLogger.getLogger.html#pyspark.logger.PySparkLogger.getLogger "pyspark.logger.PySparkLogger.getLogger")([name]) | Return a PySparkLogger with the specified name, creating it if necessary.  
---|---  
[`PySparkLogger.addHandler`](api/pyspark.logger.PySparkLogger.addHandler.html#pyspark.logger.PySparkLogger.addHandler "pyspark.logger.PySparkLogger.addHandler")(handler) | Add the specified handler to this logger in structured JSON format.  
[`PySparkLogger.info`](api/pyspark.logger.PySparkLogger.info.html#pyspark.logger.PySparkLogger.info "pyspark.logger.PySparkLogger.info")(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'INFO' in structured JSON format.  
[`PySparkLogger.warning`](api/pyspark.logger.PySparkLogger.warning.html#pyspark.logger.PySparkLogger.warning "pyspark.logger.PySparkLogger.warning")(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'WARNING' in structured JSON format.  
[`PySparkLogger.error`](api/pyspark.logger.PySparkLogger.error.html#pyspark.logger.PySparkLogger.error "pyspark.logger.PySparkLogger.error")(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'ERROR' in structured JSON format.  
[`PySparkLogger.exception`](api/pyspark.logger.PySparkLogger.exception.html#pyspark.logger.PySparkLogger.exception "pyspark.logger.PySparkLogger.exception")(msg,Â *args[,Â exc_info]) | Convenience method for logging an ERROR with exception information.  
  
__On this page

[ __Show Source](../_sources/reference/pyspark.logger.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.html

# pyspark.logger.PySparkLogger#

_class _pyspark.logger.PySparkLogger(_name ='PySparkLogger'_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger)#
    

Custom logging.Logger wrapper for PySpark that logs messages in a structured JSON format.

PySparkLogger extends the standard Python logging.Logger class, allowing seamless integration with existing logging setups. It customizes the log output to JSON format, including additional context information, making it more useful for PySpark applications.

New in version 4.0.0.

Methods

`addFilter`(filter) | Add the specified filter to this handler.  
---|---  
[`addHandler`](pyspark.logger.PySparkLogger.addHandler.html#pyspark.logger.PySparkLogger.addHandler "pyspark.logger.PySparkLogger.addHandler")(handler) | Add the specified handler to this logger in structured JSON format.  
`callHandlers`(record) | Pass a record to all relevant handlers.  
`critical`(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'CRITICAL' in structured JSON format.  
`debug`(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'DEBUG' in structured JSON format.  
[`error`](pyspark.logger.PySparkLogger.error.html#pyspark.logger.PySparkLogger.error "pyspark.logger.PySparkLogger.error")(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'ERROR' in structured JSON format.  
[`exception`](pyspark.logger.PySparkLogger.exception.html#pyspark.logger.PySparkLogger.exception "pyspark.logger.PySparkLogger.exception")(msg,Â *args[,Â exc_info]) | Convenience method for logging an ERROR with exception information.  
`fatal`(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'CRITICAL' in structured JSON format.  
`filter`(record) | Determine if a record is loggable by consulting all the filters.  
`findCaller`([stack_info,Â stacklevel]) | Find the stack frame of the caller so that we can note the source file name, line number and function name.  
`getChild`(suffix) | Get a logger which is a descendant to this one.  
`getEffectiveLevel`() | Get the effective level for this logger.  
[`getLogger`](pyspark.logger.PySparkLogger.getLogger.html#pyspark.logger.PySparkLogger.getLogger "pyspark.logger.PySparkLogger.getLogger")([name]) | Return a PySparkLogger with the specified name, creating it if necessary.  
`handle`(record) | Call the handlers for the specified record.  
`hasHandlers`() | See if this logger has any handlers configured.  
[`info`](pyspark.logger.PySparkLogger.info.html#pyspark.logger.PySparkLogger.info "pyspark.logger.PySparkLogger.info")(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'INFO' in structured JSON format.  
`isEnabledFor`(level) | Is this logger enabled for level 'level'?  
`log`(level,Â msg,Â *args,Â **kwargs) | Log 'msg % args' with the given severity in structured JSON format.  
`makeRecord`(name,Â level,Â fn,Â lno,Â msg,Â args,Â ...) | A factory method which can be overridden in subclasses to create specialized LogRecords.  
`removeFilter`(filter) | Remove the specified filter from this handler.  
`removeHandler`(hdlr) | Remove the specified handler from this logger.  
`setLevel`(level) | Set the logging level of this logger.  
`warn`(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'WARN' in structured JSON format.  
[`warning`](pyspark.logger.PySparkLogger.warning.html#pyspark.logger.PySparkLogger.warning "pyspark.logger.PySparkLogger.warning")(msg,Â *args,Â **kwargs) | Log 'msg % args' with severity 'WARNING' in structured JSON format.  
  
Attributes

`manager` |   
---|---  
`root` |   
  
[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.getLogger.html

# pyspark.logger.PySparkLogger.getLogger#

_static _PySparkLogger.getLogger(_name =None_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger.getLogger)#
    

Return a PySparkLogger with the specified name, creating it if necessary.

If no name is specified, return the logging.RootLogger.

Parameters
    

**name** str, optional
    

The name of the logger.

Returns
    

PySparkLogger
    

A configured instance of PySparkLogger.

[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.getLogger.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.addHandler.html

# pyspark.logger.PySparkLogger.addHandler#

PySparkLogger.addHandler(_handler_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger.addHandler)#
    

Add the specified handler to this logger in structured JSON format.

[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.addHandler.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.info.html

# pyspark.logger.PySparkLogger.info#

PySparkLogger.info(_msg_ , _* args_, _** kwargs_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger.info)#
    

Log âmsg % argsâ with severity âINFOâ in structured JSON format.

Parameters
    

**msg** str
    

The log message.

[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.info.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.warning.html

# pyspark.logger.PySparkLogger.warning#

PySparkLogger.warning(_msg_ , _* args_, _** kwargs_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger.warning)#
    

Log âmsg % argsâ with severity âWARNINGâ in structured JSON format.

Parameters
    

**msg** str
    

The log message.

[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.warning.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.error.html

# pyspark.logger.PySparkLogger.error#

PySparkLogger.error(_msg_ , _* args_, _** kwargs_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger.error)#
    

Log âmsg % argsâ with severity âERRORâ in structured JSON format.

Parameters
    

**msg** str
    

The log message.

[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.error.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.logger.PySparkLogger.exception.html

# pyspark.logger.PySparkLogger.exception#

PySparkLogger.exception(_msg_ , _* args_, _exc_info =True_, _** kwargs_)[[source]](../../_modules/pyspark/logger/logger.html#PySparkLogger.exception)#
    

Convenience method for logging an ERROR with exception information.

Parameters
    

**msg** str
    

The log message.

**exc_info** bool = True
    

If True, exception information is added to the logging message. This includes the exception type, value, and traceback. Default is True.

[ __Show Source](../../_sources/reference/api/pyspark.logger.PySparkLogger.exception.rst.txt)
