# -*- coding: utf-8 -*-

# Application definition

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_ROOT = os.path.dirname(BASE_DIR)


INSTALLED_APPS = (
    # Django Default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django 3rd Party Modules ( installed via pip )
    'social.apps.django_app.default',
    'storages',
    'imagekit',
    'rest_framework',
    'django_summernote',

    # Yebimom Apps
    'users',
    'centers',
    'events',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    # Django Default
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",

    # Python Social Auth Custom TEMPLATE_CONTEXT_PROCESSORS
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

ROOT_URLCONF = 'yebimom.urls'

WSGI_APPLICATION = 'yebimom.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

HASHIDS_USER_PROFILE_SALT = os.environ['HASHIDS_USER_PROFILE_SALT']
HASHIDS_CENTER_SALT = os.environ['HASHIDS_CENTER_SALT']


EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = os.environ['MAILGUN_ACCESS_KEY']
MAILGUN_SERVER_NAME = os.environ['MAILGUN_SERVER_NAME']


API_STORE_KEY = os.environ['API_STORE_KEY']
API_STORE_BASE_URL = os.environ['API_STORE_BASE_URL']

SMS_SEND_PHONE = os.environ['SMS_SEND_PHONE']
SMS_SEND_NAME = os.environ['SMS_SEND_NAME']
SMS_SUBJECT = os.environ['SMS_SUBJECT']
