"""
Django settings for ioee project.
Generated by 'django-admin startproject' using Django 3.1.7.
For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# loading environment variables
# if os.path.exists('.env'):
from dotenv import load_dotenv
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'ioestudents.herokuapp.com', 'ioee.herokuapp.com']


# Application definition
 
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'api.apps.ApiConfig',
    # 'person.apps.PersonConfig',
    'person',
    'code_share.apps.CodeShareConfig',
    'ioe_overflow.apps.IoeOverflowConfig',
    'pdf_engine.apps.PdfEngineConfig',
    'nepali_datetime_field',
    'django.contrib.humanize',
]
#'fontawesome-free',

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#For Static files
]

ROOT_URLCONF = 'ioee.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        ## To include templates folder for default templates
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ioee.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'ioee': {    # ioee <default> # heroku is ignoring dbroutes so renaming fuse_attend to default
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'utmhgxol',
        'USER': 'utmhgxol',
        'PASSWORD': os.environ.get('IOEE_DB_PASSWORD'),
        'HOST': 'tiny.db.elephantsql.com',
        'PORT': '5432',
    },

    'hotornot': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'uegbcxiy',
        'USER': 'uegbcxiy',
        'PASSWORD': os.environ.get('HOT_OR_NOT_DB_PASSWORD'),
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vysbznab',
        'USER': 'vysbznab',
        'PASSWORD': os.environ.get('FUSE_ATTEND_DB_PASSWORD'),
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'brainmap': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ltifidts',
        'USER': 'ltifidts',
        'PASSWORD': os.environ.get('BRAINMAP_DB_PASSWORD'),
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
    },
    'previous_default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'lflpirvq',
        'USER': 'lflpirvq',
        'PASSWORD': os.environ.get('DEFAULT_DB_PASSWORD'),
        'HOST': 'john.db.elephantsql.com',
        'PORT': '5432',
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
UPLOADS_DIR = os.path.join(BASE_DIR, 'uploads')

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = EMAIL_HOST_USER = os.environ.get('gmail')
EMAIL_HOST_PASSWORD = os.environ.get('gmail_password')


# Login & Logout URLs
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/login/' 
