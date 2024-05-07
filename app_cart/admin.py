from django.contrib import admin
from app_cart.models import CartItem


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['__str__']
    search_fields = ['user']
