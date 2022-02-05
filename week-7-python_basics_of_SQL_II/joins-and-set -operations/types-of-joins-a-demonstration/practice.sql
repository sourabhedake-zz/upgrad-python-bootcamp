-- Types of Joins
-- Description
-- Write a query to list the names of all customers who have placed at least one order.



-- Sample Output

-- customerName

-- Atelier graphique


use upgrad;

select  distinct customerName from Customers c inner join orders o on c.customerNumber = o.customerNumber ;
