-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
-- SQL is fun
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
