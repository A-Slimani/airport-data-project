from curl_cffi import requests as rq
from bs4 import BeautifulSoup 
import requests

HEADERS = {
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0',
  'accept': 'application/json'
}

SYD_URL = 'https://www.sydneyairport.com.au/_a/flights'

def get_syd_data(terminal_type, flight_type, date):
  params = {
    "flightType": flight_type,
    "terminalType": terminal_type,
    "date": date, 
    "sortColumn": "scheduled_time",
    "ascending": "true",
    "showAll": "true"
  }

  try:
    response = requests.get(SYD_URL, params=params, headers=HEADERS)  
    response.raise_for_status()

    data = response.json()

    return data
  
  except Exception as e:
    print(f"An error occurred when accessing the webpage: {e}")
  
def get_data(url):
  try:
    session = rq.Session(impersonate="chrome110")
    session.headers.update(HEADERS)

    response = session.get(url, allow_redirects=False)

    return {'data': response.json()} 
  
  except Exception as e:
    print(f"ERROR: {e}")


def get_per_data(date, url):
  try:
    session = rq.Session(impersonate="chrome110")
    session.headers.update(HEADERS)

    response = session.get(url, allow_redirects=False)

    soup = BeautifulSoup(response.text, 'html.parser')

    token = soup.find('input', {'name': '__RequestVerificationToken'}).get('value')

    form_data = {
      '__RequestVerificationToken': token,
      'scController': 'Flights',
      'scAction': 'GetFlightResults',
      'Nature': 'nature',
      'Date': date,
      'Time': '',
      'DomInt': '',
      'Terminal': '',
      'Query': '',
      'ItemstoSkip': 0
    } 

    response = session.post(url, data=form_data)

    return response.json()
  
  except Exception as e:
    print(f"An error occurred when accessing the webpage: {e}")


def get_mel_data():
  params = {
    'queries[flights][query]': '',
    'queries[flights][facets][0]': 'airlineCode',
    'queries[flights][limit]': 5,  
    'queries[flights][offset]': 0,
    'queries[flights][locale]': 'en'
  }

  try:
    response = rq.get(MEL_URL, impersonate="chrome110")
    print(response.status_code)

    data = response.json()

    return data 
  
  except Exception as e:
    print(f"An error occurred when accessing the webpage: {e}")


    