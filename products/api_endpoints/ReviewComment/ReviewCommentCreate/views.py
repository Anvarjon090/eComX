from rest_framework.generics import CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from products.models import Review, Comment
from products.api_endpoints.ReviewComment.ReviewCommentCreate.serializers import (
    ReviewCreateSerializer,
    CommentCreateSerializer,
)


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReviewCreateSerializer

    def create(self, request, args, kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if Review.objects.filter(
            user=self.request.user, product=serializer.validated_data["product"]
        ).exists():
            return Response(
                {"error": "You have already reviewed this product."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
