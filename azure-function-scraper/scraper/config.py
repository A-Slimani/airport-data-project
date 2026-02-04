from datetime import date, datetime, timedelta

HEADERS = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/120.0",
    "accept": "application/json"
}

DATE_YESTERDAY = date.today() - timedelta(days=1)
DATE_TODAY = date.today()

# SPECIFIC FOR MELBOURNE
yesterday_start = datetime.today() - timedelta(days=1)
yesterday_start = yesterday_start.replace(hour=0, minute=0, second=0, microsecond=0)
yesterday_end = yesterday_start.replace(hour=23, minute=59, second=59)

TIMESTAMP_YESTERDAY_START = int(yesterday_start.timestamp() * 1000)
TIMESTAMP_YESTERDAY_END = int(yesterday_end.timestamp() * 1000)
