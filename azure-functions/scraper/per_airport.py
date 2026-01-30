from .utils import download_file, upload_blob
from .config import HEADERS, DATE_YESTERDAY, DATE_TODAY
from curl_cffi import requests as rq
from bs4 import BeautifulSoup
import click

PER_URL = "https://www.perthairport.com.au/flights/departures-and-arrivals"

def get_data():
    try:
        session = rq.Session(impersonate="chrome110")
        session.headers.update(HEADERS)
        response = session.get(PER_URL, allow_redirects=False)
        soup = BeautifulSoup(response.text, 'html.parser')
        token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')
        form_data = {
            '__RequestVerificationToken': token,
            'scController': 'Flights',
            'scAction': 'GetFlightResults',
            'Nature': 'nature',
            'Date': date.today(),
            'Time': '',
            'DomInt': '',
            'Terminal': '',
            'Query': '',
            'ItemstoSkip': 0
        }
        response = session.post(PER_URL, data=form_data)
        return response.json()
    except Exception as e:
        print(f"An error occurred when accessing the webpage: {e}")


@click.command()
@click.option('--download-json', is_flag=True, default=False)
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
def main(download_dir, download_json):
    data = get_data()
    filename = f"perth-{DATE_TODAY}.json"
    if download_json:
        download_file(data, download_dir, filename)
    upload_blob(data, filename)


if __name__ == "__main__":
    main()
