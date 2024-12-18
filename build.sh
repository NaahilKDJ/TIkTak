#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt
pip freeze > requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."


python manage.py migrate user zero --noinput
python manage.py migrate posts zero --noinput
python manage.py migrate --noinput

# Crée un superuser pour l'administration
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@example.com', 'adminpassword123', nom='Admin', prenom='Super', dateDeNaissance='2000-01-01') if not User.objects.filter(email='admin@example.com').exists() else None" | python manage.py shell

chmod a+x build.sh