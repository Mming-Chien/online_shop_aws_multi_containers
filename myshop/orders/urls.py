from django.urls import path
from . import views
app_name = 'orders'
urlpatterns = [
	path('creat/', views.order_create, name='order_create'),
]