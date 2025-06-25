from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Category
from products.api_endpoints.Category.CategoryDelete.serializers import (
    CategoryDeleteSerializer,
)


class CategoryDeleteAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
