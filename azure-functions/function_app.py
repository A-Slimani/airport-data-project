from scraper.syd_airport import get_data as get_data_syd
from scraper.melb_airport import get_data as get_data_mel
from scraper.bri_airport import get_data as get_data_bri
from scraper.config import (
    DATE_TODAY,
    DATE_YESTERDAY,
    TIMESTAMP_YESTERDAY_START,
    TIMESTAMP_YESTERDAY_END
)
from scraper.utils import upload_blob_az
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=True)
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


@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=True)
def mel_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Melbourne scraper")

    filename = f"melbourne-{DATE_YESTERDAY}.json"
    data = get_data_mel(TIMESTAMP_YESTERDAY_START, TIMESTAMP_YESTERDAY_END)
    upload_blob_az(data, filename, f"BRONZE/MEL")

    logging.info("Melbourne scraper complete")


@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=True)
def bri_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Brisbane scraper")

    filename = f"brisbane-{DATE_YESTERDAY}.json"
    data = get_data_bri()
    upload_blob_az(data, filename, f"BRONZE/BRI")

    logging.info("Brisbane scraper complete")


@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=True)
def adl_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Adelaide scraper")

    filename = f"adelaide-{DATE_YESTERDAY}.json"
    data = get_data_bri()
    upload_blob_az(data, filename, f"BRONZE/ADL")

    logging.info("Adelaide scraper complete")


@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=True)
def per_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Perth scraper")

    filename = f"perth-{DATE_TODAY}.json"
    data = get_data_per()
    upload_blob_az(data, filename, f"BRONZE/PER")

    logging.info("Perth scraper complete")
