# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'django_neomodel',
    'drf_yasg',
    'defender',
    'corsheaders',
    'captcha',
    'axes',
    'django_celery_beat',
    'django_extensions',
    'django_filters',
    'django_rq',

    'books',
    'userprofile',
    'authen',
    'bookcase',
    'filemedia',
    'analytics',
    'recommender',
    'posts',
    'groups',
    'payments',
    'collector',

    'apps.vadmin.permission',
    'apps.vadmin.op_drf',
    'apps.vadmin.system',
    'apps.vadmin.celerys',
    'apps.vadmin.monitor'
]
