# Generated by Django 5.0.4 on 2024-05-02 12:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CafeBranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('phone1', models.CharField(blank=True, max_length=20, null=True)),
                ('phone2', models.CharField(blank=True, max_length=20, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Филиал',
                'verbose_name_plural': 'Филиалы',
                'db_table': 'branches',
            },
        ),
        migrations.CreateModel(
            name='PizzaAddons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название добавки')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена в руб.')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pizza_addons/', verbose_name='Изображение')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Добавка для пиццы',
                'verbose_name_plural': 'Добавки для пиццы',
                'db_table': 'pizza_addons',
            },
        ),
        migrations.CreateModel(
            name='PizzaSauce',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название соуса')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Соус-основа пиццы',
                'verbose_name_plural': 'Соус-основа пиццы',
                'db_table': 'pizza_sauces',
            },
        ),
        migrations.CreateModel(
            name='PizzaSizes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Размер в см.')),
                ('slug', models.SlugField(blank=True, max_length=3, null=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Размер пиццы',
                'verbose_name_plural': 'Размеры пиццы',
                'db_table': 'pizza_sizes',
            },
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название шапочки')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Шапочка для запеченных роллов',
                'verbose_name_plural': 'Шапочки для запеченных роллов',
                'db_table': 'toppings',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название категории')),
                ('image', models.ImageField(blank=True, null=True, upload_to='category_images', verbose_name='Изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активна')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_catalog.cafebranch')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='item_images', verbose_name='Изображение')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлен')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_catalog.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'items',
            },
        ),
        migrations.CreateModel(
            name='PizzaBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название борта')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена в руб.')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_catalog.pizzasizes', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Борт для пиццы',
                'verbose_name_plural': 'Борт для пиццы',
                'db_table': 'pizza_boards',
            },
        ),
        migrations.CreateModel(
            name='ItemParams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Количество в шт.')),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Вес в гр.')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена в руб.')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_catalog.item')),
                ('size', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app_catalog.pizzasizes', verbose_name='Размер')),
            ],
            options={
                'verbose_name': 'Параметры товара',
                'verbose_name_plural': 'Параметры товара',
                'db_table': 'item_params',
            },
        ),
    ]