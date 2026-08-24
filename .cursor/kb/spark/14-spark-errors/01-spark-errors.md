# 📘 PySpark Pandas Index Reference



---

## 🔹 001. https://spark.apache.org/docs/latest/api/python/reference/pyspark.errors.html#

# Errors#

## Classes#

[`AnalysisException`](api/pyspark.errors.AnalysisException.html#pyspark.errors.AnalysisException "pyspark.errors.AnalysisException")([message,Â errorClass,Â ...]) | Failed to analyze a SQL query plan.  
---|---  
[`ArithmeticException`](api/pyspark.errors.ArithmeticException.html#pyspark.errors.ArithmeticException "pyspark.errors.ArithmeticException")([message,Â errorClass,Â ...]) | Arithmetic exception thrown from Spark with an error class.  
[`ArrayIndexOutOfBoundsException`](api/pyspark.errors.ArrayIndexOutOfBoundsException.html#pyspark.errors.ArrayIndexOutOfBoundsException "pyspark.errors.ArrayIndexOutOfBoundsException")([message,Â ...]) | Array index out of bounds exception thrown from Spark with an error class.  
[`DateTimeException`](api/pyspark.errors.DateTimeException.html#pyspark.errors.DateTimeException "pyspark.errors.DateTimeException")([message,Â errorClass,Â ...]) | Datetime exception thrown from Spark with an error class.  
[`IllegalArgumentException`](api/pyspark.errors.IllegalArgumentException.html#pyspark.errors.IllegalArgumentException "pyspark.errors.IllegalArgumentException")([message,Â ...]) | Passed an illegal or inappropriate argument.  
[`NumberFormatException`](api/pyspark.errors.NumberFormatException.html#pyspark.errors.NumberFormatException "pyspark.errors.NumberFormatException")([message,Â errorClass,Â ...]) | Number format exception thrown from Spark with an error class.  
[`ParseException`](api/pyspark.errors.ParseException.html#pyspark.errors.ParseException "pyspark.errors.ParseException")([message,Â errorClass,Â ...]) | Failed to parse a SQL command.  
[`PySparkAssertionError`](api/pyspark.errors.PySparkAssertionError.html#pyspark.errors.PySparkAssertionError "pyspark.errors.PySparkAssertionError")([message,Â errorClass,Â ...]) | Wrapper class for AssertionError to support error classes.  
[`PySparkAttributeError`](api/pyspark.errors.PySparkAttributeError.html#pyspark.errors.PySparkAttributeError "pyspark.errors.PySparkAttributeError")([message,Â errorClass,Â ...]) | Wrapper class for AttributeError to support error classes.  
[`PySparkException`](api/pyspark.errors.PySparkException.html#pyspark.errors.PySparkException "pyspark.errors.PySparkException")([message,Â errorClass,Â ...]) | Base Exception for handling errors generated from PySpark.  
[`PySparkKeyError`](api/pyspark.errors.PySparkKeyError.html#pyspark.errors.PySparkKeyError "pyspark.errors.PySparkKeyError")([message,Â errorClass,Â ...]) | Wrapper class for KeyError to support error classes.  
[`PySparkNotImplementedError`](api/pyspark.errors.PySparkNotImplementedError.html#pyspark.errors.PySparkNotImplementedError "pyspark.errors.PySparkNotImplementedError")([message,Â ...]) | Wrapper class for NotImplementedError to support error classes.  
[`PySparkPicklingError`](api/pyspark.errors.PySparkPicklingError.html#pyspark.errors.PySparkPicklingError "pyspark.errors.PySparkPicklingError")([message,Â errorClass,Â ...]) | Wrapper class for pickle.PicklingError to support error classes.  
[`PySparkRuntimeError`](api/pyspark.errors.PySparkRuntimeError.html#pyspark.errors.PySparkRuntimeError "pyspark.errors.PySparkRuntimeError")([message,Â errorClass,Â ...]) | Wrapper class for RuntimeError to support error classes.  
[`PySparkTypeError`](api/pyspark.errors.PySparkTypeError.html#pyspark.errors.PySparkTypeError "pyspark.errors.PySparkTypeError")([message,Â errorClass,Â ...]) | Wrapper class for TypeError to support error classes.  
[`PySparkValueError`](api/pyspark.errors.PySparkValueError.html#pyspark.errors.PySparkValueError "pyspark.errors.PySparkValueError")([message,Â errorClass,Â ...]) | Wrapper class for ValueError to support error classes.  
[`PySparkImportError`](api/pyspark.errors.PySparkImportError.html#pyspark.errors.PySparkImportError "pyspark.errors.PySparkImportError")([message,Â errorClass,Â ...]) | Wrapper class for ImportError to support error classes.  
[`PySparkIndexError`](api/pyspark.errors.PySparkIndexError.html#pyspark.errors.PySparkIndexError "pyspark.errors.PySparkIndexError")([message,Â errorClass,Â ...]) | Wrapper class for IndexError to support error classes.  
[`PythonException`](api/pyspark.errors.PythonException.html#pyspark.errors.PythonException "pyspark.errors.PythonException")([message,Â errorClass,Â ...]) | Exceptions thrown from Python workers.  
[`QueryContext`](api/pyspark.errors.QueryContext.html#pyspark.errors.QueryContext "pyspark.errors.QueryContext")() | Query context of a [`PySparkException`](api/pyspark.errors.PySparkException.html#pyspark.errors.PySparkException "pyspark.errors.PySparkException").  
[`QueryContextType`](api/pyspark.errors.QueryContextType.html#pyspark.errors.QueryContextType "pyspark.errors.QueryContextType")(value) | The type of [`QueryContext`](api/pyspark.errors.QueryContext.html#pyspark.errors.QueryContext "pyspark.errors.QueryContext").  
[`QueryExecutionException`](api/pyspark.errors.QueryExecutionException.html#pyspark.errors.QueryExecutionException "pyspark.errors.QueryExecutionException")([message,Â ...]) | Failed to execute a query.  
[`RetriesExceeded`](api/pyspark.errors.RetriesExceeded.html#pyspark.errors.RetriesExceeded "pyspark.errors.RetriesExceeded")([message,Â errorClass,Â ...]) | Represents an exception which is considered retriable, but retry limits were exceeded  
[`SessionNotSameException`](api/pyspark.errors.SessionNotSameException.html#pyspark.errors.SessionNotSameException "pyspark.errors.SessionNotSameException")([message,Â ...]) | Performed the same operation on different SparkSession.  
[`SparkRuntimeException`](api/pyspark.errors.SparkRuntimeException.html#pyspark.errors.SparkRuntimeException "pyspark.errors.SparkRuntimeException")([message,Â errorClass,Â ...]) | Runtime exception thrown from Spark with an error class.  
[`SparkUpgradeException`](api/pyspark.errors.SparkUpgradeException.html#pyspark.errors.SparkUpgradeException "pyspark.errors.SparkUpgradeException")([message,Â errorClass,Â ...]) | Exception thrown because of Spark upgrade.  
[`SparkNoSuchElementException`](api/pyspark.errors.SparkNoSuchElementException.html#pyspark.errors.SparkNoSuchElementException "pyspark.errors.SparkNoSuchElementException")([message,Â ...]) | Exception thrown for java.util.NoSuchElementException.  
[`StreamingQueryException`](api/pyspark.errors.StreamingQueryException.html#pyspark.errors.StreamingQueryException "pyspark.errors.StreamingQueryException")([message,Â ...]) | Exception that stopped a `StreamingQuery`.  
[`StreamingPythonRunnerInitializationException`](api/pyspark.errors.StreamingPythonRunnerInitializationException.html#pyspark.errors.StreamingPythonRunnerInitializationException "pyspark.errors.StreamingPythonRunnerInitializationException")([...]) | Failed to initialize a streaming Python runner.  
[`TempTableAlreadyExistsException`](api/pyspark.errors.TempTableAlreadyExistsException.html#pyspark.errors.TempTableAlreadyExistsException "pyspark.errors.TempTableAlreadyExistsException")([message,Â ...]) | Failed to create temp view since it is already exists.  
[`UnknownException`](api/pyspark.errors.UnknownException.html#pyspark.errors.UnknownException "pyspark.errors.UnknownException")([message,Â errorClass,Â ...]) | None of the other exceptions.  
[`UnsupportedOperationException`](api/pyspark.errors.UnsupportedOperationException.html#pyspark.errors.UnsupportedOperationException "pyspark.errors.UnsupportedOperationException")([message,Â ...]) | Unsupported operation exception thrown from Spark with an error class.  
[`PickleException`](api/pyspark.errors.PickleException.html#pyspark.errors.PickleException "pyspark.errors.PickleException")([message,Â errorClass,Â ...]) | Represents an exception which is failed while pickling from server side such as net.razorvine.pickle.PickleException.  
  
## Methods#

[`PySparkException.getCondition`](api/pyspark.errors.PySparkException.getCondition.html#pyspark.errors.PySparkException.getCondition "pyspark.errors.PySparkException.getCondition")() | Returns an error condition.  
---|---  
[`PySparkException.getErrorClass`](api/pyspark.errors.PySparkException.getErrorClass.html#pyspark.errors.PySparkException.getErrorClass "pyspark.errors.PySparkException.getErrorClass")() | Returns an error class as a string.  
[`PySparkException.getMessage`](api/pyspark.errors.PySparkException.getMessage.html#pyspark.errors.PySparkException.getMessage "pyspark.errors.PySparkException.getMessage")() | Returns full error message.  
[`PySparkException.getMessageParameters`](api/pyspark.errors.PySparkException.getMessageParameters.html#pyspark.errors.PySparkException.getMessageParameters "pyspark.errors.PySparkException.getMessageParameters")() | Returns a message parameters as a dictionary.  
[`PySparkException.getQueryContext`](api/pyspark.errors.PySparkException.getQueryContext.html#pyspark.errors.PySparkException.getQueryContext "pyspark.errors.PySparkException.getQueryContext")() | Returns [`QueryContext`](api/pyspark.errors.QueryContext.html#pyspark.errors.QueryContext "pyspark.errors.QueryContext").  
[`PySparkException.getSqlState`](api/pyspark.errors.PySparkException.getSqlState.html#pyspark.errors.PySparkException.getSqlState "pyspark.errors.PySparkException.getSqlState")() | Returns an SQLSTATE as a string.  
  
__On this page

[ __Show Source](../_sources/reference/pyspark.errors.rst.txt)


---

## 🔹 002. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.AnalysisException.html

# pyspark.errors.AnalysisException#

_exception _pyspark.errors.AnalysisException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#AnalysisException)#
    

Failed to analyze a SQL query plan.

[ __Show Source](../../_sources/reference/api/pyspark.errors.AnalysisException.rst.txt)


---

## 🔹 003. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.ArithmeticException.html

# pyspark.errors.ArithmeticException#

_exception _pyspark.errors.ArithmeticException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#ArithmeticException)#
    

Arithmetic exception thrown from Spark with an error class.

[ __Show Source](../../_sources/reference/api/pyspark.errors.ArithmeticException.rst.txt)


---

## 🔹 004. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.ArrayIndexOutOfBoundsException.html

# pyspark.errors.ArrayIndexOutOfBoundsException#

_exception _pyspark.errors.ArrayIndexOutOfBoundsException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#ArrayIndexOutOfBoundsException)#
    

Array index out of bounds exception thrown from Spark with an error class.

[ __Show Source](../../_sources/reference/api/pyspark.errors.ArrayIndexOutOfBoundsException.rst.txt)


---

## 🔹 005. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.DateTimeException.html

# pyspark.errors.DateTimeException#

_exception _pyspark.errors.DateTimeException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#DateTimeException)#
    

Datetime exception thrown from Spark with an error class.

[ __Show Source](../../_sources/reference/api/pyspark.errors.DateTimeException.rst.txt)


---

## 🔹 006. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.IllegalArgumentException.html

# pyspark.errors.IllegalArgumentException#

_exception _pyspark.errors.IllegalArgumentException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#IllegalArgumentException)#
    

Passed an illegal or inappropriate argument.

[ __Show Source](../../_sources/reference/api/pyspark.errors.IllegalArgumentException.rst.txt)


---

## 🔹 007. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.NumberFormatException.html

# pyspark.errors.NumberFormatException#

_exception _pyspark.errors.NumberFormatException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#NumberFormatException)#
    

Number format exception thrown from Spark with an error class.

[ __Show Source](../../_sources/reference/api/pyspark.errors.NumberFormatException.rst.txt)


---

## 🔹 008. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.ParseException.html

# pyspark.errors.ParseException#

_exception _pyspark.errors.ParseException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#ParseException)#
    

Failed to parse a SQL command.

[ __Show Source](../../_sources/reference/api/pyspark.errors.ParseException.rst.txt)


---

## 🔹 009. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkAssertionError.html

# pyspark.errors.PySparkAssertionError#

_exception _pyspark.errors.PySparkAssertionError(_message =None_, _errorClass =None_, _messageParameters =None_, _data =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkAssertionError)#
    

Wrapper class for AssertionError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkAssertionError.rst.txt)


---

## 🔹 010. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkAttributeError.html

# pyspark.errors.PySparkAttributeError#

_exception _pyspark.errors.PySparkAttributeError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkAttributeError)#
    

Wrapper class for AttributeError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkAttributeError.rst.txt)


---

## 🔹 011. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.html

# pyspark.errors.PySparkException#

_exception _pyspark.errors.PySparkException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException)#
    

Base Exception for handling errors generated from PySpark.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.rst.txt)


---

## 🔹 012. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkKeyError.html

# pyspark.errors.PySparkKeyError#

_exception _pyspark.errors.PySparkKeyError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkKeyError)#
    

Wrapper class for KeyError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkKeyError.rst.txt)


---

## 🔹 013. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkNotImplementedError.html

# pyspark.errors.PySparkNotImplementedError#

_exception _pyspark.errors.PySparkNotImplementedError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkNotImplementedError)#
    

Wrapper class for NotImplementedError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkNotImplementedError.rst.txt)


---

## 🔹 014. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkPicklingError.html

# pyspark.errors.PySparkPicklingError#

_exception _pyspark.errors.PySparkPicklingError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkPicklingError)#
    

Wrapper class for pickle.PicklingError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkPicklingError.rst.txt)


---

## 🔹 015. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkRuntimeError.html

# pyspark.errors.PySparkRuntimeError#

_exception _pyspark.errors.PySparkRuntimeError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkRuntimeError)#
    

Wrapper class for RuntimeError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkRuntimeError.rst.txt)


---

## 🔹 016. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkTypeError.html

# pyspark.errors.PySparkTypeError#

_exception _pyspark.errors.PySparkTypeError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkTypeError)#
    

Wrapper class for TypeError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkTypeError.rst.txt)


---

## 🔹 017. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkValueError.html

# pyspark.errors.PySparkValueError#

_exception _pyspark.errors.PySparkValueError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkValueError)#
    

Wrapper class for ValueError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkValueError.rst.txt)


---

## 🔹 018. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkImportError.html

# pyspark.errors.PySparkImportError#

_exception _pyspark.errors.PySparkImportError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkImportError)#
    

Wrapper class for ImportError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkImportError.rst.txt)


---

## 🔹 019. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkIndexError.html

# pyspark.errors.PySparkIndexError#

_exception _pyspark.errors.PySparkIndexError(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkIndexError)#
    

Wrapper class for IndexError to support error classes.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkIndexError.rst.txt)


---

## 🔹 020. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PythonException.html

# pyspark.errors.PythonException#

_exception _pyspark.errors.PythonException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PythonException)#
    

Exceptions thrown from Python workers.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PythonException.rst.txt)


---

## 🔹 021. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.QueryContext.html

# pyspark.errors.QueryContext#

_class _pyspark.errors.QueryContext[[source]](../../_modules/pyspark/errors/exceptions/base.html#QueryContext)#
    

Query context of a [`PySparkException`](pyspark.errors.PySparkException.html#pyspark.errors.PySparkException "pyspark.errors.PySparkException"). It helps users understand where error occur while executing queries.

New in version 4.0.0.

Methods

`callSite`() | The user code (call site of the API) that caused throwing the exception.  
---|---  
`contextType`() | The type of this query context.  
`fragment`() | The corresponding fragment of the query which throws the exception.  
`objectName`() | The object name of the query which throws the exception.  
`objectType`() | The object type of the query which throws the exception.  
`startIndex`() | The starting index in the query text which throws the exception.  
`stopIndex`() | The stopping index in the query which throws the exception.  
`summary`() | Summary of the exception cause.  
  
[ __Show Source](../../_sources/reference/api/pyspark.errors.QueryContext.rst.txt)


---

## 🔹 022. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.QueryContextType.html

# pyspark.errors.QueryContextType#

_class _pyspark.errors.QueryContextType(_value_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#QueryContextType)#
    

The type of [`QueryContext`](pyspark.errors.QueryContext.html#pyspark.errors.QueryContext "pyspark.errors.QueryContext").

New in version 4.0.0.

Attributes

`SQL` |   
---|---  
`DataFrame` |   
  
[ __Show Source](../../_sources/reference/api/pyspark.errors.QueryContextType.rst.txt)


---

## 🔹 023. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.QueryExecutionException.html

# pyspark.errors.QueryExecutionException#

_exception _pyspark.errors.QueryExecutionException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#QueryExecutionException)#
    

Failed to execute a query.

[ __Show Source](../../_sources/reference/api/pyspark.errors.QueryExecutionException.rst.txt)


---

## 🔹 024. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.RetriesExceeded.html

# pyspark.errors.RetriesExceeded#

_exception _pyspark.errors.RetriesExceeded(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#RetriesExceeded)#
    

Represents an exception which is considered retriable, but retry limits were exceeded

[ __Show Source](../../_sources/reference/api/pyspark.errors.RetriesExceeded.rst.txt)


---

## 🔹 025. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.SessionNotSameException.html

# pyspark.errors.SessionNotSameException#

_exception _pyspark.errors.SessionNotSameException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#SessionNotSameException)#
    

Performed the same operation on different SparkSession.

[ __Show Source](../../_sources/reference/api/pyspark.errors.SessionNotSameException.rst.txt)


---

## 🔹 026. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.SparkRuntimeException.html

# pyspark.errors.SparkRuntimeException#

_exception _pyspark.errors.SparkRuntimeException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#SparkRuntimeException)#
    

Runtime exception thrown from Spark with an error class.

[ __Show Source](../../_sources/reference/api/pyspark.errors.SparkRuntimeException.rst.txt)


---

## 🔹 027. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.SparkUpgradeException.html

# pyspark.errors.SparkUpgradeException#

_exception _pyspark.errors.SparkUpgradeException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#SparkUpgradeException)#
    

Exception thrown because of Spark upgrade.

[ __Show Source](../../_sources/reference/api/pyspark.errors.SparkUpgradeException.rst.txt)


---

## 🔹 028. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.SparkNoSuchElementException.html

# pyspark.errors.SparkNoSuchElementException#

_exception _pyspark.errors.SparkNoSuchElementException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#SparkNoSuchElementException)#
    

Exception thrown for java.util.NoSuchElementException.

[ __Show Source](../../_sources/reference/api/pyspark.errors.SparkNoSuchElementException.rst.txt)


---

## 🔹 029. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.StreamingQueryException.html

# pyspark.errors.StreamingQueryException#

_exception _pyspark.errors.StreamingQueryException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#StreamingQueryException)#
    

Exception that stopped a `StreamingQuery`.

[ __Show Source](../../_sources/reference/api/pyspark.errors.StreamingQueryException.rst.txt)


---

## 🔹 030. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.StreamingPythonRunnerInitializationException.html

# pyspark.errors.StreamingPythonRunnerInitializationException#

_exception _pyspark.errors.StreamingPythonRunnerInitializationException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#StreamingPythonRunnerInitializationException)#
    

Failed to initialize a streaming Python runner.

[ __Show Source](../../_sources/reference/api/pyspark.errors.StreamingPythonRunnerInitializationException.rst.txt)


---

## 🔹 031. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.TempTableAlreadyExistsException.html

# pyspark.errors.TempTableAlreadyExistsException#

_exception _pyspark.errors.TempTableAlreadyExistsException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#TempTableAlreadyExistsException)#
    

Failed to create temp view since it is already exists.

[ __Show Source](../../_sources/reference/api/pyspark.errors.TempTableAlreadyExistsException.rst.txt)


---

## 🔹 032. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.UnknownException.html

# pyspark.errors.UnknownException#

_exception _pyspark.errors.UnknownException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#UnknownException)#
    

None of the other exceptions.

[ __Show Source](../../_sources/reference/api/pyspark.errors.UnknownException.rst.txt)


---

## 🔹 033. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.UnsupportedOperationException.html

# pyspark.errors.UnsupportedOperationException#

_exception _pyspark.errors.UnsupportedOperationException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#UnsupportedOperationException)#
    

Unsupported operation exception thrown from Spark with an error class.

[ __Show Source](../../_sources/reference/api/pyspark.errors.UnsupportedOperationException.rst.txt)


---

## 🔹 034. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PickleException.html

# pyspark.errors.PickleException#

_exception _pyspark.errors.PickleException(_message =None_, _errorClass =None_, _messageParameters =None_, _contexts =None_)[[source]](../../_modules/pyspark/errors/exceptions/base.html#PickleException)#
    

Represents an exception which is failed while pickling from server side such as net.razorvine.pickle.PickleException. This is different from PySparkPicklingError which represents an exception failed from Python built-in pickle.PicklingError.

[ __Show Source](../../_sources/reference/api/pyspark.errors.PickleException.rst.txt)


---

## 🔹 035. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.getCondition.html

# pyspark.errors.PySparkException.getCondition#

PySparkException.getCondition()[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException.getCondition)#
    

Returns an error condition.

New in version 4.0.0.

See also

[`PySparkException.getMessage()`](pyspark.errors.PySparkException.getMessage.html#pyspark.errors.PySparkException.getMessage "pyspark.errors.PySparkException.getMessage")
    
[`PySparkException.getMessageParameters()`](pyspark.errors.PySparkException.getMessageParameters.html#pyspark.errors.PySparkException.getMessageParameters "pyspark.errors.PySparkException.getMessageParameters")
    
[`PySparkException.getQueryContext()`](pyspark.errors.PySparkException.getQueryContext.html#pyspark.errors.PySparkException.getQueryContext "pyspark.errors.PySparkException.getQueryContext")
    
[`PySparkException.getSqlState()`](pyspark.errors.PySparkException.getSqlState.html#pyspark.errors.PySparkException.getSqlState "pyspark.errors.PySparkException.getSqlState")
    

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.getCondition.rst.txt)


---

## 🔹 036. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.getErrorClass.html

# pyspark.errors.PySparkException.getErrorClass#

PySparkException.getErrorClass()[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException.getErrorClass)#
    

Returns an error class as a string.

New in version 3.4.0.

Deprecated since version 4.0.0.

See also

[`PySparkException.getMessage()`](pyspark.errors.PySparkException.getMessage.html#pyspark.errors.PySparkException.getMessage "pyspark.errors.PySparkException.getMessage")
    
[`PySparkException.getMessageParameters()`](pyspark.errors.PySparkException.getMessageParameters.html#pyspark.errors.PySparkException.getMessageParameters "pyspark.errors.PySparkException.getMessageParameters")
    
[`PySparkException.getQueryContext()`](pyspark.errors.PySparkException.getQueryContext.html#pyspark.errors.PySparkException.getQueryContext "pyspark.errors.PySparkException.getQueryContext")
    
[`PySparkException.getSqlState()`](pyspark.errors.PySparkException.getSqlState.html#pyspark.errors.PySparkException.getSqlState "pyspark.errors.PySparkException.getSqlState")
    

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.getErrorClass.rst.txt)


---

## 🔹 037. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.getMessage.html

# pyspark.errors.PySparkException.getMessage#

PySparkException.getMessage()[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException.getMessage)#
    

Returns full error message.

New in version 4.0.0.

See also

[`PySparkException.getCondition()`](pyspark.errors.PySparkException.getCondition.html#pyspark.errors.PySparkException.getCondition "pyspark.errors.PySparkException.getCondition")
    
[`PySparkException.getMessageParameters()`](pyspark.errors.PySparkException.getMessageParameters.html#pyspark.errors.PySparkException.getMessageParameters "pyspark.errors.PySparkException.getMessageParameters")
    
[`PySparkException.getQueryContext()`](pyspark.errors.PySparkException.getQueryContext.html#pyspark.errors.PySparkException.getQueryContext "pyspark.errors.PySparkException.getQueryContext")
    
[`PySparkException.getSqlState()`](pyspark.errors.PySparkException.getSqlState.html#pyspark.errors.PySparkException.getSqlState "pyspark.errors.PySparkException.getSqlState")
    

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.getMessage.rst.txt)


---

## 🔹 038. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.getMessageParameters.html

# pyspark.errors.PySparkException.getMessageParameters#

PySparkException.getMessageParameters()[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException.getMessageParameters)#
    

Returns a message parameters as a dictionary.

New in version 3.4.0.

See also

[`PySparkException.getCondition()`](pyspark.errors.PySparkException.getCondition.html#pyspark.errors.PySparkException.getCondition "pyspark.errors.PySparkException.getCondition")
    
[`PySparkException.getMessage()`](pyspark.errors.PySparkException.getMessage.html#pyspark.errors.PySparkException.getMessage "pyspark.errors.PySparkException.getMessage")
    
[`PySparkException.getQueryContext()`](pyspark.errors.PySparkException.getQueryContext.html#pyspark.errors.PySparkException.getQueryContext "pyspark.errors.PySparkException.getQueryContext")
    
[`PySparkException.getSqlState()`](pyspark.errors.PySparkException.getSqlState.html#pyspark.errors.PySparkException.getSqlState "pyspark.errors.PySparkException.getSqlState")
    

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.getMessageParameters.rst.txt)


---

## 🔹 039. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.getQueryContext.html

# pyspark.errors.PySparkException.getQueryContext#

PySparkException.getQueryContext()[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException.getQueryContext)#
    

Returns [`QueryContext`](pyspark.errors.QueryContext.html#pyspark.errors.QueryContext "pyspark.errors.QueryContext").

New in version 4.0.0.

See also

[`PySparkException.getCondition()`](pyspark.errors.PySparkException.getCondition.html#pyspark.errors.PySparkException.getCondition "pyspark.errors.PySparkException.getCondition")
    
[`PySparkException.getMessageParameters()`](pyspark.errors.PySparkException.getMessageParameters.html#pyspark.errors.PySparkException.getMessageParameters "pyspark.errors.PySparkException.getMessageParameters")
    
[`PySparkException.getMessage()`](pyspark.errors.PySparkException.getMessage.html#pyspark.errors.PySparkException.getMessage "pyspark.errors.PySparkException.getMessage")
    
[`PySparkException.getSqlState()`](pyspark.errors.PySparkException.getSqlState.html#pyspark.errors.PySparkException.getSqlState "pyspark.errors.PySparkException.getSqlState")
    

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.getQueryContext.rst.txt)


---

## 🔹 040. https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.errors.PySparkException.getSqlState.html

# pyspark.errors.PySparkException.getSqlState#

PySparkException.getSqlState()[[source]](../../_modules/pyspark/errors/exceptions/base.html#PySparkException.getSqlState)#
    

Returns an SQLSTATE as a string.

Errors generated in Python have no SQLSTATE, so it always returns None.

New in version 3.4.0.

See also

[`PySparkException.getCondition()`](pyspark.errors.PySparkException.getCondition.html#pyspark.errors.PySparkException.getCondition "pyspark.errors.PySparkException.getCondition")
    
[`PySparkException.getMessage()`](pyspark.errors.PySparkException.getMessage.html#pyspark.errors.PySparkException.getMessage "pyspark.errors.PySparkException.getMessage")
    
[`PySparkException.getMessageParameters()`](pyspark.errors.PySparkException.getMessageParameters.html#pyspark.errors.PySparkException.getMessageParameters "pyspark.errors.PySparkException.getMessageParameters")
    
[`PySparkException.getQueryContext()`](pyspark.errors.PySparkException.getQueryContext.html#pyspark.errors.PySparkException.getQueryContext "pyspark.errors.PySparkException.getQueryContext")
    

[ __Show Source](../../_sources/reference/api/pyspark.errors.PySparkException.getSqlState.rst.txt)
