from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Coupon(models.Model):
	''' Model to store coupon information '''
	code = models.CharField(max_length=50, unique=True)
	valid_from = models.DateTimeField()
	valid_to = models.DateTimeField()
	# Discount is percent number limit from 0 to 100
	discount = models.IntegerField(
		validators = [MinValueValidator(0), MaxValueValidator(100)],
		help_text='Percentage value (0 to 100)')
	active = models.BooleanField()
	def __str__(self):
		return self.code 