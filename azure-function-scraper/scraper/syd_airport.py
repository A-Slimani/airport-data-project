from .config import DATE_YESTERDAY, HEADERS
from .utils import download_file, upload_blob_az
import requests
import click

SYD_URL = 'https://www.sydneyairport.com.au/_a/flights'

def get_data(flight_dir, terminal_type, date):
    params = {
        "flightType": flight_dir,
        "terminalType": terminal_type,
        "date": date,
        "ascending": "true",
        "showAll": "true"
    }
    try:
        response = requests.get(SYD_URL, params=params, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        if data:
            return data
        else:
            raise ValueError("Response returned valid but empty JSON")
    except Exception as e:
        print(f"An error occurred when accessing the URL: {e}")


@click.command()
@click.option('--direction', default='departure')
@click.option('--terminal', default='international')
@click.option('--download-json', is_flag=True, default=False)
@click.option('--upload-az', is_flag=True, default=False)
@click.option('--download-dir', default='/home/aboud/programming/airport-data-project/data')
@click.option('--date', default=DATE_YESTERDAY)
def main(direction, terminal, download_dir, date, download_json, upload_az):
    data = get_data(direction, terminal, date)
    filename = f"sydney-{date}-{direction}-{terminal}.json"
    if download_json:
        download_file(data, download_dir, filename)
    if upload_az:
        upload_blob_az(data, filename, f"RAW/SYD")


if __name__ == "__main__":
    main()
