from dbt.cli.main import dbtRunner
import azure.functions as func
import subprocess
import datetime
import logging
import json
import sys
import os

app = func.FunctionApp()


@app.function_name("SeedDBTRunner")
@app.route(route="seed-dbt", methods=['GET'])
def run_dbt_seed(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # logging.info(f"Loaded modules: {[m for m in sys.modules if 'protobuf' in m]}")
        # logging.info(f"Protobuf Version: {google.protobuf.__version__}")
        import google.protobuf
        logging.info(f"Protobuf Version: {google.protobuf.__version__}")
        logging.info("Starting DBT Seed")
        dbt = dbtRunner()
        res = dbt.invoke([
            "test",
            "--project-dir", "./airportdbt",
            "--profiles-dir", "./airportdbt",
            "--target", "default"
        ])
        logging.info("DBT seed ran successfully")
        logging.info(res)
        logging.info(f"Loaded modules: {[m for m in sys.modules if 'protobuf' in m]}")
        logging.info(f"Protobuf Version: {google.protobuf.__version__}")
        return func.HttpResponse(
            json.dumps({"status":"SUCCESS"}),
            status_code=200,
            mimetype="application/json"
        )
    except Exception as e:
        logging.error("Sydney DBT failed")
        return func.HttpResponse(
            json.dumps({"status": "FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )


@app.function_name("SydneyDBTRunner")
@app.route(route="sydney-dbt", methods=['GET'])
def run_dbt_seed(req: func.HttpRequest) -> func.HttpResponse:
    try:
        logging.info("Starting Sydney DBT")
        dbt = dbtRunner()
        res = dbt.invoke([
            "run",
            "--project-dir", "./airportdbt",
            "--profiles-dir", "./airportdbt"
        ])
        logging.info(res)
        if res.success:
            logging.info("Sydney DBT ran successfully")
            return func.HttpResponse(
                json.dumps({"status": "SUCCESS"}),
                status_code=200,
                mimetype="application/json"
            )
        else:
            logging.error("Sydney DBT failed")
            return func.HttpResponse(
                json.dumps({"status": "FAILED", "error": "to add"}),
                status_code=500,
                mimetype="application/json"
            )

    except Exception as e:
        logging.error("Sydney DBT failed")
        return func.HttpResponse(
            json.dumps({"status": "FAILED", "error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
