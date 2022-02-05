-- Details of Employees
-- Description
-- Write a query to return the employee number, first name and last name of all the employees. Order the employees in the alphabetical order of their first names.

use upgrad;

select employeeNumber, firstName, lastName from employees order by firstName;

-- Employee Email IDs
-- Description
-- Write a query to return the email ids of all the employees in the increasing order of their employee numbers.

use upgrad;

select email from employees order by employeeNumber;

-- Employees with a Specific Office Code
-- Description
-- Write a query to retrieve the first names and last names of all the employees having an office code of 4. Arrange them in the alphabetical order of their last names.

use upgrad;

select firstName, lastName from employees where officeCode = 4 order by lastName;

-- All Employee Details
-- Description
-- Write a query to retrieve the entire data of all the employees from the employees table. Arrange them in the alphabetical order of their first names. Please click on the sample output to view it clearly.

use upgrad;

select * from employees order by firstName;

-- Filtered Employees
-- Description
-- Write a query to retrieve the email addresses of all the employees who have an office code of 6 and report to employees with code '1088'. Arrange these employees in the increasing order of their employee numbers.

use upgrad;

select email from employees where officeCode = 6 and reportsTo = '1088' order by employeeNumber;

