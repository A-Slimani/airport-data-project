from utils import download_json, upload_blob
from datetime import date, timedelta
import requests
import click

BRIS_URL = 'https://www.bne.com.au/sites/default/files/00API-Yesterday.json'
DATE_YESTERDAY = date.today() - timedelta(days=1)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0',
    'accept': 'application/json'
}

def get_data():
    try:
        response = requests.get(BRIS_URL, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except Exception as e:
        print(f"An error occurred when accessing the URL: {e}")


@click.command()
@click.option('--download-json', is_flag=True, default=False)
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
def main(download_dir):
    data = get_data()
    filename = f"brisbane-{DATE_YESTERDAY}.json" 
    if download_json:
        download_json(data, download_dir, filename)
    upload_blob(data, filename)


if __name__ == "__main__":
    main()
