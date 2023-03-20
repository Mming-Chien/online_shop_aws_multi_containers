import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order

@csrf_exempt
def stripe_webhook(request):
	''' Webhook endpoint for recieve payment notifications to mark order as paid '''
	payload = request.body
	sig_header = request.META['HTTP_STRIPE_SIGNATURE']
	event = None
	try:
		event = stripe.Webhook.construct_event(
				payload,
				sig_header,
				settings.STRIPE_WEBHOOK_SECRET)
	except ValueError as e:
		# invalid payload
		return HttpResponse(status=400)
	except stripe.error.SignatureVerificationError as e:
		# Invalid signature
		return HttpResponse(status=400)

	# Retrieve order and mark as paid
	if event.type == 'checkout.session.completed':
		session = event.data.object 
		if session.mode=='payment' and session.payment_status=='paid':
			try:
				# the client_reference_id was passed in process view
				order = Order.objects.get(id=session.client_reference_id) 
			except Order.DoesNotExist:
				return HttpResponse(status=404)
			# Mark order as paid
			order.paid = True 
			order.save()
	return HttpResponse(status=200)
