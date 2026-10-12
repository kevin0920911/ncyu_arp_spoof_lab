#!/bin/bash

while true
do
    echo "[Victim] Requesting flag..."

    curl -i  -H 'Lab-Token: original' http://10.30.0.30:8080/flag

    echo
    echo "-------------------------"

    sleep 5
done