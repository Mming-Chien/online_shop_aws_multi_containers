import os 
from .base import *
DEBUG = True
ADMINS = [
	('Minh Chien', 'minhchien03py@gmail.com'),
]
ALLOWED_HOSTS = ['*']
DATABASES = {
	'default':{
		'ENGINE':'django.db.backends.postgresql',
		# 'NAME':os.environ.get('POSTGRES_DB'),	
		# 'USER':os.environ.get('POSTGRES_USER'),
		# 'PASSWORD':os.environ.get('POSTGRES_PASSWORD'),
		'NAME':os.environ.get('POSTGRES_DB'),	
		'USER':os.environ.get('POSTGRES_USER'),
		'PASSWORD':os.environ.get('POSTGRES_PASSWORD'),
		'HOST':'db',
		'PORT':5432,
	}
}

# REDIS_URL = 'redis://cache:6379'
# CACHES['default']['LOCATION']= REDIS_URL
# CHANNEL_LAYERS['default']['CONFIG']['host']
# Setting for Redis
REDIS_HOST = 'cache'
REDIS_PORT = 6379
REDIS_DB = 1

