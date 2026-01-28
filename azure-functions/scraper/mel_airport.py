from .utils import download_file, upload_blob_az
from .config import (
    DATE_YESTERDAY,
    HEADERS,
    TIMESTAMP_YESTERDAY_START,
    TIMESTAMP_YESTERDAY_END
)
from datetime import datetime, timedelta
import requests
import click

MELB_URL = 'https://www.melbourneairport.com.au/api/data/search'


def get_data(start_range, end_range):
    params = {
        "queries[flights][limit]": 1000,
        "queries[flights][filters]": f"scheduledTimeStamp: {start_range} TO {end_range}"
    }
    try:
        response = requests.get(MELB_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        if data:
            return data
        else:
            raise ValueError("Response returned valid but empty JSON")
    except Exception as e:
        print(f"An error occurred when accessing the URL: {e}")


@click.command()
@click.option('--timestamp-start', default=TIMESTAMP_YESTERDAY_START)
@click.option('--timestamp-end', default=TIMESTAMP_YESTERDAY_END)
@click.option('--download-json', is_flag=True, default=False)
@click.option('--upload-az', is_flag=True, default=False)
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
def main(timestamp_start, timestamp_end, download_dir, download_json, upload_az):
    data = get_data(timestamp_start, timestamp_end)
    filename = f"melbourne-{DATE_YESTERDAY}.json"
    if download_json:
        download_file(data, download_dir, filename)
    if upload_az:
        upload_blob_az(data, filename, "RAW/MEL")


if __name__ == "__main__":
    main()
