WITH flattened_table AS (
  SELECT
    name,
    jsonb_array_elements((data ->> 'data')::JSONB) AS "flight_data"
  FROM {{ source('database', 'raw_flights_adl')}}
)
SELECT
  name,
  CASE
    WHEN flight_data ->> 'flightType' = 'D' THEN 'domestic'
    WHEN flight_data ->> 'flightType' = 'I' THEN 'interational'
  END AS terminal_type,
  CASE
    WHEN flight_data ->> 'direction' = 'D' THEN 'departure'
    WHEN flight_data ->> 'direction' = 'A' THEN 'arrival'
  END AS flight_type,
  flight_data ->> 'airlineCode' AS airline_code,
  flight_data ->> 'airlineName' AS airline,
  CASE
    WHEN flight_data ->> 'direction' = 'D' THEN flight_data ->> 'toName' 
    WHEN flight_data ->> 'direction' = 'A' THEN flight_data ->> 'fromName' 
  END AS destinations,
  flight_data ->> 'flightNumber' AS flight_number,
  flight_data ->> 'scheduledDate' AS scheduled_time,
  flight_data ->> 'scheduledDate' AS scheduled_date,
  flight_data ->> 'estimatedDate' AS estimated_date
FROM flattened_table

