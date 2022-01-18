"""
Django settings for blog_project project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c31z0t+ky@s#$f^d!bsbal($2k-^5x##o+666a3h_r03tx_j97'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [".run.goorm.io"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'blog',
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount', #social 계정 사용하는법 공부해보자
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.auth0',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.google',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'blog.middleware.ProfileSetupMiddleware',
]

ROOT_URLCONF = 'blog_project.urls'

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

WSGI_APPLICATION = 'blog_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'blog.validators.CustomPasswordValidator',
    },
   
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/uploads/'


# Auth Setting

AUTH_USER_MODEL = 'blog.User'
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_SIGNUP_REDIRECT_URL = 'set_profile'
LOGIN_REDIRECT_URL = 'post-list'
LOGIN_URL = "account_login" # 데코레이터, 믹스인 위한 설정

ACCOUNT_LOGOUT_ON_GET=True
ACCOUNT_AUTHENTICATION_METHOD='email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
# SESION_COOKIE_AGE = 3600
ACCOUNT_SIGNUP_FORM_CLASS = 'blog.forms.SignupForm'
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True # 회원가입시 다른 필드가 유효성 만족 못해도 만족하는 필드 값들은 놔둠

ACCOUNT_EMAIL_VARIFICATION = "none" # mandatory optional none
ACCOUNT_CONFIRM_EMAIL_ON_GET = True # 이메일 인증 링크 누르면 바로 인증됨
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = 'account_email_confirmation_done'
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = 'account_email_confirmation_done'
ACCOUNT_EMAIL_SUBJECT_PREFIX='' #이메일 보낼때 제목 앞에 도메인 붙는거 지우기
# PASSWORD_RESET_TIMEOUT = 3600 # 디폴트 3일

# Email Setting
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' # 콘솔로 메일보내게하는 설정
# kjykjy1037@gmail.com으로 메일보내기
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend' 
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER="kjykjy1037@gmail.com"
EMAIL_HOST_PASSWORD='czcezljnuwyuwwlm'
