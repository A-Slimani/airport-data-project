WITH flattened AS (
  SELECT 
    terminalType AS terminal,
    flightType AS flight_direction,
    unnest(flightData) AS flight_data
  FROM read_json_auto('abfss://airport-data@airportdataproject.dfs.core.windows.net/RAW/SYD/*.json')
)
SELECT
  flight_data.id AS id,
  terminal AS terminal,
  flight_direction AS flight_direction,
  CASE
    WHEN flight_data.airline='' THEN m.airline_name
    ELSE flight_data.airline
  END AS airline_name,
  flight_data.airlineCode AS airline_code,
  flight_data.destinations AS destinations,
  flight_data.flightNumbers AS flight_numbers,
  flight_data.terminalNumber AS terminal_number,
  flight_data.scheduledTime AS scheduled_time,
  flight_data.scheduledDate AS scheduled_date,
  NULLIF(flight_data.estimatedTime,'-') AS estimated_time,
  NULLIF(flight_data.estimatedDate,'-') AS estimated_date,
  flight_data.latestTime AS latest_time,
  flight_data.status AS status
FROM flattened f
LEFT JOIN {{ ref('missing_airlines') }} m
ON f.flight_data.airlineCode = m.airline_code

