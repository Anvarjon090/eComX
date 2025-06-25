from rest_framework.serializers import ModelSerializer

from products.models import Review, Comment


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "product",
            "rating",
            "review",
        ]
        read_only_fields = ["id"]


class CommentCreateSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            "id",
            "product",
            "text",
            "parent",
        ]
        read_only_fields = ["id"]
