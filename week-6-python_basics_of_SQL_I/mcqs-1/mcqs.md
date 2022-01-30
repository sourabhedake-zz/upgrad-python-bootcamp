## 1 Relational Databases
Which of the following is not part of the ACID characteristics supported by relational databases?

Result:
Computational
Indexed

## 2 Relational Database
Which of the following is true with regards to the consistency property supported by all relational databases?

Result: It ensures that a change in any value is consistent with other values at the same instant.

## 3 Non-Relational Database
Which of the following properties is most commonly compromised in non-relational databases in favour of the other three in sense of the CAP theorem?

Result: Consistency

## 4 Missing Values
Consider a table named 'student' in a university database. One of the numerous columns in the student table holds the marks obtained by the student in the secondary exams. Due to various reasons, not all students have been able to update their secondary exam marks. The 'seconndary_marks' marks column of the student table is as below.

| secondary_marks |
|----|
| 88 |
| 87 |
| NULL |
| 78 |
| 88 |
| 91 |
| NULL |
| 85 |
| NULL |
| 97 |
| 98 |
| 75 |

Which of the following queries will provide with you the same output as the below query?

    select *
    from student;

Result: None of the above

## 5 Joins
Consider two tables 'table_1' and 'table_2' as below 

| column_a |	column_b |
|---|---|
| 23 |	34 |
| 23 |	46 |
| 21 |	43 |
| 20 |	34 |
| 18 |	46 |

(table_1)

| column_a |	column_b |
|---|---|
| 23 |	98 |
| 23 |	97 |
| 10 |	30 |
| 20 |	NULL |
| 21 |	9 |
| 34 |	29 |

(table_2)

How many rows will be part of the output of the following query?

    select *
    from table_1, table_2
    where table_1.column_a = table_2.column_a ;

Result: 6

## 6 String function
From your knowledge of string functions, predict the output of the following piece of code?

    select insert ('Mahaveer' ,3 , 4, 'Jain') ;

Result: MaJainer
