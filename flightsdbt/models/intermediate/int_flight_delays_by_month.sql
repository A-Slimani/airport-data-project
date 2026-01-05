SELECT
  name,
  terminal_type,
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
  TO_CHAR(scheduled_date::DATE, 'YYYY-MM') AS "flight_month"
FROM {{ ref('stg_flights_sydney') }}