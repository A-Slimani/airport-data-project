from utils.db_utils import upload_to_db
from utils.web_utils import get_syd_data
from utils.file_utils import download_json
from datetime import date, timedelta
import argparse

current_date = date.today() - timedelta(days=1)

parser = argparse.ArgumentParser()
parser.add_argument("--date", default=current_date)

args = parser.parse_args()

get_date = args.date if args.date else current_date
  
print(f'Getting Sydney Airport data for {get_date}...')

# international - departure
data = get_syd_data('international', 'departure', get_date)
upload_to_db(data, terminal_type='international', flight_type='departure', date=get_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{get_date}-international-departure.json")

# international - arrival 
data = get_syd_data('international', 'arrival', get_date)
upload_to_db(data, terminal_type='international', flight_type='arrival', date=get_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{get_date}-international-arrival.json")

# domestic - departure
data = get_syd_data('domestic', 'departure', get_date)
upload_to_db(data, terminal_type='domestic', flight_type='departure', date=get_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{get_date}-domestic-departure.json")

# domestic - arrival 
data = get_syd_data('domestic', 'arrival', get_date)
upload_to_db(data, terminal_type='domestic', flight_type='arrival', date=get_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{get_date}-domestic-arrival.json")
