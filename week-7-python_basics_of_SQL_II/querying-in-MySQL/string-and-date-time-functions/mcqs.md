## 1 String Manipulation
Assume that an employee named Diane Murphy has an employee number of 1002 in a dataset. What would the output of the following set of commands?

SELECT CONCAT(REVERSE(firstName) , '  ', UPPER(lastName))
FROM employees
WHERE employeeNumber=1002;

Result: enaiD MURPHY

## 2 Math Functions
abs() – Returns the absolute value of a number
ceil() – Returns the smallest integer value greater than or equal to the input number
floor() – Returns the largest integer value not greater than the argument
round() – Rounds a number to a specified number of decimal places
rand() – Returns a random floating-point value between 0 and 1
pow(a, b) – Returns the value a^b

 

Given the above math functions used in MySQL, what would the query given below return?

select ceil(rand() * 6);

Result: A random integer from 0 to 6.
