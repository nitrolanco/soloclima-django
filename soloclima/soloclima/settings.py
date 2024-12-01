import os
from pathlib import Path
from pymongo import MongoClient

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key (replace with your own secret key)
SECRET_KEY = "your-secret-key-here"

# Debug mode
DEBUG = True

# Allowed hosts
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Installed apps - remove default database-related apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "products",  # Your custom app
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Root URL configuration
ROOT_URLCONF = "soloclima.urls"

# Templates configuration
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application
WSGI_APPLICATION = "soloclima.wsgi.application"

# Database configuration for MongoDB
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.dummy",  # Dummy backend since we're not using Django ORM
    }
}

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017/"
MONGO_DBNAME = "soloclima"

# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files configuration
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "products/static")]

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
