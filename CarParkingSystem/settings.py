"""
Django settings for CarParkingSystem project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

from pathlib import Path
# from CarParkingSystem.middleware import AuthenticationMiddleware
# from widget_tweaks.templatetags import *
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o*bl)@-_4uv&_r%3sd++#%7w7uc_3#ezu1-ce#^+b42^#kth9^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',
    'bootstrap_modal_forms',
    'widget_tweaks',
    'rest_framework',
    'oauth2_provider',
    'imagekit',
    'storages',
    'django.contrib.sites',  # Bổ sung
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
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

ROOT_URLCONF = 'CarParkingSystem.urls'  # config cua urls.py

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

WSGI_APPLICATION = 'CarParkingSystem.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DATETIME_FORMAT = 'Y-m-d'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

AUTH_USER_MODEL = 'myapp.User'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587  # 465
# EMAIL_USE_SSL = True
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'nhom9qlda2223@gmail.com'
EMAIL_HOST_PASSWORD = 'zpqxzpdcbzqgxefk'
DEFAULT_FROM_EMAIL = 'nhom9qlda2223@gmail.com'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = 'home'  # Đường dẫn sau khi đăng nhập thành công

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '859484570336-2buunfcpo4gaajduivvgts7hk4sb8prj.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        }
    },
    'facebook': {
        'APP': {
            'client_id': 'YOUR_FACEBOOK_APP_ID',
            'secret': 'YOUR_FACEBOOK_APP_SECRET',
            'key': ''
        }
    }
}


# # Import thư viện google.auth và google.cloud để kết nối đến Firebase Storage
# import google.auth
# from google.cloud import storage
#
# _, project_id = google.auth.default()
# bucket_name = f"{project_id}.appspot.com"
#
#
# # Khai báo class để sử dụng cho việc lưu trữ file tải lên lên Firebase Storage
# class FirebaseStorage(S3Boto3Storage):
#     def __init__(self, **settings):
#         self.bucket_name = bucket_name
#         self.access_key = settings.pop('access_key')
#         self.secret_key = settings.pop('secret_key')
#         self.region_name = settings.pop('region_name')
#         self.endpoint_url = f"https://{bucket_name}"
#         super().__init__(**settings)
#
#
# # Cấu hình các biến để sử dụng với Firebase Storage
# GS_PROJECT_ID = "carparkingsystem-8d374"
# GS_BUCKET_NAME = 'CarParkingSystem'
# GS_LOCATION = 'asia-southeast1'
# GS_ACCESS_KEY_ID = 'carparkingsystem-8d374'
# GS_SECRET_ACCESS_KEY = '\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCYGVOZbeHqY2dT\nv/SkrTOIZl4EnXS6DMXRmkz0Y5QYYUT9hWrsO3M8lEwadOGNa75hlawf4xYYS22S\nhFlWjaONoSyxu44xdRWzLCr4HTj5hfyiB6xorQkOwQDRbqV62kb3kR7aCA9TU9Pe\nBJKCxVsLXkuUoshoH74AqlndGbrLmTDuJJLSVwsFfdsYpH8G7egHKaloElSde12u\nZtGQtdkakI2BLCplqIlvr2NnFU6J8P6LEZC6KMB1Cg3cYZ7rfcL53O98vEy3PgCS\nQnrrN/86zQUZsT/zCgywfUUzbHFjUksE5xCHTSXlzjxbIhQlUxkKhmHakhvl7rK9\n4zWdiSmjAgMBAAECggEACZTwljzqiS7HPGrMIp5CZuh1vD7WRSzSrKTpDgid6277\nkSjQCRXx+5s5fP153h+KunnIlMzSCXGh4SO3v6ej6dol2ZaJAAtWmUUUZ57qhgP0\nEr5+3fWUq7XqhaKG40B9uwfoMALU+XkarABsc9wg2kNGsu/I6rShN5FfMufQ+oMs\njYFDjYPlUuJn+E+GK8YWJElboPCKmNFokb4dwOEbPa0t6bPYwX2DmiJaGAyUo4OS\nMGb71cwvzBRxOwLJXMX/A3IkCrHmPYzn1VYZ8xHtm6+6CAFS3Am+AxbmAdIBYz3L\nsJ8vW31bZSdRMt766jicdgeP81theXApU4erFZl5jQKBgQDNsi97W7rSyEXSA9uT\n7ZBLvB6K62GhTBc+1DBHOq9gIyKNxw6xd9FykC+NYppHwioXhdccsLFOoSozquO/\nVoQwgmdojzG47iN+xE0e427CtmlE3lcNUIgvu3hrDwo0lZC7d1M5d4OnzKJdC5Lv\nrS9FqJLf5kB/K+NQMsXebLW3LQKBgQC9S6N2ONH2UGCyvOaZIGjVmnAA4OhgAQti\nQ/mDec6SO+ys/xN7sIfaeqCnabdolZVgz3en8eu0Q38l8xzdPV1utwp7zJa/ayxg\nWcSYqDYu0xAr1mTHNrwcLZZNkNOmqdWg2nWPdMtq3xXWoIzCeEjT1aKMBIIjSCPi\nC+xZUDXmDwKBgQCz9mNob/biF2pOtiVUJRKL0EiAjjNapXHo/EhI6WUqnVLL7A5E\n4mmS6+dOsaf9hDjDX8u2RDi8bHC5x5d+fbkln9HNPwrnmyHe9OvsTFtJa8JqCITt\nFzovWLugHwZ0vy5jdaCQtKmxE24yLcAehczICxaFYbOoD8PPFLzdPws0+QKBgQCW\ntmlAED9DIH3M8U+cLUyqfNqeKHN7NHmu1DYNsuaAUYu/tRr7CPMxRR8yC56Ge0pC\nmQxIv/mNPYw3V9fsYhZItx12sc54O0lKsU4wyQTSxSMD9B+q6O5edQFNYnjRIjk/\nZ4/gFvp6bYHCr3NCxmgdmONhHZnLo31GVX3pIk63iwKBgGd/r1+NjF7QBpXyFO9N\nIGU9+QDtYJdScQ6mVBUhSKZ2DOrZ8Qrxy4vrn8/iL8R8dJCJG1USwsTmmaW8i7ml\nBnFul5A8DDMW4/eVJVLItqcdGBROt6DTzhXXvBf9Motl1rYa2j9toYjPLHV4dVNF\nE/QMNokO3IIjAehPhq+xrclA\n'
#
# # Thiết lập DEFAULT_FILE_STORAGE và STATICFILES_STORAGE để sử dụng Firebase Storage
# DEFAULT_FILE_STORAGE = 'your_project_name.firebase_storage.FirebaseStorage'

# DEFAULT_FILE_STORAGE = 'storages.backends.firebase.FirebaseStorage'
# FIREBASE_STORAGE_BUCKET = 'carparkingsystem-8d374.appspot.com'
# # FIREBASE_STORAGE_PREFIX = 'your-prefix'
# FIREBASE_STORAGE_EXTRA_OPTIONS = {
#     # 'firebase_auth_uid': 'your-firebase-auth-uid',
#     'google_application_credentials': 'serviceAccount.json',
# }
# AUTHENTICATION_BACKENDS = [
#     'social_core.backends.google.GoogleOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# ]

# REST_FRAMEWORK ={
#     'DEFAULT_AUTHENTICATION_CLASSES':(
#     'oauth2_provider.contrib.rest_framework.OAuth2Authentication',)
# }


# CELERY_BROKER_URL = 'amqp://localhost'  # or your broker URL
# CELERY_RESULT_BACKEND = 'django-db'    # or another backend you prefer

# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_TASK_SERIALIZER = 'json'
# CELERY_RESULT_SERIALIZER = 'json'

# CELERY_BEAT_SCHEDULE = {
#     'my-task-name': {
#         'task': 'myapp.tasks.my_task_function',
#         'schedule': 10.0,  # run every 10 seconds
#     },
# }
