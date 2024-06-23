-- Script: 8-cities_of_california_subquery.sql
-- Script to list all cities of California from the database hbtn_0d_usa

-- Select all cities of California without using JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY cities.id ASC;

