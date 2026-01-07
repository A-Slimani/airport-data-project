SELECT
  airline,
  flight_month,
  terminal_type,
  flight_direction,
  COUNT(*) AS "total_flights",
  COUNT(CASE WHEN delay_status='delayed' THEN 1 END) AS "delayed_flights",
  ROUND(
    COUNT(CASE WHEN delay_status='delayed' THEN 1 END)::NUMERIC / COUNT(*)
    ,2
  ) * 100 AS "delay_percentage",
  AVG(
    CASE 
      WHEN delay_status='early' THEN '0'::INTERVAL 
      ELSE delay_duration::INTERVAL 
    END
  )::TIME AS "average_delay_duration",
  ROUND(EXTRACT(EPOCH FROM
    AVG(
      CASE 
        WHEN delay_status='early' THEN '0'::INTERVAL 
        ELSE delay_duration::INTERVAL 
      END
    ) 
  ), 0) AS "average_delay_duration_seconds"
FROM {{ ref('int_flight_delays_by_month') }}
GROUP BY airline, flight_month, terminal_type, flight_direction