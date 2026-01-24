from datetime import date, timedelta

HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0",
    "accept": "application/json"
}

DATE_YESTERDAY = date.today() - timedelta(days=1)
