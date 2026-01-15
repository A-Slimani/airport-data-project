from utils.file_utils import download_json
from utils.web_utils import get_syd_data
from utils.db_utils import upload_to_db 
from datetime import date, timedelta
from prefect import flow, task
import argparse

@task(retries=3, retry_delay_seconds=60)
def fetch_and_process_flight_data(terminal_type, flight_type, get_date):
    print(f"Getting {terminal_type} {flight_type} data...")

    data = get_syd_data(terminal_type, flight_type, get_date)

    upload_to_db(
        data,
        terminal_type=terminal_type,
        flight_type=flight_type,
        date=get_date,
        table_name='raw_flights_syd'
    )

    download_json(
        data,
        '/Users/aboud/programming/airport-data-project/data',
        f"sydney-{get_date}-{terminal_type}-{flight_type}.json",
    )

    return f"{terminal_type}-{flight_type} completed"

@flow(name="sydney-airport-data-pipeline", log_prints=True)
def main(get_date=None):
    if get_date is None:
        get_date = date.today() - timedelta(days=1)

    print(f"Getting Sydney Airport data for {get_date}...")

    combinations = [
        ('international', 'departure'),
        ('international', 'arrival'),
        ('domestic', 'departure'),
        ('domestic', 'arrival')
    ]

    results = []
    for terminal_type, flight_type in combinations:
        result = fetch_and_process_flight_data(terminal_type, flight_type, get_date)
        results.append(result)
    
    return results

if __name__ == "__main__":
   parser = argparse.ArgumentParser() 
   parser.add_argument("--date", default=None)
   args = parser.parse_args()

   main(get_date=args.date)
