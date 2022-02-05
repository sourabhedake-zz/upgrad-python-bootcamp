-- Subqueries
-- Description
-- Write a query to retrieve the names of all customers who have a credit limit greater than what La Rochelle Gifts has.
use upgrad;

select customerName from Customers where creditLimit > (select creditLimit from Customers where customerName = "La Rochelle Gifts");