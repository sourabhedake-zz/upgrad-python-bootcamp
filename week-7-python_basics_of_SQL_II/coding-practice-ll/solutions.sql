-- More Filtered Employees
-- Description
-- Write a query to retrieve the email addresses of all the employees who have an office code of 6 or report to employees with employee number '1088'. Arrange them in the reverse alphabetical order of their first names.

use upgrad;

select email from employees where officeCode = 6 or reportsTo = '1088' order by firstName desc;

-- Employees from Specific Office Codes
-- Description
-- Write a query to retrieve all the details of all the employees who have an office code from 2 to 4. Arrange them in the alphabetical order of their first names. Please click on the sample output to view it clearly.

use upgrad;

select * from employees where officeCode >= 2 and officeCode <= 4 order by firstName;

-- Employees with Odd-Numbered Office Codes
-- Description
-- Write a query to retrieve the extensions and office codes of all the employees having an odd-numbered office code. Arrange them in the alphabetical order of their first names.

use upgrad;

select extension, officeCode from employees where officeCode % 2 = 1 order by firstName;

-- Employees with Even-Numbered Office Codes
-- Description
-- Write a query to retrieve the extensions and office codes of all the employees having an even-numbered office code. Arrange them in the alphabetical order of their first names.

use upgrad;

select extension, officeCode from employees where officeCode % 2 = 0 order by firstName;

-- Lucky Employees
-- Description
-- Write a query to retrieve all the details of employees who don't report to anyone. Arrange them in the increasing order of their employee numbers. Please click on the sample output to view it clearly.

use upgrad;

select * from employees where reportsTo is NULL order by employeeNumber;