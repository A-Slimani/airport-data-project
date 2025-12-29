from utils.db_utils import upload_to_db
from utils.web_utils import get_data
from utils.file_utils import download_json
from datetime import date, timedelta

ADL_URL = 'https://adelaideairport.com.au/api/flight-information/filtered-flights?timeframe=yesterday'

print('getting yesterdays data for Adelaide Airport...')
print("====")
current_date = date.today() - timedelta(days=1)
date_formatted = current_date.strftime("%m-%d-%Y")

data = get_data(ADL_URL)
print(data)
upload_to_db(data, date=current_date, table_name='raw_flights_adl')

print('DONE')
print('====')