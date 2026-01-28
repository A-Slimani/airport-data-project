from scraper.syd_airport import get_data as get_data_syd
from scraper.adl_airport import get_data as get_data_adl
from scraper.bri_airport import get_data as get_data_bri
from scraper.mel_airport import get_data as get_data_mel
from scraper.per_airport import get_data as get_data_per
from scraper.config import (
    DATE_YESTERDAY,
    TIMESTAMP_YESTERDAY_START,
    TIMESTAMP_YESTERDAY_END
)
from scraper.utils import upload_blob_az
import azure.functions as func
import logging


app = func.FunctionApp()


@app.function_name("SydneyAirportScraper")
@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=False)
def syd_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Sydney scraper")

    directions = ["departure", "arrival"]
    terminals = ["international", "domestic"]

    for d in directions:
        for t in terminals:
            filename = f"sydney-{DATE_YESTERDAY}-{d}-{t}.json"
            data = get_data_syd(d, t, DATE_YESTERDAY)
            upload_blob_az(data, filename, f"RAW/SYD")

    logging.info("Sydney scraper complete")


@app.function_name("AdelaideAirportScraper")
@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=False)
def adl_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Adelaide..scraper")

    filename = f"adelaide-{DATE_YESTERDAY}.json"
    data = get_data_adl()
    upload_blob_az(data, filename, f"RAW/ADL")

    logging.info("Adelaide scraper complete")


@app.function_name("BrisbaneAirportScraper")
@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=False)
def bri_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Brisbane scraper")

    filename = f"brisbane-{DATE_YESTERDAY}.json"
    data = get_data_bri()
    upload_blob_az(data, filename, f"RAW/BRI")

    logging.info("Brisbane scraper complete")


@app.function_name("MelbourneAirportScraper")
@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=False)
def mel_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Melbourne..scraper")

    filename = f"melbourne-{DATE_YESTERDAY}.json"
    data = get_data_mel(TIMESTAMP_YESTERDAY_START, TIMESTAMP_YESTERDAY_END)
    upload_blob_az(data, filename, f"RAW/MEL")

    logging.info("Melbourne scraper complete")


@app.function_name("PerthAirportScraper")
@app.timer_trigger(schedule="0 0 1 * * *", arg_name="timer", run_on_startup=False)
def per_airport_scraper(timer: func.TimerRequest) -> None:
    logging.info("Starting Perth scraper")

    filename = f"perth-{DATE_TODAY}.json"
    data = get_data_per()
    upload_blob_az(data, filename, f"RAW/PER")

    logging.info("Perth scraper complete")

