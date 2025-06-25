from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from products.models import Category
from products.api_endpoints.Category.CategoryList.serializers import (
    CategoryListSerializer,
)


class CategoryListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []

    def get(self, request, *args, **kwargs):
        print("[INFO][CategoryListAPIView]", request, args, kwargs)
        serializer = self.serializer_class(self.get_queryset(), many=True)

        return Response(serializer.data)


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    permission_classes = []
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        print("[INFO][CategoryRetrieveAPIView]", request, args, kwargs)

        serializer = self.serializer_class(self.get_object())

        return Response(serializer.data)
