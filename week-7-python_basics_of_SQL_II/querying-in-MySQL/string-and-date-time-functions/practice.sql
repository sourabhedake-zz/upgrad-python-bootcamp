-- Basic String Functions
-- Description
-- Write a query to retrieve the full names of all the employees along with their employee numbers.


use upgrad;

select employeeNumber, CONCAT(firstName, ' ', lastName) as fullName  from Employees;