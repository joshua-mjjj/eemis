import os
import dj_database_url
from datetime import timedelta
import django_heroku
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-v+b4&uas+3%tf$jkqltkk9)v^596(vnb^^pqkgkw8v6q#v6+p*'
unique_token = '@regulars_encode_data$IAMTHEREFOREIAM'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = os.getenv("DEBUG")

ADMINS = [
    ("Joshua Mwesigwa", "shredakajoshua@gmail.com"),
]


ALLOWED_HOSTS = ["*"]
# ALLOWED_HOSTS = ["*"]

#
# Usually whitelisted when going for deployment
CORS_ORIGIN_WHITELIST = (
    "http://localhost:3000",
    "http://localhost:3001",
)

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Added
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "storages",
    "rest_framework",
    "rest_framework.authtoken",
    # "rest_auth",
    # "allauth",
    # "allauth.account",
    "rest_auth.registration",
    # "allauth.socialaccount",
    # "allauth.socialaccount.providers.facebook",
    # "allauth.socialaccount.providers.google",
    "drf_yasg",
    "corsheaders",
    "django_extensions",
    # "notifications",
    "oauth2_provider",
    # "social_django",
    # "rest_framework_social_oauth2",
    "import_export",
    "django_filters",
    "dbbackup",
    "api",
]

AUTHENTICATION_BACKENDS = [
    "rest_framework_social_oauth2.backends.DjangoOAuth2",
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_USER_MODEL = "api.User"


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # Added
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eemis.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
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

WSGI_APPLICATION = 'eemis.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Kampala'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Django REST Framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "api.authentication.CSRFExemptSessionAuthentication",
        "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        "oauth2_provider.contrib.rest_framework.OAuth2Authentication",
        "rest_framework_social_oauth2.authentication.SocialAuthentication",
    ),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
}

SITE_ID = 1
REST_USE_JWT = True
ACCOUNT_EMAIL_VERIFICATION = "none"

IMPORT_EXPORT_USE_TRANSACTIONS = True


JWT_AUTH = {"JWT_EXPIRATION_DELTA": timedelta(hours=12)}
LOGIN_URL = "/api/auth/login/"
LOGOUT_URL = "/api/auth/logout/"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"



EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# CELERY
BROKER_URL ='redis://localhost:6379'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='fast.sports.fusion.system@gmail.com'
EMAIL_HOST_PASSWORD='jjscsyuhecncrbks'
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='fast.sports.fusion.system@gmail.com'

DOMAIN='localhost:8000'
CELERY_BROKER='redis://localhost:6379'
CELERY_BACKEND='redis://localhost:6379'
CELERY_TIMEZONE='Africa/Kampala'
CELERY_BROKER_URL='redis://localhost:6379'
CELERY_RESULT_BACKEND='redis://localhost:6379'
REDIS_URL='redis://localhost:6379'

TWILIO_SENDER_NUMBER=+17622453734


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
django_heroku.settings(locals())