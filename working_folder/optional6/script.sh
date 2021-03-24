#! /bin/bash

echo "Hello :) I am a very simple script to test the crontab with docker (optional6)"
echo "$(date): executed script" >> cron.log 2>&1

cd ..

python readApi.py
python saveData.py

cd app

python api.py

cd ../optional6