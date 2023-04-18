from .models import Product
from django.forms import ModelForm, TextInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price',]

    widgets = {
        'name': TextInput(attrs={'placeholder' : 'Назва' })

    },
