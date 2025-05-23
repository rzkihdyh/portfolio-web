#!/bin/bash

# Build the project
echo "Building the project..."
python3.13 -m pip install -r requirements.txt

echo "Make Migration..."
python3.13 manage.py makemigrations --noinput
python3.13 manage.py migrate --noinput

echo "Collect Static..."
python3.13 manage.py collectstatic --noinput --clear

# install dependencies
pip install -r requirements.txt

# collect static files
python3 manage.py collectstatic --noinput

# copy hasil collectstatic ke staticfiles_build
mkdir -p staticfiles_build
cp -r staticfiles/* staticfiles_build/