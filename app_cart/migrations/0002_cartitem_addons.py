# Generated by Django 5.0.4 on 2024-05-06 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cart', '0001_initial'),
        ('app_catalog', '0002_remove_pizzaboard_price_remove_pizzaboard_size_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='addons',
            field=models.ManyToManyField(blank=True, to='app_catalog.pizzaaddons', verbose_name='Добавки к пицце'),
        ),
    ]