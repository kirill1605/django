from rest_framework import serializers, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "description", "price")

    def validate_name(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Название должно быть более 5 символов.")
        return value

    def validate_description(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Описание должно быть более 10 символов.")
        return value

    def validate_price(self, value):
        if value is None:
            raise serializers.ValidationError("Введите цену")
        return value

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
