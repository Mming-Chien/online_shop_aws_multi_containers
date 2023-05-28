from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.admin.views.decorators import staff_member_required
from .forms import OrderCreateForm
from .models import OrderItem, Order 
from cart.cart import Cart 
from .tasks import order_created

def order_create(request):
	cart = Cart(request)
	if request.method == 'POST':
		# OrderCreateForm is submitted
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			if cart.coupon:
				order.coupon = cart.coupon
				order.discount = cart.coupon.discount
			order.save()
			for item in cart:
				# Create OrderItem for each product in cart
				OrderItem.objects.create(order=order, product=item['product'], 
							price=item['price'], quantity=item['quantity'])
			# Clear the cart 
			cart.clear()
			# Launch asynchronous task
			#order_created.delay(order.id)
			# Set the order in the session
			request.session['order_id']=order.id 
			# Redirect for payment
			return redirect(reverse('payment:process'))
	else:
		form = OrderCreateForm()
	return render(request, 'orders/order/create.html', {'form':form})

@staff_member_required
def admin_order_detail(request, order_id):
	''' Custom view to display order detail for administration site'''
	order = get_object_or_404(Order, id=order_id)
	return render(request, 'admin/order/orders/detail.html', {'order':order})
