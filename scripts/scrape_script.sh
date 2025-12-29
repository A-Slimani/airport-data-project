#!/bin/bash

ENV_PATH='/Users/aboud/programming/airport-data-project/'

source $ENV_PATH/.venv/bin/activate

python $ENV_PATH/scraper/syd_airport.py
python $ENV_PATH/scraper/adl_airport.py
python $ENV_PATH/scraper/per_airport.py
python $ENV_PATH/scraper/bri_airport.py
# python $ENV_PATH/scraper/mel_airport.py