from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render
from app_catalog.models import Item, Category, PizzaSauce, PizzaBoard, PizzaAddons, ItemParams, BoardParams, Topping
from django.forms.models import model_to_dict


def catalog(request):
    context = {
        'title': 'Каталог',
    }
    return render(request, 'app_catalog/catalog.html', context=context)


def category_detail(request, slug):
    category = Category.objects.filter(slug=slug, is_active=True).first()
    items = Item.objects.filter(category__slug=slug, is_active=True)

    page = int(request.GET.get('page', 1))
    paginator = Paginator(items, 9)
    current_page = paginator.page(page)

    context = {
        'title': category.name if category else 'Каталог',
        'category': category,
        'items': current_page,
    }
    return render(request, 'app_catalog/catalog.html', context=context)


def item_card(request, item_id):
    item = Item.objects.get(id=item_id)
    context = {
        'title': item.name,
        'item': item,
    }
    if item.category.slug == 'picca':
        context['pizza_addons'] = PizzaAddons.objects.filter(is_active=True)
        context['pizza_sauces'] = PizzaSauce.objects.filter(is_active=True)
        context['pizza_boards'] = PizzaBoard.objects.filter(is_active=True)
    if item.category.slug == 'zapechennye-rolly':
        context['toppings'] = Topping.objects.filter(is_active=True)
    return render(request, 'app_catalog/card.html', context=context)


def get_item_params_price(request):
    if request.method == 'GET':
        param_id = request.GET.get('param_id')
        pizza_board = request.GET.get('board_id')
        pizza_size = request.GET.get('size_id')
        addons = request.GET.get('addons').split(',') if request.GET.get('addons') else None

        final_price = 0
        final_price += ItemParams.objects.get(id=param_id).price

        if pizza_board != '0' and pizza_board is not None:
            final_price += BoardParams.objects.get(board_id=pizza_board, size_id=pizza_size).price

        if addons is not None:
            final_price += sum(PizzaAddons.objects.get(id=addon).price for addon in addons if addon != '')

        print(f'Итоговая цена: {final_price}')
        response_data = {
            'final_price': float(final_price),
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
