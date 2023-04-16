from django.shortcuts import render
from .models import Product

def home(reguest):
    return render(reguest, 'orders/index.html')

def about(reguest):
    return render(reguest, 'orders/about.html')
