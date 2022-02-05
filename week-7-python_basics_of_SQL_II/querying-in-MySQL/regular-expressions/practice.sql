-- Basic Regex
-- Description
-- Write a query to retrieve the employee numbers and first names of all employees having the substring on in their first names.
use upgrad;

select employeeNumber, firstName from Employees where firstName like "%on%"