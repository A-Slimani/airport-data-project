from curl_cffi import requests as rq
from config import HEADERS

URL = "https://adelaideairport.com.au/api/flight-information/filtered-flights"

def get_data():
    session = rq.Session(impersonate="chrome110")
    session.headers.update(HEADERS)
    response = session.get(URL)

    return response.json()

if __name__ == "__main__":
    print(get_data())