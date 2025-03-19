

pip install -r requirements.txt

# Collect static files (if you're using Django's static files)
python manage.py collectstatic --noinput

# Run database migrations (if necessary)
python manage.py migrate
