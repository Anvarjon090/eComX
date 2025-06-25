from rest_framework.generics import (
    GenericAPIView,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.api_endpoints.Product.ProductList.serializers import ProductListSerializer


class ProductListAPIView(GenericAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True)
        return queryset


class ProductRetrieveAPIView(GenericAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "slug"

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object())

        return Response(serializer.data)


__all__ = [
    "ProductListAPIView",
    "ProductRetrieveAPIView",
]
