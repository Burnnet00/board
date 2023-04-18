from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(reguest):
    bord = Product.objects.order_by('-date')
    return render(reguest, 'orders/index.html', {'bord': bord})

def about(reguest):
    return render(reguest, 'orders/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = Product(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Невірна форма'
    form = ProductForm()
    data = {
        'form' : form,
        'error' : error
    }
    return render(request, 'orders/create.html', data)

def delete(request):
    pass