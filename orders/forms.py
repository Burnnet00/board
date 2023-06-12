from .models import Product
from django.forms import ModelForm, TextInput, Textarea, FileInput, ImageField, DecimalField, ClearableFileInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price']
