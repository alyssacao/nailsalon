SELECT c.c_id, c.firstname, c.lastname, COUNT(a.c_id) AS appointment_count
FROM customer c
JOIN appointment a ON c.c_id = a.c_id
GROUP BY c.c_id, c.firstname, c.lastname
HAVING COUNT(a.c_id) > 1;