from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
	# Url for all products
	path('', views.product_list, name='product_list'),
	# Url for products by a given category
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	# Url for a specific product
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]