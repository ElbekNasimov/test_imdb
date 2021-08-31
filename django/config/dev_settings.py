from .common_settings import *

DEBUG = True

SECRET_KEY = 'django-insecure-0#5jk#3(3wwnx@-dt!ppr990kk%e_vrf$%el$yz*p1fs*$em26'

INSTALLED_APPS += [
    'debug_toolbar',
]

DATABASES['default'].update({
    'NAME': 'mymdb',
    'USER': 'postgres',
    'PASSWORD': 'elbeknasimov',
    'HOST': 'localhost',
    'PORT': '5432',
})

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-locmemcache',
        'TIMEOUT': 5,   # 5 seconds
    }
}

MEDIA_ROOT = BASE_DIR / 'movies'
