#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanding database migrations
echo "Création des migrations"
python manage.py makemigrations

echo "Migration vers la base de donnée"
python manage.py migrate


echo "Lancement du serveur"
python manage.py runserver