from utils.db_utils import upload_to_db
from utils.web_utils import get_per_data
from utils.file_utils import download_json
from datetime import date, timedelta

PER_URL = 'https://www.perthairport.com.au/flights/departures-and-arrivals'

print('getting yesterdays data for Perth Airport...')
print("====")
# current_date = date.today() - timedelta(days=1)
date_formatted = date.today().strftime("%m-%d-%Y")

data = get_per_data(date_formatted, PER_URL)
upload_to_db(data, date=date.today(), table_name='raw_flights_per')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"perth-{date.today()}.json")

print('DONE')
print('====')