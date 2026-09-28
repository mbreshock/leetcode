-- Write your PostgreSQL query statement below
WITH department_max AS (
    SELECT 
        E.departmentId, 
        D.name AS department_name,
        MAX(E.salary) AS max_salary
    FROM Employee E
    JOIN Department D
        ON E.departmentId = D.id
    GROUP BY
        E.departmentId,
        D.name
)
SELECT
    DM.department_name AS "Department", 
    E.name AS "Employee",
    E.salary AS "Salary"
FROM Employee E 
JOIN department_max DM 
    ON (E.departmentId = DM.departmentId AND 
        E.salary = DM.max_salary)