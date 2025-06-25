from rest_framework import serializers

from products.models import Brand


class BrandCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name", "slug"]
