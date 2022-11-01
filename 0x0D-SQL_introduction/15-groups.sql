-- Display number of records with same score using COUNT, ORDER BY, GROUP BY
-- Display records with same score in second_table
SELECT score, COUNT(*) AS 'number' FROM second_table
GROUP BY score
ORDER BY score DESC;
