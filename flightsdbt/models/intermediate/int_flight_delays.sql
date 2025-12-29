SELECT
  name,
  terminal_type,
  airline_code,
  airline,
  destinations,
  flight_numbers,
  scheduled_time,
  latest_time,
  latest_time::TIME - scheduled_time::TIME AS "delay_duration",
  CASE
    WHEN EXTRACT(EPOCH FROM (latest_time::TIME - scheduled_time::TIME)) > 0 THEN 'delayed' 
    WHEN EXTRACT(EPOCH FROM (latest_time::TIME - scheduled_time::TIME)) < 0 THEN 'early' 
    ELSE 'on-time' 
  END AS "delay_status",
  scheduled_date,
  estimated_date,
  status
FROM {{ ref('stg_flights_sydney') }}