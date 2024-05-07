from django.shortcuts import render
from app_catalog.models import Category


def home(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'app_home/index.html', context=context)
