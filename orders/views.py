from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView
from django.views.generic.edit import FormView


from .models import Product
from .forms import ProductForm

class ProductViews(FormView):
     form_class = ProductForm
     template_name = 'orders/create.html'
     success_url = 'orders/create.html'
     def form_valid(self, form):
         form.save()
         return super(ProductViews, self).form_valid(form)

def home(reguest):
    bord = Product.objects.order_by('-date')#order = сортировка по полю (- дата от более новых)
    return render(reguest, 'orders/index.html', {'bord': bord})

class NewDetailView(DetailView):
    model = Product
    template_name = 'order/new.html'
    context_object_name = 'prod'

class NewUpdateView(UpdateView):
    model = Product
    template_name = 'orders/create.html'
    form_class = ProductForm

def about(reguest):
    return render(reguest, 'orders/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect ('home')
        else:
            error = 'Невірна форма'
    form = ProductForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'orders/create.html', data)

def delete(request):
    pass