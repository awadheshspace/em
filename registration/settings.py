
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-xkcnnjl93la&ys!)9(++5(yrokasoehj(mx@9ahf$4d8c3+zb5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.vercel.app','*','.now.sh']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'whitenoise.runserver_nostatic',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'ebooks',
    'exammantra',
    'practiceset',
    'examresult',
    'contact',
    'dashboard',
    'courses',
    'payments',
    # 'feemanagement',
    # 'exammantra.apps.ExammantraConfig',
    ]


CSRF_COOKIE_SECURE = False
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
AUTH_USER_MODEL = 'practiceset.CustomUser'
LOGIN_URL = 'dashboard:dashboard_login'    #add 20/feb
# LOGIN_URL = '/accounts/login/'
# LOGIN_REDIRECT_URL = '/courses/'
# LOGIN_REDIRECT_URL = 'examresult:test_list'


PDFKIT_CONFIG = {
    'wkhtmltopdf': '/usr/bin/wkhtmltopdf'  # Direct path for Ubuntu
}
# LOGIN_URL = '/accounts/login/'    #login add 08/02
X_FRAME_OPTIONS = 'ALLOWALL'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # add this line

]

ROOT_URLCONF = 'registration.urls'

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

WSGI_APPLICATION = 'registration.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'railway',
        'USER': 'postgres',
        'PASSWORD': 'GNpNdGADLmPGnBipWVgWguXKxiUqgMZb',
        'HOST': 'interchange.proxy.rlwy.net',
        'PORT': '54995',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # Your project-level static directory
]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build','static')  # This will be used in production


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
RAZORPAY_KEY_ID= 'rzp_test_H9I9sskuRUJluO'
RAZORPAY_KEY_SECRET='eYYlVCGV5jLuUKkodtA8EmvA'
