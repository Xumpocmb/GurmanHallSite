from django.contrib.auth.models import AbstractUser
from django.db import models

from app_catalog.models import Item, ItemParams, PizzaSauce, Topping, PizzaBoard, PizzaAddons, BoardParams
from app_user.models import User


class CartQuerySet(models.QuerySet):
    def total_quantity(self):
        return sum(item.quantity for item in self)

    def total_sum(self):
        return sum(item.sum() for item in self)


class CartItem(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='Пользователь', null=True, blank=True)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE, verbose_name='Товар', null=True, blank=True)
    item_params = models.ForeignKey(to=ItemParams, on_delete=models.CASCADE, verbose_name='Параметры', null=True,
                                    blank=True)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество', null=True, blank=True)
    description = models.TextField(verbose_name='Описание', null=True, blank=True)
    sauce_base = models.ForeignKey(to=PizzaSauce, on_delete=models.SET_NULL, verbose_name='Соус-основа', null=True,
                                   blank=True)
    pizza_board = models.ForeignKey(to=PizzaBoard, on_delete=models.SET_NULL, verbose_name='Борт для пиццы', null=True,
                                    blank=True)
    addons = models.ManyToManyField(to=PizzaAddons, verbose_name='Добавки к пицце', blank=True)
    topping = models.ForeignKey(to=Topping, on_delete=models.SET_NULL, verbose_name='Шапочка', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан', null=True, blank=True)

    objects = CartQuerySet.as_manager()

    class Meta:
        db_table = 'cart_items'
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def __str__(self):
        return f'Корзина: {self.user.username} | Продукт: {self.item.name}'

    def sum(self):
        base_price = self.item_params.price * self.quantity
        if self.pizza_board:
            board_params = BoardParams.objects.filter(board=self.pizza_board).first()
            if board_params:
                base_price += board_params.price
        addons_price = sum(addon.price for addon in self.addons.all())
        base_price += addons_price

        return base_price

    def de_json(self):
        addons_dict = {addon.name: float(addon.price) for addon in self.addons.all()}
        items = {
            'product_name': f'{self.item.category.name}|{self.item.name}',
            'price': float(self.item_params.price),
            'sum': float(self.sum()),
            'quantity': self.quantity,
            'description': self.description or '',
            'params': {
                'size': float(self.item_params.size.size) if self.item_params.size else None,
                'count': float(self.item_params.count) if self.item_params.count else None,
                'weight': float(self.item_params.weight) if self.item_params.weight else None
            },
            'sauce': self.sauce_base.name if self.sauce_base else None,
            'topping': self.topping.name if self.topping else None,
            'pizza_board': {'name': self.pizza_board.name, 'price': float(BoardParams.objects.filter(board=self.pizza_board).first().price)} if self.pizza_board else None,
            'addons': addons_dict,
        }
        return items
