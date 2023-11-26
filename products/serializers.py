from rest_framework import serializers
from rest_framework import viewsets
from django.db.models import Q
from .models import Product
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "price")


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(
        Q(price__gt=10000)
        | Q(name__startswith="С")
    )

    @action(methods=["GET"], detail=False)
    def get_most_expensive_products(self, request):
        most_expensive_products = self.get_queryset().order_by("-price")[:10]

        serialized_products = ProductSerializer(most_expensive_products, many=True)

        return Response(serialized_data=serialized_products.data)

    @action(methods=["POST"], detail=True)
    def update_price(self, request, pk):
        product = self.get_object()
        new_price = request.data["price"]

        product.price = new_price
        product.save()

        serialized_product = ProductSerializer(product)
        return Response(serialized_data=serialized_product.data)