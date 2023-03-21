from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Order, OrderItem

def order_payment(obj):
	''' HTML link for each stripe payment '''
	url = obj.get_stripe_url()
	if obj.stripe_id:
		html = f'<a href="{url}" target="_blank" >{ obj.stripe_id }</a>'
		return mark_safe(html)
	return ''

class OrderItemLine(admin.TabularInline):
	''' Inline to display in OrderAdmin edit page '''
	model = OrderItem 
	raw_id_fields = ['product']

@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email', 'addess', 
			'postal_code', 'city', 'paid',order_payment, 'updated', 'created', ]
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemLine]
