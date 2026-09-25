CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY (
    -- Write your PostgreSQL query statement below.
    WITH sals AS (
        SELECT 
            DISTINCT E.salary AS sal
        FROM Employee E
        ORDER BY 
            E.salary DESC
    ), 
    ranked_sals AS (
        SELECT 
            RANK() OVER (ORDER BY sal DESC) AS salary_rank, 
            sal
        FROM sals
    )
    SELECT 
        sal AS getNthHighestSalary 
    FROM ranked_sals
    WHERE salary_rank = N
  );
END;
$$ LANGUAGE plpgsql;