from os import getenv
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = getenv("SECRET_KEY")


TOKEN_BOT = getenv("TELEGRAM_BOT_TOKEN")
GET_FILE_URL = f"https://api.telegram.org/file/bot{TOKEN_BOT}/"

DEBUG = getenv('DEBUG', False)

ALLOWED_HOSTS = []

CRYPTHO_CONVERT = {
    "btc": "https://kursolog.com/btc/kzt/12",
    "eth": "https://kursolog.com/eth/kzt/12",
    "xrp": "https://kursolog.com/xrp/kzt/12",
    "doge": "https://kursolog.com/doge/kzt/12",
    "ltc": "https://kursolog.com/ltc/kzt/12",
}

CONVERT = {
    "euro": "https://kursolog.com/eur/kzt/",
    "usd": "https://kursolog.com/usd/kzt/",
    "rub": "https://kursolog.com/rub/kzt/",
    "kgs": "https://kursolog.com/kgs/kzt/",
    "gbp": "https://kursolog.com/gbp/kzt/",
    "aud": "https://kursolog.com/aud/kzt/",
    "cad": "https://kursolog.com/cad/kzt/",
    "chf": "https://kursolog.com/chf/kzt/",
    "cny": "https://kursolog.com/cny/kzt/",
    "czk": "https://kursolog.com/czk/kzt/",
    "dkk": "https://kursolog.com/dkk/kzt/",
    "hkd": "https://kursolog.com/hkd/kzt/",
    "huf": "https://kursolog.com/huf/kzt/",
    "idr": "https://kursolog.com/idr/kzt/",
    "ils": "https://kursolog.com/ils/kzt/",
    "inr": "https://kursolog.com/inr/kzt/",
    "jpy": "https://kursolog.com/jpy/kzt/",
    "krw": "https://kursolog.com/krw/kzt/",
    "mxn": "https://kursolog.com/mxn/kzt/",
    "myr": "https://kursolog.com/myr/kzt/",
    "nok": "https://kursolog.com/nok/kzt/",
    "nzd": "https://kursolog.com/nzd/kzt/",
    "php": "https://kursolog.com/php/kzt/",
    "pln": "https://kursolog.com/pln/kzt/",
    "ron": "https://kursolog.com/ron/kzt/",
    "sek": "https://kursolog.com/sek/kzt/",
    "sgd": "https://kursolog.com/sgd/kzt/",
    "thb": "https://kursolog.com/thb/kzt/",
    "try": "https://kursolog.com/try/kzt/",
    "twd": "https://kursolog.com/twd/kzt/",
    "uah": "https://kursolog.com/uah/kzt/",
    "zar": "https://kursolog.com/zar/kzt/"
}

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TGDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'TGDjango.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': getenv('DB_NAME'),
#         'USER': getenv('DB_USER'),
#         'PASSWORD': getenv('DB_PASSWORD'),
#         'HOST': getenv('DB_HOST'),
#         'PORT': getenv('DB_PORT'),
#     }
# }

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

LANGUAGE_CODE = getenv("LANGUAGE_CODE")

TIME_ZONE = getenv("TIME_ZONE")
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
