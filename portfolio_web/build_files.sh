#!/bin/bash

echo "📦 Installing dependencies..."
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

echo "🛠️ Running database migrations..."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput

echo "🎨 Collecting static files..."
python3.9 manage.py collectstatic --noinput --clear

echo "✅ Build completed successfully!"
echo "Static files location: staticfiles_build/"
ls -la staticfiles_build/