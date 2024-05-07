from django.urls import path
from app_order.views import order_create, orders, order_detail

app_name = 'app_order'

urlpatterns = [
    path('order_detail/<int:order_id>/', order_detail, name='order_detail'),
    path('orders/', orders, name='orders'),
    path('order-create/', order_create, name='order_create'),
]
