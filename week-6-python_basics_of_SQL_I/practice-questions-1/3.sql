-- Self Join
-- Description
-- Consider a table named 'father' storing the details of all father-son pairs in a residential society. Write a code to determine the number of grandfather-grandson pairs in the society. For the purpose of the problem, consider grandson as son of one's son. Note that the table stores data in the following form﻿
-- |father_id|son_id|
use upgrad;

select count(*)
from father f1 inner join father f2
on f1.father_id = f2.son_id;
