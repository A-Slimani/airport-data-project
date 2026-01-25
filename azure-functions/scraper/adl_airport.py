from .utils import download_file, upload_blob
from curl_cffi import requests as rq
from config import HEADERS, DATE_YESTERDAY
import click

ADL_URL = "https://adelaideairport.com.au/api/flight-information/filtered-flights" 

def get_data():
    try:
        session = rq.Session(impersonate="chrome110")
        session.headers.update(HEADERS)
        response = session.get(ADL_URL, allow_redirects=False)
        return response.json()
    except Exception as e:
        print(f"An error occurred when accessing the URL: {e}")


@click.command()
@click.option('--download-json', is_flag=True, default=False)
@click.option('--download-dir', default='/Users/aboud/programming/airport-data-project/data')
def main(download_dir, download_json):
    data = get_data()
    filename = f"adelaide-{DATE_YESTERDAY}.json"
    if download_json:
        download_file(data, download_dir, filename)
    upload_blob(data, filename)


if __name__ == "__main__":
    main()
