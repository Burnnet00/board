from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('delete', views.delete, name='delete'),
]