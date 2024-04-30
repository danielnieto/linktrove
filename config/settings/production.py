# ruff: noqa: F403, F405
from .base import *
import os

DEBUG = False
ALLOWED_HOSTS = ["linktrove.nieto.dev"]
CSRF_TRUSTED_ORIGINS = ["https://linktrove.nieto.dev"]
SECRET_KEY = os.environ.get("SECRET_KEY")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = "no-reply@nieto.dev"
