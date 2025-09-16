#!/bin/bash
MIN=$1
while true; do
    python3 app.py "$MIN" --cache="cache/*"
    sleep 5
done
