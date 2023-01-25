from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: change key before production! 
# manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
SECRET_KEY = "django-insecure-80%4ua9yonp7*z%2-e)ey_wunwczk9cpvgp9&77uq!b2_g!l=5"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
