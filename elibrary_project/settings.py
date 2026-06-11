"""
Django settings for elibrary_project project.
"""

from pathlib import Path
import os
import dj_database_url


# --------------------
# Paths
# --------------------

BASE_DIR = Path(__file__).resolve().parent.parent


# --------------------
# Security
# --------------------

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "django-insecure-h@pd#e$q(@9jdv+s9d&rk2cpwob@!j3y%_&am3c!s2_(z=x2(#"
)


DEBUG = True


ALLOWED_HOSTS = [
    ".onrender.com",
    "localhost",
    "127.0.0.1",
]


# --------------------
# Apps
# --------------------

INSTALLED_APPS = [

    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "cloudinary_storage",
    "cloudinary",

    "elibrary_app",
]


# --------------------
# Middleware
# --------------------

MIDDLEWARE = [

    "django.middleware.security.SecurityMiddleware",

    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# --------------------
# URLs
# --------------------

ROOT_URLCONF = "elibrary_project.urls"


# --------------------
# Templates
# --------------------

TEMPLATES = [
    {

        "BACKEND": "django.template.backends.django.DjangoTemplates",

        "DIRS": [],

        "APP_DIRS": True,

        "OPTIONS": {

            "context_processors": [

                "django.template.context_processors.request",

                "django.contrib.auth.context_processors.auth",

                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "elibrary_project.wsgi.application"



# --------------------
# Database (Neon PostgreSQL)
# --------------------

DATABASES = {

    "default": dj_database_url.config(

        default="sqlite:///db.sqlite3",

        conn_max_age=600,
    )
}



# --------------------
# Password validation
# --------------------

AUTH_PASSWORD_VALIDATORS = [

    {
        "NAME":
        "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.MinimumLengthValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.CommonPasswordValidator",
    },

    {
        "NAME":
        "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]



# --------------------
# Language
# --------------------

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True



# --------------------
# Static Files
# --------------------

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_DIRS = [

    BASE_DIR / "static",

]

STATICFILES_STORAGE = (
    "django.contrib.staticfiles.storage.StaticFilesStorage"
)



# --------------------
# Media Files
# --------------------

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR / "media"



# --------------------
# Cloudinary
# --------------------

CLOUDINARY_STORAGE = {

    "CLOUD_NAME": os.environ.get(
        "CLOUDINARY_CLOUD_NAME"
    ),

    "API_KEY": os.environ.get(
        "CLOUDINARY_API_KEY"
    ),

    "API_SECRET": os.environ.get(
        "CLOUDINARY_API_SECRET"
    ),
}



# Django 5 storage system

STORAGES = {

    # User uploads → Cloudinary

    "default": {

        "BACKEND":
        "cloudinary_storage.storage.MediaCloudinaryStorage",
    },


    # CSS / JS → normal static storage

    "staticfiles": {

        "BACKEND":
        "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}



# --------------------
# Other
# --------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


LOGIN_URL = "/login/"


APPEND_SLASH = True