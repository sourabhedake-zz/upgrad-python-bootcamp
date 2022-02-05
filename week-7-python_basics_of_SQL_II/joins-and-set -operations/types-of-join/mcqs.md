## 1 Joins in a Star Schema
What is the maximum number of tables that can be joined in a star schema in a single query?

Result: 3

## 2 Joins in a Star Schema
What is the maximum number of tables that can be joined in a star schema in a single query?

Result:

    select last_name, dept_name
    from employees e
    left join departments d
    on e.dept_id = d.dept_id;