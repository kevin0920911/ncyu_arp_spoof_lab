#!/bin/bash

while true
do
    echo "[Victim] Requesting flag..."

    curl -s http://10.20.0.30:8080/flag

    echo
    echo "-------------------------"

    sleep 5
done