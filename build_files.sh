#!/bin/bash

# Install Python and pip (if necessary)
apt-get update
apt-get install -y python3 python3-pip

# Ensure pip is up-to-date
python3 -m pip install --upgrade pip

# Install project dependencies
pip3 install -r requirements.txt

# Any other build steps you need, such as collecting static files or running migrations
python3 manage.py collectstatic --noinput
python3 manage.py migrate