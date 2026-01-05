WITH flattened_table AS (
  SELECT 
    name,     
    data ->> 'terminalType' AS "terminal_type",
    data ->> 'flightType'   AS "flight_type",
    jsonb_array_elements((data ->> 'flightData')::JSONB) AS "flight_data"
  FROM {{ source('database', 'raw_flights_syd') }}
), cleaned_table AS (
  SELECT
    ft.flight_data ->> 'id' AS "id",                           
    ft.name,
    ft.flight_type,
    ft.terminal_type,
    CASE
      WHEN ft.flight_data ->> 'airline'='' AND ft.flight_data ->> 'airlineCode'='VJ' THEN 'VietJet'
      WHEN ft.flight_data ->> 'airline'='' AND ft.flight_data ->> 'airlineCode'='QN' THEN 'Skytrans'
      WHEN ft.flight_data ->> 'airline'='' THEN NULL
      ELSE ft.flight_data ->> 'airline'
    END AS airline,
    ft.flight_data ->> 'flightNumbers'                    AS flight_numbers,
    ft.flight_data ->> 'airlineCode'                      AS airline_code,  
    ft.flight_data ->> 'destinations'                     AS destinations, 
    ft.flight_data ->> 'terminalNumber'                   AS terminal_number,
    (ft.flight_data ->> 'scheduledTime')::TIME            AS scheduled_time,
    ft.flight_data ->> 'scheduledDate'                    AS scheduled_date,
    NULLIF(ft.flight_data ->> 'estimatedDate', '-')       AS estimated_date,
    NULLIF(ft.flight_data ->> 'estimatedTime', '-')::TIME AS estimated_time,
    (ft.flight_data ->> 'latestTime')::TIME               AS latest_time,
    ft.flight_data ->> 'status'                           AS status
  FROM flattened_table ft
)
SELECT DISTINCT ON (id) * FROM cleaned_table
WHERE airline IS NOT NULL 