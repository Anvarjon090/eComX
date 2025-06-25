from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAdminUser

from products.models import Review, Comment


class ReviewDeleteAPIView(DestroyAPIView):
    queryset = Review.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = "id"


class CommentDeleteAPIView(DestroyAPIView):
    queryset = Comment.objects.all()
    permission_classes = [IsAdminUser]
    lookup_field = "id"
