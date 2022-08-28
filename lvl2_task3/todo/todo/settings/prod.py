from distutils.debug import DEBUG
import django_on_heroku
from decouple import config
from .dev import SECRET_KEY


from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'klaus-todo-test.herokuapp.com',
]


django_on_heroku.settings(locals(), STATICFILES_DIRS=False)
del DATABASES['default']['OPTIONS']['sslmode']