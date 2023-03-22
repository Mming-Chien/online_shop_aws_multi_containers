from django.contrib import admin
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from .models import Order, OrderItem
import csv
import datetime

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

def export_to_csv(modeladmin, request, queryset):
	''' Custom action to export model data to csv text file '''
	opts = modeladmin.model._meta
	content_disposition = f'attachment; filename={opts.verbose_name}.csv'
	response = HttpResponse(content_type='text/csv') 	# Tell the browser to treate response as csv file
	response['Content-Disposition'] = content_disposition
	writer = csv.writer(response)
	# Exclude fields with m2m and 12m relationships
	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# Write first row with header information
	writer.writerow(field.verbose_name for field in fields)
	# Write data row
	for obj in queryset:
		data_row =[]
		for field in fields:
			value = getattr(obj, field.name)
			# Convert dateimte to string 
			if isinstance(value, datetime.datetime):
				value = value.strftime('%d/%m/%Y')
			data_row.append(value)
		writer.writerow(data_row)
	return response
export_to_csv.short_discription = 'Export to CSV'


@admin.register(Order)
class OderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email', 'addess', 
			'postal_code', 'city', 'paid',order_payment, 'updated', 'created', ]
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemLine]
	actions = [export_to_csv]
