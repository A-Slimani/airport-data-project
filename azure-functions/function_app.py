from scraper.syd_airport import get_data as get_data_syd
from scraper.config import DATE_YESTERDAY
from scraper.utils import upload_blob_az
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="my_timer", run_on_startup=True)
def timer_trigger_example(my_timer: func.TimerRequest) -> None:
    logging.info("starting sydney scraper")

    direction = "departure"
    terminal = "international"
    filename = f"sydney-{DATE_YESTERDAY}-{direction}-{terminal}.json"
    data = get_data_syd(direction, terminal, DATE_YESTERDAY)
    upload_blob_az(data, filename, f"BRONZE/SYD")

    logging.info("sydney scraper complete")

