# Generated by Django 5.0.4 on 2024-05-03 10:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_catalog', '0002_remove_pizzaboard_price_remove_pizzaboard_size_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_catalog.item', verbose_name='Товар')),
                ('item_params', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_catalog.itemparams', verbose_name='Параметры')),
                ('pizza_board', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_catalog.pizzaboard', verbose_name='Борт для пиццы')),
                ('sauce_base', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_catalog.pizzasauce', verbose_name='Соус-основа')),
                ('topping', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_catalog.topping', verbose_name='Шапочка')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Товар в корзине',
                'verbose_name_plural': 'Товары в корзине',
                'db_table': 'cart_items',
            },
        ),
    ]
