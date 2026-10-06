SELECT s.category,
       COUNT(*) AS visits,
       SUM(v.price) AS revenue,
       ROUND(AVG(v.price),2) AS avg_price
FROM visits v
JOIN services s ON s.id = v.service_id
GROUP BY s.category
ORDER BY revenue DESC;
