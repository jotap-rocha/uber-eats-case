# Functions — PySpark 4.0.1 documentation
A collections of builtin functions available for DataFrame operations.

Note

From Apache Spark 3.5.0, all functions support Spark Connect.

Normal Functions[#](#normal-functions "Permalink to this headline")
-------------------------------------------------------------------


|broadcast(df)                 |Marks a DataFrame as small enough for use in broadcast joins.  |
|------------------------------|---------------------------------------------------------------|
|call_function(funcName, *cols)|Call a SQL function.                                           |
|col(col)                      |Returns a Column based on the given column name.               |
|column(col)                   |Returns a Column based on the given column name.               |
|lit(col)                      |Creates a Column of literal value.                             |
|expr(str)                     |Parses the expression string into the column that it represents|


Conditional Functions[#](#conditional-functions "Permalink to this headline")
-----------------------------------------------------------------------------



* coalesce(*cols): ifnull(col1, col2)
  * Returns the first column that is not null.: Returns col2 if col1 is null, or col1 otherwise.
* coalesce(*cols): nanvl(col1, col2)
  * Returns the first column that is not null.: Returns col1 if it is not NaN, or col2 if col1 is NaN.
* coalesce(*cols): nullif(col1, col2)
  * Returns the first column that is not null.: Returns null if col1 equals to col2, or col1 otherwise.
* coalesce(*cols): nullifzero(col)
  * Returns the first column that is not null.: Returns null if col is equal to zero, or col otherwise.
* coalesce(*cols): nvl(col1, col2)
  * Returns the first column that is not null.: Returns col2 if col1 is null, or col1 otherwise.
* coalesce(*cols): nvl2(col1, col2, col3)
  * Returns the first column that is not null.: Returns col2 if col1 is not null, or col3 otherwise.
* coalesce(*cols): when(condition, value)
  * Returns the first column that is not null.: Evaluates a list of conditions and returns one of multiple possible result expressions.
* coalesce(*cols): zeroifnull(col)
  * Returns the first column that is not null.: Returns zero if col is null, or col otherwise.


Predicate Functions[#](#predicate-functions "Permalink to this headline")
-------------------------------------------------------------------------



* equal_null(col1, col2): ilike(str, pattern[, escapeChar])
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: Returns true if str matches pattern with escape case-insensitively, null if any arguments are null, false otherwise.
* equal_null(col1, col2): isnan(col)
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: An expression that returns true if the column is NaN.
* equal_null(col1, col2): isnotnull(col)
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: Returns true if col is not null, or false otherwise.
* equal_null(col1, col2): isnull(col)
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: An expression that returns true if the column is null.
* equal_null(col1, col2): like(str, pattern[, escapeChar])
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: Returns true if str matches pattern with escape, null if any arguments are null, false otherwise.
* equal_null(col1, col2): regexp(str, regexp)
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: Returns true if str matches the Java regex regexp, or false otherwise.
* equal_null(col1, col2): regexp_like(str, regexp)
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: Returns true if str matches the Java regex regexp, or false otherwise.
* equal_null(col1, col2): rlike(str, regexp)
  * Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.: Returns true if str matches the Java regex regexp, or false otherwise.


Sort Functions[#](#sort-functions "Permalink to this headline")
---------------------------------------------------------------



* asc(col): asc_nulls_first(col)
  * Returns a sort expression for the target column in ascending order.: Sort Function: Returns a sort expression based on the ascending order of the given column name, and null values return before non-null values.
* asc(col): asc_nulls_last(col)
  * Returns a sort expression for the target column in ascending order.: Sort Function: Returns a sort expression based on the ascending order of the given column name, and null values appear after non-null values.
* asc(col): desc(col)
  * Returns a sort expression for the target column in ascending order.: Returns a sort expression for the target column in descending order.
* asc(col): desc_nulls_first(col)
  * Returns a sort expression for the target column in ascending order.: Sort Function: Returns a sort expression based on the descending order of the given column name, and null values appear before non-null values.
* asc(col): desc_nulls_last(col)
  * Returns a sort expression for the target column in ascending order.: Sort Function: Returns a sort expression based on the descending order of the given column name, and null values appear after non-null values.


Mathematical Functions[#](#mathematical-functions "Permalink to this headline")
-------------------------------------------------------------------------------



* abs(col): acos(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Mathematical Function: Computes the inverse cosine (also known as arccosine) of the given column or expression.
* abs(col): acosh(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Mathematical Function: Computes the inverse hyperbolic cosine (also known as arcosh) of the given column or expression.
* abs(col): asin(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes inverse sine of the input column.
* abs(col): asinh(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes inverse hyperbolic sine of the input column.
* abs(col): atan(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Compute inverse tangent of the input column.
* abs(col): atan2(col1, col2)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Compute the angle in radians between the positive x-axis of a plane and the point given by the coordinates
* abs(col): atanh(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes inverse hyperbolic tangent of the input column.
* abs(col): bin(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the string representation of the binary value of the given column.
* abs(col): bround(col[, scale])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Round the given value to scale decimal places using HALF_EVEN rounding mode if scale >= 0 or at integral part when scale < 0.
* abs(col): cbrt(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the cube-root of the given value.
* abs(col): ceil(col[, scale])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the ceiling of the given value.
* abs(col): ceiling(col[, scale])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the ceiling of the given value.
* abs(col): conv(col, fromBase, toBase)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Convert a number in a string column from one base to another.
* abs(col): cos(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes cosine of the input column.
* abs(col): cosh(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes hyperbolic cosine of the input column.
* abs(col): cot(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes cotangent of the input column.
* abs(col): csc(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes cosecant of the input column.
* abs(col): degrees(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Converts an angle measured in radians to an approximately equivalent angle measured in degrees.
* abs(col): e()
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns Euler's number.
* abs(col): exp(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the exponential of the given value.
* abs(col): expm1(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the exponential of the given value minus one.
* abs(col): factorial(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the factorial of the given value.
* abs(col): floor(col[, scale])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the floor of the given value.
* abs(col): greatest(*cols)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the greatest value of the list of column names, skipping null values.
* abs(col): hex(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes hex value of the given column, which could be pyspark.sql.types.StringType, pyspark.sql.types.BinaryType, pyspark.sql.types.IntegerType or pyspark.sql.types.LongType.
* abs(col): hypot(col1, col2)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes sqrt(a^2 + b^2) without intermediate overflow or underflow.
* abs(col): least(*cols)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the least value of the list of column names, skipping null values.
* abs(col): ln(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the natural logarithm of the argument.
* abs(col): log(arg1[, arg2])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the first argument-based logarithm of the second argument.
* abs(col): log10(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the logarithm of the given value in Base 10.
* abs(col): log1p(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the natural logarithm of the given value plus one.
* abs(col): log2(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the base-2 logarithm of the argument.
* abs(col): negate(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the negative value.
* abs(col): negative(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the negative value.
* abs(col): pi()
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns Pi.
* abs(col): pmod(dividend, divisor)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the positive value of dividend mod divisor.
* abs(col): positive(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the value.
* abs(col): pow(col1, col2)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the value of the first argument raised to the power of the second argument.
* abs(col): power(col1, col2)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the value of the first argument raised to the power of the second argument.
* abs(col): radians(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Converts an angle measured in degrees to an approximately equivalent angle measured in radians.
* abs(col): rand([seed])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Generates a random column with independent and identically distributed (i.i.d.) samples uniformly distributed in [0.0, 1.0).
* abs(col): randn([seed])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Generates a random column with independent and identically distributed (i.i.d.) samples from the standard normal distribution.
* abs(col): rint(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the double value that is closest in value to the argument and is equal to a mathematical integer.
* abs(col): round(col[, scale])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Round the given value to scale decimal places using HALF_UP rounding mode if scale >= 0 or at integral part when scale < 0.
* abs(col): sec(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes secant of the input column.
* abs(col): sign(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the signum of the given value.
* abs(col): signum(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the signum of the given value.
* abs(col): sin(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes sine of the input column.
* abs(col): sinh(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes hyperbolic sine of the input column.
* abs(col): sqrt(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes the square root of the specified float value.
* abs(col): tan(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes tangent of the input column.
* abs(col): tanh(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Computes hyperbolic tangent of the input column.
* abs(col): try_add(left, right)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the sum of left`and `right and the result is null on overflow.
* abs(col): try_divide(left, right)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns dividend/divisor.
* abs(col): try_mod(left, right)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the remainder after dividend/divisor.
* abs(col): try_multiply(left, right)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns left`*`right and the result is null on overflow.
* abs(col): try_subtract(left, right)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns left-right and the result is null on overflow.
* abs(col): unhex(col)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Inverse of hex.
* abs(col): uniform(min, max[, seed])
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns a random value with independent and identically distributed (i.i.d.) values with the specified range of numbers.
* abs(col): width_bucket(v, min, max, numBucket)
  * Mathematical Function: Computes the absolute value of the given column or expression.: Returns the bucket number into which the value of this expression would fall after being evaluated.


String Functions[#](#string-functions "Permalink to this headline")
-------------------------------------------------------------------



* ascii(col): base64(col)
  * Computes the numeric value of the first character of the string column.: Computes the BASE64 encoding of a binary column and returns it as a string column.
* ascii(col): bit_length(col)
  * Computes the numeric value of the first character of the string column.: Calculates the bit length for the specified string column.
* ascii(col): btrim(str[, trim])
  * Computes the numeric value of the first character of the string column.: Remove the leading and trailing trim characters from str.
* ascii(col): char(col)
  * Computes the numeric value of the first character of the string column.: Returns the ASCII character having the binary equivalent to col.
* ascii(col): char_length(str)
  * Computes the numeric value of the first character of the string column.: Returns the character length of string data or number of bytes of binary data.
* ascii(col): character_length(str)
  * Computes the numeric value of the first character of the string column.: Returns the character length of string data or number of bytes of binary data.
* ascii(col): collate(col, collation)
  * Computes the numeric value of the first character of the string column.: Marks a given column with specified collation.
* ascii(col): collation(col)
  * Computes the numeric value of the first character of the string column.: Returns the collation name of a given column.
* ascii(col): concat_ws(sep, *cols)
  * Computes the numeric value of the first character of the string column.: Concatenates multiple input string columns together into a single string column, using the given separator.
* ascii(col): contains(left, right)
  * Computes the numeric value of the first character of the string column.: Returns a boolean.
* ascii(col): decode(col, charset)
  * Computes the numeric value of the first character of the string column.: Computes the first argument into a string from a binary using the provided character set (one of 'US-ASCII', 'ISO-8859-1', 'UTF-8', 'UTF-16BE', 'UTF-16LE', 'UTF-16', 'UTF-32').
* ascii(col): elt(*inputs)
  * Computes the numeric value of the first character of the string column.: Returns the n-th input, e.g., returns input2 when n is 2.
* ascii(col): encode(col, charset)
  * Computes the numeric value of the first character of the string column.: Computes the first argument into a binary from a string using the provided character set (one of 'US-ASCII', 'ISO-8859-1', 'UTF-8', 'UTF-16BE', 'UTF-16LE', 'UTF-16', 'UTF-32').
* ascii(col): endswith(str, suffix)
  * Computes the numeric value of the first character of the string column.: Returns a boolean.
* ascii(col): find_in_set(str, str_array)
  * Computes the numeric value of the first character of the string column.: Returns the index (1-based) of the given string (str) in the comma-delimited list (strArray).
* ascii(col): format_number(col, d)
  * Computes the numeric value of the first character of the string column.: Formats the number X to a format like '#,--#,--#.--', rounded to d decimal places with HALF_EVEN round mode, and returns the result as a string.
* ascii(col): format_string(format, *cols)
  * Computes the numeric value of the first character of the string column.: Formats the arguments in printf-style and returns the result as a string column.
* ascii(col): initcap(col)
  * Computes the numeric value of the first character of the string column.: Translate the first letter of each word to upper case in the sentence.
* ascii(col): instr(str, substr)
  * Computes the numeric value of the first character of the string column.: Locate the position of the first occurrence of substr column in the given string.
* ascii(col): is_valid_utf8(str)
  * Computes the numeric value of the first character of the string column.: Returns true if the input is a valid UTF-8 string, otherwise returns false.
* ascii(col): lcase(str)
  * Computes the numeric value of the first character of the string column.: Returns str with all characters changed to lowercase.
* ascii(col): left(str, len)
  * Computes the numeric value of the first character of the string column.: Returns the leftmost len`(`len can be string type) characters from the string str, if len is less or equal than 0 the result is an empty string.
* ascii(col): length(col)
  * Computes the numeric value of the first character of the string column.: Computes the character length of string data or number of bytes of binary data.
* ascii(col): levenshtein(left, right[, threshold])
  * Computes the numeric value of the first character of the string column.: Computes the Levenshtein distance of the two given strings.
* ascii(col): locate(substr, str[, pos])
  * Computes the numeric value of the first character of the string column.: Locate the position of the first occurrence of substr in a string column, after position pos.
* ascii(col): lower(col)
  * Computes the numeric value of the first character of the string column.: Converts a string expression to lower case.
* ascii(col): lpad(col, len, pad)
  * Computes the numeric value of the first character of the string column.: Left-pad the string column to width len with pad.
* ascii(col): ltrim(col[, trim])
  * Computes the numeric value of the first character of the string column.: Trim the spaces from left end for the specified string value.
* ascii(col): make_valid_utf8(str)
  * Computes the numeric value of the first character of the string column.: Returns a new string in which all invalid UTF-8 byte sequences, if any, are replaced by the Unicode replacement character (U+FFFD).
* ascii(col): mask(col[, upperChar, lowerChar, digitChar, ...])
  * Computes the numeric value of the first character of the string column.: Masks the given string value.
* ascii(col): octet_length(col)
  * Computes the numeric value of the first character of the string column.: Calculates the byte length for the specified string column.
* ascii(col): overlay(src, replace, pos[, len])
  * Computes the numeric value of the first character of the string column.: Overlay the specified portion of src with replace, starting from byte position pos of src and proceeding for len bytes.
* ascii(col): position(substr, str[, start])
  * Computes the numeric value of the first character of the string column.: Returns the position of the first occurrence of substr in str after position start.
* ascii(col): printf(format, *cols)
  * Computes the numeric value of the first character of the string column.: Formats the arguments in printf-style and returns the result as a string column.
* ascii(col): randstr(length[, seed])
  * Computes the numeric value of the first character of the string column.: Returns a string of the specified length whose characters are chosen uniformly at random from the following pool of characters: 0-9, a-z, A-Z.
* ascii(col): regexp_count(str, regexp)
  * Computes the numeric value of the first character of the string column.: Returns a count of the number of times that the Java regex pattern regexp is matched in the string str.
* ascii(col): regexp_extract(str, pattern, idx)
  * Computes the numeric value of the first character of the string column.: Extract a specific group matched by the Java regex regexp, from the specified string column.
* ascii(col): regexp_extract_all(str, regexp[, idx])
  * Computes the numeric value of the first character of the string column.: Extract all strings in the str that match the Java regex regexp and corresponding to the regex group index.
* ascii(col): regexp_instr(str, regexp[, idx])
  * Computes the numeric value of the first character of the string column.: Returns the position of the first substring in the str that match the Java regex regexp and corresponding to the regex group index.
* ascii(col): regexp_replace(string, pattern, replacement)
  * Computes the numeric value of the first character of the string column.: Replace all substrings of the specified string value that match regexp with replacement.
* ascii(col): regexp_substr(str, regexp)
  * Computes the numeric value of the first character of the string column.: Returns the first substring that matches the Java regex regexp within the string str.
* ascii(col): repeat(col, n)
  * Computes the numeric value of the first character of the string column.: Repeats a string column n times, and returns it as a new string column.
* ascii(col): replace(src, search[, replace])
  * Computes the numeric value of the first character of the string column.: Replaces all occurrences of search with replace.
* ascii(col): right(str, len)
  * Computes the numeric value of the first character of the string column.: Returns the rightmost len`(`len can be string type) characters from the string str, if len is less or equal than 0 the result is an empty string.
* ascii(col): rpad(col, len, pad)
  * Computes the numeric value of the first character of the string column.: Right-pad the string column to width len with pad.
* ascii(col): rtrim(col[, trim])
  * Computes the numeric value of the first character of the string column.: Trim the spaces from right end for the specified string value.
* ascii(col): sentences(string[, language, country])
  * Computes the numeric value of the first character of the string column.: Splits a string into arrays of sentences, where each sentence is an array of words.
* ascii(col): soundex(col)
  * Computes the numeric value of the first character of the string column.: Returns the SoundEx encoding for a string
* ascii(col): split(str, pattern[, limit])
  * Computes the numeric value of the first character of the string column.: Splits str around matches of the given pattern.
* ascii(col): split_part(src, delimiter, partNum)
  * Computes the numeric value of the first character of the string column.: Splits str by delimiter and return requested part of the split (1-based).
* ascii(col): startswith(str, prefix)
  * Computes the numeric value of the first character of the string column.: Returns a boolean.
* ascii(col): substr(str, pos[, len])
  * Computes the numeric value of the first character of the string column.: Returns the substring of str that starts at pos and is of length len, or the slice of byte array that starts at pos and is of length len.
* ascii(col): substring(str, pos, len)
  * Computes the numeric value of the first character of the string column.: Substring starts at pos and is of length len when str is String type or returns the slice of byte array that starts at pos in byte and is of length len when str is Binary type.
* ascii(col): substring_index(str, delim, count)
  * Computes the numeric value of the first character of the string column.: Returns the substring from string str before count occurrences of the delimiter delim.
* ascii(col): to_binary(col[, format])
  * Computes the numeric value of the first character of the string column.: Converts the input col to a binary value based on the supplied format.
* ascii(col): to_char(col, format)
  * Computes the numeric value of the first character of the string column.: Convert col to a string based on the format.
* ascii(col): to_number(col, format)
  * Computes the numeric value of the first character of the string column.: Convert string 'col' to a number based on the string format 'format'.
* ascii(col): to_varchar(col, format)
  * Computes the numeric value of the first character of the string column.: Convert col to a string based on the format.
* ascii(col): translate(srcCol, matching, replace)
  * Computes the numeric value of the first character of the string column.: A function translate any character in the srcCol by a character in matching.
* ascii(col): trim(col[, trim])
  * Computes the numeric value of the first character of the string column.: Trim the spaces from both ends for the specified string column.
* ascii(col): try_to_binary(col[, format])
  * Computes the numeric value of the first character of the string column.: This is a special version of to_binary that performs the same operation, but returns a NULL value instead of raising an error if the conversion cannot be performed.
* ascii(col): try_to_number(col, format)
  * Computes the numeric value of the first character of the string column.: Convert string 'col' to a number based on the string format format.
* ascii(col): try_validate_utf8(str)
  * Computes the numeric value of the first character of the string column.: Returns the input value if it corresponds to a valid UTF-8 string, or NULL otherwise.
* ascii(col): ucase(str)
  * Computes the numeric value of the first character of the string column.: Returns str with all characters changed to uppercase.
* ascii(col): unbase64(col)
  * Computes the numeric value of the first character of the string column.: Decodes a BASE64 encoded string column and returns it as a binary column.
* ascii(col): upper(col)
  * Computes the numeric value of the first character of the string column.: Converts a string expression to upper case.
* ascii(col): validate_utf8(str)
  * Computes the numeric value of the first character of the string column.: Returns the input value if it corresponds to a valid UTF-8 string, or emits an error otherwise.


Bitwise Functions[#](#bitwise-functions "Permalink to this headline")
---------------------------------------------------------------------



* bit_count(col): bit_get(col, pos)
  * Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.: Returns the value of the bit (0 or 1) at the specified position.
* bit_count(col): bitwise_not(col)
  * Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.: Computes bitwise not.
* bit_count(col): getbit(col, pos)
  * Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.: Returns the value of the bit (0 or 1) at the specified position.
* bit_count(col): shiftleft(col, numBits)
  * Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.: Shift the given value numBits left.
* bit_count(col): shiftright(col, numBits)
  * Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.: (Signed) shift the given value numBits right.
* bit_count(col): shiftrightunsigned(col, numBits)
  * Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.: Unsigned shift the given value numBits right.


Date and Timestamp Functions[#](#date-and-timestamp-functions "Permalink to this headline")
-------------------------------------------------------------------------------------------



* add_months(start, months): convert_timezone(sourceTz, targetTz, sourceTs)
  * Returns the date that is months months after start.: Converts the timestamp without time zone sourceTs from the sourceTz time zone to targetTz.
* add_months(start, months): curdate()
  * Returns the date that is months months after start.: Returns the current date at the start of query evaluation as a DateType column.
* add_months(start, months): current_date()
  * Returns the date that is months months after start.: Returns the current date at the start of query evaluation as a DateType column.
* add_months(start, months): current_timestamp()
  * Returns the date that is months months after start.: Returns the current timestamp at the start of query evaluation as a TimestampType column.
* add_months(start, months): current_timezone()
  * Returns the date that is months months after start.: Returns the current session local timezone.
* add_months(start, months): date_add(start, days)
  * Returns the date that is months months after start.: Returns the date that is days days after start.
* add_months(start, months): date_diff(end, start)
  * Returns the date that is months months after start.: Returns the number of days from start to end.
* add_months(start, months): date_format(date, format)
  * Returns the date that is months months after start.: Converts a date/timestamp/string to a value of string in the format specified by the date format given by the second argument.
* add_months(start, months): date_from_unix_date(days)
  * Returns the date that is months months after start.: Create date from the number of days since 1970-01-01.
* add_months(start, months): date_part(field, source)
  * Returns the date that is months months after start.: Extracts a part of the date/timestamp or interval source.
* add_months(start, months): date_sub(start, days)
  * Returns the date that is months months after start.: Returns the date that is days days before start.
* add_months(start, months): date_trunc(format, timestamp)
  * Returns the date that is months months after start.: Returns timestamp truncated to the unit specified by the format.
* add_months(start, months): dateadd(start, days)
  * Returns the date that is months months after start.: Returns the date that is days days after start.
* add_months(start, months): datediff(end, start)
  * Returns the date that is months months after start.: Returns the number of days from start to end.
* add_months(start, months): datepart(field, source)
  * Returns the date that is months months after start.: Extracts a part of the date/timestamp or interval source.
* add_months(start, months): day(col)
  * Returns the date that is months months after start.: Extract the day of the month of a given date/timestamp as integer.
* add_months(start, months): dayname(col)
  * Returns the date that is months months after start.: Date and Timestamp Function: Returns the three-letter abbreviated day name from the given date.
* add_months(start, months): dayofmonth(col)
  * Returns the date that is months months after start.: Extract the day of the month of a given date/timestamp as integer.
* add_months(start, months): dayofweek(col)
  * Returns the date that is months months after start.: Extract the day of the week of a given date/timestamp as integer.
* add_months(start, months): dayofyear(col)
  * Returns the date that is months months after start.: Extract the day of the year of a given date/timestamp as integer.
* add_months(start, months): extract(field, source)
  * Returns the date that is months months after start.: Extracts a part of the date/timestamp or interval source.
* add_months(start, months): from_unixtime(timestamp[, format])
  * Returns the date that is months months after start.: Converts the number of seconds from unix epoch (1970-01-01 00:00:00 UTC) to a string representing the timestamp of that moment in the current system time zone in the given format.
* add_months(start, months): from_utc_timestamp(timestamp, tz)
  * Returns the date that is months months after start.: This is a common function for databases supporting TIMESTAMP WITHOUT TIMEZONE.
* add_months(start, months): hour(col)
  * Returns the date that is months months after start.: Extract the hours of a given timestamp as integer.
* add_months(start, months): last_day(date)
  * Returns the date that is months months after start.: Returns the last day of the month which the given date belongs to.
* add_months(start, months): localtimestamp()
  * Returns the date that is months months after start.: Returns the current timestamp without time zone at the start of query evaluation as a timestamp without time zone column.
* add_months(start, months): make_date(year, month, day)
  * Returns the date that is months months after start.: Returns a column with a date built from the year, month and day columns.
* add_months(start, months): make_dt_interval([days, hours, mins, secs])
  * Returns the date that is months months after start.: Make DayTimeIntervalType duration from days, hours, mins and secs.
* add_months(start, months): make_interval([years, months, weeks, days, ...])
  * Returns the date that is months months after start.: Make interval from years, months, weeks, days, hours, mins and secs.
* add_months(start, months): make_timestamp(years, months, days, hours, ...)
  * Returns the date that is months months after start.: Create timestamp from years, months, days, hours, mins, secs and timezone fields.
* add_months(start, months): make_timestamp_ltz(years, months, days, ...)
  * Returns the date that is months months after start.: Create the current timestamp with local time zone from years, months, days, hours, mins, secs and timezone fields.
* add_months(start, months): make_timestamp_ntz(years, months, days, ...)
  * Returns the date that is months months after start.: Create local date-time from years, months, days, hours, mins, secs fields.
* add_months(start, months): make_ym_interval([years, months])
  * Returns the date that is months months after start.: Make year-month interval from years, months.
* add_months(start, months): minute(col)
  * Returns the date that is months months after start.: Extract the minutes of a given timestamp as integer.
* add_months(start, months): month(col)
  * Returns the date that is months months after start.: Extract the month of a given date/timestamp as integer.
* add_months(start, months): monthname(col)
  * Returns the date that is months months after start.: Returns the three-letter abbreviated month name from the given date.
* add_months(start, months): months_between(date1, date2[, roundOff])
  * Returns the date that is months months after start.: Returns number of months between dates date1 and date2.
* add_months(start, months): next_day(date, dayOfWeek)
  * Returns the date that is months months after start.: Returns the first date which is later than the value of the date column based on second week day argument.
* add_months(start, months): now()
  * Returns the date that is months months after start.: Returns the current timestamp at the start of query evaluation.
* add_months(start, months): quarter(col)
  * Returns the date that is months months after start.: Extract the quarter of a given date/timestamp as integer.
* add_months(start, months): second(col)
  * Returns the date that is months months after start.: Extract the seconds of a given date as integer.
* add_months(start, months): session_window(timeColumn, gapDuration)
  * Returns the date that is months months after start.: Generates session window given a timestamp specifying column.
* add_months(start, months): timestamp_add(unit, quantity, ts)
  * Returns the date that is months months after start.: Gets the difference between the timestamps in the specified units by truncating the fraction part.
* add_months(start, months): timestamp_diff(unit, start, end)
  * Returns the date that is months months after start.: Gets the difference between the timestamps in the specified units by truncating the fraction part.
* add_months(start, months): timestamp_micros(col)
  * Returns the date that is months months after start.: Creates timestamp from the number of microseconds since UTC epoch.
* add_months(start, months): timestamp_millis(col)
  * Returns the date that is months months after start.: Creates timestamp from the number of milliseconds since UTC epoch.
* add_months(start, months): timestamp_seconds(col)
  * Returns the date that is months months after start.: Converts the number of seconds from the Unix epoch (1970-01-01T00:00:00Z) to a timestamp.
* add_months(start, months): to_date(col[, format])
  * Returns the date that is months months after start.: Converts a Column into pyspark.sql.types.DateType using the optionally specified format.
* add_months(start, months): to_timestamp(col[, format])
  * Returns the date that is months months after start.: Converts a Column into pyspark.sql.types.TimestampType using the optionally specified format.
* add_months(start, months): to_timestamp_ltz(timestamp[, format])
  * Returns the date that is months months after start.: Parses the timestamp with the format to a timestamp with time zone.
* add_months(start, months): to_timestamp_ntz(timestamp[, format])
  * Returns the date that is months months after start.: Parses the timestamp with the format to a timestamp without time zone.
* add_months(start, months): to_unix_timestamp(timestamp[, format])
  * Returns the date that is months months after start.: Returns the UNIX timestamp of the given time.
* add_months(start, months): to_utc_timestamp(timestamp, tz)
  * Returns the date that is months months after start.: This is a common function for databases supporting TIMESTAMP WITHOUT TIMEZONE.
* add_months(start, months): trunc(date, format)
  * Returns the date that is months months after start.: Returns date truncated to the unit specified by the format.
* add_months(start, months): try_make_interval([years, months, weeks, ...])
  * Returns the date that is months months after start.: This is a special version of make_interval that performs the same operation, but returns a NULL value instead of raising an error if interval cannot be created.
* add_months(start, months): try_make_timestamp(years, months, days, ...)
  * Returns the date that is months months after start.: Try to create timestamp from years, months, days, hours, mins, secs and timezone fields.
* add_months(start, months): try_make_timestamp_ltz(years, months, days, ...)
  * Returns the date that is months months after start.: Try to create the current timestamp with local time zone from years, months, days, hours, mins, secs and timezone fields.
* add_months(start, months): try_make_timestamp_ntz(years, months, days, ...)
  * Returns the date that is months months after start.: Try to create local date-time from years, months, days, hours, mins, secs fields.
* add_months(start, months): try_to_timestamp(col[, format])
  * Returns the date that is months months after start.: Parses the col with the format to a timestamp.
* add_months(start, months): unix_date(col)
  * Returns the date that is months months after start.: Returns the number of days since 1970-01-01.
* add_months(start, months): unix_micros(col)
  * Returns the date that is months months after start.: Returns the number of microseconds since 1970-01-01 00:00:00 UTC.
* add_months(start, months): unix_millis(col)
  * Returns the date that is months months after start.: Returns the number of milliseconds since 1970-01-01 00:00:00 UTC.
* add_months(start, months): unix_seconds(col)
  * Returns the date that is months months after start.: Returns the number of seconds since 1970-01-01 00:00:00 UTC.
* add_months(start, months): unix_timestamp([timestamp, format])
  * Returns the date that is months months after start.: Convert time string with given pattern ('yyyy-MM-dd HH:mm:ss', by default) to Unix time stamp (in seconds), using the default timezone and the default locale, returns null if failed.
* add_months(start, months): weekday(col)
  * Returns the date that is months months after start.: Returns the day of the week for date/timestamp (0 = Monday, 1 = Tuesday, ..., 6 = Sunday).
* add_months(start, months): weekofyear(col)
  * Returns the date that is months months after start.: Extract the week number of a given date as integer.
* add_months(start, months): window(timeColumn, windowDuration[, ...])
  * Returns the date that is months months after start.: Bucketize rows into one or more time windows given a timestamp specifying column.
* add_months(start, months): window_time(windowColumn)
  * Returns the date that is months months after start.: Computes the event time from a window column.
* add_months(start, months): year(col)
  * Returns the date that is months months after start.: Extract the year of a given date/timestamp as integer.


Hash Functions[#](#hash-functions "Permalink to this headline")
---------------------------------------------------------------



* crc32(col): hash(*cols)
  * Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.: Calculates the hash code of given columns, and returns the result as an int column.
* crc32(col): md5(col)
  * Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.: Calculates the MD5 digest and returns the value as a 32 character hex string.
* crc32(col): sha(col)
  * Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.: Returns a sha1 hash value as a hex string of the col.
* crc32(col): sha1(col)
  * Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.: Returns the hex string result of SHA-1.
* crc32(col): sha2(col, numBits)
  * Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.: Returns the hex string result of SHA-2 family of hash functions (SHA-224, SHA-256, SHA-384, and SHA-512).
* crc32(col): xxhash64(*cols)
  * Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.: Calculates the hash code of given columns using the 64-bit variant of the xxHash algorithm, and returns the result as a long column.


Collection Functions[#](#collection-functions "Permalink to this headline")
---------------------------------------------------------------------------



* aggregate(col, initialValue, merge[, finish]): array_sort(col[, comparator])
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: sorts the input array in ascending order.
* aggregate(col, initialValue, merge[, finish]): cardinality(col)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: returns the length of the array or map stored in the column.
* aggregate(col, initialValue, merge[, finish]): concat(*cols)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: Concatenates multiple input columns together into a single column.
* aggregate(col, initialValue, merge[, finish]): element_at(col, extraction)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: (array, index) - Returns element of array at given (1-based) index.
* aggregate(col, initialValue, merge[, finish]): exists(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Returns whether a predicate holds for one or more elements in the array.
* aggregate(col, initialValue, merge[, finish]): filter(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Returns an array of elements for which a predicate holds in a given array.
* aggregate(col, initialValue, merge[, finish]): forall(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Returns whether a predicate holds for every element in the array.
* aggregate(col, initialValue, merge[, finish]): map_filter(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: Returns a new map column whose key-value pairs satisfy a given predicate function.
* aggregate(col, initialValue, merge[, finish]): map_zip_with(col1, col2, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection: Merges two given maps into a single map by applying a function to the key-value pairs.
* aggregate(col, initialValue, merge[, finish]): reduce(col, initialValue, merge[, finish])
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.
* aggregate(col, initialValue, merge[, finish]): reverse(col)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: returns a reversed string or an array with elements in reverse order.
* aggregate(col, initialValue, merge[, finish]): size(col)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: returns the length of the array or map stored in the column.
* aggregate(col, initialValue, merge[, finish]): transform(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Returns an array of elements after applying a transformation to each element in the input array.
* aggregate(col, initialValue, merge[, finish]): transform_keys(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Applies a function to every key-value pair in a map and returns a map with the results of those applications as the new keys for the pairs.
* aggregate(col, initialValue, merge[, finish]): transform_values(col, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Applies a function to every key-value pair in a map and returns a map with the results of those applications as the new values for the pairs.
* aggregate(col, initialValue, merge[, finish]): try_element_at(col, extraction)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Collection function: (array, index) - Returns element of array at given (1-based) index.
* aggregate(col, initialValue, merge[, finish]): zip_with(left, right, f)
  * Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state.: Merge two given arrays, element-wise, into a single array using a function.


Array Functions[#](#array-functions "Permalink to this headline")
-----------------------------------------------------------------



* array(*cols): array_append(col, value)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns a new array column by appending value to the existing array col.
* array(*cols): array_compact(col)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: removes null values from the array.
* array(*cols): array_contains(col, value)
  * Collection function: Creates a new array column from the input columns or column names.: Collection function: This function returns a boolean indicating whether the array contains the given value, returning null if the array is null, true if the array contains the given value, and false otherwise.
* array(*cols): array_distinct(col)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: removes duplicate values from the array.
* array(*cols): array_except(col1, col2)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns a new array containing the elements present in col1 but not in col2, without duplicates.
* array(*cols): array_insert(arr, pos, value)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Inserts an item into a given array at a specified array index.
* array(*cols): array_intersect(col1, col2)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns a new array containing the intersection of elements in col1 and col2, without duplicates.
* array(*cols): array_join(col, delimiter[, null_replacement])
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Returns a string column by concatenating the elements of the input array column using the delimiter.
* array(*cols): array_max(col)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns the maximum value of the array.
* array(*cols): array_min(col)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns the minimum value of the array.
* array(*cols): array_position(col, value)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Locates the position of the first occurrence of the given value in the given array.
* array(*cols): array_prepend(col, value)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Returns an array containing the given element as the first element and the rest of the elements from the original array.
* array(*cols): array_remove(col, element)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Remove all elements that equal to element from the given array.
* array(*cols): array_repeat(col, count)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: creates an array containing a column repeated count times.
* array(*cols): array_size(col)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns the total number of elements in the array.
* array(*cols): array_union(col1, col2)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: returns a new array containing the union of elements in col1 and col2, without duplicates.
* array(*cols): arrays_overlap(a1, a2)
  * Collection function: Creates a new array column from the input columns or column names.: Collection function: This function returns a boolean column indicating if the input arrays have common non-null elements, returning true if they do, null if the arrays do not contain any common elements but are not empty and at least one of them contains a null element, and false otherwise.
* array(*cols): arrays_zip(*cols)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Returns a merged array of structs in which the N-th struct contains all N-th values of input arrays.
* array(*cols): flatten(col)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: creates a single array from an array of arrays.
* array(*cols): get(col, index)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Returns the element of an array at the given (0-based) index.
* array(*cols): sequence(start, stop[, step])
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Generate a sequence of integers from start to stop, incrementing by step.
* array(*cols): shuffle(col[, seed])
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Generates a random permutation of the given array.
* array(*cols): slice(x, start, length)
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Returns a new array column by slicing the input array column from a start index to a specific length.
* array(*cols): sort_array(col[, asc])
  * Collection function: Creates a new array column from the input columns or column names.: Array function: Sorts the input array in ascending or descending order according to the natural ordering of the array elements.


Struct Functions[#](#struct-functions "Permalink to this headline")
-------------------------------------------------------------------


|named_struct(*cols)|Creates a struct with the given field names and values.|
|-------------------|-------------------------------------------------------|
|struct(*cols)      |Creates a new struct column.                           |


Map Functions[#](#map-functions "Permalink to this headline")
-------------------------------------------------------------



* create_map(*cols): map_concat(*cols)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Returns the union of all given maps.
* create_map(*cols): map_contains_key(col, value)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Returns true if the map contains the key.
* create_map(*cols): map_entries(col)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Returns an unordered array of all entries in the given map.
* create_map(*cols): map_from_arrays(col1, col2)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Creates a new map from two arrays.
* create_map(*cols): map_from_entries(col)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Transforms an array of key-value pair entries (structs with two fields) into a map.
* create_map(*cols): map_keys(col)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Returns an unordered array containing the keys of the map.
* create_map(*cols): map_values(col)
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Returns an unordered array containing the values of the map.
* create_map(*cols): str_to_map(text[, pairDelim, keyValueDelim])
  * Map function: Creates a new map column from an even number of input columns or column references.: Map function: Converts a string into a map after splitting the text into key/value pairs using delimiters.


Aggregate Functions[#](#aggregate-functions "Permalink to this headline")
-------------------------------------------------------------------------



* any_value(col[, ignoreNulls]): approx_count_distinct(col[, rsd])
  * Returns some value of col for a group of rows.: This aggregate function returns a new Column, which estimates the approximate distinct count of elements in a specified column or a group of columns.
* any_value(col[, ignoreNulls]): approx_percentile(col, percentage[, accuracy])
  * Returns some value of col for a group of rows.: Returns the approximate percentile of the numeric column col which is the smallest value in the ordered col values (sorted from least to greatest) such that no more than percentage of col values is less than the value or equal to that value.
* any_value(col[, ignoreNulls]): array_agg(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns a list of objects with duplicates.
* any_value(col[, ignoreNulls]): avg(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the average of the values in a group.
* any_value(col[, ignoreNulls]): bit_and(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the bitwise AND of all non-null input values, or null if none.
* any_value(col[, ignoreNulls]): bit_or(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the bitwise OR of all non-null input values, or null if none.
* any_value(col[, ignoreNulls]): bit_xor(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the bitwise XOR of all non-null input values, or null if none.
* any_value(col[, ignoreNulls]): bitmap_construct_agg(col)
  * Returns some value of col for a group of rows.: Returns a bitmap with the positions of the bits set from all the values from the input column.
* any_value(col[, ignoreNulls]): bitmap_or_agg(col)
  * Returns some value of col for a group of rows.: Returns a bitmap that is the bitwise OR of all of the bitmaps from the input column.
* any_value(col[, ignoreNulls]): bool_and(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns true if all values of col are true.
* any_value(col[, ignoreNulls]): bool_or(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns true if at least one value of col is true.
* any_value(col[, ignoreNulls]): collect_list(col)
  * Returns some value of col for a group of rows.: Aggregate function: Collects the values from a column into a list, maintaining duplicates, and returns this list of objects.
* any_value(col[, ignoreNulls]): collect_set(col)
  * Returns some value of col for a group of rows.: Aggregate function: Collects the values from a column into a set, eliminating duplicates, and returns this set of objects.
* any_value(col[, ignoreNulls]): corr(col1, col2)
  * Returns some value of col for a group of rows.: Returns a new Column for the Pearson Correlation Coefficient for col1 and col2.
* any_value(col[, ignoreNulls]): count(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the number of items in a group.
* any_value(col[, ignoreNulls]): count_distinct(col, *cols)
  * Returns some value of col for a group of rows.: Returns a new Column for distinct count of col or cols.
* any_value(col[, ignoreNulls]): count_if(col)
  * Returns some value of col for a group of rows.: Aggregate function: Returns the number of TRUE values for the col.
* any_value(col[, ignoreNulls]): count_min_sketch(col, eps, confidence[, seed])
  * Returns some value of col for a group of rows.: Returns a count-min sketch of a column with the given esp, confidence and seed.
* any_value(col[, ignoreNulls]): covar_pop(col1, col2)
  * Returns some value of col for a group of rows.: Returns a new Column for the population covariance of col1 and col2.
* any_value(col[, ignoreNulls]): covar_samp(col1, col2)
  * Returns some value of col for a group of rows.: Returns a new Column for the sample covariance of col1 and col2.
* any_value(col[, ignoreNulls]): every(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns true if all values of col are true.
* any_value(col[, ignoreNulls]): first(col[, ignorenulls])
  * Returns some value of col for a group of rows.: Aggregate function: returns the first value in a group.
* any_value(col[, ignoreNulls]): first_value(col[, ignoreNulls])
  * Returns some value of col for a group of rows.: Returns the first value of col for a group of rows.
* any_value(col[, ignoreNulls]): grouping(col)
  * Returns some value of col for a group of rows.: Aggregate function: indicates whether a specified column in a GROUP BY list is aggregated or not, returns 1 for aggregated or 0 for not aggregated in the result set.
* any_value(col[, ignoreNulls]): grouping_id(*cols)
  * Returns some value of col for a group of rows.: Aggregate function: returns the level of grouping, equals to
* any_value(col[, ignoreNulls]): histogram_numeric(col, nBins)
  * Returns some value of col for a group of rows.: Computes a histogram on numeric 'col' using nb bins.
* any_value(col[, ignoreNulls]): hll_sketch_agg(col[, lgConfigK])
  * Returns some value of col for a group of rows.: Aggregate function: returns the updatable binary representation of the Datasketches HllSketch configured with lgConfigK arg.
* any_value(col[, ignoreNulls]): hll_union_agg(col[, allowDifferentLgConfigK])
  * Returns some value of col for a group of rows.: Aggregate function: returns the updatable binary representation of the Datasketches HllSketch, generated by merging previously created Datasketches HllSketch instances via a Datasketches Union instance.
* any_value(col[, ignoreNulls]): kurtosis(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the kurtosis of the values in a group.
* any_value(col[, ignoreNulls]): last(col[, ignorenulls])
  * Returns some value of col for a group of rows.: Aggregate function: returns the last value in a group.
* any_value(col[, ignoreNulls]): last_value(col[, ignoreNulls])
  * Returns some value of col for a group of rows.: Returns the last value of col for a group of rows.
* any_value(col[, ignoreNulls]): listagg(col[, delimiter])
  * Returns some value of col for a group of rows.: Aggregate function: returns the concatenation of non-null input values, separated by the delimiter.
* any_value(col[, ignoreNulls]): listagg_distinct(col[, delimiter])
  * Returns some value of col for a group of rows.: Aggregate function: returns the concatenation of distinct non-null input values, separated by the delimiter.
* any_value(col[, ignoreNulls]): max(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the maximum value of the expression in a group.
* any_value(col[, ignoreNulls]): max_by(col, ord)
  * Returns some value of col for a group of rows.: Returns the value from the col parameter that is associated with the maximum value from the ord parameter.
* any_value(col[, ignoreNulls]): mean(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the average of the values in a group.
* any_value(col[, ignoreNulls]): median(col)
  * Returns some value of col for a group of rows.: Returns the median of the values in a group.
* any_value(col[, ignoreNulls]): min(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the minimum value of the expression in a group.
* any_value(col[, ignoreNulls]): min_by(col, ord)
  * Returns some value of col for a group of rows.: Returns the value from the col parameter that is associated with the minimum value from the ord parameter.
* any_value(col[, ignoreNulls]): mode(col[, deterministic])
  * Returns some value of col for a group of rows.: Returns the most frequent value in a group.
* any_value(col[, ignoreNulls]): percentile(col, percentage[, frequency])
  * Returns some value of col for a group of rows.: Returns the exact percentile(s) of numeric column expr at the given percentage(s) with value range in [0.0, 1.0].
* any_value(col[, ignoreNulls]): percentile_approx(col, percentage[, accuracy])
  * Returns some value of col for a group of rows.: Returns the approximate percentile of the numeric column col which is the smallest value in the ordered col values (sorted from least to greatest) such that no more than percentage of col values is less than the value or equal to that value.
* any_value(col[, ignoreNulls]): product(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the product of the values in a group.
* any_value(col[, ignoreNulls]): regr_avgx(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns the average of the independent variable for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_avgy(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns the average of the dependent variable for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_count(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns the number of non-null number pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_intercept(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns the intercept of the univariate linear regression line for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_r2(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns the coefficient of determination for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_slope(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns the slope of the linear regression line for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_sxx(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns REGR_COUNT(y, x) * VAR_POP(x) for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_sxy(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns REGR_COUNT(y, x) * COVAR_POP(y, x) for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): regr_syy(y, x)
  * Returns some value of col for a group of rows.: Aggregate function: returns REGR_COUNT(y, x) * VAR_POP(y) for non-null pairs in a group, where y is the dependent variable and x is the independent variable.
* any_value(col[, ignoreNulls]): skewness(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the skewness of the values in a group.
* any_value(col[, ignoreNulls]): some(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns true if at least one value of col is true.
* any_value(col[, ignoreNulls]): std(col)
  * Returns some value of col for a group of rows.: Aggregate function: alias for stddev_samp.
* any_value(col[, ignoreNulls]): stddev(col)
  * Returns some value of col for a group of rows.: Aggregate function: alias for stddev_samp.
* any_value(col[, ignoreNulls]): stddev_pop(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns population standard deviation of the expression in a group.
* any_value(col[, ignoreNulls]): stddev_samp(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the unbiased sample standard deviation of the expression in a group.
* any_value(col[, ignoreNulls]): string_agg(col[, delimiter])
  * Returns some value of col for a group of rows.: Aggregate function: returns the concatenation of non-null input values, separated by the delimiter.
* any_value(col[, ignoreNulls]): string_agg_distinct(col[, delimiter])
  * Returns some value of col for a group of rows.: Aggregate function: returns the concatenation of distinct non-null input values, separated by the delimiter.
* any_value(col[, ignoreNulls]): sum(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the sum of all values in the expression.
* any_value(col[, ignoreNulls]): sum_distinct(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the sum of distinct values in the expression.
* any_value(col[, ignoreNulls]): try_avg(col)
  * Returns some value of col for a group of rows.: Returns the mean calculated from values of a group and the result is null on overflow.
* any_value(col[, ignoreNulls]): try_sum(col)
  * Returns some value of col for a group of rows.: Returns the sum calculated from values of a group and the result is null on overflow.
* any_value(col[, ignoreNulls]): var_pop(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the population variance of the values in a group.
* any_value(col[, ignoreNulls]): var_samp(col)
  * Returns some value of col for a group of rows.: Aggregate function: returns the unbiased sample variance of the values in a group.
* any_value(col[, ignoreNulls]): variance(col)
  * Returns some value of col for a group of rows.: Aggregate function: alias for var_samp


Window Functions[#](#window-functions "Permalink to this headline")
-------------------------------------------------------------------



* cume_dist(): dense_rank()
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the rank of rows within a window partition, without any gaps.
* cume_dist(): lag(col[, offset, default])
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the value that is offset rows before the current row, and default if there is less than offset rows before the current row.
* cume_dist(): lead(col[, offset, default])
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the value that is offset rows after the current row, and default if there is less than offset rows after the current row.
* cume_dist(): nth_value(col, offset[, ignoreNulls])
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the value that is the offsetth row of the window frame (counting from 1), and null if the size of window frame is less than offset rows.
* cume_dist(): ntile(n)
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the ntile group id (from 1 to n inclusive) in an ordered window partition.
* cume_dist(): percent_rank()
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the relative rank (i.e.
* cume_dist(): rank()
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns the rank of rows within a window partition.
* cume_dist(): row_number()
  * Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.: Window function: returns a sequential number starting at 1 within a window partition.


Generator Functions[#](#generator-functions "Permalink to this headline")
-------------------------------------------------------------------------



* explode(col): explode_outer(col)
  * Returns a new row for each element in the given array or map.: Returns a new row for each element in the given array or map.
* explode(col): inline(col)
  * Returns a new row for each element in the given array or map.: Explodes an array of structs into a table.
* explode(col): inline_outer(col)
  * Returns a new row for each element in the given array or map.: Explodes an array of structs into a table.
* explode(col): posexplode(col)
  * Returns a new row for each element in the given array or map.: Returns a new row for each element with position in the given array or map.
* explode(col): posexplode_outer(col)
  * Returns a new row for each element in the given array or map.: Returns a new row for each element with position in the given array or map.
* explode(col): stack(*cols)
  * Returns a new row for each element in the given array or map.: Separates col1, ..., colk into n rows.


Partition Transformation Functions[#](#partition-transformation-functions "Permalink to this headline")
-------------------------------------------------------------------------------------------------------



* partitioning.years(col): partitioning.months(col)
  * Partition transform function: A transform for timestamps and dates to partition data into years.: Partition transform function: A transform for timestamps and dates to partition data into months.
* partitioning.years(col): partitioning.days(col)
  * Partition transform function: A transform for timestamps and dates to partition data into years.: Partition transform function: A transform for timestamps and dates to partition data into days.
* partitioning.years(col): partitioning.hours(col)
  * Partition transform function: A transform for timestamps and dates to partition data into years.: Partition transform function: A transform for timestamps to partition data into hours.
* partitioning.years(col): partitioning.bucket(numBuckets, col)
  * Partition transform function: A transform for timestamps and dates to partition data into years.: Partition transform function: A transform for any type that partitions by a hash of the input column.


CSV Functions[#](#csv-functions "Permalink to this headline")
-------------------------------------------------------------



* from_csv(col, schema[, options]): schema_of_csv(csv[, options])
  * CSV Function: Parses a column containing a CSV string into a row with the specified schema.: CSV Function: Parses a CSV string and infers its schema in DDL format.
* from_csv(col, schema[, options]): to_csv(col[, options])
  * CSV Function: Parses a column containing a CSV string into a row with the specified schema.: CSV Function: Converts a column containing a StructType into a CSV string.


JSON Functions[#](#json-functions "Permalink to this headline")
---------------------------------------------------------------



* from_json(col, schema[, options]): get_json_object(col, path)
  * Parses a column containing a JSON string into a MapType with StringType as keys type, StructType or ArrayType with the specified schema.: Extracts json object from a json string based on json path specified, and returns json string of the extracted json object.
* from_json(col, schema[, options]): json_array_length(col)
  * Parses a column containing a JSON string into a MapType with StringType as keys type, StructType or ArrayType with the specified schema.: Returns the number of elements in the outermost JSON array.
* from_json(col, schema[, options]): json_object_keys(col)
  * Parses a column containing a JSON string into a MapType with StringType as keys type, StructType or ArrayType with the specified schema.: Returns all the keys of the outermost JSON object as an array.
* from_json(col, schema[, options]): json_tuple(col, *fields)
  * Parses a column containing a JSON string into a MapType with StringType as keys type, StructType or ArrayType with the specified schema.: Creates a new row for a json column according to the given field names.
* from_json(col, schema[, options]): schema_of_json(json[, options])
  * Parses a column containing a JSON string into a MapType with StringType as keys type, StructType or ArrayType with the specified schema.: Parses a JSON string and infers its schema in DDL format.
* from_json(col, schema[, options]): to_json(col[, options])
  * Parses a column containing a JSON string into a MapType with StringType as keys type, StructType or ArrayType with the specified schema.: Converts a column containing a StructType, ArrayType or a MapType into a JSON string.


VARIANT Functions[#](#variant-functions "Permalink to this headline")
---------------------------------------------------------------------



* is_variant_null(v): parse_json(col)
  * Check if a variant value is a variant null.: Parses a column containing a JSON string into a VariantType.
* is_variant_null(v): schema_of_variant(v)
  * Check if a variant value is a variant null.: Returns schema in the SQL format of a variant.
* is_variant_null(v): schema_of_variant_agg(v)
  * Check if a variant value is a variant null.: Returns the merged schema in the SQL format of a variant column.
* is_variant_null(v): try_variant_get(v, path, targetType)
  * Check if a variant value is a variant null.: Extracts a sub-variant from v according to path, and then cast the sub-variant to targetType.
* is_variant_null(v): variant_get(v, path, targetType)
  * Check if a variant value is a variant null.: Extracts a sub-variant from v according to path, and then cast the sub-variant to targetType.
* is_variant_null(v): try_parse_json(col)
  * Check if a variant value is a variant null.: Parses a column containing a JSON string into a VariantType.
* is_variant_null(v): to_variant_object(col)
  * Check if a variant value is a variant null.: Converts a column containing nested inputs (array/map/struct) into a variants where maps and structs are converted to variant objects which are unordered unlike SQL structs.


XML Functions[#](#xml-functions "Permalink to this headline")
-------------------------------------------------------------



* from_xml(col, schema[, options]): schema_of_xml(xml[, options])
  * Parses a column containing a XML string to a row with the specified schema.: Parses a XML string and infers its schema in DDL format.
* from_xml(col, schema[, options]): to_xml(col[, options])
  * Parses a column containing a XML string to a row with the specified schema.: Converts a column containing a StructType into a XML string.
* from_xml(col, schema[, options]): xpath(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns a string array of values within the nodes of xml that match the XPath expression.
* from_xml(col, schema[, options]): xpath_boolean(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns true if the XPath expression evaluates to true, or if a matching node is found.
* from_xml(col, schema[, options]): xpath_double(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns a double value, the value zero if no match is found, or NaN if a match is found but the value is non-numeric.
* from_xml(col, schema[, options]): xpath_float(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns a float value, the value zero if no match is found, or NaN if a match is found but the value is non-numeric.
* from_xml(col, schema[, options]): xpath_int(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns an integer value, or the value zero if no match is found, or a match is found but the value is non-numeric.
* from_xml(col, schema[, options]): xpath_long(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns a long integer value, or the value zero if no match is found, or a match is found but the value is non-numeric.
* from_xml(col, schema[, options]): xpath_number(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns a double value, the value zero if no match is found, or NaN if a match is found but the value is non-numeric.
* from_xml(col, schema[, options]): xpath_short(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns a short integer value, or the value zero if no match is found, or a match is found but the value is non-numeric.
* from_xml(col, schema[, options]): xpath_string(xml, path)
  * Parses a column containing a XML string to a row with the specified schema.: Returns the text contents of the first xml node that matches the XPath expression.


URL Functions[#](#url-functions "Permalink to this headline")
-------------------------------------------------------------



* parse_url(url, partToExtract[, key]): try_parse_url(url, partToExtract[, key])
  * URL function: Extracts a specified part from a URL.: This is a special version of parse_url that performs the same operation, but returns a NULL value instead of raising an error if the parsing cannot be performed.
* parse_url(url, partToExtract[, key]): url_decode(str)
  * URL function: Extracts a specified part from a URL.: URL function: Decodes a URL-encoded string in 'application/x-www-form-urlencoded' format to its original format.
* parse_url(url, partToExtract[, key]): url_encode(str)
  * URL function: Extracts a specified part from a URL.: URL function: Encodes a string into a URL-encoded string in 'application/x-www-form-urlencoded' format.
* parse_url(url, partToExtract[, key]): try_url_decode(str)
  * URL function: Extracts a specified part from a URL.: This is a special version of url_decode that performs the same operation, but returns a NULL value instead of raising an error if the decoding cannot be performed.


Misc Functions[#](#misc-functions "Permalink to this headline")
---------------------------------------------------------------



* aes_decrypt(input, key[, mode, padding, aad]): aes_encrypt(input, key[, mode, padding, iv, aad])
  * Returns a decrypted value of input using AES in mode with padding.: Returns an encrypted value of input using AES in given mode with the specified padding.
* aes_decrypt(input, key[, mode, padding, aad]): assert_true(col[, errMsg])
  * Returns a decrypted value of input using AES in mode with padding.: Returns null if the input column is true; throws an exception with the provided error message otherwise.
* aes_decrypt(input, key[, mode, padding, aad]): bitmap_bit_position(col)
  * Returns a decrypted value of input using AES in mode with padding.: Returns the bit position for the given input column.
* aes_decrypt(input, key[, mode, padding, aad]): bitmap_bucket_number(col)
  * Returns a decrypted value of input using AES in mode with padding.: Returns the bucket number for the given input column.
* aes_decrypt(input, key[, mode, padding, aad]): bitmap_count(col)
  * Returns a decrypted value of input using AES in mode with padding.: Returns the number of set bits in the input bitmap.
* aes_decrypt(input, key[, mode, padding, aad]): current_catalog()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the current catalog.
* aes_decrypt(input, key[, mode, padding, aad]): current_database()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the current database.
* aes_decrypt(input, key[, mode, padding, aad]): current_schema()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the current database.
* aes_decrypt(input, key[, mode, padding, aad]): current_user()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the current database.
* aes_decrypt(input, key[, mode, padding, aad]): hll_sketch_estimate(col)
  * Returns a decrypted value of input using AES in mode with padding.: Returns the estimated number of unique values given the binary representation of a Datasketches HllSketch.
* aes_decrypt(input, key[, mode, padding, aad]): hll_union(col1, col2[, allowDifferentLgConfigK])
  * Returns a decrypted value of input using AES in mode with padding.: Merges two binary representations of Datasketches HllSketch objects, using a Datasketches Union object.
* aes_decrypt(input, key[, mode, padding, aad]): input_file_block_length()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the length of the block being read, or -1 if not available.
* aes_decrypt(input, key[, mode, padding, aad]): input_file_block_start()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the start offset of the block being read, or -1 if not available.
* aes_decrypt(input, key[, mode, padding, aad]): input_file_name()
  * Returns a decrypted value of input using AES in mode with padding.: Creates a string column for the file name of the current Spark task.
* aes_decrypt(input, key[, mode, padding, aad]): java_method(*cols)
  * Returns a decrypted value of input using AES in mode with padding.: Calls a method with reflection.
* aes_decrypt(input, key[, mode, padding, aad]): monotonically_increasing_id()
  * Returns a decrypted value of input using AES in mode with padding.: A column that generates monotonically increasing 64-bit integers.
* aes_decrypt(input, key[, mode, padding, aad]): raise_error(errMsg)
  * Returns a decrypted value of input using AES in mode with padding.: Throws an exception with the provided error message.
* aes_decrypt(input, key[, mode, padding, aad]): reflect(*cols)
  * Returns a decrypted value of input using AES in mode with padding.: Calls a method with reflection.
* aes_decrypt(input, key[, mode, padding, aad]): session_user()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the user name of current execution context.
* aes_decrypt(input, key[, mode, padding, aad]): spark_partition_id()
  * Returns a decrypted value of input using AES in mode with padding.: A column for partition ID.
* aes_decrypt(input, key[, mode, padding, aad]): try_aes_decrypt(input, key[, mode, padding, aad])
  * Returns a decrypted value of input using AES in mode with padding.: This is a special version of aes_decrypt that performs the same operation, but returns a NULL value instead of raising an error if the decryption cannot be performed.
* aes_decrypt(input, key[, mode, padding, aad]): try_reflect(*cols)
  * Returns a decrypted value of input using AES in mode with padding.: This is a special version of reflect that performs the same operation, but returns a NULL value instead of raising an error if the invoke method thrown exception.
* aes_decrypt(input, key[, mode, padding, aad]): typeof(col)
  * Returns a decrypted value of input using AES in mode with padding.: Return DDL-formatted type string for the data type of the input.
* aes_decrypt(input, key[, mode, padding, aad]): user()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the current database.
* aes_decrypt(input, key[, mode, padding, aad]): version()
  * Returns a decrypted value of input using AES in mode with padding.: Returns the Spark version.


UDF, UDTF and UDT[#](#udf-udtf-and-udt "Permalink to this headline")
--------------------------------------------------------------------


|call_udf(udfName, *cols)                 |Call a user-defined function.                        |
|-----------------------------------------|-----------------------------------------------------|
|pandas_udf([f, returnType, functionType])|Creates a pandas user defined function (a.k.a.       |
|udf([f, returnType, useArrow])           |Creates a user defined function (UDF).               |
|udtf([cls, returnType, useArrow])        |Creates a user defined table function (UDTF).        |
|unwrap_udt(col)                          |Unwrap UDT data type column into its underlying type.|


Table-Valued Functions[#](#table-valued-functions "Permalink to this headline")
-------------------------------------------------------------------------------



* TableValuedFunction.collations(): TableValuedFunction.explode(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element in the given array or map.
* TableValuedFunction.collations(): TableValuedFunction.explode_outer(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element with position in the given array or map.
* TableValuedFunction.collations(): TableValuedFunction.inline(input)
  * Get all of the Spark SQL string collations.: Explodes an array of structs into a table.
* TableValuedFunction.collations(): TableValuedFunction.inline_outer(input)
  * Get all of the Spark SQL string collations.: Explodes an array of structs into a table.
* TableValuedFunction.collations(): TableValuedFunction.json_tuple(input, *fields)
  * Get all of the Spark SQL string collations.: Creates a new row for a json column according to the given field names.
* TableValuedFunction.collations(): TableValuedFunction.posexplode(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element with position in the given array or map.
* TableValuedFunction.collations(): TableValuedFunction.posexplode_outer(collection)
  * Get all of the Spark SQL string collations.: Returns a DataFrame containing a new row for each element with position in the given array or map.
* TableValuedFunction.collations(): TableValuedFunction.range(start[, end, ...])
  * Get all of the Spark SQL string collations.: Create a DataFrame with single pyspark.sql.types.LongType column named id, containing elements in a range from start to end (exclusive) with step value step.
* TableValuedFunction.collations(): TableValuedFunction.sql_keywords()
  * Get all of the Spark SQL string collations.: Get Spark SQL keywords.
* TableValuedFunction.collations(): TableValuedFunction.stack(n, *fields)
  * Get all of the Spark SQL string collations.: Separates col1, ..., colk into n rows.
* TableValuedFunction.collations(): TableValuedFunction.variant_explode(input)
  * Get all of the Spark SQL string collations.: Separates a variant object/array into multiple rows containing its fields/elements.
* TableValuedFunction.collations(): TableValuedFunction.variant_explode_outer(input)
  * Get all of the Spark SQL string collations.: Separates a variant object/array into multiple rows containing its fields/elements.


# pyspark.sql.functions.broadcast — PySpark 4.0.1 documentation
pyspark.sql.functions.broadcast(_df_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#broadcast)
[#](#pyspark.sql.functions.broadcast "Permalink to this definition")

Marks a DataFrame as small enough for use in broadcast joins.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`DataFrame`](about:blank/pyspark.sql.DataFrame.html#pyspark.sql.DataFrame "pyspark.sql.DataFrame")

DataFrame marked as ready for broadcast join.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([1, 2, 3, 3, 4], "int")
>>> df_small = spark.range(3)
>>> df_b = sf.broadcast(df_small)
>>> df.join(df_b, df.value == df_small.id).show()
+-----+---+
|value| id|
+-----+---+
|    1|  1|
|    2|  2|
+-----+---+

```


# pyspark.sql.functions.call_function — PySpark 4.0.1 documentation
pyspark.sql.functions.call\_function(_funcName_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#call_function)
[#](#pyspark.sql.functions.call_function "Permalink to this definition")

Call a SQL function.

New in version 3.5.0.

Parameters

**funcName**str

function name that follows the SQL identifier syntax (can be quoted, can be qualified)

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")s to be used in the function

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

result of executed function.

Examples

```
>>> from pyspark.sql.functions import call_udf, col
>>> from pyspark.sql.types import IntegerType, StringType
>>> df = spark.createDataFrame([(1, "a"),(2, "b"), (3, "c")],["id", "name"])
>>> _ = spark.udf.register("intX2", lambda i: i * 2, IntegerType())
>>> df.select(call_function("intX2", "id")).show()
+---------+
|intX2(id)|
+---------+
|        2|
|        4|
|        6|
+---------+
>>> _ = spark.udf.register("strX2", lambda s: s * 2, StringType())
>>> df.select(call_function("strX2", col("name"))).show()
+-----------+
|strX2(name)|
+-----------+
|         aa|
|         bb|
|         cc|
+-----------+
>>> df.select(call_function("avg", col("id"))).show()
+-------+
|avg(id)|
+-------+
|    2.0|
+-------+
>>> _ = spark.sql("CREATE FUNCTION custom_avg AS 'test.org.apache.spark.sql.MyDoubleAvg'")
... 
>>> df.select(call_function("custom_avg", col("id"))).show()
... 
+------------------------------------+
|spark_catalog.default.custom_avg(id)|
+------------------------------------+
|                               102.0|
+------------------------------------+
>>> df.select(call_function("spark_catalog.default.custom_avg", col("id"))).show()
... 
+------------------------------------+
|spark_catalog.default.custom_avg(id)|
+------------------------------------+
|                               102.0|
+------------------------------------+

```


# pyspark.sql.functions.col — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.col

pyspark.sql.functions.col(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#col)
[#](#pyspark.sql.functions.col "Permalink to this definition")

Returns a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on the given column name.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**column name

the name for the column

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the corresponding column instance.

Examples

```
>>> col('x')
Column<'x'>
>>> column('x')
Column<'x'>

```

# pyspark.sql.functions.column — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.column

pyspark.sql.functions.column(_col_)
[#](#pyspark.sql.functions.column "Permalink to this definition")

Returns a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") based on the given column name.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**column name

the name for the column

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the corresponding column instance.

Examples

```
>>> col('x')
Column<'x'>
>>> column('x')
Column<'x'>

```



# pyspark.sql.functions.lit — PySpark 4.0.1 documentation
pyspark.sql.functions.lit(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#lit)
[#](#pyspark.sql.functions.lit "Permalink to this definition")

Creates a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") of literal value.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), str, int, float, bool or list, NumPy literals or ndarray.

the value to make it as a PySpark literal. If a column is passed, it returns the column as is.

Changed in version 3.4.0: Since 3.4.0, it supports the list type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the literal instance.

Examples

Example 1: Creating a literal column with an integer value.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(1)
>>> df.select(sf.lit(5).alias('height'), df.id).show()
+------+---+
|height| id|
+------+---+
|     5|  0|
+------+---+

```


Example 2: Creating a literal column from a list.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.lit([1, 2, 3])).show()
+--------------+
|array(1, 2, 3)|
+--------------+
|     [1, 2, 3]|
+--------------+

```


Example 3: Creating a literal column from a string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(1)
>>> df.select(sf.lit("PySpark").alias('framework'), df.id).show()
+---------+---+
|framework| id|
+---------+---+
|  PySpark|  0|
+---------+---+

```


Example 4: Creating a literal column from a boolean value.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(True, "Yes"), (False, "No")], ["flag", "response"])
>>> df.select(sf.lit(False).alias('is_approved'), df.response).show()
+-----------+--------+
|is_approved|response|
+-----------+--------+
|      false|     Yes|
|      false|      No|
+-----------+--------+

```


Example 5: Creating literal columns from Numpy scalar.

```
>>> from pyspark.sql import functions as sf
>>> import numpy as np 
>>> spark.range(1).select(
...     sf.lit(np.bool_(True)),
...     sf.lit(np.int64(123)),
...     sf.lit(np.float64(0.456)),
...     sf.lit(np.str_("xyz"))
... ).show() 
+----+---+-----+---+
|true|123|0.456|xyz|
+----+---+-----+---+
|true|123|0.456|xyz|
+----+---+-----+---+

```


Example 6: Creating literal columns from Numpy ndarray.

```
>>> from pyspark.sql import functions as sf
>>> import numpy as np 
>>> spark.range(1).select(
...     sf.lit(np.array([True, False], np.bool_)),
...     sf.lit(np.array([], np.int8)),
...     sf.lit(np.array([1.5, 0.1], np.float64)),
...     sf.lit(np.array(["a", "b", "c"], np.str_)),
... ).show() 
+------------------+-------+-----------------+--------------------+
|ARRAY(true, false)|ARRAY()|ARRAY(1.5D, 0.1D)|ARRAY('a', 'b', 'c')|
+------------------+-------+-----------------+--------------------+
|     [true, false]|     []|       [1.5, 0.1]|           [a, b, c]|
+------------------+-------+-----------------+--------------------+

```


# pyspark.sql.functions.expr — PySpark 4.0.1 documentation
pyspark.sql.functions.expr(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#expr)
[#](#pyspark.sql.functions.expr "Permalink to this definition")

Parses the expression string into the column that it represents

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**str**expression string

expression defined in string.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

column representing the expression.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([["Alice"], ["Bob"]], ["name"])
>>> df.select("*", sf.expr("length(name)")).show()
+-----+------------+
| name|length(name)|
+-----+------------+
|Alice|           5|
|  Bob|           3|
+-----+------------+

```


# pyspark.sql.functions.coalesce — PySpark 4.0.1 documentation
pyspark.sql.functions.coalesce(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#coalesce)
[#](#pyspark.sql.functions.coalesce "Permalink to this definition")

Returns the first column that is not null.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

list of columns to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value of the first column that is not null.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(None, None), (1, None), (None, 2)], ("a", "b"))
>>> df.show()
+----+----+
|   a|   b|
+----+----+
|NULL|NULL|
|   1|NULL|
|NULL|   2|
+----+----+

```


```
>>> df.select('*', sf.coalesce("a", df["b"])).show()
+----+----+--------------+
|   a|   b|coalesce(a, b)|
+----+----+--------------+
|NULL|NULL|          NULL|
|   1|NULL|             1|
|NULL|   2|             2|
+----+----+--------------+

```


```
>>> df.select('*', sf.coalesce(df["a"], lit(0.0))).show()
+----+----+----------------+
|   a|   b|coalesce(a, 0.0)|
+----+----+----------------+
|NULL|NULL|             0.0|
|   1|NULL|             1.0|
|NULL|   2|             0.0|
+----+----+----------------+

```


# pyspark.sql.functions.ifnull — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.ifnull

pyspark.sql.functions.ifnull(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ifnull)
[#](#pyspark.sql.functions.ifnull "Permalink to this definition")

Returns col2 if col1 is null, or col1 otherwise.

New in version 3.5.0.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(None,), (1,)], ["e"])
>>> df.select(sf.ifnull(df.e, sf.lit(8))).show()
+------------+
|ifnull(e, 8)|
+------------+
|           8|
|           1|
+------------+

```
# pyspark.sql.functions.nanvl — PySpark 4.0.1 documentation
pyspark.sql.functions.nanvl(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#nanvl)
[#](#pyspark.sql.functions.nanvl "Permalink to this definition")

Returns col1 if it is not NaN, or col2 if col1 is NaN.

Both inputs should be floating point columns (`DoubleType` or `FloatType`).

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first column to check.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

second column to return if first is NaN.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value from first column or second if first is NaN .

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1.0, float('nan')), (float('nan'), 2.0)], ("a", "b"))
>>> df.select("*", sf.nanvl("a", "b"), sf.nanvl(df.a, df.b)).show()
+---+---+-----------+-----------+
|  a|  b|nanvl(a, b)|nanvl(a, b)|
+---+---+-----------+-----------+
|1.0|NaN|        1.0|        1.0|
|NaN|2.0|        2.0|        2.0|
+---+---+-----------+-----------+

```


# pyspark.sql.functions.nullif — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.nullif

pyspark.sql.functions.nullif(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#nullif)
[#](#pyspark.sql.functions.nullif "Permalink to this definition")

Returns null if col1 equals to col2, or col1 otherwise.

New in version 3.5.0.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(None, None,), (1, 9,)], ["a", "b"])
>>> df.select(nullif(df.a, df.b).alias('r')).collect()
[Row(r=None), Row(r=1)]

```



# pyspark.sql.functions.nullifzero — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.nullifzero

pyspark.sql.functions.nullifzero(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#nullifzero)
[#](#pyspark.sql.functions.nullifzero "Permalink to this definition")

Returns null if col is equal to zero, or col otherwise.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(0,), (1,)], ["a"])
>>> df.select(nullifzero(df.a).alias("result")).show()
+------+
|result|
+------+
|  NULL|
|     1|
+------+

```


# pyspark.sql.functions.nvl — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.nvl

pyspark.sql.functions.nvl(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#nvl)
[#](#pyspark.sql.functions.nvl "Permalink to this definition")

Returns col2 if col1 is null, or col1 otherwise.

New in version 3.5.0.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(None, 8,), (1, 9,)], ["a", "b"])
>>> df.select(nvl(df.a, df.b).alias('r')).collect()
[Row(r=8), Row(r=1)]

```

# pyspark.sql.functions.nvl2 — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.nvl2

pyspark.sql.functions.nvl2(_col1_, _col2_, _col3_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#nvl2)
[#](#pyspark.sql.functions.nvl2 "Permalink to this definition")

Returns col2 if col1 is not null, or col3 otherwise.

New in version 3.5.0.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

**col3**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(None, 8, 6,), (1, 9, 9,)], ["a", "b", "c"])
>>> df.select(nvl2(df.a, df.b, df.c).alias('r')).collect()
[Row(r=6), Row(r=9)]

```


# pyspark.sql.functions.when — PySpark 4.0.1 documentation
pyspark.sql.functions.when(_condition_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#when)
[#](#pyspark.sql.functions.when "Permalink to this definition")

Evaluates a list of conditions and returns one of multiple possible result expressions. If [`pyspark.sql.Column.otherwise()`](about:blank/pyspark.sql.Column.otherwise.html#pyspark.sql.Column.otherwise "pyspark.sql.Column.otherwise") is not invoked, None is returned for unmatched conditions.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**condition**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a boolean [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

**value**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

column representing when expression.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(3)
>>> df.select("*", sf.when(df['id'] == 2, 3).otherwise(4)).show()
+---+------------------------------------+
| id|CASE WHEN (id = 2) THEN 3 ELSE 4 END|
+---+------------------------------------+
|  0|                                   4|
|  1|                                   4|
|  2|                                   3|
+---+------------------------------------+

```


```
>>> df.select("*", sf.when(df.id == 2, df.id + 1)).show()
+---+------------------------------------+
| id|CASE WHEN (id = 2) THEN (id + 1) END|
+---+------------------------------------+
|  0|                                NULL|
|  1|                                NULL|
|  2|                                   3|
+---+------------------------------------+

```




# pyspark.sql.functions.zeroifnull — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.zeroifnull

pyspark.sql.functions.zeroifnull(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#zeroifnull)
[#](#pyspark.sql.functions.zeroifnull "Permalink to this definition")

Returns zero if col is null, or col otherwise.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(None,), (1,)], ["a"])
>>> df.select(zeroifnull(df.a).alias("result")).show()
+------+
|result|
+------+
|     0|
|     1|
+------+

```


# pyspark.sql.functions.equal_null — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.equal\_null

pyspark.sql.functions.equal\_null(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#equal_null)
[#](#pyspark.sql.functions.equal_null "Permalink to this definition")

Returns same result as the EQUAL(=) operator for non-null operands, but returns true if both are null, false if one of them is null.

New in version 3.5.0.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(None, None,), (1, 9,)], ["a", "b"])
>>> df.select(equal_null(df.a, df.b).alias('r')).collect()
[Row(r=True), Row(r=False)]

```


# pyspark.sql.functions.ilike — PySpark 4.0.1 documentation
pyspark.sql.functions.ilike(_str_, _pattern_, _escapeChar\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ilike)
[#](#pyspark.sql.functions.ilike "Permalink to this definition")

Returns true if str matches pattern with escape case-insensitively, null if any arguments are null, false otherwise. The default escape character is the ‘’.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A string.

**pattern**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A string. The pattern is a string which is matched literally, with exception to the following special symbols: \_ matches any one character in the input (similar to . in posix regular expressions) % matches zero or more characters in the input (similar to .\* in posix regular expressions) Since Spark 2.0, string literals are unescaped in our SQL parser. For example, in order to match “bc”, the pattern should be “abc”. When SQL config ‘spark.sql.parser.escapedStringLiterals’ is enabled, it falls back to Spark 1.6 behavior regarding string literal parsing. For example, if the config is enabled, the pattern to match “bc” should be “bc”.

**escapeChar**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

An character added since Spark 3.0. The default escape character is the ‘’. If an escape character precedes a special symbol or another escape character, the following character is matched literally. It is invalid to escape any other character.

Examples

```
>>> df = spark.createDataFrame([("Spark", "_park")], ['a', 'b'])
>>> df.select(ilike(df.a, df.b).alias('r')).collect()
[Row(r=True)]

```


```
>>> df = spark.createDataFrame(
...     [("%SystemDrive%/Users/John", "/%SystemDrive/%//Users%")],
...     ['a', 'b']
... )
>>> df.select(ilike(df.a, df.b, lit('/')).alias('r')).collect()
[Row(r=True)]

```


# pyspark.sql.functions.isnan — PySpark 4.0.1 documentation
pyspark.sql.functions.isnan(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#isnan)
[#](#pyspark.sql.functions.isnan "Permalink to this definition")

An expression that returns true if the column is NaN.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

True if value is NaN and False otherwise.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1.0, float('nan')), (float('nan'), 2.0)], ("a", "b"))
>>> df.select("*", sf.isnan("a"), sf.isnan(df.b)).show()
+---+---+--------+--------+
|  a|  b|isnan(a)|isnan(b)|
+---+---+--------+--------+
|1.0|NaN|   false|    true|
|NaN|2.0|    true|   false|
+---+---+--------+--------+

```

# pyspark.sql.functions.isnotnull — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.isnotnull

pyspark.sql.functions.isnotnull(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#isnotnull)
[#](#pyspark.sql.functions.isnotnull "Permalink to this definition")

Returns true if col is not null, or false otherwise.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Examples

```
>>> df = spark.createDataFrame([(None,), (1,)], ["e"])
>>> df.select(isnotnull(df.e).alias('r')).collect()
[Row(r=False), Row(r=True)]

```


# pyspark.sql.functions.isnull — PySpark 4.0.1 documentation
pyspark.sql.functions.isnull(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#isnull)
[#](#pyspark.sql.functions.isnull "Permalink to this definition")

An expression that returns true if the column is null.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

True if value is null and False otherwise.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, None), (None, 2)], ("a", "b"))
>>> df.select("*", sf.isnull("a"), isnull(df.b)).show()
+----+----+-----------+-----------+
|   a|   b|(a IS NULL)|(b IS NULL)|
+----+----+-----------+-----------+
|   1|NULL|      false|       true|
|NULL|   2|       true|      false|
+----+----+-----------+-----------+

```



# pyspark.sql.functions.like — PySpark 4.0.1 documentation
pyspark.sql.functions.like(_str_, _pattern_, _escapeChar\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#like)
[#](#pyspark.sql.functions.like "Permalink to this definition")

Returns true if str matches pattern with escape, null if any arguments are null, false otherwise. The default escape character is the ‘’.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A string.

**pattern**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A string. The pattern is a string which is matched literally, with exception to the following special symbols: \_ matches any one character in the input (similar to . in posix regular expressions) % matches zero or more characters in the input (similar to .\* in posix regular expressions) Since Spark 2.0, string literals are unescaped in our SQL parser. For example, in order to match “bc”, the pattern should be “abc”. When SQL config ‘spark.sql.parser.escapedStringLiterals’ is enabled, it falls back to Spark 1.6 behavior regarding string literal parsing. For example, if the config is enabled, the pattern to match “bc” should be “bc”.

**escapeChar**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

An character added since Spark 3.0. The default escape character is the ‘’. If an escape character precedes a special symbol or another escape character, the following character is matched literally. It is invalid to escape any other character.

Examples

```
>>> df = spark.createDataFrame([("Spark", "_park")], ['a', 'b'])
>>> df.select(like(df.a, df.b).alias('r')).collect()
[Row(r=True)]

```


```
>>> df = spark.createDataFrame(
...     [("%SystemDrive%/Users/John", "/%SystemDrive/%//Users%")],
...     ['a', 'b']
... )
>>> df.select(like(df.a, df.b, lit('/')).alias('r')).collect()
[Row(r=True)]

```

# pyspark.sql.functions.regexp — PySpark 4.0.1 documentation
pyspark.sql.functions.regexp(_str_, _regexp_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp)
[#](#pyspark.sql.functions.regexp "Permalink to this definition")

Returns true if str matches the Java regex regexp, or false otherwise.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

regex pattern to apply.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if str matches a Java regex, or false otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("1a 2b 14m", r"(\d+)")], ["str", "regexp"]
... ).select(sf.regexp('str', sf.lit(r'(\d+)'))).show()
+------------------+
|REGEXP(str, (\d+))|
+------------------+
|              true|
+------------------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("1a 2b 14m", r"(\d+)")], ["str", "regexp"]
... ).select(sf.regexp('str', sf.lit(r'\d{2}b'))).show()
+-------------------+
|REGEXP(str, \d{2}b)|
+-------------------+
|              false|
+-------------------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("1a 2b 14m", r"(\d+)")], ["str", "regexp"]
... ).select(sf.regexp('str', sf.col("regexp"))).show()
+-------------------+
|REGEXP(str, regexp)|
+-------------------+
|               true|
+-------------------+

```



# pyspark.sql.functions.regexp_like — PySpark 4.0.1 documentation
pyspark.sql.functions.regexp\_like(_str_, _regexp_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_like)
[#](#pyspark.sql.functions.regexp_like "Permalink to this definition")

Returns true if str matches the Java regex regexp, or false otherwise.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

regex pattern to apply.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if str matches a Java regex, or false otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("1a 2b 14m", r"(\d+)")], ["str", "regexp"]
... ).select(sf.regexp_like('str', sf.lit(r'(\d+)'))).show()
+-----------------------+
|REGEXP_LIKE(str, (\d+))|
+-----------------------+
|                   true|
+-----------------------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("1a 2b 14m", r"(\d+)")], ["str", "regexp"]
... ).select(sf.regexp_like('str', sf.lit(r'\d{2}b'))).show()
+------------------------+
|REGEXP_LIKE(str, \d{2}b)|
+------------------------+
|                   false|
+------------------------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("1a 2b 14m", r"(\d+)")], ["str", "regexp"]
... ).select(sf.regexp_like('str', sf.col("regexp"))).show()
+------------------------+
|REGEXP_LIKE(str, regexp)|
+------------------------+
|                    true|
+------------------------+

```

# pyspark.sql.functions.rlike — PySpark 4.0.1 documentation
pyspark.sql.functions.rlike(_str_, _regexp_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#rlike)
[#](#pyspark.sql.functions.rlike "Permalink to this definition")

Returns true if str matches the Java regex regexp, or false otherwise.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

regex pattern to apply.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if str matches a Java regex, or false otherwise.

Examples

```
>>> df = spark.createDataFrame([("1a 2b 14m", r"(\d+)")], ["str", "regexp"])
>>> df.select(rlike('str', lit(r'(\d+)')).alias('d')).collect()
[Row(d=True)]
>>> df.select(rlike('str', lit(r'\d{2}b')).alias('d')).collect()
[Row(d=False)]
>>> df.select(rlike("str", col("regexp")).alias('d')).collect()
[Row(d=True)]

```




# pyspark.sql.functions.asc — PySpark 4.0.1 documentation
pyspark.sql.functions.asc(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#asc)
[#](#pyspark.sql.functions.asc "Permalink to this definition")

Returns a sort expression for the target column in ascending order. This function is used in sort and orderBy functions.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Target column to sort by in the ascending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The column specifying the sort order.

Examples

Example 1: Sort DataFrame by ‘id’ column in ascending order.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(4, 'B'), (3, 'A'), (2, 'C')], ['id', 'value'])
>>> df.sort(sf.asc("id")).show()
+---+-----+
| id|value|
+---+-----+
|  2|    C|
|  3|    A|
|  4|    B|
+---+-----+

```


Example 2: Use asc in orderBy function to sort the DataFrame.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(4, 'B'), (3, 'A'), (2, 'C')], ['id', 'value'])
>>> df.orderBy(sf.asc("value")).show()
+---+-----+
| id|value|
+---+-----+
|  3|    A|
|  4|    B|
|  2|    C|
+---+-----+

```


Example 3: Combine asc with desc to sort by multiple columns.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(2, 'A', 4), (1, 'B', 3), (3, 'A', 2)],
...     ['id', 'group', 'value'])
>>> df.sort(sf.asc("group"), sf.desc("value")).show()
+---+-----+-----+
| id|group|value|
+---+-----+-----+
|  2|    A|    4|
|  3|    A|    2|
|  1|    B|    3|
+---+-----+-----+

```


Example 4: Implement asc from column expression.

```
>>> df = spark.createDataFrame([(4, 'B'), (3, 'A'), (2, 'C')], ['id', 'value'])
>>> df.sort(df.id.asc()).show()
+---+-----+
| id|value|
+---+-----+
|  2|    C|
|  3|    A|
|  4|    B|
+---+-----+

```


# pyspark.sql.functions.asc_nulls_first — PySpark 4.0.1 documentation
pyspark.sql.functions.asc\_nulls\_first(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#asc_nulls_first)
[#](#pyspark.sql.functions.asc_nulls_first "Permalink to this definition")

Sort Function: Returns a sort expression based on the ascending order of the given column name, and null values return before non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to sort by in the ascending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column specifying the order.

Examples

Example 1: Sorting a DataFrame with null values in ascending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "Bob"), (0, None), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.asc_nulls_first(df.name)).show()
+---+-----+
|age| name|
+---+-----+
|  0| NULL|
|  2|Alice|
|  1|  Bob|
+---+-----+

```


Example 2: Sorting a DataFrame with multiple columns, null values in ascending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [(1, "Bob", None), (0, None, "Z"), (2, "Alice", "Y")], ["age", "name", "grade"])
>>> df.sort(sf.asc_nulls_first(df.name), sf.asc_nulls_first(df.grade)).show()
+---+-----+-----+
|age| name|grade|
+---+-----+-----+
|  0| NULL|    Z|
|  2|Alice|    Y|
|  1|  Bob| NULL|
+---+-----+-----+

```


Example 3: Sorting a DataFrame with null values in ascending order using column name string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "Bob"), (0, None), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.asc_nulls_first("name")).show()
+---+-----+
|age| name|
+---+-----+
|  0| NULL|
|  2|Alice|
|  1|  Bob|
+---+-----+

```

# pyspark.sql.functions.asc_nulls_last — PySpark 4.0.1 documentation
pyspark.sql.functions.asc\_nulls\_last(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#asc_nulls_last)
[#](#pyspark.sql.functions.asc_nulls_last "Permalink to this definition")

Sort Function: Returns a sort expression based on the ascending order of the given column name, and null values appear after non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to sort by in the ascending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column specifying the order.

Examples

Example 1: Sorting a DataFrame with null values in ascending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(0, None), (1, "Bob"), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.asc_nulls_last(df.name)).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  1|  Bob|
|  0| NULL|
+---+-----+

```


Example 2: Sorting a DataFrame with multiple columns, null values in ascending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [(0, None, "Z"), (1, "Bob", None), (2, "Alice", "Y")], ["age", "name", "grade"])
>>> df.sort(sf.asc_nulls_last(df.name), sf.asc_nulls_last(df.grade)).show()
+---+-----+-----+
|age| name|grade|
+---+-----+-----+
|  2|Alice|    Y|
|  1|  Bob| NULL|
|  0| NULL|    Z|
+---+-----+-----+

```


Example 3: Sorting a DataFrame with null values in ascending order using column name string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(0, None), (1, "Bob"), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.asc_nulls_last("name")).show()
+---+-----+
|age| name|
+---+-----+
|  2|Alice|
|  1|  Bob|
|  0| NULL|
+---+-----+

```

# pyspark.sql.functions.desc — PySpark 4.0.1 documentation
pyspark.sql.functions.desc(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#desc)
[#](#pyspark.sql.functions.desc "Permalink to this definition")

Returns a sort expression for the target column in descending order. This function is used in sort and orderBy functions.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Target column to sort by in the descending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The column specifying the sort order.

Examples

Example 1: Sort DataFrame by ‘id’ column in descending order.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(4, 'B'), (3, 'A'), (2, 'C')], ['id', 'value'])
>>> df.sort(sf.desc("id")).show()
+---+-----+
| id|value|
+---+-----+
|  4|    B|
|  3|    A|
|  2|    C|
+---+-----+

```


Example 2: Use desc in orderBy function to sort the DataFrame.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(4, 'B'), (3, 'A'), (2, 'C')], ['id', 'value'])
>>> df.orderBy(sf.desc("value")).show()
+---+-----+
| id|value|
+---+-----+
|  2|    C|
|  4|    B|
|  3|    A|
+---+-----+

```


Example 3: Combine asc with desc to sort by multiple columns.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(2, 'A', 4), (1, 'B', 3), (3, 'A', 2)],
...     ['id', 'group', 'value'])
>>> df.sort(sf.desc("group"), sf.asc("value")).show()
+---+-----+-----+
| id|group|value|
+---+-----+-----+
|  1|    B|    3|
|  3|    A|    2|
|  2|    A|    4|
+---+-----+-----+

```


Example 4: Implement desc from column expression.

```
>>> df = spark.createDataFrame([(4, 'B'), (3, 'A'), (2, 'C')], ['id', 'value'])
>>> df.sort(df.id.desc()).show()
+---+-----+
| id|value|
+---+-----+
|  4|    B|
|  3|    A|
|  2|    C|
+---+-----+

```


# pyspark.sql.functions.desc_nulls_first — PySpark 4.0.1 documentation
pyspark.sql.functions.desc\_nulls\_first(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#desc_nulls_first)
[#](#pyspark.sql.functions.desc_nulls_first "Permalink to this definition")

Sort Function: Returns a sort expression based on the descending order of the given column name, and null values appear before non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to sort by in the descending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column specifying the order.

Examples

Example 1: Sorting a DataFrame with null values in descending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "Bob"), (0, None), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.desc_nulls_first(df.name)).show()
+---+-----+
|age| name|
+---+-----+
|  0| NULL|
|  1|  Bob|
|  2|Alice|
+---+-----+

```


Example 2: Sorting a DataFrame with multiple columns, null values in descending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [(1, "Bob", None), (0, None, "Z"), (2, "Alice", "Y")], ["age", "name", "grade"])
>>> df.sort(sf.desc_nulls_first(df.name), sf.desc_nulls_first(df.grade)).show()
+---+-----+-----+
|age| name|grade|
+---+-----+-----+
|  0| NULL|    Z|
|  1|  Bob| NULL|
|  2|Alice|    Y|
+---+-----+-----+

```


Example 3: Sorting a DataFrame with null values in descending order using column name string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "Bob"), (0, None), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.desc_nulls_first("name")).show()
+---+-----+
|age| name|
+---+-----+
|  0| NULL|
|  1|  Bob|
|  2|Alice|
+---+-----+

```


# pyspark.sql.functions.desc_nulls_last — PySpark 4.0.1 documentation
pyspark.sql.functions.desc\_nulls\_last(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#desc_nulls_last)
[#](#pyspark.sql.functions.desc_nulls_last "Permalink to this definition")

Sort Function: Returns a sort expression based on the descending order of the given column name, and null values appear after non-null values.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to sort by in the descending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column specifying the order.

Examples

Example 1: Sorting a DataFrame with null values in descending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(0, None), (1, "Bob"), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.desc_nulls_last(df.name)).show()
+---+-----+
|age| name|
+---+-----+
|  1|  Bob|
|  2|Alice|
|  0| NULL|
+---+-----+

```


Example 2: Sorting a DataFrame with multiple columns, null values in descending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [(0, None, "Z"), (1, "Bob", None), (2, "Alice", "Y")], ["age", "name", "grade"])
>>> df.sort(sf.desc_nulls_last(df.name), sf.desc_nulls_last(df.grade)).show()
+---+-----+-----+
|age| name|grade|
+---+-----+-----+
|  1|  Bob| NULL|
|  2|Alice|    Y|
|  0| NULL|    Z|
+---+-----+-----+

```


Example 3: Sorting a DataFrame with null values in descending order using column name string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(0, None), (1, "Bob"), (2, "Alice")], ["age", "name"])
>>> df.sort(sf.desc_nulls_last("name")).show()
+---+-----+
|age| name|
+---+-----+
|  1|  Bob|
|  2|Alice|
|  0| NULL|
+---+-----+

```



# pyspark.sql.functions.abs — PySpark 4.0.1 documentation
pyspark.sql.functions.abs(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#abs)
[#](#pyspark.sql.functions.abs "Permalink to this definition")

Mathematical Function: Computes the absolute value of the given column or expression.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or expression to compute the absolute value on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column object representing the absolute value of the input.

Examples

Example 1: Compute the absolute value of a long column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-1,), (-2,), (-3,), (None,)], ["value"])
>>> df.select("*", sf.abs(df.value)).show()
+-----+----------+
|value|abs(value)|
+-----+----------+
|   -1|         1|
|   -2|         2|
|   -3|         3|
| NULL|      NULL|
+-----+----------+

```


Example 2: Compute the absolute value of a double column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-1.5,), (-2.5,), (None,), (float("nan"),)], ["value"])
>>> df.select("*", sf.abs(df.value)).show()
+-----+----------+
|value|abs(value)|
+-----+----------+
| -1.5|       1.5|
| -2.5|       2.5|
| NULL|      NULL|
|  NaN|       NaN|
+-----+----------+

```


Example 3: Compute the absolute value of an expression

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 1), (2, -2), (3, 3)], ["id", "value"])
>>> df.select("*", sf.abs(df.id - df.value)).show()
+---+-----+-----------------+
| id|value|abs((id - value))|
+---+-----+-----------------+
|  1|    1|                0|
|  2|   -2|                4|
|  3|    3|                0|
+---+-----+-----------------+

```


# pyspark.sql.functions.acos — PySpark 4.0.1 documentation
pyspark.sql.functions.acos(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#acos)
[#](#pyspark.sql.functions.acos "Permalink to this definition")

Mathematical Function: Computes the inverse cosine (also known as arccosine) of the given column or expression.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or expression to compute the inverse cosine on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column object representing the inverse cosine of the input.

Examples

Example 1: Compute the inverse cosine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-1.0,), (-0.5,), (0.0,), (0.5,), (1.0,)], ["value"])
>>> df.select("*", sf.acos("value")).show()
+-----+------------------+
|value|       ACOS(value)|
+-----+------------------+
| -1.0| 3.141592653589...|
| -0.5|2.0943951023931...|
|  0.0|1.5707963267948...|
|  0.5|1.0471975511965...|
|  1.0|               0.0|
+-----+------------------+

```


Example 2: Compute the inverse cosine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (-2), (2), (NULL) AS TAB(value)"
... ).select("*", sf.acos("value")).show()
+-----+-----------+
|value|ACOS(value)|
+-----+-----------+
|   -2|        NaN|
|    2|        NaN|
| NULL|       NULL|
+-----+-----------+

```



# pyspark.sql.functions.acosh — PySpark 4.0.1 documentation
pyspark.sql.functions.acosh(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#acosh)
[#](#pyspark.sql.functions.acosh "Permalink to this definition")

Mathematical Function: Computes the inverse hyperbolic cosine (also known as arcosh) of the given column or expression.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or expression to compute the inverse hyperbolic cosine on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column object representing the inverse hyperbolic cosine of the input.

Examples

Example 1: Compute the inverse hyperbolic cosine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (2,)], ["value"])
>>> df.select("*", sf.acosh(df.value)).show()
+-----+------------------+
|value|      ACOSH(value)|
+-----+------------------+
|    1|               0.0|
|    2|1.3169578969248...|
+-----+------------------+

```


Example 2: Compute the inverse hyperbolic cosine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (-0.5), (0.5), (NULL) AS TAB(value)"
... ).select("*", sf.acosh("value")).show()
+-----+------------+
|value|ACOSH(value)|
+-----+------------+
| -0.5|         NaN|
|  0.5|         NaN|
| NULL|        NULL|
+-----+------------+

```

# pyspark.sql.functions.asin — PySpark 4.0.1 documentation
pyspark.sql.functions.asin(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#asin)
[#](#pyspark.sql.functions.asin "Permalink to this definition")

Computes inverse sine of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

inverse sine of col, as if computed by java.lang.Math.asin()

Examples

Example 1: Compute the inverse sine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-0.5,), (0.0,), (0.5,)], ["value"])
>>> df.select("*", sf.asin(df.value)).show()
+-----+-------------------+
|value|        ASIN(value)|
+-----+-------------------+
| -0.5|-0.5235987755982...|
|  0.0|                0.0|
|  0.5| 0.5235987755982...|
+-----+-------------------+

```


Example 2: Compute the inverse sine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (-2), (2), (NULL) AS TAB(value)"
... ).select("*", sf.asin("value")).show()
+-----+-----------+
|value|ASIN(value)|
+-----+-----------+
|   -2|        NaN|
|    2|        NaN|
| NULL|       NULL|
+-----+-----------+

```

# pyspark.sql.functions.asinh — PySpark 4.0.1 documentation
pyspark.sql.functions.asinh(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#asinh)
[#](#pyspark.sql.functions.asinh "Permalink to this definition")

Computes inverse hyperbolic sine of the input column.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Compute the inverse hyperbolic sine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-0.5,), (0.0,), (0.5,)], ["value"])
>>> df.select("*", sf.asinh(df.value)).show()
+-----+--------------------+
|value|        ASINH(value)|
+-----+--------------------+
| -0.5|-0.48121182505960...|
|  0.0|                 0.0|
|  0.5| 0.48121182505960...|
+-----+--------------------+

```


Example 2: Compute the inverse hyperbolic sine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.asinh("value")).show()
+-----+------------+
|value|ASINH(value)|
+-----+------------+
|  NaN|         NaN|
| NULL|        NULL|
+-----+------------+

```


# pyspark.sql.functions.atan — PySpark 4.0.1 documentation
pyspark.sql.functions.atan(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#atan)
[#](#pyspark.sql.functions.atan "Permalink to this definition")

Compute inverse tangent of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

inverse tangent of col, as if computed by java.lang.Math.atan()

Examples

Example 1: Compute the inverse tangent

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-0.5,), (0.0,), (0.5,)], ["value"])
>>> df.select("*", sf.atan(df.value)).show()
+-----+-------------------+
|value|        ATAN(value)|
+-----+-------------------+
| -0.5|-0.4636476090008...|
|  0.0|                0.0|
|  0.5| 0.4636476090008...|
+-----+-------------------+

```


Example 2: Compute the inverse tangent of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.atan("value")).show()
+-----+-----------+
|value|ATAN(value)|
+-----+-----------+
|  NaN|        NaN|
| NULL|       NULL|
+-----+-----------+

```



# pyspark.sql.functions.atan2 — PySpark 4.0.1 documentation
pyspark.sql.functions.atan2(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#atan2)
[#](#pyspark.sql.functions.atan2 "Permalink to this definition")

Compute the angle in radians between the positive x-axis of a plane and the point given by the coordinates

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

coordinate on y-axis

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

coordinate on x-axis

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the theta component of the point (r, theta) in polar coordinates that corresponds to the point (x, y) in Cartesian coordinates, as if computed by java.lang.Math.atan2()

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.atan2(sf.lit(1), sf.lit(2))).show()
+------------------+
|       ATAN2(1, 2)|
+------------------+
|0.4636476090008...|
+------------------+

```


# pyspark.sql.functions.atanh — PySpark 4.0.1 documentation
pyspark.sql.functions.atanh(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#atanh)
[#](#pyspark.sql.functions.atanh "Permalink to this definition")

Computes inverse hyperbolic tangent of the input column.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Compute the inverse hyperbolic tangent

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-0.5,), (0.0,), (0.5,)], ["value"])
>>> df.select("*", sf.atanh(df.value)).show()
+-----+-------------------+
|value|       ATANH(value)|
+-----+-------------------+
| -0.5|-0.5493061443340...|
|  0.0|                0.0|
|  0.5| 0.5493061443340...|
+-----+-------------------+

```


Example 2: Compute the inverse hyperbolic tangent of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (-2), (2), (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.atanh("value")).show()
+-----+------------+
|value|ATANH(value)|
+-----+------------+
| -2.0|         NaN|
|  2.0|         NaN|
|  NaN|         NaN|
| NULL|        NULL|
+-----+------------+

```


# pyspark.sql.functions.bin — PySpark 4.0.1 documentation
pyspark.sql.functions.bin(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bin)
[#](#pyspark.sql.functions.bin "Permalink to this definition")

Returns the string representation of the binary value of the given column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

binary representation of given value as string.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(10).select("*", sf.bin("id")).show()
+---+-------+
| id|bin(id)|
+---+-------+
|  0|      0|
|  1|      1|
|  2|     10|
|  3|     11|
|  4|    100|
|  5|    101|
|  6|    110|
|  7|    111|
|  8|   1000|
|  9|   1001|
+---+-------+

```

# pyspark.sql.functions.bround — PySpark 4.0.1 documentation
pyspark.sql.functions.bround(_col_, _scale\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bround)
[#](#pyspark.sql.functions.bround "Permalink to this definition")

Round the given value to scale decimal places using HALF\_EVEN rounding mode if scale >= 0 or at integral part when scale < 0.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or column name to compute the round on.

**scale**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

An optional parameter to control the rounding behavior.

Changed in version 4.0.0: Support Column type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column for the rounded value.

Examples

Example 1: Compute the rounded of a column value

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.bround(sf.lit(2.5))).show()
+--------------+
|bround(2.5, 0)|
+--------------+
|           2.0|
+--------------+

```


Example 2: Compute the rounded of a column value with a specified scale

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.bround(sf.lit(2.1267), sf.lit(2))).show()
+-----------------+
|bround(2.1267, 2)|
+-----------------+
|             2.13|
+-----------------+

```

# pyspark.sql.functions.cbrt — PySpark 4.0.1 documentation
pyspark.sql.functions.cbrt(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#cbrt)
[#](#pyspark.sql.functions.cbrt "Permalink to this definition")

Computes the cube-root of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Compute the cube-root

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-8,), (0,), (8,)], ["value"])
>>> df.select("*", sf.cbrt(df.value)).show()
+-----+-----------+
|value|CBRT(value)|
+-----+-----------+
|   -8|       -2.0|
|    0|        0.0|
|    8|        2.0|
+-----+-----------+

```


Example 2: Compute the cube-root of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.cbrt("value")).show()
+-----+-----------+
|value|CBRT(value)|
+-----+-----------+
|  NaN|        NaN|
| NULL|       NULL|
+-----+-----------+

```

# pyspark.sql.functions.ceil — PySpark 4.0.1 documentation
pyspark.sql.functions.ceil(_col_, _scale\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ceil)
[#](#pyspark.sql.functions.ceil "Permalink to this definition")

Computes the ceiling of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or column name to compute the ceiling on.

**scale**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

An optional parameter to control the rounding behavior.

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column for the computed results.

Examples

Example 1: Compute the ceiling of a column value

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.ceil(sf.lit(-0.1))).show()
+----------+
|CEIL(-0.1)|
+----------+
|         0|
+----------+

```


Example 2: Compute the ceiling of a column value with a specified scale

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.ceil(sf.lit(-0.1), 1)).show()
+-------------+
|ceil(-0.1, 1)|
+-------------+
|         -0.1|
+-------------+

```


# pyspark.sql.functions.ceiling — PySpark 4.0.1 documentation
pyspark.sql.functions.ceiling(_col_, _scale\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ceiling)
[#](#pyspark.sql.functions.ceiling "Permalink to this definition")

Computes the ceiling of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or column name to compute the ceiling on.

**scale**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

An optional parameter to control the rounding behavior.

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column for the computed results.

Examples

Example 1: Compute the ceiling of a column value

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.ceiling(sf.lit(-0.1))).show()
+-------------+
|ceiling(-0.1)|
+-------------+
|            0|
+-------------+

```


Example 2: Compute the ceiling of a column value with a specified scale

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.ceiling(sf.lit(-0.1), 1)).show()
+----------------+
|ceiling(-0.1, 1)|
+----------------+
|            -0.1|
+----------------+

```



# pyspark.sql.functions.conv — PySpark 4.0.1 documentation
pyspark.sql.functions.conv(_col_, _fromBase_, _toBase_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#conv)
[#](#pyspark.sql.functions.conv "Permalink to this definition")

Convert a number in a string column from one base to another.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column to convert base for.

**fromBase: int**

from base number.

**toBase: int**

to base number.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

logariphm of given value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("010101",), ( "101",), ("001",)], ['n'])
>>> df.select("*", sf.conv(df.n, 2, 16)).show()
+------+--------------+
|     n|conv(n, 2, 16)|
+------+--------------+
|010101|            15|
|   101|             5|
|   001|             1|
+------+--------------+

```

# pyspark.sql.functions.cos — PySpark 4.0.1 documentation
pyspark.sql.functions.cos(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#cos)
[#](#pyspark.sql.functions.cos "Permalink to this definition")

Computes cosine of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

angle in radians

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

cosine of the angle, as if computed by java.lang.Math.cos().

Examples

Example 1: Compute the cosine

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (PI()), (PI() / 4), (PI() / 16) AS TAB(value)"
... ).select("*", sf.cos("value")).show()
+-------------------+------------------+
|              value|        COS(value)|
+-------------------+------------------+
|  3.141592653589...|              -1.0|
| 0.7853981633974...|0.7071067811865...|
|0.19634954084936...|0.9807852804032...|
+-------------------+------------------+

```


Example 2: Compute the cosine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.cos("value")).show()
+-----+----------+
|value|COS(value)|
+-----+----------+
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```


# pyspark.sql.functions.cosh — PySpark 4.0.1 documentation
pyspark.sql.functions.cosh(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#cosh)
[#](#pyspark.sql.functions.cosh "Permalink to this definition")

Computes hyperbolic cosine of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

hyperbolic angle

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hyperbolic cosine of the angle, as if computed by java.lang.Math.cosh()

Examples

Example 1: Compute the cosine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-1,), (0,), (1,)], ["value"])
>>> df.select("*", sf.cosh(df.value)).show()
+-----+-----------------+
|value|      COSH(value)|
+-----+-----------------+
|   -1|1.543080634815...|
|    0|              1.0|
|    1|1.543080634815...|
+-----+-----------------+

```


Example 2: Compute the cosine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.cosh("value")).show()
+-----+-----------+
|value|COSH(value)|
+-----+-----------+
|  NaN|        NaN|
| NULL|       NULL|
+-----+-----------+

```

# pyspark.sql.functions.cot — PySpark 4.0.1 documentation
pyspark.sql.functions.cot(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#cot)
[#](#pyspark.sql.functions.cot "Permalink to this definition")

Computes cotangent of the input column.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

angle in radians.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

cotangent of the angle.

Examples

Example 1: Compute the cotangent

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (PI() / 4), (PI() / 16) AS TAB(value)"
... ).select("*", sf.cot("value")).show()
+-------------------+------------------+
|              value|        COT(value)|
+-------------------+------------------+
| 0.7853981633974...|1.0000000000000...|
|0.19634954084936...| 5.027339492125...|
+-------------------+------------------+

```


Example 2: Compute the cotangent of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0.0), (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.cot("value")).show()
+-----+----------+
|value|COT(value)|
+-----+----------+
|  0.0|  Infinity|
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```


# pyspark.sql.functions.csc — PySpark 4.0.1 documentation
pyspark.sql.functions.csc(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#csc)
[#](#pyspark.sql.functions.csc "Permalink to this definition")

Computes cosecant of the input column.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

angle in radians.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

cosecant of the angle.

Examples

Example 1: Compute the cosecant

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (PI() / 2), (PI() / 4) AS TAB(value)"
... ).select("*", sf.csc("value")).show()
+------------------+------------------+
|             value|        CSC(value)|
+------------------+------------------+
|1.5707963267948...|               1.0|
|0.7853981633974...|1.4142135623730...|
+------------------+------------------+

```


Example 2: Compute the cosecant of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0.0), (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.csc("value")).show()
+-----+----------+
|value|CSC(value)|
+-----+----------+
|  0.0|  Infinity|
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```


# pyspark.sql.functions.degrees — PySpark 4.0.1 documentation
pyspark.sql.functions.degrees(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#degrees)
[#](#pyspark.sql.functions.degrees "Permalink to this definition")

Converts an angle measured in radians to an approximately equivalent angle measured in degrees.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

angle in radians

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

angle in degrees, as if computed by java.lang.Math.toDegrees()

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0.0), (PI()), (PI() / 2), (PI() / 4) AS TAB(value)"
... ).select("*", sf.degrees("value")).show()
+------------------+--------------+
|             value|DEGREES(value)|
+------------------+--------------+
|               0.0|           0.0|
| 3.141592653589...|         180.0|
|1.5707963267948...|          90.0|
|0.7853981633974...|          45.0|
+------------------+--------------+

```


# pyspark.sql.functions.e — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.e

pyspark.sql.functions.e()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#e)
[#](#pyspark.sql.functions.e "Permalink to this definition")

Returns Euler’s number.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.e()).show()
+-----------------+
|              E()|
+-----------------+
|2.718281828459045|
+-----------------+

```


# pyspark.sql.functions.exp — PySpark 4.0.1 documentation
pyspark.sql.functions.exp(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#exp)
[#](#pyspark.sql.functions.exp "Permalink to this definition")

Computes the exponential of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to calculate exponential for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

exponential of the given value.

Examples

Example 1: Compute the exponential

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT id AS value FROM RANGE(5)")
>>> df.select("*", sf.exp(df.value)).show()
+-----+------------------+
|value|        EXP(value)|
+-----+------------------+
|    0|               1.0|
|    1|2.7182818284590...|
|    2|  7.38905609893...|
|    3|20.085536923187...|
|    4|54.598150033144...|
+-----+------------------+

```


Example 2: Compute the exponential of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.exp("value")).show()
+-----+----------+
|value|EXP(value)|
+-----+----------+
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```


# pyspark.sql.functions.expm1 — PySpark 4.0.1 documentation
pyspark.sql.functions.expm1(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#expm1)
[#](#pyspark.sql.functions.expm1 "Permalink to this definition")

Computes the exponential of the given value minus one.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to calculate exponential for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

exponential less one.

Examples

Example 1: Compute the exponential minus one

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT id AS value FROM RANGE(5)")
>>> df.select("*", sf.expm1(df.value)).show()
+-----+------------------+
|value|      EXPM1(value)|
+-----+------------------+
|    0|               0.0|
|    1| 1.718281828459...|
|    2|  6.38905609893...|
|    3|19.085536923187...|
|    4|53.598150033144...|
+-----+------------------+

```


Example 2: Compute the exponential minus one of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.expm1("value")).show()
+-----+------------+
|value|EXPM1(value)|
+-----+------------+
|  NaN|         NaN|
| NULL|        NULL|
+-----+------------+

```



# pyspark.sql.functions.factorial — PySpark 4.0.1 documentation
pyspark.sql.functions.factorial(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#factorial)
[#](#pyspark.sql.functions.factorial "Permalink to this definition")

Computes the factorial of the given value.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column to calculate factorial for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

factorial of given value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(10).select("*", sf.factorial('id')).show()
+---+-------------+
| id|factorial(id)|
+---+-------------+
|  0|            1|
|  1|            1|
|  2|            2|
|  3|            6|
|  4|           24|
|  5|          120|
|  6|          720|
|  7|         5040|
|  8|        40320|
|  9|       362880|
+---+-------------+

```
# pyspark.sql.functions.floor — PySpark 4.0.1 documentation
pyspark.sql.functions.floor(_col_, _scale\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#floor)
[#](#pyspark.sql.functions.floor "Permalink to this definition")

Computes the floor of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or column name to compute the floor on.

**scale**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

An optional parameter to control the rounding behavior.

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

nearest integer that is less than or equal to given value.

Examples

Example 1: Compute the floor of a column value

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.floor(sf.lit(2.5))).show()
+----------+
|FLOOR(2.5)|
+----------+
|         2|
+----------+

```


Example 2: Compute the floor of a column value with a specified scale

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.floor(sf.lit(2.1267), sf.lit(2))).show()
+----------------+
|floor(2.1267, 2)|
+----------------+
|            2.12|
+----------------+

```

# pyspark.sql.functions.greatest — PySpark 4.0.1 documentation
pyspark.sql.functions.greatest(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#greatest)
[#](#pyspark.sql.functions.greatest "Permalink to this definition")

Returns the greatest value of the list of column names, skipping null values. This function takes at least 2 parameters. It will return null if all parameters are null.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols: :class:\`~pyspark.sql.Column\` or column name**

columns to check for greatest value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

greatest value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, 4, 3)], ['a', 'b', 'c'])
>>> df.select("*", sf.greatest(df.a, "b", df.c)).show()
+---+---+---+-----------------+
|  a|  b|  c|greatest(a, b, c)|
+---+---+---+-----------------+
|  1|  4|  3|                4|
+---+---+---+-----------------+

```


# pyspark.sql.functions.hex — PySpark 4.0.1 documentation
pyspark.sql.functions.hex(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hex)
[#](#pyspark.sql.functions.hex "Permalink to this definition")

Computes hex value of the given column, which could be [`pyspark.sql.types.StringType`](about:blank/pyspark.sql.types.StringType.html#pyspark.sql.types.StringType "pyspark.sql.types.StringType"), [`pyspark.sql.types.BinaryType`](about:blank/pyspark.sql.types.BinaryType.html#pyspark.sql.types.BinaryType "pyspark.sql.types.BinaryType"), [`pyspark.sql.types.IntegerType`](about:blank/pyspark.sql.types.IntegerType.html#pyspark.sql.types.IntegerType "pyspark.sql.types.IntegerType") or [`pyspark.sql.types.LongType`](about:blank/pyspark.sql.types.LongType.html#pyspark.sql.types.LongType "pyspark.sql.types.LongType").

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hexadecimal representation of given value as string.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ABC', 3)], ['a', 'b'])
>>> df.select('*', sf.hex('a'), sf.hex(df.b)).show()
+---+---+------+------+
|  a|  b|hex(a)|hex(b)|
+---+---+------+------+
|ABC|  3|414243|     3|
+---+---+------+------+

```



# pyspark.sql.functions.hypot — PySpark 4.0.1 documentation
pyspark.sql.functions.hypot(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hypot)
[#](#pyspark.sql.functions.hypot "Permalink to this definition")

Computes `sqrt(a^2 + b^2)` without intermediate overflow or underflow.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

a leg.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

b leg.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

length of the hypotenuse.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.hypot(sf.lit(1), sf.lit(2))).show()
+----------------+
|     HYPOT(1, 2)|
+----------------+
|2.23606797749...|
+----------------+

```

# pyspark.sql.functions.least — PySpark 4.0.1 documentation
pyspark.sql.functions.least(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#least)
[#](#pyspark.sql.functions.least "Permalink to this definition")

Returns the least value of the list of column names, skipping null values. This function takes at least 2 parameters. It will return null if all parameters are null.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column names or columns to be compared

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

least value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, 4, 3)], ['a', 'b', 'c'])
>>> df.select("*", sf.least(df.a, "b", df.c)).show()
+---+---+---+--------------+
|  a|  b|  c|least(a, b, c)|
+---+---+---+--------------+
|  1|  4|  3|             1|
+---+---+---+--------------+

```



# pyspark.sql.functions.ln — PySpark 4.0.1 documentation
pyspark.sql.functions.ln(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ln)
[#](#pyspark.sql.functions.ln "Permalink to this definition")

Returns the natural logarithm of the argument.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column to calculate logariphm for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

natural logarithm of given value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(10).select("*", sf.ln('id')).show()
+---+------------------+
| id|            ln(id)|
+---+------------------+
|  0|              NULL|
|  1|               0.0|
|  2|0.6931471805599...|
|  3|1.0986122886681...|
|  4|1.3862943611198...|
|  5|1.6094379124341...|
|  6| 1.791759469228...|
|  7|1.9459101490553...|
|  8|2.0794415416798...|
|  9|2.1972245773362...|
+---+------------------+

```




# pyspark.sql.functions.log — PySpark 4.0.1 documentation
pyspark.sql.functions.log(_arg1_, _arg2\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#log)
[#](#pyspark.sql.functions.log "Permalink to this definition")

Returns the first argument-based logarithm of the second argument.

If there is only one argument, then this takes the natural logarithm of the argument.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**arg1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), str or float

base number or actual number (in this case base is e)

**arg2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), str or float, optional

number to calculate logariphm for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

logariphm of given value.

Examples

Example 1: Specify both base number and the input value

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1), (2), (4) AS t(value)")
>>> df.select("*", sf.log(2.0, df.value)).show()
+-----+---------------+
|value|LOG(2.0, value)|
+-----+---------------+
|    1|            0.0|
|    2|            1.0|
|    4|            2.0|
+-----+---------------+

```


Example 2: Return NULL for invalid input values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1), (2), (0), (-1), (NULL) AS t(value)")
>>> df.select("*", sf.log(3.0, df.value)).show()
+-----+------------------+
|value|   LOG(3.0, value)|
+-----+------------------+
|    1|               0.0|
|    2|0.6309297535714...|
|    0|              NULL|
|   -1|              NULL|
| NULL|              NULL|
+-----+------------------+

```


Example 3: Specify only the input value (Natural logarithm)

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1), (2), (4) AS t(value)")
>>> df.select("*", sf.log(df.value)).show()
+-----+------------------+
|value|         ln(value)|
+-----+------------------+
|    1|               0.0|
|    2|0.6931471805599...|
|    4|1.3862943611198...|
+-----+------------------+

```




# pyspark.sql.functions.log10 — PySpark 4.0.1 documentation
pyspark.sql.functions.log10(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#log10)
[#](#pyspark.sql.functions.log10 "Permalink to this definition")

Computes the logarithm of the given value in Base 10.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to calculate logarithm for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

logarithm of the given value in Base 10.

Examples

Example 1: Compute the logarithm in Base 10

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (10,), (100,)], ["value"])
>>> df.select("*", sf.log10(df.value)).show()
+-----+------------+
|value|LOG10(value)|
+-----+------------+
|    1|         0.0|
|   10|         1.0|
|  100|         2.0|
+-----+------------+

```


Example 2: Compute the logarithm in Base 10 of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (-1), (0), (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.log10("value")).show()
+-----+------------+
|value|LOG10(value)|
+-----+------------+
| -1.0|        NULL|
|  0.0|        NULL|
|  NaN|         NaN|
| NULL|        NULL|
+-----+------------+

```


# pyspark.sql.functions.log1p — PySpark 4.0.1 documentation
pyspark.sql.functions.log1p(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#log1p)
[#](#pyspark.sql.functions.log1p "Permalink to this definition")

Computes the natural logarithm of the given value plus one.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to calculate natural logarithm for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

natural logarithm of the “given value plus one”.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.log1p(sf.e())).show()
+------------------+
|        LOG1P(E())|
+------------------+
|1.3132616875182...|
+------------------+

```


Same as:

```
>>> spark.range(1).select(sf.log(sf.e() + 1)).show()
+------------------+
|     ln((E() + 1))|
+------------------+
|1.3132616875182...|
+------------------+

```


# pyspark.sql.functions.log2 — PySpark 4.0.1 documentation
pyspark.sql.functions.log2(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#log2)
[#](#pyspark.sql.functions.log2 "Permalink to this definition")

Returns the base-2 logarithm of the argument.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column to calculate logariphm for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

logariphm of given value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(10).select("*", sf.log2('id')).show()
+---+------------------+
| id|          LOG2(id)|
+---+------------------+
|  0|              NULL|
|  1|               0.0|
|  2|               1.0|
|  3| 1.584962500721...|
|  4|               2.0|
|  5| 2.321928094887...|
|  6| 2.584962500721...|
|  7| 2.807354922057...|
|  8|               3.0|
|  9|3.1699250014423...|
+---+------------------+

```


# pyspark.sql.functions.negate — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.negate

pyspark.sql.functions.negate(_col_)
[#](#pyspark.sql.functions.negate "Permalink to this definition")

Returns the negative value.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to calculate negative value for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

negative value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(-1,), (0,), (1,)], ["value"])
>>> df.select("*", sf.negative(df.value)).show()
+-----+---------------+
|value|negative(value)|
+-----+---------------+
|   -1|              1|
|    0|              0|
|    1|             -1|
+-----+---------------+

```


# pyspark.sql.functions.negative — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.negative

pyspark.sql.functions.negative(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#negative)
[#](#pyspark.sql.functions.negative "Permalink to this definition")

Returns the negative value.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to calculate negative value for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

negative value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(-1,), (0,), (1,)], ["value"])
>>> df.select("*", sf.negative(df.value)).show()
+-----+---------------+
|value|negative(value)|
+-----+---------------+
|   -1|              1|
|    0|              0|
|    1|             -1|
+-----+---------------+

```

# pyspark.sql.functions.pi — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.pi

pyspark.sql.functions.pi()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#pi)
[#](#pyspark.sql.functions.pi "Permalink to this definition")

Returns Pi.

New in version 3.5.0.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.pi()).show()
+-----------------+
|             PI()|
+-----------------+
|3.141592653589793|
+-----------------+

```

# pyspark.sql.functions.pmod — PySpark 4.0.1 documentation
pyspark.sql.functions.pmod(_dividend_, _divisor_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#pmod)
[#](#pyspark.sql.functions.pmod "Permalink to this definition")

Returns the positive value of dividend mod divisor.

New in version 3.4.0.

Parameters

**dividend**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

the column that contains dividend, or the specified dividend value

**divisor**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

the column that contains divisor, or the specified divisor value

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

positive value of dividend mod divisor.

Notes

Supports Spark Connect.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (1.0, float('nan')), (float('nan'), 2.0), (10.0, 3.0),
...     (float('nan'), float('nan')), (-3.0, 4.0), (-10.0, 3.0),
...     (-5.0, -6.0), (7.0, -8.0), (1.0, 2.0)],
...     ("a", "b"))
>>> df.select("*", sf.pmod("a", "b")).show()
+-----+----+----------+
|    a|   b|pmod(a, b)|
+-----+----+----------+
|  1.0| NaN|       NaN|
|  NaN| 2.0|       NaN|
| 10.0| 3.0|       1.0|
|  NaN| NaN|       NaN|
| -3.0| 4.0|       1.0|
|-10.0| 3.0|       2.0|
| -5.0|-6.0|      -5.0|
|  7.0|-8.0|       7.0|
|  1.0| 2.0|       1.0|
+-----+----+----------+

```


# pyspark.sql.functions.positive — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.positive

pyspark.sql.functions.positive(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#positive)
[#](#pyspark.sql.functions.positive "Permalink to this definition")

Returns the value.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input value column.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(-1,), (0,), (1,)], ["value"])
>>> df.select("*", sf.positive(df.value)).show()
+-----+---------+
|value|(+ value)|
+-----+---------+
|   -1|       -1|
|    0|        0|
|    1|        1|
+-----+---------+

```


# pyspark.sql.functions.pow — PySpark 4.0.1 documentation
pyspark.sql.functions.pow(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#pow)
[#](#pyspark.sql.functions.pow "Permalink to this definition")

Returns the value of the first argument raised to the power of the second argument.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

the base number.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

the exponent number.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the base rased to the power the argument.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(5).select("*", sf.pow("id", 2)).show()
+---+------------+
| id|POWER(id, 2)|
+---+------------+
|  0|         0.0|
|  1|         1.0|
|  2|         4.0|
|  3|         9.0|
|  4|        16.0|
+---+------------+

```


# pyspark.sql.functions.power — PySpark 4.0.1 documentation
pyspark.sql.functions.power(_col1_, _col2_)
[#](#pyspark.sql.functions.power "Permalink to this definition")

Returns the value of the first argument raised to the power of the second argument.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

the base number.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or float

the exponent number.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the base rased to the power the argument.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(5).select("*", sf.pow("id", 2)).show()
+---+------------+
| id|POWER(id, 2)|
+---+------------+
|  0|         0.0|
|  1|         1.0|
|  2|         4.0|
|  3|         9.0|
|  4|        16.0|
+---+------------+

```


# pyspark.sql.functions.radians — PySpark 4.0.1 documentation
pyspark.sql.functions.radians(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#radians)
[#](#pyspark.sql.functions.radians "Permalink to this definition")

Converts an angle measured in degrees to an approximately equivalent angle measured in radians.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

angle in degrees

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

angle in radians, as if computed by java.lang.Math.toRadians()

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (180), (90), (45), (0) AS TAB(value)"
... ).select("*", sf.radians("value")).show()
+-----+------------------+
|value|    RADIANS(value)|
+-----+------------------+
|  180| 3.141592653589...|
|   90|1.5707963267948...|
|   45|0.7853981633974...|
|    0|               0.0|
+-----+------------------+

```


# pyspark.sql.functions.rand — PySpark 4.0.1 documentation
pyspark.sql.functions.rand(_seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#rand)
[#](#pyspark.sql.functions.rand "Permalink to this definition")

Generates a random column with independent and identically distributed (i.i.d.) samples uniformly distributed in \[0.0, 1.0).

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**seed**int, optional

Seed value for the random generator.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column of random values.

Notes

The function is non-deterministic in general case.

Examples

Example 1: Generate a random column without a seed

```
>>> from pyspark.sql import functions as sf
>>> spark.range(0, 2, 1, 1).select("*", sf.rand()).show() 
+---+-------------------------+
| id|rand(-158884697681280011)|
+---+-------------------------+
|  0|       0.9253464547887...|
|  1|       0.6533254118758...|
+---+-------------------------+

```


Example 2: Generate a random column with a specific seed

```
>>> spark.range(0, 2, 1, 1).select("*", sf.rand(seed=42)).show()
+---+------------------+
| id|          rand(42)|
+---+------------------+
|  0| 0.619189370225...|
|  1|0.5096018842446...|
+---+------------------+

```


# pyspark.sql.functions.randn — PySpark 4.0.1 documentation
pyspark.sql.functions.randn(_seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#randn)
[#](#pyspark.sql.functions.randn "Permalink to this definition")

Generates a random column with independent and identically distributed (i.i.d.) samples from the standard normal distribution.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**seed**int (default: None)

Seed value for the random generator.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column of random values.

Notes

The function is non-deterministic in general case.

Examples

Example 1: Generate a random column without a seed

```
>>> from pyspark.sql import functions as sf
>>> spark.range(0, 2, 1, 1).select("*", sf.randn()).show() 
+---+--------------------------+
| id|randn(3968742514375399317)|
+---+--------------------------+
|  0|      -0.47968645355788...|
|  1|       -0.4950952457305...|
+---+--------------------------+

```


Example 2: Generate a random column with a specific seed

```
>>> spark.range(0, 2, 1, 1).select("*", sf.randn(seed=42)).show()
+---+------------------+
| id|         randn(42)|
+---+------------------+
|  0| 2.384479054241...|
|  1|0.1920934041293...|
+---+------------------+

```

# pyspark.sql.functions.rint — PySpark 4.0.1 documentation
pyspark.sql.functions.rint(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#rint)
[#](#pyspark.sql.functions.rint "Permalink to this definition")

Returns the double value that is closest in value to the argument and is equal to a mathematical integer.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.rint(sf.lit(10.6))).show()
+----------+
|rint(10.6)|
+----------+
|      11.0|
+----------+

```


```
>>> spark.range(1).select(sf.rint(sf.lit(10.3))).show()
+----------+
|rint(10.3)|
+----------+
|      10.0|
+----------+

```


# pyspark.sql.functions.round — PySpark 4.0.1 documentation
pyspark.sql.functions.round(_col_, _scale\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#round)
[#](#pyspark.sql.functions.round "Permalink to this definition")

Round the given value to scale decimal places using HALF\_UP rounding mode if scale >= 0 or at integral part when scale < 0.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column or column name to compute the round on.

**scale**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

An optional parameter to control the rounding behavior.

Changed in version 4.0.0: Support Column type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column for the rounded value.

Examples

Example 1: Compute the rounded of a column value

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.round(sf.lit(2.5))).show()
+-------------+
|round(2.5, 0)|
+-------------+
|          3.0|
+-------------+

```


Example 2: Compute the rounded of a column value with a specified scale

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.round(sf.lit(2.1267), sf.lit(2))).show()
+----------------+
|round(2.1267, 2)|
+----------------+
|            2.13|
+----------------+

```

# pyspark.sql.functions.sec — PySpark 4.0.1 documentation
pyspark.sql.functions.sec(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sec)
[#](#pyspark.sql.functions.sec "Permalink to this definition")

Computes secant of the input column.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Angle in radians

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Secant of the angle.

Examples

Example 1: Compute the secant

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (PI() / 4), (PI() / 16) AS TAB(value)"
... ).select("*", sf.sec("value")).show()
+-------------------+------------------+
|              value|        SEC(value)|
+-------------------+------------------+
| 0.7853981633974...| 1.414213562373...|
|0.19634954084936...|1.0195911582083...|
+-------------------+------------------+

```


Example 2: Compute the secant of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.sec("value")).show()
+-----+----------+
|value|SEC(value)|
+-----+----------+
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```



# pyspark.sql.functions.sign — PySpark 4.0.1 documentation
pyspark.sql.functions.sign(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sign)
[#](#pyspark.sql.functions.sign "Permalink to this definition")

Computes the signum of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(
...     sf.sign(sf.lit(-5)),
...     sf.sign(sf.lit(6)),
...     sf.sign(sf.lit(float('nan'))),
...     sf.sign(sf.lit(None))
... ).show()
+--------+-------+---------+----------+
|sign(-5)|sign(6)|sign(NaN)|sign(NULL)|
+--------+-------+---------+----------+
|    -1.0|    1.0|      NaN|      NULL|
+--------+-------+---------+----------+

```

# pyspark.sql.functions.signum — PySpark 4.0.1 documentation
pyspark.sql.functions.signum(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#signum)
[#](#pyspark.sql.functions.signum "Permalink to this definition")

Computes the signum of the given value.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(
...     sf.signum(sf.lit(-5)),
...     sf.signum(sf.lit(6)),
...     sf.signum(sf.lit(float('nan'))),
...     sf.signum(sf.lit(None))
... ).show()
+----------+---------+-----------+------------+
|SIGNUM(-5)|SIGNUM(6)|SIGNUM(NaN)|SIGNUM(NULL)|
+----------+---------+-----------+------------+
|      -1.0|      1.0|        NaN|        NULL|
+----------+---------+-----------+------------+

```


# pyspark.sql.functions.sin — PySpark 4.0.1 documentation
pyspark.sql.functions.sin(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sin)
[#](#pyspark.sql.functions.sin "Permalink to this definition")

Computes sine of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

sine of the angle, as if computed by java.lang.Math.sin()

Examples

Example 1: Compute the sine

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0.0), (PI() / 2), (PI() / 4) AS TAB(value)"
... ).select("*", sf.sin("value")).show()
+------------------+------------------+
|             value|        SIN(value)|
+------------------+------------------+
|               0.0|               0.0|
|1.5707963267948...|               1.0|
|0.7853981633974...|0.7071067811865...|
+------------------+------------------+

```


Example 2: Compute the sine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.sin("value")).show()
+-----+----------+
|value|SIN(value)|
+-----+----------+
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```


# pyspark.sql.functions.sinh — PySpark 4.0.1 documentation
pyspark.sql.functions.sinh(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sinh)
[#](#pyspark.sql.functions.sinh "Permalink to this definition")

Computes hyperbolic sine of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

hyperbolic angle.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hyperbolic sine of the given value, as if computed by java.lang.Math.sinh()

Examples

Example 1: Compute the hyperbolic sine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-1,), (0,), (1,)], ["value"])
>>> df.select("*", sf.sinh(df.value)).show()
+-----+-------------------+
|value|        SINH(value)|
+-----+-------------------+
|   -1|-1.1752011936438...|
|    0|                0.0|
|    1| 1.1752011936438...|
+-----+-------------------+

```


Example 2: Compute the hyperbolic sine of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.sinh("value")).show()
+-----+-----------+
|value|SINH(value)|
+-----+-----------+
|  NaN|        NaN|
| NULL|       NULL|
+-----+-----------+

```

# pyspark.sql.functions.sqrt — PySpark 4.0.1 documentation
pyspark.sql.functions.sqrt(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sqrt)
[#](#pyspark.sql.functions.sqrt "Permalink to this definition")

Computes the square root of the specified float value.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

column for computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (-1), (0), (1), (4), (NULL) AS TAB(value)"
... ).select("*", sf.sqrt("value")).show()
+-----+-----------+
|value|SQRT(value)|
+-----+-----------+
|   -1|        NaN|
|    0|        0.0|
|    1|        1.0|
|    4|        2.0|
| NULL|       NULL|
+-----+-----------+

```


# pyspark.sql.functions.tan — PySpark 4.0.1 documentation
pyspark.sql.functions.tan(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#tan)
[#](#pyspark.sql.functions.tan "Permalink to this definition")

Computes tangent of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

angle in radians

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

tangent of the given value, as if computed by java.lang.Math.tan()

Examples

Example 1: Compute the tangent

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0.0), (PI() / 4), (PI() / 6) AS TAB(value)"
... ).select("*", sf.tan("value")).show()
+------------------+------------------+
|             value|        TAN(value)|
+------------------+------------------+
|               0.0|               0.0|
|0.7853981633974...|0.9999999999999...|
|0.5235987755982...|0.5773502691896...|
+------------------+------------------+

```


Example 2: Compute the tangent of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.tan("value")).show()
+-----+----------+
|value|TAN(value)|
+-----+----------+
|  NaN|       NaN|
| NULL|      NULL|
+-----+----------+

```

# pyspark.sql.functions.tanh — PySpark 4.0.1 documentation
pyspark.sql.functions.tanh(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#tanh)
[#](#pyspark.sql.functions.tanh "Permalink to this definition")

Computes hyperbolic tangent of the input column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

hyperbolic angle

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hyperbolic tangent of the given value as if computed by java.lang.Math.tanh()

Examples

Example 1: Compute the hyperbolic tangent sine

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-1,), (0,), (1,)], ["value"])
>>> df.select("*", sf.tanh(df.value)).show()
+-----+-------------------+
|value|        TANH(value)|
+-----+-------------------+
|   -1|-0.7615941559557...|
|    0|                0.0|
|    1| 0.7615941559557...|
+-----+-------------------+

```


Example 2: Compute the hyperbolic tangent of invalid values

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (FLOAT('NAN')), (NULL) AS TAB(value)"
... ).select("*", sf.tanh("value")).show()
+-----+-----------+
|value|TANH(value)|
+-----+-----------+
|  NaN|        NaN|
| NULL|       NULL|
+-----+-----------+

```

# pyspark.sql.functions.try_add — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_add(_left_, _right_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_add)
[#](#pyspark.sql.functions.try_add "Permalink to this definition")

Returns the sum of left\`and \`right and the result is null on overflow. The acceptable input types are the same with the + operator.

New in version 3.5.0.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Examples

Example 1: Integer plus Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(1982, 15), (1990, 2)], ["birth", "age"]
... ).select("*", sf.try_add("birth", "age")).show()
+-----+---+-------------------+
|birth|age|try_add(birth, age)|
+-----+---+-------------------+
| 1982| 15|               1997|
| 1990|  2|               1992|
+-----+---+-------------------+

```


Example 2: Date plus Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (DATE('2015-09-30')) AS TAB(date)"
... ).select("*", sf.try_add("date", sf.lit(1))).show()
+----------+----------------+
|      date|try_add(date, 1)|
+----------+----------------+
|2015-09-30|      2015-10-01|
+----------+----------------+

```


Example 3: Date plus Interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (DATE('2015-09-30'), INTERVAL 1 YEAR) AS TAB(date, itvl)"
... ).select("*", sf.try_add("date", "itvl")).show()
+----------+-----------------+-------------------+
|      date|             itvl|try_add(date, itvl)|
+----------+-----------------+-------------------+
|2015-09-30|INTERVAL '1' YEAR|         2016-09-30|
+----------+-----------------+-------------------+

```


Example 4: Interval plus Interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (INTERVAL 1 YEAR, INTERVAL 2 YEAR) AS TAB(itvl1, itvl2)"
... ).select("*", sf.try_add("itvl1", "itvl2")).show()
+-----------------+-----------------+---------------------+
|            itvl1|            itvl2|try_add(itvl1, itvl2)|
+-----------------+-----------------+---------------------+
|INTERVAL '1' YEAR|INTERVAL '2' YEAR|    INTERVAL '3' YEAR|
+-----------------+-----------------+---------------------+

```


Example 5: Overflow results in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     spark.range(1).select(sf.try_add(sf.lit(sys.maxsize), sf.lit(sys.maxsize))).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+-------------------------------------------------+
|try_add(9223372036854775807, 9223372036854775807)|
+-------------------------------------------------+
|                                             NULL|
+-------------------------------------------------+

```


# pyspark.sql.functions.try_divide — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_divide(_left_, _right_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_divide)
[#](#pyspark.sql.functions.try_divide "Permalink to this definition")

Returns dividend/divisor. It always performs floating point division. Its result is always null if divisor is 0.

New in version 3.5.0.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

dividend

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

divisor

Examples

Example 1: Integer divided by Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(6000, 15), (1990, 2), (1234, 0)], ["a", "b"]
... ).select("*", sf.try_divide("a", "b")).show()
+----+---+----------------+
|   a|  b|try_divide(a, b)|
+----+---+----------------+
|6000| 15|           400.0|
|1990|  2|           995.0|
|1234|  0|            NULL|
+----+---+----------------+

```


Example 2: Interval divided by Integer.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(4).select(sf.make_interval(sf.lit(1)).alias("itvl"), "id")
>>> df.select("*", sf.try_divide("itvl", "id")).show()
+-------+---+--------------------+
|   itvl| id|try_divide(itvl, id)|
+-------+---+--------------------+
|1 years|  0|                NULL|
|1 years|  1|             1 years|
|1 years|  2|            6 months|
|1 years|  3|            4 months|
+-------+---+--------------------+

```


Example 3: Exception during division, resulting in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     spark.range(1).select(sf.try_divide("id", sf.lit(0))).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+-----------------+
|try_divide(id, 0)|
+-----------------+
|             NULL|
+-----------------+

```


# pyspark.sql.functions.try_mod — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_mod(_left_, _right_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_mod)
[#](#pyspark.sql.functions.try_mod "Permalink to this definition")

Returns the remainder after dividend/divisor. Its result is always null if divisor is 0.

New in version 4.0.0.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

dividend

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

divisor

Examples

Example 1: Integer divided by Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(6000, 15), (3, 2), (1234, 0)], ["a", "b"]
... ).select("*", sf.try_mod("a", "b")).show()
+----+---+-------------+
|   a|  b|try_mod(a, b)|
+----+---+-------------+
|6000| 15|            0|
|   3|  2|            1|
|1234|  0|         NULL|
+----+---+-------------+

```


Example 2: Exception during division, resulting in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     spark.range(1).select(sf.try_mod("id", sf.lit(0))).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+--------------+
|try_mod(id, 0)|
+--------------+
|          NULL|
+--------------+

```



# pyspark.sql.functions.try_multiply — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_multiply(_left_, _right_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_multiply)
[#](#pyspark.sql.functions.try_multiply "Permalink to this definition")

Returns left\`\*\`right and the result is null on overflow. The acceptable input types are the same with the \* operator.

New in version 3.5.0.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

multiplicand

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

multiplier

Examples

Example 1: Integer multiplied by Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(6000, 15), (1990, 2)], ["a", "b"]
... ).select("*", sf.try_multiply("a", "b")).show()
+----+---+------------------+
|   a|  b|try_multiply(a, b)|
+----+---+------------------+
|6000| 15|             90000|
|1990|  2|              3980|
+----+---+------------------+

```


Example 2: Interval multiplied by Integer.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(6).select(sf.make_interval(sf.col("id"), sf.lit(3)).alias("itvl"), "id")
>>> df.select("*", sf.try_multiply("itvl", "id")).show()
+----------------+---+----------------------+
|            itvl| id|try_multiply(itvl, id)|
+----------------+---+----------------------+
|        3 months|  0|             0 seconds|
|1 years 3 months|  1|      1 years 3 months|
|2 years 3 months|  2|      4 years 6 months|
|3 years 3 months|  3|      9 years 9 months|
|4 years 3 months|  4|              17 years|
|5 years 3 months|  5|     26 years 3 months|
+----------------+---+----------------------+

```


Example 3: Overflow results in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     spark.range(1).select(sf.try_multiply(sf.lit(sys.maxsize), sf.lit(sys.maxsize))).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+------------------------------------------------------+
|try_multiply(9223372036854775807, 9223372036854775807)|
+------------------------------------------------------+
|                                                  NULL|
+------------------------------------------------------+

```


# pyspark.sql.functions.try_subtract — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_subtract(_left_, _right_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_subtract)
[#](#pyspark.sql.functions.try_subtract "Permalink to this definition")

Returns left\-right and the result is null on overflow. The acceptable input types are the same with the \- operator.

New in version 3.5.0.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Examples

Example 1: Integer minus Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(1982, 15), (1990, 2)], ["birth", "age"]
... ).select("*", sf.try_subtract("birth", "age")).show()
+-----+---+------------------------+
|birth|age|try_subtract(birth, age)|
+-----+---+------------------------+
| 1982| 15|                    1967|
| 1990|  2|                    1988|
+-----+---+------------------------+

```


Example 2: Date minus Integer.

```
>>> import pyspark.sql.functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (DATE('2015-10-01')) AS TAB(date)"
... ).select("*", sf.try_subtract("date", sf.lit(1))).show()
+----------+---------------------+
|      date|try_subtract(date, 1)|
+----------+---------------------+
|2015-10-01|           2015-09-30|
+----------+---------------------+

```


Example 3: Date minus Interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (DATE('2015-09-30'), INTERVAL 1 YEAR) AS TAB(date, itvl)"
... ).select("*", sf.try_subtract("date", "itvl")).show()
+----------+-----------------+------------------------+
|      date|             itvl|try_subtract(date, itvl)|
+----------+-----------------+------------------------+
|2015-09-30|INTERVAL '1' YEAR|              2014-09-30|
+----------+-----------------+------------------------+

```


Example 4: Interval minus Interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (INTERVAL 1 YEAR, INTERVAL 2 YEAR) AS TAB(itvl1, itvl2)"
... ).select("*", sf.try_subtract("itvl1", "itvl2")).show()
+-----------------+-----------------+--------------------------+
|            itvl1|            itvl2|try_subtract(itvl1, itvl2)|
+-----------------+-----------------+--------------------------+
|INTERVAL '1' YEAR|INTERVAL '2' YEAR|        INTERVAL '-1' YEAR|
+-----------------+-----------------+--------------------------+

```


Example 5: Overflow results in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     spark.range(1).select(sf.try_subtract(sf.lit(-sys.maxsize), sf.lit(sys.maxsize))).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+-------------------------------------------------------+
|try_subtract(-9223372036854775807, 9223372036854775807)|
+-------------------------------------------------------+
|                                                   NULL|
+-------------------------------------------------------+

```




# pyspark.sql.functions.unhex — PySpark 4.0.1 documentation
pyspark.sql.functions.unhex(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unhex)
[#](#pyspark.sql.functions.unhex "Permalink to this definition")

Inverse of hex. Interprets each pair of characters as a hexadecimal number and converts to the byte representation of number.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string representation of given hexadecimal value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('414243',)], ['a'])
>>> df.select('*', sf.unhex('a')).show()
+------+----------+
|     a|  unhex(a)|
+------+----------+
|414243|[41 42 43]|
+------+----------+

```


# pyspark.sql.functions.uniform — PySpark 4.0.1 documentation
pyspark.sql.functions.uniform(_min_, _max_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#uniform)
[#](#pyspark.sql.functions.uniform "Permalink to this definition")

Returns a random value with independent and identically distributed (i.i.d.) values with the specified range of numbers. The random seed is optional. The provided numbers specifying the minimum and maximum values of the range must be constant. If both of these numbers are integers, then the result will also be an integer. Otherwise if one or both of these are floating-point numbers, then the result will also be a floating-point number.

New in version 4.0.0.

Parameters

**min**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), int, or float

Minimum value in the range.

**max**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), int, or float

Maximum value in the range.

**seed**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

Optional random number seed to use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The generated random number within the specified range.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(0, 10, 1, 1).select(sf.uniform(5, 105, 3)).show()
+------------------+
|uniform(5, 105, 3)|
+------------------+
|                30|
|                71|
|                99|
|                77|
|                16|
|                25|
|                89|
|                80|
|                51|
|                83|
+------------------+

```


# pyspark.sql.functions.width_bucket — PySpark 4.0.1 documentation
pyspark.sql.functions.width\_bucket(_v_, _min_, _max_, _numBucket_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#width_bucket)
[#](#pyspark.sql.functions.width_bucket "Permalink to this definition")

Returns the bucket number into which the value of this expression would fall after being evaluated. Note that input arguments must follow conditions listed below; otherwise, the method will return null.

New in version 3.5.0.

Parameters

**v**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

value to compute a bucket number in the histogram

**min**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

minimum value of the histogram

**max**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

maximum value of the histogram

**numBucket**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), column name or int

the number of buckets

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the bucket number into which the value would fall after being evaluated

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (5.3, 0.2, 10.6, 5),
...     (-2.1, 1.3, 3.4, 3),
...     (8.1, 0.0, 5.7, 4),
...     (-0.9, 5.2, 0.5, 2)],
...     ['v', 'min', 'max', 'n'])
>>> df.select("*", sf.width_bucket('v', 'min', 'max', 'n')).show()
+----+---+----+---+----------------------------+
|   v|min| max|  n|width_bucket(v, min, max, n)|
+----+---+----+---+----------------------------+
| 5.3|0.2|10.6|  5|                           3|
|-2.1|1.3| 3.4|  3|                           0|
| 8.1|0.0| 5.7|  4|                           5|
|-0.9|5.2| 0.5|  2|                           3|
+----+---+----+---+----------------------------+

```


# pyspark.sql.functions.ascii — PySpark 4.0.1 documentation
pyspark.sql.functions.ascii(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ascii)
[#](#pyspark.sql.functions.ascii "Permalink to this definition")

Computes the numeric value of the first character of the string column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

numeric value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["Spark", "PySpark", "Pandas API"], "STRING")
>>> df.select("*", sf.ascii("value")).show()
+----------+------------+
|     value|ascii(value)|
+----------+------------+
|     Spark|          83|
|   PySpark|          80|
|Pandas API|          80|
+----------+------------+

```


# pyspark.sql.functions.base64 — PySpark 4.0.1 documentation
pyspark.sql.functions.base64(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#base64)
[#](#pyspark.sql.functions.base64 "Permalink to this definition")

Computes the BASE64 encoding of a binary column and returns it as a string column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

BASE64 encoding of string value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["Spark", "PySpark", "Pandas API"], "STRING")
>>> df.select("*", sf.base64("value")).show()
+----------+----------------+
|     value|   base64(value)|
+----------+----------------+
|     Spark|        U3Bhcms=|
|   PySpark|    UHlTcGFyaw==|
|Pandas API|UGFuZGFzIEFQSQ==|
+----------+----------------+

```


# pyspark.sql.functions.bit_length — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.bit\_length

pyspark.sql.functions.bit\_length(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bit_length)
[#](#pyspark.sql.functions.bit_length "Permalink to this definition")

Calculates the bit length for the specified string column.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Source column or strings

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Bit length of the col

Examples

```
>>> from pyspark.sql.functions import bit_length
>>> spark.createDataFrame([('cat',), ( '🐈',)], ['cat']) \
...      .select(bit_length('cat')).collect()
    [Row(bit_length(cat)=24), Row(bit_length(cat)=32)]

```


# pyspark.sql.functions.btrim — PySpark 4.0.1 documentation
pyspark.sql.functions.btrim(_str_, _trim\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#btrim)
[#](#pyspark.sql.functions.btrim "Permalink to this definition")

Remove the leading and trailing trim characters from str.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**trim**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

The trim string characters to trim, the default value is a single space

Examples

```
>>> df = spark.createDataFrame([("SSparkSQLS", "SL", )], ['a', 'b'])
>>> df.select(btrim(df.a, df.b).alias('r')).collect()
[Row(r='parkSQ')]

```


```
>>> df = spark.createDataFrame([("    SparkSQL   ",)], ['a'])
>>> df.select(btrim(df.a).alias('r')).collect()
[Row(r='SparkSQL')]

```


# pyspark.sql.functions.char — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.char

pyspark.sql.functions.char(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#char)
[#](#pyspark.sql.functions.char "Permalink to this definition")

Returns the ASCII character having the binary equivalent to col. If col is larger than 256 the result is equivalent to char(col % 256)

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.char(sf.lit(65))).show()
+--------+
|char(65)|
+--------+
|       A|
+--------+

```

# pyspark.sql.functions.char_length — PySpark 4.0.1 documentation
pyspark.sql.functions.char\_length(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#char_length)
[#](#pyspark.sql.functions.char_length "Permalink to this definition")

Returns the character length of string data or number of bytes of binary data. The length of string data includes the trailing spaces. The length of binary data includes binary zeros.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.char_length(sf.lit("SparkSQL"))).show()
+---------------------+
|char_length(SparkSQL)|
+---------------------+
|                    8|
+---------------------+

```


# pyspark.sql.functions.character_length — PySpark 4.0.1 documentation
pyspark.sql.functions.character\_length(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#character_length)
[#](#pyspark.sql.functions.character_length "Permalink to this definition")

Returns the character length of string data or number of bytes of binary data. The length of string data includes the trailing spaces. The length of binary data includes binary zeros.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.character_length(sf.lit("SparkSQL"))).show()
+--------------------------+
|character_length(SparkSQL)|
+--------------------------+
|                         8|
+--------------------------+

```

# pyspark.sql.functions.collate — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.collate

pyspark.sql.functions.collate(_col_, _collation_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#collate)
[#](#pyspark.sql.functions.collate "Permalink to this definition")

Marks a given column with specified collation.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Target string column to work on.

**collation**str

Target collation name.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of string type, where each value has the specified collation.

# pyspark.sql.functions.collation — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.collation

pyspark.sql.functions.collation(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#collation)
[#](#pyspark.sql.functions.collation "Permalink to this definition")

Returns the collation name of a given column.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Target string column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

collation name of a given expression.

Examples

```
>>> df = spark.createDataFrame([('name',)], ['dt'])
>>> df.select(collation('dt').alias('collation')).show(truncate=False)
+--------------------------+
|collation                 |
+--------------------------+
|SYSTEM.BUILTIN.UTF8_BINARY|
+--------------------------+

```
# pyspark.sql.functions.concat_ws — PySpark 4.0.1 documentation
pyspark.sql.functions.concat\_ws(_sep_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#concat_ws)
[#](#pyspark.sql.functions.concat_ws "Permalink to this definition")

Concatenates multiple input string columns together into a single string column, using the given separator.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**sep**literal string

words separator.

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

list of columns to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string of concatenated words.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("abcd", "123")], ["s", "d"])
>>> df.select("*", sf.concat_ws("-", df.s, "d", sf.lit("xyz"))).show()
+----+---+-----------------------+
|   s|  d|concat_ws(-, s, d, xyz)|
+----+---+-----------------------+
|abcd|123|           abcd-123-xyz|
+----+---+-----------------------+

```


# pyspark.sql.functions.contains — PySpark 4.0.1 documentation
pyspark.sql.functions.contains(_left_, _right_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#contains)
[#](#pyspark.sql.functions.contains "Permalink to this definition")

Returns a boolean. The value is True if right is found inside left. Returns NULL if either input expression is NULL. Otherwise, returns False. Both left or right must be of STRING or BINARY type.

New in version 3.5.0.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The input column or strings to check, may be NULL.

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The input column or strings to find, may be NULL.

Examples

```
>>> df = spark.createDataFrame([("Spark SQL", "Spark")], ['a', 'b'])
>>> df.select(contains(df.a, df.b).alias('r')).collect()
[Row(r=True)]

```


```
>>> df = spark.createDataFrame([("414243", "4243",)], ["c", "d"])
>>> df = df.select(to_binary("c").alias("c"), to_binary("d").alias("d"))
>>> df.printSchema()
root
 |-- c: binary (nullable = true)
 |-- d: binary (nullable = true)
>>> df.select(contains("c", "d"), contains("d", "c")).show()
+--------------+--------------+
|contains(c, d)|contains(d, c)|
+--------------+--------------+
|          true|         false|
+--------------+--------------+

```


# pyspark.sql.functions.decode — PySpark 4.0.1 documentation
pyspark.sql.functions.decode(_col_, _charset_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#decode)
[#](#pyspark.sql.functions.decode "Permalink to this definition")

Computes the first argument into a string from a binary using the provided character set (one of ‘US-ASCII’, ‘ISO-8859-1’, ‘UTF-8’, ‘UTF-16BE’, ‘UTF-16LE’, ‘UTF-16’, ‘UTF-32’).

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**charset**literal string

charset to use to decode to.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(b"abcd",)], ["a"])
>>> df.select("*", sf.decode("a", "UTF-8")).show()
+-------------+----------------+
|            a|decode(a, UTF-8)|
+-------------+----------------+
|[61 62 63 64]|            abcd|
+-------------+----------------+

```

# pyspark.sql.functions.elt — PySpark 4.0.1 documentation
pyspark.sql.functions.elt(_\*inputs_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#elt)
[#](#pyspark.sql.functions.elt "Permalink to this definition")

Returns the n\-th input, e.g., returns input2 when n is 2. The function returns NULL if the index exceeds the length of the array and spark.sql.ansi.enabled is set to false. If spark.sql.ansi.enabled is set to true, it throws ArrayIndexOutOfBoundsException for invalid indices.

New in version 3.5.0.

Parameters

**inputs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input columns or strings.

Examples

```
>>> df = spark.createDataFrame([(1, "scala", "java")], ['a', 'b', 'c'])
>>> df.select(elt(df.a, df.b, df.c).alias('r')).collect()
[Row(r='scala')]

```



# pyspark.sql.functions.encode — PySpark 4.0.1 documentation
pyspark.sql.functions.encode(_col_, _charset_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#encode)
[#](#pyspark.sql.functions.encode "Permalink to this definition")

Computes the first argument into a binary from a string using the provided character set (one of ‘US-ASCII’, ‘ISO-8859-1’, ‘UTF-8’, ‘UTF-16BE’, ‘UTF-16LE’, ‘UTF-16’, ‘UTF-32’).

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**charset**literal string

charset to use to encode.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("abcd",)], ["c"])
>>> df.select("*", sf.encode("c", "UTF-8")).show()
+----+----------------+
|   c|encode(c, UTF-8)|
+----+----------------+
|abcd|   [61 62 63 64]|
+----+----------------+

```

# pyspark.sql.functions.endswith — PySpark 4.0.1 documentation
pyspark.sql.functions.endswith(_str_, _suffix_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#endswith)
[#](#pyspark.sql.functions.endswith "Permalink to this definition")

Returns a boolean. The value is True if str ends with suffix. Returns NULL if either input expression is NULL. Otherwise, returns False. Both str or suffix must be of STRING or BINARY type.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string.

**suffix**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string, the suffix.

Examples

```
>>> df = spark.createDataFrame([("Spark SQL", "Spark",)], ["a", "b"])
>>> df.select(endswith(df.a, df.b).alias('r')).collect()
[Row(r=False)]

```


```
>>> df = spark.createDataFrame([("414243", "4243",)], ["e", "f"])
>>> df = df.select(to_binary("e").alias("e"), to_binary("f").alias("f"))
>>> df.printSchema()
root
 |-- e: binary (nullable = true)
 |-- f: binary (nullable = true)
>>> df.select(endswith("e", "f"), endswith("f", "e")).show()
+--------------+--------------+
|endswith(e, f)|endswith(f, e)|
+--------------+--------------+
|          true|         false|
+--------------+--------------+

```


# pyspark.sql.functions.find_in_set — PySpark 4.0.1 documentation
pyspark.sql.functions.find\_in\_set(_str_, _str\_array_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#find_in_set)
[#](#pyspark.sql.functions.find_in_set "Permalink to this definition")

Returns the index (1-based) of the given string (str) in the comma-delimited list (strArray). Returns 0, if the string was not found or if the given string (str) contains a comma.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The given string to be found.

**str\_array**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The comma-delimited list.

Examples

```
>>> df = spark.createDataFrame([("ab", "abc,b,ab,c,def")], ['a', 'b'])
>>> df.select(find_in_set(df.a, df.b).alias('r')).collect()
[Row(r=3)]

```


# pyspark.sql.functions.format_number — PySpark 4.0.1 documentation
pyspark.sql.functions.format\_number(_col_, _d_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#format_number)
[#](#pyspark.sql.functions.format_number "Permalink to this definition")

Formats the number X to a format like ‘#,–#,–#.–’, rounded to d decimal places with HALF\_EVEN round mode, and returns the result as a string.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the column name of the numeric value to be formatted

**d**int

the N decimal places

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column of formatted results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(5,)], ["a"])
>>> df.select("*", sf.format_number("a", 4), sf.format_number(df.a, 6)).show()
+---+-------------------+-------------------+
|  a|format_number(a, 4)|format_number(a, 6)|
+---+-------------------+-------------------+
|  5|             5.0000|           5.000000|
+---+-------------------+-------------------+

```




# pyspark.sql.functions.format_string — PySpark 4.0.1 documentation
pyspark.sql.functions.format\_string(_format_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#format_string)
[#](#pyspark.sql.functions.format_string "Permalink to this definition")

Formats the arguments in printf-style and returns the result as a string column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**format**literal string

string that can contain embedded format tags and used as result column’s value

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")s to be used in formatting

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column of formatted results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(5, "hello")], ["a", "b"])
>>> df.select("*", sf.format_string('%d %s', "a", df.b)).show()
+---+-----+--------------------------+
|  a|    b|format_string(%d %s, a, b)|
+---+-----+--------------------------+
|  5|hello|                   5 hello|
+---+-----+--------------------------+

```



# pyspark.sql.functions.initcap — PySpark 4.0.1 documentation
pyspark.sql.functions.initcap(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#initcap)
[#](#pyspark.sql.functions.initcap "Permalink to this definition")

Translate the first letter of each word to upper case in the sentence.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string with all first letters are uppercase in each word.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ab cd',)], ['a'])
>>> df.select("*", sf.initcap("a")).show()
+-----+----------+
|    a|initcap(a)|
+-----+----------+
|ab cd|     Ab Cd|
+-----+----------+

```

# pyspark.sql.functions.instr — PySpark 4.0.1 documentation
pyspark.sql.functions.instr(_str_, _substr_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#instr)
[#](#pyspark.sql.functions.instr "Permalink to this definition")

Locate the position of the first occurrence of substr column in the given string. Returns null if either of the arguments are null.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**substr**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

substring to look for.

Changed in version 4.0.0: substr now accepts column.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

location of the first occurrence of the substring as integer.

Notes

The position is not zero based, but 1 based index. Returns 0 if substr could not be found in str.

Examples

Example 1: Using a literal string as the ‘substring’

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("abcd",), ("xyz",)], ["s",])
>>> df.select("*", sf.instr(df.s, "b")).show()
+----+-----------+
|   s|instr(s, b)|
+----+-----------+
|abcd|          2|
| xyz|          0|
+----+-----------+

```


Example 2: Using a Column ‘substring’

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("abcd",), ("xyz",)], ["s",])
>>> df.select("*", sf.instr("s", sf.lit("abc").substr(0, 2))).show()
+----+---------------------------+
|   s|instr(s, substr(abc, 0, 2))|
+----+---------------------------+
|abcd|                          1|
| xyz|                          0|
+----+---------------------------+

```
# pyspark.sql.functions.is_valid_utf8 — PySpark 4.0.1 documentation
pyspark.sql.functions.is\_valid\_utf8(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#is_valid_utf8)
[#](#pyspark.sql.functions.is_valid_utf8 "Permalink to this definition")

Returns true if the input is a valid UTF-8 string, otherwise returns false.

New in version 4.0.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of strings, each representing a UTF-8 byte sequence.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

whether the input string is a valid UTF-8 string.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.is_valid_utf8(sf.lit("SparkSQL"))).show()
+-----------------------+
|is_valid_utf8(SparkSQL)|
+-----------------------+
|                   true|
+-----------------------+

```


# pyspark.sql.functions.lcase — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.lcase

pyspark.sql.functions.lcase(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#lcase)
[#](#pyspark.sql.functions.lcase "Permalink to this definition")

Returns str with all characters changed to lowercase.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.lcase(sf.lit("Spark"))).show()
+------------+
|lcase(Spark)|
+------------+
|       spark|
+------------+

```



# pyspark.sql.functions.left — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.left

pyspark.sql.functions.left(_str_, _len_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#left)
[#](#pyspark.sql.functions.left "Permalink to this definition")

Returns the leftmost len\`(\`len can be string type) characters from the string str, if len is less or equal than 0 the result is an empty string.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings, the leftmost len.

Examples

```
>>> df = spark.createDataFrame([("Spark SQL", 3,)], ['a', 'b'])
>>> df.select(left(df.a, df.b).alias('r')).collect()
[Row(r='Spa')]

```

# pyspark.sql.functions.length — PySpark 4.0.1 documentation
pyspark.sql.functions.length(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#length)
[#](#pyspark.sql.functions.length "Permalink to this definition")

Computes the character length of string data or number of bytes of binary data. The length of character data includes the trailing spaces. The length of binary data includes binary zeros.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

length of the value.

Examples

```
>>> spark.createDataFrame([('ABC ',)], ['a']).select(length('a').alias('length')).collect()
[Row(length=4)]

```


# pyspark.sql.functions.levenshtein — PySpark 4.0.1 documentation
pyspark.sql.functions.levenshtein(_left_, _right_, _threshold\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#levenshtein)
[#](#pyspark.sql.functions.levenshtein "Permalink to this definition")

Computes the Levenshtein distance of the two given strings.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first column value.

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

second column value.

**threshold**int, optional

if set when the levenshtein distance of the two given strings less than or equal to a given threshold then return result distance, or -1

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Levenshtein distance as integer value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('kitten', 'sitting',)], ['l', 'r'])
>>> df.select('*', sf.levenshtein('l', 'r')).show()
+------+-------+-----------------+
|     l|      r|levenshtein(l, r)|
+------+-------+-----------------+
|kitten|sitting|                3|
+------+-------+-----------------+

```


```
>>> df.select('*', sf.levenshtein(df.l, df.r, 2)).show()
+------+-------+--------------------+
|     l|      r|levenshtein(l, r, 2)|
+------+-------+--------------------+
|kitten|sitting|                  -1|
+------+-------+--------------------+

```


# pyspark.sql.functions.locate — PySpark 4.0.1 documentation
pyspark.sql.functions.locate(_substr_, _str_, _pos\=1_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#locate)
[#](#pyspark.sql.functions.locate "Permalink to this definition")

Locate the position of the first occurrence of substr in a string column, after position pos.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**substr**literal string

a string

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

a Column of [`pyspark.sql.types.StringType`](about:blank/pyspark.sql.types.StringType.html#pyspark.sql.types.StringType "pyspark.sql.types.StringType")

**pos**int, optional

start position (zero based)

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

position of the substring.

Notes

The position is not zero based, but 1 based index. Returns 0 if substr could not be found in str.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('abcd',)], ['s',])
>>> df.select('*', sf.locate('b', 's', 1)).show()
+----+---------------+
|   s|locate(b, s, 1)|
+----+---------------+
|abcd|              2|
+----+---------------+

```


```
>>> df.select('*', sf.locate('b', df.s, 3)).show()
+----+---------------+
|   s|locate(b, s, 3)|
+----+---------------+
|abcd|              0|
+----+---------------+

```

# pyspark.sql.functions.lower — PySpark 4.0.1 documentation
pyspark.sql.functions.lower(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#lower)
[#](#pyspark.sql.functions.lower "Permalink to this definition")

Converts a string expression to lower case.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

lower case values.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["Spark", "PySpark", "Pandas API"], "STRING")
>>> df.select("*", sf.lower("value")).show()
+----------+------------+
|     value|lower(value)|
+----------+------------+
|     Spark|       spark|
|   PySpark|     pyspark|
|Pandas API|  pandas api|
+----------+------------+

```



# pyspark.sql.functions.lpad — PySpark 4.0.1 documentation
pyspark.sql.functions.lpad(_col_, _len_, _pad_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#lpad)
[#](#pyspark.sql.functions.lpad "Permalink to this definition")

Left-pad the string column to width len with pad.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

length of the final string.

Changed in version 4.0.0: pattern now accepts column.

**pad**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

chars to prepend.

Changed in version 4.0.0: pattern now accepts column.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

left padded result.

Examples

Example 1: Pad with a literal string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('abcd',), ('xyz',), ('12',)], ['s',])
>>> df.select("*", sf.lpad(df.s, 6, '#')).show()
+----+-------------+
|   s|lpad(s, 6, #)|
+----+-------------+
|abcd|       ##abcd|
| xyz|       ###xyz|
|  12|       ####12|
+----+-------------+

```


Example 2: Pad with a bytes column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('abcd',), ('xyz',), ('12',)], ['s',])
>>> df.select("*", sf.lpad(df.s, 6, sf.lit(b"uv"))).show()
+----+-------------------+
|   s|lpad(s, 6, X'7576')|
+----+-------------------+
|abcd|             uvabcd|
| xyz|             uvuxyz|
|  12|             uvuv12|
+----+-------------------+

```


# pyspark.sql.functions.ltrim — PySpark 4.0.1 documentation
pyspark.sql.functions.ltrim(_col_, _trim\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ltrim)
[#](#pyspark.sql.functions.ltrim "Permalink to this definition")

Trim the spaces from left end for the specified string value.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**trim**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The trim string characters to trim, the default value is a single space

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

left trimmed values.

Examples

Example 1: Trim the spaces

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["   Spark", "Spark  ", " Spark"], "STRING")
>>> df.select("*", sf.ltrim("value")).show()
+--------+------------+
|   value|ltrim(value)|
+--------+------------+
|   Spark|       Spark|
| Spark  |     Spark  |
|   Spark|       Spark|
+--------+------------+

```


Example 2: Trim specified characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["***Spark", "Spark**", "*Spark"], "STRING")
>>> df.select("*", sf.ltrim("value", sf.lit("*"))).show()
+--------+--------------------------+
|   value|TRIM(LEADING * FROM value)|
+--------+--------------------------+
|***Spark|                     Spark|
| Spark**|                   Spark**|
|  *Spark|                     Spark|
+--------+--------------------------+

```


Example 3: Trim a column containing different characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("**Spark*", "*"), ("==Spark=", "=")], ["value", "t"])
>>> df.select("*", sf.ltrim("value", "t")).show()
+--------+---+--------------------------+
|   value|  t|TRIM(LEADING t FROM value)|
+--------+---+--------------------------+
|**Spark*|  *|                    Spark*|
|==Spark=|  =|                    Spark=|
+--------+---+--------------------------+

```

# pyspark.sql.functions.make_valid_utf8 — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_valid\_utf8(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_valid_utf8)
[#](#pyspark.sql.functions.make_valid_utf8 "Permalink to this definition")

Returns a new string in which all invalid UTF-8 byte sequences, if any, are replaced by the Unicode replacement character (U+FFFD).

New in version 4.0.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of strings, each representing a UTF-8 byte sequence.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the valid UTF-8 version of the given input string.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.make_valid_utf8(sf.lit("SparkSQL"))).show()
+-------------------------+
|make_valid_utf8(SparkSQL)|
+-------------------------+
|                 SparkSQL|
+-------------------------+

```


# pyspark.sql.functions.mask — PySpark 4.0.1 documentation
pyspark.sql.functions.mask(_col_, _upperChar\=None_, _lowerChar\=None_, _digitChar\=None_, _otherChar\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#mask)
[#](#pyspark.sql.functions.mask "Permalink to this definition")

Masks the given string value. This can be useful for creating copies of tables with sensitive information removed.

New in version 3.5.0.

Parameters

**col: :class:\`~pyspark.sql.Column\` or str**

target column to compute on.

**upperChar: :class:\`~pyspark.sql.Column\` or str, optional**

character to replace upper-case characters with. Specify NULL to retain original character.

**lowerChar: :class:\`~pyspark.sql.Column\` or str, optional**

character to replace lower-case characters with. Specify NULL to retain original character.

**digitChar: :class:\`~pyspark.sql.Column\` or str, optional**

character to replace digit characters with. Specify NULL to retain original character.

**otherChar: :class:\`~pyspark.sql.Column\` or str, optional**

character to replace all other characters with. Specify NULL to retain original character.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Examples

```
>>> df = spark.createDataFrame([("AbCD123-@$#",), ("abcd-EFGH-8765-4321",)], ['data'])
>>> df.select(mask(df.data).alias('r')).collect()
[Row(r='XxXXnnn-@$#'), Row(r='xxxx-XXXX-nnnn-nnnn')]
>>> df.select(mask(df.data, lit('Y')).alias('r')).collect()
[Row(r='YxYYnnn-@$#'), Row(r='xxxx-YYYY-nnnn-nnnn')]
>>> df.select(mask(df.data, lit('Y'), lit('y')).alias('r')).collect()
[Row(r='YyYYnnn-@$#'), Row(r='yyyy-YYYY-nnnn-nnnn')]
>>> df.select(mask(df.data, lit('Y'), lit('y'), lit('d')).alias('r')).collect()
[Row(r='YyYYddd-@$#'), Row(r='yyyy-YYYY-dddd-dddd')]
>>> df.select(mask(df.data, lit('Y'), lit('y'), lit('d'), lit('*')).alias('r')).collect()
[Row(r='YyYYddd****'), Row(r='yyyy*YYYY*dddd*dddd')]

```



# pyspark.sql.functions.octet_length — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.octet\_length

pyspark.sql.functions.octet\_length(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#octet_length)
[#](#pyspark.sql.functions.octet_length "Permalink to this definition")

Calculates the byte length for the specified string column.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Source column or strings

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Byte length of the col

Examples

```
>>> from pyspark.sql.functions import octet_length
>>> spark.createDataFrame([('cat',), ( '🐈',)], ['cat']) \
...      .select(octet_length('cat')).collect()
    [Row(octet_length(cat)=3), Row(octet_length(cat)=4)]

```



# pyspark.sql.functions.overlay — PySpark 4.0.1 documentation
pyspark.sql.functions.overlay(_src_, _replace_, _pos_, _len\=\- 1_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#overlay)
[#](#pyspark.sql.functions.overlay "Permalink to this definition")

Overlay the specified portion of src with replace, starting from byte position pos of src and proceeding for len bytes.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**src**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the string that will be replaced

**replace**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the substitution string

**pos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

the starting position in src

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int, optional

the number of bytes to replace in src string by ‘replace’ defaults to -1, which represents the length of the ‘replace’ string

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string with replaced values.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("SPARK_SQL", "CORE")], ("x", "y"))
>>> df.select("*", sf.overlay("x", df.y, 7)).show()
+---------+----+--------------------+
|        x|   y|overlay(x, y, 7, -1)|
+---------+----+--------------------+
|SPARK_SQL|CORE|          SPARK_CORE|
+---------+----+--------------------+

```


```
>>> df.select("*", sf.overlay("x", df.y, 7, 0)).show()
+---------+----+-------------------+
|        x|   y|overlay(x, y, 7, 0)|
+---------+----+-------------------+
|SPARK_SQL|CORE|      SPARK_CORESQL|
+---------+----+-------------------+

```


```
>>> df.select("*", sf.overlay("x", "y", 7, 2)).show()
+---------+----+-------------------+
|        x|   y|overlay(x, y, 7, 2)|
+---------+----+-------------------+
|SPARK_SQL|CORE|        SPARK_COREL|
+---------+----+-------------------+

```

# pyspark.sql.functions.position — PySpark 4.0.1 documentation
pyspark.sql.functions.position(_substr_, _str_, _start\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#position)
[#](#pyspark.sql.functions.position "Permalink to this definition")

Returns the position of the first occurrence of substr in str after position start. The given start and return value are 1-based.

New in version 3.5.0.

Parameters

**substr**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string, substring.

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string.

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

A column of string, start position.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("bar", "foobarbar", 5,)], ["a", "b", "c"]
... ).select(sf.position("a", "b", "c")).show()
+-----------------+
|position(a, b, c)|
+-----------------+
|                7|
+-----------------+

```


```
>>> spark.createDataFrame(
...     [("bar", "foobarbar", 5,)], ["a", "b", "c"]
... ).select(sf.position("a", "b")).show()
+-----------------+
|position(a, b, 1)|
+-----------------+
|                4|
+-----------------+

```


# pyspark.sql.functions.printf — PySpark 4.0.1 documentation
pyspark.sql.functions.printf(_format_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#printf)
[#](#pyspark.sql.functions.printf "Permalink to this definition")

Formats the arguments in printf-style and returns the result as a string column.

New in version 3.5.0.

Parameters

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

string that can contain embedded format tags and used as result column’s value

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")s to be used in formatting

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("aa%d%s", 123, "cc",)], ["a", "b", "c"]
... ).select(sf.printf("a", "b", "c")).show()
+---------------+
|printf(a, b, c)|
+---------------+
|        aa123cc|
+---------------+

```


# pyspark.sql.functions.randstr — PySpark 4.0.1 documentation
pyspark.sql.functions.randstr(_length_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#randstr)
[#](#pyspark.sql.functions.randstr "Permalink to this definition")

Returns a string of the specified length whose characters are chosen uniformly at random from the following pool of characters: 0-9, a-z, A-Z. The random seed is optional. The string length must be a constant two-byte or four-byte integer (SMALLINT or INT, respectively).

New in version 4.0.0.

Parameters

**length**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

Number of characters in the string to generate.

**seed**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

Optional random number seed to use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The generated random string with the specified length.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(0, 10, 1, 1).select(sf.randstr(16, 3)).show()
+----------------+
|  randstr(16, 3)|
+----------------+
|nurJIpH4cmmMnsCG|
|fl9YtT5m01trZtIt|
|PD19rAgscTHS7qQZ|
|2CuAICF5UJOruVv4|
|kNZEs8nDpJEoz3Rl|
|OXiU0KN5eaXfjXFs|
|qfnTM1BZAHtN0gBV|
|1p8XiSKwg33KnRPK|
|od5y5MucayQq1bKK|
|tklYPmKmc5sIppWM|
+----------------+

```

# pyspark.sql.functions.regexp_count — PySpark 4.0.1 documentation
pyspark.sql.functions.regexp\_count(_str_, _regexp_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_count)
[#](#pyspark.sql.functions.regexp_count "Permalink to this definition")

Returns a count of the number of times that the Java regex pattern regexp is matched in the string str.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

regex pattern to apply.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of times that a Java regex pattern is matched in the string.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("1a 2b 14m", r"\d+")], ["str", "regexp"])
>>> df.select('*', sf.regexp_count('str', sf.lit(r'\d+'))).show()
+---------+------+----------------------+
|      str|regexp|regexp_count(str, \d+)|
+---------+------+----------------------+
|1a 2b 14m|   \d+|                     3|
+---------+------+----------------------+

```


```
>>> df.select('*', sf.regexp_count('str', sf.lit(r'mmm'))).show()
+---------+------+----------------------+
|      str|regexp|regexp_count(str, mmm)|
+---------+------+----------------------+
|1a 2b 14m|   \d+|                     0|
+---------+------+----------------------+

```


```
>>> df.select('*', sf.regexp_count("str", sf.col("regexp"))).show()
+---------+------+-------------------------+
|      str|regexp|regexp_count(str, regexp)|
+---------+------+-------------------------+
|1a 2b 14m|   \d+|                        3|
+---------+------+-------------------------+

```


```
>>> df.select('*', sf.regexp_count(sf.col('str'), "regexp")).show()
+---------+------+-------------------------+
|      str|regexp|regexp_count(str, regexp)|
+---------+------+-------------------------+
|1a 2b 14m|   \d+|                        3|
+---------+------+-------------------------+

```




# pyspark.sql.functions.regexp_extract — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.regexp\_extract

pyspark.sql.functions.regexp\_extract(_str_, _pattern_, _idx_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_extract)
[#](#pyspark.sql.functions.regexp_extract "Permalink to this definition")

Extract a specific group matched by the Java regex regexp, from the specified string column. If the regex did not match, or the specified group did not match, an empty string is returned.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**pattern**str

regex pattern to apply.

**idx**int

matched group id.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

matched value specified by idx group id.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('100-200',)], ['str'])
>>> df.select('*', sf.regexp_extract('str', r'(\d+)-(\d+)', 1)).show()
+-------+-----------------------------------+
|    str|regexp_extract(str, (\d+)-(\d+), 1)|
+-------+-----------------------------------+
|100-200|                                100|
+-------+-----------------------------------+

```


```
>>> df = spark.createDataFrame([('foo',)], ['str'])
>>> df.select('*', sf.regexp_extract('str', r'(\d+)', 1)).show()
+---+-----------------------------+
|str|regexp_extract(str, (\d+), 1)|
+---+-----------------------------+
|foo|                             |
+---+-----------------------------+

```


```
>>> df = spark.createDataFrame([('aaaac',)], ['str'])
>>> df.select('*', sf.regexp_extract(sf.col('str'), '(a+)(b)?(c)', 2)).show()
+-----+-----------------------------------+
|  str|regexp_extract(str, (a+)(b)?(c), 2)|
+-----+-----------------------------------+
|aaaac|                                   |
+-----+-----------------------------------+

```

# pyspark.sql.functions.regexp_extract_all — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.regexp\_extract\_all

pyspark.sql.functions.regexp\_extract\_all(_str_, _regexp_, _idx\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_extract_all)
[#](#pyspark.sql.functions.regexp_extract_all "Permalink to this definition")

Extract all strings in the str that match the Java regex regexp and corresponding to the regex group index.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

regex pattern to apply.

**idx**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

matched group id.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

all strings in the str that match a Java regex and corresponding to the regex group index.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("100-200, 300-400", r"(\d+)-(\d+)")], ["str", "regexp"])
>>> df.select('*', sf.regexp_extract_all('str', sf.lit(r'(\d+)-(\d+)'))).show()
+----------------+-----------+---------------------------------------+
|             str|     regexp|regexp_extract_all(str, (\d+)-(\d+), 1)|
+----------------+-----------+---------------------------------------+
|100-200, 300-400|(\d+)-(\d+)|                             [100, 300]|
+----------------+-----------+---------------------------------------+

```


```
>>> df.select('*', sf.regexp_extract_all('str', sf.lit(r'(\d+)-(\d+)'), sf.lit(1))).show()
+----------------+-----------+---------------------------------------+
|             str|     regexp|regexp_extract_all(str, (\d+)-(\d+), 1)|
+----------------+-----------+---------------------------------------+
|100-200, 300-400|(\d+)-(\d+)|                             [100, 300]|
+----------------+-----------+---------------------------------------+

```


```
>>> df.select('*', sf.regexp_extract_all('str', sf.lit(r'(\d+)-(\d+)'), 2)).show()
+----------------+-----------+---------------------------------------+
|             str|     regexp|regexp_extract_all(str, (\d+)-(\d+), 2)|
+----------------+-----------+---------------------------------------+
|100-200, 300-400|(\d+)-(\d+)|                             [200, 400]|
+----------------+-----------+---------------------------------------+

```


```
>>> df.select('*', sf.regexp_extract_all('str', sf.col("regexp"))).show()
+----------------+-----------+----------------------------------+
|             str|     regexp|regexp_extract_all(str, regexp, 1)|
+----------------+-----------+----------------------------------+
|100-200, 300-400|(\d+)-(\d+)|                        [100, 300]|
+----------------+-----------+----------------------------------+

```


```
>>> df.select('*', sf.regexp_extract_all(sf.col('str'), "regexp")).show()
+----------------+-----------+----------------------------------+
|             str|     regexp|regexp_extract_all(str, regexp, 1)|
+----------------+-----------+----------------------------------+
|100-200, 300-400|(\d+)-(\d+)|                        [100, 300]|
+----------------+-----------+----------------------------------+

```


# pyspark.sql.functions.regexp_instr — PySpark 4.0.1 documentation
pyspark.sql.functions.regexp\_instr(_str_, _regexp_, _idx\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_instr)
[#](#pyspark.sql.functions.regexp_instr "Permalink to this definition")

Returns the position of the first substring in the str that match the Java regex regexp and corresponding to the regex group index.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

regex pattern to apply.

**idx**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

matched group id.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the position of the first substring in the str that match a Java regex and corresponding to the regex group index.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("1a 2b 14m", r"\d+(a|b|m)")], ["str", "regexp"])

```


Example 1: Returns the position of the first substring in the str column name that match the regex pattern (d+(a|b|m)) (one or more digits followed by ‘a’, ‘b’, or ‘m’).

```
>>> df.select('*', sf.regexp_instr('str', sf.lit(r'\d+(a|b|m)'))).show()
+---------+----------+--------------------------------+
|      str|    regexp|regexp_instr(str, \d+(a|b|m), 0)|
+---------+----------+--------------------------------+
|1a 2b 14m|\d+(a|b|m)|                               1|
+---------+----------+--------------------------------+

```


Example 2: Returns the position of the first substring in the str column name that match the regex pattern (d+(a|b|m)) (one or more digits followed by ‘a’, ‘b’, or ‘m’),

```
>>> df.select('*', sf.regexp_instr('str', sf.lit(r'\d+(a|b|m)'), sf.lit(1))).show()
+---------+----------+--------------------------------+
|      str|    regexp|regexp_instr(str, \d+(a|b|m), 1)|
+---------+----------+--------------------------------+
|1a 2b 14m|\d+(a|b|m)|                               1|
+---------+----------+--------------------------------+

```


Example 3: Returns the position of the first substring in the str column name that match the regex pattern in regexp Column.

```
>>> df.select('*', sf.regexp_instr('str', sf.col("regexp"))).show()
+---------+----------+----------------------------+
|      str|    regexp|regexp_instr(str, regexp, 0)|
+---------+----------+----------------------------+
|1a 2b 14m|\d+(a|b|m)|                           1|
+---------+----------+----------------------------+

```


Example 4: Returns the position of the first substring in the str Column that match the regex pattern in regexp column name.

```
>>> df.select('*', sf.regexp_instr(sf.col("str"), "regexp")).show()
+---------+----------+----------------------------+
|      str|    regexp|regexp_instr(str, regexp, 0)|
+---------+----------+----------------------------+
|1a 2b 14m|\d+(a|b|m)|                           1|
+---------+----------+----------------------------+

```


# pyspark.sql.functions.regexp_replace — PySpark 4.0.1 documentation
pyspark.sql.functions.regexp\_replace(_string_, _pattern_, _replacement_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_replace)
[#](#pyspark.sql.functions.regexp_replace "Permalink to this definition")

Replace all substrings of the specified string value that match regexp with replacement.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**string**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column name or column containing the string value

**pattern**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column object or str containing the regexp pattern

**replacement**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column object or str containing the replacement

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string with all substrings replaced.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...      [("100-200", r"(\d+)", "--")],
...      ["str", "pattern", "replacement"]
... )

```


Example 1: Replaces all the substrings in the str column name that match the regex pattern (d+) (one or more digits) with the replacement string “–“.

```
>>> df.select('*', sf.regexp_replace('str', r'(\d+)', '--')).show()
+-------+-------+-----------+---------------------------------+
|    str|pattern|replacement|regexp_replace(str, (\d+), --, 1)|
+-------+-------+-----------+---------------------------------+
|100-200|  (\d+)|         --|                            -----|
+-------+-------+-----------+---------------------------------+

```


Example 2: Replaces all the substrings in the str Column that match the regex pattern in the pattern Column with the string in the replacement column.

```
>>> df.select('*', \
...     sf.regexp_replace(sf.col("str"), sf.col("pattern"), sf.col("replacement")) \
... ).show()
+-------+-------+-----------+--------------------------------------------+
|    str|pattern|replacement|regexp_replace(str, pattern, replacement, 1)|
+-------+-------+-----------+--------------------------------------------+
|100-200|  (\d+)|         --|                                       -----|
+-------+-------+-----------+--------------------------------------------+

```



# pyspark.sql.functions.regexp_substr — PySpark 4.0.1 documentation
pyspark.sql.functions.regexp\_substr(_str_, _regexp_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regexp_substr)
[#](#pyspark.sql.functions.regexp_substr "Permalink to this definition")

Returns the first substring that matches the Java regex regexp within the string str. If the regular expression is not found, the result is null.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**regexp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

regex pattern to apply.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the first substring that matches a Java regex within the string str.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("1a 2b 14m", r"\d+")], ["str", "regexp"])

```


Example 1: Returns the first substring in the str column name that matches the regex pattern (d+) (one or more digits).

```
>>> df.select('*', sf.regexp_substr('str', sf.lit(r'\d+'))).show()
+---------+------+-----------------------+
|      str|regexp|regexp_substr(str, \d+)|
+---------+------+-----------------------+
|1a 2b 14m|   \d+|                      1|
+---------+------+-----------------------+

```


Example 2: Returns the first substring in the str column name that matches the regex pattern (mmm) (three consecutive ‘m’ characters)

```
>>> df.select('*', sf.regexp_substr('str', sf.lit(r'mmm'))).show()
+---------+------+-----------------------+
|      str|regexp|regexp_substr(str, mmm)|
+---------+------+-----------------------+
|1a 2b 14m|   \d+|                   NULL|
+---------+------+-----------------------+

```


Example 3: Returns the first substring in the str column name that matches the regex pattern in regexp Column.

```
>>> df.select('*', sf.regexp_substr("str", sf.col("regexp"))).show()
+---------+------+--------------------------+
|      str|regexp|regexp_substr(str, regexp)|
+---------+------+--------------------------+
|1a 2b 14m|   \d+|                         1|
+---------+------+--------------------------+

```


Example 4: Returns the first substring in the str Column that matches the regex pattern in regexp column name.

```
>>> df.select('*', sf.regexp_substr(sf.col("str"), "regexp")).show()
+---------+------+--------------------------+
|      str|regexp|regexp_substr(str, regexp)|
+---------+------+--------------------------+
|1a 2b 14m|   \d+|                         1|
+---------+------+--------------------------+

```



# pyspark.sql.functions.repeat — PySpark 4.0.1 documentation
pyspark.sql.functions.repeat(_col_, _n_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#repeat)
[#](#pyspark.sql.functions.repeat "Permalink to this definition")

Repeats a string column n times, and returns it as a new string column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**n**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

number of times to repeat value.

Changed in version 4.0.0: n now accepts column and column name.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string with repeated values.

Examples

Example 1: Repeat with a constant number of times

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ab',)], ['s',])
>>> df.select("*", sf.repeat("s", 3)).show()
+---+------------+
|  s|repeat(s, 3)|
+---+------------+
| ab|      ababab|
+---+------------+

```


```
>>> df.select("*", sf.repeat(df.s, sf.lit(4))).show()
+---+------------+
|  s|repeat(s, 4)|
+---+------------+
| ab|    abababab|
+---+------------+

```


Example 2: Repeat with a column containing different number of times

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ab', 5,), ('abc', 6,)], ['s', 't'])
>>> df.select("*", sf.repeat("s", "t")).show()
+---+---+------------------+
|  s|  t|      repeat(s, t)|
+---+---+------------------+
| ab|  5|        ababababab|
|abc|  6|abcabcabcabcabcabc|
+---+---+------------------+

```

# pyspark.sql.functions.replace — PySpark 4.0.1 documentation
pyspark.sql.functions.replace(_src_, _search_, _replace\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#replace)
[#](#pyspark.sql.functions.replace "Permalink to this definition")

Replaces all occurrences of search with replace.

New in version 3.5.0.

Parameters

**src**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string to be replaced.

**search**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string, If search is not found in str, str is returned unchanged.

**replace**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

A column of string, If replace is not specified or is an empty string, nothing replaces the string that is removed from str.

Examples

```
>>> df = spark.createDataFrame([("ABCabc", "abc", "DEF",)], ["a", "b", "c"])
>>> df.select(replace(df.a, df.b, df.c).alias('r')).collect()
[Row(r='ABCDEF')]

```


```
>>> df.select(replace(df.a, df.b).alias('r')).collect()
[Row(r='ABC')]

```

# pyspark.sql.functions.right — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.right

pyspark.sql.functions.right(_str_, _len_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#right)
[#](#pyspark.sql.functions.right "Permalink to this definition")

Returns the rightmost len\`(\`len can be string type) characters from the string str, if len is less or equal than 0 the result is an empty string.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings, the rightmost len.

Examples

```
>>> df = spark.createDataFrame([("Spark SQL", 3,)], ['a', 'b'])
>>> df.select(right(df.a, df.b).alias('r')).collect()
[Row(r='SQL')]

```



# pyspark.sql.functions.rpad — PySpark 4.0.1 documentation
pyspark.sql.functions.rpad(_col_, _len_, _pad_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#rpad)
[#](#pyspark.sql.functions.rpad "Permalink to this definition")

Right-pad the string column to width len with pad.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to work on.

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

length of the final string.

Changed in version 4.0.0: pattern now accepts column.

**pad**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

chars to prepend.

Changed in version 4.0.0: pattern now accepts column.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

right padded result.

Examples

Example 1: Pad with a literal string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('abcd',), ('xyz',), ('12',)], ['s',])
>>> df.select("*", sf.rpad(df.s, 6, '#')).show()
+----+-------------+
|   s|rpad(s, 6, #)|
+----+-------------+
|abcd|       abcd##|
| xyz|       xyz###|
|  12|       12####|
+----+-------------+

```


Example 2: Pad with a bytes column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('abcd',), ('xyz',), ('12',)], ['s',])
>>> df.select("*", sf.rpad(df.s, 6, sf.lit(b"uv"))).show()
+----+-------------------+
|   s|rpad(s, 6, X'7576')|
+----+-------------------+
|abcd|             abcduv|
| xyz|             xyzuvu|
|  12|             12uvuv|
+----+-------------------+

```


# pyspark.sql.functions.rtrim — PySpark 4.0.1 documentation
pyspark.sql.functions.rtrim(_col_, _trim\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#rtrim)
[#](#pyspark.sql.functions.rtrim "Permalink to this definition")

Trim the spaces from right end for the specified string value.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**trim**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The trim string characters to trim, the default value is a single space

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

right trimmed values.

Examples

Example 1: Trim the spaces

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["   Spark", "Spark  ", " Spark"], "STRING")
>>> df.select("*", sf.rtrim("value")).show()
+--------+------------+
|   value|rtrim(value)|
+--------+------------+
|   Spark|       Spark|
| Spark  |       Spark|
|   Spark|       Spark|
+--------+------------+

```


Example 2: Trim specified characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["***Spark", "Spark**", "*Spark"], "STRING")
>>> df.select("*", sf.rtrim("value", sf.lit("*"))).show()
+--------+---------------------------+
|   value|TRIM(TRAILING * FROM value)|
+--------+---------------------------+
|***Spark|                   ***Spark|
| Spark**|                      Spark|
|  *Spark|                     *Spark|
+--------+---------------------------+

```


Example 3: Trim a column containing different characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("**Spark*", "*"), ("==Spark=", "=")], ["value", "t"])
>>> df.select("*", sf.rtrim("value", "t")).show()
+--------+---+---------------------------+
|   value|  t|TRIM(TRAILING t FROM value)|
+--------+---+---------------------------+
|**Spark*|  *|                    **Spark|
|==Spark=|  =|                    ==Spark|
+--------+---+---------------------------+

```


# pyspark.sql.functions.sentences — PySpark 4.0.1 documentation
pyspark.sql.functions.sentences(_string_, _language\=None_, _country\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sentences)
[#](#pyspark.sql.functions.sentences "Permalink to this definition")

Splits a string into arrays of sentences, where each sentence is an array of words. The language and country arguments are optional, When they are omitted: 1.If they are both omitted, the Locale.ROOT - locale(language=’’, country=’’) is used. The Locale.ROOT is regarded as the base locale of all locales, and is used as the language/country neutral locale for the locale sensitive operations. 2.If the country is omitted, the locale(language, country=’’) is used. When they are null: 1.If they are both null, the Locale.US - locale(language=’en’, country=’US’) is used. 2.If the language is null and the country is not null, the Locale.US - locale(language=’en’, country=’US’) is used. 3.If the language is not null and the country is null, the locale(language) is used. 4.If neither is null, the locale(language, country) is used.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Changed in version 4.0.0: Supports sentences(string, language).

Parameters

**string**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

a string to be split

**language**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

a language of the locale

**country**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

a country of the locale

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

arrays of split sentences.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("This is an example sentence.", )], ["s"])
>>> df.select("*", sf.sentences(df.s, sf.lit("en"), sf.lit("US"))).show(truncate=False)
+----------------------------+-----------------------------------+
|s                           |sentences(s, en, US)               |
+----------------------------+-----------------------------------+
|This is an example sentence.|[[This, is, an, example, sentence]]|
+----------------------------+-----------------------------------+

```


```
>>> df.select("*", sf.sentences(df.s, sf.lit("en"))).show(truncate=False)
+----------------------------+-----------------------------------+
|s                           |sentences(s, en, )                 |
+----------------------------+-----------------------------------+
|This is an example sentence.|[[This, is, an, example, sentence]]|
+----------------------------+-----------------------------------+

```


```
>>> df.select("*", sf.sentences(df.s)).show(truncate=False)
+----------------------------+-----------------------------------+
|s                           |sentences(s, , )                   |
+----------------------------+-----------------------------------+
|This is an example sentence.|[[This, is, an, example, sentence]]|
+----------------------------+-----------------------------------+

```


# pyspark.sql.functions.soundex — PySpark 4.0.1 documentation
pyspark.sql.functions.soundex(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#soundex)
[#](#pyspark.sql.functions.soundex "Permalink to this definition")

Returns the SoundEx encoding for a string

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

SoundEx encoded string.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("Peters",),("Uhrbach",)], ["s"])
>>> df.select("*", sf.soundex("s")).show()
+-------+----------+
|      s|soundex(s)|
+-------+----------+
| Peters|      P362|
|Uhrbach|      U612|
+-------+----------+

```


# pyspark.sql.functions.split — PySpark 4.0.1 documentation
pyspark.sql.functions.split(_str_, _pattern_, _limit\=\- 1_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#split)
[#](#pyspark.sql.functions.split "Permalink to this definition")

Splits str around matches of the given pattern.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

a string expression to split

**pattern**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

a string representing a regular expression. The regex string should be a Java regular expression.

Changed in version 4.0.0: pattern now accepts column. Does not accept column name since string type remain accepted as a regular expression representation, for backwards compatibility. In addition to int, limit now accepts column and column name.

**limit**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

an integer which controls the number of times pattern is applied.

*   `limit > 0`: The resulting array’s length will not be more than limit, and the
    
    resulting array’s last entry will contain all input beyond the last matched pattern.
    
*   `limit <= 0`: pattern will be applied as many times as possible, and the resulting
    
    array can be of any size.
    

Changed in version 3.0: split now takes an optional limit field. If not provided, default limit value is -1.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

array of separated strings.

Examples

Example 1: Repeat with a constant pattern

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('oneAtwoBthreeC',)], ['s',])
>>> df.select('*', sf.split(df.s, '[ABC]')).show()
+--------------+-------------------+
|             s|split(s, [ABC], -1)|
+--------------+-------------------+
|oneAtwoBthreeC|[one, two, three, ]|
+--------------+-------------------+

```


```
>>> df.select('*', sf.split(df.s, '[ABC]', 2)).show()
+--------------+------------------+
|             s|split(s, [ABC], 2)|
+--------------+------------------+
|oneAtwoBthreeC| [one, twoBthreeC]|
+--------------+------------------+

```


```
>>> df.select('*', sf.split('s', '[ABC]', -2)).show()
+--------------+-------------------+
|             s|split(s, [ABC], -2)|
+--------------+-------------------+
|oneAtwoBthreeC|[one, two, three, ]|
+--------------+-------------------+

```


Example 2: Repeat with a column containing different patterns and limits

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ('oneAtwoBthreeC', '[ABC]', 2),
...     ('1A2B3C', '[1-9]+', 1),
...     ('aa2bb3cc4', '[1-9]+', -1)], ['s', 'p', 'l'])
>>> df.select('*', sf.split(df.s, df.p)).show()
+--------------+------+---+-------------------+
|             s|     p|  l|    split(s, p, -1)|
+--------------+------+---+-------------------+
|oneAtwoBthreeC| [ABC]|  2|[one, two, three, ]|
|        1A2B3C|[1-9]+|  1|        [, A, B, C]|
|     aa2bb3cc4|[1-9]+| -1|     [aa, bb, cc, ]|
+--------------+------+---+-------------------+

```


```
>>> df.select(sf.split('s', df.p, 'l')).show()
+-----------------+
|   split(s, p, l)|
+-----------------+
|[one, twoBthreeC]|
|         [1A2B3C]|
|   [aa, bb, cc, ]|
+-----------------+

```


# pyspark.sql.functions.split_part — PySpark 4.0.1 documentation
pyspark.sql.functions.split\_part(_src_, _delimiter_, _partNum_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#split_part)
[#](#pyspark.sql.functions.split_part "Permalink to this definition")

Splits str by delimiter and return requested part of the split (1-based). If any input is null, returns null. if partNum is out of range of split parts, returns empty string. If partNum is 0, throws an error. If partNum is negative, the parts are counted backward from the end of the string. If the delimiter is an empty string, the str is not split.

New in version 3.5.0.

Parameters

**src**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of string to be split.

**delimiter**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of string, the delimiter used for split.

**partNum**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of string, requested part of the split (1-based).

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("11.12.13", ".", 3,)], ["a", "b", "c"])
>>> df.select("*", sf.split_part("a", "b", "c")).show()
+--------+---+---+-------------------+
|       a|  b|  c|split_part(a, b, c)|
+--------+---+---+-------------------+
|11.12.13|  .|  3|                 13|
+--------+---+---+-------------------+

```


```
>>> df.select("*", sf.split_part(df.a, df.b, sf.lit(-2))).show()
+--------+---+---+--------------------+
|       a|  b|  c|split_part(a, b, -2)|
+--------+---+---+--------------------+
|11.12.13|  .|  3|                  12|
+--------+---+---+--------------------+

```


# pyspark.sql.functions.startswith — PySpark 4.0.1 documentation
pyspark.sql.functions.startswith(_str_, _prefix_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#startswith)
[#](#pyspark.sql.functions.startswith "Permalink to this definition")

Returns a boolean. The value is True if str starts with prefix. Returns NULL if either input expression is NULL. Otherwise, returns False. Both str or prefix must be of STRING or BINARY type.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string.

**prefix**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of string, the prefix.

Examples

```
>>> df = spark.createDataFrame([("Spark SQL", "Spark",)], ["a", "b"])
>>> df.select(startswith(df.a, df.b).alias('r')).collect()
[Row(r=True)]

```


```
>>> df = spark.createDataFrame([("414243", "4142",)], ["e", "f"])
>>> df = df.select(to_binary("e").alias("e"), to_binary("f").alias("f"))
>>> df.printSchema()
root
 |-- e: binary (nullable = true)
 |-- f: binary (nullable = true)
>>> df.select(startswith("e", "f"), startswith("f", "e")).show()
+----------------+----------------+
|startswith(e, f)|startswith(f, e)|
+----------------+----------------+
|            true|           false|
+----------------+----------------+

```

# pyspark.sql.functions.substr — PySpark 4.0.1 documentation
pyspark.sql.functions.substr(_str_, _pos_, _len\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#substr)
[#](#pyspark.sql.functions.substr "Permalink to this definition")

Returns the substring of str that starts at pos and is of length len, or the slice of byte array that starts at pos and is of length len.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of string.

**pos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of string, the substring of str that starts at pos.

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

A column of string, the substring of str is of length len.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

substring of given value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Spark SQL", 5, 1,)], ["a", "b", "c"])
>>> df.select("*", sf.substr("a", "b", "c")).show()
+---------+---+---+---------------+
|        a|  b|  c|substr(a, b, c)|
+---------+---+---+---------------+
|Spark SQL|  5|  1|              k|
+---------+---+---+---------------+

```


```
>>> df.select("*", sf.substr(df.a, df.b)).show()
+---------+---+---+------------------------+
|        a|  b|  c|substr(a, b, 2147483647)|
+---------+---+---+------------------------+
|Spark SQL|  5|  1|                   k SQL|
+---------+---+---+------------------------+

```

# pyspark.sql.functions.substring — PySpark 4.0.1 documentation
pyspark.sql.functions.substring(_str_, _pos_, _len_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#substring)
[#](#pyspark.sql.functions.substring "Permalink to this definition")

Substring starts at pos and is of length len when str is String type or returns the slice of byte array that starts at pos in byte and is of length len when str is Binary type.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**pos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

starting position in str.

Changed in version 4.0.0: pos now accepts column and column name.

**len**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

length of chars.

Changed in version 4.0.0: len now accepts column and column name.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

substring of given value.

Notes

The position is not zero based, but 1 based index.

Examples

Example 1: Using literal integers as arguments

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('abcd',)], ['s',])
>>> df.select('*', sf.substring(df.s, 1, 2)).show()
+----+------------------+
|   s|substring(s, 1, 2)|
+----+------------------+
|abcd|                ab|
+----+------------------+

```


Example 2: Using columns as arguments

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('Spark', 2, 3)], ['s', 'p', 'l'])
>>> df.select('*', sf.substring(df.s, 2, df.l)).show()
+-----+---+---+------------------+
|    s|  p|  l|substring(s, 2, l)|
+-----+---+---+------------------+
|Spark|  2|  3|               par|
+-----+---+---+------------------+

```


```
>>> df.select('*', sf.substring(df.s, df.p, 3)).show()
+-----+---+---+------------------+
|    s|  p|  l|substring(s, p, 3)|
+-----+---+---+------------------+
|Spark|  2|  3|               par|
+-----+---+---+------------------+

```


```
>>> df.select('*', sf.substring(df.s, df.p, df.l)).show()
+-----+---+---+------------------+
|    s|  p|  l|substring(s, p, l)|
+-----+---+---+------------------+
|Spark|  2|  3|               par|
+-----+---+---+------------------+

```


Example 3: Using column names as arguments

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('Spark', 2, 3)], ['s', 'p', 'l'])
>>> df.select('*', sf.substring(df.s, 2, 'l')).show()
+-----+---+---+------------------+
|    s|  p|  l|substring(s, 2, l)|
+-----+---+---+------------------+
|Spark|  2|  3|               par|
+-----+---+---+------------------+

```


```
>>> df.select('*', sf.substring('s', 'p', 'l')).show()
+-----+---+---+------------------+
|    s|  p|  l|substring(s, p, l)|
+-----+---+---+------------------+
|Spark|  2|  3|               par|
+-----+---+---+------------------+

```


# pyspark.sql.functions.substring_index — PySpark 4.0.1 documentation
pyspark.sql.functions.substring\_index(_str_, _delim_, _count_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#substring_index)
[#](#pyspark.sql.functions.substring_index "Permalink to this definition")

Returns the substring from string str before count occurrences of the delimiter delim. If count is positive, everything the left of the final delimiter (counting from left) is returned. If count is negative, every to the right of the final delimiter (counting from the right) is returned. substring\_index performs a case-sensitive match when searching for delim.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**delim**literal string

delimiter of values.

**count**int

number of occurrences.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

substring of given value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a.b.c.d',)], ['s'])
>>> df.select('*', sf.substring_index(df.s, '.', 2)).show()
+-------+------------------------+
|      s|substring_index(s, ., 2)|
+-------+------------------------+
|a.b.c.d|                     a.b|
+-------+------------------------+

```


```
>>> df.select('*', sf.substring_index('s', '.', -3)).show()
+-------+-------------------------+
|      s|substring_index(s, ., -3)|
+-------+-------------------------+
|a.b.c.d|                    b.c.d|
+-------+-------------------------+

```


# pyspark.sql.functions.to_binary — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_binary(_col_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_binary)
[#](#pyspark.sql.functions.to_binary "Permalink to this definition")

Converts the input col to a binary value based on the supplied format. The format can be a case-insensitive string literal of “hex”, “utf-8”, “utf8”, or “base64”. By default, the binary format for conversion is “hex” if format is omitted. The function returns NULL if at least one of the input parameters is NULL.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

format to use to convert binary values.

Examples

Example 1: Convert string to a binary with encoding specified

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("abc",)], ["e"])
>>> df.select(sf.try_to_binary(df.e, sf.lit("utf-8")).alias('r')).collect()
[Row(r=bytearray(b'abc'))]

```


Example 2: Convert string to a timestamp without encoding specified

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("414243",)], ["e"])
>>> df.select(sf.try_to_binary(df.e).alias('r')).collect()
[Row(r=bytearray(b'ABC'))]

```


# pyspark.sql.functions.to_char — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_char(_col_, _format_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_char)
[#](#pyspark.sql.functions.to_char "Permalink to this definition")

Convert col to a string based on the format. Throws an exception if the conversion fails. The format can consist of the following characters, case insensitive: ‘0’ or ‘9’: Specifies an expected digit between 0 and 9. A sequence of 0 or 9 in the format string matches a sequence of digits in the input value, generating a result string of the same length as the corresponding sequence in the format string. The result string is left-padded with zeros if the 0/9 sequence comprises more digits than the matching part of the decimal value, starts with 0, and is before the decimal point. Otherwise, it is padded with spaces. ‘.’ or ‘D’: Specifies the position of the decimal point (optional, only allowed once). ‘,’ or ‘G’: Specifies the position of the grouping (thousands) separator (,). There must be a 0 or 9 to the left and right of each grouping separator. ‘$’: Specifies the location of the $ currency sign. This character may only be specified once. ‘S’ or ‘MI’: Specifies the position of a ‘-’ or ‘+’ sign (optional, only allowed once at the beginning or end of the format string). Note that ‘S’ prints ‘+’ for positive values but ‘MI’ prints a space. ‘PR’: Only allowed at the end of the format string; specifies that the result string will be wrapped by angle brackets if the input value is negative. If col is a datetime, format shall be a valid datetime pattern, see <a href=”[https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)”>Patterns</a>. If col is a binary, it is converted to a string in one of the formats: ‘base64’: a base 64 string. ‘hex’: a string in the hexadecimal format. ‘utf-8’: the input binary is decoded to UTF-8 string.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

format to use to convert char values.

Examples

```
>>> df = spark.createDataFrame([(78.12,)], ["e"])
>>> df.select(to_char(df.e, lit("$99.99")).alias('r')).collect()
[Row(r='$78.12')]

```


# pyspark.sql.functions.to_number — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_number(_col_, _format_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_number)
[#](#pyspark.sql.functions.to_number "Permalink to this definition")

Convert string ‘col’ to a number based on the string format ‘format’. Throws an exception if the conversion fails. The format can consist of the following characters, case insensitive: ‘0’ or ‘9’: Specifies an expected digit between 0 and 9. A sequence of 0 or 9 in the format string matches a sequence of digits in the input string. If the 0/9 sequence starts with 0 and is before the decimal point, it can only match a digit sequence of the same size. Otherwise, if the sequence starts with 9 or is after the decimal point, it can match a digit sequence that has the same or smaller size. ‘.’ or ‘D’: Specifies the position of the decimal point (optional, only allowed once). ‘,’ or ‘G’: Specifies the position of the grouping (thousands) separator (,). There must be a 0 or 9 to the left and right of each grouping separator. ‘col’ must match the grouping separator relevant for the size of the number. ‘$’: Specifies the location of the $ currency sign. This character may only be specified once. ‘S’ or ‘MI’: Specifies the position of a ‘-’ or ‘+’ sign (optional, only allowed once at the beginning or end of the format string). Note that ‘S’ allows ‘-’ but ‘MI’ does not. ‘PR’: Only allowed at the end of the format string; specifies that ‘col’ indicates a negative number with wrapping angled brackets.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

format to use to convert number values.

Examples

```
>>> df = spark.createDataFrame([("$78.12",)], ["e"])
>>> df.select(to_number(df.e, lit("$99.99")).alias('r')).collect()
[Row(r=Decimal('78.12'))]

```



# pyspark.sql.functions.to_varchar — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_varchar(_col_, _format_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_varchar)
[#](#pyspark.sql.functions.to_varchar "Permalink to this definition")

Convert col to a string based on the format. Throws an exception if the conversion fails. The format can consist of the following characters, case insensitive: ‘0’ or ‘9’: Specifies an expected digit between 0 and 9. A sequence of 0 or 9 in the format string matches a sequence of digits in the input value, generating a result string of the same length as the corresponding sequence in the format string. The result string is left-padded with zeros if the 0/9 sequence comprises more digits than the matching part of the decimal value, starts with 0, and is before the decimal point. Otherwise, it is padded with spaces. ‘.’ or ‘D’: Specifies the position of the decimal point (optional, only allowed once). ‘,’ or ‘G’: Specifies the position of the grouping (thousands) separator (,). There must be a 0 or 9 to the left and right of each grouping separator. ‘$’: Specifies the location of the $ currency sign. This character may only be specified once. ‘S’ or ‘MI’: Specifies the position of a ‘-’ or ‘+’ sign (optional, only allowed once at the beginning or end of the format string). Note that ‘S’ prints ‘+’ for positive values but ‘MI’ prints a space. ‘PR’: Only allowed at the end of the format string; specifies that the result string will be wrapped by angle brackets if the input value is negative. If col is a datetime, format shall be a valid datetime pattern, see <a href=”[https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html)”>Patterns</a>. If col is a binary, it is converted to a string in one of the formats: ‘base64’: a base 64 string. ‘hex’: a string in the hexadecimal format. ‘utf-8’: the input binary is decoded to UTF-8 string.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

format to use to convert char values.

Examples

```
>>> df = spark.createDataFrame([(78.12,)], ["e"])
>>> df.select(to_varchar(df.e, lit("$99.99")).alias('r')).collect()
[Row(r='$78.12')]

```


# pyspark.sql.functions.translate — PySpark 4.0.1 documentation
pyspark.sql.functions.translate(_srcCol_, _matching_, _replace_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#translate)
[#](#pyspark.sql.functions.translate "Permalink to this definition")

A function translate any character in the srcCol by a character in matching. The characters in replace is corresponding to the characters in matching. Translation will happen whenever any character in the string is matching with the character in the matching.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**srcCol**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Source column or strings

**matching**str

matching characters.

**replace**str

characters for replacement. If this is shorter than matching string then those chars that don’t have replacement will be dropped.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

replaced value.

Examples

```
>>> spark.createDataFrame([('translate',)], ['a']).select(translate('a', "rnlt", "123") \
...     .alias('r')).collect()
[Row(r='1a2s3ae')]

```


# pyspark.sql.functions.trim — PySpark 4.0.1 documentation
pyspark.sql.functions.trim(_col_, _trim\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#trim)
[#](#pyspark.sql.functions.trim "Permalink to this definition")

Trim the spaces from both ends for the specified string column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**trim**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The trim string characters to trim, the default value is a single space

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

trimmed values from both sides.

Examples

Example 1: Trim the spaces

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["   Spark", "Spark  ", " Spark"], "STRING")
>>> df.select("*", sf.trim("value")).show()
+--------+-----------+
|   value|trim(value)|
+--------+-----------+
|   Spark|      Spark|
| Spark  |      Spark|
|   Spark|      Spark|
+--------+-----------+

```


Example 2: Trim specified characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["***Spark", "Spark**", "*Spark"], "STRING")
>>> df.select("*", sf.trim("value", sf.lit("*"))).show()
+--------+-----------------------+
|   value|TRIM(BOTH * FROM value)|
+--------+-----------------------+
|***Spark|                  Spark|
| Spark**|                  Spark|
|  *Spark|                  Spark|
+--------+-----------------------+

```


Example 3: Trim a column containing different characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("**Spark*", "*"), ("==Spark=", "=")], ["value", "t"])
>>> df.select("*", sf.trim("value", "t")).show()
+--------+---+-----------------------+
|   value|  t|TRIM(BOTH t FROM value)|
+--------+---+-----------------------+
|**Spark*|  *|                  Spark|
|==Spark=|  =|                  Spark|
+--------+---+-----------------------+

```


# pyspark.sql.functions.try_to_binary — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_to\_binary(_col_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_to_binary)
[#](#pyspark.sql.functions.try_to_binary "Permalink to this definition")

This is a special version of to\_binary that performs the same operation, but returns a NULL value instead of raising an error if the conversion cannot be performed.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

format to use to convert binary values.

Examples

Example 1: Convert string to a binary with encoding specified

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("abc",)], ["e"])
>>> df.select(sf.try_to_binary(df.e, sf.lit("utf-8")).alias('r')).collect()
[Row(r=bytearray(b'abc'))]

```


Example 2: Convert string to a timestamp without encoding specified

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("414243",)], ["e"])
>>> df.select(sf.try_to_binary(df.e).alias('r')).collect()
[Row(r=bytearray(b'ABC'))]

```


Example 3: Converion failure results in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     df = spark.range(1)
...     df.select(sf.try_to_binary(sf.lit("malformed"), sf.lit("hex"))).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+-----------------------------+
|try_to_binary(malformed, hex)|
+-----------------------------+
|                         NULL|
+-----------------------------+

```


# pyspark.sql.functions.try_to_number — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_to\_number(_col_, _format_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_to_number)
[#](#pyspark.sql.functions.try_to_number "Permalink to this definition")

Convert string ‘col’ to a number based on the string format format. Returns NULL if the string ‘col’ does not match the expected format. The format follows the same semantics as the to\_number function.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

format to use to convert number values.

Examples

Example 1: Convert a string to a number with a format specified

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("$78.12",)], ["e"])
>>> df.select(sf.try_to_number(df.e, sf.lit("$99.99")).alias('r')).show()
+-----+
|    r|
+-----+
|78.12|
+-----+

```


Example 2: Converion failure results in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     df = spark.range(1)
...     df.select(sf.try_to_number(sf.lit("77"), sf.lit("$99.99")).alias('r')).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+----+
|   r|
+----+
|NULL|
+----+

```


# pyspark.sql.functions.try_validate_utf8 — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_validate\_utf8(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_validate_utf8)
[#](#pyspark.sql.functions.try_validate_utf8 "Permalink to this definition")

Returns the input value if it corresponds to a valid UTF-8 string, or NULL otherwise.

New in version 4.0.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of strings, each representing a UTF-8 byte sequence.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the input string if it is a valid UTF-8 string, null otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.try_validate_utf8(sf.lit("SparkSQL"))).show()
+---------------------------+
|try_validate_utf8(SparkSQL)|
+---------------------------+
|                   SparkSQL|
+---------------------------+

```


# pyspark.sql.functions.ucase — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.ucase

pyspark.sql.functions.ucase(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ucase)
[#](#pyspark.sql.functions.ucase "Permalink to this definition")

Returns str with all characters changed to uppercase.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.ucase(sf.lit("Spark"))).show()
+------------+
|ucase(Spark)|
+------------+
|       SPARK|
+------------+

```


# pyspark.sql.functions.unbase64 — PySpark 4.0.1 documentation
pyspark.sql.functions.unbase64(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unbase64)
[#](#pyspark.sql.functions.unbase64 "Permalink to this definition")

Decodes a BASE64 encoded string column and returns it as a binary column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

encoded string value.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["U3Bhcms=", "UHlTcGFyaw==", "UGFuZGFzIEFQSQ=="], "STRING")
>>> df.select("*", sf.unbase64("value")).show(truncate=False)
+----------------+-------------------------------+
|value           |unbase64(value)                |
+----------------+-------------------------------+
|U3Bhcms=        |[53 70 61 72 6B]               |
|UHlTcGFyaw==    |[50 79 53 70 61 72 6B]         |
|UGFuZGFzIEFQSQ==|[50 61 6E 64 61 73 20 41 50 49]|
+----------------+-------------------------------+

```


# pyspark.sql.functions.upper — PySpark 4.0.1 documentation
pyspark.sql.functions.upper(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#upper)
[#](#pyspark.sql.functions.upper "Permalink to this definition")

Converts a string expression to upper case.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

upper case values.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(["Spark", "PySpark", "Pandas API"], "STRING")
>>> df.select("*", sf.upper("value")).show()
+----------+------------+
|     value|upper(value)|
+----------+------------+
|     Spark|       SPARK|
|   PySpark|     PYSPARK|
|Pandas API|  PANDAS API|
+----------+------------+

```


# pyspark.sql.functions.validate_utf8 — PySpark 4.0.1 documentation
pyspark.sql.functions.validate\_utf8(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#validate_utf8)
[#](#pyspark.sql.functions.validate_utf8 "Permalink to this definition")

Returns the input value if it corresponds to a valid UTF-8 string, or emits an error otherwise.

New in version 4.0.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A column of strings, each representing a UTF-8 byte sequence.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the input string if it is a valid UTF-8 string, error otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.validate_utf8(sf.lit("SparkSQL"))).show()
+-----------------------+
|validate_utf8(SparkSQL)|
+-----------------------+
|               SparkSQL|
+-----------------------+

```


# pyspark.sql.functions.bit_count — PySpark 4.0.1 documentation
pyspark.sql.functions.bit\_count(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bit_count)
[#](#pyspark.sql.functions.bit_count "Permalink to this definition")

Returns the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of bits that are set in the argument expr as an unsigned 64-bit integer, or NULL if the argument is NULL.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0), (1), (2), (3), (NULL) AS TAB(value)"
... ).select("*", sf.bit_count("value")).show()
+-----+----------------+
|value|bit_count(value)|
+-----+----------------+
|    0|               0|
|    1|               1|
|    2|               1|
|    3|               2|
| NULL|            NULL|
+-----+----------------+

```


# pyspark.sql.functions.bit_get — PySpark 4.0.1 documentation
pyspark.sql.functions.bit\_get(_col_, _pos_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bit_get)
[#](#pyspark.sql.functions.bit_get "Permalink to this definition")

Returns the value of the bit (0 or 1) at the specified position. The positions are numbered from right to left, starting at zero. The position argument cannot be negative.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**pos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The positions are numbered from right to left, starting at zero.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the value of the bit (0 or 1) at the specified position.

Examples

Example 1: Get the bit with a literal position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[2],[3],[None]], ["value"])
>>> df.select("*", sf.bit_get("value", sf.lit(1))).show()
+-----+-----------------+
|value|bit_get(value, 1)|
+-----+-----------------+
|    1|                0|
|    2|                1|
|    3|                1|
| NULL|             NULL|
+-----+-----------------+

```


Example 2: Get the bit with a column position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1,2],[2,1],[3,None],[None,1]], ["value", "pos"])
>>> df.select("*", sf.bit_get(df.value, "pos")).show()
+-----+----+-------------------+
|value| pos|bit_get(value, pos)|
+-----+----+-------------------+
|    1|   2|                  0|
|    2|   1|                  1|
|    3|NULL|               NULL|
| NULL|   1|               NULL|
+-----+----+-------------------+

```


# pyspark.sql.functions.bitwise_not — PySpark 4.0.1 documentation
pyspark.sql.functions.bitwise\_not(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bitwise_not)
[#](#pyspark.sql.functions.bitwise_not "Permalink to this definition")

Computes bitwise not.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.sql(
...     "SELECT * FROM VALUES (0), (1), (2), (3), (NULL) AS TAB(value)"
... ).select("*", sf.bitwise_not("value")).show()
+-----+------+
|value|~value|
+-----+------+
|    0|    -1|
|    1|    -2|
|    2|    -3|
|    3|    -4|
| NULL|  NULL|
+-----+------+

```

# pyspark.sql.functions.getbit — PySpark 4.0.1 documentation
pyspark.sql.functions.getbit(_col_, _pos_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#getbit)
[#](#pyspark.sql.functions.getbit "Permalink to this definition")

Returns the value of the bit (0 or 1) at the specified position. The positions are numbered from right to left, starting at zero. The position argument cannot be negative.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**pos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The positions are numbered from right to left, starting at zero.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the value of the bit (0 or 1) at the specified position.

Examples

Example 1: Get the bit with a literal position

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[1], [2], [3], [None]], ["value"]
... ).select("*", sf.getbit("value", sf.lit(1))).show()
+-----+----------------+
|value|getbit(value, 1)|
+-----+----------------+
|    1|               0|
|    2|               1|
|    3|               1|
| NULL|            NULL|
+-----+----------------+

```


Example 2: Get the bit with a column position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1,2],[2,1],[3,None],[None,1]], ["value", "pos"])
>>> df.select("*", sf.getbit(df.value, "pos")).show()
+-----+----+------------------+
|value| pos|getbit(value, pos)|
+-----+----+------------------+
|    1|   2|                 0|
|    2|   1|                 1|
|    3|NULL|              NULL|
| NULL|   1|              NULL|
+-----+----+------------------+

```



# pyspark.sql.functions.shiftleft — PySpark 4.0.1 documentation
pyspark.sql.functions.shiftleft(_col_, _numBits_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#shiftleft)
[#](#pyspark.sql.functions.shiftleft "Permalink to this definition")

Shift the given value numBits left.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to shift.

**numBits**int

number of bits to shift.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

shifted value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(4).select("*", sf.shiftleft('id', 1)).show()
+---+----------------+
| id|shiftleft(id, 1)|
+---+----------------+
|  0|               0|
|  1|               2|
|  2|               4|
|  3|               6|
+---+----------------+

```


# pyspark.sql.functions.shiftright — PySpark 4.0.1 documentation
pyspark.sql.functions.shiftright(_col_, _numBits_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#shiftright)
[#](#pyspark.sql.functions.shiftright "Permalink to this definition")

(Signed) shift the given value numBits right.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to shift.

**numBits**int

number of bits to shift.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

shifted values.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(4).select("*", sf.shiftright('id', 1)).show()
+---+-----------------+
| id|shiftright(id, 1)|
+---+-----------------+
|  0|                0|
|  1|                0|
|  2|                1|
|  3|                1|
+---+-----------------+

```


# pyspark.sql.functions.shiftrightunsigned — PySpark 4.0.1 documentation
pyspark.sql.functions.shiftrightunsigned(_col_, _numBits_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#shiftrightunsigned)
[#](#pyspark.sql.functions.shiftrightunsigned "Permalink to this definition")

Unsigned shift the given value numBits right.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to shift.

**numBits**int

number of bits to shift.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

shifted value.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(4).select("*", sf.shiftrightunsigned(sf.col('id') - 2, 1)).show()
+---+-------------------------------+
| id|shiftrightunsigned((id - 2), 1)|
+---+-------------------------------+
|  0|            9223372036854775807|
|  1|            9223372036854775807|
|  2|                              0|
|  3|                              0|
+---+-------------------------------+

```

# pyspark.sql.functions.add_months — PySpark 4.0.1 documentation
pyspark.sql.functions.add\_months(_start_, _months_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#add_months)
[#](#pyspark.sql.functions.add_months "Permalink to this definition")

Returns the date that is months months after start. If months is a negative value then these amount of months will be deducted from the start.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

date column to work on.

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

how many months after the given date to calculate. Accepts negative value as well to calculate backwards.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a date after/before given number of months.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08', 2,)], 'struct<dt:string,a:int>')
>>> df.select('*', sf.add_months(df.dt, 1)).show()
+----------+---+-----------------+
|        dt|  a|add_months(dt, 1)|
+----------+---+-----------------+
|2015-04-08|  2|       2015-05-08|
+----------+---+-----------------+

```


```
>>> df.select('*', sf.add_months('dt', 'a')).show()
+----------+---+-----------------+
|        dt|  a|add_months(dt, a)|
+----------+---+-----------------+
|2015-04-08|  2|       2015-06-08|
+----------+---+-----------------+

```


```
>>> df.select('*', sf.add_months('dt', sf.lit(-1))).show()
+----------+---+------------------+
|        dt|  a|add_months(dt, -1)|
+----------+---+------------------+
|2015-04-08|  2|        2015-03-08|
+----------+---+------------------+

```



# pyspark.sql.functions.convert_timezone — PySpark 4.0.1 documentation
pyspark.sql.functions.convert\_timezone(_sourceTz_, _targetTz_, _sourceTs_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#convert_timezone)
[#](#pyspark.sql.functions.convert_timezone "Permalink to this definition")

Converts the timestamp without time zone sourceTs from the sourceTz time zone to targetTz.

New in version 3.5.0.

Parameters

**sourceTz**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), optional

The time zone for the input timestamp. If it is missed, the current session time zone is used as the source time zone.

**targetTz**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The time zone to which the input timestamp should be converted.

**sourceTs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A timestamp without time zone.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a timestamp for converted time zone.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Converts the timestamp without time zone sourceTs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08 00:00:00',)], ['ts'])
>>> df.select(
...     '*',
...     sf.convert_timezone(None, sf.lit('Asia/Hong_Kong'), 'ts')
... ).show() 
+-------------------+--------------------------------------------------------+
|                 ts|convert_timezone(current_timezone(), Asia/Hong_Kong, ts)|
+-------------------+--------------------------------------------------------+
|2015-04-08 00:00:00|                                     2015-04-08 15:00:00|
+-------------------+--------------------------------------------------------+

```


Example 2: Converts the timestamp with time zone sourceTs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08 15:00:00',)], ['ts'])
>>> df.select(
...     '*',
...     sf.convert_timezone(sf.lit('Asia/Hong_Kong'), sf.lit('America/Los_Angeles'), df.ts)
... ).show()
+-------------------+---------------------------------------------------------+
|                 ts|convert_timezone(Asia/Hong_Kong, America/Los_Angeles, ts)|
+-------------------+---------------------------------------------------------+
|2015-04-08 15:00:00|                                      2015-04-08 00:00:00|
+-------------------+---------------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.curdate — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.curdate

pyspark.sql.functions.curdate()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#curdate)
[#](#pyspark.sql.functions.curdate "Permalink to this definition")

Returns the current date at the start of query evaluation as a `DateType` column. All calls of current\_date within the same query return the same value.

New in version 3.5.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

current date.

See also

[`pyspark.sql.functions.now()`](about:blank/pyspark.sql.functions.now.html#pyspark.sql.functions.now "pyspark.sql.functions.now")

[`pyspark.sql.functions.current_date()`](about:blank/pyspark.sql.functions.current_date.html#pyspark.sql.functions.current_date "pyspark.sql.functions.current_date")

[`pyspark.sql.functions.current_timestamp()`](about:blank/pyspark.sql.functions.current_timestamp.html#pyspark.sql.functions.current_timestamp "pyspark.sql.functions.current_timestamp")

[`pyspark.sql.functions.localtimestamp()`](about:blank/pyspark.sql.functions.localtimestamp.html#pyspark.sql.functions.localtimestamp "pyspark.sql.functions.localtimestamp")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.curdate()).show() 
+--------------+
|current_date()|
+--------------+
|    2022-08-26|
+--------------+

```


# pyspark.sql.functions.current_date — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.current\_date

pyspark.sql.functions.current\_date()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_date)
[#](#pyspark.sql.functions.current_date "Permalink to this definition")

Returns the current date at the start of query evaluation as a `DateType` column. All calls of current\_date within the same query return the same value.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

current date.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.current_date()).show() 
+--------------+
|current_date()|
+--------------+
|    2022-08-26|
+--------------+

```


# pyspark.sql.functions.current_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.current\_timestamp()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_timestamp)
[#](#pyspark.sql.functions.current_timestamp "Permalink to this definition")

Returns the current timestamp at the start of query evaluation as a `TimestampType` column. All calls of current\_timestamp within the same query return the same value.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

current date and time.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.current_timestamp()).show(truncate=False) 
+-----------------------+
|current_timestamp()    |
+-----------------------+
|2022-08-26 21:23:22.716|
+-----------------------+

```


# pyspark.sql.functions.current_timezone — PySpark 4.0.1 documentation
pyspark.sql.functions.current\_timezone()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_timezone)
[#](#pyspark.sql.functions.current_timezone "Permalink to this definition")

Returns the current session local timezone.

New in version 3.5.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

current session local timezone.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.current_timezone()).show()
+-------------------+
| current_timezone()|
+-------------------+
|America/Los_Angeles|
+-------------------+

```


Switch the timezone to Shanghai.

```
>>> spark.conf.set("spark.sql.session.timeZone", "Asia/Shanghai")
>>> spark.range(1).select(sf.current_timezone()).show()
+------------------+
|current_timezone()|
+------------------+
|     Asia/Shanghai|
+------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.date_add — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_add(_start_, _days_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_add)
[#](#pyspark.sql.functions.date_add "Permalink to this definition")

Returns the date that is days days after start. If days is a negative value then these amount of days will be deducted from start.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

date column to work on.

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

how many days after the given date to calculate. Accepts negative value as well to calculate backwards in time.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a date after/before given number of days.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08', 2,)], 'struct<dt:string,a:int>')
>>> df.select('*', sf.date_add(df.dt, 1)).show()
+----------+---+---------------+
|        dt|  a|date_add(dt, 1)|
+----------+---+---------------+
|2015-04-08|  2|     2015-04-09|
+----------+---+---------------+

```


```
>>> df.select('*', sf.date_add('dt', 'a')).show()
+----------+---+---------------+
|        dt|  a|date_add(dt, a)|
+----------+---+---------------+
|2015-04-08|  2|     2015-04-10|
+----------+---+---------------+

```


```
>>> df.select('*', sf.date_add('dt', sf.lit(-1))).show()
+----------+---+----------------+
|        dt|  a|date_add(dt, -1)|
+----------+---+----------------+
|2015-04-08|  2|      2015-04-07|
+----------+---+----------------+

```


# pyspark.sql.functions.date_diff — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_diff(_end_, _start_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_diff)
[#](#pyspark.sql.functions.date_diff "Permalink to this definition")

Returns the number of days from start to end.

New in version 3.5.0.

Parameters

**end**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

to date column to work on.

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

from date column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

difference in days between two dates.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08','2015-05-10')], ['d1', 'd2'])
>>> df.select('*', sf.date_diff('d1', 'd2')).show()
+----------+----------+-----------------+
|        d1|        d2|date_diff(d1, d2)|
+----------+----------+-----------------+
|2015-04-08|2015-05-10|              -32|
+----------+----------+-----------------+

```


```
>>> df.select('*', sf.date_diff(df.d2, df.d1)).show()
+----------+----------+-----------------+
|        d1|        d2|date_diff(d2, d1)|
+----------+----------+-----------------+
|2015-04-08|2015-05-10|               32|
+----------+----------+-----------------+

```

# pyspark.sql.functions.date_format — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_format(_date_, _format_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_format)
[#](#pyspark.sql.functions.date_format "Permalink to this definition")

Converts a date/timestamp/string to a value of string in the format specified by the date format given by the second argument.

A pattern could be for instance dd.MM.yyyy and could return a string like ‘18.03.1993’. All pattern letters of [datetime pattern](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html). can be used.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**date**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to format.

**format: literal string**

format to use to represent datetime values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string value representing formatted datetime.

Notes

Whenever possible, use specialized functions like year.

Examples

Example 1: Format a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.date_format('dt', 'MM/dd/yyyy')).show()
+----------+----------+---------------------------+
|        dt|typeof(dt)|date_format(dt, MM/dd/yyyy)|
+----------+----------+---------------------------+
|2015-04-08|    string|                 04/08/2015|
|2024-10-31|    string|                 10/31/2024|
+----------+----------+---------------------------+

```


Example 2: Format a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.date_format('ts', 'yy=MM=dd HH=mm=ss')).show()
+-------------------+----------+----------------------------------+
|                 ts|typeof(ts)|date_format(ts, yy=MM=dd HH=mm=ss)|
+-------------------+----------+----------------------------------+
|2015-04-08 13:08:15|    string|                 15=04=08 13=08=15|
|2024-10-31 10:09:16|    string|                 24=10=31 10=09=16|
+-------------------+----------+----------------------------------+

```


Example 3: Format a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.date_format('dt', 'yy--MM--dd')).show()
+----------+----------+---------------------------+
|        dt|typeof(dt)|date_format(dt, yy--MM--dd)|
+----------+----------+---------------------------+
|2015-04-08|      date|                 15--04--08|
|2024-10-31|      date|                 24--10--31|
+----------+----------+---------------------------+

```


Example 4: Format a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.date_format('ts', 'yy=MM=dd HH=mm=ss')).show()
+-------------------+----------+----------------------------------+
|                 ts|typeof(ts)|date_format(ts, yy=MM=dd HH=mm=ss)|
+-------------------+----------+----------------------------------+
|2015-04-08 13:08:15| timestamp|                 15=04=08 13=08=15|
|2024-10-31 10:09:16| timestamp|                 24=10=31 10=09=16|
+-------------------+----------+----------------------------------+

```


# pyspark.sql.functions.date_from_unix_date — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_from\_unix\_date(_days_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_from_unix_date)
[#](#pyspark.sql.functions.date_from_unix_date "Permalink to this definition")

Create date from the number of days since 1970-01-01.

New in version 3.5.0.

Parameters

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the date from the number of days since 1970-01-01.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(4).select('*', sf.date_from_unix_date('id')).show()
+---+-----------------------+
| id|date_from_unix_date(id)|
+---+-----------------------+
|  0|             1970-01-01|
|  1|             1970-01-02|
|  2|             1970-01-03|
|  3|             1970-01-04|
+---+-----------------------+

```



# pyspark.sql.functions.date_part — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_part(_field_, _source_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_part)
[#](#pyspark.sql.functions.date_part "Permalink to this definition")

Extracts a part of the date/timestamp or interval source.

New in version 3.5.0.

Parameters

**field**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

selects which part of the source should be extracted, and supported string values are as same as the fields of the equivalent function extract.

**source**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

a date/timestamp or interval column from where field should be extracted.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a part of the date/timestamp or interval source.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(datetime.datetime(2015, 4, 8, 13, 8, 15),)], ['ts'])
>>> df.select(
...     '*',
...     sf.date_part(sf.lit('YEAR'), 'ts').alias('year'),
...     sf.date_part(sf.lit('month'), 'ts').alias('month'),
...     sf.date_part(sf.lit('WEEK'), 'ts').alias('week'),
...     sf.date_part(sf.lit('D'), df.ts).alias('day'),
...     sf.date_part(sf.lit('M'), df.ts).alias('minute'),
...     sf.date_part(sf.lit('S'), df.ts).alias('second')
... ).show()
+-------------------+----+-----+----+---+------+---------+
|                 ts|year|month|week|day|minute|   second|
+-------------------+----+-----+----+---+------+---------+
|2015-04-08 13:08:15|2015|    4|  15|  8|     8|15.000000|
+-------------------+----+-----+----+---+------+---------+

```
# pyspark.sql.functions.date_sub — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_sub(_start_, _days_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_sub)
[#](#pyspark.sql.functions.date_sub "Permalink to this definition")

Returns the date that is days days before start. If days is a negative value then these amount of days will be added to start.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

date column to work on.

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

how many days before the given date to calculate. Accepts negative value as well to calculate forward in time.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a date before/after given number of days.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08', 2,)], 'struct<dt:string,a:int>')
>>> df.select('*', sf.date_sub(df.dt, 1)).show()
+----------+---+---------------+
|        dt|  a|date_sub(dt, 1)|
+----------+---+---------------+
|2015-04-08|  2|     2015-04-07|
+----------+---+---------------+

```


```
>>> df.select('*', sf.date_sub('dt', 'a')).show()
+----------+---+---------------+
|        dt|  a|date_sub(dt, a)|
+----------+---+---------------+
|2015-04-08|  2|     2015-04-06|
+----------+---+---------------+

```


```
>>> df.select('*', sf.date_sub('dt', sf.lit(-1))).show()
+----------+---+----------------+
|        dt|  a|date_sub(dt, -1)|
+----------+---+----------------+
|2015-04-08|  2|      2015-04-09|
+----------+---+----------------+

```

# pyspark.sql.functions.date_trunc — PySpark 4.0.1 documentation
pyspark.sql.functions.date\_trunc(_format_, _timestamp_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#date_trunc)
[#](#pyspark.sql.functions.date_trunc "Permalink to this definition")

Returns timestamp truncated to the unit specified by the format.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**format**literal string

‘year’, ‘yyyy’, ‘yy’ to truncate by year, ‘month’, ‘mon’, ‘mm’ to truncate by month, ‘day’, ‘dd’ to truncate by day, Other options are: ‘microsecond’, ‘millisecond’, ‘second’, ‘minute’, ‘hour’, ‘week’, ‘quarter’

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to truncate.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

truncated timestamp.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('1997-02-28 05:02:11',)], ['ts'])
>>> df.select('*', sf.date_trunc('year', df.ts)).show()
+-------------------+--------------------+
|                 ts|date_trunc(year, ts)|
+-------------------+--------------------+
|1997-02-28 05:02:11| 1997-01-01 00:00:00|
+-------------------+--------------------+

```


```
>>> df.select('*', sf.date_trunc('mon', 'ts')).show()
+-------------------+-------------------+
|                 ts|date_trunc(mon, ts)|
+-------------------+-------------------+
|1997-02-28 05:02:11|1997-02-01 00:00:00|
+-------------------+-------------------+

```



# pyspark.sql.functions.dateadd — PySpark 4.0.1 documentation
pyspark.sql.functions.dateadd(_start_, _days_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#dateadd)
[#](#pyspark.sql.functions.dateadd "Permalink to this definition")

Returns the date that is days days after start. If days is a negative value then these amount of days will be deducted from start.

New in version 3.5.0.

Parameters

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

date column to work on.

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name or int

how many days after the given date to calculate. Accepts negative value as well to calculate backwards in time.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a date after/before given number of days.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08', 2,)], 'struct<dt:string,a:int>')
>>> df.select('*', sf.dateadd(df.dt, 1)).show()
+----------+---+---------------+
|        dt|  a|date_add(dt, 1)|
+----------+---+---------------+
|2015-04-08|  2|     2015-04-09|
+----------+---+---------------+

```


```
>>> df.select('*', sf.dateadd('dt', 'a')).show()
+----------+---+---------------+
|        dt|  a|date_add(dt, a)|
+----------+---+---------------+
|2015-04-08|  2|     2015-04-10|
+----------+---+---------------+

```


```
>>> df.select('*', sf.dateadd('dt', sf.lit(-1))).show()
+----------+---+----------------+
|        dt|  a|date_add(dt, -1)|
+----------+---+----------------+
|2015-04-08|  2|      2015-04-07|
+----------+---+----------------+

```


# pyspark.sql.functions.datediff — PySpark 4.0.1 documentation
pyspark.sql.functions.datediff(_end_, _start_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#datediff)
[#](#pyspark.sql.functions.datediff "Permalink to this definition")

Returns the number of days from start to end.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**end**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

to date column to work on.

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

from date column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

difference in days between two dates.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08','2015-05-10')], ['d1', 'd2'])
>>> df.select('*', sf.datediff('d1', 'd2')).show()
+----------+----------+----------------+
|        d1|        d2|datediff(d1, d2)|
+----------+----------+----------------+
|2015-04-08|2015-05-10|             -32|
+----------+----------+----------------+

```


```
>>> df.select('*', sf.datediff(df.d2, df.d1)).show()
+----------+----------+----------------+
|        d1|        d2|datediff(d2, d1)|
+----------+----------+----------------+
|2015-04-08|2015-05-10|              32|
+----------+----------+----------------+

```


# pyspark.sql.functions.datepart — PySpark 4.0.1 documentation
pyspark.sql.functions.datepart(_field_, _source_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#datepart)
[#](#pyspark.sql.functions.datepart "Permalink to this definition")

Extracts a part of the date/timestamp or interval source.

New in version 3.5.0.

Parameters

**field**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

selects which part of the source should be extracted, and supported string values are as same as the fields of the equivalent function extract.

**source**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

a date/timestamp or interval column from where field should be extracted.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a part of the date/timestamp or interval source.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(datetime.datetime(2015, 4, 8, 13, 8, 15),)], ['ts'])
>>> df.select(
...     '*',
...     sf.datepart(sf.lit('YEAR'), 'ts').alias('year'),
...     sf.datepart(sf.lit('month'), 'ts').alias('month'),
...     sf.datepart(sf.lit('WEEK'), 'ts').alias('week'),
...     sf.datepart(sf.lit('D'), df.ts).alias('day'),
...     sf.datepart(sf.lit('M'), df.ts).alias('minute'),
...     sf.datepart(sf.lit('S'), df.ts).alias('second')
... ).show()
+-------------------+----+-----+----+---+------+---------+
|                 ts|year|month|week|day|minute|   second|
+-------------------+----+-----+----+---+------+---------+
|2015-04-08 13:08:15|2015|    4|  15|  8|     8|15.000000|
+-------------------+----+-----+----+---+------+---------+

```


# pyspark.sql.functions.day — PySpark 4.0.1 documentation
pyspark.sql.functions.day(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#day)
[#](#pyspark.sql.functions.day "Permalink to this definition")

Extract the day of the month of a given date/timestamp as integer.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

day of the month for given date/timestamp as integer.

Examples

Example 1: Extract the day of the month from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.day('dt')).show()
+----------+----------+-------+
|        dt|typeof(dt)|day(dt)|
+----------+----------+-------+
|2015-04-08|    string|      8|
|2024-10-31|    string|     31|
+----------+----------+-------+

```


Example 2: Extract the day of the month from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.day('ts')).show()
+-------------------+----------+-------+
|                 ts|typeof(ts)|day(ts)|
+-------------------+----------+-------+
|2015-04-08 13:08:15|    string|      8|
|2024-10-31 10:09:16|    string|     31|
+-------------------+----------+-------+

```


Example 3: Extract the day of the month from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.day('dt')).show()
+----------+----------+-------+
|        dt|typeof(dt)|day(dt)|
+----------+----------+-------+
|2015-04-08|      date|      8|
|2024-10-31|      date|     31|
+----------+----------+-------+

```


Example 4: Extract the day of the month from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.day('ts')).show()
+-------------------+----------+-------+
|                 ts|typeof(ts)|day(ts)|
+-------------------+----------+-------+
|2015-04-08 13:08:15| timestamp|      8|
|2024-10-31 10:09:16| timestamp|     31|
+-------------------+----------+-------+

```

# pyspark.sql.functions.dayname — PySpark 4.0.1 documentation
pyspark.sql.functions.dayname(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#dayname)
[#](#pyspark.sql.functions.dayname "Permalink to this definition")

Date and Timestamp Function: Returns the three-letter abbreviated day name from the given date.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the three-letter abbreviation of day name for date/timestamp (Mon, Tue, Wed…)

Examples

Example 1: Extract the weekday name from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayname('dt')).show()
+----------+----------+-----------+
|        dt|typeof(dt)|dayname(dt)|
+----------+----------+-----------+
|2015-04-08|    string|        Wed|
|2024-10-31|    string|        Thu|
+----------+----------+-----------+

```


Example 2: Extract the weekday name from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayname('ts')).show()
+-------------------+----------+-----------+
|                 ts|typeof(ts)|dayname(ts)|
+-------------------+----------+-----------+
|2015-04-08 13:08:15|    string|        Wed|
|2024-10-31 10:09:16|    string|        Thu|
+-------------------+----------+-----------+

```


Example 3: Extract the weekday name from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayname('dt')).show()
+----------+----------+-----------+
|        dt|typeof(dt)|dayname(dt)|
+----------+----------+-----------+
|2015-04-08|      date|        Wed|
|2024-10-31|      date|        Thu|
+----------+----------+-----------+

```


Example 4: Extract the weekday name from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayname('ts')).show()
+-------------------+----------+-----------+
|                 ts|typeof(ts)|dayname(ts)|
+-------------------+----------+-----------+
|2015-04-08 13:08:15| timestamp|        Wed|
|2024-10-31 10:09:16| timestamp|        Thu|
+-------------------+----------+-----------+

```



# pyspark.sql.functions.dayofmonth — PySpark 4.0.1 documentation
pyspark.sql.functions.dayofmonth(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#dayofmonth)
[#](#pyspark.sql.functions.dayofmonth "Permalink to this definition")

Extract the day of the month of a given date/timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

day of the month for given date/timestamp as integer.

Examples

Example 1: Extract the day of the month from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayofmonth('dt')).show()
+----------+----------+--------------+
|        dt|typeof(dt)|dayofmonth(dt)|
+----------+----------+--------------+
|2015-04-08|    string|             8|
|2024-10-31|    string|            31|
+----------+----------+--------------+

```


Example 2: Extract the day of the month from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayofmonth('ts')).show()
+-------------------+----------+--------------+
|                 ts|typeof(ts)|dayofmonth(ts)|
+-------------------+----------+--------------+
|2015-04-08 13:08:15|    string|             8|
|2024-10-31 10:09:16|    string|            31|
+-------------------+----------+--------------+

```


Example 3: Extract the day of the month from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayofmonth('dt')).show()
+----------+----------+--------------+
|        dt|typeof(dt)|dayofmonth(dt)|
+----------+----------+--------------+
|2015-04-08|      date|             8|
|2024-10-31|      date|            31|
+----------+----------+--------------+

```


Example 4: Extract the day of the month from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayofmonth('ts')).show()
+-------------------+----------+--------------+
|                 ts|typeof(ts)|dayofmonth(ts)|
+-------------------+----------+--------------+
|2015-04-08 13:08:15| timestamp|             8|
|2024-10-31 10:09:16| timestamp|            31|
+-------------------+----------+--------------+

```
# pyspark.sql.functions.dayofweek — PySpark 4.0.1 documentation
pyspark.sql.functions.dayofweek(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#dayofweek)
[#](#pyspark.sql.functions.dayofweek "Permalink to this definition")

Extract the day of the week of a given date/timestamp as integer. Ranges from 1 for a Sunday through to 7 for a Saturday

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

day of the week for given date/timestamp as integer.

Examples

Example 1: Extract the day of the week from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayofweek('dt')).show()
+----------+----------+-------------+
|        dt|typeof(dt)|dayofweek(dt)|
+----------+----------+-------------+
|2015-04-08|    string|            4|
|2024-10-31|    string|            5|
+----------+----------+-------------+

```


Example 2: Extract the day of the week from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayofweek('ts')).show()
+-------------------+----------+-------------+
|                 ts|typeof(ts)|dayofweek(ts)|
+-------------------+----------+-------------+
|2015-04-08 13:08:15|    string|            4|
|2024-10-31 10:09:16|    string|            5|
+-------------------+----------+-------------+

```


Example 3: Extract the day of the week from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayofweek('dt')).show()
+----------+----------+-------------+
|        dt|typeof(dt)|dayofweek(dt)|
+----------+----------+-------------+
|2015-04-08|      date|            4|
|2024-10-31|      date|            5|
+----------+----------+-------------+

```


Example 4: Extract the day of the week from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayofweek('ts')).show()
+-------------------+----------+-------------+
|                 ts|typeof(ts)|dayofweek(ts)|
+-------------------+----------+-------------+
|2015-04-08 13:08:15| timestamp|            4|
|2024-10-31 10:09:16| timestamp|            5|
+-------------------+----------+-------------+

```




# pyspark.sql.functions.dayofyear — PySpark 4.0.1 documentation
pyspark.sql.functions.dayofyear(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#dayofyear)
[#](#pyspark.sql.functions.dayofyear "Permalink to this definition")

Extract the day of the year of a given date/timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

day of the year for given date/timestamp as integer.

Examples

Example 1: Extract the day of the year from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayofyear('dt')).show()
+----------+----------+-------------+
|        dt|typeof(dt)|dayofyear(dt)|
+----------+----------+-------------+
|2015-04-08|    string|           98|
|2024-10-31|    string|          305|
+----------+----------+-------------+

```


Example 2: Extract the day of the year from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayofyear('ts')).show()
+-------------------+----------+-------------+
|                 ts|typeof(ts)|dayofyear(ts)|
+-------------------+----------+-------------+
|2015-04-08 13:08:15|    string|           98|
|2024-10-31 10:09:16|    string|          305|
+-------------------+----------+-------------+

```


Example 3: Extract the day of the year from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.dayofyear('dt')).show()
+----------+----------+-------------+
|        dt|typeof(dt)|dayofyear(dt)|
+----------+----------+-------------+
|2015-04-08|      date|           98|
|2024-10-31|      date|          305|
+----------+----------+-------------+

```


Example 4: Extract the day of the year from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.dayofyear('ts')).show()
+-------------------+----------+-------------+
|                 ts|typeof(ts)|dayofyear(ts)|
+-------------------+----------+-------------+
|2015-04-08 13:08:15| timestamp|           98|
|2024-10-31 10:09:16| timestamp|          305|
+-------------------+----------+-------------+

```


# pyspark.sql.functions.extract — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.extract

pyspark.sql.functions.extract(_field_, _source_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#extract)
[#](#pyspark.sql.functions.extract "Permalink to this definition")

Extracts a part of the date/timestamp or interval source.

New in version 3.5.0.

Parameters

**field**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

selects which part of the source should be extracted.

**source**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

a date/timestamp or interval column from where field should be extracted.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a part of the date/timestamp or interval source.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(datetime.datetime(2015, 4, 8, 13, 8, 15),)], ['ts'])
>>> df.select(
...     '*',
...     sf.extract(sf.lit('YEAR'), 'ts').alias('year'),
...     sf.extract(sf.lit('month'), 'ts').alias('month'),
...     sf.extract(sf.lit('WEEK'), 'ts').alias('week'),
...     sf.extract(sf.lit('D'), df.ts).alias('day'),
...     sf.extract(sf.lit('M'), df.ts).alias('minute'),
...     sf.extract(sf.lit('S'), df.ts).alias('second')
... ).show()
+-------------------+----+-----+----+---+------+---------+
|                 ts|year|month|week|day|minute|   second|
+-------------------+----+-----+----+---+------+---------+
|2015-04-08 13:08:15|2015|    4|  15|  8|     8|15.000000|
+-------------------+----+-----+----+---+------+---------+

```

# pyspark.sql.functions.from_unixtime — PySpark 4.0.1 documentation
pyspark.sql.functions.from\_unixtime(_timestamp_, _format\='yyyy-MM-dd HH:mm:ss'_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#from_unixtime)
[#](#pyspark.sql.functions.from_unixtime "Permalink to this definition")

Converts the number of seconds from unix epoch (1970-01-01 00:00:00 UTC) to a string representing the timestamp of that moment in the current system time zone in the given format.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column of unix time values.

**format**literal string, optional

format to use to convert to (default: yyyy-MM-dd HH:mm:ss)

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

formatted timestamp as string.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1428476400,)], ['unix_time'])
>>> df.select('*', sf.from_unixtime('unix_time')).show()
+----------+---------------------------------------------+
| unix_time|from_unixtime(unix_time, yyyy-MM-dd HH:mm:ss)|
+----------+---------------------------------------------+
|1428476400|                          2015-04-08 00:00:00|
+----------+---------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```

# pyspark.sql.functions.from_utc_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.from\_utc\_timestamp(_timestamp_, _tz_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#from_utc_timestamp)
[#](#pyspark.sql.functions.from_utc_timestamp "Permalink to this definition")

This is a common function for databases supporting TIMESTAMP WITHOUT TIMEZONE. This function takes a timestamp which is timezone-agnostic, and interprets it as a timestamp in UTC, and renders that timestamp as a timestamp in the given time zone.

However, timestamp in Spark represents number of microseconds from the Unix epoch, which is not timezone-agnostic. So in Spark this function just shift the timestamp value from UTC timezone to the given timezone.

This function may return confusing result if the input is a string with timezone, e.g. ‘2018-03-13T06:18:23+00:00’. The reason is that, Spark firstly cast the string to timestamp according to the timezone in the string, and finally display the result by converting the timestamp to string according to the session local timezone.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the column that contains timestamps

**tz**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

A string detailing the time zone ID that the input should be adjusted to. It should be in the format of either region-based zone IDs or zone offsets. Region IDs must have the form ‘area/city’, such as ‘America/Los\_Angeles’. Zone offsets must be in the format ‘(+|-)HH:mm’, for example ‘-08:00’ or ‘+01:00’. Also ‘UTC’ and ‘Z’ are supported as aliases of ‘+00:00’. Other short names are not recommended to use because they can be ambiguous.

Changed in version 2.4: tz can take a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") containing timezone ID strings.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

timestamp value represented in given timezone.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00', 'JST')], ['ts', 'tz'])
>>> df.select('*', sf.from_utc_timestamp('ts', 'PST')).show()
+-------------------+---+---------------------------+
|                 ts| tz|from_utc_timestamp(ts, PST)|
+-------------------+---+---------------------------+
|1997-02-28 10:30:00|JST|        1997-02-28 02:30:00|
+-------------------+---+---------------------------+

```


```
>>> df.select('*', sf.from_utc_timestamp(df.ts, df.tz)).show()
+-------------------+---+--------------------------+
|                 ts| tz|from_utc_timestamp(ts, tz)|
+-------------------+---+--------------------------+
|1997-02-28 10:30:00|JST|       1997-02-28 19:30:00|
+-------------------+---+--------------------------+

```


# pyspark.sql.functions.hour — PySpark 4.0.1 documentation
pyspark.sql.functions.hour(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hour)
[#](#pyspark.sql.functions.hour "Permalink to this definition")

Extract the hours of a given timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hour part of the timestamp as integer.

Examples

Example 1: Extract the hours from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.hour('ts')).show()
+-------------------+----------+--------+
|                 ts|typeof(ts)|hour(ts)|
+-------------------+----------+--------+
|2015-04-08 13:08:15|    string|      13|
|2024-10-31 10:09:16|    string|      10|
+-------------------+----------+--------+

```


Example 2: Extract the hours from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.hour('ts')).show()
+-------------------+----------+--------+
|                 ts|typeof(ts)|hour(ts)|
+-------------------+----------+--------+
|2015-04-08 13:08:15| timestamp|      13|
|2024-10-31 10:09:16| timestamp|      10|
+-------------------+----------+--------+

```


# pyspark.sql.functions.last_day — PySpark 4.0.1 documentation
pyspark.sql.functions.last\_day(_date_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#last_day)
[#](#pyspark.sql.functions.last_day "Permalink to this definition")

Returns the last day of the month which the given date belongs to.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**date**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

last day of the month.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('1997-02-10',)], ['dt'])
>>> df.select('*', sf.last_day(df.dt)).show()
+----------+------------+
|        dt|last_day(dt)|
+----------+------------+
|1997-02-10|  1997-02-28|
+----------+------------+

```


```
>>> df.select('*', sf.last_day('dt')).show()
+----------+------------+
|        dt|last_day(dt)|
+----------+------------+
|1997-02-10|  1997-02-28|
+----------+------------+

```


# pyspark.sql.functions.localtimestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.localtimestamp()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#localtimestamp)
[#](#pyspark.sql.functions.localtimestamp "Permalink to this definition")

Returns the current timestamp without time zone at the start of query evaluation as a timestamp without time zone column. All calls of localtimestamp within the same query return the same value.

New in version 3.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

current local date and time.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.localtimestamp()).show(truncate=False) 
+-----------------------+
|localtimestamp()       |
+-----------------------+
|2022-08-26 21:28:34.639|
+-----------------------+

```

# pyspark.sql.functions.make_date — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_date(_year_, _month_, _day_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_date)
[#](#pyspark.sql.functions.make_date "Permalink to this definition")

Returns a column with a date built from the year, month and day columns.

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**year**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The year to build the date

**month**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The month to build the date

**day**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The day to build the date

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a date built from given parts.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2020, 6, 26)], ['Y', 'M', 'D'])
>>> df.select('*', sf.make_date(df.Y, 'M', df.D)).show()
+----+---+---+------------------+
|   Y|  M|  D|make_date(Y, M, D)|
+----+---+---+------------------+
|2020|  6| 26|        2020-06-26|
+----+---+---+------------------+

```


# pyspark.sql.functions.make_dt_interval — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_dt\_interval(_days\=None_, _hours\=None_, _mins\=None_, _secs\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_dt_interval)
[#](#pyspark.sql.functions.make_dt_interval "Permalink to this definition")

Make DayTimeIntervalType duration from days, hours, mins and secs.

New in version 3.5.0.

Parameters

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of days, positive or negative.

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of hours, positive or negative.

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of minutes, positive or negative.

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of seconds with the fractional part in microsecond precision.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a DayTimeIntervalType duration.

Examples

Example 1: Make DayTimeIntervalType duration from days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[1, 12, 30, 01.001001]], ['day', 'hour', 'min', 'sec'])
>>> df.select('*', sf.make_dt_interval(df.day, df.hour, df.min, df.sec)).show(truncate=False)
+---+----+---+--------+------------------------------------------+
|day|hour|min|sec     |make_dt_interval(day, hour, min, sec)     |
+---+----+---+--------+------------------------------------------+
|1  |12  |30 |1.001001|INTERVAL '1 12:30:01.001001' DAY TO SECOND|
+---+----+---+--------+------------------------------------------+

```


Example 2: Make DayTimeIntervalType duration from days, hours and mins.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[1, 12, 30, 01.001001]], ['day', 'hour', 'min', 'sec'])
>>> df.select('*', sf.make_dt_interval(df.day, 'hour', df.min)).show(truncate=False)
+---+----+---+--------+-----------------------------------+
|day|hour|min|sec     |make_dt_interval(day, hour, min, 0)|
+---+----+---+--------+-----------------------------------+
|1  |12  |30 |1.001001|INTERVAL '1 12:30:00' DAY TO SECOND|
+---+----+---+--------+-----------------------------------+

```


Example 3: Make DayTimeIntervalType duration from days and hours.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[1, 12, 30, 01.001001]], ['day', 'hour', 'min', 'sec'])
>>> df.select('*', sf.make_dt_interval(df.day, df.hour)).show(truncate=False)
+---+----+---+--------+-----------------------------------+
|day|hour|min|sec     |make_dt_interval(day, hour, 0, 0)  |
+---+----+---+--------+-----------------------------------+
|1  |12  |30 |1.001001|INTERVAL '1 12:00:00' DAY TO SECOND|
+---+----+---+--------+-----------------------------------+

```


Example 4: Make DayTimeIntervalType duration from days.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[1, 12, 30, 01.001001]], ['day', 'hour', 'min', 'sec'])
>>> df.select('*', sf.make_dt_interval('day')).show(truncate=False)
+---+----+---+--------+-----------------------------------+
|day|hour|min|sec     |make_dt_interval(day, 0, 0, 0)     |
+---+----+---+--------+-----------------------------------+
|1  |12  |30 |1.001001|INTERVAL '1 00:00:00' DAY TO SECOND|
+---+----+---+--------+-----------------------------------+

```


Example 5: Make empty interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.make_dt_interval()).show(truncate=False)
+-----------------------------------+
|make_dt_interval(0, 0, 0, 0)       |
+-----------------------------------+
|INTERVAL '0 00:00:00' DAY TO SECOND|
+-----------------------------------+

```

# pyspark.sql.functions.make_interval — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_interval(_years\=None_, _months\=None_, _weeks\=None_, _days\=None_, _hours\=None_, _mins\=None_, _secs\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_interval)
[#](#pyspark.sql.functions.make_interval "Permalink to this definition")

Make interval from years, months, weeks, days, hours, mins and secs.

New in version 3.5.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of years, positive or negative.

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of months, positive or negative.

**weeks**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of weeks, positive or negative.

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of days, positive or negative.

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of hours, positive or negative.

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of minutes, positive or negative.

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of seconds with the fractional part in microsecond precision.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains an interval.

Examples

Example 1: Make interval from years, months, weeks, days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.make_interval(df.year, df.month, 'week', df.day, df.hour, df.min, df.sec)
... ).show(truncate=False)
+---------------------------------------------------------------+
|make_interval(year, month, week, day, hour, min, sec)          |
+---------------------------------------------------------------+
|100 years 11 months 8 days 12 hours 30 minutes 1.001001 seconds|
+---------------------------------------------------------------+

```


Example 2: Make interval from years, months, weeks, days, hours and mins.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.make_interval(df.year, df.month, 'week', df.day, df.hour, df.min)
... ).show(truncate=False)
+---------------------------------------------------+
|make_interval(year, month, week, day, hour, min, 0)|
+---------------------------------------------------+
|100 years 11 months 8 days 12 hours 30 minutes     |
+---------------------------------------------------+

```


Example 3: Make interval from years, months, weeks, days and hours.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.make_interval(df.year, df.month, 'week', df.day, df.hour)
... ).show(truncate=False)
+-------------------------------------------------+
|make_interval(year, month, week, day, hour, 0, 0)|
+-------------------------------------------------+
|100 years 11 months 8 days 12 hours              |
+-------------------------------------------------+

```


Example 4: Make interval from years, months, weeks and days.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.make_interval(df.year, df.month, 'week', df.day)).show(truncate=False)
+----------------------------------------------+
|make_interval(year, month, week, day, 0, 0, 0)|
+----------------------------------------------+
|100 years 11 months 8 days                    |
+----------------------------------------------+

```


Example 5: Make interval from years, months and weeks.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.make_interval(df.year, df.month, 'week')).show(truncate=False)
+--------------------------------------------+
|make_interval(year, month, week, 0, 0, 0, 0)|
+--------------------------------------------+
|100 years 11 months 7 days                  |
+--------------------------------------------+

```


Example 6: Make interval from years and months.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.make_interval(df.year, df.month)).show(truncate=False)
+-----------------------------------------+
|make_interval(year, month, 0, 0, 0, 0, 0)|
+-----------------------------------------+
|100 years 11 months                      |
+-----------------------------------------+

```


Example 7: Make interval from years.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.make_interval(df.year)).show(truncate=False)
+-------------------------------------+
|make_interval(year, 0, 0, 0, 0, 0, 0)|
+-------------------------------------+
|100 years                            |
+-------------------------------------+

```


Example 8: Make empty interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.make_interval()).show(truncate=False)
+----------------------------------+
|make_interval(0, 0, 0, 0, 0, 0, 0)|
+----------------------------------+
|0 seconds                         |
+----------------------------------+

```


# pyspark.sql.functions.make_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_timestamp(_years_, _months_, _days_, _hours_, _mins_, _secs_, _timezone\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_timestamp)
[#](#pyspark.sql.functions.make_timestamp "Permalink to this definition")

Create timestamp from years, months, days, hours, mins, secs and timezone fields. The result data type is consistent with the value of configuration spark.sql.timestampType. If the configuration spark.sql.ansi.enabled is false, the function returns NULL on invalid inputs. Otherwise, it will throw an error instead.

New in version 3.5.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The year to represent, from 1 to 9999

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The month-of-year to represent, from 1 (January) to 12 (December)

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The day-of-month to represent, from 1 to 31

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The hour-of-day to represent, from 0 to 23

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The minute-of-hour to represent, from 0 to 59

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The second-of-minute and its micro-fraction to represent, from 0 to 60. The value can be either an integer like 13 , or a fraction like 13.123. If the sec argument equals to 60, the seconds field is set to 0 and 1 minute is added to the final timestamp.

**timezone**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The time zone identifier. For example, CET, UTC and etc.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a timestamp.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Make timestamp from years, months, days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.make_timestamp(df.year, df.month, df.day, 'hour', df.min, df.sec, 'tz')
... ).show(truncate=False)
+----------------------------------------------------+
|make_timestamp(year, month, day, hour, min, sec, tz)|
+----------------------------------------------------+
|2014-12-27 21:30:45.887                             |
+----------------------------------------------------+

```


Example 2: Make timestamp without timezone.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.make_timestamp(df.year, df.month, df.day, 'hour', df.min, df.sec)
... ).show(truncate=False)
+------------------------------------------------+
|make_timestamp(year, month, day, hour, min, sec)|
+------------------------------------------------+
|2014-12-28 06:30:45.887                         |
+------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.make_timestamp_ltz — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_timestamp\_ltz(_years_, _months_, _days_, _hours_, _mins_, _secs_, _timezone\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_timestamp_ltz)
[#](#pyspark.sql.functions.make_timestamp_ltz "Permalink to this definition")

Create the current timestamp with local time zone from years, months, days, hours, mins, secs and timezone fields. If the configuration spark.sql.ansi.enabled is false, the function returns NULL on invalid inputs. Otherwise, it will throw an error instead.

New in version 3.5.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The year to represent, from 1 to 9999

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The month-of-year to represent, from 1 (January) to 12 (December)

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The day-of-month to represent, from 1 to 31

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The hour-of-day to represent, from 0 to 23

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The minute-of-hour to represent, from 0 to 59

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The second-of-minute and its micro-fraction to represent, from 0 to 60. The value can be either an integer like 13 , or a fraction like 13.123. If the sec argument equals to 60, the seconds field is set to 0 and 1 minute is added to the final timestamp.

**timezone**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

The time zone identifier. For example, CET, UTC and etc.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a current timestamp.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Make the current timestamp from years, months, days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.make_timestamp_ltz(df.year, df.month, 'day', df.hour, df.min, df.sec, 'tz')
... ).show(truncate=False)
+--------------------------------------------------------+
|make_timestamp_ltz(year, month, day, hour, min, sec, tz)|
+--------------------------------------------------------+
|2014-12-27 21:30:45.887                                 |
+--------------------------------------------------------+

```


Example 2: Make the current timestamp without timezone.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.make_timestamp_ltz(df.year, df.month, 'day', df.hour, df.min, df.sec)
... ).show(truncate=False)
+----------------------------------------------------+
|make_timestamp_ltz(year, month, day, hour, min, sec)|
+----------------------------------------------------+
|2014-12-28 06:30:45.887                             |
+----------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.make_timestamp_ntz — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_timestamp\_ntz(_years_, _months_, _days_, _hours_, _mins_, _secs_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_timestamp_ntz)
[#](#pyspark.sql.functions.make_timestamp_ntz "Permalink to this definition")

Create local date-time from years, months, days, hours, mins, secs fields. If the configuration spark.sql.ansi.enabled is false, the function returns NULL on invalid inputs. Otherwise, it will throw an error instead.

New in version 3.5.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The year to represent, from 1 to 9999

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The month-of-year to represent, from 1 (January) to 12 (December)

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The day-of-month to represent, from 1 to 31

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The hour-of-day to represent, from 0 to 23

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The minute-of-hour to represent, from 0 to 59

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The second-of-minute and its micro-fraction to represent, from 0 to 60. The value can be either an integer like 13 , or a fraction like 13.123. If the sec argument equals to 60, the seconds field is set to 0 and 1 minute is added to the final timestamp.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a local date-time.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887]],
...     ['year', 'month', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.make_timestamp_ntz('year', 'month', df.day, df.hour, df.min, df.sec)
... ).show(truncate=False)
+----------------------------------------------------+
|make_timestamp_ntz(year, month, day, hour, min, sec)|
+----------------------------------------------------+
|2014-12-28 06:30:45.887                             |
+----------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.make_ym_interval — PySpark 4.0.1 documentation
pyspark.sql.functions.make\_ym\_interval(_years\=None_, _months\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#make_ym_interval)
[#](#pyspark.sql.functions.make_ym_interval "Permalink to this definition")

Make year-month interval from years, months.

New in version 3.5.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of years, positive or negative

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of months, positive or negative

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a year-month interval.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Make year-month interval from years, months.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12]], ['year', 'month'])
>>> df.select('*', sf.make_ym_interval('year', df.month)).show(truncate=False)
+----+-----+-------------------------------+
|year|month|make_ym_interval(year, month)  |
+----+-----+-------------------------------+
|2014|12   |INTERVAL '2015-0' YEAR TO MONTH|
+----+-----+-------------------------------+

```


Example 2: Make year-month interval from years.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12]], ['year', 'month'])
>>> df.select('*', sf.make_ym_interval(df.year)).show(truncate=False)
+----+-----+-------------------------------+
|year|month|make_ym_interval(year, 0)      |
+----+-----+-------------------------------+
|2014|12   |INTERVAL '2014-0' YEAR TO MONTH|
+----+-----+-------------------------------+

```


Example 3: Make empty interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.make_ym_interval()).show(truncate=False)
+----------------------------+
|make_ym_interval(0, 0)      |
+----------------------------+
|INTERVAL '0-0' YEAR TO MONTH|
+----------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```



# pyspark.sql.functions.minute — PySpark 4.0.1 documentation
pyspark.sql.functions.minute(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#minute)
[#](#pyspark.sql.functions.minute "Permalink to this definition")

Extract the minutes of a given timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

minutes part of the timestamp as integer.

Examples

Example 1: Extract the minutes from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.minute('ts')).show()
+-------------------+----------+----------+
|                 ts|typeof(ts)|minute(ts)|
+-------------------+----------+----------+
|2015-04-08 13:08:15|    string|         8|
|2024-10-31 10:09:16|    string|         9|
+-------------------+----------+----------+

```


Example 2: Extract the minutes from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.minute('ts')).show()
+-------------------+----------+----------+
|                 ts|typeof(ts)|minute(ts)|
+-------------------+----------+----------+
|2015-04-08 13:08:15| timestamp|         8|
|2024-10-31 10:09:16| timestamp|         9|
+-------------------+----------+----------+

```



# pyspark.sql.functions.month — PySpark 4.0.1 documentation
pyspark.sql.functions.month(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#month)
[#](#pyspark.sql.functions.month "Permalink to this definition")

Extract the month of a given date/timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

month part of the date/timestamp as integer.

Examples

Example 1: Extract the month from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.month('dt')).show()
+----------+----------+---------+
|        dt|typeof(dt)|month(dt)|
+----------+----------+---------+
|2015-04-08|    string|        4|
|2024-10-31|    string|       10|
+----------+----------+---------+

```


Example 2: Extract the month from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.month('ts')).show()
+-------------------+----------+---------+
|                 ts|typeof(ts)|month(ts)|
+-------------------+----------+---------+
|2015-04-08 13:08:15|    string|        4|
|2024-10-31 10:09:16|    string|       10|
+-------------------+----------+---------+

```


Example 3: Extract the month from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.month('dt')).show()
+----------+----------+---------+
|        dt|typeof(dt)|month(dt)|
+----------+----------+---------+
|2015-04-08|      date|        4|
|2024-10-31|      date|       10|
+----------+----------+---------+

```


Example 3: Extract the month from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.month('ts')).show()
+-------------------+----------+---------+
|                 ts|typeof(ts)|month(ts)|
+-------------------+----------+---------+
|2015-04-08 13:08:15| timestamp|        4|
|2024-10-31 10:09:16| timestamp|       10|
+-------------------+----------+---------+

```



# pyspark.sql.functions.monthname — PySpark 4.0.1 documentation
pyspark.sql.functions.monthname(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#monthname)
[#](#pyspark.sql.functions.monthname "Permalink to this definition")

Returns the three-letter abbreviated month name from the given date.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the three-letter abbreviation of month name for date/timestamp (Jan, Feb, Mar…)

Examples

Example 1: Extract the month name from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.monthname('dt')).show()
+----------+----------+-------------+
|        dt|typeof(dt)|monthname(dt)|
+----------+----------+-------------+
|2015-04-08|    string|          Apr|
|2024-10-31|    string|          Oct|
+----------+----------+-------------+

```


Example 2: Extract the month name from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.monthname('ts')).show()
+-------------------+----------+-------------+
|                 ts|typeof(ts)|monthname(ts)|
+-------------------+----------+-------------+
|2015-04-08 13:08:15|    string|          Apr|
|2024-10-31 10:09:16|    string|          Oct|
+-------------------+----------+-------------+

```


Example 3: Extract the month name from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.monthname('dt')).show()
+----------+----------+-------------+
|        dt|typeof(dt)|monthname(dt)|
+----------+----------+-------------+
|2015-04-08|      date|          Apr|
|2024-10-31|      date|          Oct|
+----------+----------+-------------+

```


Example 4: Extract the month name from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.monthname('ts')).show()
+-------------------+----------+-------------+
|                 ts|typeof(ts)|monthname(ts)|
+-------------------+----------+-------------+
|2015-04-08 13:08:15| timestamp|          Apr|
|2024-10-31 10:09:16| timestamp|          Oct|
+-------------------+----------+-------------+

```


# pyspark.sql.functions.months_between — PySpark 4.0.1 documentation
pyspark.sql.functions.months\_between(_date1_, _date2_, _roundOff\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#months_between)
[#](#pyspark.sql.functions.months_between "Permalink to this definition")

Returns number of months between dates date1 and date2. If date1 is later than date2, then the result is positive. A whole number is returned if both inputs have the same day of month or both are the last day of their respective months. Otherwise, the difference is calculated assuming 31 days per month. The result is rounded off to 8 digits unless roundOff is set to False.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**date1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first date column.

**date2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

second date column.

**roundOff**bool, optional

whether to round (to 8 digits) the final value or not (default: True).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

number of months between two dates.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00', '1996-10-30')], ['d1', 'd2'])
>>> df.select('*', sf.months_between(df.d1, df.d2)).show()
+-------------------+----------+----------------------------+
|                 d1|        d2|months_between(d1, d2, true)|
+-------------------+----------+----------------------------+
|1997-02-28 10:30:00|1996-10-30|                  3.94959677|
+-------------------+----------+----------------------------+

```


```
>>> df.select('*', sf.months_between('d2', 'd1')).show()
+-------------------+----------+----------------------------+
|                 d1|        d2|months_between(d2, d1, true)|
+-------------------+----------+----------------------------+
|1997-02-28 10:30:00|1996-10-30|                 -3.94959677|
+-------------------+----------+----------------------------+

```


```
>>> df.select('*', sf.months_between('d1', df.d2, False)).show()
+-------------------+----------+-----------------------------+
|                 d1|        d2|months_between(d1, d2, false)|
+-------------------+----------+-----------------------------+
|1997-02-28 10:30:00|1996-10-30|           3.9495967741935...|
+-------------------+----------+-----------------------------+

```


# pyspark.sql.functions.next_day — PySpark 4.0.1 documentation
pyspark.sql.functions.next\_day(_date_, _dayOfWeek_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#next_day)
[#](#pyspark.sql.functions.next_day "Permalink to this definition")

Returns the first date which is later than the value of the date column based on second week day argument.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**date**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**dayOfWeek**literal string

day of the week, case-insensitive, accepts:

“Mon”, “Tue”, “Wed”, “Thu”, “Fri”, “Sat”, “Sun”

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column of computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-07-27',)], ['dt'])
>>> df.select('*', sf.next_day(df.dt, 'Sun')).show()
+----------+-----------------+
|        dt|next_day(dt, Sun)|
+----------+-----------------+
|2015-07-27|       2015-08-02|
+----------+-----------------+

```


```
>>> df.select('*', sf.next_day('dt', 'Sat')).show()
+----------+-----------------+
|        dt|next_day(dt, Sat)|
+----------+-----------------+
|2015-07-27|       2015-08-01|
+----------+-----------------+

```


# pyspark.sql.functions.now — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.now

pyspark.sql.functions.now()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#now)
[#](#pyspark.sql.functions.now "Permalink to this definition")

Returns the current timestamp at the start of query evaluation.

New in version 3.5.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

current timestamp at the start of query evaluation.

See also

[`pyspark.sql.functions.curdate()`](about:blank/pyspark.sql.functions.curdate.html#pyspark.sql.functions.curdate "pyspark.sql.functions.curdate")

[`pyspark.sql.functions.current_date()`](about:blank/pyspark.sql.functions.current_date.html#pyspark.sql.functions.current_date "pyspark.sql.functions.current_date")

[`pyspark.sql.functions.current_timestamp()`](about:blank/pyspark.sql.functions.current_timestamp.html#pyspark.sql.functions.current_timestamp "pyspark.sql.functions.current_timestamp")

[`pyspark.sql.functions.localtimestamp()`](about:blank/pyspark.sql.functions.localtimestamp.html#pyspark.sql.functions.localtimestamp "pyspark.sql.functions.localtimestamp")

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.now()).show(truncate=False) 
+--------------------------+
|now()                     |
+--------------------------+
|2023-12-08 15:18:18.482269|
+--------------------------+

```


# pyspark.sql.functions.quarter — PySpark 4.0.1 documentation
pyspark.sql.functions.quarter(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#quarter)
[#](#pyspark.sql.functions.quarter "Permalink to this definition")

Extract the quarter of a given date/timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

quarter of the date/timestamp as integer.

Examples

Example 1: Extract the quarter from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.quarter('dt')).show()
+----------+----------+-----------+
|        dt|typeof(dt)|quarter(dt)|
+----------+----------+-----------+
|2015-04-08|    string|          2|
|2024-10-31|    string|          4|
+----------+----------+-----------+

```


Example 2: Extract the quarter from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.quarter('ts')).show()
+-------------------+----------+-----------+
|                 ts|typeof(ts)|quarter(ts)|
+-------------------+----------+-----------+
|2015-04-08 13:08:15|    string|          2|
|2024-10-31 10:09:16|    string|          4|
+-------------------+----------+-----------+

```


Example 3: Extract the quarter from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.quarter('dt')).show()
+----------+----------+-----------+
|        dt|typeof(dt)|quarter(dt)|
+----------+----------+-----------+
|2015-04-08|      date|          2|
|2024-10-31|      date|          4|
+----------+----------+-----------+

```


Example 4: Extract the quarter from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.quarter('ts')).show()
+-------------------+----------+-----------+
|                 ts|typeof(ts)|quarter(ts)|
+-------------------+----------+-----------+
|2015-04-08 13:08:15| timestamp|          2|
|2024-10-31 10:09:16| timestamp|          4|
+-------------------+----------+-----------+

```



# pyspark.sql.functions.second — PySpark 4.0.1 documentation
pyspark.sql.functions.second(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#second)
[#](#pyspark.sql.functions.second "Permalink to this definition")

Extract the seconds of a given date as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

seconds part of the timestamp as integer.

Examples

Example 1: Extract the seconds from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.second('ts')).show()
+-------------------+----------+----------+
|                 ts|typeof(ts)|second(ts)|
+-------------------+----------+----------+
|2015-04-08 13:08:15|    string|        15|
|2024-10-31 10:09:16|    string|        16|
+-------------------+----------+----------+

```


Example 2: Extract the seconds from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.second('ts')).show()
+-------------------+----------+----------+
|                 ts|typeof(ts)|second(ts)|
+-------------------+----------+----------+
|2015-04-08 13:08:15| timestamp|        15|
|2024-10-31 10:09:16| timestamp|        16|
+-------------------+----------+----------+

```



# pyspark.sql.functions.session_window — PySpark 4.0.1 documentation
pyspark.sql.functions.session\_window(_timeColumn_, _gapDuration_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#session_window)
[#](#pyspark.sql.functions.session_window "Permalink to this definition")

Generates session window given a timestamp specifying column. Session window is one of dynamic windows, which means the length of window is varying according to the given inputs. The length of session window is defined as “the timestamp of latest input of the session + gap duration”, so when the new inputs are bound to the current session window, the end time of session window can be expanded according to the new inputs. Windows can support microsecond precision. Windows in the order of months are not supported. For a streaming query, you may use the function current\_timestamp to generate windows on processing time. gapDuration is provided as strings, e.g. ‘1 second’, ‘1 day 12 hours’, ‘2 minutes’. Valid interval strings are ‘week’, ‘day’, ‘hour’, ‘minute’, ‘second’, ‘millisecond’, ‘microsecond’. It could also be a Column which can be evaluated to gap duration dynamically based on the input row. The output column will be a struct called ‘session\_window’ by default with the nested columns ‘start’ and ‘end’, where ‘start’ and ‘end’ will be of [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType").

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**timeColumn**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The column name or column to use as the timestamp for windowing by time. The time column must be of TimestampType or TimestampNTZType.

**gapDuration**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

A Python string literal or column specifying the timeout of the session. It could be static value, e.g. 10 minutes, 1 second, or an expression/UDF that specifies gap duration dynamically based on the input row.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2016-03-11 09:00:07', 1)], ['dt', 'v'])
>>> df2 = df.groupBy(sf.session_window('dt', '5 seconds')).agg(sf.sum('v'))
>>> df2.show(truncate=False)
+------------------------------------------+------+
|session_window                            |sum(v)|
+------------------------------------------+------+
|{2016-03-11 09:00:07, 2016-03-11 09:00:12}|1     |
+------------------------------------------+------+

```


```
>>> df2.printSchema()
root
 |-- session_window: struct (nullable = false)
 |    |-- start: timestamp (nullable = true)
 |    |-- end: timestamp (nullable = true)
 |-- sum(v): long (nullable = true)

```


# pyspark.sql.functions.timestamp_add — PySpark 4.0.1 documentation
pyspark.sql.functions.timestamp\_add(_unit_, _quantity_, _ts_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#timestamp_add)
[#](#pyspark.sql.functions.timestamp_add "Permalink to this definition")

Gets the difference between the timestamps in the specified units by truncating the fraction part.

New in version 4.0.0.

Parameters

**unit**literal string

This indicates the units of the difference between the given timestamps. Supported options are (case insensitive): “YEAR”, “QUARTER”, “MONTH”, “WEEK”, “DAY”, “HOUR”, “MINUTE”, “SECOND”, “MILLISECOND” and “MICROSECOND”.

**quantity**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The number of units of time that you want to add.

**ts**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A timestamp to which you want to add.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the difference between the timestamps.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(datetime.datetime(2016, 3, 11, 9, 0, 7), 2),
...      (datetime.datetime(2024, 4, 2, 9, 0, 7), 3)], ['ts', 'quantity'])
>>> df.select('*', sf.timestamp_add('year', 'quantity', 'ts')).show()
+-------------------+--------+--------------------------------+
|                 ts|quantity|timestampadd(year, quantity, ts)|
+-------------------+--------+--------------------------------+
|2016-03-11 09:00:07|       2|             2018-03-11 09:00:07|
|2024-04-02 09:00:07|       3|             2027-04-02 09:00:07|
+-------------------+--------+--------------------------------+

```


```
>>> df.select('*', sf.timestamp_add('WEEK', sf.lit(5), df.ts)).show()
+-------------------+--------+-------------------------+
|                 ts|quantity|timestampadd(WEEK, 5, ts)|
+-------------------+--------+-------------------------+
|2016-03-11 09:00:07|       2|      2016-04-15 09:00:07|
|2024-04-02 09:00:07|       3|      2024-05-07 09:00:07|
+-------------------+--------+-------------------------+

```


```
>>> df.select('*', sf.timestamp_add('day', sf.lit(-5), 'ts')).show()
+-------------------+--------+-------------------------+
|                 ts|quantity|timestampadd(day, -5, ts)|
+-------------------+--------+-------------------------+
|2016-03-11 09:00:07|       2|      2016-03-06 09:00:07|
|2024-04-02 09:00:07|       3|      2024-03-28 09:00:07|
+-------------------+--------+-------------------------+

```


# pyspark.sql.functions.timestamp_diff — PySpark 4.0.1 documentation
pyspark.sql.functions.timestamp\_diff(_unit_, _start_, _end_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#timestamp_diff)
[#](#pyspark.sql.functions.timestamp_diff "Permalink to this definition")

Gets the difference between the timestamps in the specified units by truncating the fraction part.

New in version 4.0.0.

Parameters

**unit**literal string

This indicates the units of the difference between the given timestamps. Supported options are (case insensitive): “YEAR”, “QUARTER”, “MONTH”, “WEEK”, “DAY”, “HOUR”, “MINUTE”, “SECOND”, “MILLISECOND” and “MICROSECOND”.

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A timestamp which the expression subtracts from endTimestamp.

**end**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

A timestamp from which the expression subtracts startTimestamp.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the difference between the timestamps.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(datetime.datetime(2016, 3, 11, 9, 0, 7), datetime.datetime(2024, 4, 2, 9, 0, 7))],
...     ['ts1', 'ts2'])
>>> df.select('*', sf.timestamp_diff('year', 'ts1', 'ts2')).show()
+-------------------+-------------------+-----------------------------+
|                ts1|                ts2|timestampdiff(year, ts1, ts2)|
+-------------------+-------------------+-----------------------------+
|2016-03-11 09:00:07|2024-04-02 09:00:07|                            8|
+-------------------+-------------------+-----------------------------+

```


```
>>> df.select('*', sf.timestamp_diff('WEEK', 'ts1', 'ts2')).show()
+-------------------+-------------------+-----------------------------+
|                ts1|                ts2|timestampdiff(WEEK, ts1, ts2)|
+-------------------+-------------------+-----------------------------+
|2016-03-11 09:00:07|2024-04-02 09:00:07|                          420|
+-------------------+-------------------+-----------------------------+

```


```
>>> df.select('*', sf.timestamp_diff('day', df.ts2, df.ts1)).show()
+-------------------+-------------------+----------------------------+
|                ts1|                ts2|timestampdiff(day, ts2, ts1)|
+-------------------+-------------------+----------------------------+
|2016-03-11 09:00:07|2024-04-02 09:00:07|                       -2944|
+-------------------+-------------------+----------------------------+

```

# pyspark.sql.functions.timestamp_micros — PySpark 4.0.1 documentation
pyspark.sql.functions.timestamp\_micros(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#timestamp_micros)
[#](#pyspark.sql.functions.timestamp_micros "Permalink to this definition")

Creates timestamp from the number of microseconds since UTC epoch.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

unix time values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

converted timestamp value.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "UTC")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1230219000,), (1280219000,)], ['micros'])
>>> df.select('*', sf.timestamp_micros('micros')).show(truncate=False)
+----------+------------------------+
|micros    |timestamp_micros(micros)|
+----------+------------------------+
|1230219000|1970-01-01 00:20:30.219 |
|1280219000|1970-01-01 00:21:20.219 |
+----------+------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```

# pyspark.sql.functions.timestamp_millis — PySpark 4.0.1 documentation
pyspark.sql.functions.timestamp\_millis(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#timestamp_millis)
[#](#pyspark.sql.functions.timestamp_millis "Permalink to this definition")

Creates timestamp from the number of milliseconds since UTC epoch.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

unix time values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

converted timestamp value.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "UTC")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1230219000,), (1280219000,)], ['millis'])
>>> df.select('*', sf.timestamp_millis('millis')).show()
+----------+------------------------+
|    millis|timestamp_millis(millis)|
+----------+------------------------+
|1230219000|     1970-01-15 05:43:39|
|1280219000|     1970-01-15 19:36:59|
+----------+------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```

# pyspark.sql.functions.timestamp_seconds — PySpark 4.0.1 documentation
pyspark.sql.functions.timestamp\_seconds(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#timestamp_seconds)
[#](#pyspark.sql.functions.timestamp_seconds "Permalink to this definition")

Converts the number of seconds from the Unix epoch (1970-01-01T00:00:00Z) to a timestamp.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

unix time values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

converted timestamp value.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "UTC")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1230219000,), (1280219000,)], ['seconds'])
>>> df.select('*', sf.timestamp_seconds('seconds')).show()
+----------+--------------------------+
|   seconds|timestamp_seconds(seconds)|
+----------+--------------------------+
|1230219000|       2008-12-25 15:30:00|
|1280219000|       2010-07-27 08:23:20|
+----------+--------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.to_date — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_date(_col_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_date)
[#](#pyspark.sql.functions.to_date "Permalink to this definition")

Converts a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") into [`pyspark.sql.types.DateType`](about:blank/pyspark.sql.types.DateType.html#pyspark.sql.types.DateType "pyspark.sql.types.DateType") using the optionally specified format. Specify formats according to [datetime pattern](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html). By default, it follows casting rules to [`pyspark.sql.types.DateType`](about:blank/pyspark.sql.types.DateType.html#pyspark.sql.types.DateType "pyspark.sql.types.DateType") if the format is omitted. Equivalent to `col.cast("date")`.

New in version 2.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to convert.

**format: literal string, optional**

format to use to convert date values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

date value as [`pyspark.sql.types.DateType`](about:blank/pyspark.sql.types.DateType.html#pyspark.sql.types.DateType "pyspark.sql.types.DateType") type.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['ts'])
>>> df.select('*', sf.to_date(df.ts)).show()
+-------------------+-----------+
|                 ts|to_date(ts)|
+-------------------+-----------+
|1997-02-28 10:30:00| 1997-02-28|
+-------------------+-----------+

```


```
>>> df.select('*', sf.to_date('ts', 'yyyy-MM-dd HH:mm:ss')).show()
+-------------------+--------------------------------+
|                 ts|to_date(ts, yyyy-MM-dd HH:mm:ss)|
+-------------------+--------------------------------+
|1997-02-28 10:30:00|                      1997-02-28|
+-------------------+--------------------------------+

```


# pyspark.sql.functions.to_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_timestamp(_col_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_timestamp)
[#](#pyspark.sql.functions.to_timestamp "Permalink to this definition")

Converts a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") into [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType") using the optionally specified format. Specify formats according to [datetime pattern](https://spark.apache.org/docs/latest/sql-ref-datetime-pattern.html). By default, it follows casting rules to [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType") if the format is omitted. Equivalent to `col.cast("timestamp")`.

New in version 2.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column values to convert.

**format: literal string, optional**

format to use to convert timestamp values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

timestamp value as [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType") type.

Examples

Example 1: Convert string to a timestamp

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['t'])
>>> df.select(sf.to_timestamp(df.t)).show()
+-------------------+
|    to_timestamp(t)|
+-------------------+
|1997-02-28 10:30:00|
+-------------------+

```


Example 2: Convert string to a timestamp with a format

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['t'])
>>> df.select(sf.to_timestamp(df.t, 'yyyy-MM-dd HH:mm:ss')).show()
+------------------------------------+
|to_timestamp(t, yyyy-MM-dd HH:mm:ss)|
+------------------------------------+
|                 1997-02-28 10:30:00|
+------------------------------------+

```

# pyspark.sql.functions.to_timestamp_ltz — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_timestamp\_ltz(_timestamp_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_timestamp_ltz)
[#](#pyspark.sql.functions.to_timestamp_ltz "Permalink to this definition")

Parses the timestamp with the format to a timestamp with time zone. Returns null with invalid input.

New in version 3.5.0.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

format to use to convert type TimestampType timestamp values.

Examples

Example 1: Using default format to parse the timestamp string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08 12:12:12',)], ['ts'])
>>> df.select('*', sf.to_timestamp_ltz('ts')).show()
+-------------------+--------------------+
|                 ts|to_timestamp_ltz(ts)|
+-------------------+--------------------+
|2015-04-08 12:12:12| 2015-04-08 12:12:12|
+-------------------+--------------------+

```


Example 2: Using user-specified format to parse the date string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2016-12-31',)], ['dt'])
>>> df.select('*', sf.to_timestamp_ltz(df.dt, sf.lit('yyyy-MM-dd'))).show()
+----------+--------------------------------+
|        dt|to_timestamp_ltz(dt, yyyy-MM-dd)|
+----------+--------------------------------+
|2016-12-31|             2016-12-31 00:00:00|
+----------+--------------------------------+

```


Example 3: Using a format column to represent different formats.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [('2015-04-08', 'yyyy-MM-dd'), ('2025+01+09', 'yyyy+MM+dd')], ['dt', 'fmt'])
>>> df.select('*', sf.to_timestamp_ltz('dt', 'fmt')).show()
+----------+----------+-------------------------+
|        dt|       fmt|to_timestamp_ltz(dt, fmt)|
+----------+----------+-------------------------+
|2015-04-08|yyyy-MM-dd|      2015-04-08 00:00:00|
|2025+01+09|yyyy+MM+dd|      2025-01-09 00:00:00|
+----------+----------+-------------------------+

```



# pyspark.sql.functions.to_timestamp_ntz — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_timestamp\_ntz(_timestamp_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_timestamp_ntz)
[#](#pyspark.sql.functions.to_timestamp_ntz "Permalink to this definition")

Parses the timestamp with the format to a timestamp without time zone. Returns null with invalid input.

New in version 3.5.0.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

format to use to convert type TimestampNTZType timestamp values.

Examples

Example 1: Using default format to parse the timestamp string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08 12:12:12',)], ['ts'])
>>> df.select('*', sf.to_timestamp_ntz('ts')).show()
+-------------------+--------------------+
|                 ts|to_timestamp_ntz(ts)|
+-------------------+--------------------+
|2015-04-08 12:12:12| 2015-04-08 12:12:12|
+-------------------+--------------------+

```


Example 2: Using user-specified format ‘yyyy-MM-dd’ to parse the date string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2016-12-31',)], ['dt'])
>>> df.select('*', sf.to_timestamp_ntz(df.dt, sf.lit('yyyy-MM-dd'))).show()
+----------+--------------------------------+
|        dt|to_timestamp_ntz(dt, yyyy-MM-dd)|
+----------+--------------------------------+
|2016-12-31|             2016-12-31 00:00:00|
+----------+--------------------------------+

```


Example 3: Using a format column to represent different formats.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [('2015-04-08', 'yyyy-MM-dd'), ('2025+01+09', 'yyyy+MM+dd')], ['dt', 'fmt'])
>>> df.select('*', sf.to_timestamp_ntz('dt', 'fmt')).show()
+----------+----------+-------------------------+
|        dt|       fmt|to_timestamp_ntz(dt, fmt)|
+----------+----------+-------------------------+
|2015-04-08|yyyy-MM-dd|      2015-04-08 00:00:00|
|2025+01+09|yyyy+MM+dd|      2025-01-09 00:00:00|
+----------+----------+-------------------------+

```


# pyspark.sql.functions.to_unix_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_unix\_timestamp(_timestamp_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_unix_timestamp)
[#](#pyspark.sql.functions.to_unix_timestamp "Permalink to this definition")

Returns the UNIX timestamp of the given time.

New in version 3.5.0.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Input column or strings.

**format**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

format to use to convert UNIX timestamp values.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Using default format to parse the timestamp string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08 12:12:12',)], ['ts'])
>>> df.select('*', sf.to_unix_timestamp('ts')).show()
+-------------------+------------------------------------------+
|                 ts|to_unix_timestamp(ts, yyyy-MM-dd HH:mm:ss)|
+-------------------+------------------------------------------+
|2015-04-08 12:12:12|                                1428520332|
+-------------------+------------------------------------------+

```


Example 2: Using user-specified format ‘yyyy-MM-dd’ to parse the date string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08',)], ['dt'])
>>> df.select('*', sf.to_unix_timestamp(df.dt, sf.lit('yyyy-MM-dd'))).show()
+----------+---------------------------------+
|        dt|to_unix_timestamp(dt, yyyy-MM-dd)|
+----------+---------------------------------+
|2015-04-08|                       1428476400|
+----------+---------------------------------+

```


Example 3: Using a format column to represent different formats.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [('2015-04-08', 'yyyy-MM-dd'), ('2025+01+09', 'yyyy+MM+dd')], ['dt', 'fmt'])
>>> df.select('*', sf.to_unix_timestamp('dt', 'fmt')).show()
+----------+----------+--------------------------+
|        dt|       fmt|to_unix_timestamp(dt, fmt)|
+----------+----------+--------------------------+
|2015-04-08|yyyy-MM-dd|                1428476400|
|2025+01+09|yyyy+MM+dd|                1736409600|
+----------+----------+--------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```

# pyspark.sql.functions.to_utc_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_utc\_timestamp(_timestamp_, _tz_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_utc_timestamp)
[#](#pyspark.sql.functions.to_utc_timestamp "Permalink to this definition")

This is a common function for databases supporting TIMESTAMP WITHOUT TIMEZONE. This function takes a timestamp which is timezone-agnostic, and interprets it as a timestamp in the given timezone, and renders that timestamp as a timestamp in UTC.

However, timestamp in Spark represents number of microseconds from the Unix epoch, which is not timezone-agnostic. So in Spark this function just shift the timestamp value from the given timezone to UTC timezone.

This function may return confusing result if the input is a string with timezone, e.g. ‘2018-03-13T06:18:23+00:00’. The reason is that, Spark firstly cast the string to timestamp according to the timezone in the string, and finally display the result by converting the timestamp to string according to the session local timezone.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the column that contains timestamps

**tz**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

A string detailing the time zone ID that the input should be adjusted to. It should be in the format of either region-based zone IDs or zone offsets. Region IDs must have the form ‘area/city’, such as ‘America/Los\_Angeles’. Zone offsets must be in the format ‘(+|-)HH:mm’, for example ‘-08:00’ or ‘+01:00’. Also ‘UTC’ and ‘Z’ are supported as aliases of ‘+00:00’. Other short names are not recommended to use because they can be ambiguous.

Changed in version 2.4.0: tz can take a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") containing timezone ID strings.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

timestamp value represented in UTC timezone.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00', 'JST')], ['ts', 'tz'])
>>> df.select('*', sf.to_utc_timestamp('ts', "PST")).show()
+-------------------+---+-------------------------+
|                 ts| tz|to_utc_timestamp(ts, PST)|
+-------------------+---+-------------------------+
|1997-02-28 10:30:00|JST|      1997-02-28 18:30:00|
+-------------------+---+-------------------------+

```


```
>>> df.select('*', sf.to_utc_timestamp(df.ts, df.tz)).show()
+-------------------+---+------------------------+
|                 ts| tz|to_utc_timestamp(ts, tz)|
+-------------------+---+------------------------+
|1997-02-28 10:30:00|JST|     1997-02-28 01:30:00|
+-------------------+---+------------------------+

```



# pyspark.sql.functions.trunc — PySpark 4.0.1 documentation
pyspark.sql.functions.trunc(_date_, _format_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#trunc)
[#](#pyspark.sql.functions.trunc "Permalink to this definition")

Returns date truncated to the unit specified by the format.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**date**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to truncate.

**format**literal string

‘year’, ‘yyyy’, ‘yy’ to truncate by year, or ‘month’, ‘mon’, ‘mm’ to truncate by month Other options are: ‘week’, ‘quarter’

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

truncated date.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('1997-02-28',)], ['dt'])
>>> df.select('*', sf.trunc(df.dt, 'year')).show()
+----------+---------------+
|        dt|trunc(dt, year)|
+----------+---------------+
|1997-02-28|     1997-01-01|
+----------+---------------+

```


```
>>> df.select('*', sf.trunc('dt', 'mon')).show()
+----------+--------------+
|        dt|trunc(dt, mon)|
+----------+--------------+
|1997-02-28|    1997-02-01|
+----------+--------------+

```



# pyspark.sql.functions.try_make_interval — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_make\_interval(_years\=None_, _months\=None_, _weeks\=None_, _days\=None_, _hours\=None_, _mins\=None_, _secs\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_make_interval)
[#](#pyspark.sql.functions.try_make_interval "Permalink to this definition")

This is a special version of make\_interval that performs the same operation, but returns a NULL value instead of raising an error if interval cannot be created.

New in version 4.0.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of years, positive or negative.

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of months, positive or negative.

**weeks**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of weeks, positive or negative.

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of days, positive or negative.

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of hours, positive or negative.

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of minutes, positive or negative.

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The number of seconds with the fractional part in microsecond precision.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains an interval.

Examples

Example 1: Try make interval from years, months, weeks, days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.try_make_interval(df.year, df.month, 'week', df.day, 'hour', df.min, df.sec)
... ).show(truncate=False)
+---------------------------------------------------------------+
|try_make_interval(year, month, week, day, hour, min, sec)      |
+---------------------------------------------------------------+
|100 years 11 months 8 days 12 hours 30 minutes 1.001001 seconds|
+---------------------------------------------------------------+

```


Example 2: Try make interval from years, months, weeks, days, hours and mins.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.try_make_interval(df.year, df.month, 'week', df.day, df.hour, df.min)
... ).show(truncate=False)
+-------------------------------------------------------+
|try_make_interval(year, month, week, day, hour, min, 0)|
+-------------------------------------------------------+
|100 years 11 months 8 days 12 hours 30 minutes         |
+-------------------------------------------------------+

```


Example 3: Try make interval from years, months, weeks, days and hours.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.try_make_interval(df.year, df.month, 'week', df.day, df.hour)
... ).show(truncate=False)
+-----------------------------------------------------+
|try_make_interval(year, month, week, day, hour, 0, 0)|
+-----------------------------------------------------+
|100 years 11 months 8 days 12 hours                  |
+-----------------------------------------------------+

```


Example 4: Try make interval from years, months, weeks and days.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.try_make_interval(df.year, 'month', df.week, df.day)).show(truncate=False)
+--------------------------------------------------+
|try_make_interval(year, month, week, day, 0, 0, 0)|
+--------------------------------------------------+
|100 years 11 months 8 days                        |
+--------------------------------------------------+

```


Example 5: Try make interval from years, months and weeks.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.try_make_interval(df.year, 'month', df.week)).show(truncate=False)
+------------------------------------------------+
|try_make_interval(year, month, week, 0, 0, 0, 0)|
+------------------------------------------------+
|100 years 11 months 7 days                      |
+------------------------------------------------+

```


Example 6: Try make interval from years and months.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.try_make_interval(df.year, 'month')).show(truncate=False)
+---------------------------------------------+
|try_make_interval(year, month, 0, 0, 0, 0, 0)|
+---------------------------------------------+
|100 years 11 months                          |
+---------------------------------------------+

```


Example 7: Try make interval from years.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[100, 11, 1, 1, 12, 30, 01.001001]],
...     ['year', 'month', 'week', 'day', 'hour', 'min', 'sec'])
>>> df.select(sf.try_make_interval(df.year)).show(truncate=False)
+-----------------------------------------+
|try_make_interval(year, 0, 0, 0, 0, 0, 0)|
+-----------------------------------------+
|100 years                                |
+-----------------------------------------+

```


Example 8: Try make empty interval.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.try_make_interval()).show(truncate=False)
+--------------------------------------+
|try_make_interval(0, 0, 0, 0, 0, 0, 0)|
+--------------------------------------+
|0 seconds                             |
+--------------------------------------+

```


Example 9: Try make interval from years with overflow.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.try_make_interval(sf.lit(2147483647))).show(truncate=False)
+-----------------------------------------------+
|try_make_interval(2147483647, 0, 0, 0, 0, 0, 0)|
+-----------------------------------------------+
|NULL                                           |
+-----------------------------------------------+

```


# pyspark.sql.functions.try_make_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_make\_timestamp(_years_, _months_, _days_, _hours_, _mins_, _secs_, _timezone\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_make_timestamp)
[#](#pyspark.sql.functions.try_make_timestamp "Permalink to this definition")

Try to create timestamp from years, months, days, hours, mins, secs and timezone fields. The result data type is consistent with the value of configuration spark.sql.timestampType. The function returns NULL on invalid inputs.

New in version 4.0.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The year to represent, from 1 to 9999

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The month-of-year to represent, from 1 (January) to 12 (December)

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The day-of-month to represent, from 1 to 31

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The hour-of-day to represent, from 0 to 23

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The minute-of-hour to represent, from 0 to 59

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The second-of-minute and its micro-fraction to represent, from 0 to 60. The value can be either an integer like 13 , or a fraction like 13.123. If the sec argument equals to 60, the seconds field is set to 0 and 1 minute is added to the final timestamp.

**timezone**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The time zone identifier. For example, CET, UTC and etc.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a timestamp or NULL in case of an error.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Make timestamp from years, months, days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.try_make_timestamp(df.year, df.month, df.day, 'hour', df.min, df.sec, 'tz')
... ).show(truncate=False)
+----------------------------------------------------+
|try_make_timestamp(year, month, day, hour, min, sec)|
+----------------------------------------------------+
|2014-12-27 21:30:45.887                             |
+----------------------------------------------------+

```


Example 2: Make timestamp without timezone.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.try_make_timestamp(df.year, df.month, df.day, 'hour', df.min, df.sec)
... ).show(truncate=False)
+----------------------------------------------------+
|try_make_timestamp(year, month, day, hour, min, sec)|
+----------------------------------------------------+
|2014-12-28 06:30:45.887                             |
+----------------------------------------------------+
>>> spark.conf.unset("spark.sql.session.timeZone")

```


Example 3: Make timestamp with invalid input.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 13, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.try_make_timestamp(df.year, df.month, df.day, 'hour', df.min, df.sec)
... ).show(truncate=False)
+----------------------------------------------------+
|try_make_timestamp(year, month, day, hour, min, sec)|
+----------------------------------------------------+
|NULL                                                |
+----------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```



# pyspark.sql.functions.try_make_timestamp_ltz — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_make\_timestamp\_ltz(_years_, _months_, _days_, _hours_, _mins_, _secs_, _timezone\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_make_timestamp_ltz)
[#](#pyspark.sql.functions.try_make_timestamp_ltz "Permalink to this definition")

Try to create the current timestamp with local time zone from years, months, days, hours, mins, secs and timezone fields. The function returns NULL on invalid inputs.

New in version 4.0.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The year to represent, from 1 to 9999

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The month-of-year to represent, from 1 (January) to 12 (December)

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The day-of-month to represent, from 1 to 31

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The hour-of-day to represent, from 0 to 23

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The minute-of-hour to represent, from 0 to 59

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The second-of-minute and its micro-fraction to represent, from 0 to 60. The value can be either an integer like 13 , or a fraction like 13.123. If the sec argument equals to 60, the seconds field is set to 0 and 1 minute is added to the final timestamp.

**timezone**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

The time zone identifier. For example, CET, UTC and etc.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a current timestamp, or NULL in case of an error.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Make the current timestamp from years, months, days, hours, mins and secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.try_make_timestamp_ltz('year', 'month', df.day, df.hour, df.min, df.sec, 'tz')
... ).show(truncate=False)
+------------------------------------------------------------+
|try_make_timestamp_ltz(year, month, day, hour, min, sec, tz)|
+------------------------------------------------------------+
|2014-12-27 21:30:45.887                                     |
+------------------------------------------------------------+

```


Example 2: Make the current timestamp without timezone.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.try_make_timestamp_ltz('year', 'month', df.day, df.hour, df.min, df.sec)
... ).show(truncate=False)
+--------------------------------------------------------+
|try_make_timestamp_ltz(year, month, day, hour, min, sec)|
+--------------------------------------------------------+
|2014-12-28 06:30:45.887                                 |
+--------------------------------------------------------+

```


Example 3: Make the current timestamp with invalid input.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 13, 28, 6, 30, 45.887, 'CET']],
...     ['year', 'month', 'day', 'hour', 'min', 'sec', 'tz'])
>>> df.select(
...     sf.try_make_timestamp_ltz('year', 'month', df.day, df.hour, df.min, df.sec)
... ).show(truncate=False)
+--------------------------------------------------------+
|try_make_timestamp_ltz(year, month, day, hour, min, sec)|
+--------------------------------------------------------+
|NULL                                                    |
+--------------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```



# pyspark.sql.functions.try_make_timestamp_ntz — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_make\_timestamp\_ntz(_years_, _months_, _days_, _hours_, _mins_, _secs_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_make_timestamp_ntz)
[#](#pyspark.sql.functions.try_make_timestamp_ntz "Permalink to this definition")

Try to create local date-time from years, months, days, hours, mins, secs fields. The function returns NULL on invalid inputs.

New in version 4.0.0.

Parameters

**years**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The year to represent, from 1 to 9999

**months**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The month-of-year to represent, from 1 (January) to 12 (December)

**days**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The day-of-month to represent, from 1 to 31

**hours**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The hour-of-day to represent, from 0 to 23

**mins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The minute-of-hour to represent, from 0 to 59

**secs**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The second-of-minute and its micro-fraction to represent, from 0 to 60. The value can be either an integer like 13 , or a fraction like 13.123. If the sec argument equals to 60, the seconds field is set to 0 and 1 minute is added to the final timestamp.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a local date-time, or NULL in case of an error.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Make local date-time from years, months, days, hours, mins, secs.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 12, 28, 6, 30, 45.887]],
...     ['year', 'month', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.try_make_timestamp_ntz('year', 'month', df.day, df.hour, df.min, df.sec)
... ).show(truncate=False)
+--------------------------------------------------------+
|try_make_timestamp_ntz(year, month, day, hour, min, sec)|
+--------------------------------------------------------+
|2014-12-28 06:30:45.887                                 |
+--------------------------------------------------------+

```


Example 2: Make local date-time with invalid input

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[2014, 13, 28, 6, 30, 45.887]],
...     ['year', 'month', 'day', 'hour', 'min', 'sec'])
>>> df.select(
...     sf.try_make_timestamp_ntz('year', 'month', df.day, df.hour, df.min, df.sec)
... ).show(truncate=False)
+--------------------------------------------------------+
|try_make_timestamp_ntz(year, month, day, hour, min, sec)|
+--------------------------------------------------------+
|NULL                                                    |
+--------------------------------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```



# pyspark.sql.functions.try_to_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_to\_timestamp(_col_, _format\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_to_timestamp)
[#](#pyspark.sql.functions.try_to_timestamp "Permalink to this definition")

Parses the col with the format to a timestamp. The function always returns null on an invalid input with/without ANSI SQL mode enabled. The result data type is consistent with the value of configuration spark.sql.timestampType.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column values to convert.

**format: literal string, optional**

format to use to convert timestamp values.

Examples

Example 1: Convert string to a timestamp

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['t'])
>>> df.select(sf.try_to_timestamp(df.t).alias('dt')).show()
+-------------------+
|                 dt|
+-------------------+
|1997-02-28 10:30:00|
+-------------------+

```


Example 2: Convert string to a timestamp with a format

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1997-02-28 10:30:00',)], ['t'])
>>> df.select(sf.try_to_timestamp(df.t, sf.lit('yyyy-MM-dd HH:mm:ss')).alias('dt')).show()
+-------------------+
|                 dt|
+-------------------+
|1997-02-28 10:30:00|
+-------------------+

```


Example 3: Converion failure results in NULL when ANSI mode is on

```
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     df = spark.createDataFrame([('malformed',)], ['t'])
...     df.select(sf.try_to_timestamp(df.t)).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+-------------------+
|try_to_timestamp(t)|
+-------------------+
|               NULL|
+-------------------+

```


# pyspark.sql.functions.unix_date — PySpark 4.0.1 documentation
pyspark.sql.functions.unix\_date(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unix_date)
[#](#pyspark.sql.functions.unix_date "Permalink to this definition")

Returns the number of days since 1970-01-01.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to convert.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of days since 1970-01-01.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('1970-01-02',), ('2022-01-02',)], ['dt'])
>>> df.select('*', sf.unix_date(sf.to_date('dt'))).show()
+----------+----------------------+
|        dt|unix_date(to_date(dt))|
+----------+----------------------+
|1970-01-02|                     1|
|2022-01-02|                 18994|
+----------+----------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.unix_micros — PySpark 4.0.1 documentation
pyspark.sql.functions.unix\_micros(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unix_micros)
[#](#pyspark.sql.functions.unix_micros "Permalink to this definition")

Returns the number of microseconds since 1970-01-01 00:00:00 UTC.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to convert.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of microseconds since 1970-01-01 00:00:00 UTC.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-07-22 10:00:00',), ('2022-10-09 11:12:13',)], ['ts'])
>>> df.select('*', sf.unix_micros(sf.to_timestamp('ts'))).show()
+-------------------+-----------------------------+
|                 ts|unix_micros(to_timestamp(ts))|
+-------------------+-----------------------------+
|2015-07-22 10:00:00|             1437584400000000|
|2022-10-09 11:12:13|             1665339133000000|
+-------------------+-----------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.unix_millis — PySpark 4.0.1 documentation
pyspark.sql.functions.unix\_millis(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unix_millis)
[#](#pyspark.sql.functions.unix_millis "Permalink to this definition")

Returns the number of milliseconds since 1970-01-01 00:00:00 UTC. Truncates higher levels of precision.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to convert.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of milliseconds since 1970-01-01 00:00:00 UTC.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-07-22 10:00:00',), ('2022-10-09 11:12:13',)], ['ts'])
>>> df.select('*', sf.unix_millis(sf.to_timestamp('ts'))).show()
+-------------------+-----------------------------+
|                 ts|unix_millis(to_timestamp(ts))|
+-------------------+-----------------------------+
|2015-07-22 10:00:00|                1437584400000|
|2022-10-09 11:12:13|                1665339133000|
+-------------------+-----------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```



# pyspark.sql.functions.unix_seconds — PySpark 4.0.1 documentation
pyspark.sql.functions.unix\_seconds(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unix_seconds)
[#](#pyspark.sql.functions.unix_seconds "Permalink to this definition")

Returns the number of seconds since 1970-01-01 00:00:00 UTC. Truncates higher levels of precision.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to convert.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of seconds since 1970-01-01 00:00:00 UTC.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-07-22 10:00:00',), ('2022-10-09 11:12:13',)], ['ts'])
>>> df.select('*', sf.unix_seconds(sf.to_timestamp('ts'))).show()
+-------------------+------------------------------+
|                 ts|unix_seconds(to_timestamp(ts))|
+-------------------+------------------------------+
|2015-07-22 10:00:00|                    1437584400|
|2022-10-09 11:12:13|                    1665339133|
+-------------------+------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.unix_timestamp — PySpark 4.0.1 documentation
pyspark.sql.functions.unix\_timestamp(_timestamp\=None_, _format\='yyyy-MM-dd HH:mm:ss'_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unix_timestamp)
[#](#pyspark.sql.functions.unix_timestamp "Permalink to this definition")

Convert time string with given pattern (‘yyyy-MM-dd HH:mm:ss’, by default) to Unix time stamp (in seconds), using the default timezone and the default locale, returns null if failed.

if timestamp is None, then it returns current timestamp.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**timestamp**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

timestamps of string values.

**format**literal string, optional

alternative format to use for converting (default: yyyy-MM-dd HH:mm:ss).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

unix time as long integer.

Examples

```
>>> spark.conf.set("spark.sql.session.timeZone", "America/Los_Angeles")

```


Example 1: Returns the current timestamp in UNIX.

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.unix_timestamp()).show() 
+----------+
| unix_time|
+----------+
|1702018137|
+----------+

```


Example 2: Using default format ‘yyyy-MM-dd HH:mm:ss’ parses the timestamp string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08 12:12:12',)], ['ts'])
>>> df.select('*', sf.unix_timestamp('ts')).show()
+-------------------+---------------------------------------+
|                 ts|unix_timestamp(ts, yyyy-MM-dd HH:mm:ss)|
+-------------------+---------------------------------------+
|2015-04-08 12:12:12|                             1428520332|
+-------------------+---------------------------------------+

```


Example 3: Using user-specified format ‘yyyy-MM-dd’ parses the timestamp string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('2015-04-08',)], ['dt'])
>>> df.select('*', sf.unix_timestamp('dt', 'yyyy-MM-dd')).show()
+----------+------------------------------+
|        dt|unix_timestamp(dt, yyyy-MM-dd)|
+----------+------------------------------+
|2015-04-08|                    1428476400|
+----------+------------------------------+

```


```
>>> spark.conf.unset("spark.sql.session.timeZone")

```


# pyspark.sql.functions.weekday — PySpark 4.0.1 documentation
pyspark.sql.functions.weekday(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#weekday)
[#](#pyspark.sql.functions.weekday "Permalink to this definition")

Returns the day of the week for date/timestamp (0 = Monday, 1 = Tuesday, …, 6 = Sunday).

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the day of the week for date/timestamp (0 = Monday, 1 = Tuesday, …, 6 = Sunday).

Examples

Example 1: Extract the day of the week from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.weekday('dt')).show()
+----------+----------+-----------+
|        dt|typeof(dt)|weekday(dt)|
+----------+----------+-----------+
|2015-04-08|    string|          2|
|2024-10-31|    string|          3|
+----------+----------+-----------+

```


Example 2: Extract the day of the week from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.weekday('ts')).show()
+-------------------+----------+-----------+
|                 ts|typeof(ts)|weekday(ts)|
+-------------------+----------+-----------+
|2015-04-08 13:08:15|    string|          2|
|2024-10-31 10:09:16|    string|          3|
+-------------------+----------+-----------+

```


Example 3: Extract the day of the week from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.weekday('dt')).show()
+----------+----------+-----------+
|        dt|typeof(dt)|weekday(dt)|
+----------+----------+-----------+
|2015-04-08|      date|          2|
|2024-10-31|      date|          3|
+----------+----------+-----------+

```


Example 4: Extract the day of the week from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.weekday('ts')).show()
+-------------------+----------+-----------+
|                 ts|typeof(ts)|weekday(ts)|
+-------------------+----------+-----------+
|2015-04-08 13:08:15| timestamp|          2|
|2024-10-31 10:09:16| timestamp|          3|
+-------------------+----------+-----------+

```


# pyspark.sql.functions.weekofyear — PySpark 4.0.1 documentation
pyspark.sql.functions.weekofyear(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#weekofyear)
[#](#pyspark.sql.functions.weekofyear "Permalink to this definition")

Extract the week number of a given date as integer. A week is considered to start on a Monday and week 1 is the first week with more than 3 days, as defined by ISO 8601

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

week of the year for given date as integer.

Examples

Example 1: Extract the week of the year from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.weekofyear('dt')).show()
+----------+----------+--------------+
|        dt|typeof(dt)|weekofyear(dt)|
+----------+----------+--------------+
|2015-04-08|    string|            15|
|2024-10-31|    string|            44|
+----------+----------+--------------+

```


Example 2: Extract the week of the year from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.weekofyear('ts')).show()
+-------------------+----------+--------------+
|                 ts|typeof(ts)|weekofyear(ts)|
+-------------------+----------+--------------+
|2015-04-08 13:08:15|    string|            15|
|2024-10-31 10:09:16|    string|            44|
+-------------------+----------+--------------+

```


Example 3: Extract the week of the year from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.weekofyear('dt')).show()
+----------+----------+--------------+
|        dt|typeof(dt)|weekofyear(dt)|
+----------+----------+--------------+
|2015-04-08|      date|            15|
|2024-10-31|      date|            44|
+----------+----------+--------------+

```


Example 4: Extract the week of the year from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.weekofyear('ts')).show()
+-------------------+----------+--------------+
|                 ts|typeof(ts)|weekofyear(ts)|
+-------------------+----------+--------------+
|2015-04-08 13:08:15| timestamp|            15|
|2024-10-31 10:09:16| timestamp|            44|
+-------------------+----------+--------------+

```

# pyspark.sql.functions.window — PySpark 4.0.1 documentation
pyspark.sql.functions.window(_timeColumn_, _windowDuration_, _slideDuration\=None_, _startTime\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#window)
[#](#pyspark.sql.functions.window "Permalink to this definition")

Bucketize rows into one or more time windows given a timestamp specifying column. Window starts are inclusive but the window ends are exclusive, e.g. 12:05 will be in the window \[12:05,12:10) but not in \[12:00,12:05). Windows can support microsecond precision. Windows in the order of months are not supported.

The time column must be of [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType").

Durations are provided as strings, e.g. ‘1 second’, ‘1 day 12 hours’, ‘2 minutes’. Valid interval strings are ‘week’, ‘day’, ‘hour’, ‘minute’, ‘second’, ‘millisecond’, ‘microsecond’. If the `slideDuration` is not provided, the windows will be tumbling windows.

The startTime is the offset with respect to 1970-01-01 00:00:00 UTC with which to start window intervals. For example, in order to have hourly tumbling windows that start 15 minutes past the hour, e.g. 12:15-13:15, 13:15-14:15… provide startTime as 15 minutes.

The output column will be a struct called ‘window’ by default with the nested columns ‘start’ and ‘end’, where ‘start’ and ‘end’ will be of [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType").

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**timeColumn**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The column or the expression to use as the timestamp for windowing by time. The time column must be of TimestampType or TimestampNTZType.

**windowDuration**literal string

A string specifying the width of the window, e.g. 10 minutes, 1 second. Check org.apache.spark.unsafe.types.CalendarInterval for valid duration identifiers. Note that the duration is a fixed length of time, and does not vary over time according to a calendar. For example, 1 day always means 86,400,000 milliseconds, not a calendar day.

**slideDuration**literal string, optional

A new window will be generated every slideDuration. Must be less than or equal to the windowDuration. Check org.apache.spark.unsafe.types.CalendarInterval for valid duration identifiers. This duration is likewise absolute, and does not vary according to a calendar.

**startTime**literal string, optional

The offset with respect to 1970-01-01 00:00:00 UTC with which to start window intervals. For example, in order to have hourly tumbling windows that start 15 minutes past the hour, e.g. 12:15-13:15, 13:15-14:15… provide startTime as 15 minutes.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(datetime.datetime(2016, 3, 11, 9, 0, 7), 1)], ['dt', 'v'])
>>> df2 = df.groupBy(sf.window('dt', '5 seconds')).agg(sf.sum('v'))
>>> df2.show(truncate=False)
+------------------------------------------+------+
|window                                    |sum(v)|
+------------------------------------------+------+
|{2016-03-11 09:00:05, 2016-03-11 09:00:10}|1     |
+------------------------------------------+------+

```


```
>>> df2.printSchema()
root
 |-- window: struct (nullable = false)
 |    |-- start: timestamp (nullable = true)
 |    |-- end: timestamp (nullable = true)
 |-- sum(v): long (nullable = true)

```



# pyspark.sql.functions.window_time — PySpark 4.0.1 documentation
pyspark.sql.functions.window\_time(_windowColumn_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#window_time)
[#](#pyspark.sql.functions.window_time "Permalink to this definition")

Computes the event time from a window column. The column window values are produced by window aggregating operators and are of type STRUCT<start: TIMESTAMP, end: TIMESTAMP> where start is inclusive and end is exclusive. The event time of records produced by window aggregating operators can be computed as `window_time(window)` and are `window.end - lit(1).alias("microsecond")` (as microsecond is the minimal supported event time precision). The window column must be one produced by a window aggregating operator.

New in version 3.4.0.

Parameters

**windowColumn**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The window column of a window aggregate records.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(datetime.datetime(2016, 3, 11, 9, 0, 7), 1)], ['dt', 'v'])

```


Group the data into 5 second time windows and aggregate as sum.

```
>>> df2 = df.groupBy(sf.window('dt', '5 seconds')).agg(sf.sum('v'))

```


Extract the window event time using the window\_time function.

```
>>> df2.select('*', sf.window_time('window')).show(truncate=False)
+------------------------------------------+------+--------------------------+
|window                                    |sum(v)|window_time(window)       |
+------------------------------------------+------+--------------------------+
|{2016-03-11 09:00:05, 2016-03-11 09:00:10}|1     |2016-03-11 09:00:09.999999|
+------------------------------------------+------+--------------------------+

```


# pyspark.sql.functions.year — PySpark 4.0.1 documentation
pyspark.sql.functions.year(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#year)
[#](#pyspark.sql.functions.year "Permalink to this definition")

Extract the year of a given date/timestamp as integer.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target date/timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

year part of the date/timestamp as integer.

Examples

Example 1: Extract the year from a string column representing dates

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08',), ('2024-10-31',)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.year('dt')).show()
+----------+----------+--------+
|        dt|typeof(dt)|year(dt)|
+----------+----------+--------+
|2015-04-08|    string|    2015|
|2024-10-31|    string|    2024|
+----------+----------+--------+

```


Example 2: Extract the year from a string column representing timestamp

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('2015-04-08 13:08:15',), ('2024-10-31 10:09:16',)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.year('ts')).show()
+-------------------+----------+--------+
|                 ts|typeof(ts)|year(ts)|
+-------------------+----------+--------+
|2015-04-08 13:08:15|    string|    2015|
|2024-10-31 10:09:16|    string|    2024|
+-------------------+----------+--------+

```


Example 3: Extract the year from a date column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.date(2015, 4, 8),),
...     (datetime.date(2024, 10, 31),)], ['dt'])
>>> df.select("*", sf.typeof('dt'), sf.year('dt')).show()
+----------+----------+--------+
|        dt|typeof(dt)|year(dt)|
+----------+----------+--------+
|2015-04-08|      date|    2015|
|2024-10-31|      date|    2024|
+----------+----------+--------+

```


Example 4: Extract the year from a timestamp column

```
>>> import datetime
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     (datetime.datetime(2015, 4, 8, 13, 8, 15),),
...     (datetime.datetime(2024, 10, 31, 10, 9, 16),)], ['ts'])
>>> df.select("*", sf.typeof('ts'), sf.year('ts')).show()
+-------------------+----------+--------+
|                 ts|typeof(ts)|year(ts)|
+-------------------+----------+--------+
|2015-04-08 13:08:15| timestamp|    2015|
|2024-10-31 10:09:16| timestamp|    2024|
+-------------------+----------+--------+

```

# pyspark.sql.functions.crc32 — PySpark 4.0.1 documentation
pyspark.sql.functions.crc32(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#crc32)
[#](#pyspark.sql.functions.crc32 "Permalink to this definition")

Calculates the cyclic redundancy check value (CRC32) of a binary column and returns the value as a bigint.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

New in version 1.5.0: ..

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ABC',)], ['a'])
>>> df.select('*', sf.crc32('a')).show(truncate=False)
+---+----------+
|a  |crc32(a)  |
+---+----------+
|ABC|2743272264|
+---+----------+

```

# pyspark.sql.functions.hash — PySpark 4.0.1 documentation
pyspark.sql.functions.hash(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hash)
[#](#pyspark.sql.functions.hash "Permalink to this definition")

Calculates the hash code of given columns, and returns the result as an int column.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

one or more columns to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hash value as int column.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ABC', 'DEF')], ['c1', 'c2'])
>>> df.select('*', sf.hash('c1')).show()
+---+---+----------+
| c1| c2|  hash(c1)|
+---+---+----------+
|ABC|DEF|-757602832|
+---+---+----------+

```


```
>>> df.select('*', sf.hash('c1', df.c2)).show()
+---+---+------------+
| c1| c2|hash(c1, c2)|
+---+---+------------+
|ABC|DEF|   599895104|
+---+---+------------+

```


```
>>> df.select('*', sf.hash('*')).show()
+---+---+------------+
| c1| c2|hash(c1, c2)|
+---+---+------------+
|ABC|DEF|   599895104|
+---+---+------------+

```

# pyspark.sql.functions.md5 — PySpark 4.0.1 documentation
pyspark.sql.functions.md5(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#md5)
[#](#pyspark.sql.functions.md5 "Permalink to this definition")

Calculates the MD5 digest and returns the value as a 32 character hex string.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ABC',)], ['a'])
>>> df.select('*', sf.md5('a')).show(truncate=False)
+---+--------------------------------+
|a  |md5(a)                          |
+---+--------------------------------+
|ABC|902fbdd2b1df0c4f70b4a5d23525e932|
+---+--------------------------------+

```


# pyspark.sql.functions.sha — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.sha

pyspark.sql.functions.sha(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sha)
[#](#pyspark.sql.functions.sha "Permalink to this definition")

Returns a sha1 hash value as a hex string of the col.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

See also

[`pyspark.sql.functions.sha1()`](about:blank/pyspark.sql.functions.sha1.html#pyspark.sql.functions.sha1 "pyspark.sql.functions.sha1")

[`pyspark.sql.functions.sha2()`](about:blank/pyspark.sql.functions.sha2.html#pyspark.sql.functions.sha2 "pyspark.sql.functions.sha2")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.sha(sf.lit("Spark"))).show()
+--------------------+
|          sha(Spark)|
+--------------------+
|85f5955f4b27a9a4c...|
+--------------------+

```


# pyspark.sql.functions.sha1 — PySpark 4.0.1 documentation
pyspark.sql.functions.sha1(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sha1)
[#](#pyspark.sql.functions.sha1 "Permalink to this definition")

Returns the hex string result of SHA-1.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ABC',)], ['a'])
>>> df.select('*', sf.sha1('a')).show(truncate=False)
+---+----------------------------------------+
|a  |sha1(a)                                 |
+---+----------------------------------------+
|ABC|3c01bdbb26f358bab27f267924aa2c9a03fcfdb8|
+---+----------------------------------------+

```



# pyspark.sql.functions.sha2 — PySpark 4.0.1 documentation
pyspark.sql.functions.sha2(_col_, _numBits_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sha2)
[#](#pyspark.sql.functions.sha2 "Permalink to this definition")

Returns the hex string result of SHA-2 family of hash functions (SHA-224, SHA-256, SHA-384, and SHA-512). The numBits indicates the desired bit length of the result, which must have a value of 224, 256, 384, 512, or 0 (which is equivalent to 256).

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**numBits**int

the desired bit length of the result, which must have a value of 224, 256, 384, 512, or 0 (which is equivalent to 256).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([['Alice'], ['Bob']], ['name'])
>>> df.select('*', sf.sha2('name', 256)).show(truncate=False)
+-----+----------------------------------------------------------------+
|name |sha2(name, 256)                                                 |
+-----+----------------------------------------------------------------+
|Alice|3bc51062973c458d5a6f2d8d64a023246354ad7e064b1e4e009ec8a0699a3043|
|Bob  |cd9fb1e148ccd8442e5aa74904cc73bf6fb54d1d54d333bd596aa9bb4bb4e961|
+-----+----------------------------------------------------------------+

```

# pyspark.sql.functions.xxhash64 — PySpark 4.0.1 documentation
pyspark.sql.functions.xxhash64(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xxhash64)
[#](#pyspark.sql.functions.xxhash64 "Permalink to this definition")

Calculates the hash code of given columns using the 64-bit variant of the xxHash algorithm, and returns the result as a long column. The hash computation uses an initial seed of 42.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

one or more columns to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

hash value as long column.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('ABC', 'DEF')], ['c1', 'c2'])
>>> df.select('*', sf.xxhash64('c1')).show()
+---+---+-------------------+
| c1| c2|       xxhash64(c1)|
+---+---+-------------------+
|ABC|DEF|4105715581806190027|
+---+---+-------------------+

```


```
>>> df.select('*', sf.xxhash64('c1', df.c2)).show()
+---+---+-------------------+
| c1| c2|   xxhash64(c1, c2)|
+---+---+-------------------+
|ABC|DEF|3233247871021311208|
+---+---+-------------------+

```


```
>>> df.select('*', sf.xxhash64('*')).show()
+---+---+-------------------+
| c1| c2|   xxhash64(c1, c2)|
+---+---+-------------------+
|ABC|DEF|3233247871021311208|
+---+---+-------------------+

```


# pyspark.sql.functions.aggregate — PySpark 4.0.1 documentation
pyspark.sql.functions.aggregate(_col_, _initialValue_, _merge_, _finish\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#aggregate)
[#](#pyspark.sql.functions.aggregate "Permalink to this definition")

Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state. The final state is converted into the final result by applying a finish function.

Both functions can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**initialValue**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

initial value. Name of column or expression

**merge**function

a binary function `(acc: Column, x: Column) -> Column...` returning expression of the same type as `initialValue`

**finish**function, optional

an optional unary function `(x: Column) -> Column: ...` used to convert accumulated value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

final value after aggregate function is applied.

Examples

```
>>> df = spark.createDataFrame([(1, [20.0, 4.0, 2.0, 6.0, 10.0])], ("id", "values"))
>>> df.select(aggregate("values", lit(0.0), lambda acc, x: acc + x).alias("sum")).show()
+----+
| sum|
+----+
|42.0|
+----+

```


```
>>> def merge(acc, x):
...     count = acc.count + 1
...     sum = acc.sum + x
...     return struct(count.alias("count"), sum.alias("sum"))
...
>>> df.select(
...     aggregate(
...         "values",
...         struct(lit(0).alias("count"), lit(0.0).alias("sum")),
...         merge,
...         lambda acc: acc.sum / acc.count,
...     ).alias("mean")
... ).show()
+----+
|mean|
+----+
| 8.4|
+----+

```

# pyspark.sql.functions.array_sort — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_sort(_col_, _comparator\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_sort)
[#](#pyspark.sql.functions.array_sort "Permalink to this definition")

Collection function: sorts the input array in ascending order. The elements of the input array must be orderable. Null elements will be placed at the end of the returned array.

New in version 2.4.0.

Changed in version 3.4.0: Can take a comparator function.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**comparator**callable, optional

A binary `(Column, Column) -> Column: ...`. The comparator will take two arguments representing two elements of the array. It returns a negative integer, 0, or a positive integer as the first element is less than, equal to, or greater than the second element. If the comparator function returns null, the function will fail and raise an error.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

sorted array.

Examples

```
>>> df = spark.createDataFrame([([2, 1, None, 3],),([1],),([],)], ['data'])
>>> df.select(array_sort(df.data).alias('r')).collect()
[Row(r=[1, 2, 3, None]), Row(r=[1]), Row(r=[])]
>>> df = spark.createDataFrame([(["foo", "foobar", None, "bar"],),(["foo"],),([],)], ['data'])
>>> df.select(array_sort(
...     "data",
...     lambda x, y: when(x.isNull() | y.isNull(), lit(0)).otherwise(length(y) - length(x))
... ).alias("r")).collect()
[Row(r=['foobar', 'foo', None, 'bar']), Row(r=['foo']), Row(r=[])]

```


# pyspark.sql.functions.cardinality — PySpark 4.0.1 documentation
pyspark.sql.functions.cardinality(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#cardinality)
[#](#pyspark.sql.functions.cardinality "Permalink to this definition")

Collection function: returns the length of the array or map stored in the column.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

length of the array/map.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [([1, 2, 3],),([1],),([],)], ['data']
... ).select(sf.cardinality("data")).show()
+-----------------+
|cardinality(data)|
+-----------------+
|                3|
|                1|
|                0|
+-----------------+

```

# pyspark.sql.functions.concat — PySpark 4.0.1 documentation
pyspark.sql.functions.concat(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#concat)
[#](#pyspark.sql.functions.concat "Permalink to this definition")

Collection function: Concatenates multiple input columns together into a single column. The function works with strings, numeric, binary and compatible array columns.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column or columns to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

concatenated values. Type of the Column depends on input columns’ type.

Examples

Example 1: Concatenating string columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('abcd','123')], ['s', 'd'])
>>> df.select(sf.concat(df.s, df.d)).show()
+------------+
|concat(s, d)|
+------------+
|     abcd123|
+------------+

```


Example 2: Concatenating array columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2], [3, 4], [5]), ([1, 2], None, [3])], ['a', 'b', 'c'])
>>> df.select(sf.concat(df.a, df.b, df.c)).show()
+---------------+
|concat(a, b, c)|
+---------------+
|[1, 2, 3, 4, 5]|
|           NULL|
+---------------+

```


Example 3: Concatenating numeric columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 2, 3)], ['a', 'b', 'c'])
>>> df.select(sf.concat(df.a, df.b, df.c)).show()
+---------------+
|concat(a, b, c)|
+---------------+
|            123|
+---------------+

```


Example 4: Concatenating binary columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(bytearray(b'abc'), bytearray(b'def'))], ['a', 'b'])
>>> df.select(sf.concat(df.a, df.b)).show()
+-------------------+
|       concat(a, b)|
+-------------------+
|[61 62 63 64 65 66]|
+-------------------+

```


Example 5: Concatenating mixed types of columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,"abc",3,"def")], ['a','b','c','d'])
>>> df.select(sf.concat(df.a, df.b, df.c, df.d)).show()
+------------------+
|concat(a, b, c, d)|
+------------------+
|          1abc3def|
+------------------+

```


# pyspark.sql.functions.element_at — PySpark 4.0.1 documentation
pyspark.sql.functions.element\_at(_col_, _extraction_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#element_at)
[#](#pyspark.sql.functions.element_at "Permalink to this definition")

Collection function: (array, index) - Returns element of array at given (1-based) index. If Index is 0, Spark will throw an error. If index < 0, accesses elements from the last to the first. If ‘spark.sql.ansi.enabled’ is set to true, an exception will be thrown if the index is out of array boundaries instead of returning NULL.

(map, key) - Returns value for given key in extraction if col is map. The function always returns NULL if the key is not contained in the map.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing array or map

**extraction**

index to check for in array or key to check for in map

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value at given position.

Notes

The position is not zero based, but 1 based index. If extraction is a string, [`element_at()`](#pyspark.sql.functions.element_at "pyspark.sql.functions.element_at") treats it as a literal string, while [`try_element_at()`](about:blank/pyspark.sql.functions.try_element_at.html#pyspark.sql.functions.try_element_at "pyspark.sql.functions.try_element_at") treats it as a column name.

Examples

Example 1: Getting the first element of an array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.element_at(df.data, 1)).show()
+-------------------+
|element_at(data, 1)|
+-------------------+
|                  a|
+-------------------+

```


Example 2: Getting the last element of an array using negative index

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.element_at(df.data, -1)).show()
+--------------------+
|element_at(data, -1)|
+--------------------+
|                   c|
+--------------------+

```


Example 3: Getting a value from a map using a key

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0},)], ['data'])
>>> df.select(sf.element_at(df.data, sf.lit("a"))).show()
+-------------------+
|element_at(data, a)|
+-------------------+
|                1.0|
+-------------------+

```


Example 4: Getting a non-existing value from a map using a key

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0},)], ['data'])
>>> df.select(sf.element_at(df.data, sf.lit("c"))).show()
+-------------------+
|element_at(data, c)|
+-------------------+
|               NULL|
+-------------------+

```


Example 5: Getting a value from a map using a literal string as the key

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0}, "a")], ['data', 'b'])
>>> df.select(sf.element_at(df.data, 'b')).show()
+-------------------+
|element_at(data, b)|
+-------------------+
|                2.0|
+-------------------+

```


# pyspark.sql.functions.exists — PySpark 4.0.1 documentation
pyspark.sql.functions.exists(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#exists)
[#](#pyspark.sql.functions.exists "Permalink to this definition")

Returns whether a predicate holds for one or more elements in the array.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**f**function

`(x: Column) -> Column: ...` returning the Boolean expression. Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

True if “any” element of an array evaluates to True when passed as an argument to given function and False otherwise.

Examples

```
>>> df = spark.createDataFrame([(1, [1, 2, 3, 4]), (2, [3, -1, 0])],("key", "values"))
>>> df.select(exists("values", lambda x: x < 0).alias("any_negative")).show()
+------------+
|any_negative|
+------------+
|       false|
|        true|
+------------+

```
# pyspark.sql.functions.filter — PySpark 4.0.1 documentation
pyspark.sql.functions.filter(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#filter)
[#](#pyspark.sql.functions.filter "Permalink to this definition")

Returns an array of elements for which a predicate holds in a given array.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**f**function

A function that returns the Boolean expression. Can take one of the following forms:

*   Unary `(x: Column) -> Column: ...`
    
*   Binary `(x: Column, i: Column) -> Column...`, where the second argument is
    
    a 0-based index of the element.
    

and can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

filtered array of elements where given function evaluated to True when passed as an argument.

Examples

```
>>> df = spark.createDataFrame(
...     [(1, ["2018-09-20",  "2019-02-03", "2019-07-01", "2020-06-01"])],
...     ("key", "values")
... )
>>> def after_second_quarter(x):
...     return month(to_date(x)) > 6
...
>>> df.select(
...     filter("values", after_second_quarter).alias("after_second_quarter")
... ).show(truncate=False)
+------------------------+
|after_second_quarter    |
+------------------------+
|[2018-09-20, 2019-07-01]|
+------------------------+

```


# pyspark.sql.functions.forall — PySpark 4.0.1 documentation
pyspark.sql.functions.forall(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#forall)
[#](#pyspark.sql.functions.forall "Permalink to this definition")

Returns whether a predicate holds for every element in the array.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**f**function

`(x: Column) -> Column: ...` returning the Boolean expression. Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

True if “all” elements of an array evaluates to True when passed as an argument to given function and False otherwise.

Examples

```
>>> df = spark.createDataFrame(
...     [(1, ["bar"]), (2, ["foo", "bar"]), (3, ["foobar", "foo"])],
...     ("key", "values")
... )
>>> df.select(forall("values", lambda x: x.rlike("foo")).alias("all_foo")).show()
+-------+
|all_foo|
+-------+
|  false|
|  false|
|   true|
+-------+

```

# pyspark.sql.functions.map_filter — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_filter(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_filter)
[#](#pyspark.sql.functions.map_filter "Permalink to this definition")

Collection function: Returns a new map column whose key-value pairs satisfy a given predicate function.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or a column expression representing the map to be filtered.

**f**function

A binary function `(k: Column, v: Column) -> Column...` that defines the predicate. This function should return a boolean column that will be used to filter the input map. Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new map column containing only the key-value pairs that satisfy the predicate.

Examples

Example 1: Filtering a map with a simple condition

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, {"foo": 42.0, "bar": 1.0, "baz": 32.0})], ("id", "data"))
>>> row = df.select(
...   sf.map_filter("data", lambda _, v: v > 30.0).alias("data_filtered")
... ).head()
>>> sorted(row["data_filtered"].items())
[('baz', 32.0), ('foo', 42.0)]

```


Example 2: Filtering a map with a condition on keys

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, {"foo": 42.0, "bar": 1.0, "baz": 32.0})], ("id", "data"))
>>> row = df.select(
...   sf.map_filter("data", lambda k, _: k.startswith("b")).alias("data_filtered")
... ).head()
>>> sorted(row["data_filtered"].items())
[('bar', 1.0), ('baz', 32.0)]

```


Example 3: Filtering a map with a complex condition

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, {"foo": 42.0, "bar": 1.0, "baz": 32.0})], ("id", "data"))
>>> row = df.select(
...   sf.map_filter("data", lambda k, v: k.startswith("b") & (v > 1.0)).alias("data_filtered")
... ).head()
>>> sorted(row["data_filtered"].items())
[('baz', 32.0)]

```


# pyspark.sql.functions.map_zip_with — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_zip\_with(_col1_, _col2_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_zip_with)
[#](#pyspark.sql.functions.map_zip_with "Permalink to this definition")

Collection: Merges two given maps into a single map by applying a function to the key-value pairs.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the first column or a column expression representing the first map.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the second column or a column expression representing the second map.

**f**function

A ternary function `(k: Column, v1: Column, v2: Column) -> Column...` that defines how to merge the values from the two maps. This function should return a column that will be used as the value in the resulting map. Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new map column where each key-value pair is the result of applying the function to the corresponding key-value pairs in the input maps.

Examples

Example 1: Merging two maps with a simple function

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...   (1, {"A": 1, "B": 2}, {"A": 3, "B": 4})],
...   ("id", "map1", "map2"))
>>> row = df.select(
...   sf.map_zip_with("map1", "map2", lambda _, v1, v2: v1 + v2).alias("updated_data")
... ).head()
>>> sorted(row["updated_data"].items())
[('A', 4), ('B', 6)]

```


Example 2: Merging two maps with a complex function

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...   (1, {"A": 1, "B": 2}, {"A": 3, "B": 4})],
...   ("id", "map1", "map2"))
>>> row = df.select(
...   sf.map_zip_with("map1", "map2",
...     lambda k, v1, v2: sf.when(k == "A", v1 + v2).otherwise(v1 - v2)
...   ).alias("updated_data")
... ).head()
>>> sorted(row["updated_data"].items())
[('A', 4), ('B', -2)]

```


Example 3: Merging two maps with mismatched keys

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...   (1, {"A": 1, "B": 2}, {"B": 3, "C": 4})],
...   ("id", "map1", "map2"))
>>> row = df.select(
...   sf.map_zip_with("map1", "map2",
...     lambda _, v1, v2: sf.when(v2.isNull(), v1).otherwise(v1 + v2)
...   ).alias("updated_data")
... ).head()
>>> sorted(row["updated_data"].items())
[('A', 1), ('B', 5), ('C', None)]

```


# pyspark.sql.functions.reduce — PySpark 4.0.1 documentation
pyspark.sql.functions.reduce(_col_, _initialValue_, _merge_, _finish\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#reduce)
[#](#pyspark.sql.functions.reduce "Permalink to this definition")

Applies a binary operator to an initial state and all elements in the array, and reduces this to a single state. The final state is converted into the final result by applying a finish function.

Both functions can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**initialValue**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

initial value. Name of column or expression

**merge**function

a binary function `(acc: Column, x: Column) -> Column...` returning expression of the same type as `zero`

**finish**function, optional

an optional unary function `(x: Column) -> Column: ...` used to convert accumulated value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

final value after aggregate function is applied.

Examples

```
>>> df = spark.createDataFrame([(1, [20.0, 4.0, 2.0, 6.0, 10.0])], ("id", "values"))
>>> df.select(reduce("values", lit(0.0), lambda acc, x: acc + x).alias("sum")).show()
+----+
| sum|
+----+
|42.0|
+----+

```


```
>>> def merge(acc, x):
...     count = acc.count + 1
...     sum = acc.sum + x
...     return struct(count.alias("count"), sum.alias("sum"))
...
>>> df.select(
...     reduce(
...         "values",
...         struct(lit(0).alias("count"), lit(0.0).alias("sum")),
...         merge,
...         lambda acc: acc.sum / acc.count,
...     ).alias("mean")
... ).show()
+----+
|mean|
+----+
| 8.4|
+----+

```



# pyspark.sql.functions.reverse — PySpark 4.0.1 documentation
pyspark.sql.functions.reverse(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#reverse)
[#](#pyspark.sql.functions.reverse "Permalink to this definition")

Collection function: returns a reversed string or an array with elements in reverse order.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or an expression that represents the element to be reversed.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a reversed string or an array with elements in reverse order.

Examples

Example 1: Reverse a string

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('Spark SQL',)], ['data'])
>>> df.select(sf.reverse(df.data)).show()
+-------------+
|reverse(data)|
+-------------+
|    LQS krapS|
+-------------+

```


Example 2: Reverse an array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([2, 1, 3],) ,([1],) ,([],)], ['data'])
>>> df.select(sf.reverse(df.data)).show()
+-------------+
|reverse(data)|
+-------------+
|    [3, 1, 2]|
|          [1]|
|           []|
+-------------+

```



# pyspark.sql.functions.size — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.size

pyspark.sql.functions.size(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#size)
[#](#pyspark.sql.functions.size "Permalink to this definition")

Collection function: returns the length of the array or map stored in the column.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

length of the array/map.

Examples

```
>>> df = spark.createDataFrame([([1, 2, 3],),([1],),([],)], ['data'])
>>> df.select(size(df.data)).collect()
[Row(size(data)=3), Row(size(data)=1), Row(size(data)=0)]

```

# pyspark.sql.functions.transform — PySpark 4.0.1 documentation
pyspark.sql.functions.transform(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#transform)
[#](#pyspark.sql.functions.transform "Permalink to this definition")

Returns an array of elements after applying a transformation to each element in the input array.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**f**function

a function that is applied to each element of the input array. Can take one of the following forms:

*   Unary `(x: Column) -> Column: ...`
    
*   Binary `(x: Column, i: Column) -> Column...`, where the second argument is
    
    a 0-based index of the element.
    

and can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new array of transformed elements.

Examples

```
>>> df = spark.createDataFrame([(1, [1, 2, 3, 4])], ("key", "values"))
>>> df.select(transform("values", lambda x: x * 2).alias("doubled")).show()
+------------+
|     doubled|
+------------+
|[2, 4, 6, 8]|
+------------+

```


```
>>> def alternate(x, i):
...     return when(i % 2 == 0, x).otherwise(-x)
...
>>> df.select(transform("values", alternate).alias("alternated")).show()
+--------------+
|    alternated|
+--------------+
|[1, -2, 3, -4]|
+--------------+

```



# pyspark.sql.functions.transform_keys — PySpark 4.0.1 documentation
pyspark.sql.functions.transform\_keys(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#transform_keys)
[#](#pyspark.sql.functions.transform_keys "Permalink to this definition")

Applies a function to every key-value pair in a map and returns a map with the results of those applications as the new keys for the pairs.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**f**function

a binary function `(k: Column, v: Column) -> Column...` Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new map of entries where new keys were calculated by applying given function to each key value argument.

Examples

```
>>> df = spark.createDataFrame([(1, {"foo": -2.0, "bar": 2.0})], ("id", "data"))
>>> row = df.select(transform_keys(
...     "data", lambda k, _: upper(k)).alias("data_upper")
... ).head()
>>> sorted(row["data_upper"].items())
[('BAR', 2.0), ('FOO', -2.0)]

```



# pyspark.sql.functions.transform_values — PySpark 4.0.1 documentation
pyspark.sql.functions.transform\_values(_col_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#transform_values)
[#](#pyspark.sql.functions.transform_values "Permalink to this definition")

Applies a function to every key-value pair in a map and returns a map with the results of those applications as the new values for the pairs.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

**f**function

a binary function `(k: Column, v: Column) -> Column...` Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new map of entries where new values were calculated by applying given function to each key value argument.

Examples

```
>>> df = spark.createDataFrame([(1, {"IT": 10.0, "SALES": 2.0, "OPS": 24.0})], ("id", "data"))
>>> row = df.select(transform_values(
...     "data", lambda k, v: when(k.isin("IT", "OPS"), v + 10.0).otherwise(v)
... ).alias("new_data")).head()
>>> sorted(row["new_data"].items())
[('IT', 20.0), ('OPS', 34.0), ('SALES', 2.0)]

```




# pyspark.sql.functions.try_element_at — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_element\_at(_col_, _extraction_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_element_at)
[#](#pyspark.sql.functions.try_element_at "Permalink to this definition")

Collection function: (array, index) - Returns element of array at given (1-based) index. If Index is 0, Spark will throw an error. If index < 0, accesses elements from the last to the first. The function always returns NULL if the index exceeds the length of the array.

(map, key) - Returns value for given key. The function always returns NULL if the key is not contained in the map.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing array or map

**extraction**

index to check for in array or key to check for in map

Notes

The position is not zero based, but 1 based index. If extraction is a string, [`try_element_at()`](#pyspark.sql.functions.try_element_at "pyspark.sql.functions.try_element_at") treats it as a column name, while [`element_at()`](about:blank/pyspark.sql.functions.element_at.html#pyspark.sql.functions.element_at "pyspark.sql.functions.element_at") treats it as a literal string.

Examples

Example 1: Getting the first element of an array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.try_element_at(df.data, sf.lit(1))).show()
+-----------------------+
|try_element_at(data, 1)|
+-----------------------+
|                      a|
+-----------------------+

```


Example 2: Getting the last element of an array using negative index

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.try_element_at(df.data, sf.lit(-1))).show()
+------------------------+
|try_element_at(data, -1)|
+------------------------+
|                       c|
+------------------------+

```


Example 3: Getting a value from a map using a key

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0},)], ['data'])
>>> df.select(sf.try_element_at(df.data, sf.lit("a"))).show()
+-----------------------+
|try_element_at(data, a)|
+-----------------------+
|                    1.0|
+-----------------------+

```


Example 4: Getting a non-existing element from an array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.try_element_at(df.data, sf.lit(4))).show()
+-----------------------+
|try_element_at(data, 4)|
+-----------------------+
|                   NULL|
+-----------------------+

```


Example 5: Getting a non-existing value from a map using a key

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0},)], ['data'])
>>> df.select(sf.try_element_at(df.data, sf.lit("c"))).show()
+-----------------------+
|try_element_at(data, c)|
+-----------------------+
|                   NULL|
+-----------------------+

```


Example 6: Getting a value from a map using a column name as the key

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([({"a": 1.0, "b": 2.0}, "a")], ['data', 'b'])
>>> df.select(sf.try_element_at(df.data, 'b')).show()
+-----------------------+
|try_element_at(data, b)|
+-----------------------+
|                    1.0|
+-----------------------+

```



# pyspark.sql.functions.zip_with — PySpark 4.0.1 documentation
pyspark.sql.functions.zip\_with(_left_, _right_, _f_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#zip_with)
[#](#pyspark.sql.functions.zip_with "Permalink to this definition")

Merge two given arrays, element-wise, into a single array using a function. If one array is shorter, nulls are appended at the end to match the length of the longer array, before applying the function.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**left**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of the first column or expression

**right**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of the second column or expression

**f**function

a binary function `(x1: Column, x2: Column) -> Column...` Can use methods of [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), functions defined in `pyspark.sql.functions` and Scala `UserDefinedFunctions`. Python `UserDefinedFunctions` are not supported ([SPARK-27052](https://issues.apache.org/jira/browse/SPARK-27052)).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

array of calculated values derived by applying given function to each pair of arguments.

Examples

```
>>> df = spark.createDataFrame([(1, [1, 3, 5, 8], [0, 2, 4, 6])], ("id", "xs", "ys"))
>>> df.select(zip_with("xs", "ys", lambda x, y: x ** y).alias("powers")).show(truncate=False)
+---------------------------+
|powers                     |
+---------------------------+
|[1.0, 9.0, 625.0, 262144.0]|
+---------------------------+

```


```
>>> df = spark.createDataFrame([(1, ["foo", "bar"], [1, 2, 3])], ("id", "xs", "ys"))
>>> df.select(zip_with("xs", "ys", lambda x, y: concat_ws("_", x, y)).alias("xs_ys")).show()
+-----------------+
|            xs_ys|
+-----------------+
|[foo_1, bar_2, 3]|
+-----------------+

```

# pyspark.sql.functions.array — PySpark 4.0.1 documentation
pyspark.sql.functions.array(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array)
[#](#pyspark.sql.functions.array "Permalink to this definition")

Collection function: Creates a new array column from the input columns or column names.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") objects that have the same data type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column of array type, where each value is an array containing the corresponding values from the input columns.

Examples

Example 1: Basic usage of array function with column names.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", "doctor"), ("Bob", "engineer")],
...     ("name", "occupation"))
>>> df.select(sf.array('name', 'occupation')).show()
+-----------------------+
|array(name, occupation)|
+-----------------------+
|        [Alice, doctor]|
|        [Bob, engineer]|
+-----------------------+

```


Example 2: Usage of array function with Column objects.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", "doctor"), ("Bob", "engineer")],
...     ("name", "occupation"))
>>> df.select(sf.array(df.name, df.occupation)).show()
+-----------------------+
|array(name, occupation)|
+-----------------------+
|        [Alice, doctor]|
|        [Bob, engineer]|
+-----------------------+

```


Example 3: Single argument as list of column names.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", "doctor"), ("Bob", "engineer")],
...     ("name", "occupation"))
>>> df.select(sf.array(['name', 'occupation'])).show()
+-----------------------+
|array(name, occupation)|
+-----------------------+
|        [Alice, doctor]|
|        [Bob, engineer]|
+-----------------------+

```


Example 4: Usage of array function with columns of different types.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [("Alice", 2, 22.2), ("Bob", 5, 36.1)],
...     ("name", "age", "weight"))
>>> df.select(sf.array(['age', 'weight'])).show()
+------------------+
|array(age, weight)|
+------------------+
|       [2.0, 22.2]|
|       [5.0, 36.1]|
+------------------+

```


Example 5: array function with a column containing null values.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", None), ("Bob", "engineer")],
...     ("name", "occupation"))
>>> df.select(sf.array('name', 'occupation')).show()
+-----------------------+
|array(name, occupation)|
+-----------------------+
|          [Alice, NULL]|
|        [Bob, engineer]|
+-----------------------+

```

# pyspark.sql.functions.array_append — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_append(_col_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_append)
[#](#pyspark.sql.functions.array_append "Permalink to this definition")

Array function: returns a new array column by appending value to the existing array col.

New in version 3.4.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column containing the array.

**value**

A literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression to be appended to the array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new array column with value appended to the original array.

Notes

Supports Spark Connect.

Examples

Example 1: Appending a column value to an array column

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2="c")])
>>> df.select(sf.array_append(df.c1, df.c2)).show()
+--------------------+
|array_append(c1, c2)|
+--------------------+
|        [b, a, c, c]|
+--------------------+

```


Example 2: Appending a numeric value to an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_append(df.data, 4)).show()
+---------------------+
|array_append(data, 4)|
+---------------------+
|         [1, 2, 3, 4]|
+---------------------+

```


Example 3: Appending a null value to an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_append(df.data, None)).show()
+------------------------+
|array_append(data, NULL)|
+------------------------+
|         [1, 2, 3, NULL]|
+------------------------+

```


Example 4: Appending a value to a NULL array column

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([(None,)], schema=schema)
>>> df.select(sf.array_append(df.data, 4)).show()
+---------------------+
|array_append(data, 4)|
+---------------------+
|                 NULL|
+---------------------+

```


Example 5: Appending a value to an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.array_append(df.data, 1)).show()
+---------------------+
|array_append(data, 1)|
+---------------------+
|                  [1]|
+---------------------+

```


# pyspark.sql.functions.array_compact — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_compact(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_compact)
[#](#pyspark.sql.functions.array_compact "Permalink to this definition")

Array function: removes null values from the array.

New in version 3.4.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that is an array excluding the null values from the input column.

Notes

Supports Spark Connect.

Examples

Example 1: Removing null values from a simple array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, None, 2, 3],)], ['data'])
>>> df.select(sf.array_compact(df.data)).show()
+-------------------+
|array_compact(data)|
+-------------------+
|          [1, 2, 3]|
+-------------------+

```


Example 2: Removing null values from multiple arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, None, 2, 3],), ([4, 5, None, 4],)], ['data'])
>>> df.select(sf.array_compact(df.data)).show()
+-------------------+
|array_compact(data)|
+-------------------+
|          [1, 2, 3]|
|          [4, 5, 4]|
+-------------------+

```


Example 3: Removing null values from an array with all null values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> schema = StructType([
...   StructField("data", ArrayType(StringType()), True)
... ])
>>> df = spark.createDataFrame([([None, None, None],)], schema)
>>> df.select(sf.array_compact(df.data)).show()
+-------------------+
|array_compact(data)|
+-------------------+
|                 []|
+-------------------+

```


Example 4: Removing null values from an array with no null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_compact(df.data)).show()
+-------------------+
|array_compact(data)|
+-------------------+
|          [1, 2, 3]|
+-------------------+

```


Example 5: Removing null values from an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> schema = StructType([
...   StructField("data", ArrayType(StringType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema)
>>> df.select(sf.array_compact(df.data)).show()
+-------------------+
|array_compact(data)|
+-------------------+
|                 []|
+-------------------+

```


# pyspark.sql.functions.array_contains — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_contains(_col_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_contains)
[#](#pyspark.sql.functions.array_contains "Permalink to this definition")

Collection function: This function returns a boolean indicating whether the array contains the given value, returning null if the array is null, true if the array contains the given value, and false otherwise.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The target column containing the arrays.

**value**

The value or column to check for in the array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column of Boolean type, where each value indicates whether the corresponding array from the input column contains the specified value.

Examples

Example 1: Basic usage of array\_contains function.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],), ([],)], ['data'])
>>> df.select(sf.array_contains(df.data, "a")).show()
+-----------------------+
|array_contains(data, a)|
+-----------------------+
|                   true|
|                  false|
+-----------------------+

```


Example 2: Usage of array\_contains function with a column.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"], "c"),
...                            (["c", "d", "e"], "d"),
...                            (["e", "a", "c"], "b")], ["data", "item"])
>>> df.select(sf.array_contains(df.data, sf.col("item"))).show()
+--------------------------+
|array_contains(data, item)|
+--------------------------+
|                      true|
|                      true|
|                     false|
+--------------------------+

```


Example 3: Attempt to use array\_contains function with a null array.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(None,), (["a", "b", "c"],)], ['data'])
>>> df.select(sf.array_contains(df.data, "a")).show()
+-----------------------+
|array_contains(data, a)|
+-----------------------+
|                   NULL|
|                   true|
+-----------------------+

```


Example 4: Usage of array\_contains with an array column containing null values.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", None, "c"],)], ['data'])
>>> df.select(sf.array_contains(df.data, "a")).show()
+-----------------------+
|array_contains(data, a)|
+-----------------------+
|                   true|
+-----------------------+

```


# pyspark.sql.functions.array_distinct — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_distinct(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_distinct)
[#](#pyspark.sql.functions.array_distinct "Permalink to this definition")

Array function: removes duplicate values from the array.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that is an array of unique values from the input column.

Examples

Example 1: Removing duplicate values from a simple array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3, 2],)], ['data'])
>>> df.select(sf.array_distinct(df.data)).show()
+--------------------+
|array_distinct(data)|
+--------------------+
|           [1, 2, 3]|
+--------------------+

```


Example 2: Removing duplicate values from multiple arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3, 2],), ([4, 5, 5, 4],)], ['data'])
>>> df.select(sf.array_distinct(df.data)).show()
+--------------------+
|array_distinct(data)|
+--------------------+
|           [1, 2, 3]|
|              [4, 5]|
+--------------------+

```


Example 3: Removing duplicate values from an array with all identical values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 1, 1],)], ['data'])
>>> df.select(sf.array_distinct(df.data)).show()
+--------------------+
|array_distinct(data)|
+--------------------+
|                 [1]|
+--------------------+

```


Example 4: Removing duplicate values from an array with no duplicate values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_distinct(df.data)).show()
+--------------------+
|array_distinct(data)|
+--------------------+
|           [1, 2, 3]|
+--------------------+

```


Example 5: Removing duplicate values from an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema)
>>> df.select(sf.array_distinct(df.data)).show()
+--------------------+
|array_distinct(data)|
+--------------------+
|                  []|
+--------------------+

```

# pyspark.sql.functions.array_except — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_except(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_except)
[#](#pyspark.sql.functions.array_except "Permalink to this definition")

Array function: returns a new array containing the elements present in col1 but not in col2, without duplicates.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing the first array.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing the second array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new array containing the elements present in col1 but not in col2.

Notes

This function does not preserve the order of the elements in the input arrays.

Examples

Example 1: Basic usage

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2=["c", "d", "a", "f"])])
>>> df.select(sf.array_except(df.c1, df.c2)).show()
+--------------------+
|array_except(c1, c2)|
+--------------------+
|                 [b]|
+--------------------+

```


Example 2: Except with no common elements

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2=["d", "e", "f"])])
>>> df.select(sf.sort_array(sf.array_except(df.c1, df.c2))).show()
+--------------------------------------+
|sort_array(array_except(c1, c2), true)|
+--------------------------------------+
|                             [a, b, c]|
+--------------------------------------+

```


Example 3: Except with all common elements

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["a", "b", "c"], c2=["a", "b", "c"])])
>>> df.select(sf.array_except(df.c1, df.c2)).show()
+--------------------+
|array_except(c1, c2)|
+--------------------+
|                  []|
+--------------------+

```


Example 4: Except with null values

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["a", "b", None], c2=["a", None, "c"])])
>>> df.select(sf.array_except(df.c1, df.c2)).show()
+--------------------+
|array_except(c1, c2)|
+--------------------+
|                 [b]|
+--------------------+

```


Example 5: Except with empty arrays

```
>>> from pyspark.sql import Row, functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> data = [Row(c1=[], c2=["a", "b", "c"])]
>>> schema = StructType([
...   StructField("c1", ArrayType(StringType()), True),
...   StructField("c2", ArrayType(StringType()), True)
... ])
>>> df = spark.createDataFrame(data, schema)
>>> df.select(sf.array_except(df.c1, df.c2)).show()
+--------------------+
|array_except(c1, c2)|
+--------------------+
|                  []|
+--------------------+

```



# pyspark.sql.functions.array_insert — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_insert(_arr_, _pos_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_insert)
[#](#pyspark.sql.functions.array_insert "Permalink to this definition")

Array function: Inserts an item into a given array at a specified array index. Array indices start at 1, or start from the end if index is negative. Index above array size appends the array, or prepends the array if index is negative, with ‘null’ elements.

New in version 3.4.0.

Parameters

**arr**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing an array

**pos**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str or int

name of Numeric type column indicating position of insertion (starting at index 1, negative position is a start from the back of the array)

**value**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

an array of values, including the new specified value

Notes

Supports Spark Connect.

Examples

Example 1: Inserting a value at a specific position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['a', 'b', 'c'],)], ['data'])
>>> df.select(sf.array_insert(df.data, 2, 'd')).show()
+------------------------+
|array_insert(data, 2, d)|
+------------------------+
|            [a, d, b, c]|
+------------------------+

```


Example 2: Inserting a value at a negative position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['a', 'b', 'c'],)], ['data'])
>>> df.select(sf.array_insert(df.data, -2, 'd')).show()
+-------------------------+
|array_insert(data, -2, d)|
+-------------------------+
|             [a, b, d, c]|
+-------------------------+

```


Example 3: Inserting a value at a position greater than the array size

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['a', 'b', 'c'],)], ['data'])
>>> df.select(sf.array_insert(df.data, 5, 'e')).show()
+------------------------+
|array_insert(data, 5, e)|
+------------------------+
|      [a, b, c, NULL, e]|
+------------------------+

```


Example 4: Inserting a NULL value

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['a', 'b', 'c'],)], ['data'])
>>> df.select(sf.array_insert(df.data, 2, sf.lit(None))).show()
+---------------------------+
|array_insert(data, 2, NULL)|
+---------------------------+
|            [a, NULL, b, c]|
+---------------------------+

```


Example 5: Inserting a value into a NULL array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([StructField("data", ArrayType(IntegerType()), True)])
>>> df = spark.createDataFrame([(None,)], schema=schema)
>>> df.select(sf.array_insert(df.data, 1, 5)).show()
+------------------------+
|array_insert(data, 1, 5)|
+------------------------+
|                    NULL|
+------------------------+

```


# pyspark.sql.functions.array_intersect — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_intersect(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_intersect)
[#](#pyspark.sql.functions.array_intersect "Permalink to this definition")

Array function: returns a new array containing the intersection of elements in col1 and col2, without duplicates.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing the first array.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing the second array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new array containing the intersection of elements in col1 and col2.

Notes

This function does not preserve the order of the elements in the input arrays.

Examples

Example 1: Basic usage

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2=["c", "d", "a", "f"])])
>>> df.select(sf.sort_array(sf.array_intersect(df.c1, df.c2))).show()
+-----------------------------------------+
|sort_array(array_intersect(c1, c2), true)|
+-----------------------------------------+
|                                   [a, c]|
+-----------------------------------------+

```


Example 2: Intersection with no common elements

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2=["d", "e", "f"])])
>>> df.select(sf.array_intersect(df.c1, df.c2)).show()
+-----------------------+
|array_intersect(c1, c2)|
+-----------------------+
|                     []|
+-----------------------+

```


Example 3: Intersection with all common elements

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["a", "b", "c"], c2=["a", "b", "c"])])
>>> df.select(sf.sort_array(sf.array_intersect(df.c1, df.c2))).show()
+-----------------------------------------+
|sort_array(array_intersect(c1, c2), true)|
+-----------------------------------------+
|                                [a, b, c]|
+-----------------------------------------+

```


Example 4: Intersection with null values

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["a", "b", None], c2=["a", None, "c"])])
>>> df.select(sf.sort_array(sf.array_intersect(df.c1, df.c2))).show()
+-----------------------------------------+
|sort_array(array_intersect(c1, c2), true)|
+-----------------------------------------+
|                                [NULL, a]|
+-----------------------------------------+

```


Example 5: Intersection with empty arrays

```
>>> from pyspark.sql import Row, functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> data = [Row(c1=[], c2=["a", "b", "c"])]
>>> schema = StructType([
...   StructField("c1", ArrayType(StringType()), True),
...   StructField("c2", ArrayType(StringType()), True)
... ])
>>> df = spark.createDataFrame(data, schema)
>>> df.select(sf.array_intersect(df.c1, df.c2)).show()
+-----------------------+
|array_intersect(c1, c2)|
+-----------------------+
|                     []|
+-----------------------+

```


# pyspark.sql.functions.array_join — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_join(_col_, _delimiter_, _null\_replacement\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_join)
[#](#pyspark.sql.functions.array_join "Permalink to this definition")

Array function: Returns a string column by concatenating the elements of the input array column using the delimiter. Null values within the array can be replaced with a specified string through the null\_replacement argument. If null\_replacement is not set, null values are ignored.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The input column containing the arrays to be joined.

**delimiter**str

The string to be used as the delimiter when joining the array elements.

**null\_replacement**str, optional

The string to replace null values within the array. If not set, null values are ignored.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of string type, where each value is the result of joining the corresponding array from the input column.

Examples

Example 1: Basic usage of array\_join function.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],), (["a", "b"],)], ['data'])
>>> df.select(sf.array_join(df.data, ",")).show()
+-------------------+
|array_join(data, ,)|
+-------------------+
|              a,b,c|
|                a,b|
+-------------------+

```


Example 2: Usage of array\_join function with null\_replacement argument.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", None, "c"],)], ['data'])
>>> df.select(sf.array_join(df.data, ",", "NULL")).show()
+-------------------------+
|array_join(data, ,, NULL)|
+-------------------------+
|                 a,NULL,c|
+-------------------------+

```


Example 3: Usage of array\_join function without null\_replacement argument.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", None, "c"],)], ['data'])
>>> df.select(sf.array_join(df.data, ",")).show()
+-------------------+
|array_join(data, ,)|
+-------------------+
|                a,c|
+-------------------+

```


Example 4: Usage of array\_join function with an array that is null.

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, ArrayType, StringType
>>> schema = StructType([StructField("data", ArrayType(StringType()), True)])
>>> df = spark.createDataFrame([(None,)], schema)
>>> df.select(sf.array_join(df.data, ",")).show()
+-------------------+
|array_join(data, ,)|
+-------------------+
|               NULL|
+-------------------+

```


Example 5: Usage of array\_join function with an array containing only null values.

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, ArrayType, StringType
>>> schema = StructType([StructField("data", ArrayType(StringType()), True)])
>>> df = spark.createDataFrame([([None, None],)], schema)
>>> df.select(sf.array_join(df.data, ",", "NULL")).show()
+-------------------------+
|array_join(data, ,, NULL)|
+-------------------------+
|                NULL,NULL|
+-------------------------+

```


# pyspark.sql.functions.array_max — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_max(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_max)
[#](#pyspark.sql.functions.array_max "Permalink to this definition")

Array function: returns the maximum value of the array.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or an expression that represents the array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains the maximum value of each array.

Examples

Example 1: Basic usage with integer array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([2, 1, 3],), ([None, 10, -1],)], ['data'])
>>> df.select(sf.array_max(df.data)).show()
+---------------+
|array_max(data)|
+---------------+
|              3|
|             10|
+---------------+

```


Example 2: Usage with string array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 'banana', 'cherry'],)], ['data'])
>>> df.select(sf.array_max(df.data)).show()
+---------------+
|array_max(data)|
+---------------+
|         cherry|
+---------------+

```


Example 3: Usage with mixed type array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 1, 'cherry'],)], ['data'])
>>> df.select(sf.array_max(df.data)).show()
+---------------+
|array_max(data)|
+---------------+
|         cherry|
+---------------+

```


Example 4: Usage with array of arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([[2, 1], [3, 4]],)], ['data'])
>>> df.select(sf.array_max(df.data)).show()
+---------------+
|array_max(data)|
+---------------+
|         [3, 4]|
+---------------+

```


Example 5: Usage with empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.array_max(df.data)).show()
+---------------+
|array_max(data)|
+---------------+
|           NULL|
+---------------+

```
# pyspark.sql.functions.array_min — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_min(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_min)
[#](#pyspark.sql.functions.array_min "Permalink to this definition")

Array function: returns the minimum value of the array.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or an expression that represents the array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains the minimum value of each array.

Examples

Example 1: Basic usage with integer array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([2, 1, 3],), ([None, 10, -1],)], ['data'])
>>> df.select(sf.array_min(df.data)).show()
+---------------+
|array_min(data)|
+---------------+
|              1|
|             -1|
+---------------+

```


Example 2: Usage with string array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 'banana', 'cherry'],)], ['data'])
>>> df.select(sf.array_min(df.data)).show()
+---------------+
|array_min(data)|
+---------------+
|          apple|
+---------------+

```


Example 3: Usage with mixed type array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 1, 'cherry'],)], ['data'])
>>> df.select(sf.array_min(df.data)).show()
+---------------+
|array_min(data)|
+---------------+
|              1|
+---------------+

```


Example 4: Usage with array of arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([[2, 1], [3, 4]],)], ['data'])
>>> df.select(sf.array_min(df.data)).show()
+---------------+
|array_min(data)|
+---------------+
|         [2, 1]|
+---------------+

```


Example 5: Usage with empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.array_min(df.data)).show()
+---------------+
|array_min(data)|
+---------------+
|           NULL|
+---------------+

```



# pyspark.sql.functions.array_position — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_position(_col_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_position)
[#](#pyspark.sql.functions.array_position "Permalink to this definition")

Array function: Locates the position of the first occurrence of the given value in the given array. Returns null if either of the arguments are null.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target column to work on.

**value**Any

value or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression to look for.

Changed in version 4.0.0: value now also accepts a Column type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

position of the value in the given array if found and 0 otherwise.

Notes

The position is not zero based, but 1 based index. Returns 0 if the given value could not be found in the array.

Examples

Example 1: Finding the position of a string in an array of strings

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["c", "b", "a"],)], ['data'])
>>> df.select(sf.array_position(df.data, "a")).show()
+-----------------------+
|array_position(data, a)|
+-----------------------+
|                      3|
+-----------------------+

```


Example 2: Finding the position of a string in an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> schema = StructType([StructField("data", ArrayType(StringType()), True)])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.array_position(df.data, "a")).show()
+-----------------------+
|array_position(data, a)|
+-----------------------+
|                      0|
+-----------------------+

```


Example 3: Finding the position of an integer in an array of integers

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_position(df.data, 2)).show()
+-----------------------+
|array_position(data, 2)|
+-----------------------+
|                      2|
+-----------------------+

```


Example 4: Finding the position of a non-existing value in an array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["c", "b", "a"],)], ['data'])
>>> df.select(sf.array_position(df.data, "d")).show()
+-----------------------+
|array_position(data, d)|
+-----------------------+
|                      0|
+-----------------------+

```


Example 5: Finding the position of a value in an array with nulls

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([None, "b", "a"],)], ['data'])
>>> df.select(sf.array_position(df.data, "a")).show()
+-----------------------+
|array_position(data, a)|
+-----------------------+
|                      3|
+-----------------------+

```


Example 6: Finding the position of a column’s value in an array of integers

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([10, 20, 30], 20)], ['data', 'col'])
>>> df.select(sf.array_position(df.data, df.col)).show()
+-------------------------+
|array_position(data, col)|
+-------------------------+
|                        2|
+-------------------------+

```


# pyspark.sql.functions.array_prepend — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_prepend(_col_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_prepend)
[#](#pyspark.sql.functions.array_prepend "Permalink to this definition")

Array function: Returns an array containing the given element as the first element and the rest of the elements from the original array.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing array

**value**

a literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

an array with the given value prepended.

Examples

Example 1: Prepending a column value to an array column

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2="c")])
>>> df.select(sf.array_prepend(df.c1, df.c2)).show()
+---------------------+
|array_prepend(c1, c2)|
+---------------------+
|         [c, b, a, c]|
+---------------------+

```


Example 2: Prepending a numeric value to an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_prepend(df.data, 4)).show()
+----------------------+
|array_prepend(data, 4)|
+----------------------+
|          [4, 1, 2, 3]|
+----------------------+

```


Example 3: Prepending a null value to an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_prepend(df.data, None)).show()
+-------------------------+
|array_prepend(data, NULL)|
+-------------------------+
|          [NULL, 1, 2, 3]|
+-------------------------+

```


Example 4: Prepending a value to a NULL array column

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([(None,)], schema=schema)
>>> df.select(sf.array_prepend(df.data, 4)).show()
+----------------------+
|array_prepend(data, 4)|
+----------------------+
|                  NULL|
+----------------------+

```


Example 5: Prepending a value to an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.array_prepend(df.data, 1)).show()
+----------------------+
|array_prepend(data, 1)|
+----------------------+
|                   [1]|
+----------------------+

```


# pyspark.sql.functions.array_remove — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_remove(_col_, _element_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_remove)
[#](#pyspark.sql.functions.array_remove "Permalink to this definition")

Array function: Remove all elements that equal to element from the given array.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing array

**element**

element or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression to be removed from the array

Changed in version 4.0.0: element now also accepts a Column type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that is an array excluding the given value from the input column.

Examples

Example 1: Removing a specific value from a simple array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3, 1, 1],)], ['data'])
>>> df.select(sf.array_remove(df.data, 1)).show()
+---------------------+
|array_remove(data, 1)|
+---------------------+
|               [2, 3]|
+---------------------+

```


Example 2: Removing a specific value from multiple arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3, 1, 1],), ([4, 5, 5, 4],)], ['data'])
>>> df.select(sf.array_remove(df.data, 5)).show()
+---------------------+
|array_remove(data, 5)|
+---------------------+
|      [1, 2, 3, 1, 1]|
|               [4, 4]|
+---------------------+

```


Example 3: Removing a value that does not exist in the array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],)], ['data'])
>>> df.select(sf.array_remove(df.data, 4)).show()
+---------------------+
|array_remove(data, 4)|
+---------------------+
|            [1, 2, 3]|
+---------------------+

```


Example 4: Removing a value from an array with all identical values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 1, 1],)], ['data'])
>>> df.select(sf.array_remove(df.data, 1)).show()
+---------------------+
|array_remove(data, 1)|
+---------------------+
|                   []|
+---------------------+

```


Example 5: Removing a value from an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema)
>>> df.select(sf.array_remove(df.data, 1)).show()
+---------------------+
|array_remove(data, 1)|
+---------------------+
|                   []|
+---------------------+

```


Example 6: Removing a column’s value from a simple array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3, 1, 1], 1)], ['data', 'col'])
>>> df.select(sf.array_remove(df.data, df.col)).show()
+-----------------------+
|array_remove(data, col)|
+-----------------------+
|                 [2, 3]|
+-----------------------+

```



# pyspark.sql.functions.array_repeat — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_repeat(_col_, _count_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_repeat)
[#](#pyspark.sql.functions.array_repeat "Permalink to this definition")

Array function: creates an array containing a column repeated count times.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or an expression that represents the element to be repeated.

**count**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str or int

The name of the column, an expression, or an integer that represents the number of times to repeat the element.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains an array of repeated elements.

Examples

Example 1: Usage with string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('ab',)], ['data'])
>>> df.select(sf.array_repeat(df.data, 3)).show()
+---------------------+
|array_repeat(data, 3)|
+---------------------+
|         [ab, ab, ab]|
+---------------------+

```


Example 2: Usage with integer

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(3,)], ['data'])
>>> df.select(sf.array_repeat(df.data, 2)).show()
+---------------------+
|array_repeat(data, 2)|
+---------------------+
|               [3, 3]|
+---------------------+

```


Example 3: Usage with array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 'banana'],)], ['data'])
>>> df.select(sf.array_repeat(df.data, 2)).show(truncate=False)
+----------------------------------+
|array_repeat(data, 2)             |
+----------------------------------+
|[[apple, banana], [apple, banana]]|
+----------------------------------+

```


Example 4: Usage with null

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", IntegerType(), True)
... ])
>>> df = spark.createDataFrame([(None, )], schema=schema)
>>> df.select(sf.array_repeat(df.data, 3)).show()
+---------------------+
|array_repeat(data, 3)|
+---------------------+
|   [NULL, NULL, NULL]|
+---------------------+

```



# pyspark.sql.functions.array_size — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_size(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_size)
[#](#pyspark.sql.functions.array_size "Permalink to this definition")

Array function: returns the total number of elements in the array. The function returns null for null input.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or an expression that represents the array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains the size of each array.

Examples

Example 1: Basic usage with integer array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([2, 1, 3],), (None,)], ['data'])
>>> df.select(sf.array_size(df.data)).show()
+----------------+
|array_size(data)|
+----------------+
|               3|
|            NULL|
+----------------+

```


Example 2: Usage with string array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 'banana', 'cherry'],)], ['data'])
>>> df.select(sf.array_size(df.data)).show()
+----------------+
|array_size(data)|
+----------------+
|               3|
+----------------+

```


Example 3: Usage with mixed type array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(['apple', 1, 'cherry'],)], ['data'])
>>> df.select(sf.array_size(df.data)).show()
+----------------+
|array_size(data)|
+----------------+
|               3|
+----------------+

```


Example 4: Usage with array of arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([[2, 1], [3, 4]],)], ['data'])
>>> df.select(sf.array_size(df.data)).show()
+----------------+
|array_size(data)|
+----------------+
|               2|
+----------------+

```


Example 5: Usage with empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(IntegerType()), True)
... ])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.array_size(df.data)).show()
+----------------+
|array_size(data)|
+----------------+
|               0|
+----------------+

```

# pyspark.sql.functions.array_union — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_union(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_union)
[#](#pyspark.sql.functions.array_union "Permalink to this definition")

Array function: returns a new array containing the union of elements in col1 and col2, without duplicates.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing the first array.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing the second array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new array containing the union of elements in col1 and col2.

Notes

This function does not preserve the order of the elements in the input arrays.

Examples

Example 1: Basic usage

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2=["c", "d", "a", "f"])])
>>> df.select(sf.sort_array(sf.array_union(df.c1, df.c2))).show()
+-------------------------------------+
|sort_array(array_union(c1, c2), true)|
+-------------------------------------+
|                      [a, b, c, d, f]|
+-------------------------------------+

```


Example 2: Union with no common elements

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["b", "a", "c"], c2=["d", "e", "f"])])
>>> df.select(sf.sort_array(sf.array_union(df.c1, df.c2))).show()
+-------------------------------------+
|sort_array(array_union(c1, c2), true)|
+-------------------------------------+
|                   [a, b, c, d, e, f]|
+-------------------------------------+

```


Example 3: Union with all common elements

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["a", "b", "c"], c2=["a", "b", "c"])])
>>> df.select(sf.sort_array(sf.array_union(df.c1, df.c2))).show()
+-------------------------------------+
|sort_array(array_union(c1, c2), true)|
+-------------------------------------+
|                            [a, b, c]|
+-------------------------------------+

```


Example 4: Union with null values

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([Row(c1=["a", "b", None], c2=["a", None, "c"])])
>>> df.select(sf.sort_array(sf.array_union(df.c1, df.c2))).show()
+-------------------------------------+
|sort_array(array_union(c1, c2), true)|
+-------------------------------------+
|                      [NULL, a, b, c]|
+-------------------------------------+

```


Example 5: Union with empty arrays

```
>>> from pyspark.sql import Row, functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> data = [Row(c1=[], c2=["a", "b", "c"])]
>>> schema = StructType([
...   StructField("c1", ArrayType(StringType()), True),
...   StructField("c2", ArrayType(StringType()), True)
... ])
>>> df = spark.createDataFrame(data, schema)
>>> df.select(sf.sort_array(sf.array_union(df.c1, df.c2))).show()
+-------------------------------------+
|sort_array(array_union(c1, c2), true)|
+-------------------------------------+
|                            [a, b, c]|
+-------------------------------------+

```


# pyspark.sql.functions.arrays_overlap — PySpark 4.0.1 documentation
pyspark.sql.functions.arrays\_overlap(_a1_, _a2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#arrays_overlap)
[#](#pyspark.sql.functions.arrays_overlap "Permalink to this definition")

Collection function: This function returns a boolean column indicating if the input arrays have common non-null elements, returning true if they do, null if the arrays do not contain any common elements but are not empty and at least one of them contains a null element, and false otherwise.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**a1, a2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The names of the columns that contain the input arrays.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column of Boolean type, where each value indicates whether the corresponding arrays from the input columns contain any common elements.

Examples

Example 1: Basic usage of arrays\_overlap function.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b"], ["b", "c"]), (["a"], ["b", "c"])], ['x', 'y'])
>>> df.select(sf.arrays_overlap(df.x, df.y)).show()
+--------------------+
|arrays_overlap(x, y)|
+--------------------+
|                true|
|               false|
+--------------------+

```


Example 2: Usage of arrays\_overlap function with arrays containing null elements.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", None], ["b", None]), (["a"], ["b", "c"])], ['x', 'y'])
>>> df.select(sf.arrays_overlap(df.x, df.y)).show()
+--------------------+
|arrays_overlap(x, y)|
+--------------------+
|                NULL|
|               false|
+--------------------+

```


Example 3: Usage of arrays\_overlap function with arrays that are null.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(None, ["b", "c"]), (["a"], None)], ['x', 'y'])
>>> df.select(sf.arrays_overlap(df.x, df.y)).show()
+--------------------+
|arrays_overlap(x, y)|
+--------------------+
|                NULL|
|                NULL|
+--------------------+

```


Example 4: Usage of arrays\_overlap on arrays with identical elements.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b"], ["a", "b"]), (["a"], ["a"])], ['x', 'y'])
>>> df.select(sf.arrays_overlap(df.x, df.y)).show()
+--------------------+
|arrays_overlap(x, y)|
+--------------------+
|                true|
|                true|
+--------------------+

```



# pyspark.sql.functions.arrays_zip — PySpark 4.0.1 documentation
pyspark.sql.functions.arrays\_zip(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#arrays_zip)
[#](#pyspark.sql.functions.arrays_zip "Permalink to this definition")

Array function: Returns a merged array of structs in which the N-th struct contains all N-th values of input arrays. If one of the arrays is shorter than others then the resulting struct type value will be a null for missing elements.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Columns of arrays to be merged.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Merged array of entries.

Examples

Example 1: Zipping two arrays of the same length

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3], ['a', 'b', 'c'])], ['nums', 'letters'])
>>> df.select(sf.arrays_zip(df.nums, df.letters)).show(truncate=False)
+-------------------------+
|arrays_zip(nums, letters)|
+-------------------------+
|[{1, a}, {2, b}, {3, c}] |
+-------------------------+

```


Example 2: Zipping arrays of different lengths

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2], ['a', 'b', 'c'])], ['nums', 'letters'])
>>> df.select(sf.arrays_zip(df.nums, df.letters)).show(truncate=False)
+---------------------------+
|arrays_zip(nums, letters)  |
+---------------------------+
|[{1, a}, {2, b}, {NULL, c}]|
+---------------------------+

```


Example 3: Zipping more than two arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [([1, 2], ['a', 'b'], [True, False])], ['nums', 'letters', 'bools'])
>>> df.select(sf.arrays_zip(df.nums, df.letters, df.bools)).show(truncate=False)
+--------------------------------+
|arrays_zip(nums, letters, bools)|
+--------------------------------+
|[{1, a, true}, {2, b, false}]   |
+--------------------------------+

```


Example 4: Zipping arrays with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, None], ['a', None, 'c'])], ['nums', 'letters'])
>>> df.select(sf.arrays_zip(df.nums, df.letters)).show(truncate=False)
+------------------------------+
|arrays_zip(nums, letters)     |
+------------------------------+
|[{1, a}, {2, NULL}, {NULL, c}]|
+------------------------------+

```


# pyspark.sql.functions.flatten — PySpark 4.0.1 documentation
pyspark.sql.functions.flatten(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#flatten)
[#](#pyspark.sql.functions.flatten "Permalink to this definition")

Array function: creates a single array from an array of arrays. If a structure of nested arrays is deeper than two levels, only one level of nesting is removed.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or expression to be flattened.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains the flattened array.

Examples

Example 1: Flattening a simple nested array

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([[1, 2, 3], [4, 5], [6]],)], ['data'])
>>> df.select(sf.flatten(df.data)).show()
+------------------+
|     flatten(data)|
+------------------+
|[1, 2, 3, 4, 5, 6]|
+------------------+

```


Example 2: Flattening an array with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([None, [4, 5]],)], ['data'])
>>> df.select(sf.flatten(df.data)).show()
+-------------+
|flatten(data)|
+-------------+
|         NULL|
+-------------+

```


Example 3: Flattening an array with more than two levels of nesting

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([[[1, 2], [3, 4]], [[5, 6], [7, 8]]],)], ['data'])
>>> df.select(sf.flatten(df.data)).show(truncate=False)
+--------------------------------+
|flatten(data)                   |
+--------------------------------+
|[[1, 2], [3, 4], [5, 6], [7, 8]]|
+--------------------------------+

```


Example 4: Flattening an array with mixed types

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([['a', 'b', 'c'], [1, 2, 3]],)], ['data'])
>>> df.select(sf.flatten(df.data)).show()
+------------------+
|     flatten(data)|
+------------------+
|[a, b, c, 1, 2, 3]|
+------------------+

```


# pyspark.sql.functions.get — PySpark 4.0.1 documentation
pyspark.sql.functions.get(_col_, _index_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#get)
[#](#pyspark.sql.functions.get "Permalink to this definition")

Array function: Returns the element of an array at the given (0-based) index. If the index points outside of the array boundaries, then this function returns NULL.

New in version 3.4.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of the column containing the array.

**index**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str or int

Index to check for in the array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Value at the given position.

Notes

The position is not 1-based, but 0-based index. Supports Spark Connect.

Examples

Example 1: Getting an element at a fixed position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.get(df.data, 1)).show()
+------------+
|get(data, 1)|
+------------+
|           b|
+------------+

```


Example 2: Getting an element at a position outside the array boundaries

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"],)], ['data'])
>>> df.select(sf.get(df.data, 3)).show()
+------------+
|get(data, 3)|
+------------+
|        NULL|
+------------+

```


Example 3: Getting an element at a position specified by another column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"], 2)], ['data', 'index'])
>>> df.select(sf.get(df.data, df.index)).show()
+----------------+
|get(data, index)|
+----------------+
|               c|
+----------------+

```


Example 4: Getting an element at a position calculated from another column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"], 2)], ['data', 'index'])
>>> df.select(sf.get(df.data, df.index - 1)).show()
+----------------------+
|get(data, (index - 1))|
+----------------------+
|                     b|
+----------------------+

```


Example 5: Getting an element at a negative position

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(["a", "b", "c"], )], ['data'])
>>> df.select(sf.get(df.data, -1)).show()
+-------------+
|get(data, -1)|
+-------------+
|         NULL|
+-------------+

```


# pyspark.sql.functions.sequence — PySpark 4.0.1 documentation
pyspark.sql.functions.sequence(_start_, _stop_, _step\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sequence)
[#](#pyspark.sql.functions.sequence "Permalink to this definition")

Array function: Generate a sequence of integers from start to stop, incrementing by step. If step is not set, the function increments by 1 if start is less than or equal to stop, otherwise it decrements by 1.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The starting value (inclusive) of the sequence.

**stop**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The last value (inclusive) of the sequence.

**step**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

The value to add to the current element to get the next element in the sequence. The default is 1 if start is less than or equal to stop, otherwise -1.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains an array of sequence values.

Examples

Example 1: Generating a sequence with default step

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(-2, 2)], ['start', 'stop'])
>>> df.select(sf.sequence(df.start, df.stop)).show()
+---------------------+
|sequence(start, stop)|
+---------------------+
|    [-2, -1, 0, 1, 2]|
+---------------------+

```


Example 2: Generating a sequence with a custom step

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(4, -4, -2)], ['start', 'stop', 'step'])
>>> df.select(sf.sequence(df.start, df.stop, df.step)).show()
+---------------------------+
|sequence(start, stop, step)|
+---------------------------+
|          [4, 2, 0, -2, -4]|
+---------------------------+

```


Example 3: Generating a sequence with a negative step

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(5, 1, -1)], ['start', 'stop', 'step'])
>>> df.select(sf.sequence(df.start, df.stop, df.step)).show()
+---------------------------+
|sequence(start, stop, step)|
+---------------------------+
|            [5, 4, 3, 2, 1]|
+---------------------------+

```


# pyspark.sql.functions.shuffle — PySpark 4.0.1 documentation
pyspark.sql.functions.shuffle(_col_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#shuffle)
[#](#pyspark.sql.functions.shuffle "Permalink to this definition")

Array function: Generates a random permutation of the given array.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or expression to be shuffled.

**seed**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

Seed value for the random generator.

New in version 4.0.0.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains an array of elements in random order.

Notes

The shuffle function is non-deterministic, meaning the order of the output array can be different for each execution.

Examples

Example 1: Shuffling a simple array

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT ARRAY(1, 20, 3, 5) AS data")
>>> df.select("*", sf.shuffle(df.data, sf.lit(123))).show()
+-------------+-------------+
|         data|shuffle(data)|
+-------------+-------------+
|[1, 20, 3, 5]|[5, 1, 20, 3]|
+-------------+-------------+

```


Example 2: Shuffling an array with null values

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT ARRAY(1, 20, NULL, 5) AS data")
>>> df.select("*", sf.shuffle(sf.col("data"), 234)).show()
+----------------+----------------+
|            data|   shuffle(data)|
+----------------+----------------+
|[1, 20, NULL, 5]|[NULL, 5, 20, 1]|
+----------------+----------------+

```


Example 3: Shuffling an array with duplicate values

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT ARRAY(1, 2, 2, 3, 3, 3) AS data")
>>> df.select("*", sf.shuffle("data", 345)).show()
+------------------+------------------+
|              data|     shuffle(data)|
+------------------+------------------+
|[1, 2, 2, 3, 3, 3]|[2, 3, 3, 1, 2, 3]|
+------------------+------------------+

```


Example 4: Shuffling an array with random seed

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT ARRAY(1, 2, 2, 3, 3, 3) AS data")
>>> df.select("*", sf.shuffle("data")).show() 
+------------------+------------------+
|              data|     shuffle(data)|
+------------------+------------------+
|[1, 2, 2, 3, 3, 3]|[3, 3, 2, 3, 2, 1]|
+------------------+------------------+

```

# pyspark.sql.functions.slice — PySpark 4.0.1 documentation
pyspark.sql.functions.slice(_x_, _start_, _length_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#slice)
[#](#pyspark.sql.functions.slice "Permalink to this definition")

Array function: Returns a new array column by slicing the input array column from a start index to a specific length. The indices start at 1, and can be negative to index from the end of the array. The length specifies the number of elements in the resulting array.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input array column or column name to be sliced.

**start**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), str, or int

The start index for the slice operation. If negative, starts the index from the end of the array.

**length**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), str, or int

The length of the slice, representing number of elements in the resulting array.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column object of Array type, where each value is a slice of the corresponding list from the input column.

Examples

Example 1: Basic usage of the slice function.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],), ([4, 5],)], ['x'])
>>> df.select(sf.slice(df.x, 2, 2)).show()
+--------------+
|slice(x, 2, 2)|
+--------------+
|        [2, 3]|
|           [5]|
+--------------+

```


Example 2: Slicing with negative start index.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3],), ([4, 5],)], ['x'])
>>> df.select(sf.slice(df.x, -1, 1)).show()
+---------------+
|slice(x, -1, 1)|
+---------------+
|            [3]|
|            [5]|
+---------------+

```


Example 3: Slice function with column inputs for start and length.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2, 3], 2, 2), ([4, 5], 1, 3)], ['x', 'start', 'length'])
>>> df.select(sf.slice(df.x, df.start, df.length)).show()
+-----------------------+
|slice(x, start, length)|
+-----------------------+
|                 [2, 3]|
|                 [4, 5]|
+-----------------------+

```


# pyspark.sql.functions.sort_array — PySpark 4.0.1 documentation
pyspark.sql.functions.sort\_array(_col_, _asc\=True_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sort_array)
[#](#pyspark.sql.functions.sort_array "Permalink to this definition")

Array function: Sorts the input array in ascending or descending order according to the natural ordering of the array elements. Null elements will be placed at the beginning of the returned array in ascending order or at the end of the returned array in descending order.

New in version 1.5.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of the column or expression.

**asc**bool, optional

Whether to sort in ascending or descending order. If asc is True (default), then the sorting is in ascending order. If False, then in descending order.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Sorted array.

Examples

Example 1: Sorting an array in ascending order

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([([2, 1, None, 3],)], ['data'])
>>> df.select(sf.sort_array(df.data)).show()
+----------------------+
|sort_array(data, true)|
+----------------------+
|       [NULL, 1, 2, 3]|
+----------------------+

```


Example 2: Sorting an array in descending order

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([([2, 1, None, 3],)], ['data'])
>>> df.select(sf.sort_array(df.data, asc=False)).show()
+-----------------------+
|sort_array(data, false)|
+-----------------------+
|        [3, 2, 1, NULL]|
+-----------------------+

```


Example 3: Sorting an array with a single element

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([([1],)], ['data'])
>>> df.select(sf.sort_array(df.data)).show()
+----------------------+
|sort_array(data, true)|
+----------------------+
|                   [1]|
+----------------------+

```


Example 4: Sorting an empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, StructField, StructType
>>> schema = StructType([StructField("data", ArrayType(StringType()), True)])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.sort_array(df.data)).show()
+----------------------+
|sort_array(data, true)|
+----------------------+
|                    []|
+----------------------+

```


Example 5: Sorting an array with null values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType, StructType, StructField
>>> schema = StructType([StructField("data", ArrayType(IntegerType()), True)])
>>> df = spark.createDataFrame([([None, None, None],)], schema=schema)
>>> df.select(sf.sort_array(df.data)).show()
+----------------------+
|sort_array(data, true)|
+----------------------+
|    [NULL, NULL, NULL]|
+----------------------+

```



# pyspark.sql.functions.named_struct — PySpark 4.0.1 documentation
pyspark.sql.functions.named\_struct(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#named_struct)
[#](#pyspark.sql.functions.named_struct "Permalink to this definition")

Creates a struct with the given field names and values.

New in version 3.5.0.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

list of columns to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, 2)], ['a', 'b'])
>>> df.select("*", sf.named_struct(sf.lit('x'), df.a, sf.lit('y'), "b")).show()
+---+---+------------------------+
|  a|  b|named_struct(x, a, y, b)|
+---+---+------------------------+
|  1|  2|                  {1, 2}|
+---+---+------------------------+

```



# pyspark.sql.functions.struct — PySpark 4.0.1 documentation
pyspark.sql.functions.struct(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#struct)
[#](#pyspark.sql.functions.struct "Permalink to this definition")

Creates a new struct column.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**list, set, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")s to contain in the output struct.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a struct type column of given columns.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5)], ("name", "age"))
>>> df.select("*", sf.struct('age', df.name)).show()
+-----+---+-----------------+
| name|age|struct(age, name)|
+-----+---+-----------------+
|Alice|  2|       {2, Alice}|
|  Bob|  5|         {5, Bob}|
+-----+---+-----------------+

```



# pyspark.sql.functions.create_map — PySpark 4.0.1 documentation
pyspark.sql.functions.create\_map(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#create_map)
[#](#pyspark.sql.functions.create_map "Permalink to this definition")

Map function: Creates a new map column from an even number of input columns or column references. The input columns are grouped into key-value pairs to form a map. For instance, the input (key1, value1, key2, value2, …) would produce a map that associates key1 with value1, key2 with value2, and so on. The function supports grouping columns as a list as well.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The input column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") objects grouped into key-value pairs. These can also be expressed as a list of columns.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column of Map type, where each value is a map formed from the corresponding key-value pairs provided in the input arguments.

Examples

Example 1: Basic usage of create\_map function.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5)], ("name", "age"))
>>> df.select(sf.create_map('name', 'age')).show()
+--------------+
|map(name, age)|
+--------------+
|  {Alice -> 2}|
|    {Bob -> 5}|
+--------------+

```


Example 2: Usage of create\_map function with a list of columns.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5)], ("name", "age"))
>>> df.select(sf.create_map([df.name, df.age])).show()
+--------------+
|map(name, age)|
+--------------+
|  {Alice -> 2}|
|    {Bob -> 5}|
+--------------+

```


Example 3: Usage of create\_map function with more than one key-value pair.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", 2, "female"),
...     ("Bob", 5, "male")], ("name", "age", "gender"))
>>> df.select(sf.create_map(sf.lit('name'), df['name'],
...     sf.lit('gender'), df['gender'])).show(truncate=False)
+---------------------------------+
|map(name, name, gender, gender)  |
+---------------------------------+
|{name -> Alice, gender -> female}|
|{name -> Bob, gender -> male}    |
+---------------------------------+

```


Example 4: Usage of create\_map function with values of different types.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", 2, 22.2),
...     ("Bob", 5, 36.1)], ("name", "age", "weight"))
>>> df.select(sf.create_map(sf.lit('age'), df['age'],
...     sf.lit('weight'), df['weight'])).show(truncate=False)
+-----------------------------+
|map(age, age, weight, weight)|
+-----------------------------+
|{age -> 2.0, weight -> 22.2} |
|{age -> 5.0, weight -> 36.1} |
+-----------------------------+

```

# pyspark.sql.functions.map_concat — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_concat(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_concat)
[#](#pyspark.sql.functions.map_concat "Permalink to this definition")

Map function: Returns the union of all given maps.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A map of merged entries from other maps.

Notes

For duplicate keys in input maps, the handling is governed by spark.sql.mapKeyDedupPolicy. By default, it throws an exception. If set to LAST\_WIN, it uses the last map’s value.

Examples

Example 1: Basic usage of map\_concat

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as map1, map(3, 'c') as map2")
>>> df.select(sf.map_concat("map1", "map2")).show(truncate=False)
+------------------------+
|map_concat(map1, map2)  |
+------------------------+
|{1 -> a, 2 -> b, 3 -> c}|
+------------------------+

```


Example 2: map\_concat with overlapping keys

```
>>> from pyspark.sql import functions as sf
>>> originalmapKeyDedupPolicy = spark.conf.get("spark.sql.mapKeyDedupPolicy")
>>> spark.conf.set("spark.sql.mapKeyDedupPolicy", "LAST_WIN")
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as map1, map(2, 'c', 3, 'd') as map2")
>>> df.select(sf.map_concat("map1", "map2")).show(truncate=False)
+------------------------+
|map_concat(map1, map2)  |
+------------------------+
|{1 -> a, 2 -> c, 3 -> d}|
+------------------------+
>>> spark.conf.set("spark.sql.mapKeyDedupPolicy", originalmapKeyDedupPolicy)

```


Example 3: map\_concat with three maps

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a') as map1, map(2, 'b') as map2, map(3, 'c') as map3")
>>> df.select(sf.map_concat("map1", "map2", "map3")).show(truncate=False)
+----------------------------+
|map_concat(map1, map2, map3)|
+----------------------------+
|{1 -> a, 2 -> b, 3 -> c}    |
+----------------------------+

```


Example 4: map\_concat with empty map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as map1, map() as map2")
>>> df.select(sf.map_concat("map1", "map2")).show(truncate=False)
+----------------------+
|map_concat(map1, map2)|
+----------------------+
|{1 -> a, 2 -> b}      |
+----------------------+

```


Example 5: map\_concat with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as map1, map(3, null) as map2")
>>> df.select(sf.map_concat("map1", "map2")).show(truncate=False)
+---------------------------+
|map_concat(map1, map2)     |
+---------------------------+
|{1 -> a, 2 -> b, 3 -> NULL}|
+---------------------------+

```


# pyspark.sql.functions.map_contains_key — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_contains\_key(_col_, _value_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_contains_key)
[#](#pyspark.sql.functions.map_contains_key "Permalink to this definition")

Map function: Returns true if the map contains the key.

New in version 3.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

The name of the column or an expression that represents the map.

**value**

A literal value, or a [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") expression.

Changed in version 4.0.0: value now also accepts a Column type.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

True if key is in the map and False otherwise.

Examples

Example 1: The key is in the map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as data")
>>> df.select(sf.map_contains_key("data", 1)).show()
+-------------------------+
|map_contains_key(data, 1)|
+-------------------------+
|                     true|
+-------------------------+

```


Example 2: The key is not in the map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as data")
>>> df.select(sf.map_contains_key("data", -1)).show()
+--------------------------+
|map_contains_key(data, -1)|
+--------------------------+
|                     false|
+--------------------------+

```


Example 3: Check for key using a column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as data, 1 as key")
>>> df.select(sf.map_contains_key("data", sf.col("key"))).show()
+---------------------------+
|map_contains_key(data, key)|
+---------------------------+
|                       true|
+---------------------------+

```


# pyspark.sql.functions.map_entries — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_entries(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_entries)
[#](#pyspark.sql.functions.map_entries "Permalink to this definition")

Map function: Returns an unordered array of all entries in the given map.

New in version 3.0.0.

Changed in version 3.4.0: Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

An array of key value pairs as a struct type

Examples

Example 1: Extracting entries from a simple map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as data")
>>> df.select(sf.sort_array(sf.map_entries("data"))).show()
+-----------------------------------+
|sort_array(map_entries(data), true)|
+-----------------------------------+
|                   [{1, a}, {2, b}]|
+-----------------------------------+

```


Example 2: Extracting entries from a map with complex keys and values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(array(1, 2), array('a', 'b'), "
...   "array(3, 4), array('c', 'd')) as data")
>>> df.select(sf.sort_array(sf.map_entries("data"))).show(truncate=False)
+------------------------------------+
|sort_array(map_entries(data), true) |
+------------------------------------+
|[{[1, 2], [a, b]}, {[3, 4], [c, d]}]|
+------------------------------------+

```


Example 3: Extracting entries from a map with duplicate keys

```
>>> from pyspark.sql import functions as sf
>>> originalmapKeyDedupPolicy = spark.conf.get("spark.sql.mapKeyDedupPolicy")
>>> spark.conf.set("spark.sql.mapKeyDedupPolicy", "LAST_WIN")
>>> df = spark.sql("SELECT map(1, 'a', 1, 'b') as data")
>>> df.select(sf.map_entries("data")).show()
+-----------------+
|map_entries(data)|
+-----------------+
|         [{1, b}]|
+-----------------+
>>> spark.conf.set("spark.sql.mapKeyDedupPolicy", originalmapKeyDedupPolicy)

```


Example 4: Extracting entries from an empty map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map() as data")
>>> df.select(sf.map_entries("data")).show()
+-----------------+
|map_entries(data)|
+-----------------+
|               []|
+-----------------+

```


# pyspark.sql.functions.map_from_arrays — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_from\_arrays(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_from_arrays)
[#](#pyspark.sql.functions.map_from_arrays "Permalink to this definition")

Map function: Creates a new map from two arrays. This function takes two arrays of keys and values respectively, and returns a new map column. .. versionadded:: 2.4.0

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing a set of keys. All elements should not be null.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing a set of values.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column of map type.

Notes

The input arrays for keys and values must have the same length and all elements in keys should not be null. If these conditions are not met, an exception will be thrown.

Examples

Example 1: Basic usage of map\_from\_arrays

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([2, 5], ['a', 'b'])], ['k', 'v'])
>>> df.select(sf.map_from_arrays(df.k, df.v)).show()
+---------------------+
|map_from_arrays(k, v)|
+---------------------+
|     {2 -> a, 5 -> b}|
+---------------------+

```


Example 2: map\_from\_arrays with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([([1, 2], ['a', None])], ['k', 'v'])
>>> df.select(sf.map_from_arrays(df.k, df.v)).show()
+---------------------+
|map_from_arrays(k, v)|
+---------------------+
|  {1 -> a, 2 -> NULL}|
+---------------------+

```


Example 3: map\_from\_arrays with empty arrays

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField('k', ArrayType(IntegerType())),
...   StructField('v', ArrayType(StringType()))
... ])
>>> df = spark.createDataFrame([([], [])], schema=schema)
>>> df.select(sf.map_from_arrays(df.k, df.v)).show()
+---------------------+
|map_from_arrays(k, v)|
+---------------------+
|                   {}|
+---------------------+

```


# pyspark.sql.functions.map_from_entries — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_from\_entries(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_from_entries)
[#](#pyspark.sql.functions.map_from_entries "Permalink to this definition")

Map function: Transforms an array of key-value pair entries (structs with two fields) into a map. The first field of each entry is used as the key and the second field as the value in the resulting map column

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A map created from the given array of entries.

Examples

Example 1: Basic usage of map\_from\_entries

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT array(struct(1, 'a'), struct(2, 'b')) as data")
>>> df.select(sf.map_from_entries(df.data)).show()
+----------------------+
|map_from_entries(data)|
+----------------------+
|      {1 -> a, 2 -> b}|
+----------------------+

```


Example 2: map\_from\_entries with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT array(struct(1, null), struct(2, 'b')) as data")
>>> df.select(sf.map_from_entries(df.data)).show()
+----------------------+
|map_from_entries(data)|
+----------------------+
|   {1 -> NULL, 2 -> b}|
+----------------------+

```


Example 3: map\_from\_entries with a DataFrame

```
>>> from pyspark.sql import Row, functions as sf
>>> df = spark.createDataFrame([([Row(1, "a"), Row(2, "b")],), ([Row(3, "c")],)], ['data'])
>>> df.select(sf.map_from_entries(df.data)).show()
+----------------------+
|map_from_entries(data)|
+----------------------+
|      {1 -> a, 2 -> b}|
|              {3 -> c}|
+----------------------+

```


Example 4: map\_from\_entries with empty array

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StringType, IntegerType, StructType, StructField
>>> schema = StructType([
...   StructField("data", ArrayType(
...     StructType([
...       StructField("key", IntegerType()),
...       StructField("value", StringType())
...     ])
...   ), True)
... ])
>>> df = spark.createDataFrame([([],)], schema=schema)
>>> df.select(sf.map_from_entries(df.data)).show()
+----------------------+
|map_from_entries(data)|
+----------------------+
|                    {}|
+----------------------+

```

# pyspark.sql.functions.map_keys — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_keys(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_keys)
[#](#pyspark.sql.functions.map_keys "Permalink to this definition")

Map function: Returns an unordered array containing the keys of the map.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Keys of the map as an array.

Examples

Example 1: Extracting keys from a simple map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as data")
>>> df.select(sf.sort_array(sf.map_keys("data"))).show()
+--------------------------------+
|sort_array(map_keys(data), true)|
+--------------------------------+
|                          [1, 2]|
+--------------------------------+

```


Example 2: Extracting keys from a map with complex keys

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(array(1, 2), 'a', array(3, 4), 'b') as data")
>>> df.select(sf.sort_array(sf.map_keys("data"))).show()
+--------------------------------+
|sort_array(map_keys(data), true)|
+--------------------------------+
|                [[1, 2], [3, 4]]|
+--------------------------------+

```


Example 3: Extracting keys from a map with duplicate keys

```
>>> from pyspark.sql import functions as sf
>>> originalmapKeyDedupPolicy = spark.conf.get("spark.sql.mapKeyDedupPolicy")
>>> spark.conf.set("spark.sql.mapKeyDedupPolicy", "LAST_WIN")
>>> df = spark.sql("SELECT map(1, 'a', 1, 'b') as data")
>>> df.select(sf.map_keys("data")).show()
+--------------+
|map_keys(data)|
+--------------+
|           [1]|
+--------------+
>>> spark.conf.set("spark.sql.mapKeyDedupPolicy", originalmapKeyDedupPolicy)

```


Example 4: Extracting keys from an empty map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map() as data")
>>> df.select(sf.map_keys("data")).show()
+--------------+
|map_keys(data)|
+--------------+
|            []|
+--------------+

```

# pyspark.sql.functions.map_values — PySpark 4.0.1 documentation
pyspark.sql.functions.map\_values(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#map_values)
[#](#pyspark.sql.functions.map_values "Permalink to this definition")

Map function: Returns an unordered array containing the values of the map.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column or expression

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Values of the map as an array.

Examples

Example 1: Extracting values from a simple map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'b') as data")
>>> df.select(sf.sort_array(sf.map_values("data"))).show()
+----------------------------------+
|sort_array(map_values(data), true)|
+----------------------------------+
|                            [a, b]|
+----------------------------------+

```


Example 2: Extracting values from a map with complex values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, array('a', 'b'), 2, array('c', 'd')) as data")
>>> df.select(sf.sort_array(sf.map_values("data"))).show()
+----------------------------------+
|sort_array(map_values(data), true)|
+----------------------------------+
|                  [[a, b], [c, d]]|
+----------------------------------+

```


Example 3: Extracting values from a map with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, null, 2, 'b') as data")
>>> df.select(sf.sort_array(sf.map_values("data"))).show()
+----------------------------------+
|sort_array(map_values(data), true)|
+----------------------------------+
|                         [NULL, b]|
+----------------------------------+

```


Example 4: Extracting values from a map with duplicate values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map(1, 'a', 2, 'a') as data")
>>> df.select(sf.map_values("data")).show()
+----------------+
|map_values(data)|
+----------------+
|          [a, a]|
+----------------+

```


Example 5: Extracting values from an empty map

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT map() as data")
>>> df.select(sf.map_values("data")).show()
+----------------+
|map_values(data)|
+----------------+
|              []|
+----------------+

```


# pyspark.sql.functions.str_to_map — PySpark 4.0.1 documentation
pyspark.sql.functions.str\_to\_map(_text_, _pairDelim\=None_, _keyValueDelim\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#str_to_map)
[#](#pyspark.sql.functions.str_to_map "Permalink to this definition")

Map function: Converts a string into a map after splitting the text into key/value pairs using delimiters. Both pairDelim and keyValueDelim are treated as regular expressions.

New in version 3.5.0.

Parameters

**text**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Input column or strings.

**pairDelim**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

Delimiter to use to split pairs. Default is comma (,).

**keyValueDelim**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

Delimiter to use to split key/value. Default is colon (:).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of map type where each string in the original column is converted into a map.

Examples

Example 1: Using default delimiters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a:1,b:2,c:3",)], ["e"])
>>> df.select(sf.str_to_map(df.e)).show(truncate=False)
+------------------------+
|str_to_map(e, ,, :)     |
+------------------------+
|{a -> 1, b -> 2, c -> 3}|
+------------------------+

```


Example 2: Using custom delimiters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a=1;b=2;c=3",)], ["e"])
>>> df.select(sf.str_to_map(df.e, sf.lit(";"), sf.lit("="))).show(truncate=False)
+------------------------+
|str_to_map(e, ;, =)     |
+------------------------+
|{a -> 1, b -> 2, c -> 3}|
+------------------------+

```


Example 3: Using different delimiters for different rows

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a:1,b:2,c:3",), ("d=4;e=5;f=6",)], ["e"])
>>> df.select(sf.str_to_map(df.e,
...   sf.when(df.e.contains(";"), sf.lit(";")).otherwise(sf.lit(",")),
...   sf.when(df.e.contains("="), sf.lit("=")).otherwise(sf.lit(":"))).alias("str_to_map")
... ).show(truncate=False)
+------------------------+
|str_to_map              |
+------------------------+
|{a -> 1, b -> 2, c -> 3}|
|{d -> 4, e -> 5, f -> 6}|
+------------------------+

```


Example 4: Using a column of delimiters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a:1,b:2,c:3", ","), ("d=4;e=5;f=6", ";")], ["e", "delim"])
>>> df.select(sf.str_to_map(df.e, df.delim, sf.lit(":"))).show(truncate=False)
+---------------------------------------+
|str_to_map(e, delim, :)                |
+---------------------------------------+
|{a -> 1, b -> 2, c -> 3}               |
|{d=4 -> NULL, e=5 -> NULL, f=6 -> NULL}|
+---------------------------------------+

```


Example 5: Using a column of key/value delimiters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a:1,b:2,c:3", ":"), ("d=4;e=5;f=6", "=")], ["e", "delim"])
>>> df.select(sf.str_to_map(df.e, sf.lit(","), df.delim)).show(truncate=False)
+------------------------+
|str_to_map(e, ,, delim) |
+------------------------+
|{a -> 1, b -> 2, c -> 3}|
|{d -> 4;e=5;f=6}        |
+------------------------+

```
# pyspark.sql.functions.any_value — PySpark 4.0.1 documentation
pyspark.sql.functions.any\_value(_col_, _ignoreNulls\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#any_value)
[#](#pyspark.sql.functions.any_value "Permalink to this definition")

Returns some value of col for a group of rows.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**ignoreNulls**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or bool, optional

if first value is null then look for first non-null value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

some value of col for a group of rows.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(None, 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["c1", "c2"])
>>> df.select(sf.any_value('c1'), sf.any_value('c2')).show()
+-------------+-------------+
|any_value(c1)|any_value(c2)|
+-------------+-------------+
|         NULL|            1|
+-------------+-------------+

```


```
>>> df.select(sf.any_value('c1', True), sf.any_value('c2', True)).show()
+-------------+-------------+
|any_value(c1)|any_value(c2)|
+-------------+-------------+
|            a|            1|
+-------------+-------------+

```


# pyspark.sql.functions.approx_count_distinct — PySpark 4.0.1 documentation
pyspark.sql.functions.approx\_count\_distinct(_col_, _rsd\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#approx_count_distinct)
[#](#pyspark.sql.functions.approx_count_distinct "Permalink to this definition")

This aggregate function returns a new [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), which estimates the approximate distinct count of elements in a specified column or a group of columns.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The label of the column to count distinct values in.

**rsd**float, optional

The maximum allowed relative standard deviation (default = 0.05). If rsd < 0.01, it would be more efficient to use [`count_distinct()`](about:blank/pyspark.sql.functions.count_distinct.html#pyspark.sql.functions.count_distinct "pyspark.sql.functions.count_distinct").

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column object representing the approximate unique count.

Examples

Example 1: Counting distinct values in a single column DataFrame representing integers

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([1,2,2,3], "int")
>>> df.agg(sf.approx_count_distinct("value")).show()
+----------------------------+
|approx_count_distinct(value)|
+----------------------------+
|                           3|
+----------------------------+

```


Example 2: Counting distinct values in a single column DataFrame representing strings

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("apple",), ("orange",), ("apple",), ("banana",)], ['fruit'])
>>> df.agg(sf.approx_count_distinct("fruit")).show()
+----------------------------+
|approx_count_distinct(fruit)|
+----------------------------+
|                           3|
+----------------------------+

```


Example 3: Counting distinct values in a DataFrame with multiple columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [("Alice", 1), ("Alice", 2), ("Bob", 3), ("Bob", 3)], ["name", "value"])
>>> df = df.withColumn("combined", sf.struct("name", "value"))
>>> df.agg(sf.approx_count_distinct(df.combined)).show()
+-------------------------------+
|approx_count_distinct(combined)|
+-------------------------------+
|                              3|
+-------------------------------+

```


Example 4: Counting distinct values with a specified relative standard deviation

```
>>> from pyspark.sql import functions as sf
>>> spark.range(100000).agg(
...     sf.approx_count_distinct("id").alias('with_default_rsd'),
...     sf.approx_count_distinct("id", 0.1).alias('with_rsd_0.1')
... ).show()
+----------------+------------+
|with_default_rsd|with_rsd_0.1|
+----------------+------------+
|           95546|      102065|
+----------------+------------+

```


# pyspark.sql.functions.approx_percentile — PySpark 4.0.1 documentation
pyspark.sql.functions.approx\_percentile(_col_, _percentage_, _accuracy\=10000_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#approx_percentile)
[#](#pyspark.sql.functions.approx_percentile "Permalink to this definition")

Returns the approximate percentile of the numeric column col which is the smallest value in the ordered col values (sorted from least to greatest) such that no more than percentage of col values is less than the value or equal to that value.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column.

**percentage**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), float, list of floats or tuple of floats

percentage in decimal (must be between 0.0 and 1.0). When percentage is an array, each value of the percentage array must be between 0.0 and 1.0. In this case, returns the approximate percentile array of column col at the given percentage array.

**accuracy**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

is a positive numeric literal which controls approximation accuracy at the cost of memory. Higher value of accuracy yields better accuracy, 1.0/accuracy is the relative error of the approximation. (default: 10000).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

approximate percentile of the numeric column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> key = (sf.col("id") % 3).alias("key")
>>> value = (sf.randn(42) + key * 10).alias("value")
>>> df = spark.range(0, 1000, 1, 1).select(key, value)
>>> df.select(
...     sf.approx_percentile("value", [0.25, 0.5, 0.75], 1000000)
... ).show(truncate=False)
+----------------------------------------------------------+
|approx_percentile(value, array(0.25, 0.5, 0.75), 1000000) |
+----------------------------------------------------------+
|[0.7264430125286..., 9.98975299938..., 19.335304783039...]|
+----------------------------------------------------------+

```


```
>>> df.groupBy("key").agg(
...     sf.approx_percentile("value", sf.lit(0.5), sf.lit(1000000))
... ).sort("key").show()
+---+--------------------------------------+
|key|approx_percentile(value, 0.5, 1000000)|
+---+--------------------------------------+
|  0|                  -0.03519435193070...|
|  1|                     9.990389751837...|
|  2|                    19.967859769284...|
+---+--------------------------------------+

```


# pyspark.sql.functions.array_agg — PySpark 4.0.1 documentation
pyspark.sql.functions.array\_agg(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#array_agg)
[#](#pyspark.sql.functions.array_agg "Permalink to this definition")

Aggregate function: returns a list of objects with duplicates.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

list of objects with duplicates.

Examples

Example 1: Using array\_agg function on an int column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[1],[2]], ["c"])
>>> df.agg(sf.sort_array(sf.array_agg('c')).alias('sorted_list')).show()
+-----------+
|sorted_list|
+-----------+
|  [1, 1, 2]|
+-----------+

```


Example 2: Using array\_agg function on a string column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([["apple"],["apple"],["banana"]], ["c"])
>>> df.agg(sf.sort_array(sf.array_agg('c')).alias('sorted_list')).show(truncate=False)
+----------------------+
|sorted_list           |
+----------------------+
|[apple, apple, banana]|
+----------------------+

```


Example 3: Using array\_agg function on a column with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[None],[2]], ["c"])
>>> df.agg(sf.sort_array(sf.array_agg('c')).alias('sorted_list')).show()
+-----------+
|sorted_list|
+-----------+
|     [1, 2]|
+-----------+

```


Example 4: Using array\_agg function on a column with different data types

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],["apple"],[2]], ["c"])
>>> df.agg(sf.sort_array(sf.array_agg('c')).alias('sorted_list')).show()
+-------------+
|  sorted_list|
+-------------+
|[1, 2, apple]|
+-------------+

```


# pyspark.sql.functions.avg — PySpark 4.0.1 documentation
pyspark.sql.functions.avg(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#avg)
[#](#pyspark.sql.functions.avg "Permalink to this definition")

Aggregate function: returns the average of the values in a group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Calculating the average age

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, 15), (1990, 2)], ["birth", "age"])
>>> df.select(sf.avg("age")).show()
+--------+
|avg(age)|
+--------+
|     8.5|
+--------+

```


Example 2: Calculating the average age with None

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, None), (1990, 2), (2000, 4)], ["birth", "age"])
>>> df.select(sf.avg("age")).show()
+--------+
|avg(age)|
+--------+
|     3.0|
+--------+

```


# pyspark.sql.functions.bit_and — PySpark 4.0.1 documentation
pyspark.sql.functions.bit\_and(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bit_and)
[#](#pyspark.sql.functions.bit_and "Permalink to this definition")

Aggregate function: returns the bitwise AND of all non-null input values, or null if none.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the bitwise AND of all non-null input values, or null if none.

Examples

Example 1: Bitwise AND with all non-null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[1],[2]], ["c"])
>>> df.select(sf.bit_and("c")).show()
+----------+
|bit_and(c)|
+----------+
|         0|
+----------+

```


Example 2: Bitwise AND with null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[None],[2]], ["c"])
>>> df.select(sf.bit_and("c")).show()
+----------+
|bit_and(c)|
+----------+
|         0|
+----------+

```


Example 3: Bitwise AND with all null values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import IntegerType, StructType, StructField
>>> schema = StructType([StructField("c", IntegerType(), True)])
>>> df = spark.createDataFrame([[None],[None],[None]], schema=schema)
>>> df.select(sf.bit_and("c")).show()
+----------+
|bit_and(c)|
+----------+
|      NULL|
+----------+

```


Example 4: Bitwise AND with single input value

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[5]], ["c"])
>>> df.select(sf.bit_and("c")).show()
+----------+
|bit_and(c)|
+----------+
|         5|
+----------+

```

# pyspark.sql.functions.bit_or — PySpark 4.0.1 documentation
pyspark.sql.functions.bit\_or(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bit_or)
[#](#pyspark.sql.functions.bit_or "Permalink to this definition")

Aggregate function: returns the bitwise OR of all non-null input values, or null if none.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the bitwise OR of all non-null input values, or null if none.

Examples

Example 1: Bitwise OR with all non-null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[1],[2]], ["c"])
>>> df.select(sf.bit_or("c")).show()
+---------+
|bit_or(c)|
+---------+
|        3|
+---------+

```


Example 2: Bitwise OR with some null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[None],[2]], ["c"])
>>> df.select(sf.bit_or("c")).show()
+---------+
|bit_or(c)|
+---------+
|        3|
+---------+

```


Example 3: Bitwise OR with all null values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import IntegerType, StructType, StructField
>>> schema = StructType([StructField("c", IntegerType(), True)])
>>> df = spark.createDataFrame([[None],[None],[None]], schema=schema)
>>> df.select(sf.bit_or("c")).show()
+---------+
|bit_or(c)|
+---------+
|     NULL|
+---------+

```


Example 4: Bitwise OR with single input value

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[5]], ["c"])
>>> df.select(sf.bit_or("c")).show()
+---------+
|bit_or(c)|
+---------+
|        5|
+---------+

```


# pyspark.sql.functions.bit_xor — PySpark 4.0.1 documentation
pyspark.sql.functions.bit\_xor(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bit_xor)
[#](#pyspark.sql.functions.bit_xor "Permalink to this definition")

Aggregate function: returns the bitwise XOR of all non-null input values, or null if none.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the bitwise XOR of all non-null input values, or null if none.

Examples

Example 1: Bitwise XOR with all non-null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[1],[2]], ["c"])
>>> df.select(sf.bit_xor("c")).show()
+----------+
|bit_xor(c)|
+----------+
|         2|
+----------+

```


Example 2: Bitwise XOR with some null values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[None],[2]], ["c"])
>>> df.select(sf.bit_xor("c")).show()
+----------+
|bit_xor(c)|
+----------+
|         3|
+----------+

```


Example 3: Bitwise XOR with all null values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import IntegerType, StructType, StructField
>>> schema = StructType([StructField("c", IntegerType(), True)])
>>> df = spark.createDataFrame([[None],[None],[None]], schema=schema)
>>> df.select(sf.bit_xor("c")).show()
+----------+
|bit_xor(c)|
+----------+
|      NULL|
+----------+

```


Example 4: Bitwise XOR with single input value

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[5]], ["c"])
>>> df.select(sf.bit_xor("c")).show()
+----------+
|bit_xor(c)|
+----------+
|         5|
+----------+

```


# pyspark.sql.functions.bitmap_construct_agg — PySpark 4.0.1 documentation
pyspark.sql.functions.bitmap\_construct\_agg(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bitmap_construct_agg)
[#](#pyspark.sql.functions.bitmap_construct_agg "Permalink to this definition")

Returns a bitmap with the positions of the bits set from all the values from the input column. The input column will most likely be bitmap\_bit\_position().

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The input column will most likely be bitmap\_bit\_position().

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,),(2,),(3,)], ["a"])
>>> df.select(
...     sf.bitmap_construct_agg(sf.bitmap_bit_position('a'))
... ).show()
+--------------------------------------------+
|bitmap_construct_agg(bitmap_bit_position(a))|
+--------------------------------------------+
|                        [07 00 00 00 00 0...|
+--------------------------------------------+

```


# pyspark.sql.functions.bitmap_or_agg — PySpark 4.0.1 documentation
pyspark.sql.functions.bitmap\_or\_agg(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bitmap_or_agg)
[#](#pyspark.sql.functions.bitmap_or_agg "Permalink to this definition")

Returns a bitmap that is the bitwise OR of all of the bitmaps from the input column. The input column should be bitmaps created from bitmap\_construct\_agg().

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The input column should be bitmaps created from bitmap\_construct\_agg().

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("10",),("20",),("40",)], ["a"])
>>> df.select(sf.bitmap_or_agg(sf.to_binary(df.a, sf.lit("hex")))).show()
+--------------------------------+
|bitmap_or_agg(to_binary(a, hex))|
+--------------------------------+
|            [70 00 00 00 00 0...|
+--------------------------------+

```
# pyspark.sql.functions.bool_and — PySpark 4.0.1 documentation
pyspark.sql.functions.bool\_and(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bool_and)
[#](#pyspark.sql.functions.bool_and "Permalink to this definition")

Aggregate function: returns true if all values of col are true.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to check if all values are true.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if all values of col are true, false otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[True], [True], [True]], ["flag"])
>>> df.select(sf.bool_and("flag")).show()
+--------------+
|bool_and(flag)|
+--------------+
|          true|
+--------------+

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[True], [False], [True]], ["flag"])
>>> df.select(sf.bool_and("flag")).show()
+--------------+
|bool_and(flag)|
+--------------+
|         false|
+--------------+

```


```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([[False], [False], [False]], ["flag"])
>>> df.select(sf.bool_and("flag")).show()
+--------------+
|bool_and(flag)|
+--------------+
|         false|
+--------------+

```


# pyspark.sql.functions.bool_or — PySpark 4.0.1 documentation
pyspark.sql.functions.bool\_or(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bool_or)
[#](#pyspark.sql.functions.bool_or "Permalink to this definition")

Aggregate function: returns true if at least one value of col is true.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to check if at least one value is true.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if at least one value of col is true, false otherwise.

Examples

```
>>> df = spark.createDataFrame([[True], [True], [True]], ["flag"])
>>> df.select(bool_or("flag")).show()
+-------------+
|bool_or(flag)|
+-------------+
|         true|
+-------------+
>>> df = spark.createDataFrame([[True], [False], [True]], ["flag"])
>>> df.select(bool_or("flag")).show()
+-------------+
|bool_or(flag)|
+-------------+
|         true|
+-------------+
>>> df = spark.createDataFrame([[False], [False], [False]], ["flag"])
>>> df.select(bool_or("flag")).show()
+-------------+
|bool_or(flag)|
+-------------+
|        false|
+-------------+

```


# pyspark.sql.functions.collect_list — PySpark 4.0.1 documentation
pyspark.sql.functions.collect\_list(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#collect_list)
[#](#pyspark.sql.functions.collect_list "Permalink to this definition")

Aggregate function: Collects the values from a column into a list, maintaining duplicates, and returns this list of objects.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column on which the function is computed.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column object representing a list of collected values, with duplicate values included.

Notes

The function is non-deterministic as the order of collected results depends on the order of the rows, which possibly becomes non-deterministic after shuffle operations.

Examples

Example 1: Collect values from a DataFrame and sort the result in ascending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (2,), (2,)], ('value',))
>>> df.select(sf.sort_array(sf.collect_list('value')).alias('sorted_list')).show()
+-----------+
|sorted_list|
+-----------+
|  [1, 2, 2]|
+-----------+

```


Example 2: Collect values from a DataFrame and sort the result in descending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2,), (5,), (5,)], ('age',))
>>> df.select(sf.sort_array(sf.collect_list('age'), asc=False).alias('sorted_list')).show()
+-----------+
|sorted_list|
+-----------+
|  [5, 5, 2]|
+-----------+

```


Example 3: Collect values from a DataFrame with multiple columns and sort the result

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "John"), (2, "John"), (3, "Ana")], ("id", "name"))
>>> df = df.groupBy("name").agg(sf.sort_array(sf.collect_list('id')).alias('sorted_list'))
>>> df.orderBy(sf.desc("name")).show()
+----+-----------+
|name|sorted_list|
+----+-----------+
|John|     [1, 2]|
| Ana|        [3]|
+----+-----------+

```

# pyspark.sql.functions.collect_set — PySpark 4.0.1 documentation
pyspark.sql.functions.collect\_set(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#collect_set)
[#](#pyspark.sql.functions.collect_set "Permalink to this definition")

Aggregate function: Collects the values from a column into a set, eliminating duplicates, and returns this set of objects.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column on which the function is computed.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new Column object representing a set of collected values, duplicates excluded.

Notes

This function is non-deterministic as the order of collected results depends on the order of the rows, which may be non-deterministic after any shuffle operations.

Examples

Example 1: Collect values from a DataFrame and sort the result in ascending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (2,), (2,)], ('value',))
>>> df.select(sf.sort_array(sf.collect_set('value')).alias('sorted_set')).show()
+----------+
|sorted_set|
+----------+
|    [1, 2]|
+----------+

```


Example 2: Collect values from a DataFrame and sort the result in descending order

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(2,), (5,), (5,)], ('age',))
>>> df.select(sf.sort_array(sf.collect_set('age'), asc=False).alias('sorted_set')).show()
+----------+
|sorted_set|
+----------+
|    [5, 2]|
+----------+

```


Example 3: Collect values from a DataFrame with multiple columns and sort the result

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, "John"), (2, "John"), (3, "Ana")], ("id", "name"))
>>> df = df.groupBy("name").agg(sf.sort_array(sf.collect_set('id')).alias('sorted_set'))
>>> df.orderBy(sf.desc("name")).show()
+----+----------+
|name|sorted_set|
+----+----------+
|John|    [1, 2]|
| Ana|       [3]|
+----+----------+

```

# pyspark.sql.functions.corr — PySpark 4.0.1 documentation
pyspark.sql.functions.corr(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#corr)
[#](#pyspark.sql.functions.corr "Permalink to this definition")

Returns a new [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") for the Pearson Correlation Coefficient for `col1` and `col2`.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first column to calculate correlation.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

second column to calculate correlation.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Pearson Correlation Coefficient of these two column values.

Examples

```
>>> from pyspark.sql import functions as sf
>>> a = range(20)
>>> b = [2 * x for x in range(20)]
>>> df = spark.createDataFrame(zip(a, b), ["a", "b"])
>>> df.agg(sf.corr("a", df.b)).show()
+----------+
|corr(a, b)|
+----------+
|       1.0|
+----------+

```

# pyspark.sql.functions.count — PySpark 4.0.1 documentation
pyspark.sql.functions.count(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#count)
[#](#pyspark.sql.functions.count "Permalink to this definition")

Aggregate function: returns the number of items in a group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

column for computed results.

Examples

Example 1: Count all rows in a DataFrame

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(None,), ("a",), ("b",), ("c",)], schema=["alphabets"])
>>> df.select(sf.count(sf.expr("*"))).show()
+--------+
|count(1)|
+--------+
|       4|
+--------+

```


Example 2: Count non-null values in a specific column

```
>>> from pyspark.sql import functions as sf
>>> df.select(sf.count(df.alphabets)).show()
+----------------+
|count(alphabets)|
+----------------+
|               3|
+----------------+

```


Example 3: Count all rows in a DataFrame with multiple columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(1, "apple"), (2, "banana"), (3, None)], schema=["id", "fruit"])
>>> df.select(sf.count(sf.expr("*"))).show()
+--------+
|count(1)|
+--------+
|       3|
+--------+

```


Example 4: Count non-null values in multiple columns

```
>>> from pyspark.sql import functions as sf
>>> df.select(sf.count(df.id), sf.count(df.fruit)).show()
+---------+------------+
|count(id)|count(fruit)|
+---------+------------+
|        3|           2|
+---------+------------+

```


# pyspark.sql.functions.count_distinct — PySpark 4.0.1 documentation
pyspark.sql.functions.count\_distinct(_col_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#count_distinct)
[#](#pyspark.sql.functions.count_distinct "Permalink to this definition")

Returns a new `Column` for distinct count of `col` or `cols`.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first column to compute on.

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

other columns to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

distinct values of these two column values.

Examples

Example 1: Counting distinct values of a single column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (1,), (3,)], ["value"])
>>> df.select(sf.count_distinct(df.value)).show()
+---------------------+
|count(DISTINCT value)|
+---------------------+
|                    2|
+---------------------+

```


Example 2: Counting distinct values of multiple columns

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 1), (1, 2)], ["value1", "value2"])
>>> df.select(sf.count_distinct(df.value1, df.value2)).show()
+------------------------------+
|count(DISTINCT value1, value2)|
+------------------------------+
|                             2|
+------------------------------+

```


Example 3: Counting distinct values with column names as strings

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 1), (1, 2)], ["value1", "value2"])
>>> df.select(sf.count_distinct("value1", "value2")).show()
+------------------------------+
|count(DISTINCT value1, value2)|
+------------------------------+
|                             2|
+------------------------------+

```


# pyspark.sql.functions.count_if — PySpark 4.0.1 documentation
pyspark.sql.functions.count\_if(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#count_if)
[#](#pyspark.sql.functions.count_if "Permalink to this definition")

Aggregate function: Returns the number of TRUE values for the col.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of TRUE values for the col.

Examples

Example 1: Counting the number of even numbers in a numeric column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a", 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["c1", "c2"])
>>> df.select(sf.count_if(sf.col('c2') % 2 == 0)).show()
+------------------------+
|count_if(((c2 % 2) = 0))|
+------------------------+
|                       3|
+------------------------+

```


Example 2: Counting the number of rows where a string column starts with a certain letter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("apple",), ("banana",), ("cherry",), ("apple",), ("banana",)], ["fruit"])
>>> df.select(sf.count_if(sf.col('fruit').startswith('a'))).show()
+------------------------------+
|count_if(startswith(fruit, a))|
+------------------------------+
|                             2|
+------------------------------+

```


Example 3: Counting the number of rows where a numeric column is greater than a certain value

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (2,), (3,), (4,), (5,)], ["num"])
>>> df.select(sf.count_if(sf.col('num') > 3)).show()
+-------------------+
|count_if((num > 3))|
+-------------------+
|                  2|
+-------------------+

```


Example 4: Counting the number of rows where a boolean column is True

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(True,), (False,), (True,), (False,), (True,)], ["b"])
>>> df.select(sf.count('b'), sf.count_if('b')).show()
+--------+-----------+
|count(b)|count_if(b)|
+--------+-----------+
|       5|          3|
+--------+-----------+

```


# pyspark.sql.functions.count_min_sketch — PySpark 4.0.1 documentation
pyspark.sql.functions.count\_min\_sketch(_col_, _eps_, _confidence_, _seed\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#count_min_sketch)
[#](#pyspark.sql.functions.count_min_sketch "Permalink to this definition")

Returns a count-min sketch of a column with the given esp, confidence and seed. The result is an array of bytes, which can be deserialized to a CountMinSketch before usage. Count-min sketch is a probabilistic data structure used for cardinality estimation using sub-linear space.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**eps**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or float

relative error, must be positive

Changed in version 4.0.0: eps now accepts float value.

**confidence**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or float

confidence, must be positive and less than 1.0

Changed in version 4.0.0: confidence now accepts float value.

**seed**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

random seed

Changed in version 4.0.0: seed now accepts int value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

count-min sketch of the column

Examples

Example 1: Using columns as arguments

```
>>> from pyspark.sql import functions as sf
>>> spark.range(100).select(
...     sf.hex(sf.count_min_sketch(sf.col("id"), sf.lit(3.0), sf.lit(0.1), sf.lit(1)))
... ).show(truncate=False)
+------------------------------------------------------------------------+
|hex(count_min_sketch(id, 3.0, 0.1, 1))                                  |
+------------------------------------------------------------------------+
|0000000100000000000000640000000100000001000000005D8D6AB90000000000000064|
+------------------------------------------------------------------------+

```


Example 2: Using numbers as arguments

```
>>> from pyspark.sql import functions as sf
>>> spark.range(100).select(
...     sf.hex(sf.count_min_sketch("id", 1.0, 0.3, 2))
... ).show(truncate=False)
+----------------------------------------------------------------------------------------+
|hex(count_min_sketch(id, 1.0, 0.3, 2))                                                  |
+----------------------------------------------------------------------------------------+
|0000000100000000000000640000000100000002000000005D96391C00000000000000320000000000000032|
+----------------------------------------------------------------------------------------+

```


Example 3: Using a long seed

```
>>> from pyspark.sql import functions as sf
>>> spark.range(100).select(
...     sf.hex(sf.count_min_sketch("id", sf.lit(1.5), 0.2, 1111111111111111111))
... ).show(truncate=False)
+----------------------------------------------------------------------------------------+
|hex(count_min_sketch(id, 1.5, 0.2, 1111111111111111111))                                |
+----------------------------------------------------------------------------------------+
|00000001000000000000006400000001000000020000000044078BA100000000000000320000000000000032|
+----------------------------------------------------------------------------------------+

```


Example 4: Using a random seed

```
>>> from pyspark.sql import functions as sf
>>> spark.range(100).select(
...     sf.hex(sf.count_min_sketch("id", sf.lit(1.5), 0.6))
... ).show(truncate=False) 
+----------------------------------------------------------------------------------------------------------------------------------------+
|hex(count_min_sketch(id, 1.5, 0.6, 2120704260))                                                                                         |
+----------------------------------------------------------------------------------------------------------------------------------------+
|0000000100000000000000640000000200000002000000005ADECCEE00000000153EBE090000000000000033000000000000003100000000000000320000000000000032|
+----------------------------------------------------------------------------------------------------------------------------------------+

```

# pyspark.sql.functions.covar_pop — PySpark 4.0.1 documentation
pyspark.sql.functions.covar\_pop(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#covar_pop)
[#](#pyspark.sql.functions.covar_pop "Permalink to this definition")

Returns a new [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") for the population covariance of `col1` and `col2`.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first column to calculate covariance.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

second column to calculate covariance.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

covariance of these two column values.

Examples

```
>>> from pyspark.sql import functions as sf
>>> a = [1] * 10
>>> b = [1] * 10
>>> df = spark.createDataFrame(zip(a, b), ["a", "b"])
>>> df.agg(sf.covar_pop("a", df.b)).show()
+---------------+
|covar_pop(a, b)|
+---------------+
|            0.0|
+---------------+

```

# pyspark.sql.functions.covar_samp — PySpark 4.0.1 documentation
pyspark.sql.functions.covar\_samp(_col1_, _col2_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#covar_samp)
[#](#pyspark.sql.functions.covar_samp "Permalink to this definition")

Returns a new [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") for the sample covariance of `col1` and `col2`.

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

first column to calculate covariance.

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

second column to calculate covariance.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

sample covariance of these two column values.

Examples

```
>>> from pyspark.sql import functions as sf
>>> a = [1] * 10
>>> b = [1] * 10
>>> df = spark.createDataFrame(zip(a, b), ["a", "b"])
>>> df.agg(sf.covar_samp("a", df.b)).show()
+----------------+
|covar_samp(a, b)|
+----------------+
|             0.0|
+----------------+

```



# pyspark.sql.functions.every — PySpark 4.0.1 documentation
pyspark.sql.functions.every(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#every)
[#](#pyspark.sql.functions.every "Permalink to this definition")

Aggregate function: returns true if all values of col are true.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to check if all values are true.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if all values of col are true, false otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[True], [True], [True]], ["flag"]
... ).select(sf.every("flag")).show()
+-----------+
|every(flag)|
+-----------+
|       true|
+-----------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[True], [False], [True]], ["flag"]
... ).select(sf.every("flag")).show()
+-----------+
|every(flag)|
+-----------+
|      false|
+-----------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[False], [False], [False]], ["flag"]
... ).select(sf.every("flag")).show()
+-----------+
|every(flag)|
+-----------+
|      false|
+-----------+

```


# pyspark.sql.functions.first — PySpark 4.0.1 documentation
pyspark.sql.functions.first(_col_, _ignorenulls\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#first)
[#](#pyspark.sql.functions.first "Permalink to this definition")

Aggregate function: returns the first value in a group.

The function by default returns the first values it sees. It will return the first non-null value it sees when ignoreNulls is set to true. If all values are null, then null is returned.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to fetch first value for.

**ignorenulls**bool

if first value is null then look for first non-null value. `` False` `` by default.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

first value of the group.

Notes

The function is non-deterministic because its results depends on the order of the rows which may be non-deterministic after a shuffle.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5), ("Alice", None)], ("name", "age"))
>>> df = df.orderBy(df.age)
>>> df.groupby("name").agg(sf.first("age")).orderBy("name").show()
+-----+----------+
| name|first(age)|
+-----+----------+
|Alice|      NULL|
|  Bob|         5|
+-----+----------+

```


To ignore any null values, set `ignorenulls` to True

```
>>> df.groupby("name").agg(sf.first("age", ignorenulls=True)).orderBy("name").show()
+-----+----------+
| name|first(age)|
+-----+----------+
|Alice|         2|
|  Bob|         5|
+-----+----------+

```


# pyspark.sql.functions.first_value — PySpark 4.0.1 documentation
pyspark.sql.functions.first\_value(_col_, _ignoreNulls\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#first_value)
[#](#pyspark.sql.functions.first_value "Permalink to this definition")

Returns the first value of col for a group of rows. It will return the first non-null value it sees when ignoreNulls is set to true. If all values are null, then null is returned.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**ignoreNulls**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or bool, optional

if first value is null then look for first non-null value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

some value of col for a group of rows.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(None, 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["a", "b"]
... ).select(sf.first_value('a'), sf.first_value('b')).show()
+--------------+--------------+
|first_value(a)|first_value(b)|
+--------------+--------------+
|          NULL|             1|
+--------------+--------------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [(None, 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["a", "b"]
... ).select(sf.first_value('a', True), sf.first_value('b', True)).show()
+--------------+--------------+
|first_value(a)|first_value(b)|
+--------------+--------------+
|             a|             1|
+--------------+--------------+

```


# pyspark.sql.functions.grouping_id — PySpark 4.0.1 documentation
pyspark.sql.functions.grouping\_id(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#grouping_id)
[#](#pyspark.sql.functions.grouping_id "Permalink to this definition")

Aggregate function: returns the level of grouping, equals to

> (grouping(c1) << (n-1)) + (grouping(c2) << (n-2)) + … + grouping(cn)

New in version 2.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

columns to check for.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

returns level of the grouping it relates to.

Notes

The list of columns should match with grouping columns exactly, or empty (means all the grouping columns).

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [(1, "a", "a"), (3, "a", "a"), (4, "b", "c")], ["c1", "c2", "c3"])
>>> df.cube("c2", "c3").agg(sf.grouping_id(), sf.sum("c1")).orderBy("c2", "c3").show()
+----+----+-------------+-------+
|  c2|  c3|grouping_id()|sum(c1)|
+----+----+-------------+-------+
|NULL|NULL|            3|      8|
|NULL|   a|            2|      4|
|NULL|   c|            2|      4|
|   a|NULL|            1|      4|
|   a|   a|            0|      4|
|   b|NULL|            1|      4|
|   b|   c|            0|      4|
+----+----+-------------+-------+

```


# pyspark.sql.functions.histogram_numeric — PySpark 4.0.1 documentation
pyspark.sql.functions.histogram\_numeric(_col_, _nBins_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#histogram_numeric)
[#](#pyspark.sql.functions.histogram_numeric "Permalink to this definition")

Computes a histogram on numeric ‘col’ using nb bins. The return value is an array of (x,y) pairs representing the centers of the histogram’s bins. As the value of ‘nb’ is increased, the histogram approximation gets finer-grained, but may yield artifacts around outliers. In practice, 20-40 histogram bins appear to work well, with more bins being required for skewed or smaller datasets. Note that this function creates a histogram with non-uniform bin widths. It offers no guarantees in terms of the mean-squared-error of the histogram, but in practice is comparable to the histograms produced by the R/S-Plus statistical computing packages. Note: the output type of the ‘x’ field in the return value is propagated from the input value consumed in the aggregate function.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**nBins**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

number of Histogram columns.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a histogram on numeric ‘col’ using nb bins.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(100, numPartitions=1)
>>> df.select(sf.histogram_numeric('id', sf.lit(5))).show(truncate=False)
+-----------------------------------------------------------+
|histogram_numeric(id, 5)                                   |
+-----------------------------------------------------------+
|[{11, 25.0}, {36, 24.0}, {59, 23.0}, {84, 25.0}, {98, 3.0}]|
+-----------------------------------------------------------+

```


# pyspark.sql.functions.hll_sketch_agg — PySpark 4.0.1 documentation
pyspark.sql.functions.hll\_sketch\_agg(_col_, _lgConfigK\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hll_sketch_agg)
[#](#pyspark.sql.functions.hll_sketch_agg "Permalink to this definition")

Aggregate function: returns the updatable binary representation of the Datasketches HllSketch configured with lgConfigK arg.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**lgConfigK**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int, optional

The log-base-2 of K, where K is the number of buckets or slots for the HllSketch

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The binary representation of the HllSketch.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([1,2,2,3], "INT")
>>> df.agg(sf.hll_sketch_estimate(sf.hll_sketch_agg("value"))).show()
+----------------------------------------------+
|hll_sketch_estimate(hll_sketch_agg(value, 12))|
+----------------------------------------------+
|                                             3|
+----------------------------------------------+

```


```
>>> df.agg(sf.hll_sketch_estimate(sf.hll_sketch_agg("value", 12))).show()
+----------------------------------------------+
|hll_sketch_estimate(hll_sketch_agg(value, 12))|
+----------------------------------------------+
|                                             3|
+----------------------------------------------+

```


# pyspark.sql.functions.hll_union_agg — PySpark 4.0.1 documentation
pyspark.sql.functions.hll\_union\_agg(_col_, _allowDifferentLgConfigK\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hll_union_agg)
[#](#pyspark.sql.functions.hll_union_agg "Permalink to this definition")

Aggregate function: returns the updatable binary representation of the Datasketches HllSketch, generated by merging previously created Datasketches HllSketch instances via a Datasketches Union instance. Throws an exception if sketches have different lgConfigK values and allowDifferentLgConfigK is unset or set to false.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**allowDifferentLgConfigK**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or bool, optional

Allow sketches with different lgConfigK values to be merged (defaults to false).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The binary representation of the merged HllSketch.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df1 = spark.createDataFrame([1,2,2,3], "INT")
>>> df1 = df1.agg(sf.hll_sketch_agg("value").alias("sketch"))
>>> df2 = spark.createDataFrame([4,5,5,6], "INT")
>>> df2 = df2.agg(sf.hll_sketch_agg("value").alias("sketch"))
>>> df3 = df1.union(df2)
>>> df3.agg(sf.hll_sketch_estimate(sf.hll_union_agg("sketch"))).show()
+-------------------------------------------------+
|hll_sketch_estimate(hll_union_agg(sketch, false))|
+-------------------------------------------------+
|                                                6|
+-------------------------------------------------+

```


```
>>> df3.agg(sf.hll_sketch_estimate(sf.hll_union_agg("sketch", False))).show()
+-------------------------------------------------+
|hll_sketch_estimate(hll_union_agg(sketch, false))|
+-------------------------------------------------+
|                                                6|
+-------------------------------------------------+

```


# pyspark.sql.functions.kurtosis — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.kurtosis

pyspark.sql.functions.kurtosis(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#kurtosis)
[#](#pyspark.sql.functions.kurtosis "Permalink to this definition")

Aggregate function: returns the kurtosis of the values in a group.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

kurtosis of given column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[1],[2]], ["c"])
>>> df.select(sf.kurtosis(df.c)).show()
+-----------+
|kurtosis(c)|
+-----------+
|       -1.5|
+-----------+

```

# pyspark.sql.functions.last — PySpark 4.0.1 documentation
pyspark.sql.functions.last(_col_, _ignorenulls\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#last)
[#](#pyspark.sql.functions.last "Permalink to this definition")

Aggregate function: returns the last value in a group.

The function by default returns the last values it sees. It will return the last non-null value it sees when ignoreNulls is set to true. If all values are null, then null is returned.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to fetch last value for.

**ignorenulls**bool

if last value is null then look for non-null value. `` False` `` by default.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

last value of the group.

Notes

The function is non-deterministic because its results depends on the order of the rows which may be non-deterministic after a shuffle.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Alice", 2), ("Bob", 5), ("Alice", None)], ("name", "age"))
>>> df = df.orderBy(df.age.desc())
>>> df.groupby("name").agg(sf.last("age")).orderBy("name").show()
+-----+---------+
| name|last(age)|
+-----+---------+
|Alice|     NULL|
|  Bob|        5|
+-----+---------+

```


To ignore any null values, set `ignorenulls` to True

```
>>> df.groupby("name").agg(sf.last("age", ignorenulls=True)).orderBy("name").show()
+-----+---------+
| name|last(age)|
+-----+---------+
|Alice|        2|
|  Bob|        5|
+-----+---------+

```


# pyspark.sql.functions.last_value — PySpark 4.0.1 documentation
pyspark.sql.functions.last\_value(_col_, _ignoreNulls\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#last_value)
[#](#pyspark.sql.functions.last_value "Permalink to this definition")

Returns the last value of col for a group of rows. It will return the last non-null value it sees when ignoreNulls is set to true. If all values are null, then null is returned.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

**ignoreNulls**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or bool, optional

if first value is null then look for first non-null value.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

some value of col for a group of rows.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("a", 1), ("a", 2), ("a", 3), ("b", 8), (None, 2)], ["a", "b"]
... ).select(sf.last_value('a'), sf.last_value('b')).show()
+-------------+-------------+
|last_value(a)|last_value(b)|
+-------------+-------------+
|         NULL|            2|
+-------------+-------------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [("a", 1), ("a", 2), ("a", 3), ("b", 8), (None, 2)], ["a", "b"]
... ).select(sf.last_value('a', True), sf.last_value('b', True)).show()
+-------------+-------------+
|last_value(a)|last_value(b)|
+-------------+-------------+
|            b|            2|
+-------------+-------------+

```

# pyspark.sql.functions.listagg — PySpark 4.0.1 documentation
pyspark.sql.functions.listagg(_col_, _delimiter\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#listagg)
[#](#pyspark.sql.functions.listagg "Permalink to this definition")

Aggregate function: returns the concatenation of non-null input values, separated by the delimiter.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**delimiter**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), literal string or bytes, optional

the delimiter to separate the values. The default value is None.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Using listagg function

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',)], ['strings'])
>>> df.select(sf.listagg('strings')).show()
+----------------------+
|listagg(strings, NULL)|
+----------------------+
|                   abc|
+----------------------+

```


Example 2: Using listagg function with a delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',)], ['strings'])
>>> df.select(sf.listagg('strings', ', ')).show()
+--------------------+
|listagg(strings, , )|
+--------------------+
|             a, b, c|
+--------------------+

```


Example 3: Using listagg function with a binary column and delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(b'',), (b'',), (None,), (b'',)], ['bytes'])
>>> df.select(sf.listagg('bytes', b'B')).show()
+---------------------+
|listagg(bytes, X'42')|
+---------------------+
|     [01 42 02 42 03]|
+---------------------+

```


Example 4: Using listagg function on a column with all None values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, StringType
>>> schema = StructType([StructField("strings", StringType(), True)])
>>> df = spark.createDataFrame([(None,), (None,), (None,), (None,)], schema=schema)
>>> df.select(sf.listagg('strings')).show()
+----------------------+
|listagg(strings, NULL)|
+----------------------+
|                  NULL|
+----------------------+

```


# pyspark.sql.functions.listagg_distinct — PySpark 4.0.1 documentation
pyspark.sql.functions.listagg\_distinct(_col_, _delimiter\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#listagg_distinct)
[#](#pyspark.sql.functions.listagg_distinct "Permalink to this definition")

Aggregate function: returns the concatenation of distinct non-null input values, separated by the delimiter.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**delimiter**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), literal string or bytes, optional

the delimiter to separate the values. The default value is None.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Using listagg\_distinct function

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',), ('b',)], ['strings'])
>>> df.select(sf.listagg_distinct('strings')).show()
+-------------------------------+
|listagg(DISTINCT strings, NULL)|
+-------------------------------+
|                            abc|
+-------------------------------+

```


Example 2: Using listagg\_distinct function with a delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',), ('b',)], ['strings'])
>>> df.select(sf.listagg_distinct('strings', ', ')).show()
+-----------------------------+
|listagg(DISTINCT strings, , )|
+-----------------------------+
|                      a, b, c|
+-----------------------------+

```


Example 3: Using listagg\_distinct function with a binary column and delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(b'',), (b'',), (None,), (b'',), (b'',)],
...                            ['bytes'])
>>> df.select(sf.listagg_distinct('bytes', b'B')).show()
+------------------------------+
|listagg(DISTINCT bytes, X'42')|
+------------------------------+
|              [01 42 02 42 03]|
+------------------------------+

```


Example 4: Using listagg\_distinct function on a column with all None values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, StringType
>>> schema = StructType([StructField("strings", StringType(), True)])
>>> df = spark.createDataFrame([(None,), (None,), (None,), (None,)], schema=schema)
>>> df.select(sf.listagg_distinct('strings')).show()
+-------------------------------+
|listagg(DISTINCT strings, NULL)|
+-------------------------------+
|                           NULL|
+-------------------------------+

```


# pyspark.sql.functions.max — PySpark 4.0.1 documentation
pyspark.sql.functions.max(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#max)
[#](#pyspark.sql.functions.max "Permalink to this definition")

Aggregate function: returns the maximum value of the expression in a group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column on which the maximum value is computed.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column that contains the maximum value computed.

Notes

*   Null values are ignored during the computation.
    
*   NaN values are larger than any other numeric value.
    

Examples

Example 1: Compute the maximum value of a numeric column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(10)
>>> df.select(sf.max(df.id)).show()
+-------+
|max(id)|
+-------+
|      9|
+-------+

```


Example 2: Compute the maximum value of a string column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("A",), ("B",), ("C",)], ["value"])
>>> df.select(sf.max(df.value)).show()
+----------+
|max(value)|
+----------+
|         C|
+----------+

```


Example 3: Compute the maximum value of a column in a grouped DataFrame

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("A", 1), ("A", 2), ("B", 3), ("B", 4)], ["key", "value"])
>>> df.groupBy("key").agg(sf.max(df.value)).show()
+---+----------+
|key|max(value)|
+---+----------+
|  A|         2|
|  B|         4|
+---+----------+

```


Example 4: Compute the maximum value of multiple columns in a grouped DataFrame

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [("A", 1, 2), ("A", 2, 3), ("B", 3, 4), ("B", 4, 5)], ["key", "value1", "value2"])
>>> df.groupBy("key").agg(sf.max("value1"), sf.max("value2")).show()
+---+-----------+-----------+
|key|max(value1)|max(value2)|
+---+-----------+-----------+
|  A|          2|          3|
|  B|          4|          5|
+---+-----------+-----------+

```


Example 5: Compute the maximum value of a column with null values

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1,), (2,), (None,)], ["value"])
>>> df.select(sf.max(df.value)).show()
+----------+
|max(value)|
+----------+
|         2|
+----------+

```


Example 6: Compute the maximum value of a column with “NaN” values

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1.1,), (float("nan"),), (3.3,)], ["value"])
>>> df.select(sf.max(df.value)).show()
+----------+
|max(value)|
+----------+
|       NaN|
+----------+

```# pyspark.sql.functions.max_by — PySpark 4.0.1 documentation
pyspark.sql.functions.max\_by(_col_, _ord_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#max_by)
[#](#pyspark.sql.functions.max_by "Permalink to this definition")

Returns the value from the col parameter that is associated with the maximum value from the ord parameter. This function is often used to find the col parameter value corresponding to the maximum ord parameter value within each group when used with groupBy().

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The column representing the values to be returned. This could be the column instance or the column name as string.

**ord**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The column that needs to be maximized. This could be the column instance or the column name as string.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column object representing the value from col that is associated with the maximum value from ord.

Notes

The function is non-deterministic so the output order can be different for those associated the same values of col.

Examples

Example 1: Using max\_by with groupBy

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ("Java", 2012, 20000), ("dotNET", 2012, 5000),
...     ("dotNET", 2013, 48000), ("Java", 2013, 30000)],
...     schema=("course", "year", "earnings"))
>>> df.groupby("course").agg(sf.max_by("year", "earnings")).sort("course").show()
+------+----------------------+
|course|max_by(year, earnings)|
+------+----------------------+
|  Java|                  2013|
|dotNET|                  2013|
+------+----------------------+

```


Example 2: Using max\_by with different data types

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ("Marketing", "Anna", 4), ("IT", "Bob", 2),
...     ("IT", "Charlie", 3), ("Marketing", "David", 1)],
...     schema=("department", "name", "years_in_dept"))
>>> df.groupby("department").agg(
...     sf.max_by("name", "years_in_dept")
... ).sort("department").show()
+----------+---------------------------+
|department|max_by(name, years_in_dept)|
+----------+---------------------------+
|        IT|                    Charlie|
| Marketing|                       Anna|
+----------+---------------------------+

```


Example 3: Using max\_by where ord has multiple maximum values

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ("Consult", "Eva", 6), ("Finance", "Frank", 5),
...     ("Finance", "George", 9), ("Consult", "Henry", 7)],
...     schema=("department", "name", "years_in_dept"))
>>> df.groupby("department").agg(
...     sf.max_by("name", "years_in_dept")
... ).sort("department").show()
+----------+---------------------------+
|department|max_by(name, years_in_dept)|
+----------+---------------------------+
|   Consult|                      Henry|
|   Finance|                     George|
+----------+---------------------------+

```



# pyspark.sql.functions.mean — PySpark 4.0.1 documentation
pyspark.sql.functions.mean(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#mean)
[#](#pyspark.sql.functions.mean "Permalink to this definition")

Aggregate function: returns the average of the values in a group. An alias of [`avg()`](about:blank/pyspark.sql.functions.avg.html#pyspark.sql.functions.avg "pyspark.sql.functions.avg").

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Calculating the average age

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, 15), (1990, 2)], ["birth", "age"])
>>> df.select(sf.mean("age")).show()
+--------+
|avg(age)|
+--------+
|     8.5|
+--------+

```


Example 2: Calculating the average age with None

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, None), (1990, 2), (2000, 4)], ["birth", "age"])
>>> df.select(sf.mean("age")).show()
+--------+
|avg(age)|
+--------+
|     3.0|
+--------+

```

# pyspark.sql.functions.median — PySpark 4.0.1 documentation
pyspark.sql.functions.median(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#median)
[#](#pyspark.sql.functions.median "Permalink to this definition")

Returns the median of the values in a group.

New in version 3.4.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the median of the values in a group.

Notes

Supports Spark Connect.

[`pyspark.sql.functions.percentile()`](about:blank/pyspark.sql.functions.percentile.html#pyspark.sql.functions.percentile "pyspark.sql.functions.percentile") [`pyspark.sql.functions.approx_percentile()`](about:blank/pyspark.sql.functions.approx_percentile.html#pyspark.sql.functions.approx_percentile "pyspark.sql.functions.approx_percentile") [`pyspark.sql.functions.percentile_approx()`](about:blank/pyspark.sql.functions.percentile_approx.html#pyspark.sql.functions.percentile_approx "pyspark.sql.functions.percentile_approx")

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     ("Java", 2012, 20000), ("dotNET", 2012, 5000),
...     ("Java", 2012, 22000), ("dotNET", 2012, 10000),
...     ("dotNET", 2013, 48000), ("Java", 2013, 30000)],
...     schema=("course", "year", "earnings"))
>>> df.groupby("course").agg(sf.median("earnings")).show()
+------+----------------+
|course|median(earnings)|
+------+----------------+
|  Java|         22000.0|
|dotNET|         10000.0|
+------+----------------+

```



# pyspark.sql.functions.min — PySpark 4.0.1 documentation
pyspark.sql.functions.min(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#min)
[#](#pyspark.sql.functions.min "Permalink to this definition")

Aggregate function: returns the minimum value of the expression in a group.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The target column on which the minimum value is computed.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column that contains the minimum value computed.

Examples

Example 1: Compute the minimum value of a numeric column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.range(10)
>>> df.select(sf.min(df.id)).show()
+-------+
|min(id)|
+-------+
|      0|
+-------+

```


Example 2: Compute the minimum value of a string column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("Alice",), ("Bob",), ("Charlie",)], ["name"])
>>> df.select(sf.min("name")).show()
+---------+
|min(name)|
+---------+
|    Alice|
+---------+

```


Example 3: Compute the minimum value of a column with null values

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1,), (None,), (3,)], ["value"])
>>> df.select(sf.min("value")).show()
+----------+
|min(value)|
+----------+
|         1|
+----------+

```


Example 4: Compute the minimum value of a column in a grouped DataFrame

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([("Alice", 1), ("Alice", 2), ("Bob", 3)], ["name", "value"])
>>> df.groupBy("name").agg(sf.min("value")).show()
+-----+----------+
| name|min(value)|
+-----+----------+
|Alice|         1|
|  Bob|         3|
+-----+----------+

```


Example 5: Compute the minimum value of a column in a DataFrame with multiple columns

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame(
...     [("Alice", 1, 100), ("Bob", 2, 200), ("Charlie", 3, 300)],
...     ["name", "value1", "value2"])
>>> df.select(sf.min("value1"), sf.min("value2")).show()
+-----------+-----------+
|min(value1)|min(value2)|
+-----------+-----------+
|          1|        100|
+-----------+-----------+

```


# pyspark.sql.functions.min_by — PySpark 4.0.1 documentation
pyspark.sql.functions.min\_by(_col_, _ord_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#min_by)
[#](#pyspark.sql.functions.min_by "Permalink to this definition")

Returns the value from the col parameter that is associated with the minimum value from the ord parameter. This function is often used to find the col parameter value corresponding to the minimum ord parameter value within each group when used with groupBy().

New in version 3.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The column representing the values that will be returned. This could be the column instance or the column name as string.

**ord**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The column that needs to be minimized. This could be the column instance or the column name as string.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Column object that represents the value from col associated with the minimum value from ord.

Notes

The function is non-deterministic so the output order can be different for those associated the same values of col.

Examples

Example 1: Using min\_by with groupBy:

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ("Java", 2012, 20000), ("dotNET", 2012, 5000),
...     ("dotNET", 2013, 48000), ("Java", 2013, 30000)],
...     schema=("course", "year", "earnings"))
>>> df.groupby("course").agg(sf.min_by("year", "earnings")).sort("course").show()
+------+----------------------+
|course|min_by(year, earnings)|
+------+----------------------+
|  Java|                  2012|
|dotNET|                  2012|
+------+----------------------+

```


Example 2: Using min\_by with different data types:

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ("Marketing", "Anna", 4), ("IT", "Bob", 2),
...     ("IT", "Charlie", 3), ("Marketing", "David", 1)],
...     schema=("department", "name", "years_in_dept"))
>>> df.groupby("department").agg(
...     sf.min_by("name", "years_in_dept")
... ).sort("department").show()
+----------+---------------------------+
|department|min_by(name, years_in_dept)|
+----------+---------------------------+
|        IT|                        Bob|
| Marketing|                      David|
+----------+---------------------------+

```


Example 3: Using min\_by where ord has multiple minimum values:

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([
...     ("Consult", "Eva", 6), ("Finance", "Frank", 5),
...     ("Finance", "George", 9), ("Consult", "Henry", 7)],
...     schema=("department", "name", "years_in_dept"))
>>> df.groupby("department").agg(
...     sf.min_by("name", "years_in_dept")
... ).sort("department").show()
+----------+---------------------------+
|department|min_by(name, years_in_dept)|
+----------+---------------------------+
|   Consult|                        Eva|
|   Finance|                      Frank|
+----------+---------------------------+

```


# pyspark.sql.functions.mode — PySpark 4.0.1 documentation
pyspark.sql.functions.mode(_col_, _deterministic\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#mode)
[#](#pyspark.sql.functions.mode "Permalink to this definition")

Returns the most frequent value in a group.

New in version 3.4.0.

Changed in version 4.0.0: Supports deterministic argument.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**deterministic**bool, optional

if there are multiple equally-frequent results then return the lowest (defaults to false).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the most frequent value in a group.

Notes

Supports Spark Connect.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([
...     ("Java", 2012, 20000), ("dotNET", 2012, 5000),
...     ("Java", 2012, 20000), ("dotNET", 2012, 5000),
...     ("dotNET", 2013, 48000), ("Java", 2013, 30000)],
...     schema=("course", "year", "earnings"))
>>> df.groupby("course").agg(sf.mode("year")).sort("course").show()
+------+----------+
|course|mode(year)|
+------+----------+
|  Java|      2012|
|dotNET|      2012|
+------+----------+

```


When multiple values have the same greatest frequency then either any of values is returned if deterministic is false or is not defined, or the lowest value is returned if deterministic is true.

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(-10,), (0,), (10,)], ["col"])
>>> df.select(sf.mode("col", False)).show() 
+---------+
|mode(col)|
+---------+
|        0|
+---------+

```


```
>>> df.select(sf.mode("col", True)).show()
+---------------------------------------+
|mode() WITHIN GROUP (ORDER BY col DESC)|
+---------------------------------------+
|                                    -10|
+---------------------------------------+

```

# pyspark.sql.functions.percentile — PySpark 4.0.1 documentation
pyspark.sql.functions.percentile(_col_, _percentage_, _frequency\=1_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#percentile)
[#](#pyspark.sql.functions.percentile "Permalink to this definition")

Returns the exact percentile(s) of numeric column expr at the given percentage(s) with value range in \[0.0, 1.0\].

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**percentage**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), float, list of floats or tuple of floats

percentage in decimal (must be between 0.0 and 1.0).

**frequency**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int is a positive numeric literal which

controls frequency.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the exact percentile of the numeric column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> key = (sf.col("id") % 3).alias("key")
>>> value = (sf.randn(42) + key * 10).alias("value")
>>> df = spark.range(0, 1000, 1, 1).select(key, value)
>>> df.select(
...     sf.percentile("value", [0.25, 0.5, 0.75], sf.lit(1))
... ).show(truncate=False)
+--------------------------------------------------------+
|percentile(value, array(0.25, 0.5, 0.75), 1)            |
+--------------------------------------------------------+
|[0.7441991494121..., 9.9900713756..., 19.33740203080...]|
+--------------------------------------------------------+

```


```
>>> df.groupBy("key").agg(
...     sf.percentile("value", sf.lit(0.5), sf.lit(1))
... ).sort("key").show()
+---+-------------------------+
|key|percentile(value, 0.5, 1)|
+---+-------------------------+
|  0|     -0.03449962216667901|
|  1|        9.990389751837329|
|  2|       19.967859769284075|
+---+-------------------------+

```


# pyspark.sql.functions.percentile_approx — PySpark 4.0.1 documentation
pyspark.sql.functions.percentile\_approx(_col_, _percentage_, _accuracy\=10000_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#percentile_approx)
[#](#pyspark.sql.functions.percentile_approx "Permalink to this definition")

Returns the approximate percentile of the numeric column col which is the smallest value in the ordered col values (sorted from least to greatest) such that no more than percentage of col values is less than the value or equal to that value.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column.

**percentage**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), float, list of floats or tuple of floats

percentage in decimal (must be between 0.0 and 1.0). When percentage is an array, each value of the percentage array must be between 0.0 and 1.0. In this case, returns the approximate percentile array of column col at the given percentage array.

**accuracy**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

is a positive numeric literal which controls approximation accuracy at the cost of memory. Higher value of accuracy yields better accuracy, 1.0/accuracy is the relative error of the approximation. (default: 10000).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

approximate percentile of the numeric column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> key = (sf.col("id") % 3).alias("key")
>>> value = (sf.randn(42) + key * 10).alias("value")
>>> df = spark.range(0, 1000, 1, 1).select(key, value)
>>> df.select(
...     sf.percentile_approx("value", [0.25, 0.5, 0.75], 1000000)
... ).show(truncate=False)
+----------------------------------------------------------+
|percentile_approx(value, array(0.25, 0.5, 0.75), 1000000) |
+----------------------------------------------------------+
|[0.7264430125286..., 9.98975299938..., 19.335304783039...]|
+----------------------------------------------------------+

```


```
>>> df.groupBy("key").agg(
...     sf.percentile_approx("value", sf.lit(0.5), sf.lit(1000000))
... ).sort("key").show()
+---+--------------------------------------+
|key|percentile_approx(value, 0.5, 1000000)|
+---+--------------------------------------+
|  0|                  -0.03519435193070...|
|  1|                     9.990389751837...|
|  2|                    19.967859769284...|
+---+--------------------------------------+

```


# pyspark.sql.functions.product — PySpark 4.0.1 documentation
pyspark.sql.functions.product(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#product)
[#](#pyspark.sql.functions.product "Permalink to this definition")

Aggregate function: returns the product of the values in a group.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column containing values to be multiplied together

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the column for computed results.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql("SELECT id % 3 AS mod3, id AS value FROM RANGE(10)")
>>> df.groupBy('mod3').agg(sf.product('value')).orderBy('mod3').show()
+----+--------------+
|mod3|product(value)|
+----+--------------+
|   0|           0.0|
|   1|          28.0|
|   2|          80.0|
+----+--------------+

```

# pyspark.sql.functions.regr_avgx — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_avgx(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_avgx)
[#](#pyspark.sql.functions.regr_avgx "Permalink to this definition")

Aggregate function: returns the average of the independent variable for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the average of the independent variable for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, 2), (2, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_avgx("y", "x"), sf.avg("x")).show()
+---------------+------+
|regr_avgx(y, x)|avg(x)|
+---------------+------+
|           2.75|  2.75|
+---------------+------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_avgx("y", "x"), sf.avg("x")).show()
+---------------+------+
|regr_avgx(y, x)|avg(x)|
+---------------+------+
|           NULL|  NULL|
+---------------+------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_avgx("y", "x"), sf.avg("x")).show()
+---------------+------+
|regr_avgx(y, x)|avg(x)|
+---------------+------+
|           NULL|   1.0|
+---------------+------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, null), (2, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_avgx("y", "x"), sf.avg("x")).show()
+---------------+------+
|regr_avgx(y, x)|avg(x)|
+---------------+------+
|            3.0|   3.0|
+---------------+------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, null), (null, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_avgx("y", "x"), sf.avg("x")).show()
+---------------+------+
|regr_avgx(y, x)|avg(x)|
+---------------+------+
|            3.0|   3.0|
+---------------+------+

```

# pyspark.sql.functions.regr_avgy — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_avgy(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_avgy)
[#](#pyspark.sql.functions.regr_avgy "Permalink to this definition")

Aggregate function: returns the average of the dependent variable for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the average of the dependent variable for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, 2), (2, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_avgy("y", "x"), sf.avg("y")).show()
+---------------+------+
|regr_avgy(y, x)|avg(y)|
+---------------+------+
|           1.75|  1.75|
+---------------+------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_avgy("y", "x"), sf.avg("y")).show()
+---------------+------+
|regr_avgy(y, x)|avg(y)|
+---------------+------+
|           NULL|   1.0|
+---------------+------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_avgy("y", "x"), sf.avg("y")).show()
+---------------+------+
|regr_avgy(y, x)|avg(y)|
+---------------+------+
|           NULL|  NULL|
+---------------+------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, null), (2, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_avgy("y", "x"), sf.avg("y")).show()
+------------------+------+
|   regr_avgy(y, x)|avg(y)|
+------------------+------+
|1.6666666666666...|  1.75|
+------------------+------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, null), (null, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_avgy("y", "x"), sf.avg("y")).show()
+---------------+------------------+
|regr_avgy(y, x)|            avg(y)|
+---------------+------------------+
|            1.5|1.6666666666666...|
+---------------+------------------+

```


# pyspark.sql.functions.regr_count — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_count(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_count)
[#](#pyspark.sql.functions.regr_count "Permalink to this definition")

Aggregate function: returns the number of non-null number pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of non-null number pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, 2), (2, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_count("y", "x"), sf.count(sf.lit(0))).show()
+----------------+--------+
|regr_count(y, x)|count(0)|
+----------------+--------+
|               4|       4|
+----------------+--------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_count("y", "x"), sf.count(sf.lit(0))).show()
+----------------+--------+
|regr_count(y, x)|count(0)|
+----------------+--------+
|               0|       1|
+----------------+--------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_count("y", "x"), sf.count(sf.lit(0))).show()
+----------------+--------+
|regr_count(y, x)|count(0)|
+----------------+--------+
|               0|       1|
+----------------+--------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, null), (2, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_count("y", "x"), sf.count(sf.lit(0))).show()
+----------------+--------+
|regr_count(y, x)|count(0)|
+----------------+--------+
|               3|       4|
+----------------+--------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 2), (2, null), (null, 3), (2, 4) AS tab(y, x)")
>>> df.select(sf.regr_count("y", "x"), sf.count(sf.lit(0))).show()
+----------------+--------+
|regr_count(y, x)|count(0)|
+----------------+--------+
|               2|       4|
+----------------+--------+

```



# pyspark.sql.functions.regr_intercept — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_intercept(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_intercept)
[#](#pyspark.sql.functions.regr_intercept "Permalink to this definition")

Aggregate function: returns the intercept of the univariate linear regression line for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the intercept of the univariate linear regression line for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, 2), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_intercept("y", "x")).show()
+--------------------+
|regr_intercept(y, x)|
+--------------------+
|                 0.0|
+--------------------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_intercept("y", "x")).show()
+--------------------+
|regr_intercept(y, x)|
+--------------------+
|                NULL|
+--------------------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_intercept("y", "x")).show()
+--------------------+
|regr_intercept(y, x)|
+--------------------+
|                NULL|
+--------------------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_intercept("y", "x")).show()
+--------------------+
|regr_intercept(y, x)|
+--------------------+
|                 0.0|
+--------------------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (null, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_intercept("y", "x")).show()
+--------------------+
|regr_intercept(y, x)|
+--------------------+
|                 0.0|
+--------------------+

```

# pyspark.sql.functions.regr_r2 — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_r2(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_r2)
[#](#pyspark.sql.functions.regr_r2 "Permalink to this definition")

Aggregate function: returns the coefficient of determination for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the coefficient of determination for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, 2), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_r2("y", "x")).show()
+-------------+
|regr_r2(y, x)|
+-------------+
|          1.0|
+-------------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_r2("y", "x")).show()
+-------------+
|regr_r2(y, x)|
+-------------+
|         NULL|
+-------------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_r2("y", "x")).show()
+-------------+
|regr_r2(y, x)|
+-------------+
|         NULL|
+-------------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_r2("y", "x")).show()
+-------------+
|regr_r2(y, x)|
+-------------+
|          1.0|
+-------------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (null, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_r2("y", "x")).show()
+-------------+
|regr_r2(y, x)|
+-------------+
|          1.0|
+-------------+

```


# pyspark.sql.functions.regr_slope — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_slope(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_slope)
[#](#pyspark.sql.functions.regr_slope "Permalink to this definition")

Aggregate function: returns the slope of the linear regression line for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the slope of the linear regression line for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, 2), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_slope("y", "x")).show()
+----------------+
|regr_slope(y, x)|
+----------------+
|             1.0|
+----------------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_slope("y", "x")).show()
+----------------+
|regr_slope(y, x)|
+----------------+
|            NULL|
+----------------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_slope("y", "x")).show()
+----------------+
|regr_slope(y, x)|
+----------------+
|            NULL|
+----------------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_slope("y", "x")).show()
+----------------+
|regr_slope(y, x)|
+----------------+
|             1.0|
+----------------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (null, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_slope("y", "x")).show()
+----------------+
|regr_slope(y, x)|
+----------------+
|             1.0|
+----------------+

```



# pyspark.sql.functions.regr_sxx — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_sxx(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_sxx)
[#](#pyspark.sql.functions.regr_sxx "Permalink to this definition")

Aggregate function: returns REGR\_COUNT(y, x) \* VAR\_POP(x) for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

REGR\_COUNT(y, x) \* VAR\_POP(x) for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, 2), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_sxx("y", "x")).show()
+--------------+
|regr_sxx(y, x)|
+--------------+
|           5.0|
+--------------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_sxx("y", "x")).show()
+--------------+
|regr_sxx(y, x)|
+--------------+
|          NULL|
+--------------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_sxx("y", "x")).show()
+--------------+
|regr_sxx(y, x)|
+--------------+
|          NULL|
+--------------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_sxx("y", "x")).show()
+-----------------+
|   regr_sxx(y, x)|
+-----------------+
|4.666666666666...|
+-----------------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (null, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_sxx("y", "x")).show()
+--------------+
|regr_sxx(y, x)|
+--------------+
|           4.5|
+--------------+

```

# pyspark.sql.functions.regr_sxy — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_sxy(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_sxy)
[#](#pyspark.sql.functions.regr_sxy "Permalink to this definition")

Aggregate function: returns REGR\_COUNT(y, x) \* COVAR\_POP(y, x) for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

REGR\_COUNT(y, x) \* COVAR\_POP(y, x) for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, 2), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_sxy("y", "x")).show()
+--------------+
|regr_sxy(y, x)|
+--------------+
|           5.0|
+--------------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_sxy("y", "x")).show()
+--------------+
|regr_sxy(y, x)|
+--------------+
|          NULL|
+--------------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_sxy("y", "x")).show()
+--------------+
|regr_sxy(y, x)|
+--------------+
|          NULL|
+--------------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_sxy("y", "x")).show()
+-----------------+
|   regr_sxy(y, x)|
+-----------------+
|4.666666666666...|
+-----------------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (null, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_sxy("y", "x")).show()
+--------------+
|regr_sxy(y, x)|
+--------------+
|           4.5|
+--------------+

```



# pyspark.sql.functions.regr_syy — PySpark 4.0.1 documentation
pyspark.sql.functions.regr\_syy(_y_, _x_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#regr_syy)
[#](#pyspark.sql.functions.regr_syy "Permalink to this definition")

Aggregate function: returns REGR\_COUNT(y, x) \* VAR\_POP(y) for non-null pairs in a group, where y is the dependent variable and x is the independent variable.

New in version 3.5.0.

Parameters

**y**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the dependent variable.

**x**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the independent variable.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

REGR\_COUNT(y, x) \* VAR\_POP(y) for non-null pairs in a group.

Examples

Example 1: All pairs are non-null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, 2), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_syy("y", "x")).show()
+--------------+
|regr_syy(y, x)|
+--------------+
|           5.0|
+--------------+

```


Example 2: All pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, null) AS tab(y, x)")
>>> df.select(sf.regr_syy("y", "x")).show()
+--------------+
|regr_syy(y, x)|
+--------------+
|          NULL|
+--------------+

```


Example 3: All pairs’ y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (null, 1) AS tab(y, x)")
>>> df.select(sf.regr_syy("y", "x")).show()
+--------------+
|regr_syy(y, x)|
+--------------+
|          NULL|
+--------------+

```


Example 4: Some pairs’ x values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (3, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_syy("y", "x")).show()
+-----------------+
|   regr_syy(y, x)|
+-----------------+
|4.666666666666...|
+-----------------+

```


Example 5: Some pairs’ x or y values are null

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT * FROM VALUES (1, 1), (2, null), (null, 3), (4, 4) AS tab(y, x)")
>>> df.select(sf.regr_syy("y", "x")).show()
+--------------+
|regr_syy(y, x)|
+--------------+
|           4.5|
+--------------+

```


# pyspark.sql.functions.skewness — PySpark 4.0.1 documentation
pyspark.sql.functions.skewness(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#skewness)
[#](#pyspark.sql.functions.skewness "Permalink to this definition")

Aggregate function: returns the skewness of the values in a group.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

skewness of given column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([[1],[1],[2]], ["c"])
>>> df.select(sf.skewness(df.c)).show()
+------------------+
|       skewness(c)|
+------------------+
|0.7071067811865...|
+------------------+

```


# pyspark.sql.functions.some — PySpark 4.0.1 documentation
pyspark.sql.functions.some(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#some)
[#](#pyspark.sql.functions.some "Permalink to this definition")

Aggregate function: returns true if at least one value of col is true.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column to check if at least one value is true.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

true if at least one value of col is true, false otherwise.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[True], [True], [True]], ["flag"]
... ).select(sf.some("flag")).show()
+----------+
|some(flag)|
+----------+
|      true|
+----------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[True], [False], [True]], ["flag"]
... ).select(sf.some("flag")).show()
+----------+
|some(flag)|
+----------+
|      true|
+----------+

```


```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [[False], [False], [False]], ["flag"]
... ).select(sf.some("flag")).show()
+----------+
|some(flag)|
+----------+
|     false|
+----------+

```


# pyspark.sql.functions.std — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.std

pyspark.sql.functions.std(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#std)
[#](#pyspark.sql.functions.std "Permalink to this definition")

Aggregate function: alias for stddev\_samp.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

standard deviation of given column.

See also

[`pyspark.sql.functions.stddev()`](about:blank/pyspark.sql.functions.stddev.html#pyspark.sql.functions.stddev "pyspark.sql.functions.stddev")

[`pyspark.sql.functions.stddev_pop()`](about:blank/pyspark.sql.functions.stddev_pop.html#pyspark.sql.functions.stddev_pop "pyspark.sql.functions.stddev_pop")

[`pyspark.sql.functions.stddev_samp()`](about:blank/pyspark.sql.functions.stddev_samp.html#pyspark.sql.functions.stddev_samp "pyspark.sql.functions.stddev_samp")

[`pyspark.sql.functions.variance()`](about:blank/pyspark.sql.functions.variance.html#pyspark.sql.functions.variance "pyspark.sql.functions.variance")

[`pyspark.sql.functions.skewness()`](about:blank/pyspark.sql.functions.skewness.html#pyspark.sql.functions.skewness "pyspark.sql.functions.skewness")

[`pyspark.sql.functions.kurtosis()`](about:blank/pyspark.sql.functions.kurtosis.html#pyspark.sql.functions.kurtosis "pyspark.sql.functions.kurtosis")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(6).select(sf.std("id")).show()
+------------------+
|           std(id)|
+------------------+
|1.8708286933869...|
+------------------+

```


# pyspark.sql.functions.stddev — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.stddev

pyspark.sql.functions.stddev(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#stddev)
[#](#pyspark.sql.functions.stddev "Permalink to this definition")

Aggregate function: alias for stddev\_samp.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

standard deviation of given column.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(6).select(sf.stddev("id")).show()
+------------------+
|        stddev(id)|
+------------------+
|1.8708286933869...|
+------------------+

```





# pyspark.sql.functions.stddev_pop — PySpark 4.0.1 documentation
pyspark.sql.functions.stddev\_pop(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#stddev_pop)
[#](#pyspark.sql.functions.stddev_pop "Permalink to this definition")

Aggregate function: returns population standard deviation of the expression in a group.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

standard deviation of given column.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(6).select(sf.stddev_pop("id")).show()
+-----------------+
|   stddev_pop(id)|
+-----------------+
|1.707825127659...|
+-----------------+

```



# pyspark.sql.functions.stddev_samp — PySpark 4.0.1 documentation
pyspark.sql.functions.stddev\_samp(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#stddev_samp)
[#](#pyspark.sql.functions.stddev_samp "Permalink to this definition")

Aggregate function: returns the unbiased sample standard deviation of the expression in a group.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

standard deviation of given column.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(6).select(sf.stddev_samp("id")).show()
+------------------+
|   stddev_samp(id)|
+------------------+
|1.8708286933869...|
+------------------+

```


# pyspark.sql.functions.string_agg — PySpark 4.0.1 documentation
pyspark.sql.functions.string\_agg(_col_, _delimiter\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#string_agg)
[#](#pyspark.sql.functions.string_agg "Permalink to this definition")

Aggregate function: returns the concatenation of non-null input values, separated by the delimiter.

An alias of [`listagg()`](about:blank/pyspark.sql.functions.listagg.html#pyspark.sql.functions.listagg "pyspark.sql.functions.listagg").

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**delimiter**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), literal string or bytes, optional

the delimiter to separate the values. The default value is None.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Using string\_agg function

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',)], ['strings'])
>>> df.select(sf.string_agg('strings')).show()
+-------------------------+
|string_agg(strings, NULL)|
+-------------------------+
|                      abc|
+-------------------------+

```


Example 2: Using string\_agg function with a delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',)], ['strings'])
>>> df.select(sf.string_agg('strings', ', ')).show()
+-----------------------+
|string_agg(strings, , )|
+-----------------------+
|                a, b, c|
+-----------------------+

```


Example 3: Using string\_agg function with a binary column and delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(b'',), (b'',), (None,), (b'',)], ['bytes'])
>>> df.select(sf.string_agg('bytes', b'B')).show()
+------------------------+
|string_agg(bytes, X'42')|
+------------------------+
|        [01 42 02 42 03]|
+------------------------+

```


Example 4: Using string\_agg function on a column with all None values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, StringType
>>> schema = StructType([StructField("strings", StringType(), True)])
>>> df = spark.createDataFrame([(None,), (None,), (None,), (None,)], schema=schema)
>>> df.select(sf.string_agg('strings')).show()
+-------------------------+
|string_agg(strings, NULL)|
+-------------------------+
|                     NULL|
+-------------------------+

```


# pyspark.sql.functions.string_agg_distinct — PySpark 4.0.1 documentation
pyspark.sql.functions.string\_agg\_distinct(_col_, _delimiter\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#string_agg_distinct)
[#](#pyspark.sql.functions.string_agg_distinct "Permalink to this definition")

Aggregate function: returns the concatenation of distinct non-null input values, separated by the delimiter.

An alias of [`listagg_distinct()`](about:blank/pyspark.sql.functions.listagg_distinct.html#pyspark.sql.functions.listagg_distinct "pyspark.sql.functions.listagg_distinct").

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

**delimiter**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column"), literal string or bytes, optional

the delimiter to separate the values. The default value is None.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Using string\_agg\_distinct function

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',), ('b',)], ['strings'])
>>> df.select(sf.string_agg_distinct('strings')).show()
+----------------------------------+
|string_agg(DISTINCT strings, NULL)|
+----------------------------------+
|                               abc|
+----------------------------------+

```


Example 2: Using string\_agg\_distinct function with a delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('a',), ('b',), (None,), ('c',), ('b',)], ['strings'])
>>> df.select(sf.string_agg_distinct('strings', ', ')).show()
+--------------------------------+
|string_agg(DISTINCT strings, , )|
+--------------------------------+
|                         a, b, c|
+--------------------------------+

```


Example 3: Using string\_agg\_distinct function with a binary column and delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(b'',), (b'',), (None,), (b'',), (b'',)],
...                            ['bytes'])
>>> df.select(sf.string_agg_distinct('bytes', b'B')).show()
+---------------------------------+
|string_agg(DISTINCT bytes, X'42')|
+---------------------------------+
|                 [01 42 02 42 03]|
+---------------------------------+

```


Example 4: Using string\_agg\_distinct function on a column with all None values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, StringType
>>> schema = StructType([StructField("strings", StringType(), True)])
>>> df = spark.createDataFrame([(None,), (None,), (None,), (None,)], schema=schema)
>>> df.select(sf.string_agg_distinct('strings')).show()
+----------------------------------+
|string_agg(DISTINCT strings, NULL)|
+----------------------------------+
|                              NULL|
+----------------------------------+

```

# pyspark.sql.functions.sum — PySpark 4.0.1 documentation
pyspark.sql.functions.sum(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sum)
[#](#pyspark.sql.functions.sum "Permalink to this definition")

Aggregate function: returns the sum of all values in the expression.

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Calculating the sum of values in a column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(10)
>>> df.select(sf.sum(df["id"])).show()
+-------+
|sum(id)|
+-------+
|     45|
+-------+

```


Example 2: Using a plus expression together to calculate the sum

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 2), (3, 4)], ["A", "B"])
>>> df.select(sf.sum(sf.col("A") + sf.col("B"))).show()
+------------+
|sum((A + B))|
+------------+
|          10|
+------------+

```


Example 3: Calculating the summation of ages with None

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, None), (1990, 2), (2000, 4)], ["birth", "age"])
>>> df.select(sf.sum("age")).show()
+--------+
|sum(age)|
+--------+
|       6|
+--------+

```



# pyspark.sql.functions.sum_distinct — PySpark 4.0.1 documentation
pyspark.sql.functions.sum\_distinct(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#sum_distinct)
[#](#pyspark.sql.functions.sum_distinct "Permalink to this definition")

Aggregate function: returns the sum of distinct values in the expression.

New in version 3.2.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for computed results.

Examples

Example 1: Using sum\_distinct function on a column with all distinct values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (2,), (3,), (4,)], ["numbers"])
>>> df.select(sf.sum_distinct('numbers')).show()
+---------------------+
|sum(DISTINCT numbers)|
+---------------------+
|                   10|
+---------------------+

```


Example 2: Using sum\_distinct function on a column with no distinct values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,), (1,), (1,), (1,)], ["numbers"])
>>> df.select(sf.sum_distinct('numbers')).show()
+---------------------+
|sum(DISTINCT numbers)|
+---------------------+
|                    1|
+---------------------+

```


Example 3: Using sum\_distinct function on a column with null and duplicate values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(None,), (1,), (1,), (2,)], ["numbers"])
>>> df.select(sf.sum_distinct('numbers')).show()
+---------------------+
|sum(DISTINCT numbers)|
+---------------------+
|                    3|
+---------------------+

```


Example 4: Using sum\_distinct function on a column with all None values

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import StructType, StructField, IntegerType
>>> schema = StructType([StructField("numbers", IntegerType(), True)])
>>> df = spark.createDataFrame([(None,), (None,), (None,), (None,)], schema=schema)
>>> df.select(sf.sum_distinct('numbers')).show()
+---------------------+
|sum(DISTINCT numbers)|
+---------------------+
|                 NULL|
+---------------------+

```

# pyspark.sql.functions.try_avg — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_avg(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_avg)
[#](#pyspark.sql.functions.try_avg "Permalink to this definition")

Returns the mean calculated from values of a group and the result is null on overflow.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Examples

Example 1: Calculating the average age

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, 15), (1990, 2)], ["birth", "age"])
>>> df.select(sf.try_avg("age")).show()
+------------+
|try_avg(age)|
+------------+
|         8.5|
+------------+

```


Example 2: Calculating the average age with None

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, None), (1990, 2), (2000, 4)], ["birth", "age"])
>>> df.select(sf.try_avg("age")).show()
+------------+
|try_avg(age)|
+------------+
|         3.0|
+------------+

```


Example 3: Overflow results in NULL when ANSI mode is on

```
>>> from decimal import Decimal
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     df = spark.createDataFrame(
...         [(Decimal("1" * 38),), (Decimal(0),)], "number DECIMAL(38, 0)")
...     df.select(sf.try_avg(df.number)).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+---------------+
|try_avg(number)|
+---------------+
|           NULL|
+---------------+

```


# pyspark.sql.functions.try_sum — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_sum(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_sum)
[#](#pyspark.sql.functions.try_sum "Permalink to this definition")

Returns the sum calculated from values of a group and the result is null on overflow.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Examples

Example 1: Calculating the sum of values in a column

```
>>> from pyspark.sql import functions as sf
>>> spark.range(10).select(sf.try_sum("id")).show()
+-----------+
|try_sum(id)|
+-----------+
|         45|
+-----------+

```


Example 2: Using a plus expression together to calculate the sum

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 2), (3, 4)], ["A", "B"])
>>> df.select(sf.try_sum(sf.col("A") + sf.col("B"))).show()
+----------------+
|try_sum((A + B))|
+----------------+
|              10|
+----------------+

```


Example 3: Calculating the summation of ages with None

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1982, None), (1990, 2), (2000, 4)], ["birth", "age"])
>>> df.select(sf.try_sum("age")).show()
+------------+
|try_sum(age)|
+------------+
|           6|
+------------+

```


Example 4: Overflow results in NULL when ANSI mode is on

```
>>> from decimal import Decimal
>>> import pyspark.sql.functions as sf
>>> origin = spark.conf.get("spark.sql.ansi.enabled")
>>> spark.conf.set("spark.sql.ansi.enabled", "true")
>>> try:
...     df = spark.createDataFrame([(Decimal("1" * 38),)] * 10, "number DECIMAL(38, 0)")
...     df.select(sf.try_sum(df.number)).show()
... finally:
...     spark.conf.set("spark.sql.ansi.enabled", origin)
+---------------+
|try_sum(number)|
+---------------+
|           NULL|
+---------------+

```

# pyspark.sql.functions.var_pop — PySpark 4.0.1 documentation
pyspark.sql.functions.var\_pop(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#var_pop)
[#](#pyspark.sql.functions.var_pop "Permalink to this definition")

Aggregate function: returns the population variance of the values in a group.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

variance of given column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(6)
>>> df.select(sf.var_pop(df.id)).show()
+------------------+
|       var_pop(id)|
+------------------+
|2.9166666666666...|
+------------------+

```

# pyspark.sql.functions.var_samp — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.var\_samp

pyspark.sql.functions.var\_samp(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#var_samp)
[#](#pyspark.sql.functions.var_samp "Permalink to this definition")

Aggregate function: returns the unbiased sample variance of the values in a group.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

variance of given column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(6)
>>> df.select(sf.var_samp(df.id)).show()
+------------+
|var_samp(id)|
+------------+
|         3.5|
+------------+

```


# pyspark.sql.functions.variance — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.variance

pyspark.sql.functions.variance(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#variance)
[#](#pyspark.sql.functions.variance "Permalink to this definition")

Aggregate function: alias for var\_samp

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

variance of given column.

See also

[`pyspark.sql.functions.var_pop()`](about:blank/pyspark.sql.functions.var_pop.html#pyspark.sql.functions.var_pop "pyspark.sql.functions.var_pop")

[`pyspark.sql.functions.var_samp()`](about:blank/pyspark.sql.functions.var_samp.html#pyspark.sql.functions.var_samp "pyspark.sql.functions.var_samp")

[`pyspark.sql.functions.stddev()`](about:blank/pyspark.sql.functions.stddev.html#pyspark.sql.functions.stddev "pyspark.sql.functions.stddev")

[`pyspark.sql.functions.skewness()`](about:blank/pyspark.sql.functions.skewness.html#pyspark.sql.functions.skewness "pyspark.sql.functions.skewness")

[`pyspark.sql.functions.kurtosis()`](about:blank/pyspark.sql.functions.kurtosis.html#pyspark.sql.functions.kurtosis "pyspark.sql.functions.kurtosis")

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(6)
>>> df.select(sf.variance(df.id)).show()
+------------+
|variance(id)|
+------------+
|         3.5|
+------------+

```




# pyspark.sql.functions.cume_dist — PySpark 4.0.1 documentation
pyspark.sql.functions.cume\_dist()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#cume_dist)
[#](#pyspark.sql.functions.cume_dist "Permalink to this definition")

Window function: returns the cumulative distribution of values within a window partition, i.e. the fraction of rows that are below the current row.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for calculating cumulative distribution.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame([1, 2, 3, 3, 4], "int")
>>> w = Window.orderBy("value")
>>> df.withColumn("cd", sf.cume_dist().over(w)).show()
+-----+---+
|value| cd|
+-----+---+
|    1|0.2|
|    2|0.4|
|    3|0.8|
|    3|0.8|
|    4|1.0|
+-----+---+

```

# pyspark.sql.functions.dense_rank — PySpark 4.0.1 documentation
pyspark.sql.functions.dense\_rank()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#dense_rank)
[#](#pyspark.sql.functions.dense_rank "Permalink to this definition")

Window function: returns the rank of rows within a window partition, without any gaps.

The difference between rank and dense\_rank is that dense\_rank leaves no gaps in ranking sequence when there are ties. That is, if you were ranking a competition using dense\_rank and had three people tie for second place, you would say that all three were in second place and that the next person came in third. Rank would give me sequential numbers, making the person that came in third place (after the ties) would register as coming in fifth.

This is equivalent to the DENSE\_RANK function in SQL.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for calculating ranks.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame([1, 1, 2, 3, 3, 4], "int")
>>> w = Window.orderBy("value")
>>> df.withColumn("drank", sf.dense_rank().over(w)).show()
+-----+-----+
|value|drank|
+-----+-----+
|    1|    1|
|    1|    1|
|    2|    2|
|    3|    3|
|    3|    3|
|    4|    4|
+-----+-----+

```

# pyspark.sql.functions.lag — PySpark 4.0.1 documentation
pyspark.sql.functions.lag(_col_, _offset\=1_, _default\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#lag)
[#](#pyspark.sql.functions.lag "Permalink to this definition")

Window function: returns the value that is offset rows before the current row, and default if there is less than offset rows before the current row. For example, an offset of one will return the previous row at any given point in the window partition.

This is equivalent to the LAG function in SQL.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

name of column or expression

**offset**int, optional default 1

number of row to extend

**default**optional

default value

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value before current row based on offset.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame(
...     [("a", 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["c1", "c2"])
>>> df.show()
+---+---+
| c1| c2|
+---+---+
|  a|  1|
|  a|  2|
|  a|  3|
|  b|  8|
|  b|  2|
+---+---+

```


```
>>> w = Window.partitionBy("c1").orderBy("c2")
>>> df.withColumn("previous_value", sf.lag("c2").over(w)).show()
+---+---+--------------+
| c1| c2|previous_value|
+---+---+--------------+
|  a|  1|          NULL|
|  a|  2|             1|
|  a|  3|             2|
|  b|  2|          NULL|
|  b|  8|             2|
+---+---+--------------+

```


```
>>> df.withColumn("previous_value", sf.lag("c2", 1, 0).over(w)).show()
+---+---+--------------+
| c1| c2|previous_value|
+---+---+--------------+
|  a|  1|             0|
|  a|  2|             1|
|  a|  3|             2|
|  b|  2|             0|
|  b|  8|             2|
+---+---+--------------+

```


```
>>> df.withColumn("previous_value", sf.lag("c2", 2, -1).over(w)).show()
+---+---+--------------+
| c1| c2|previous_value|
+---+---+--------------+
|  a|  1|            -1|
|  a|  2|            -1|
|  a|  3|             1|
|  b|  2|            -1|
|  b|  8|            -1|
+---+---+--------------+

```




# pyspark.sql.functions.lead — PySpark 4.0.1 documentation
pyspark.sql.functions.lead(_col_, _offset\=1_, _default\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#lead)
[#](#pyspark.sql.functions.lead "Permalink to this definition")

Window function: returns the value that is offset rows after the current row, and default if there is less than offset rows after the current row. For example, an offset of one will return the next row at any given point in the window partition.

This is equivalent to the LEAD function in SQL.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

name of column or expression

**offset**int, optional default 1

number of row to extend

**default**optional

default value

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value after current row based on offset.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame(
...     [("a", 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["c1", "c2"])
>>> df.show()
+---+---+
| c1| c2|
+---+---+
|  a|  1|
|  a|  2|
|  a|  3|
|  b|  8|
|  b|  2|
+---+---+

```


```
>>> w = Window.partitionBy("c1").orderBy("c2")
>>> df.withColumn("next_value", sf.lead("c2").over(w)).show()
+---+---+----------+
| c1| c2|next_value|
+---+---+----------+
|  a|  1|         2|
|  a|  2|         3|
|  a|  3|      NULL|
|  b|  2|         8|
|  b|  8|      NULL|
+---+---+----------+

```


```
>>> df.withColumn("next_value", sf.lead("c2", 1, 0).over(w)).show()
+---+---+----------+
| c1| c2|next_value|
+---+---+----------+
|  a|  1|         2|
|  a|  2|         3|
|  a|  3|         0|
|  b|  2|         8|
|  b|  8|         0|
+---+---+----------+

```


```
>>> df.withColumn("next_value", sf.lead("c2", 2, -1).over(w)).show()
+---+---+----------+
| c1| c2|next_value|
+---+---+----------+
|  a|  1|         3|
|  a|  2|        -1|
|  a|  3|        -1|
|  b|  2|        -1|
|  b|  8|        -1|
+---+---+----------+

```


# pyspark.sql.functions.nth_value — PySpark 4.0.1 documentation
pyspark.sql.functions.nth\_value(_col_, _offset_, _ignoreNulls\=False_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#nth_value)
[#](#pyspark.sql.functions.nth_value "Permalink to this definition")

Window function: returns the value that is the offsetth row of the window frame (counting from 1), and null if the size of window frame is less than offset rows.

It will return the offsetth non-null value it sees when ignoreNulls is set to true. If all values are null, then null is returned.

This is equivalent to the nth\_value function in SQL.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

name of column or expression

**offset**int

number of row to use as the value

**ignoreNulls**bool, optional

indicates the Nth value should skip null in the determination of which row to use

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

value of nth row.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame(
...     [("a", 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["c1", "c2"])
>>> df.show()
+---+---+
| c1| c2|
+---+---+
|  a|  1|
|  a|  2|
|  a|  3|
|  b|  8|
|  b|  2|
+---+---+

```


```
>>> w = Window.partitionBy("c1").orderBy("c2")
>>> df.withColumn("nth_value", sf.nth_value("c2", 1).over(w)).show()
+---+---+---------+
| c1| c2|nth_value|
+---+---+---------+
|  a|  1|        1|
|  a|  2|        1|
|  a|  3|        1|
|  b|  2|        2|
|  b|  8|        2|
+---+---+---------+

```


```
>>> df.withColumn("nth_value", sf.nth_value("c2", 2).over(w)).show()
+---+---+---------+
| c1| c2|nth_value|
+---+---+---------+
|  a|  1|     NULL|
|  a|  2|        2|
|  a|  3|        2|
|  b|  2|     NULL|
|  b|  8|        8|
+---+---+---------+

```


# pyspark.sql.functions.ntile — PySpark 4.0.1 documentation
pyspark.sql.functions.ntile(_n_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#ntile)
[#](#pyspark.sql.functions.ntile "Permalink to this definition")

Window function: returns the ntile group id (from 1 to n inclusive) in an ordered window partition. For example, if n is 4, the first quarter of the rows will get value 1, the second quarter will get 2, the third quarter will get 3, and the last quarter will get 4.

This is equivalent to the NTILE function in SQL.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**n**int

an integer

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

portioned group id.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame(
...     [("a", 1), ("a", 2), ("a", 3), ("b", 8), ("b", 2)], ["c1", "c2"])
>>> df.show()
+---+---+
| c1| c2|
+---+---+
|  a|  1|
|  a|  2|
|  a|  3|
|  b|  8|
|  b|  2|
+---+---+

```


```
>>> w = Window.partitionBy("c1").orderBy("c2")
>>> df.withColumn("ntile", sf.ntile(2).over(w)).show()
+---+---+-----+
| c1| c2|ntile|
+---+---+-----+
|  a|  1|    1|
|  a|  2|    1|
|  a|  3|    2|
|  b|  2|    1|
|  b|  8|    2|
+---+---+-----+

```



# pyspark.sql.functions.percent_rank — PySpark 4.0.1 documentation
pyspark.sql.functions.percent\_rank()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#percent_rank)
[#](#pyspark.sql.functions.percent_rank "Permalink to this definition")

Window function: returns the relative rank (i.e. percentile) of rows within a window partition.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for calculating relative rank.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame([1, 1, 2, 3, 3, 4], "int")
>>> w = Window.orderBy("value")
>>> df.withColumn("pr", sf.percent_rank().over(w)).show()
+-----+---+
|value| pr|
+-----+---+
|    1|0.0|
|    1|0.0|
|    2|0.4|
|    3|0.6|
|    3|0.6|
|    4|1.0|
+-----+---+

```


# pyspark.sql.functions.rank — PySpark 4.0.1 documentation
pyspark.sql.functions.rank()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#rank)
[#](#pyspark.sql.functions.rank "Permalink to this definition")

Window function: returns the rank of rows within a window partition.

The difference between rank and dense\_rank is that dense\_rank leaves no gaps in ranking sequence when there are ties. That is, if you were ranking a competition using dense\_rank and had three people tie for second place, you would say that all three were in second place and that the next person came in third. Rank would give me sequential numbers, making the person that came in third place (after the ties) would register as coming in fifth.

This is equivalent to the RANK function in SQL.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for calculating ranks.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.createDataFrame([1, 1, 2, 3, 3, 4], "int")
>>> w = Window.orderBy("value")
>>> df.withColumn("drank", sf.rank().over(w)).show()
+-----+-----+
|value|drank|
+-----+-----+
|    1|    1|
|    1|    1|
|    2|    3|
|    3|    4|
|    3|    4|
|    4|    6|
+-----+-----+

```

# pyspark.sql.functions.row_number — PySpark 4.0.1 documentation
pyspark.sql.functions.row\_number()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#row_number)
[#](#pyspark.sql.functions.row_number "Permalink to this definition")

Window function: returns a sequential number starting at 1 within a window partition.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the column for calculating row numbers.

Examples

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql import Window
>>> df = spark.range(3)
>>> w = Window.orderBy(df.id.desc())
>>> df.withColumn("desc_order", sf.row_number().over(w)).show()
+---+----------+
| id|desc_order|
+---+----------+
|  2|         1|
|  1|         2|
|  0|         3|
+---+----------+

```


# pyspark.sql.functions.explode — PySpark 4.0.1 documentation
pyspark.sql.functions.explode(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#explode)
[#](#pyspark.sql.functions.explode "Permalink to this definition")

Returns a new row for each element in the given array or map. Uses the default column name col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 1.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

One row per array item or map key value.

Notes

Only one explode is allowed per SELECT clause.

Examples

Example 1: Exploding an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,ARRAY(1,2,3,NULL)), (2,ARRAY()), (3,NULL) AS t(i,a)')
>>> df.show()
+---+---------------+
|  i|              a|
+---+---------------+
|  1|[1, 2, 3, NULL]|
|  2|             []|
|  3|           NULL|
+---+---------------+

```


```
>>> df.select('*', sf.explode('a')).show()
+---+---------------+----+
|  i|              a| col|
+---+---------------+----+
|  1|[1, 2, 3, NULL]|   1|
|  1|[1, 2, 3, NULL]|   2|
|  1|[1, 2, 3, NULL]|   3|
|  1|[1, 2, 3, NULL]|NULL|
+---+---------------+----+

```


Example 2: Exploding a map column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,MAP(1,2,3,4,5,NULL)), (2,MAP()), (3,NULL) AS t(i,m)')
>>> df.show(truncate=False)
+---+---------------------------+
|i  |m                          |
+---+---------------------------+
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|
|2  |{}                         |
|3  |NULL                       |
+---+---------------------------+

```


```
>>> df.select('*', sf.explode('m')).show(truncate=False)
+---+---------------------------+---+-----+
|i  |m                          |key|value|
+---+---------------------------+---+-----+
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|1  |2    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|3  |4    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|5  |NULL |
+---+---------------------------+---+-----+

```


Example 3: Exploding multiple array columns

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT ARRAY(1,2) AS a1, ARRAY(3,4,5) AS a2')
>>> df.select(
...     '*', sf.explode('a1').alias('v1')
... ).select('*', sf.explode('a2').alias('v2')).show()
+------+---------+---+---+
|    a1|       a2| v1| v2|
+------+---------+---+---+
|[1, 2]|[3, 4, 5]|  1|  3|
|[1, 2]|[3, 4, 5]|  1|  4|
|[1, 2]|[3, 4, 5]|  1|  5|
|[1, 2]|[3, 4, 5]|  2|  3|
|[1, 2]|[3, 4, 5]|  2|  4|
|[1, 2]|[3, 4, 5]|  2|  5|
+------+---------+---+---+

```


Example 4: Exploding an array of struct column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT ARRAY(NAMED_STRUCT("a",1,"b",2), NAMED_STRUCT("a",3,"b",4)) AS a')
>>> df.select(sf.explode('a').alias("s")).select("s.*").show()
+---+---+
|  a|  b|
+---+---+
|  1|  2|
|  3|  4|
+---+---+

```



# pyspark.sql.functions.explode_outer — PySpark 4.0.1 documentation
pyspark.sql.functions.explode\_outer(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#explode_outer)
[#](#pyspark.sql.functions.explode_outer "Permalink to this definition")

Returns a new row for each element in the given array or map. Unlike explode, if the array/map is null or empty then null is produced. Uses the default column name col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

one row per array item or map key value.

Examples

Example 1: Using an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,ARRAY(1,2,3,NULL)), (2,ARRAY()), (3,NULL) AS t(i,a)')
>>> df.select('*', sf.explode_outer('a')).show()
+---+---------------+----+
|  i|              a| col|
+---+---------------+----+
|  1|[1, 2, 3, NULL]|   1|
|  1|[1, 2, 3, NULL]|   2|
|  1|[1, 2, 3, NULL]|   3|
|  1|[1, 2, 3, NULL]|NULL|
|  2|             []|NULL|
|  3|           NULL|NULL|
+---+---------------+----+

```


Example 2: Using a map column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,MAP(1,2,3,4,5,NULL)), (2,MAP()), (3,NULL) AS t(i,m)')
>>> df.select('*', sf.explode_outer('m')).show(truncate=False)
+---+---------------------------+----+-----+
|i  |m                          |key |value|
+---+---------------------------+----+-----+
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|1   |2    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|3   |4    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|5   |NULL |
|2  |{}                         |NULL|NULL |
|3  |NULL                       |NULL|NULL |
+---+---------------------------+----+-----+

```
# pyspark.sql.functions.inline — PySpark 4.0.1 documentation
pyspark.sql.functions.inline(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#inline)
[#](#pyspark.sql.functions.inline "Permalink to this definition")

Explodes an array of structs into a table.

This function takes an input column containing an array of structs and returns a new column where each struct in the array is exploded into a separate row.

New in version 3.4.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Input column of values to explode.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Generator expression with the inline exploded result.

Examples

Example 1: Using inline with a single struct array column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT ARRAY(NAMED_STRUCT("a",1,"b",2), NAMED_STRUCT("a",3,"b",4)) AS a')
>>> df.select('*', sf.inline(df.a)).show()
+----------------+---+---+
|               a|  a|  b|
+----------------+---+---+
|[{1, 2}, {3, 4}]|  1|  2|
|[{1, 2}, {3, 4}]|  3|  4|
+----------------+---+---+

```


Example 2: Using inline with a column name

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT ARRAY(NAMED_STRUCT("a",1,"b",2), NAMED_STRUCT("a",3,"b",4)) AS a')
>>> df.select('*', sf.inline('a')).show()
+----------------+---+---+
|               a|  a|  b|
+----------------+---+---+
|[{1, 2}, {3, 4}]|  1|  2|
|[{1, 2}, {3, 4}]|  3|  4|
+----------------+---+---+

```


Example 3: Using inline with an alias

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT ARRAY(NAMED_STRUCT("a",1,"b",2), NAMED_STRUCT("a",3,"b",4)) AS a')
>>> df.select('*', sf.inline('a').alias("c1", "c2")).show()
+----------------+---+---+
|               a| c1| c2|
+----------------+---+---+
|[{1, 2}, {3, 4}]|  1|  2|
|[{1, 2}, {3, 4}]|  3|  4|
+----------------+---+---+

```


Example 4: Using inline with multiple struct array columns

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT ARRAY(NAMED_STRUCT("a",1,"b",2), NAMED_STRUCT("a",3,"b",4)) AS a1, ARRAY(NAMED_STRUCT("c",5,"d",6), NAMED_STRUCT("c",7,"d",8)) AS a2')
>>> df.select(
...     '*', sf.inline('a1')
... ).select('*', sf.inline('a2')).show()
+----------------+----------------+---+---+---+---+
|              a1|              a2|  a|  b|  c|  d|
+----------------+----------------+---+---+---+---+
|[{1, 2}, {3, 4}]|[{5, 6}, {7, 8}]|  1|  2|  5|  6|
|[{1, 2}, {3, 4}]|[{5, 6}, {7, 8}]|  1|  2|  7|  8|
|[{1, 2}, {3, 4}]|[{5, 6}, {7, 8}]|  3|  4|  5|  6|
|[{1, 2}, {3, 4}]|[{5, 6}, {7, 8}]|  3|  4|  7|  8|
+----------------+----------------+---+---+---+---+

```


Example 5: Using inline with a nested struct array column

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql('SELECT NAMED_STRUCT("a",1,"b",2,"c",ARRAY(NAMED_STRUCT("c",3,"d",4), NAMED_STRUCT("c",5,"d",6))) AS s')
>>> df.select('*', sf.inline('s.c')).show(truncate=False)
+------------------------+---+---+
|s                       |c  |d  |
+------------------------+---+---+
|{1, 2, [{3, 4}, {5, 6}]}|3  |4  |
|{1, 2, [{3, 4}, {5, 6}]}|5  |6  |
+------------------------+---+---+

```


Example 6: Using inline with a column containing: array continaing null, empty array and null

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,ARRAY(NAMED_STRUCT("a",1,"b",2), NULL, NAMED_STRUCT("a",3,"b",4))), (2,ARRAY()), (3,NULL) AS t(i,s)')
>>> df.show(truncate=False)
+---+----------------------+
|i  |s                     |
+---+----------------------+
|1  |[{1, 2}, NULL, {3, 4}]|
|2  |[]                    |
|3  |NULL                  |
+---+----------------------+

```


```
>>> df.select('*', sf.inline('s')).show(truncate=False)
+---+----------------------+----+----+
|i  |s                     |a   |b   |
+---+----------------------+----+----+
|1  |[{1, 2}, NULL, {3, 4}]|1   |2   |
|1  |[{1, 2}, NULL, {3, 4}]|NULL|NULL|
|1  |[{1, 2}, NULL, {3, 4}]|3   |4   |
+---+----------------------+----+----+

```



# pyspark.sql.functions.inline_outer — PySpark 4.0.1 documentation
pyspark.sql.functions.inline\_outer(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#inline_outer)
[#](#pyspark.sql.functions.inline_outer "Permalink to this definition")

Explodes an array of structs into a table. Unlike inline, if the array is null or empty then null is produced for each nested column.

New in version 3.4.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

input column of values to explode.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

generator expression with the inline exploded result.

Notes

Supports Spark Connect.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,ARRAY(NAMED_STRUCT("a",1,"b",2), NULL, NAMED_STRUCT("a",3,"b",4))), (2,ARRAY()), (3,NULL) AS t(i,s)')
>>> df.printSchema()
root
 |-- i: integer (nullable = false)
 |-- s: array (nullable = true)
 |    |-- element: struct (containsNull = true)
 |    |    |-- a: integer (nullable = false)
 |    |    |-- b: integer (nullable = false)

```


```
>>> df.select('*', sf.inline_outer('s')).show(truncate=False)
+---+----------------------+----+----+
|i  |s                     |a   |b   |
+---+----------------------+----+----+
|1  |[{1, 2}, NULL, {3, 4}]|1   |2   |
|1  |[{1, 2}, NULL, {3, 4}]|NULL|NULL|
|1  |[{1, 2}, NULL, {3, 4}]|3   |4   |
|2  |[]                    |NULL|NULL|
|3  |NULL                  |NULL|NULL|
+---+----------------------+----+----+

```



# pyspark.sql.functions.posexplode — PySpark 4.0.1 documentation
pyspark.sql.functions.posexplode(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#posexplode)
[#](#pyspark.sql.functions.posexplode "Permalink to this definition")

Returns a new row for each element with position in the given array or map. Uses the default column name pos for position, and col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

one row per array item or map key value including positions as a separate column.

Examples

Example 1: Exploding an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,ARRAY(1,2,3,NULL)), (2,ARRAY()), (3,NULL) AS t(i,a)')
>>> df.show()
+---+---------------+
|  i|              a|
+---+---------------+
|  1|[1, 2, 3, NULL]|
|  2|             []|
|  3|           NULL|
+---+---------------+

```


```
>>> df.select('*', sf.posexplode('a')).show()
+---+---------------+---+----+
|  i|              a|pos| col|
+---+---------------+---+----+
|  1|[1, 2, 3, NULL]|  0|   1|
|  1|[1, 2, 3, NULL]|  1|   2|
|  1|[1, 2, 3, NULL]|  2|   3|
|  1|[1, 2, 3, NULL]|  3|NULL|
+---+---------------+---+----+

```


Example 2: Exploding a map column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,MAP(1,2,3,4,5,NULL)), (2,MAP()), (3,NULL) AS t(i,m)')
>>> df.show(truncate=False)
+---+---------------------------+
|i  |m                          |
+---+---------------------------+
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|
|2  |{}                         |
|3  |NULL                       |
+---+---------------------------+

```


```
>>> df.select('*', sf.posexplode('m')).show(truncate=False)
+---+---------------------------+---+---+-----+
|i  |m                          |pos|key|value|
+---+---------------------------+---+---+-----+
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|0  |1  |2    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|1  |3  |4    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|2  |5  |NULL |
+---+---------------------------+---+---+-----+

```


# pyspark.sql.functions.posexplode_outer — PySpark 4.0.1 documentation
pyspark.sql.functions.posexplode\_outer(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#posexplode_outer)
[#](#pyspark.sql.functions.posexplode_outer "Permalink to this definition")

Returns a new row for each element with position in the given array or map. Unlike posexplode, if the array/map is null or empty then the row (null, null) is produced. Uses the default column name pos for position, and col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

target column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

one row per array item or map key value including positions as a separate column.

Examples

Example 1: Using an array column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,ARRAY(1,2,3,NULL)), (2,ARRAY()), (3,NULL) AS t(i,a)')
>>> df.select('*', sf.posexplode_outer('a')).show()
+---+---------------+----+----+
|  i|              a| pos| col|
+---+---------------+----+----+
|  1|[1, 2, 3, NULL]|   0|   1|
|  1|[1, 2, 3, NULL]|   1|   2|
|  1|[1, 2, 3, NULL]|   2|   3|
|  1|[1, 2, 3, NULL]|   3|NULL|
|  2|             []|NULL|NULL|
|  3|           NULL|NULL|NULL|
+---+---------------+----+----+

```


Example 2: Using a map column

```
>>> from pyspark.sql import functions as sf
>>> df = spark.sql('SELECT * FROM VALUES (1,MAP(1,2,3,4,5,NULL)), (2,MAP()), (3,NULL) AS t(i,m)')
>>> df.select('*', sf.posexplode_outer('m')).show(truncate=False)
+---+---------------------------+----+----+-----+
|i  |m                          |pos |key |value|
+---+---------------------------+----+----+-----+
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|0   |1   |2    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|1   |3   |4    |
|1  |{1 -> 2, 3 -> 4, 5 -> NULL}|2   |5   |NULL |
|2  |{}                         |NULL|NULL|NULL |
|3  |NULL                       |NULL|NULL|NULL |
+---+---------------------------+----+----+-----+

```

# pyspark.sql.functions.stack — PySpark 4.0.1 documentation
pyspark.sql.functions.stack(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#stack)
[#](#pyspark.sql.functions.stack "Permalink to this definition")

Separates col1, …, colk into n rows. Uses column names col0, col1, etc. by default unless specified otherwise.

New in version 3.5.0.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the first element should be a literal int for the number of rows to be separated, and the remaining are input elements to be separated.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1, 2, 3)], ['a', 'b', 'c'])
>>> df.select('*', sf.stack(sf.lit(2), df.a, df.b, 'c')).show()
+---+---+---+----+----+
|  a|  b|  c|col0|col1|
+---+---+---+----+----+
|  1|  2|  3|   1|   2|
|  1|  2|  3|   3|NULL|
+---+---+---+----+----+

```


```
>>> df.select('*', sf.stack(sf.lit(2), df.a, df.b, 'c').alias('x', 'y')).show()
+---+---+---+---+----+
|  a|  b|  c|  x|   y|
+---+---+---+---+----+
|  1|  2|  3|  1|   2|
|  1|  2|  3|  3|NULL|
+---+---+---+---+----+

```


```
>>> df.select('*', sf.stack(sf.lit(3), df.a, df.b, 'c')).show()
+---+---+---+----+
|  a|  b|  c|col0|
+---+---+---+----+
|  1|  2|  3|   1|
|  1|  2|  3|   2|
|  1|  2|  3|   3|
+---+---+---+----+

```


```
>>> df.select('*', sf.stack(sf.lit(4), df.a, df.b, 'c')).show()
+---+---+---+----+
|  a|  b|  c|col0|
+---+---+---+----+
|  1|  2|  3|   1|
|  1|  2|  3|   2|
|  1|  2|  3|   3|
|  1|  2|  3|NULL|
+---+---+---+----+

```


# pyspark.sql.functions.partitioning.years — PySpark 4.0.1 documentation
pyspark.sql.functions.partitioning.years(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/partitioning.html#years)
[#](#pyspark.sql.functions.partitioning.years "Permalink to this definition")

Partition transform function: A transform for timestamps and dates to partition data into years.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target date or timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

data partitioned by years.

Notes

This function can be used only in combination with `partitionedBy()` method of the DataFrameWriterV2.

Examples

```
>>> df.writeTo("catalog.db.table").partitionedBy(  
...     partitioning.years("ts")
... ).createOrReplace()

```



# pyspark.sql.functions.partitioning.months — PySpark 4.0.1 documentation
pyspark.sql.functions.partitioning.months(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/partitioning.html#months)
[#](#pyspark.sql.functions.partitioning.months "Permalink to this definition")

Partition transform function: A transform for timestamps and dates to partition data into months.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target date or timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

data partitioned by months.

Notes

This function can be used only in combination with `partitionedBy()` method of the DataFrameWriterV2.

Examples

```
>>> df.writeTo("catalog.db.table").partitionedBy(
...     partitioning.months("ts")
... ).createOrReplace()  

```



# pyspark.sql.functions.partitioning.days — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.partitioning.days

pyspark.sql.functions.partitioning.days(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/partitioning.html#days)
[#](#pyspark.sql.functions.partitioning.days "Permalink to this definition")

Partition transform function: A transform for timestamps and dates to partition data into days.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target date or timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

data partitioned by days.

Notes

This function can be used only in combination with `partitionedBy()` method of the DataFrameWriterV2.

Examples

```
>>> df.writeTo("catalog.db.table").partitionedBy(  
...     partitioning.days("ts")
... ).createOrReplace()

```


# pyspark.sql.functions.partitioning.hours — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.partitioning.hours

pyspark.sql.functions.partitioning.hours(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/partitioning.html#hours)
[#](#pyspark.sql.functions.partitioning.hours "Permalink to this definition")

Partition transform function: A transform for timestamps to partition data into hours.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target date or timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

data partitioned by hours.

Notes

This function can be used only in combination with `partitionedBy()` method of the DataFrameWriterV2.

Examples

```
>>> df.writeTo("catalog.db.table").partitionedBy(   
...     partitioning.hours("ts")
... ).createOrReplace()

```


# pyspark.sql.functions.partitioning.bucket — PySpark 4.0.1 documentation
pyspark.sql.functions.partitioning.bucket(_numBuckets_, _col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/partitioning.html#bucket)
[#](#pyspark.sql.functions.partitioning.bucket "Permalink to this definition")

Partition transform function: A transform for any type that partitions by a hash of the input column.

New in version 4.0.0.

Parameters

**numBuckets**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or int

the number of buckets

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

target date or timestamp column to work on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

data partitioned by given columns.

Notes

This function can be used only in combination with `partitionedBy()` method of the DataFrameWriterV2.

Examples

```
>>> df.writeTo("catalog.db.table").partitionedBy(  
...     partitioning.bucket(42, "ts")
... ).createOrReplace()

```


# pyspark.sql.functions.from_csv — PySpark 4.0.1 documentation
pyspark.sql.functions.from\_csv(_col_, _schema_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#from_csv)
[#](#pyspark.sql.functions.from_csv "Permalink to this definition")

CSV Function: Parses a column containing a CSV string into a row with the specified schema. Returns null if the string cannot be parsed.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column or column name in CSV format.

**schema**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column, or Python string literal with schema in DDL format, to use when parsing the CSV column.

**options**dict, optional

Options to control parsing. Accepts the same options as the CSV datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A column of parsed CSV values.

Examples

Example 1: Parsing a simple CSV string

```
>>> from pyspark.sql import functions as sf
>>> data = [("1,2,3",)]
>>> df = spark.createDataFrame(data, ("value",))
>>> df.select(sf.from_csv(df.value, "a INT, b INT, c INT")).show()
+---------------+
|from_csv(value)|
+---------------+
|      {1, 2, 3}|
+---------------+

```


Example 2: Using schema\_of\_csv to infer the schema

```
>>> from pyspark.sql import functions as sf
>>> data = [("1,2,3",)]
>>> value = data[0][0]
>>> df.select(sf.from_csv(df.value, sf.schema_of_csv(value))).show()
+---------------+
|from_csv(value)|
+---------------+
|      {1, 2, 3}|
+---------------+

```


Example 3: Ignoring leading white space in the CSV string

```
>>> from pyspark.sql import functions as sf
>>> data = [("   abc",)]
>>> df = spark.createDataFrame(data, ("value",))
>>> options = {'ignoreLeadingWhiteSpace': True}
>>> df.select(sf.from_csv(df.value, "s string", options)).show()
+---------------+
|from_csv(value)|
+---------------+
|          {abc}|
+---------------+

```


Example 4: Parsing a CSV string with a missing value

```
>>> from pyspark.sql import functions as sf
>>> data = [("1,2,",)]
>>> df = spark.createDataFrame(data, ("value",))
>>> df.select(sf.from_csv(df.value, "a INT, b INT, c INT")).show()
+---------------+
|from_csv(value)|
+---------------+
|   {1, 2, NULL}|
+---------------+

```


Example 5: Parsing a CSV string with a different delimiter

```
>>> from pyspark.sql import functions as sf
>>> data = [("1;2;3",)]
>>> df = spark.createDataFrame(data, ("value",))
>>> options = {'delimiter': ';'}
>>> df.select(sf.from_csv(df.value, "a INT, b INT, c INT", options)).show()
+---------------+
|from_csv(value)|
+---------------+
|      {1, 2, 3}|
+---------------+

```


# pyspark.sql.functions.schema_of_csv — PySpark 4.0.1 documentation
pyspark.sql.functions.schema\_of\_csv(_csv_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#schema_of_csv)
[#](#pyspark.sql.functions.schema_of_csv "Permalink to this definition")

CSV Function: Parses a CSV string and infers its schema in DDL format.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**csv**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A CSV string or a foldable string column containing a CSV string.

**options**dict, optional

Options to control parsing. Accepts the same options as the CSV datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A string representation of a `StructType` parsed from the given CSV.

Examples

Example 1: Inferring the schema of a CSV string with different data types

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(1)
>>> df.select(sf.schema_of_csv(sf.lit('1|a|true'), {'sep':'|'})).show(truncate=False)
+-------------------------------------------+
|schema_of_csv(1|a|true)                    |
+-------------------------------------------+
|STRUCT<_c0: INT, _c1: STRING, _c2: BOOLEAN>|
+-------------------------------------------+

```


Example 2: Inferring the schema of a CSV string with missing values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(1)
>>> df.select(sf.schema_of_csv(sf.lit('1||true'), {'sep':'|'})).show(truncate=False)
+-------------------------------------------+
|schema_of_csv(1||true)                     |
+-------------------------------------------+
|STRUCT<_c0: INT, _c1: STRING, _c2: BOOLEAN>|
+-------------------------------------------+

```


Example 3: Inferring the schema of a CSV string with a different delimiter

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(1)
>>> df.select(sf.schema_of_csv(sf.lit('1;a;true'), {'sep':';'})).show(truncate=False)
+-------------------------------------------+
|schema_of_csv(1;a;true)                    |
+-------------------------------------------+
|STRUCT<_c0: INT, _c1: STRING, _c2: BOOLEAN>|
+-------------------------------------------+

```


Example 4: Inferring the schema of a CSV string with quoted fields

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(1)
>>> df.select(sf.schema_of_csv(sf.lit('"1","a","true"'), {'sep':','})).show(truncate=False)
+-------------------------------------------+
|schema_of_csv("1","a","true")              |
+-------------------------------------------+
|STRUCT<_c0: INT, _c1: STRING, _c2: BOOLEAN>|
+-------------------------------------------+

```


# pyspark.sql.functions.to_csv — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_csv(_col_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_csv)
[#](#pyspark.sql.functions.to_csv "Permalink to this definition")

CSV Function: Converts a column containing a `StructType` into a CSV string. Throws an exception, in the case of an unsupported type.

New in version 3.0.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

Name of column containing a struct.

**options: dict, optional**

Options to control converting. Accepts the same options as the CSV datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-csv.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A CSV string converted from the given `StructType`.

Examples

Example 1: Converting a simple StructType to a CSV string

```
>>> from pyspark.sql import Row, functions as sf
>>> data = [(1, Row(age=2, name='Alice'))]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> df.select(sf.to_csv(df.value)).show()
+-------------+
|to_csv(value)|
+-------------+
|      2,Alice|
+-------------+

```


Example 2: Converting a complex StructType to a CSV string

```
>>> from pyspark.sql import Row, functions as sf
>>> data = [(1, Row(age=2, name='Alice', scores=[100, 200, 300]))]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> df.select(sf.to_csv(df.value)).show(truncate=False)
+-------------------------+
|to_csv(value)            |
+-------------------------+
|2,Alice,"[100, 200, 300]"|
+-------------------------+

```


Example 3: Converting a StructType with null values to a CSV string

```
>>> from pyspark.sql import Row, functions as sf
>>> from pyspark.sql.types import StructType, StructField, IntegerType, StringType
>>> data = [(1, Row(age=None, name='Alice'))]
>>> schema = StructType([
...   StructField("key", IntegerType(), True),
...   StructField("value", StructType([
...     StructField("age", IntegerType(), True),
...     StructField("name", StringType(), True)
...   ]), True)
... ])
>>> df = spark.createDataFrame(data, schema)
>>> df.select(sf.to_csv(df.value)).show()
+-------------+
|to_csv(value)|
+-------------+
|       ,Alice|
+-------------+

```


Example 4: Converting a StructType with different data types to a CSV string

```
>>> from pyspark.sql import Row, functions as sf
>>> data = [(1, Row(age=2, name='Alice', isStudent=True))]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> df.select(sf.to_csv(df.value)).show()
+-------------+
|to_csv(value)|
+-------------+
| 2,Alice,true|
+-------------+

```



# pyspark.sql.functions.from_json — PySpark 4.0.1 documentation
pyspark.sql.functions.from\_json(_col_, _schema_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#from_json)
[#](#pyspark.sql.functions.from_json "Permalink to this definition")

Parses a column containing a JSON string into a `MapType` with `StringType` as keys type, `StructType` or `ArrayType` with the specified schema. Returns null, in the case of an unparsable string.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column or column name in JSON format

**schema**`DataType` or str

a StructType, ArrayType of StructType or Python string literal with a DDL-formatted string to use when parsing the json column

**options**dict, optional

options to control parsing. accepts the same options as the json datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new column of complex type from given JSON object.

Examples

Example 1: Parsing JSON with a specified schema

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql.types import StructType, StructField, IntegerType
>>> schema = StructType([StructField("a", IntegerType())])
>>> df = spark.createDataFrame([(1, '''{"a": 1}''')], ("key", "value"))
>>> df.select(sf.from_json(df.value, schema).alias("json")).show()
+----+
|json|
+----+
| {1}|
+----+

```


Example 2: Parsing JSON with a DDL-formatted string.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, '''{"a": 1}''')], ("key", "value"))
>>> df.select(sf.from_json(df.value, "a INT").alias("json")).show()
+----+
|json|
+----+
| {1}|
+----+

```


Example 3: Parsing JSON into a MapType

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, '''{"a": 1}''')], ("key", "value"))
>>> df.select(sf.from_json(df.value, "MAP<STRING,INT>").alias("json")).show()
+--------+
|    json|
+--------+
|{a -> 1}|
+--------+

```


Example 4: Parsing JSON into an ArrayType of StructType

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql.types import ArrayType, StructType, StructField, IntegerType
>>> schema = ArrayType(StructType([StructField("a", IntegerType())]))
>>> df = spark.createDataFrame([(1, '''[{"a": 1}]''')], ("key", "value"))
>>> df.select(sf.from_json(df.value, schema).alias("json")).show()
+-----+
| json|
+-----+
|[{1}]|
+-----+

```


Example 5: Parsing JSON into an ArrayType

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql.types import ArrayType, IntegerType
>>> schema = ArrayType(IntegerType())
>>> df = spark.createDataFrame([(1, '''[1, 2, 3]''')], ("key", "value"))
>>> df.select(sf.from_json(df.value, schema).alias("json")).show()
+---------+
|     json|
+---------+
|[1, 2, 3]|
+---------+

```


Example 6: Parsing JSON with specified options

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, '''{a:123}'''), (2, '''{"a":456}''')], ("key", "value"))
>>> parsed1 = sf.from_json(df.value, "a INT")
>>> parsed2 = sf.from_json(df.value, "a INT", {"allowUnquotedFieldNames": "true"})
>>> df.select("value", parsed1, parsed2).show()
+---------+----------------+----------------+
|    value|from_json(value)|from_json(value)|
+---------+----------------+----------------+
|  {a:123}|          {NULL}|           {123}|
|{"a":456}|           {456}|           {456}|
+---------+----------------+----------------+

```
# pyspark.sql.functions.get_json_object — PySpark 4.0.1 documentation
pyspark.sql.functions.get\_json\_object(_col_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#get_json_object)
[#](#pyspark.sql.functions.get_json_object "Permalink to this definition")

Extracts json object from a json string based on json path specified, and returns json string of the extracted json object. It will return null if the input json string is invalid.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

string column in json format

**path**str

path to the json object to extract

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string representation of given JSON object value.

Examples

```
>>> data = [("1", '''{"f1": "value1", "f2": "value2"}'''), ("2", '''{"f1": "value12"}''')]
>>> df = spark.createDataFrame(data, ("key", "jstring"))
>>> df.select(df.key, get_json_object(df.jstring, '$.f1').alias("c0"), \
...                   get_json_object(df.jstring, '$.f2').alias("c1") ).collect()
[Row(key='1', c0='value1', c1='value2'), Row(key='2', c0='value12', c1=None)]

```


# pyspark.sql.functions.json_array_length — PySpark 4.0.1 documentation
pyspark.sql.functions.json\_array\_length(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#json_array_length)
[#](#pyspark.sql.functions.json_array_length "Permalink to this definition")

Returns the number of elements in the outermost JSON array. NULL is returned in case of any other valid JSON string, NULL or an invalid JSON.

New in version 3.5.0.

Parameters

**col: :class:\`~pyspark.sql.Column\` or str**

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

length of json array.

Examples

```
>>> df = spark.createDataFrame([(None,), ('[1, 2, 3]',), ('[]',)], ['data'])
>>> df.select(json_array_length(df.data).alias('r')).collect()
[Row(r=None), Row(r=3), Row(r=0)]

```



# pyspark.sql.functions.json_object_keys — PySpark 4.0.1 documentation
pyspark.sql.functions.json\_object\_keys(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#json_object_keys)
[#](#pyspark.sql.functions.json_object_keys "Permalink to this definition")

Returns all the keys of the outermost JSON object as an array. If a valid JSON object is given, all the keys of the outermost object will be returned as an array. If it is any other valid JSON string, an invalid JSON string or an empty string, the function returns null.

New in version 3.5.0.

Parameters

**col: :class:\`~pyspark.sql.Column\` or str**

target column to compute on.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

all the keys of the outermost JSON object.

Examples

```
>>> df = spark.createDataFrame([(None,), ('{}',), ('{"key1":1, "key2":2}',)], ['data'])
>>> df.select(json_object_keys(df.data).alias('r')).collect()
[Row(r=None), Row(r=[]), Row(r=['key1', 'key2'])]

```


# pyspark.sql.functions.json_tuple — PySpark 4.0.1 documentation
pyspark.sql.functions.json\_tuple(_col_, _\*fields_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#json_tuple)
[#](#pyspark.sql.functions.json_tuple "Permalink to this definition")

Creates a new row for a json column according to the given field names.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

string column in json format

**fields**str

a field or fields to extract

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new row for each given field value from json object

Examples

```
>>> data = [("1", '''{"f1": "value1", "f2": "value2"}'''), ("2", '''{"f1": "value12"}''')]
>>> df = spark.createDataFrame(data, ("key", "jstring"))
>>> df.select(df.key, json_tuple(df.jstring, 'f1', 'f2')).collect()
[Row(key='1', c0='value1', c1='value2'), Row(key='2', c0='value12', c1=None)]

```


# pyspark.sql.functions.schema_of_json — PySpark 4.0.1 documentation
pyspark.sql.functions.schema\_of\_json(_json_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#schema_of_json)
[#](#pyspark.sql.functions.schema_of_json "Permalink to this definition")

Parses a JSON string and infers its schema in DDL format.

New in version 2.4.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**json**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a JSON string or a foldable string column containing a JSON string.

**options**dict, optional

options to control parsing. accepts the same options as the JSON datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option) for the version you use.

Changed in version 3.0.0: It accepts options parameter to control schema inferring.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a string representation of a `StructType` parsed from given JSON.

Examples

```
>>> import pyspark.sql.functions as sf
>>> parsed1 = sf.schema_of_json(sf.lit('{"a": 0}'))
>>> parsed2 = sf.schema_of_json('{a: 1}', {'allowUnquotedFieldNames':'true'})
>>> spark.range(1).select(parsed1, parsed2).show()
+------------------------+----------------------+
|schema_of_json({"a": 0})|schema_of_json({a: 1})|
+------------------------+----------------------+
|       STRUCT<a: BIGINT>|     STRUCT<a: BIGINT>|
+------------------------+----------------------+

```


# pyspark.sql.functions.to_json — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_json(_col_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_json)
[#](#pyspark.sql.functions.to_json "Permalink to this definition")

Converts a column containing a `StructType`, `ArrayType` or a `MapType` into a JSON string. Throws an exception, in the case of an unsupported type.

New in version 2.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing a struct, an array or a map.

**options**dict, optional

options to control converting. accepts the same options as the JSON datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-json.html#data-source-option) for the version you use. Additionally the function supports the pretty option which enables pretty JSON generation.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

JSON object as string column.

Examples

Example 1: Converting a StructType column to JSON

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql import Row
>>> data = [(1, Row(age=2, name='Alice'))]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> df.select(sf.to_json(df.value).alias("json")).show(truncate=False)
+------------------------+
|json                    |
+------------------------+
|{"age":2,"name":"Alice"}|
+------------------------+

```


Example 2: Converting an ArrayType column to JSON

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql import Row
>>> data = [(1, [Row(age=2, name='Alice'), Row(age=3, name='Bob')])]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> df.select(sf.to_json(df.value).alias("json")).show(truncate=False)
+-------------------------------------------------+
|json                                             |
+-------------------------------------------------+
|[{"age":2,"name":"Alice"},{"age":3,"name":"Bob"}]|
+-------------------------------------------------+

```


Example 3: Converting a MapType column to JSON

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, {"name": "Alice"})], ("key", "value"))
>>> df.select(sf.to_json(df.value).alias("json")).show(truncate=False)
+----------------+
|json            |
+----------------+
|{"name":"Alice"}|
+----------------+

```


Example 4: Converting a nested MapType column to JSON

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, [{"name": "Alice"}, {"name": "Bob"}])], ("key", "value"))
>>> df.select(sf.to_json(df.value).alias("json")).show(truncate=False)
+---------------------------------+
|json                             |
+---------------------------------+
|[{"name":"Alice"},{"name":"Bob"}]|
+---------------------------------+

```


Example 5: Converting a simple ArrayType column to JSON

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(1, ["Alice", "Bob"])], ("key", "value"))
>>> df.select(sf.to_json(df.value).alias("json")).show(truncate=False)
+---------------+
|json           |
+---------------+
|["Alice","Bob"]|
+---------------+

```


Example 6: Converting to JSON with specified options

```
>>> import pyspark.sql.functions as sf
>>> df = spark.sql("SELECT (DATE('2022-02-22'), 1) AS date")
>>> json1 = sf.to_json(df.date)
>>> json2 = sf.to_json(df.date, {"dateFormat": "yyyy/MM/dd"})
>>> df.select("date", json1, json2).show(truncate=False)
+---------------+------------------------------+------------------------------+
|date           |to_json(date)                 |to_json(date)                 |
+---------------+------------------------------+------------------------------+
|{2022-02-22, 1}|{"col1":"2022-02-22","col2":1}|{"col1":"2022/02/22","col2":1}|
+---------------+------------------------------+------------------------------+

```



# pyspark.sql.functions.is_variant_null — PySpark 4.0.1 documentation
pyspark.sql.functions.is\_variant\_null(_v_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#is_variant_null)
[#](#pyspark.sql.functions.is_variant_null "Permalink to this definition")

Check if a variant value is a variant null. Returns true if and only if the input is a variant null and false otherwise (including in the case of SQL NULL).

New in version 4.0.0.

Parameters

**v**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a variant column or column name

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a boolean column indicating whether the variant value is a variant null

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }'''} ])
>>> df.select(is_variant_null(parse_json(df.json)).alias("r")).collect()
[Row(r=False)]

```

# pyspark.sql.functions.parse_json — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.parse\_json

pyspark.sql.functions.parse\_json(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#parse_json)
[#](#pyspark.sql.functions.parse_json "Permalink to this definition")

Parses a column containing a JSON string into a `VariantType`. Throws exception if a string represents an invalid JSON value.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column or column name JSON formatted strings

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new column of VariantType.

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }'''} ])
>>> df.select(to_json(parse_json(df.json))).collect()
[Row(to_json(parse_json(json))='{"a":1}')]

```


# pyspark.sql.functions.schema_of_variant — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.schema\_of\_variant

pyspark.sql.functions.schema\_of\_variant(_v_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#schema_of_variant)
[#](#pyspark.sql.functions.schema_of_variant "Permalink to this definition")

Returns schema in the SQL format of a variant.

New in version 4.0.0.

Parameters

**v**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a variant column or column name

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a string column representing the variant schema

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }'''} ])
>>> df.select(schema_of_variant(parse_json(df.json)).alias("r")).collect()
[Row(r='OBJECT<a: BIGINT>')]

```


# pyspark.sql.functions.schema_of_variant_agg — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.schema\_of\_variant\_agg

pyspark.sql.functions.schema\_of\_variant\_agg(_v_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#schema_of_variant_agg)
[#](#pyspark.sql.functions.schema_of_variant_agg "Permalink to this definition")

Returns the merged schema in the SQL format of a variant column.

New in version 4.0.0.

Parameters

**v**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a variant column or column name

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a string column representing the variant schema

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }'''} ])
>>> df.select(schema_of_variant_agg(parse_json(df.json)).alias("r")).collect()
[Row(r='OBJECT<a: BIGINT>')]

```


# pyspark.sql.functions.try_variant_get — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_variant\_get(_v_, _path_, _targetType_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_variant_get)
[#](#pyspark.sql.functions.try_variant_get "Permalink to this definition")

Extracts a sub-variant from v according to path, and then cast the sub-variant to targetType. Returns null if the path does not exist or the cast fails.

New in version 4.0.0.

Parameters

**v**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a variant column or column name

**path**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column containing the extraction path strings or a string representing the extraction path. A valid path should start with $ and is followed by zero or more segments like \[123\], .name, \[‘name’\], or \[“name”\].

**targetType**str

the target data type to cast into, in a DDL-formatted string

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a column of targetType representing the extracted result

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }''', 'path': '$.a'} ])
>>> df.select(try_variant_get(parse_json(df.json), "$.a", "int").alias("r")).collect()
[Row(r=1)]
>>> df.select(try_variant_get(parse_json(df.json), "$.b", "int").alias("r")).collect()
[Row(r=None)]
>>> df.select(try_variant_get(parse_json(df.json), "$.a", "binary").alias("r")).collect()
[Row(r=None)]
>>> df.select(try_variant_get(parse_json(df.json), df.path, "int").alias("r")).collect()
[Row(r=1)]

```


# pyspark.sql.functions.variant_get — PySpark 4.0.1 documentation
pyspark.sql.functions.variant\_get(_v_, _path_, _targetType_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#variant_get)
[#](#pyspark.sql.functions.variant_get "Permalink to this definition")

Extracts a sub-variant from v according to path, and then cast the sub-variant to targetType. Returns null if the path does not exist. Throws an exception if the cast fails.

New in version 4.0.0.

Parameters

**v**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a variant column or column name

**path**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column containing the extraction path strings or a string representing the extraction path. A valid path should start with $ and is followed by zero or more segments like \[123\], .name, \[‘name’\], or \[“name”\].

**targetType**str

the target data type to cast into, in a DDL-formatted string

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a column of targetType representing the extracted result

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }''', 'path': '$.a'} ])
>>> df.select(variant_get(parse_json(df.json), "$.a", "int").alias("r")).collect()
[Row(r=1)]
>>> df.select(variant_get(parse_json(df.json), "$.b", "int").alias("r")).collect()
[Row(r=None)]
>>> df.select(variant_get(parse_json(df.json), df.path, "int").alias("r")).collect()
[Row(r=1)]

```


# pyspark.sql.functions.try_parse_json — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_parse\_json(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_parse_json)
[#](#pyspark.sql.functions.try_parse_json "Permalink to this definition")

Parses a column containing a JSON string into a `VariantType`. Returns None if a string contains an invalid JSON value.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column or column name JSON formatted strings

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new column of VariantType.

Examples

```
>>> df = spark.createDataFrame([ {'json': '''{ "a" : 1 }'''}, {'json': '''{a : 1}'''} ])
>>> df.select(to_json(try_parse_json(df.json))).collect()
[Row(to_json(try_parse_json(json))='{"a":1}'), Row(to_json(try_parse_json(json))=None)]

```


# pyspark.sql.functions.to_variant_object — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_variant\_object(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_variant_object)
[#](#pyspark.sql.functions.to_variant_object "Permalink to this definition")

Converts a column containing nested inputs (array/map/struct) into a variants where maps and structs are converted to variant objects which are unordered unlike SQL structs. Input maps can only have string keys.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column with a nested schema or column name

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new column of VariantType.

Examples

Example 1: Converting an array containing a nested struct into a variant

```
>>> from pyspark.sql import functions as sf
>>> from pyspark.sql.types import ArrayType, StructType, StructField, StringType, MapType
>>> schema = StructType([
...     StructField("i", StringType(), True),
...     StructField("v", ArrayType(StructType([
...         StructField("a", MapType(StringType(), StringType()), True)
...     ]), True))
... ])
>>> data = [("1", [{"a": {"b": 2}}])]
>>> df = spark.createDataFrame(data, schema)
>>> df.select(sf.to_variant_object(df.v))
DataFrame[to_variant_object(v): variant]
>>> df.select(sf.to_variant_object(df.v)).show(truncate=False)
+--------------------+
|to_variant_object(v)|
+--------------------+
|[{"a":{"b":"2"}}]   |
+--------------------+

```


# pyspark.sql.functions.from_xml — PySpark 4.0.1 documentation
pyspark.sql.functions.from\_xml(_col_, _schema_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#from_xml)
[#](#pyspark.sql.functions.from_xml "Permalink to this definition")

Parses a column containing a XML string to a row with the specified schema. Returns null, in the case of an unparsable string.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a column or column name in XML format

**schema**`StructType`, [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a StructType, Column or Python string literal with a DDL-formatted string to use when parsing the Xml column

**options**dict, optional

options to control parsing. accepts the same options as the Xml datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-xml.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a new column of complex type from given XML object.

Examples

Example 1: Parsing XML with a DDL-formatted string schema

```
>>> import pyspark.sql.functions as sf
>>> data = [(1, '''<p><a>1</a></p>''')]
>>> df = spark.createDataFrame(data, ("key", "value"))
... # Define the schema using a DDL-formatted string
>>> schema = "STRUCT<a: BIGINT>"
... # Parse the XML column using the DDL-formatted schema
>>> df.select(sf.from_xml(df.value, schema).alias("xml")).collect()
[Row(xml=Row(a=1))]

```


Example 2: Parsing XML with a `StructType` schema

```
>>> import pyspark.sql.functions as sf
>>> from pyspark.sql.types import StructType, LongType
>>> data = [(1, '''<p><a>1</a></p>''')]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> schema = StructType().add("a", LongType())
>>> df.select(sf.from_xml(df.value, schema)).show()
+---------------+
|from_xml(value)|
+---------------+
|            {1}|
+---------------+

```


Example 3: Parsing XML with `ArrayType` in schema

```
>>> import pyspark.sql.functions as sf
>>> data = [(1, '<p><a>1</a><a>2</a></p>')]
>>> df = spark.createDataFrame(data, ("key", "value"))
... # Define the schema with an Array type
>>> schema = "STRUCT<a: ARRAY<BIGINT>>"
... # Parse the XML column using the schema with an Array
>>> df.select(sf.from_xml(df.value, schema).alias("xml")).collect()
[Row(xml=Row(a=[1, 2]))]

```


Example 4: Parsing XML using [`pyspark.sql.functions.schema_of_xml()`](about:blank/pyspark.sql.functions.schema_of_xml.html#pyspark.sql.functions.schema_of_xml "pyspark.sql.functions.schema_of_xml")

```
>>> import pyspark.sql.functions as sf
>>> # Sample data with an XML column
... data = [(1, '<p><a>1</a><a>2</a></p>')]
>>> df = spark.createDataFrame(data, ("key", "value"))
... # Generate the schema from an example XML value
>>> schema = sf.schema_of_xml(sf.lit(data[0][1]))
... # Parse the XML column using the generated schema
>>> df.select(sf.from_xml(df.value, schema).alias("xml")).collect()
[Row(xml=Row(a=[1, 2]))]

```



# pyspark.sql.functions.schema_of_xml — PySpark 4.0.1 documentation
pyspark.sql.functions.schema\_of\_xml(_xml_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#schema_of_xml)
[#](#pyspark.sql.functions.schema_of_xml "Permalink to this definition")

Parses a XML string and infers its schema in DDL format.

New in version 4.0.0.

Parameters

**xml**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

a XML string or a foldable string column containing a XML string.

**options**dict, optional

options to control parsing. accepts the same options as the XML datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-xml.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a string representation of a `StructType` parsed from given XML.

Examples

Example 1: Parsing a simple XML with a single element

```
>>> from pyspark.sql import functions as sf
>>> df = spark.range(1)
>>> df.select(sf.schema_of_xml(sf.lit('<p><a>1</a></p>')).alias("xml")).collect()
[Row(xml='STRUCT<a: BIGINT>')]

```


Example 2: Parsing an XML with multiple elements in an array

```
>>> from pyspark.sql import functions as sf
>>> df.select(sf.schema_of_xml(sf.lit('<p><a>1</a><a>2</a></p>')).alias("xml")).collect()
[Row(xml='STRUCT<a: ARRAY<BIGINT>>')]

```


Example 3: Parsing XML with options to exclude attributes

```
>>> from pyspark.sql import functions as sf
>>> schema = sf.schema_of_xml('<p><a attr="2">1</a></p>', {'excludeAttribute':'true'})
>>> df.select(schema.alias("xml")).collect()
[Row(xml='STRUCT<a: BIGINT>')]

```


Example 4: Parsing XML with complex structure

```
>>> from pyspark.sql import functions as sf
>>> df.select(
...     sf.schema_of_xml(
...         sf.lit('<root><person><name>Alice</name><age>30</age></person></root>')
...     ).alias("xml")
... ).collect()
[Row(xml='STRUCT<person: STRUCT<age: BIGINT, name: STRING>>')]

```


Example 5: Parsing XML with nested arrays

```
>>> from pyspark.sql import functions as sf
>>> df.select(
...     sf.schema_of_xml(
...         sf.lit('<data><values><value>1</value><value>2</value></values></data>')
...     ).alias("xml")
... ).collect()
[Row(xml='STRUCT<values: STRUCT<value: ARRAY<BIGINT>>>')]

```


# pyspark.sql.functions.to_xml — PySpark 4.0.1 documentation
pyspark.sql.functions.to\_xml(_col_, _options\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#to_xml)
[#](#pyspark.sql.functions.to_xml "Permalink to this definition")

Converts a column containing a `StructType` into a XML string. Throws an exception, in the case of an unsupported type.

New in version 4.0.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

name of column containing a struct.

**options: dict, optional**

options to control converting. accepts the same options as the XML datasource. See [Data Source Option](https://spark.apache.org/docs/latest/sql-data-sources-xml.html#data-source-option) for the version you use.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a XML string converted from given `StructType`.

Examples

```
>>> from pyspark.sql import Row
>>> data = [(1, Row(age=2, name='Alice'))]
>>> df = spark.createDataFrame(data, ("key", "value"))
>>> df.select(to_xml(df.value, {'rowTag':'person'}).alias("xml")).collect()
[Row(xml='<person>\n    <age>2</age>\n    <name>Alice</name>\n</person>')]

```



# pyspark.sql.functions.xpath — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath

pyspark.sql.functions.xpath(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath)
[#](#pyspark.sql.functions.xpath "Permalink to this definition")

Returns a string array of values within the nodes of xml that match the XPath expression.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...     [('<a><b>b1</b><b>b2</b><b>b3</b><c>c1</c><c>c2</c></a>',)], ['x'])
>>> df.select(sf.xpath(df.x, sf.lit('a/b/text()'))).show()
+--------------------+
|xpath(x, a/b/text())|
+--------------------+
|        [b1, b2, b3]|
+--------------------+

```

# pyspark.sql.functions.xpath_boolean — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_boolean

pyspark.sql.functions.xpath\_boolean(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_boolean)
[#](#pyspark.sql.functions.xpath_boolean "Permalink to this definition")

Returns true if the XPath expression evaluates to true, or if a matching node is found.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>1</b></a>',)], ['x'])
>>> df.select(sf.xpath_boolean(df.x, sf.lit('a/b'))).show()
+---------------------+
|xpath_boolean(x, a/b)|
+---------------------+
|                 true|
+---------------------+

```



# pyspark.sql.functions.xpath_double — PySpark 4.0.1 documentation
pyspark.sql.functions.xpath\_double(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_double)
[#](#pyspark.sql.functions.xpath_double "Permalink to this definition")

Returns a double value, the value zero if no match is found, or NaN if a match is found but the value is non-numeric.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>1</b><b>2</b></a>',)], ['x'])
>>> df.select(sf.xpath_double(df.x, sf.lit('sum(a/b)'))).show()
+-------------------------+
|xpath_double(x, sum(a/b))|
+-------------------------+
|                      3.0|
+-------------------------+

```

# pyspark.sql.functions.xpath_float — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_float

pyspark.sql.functions.xpath\_float(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_float)
[#](#pyspark.sql.functions.xpath_float "Permalink to this definition")

Returns a float value, the value zero if no match is found, or NaN if a match is found but the value is non-numeric.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>1</b><b>2</b></a>',)], ['x'])
>>> df.select(sf.xpath_float(df.x, sf.lit('sum(a/b)'))).show()
+------------------------+
|xpath_float(x, sum(a/b))|
+------------------------+
|                     3.0|
+------------------------+

```

# pyspark.sql.functions.xpath_int — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_int

pyspark.sql.functions.xpath\_int(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_int)
[#](#pyspark.sql.functions.xpath_int "Permalink to this definition")

Returns an integer value, or the value zero if no match is found, or a match is found but the value is non-numeric.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>1</b><b>2</b></a>',)], ['x'])
>>> df.select(sf.xpath_int(df.x, sf.lit('sum(a/b)'))).show()
+----------------------+
|xpath_int(x, sum(a/b))|
+----------------------+
|                     3|
+----------------------+

```


# pyspark.sql.functions.xpath_long — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_long

pyspark.sql.functions.xpath\_long(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_long)
[#](#pyspark.sql.functions.xpath_long "Permalink to this definition")

Returns a long integer value, or the value zero if no match is found, or a match is found but the value is non-numeric.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>1</b><b>2</b></a>',)], ['x'])
>>> df.select(sf.xpath_long(df.x, sf.lit('sum(a/b)'))).show()
+-----------------------+
|xpath_long(x, sum(a/b))|
+-----------------------+
|                      3|
+-----------------------+

```


# pyspark.sql.functions.xpath_number — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_number

pyspark.sql.functions.xpath\_number(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_number)
[#](#pyspark.sql.functions.xpath_number "Permalink to this definition")

Returns a double value, the value zero if no match is found, or NaN if a match is found but the value is non-numeric.

New in version 3.5.0.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.createDataFrame(
...     [('<a><b>1</b><b>2</b></a>',)], ['x']
... ).select(sf.xpath_number('x', sf.lit('sum(a/b)'))).show()
+-------------------------+
|xpath_number(x, sum(a/b))|
+-------------------------+
|                      3.0|
+-------------------------+

```



# pyspark.sql.functions.xpath_short — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_short

pyspark.sql.functions.xpath\_short(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_short)
[#](#pyspark.sql.functions.xpath_short "Permalink to this definition")

Returns a short integer value, or the value zero if no match is found, or a match is found but the value is non-numeric.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>1</b><b>2</b></a>',)], ['x'])
>>> df.select(sf.xpath_short(df.x, sf.lit('sum(a/b)'))).show()
+------------------------+
|xpath_short(x, sum(a/b))|
+------------------------+
|                       3|
+------------------------+

```


# pyspark.sql.functions.xpath_string — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.xpath\_string

pyspark.sql.functions.xpath\_string(_xml_, _path_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#xpath_string)
[#](#pyspark.sql.functions.xpath_string "Permalink to this definition")

Returns the text contents of the first xml node that matches the XPath expression.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([('<a><b>b</b><c>cc</c></a>',)], ['x'])
>>> df.select(sf.xpath_string(df.x, sf.lit('a/c'))).show()
+--------------------+
|xpath_string(x, a/c)|
+--------------------+
|                  cc|
+--------------------+

```

# pyspark.sql.functions.parse_url — PySpark 4.0.1 documentation
pyspark.sql.functions.parse\_url(_url_, _partToExtract_, _key\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#parse_url)
[#](#pyspark.sql.functions.parse_url "Permalink to this definition")

URL function: Extracts a specified part from a URL. If a key is provided, it returns the associated query parameter value.

New in version 3.5.0.

Parameters

**url**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of strings, each representing a URL.

**partToExtract**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of strings, each representing the part to extract from the URL.

**key**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

A column of strings, each representing the key of a query parameter in the URL.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of strings, each representing the value of the extracted part from the URL.

Examples

Example 1: Extracting the query part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "QUERY")],
...   ["url", "part"]
... )
>>> df.select(sf.parse_url(df.url, df.part)).show()
+--------------------+
|parse_url(url, part)|
+--------------------+
|             query=1|
+--------------------+

```


Example 2: Extracting the value of a specific query parameter from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "QUERY", "query")],
...   ["url", "part", "key"]
... )
>>> df.select(sf.parse_url(df.url, df.part, df.key)).show()
+-------------------------+
|parse_url(url, part, key)|
+-------------------------+
|                        1|
+-------------------------+

```


Example 3: Extracting the protocol part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "PROTOCOL")],
...   ["url", "part"]
... )
>>> df.select(sf.parse_url(df.url, df.part)).show()
+--------------------+
|parse_url(url, part)|
+--------------------+
|               https|
+--------------------+

```


Example 4: Extracting the host part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "HOST")],
...   ["url", "part"]
... )
>>> df.select(sf.parse_url(df.url, df.part)).show()
+--------------------+
|parse_url(url, part)|
+--------------------+
|    spark.apache.org|
+--------------------+

```


Example 5: Extracting the path part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "PATH")],
...   ["url", "part"]
... )
>>> df.select(sf.parse_url(df.url, df.part)).show()
+--------------------+
|parse_url(url, part)|
+--------------------+
|               /path|
+--------------------+

```


# pyspark.sql.functions.try_parse_url — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_parse\_url(_url_, _partToExtract_, _key\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_parse_url)
[#](#pyspark.sql.functions.try_parse_url "Permalink to this definition")

This is a special version of parse\_url that performs the same operation, but returns a NULL value instead of raising an error if the parsing cannot be performed.

New in version 4.0.0.

Parameters

**url**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of strings, each representing a URL.

**partToExtract**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of strings, each representing the part to extract from the URL.

**key**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

A column of strings, each representing the key of a query parameter in the URL.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of strings, each representing the value of the extracted part from the URL.

Examples

Example 1: Extracting the query part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "QUERY")],
...   ["url", "part"]
... )
>>> df.select(sf.try_parse_url(df.url, df.part)).show()
+------------------------+
|try_parse_url(url, part)|
+------------------------+
|                 query=1|
+------------------------+

```


Example 2: Extracting the value of a specific query parameter from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "QUERY", "query")],
...   ["url", "part", "key"]
... )
>>> df.select(sf.try_parse_url(df.url, df.part, df.key)).show()
+-----------------------------+
|try_parse_url(url, part, key)|
+-----------------------------+
|                            1|
+-----------------------------+

```


Example 3: Extracting the protocol part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "PROTOCOL")],
...   ["url", "part"]
... )
>>> df.select(sf.try_parse_url(df.url, df.part)).show()
+------------------------+
|try_parse_url(url, part)|
+------------------------+
|                   https|
+------------------------+

```


Example 4: Extracting the host part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "HOST")],
...   ["url", "part"]
... )
>>> df.select(sf.try_parse_url(df.url, df.part)).show()
+------------------------+
|try_parse_url(url, part)|
+------------------------+
|        spark.apache.org|
+------------------------+

```


Example 5: Extracting the path part from a URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("https://spark.apache.org/path?query=1", "PATH")],
...   ["url", "part"]
... )
>>> df.select(sf.try_parse_url(df.url, df.part)).show()
+------------------------+
|try_parse_url(url, part)|
+------------------------+
|                   /path|
+------------------------+

```


Example 6: Invalid URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame(
...   [("inva lid://spark.apache.org/path?query=1", "QUERY", "query")],
...   ["url", "part", "key"]
... )
>>> df.select(sf.try_parse_url(df.url, df.part, df.key)).show()
+-----------------------------+
|try_parse_url(url, part, key)|
+-----------------------------+
|                         NULL|
+-----------------------------+

```

# pyspark.sql.functions.url_decode — PySpark 4.0.1 documentation
pyspark.sql.functions.url\_decode(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#url_decode)
[#](#pyspark.sql.functions.url_decode "Permalink to this definition")

URL function: Decodes a URL-encoded string in ‘application/x-www-form-urlencoded’ format to its original format.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of strings, each representing a URL-encoded string.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of strings, each representing the decoded string.

Examples

Example 1: Decoding a URL-encoded string

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("https%3A%2F%2Fspark.apache.org",)], ["url"])
>>> df.select(sf.url_decode(df.url)).show(truncate=False)
+------------------------+
|url_decode(url)         |
+------------------------+
|https://spark.apache.org|
+------------------------+

```


Example 2: Decoding a URL-encoded string with spaces

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Hello%20World%21",)], ["url"])
>>> df.select(sf.url_decode(df.url)).show()
+---------------+
|url_decode(url)|
+---------------+
|   Hello World!|
+---------------+

```


Example 3: Decoding a URL-encoded string with special characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("A%2BB%3D%3D",)], ["url"])
>>> df.select(sf.url_decode(df.url)).show()
+---------------+
|url_decode(url)|
+---------------+
|          A+B==|
+---------------+

```


Example 4: Decoding a URL-encoded string with non-ASCII characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("%E4%BD%A0%E5%A5%BD",)], ["url"])
>>> df.select(sf.url_decode(df.url)).show()
+---------------+
|url_decode(url)|
+---------------+
|           你好|
+---------------+

```


Example 5: Decoding a URL-encoded string with hexadecimal values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("%7E%21%40%23%24%25%5E%26%2A%28%29%5F%2B",)], ["url"])
>>> df.select(sf.url_decode(df.url)).show()
+---------------+
|url_decode(url)|
+---------------+
|  ~!@#$%^&*()_+|
+---------------+

```



# pyspark.sql.functions.url_encode — PySpark 4.0.1 documentation
pyspark.sql.functions.url\_encode(_str_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#url_encode)
[#](#pyspark.sql.functions.url_encode "Permalink to this definition")

URL function: Encodes a string into a URL-encoded string in ‘application/x-www-form-urlencoded’ format.

New in version 3.5.0.

Parameters

**str**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

A column of strings, each representing a string to be URL-encoded.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column of strings, each representing the URL-encoded string.

Examples

Example 1: Encoding a simple URL

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("https://spark.apache.org",)], ["url"])
>>> df.select(sf.url_encode(df.url)).show(truncate=False)
+------------------------------+
|url_encode(url)               |
+------------------------------+
|https%3A%2F%2Fspark.apache.org|
+------------------------------+

```


Example 2: Encoding a URL with spaces

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("Hello World!",)], ["url"])
>>> df.select(sf.url_encode(df.url)).show()
+---------------+
|url_encode(url)|
+---------------+
| Hello+World%21|
+---------------+

```


Example 3: Encoding a URL with special characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("A+B==",)], ["url"])
>>> df.select(sf.url_encode(df.url)).show()
+---------------+
|url_encode(url)|
+---------------+
|    A%2BB%3D%3D|
+---------------+

```


Example 4: Encoding a URL with non-ASCII characters

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("你好",)], ["url"])
>>> df.select(sf.url_encode(df.url)).show()
+------------------+
|   url_encode(url)|
+------------------+
|%E4%BD%A0%E5%A5%BD|
+------------------+

```


Example 5: Encoding a URL with hexadecimal values

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("~!@#$%^&*()_+",)], ["url"])
>>> df.select(sf.url_encode(df.url)).show(truncate=False)
+-----------------------------------+
|url_encode(url)                    |
+-----------------------------------+
|%7E%21%40%23%24%25%5E%26*%28%29_%2B|
+-----------------------------------+

```



# pyspark.sql.functions.aes_decrypt — PySpark 4.0.1 documentation
pyspark.sql.functions.aes\_decrypt(_input_, _key_, _mode\=None_, _padding\=None_, _aad\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#aes_decrypt)
[#](#pyspark.sql.functions.aes_decrypt "Permalink to this definition")

Returns a decrypted value of input using AES in mode with padding. Key lengths of 16, 24 and 32 bits are supported. Supported combinations of (mode, padding) are (‘ECB’, ‘PKCS’), (‘GCM’, ‘NONE’) and (‘CBC’, ‘PKCS’). Optional additional authenticated data (AAD) is only supported for GCM. If provided for encryption, the identical AAD value must be provided for decryption. The default mode is GCM.

New in version 3.5.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The binary value to decrypt.

**key**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The passphrase to use to decrypt the data.

**mode**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Specifies which block cipher mode should be used to decrypt messages. Valid modes: ECB, GCM, CBC.

**padding**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Specifies how to pad messages whose length is not a multiple of the block size. Valid values: PKCS, NONE, DEFAULT. The DEFAULT padding means PKCS for ECB, NONE for GCM and PKCS for CBC.

**aad**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Optional additional authenticated data. Only supported for GCM mode. This can be any free-form input and must be provided for both encryption and decryption.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a decrypted value.

Examples

Example 1: Decrypt data with key, mode, padding and aad.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAQiYi+sTLm7KD9UcZ2nlRdYDe/PX4",
...     "abcdefghijklmnop12345678ABCDEFGH", "GCM", "DEFAULT",
...     "This is an AAD mixed into the input",)],
...     ["input", "key", "mode", "padding", "aad"]
... )
>>> df.select(sf.aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode", df.padding, df.aad
... ).cast("STRING")).show(truncate=False)
+---------------------------------------------------------------------+
|CAST(aes_decrypt(unbase64(input), key, mode, padding, aad) AS STRING)|
+---------------------------------------------------------------------+
|Spark                                                                |
+---------------------------------------------------------------------+

```


Example 2: Decrypt data with key, mode and padding.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAAAAAAPSd4mWyMZ5mhvjiAPQJnfg=",
...     "abcdefghijklmnop12345678ABCDEFGH", "CBC", "DEFAULT",)],
...     ["input", "key", "mode", "padding"]
... )
>>> df.select(sf.aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode", df.padding
... ).cast("STRING")).show(truncate=False)
+------------------------------------------------------------------+
|CAST(aes_decrypt(unbase64(input), key, mode, padding, ) AS STRING)|
+------------------------------------------------------------------+
|Spark                                                             |
+------------------------------------------------------------------+

```


Example 3: Decrypt data with key and mode.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAAAAAAPSd4mWyMZ5mhvjiAPQJnfg=",
...     "abcdefghijklmnop12345678ABCDEFGH", "CBC", "DEFAULT",)],
...     ["input", "key", "mode", "padding"]
... )
>>> df.select(sf.aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode"
... ).cast("STRING")).show(truncate=False)
+------------------------------------------------------------------+
|CAST(aes_decrypt(unbase64(input), key, mode, DEFAULT, ) AS STRING)|
+------------------------------------------------------------------+
|Spark                                                             |
+------------------------------------------------------------------+

```


Example 4: Decrypt data with key.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "83F16B2AA704794132802D248E6BFD4E380078182D1544813898AC97E709B28A94",
...     "0000111122223333",)],
...     ["input", "key"]
... )
>>> df.select(sf.aes_decrypt(
...     sf.unhex(df.input), df.key
... ).cast("STRING")).show(truncate=False)
+--------------------------------------------------------------+
|CAST(aes_decrypt(unhex(input), key, GCM, DEFAULT, ) AS STRING)|
+--------------------------------------------------------------+
|Spark                                                         |
+--------------------------------------------------------------+

```


# pyspark.sql.functions.aes_encrypt — PySpark 4.0.1 documentation
pyspark.sql.functions.aes\_encrypt(_input_, _key_, _mode\=None_, _padding\=None_, _iv\=None_, _aad\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#aes_encrypt)
[#](#pyspark.sql.functions.aes_encrypt "Permalink to this definition")

Returns an encrypted value of input using AES in given mode with the specified padding. Key lengths of 16, 24 and 32 bits are supported. Supported combinations of (mode, padding) are (‘ECB’, ‘PKCS’), (‘GCM’, ‘NONE’) and (‘CBC’, ‘PKCS’). Optional initialization vectors (IVs) are only supported for CBC and GCM modes. These must be 16 bytes for CBC and 12 bytes for GCM. If not provided, a random vector will be generated and prepended to the output. Optional additional authenticated data (AAD) is only supported for GCM. If provided for encryption, the identical AAD value must be provided for decryption. The default mode is GCM.

New in version 3.5.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The binary value to encrypt.

**key**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The passphrase to use to encrypt the data.

**mode**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str, optional

Specifies which block cipher mode should be used to encrypt messages. Valid modes: ECB, GCM, CBC.

**padding**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Specifies how to pad messages whose length is not a multiple of the block size. Valid values: PKCS, NONE, DEFAULT. The DEFAULT padding means PKCS for ECB, NONE for GCM and PKCS for CBC.

**iv**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Optional initialization vector. Only supported for CBC and GCM modes. Valid values: None or “”. 16-byte array for CBC mode. 12-byte array for GCM mode.

**aad**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Optional additional authenticated data. Only supported for GCM mode. This can be any free-form input and must be provided for both encryption and decryption.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains an encrypted value.

Examples

Example 1: Encrypt data with key, mode, padding, iv and aad.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "Spark", "abcdefghijklmnop12345678ABCDEFGH", "GCM", "DEFAULT",
...     "000000000000000000000000", "This is an AAD mixed into the input",)],
...     ["input", "key", "mode", "padding", "iv", "aad"]
... )
>>> df.select(sf.base64(sf.aes_encrypt(
...     df.input, df.key, "mode", df.padding, sf.to_binary(df.iv, sf.lit("hex")), df.aad)
... )).show(truncate=False)
+-----------------------------------------------------------------------+
|base64(aes_encrypt(input, key, mode, padding, to_binary(iv, hex), aad))|
+-----------------------------------------------------------------------+
|AAAAAAAAAAAAAAAAQiYi+sTLm7KD9UcZ2nlRdYDe/PX4                           |
+-----------------------------------------------------------------------+

```


Example 2: Encrypt data with key, mode, padding and iv.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "Spark", "abcdefghijklmnop12345678ABCDEFGH", "GCM", "DEFAULT",
...     "000000000000000000000000", "This is an AAD mixed into the input",)],
...     ["input", "key", "mode", "padding", "iv", "aad"]
... )
>>> df.select(sf.base64(sf.aes_encrypt(
...     df.input, df.key, "mode", df.padding, sf.to_binary(df.iv, sf.lit("hex")))
... )).show(truncate=False)
+--------------------------------------------------------------------+
|base64(aes_encrypt(input, key, mode, padding, to_binary(iv, hex), ))|
+--------------------------------------------------------------------+
|AAAAAAAAAAAAAAAAQiYi+sRNYDAOTjdSEcYBFsAWPL1f                        |
+--------------------------------------------------------------------+

```


Example 3: Encrypt data with key, mode and padding.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "Spark SQL", "1234567890abcdef", "ECB", "PKCS",)],
...     ["input", "key", "mode", "padding"]
... )
>>> df.select(sf.aes_decrypt(sf.aes_encrypt(df.input, df.key, "mode", df.padding),
...     df.key, df.mode, df.padding
... ).cast("STRING")).show(truncate=False)
+---------------------------------------------------------------------------------------------+
|CAST(aes_decrypt(aes_encrypt(input, key, mode, padding, , ), key, mode, padding, ) AS STRING)|
+---------------------------------------------------------------------------------------------+
|Spark SQL                                                                                    |
+---------------------------------------------------------------------------------------------+

```


Example 4: Encrypt data with key and mode.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "Spark SQL", "0000111122223333", "ECB",)],
...     ["input", "key", "mode"]
... )
>>> df.select(sf.aes_decrypt(sf.aes_encrypt(df.input, df.key, "mode"),
...     df.key, df.mode
... ).cast("STRING")).show(truncate=False)
+---------------------------------------------------------------------------------------------+
|CAST(aes_decrypt(aes_encrypt(input, key, mode, DEFAULT, , ), key, mode, DEFAULT, ) AS STRING)|
+---------------------------------------------------------------------------------------------+
|Spark SQL                                                                                    |
+---------------------------------------------------------------------------------------------+

```


Example 5: Encrypt data with key.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "Spark SQL", "abcdefghijklmnop",)],
...     ["input", "key"]
... )
>>> df.select(sf.aes_decrypt(
...     sf.unbase64(sf.base64(sf.aes_encrypt(df.input, df.key))), df.key
... ).cast("STRING")).show(truncate=False)
+-------------------------------------------------------------------------------------------------------------+
|CAST(aes_decrypt(unbase64(base64(aes_encrypt(input, key, GCM, DEFAULT, , ))), key, GCM, DEFAULT, ) AS STRING)|
+-------------------------------------------------------------------------------------------------------------+
|Spark SQL                                                                                                    |
+-------------------------------------------------------------------------------------------------------------+

```



# pyspark.sql.functions.assert_true — PySpark 4.0.1 documentation
pyspark.sql.functions.assert\_true(_col_, _errMsg\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#assert_true)
[#](#pyspark.sql.functions.assert_true "Permalink to this definition")

Returns null if the input column is true; throws an exception with the provided error message otherwise.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

column name or column that represents the input column to test

**errMsg**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string, optional

A Python string literal or column containing the error message

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

null if the input column is true otherwise throws an error with specified message.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(0, 1)], ['a', 'b'])
>>> df.select('*', sf.assert_true(df.a < df.b)).show() 
+------------------------------------------------------+
|assert_true((a < b), '(a#788L < b#789L)' is not true!)|
+------------------------------------------------------+
|                                                  NULL|
+------------------------------------------------------+

```


```
>>> df.select('*', sf.assert_true(df.a < df.b, df.a)).show()
+---+---+-----------------------+
|  a|  b|assert_true((a < b), a)|
+---+---+-----------------------+
|  0|  1|                   NULL|
+---+---+-----------------------+

```


```
>>> df.select('*', sf.assert_true(df.a < df.b, 'error')).show()
+---+---+---------------------------+
|  a|  b|assert_true((a < b), error)|
+---+---+---------------------------+
|  0|  1|                       NULL|
+---+---+---------------------------+

```


```
>>> df.select('*', sf.assert_true(df.a > df.b, 'My error msg')).show() 
...
java.lang.RuntimeException: My error msg
...

```


# pyspark.sql.functions.bitmap_bit_position — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.bitmap\_bit\_position

pyspark.sql.functions.bitmap\_bit\_position(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bitmap_bit_position)
[#](#pyspark.sql.functions.bitmap_bit_position "Permalink to this definition")

Returns the bit position for the given input column.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The input column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(123,)], ['a'])
>>> df.select('*', sf.bitmap_bit_position('a')).show()
+---+----------------------+
|  a|bitmap_bit_position(a)|
+---+----------------------+
|123|                   122|
+---+----------------------+

```



# pyspark.sql.functions.bitmap_bucket_number — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.bitmap\_bucket\_number

pyspark.sql.functions.bitmap\_bucket\_number(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bitmap_bucket_number)
[#](#pyspark.sql.functions.bitmap_bucket_number "Permalink to this definition")

Returns the bucket number for the given input column.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The input column.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(123,)], ['a'])
>>> df.select('*', sf.bitmap_bucket_number('a')).show()
+---+-----------------------+
|  a|bitmap_bucket_number(a)|
+---+-----------------------+
|123|                      1|
+---+-----------------------+

```

# pyspark.sql.functions.bitmap_count — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.bitmap\_count

pyspark.sql.functions.bitmap\_count(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#bitmap_count)
[#](#pyspark.sql.functions.bitmap_count "Permalink to this definition")

Returns the number of set bits in the input bitmap.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The input bitmap.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("FFFF",)], ["a"])
>>> df.select(sf.bitmap_count(sf.to_binary(df.a, sf.lit("hex")))).show()
+-------------------------------+
|bitmap_count(to_binary(a, hex))|
+-------------------------------+
|                             16|
+-------------------------------+

```

# pyspark.sql.functions.current_catalog — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.current\_catalog

pyspark.sql.functions.current\_catalog()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_catalog)
[#](#pyspark.sql.functions.current_catalog "Permalink to this definition")

Returns the current catalog.

New in version 3.5.0.

See also

[`pyspark.sql.functions.current_database()`](about:blank/pyspark.sql.functions.current_database.html#pyspark.sql.functions.current_database "pyspark.sql.functions.current_database")

[`pyspark.sql.functions.current_schema()`](about:blank/pyspark.sql.functions.current_schema.html#pyspark.sql.functions.current_schema "pyspark.sql.functions.current_schema")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.current_catalog()).show()
+-----------------+
|current_catalog()|
+-----------------+
|    spark_catalog|
+-----------------+

```



# pyspark.sql.functions.current_database — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.current\_database

pyspark.sql.functions.current\_database()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_database)
[#](#pyspark.sql.functions.current_database "Permalink to this definition")

Returns the current database.

New in version 3.5.0.

See also

[`pyspark.sql.functions.current_catalog()`](about:blank/pyspark.sql.functions.current_catalog.html#pyspark.sql.functions.current_catalog "pyspark.sql.functions.current_catalog")

[`pyspark.sql.functions.current_schema()`](about:blank/pyspark.sql.functions.current_schema.html#pyspark.sql.functions.current_schema "pyspark.sql.functions.current_schema")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.current_database()).show()
+----------------+
|current_schema()|
+----------------+
|         default|
+----------------+

```


# pyspark.sql.functions.current_schema — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.current\_schema

pyspark.sql.functions.current\_schema()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_schema)
[#](#pyspark.sql.functions.current_schema "Permalink to this definition")

Returns the current database.

New in version 3.5.0.

See also

[`pyspark.sql.functions.current_catalog()`](about:blank/pyspark.sql.functions.current_catalog.html#pyspark.sql.functions.current_catalog "pyspark.sql.functions.current_catalog")

[`pyspark.sql.functions.current_database()`](about:blank/pyspark.sql.functions.current_database.html#pyspark.sql.functions.current_database "pyspark.sql.functions.current_database")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.current_schema()).show()
+----------------+
|current_schema()|
+----------------+
|         default|
+----------------+

```




# pyspark.sql.functions.current_user — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.current\_user

pyspark.sql.functions.current\_user()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#current_user)
[#](#pyspark.sql.functions.current_user "Permalink to this definition")

Returns the current database.

New in version 3.5.0.

See also

[`pyspark.sql.functions.user()`](about:blank/pyspark.sql.functions.user.html#pyspark.sql.functions.user "pyspark.sql.functions.user")

[`pyspark.sql.functions.session_user()`](about:blank/pyspark.sql.functions.session_user.html#pyspark.sql.functions.session_user "pyspark.sql.functions.session_user")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.current_user()).show() 
+--------------+
|current_user()|
+--------------+
| ruifeng.zheng|
+--------------+

```


# pyspark.sql.functions.hll_sketch_estimate — PySpark 4.0.1 documentation
pyspark.sql.functions.hll\_sketch\_estimate(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hll_sketch_estimate)
[#](#pyspark.sql.functions.hll_sketch_estimate "Permalink to this definition")

Returns the estimated number of unique values given the binary representation of a Datasketches HllSketch.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The estimated number of unique values for the HllSketch.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([1,2,2,3], "INT")
>>> df.agg(sf.hll_sketch_estimate(sf.hll_sketch_agg("value"))).show()
+----------------------------------------------+
|hll_sketch_estimate(hll_sketch_agg(value, 12))|
+----------------------------------------------+
|                                             3|
+----------------------------------------------+

```



# pyspark.sql.functions.hll_union — PySpark 4.0.1 documentation
pyspark.sql.functions.hll\_union(_col1_, _col2_, _allowDifferentLgConfigK\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#hll_union)
[#](#pyspark.sql.functions.hll_union "Permalink to this definition")

Merges two binary representations of Datasketches HllSketch objects, using a Datasketches Union object. Throws an exception if sketches have different lgConfigK values and allowDifferentLgConfigK is unset or set to false.

New in version 3.5.0.

Parameters

**col1**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**col2**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

**allowDifferentLgConfigK**bool, optional

Allow sketches with different lgConfigK values to be merged (defaults to false).

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

The binary representation of the merged HllSketch.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(1,4),(2,5),(2,5),(3,6)], "struct<v1:int,v2:int>")
>>> df = df.agg(
...     sf.hll_sketch_agg("v1").alias("sketch1"),
...     sf.hll_sketch_agg("v2").alias("sketch2")
... )
>>> df.select(sf.hll_sketch_estimate(sf.hll_union(df.sketch1, "sketch2"))).show()
+-------------------------------------------------------+
|hll_sketch_estimate(hll_union(sketch1, sketch2, false))|
+-------------------------------------------------------+
|                                                      6|
+-------------------------------------------------------+

```

# pyspark.sql.functions.input_file_block_length — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.input\_file\_block\_length

pyspark.sql.functions.input\_file\_block\_length()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#input_file_block_length)
[#](#pyspark.sql.functions.input_file_block_length "Permalink to this definition")

Returns the length of the block being read, or -1 if not available.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.read.text("python/test_support/sql/ages_newlines.csv", lineSep=",")
>>> df.select(sf.input_file_block_length()).show()
+-------------------------+
|input_file_block_length()|
+-------------------------+
|                       87|
|                       87|
|                       87|
|                       87|
|                       87|
|                       87|
|                       87|
|                       87|
+-------------------------+

```




# pyspark.sql.functions.input_file_block_start — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.input\_file\_block\_start

pyspark.sql.functions.input\_file\_block\_start()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#input_file_block_start)
[#](#pyspark.sql.functions.input_file_block_start "Permalink to this definition")

Returns the start offset of the block being read, or -1 if not available.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.read.text("python/test_support/sql/ages_newlines.csv", lineSep=",")
>>> df.select(sf.input_file_block_start()).show()
+------------------------+
|input_file_block_start()|
+------------------------+
|                       0|
|                       0|
|                       0|
|                       0|
|                       0|
|                       0|
|                       0|
|                       0|
+------------------------+

```


# pyspark.sql.functions.input_file_name — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.input\_file\_name

pyspark.sql.functions.input\_file\_name()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#input_file_name)
[#](#pyspark.sql.functions.input_file_name "Permalink to this definition")

Creates a string column for the file name of the current Spark task.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

file names.

See also

[`pyspark.sql.functions.input_file_block_length()`](about:blank/pyspark.sql.functions.input_file_block_length.html#pyspark.sql.functions.input_file_block_length "pyspark.sql.functions.input_file_block_length")

[`pyspark.sql.functions.input_file_block_start()`](about:blank/pyspark.sql.functions.input_file_block_start.html#pyspark.sql.functions.input_file_block_start "pyspark.sql.functions.input_file_block_start")

Examples

```
>>> import os
>>> from pyspark.sql import functions as sf
>>> path = os.path.abspath(__file__)
>>> df = spark.read.text(path)
>>> df.select(sf.input_file_name()).first()
Row(input_file_name()='file:///...')

```



# pyspark.sql.functions.java_method — PySpark 4.0.1 documentation
pyspark.sql.functions.java\_method(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#java_method)
[#](#pyspark.sql.functions.java_method "Permalink to this definition")

Calls a method with reflection.

New in version 3.5.0.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the first element should be a Column representing literal string for the class name, and the second element should be a Column representing literal string for the method name, and the remaining are input arguments (Columns or column names) to the Java method.

Examples

Example 1: Reflecting a method call with a column argument

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(
...     sf.java_method(
...         sf.lit("java.util.UUID"),
...         sf.lit("fromString"),
...         sf.lit("a5cf6c42-0c85-418f-af6c-3e4e5b1328f2")
...     )
... ).show(truncate=False)
+-----------------------------------------------------------------------------+
|java_method(java.util.UUID, fromString, a5cf6c42-0c85-418f-af6c-3e4e5b1328f2)|
+-----------------------------------------------------------------------------+
|a5cf6c42-0c85-418f-af6c-3e4e5b1328f2                                         |
+-----------------------------------------------------------------------------+

```


Example 2: Reflecting a method call with a column name argument

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('a5cf6c42-0c85-418f-af6c-3e4e5b1328f2',)], ['a'])
>>> df.select(
...     sf.java_method(sf.lit('java.util.UUID'), sf.lit('fromString'), 'a')
... ).show(truncate=False)
+------------------------------------------+
|java_method(java.util.UUID, fromString, a)|
+------------------------------------------+
|a5cf6c42-0c85-418f-af6c-3e4e5b1328f2      |
+------------------------------------------+

```


# pyspark.sql.functions.monotonically_increasing_id — PySpark 4.0.1 documentation
pyspark.sql.functions.monotonically\_increasing\_id()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#monotonically_increasing_id)
[#](#pyspark.sql.functions.monotonically_increasing_id "Permalink to this definition")

A column that generates monotonically increasing 64-bit integers.

The generated ID is guaranteed to be monotonically increasing and unique, but not consecutive. The current implementation puts the partition ID in the upper 31 bits, and the record number within each partition in the lower 33 bits. The assumption is that the data frame has less than 1 billion partitions, and each partition has less than 8 billion records.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

last value of the group.

Notes

The function is non-deterministic because its result depends on partition IDs.

As an example, consider a `DataFrame` with two partitions, each with 3 records. This expression would return the following IDs: 0, 1, 2, 8589934592 (1L << 33), 8589934593, 8589934594.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(0, 10, 1, 2).select(
...     "*",
...     sf.spark_partition_id(),
...     sf.monotonically_increasing_id()).show()
+---+--------------------+-----------------------------+
| id|SPARK_PARTITION_ID()|monotonically_increasing_id()|
+---+--------------------+-----------------------------+
|  0|                   0|                            0|
|  1|                   0|                            1|
|  2|                   0|                            2|
|  3|                   0|                            3|
|  4|                   0|                            4|
|  5|                   1|                   8589934592|
|  6|                   1|                   8589934593|
|  7|                   1|                   8589934594|
|  8|                   1|                   8589934595|
|  9|                   1|                   8589934596|
+---+--------------------+-----------------------------+

```




# pyspark.sql.functions.raise_error — PySpark 4.0.1 documentation
pyspark.sql.functions.raise\_error(_errMsg_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#raise_error)
[#](#pyspark.sql.functions.raise_error "Permalink to this definition")

Throws an exception with the provided error message.

New in version 3.1.0.

Changed in version 3.4.0: Supports Spark Connect.

Parameters

**errMsg**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or literal string

A Python string literal or column containing the error message

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

throws an error with specified message.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.raise_error("My error message")).show() 
...
java.lang.RuntimeException: My error message
...

```

# pyspark.sql.functions.reflect — PySpark 4.0.1 documentation
pyspark.sql.functions.reflect(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#reflect)
[#](#pyspark.sql.functions.reflect "Permalink to this definition")

Calls a method with reflection.

New in version 3.5.0.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the first element should be a Column representing literal string for the class name, and the second element should be a Column representing literal string for the method name, and the remaining are input arguments (Columns or column names) to the Java method.

Examples

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([('a5cf6c42-0c85-418f-af6c-3e4e5b1328f2',)], ['a'])
>>> df.select(
...     sf.reflect(sf.lit('java.util.UUID'), sf.lit('fromString'), 'a')
... ).show(truncate=False)
+--------------------------------------+
|reflect(java.util.UUID, fromString, a)|
+--------------------------------------+
|a5cf6c42-0c85-418f-af6c-3e4e5b1328f2  |
+--------------------------------------+

```



# pyspark.sql.functions.session_user — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.session\_user

pyspark.sql.functions.session\_user()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#session_user)
[#](#pyspark.sql.functions.session_user "Permalink to this definition")

Returns the user name of current execution context.

New in version 4.0.0.

See also

[`pyspark.sql.functions.user()`](about:blank/pyspark.sql.functions.user.html#pyspark.sql.functions.user "pyspark.sql.functions.user")

[`pyspark.sql.functions.current_user()`](about:blank/pyspark.sql.functions.current_user.html#pyspark.sql.functions.current_user "pyspark.sql.functions.current_user")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.session_user()).show() 
+--------------+
|session_user()|
+--------------+
| ruifeng.zheng|
+--------------+

```


# pyspark.sql.functions.spark_partition_id — PySpark 4.0.1 documentation
pyspark.sql.functions.spark\_partition\_id()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#spark_partition_id)
[#](#pyspark.sql.functions.spark_partition_id "Permalink to this definition")

A column for partition ID.

New in version 1.6.0.

Changed in version 3.4.0: Supports Spark Connect.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

partition id the record belongs to.

Notes

This is non deterministic because it depends on data partitioning and task scheduling.

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(10, numPartitions=5).select("*", sf.spark_partition_id()).show()
+---+--------------------+
| id|SPARK_PARTITION_ID()|
+---+--------------------+
|  0|                   0|
|  1|                   0|
|  2|                   1|
|  3|                   1|
|  4|                   2|
|  5|                   2|
|  6|                   3|
|  7|                   3|
|  8|                   4|
|  9|                   4|
+---+--------------------+

```


# pyspark.sql.functions.try_aes_decrypt — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_aes\_decrypt(_input_, _key_, _mode\=None_, _padding\=None_, _aad\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_aes_decrypt)
[#](#pyspark.sql.functions.try_aes_decrypt "Permalink to this definition")

This is a special version of aes\_decrypt that performs the same operation, but returns a NULL value instead of raising an error if the decryption cannot be performed. Returns a decrypted value of input using AES in mode with padding. Key lengths of 16, 24 and 32 bits are supported. Supported combinations of (mode, padding) are (‘ECB’, ‘PKCS’), (‘GCM’, ‘NONE’) and (‘CBC’, ‘PKCS’). Optional additional authenticated data (AAD) is only supported for GCM. If provided for encryption, the identical AAD value must be provided for decryption. The default mode is GCM.

New in version 3.5.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The binary value to decrypt.

**key**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

The passphrase to use to decrypt the data.

**mode**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Specifies which block cipher mode should be used to decrypt messages. Valid modes: ECB, GCM, CBC.

**padding**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Specifies how to pad messages whose length is not a multiple of the block size. Valid values: PKCS, NONE, DEFAULT. The DEFAULT padding means PKCS for ECB, NONE for GCM and PKCS for CBC.

**aad**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name, optional

Optional additional authenticated data. Only supported for GCM mode. This can be any free-form input and must be provided for both encryption and decryption.

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

A new column that contains a decrypted value or a NULL value.

Examples

Example 1: Decrypt data with key, mode, padding and aad.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAQiYi+sTLm7KD9UcZ2nlRdYDe/PX4",
...     "abcdefghijklmnop12345678ABCDEFGH", "GCM", "DEFAULT",
...     "This is an AAD mixed into the input",)],
...     ["input", "key", "mode", "padding", "aad"]
... )
>>> df.select(sf.try_aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode", df.padding, df.aad
... ).cast("STRING")).show(truncate=False)
+-------------------------------------------------------------------------+
|CAST(try_aes_decrypt(unbase64(input), key, mode, padding, aad) AS STRING)|
+-------------------------------------------------------------------------+
|Spark                                                                    |
+-------------------------------------------------------------------------+

```


Example 2: Failed to decrypt data with key, mode, padding and aad.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAQiYi+sTLm7KD9UcZ2nlRdYDe/PX4",
...     "abcdefghijklmnop12345678ABCDEFGH", "CBC", "DEFAULT",
...     "This is an AAD mixed into the input",)],
...     ["input", "key", "mode", "padding", "aad"]
... )
>>> df.select(sf.try_aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode", df.padding, df.aad
... ).cast("STRING")).show(truncate=False)
+-------------------------------------------------------------------------+
|CAST(try_aes_decrypt(unbase64(input), key, mode, padding, aad) AS STRING)|
+-------------------------------------------------------------------------+
|NULL                                                                     |
+-------------------------------------------------------------------------+

```


Example 3: Decrypt data with key, mode and padding.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAAAAAAPSd4mWyMZ5mhvjiAPQJnfg=",
...     "abcdefghijklmnop12345678ABCDEFGH", "CBC", "DEFAULT",)],
...     ["input", "key", "mode", "padding"]
... )
>>> df.select(sf.try_aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode", df.padding
... ).cast("STRING")).show(truncate=False)
+----------------------------------------------------------------------+
|CAST(try_aes_decrypt(unbase64(input), key, mode, padding, ) AS STRING)|
+----------------------------------------------------------------------+
|Spark                                                                 |
+----------------------------------------------------------------------+

```


Example 4: Decrypt data with key and mode.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "AAAAAAAAAAAAAAAAAAAAAPSd4mWyMZ5mhvjiAPQJnfg=",
...     "abcdefghijklmnop12345678ABCDEFGH", "CBC", "DEFAULT",)],
...     ["input", "key", "mode", "padding"]
... )
>>> df.select(sf.try_aes_decrypt(
...     sf.unbase64(df.input), df.key, "mode"
... ).cast("STRING")).show(truncate=False)
+----------------------------------------------------------------------+
|CAST(try_aes_decrypt(unbase64(input), key, mode, DEFAULT, ) AS STRING)|
+----------------------------------------------------------------------+
|Spark                                                                 |
+----------------------------------------------------------------------+

```


Example 5: Decrypt data with key.

```
>>> import pyspark.sql.functions as sf
>>> df = spark.createDataFrame([(
...     "83F16B2AA704794132802D248E6BFD4E380078182D1544813898AC97E709B28A94",
...     "0000111122223333",)],
...     ["input", "key"]
... )
>>> df.select(sf.try_aes_decrypt(
...     sf.unhex(df.input), df.key
... ).cast("STRING")).show(truncate=False)
+------------------------------------------------------------------+
|CAST(try_aes_decrypt(unhex(input), key, GCM, DEFAULT, ) AS STRING)|
+------------------------------------------------------------------+
|Spark                                                             |
+------------------------------------------------------------------+

```

# pyspark.sql.functions.try_reflect — PySpark 4.0.1 documentation
pyspark.sql.functions.try\_reflect(_\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#try_reflect)
[#](#pyspark.sql.functions.try_reflect "Permalink to this definition")

This is a special version of reflect that performs the same operation, but returns a NULL value instead of raising an error if the invoke method thrown exception.

New in version 4.0.0.

Parameters

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

the first element should be a Column representing literal string for the class name, and the second element should be a Column representing literal string for the method name, and the remaining are input arguments (Columns or column names) to the Java method.

Examples

Example 1: Reflecting a method call with arguments

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([("a5cf6c42-0c85-418f-af6c-3e4e5b1328f2",)], ["a"])
>>> df.select(
...     sf.try_reflect(sf.lit("java.util.UUID"), sf.lit("fromString"), "a")
... ).show(truncate=False)
+------------------------------------------+
|try_reflect(java.util.UUID, fromString, a)|
+------------------------------------------+
|a5cf6c42-0c85-418f-af6c-3e4e5b1328f2      |
+------------------------------------------+

```


Example 2: Exception in the reflection call, resulting in null

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(
...     sf.try_reflect(sf.lit("scala.Predef"), sf.lit("require"), sf.lit(False))
... ).show(truncate=False)
+-----------------------------------------+
|try_reflect(scala.Predef, require, false)|
+-----------------------------------------+
|NULL                                     |
+-----------------------------------------+

```

# pyspark.sql.functions.typeof — PySpark 4.0.1 documentation
pyspark.sql.functions.typeof(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#typeof)
[#](#pyspark.sql.functions.typeof "Permalink to this definition")

Return DDL-formatted type string for the data type of the input.

New in version 3.5.0.

Parameters

**col**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or column name

Examples

```
>>> from pyspark.sql import functions as sf
>>> df = spark.createDataFrame([(True, 1, 1.0, 'xyz',)], ['a', 'b', 'c', 'd'])
>>> df.select(sf.typeof(df.a), sf.typeof(df.b), sf.typeof('c'), sf.typeof('d')).show()
+---------+---------+---------+---------+
|typeof(a)|typeof(b)|typeof(c)|typeof(d)|
+---------+---------+---------+---------+
|  boolean|   bigint|   double|   string|
+---------+---------+---------+---------+

```

# pyspark.sql.functions.user — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.user

pyspark.sql.functions.user()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#user)
[#](#pyspark.sql.functions.user "Permalink to this definition")

Returns the current database.

New in version 3.5.0.

See also

[`pyspark.sql.functions.current_user()`](about:blank/pyspark.sql.functions.current_user.html#pyspark.sql.functions.current_user "pyspark.sql.functions.current_user")

[`pyspark.sql.functions.session_user()`](about:blank/pyspark.sql.functions.session_user.html#pyspark.sql.functions.session_user "pyspark.sql.functions.session_user")

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.range(1).select(sf.user()).show() 
+--------------+
|        user()|
+--------------+
| ruifeng.zheng|
+--------------+

```



# pyspark.sql.functions.version — PySpark 4.0.1 documentation
pyspark.sql.functions.version()
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#version)
[#](#pyspark.sql.functions.version "Permalink to this definition")

Returns the Spark version. The string contains 2 fields, the first being a release version and the second being a git revision.

New in version 3.5.0.

Examples

```
>>> from pyspark.sql import functions as sf
>>> spark.range(1).select(sf.version()).show(truncate=False) 
+----------------------------------------------+
|version()                                     |
+----------------------------------------------+
|4.0.0 4f8d1f575e99aeef8990c63a9614af0fc5479330|
+----------------------------------------------+

```


# pyspark.sql.functions.call_udf — PySpark 4.0.1 documentation
pyspark.sql.functions.call\_udf(_udfName_, _\*cols_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#call_udf)
[#](#pyspark.sql.functions.call_udf "Permalink to this definition")

Call a user-defined function.

New in version 3.4.0.

Parameters

**udfName**str

name of the user defined function (UDF)

**cols**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column") or str

column names or [`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")s to be used in the UDF

Returns

[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

result of executed udf.

Examples

```
>>> from pyspark.sql.functions import call_udf, col
>>> from pyspark.sql.types import IntegerType, StringType
>>> df = spark.createDataFrame([(1, "a"),(2, "b"), (3, "c")],["id", "name"])
>>> _ = spark.udf.register("intX2", lambda i: i * 2, IntegerType())
>>> df.select(call_udf("intX2", "id")).show()
+---------+
|intX2(id)|
+---------+
|        2|
|        4|
|        6|
+---------+
>>> _ = spark.udf.register("strX2", lambda s: s * 2, StringType())
>>> df.select(call_udf("strX2", col("name"))).show()
+-----------+
|strX2(name)|
+-----------+
|         aa|
|         bb|
|         cc|
+-----------+

```

# pyspark.sql.functions.pandas_udf — PySpark 4.0.1 documentation
pyspark.sql.functions.pandas\_udf(_f\=None_, _returnType\=None_, _functionType\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/pandas/functions.html#pandas_udf)
[#](#pyspark.sql.functions.pandas_udf "Permalink to this definition")

Creates a pandas user defined function (a.k.a. vectorized user defined function).

Pandas UDFs are user defined functions that are executed by Spark using Arrow to transfer data and Pandas to work with the data, which allows vectorized operations. A Pandas UDF is defined using the pandas\_udf as a decorator or to wrap the function, and no additional configuration is required. A Pandas UDF behaves as a regular PySpark function API in general.

New in version 2.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Changed in version 4.0.0: Supports keyword-arguments in SCALAR and GROUPED\_AGG type.

Parameters

**f**function, optional

user-defined function. A python function if used as a standalone function

**returnType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str, optional

the return type of the user-defined function. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string.

**functionType**int, optional

an enum value in `pyspark.sql.functions.PandasUDFType`. Default: SCALAR. This parameter exists for compatibility. Using Python type hints is encouraged.

Notes

The user-defined functions do not support conditional expressions or short circuiting in boolean expressions and it ends up with being executed all internally. If the functions can fail on special rows, the workaround is to incorporate the condition into the functions.

The user-defined functions do not take keyword arguments on the calling side.

The data type of returned pandas.Series from the user-defined functions should be matched with defined returnType (see `types.to_arrow_type()` and `types.from_arrow_type()`). When there is mismatch between them, Spark might do conversion on returned data. The conversion is not guaranteed to be correct and results should be checked for accuracy by users.

Currently, [`pyspark.sql.types.ArrayType`](about:blank/pyspark.sql.types.ArrayType.html#pyspark.sql.types.ArrayType "pyspark.sql.types.ArrayType") of [`pyspark.sql.types.TimestampType`](about:blank/pyspark.sql.types.TimestampType.html#pyspark.sql.types.TimestampType "pyspark.sql.types.TimestampType") and nested [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") are currently not supported as output types.

Examples

In order to use this API, customarily the below are imported:

```
>>> import pandas as pd
>>> from pyspark.sql.functions import pandas_udf

```


From Spark 3.0 with Python 3.6+, [Python type hints](https://www.python.org/dev/peps/pep-0484) detect the function types as below:

```
>>> @pandas_udf(IntegerType())
... def slen(s: pd.Series) -> pd.Series:
...     return s.str.len()

```


Prior to Spark 3.0, the pandas UDF used functionType to decide the execution type as below:

```
>>> from pyspark.sql.functions import PandasUDFType
>>> from pyspark.sql.types import IntegerType
>>> @pandas_udf(IntegerType(), PandasUDFType.SCALAR)
... def slen(s):
...     return s.str.len()

```


It is preferred to specify type hints for the pandas UDF instead of specifying pandas UDF type via functionType which will be deprecated in the future releases.

Note that the type hint should use pandas.Series in all cases but there is one variant that pandas.DataFrame should be used for its input or output type hint instead when the input or output column is of [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType"). The following example shows a Pandas UDF which takes long column, string column and struct column, and outputs a struct column. It requires the function to specify the type hints of pandas.Series and pandas.DataFrame as below:

```
>>> @pandas_udf("col1 string, col2 long")
>>> def func(s1: pd.Series, s2: pd.Series, s3: pd.DataFrame) -> pd.DataFrame:
...     s3['col2'] = s1 + s2.str.len()
...     return s3
...
>>> # Create a Spark DataFrame that has three columns including a struct column.
... df = spark.createDataFrame(
...     [[1, "a string", ("a nested string",)]],
...     "long_col long, string_col string, struct_col struct<col1:string>")
>>> df.printSchema()
root
|-- long_column: long (nullable = true)
|-- string_column: string (nullable = true)
|-- struct_column: struct (nullable = true)
|    |-- col1: string (nullable = true)
>>> df.select(func("long_col", "string_col", "struct_col")).printSchema()
|-- func(long_col, string_col, struct_col): struct (nullable = true)
|    |-- col1: string (nullable = true)
|    |-- col2: long (nullable = true)

```


In the following sections, it describes the combinations of the supported type hints. For simplicity, pandas.DataFrame variant is omitted.

*   Series to Series
    
    pandas.Series, … -> pandas.Series
    
    The function takes one or more pandas.Series and outputs one pandas.Series. The output of the function should always be of the same length as the input.
    
    ```
>>> @pandas_udf("string")
... def to_upper(s: pd.Series) -> pd.Series:
...     return s.str.upper()
...
>>> df = spark.createDataFrame([("John Doe",)], ("name",))
>>> df.select(to_upper("name")).show()
+--------------+
|to_upper(name)|
+--------------+
|      JOHN DOE|
+--------------+

```

    
    ```
>>> @pandas_udf("first string, last string")
... def split_expand(s: pd.Series) -> pd.DataFrame:
...     return s.str.split(expand=True)
...
>>> df = spark.createDataFrame([("John Doe",)], ("name",))
>>> df.select(split_expand("name")).show()
+------------------+
|split_expand(name)|
+------------------+
|       {John, Doe}|
+------------------+

```

    
    This type of Pandas UDF can use keyword arguments:
    
    ```
>>> @pandas_udf(returnType=IntegerType())
... def calc(a: pd.Series, b: pd.Series) -> pd.Series:
...     return a + 10 * b
...
>>> spark.range(2).select(calc(b=col("id") * 10, a=col("id"))).show()
+-----------------------------+
|calc(b => (id * 10), a => id)|
+-----------------------------+
|                            0|
|                          101|
+-----------------------------+

```

    
    Note
    
    The length of the input is not that of the whole input column, but is the length of an internal batch used for each call to the function.
    
*   Iterator of Series to Iterator of Series
    
    Iterator\[pandas.Series\] -> Iterator\[pandas.Series\]
    
    The function takes an iterator of pandas.Series and outputs an iterator of pandas.Series. In this case, the created pandas UDF instance requires one input column when this is called as a PySpark column. The length of the entire output from the function should be the same length of the entire input; therefore, it can prefetch the data from the input iterator as long as the lengths are the same.
    
    It is also useful when the UDF execution requires initializing some states although internally it works identically as Series to Series case. The pseudocode below illustrates the example.
    
    ```
@pandas_udf("long")
def calculate(iterator: Iterator[pd.Series]) -> Iterator[pd.Series]:
    # Do some expensive initialization with a state
    state = very_expensive_initialization()
    for x in iterator:
        # Use that state for whole iterator.
        yield calculate_with_state(x, state)

df.select(calculate("value")).show()

```

    
    ```
>>> from typing import Iterator
>>> @pandas_udf("long")
... def plus_one(iterator: Iterator[pd.Series]) -> Iterator[pd.Series]:
...     for s in iterator:
...         yield s + 1
...
>>> df = spark.createDataFrame(pd.DataFrame([1, 2, 3], columns=["v"]))
>>> df.select(plus_one(df.v)).show()
+-----------+
|plus_one(v)|
+-----------+
|          2|
|          3|
|          4|
+-----------+

```

    
    Note
    
    The length of each series is the length of a batch internally used.
    
*   Iterator of Multiple Series to Iterator of Series
    
    Iterator\[Tuple\[pandas.Series, …\]\] -> Iterator\[pandas.Series\]
    
    The function takes an iterator of a tuple of multiple pandas.Series and outputs an iterator of pandas.Series. In this case, the created pandas UDF instance requires input columns as many as the series when this is called as a PySpark column. Otherwise, it has the same characteristics and restrictions as Iterator of Series to Iterator of Series case.
    
    ```
>>> from typing import Iterator, Tuple
>>> from pyspark.sql.functions import struct, col
>>> @pandas_udf("long")
... def multiply(iterator: Iterator[Tuple[pd.Series, pd.DataFrame]]) -> Iterator[pd.Series]:
...     for s1, df in iterator:
...         yield s1 * df.v
...
>>> df = spark.createDataFrame(pd.DataFrame([1, 2, 3], columns=["v"]))
>>> df.withColumn('output', multiply(col("v"), struct(col("v")))).show()
+---+------+
|  v|output|
+---+------+
|  1|     1|
|  2|     4|
|  3|     9|
+---+------+

```

    
    Note
    
    The length of each series is the length of a batch internally used.
    
*   Series to Scalar
    
    pandas.Series, … -> Any
    
    The function takes pandas.Series and returns a scalar value. The returnType should be a primitive data type, and the returned scalar can be either a python primitive type, e.g., int or float or a numpy data type, e.g., numpy.int64 or numpy.float64. Any should ideally be a specific scalar type accordingly.
    
    ```
>>> @pandas_udf("double")
... def mean_udf(v: pd.Series) -> float:
...     return v.mean()
...
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)], ("id", "v"))
>>> df.groupby("id").agg(mean_udf(df['v'])).show()
+---+-----------+
| id|mean_udf(v)|
+---+-----------+
|  1|        1.5|
|  2|        6.0|
+---+-----------+

```

    
    This type of Pandas UDF can use keyword arguments:
    
    ```
>>> @pandas_udf("double")
... def weighted_mean_udf(v: pd.Series, w: pd.Series) -> float:
...     import numpy as np
...     return np.average(v, weights=w)
...
>>> df = spark.createDataFrame(
...     [(1, 1.0, 1.0), (1, 2.0, 2.0), (2, 3.0, 1.0), (2, 5.0, 2.0), (2, 10.0, 3.0)],
...     ("id", "v", "w"))
>>> df.groupby("id").agg(weighted_mean_udf(w=df["w"], v=df["v"])).show()
+---+---------------------------------+
| id|weighted_mean_udf(w => w, v => v)|
+---+---------------------------------+
|  1|               1.6666666666666667|
|  2|                7.166666666666667|
+---+---------------------------------+

```

    
    This UDF can also be used as window functions as below:
    
    ```
>>> from pyspark.sql import Window
>>> @pandas_udf("double")
... def mean_udf(v: pd.Series) -> float:
...     return v.mean()
...
>>> df = spark.createDataFrame(
...     [(1, 1.0), (1, 2.0), (2, 3.0), (2, 5.0), (2, 10.0)], ("id", "v"))
>>> w = Window.partitionBy('id').orderBy('v').rowsBetween(-1, 0)
>>> df.withColumn('mean_v', mean_udf("v").over(w)).show()
+---+----+------+
| id|   v|mean_v|
+---+----+------+
|  1| 1.0|   1.0|
|  1| 2.0|   1.5|
|  2| 3.0|   3.0|
|  2| 5.0|   4.0|
|  2|10.0|   7.5|
+---+----+------+

```

    
    Note
    
    For performance reasons, the input series to window functions are not copied. Therefore, mutating the input series is not allowed and will cause incorrect results. For the same reason, users should also not rely on the index of the input series.





# pyspark.sql.functions.udf — PySpark 4.0.1 documentation
pyspark.sql.functions.udf(_f\=None_, _returnType\=StringType()_, _\*_, _useArrow\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#udf)
[#](#pyspark.sql.functions.udf "Permalink to this definition")

Creates a user defined function (UDF).

New in version 1.3.0.

Changed in version 3.4.0: Supports Spark Connect.

Changed in version 4.0.0: Supports keyword-arguments.

Parameters

**f**function, optional

python function if used as a standalone function

**returnType**[`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") or str, optional

the return type of the user-defined function. The value can be either a [`pyspark.sql.types.DataType`](about:blank/pyspark.sql.types.DataType.html#pyspark.sql.types.DataType "pyspark.sql.types.DataType") object or a DDL-formatted type string. Defaults to `StringType`.

**useArrow**bool, optional

whether to use Arrow to optimize the (de)serialization. When it is None, the Spark config “spark.sql.execution.pythonUDF.arrow.enabled” takes effect.

Notes

The user-defined functions are considered deterministic by default. Due to optimization, duplicate invocations may be eliminated or the function may even be invoked more times than it is present in the query. If your function is not deterministic, call asNondeterministic on the user defined function. E.g.:

```
>>> from pyspark.sql.types import IntegerType
>>> import random
>>> random_udf = udf(lambda: int(random.random() * 100), IntegerType()).asNondeterministic()

```


The user-defined functions do not support conditional expressions or short circuiting in boolean expressions and it ends up with being executed all internally. If the functions can fail on special rows, the workaround is to incorporate the condition into the functions.

The user-defined functions do not take keyword arguments on the calling side.

Examples

```
>>> from pyspark.sql.types import IntegerType
>>> slen = udf(lambda s: len(s), IntegerType())
>>> @udf
... def to_upper(s):
...     if s is not None:
...         return s.upper()
...
>>> @udf(returnType=IntegerType())
... def add_one(x):
...     if x is not None:
...         return x + 1
...
>>> df = spark.createDataFrame([(1, "John Doe", 21)], ("id", "name", "age"))
>>> df.select(slen("name").alias("slen(name)"), to_upper("name"), add_one("age")).show()
+----------+--------------+------------+
|slen(name)|to_upper(name)|add_one(age)|
+----------+--------------+------------+
|         8|      JOHN DOE|          22|
+----------+--------------+------------+

```


UDF can use keyword arguments:

```
>>> @udf(returnType=IntegerType())
... def calc(a, b):
...     return a + 10 * b
...
>>> spark.range(2).select(calc(b=col("id") * 10, a=col("id"))).show()
+-----------------------------+
|calc(b => (id * 10), a => id)|
+-----------------------------+
|                            0|
|                          101|
+-----------------------------+

```


# pyspark.sql.functions.udtf — PySpark 4.0.1 documentation
pyspark.sql.functions.udtf(_cls\=None_, _\*_, _returnType\=None_, _useArrow\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#udtf)
[#](#pyspark.sql.functions.udtf "Permalink to this definition")

Creates a user defined table function (UDTF).

New in version 3.5.0.

Changed in version 4.0.0: Supports Python side analysis.

Changed in version 4.0.0: Supports keyword-arguments.

Parameters

**cls**class, optional

the Python user-defined table function handler class.

**returnType**[`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") or str, optional

the return type of the user-defined table function. The value can be either a [`pyspark.sql.types.StructType`](about:blank/pyspark.sql.types.StructType.html#pyspark.sql.types.StructType "pyspark.sql.types.StructType") object or a DDL-formatted struct type string. If None, the handler class must provide analyze static method.

**useArrow**bool, optional

whether to use Arrow to optimize the (de)serializations. When it’s set to None, the Spark config “spark.sql.execution.pythonUDTF.arrow.enabled” is used.

Notes

User-defined table functions (UDTFs) are considered non-deterministic by default. Use asDeterministic() to mark a function as deterministic. E.g.:

```
>>> class PlusOne:
...     def eval(self, a: int):
...         yield a + 1,
>>> plus_one = udtf(PlusOne, returnType="r: int").asDeterministic()

```


Use “yield” to produce one row for the UDTF result relation as many times as needed. In the context of a lateral join, each such result row will be associated with the most recent input row consumed from the “eval” method.

User-defined table functions are considered opaque to the optimizer by default. As a result, operations like filters from WHERE clauses or limits from LIMIT/OFFSET clauses that appear after the UDTF call will execute on the UDTF’s result relation. By the same token, any relations forwarded as input to UDTFs will plan as full table scans in the absence of any explicit such filtering or other logic explicitly written in a table subquery surrounding the provided input relation.

User-defined table functions do not accept keyword arguments on the calling side.

Examples

Implement the UDTF class and create a UDTF:

```
>>> class TestUDTF:
...     def eval(self, *args: Any):
...         yield "hello", "world"
...
>>> from pyspark.sql.functions import udtf
>>> test_udtf = udtf(TestUDTF, returnType="c1: string, c2: string")
>>> test_udtf().show()
+-----+-----+
|   c1|   c2|
+-----+-----+
|hello|world|
+-----+-----+

```


UDTF can also be created using the decorator syntax:

```
>>> @udtf(returnType="c1: int, c2: int")
... class PlusOne:
...     def eval(self, x: int):
...         yield x, x + 1
...
>>> from pyspark.sql.functions import lit
>>> PlusOne(lit(1)).show()
+---+---+
| c1| c2|
+---+---+
|  1|  2|
+---+---+

```


UDTF can also have analyze static method instead of a static return type:

The analyze static method should take arguments:

*   The number and order of arguments are the same as the UDTF inputs
    
*   Each argument is a `pyspark.sql.udtf.AnalyzeArgument`, containing: - dataType: DataType - value: Any: the calculated value if the argument is foldable; otherwise None - isTable: bool: True if the argument is a table argument
    

and return a `pyspark.sql.udtf.AnalyzeResult`, containing.

*   schema: StructType
    

```
>>> from pyspark.sql.udtf import AnalyzeArgument, AnalyzeResult
>>> # or from pyspark.sql.functions import AnalyzeArgument, AnalyzeResult
>>> @udtf
... class TestUDTFWithAnalyze:
...     @staticmethod
...     def analyze(a: AnalyzeArgument, b: AnalyzeArgument) -> AnalyzeResult:
...         return AnalyzeResult(StructType().add("a", a.dataType).add("b", b.dataType))
...
...     def eval(self, a, b):
...         yield a, b
...
>>> TestUDTFWithAnalyze(lit(1), lit("x")).show()
+---+---+
|  a|  b|
+---+---+
|  1|  x|
+---+---+

```


UDTF can use keyword arguments:

```
>>> @udtf
... class TestUDTFWithKwargs:
...     @staticmethod
...     def analyze(
...         a: AnalyzeArgument, b: AnalyzeArgument, **kwargs: AnalyzeArgument
...     ) -> AnalyzeResult:
...         return AnalyzeResult(
...             StructType().add("a", a.dataType)
...                 .add("b", b.dataType)
...                 .add("x", kwargs["x"].dataType)
...         )
...
...     def eval(self, a, b, **kwargs):
...         yield a, b, kwargs["x"]
...
>>> TestUDTFWithKwargs(lit(1), x=lit("x"), b=lit("b")).show()
+---+---+---+
|  a|  b|  x|
+---+---+---+
|  1|  b|  x|
+---+---+---+

```


```
>>> _ = spark.udtf.register("test_udtf", TestUDTFWithKwargs)
>>> spark.sql("SELECT * FROM test_udtf(1, x => 'x', b => 'b')").show()
+---+---+---+
|  a|  b|  x|
+---+---+---+
|  1|  b|  x|
+---+---+---+

```


Arrow optimization can be explicitly enabled when creating UDTFs:

```
>>> @udtf(returnType="c1: int, c2: int", useArrow=True)
... class ArrowPlusOne:
...     def eval(self, x: int):
...         yield x, x + 1
...
>>> ArrowPlusOne(lit(1)).show()
+---+---+
| c1| c2|
+---+---+
|  1|  2|
+---+---+

```


# pyspark.sql.functions.unwrap_udt — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.functions.unwrap\_udt

pyspark.sql.functions.unwrap\_udt(_col_)
[\[source\]](about:blank/_modules/pyspark/sql/functions/builtin.html#unwrap_udt)
[#](#pyspark.sql.functions.unwrap_udt "Permalink to this definition")

Unwrap UDT data type column into its underlying type.

New in version 3.4.0.

Notes

Supports Spark Connect.



# pyspark.sql.tvf.TableValuedFunction.collations — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.tvf.TableValuedFunction.collations

TableValuedFunction.collations()
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.collations)
[#](#pyspark.sql.tvf.TableValuedFunction.collations "Permalink to this definition")

Get all of the Spark SQL string collations.

New in version 4.0.0.

Returns

`DataFrame`

Examples

```
>>> spark.tvf.collations().show()
+-------+-------+-------------------+...
|CATALOG| SCHEMA|               NAME|...
+-------+-------+-------------------+...
...
+-------+-------+-------------------+...

```



# pyspark.sql.tvf.TableValuedFunction.explode — PySpark 4.0.1 documentation
TableValuedFunction.explode(_collection_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.explode)
[#](#pyspark.sql.tvf.TableValuedFunction.explode "Permalink to this definition")

Returns a `DataFrame` containing a new row for each element in the given array or map. Uses the default column name col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 4.0.0.

Parameters

**collection**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Target column to work on.

Returns

`DataFrame`

Examples

Example 1: Exploding an array column

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode(sf.array(sf.lit(1), sf.lit(2), sf.lit(3))).show()
+---+
|col|
+---+
|  1|
|  2|
|  3|
+---+

```


Example 2: Exploding a map column

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode(
...     sf.create_map(sf.lit("a"), sf.lit("b"), sf.lit("c"), sf.lit("d"))
... ).show()
+---+-----+
|key|value|
+---+-----+
|  a|    b|
|  c|    d|
+---+-----+

```


Example 3: Exploding an array of struct column

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode(sf.array(
...     sf.named_struct(sf.lit("a"), sf.lit(1), sf.lit("b"), sf.lit(2)),
...     sf.named_struct(sf.lit("a"), sf.lit(3), sf.lit("b"), sf.lit(4))
... )).select("col.*").show()
+---+---+
|  a|  b|
+---+---+
|  1|  2|
|  3|  4|
+---+---+

```


Example 4: Exploding an empty array column

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode(sf.array()).show()
+---+
|col|
+---+
+---+

```


Example 5: Exploding an empty map column

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode(sf.create_map()).show()
+---+-----+
|key|value|
+---+-----+
+---+-----+

```


# pyspark.sql.tvf.TableValuedFunction.explode_outer — PySpark 4.0.1 documentation
TableValuedFunction.explode\_outer(_collection_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.explode_outer)
[#](#pyspark.sql.tvf.TableValuedFunction.explode_outer "Permalink to this definition")

Returns a `DataFrame` containing a new row for each element with position in the given array or map. Unlike explode, if the array/map is null or empty then null is produced. Uses the default column name col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 4.0.0.

Parameters

**collection**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

target column to work on.

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.explode_outer(sf.array(sf.lit("foo"), sf.lit("bar"))).show()
+---+
|col|
+---+
|foo|
|bar|
+---+
>>> spark.tvf.explode_outer(sf.array()).show()
+----+
| col|
+----+
|NULL|
+----+
>>> spark.tvf.explode_outer(sf.create_map(sf.lit("x"), sf.lit(1.0))).show()
+---+-----+
|key|value|
+---+-----+
|  x|  1.0|
+---+-----+
>>> spark.tvf.explode_outer(sf.create_map()).show()
+----+-----+
| key|value|
+----+-----+
|NULL| NULL|
+----+-----+

```

# pyspark.sql.tvf.TableValuedFunction.inline — PySpark 4.0.1 documentation
TableValuedFunction.inline(_input_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.inline)
[#](#pyspark.sql.tvf.TableValuedFunction.inline "Permalink to this definition")

Explodes an array of structs into a table.

This function takes an input column containing an array of structs and returns a new column where each struct in the array is exploded into a separate row.

New in version 4.0.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

Input column of values to explode.

Returns

`DataFrame`

Examples

Example 1: Using inline with a single struct array

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.inline(sf.array(
...     sf.named_struct(sf.lit("a"), sf.lit(1), sf.lit("b"), sf.lit(2)),
...     sf.named_struct(sf.lit("a"), sf.lit(3), sf.lit("b"), sf.lit(4))
... )).show()
+---+---+
|  a|  b|
+---+---+
|  1|  2|
|  3|  4|
+---+---+

```


Example 2: Using inline with an empty struct array column

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.inline(sf.array().astype("array<struct<a:int,b:int>>")).show()
+---+---+
|  a|  b|
+---+---+
+---+---+

```


Example 3: Using inline with a struct array column containing null values

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.inline(sf.array(
...     sf.named_struct(sf.lit("a"), sf.lit(1), sf.lit("b"), sf.lit(2)),
...     sf.lit(None),
...     sf.named_struct(sf.lit("a"), sf.lit(3), sf.lit("b"), sf.lit(4))
... )).show()
+----+----+
|   a|   b|
+----+----+
|   1|   2|
|NULL|NULL|
|   3|   4|
+----+----+

```

# pyspark.sql.tvf.TableValuedFunction.inline_outer — PySpark 4.0.1 documentation
TableValuedFunction.inline\_outer(_input_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.inline_outer)
[#](#pyspark.sql.tvf.TableValuedFunction.inline_outer "Permalink to this definition")

Explodes an array of structs into a table. Unlike inline, if the array is null or empty then null is produced for each nested column.

New in version 4.0.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

input column of values to explode.

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.inline_outer(sf.array(
...     sf.named_struct(sf.lit("a"), sf.lit(1), sf.lit("b"), sf.lit(2)),
...     sf.named_struct(sf.lit("a"), sf.lit(3), sf.lit("b"), sf.lit(4))
... )).show()
+---+---+
|  a|  b|
+---+---+
|  1|  2|
|  3|  4|
+---+---+
>>> spark.tvf.inline_outer(sf.array().astype("array<struct<a:int,b:int>>")).show()
+----+----+
|   a|   b|
+----+----+
|NULL|NULL|
+----+----+

```


# pyspark.sql.tvf.TableValuedFunction.json_tuple — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.tvf.TableValuedFunction.json\_tuple

TableValuedFunction.json\_tuple(_input_, _\*fields_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.json_tuple)
[#](#pyspark.sql.tvf.TableValuedFunction.json_tuple "Permalink to this definition")

Creates a new row for a json column according to the given field names.

New in version 4.0.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

string column in json format

**fields**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

a field or fields to extract

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.json_tuple(
...     sf.lit('{"f1": "value1", "f2": "value2"}'), sf.lit("f1"), sf.lit("f2")
... ).show()
+------+------+
|    c0|    c1|
+------+------+
|value1|value2|
+------+------+

```



# pyspark.sql.tvf.TableValuedFunction.posexplode — PySpark 4.0.1 documentation
TableValuedFunction.posexplode(_collection_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.posexplode)
[#](#pyspark.sql.tvf.TableValuedFunction.posexplode "Permalink to this definition")

Returns a `DataFrame` containing a new row for each element with position in the given array or map. Uses the default column name pos for position, and col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 4.0.0.

Parameters

**collection**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

target column to work on.

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.posexplode(sf.array(sf.lit(1), sf.lit(2), sf.lit(3))).show()
+---+---+
|pos|col|
+---+---+
|  0|  1|
|  1|  2|
|  2|  3|
+---+---+
>>> spark.tvf.posexplode(sf.create_map(sf.lit("a"), sf.lit("b"))).show()
+---+---+-----+
|pos|key|value|
+---+---+-----+
|  0|  a|    b|
+---+---+-----+

```


# pyspark.sql.tvf.TableValuedFunction.posexplode_outer — PySpark 4.0.1 documentation
TableValuedFunction.posexplode\_outer(_collection_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.posexplode_outer)
[#](#pyspark.sql.tvf.TableValuedFunction.posexplode_outer "Permalink to this definition")

Returns a `DataFrame` containing a new row for each element with position in the given array or map. Unlike posexplode, if the array/map is null or empty then the row (null, null) is produced. Uses the default column name pos for position, and col for elements in the array and key and value for elements in the map unless specified otherwise.

New in version 4.0.0.

Parameters

**collection**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

target column to work on.

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.posexplode_outer(sf.array(sf.lit("foo"), sf.lit("bar"))).show()
+---+---+
|pos|col|
+---+---+
|  0|foo|
|  1|bar|
+---+---+
>>> spark.tvf.posexplode_outer(sf.array()).show()
+----+----+
| pos| col|
+----+----+
|NULL|NULL|
+----+----+
>>> spark.tvf.posexplode_outer(sf.create_map(sf.lit("x"), sf.lit(1.0))).show()
+---+---+-----+
|pos|key|value|
+---+---+-----+
|  0|  x|  1.0|
+---+---+-----+
>>> spark.tvf.posexplode_outer(sf.create_map()).show()
+----+----+-----+
| pos| key|value|
+----+----+-----+
|NULL|NULL| NULL|
+----+----+-----+

```




# pyspark.sql.tvf.TableValuedFunction.range — PySpark 4.0.1 documentation
TableValuedFunction.range(_start_, _end\=None_, _step\=1_, _numPartitions\=None_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.range)
[#](#pyspark.sql.tvf.TableValuedFunction.range "Permalink to this definition")

Create a `DataFrame` with single [`pyspark.sql.types.LongType`](about:blank/pyspark.sql.types.LongType.html#pyspark.sql.types.LongType "pyspark.sql.types.LongType") column named `id`, containing elements in a range from `start` to `end` (exclusive) with step value `step`.

New in version 4.0.0.

Parameters

**start**int

the start value

**end**int, optional

the end value (exclusive)

**step**int, optional

the incremental step (default: 1)

**numPartitions**int, optional

the number of partitions of the DataFrame

Returns

`DataFrame`

Examples

```
>>> spark.tvf.range(1, 7, 2).show()
+---+
| id|
+---+
|  1|
|  3|
|  5|
+---+

```


If only one argument is specified, it will be used as the end value.

```
>>> spark.tvf.range(3).show()
+---+
| id|
+---+
|  0|
|  1|
|  2|
+---+

```

# pyspark.sql.tvf.TableValuedFunction.sql_keywords — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.tvf.TableValuedFunction.sql\_keywords

TableValuedFunction.sql\_keywords()
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.sql_keywords)
[#](#pyspark.sql.tvf.TableValuedFunction.sql_keywords "Permalink to this definition")

Get Spark SQL keywords.

New in version 4.0.0.

Returns

`DataFrame`

Examples

```
>>> spark.tvf.sql_keywords().show()
+-------------+--------+
|      keyword|reserved|
+-------------+--------+
...
+-------------+--------+...

```


# pyspark.sql.tvf.TableValuedFunction.stack — PySpark 4.0.1 documentation
*   [](../../../index.html)
*   [API Reference](../../index.html)

*   [Functions](../functions.html)
*   pyspark.sql.tvf.TableValuedFunction.stack

TableValuedFunction.stack(_n_, _\*fields_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.stack)
[#](#pyspark.sql.tvf.TableValuedFunction.stack "Permalink to this definition")

Separates col1, …, colk into n rows. Uses column names col0, col1, etc. by default unless specified otherwise.

New in version 4.0.0.

Parameters

**n**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

the number of rows to separate

**fields**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

input elements to be separated

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.stack(sf.lit(2), sf.lit(1), sf.lit(2), sf.lit(3)).show()
+----+----+
|col0|col1|
+----+----+
|   1|   2|
|   3|NULL|
+----+----+

```



# pyspark.sql.tvf.TableValuedFunction.variant_explode — PySpark 4.0.1 documentation
TableValuedFunction.variant\_explode(_input_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.variant_explode)
[#](#pyspark.sql.tvf.TableValuedFunction.variant_explode "Permalink to this definition")

Separates a variant object/array into multiple rows containing its fields/elements.

Its result schema is struct<pos int, key string, value variant>. pos is the position of the field/element in its parent object/array, and value is the field/element value. key is the field name when exploding a variant object, or is NULL when exploding a variant array. It ignores any input that is not a variant array/object, including SQL NULL, variant null, and any other variant values.

New in version 4.0.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

input column of values to explode.

Returns

`DataFrame`

Examples

Example 1: Using variant\_explode with a variant array

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.variant_explode(sf.parse_json(sf.lit('["hello", "world"]'))).show()
+---+----+-------+
|pos| key|  value|
+---+----+-------+
|  0|NULL|"hello"|
|  1|NULL|"world"|
+---+----+-------+

```


Example 2: Using variant\_explode with a variant object

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.variant_explode(sf.parse_json(sf.lit('{"a": true, "b": 3.14}'))).show()
+---+---+-----+
|pos|key|value|
+---+---+-----+
|  0|  a| true|
|  1|  b| 3.14|
+---+---+-----+

```


Example 3: Using variant\_explode with an empty variant array

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.variant_explode(sf.parse_json(sf.lit('[]'))).show()
+---+---+-----+
|pos|key|value|
+---+---+-----+
+---+---+-----+

```


Example 4: Using variant\_explode with an empty variant object

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.variant_explode(sf.parse_json(sf.lit('{}'))).show()
+---+---+-----+
|pos|key|value|
+---+---+-----+
+---+---+-----+

```


# pyspark.sql.tvf.TableValuedFunction.variant_explode_outer — PySpark 4.0.1 documentation
TableValuedFunction.variant\_explode\_outer(_input_)
[\[source\]](about:blank/_modules/pyspark/sql/tvf.html#TableValuedFunction.variant_explode_outer)
[#](#pyspark.sql.tvf.TableValuedFunction.variant_explode_outer "Permalink to this definition")

Separates a variant object/array into multiple rows containing its fields/elements.

Its result schema is struct<pos int, key string, value variant>. pos is the position of the field/element in its parent object/array, and value is the field/element value. key is the field name when exploding a variant object, or is NULL when exploding a variant array. Unlike variant\_explode, if the given variant is not a variant array/object, including SQL NULL, variant null, and any other variant values, then NULL is produced.

New in version 4.0.0.

Parameters

**input**[`Column`](about:blank/pyspark.sql.Column.html#pyspark.sql.Column "pyspark.sql.Column")

input column of values to explode.

Returns

`DataFrame`

Examples

```
>>> import pyspark.sql.functions as sf
>>> spark.tvf.variant_explode_outer(sf.parse_json(sf.lit('["hello", "world"]'))).show()
+---+----+-------+
|pos| key|  value|
+---+----+-------+
|  0|NULL|"hello"|
|  1|NULL|"world"|
+---+----+-------+
>>> spark.tvf.variant_explode_outer(sf.parse_json(sf.lit('[]'))).show()
+----+----+-----+
| pos| key|value|
+----+----+-----+
|NULL|NULL| NULL|
+----+----+-----+
>>> spark.tvf.variant_explode_outer(sf.parse_json(sf.lit('{"a": true, "b": 3.14}'))).show()
+---+---+-----+
|pos|key|value|
+---+---+-----+
|  0|  a| true|
|  1|  b| 3.14|
+---+---+-----+
>>> spark.tvf.variant_explode_outer(sf.parse_json(sf.lit('{}'))).show()
+----+----+-----+
| pos| key|value|
+----+----+-----+
|NULL|NULL| NULL|
+----+----+-----+

```


