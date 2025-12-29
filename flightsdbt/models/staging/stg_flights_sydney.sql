WITH flattened_table AS (
  SELECT 
    name,     
    data ->> 'terminalType' AS "terminal_type",
    data ->> 'flightType'   AS "flight_type",
    jsonb_array_elements((data ->> 'flightData')::JSONB) AS "flight_data"
  FROM {{ source('database', 'raw_flights_syd') }}
)
SELECT  
  name,
  terminal_type,
  flight_type,
  flight_data ->> 'airlineCode'                AS airline_code,  
  CASE
    WHEN flight_data ->> 'airline'='' AND flight_data ->> 'airlineCode'='VJ' THEN 'VietJet'
    WHEN flight_data ->> 'airline'='' AND flight_data ->> 'airlineCode'='QN' THEN 'Skytrans'
    WHEN flight_data ->> 'airline'='' THEN NULL
    ELSE flight_data ->> 'airline'
  END AS airline,
  flight_data ->> 'destinations'               AS destinations, 
  flight_data ->> 'flightNumbers'              AS flight_numbers, 
  flight_data ->> 'terminalNumber'             AS terminal_number,
  flight_data ->> 'scheduledTime'              AS scheduled_time,
  flight_data ->> 'scheduledDate'              AS scheduled_date,
  NULLIF(flight_data ->> 'estimatedDate', '-') AS estimated_date,
  flight_data ->> 'latestTime'                 AS latest_time,
  flight_data ->> 'status'                     AS status
FROM flattened_table
WHERE 
  flight_data ->> 'airline' IS NOT NULL
  AND
  flight_data ->> 'airline' <> ''