from pathlib import Path
import os
import environ


from datetime import timedelta
from django.utils.translation import ugettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# 環境変数の読み込み
env = environ.Env(DEBUG=(bool,False))

# 開発環境と本番環境での設定ファイルの分岐
# 一旦開発環境のみ
env.read_env(os.path.join(BASE_DIR,'.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get_value('DEBUG', cast = bool, default = True)

if DEBUG:
    ALLOWED_HOSTS = ['*']
else:
    ALLOWED_HOSTS = ['social-drawing-guessing-game.com', 'yourdomain.com']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'djoser',
    'corsheaders',
    'accounts',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'app.wsgi.application'


# Data base接続
SQLITE = env.get_value('SQLITE', cast = bool, default = True)

if SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME_SQL'),
        'USER': env('DB_USER_SQL'),
        'PASSWORD': env('DB_PASSWORD_SQL'),
        'HOST': env('DB_HOST_SQL'),
        'PORT': 3306 if DEBUG else env('DB_PORT_SQL'),
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

# Core URL settings
# ログイン機能がある場合はコメントアウトを外す
# LOGIN_REDIRECT_URL = 'account:index' #ログイン後のダッシュボード
# LOGIN_URL = 'account:login'
# LOGOUT_REDIRECT_URL = 'account:login'


# JWT認証setting
SIMPLE_JWT = {
    #トークンをJWTに設定
    'AUTH_HEADER_TYPES':('JWT'),
    #トークンの持続時間の設定
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60)
}

# Rest framework setting
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}

# CORS
CORS_ALLOW_ALL_ORIGINS = True
#CORS_ALLOWED_ORIGINS = [
#    'http://localhost:3000',
#]



# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ja'

# 英語対応の場合は 下記コメントアウトを外す
LANGUAGES = [
    ('ja', _('日本語')),
    # ('en', _('English')),
]

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media/'

# Custom User model
AUTH_USER_MODEL = 'accounts.User'