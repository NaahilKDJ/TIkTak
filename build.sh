#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Apply specific app migrations if needed
python manage.py makemigrations user
python manage.py makemigrations posts
python manage.py migrate user
python manage.py migrate posts

chmod +x build.sh