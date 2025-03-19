

pip install -r requirements.txt

# Collect static files (if you're using Django's static files)
python3 manage.py collectstatic --noinput

# Run database migrations (if necessary)
python3 manage.py migrate
