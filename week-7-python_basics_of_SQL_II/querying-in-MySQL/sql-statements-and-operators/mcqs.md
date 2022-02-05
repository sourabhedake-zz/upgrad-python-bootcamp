## 1 Pattern Matching
What would be the output of the following query: 'select * from employee where first_name like "%ee%";'?

Result: It will display the details of all the employees whose name contains ‘ee’.

## 2 Reading the Documentation
Refer to the MySQL documentation online and answer the following question:

Which of the following wildcards are supported in SQL?

Result: Both % and _ (underscore)

## 3 Operators
With SQL, how do you select all the records from a table named ‘employees’ where the ‘LastName’ is alphabetically between (and includes) ‘Joshi’ and ‘Sharma’?

Result: select * from employees where LastName between ‘Joshi’ and ‘Sharma’;

## 4 Operators
Which of the queries given below would return the same output? More than one option may be correct.

Result:
    select * from employees where EmpID in (2,3,4, 5);
    select * from employees where EmpID between 2 and 5;
    select * from employees where EmpID >= 2 and EmpID <= 5;

