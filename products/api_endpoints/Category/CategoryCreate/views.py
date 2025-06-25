from rest_framework.generics import CreateAPIView

from products.models import Category
from products.api_endpoints.Category.CategoryCreate.serializers import (
    CategoryCreateSerializer,
)


class CategoryCreateAPIView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    def post(self, request, *args, **kwargs):
        print(request, args, kwargs)
        return super().post(request, *args, **kwargs)
