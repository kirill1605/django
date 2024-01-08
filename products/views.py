from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from .models import Product
from .forms import ProductForm
from .serializers import ProductSerializer
from rest_framework import generics
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action


class ProductListView(ListView):
    model = Product
    template_name = "products/products.html"
    context_object_name = "products"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_create.html"
    success_url = reverse_lazy("products:products")
    widgets = {"storage": forms.TextInput(attrs={"class": "storage__input"})}


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/product_update.html"
    success_url = reverse_lazy("products:products")
    widgets = {"storage": forms.TextInput(attrs={"class": "storage__input"})}


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "products/product_delete.html"
    success_url = reverse_lazy("products:products")


class ProductAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = [
        "price"
    ]
    search_fields = [
        "name",
        "description",
    ]
    ordering_fields = [
        'price'
    ]

    def get_queryset(self):
        user = self.request.user

        queryset = Product.objects.filter(user=user)

        queryset = queryset.filter(Q(price__gt=10000) | (Q(name__startswith = 'П') | ~ Q(name__startswith = 'С')))

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False, methods=["GET"])
    def get_most_expensive_products(self, request):
        most_expensive_products = self.get_queryset().order_by("-price")[:10]
        serialized_products = ProductSerializer(most_expensive_products, many=True)
        return Response(data=serialized_products.data)

    @action(detail=True, methods=["POST"])
    def update_price(self, request, pk):
        product = self.get_object()
        new_price = request.data.get("price")

        if new_price is not None:
            product.price = new_price
            product.save()

            serialized_product = ProductSerializer(product)
            return Response(data=serialized_product.data)
        else:
            return Response(data={"error": "Price is required"}, status=400)