-- # Top 3 students
-- # Description
-- # Consider the 'upgrad' schema having a 'marks' table containing the following columns.
-- # application_id|email_id|physics|chemistry|mathematics
-- # The university needs to select the top 3 students to offer a seat. The students have to be selected on the basis of the total marks obtained in all three subjects. In case two students have the same total marks, a student with higher marks in mathematics is given priority. In case the deadlock still persists, higher marks in physics are given priority. Write a query that will provide the email for the top 3 students?
use upgrad;

select email_id
from marks
order by physics+mathematics+chemistry desc, mathematics desc, physics desc
limit 3;