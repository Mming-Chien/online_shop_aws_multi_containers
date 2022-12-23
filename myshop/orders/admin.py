from django.contrib import admin

from .models import Order, OrderItem
class OrderItemLine(admin.TabularInline):
	''' Inline to display in OrderAdmin edit page '''
	model = OrderItem 
	raw_id_fields = ['product']

@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email', 'addess', 
			'postal_code', 'city', 'paid', 'updated', 'created']
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemLine]
