from django import forms
from .models import Order
class OrderCreateForm(forms.ModelForm):
	''' Form for create new order '''
	class Meta:
		model = Order 
		fields = ['first_name', 'last_name', 'email', 'addess', 'postal_code', 'city']
		