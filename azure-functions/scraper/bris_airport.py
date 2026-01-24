from utils import download_file, upload_blob_az
from config import DATE_YESTERDAY, HEADERS
from datetime import date, timedelta
import requests
import click

BRIS_URL = 'https://www.bne.com.au/sites/default/files/00API-Yesterday.json'


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
@click.option('--upload-az', is_flag=True, default=False)
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
def main(download_dir, download_json, upload_az):
    data = get_data()
    filename = f"brisbane-{DATE_YESTERDAY}.json" 
    if download_json:
        download_file(data, download_dir, filename)
    if upload_az:
        upload_blob_az(data, filename, "BRONZE/BRI")


if __name__ == "__main__":
    main()
