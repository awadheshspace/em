#!/bin/bash

# Update package lists and install Python 3 and pip3
apt-get update
apt-get install -y python3 python3-pip

# Ensure pip3 is up-to-date
python3 -m pip install --upgrade pip

# Install the dependencies from requirements.txt
pip3 install -r requirements.txt

# Collect static files and run migrations (if necessary)
python3 manage.py collectstatic --noinput
python3 manage.py migrate
