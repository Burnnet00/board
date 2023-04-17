from django.shortcuts import render
from .models import Product

def home(reguest):
    bord = Product.objects.order_by('-date')
    return render(reguest, 'orders/index.html', {'bord': bord})

def about(reguest):
    return render(reguest, 'orders/about.html')
