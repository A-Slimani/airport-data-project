from utils.db_utils import upload_to_db
from utils.web_utils import get_syd_data
from utils.file_utils import download_json
from datetime import date, timedelta


print('getting yesterdays data for Sydney Airport...')
print("====")
current_date = date.today() - timedelta(days=1)

# international - departure
data = get_syd_data('international', 'departure', current_date)
upload_to_db(data, terminal_type='international', flight_type='departure', date=current_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{current_date}-international-departure.json")

# international - arrival 
data = get_syd_data('international', 'arrival', current_date)
upload_to_db(data, terminal_type='international', flight_type='arrival', date=current_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{current_date}-international-arrival.json")

# domestic - departure
data = get_syd_data('domestic', 'departure', current_date)
upload_to_db(data, terminal_type='domestic', flight_type='departure', date=current_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{current_date}-domestic-departure.json")

# domestic - arrival 
data = get_syd_data('domestic', 'arrival', current_date)
upload_to_db(data, terminal_type='domestic', flight_type='arrival', date=current_date, table_name='raw_flights_syd')
download_json(data, '/Users/aboud/programming/airport-data-project/data', f"sydney-{current_date}-domestic-arrival.json")

print('DONE')
print('====')