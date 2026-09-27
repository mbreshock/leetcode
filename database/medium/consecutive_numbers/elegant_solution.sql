-- Write your PostgreSQL query statement below
WITH consecutive_counts AS (
    SELECT 
        num, 
        grp, 
        COUNT(*) AS run_length
    FROM (
        SELECT 
            num,
            id - ROW_NUMBER() OVER (PARTITION BY num ORDER BY id) AS grp
        FROM Logs
    )
    GROUP BY 
        num, grp
)
SELECT
    DISTINCT num AS "ConsecutiveNums"
FROM consecutive_counts 
WHERE run_length >= 3