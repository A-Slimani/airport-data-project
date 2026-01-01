# TODO LIST
- [ ] Get data for
    - [ ] Download each one into the folder
    - [ ] Melbourne
        - Blocked by cloudflare
    - [x] Brisbane 
        - Only has yesterdays flights from afternoon
    - [x] Perth 
        - Only has todays and tommorows flight data
    - [x] Adelaide 
        - [ ] Create dbt tables
        - Do I even have enough data for this
        - Just do it to ensure the schema is correct
        - Only got data for today
            - [x] Stg tables
            - [ ] Intermediate tables
            - [ ] Seperate tables
            - [ ] Merged tables

- [ ] Have more robust testing for dbt tables
    - [ ] Ensure I have the correct columns for calculating delays
        - `latest_time`
        - `scheduled_time`
        - In this format `MM:SS`
        - Write tests to check its valid
            - Maybe use great expectations
        - [ ] Create time columns
        - [ ] Add great expectations?

## Low Priority

### Pipeline / ELT
- [ ] Add retries if data was not collected
- [ ] Find a backup solution for the current flight data
- [ ] Add logging

### Reporting
- [ ] Write about my intermediate table and decisions
- [ ] Write about how to flatten arrray in psql jsonb
    - Is there even anything to write about....

### Flight reporting
- [ ] Get top stats for delays to put on obsidian
    - [ ] For airline
    - [ ] ...

### DBT
- [ ] Create marts table
    - [x] For airline
    - [ ] For routes 
        - How to handle for flights with multiple routes
        - Should I flatten it as well?
    - [x] For time of day

### Dashboard
- [ ] Setup dashboard with streamlit 
    - [x] Create graphs tables for flight delays by airline
    - [ ] Setup home page
- [ ] Delay by hour graph make it ignore hours with no delays or no flights
- [ ] Find a way to show MM:SS instead of seconds on the `average_delay_graphs`

## DB
- [x] Implement materialised views to speed up queries
- [ ] Implement `jsonb_to_recordset`
- [ ] Rename flight_type column to flight_direction