from utils.file_utils import download_json
from utils.db_utils import upload_to_db
from utils.web_utils import get_adl_data
from datetime import date, timedelta

MEL_URL = 'https://www.melbourneairport.com.au/api/data/search'

print('getting yesterdays data for Melbourne Airport...')
print("====")
current_date = date.today() - timedelta(days=1)

data = get_adl_data(PER_URL)

print(data)