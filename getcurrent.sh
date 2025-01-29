#!/bin/bash
cd /var/www-fastapi
counter=0

while true 
do
date > ./log/current_lastrun
echo $counter >>./log/current_lastrun
source ./venv/bin/activate
python3 ./getcurrent.py
r=$((counter % 48))
if [[ $r == 0 ]]
then
    date > ./log/forecast_lastrun
    python3 ./getforecast.py
fi
sleep 300
counter=$((counter + 1))
done
