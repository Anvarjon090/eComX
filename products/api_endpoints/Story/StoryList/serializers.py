from rest_framework.serializers import ModelSerializer

from products.models import Story


class StoryListSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ["id", "title", "product", "image"]
        read_only_fields = ["id"]
