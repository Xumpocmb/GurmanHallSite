from django.contrib import admin

from django.contrib import admin
from app_order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['__str__', ]
    fields = ['id', 'status', 'created_at', 'customer',
              ('first_name', 'email', 'address', 'phone',),
              'delivery_method', 'cart_history']

    readonly_fields = ['id', 'created_at', 'customer', 'cart_history']
