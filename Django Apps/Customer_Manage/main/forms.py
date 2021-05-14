from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'  # Order class'ında bulunan tüm attributelere field aç demek
        # bunu yerine ['name', ..] gibi de yazabilirdik.