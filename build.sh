#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
# Créer les migrations si elles n'existent pas
python manage.py makemigrations


# Appliquer les migrations dans l'ordre
echo "Applying migrations..."
python manage.py migrate

python manage.py runserver
chmod a+x build.sh