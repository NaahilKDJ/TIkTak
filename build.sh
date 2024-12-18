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

# Create a superuser if needed (optional)
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@example.com', 'adminpassword123') if not User.objects.filter(email='admin@example.com').exists() else None" | python manage.py shell

chmod +x build.sh