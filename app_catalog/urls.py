from django.urls import path
from app_catalog.views import catalog, category_detail, get_item_params_price, item_card

app_name = 'app_catalog'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('item/<int:item_id>/', item_card, name='item_detail_view'),
    path('get_item_params_price/', get_item_params_price, name='get_item_params_price'),
    path('<slug:slug>/', category_detail, name='category_detail'),
]
