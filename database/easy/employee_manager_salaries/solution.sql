-- Write your PostgreSQL query statement below
WITH mngr_salaries AS (
    SELECT 
        e1.id,
        e1.name, 
        e1.salary,
        e1.managerId,
        e2.salary AS manager_salary
    FROM Employee e1
    LEFT JOIN Employee e2
        ON e1.managerId = e2.id
)
SELECT 
    name AS "Employee"
FROM mngr_salaries
WHERE 
    salary > manager_salary;