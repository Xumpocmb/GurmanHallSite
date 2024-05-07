from app_catalog.models import Category


def menu_items(request):
    return {'categories': Category.objects.filter(is_active=True)}
