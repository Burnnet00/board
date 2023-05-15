from .models import Product
from django.forms import ModelForm, TextInput, Textarea, FileInput, ImageField, DecimalField, ClearableFileInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва'
            }),
            'image': ClearableFileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Світлина'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опис'
            }),
            'price': DecimalField(max_digits=5, decimal_places=2, widget=TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ціна'
            })),

        },
