-- Script: 11-best_score.sql
-- Script to list all records with a score >= 10 from the table second_table, displaying score and name, ordered by score in descending order

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
