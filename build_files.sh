echo "BUILD STARTED"
# Install required packages
apt-get update
apt-get install -y python3 python3-pip python3-dev python3-venv

pip3 install -r requirements.txt

# Collect static files (if you're using Django's static files)
python3 manage.py collectstatic --noinput

# Run database migrations (if necessary)
python3 manage.py migrate
echo "BUILD COMPLETED"