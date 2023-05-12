from .models import Product
from django.forms import ModelForm, TextInput, Textarea, FileField, ImageField


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']

    widgets = {
        'name': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Назва'
        }),
        'image': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Світлина'
        }),
        'description': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Опис'
        }),
        'price': TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ціна'
        }),

    },
