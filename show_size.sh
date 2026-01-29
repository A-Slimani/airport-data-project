#!/bin/bash

az storage fs file list \
  --account-name airportdataproject \
  --file-system airport-data \
  --path "RAW/SYD" \
  --recursive \
  --auth-mode login \
  --query "[].contentLength" \
  -o tsv | awk '{s+=$1} END {print s/1024/1024 " MB"}'
