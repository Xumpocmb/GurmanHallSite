# Generated by Django 5.0.4 on 2024-05-06 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='basket_history',
            new_name='cart_history',
        ),
    ]