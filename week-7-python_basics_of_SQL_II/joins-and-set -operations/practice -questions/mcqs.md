## 1 Joins
What will be the output of the following query?

    select id, col_1, col_2
    from table_1 a
    inner join table_2 b
    using(id)
    inner join table_3 c
    using(id_2)

Result: 
This query will perform an inner join of table_1 and table_2 on ‘id’ and then perform an inner join on ‘id_2’ with table_3.

## 2 Joins
You have been given the following two tables ‘Transactions’ and ‘Company’.

If you perform an inner join on these two tables on ‘Company_id’, then how many rows will the resulting table contain?

Result: 3

## 3 Joins
You have been given the following three tables ‘Transactions’, Company’ and ‘Headquarter’.

Suppose you want to get the company name corresponding to the highest amount paid in the ‘Transactions’ table. Which method will be the most efficient to perform such an operation?

Result:

Inner join the three tables and query for the maximum amount in the inner joined table directly.

## 4 Joins
Suppose you have been given the following two tables ‘Customers’ and ‘Orders’.

These two tables are to be joined on the ‘dept_no’ key.

Match each join type with the resulting table.
Select the correct option from below.

Result: 
A-5, B-3, C-1, D-2, E-4
