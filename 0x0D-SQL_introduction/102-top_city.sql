-- Script: 102-top_city.sql
-- Script to display the top 3 cities with the highest average temperature during July and August, ordered by temperature (descending)

SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)  -- Filter for July (6) and August (7)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
