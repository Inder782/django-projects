#!/bin/bash

BACKEND_DIR="/home/inder782/programs/django-projects/auth/auth"
FRONTEND_DIR="/home/inder782/programs/django-projects/auth/auth"

gnome-terminal --bash -c "cd  $BACKEND_DIR python manage.py runserver"

gnome-terminal --bash -c "cd $FRONTEND_DIR npm run dev"

echo "Backend and Frontend started in separate terminals!"