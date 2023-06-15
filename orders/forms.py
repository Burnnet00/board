from .models import Product
from django.forms import ModelForm, TextInput, Textarea, FileInput, ImageField, NumberInput, ClearableFileInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']
        widgets = {'name': TextInput(attrs={"class": "form-control", "placeholder": "Введіть назву"}),
                   'image': ClearableFileInput(attrs={"class": "form-control", "placeholder": "Світлина"}),
                   'description': Textarea(attrs={"class": "form-control", "placeholder": "Опис"}),
                   'price': NumberInput(attrs={"class": "form-control", "placeholder": "Ціна"})
                   }
