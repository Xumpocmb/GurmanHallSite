from django import forms
from app_order.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'email', 'address', 'phone', 'delivery_method']
        widgets = {
            'delivery_method': forms.RadioSelect(choices=(
                ('pickup', 'Самовывоз'),
                ('delivery', 'Курьер'),
            )),
        }


