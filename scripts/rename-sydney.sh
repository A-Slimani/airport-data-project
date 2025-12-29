#!/bin/bash

PATH = '/Users/aboud/programming/airport-data-project/data'

for file in $PATH/*.json; do
    if [[ $file != sydney-* ]]; then 
        mv "$file" "sydney-$file"
    fi
done
