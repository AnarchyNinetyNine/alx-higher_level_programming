-- Script: 16-no_link.sql
-- Script to list all records of the table second_table with a name value, displaying score and name, ordered by score in descending order

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
