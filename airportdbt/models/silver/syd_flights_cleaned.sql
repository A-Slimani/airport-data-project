WITH flattened AS (
  SELECT 
    terminalType AS terminal,
    flightType AS flight_direction,
    unnest(flightData) AS flight_data
  FROM read_json_auto('abfss://airport-data@airportdataproject.dfs.core.windows.net/RAW/SYD/*.json')
)
SELECT
  flight_data.id AS id,
  terminal,
  flight_direction,
  flight_data.airline AS airline,
  flight_data.airlineCode AS airline_code,
  flight_data.destinations AS destinations,
  flight_data.flightNumbers AS flight_numbers,
  flight_data.terminalNumber AS terminal_number,
  flight_data.scheduledTime AS scheduled_time,
  flight_data.scheduledDate AS scheduled_date,
  flight_data.estimatedTime AS estimated_time,
  flight_data.estimatedDate AS estimated_date,
  flight_data.latestTime AS latest_time,
  flight_data.status AS status
FROM flattened

