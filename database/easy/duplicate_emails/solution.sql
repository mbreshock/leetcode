-- Write your PostgreSQL query statement below
WITH email_counts AS (
    SELECT 
        email, 
        COUNT(*) AS n_copies
    FROM Person
    GROUP BY
        email
)
SELECT
    email
FROM email_counts
WHERE n_copies > 1