from scraper.syd_airport import get_data as get_data_syd
from scraper.config import DATE_YESTERDAY
from scraper.utils import upload_blob_az
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 * * * * *", arg_name="my_timer", run_on_startup=True)
def syd_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Sydney scraper")

    directions = ["departure", "arrival"]
    terminals = ["international", "domestic"]

    for d in directions:
        for t in terminals:
            filename = f"sydney-{DATE_YESTERDAY}-{d}-{t}.json"
            data = get_data_syd(d, t, DATE_YESTERDAY)
            upload_blob_az(data, filename, f"BRONZE/SYD")

    logging.info("Sydney scraper complete")


@app.timer_trigger(schedule="0 * * * * *", arg_name="timer", run_on_startup=True)
def timer_trigger_example(timer: func.TimerRequest) -> None:
    logging.info("Starting Melbourne scraper")

    filename = f"sydney-{DATE_YESTERDAY}-{direction}-{terminal}.json"
    data = get_data_syd(direction, terminal, DATE_YESTERDAY)
    upload_blob_az(data, filename, f"BRONZE/SYD")

    logging.info("Melbourne scraper complete")
