from rest_framework.generics import ListAPIView
from rest_framework import permissions

from products.models import Review, Comment
from products.api_endpoints.ReviewComment.ReviewCommentList.serializers import (
    UserReviewsListSerializer,
    UserCommentsListSerializer,
)


class UserReviewsListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserReviewsListSerializer

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user).order_by("created_at")


class UserCommentsListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserCommentsListSerializer

    def get_queryset(self):
        return Comment.objects.filter(user=self.request.user).order_by("created_at")
