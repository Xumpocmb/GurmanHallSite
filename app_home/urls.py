from django.urls import path
from app_home.views import home

app_name = 'app_home'

urlpatterns = [
    path('', home, name='home'),
]
