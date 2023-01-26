#!/bin/sh
python manage.py migrate --no-input
exec gunicorn backend.wsgi:application --bind 0.0.0.0:7999 --workers 3