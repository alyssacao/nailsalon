SELECT a.service, a.staffid, nt.name, a.service_count
FROM (
    SELECT service, staffid, DENSE_RANK() OVER (PARTITION BY service ORDER BY COUNT(*) DESC) AS service_rank,
           COUNT(*) AS service_count
    FROM appointment
    GROUP BY service, staffid
) a
JOIN nailtechnician nt ON a.staffid = nt.staffid::INT
WHERE a.service_rank = 1;