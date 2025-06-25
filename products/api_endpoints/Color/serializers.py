from rest_framework import serializers
from products.models import Color


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "name", "slug"]
        read_only_fields = ["id"]
