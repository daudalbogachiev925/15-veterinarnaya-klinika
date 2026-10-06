SELECT diagnosis, COUNT(*) AS cases,
       ROUND(AVG(price),2) AS avg_price
FROM visits
WHERE diagnosis IS NOT NULL
GROUP BY diagnosis
ORDER BY cases DESC
LIMIT 20;
