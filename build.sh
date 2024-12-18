#!/usr/bin/env bash
# exit on error
set -o errexit

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Collecting static files..."
python manage.py collectstatic --no-input

echo "Running migrations..."
# Créer les migrations si elles n'existent pas
python manage.py makemigrations user
python manage.py makemigrations posts

# Réinitialiser la base de données
echo "Resetting database..."
python manage.py sqlflush | python manage.py dbshell

# Appliquer les migrations dans l'ordre
echo "Applying migrations..."
python manage.py migrate auth
python manage.py migrate contenttypes
python manage.py migrate admin
python manage.py migrate sessions
python manage.py migrate user
python manage.py migrate posts

# Crée un superuser pour l'administration
echo "Creating superuser..."
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin@example.com', 'adminpassword123', nom='Admin', prenom='Super', dateDeNaissance='2000-01-01') if not User.objects.filter(email='admin@example.com').exists() else None" | python manage.py shell

chmod a+x build.sh