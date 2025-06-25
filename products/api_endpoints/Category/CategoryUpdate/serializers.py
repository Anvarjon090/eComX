from rest_framework import serializers

from products.models import Category


class CategoryUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug"]
