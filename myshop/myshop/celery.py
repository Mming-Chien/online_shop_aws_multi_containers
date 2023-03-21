import os 
from celery import Celery
''' celery -A myshop worker --concurrency=1000 -P eventlet
need to add the -P pool for the celery to work properly'''
# Set the default Django settings models for the 'celery' program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')
app = Celery('myshop')
app.config_from_object('django.conf:settings', namespace='CELERY') 
app.autodiscover_tasks()