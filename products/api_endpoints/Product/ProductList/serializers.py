from rest_framework import serializers

from products.models import Product, Category


class CategoryProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "slug"]


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "brand",
        ]

    def to_representation(self, instance):
        instance = {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            "brand": instance.brand.name,
            "slug": instance.slug,
            "is_active": instance.is_active,
            "category": CategoryProductListSerializer(instance.category).data,
        }

        return instance
