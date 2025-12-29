from utils.db_utils import upload_to_db
from utils.web_utils import get_data
from utils.file_utils import download_json
from datetime import date, timedelta

BRI_URL = 'https://www.bne.com.au/sites/default/files/00API-Yesterday.json'

print('getting yesterdays data for Brisbane Airport...')
print("====")
current_date = date.today() - timedelta(days=1)

data = get_data(BRI_URL)
upload_to_db(data, date=current_date, table_name='raw_flights_bri')

print('DONE')
print('====')