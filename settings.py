from settings_secret import *

#DEBUG = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Michal Mazurek', 'akfaew@gmail.com'),
)

MANAGERS = ADMINS

# DATABASES from settings_secret

APPEND_SLASH = True
TIME_ZONE = 'Europe/Warsaw'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
MEDIA_ROOT = '/home/longturn-www/media/'
MEDIA_URL = 'http://longturn.net/media/'
STATIC_ROOT = '/home/longturn-www/longturn/static/'
STATIC_URL = 'http://longturn.net/static/'
PLOT_PATH = '/home/longturn-www/longturn/plots/'
ADMIN_MEDIA_PREFIX = '/media/'
# SECRET_KEY from settings_secret

TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.Loader',
	'django.template.loaders.app_directories.Loader',
#	'django.template.loaders.app_directories.load_template_source',
#	'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
#	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'longturn.urls'

ALLOWED_HOSTS = ['longturn.net', 'www.longturn.net']

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
    'DIRS': ['templates'],
}]

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
#	'django.contrib.sites',
	'django.contrib.messages',
	#'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.humanize',
	'longturn.main',
	'longturn.player',
	'longturn.game',
	'longturn.warcalc',
	'longturn.serv',
	'longturn.fluxbb',
	'longturn.old',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.contrib.auth.context_processors.auth",
	"django.core.context_processors.debug",
	#"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.contrib.messages.context_processors.messages",
	'longturn.main.models.paths',
	'longturn.main.models.active_games',
)
LOGIN_REDIRECT_URL = "/account/profile/"

AUTHENTICATION_BACKENDS = ('longturn.player.backends.GenMD5ModelBackend',)
