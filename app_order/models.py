from django.db import models
from app_user.models import User
from app_cart.models import CartItem


class Order(models.Model):
    DELIVERY_METHOD_CHOICES = [
        ('pickup', 'Самовывоз'),
        ('delivery', 'Доставка'),
    ]

    STATUS_CHOICES = [
        (0, 'Создан'),
        (1, 'В обработке'),
        (2, 'Доставляется'),
        (3, 'Доставлен'),
        (4, 'Отменен'),
    ]

    customer = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name='Покупатель', null=True, blank=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', null=True, blank=True)
    email = models.EmailField(max_length=254, verbose_name='Email', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    phone = models.CharField(max_length=255, verbose_name='Телефон', null=True, blank=True)
    cart_history = models.JSONField(default=dict)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0, verbose_name='Статус заказа')
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHOD_CHOICES, verbose_name='Способ доставки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        formatted_date = self.created_at.strftime('%d-%m-%Y %H:%M')
        return f'Заказ № {self.id} от {formatted_date}, статус: {self.get_status_display()}'

    def fill_cart_history(self):
        carts = CartItem.objects.filter(user=self.customer)
        total_sum = float(carts.total_sum())
        basket_history = {
            'carts': [cart.de_json() for cart in carts],
            'total_sum': total_sum
        }
        self.cart_history = basket_history
        carts.delete()
        self.save()
