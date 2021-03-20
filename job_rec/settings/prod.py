from .base import *
import os

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1","localhost",'jobitmatch.herokuapp.com','jobitmatch.com']

