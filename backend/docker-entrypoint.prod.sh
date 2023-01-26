#!/bin/sh
#exec python manage.py check --deploy
export DJANGO_SETTINGS_MODULE="backend.settings.production"
exec gunicorn backend.wsgi:application --bind 0.0.0.0:7999