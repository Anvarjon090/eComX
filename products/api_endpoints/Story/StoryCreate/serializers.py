from rest_framework.serializers import ModelSerializer

from products.models import Story


class StoryCreateSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ["title", "product", "image"]
