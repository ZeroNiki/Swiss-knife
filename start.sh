#!/bin/bash

source venv/bin/activate
cd app/

while true; do
    timeout 60 python3 manage.py runserver
done &


