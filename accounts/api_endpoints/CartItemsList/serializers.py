from rest_framework import serializers

from products.models import ProductVariant


class CartItemProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductVariant
        fields = ["id", "name", "price"]


class CartItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    product = CartItemProductVariantSerializer()
    quantity = serializers.IntegerField()
