from .base import *
import os
from dotenv import load_dotenv, dotenv_values

# settings are in .env file. Rename sample.env to .env
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(PROJECT_DIR,".env"))

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS =  os.environ.get("ALLOWED_HOSTS").split(",")
SECURE_SSL_REDIRECT = (os.environ.get("SECURE_SSL_REDIRECT") == 'true')
SESSION_COOKIE_SECURE =(os.environ.get("SESSION_COOKIE_SECURE") == 'true')
CSRF_COOKIE_SECURE = (os.environ.get("CSRF_COOKIE_SECURE") == 'true')
SECURE_HSTS_PRELOAD = (os.environ.get("SECURE_HSTS_PRELOAD") == 'true')
SECURE_HSTS_SECONDS = os.environ.get("SECURE_HSTS_SECONDS")
SECURE_HSTS_INCLUDE_SUBDOMAINS = (os.environ.get("SECURE_HSTS_INCLUDE_SUBDOMAINS") == 'true')
DEBUG = False

try:
    from .local import *
except ImportError:
    pass
