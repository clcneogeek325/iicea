import os
URL_LOGIN = "/login/"

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '-8jb=0vw7o=5iy_8pg9y6-_)-$*syhaoda1y@^jvj1%1-dif7)'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_sockjs_tornado',
    'apps.asistencia_alumno',
    'apps.asistencia_empleado',
    'apps.concepto_pago',
    'apps.empleado',
    'apps.alumno',
    'apps.grupo',
    'apps.pago',
    'apps.nomina',
    'apps.horario',
    'apps.materia',
    'apps.perfil',
    'apps.semestre',
    'apps.tutor',
    'apps.home',
    'apps.observacion',
    'apps.calificacion',
    'apps.chat',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'iicea.urls'

WSGI_APPLICATION = 'iicea.wsgi.application'


db = "sqlite"

if db == "sqlite":
	DATABASES = {
		'default': {
		    'ENGINE': 'django.db.backends.sqlite3',
		    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
		}
	}
if db == "mysql":
	DATABASES = {
		'default': {
		    'ENGINE': 'django.db.backends.mysql',
		    'NAME': 'iicea',
		    'USER': 'root',
		    'PASSWORD': 'rapero04',
		    'HOST': '127.0.0.1',
		    'PORT': '',
		}
	}

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
		'static/',
		)

TEMPLATE_DIRS = (
		'plantillas/',
		)

MEDIA_URL = '/media/'
MEDIA_ROOT =  os.path.normpath(os.path.join(BASE_DIR,'media/'))
		
AUTH_USER_MODEL = 'auth.User'


SOCKJS_PORT = 9999
SOCKJS_CHANNEL = 'echo'
SOCKJS_CLASSES = (
    'apps.chat.sockserver.ChatConnection',
)

