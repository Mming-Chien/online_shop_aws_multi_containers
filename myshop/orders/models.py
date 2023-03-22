from django.db import models
from django.conf import settings
from shop.models import Product 

class Order(models.Model):
	''' Model for information of customer who place an order '''
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	addess = models.CharField(max_length=250)
	postal_code = models.CharField(max_length=25)
	city = models.CharField(max_length=250)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)
	stripe_id = models.CharField(max_length=250, blank=True)

	class Meta:
		ordering = ['-created']
		indexes = [
			models.Index(fields=['-created']),
		]

	def __str__(self):
		return f'Oder {self.id}'

	def get_total_cost(self):
		return sum(item.get_cost() for item in self.items.all())

	def get_stripe_url(self):
		''' stripe url for payment detail '''
		if not self.stripe_id:
			# No payment is associated
			return ''
		if '_test_' in settings.STRIPE_SECRET_KEY:
			# Stripe path for test environment
			path = '/test/'
		else:
			# Stripe path for production environment
			path ='/'
		return f'http://dashboard.stripe.com{path}payments/{self.stripe_id}'


class OrderItem(models.Model):
	''' Store information for each product in the order '''
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return str(self.id)

	def get_cost(self):
		''' get cost for each product '''
		return self.price*self.quantity
