-- Script: 10-top_score.sql
-- Script to list all records of the table second_table, displaying score and name, ordered by score in descending order

SELECT score, name
FROM second_table
ORDER BY score DESC;
