from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart 
from .tasks import order_created

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		# OrderCreateForm is submitted
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				# Create OrderItem for each product in cart
				OrderItem.objects.create(order=order, product=item['product'], 
							price=item['price'], quantity=item['quantity'])
			# Clear the cart 
			cart.clear()
			# Launch asynchronous task
			order_created.delay(order.id)
			# Set the order in the session
			request.session['order_id']=order.id 
			# Redirect for payment
			return redirect(reverse('payment:process'))
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'form':form})
