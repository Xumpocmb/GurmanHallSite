from django.urls import path
from app_cart.views import add_to_cart_view, cart_view, remove_from_cart_view, click_on_minus, click_on_plus

app_name = 'app_cart'

urlpatterns = [
    path('add-to-cart/', add_to_cart_view, name='add_to_cart'),
    path('remove-from-cart/<int:cart_id>/', remove_from_cart_view, name='remove_from_cart'),
    path('cart/', cart_view, name='cart'),
    path('click_on_minus/<int:cart_id>/', click_on_minus, name='click_on_minus'),
    path('click_on_plus/<int:cart_id>/', click_on_plus, name='click_on_plus'),
]
