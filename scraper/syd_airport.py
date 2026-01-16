from utils import download_json, upload_blob
from datetime import date, timedelta
import requests
import click

SYD_URL = 'https://www.sydneyairport.com.au/_a/flights'
DATE_YESTERDAY = date.today() - timedelta(days=1)
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0',
    'accept': 'application/json'
}


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
        return data
    except Exception as e:
        print(f"An error occurred when accessing the URL: {e}")


@click.command()
@click.option('--direction', default='departure')
@click.option('--terminal', default='international')
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
@click.option('--date', default=DATE_YESTERDAY)
def main(direction, terminal, download_dir, date):
    data = get_data(direction, terminal, date)    
    filename = f"sydney-{DATE_YESTERDAY}-{direction}-{terminal}.json"
    download_json(data, download_dir, filename)
    upload_blob(data, filename)


if __name__ == "__main__":
    main()