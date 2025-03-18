#!/bin/bash

# Upgrade pip to the latest version (if necessary)
python3 -m pip install --upgrade pip

# Install dependencies from requirements.txt
pip3 install -r requirements.txt

# Collect static files (if you're using Django's static files)
python3 manage.py collectstatic --noinput

# Run database migrations (if necessary)
python3 manage.py migrate
