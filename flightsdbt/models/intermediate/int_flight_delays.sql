SELECT
  name,
  terminal_type,
  flight_direction,
  airline_code,
  airline,
  destinations,
  flight_numbers,
  scheduled_time,
  latest_time,
  latest_time - scheduled_time AS "delay_duration",
  CASE
    WHEN EXTRACT(EPOCH FROM (latest_time - scheduled_time)) > 0 THEN 'delayed' 
    WHEN EXTRACT(EPOCH FROM (latest_time - scheduled_time)) < 0 THEN 'early' 
    ELSE 'on-time' 
  END AS "delay_status",
  scheduled_date,
  estimated_date,
  status
FROM {{ ref('stg_flights_sydney') }}