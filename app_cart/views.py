from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render

from app_cart.models import CartItem
from app_catalog.models import Item, ItemParams, PizzaSauce, Topping, PizzaBoard, Category, PizzaAddons


@login_required(login_url='app_user:login')
def add_to_cart_view(request):
    user = request.user
    item_id = request.POST.get('item_id')
    param_id = request.POST.get('item-size-radio')
    pizza_sauce = PizzaSauce.objects.filter(pk=request.POST.get('pizza_sauce')).first() if request.POST.get(
        'pizza_sauce') else None
    pizza_board = PizzaBoard.objects.filter(pk=request.POST.get('pizza_board')).first() if request.POST.get(
        'pizza_board') else None
    topping = Topping.objects.filter(pk=request.POST.get('souse-option')).first() if request.POST.get(
        'souse-option') else None
    addons_ids = request.POST.getlist('addons') if request.POST.getlist('addons') else None
    if addons_ids is not None:
        addons_ids = [int(addon) for addon in addons_ids]

    addons = PizzaAddons.objects.filter(pk__in=addons_ids) if addons_ids else None
    item = Item.objects.filter(pk=item_id).first()
    item_params = ItemParams.objects.filter(pk=param_id).first()

    if item_params.size:
        size = item_params.size
    elif item_params.count:
        size = item_params.count
    else:
        size = item_params.weight

    # Проверка наличия уже добавленного продукта в корзине
    existing_cart_item = CartItem.objects.filter(
        user=user,
        item=item,
        item_params=item_params,
        sauce_base=pizza_sauce,
        topping=topping,
        pizza_board=pizza_board
    )

    if addons_ids is not None:
        existing_cart_item = existing_cart_item.filter(addons__in=addons)

    existing_cart_item = existing_cart_item.first()

    if existing_cart_item:
        existing_cart_item.quantity += 1
        existing_cart_item.save()
        messages.success(request, f'{item.name} добавлен в корзину', extra_tags='success')
    else:
        cart_item = CartItem.objects.create(user=user, item=item, item_params=item_params, quantity=1,
                                            sauce_base=pizza_sauce, pizza_board=pizza_board, topping=topping)
        cart_item.addons.set(addons) if addons else None
        messages.success(request, f'{item.name} добавлен в корзину', extra_tags='success')
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def remove_from_cart_view(request, cart_id):
    cart_item = CartItem.objects.filter(id=cart_id).first()
    if cart_item:
        cart_item.delete()
        messages.success(request, 'Товар удален из корзины.', extra_tags='info')
    return redirect('app_cart:cart')


def cart_view(request):
    context = {
        'title': 'Корзина',
    }
    return render(request, 'app_cart/cart.html', context=context)


def click_on_plus(request, cart_id):
    cart_item = CartItem.objects.filter(id=cart_id).first()
    cart_item.quantity += 1
    cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def click_on_minus(request, cart_id):
    cart_item = CartItem.objects.filter(id=cart_id).first()
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

