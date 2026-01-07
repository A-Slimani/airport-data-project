SELECT
  EXTRACT(HOUR FROM scheduled_time::TIME) AS "flight_hour",
  COUNT(*) AS "total_flights",
  COUNT(CASE WHEN delay_status='delayed' THEN 1 END) AS "delayed_flights",
  COALESCE(ROUND(
    COUNT(CASE WHEN delay_status='delayed' THEN 1 END)::NUMERIC / COUNT(*)
    ,4
  ) * 100, 0) AS "delay_percentage",
  COALESCE(AVG(
    CASE WHEN delay_status='delayed' THEN delay_duration::INTERVAL END
  ), '00:00')::TIME AS "average_delay_duration",
  COALESCE(ROUND(EXTRACT(EPOCH FROM
    AVG(
      CASE WHEN delay_status='delayed' THEN delay_duration::INTERVAL END
    ) 
  ), 0), 0) AS "average_delay_duration_seconds"
FROM {{ ref('int_flight_delays') }}
GROUP BY flight_hour 