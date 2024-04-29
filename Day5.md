## SQL In-Built Functions

### String Functions:
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/1e7fc21f-6681-44f9-a94b-d514d82bab0c)

| Function                                      | Description                                           | Example                                         | Output          |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------------|-----------------|
| `CONCAT(str1, str2, ...)`                    | Concatenates strings                                 | `SELECT CONCAT('Hello', ' ', 'World');`        | `Hello World`   |
| `CONCAT_WS(separator, str1, str2, ...)`      | Concatenates strings with a separator                | `SELECT CONCAT_WS('-', '2022', '04', '25');`   | `2022-04-25`    |
| `LENGTH(str)`                                | Returns the length of a string                       | `SELECT LENGTH('Hello');`                      | `5`             |
| `CHAR_LENGTH(str)` or `CHARACTER_LENGTH(str)`| Returns the number of characters in a string         | `SELECT CHAR_LENGTH('Hello');`                 | `5`             |
| `UPPER(str)`                                 | Converts a string to uppercase                       | `SELECT UPPER('hello');`                       | `HELLO`         |
| `LOWER(str)`                                 | Converts a string to lowercase                       | `SELECT LOWER('HELLO');`                       | `hello`         |
| `SUBSTRING(str, start, length)` or `SUBSTR(str, start, length)` | Extracts a substring from a string       | `SELECT SUBSTRING('Hello World', 1, 5);`       | `Hello`         |
| `LEFT(str, length)`                          | Extracts characters from the left of a string        | `SELECT LEFT('Hello World', 5);`               | `Hello`         |
| `RIGHT(str, length)`                         | Extracts characters from the right of a string       | `SELECT RIGHT('Hello World', 5);`              | `World`         |
| `REPLACE(str, search_str, replace_str)`      | Replaces occurrences of a substring in a string     | `SELECT REPLACE('Hello World', 'World', 'Universe');` | `Hello Universe` |
| `LTRIM(str)`                                 | Removes leading spaces from a string                | `SELECT LTRIM('   Hello');`                    | `Hello`         |
| `RTRIM(str)`                                 | Removes trailing spaces from a string               | `SELECT RTRIM('Hello   ');`                    | `Hello`         |
| `TRIM([leading \| trailing \| both] [trim_str] FROM str)` | Removes leading, trailing, or both leading and trailing characters from a string | `SELECT TRIM('   Hello   ');` | `Hello` |
| `REVERSE(str)`                               | Reverses the characters in a string                 | `SELECT REVERSE('Hello');`                     | `olleH`         |
| `LOCATE(substr, str [, start])` or `INSTR(str, substr)` | Searches for a substring in a string and returns its position | `SELECT LOCATE('World', 'Hello World');` | `7` |
| `LPAD(str, length, pad_str)`                 | Left-pads a string with another string              | `SELECT LPAD('Hello', 10, '*');`               | `*****Hello`    |
| `RPAD(str, length, pad_str)`                 | Right-pads a string with another string             | `SELECT RPAD('Hello', 10, '*');`               | `Hello*****`    |


### Mathematical Functions:
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/b5525eb6-89c6-4f94-a296-d0c1346d083e)

| Function                                      | Description                                           | Example                                         | Output          |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------------|-----------------|
| `ABS(num)`                                   | Returns the absolute (positive) value of a number    | `SELECT ABS(-5);`                              | `5`             |
| `CEIL(num)` or `CEILING(num)`                | Rounds a number up to the nearest integer            | `SELECT CEIL(3.5);`                            | `4`             |
| `FLOOR(num)`                                 | Rounds a number down to the nearest integer          | `SELECT FLOOR(3.5);`                           | `3`             |
| `ROUND(num [, decimals])`                    | Rounds a number to a specified number of decimal places | `SELECT ROUND(3.14159, 2);`                  | `3.14`          |
| `SIGN(num)`                                  | Returns the sign of a number (-1, 0, or 1)           | `SELECT SIGN(-5);`                             | `-1`            |
| `MOD(num, divisor)`                          | Returns the remainder of a division operation        | `SELECT MOD(10, 3);`                           | `1`             |
| `SQRT(num)`                                  | Returns the square root of a number                  | `SELECT SQRT(25);`                             | `5`             |
| `POWER(num, exponent)`                       | Raises a number to the power of an exponent          | `SELECT POWER(2, 3);`                          | `8`             |
| `RAND([seed])`                               | Returns a random floating-point value between 0 and 1 | `SELECT RAND();`                              | (Random value)  |


### Date Functions:
![image](https://github.com/nandini-gangrade/Hexaware-Python-Training/assets/87817417/8561d419-094e-4ba1-91bc-847fdb62a65e)

| Function                                      | Description                                           | Example                                         | Output          |
|-----------------------------------------------|-------------------------------------------------------|-------------------------------------------------|-----------------|
| `NOW()`                                      | Returns the current date and time                    | `SELECT NOW();`                                | `2022-04-25 10:30:15` |
| `CURDATE()`                                  | Returns the current date                             | `SELECT CURDATE();`                            | `2022-04-25`    |
| `CURTIME()`                                  | Returns the current time                             | `SELECT CURTIME();`                            | `10:30:15`      |
| `DATE_FORMAT(date, format)`                  | Formats a date according to a specified format       | `SELECT DATE_FORMAT(NOW(), '%Y-%m-%d');`       | `2022-04-25`    |
| `DATE_ADD(date, INTERVAL value unit)`        | Adds a specified value to a date                     | `SELECT DATE_ADD('2022-04-25', INTERVAL 1 MONTH);` | `2022-05-25` |
| `DATE_SUB(date, INTERVAL value unit)`        | Subtracts a specified value from a date              | `SELECT DATE_SUB('2022-04-25', INTERVAL 7 DAY);` | `2022-04-18`   |
| `DATEDIFF(date1, date2)`                     | Returns the number of days between two dates         | `SELECT DATEDIFF('2022-04-30', '2022-04-25');` | `5`             |
| `DAYNAME(date)`                              | Returns the name of the day for a given date         | `SELECT DAYNAME('2022-04-25');`               | `Monday`        |
| `DAYOFMONTH(date)`                           | Returns the day of the month for a given date        | `SELECT DAYOFMONTH('2022-04-25');`            | `25`            |
| `DAYOFWEEK(date)`                            | Returns the day of the week for a given date         | `SELECT DAYOFWEEK('2022-04-25');`             | `2` (Monday)    |
| `DAYOFYEAR(date)`                            | Returns the day of the year for a given date         | `SELECT DAYOFYEAR('2022-04-25');`             | `115`           |
| `MONTH(date)`                                | Returns the month for a given date                   | `SELECT MONTH('2022-04-25');`                 | `4`             |
| `YEAR(date)`                                 | Returns the year for a given date                    | `SELECT YEAR('2022-04-25');`                  | `2022`          |
| `HOUR(time)`                                 | Returns the hour component of a time value           | `SELECT HOUR('10:30:15');`                    | `10`            |
| `MINUTE(time)`                               | Returns the minute component of a time value         | `SELECT MINUTE('10:30:15');`                  | `30`            |
| `SECOND(time)`                               | Returns the second component of a time value         | `SELECT SECOND('10:30:15');`                  | `15`            |
| `TIMESTAMPDIFF(unit, start_datetime, end_datetime)` | Returns the difference between two datetime expressions based on a specified unit | `SELECT TIMESTAMPDIFF(DAY, '2022-04-25', '2022-05-01');` | `6` (days) |
| `TIMESTAMPADD(unit, value, datetime)`       | Adds a specified value to a datetime expression based on a specified unit | `SELECT TIMESTAMPADD(MONTH, 1, '2022-04-25');` | `2022-05-25` |
| `UNIX_TIMESTAMP([datetime])`                | Returns the number of seconds since the Unix epoch   | `SELECT UNIX_TIMESTAMP('2022-04-25 10:30:15');` | `1671970215`   |