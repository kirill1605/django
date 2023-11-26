from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer
from rest_framework import generics

class ProductListView(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'products'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'
    success_url = reverse_lazy('products:products')
    widgets = {
        'storage': forms.TextInput(attrs={'class': 'storage__input'})
    }

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('products:products')
    widgets = {
        'storage': forms.TextInput(attrs={'class': 'storage__input'})
    }

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:products')

class ProductAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
