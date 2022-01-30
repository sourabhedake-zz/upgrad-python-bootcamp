-- Spread
-- Description
-- Consider the following table marks part of a school database containing the following columns
-- Student_id : Storing the id of the student
-- Course     : Storing the name of the course 
-- Marks      : Storing the marks obtained by the student in the particular course
-- Write a query to determine the spread of the marks of the student having average marks greater than the overall average. Spread is defined as the difference between the highest and lowest marks obtained by the student.
-- The output should be as below
-- |Student_id|Marks|
use upgrad;

select student_id , max(marks) - min(marks) 'Spread'
from marks
group by student_id
having avg(marks) > (select avg(marks) from marks)
order by student_id;