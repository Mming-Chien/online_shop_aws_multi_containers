from django import forms
from .models import Order
from localflavor.us.forms import USZipCodeField
class OrderCreateForm(forms.ModelForm):
	''' Form for create new order '''
	# only accept us zip code 
	postal_code = USZipCodeField()
	class Meta:
		model = Order 
		fields = ['first_name', 'last_name', 'email', 'addess', 'postal_code', 'city']
		