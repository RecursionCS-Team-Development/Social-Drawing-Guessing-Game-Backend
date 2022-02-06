from pathlib import Path
import os
import environ

import django_heroku

from datetime import timedelta
from django.utils.translation import ugettext_lazy as _


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

# 環境変数の読み込み
env = environ.Env(DEBUG=(bool,False))

# 開発環境と本番環境での設定ファイルの分岐
IS_ON_HEROKU = env.bool('ON_HEROKU', default=False)

if not IS_ON_HEROKU:
    env.read_env(os.path.join(BASE_DIR,'.env'))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.get_value('DEBUG', cast = bool, default = True)

if DEBUG:
    ALLOWED_HOSTS = ['http://localhost:8080/']
else:
    ALLOWED_HOSTS = ['social-drawing-guessing.herokuapp.com', 'yourdomain.com', 'kind-ardinghelli-bdabe2.netlify.app']


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
    'drawing',
    'chat',
    'channels'
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
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

# CORS
# CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:8080',
    'http://127.0.0.1:8080',
    'https://social-drawing-guessing.netlify.app',
    'https://kind-ardinghelli-bdabe2.netlify.app'
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'access-control-allow-origin',
)

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
ASGI_APPLICATION = 'app.asgi.application'

if DEBUG:
    CHANNEL_LAYERS = {
        'default': {
            'BACKEND': 'channels.layers.InMemoryChannelLayer',
        },
    }
else:
    CHANNEL_LAYERS = {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': ('127.0.0.1', 'redis://localhost:6379'),
        },
    }

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


# EMAIL
# ローカル確認用
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 本番環境用
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hicos69899@reamtv.com'
# EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True


# Djoser
DJOSER = {
    'LOGIN_FIELD': 'email', # メールアドレスでログイン
    # 'SEND_ACTIVATION_EMAIL': True, # アカウント本登録メール
    # 'SEND_CONFIRMATION_EMAIL': True, # アカウント本登録完了メール
    'USERNAME_CHANGED_EMAIL_CONFIRMATION': True, # メールアドレス変更完了メール
    'PASSWORD_CHANGED_EMAIL_CONFIRMATION': True, # パスワード変更完了メール
    'USER_CREATE_PASSWORD_RETYPE': True, # 新規登録時に確認用パスワード必須
    'SET_USERNAME_RETYPE': True, # メールアドレス変更時に確認用メールアドレス必須
    'SET_PASSWORD_RETYPE': True, # パスワード変更時に確認用パスワード必須
    'ACTIVATION_URL': 'activate/{uid}/{token}', # アカウント本登録用URL
    'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}', # メールアドレスリセット完了用URL
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}', # パスワードリセット完了用URL
    'SERIALIZER': {
        # カスタムユーザー用のserializer
        'user_create': 'accounts.serializers.UserSerializer',
        'user': 'accounts.serializers.UserSerializer',
        'current_user': 'accounts.serializers.UserSerializer',
    },
    # 'EMAIL': {},
}


# JWT認証setting
SIMPLE_JWT = {
    # トークンタイプをJWTに設定
    'AUTH_HEADER_TYPES':('JWT', ),
    # 認証トークン
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken', ),
    # アクセストークンの持続時間の設定
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    # リフレッシュトークンの持続時間
    'REFRESH_TOKEN_LIFETIME': timedelta(days=3),
}

# Rest framework setting
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
}



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
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'

MEDIA_ROOT = 'media/'

# Custom User model
AUTH_USER_MODEL = 'accounts.User'

# heroku
django_heroku.settings(locals())
