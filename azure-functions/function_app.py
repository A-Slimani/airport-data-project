from scraper.syd_airport import get_data as get_data_syd
from scraper.adl_airport import get_data as get_data_adl
from scraper.bri_airport import get_data as get_data_bri
from scraper.mel_airport import get_data as get_data_mel
from scraper.per_airport import get_data as get_data_per
from scraper.config import (
    DATE_YESTERDAY,
    DATE_TODAY,
    TIMESTAMP_YESTERDAY_START,
    TIMESTAMP_YESTERDAY_END
)
from scraper.utils import upload_blob_az
import azure.functions as func
import logging
import json


app = func.FunctionApp()


@app.function_name("SydneyAirportScraper")
@app.route(route="sydney-scraper", methods=['GET'])
def syd_airport_scraper(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Starting Sydney scraper")

        directions = ["departure", "arrival"]
        terminals = ["international", "domestic"]

        for d in directions:
            for t in terminals:
                filename = f"sydney-{DATE_YESTERDAY}-{d}-{t}.json"
                data = get_data_syd(d, t, DATE_YESTERDAY)
                upload_blob_az(data, filename, f"RAW/SYD")

        logging.info("Sydney scraper completed successfully")

        return func.HttpResponse(
            json.dumps({"status":"SUCCESS"}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.info("Sydney scraper failed")
        return func.HttpResponse(
            json.dumps({"status":"FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


@app.function_name("AdelaideAirportScraper")
@app.route(route="adelaide-scraper", methods=['GET'])
def adl_airport_scraper(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Starting Adelaide scraper")

        filename = f"adelaide-{DATE_YESTERDAY}.json"
        data = get_data_adl()
        upload_blob_az(data, filename, f"RAW/ADL")

        logging.info("Adelaide scraper complete")

        return func.HttpResponse(
            json.dumps({"status":"SUCCESS"}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.info("Adelaide scraper failed")
        return func.HttpResponse(
            json.dumps({"status":"FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )



@app.function_name("BrisbaneAirportScraper")
@app.route(route="brisbane-scraper", methods=['GET'])
def bri_airport_scraper(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Starting Brisbane scraper")

        filename = f"brisbane-{DATE_YESTERDAY}.json"
        data = get_data_bri()
        upload_blob_az(data, filename, f"RAW/BRI")

        logging.info("Brisbane scraper complete")

        return func.HttpResponse(
            json.dumps({"status":"SUCCESS"}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.info("Brisbane scraper failed")
        return func.HttpResponse(
            json.dumps({"status":"FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


@app.function_name("MelbourneAirportScraper")
@app.route(route="melbourne-scraper", methods=['GET'])
def mel_airport_scraper(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Starting Melbourne scraper")

        filename = f"melbourne-{DATE_YESTERDAY}.json"
        data = get_data_mel(TIMESTAMP_YESTERDAY_START, TIMESTAMP_YESTERDAY_END)
        upload_blob_az(data, filename, f"RAW/MEL")

        logging.info("Melbourne scraper complete")

        return func.HttpResponse(
            json.dumps({"status":"SUCCESS"}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.info("Melbourne scraper failed")
        return func.HttpResponse(
            json.dumps({"status":"FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


@app.function_name("PerthAirportScraper")
@app.route(route="perth-scraper", methods=['GET'])
def per_airport_scraper(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Starting Perth scraper")

        filename = f"perth-{DATE_TODAY}.json"
        data = get_data_per()
        upload_blob_az(data, filename, f"RAW/PER")

        logging.info("Perth scraper complete")
        
        return func.HttpResponse(
            json.dumps({"status":"SUCCESS"}),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.info("Perth scraper failed")
        return func.HttpResponse(
            json.dumps({"status":"FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )

