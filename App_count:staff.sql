SELECT staffid, COUNT(*) AS appointment_count
FROM appointment
GROUP BY staffid
ORDER BY appointment_count DESC;





