from rest_framework.generics import UpdateAPIView

from products.models import Category
from products.api_endpoints.Category.CategoryUpdate.serializers import (
    CategoryUpdateSerializer,
)


class CategoryUpdateAPIView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryUpdateSerializer
