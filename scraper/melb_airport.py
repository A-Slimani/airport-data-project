from utils import download_json, upload_blob
from datetime import datetime, timedelta
import requests
import click

MELB_URL = 'https://www.melbourneairport.com.au/api/data/search'

yesterday_start = datetime.today() - timedelta(days=1)
yesterday_start = yesterday_start.replace(hour=0, minute=0, second=0, microsecond=0)
yesterday_end = yesterday_start.replace(hour=23, minute=59, second=59)

start_ts = int(yesterday_start.timestamp() * 1000)
end_ts = int(yesterday_end.timestamp() * 1000)

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0',
    'accept': 'application/json'
}


def get_data(start_range, end_range):
    params = {
        "queries[flights][limit]": 1000,
        "queries[flights][filters]": f"scheduledTimeStamp: {start_range} TO {end_range}"
    }

    try:
        response = requests.get(MELB_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred when accessing the URL: {e}")



@click.command()
@click.option('--timestamp-start', default=start_ts)
@click.option('--timestamp-end', default=end_ts)
@click.option('--download-json', is_flag=True, default=False)
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
def main(timestamp_start, timestamp_end, download_dir):
    data = get_data(timestamp_start, timestamp_end)
    filename = f"melbourne-{yesterday_start.date()}.json"
    if download_json:
        download_json(data, download_dir, filename)
    upload_blob(data, filename)


if __name__ == "__main__":
    main()
