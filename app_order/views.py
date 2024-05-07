from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app_order.forms import OrderForm
from app_order.models import Order
from app_user.models import User


@login_required(login_url='app_user:login')
def order_create(request):
    context = {
        'title': 'Оформление заказа',
        'form': OrderForm(),
    }

    if request.method == 'POST':
        form = OrderForm(request.POST)
        form.instance.customer = User.objects.get(username=request.user)

        if form.is_valid():
            if form.instance.phone and form.instance.address:
                user_order = form.save()
                user_order.fill_cart_history()
                messages.success(request, 'Заказ оформлен', extra_tags='success')
                return HttpResponseRedirect(reverse('app_order:orders'))
            else:
                messages.error(request, 'Укажите ваш телефон и адрес для оформления заказа!',
                               extra_tags='danger')
        else:
            messages.error(request, 'Ошибка при оформлении заказа!', extra_tags='danger')
    return render(request, 'app_order/create.html', context=context)


@login_required(login_url='app_user:login')
def orders(request):
    user_orders = Order.objects.filter(customer=request.user)
    context = {
        'title': 'Мои заказы',
        'orders': user_orders,
    }
    return render(request, 'app_order/orders.html', context=context)


@login_required(login_url='app_user:login')
def order_detail(request, order_id):
    order = Order.objects.get(pk=order_id)
    context = {
        'title': 'Детали заказа',
        'order': order,
    }
    return render(request, 'app_order/order_detail.html', context=context)
