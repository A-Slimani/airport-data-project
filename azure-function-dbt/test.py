from dbt.cli.main import dbtRunner
import google.protobuf
import subprocess
import datetime
import logging
import json
import sys
import os


def run_dbt_seed():
    try:
        print(f"Loaded modules: {[m for m in sys.modules if 'protobuf' in m]}")
        print(f"Protobuf Version: {google.protobuf.__version__}")
        print(os.getcwd())
        print("Starting DBT Seed")
        dbt = dbtRunner()
        res = dbt.invoke([
            "seed",
            "--project-dir", "./airportdbt",
            "--profiles-dir", "./airportdbt",
            "--target", "default"
        ])
        print("DBT seed ran successfully")
        print(res)
        print(f"Loaded modules: {[m for m in sys.modules if 'protobuf' in m]}")
        print(f"Protobuf Version: {google.protobuf.__version__}")
    except Exception as e:
        print("Sydney DBT seed failed")


run_dbt_seed()
