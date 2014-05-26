"""
Django settings for projectAdmin project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))


BASE_EMAIL = "singleprojects@gmail.com"



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+42=#+!zz&-h2au845b4bkq)bart*wm$$)%o#-0&$bx&nhbvm6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

ADMINS = ('silviobravo', 'bravocado@gmail.com')

MANAGERS = ADMINS

# Application definition

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates")
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'principal',
    #'django_extensions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'projectAdmin.urls'

WSGI_APPLICATION = 'projectAdmin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        #'NAME' : 'projectadmin',
#        'NAME' : 'project',
#        'USER' : 'postgres',
#        'PASSWORD' : 'pass',
#        'HOST' : 'localhost',
#        'PORT' : '5432',
#    }
#}


DATABASE = {
    'default' : {
        'ENGINE': 'django.db.backends.',
        'NAME' : 'project',
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : '',
        'PORT' : '',
    }    
}




MEDIA_ROOT = os.path.join(PROJECT_ROOT, '..', 'media')
MEDIA_URL = '/media/'

###################### DATOS PARA MONGO DB ::::::::::::::)


AUTHENTICATION_BACKENDS = (
    'mongoengine.django.auth.MongoEngineBackend',
)

SESSION_ENGINE = 'mongoengine.django.sessions'

MONGO_DATABASE_NAME = 'project'

########################## CONECTAS CON MONGO DB #####################

from mongoengine import connect
connect(MONGO_DATABASE_NAME)





####################  FINALIZA LOS DATOS DE MONGO DB :::::::::::::)




# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)



STATICFILES_IMAGES_DIR = (
    os.path.join(BASE_DIR, "static/images"),
)



STATICFILES_USER_IMAGES_DIRS = (
    os.path.join(BASE_DIR, "static/images/users"),
)


STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"

)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)