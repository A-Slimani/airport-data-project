WITH dup_rec AS (
    SELECT
        flight_numbers,
        scheduled_date,
        flight_type
    FROM dbt.stg_flights_sydney
    GROUP BY
        flight_numbers,
        scheduled_date,
        flight_type
    HAVING COUNT(*) > 1
    ORDER BY scheduled_date::TIMESTAMP
)
SELECT 
	s.*,
    CASE
        WHEN LAG(s.scheduled_date) OVER (
           PARTITION BY 
               s.flight_numbers, 
               s.scheduled_date, 
               s.flight_type
           ORDER BY s.scheduled_date, s.scheduled_time
        ) = s.scheduled_date THEN 'PASS'
        WHEN IS NULL THEN 'PASS'
        ELSE 'FAIL'
    END AS "check"
FROM dup_rec d
INNER JOIN dbt.stg_flights_sydney s
ON 
    d.flight_numbers = s.flight_numbers
    AND
    d.scheduled_date = s.scheduled_date
    AND
    d.flight_type = s.flight_type
ORDER BY s.scheduled_date::TIMESTAMP, scheduled_time