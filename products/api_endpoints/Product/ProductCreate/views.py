from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import permissions

from products.models import Product
from products.api_endpoints.Product.ProductCreate.serializers import (
    ProductCreateSerializer,
)


class ProductCreateAPIView(GenericAPIView, CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductCreateSerializer
    permission_classes = [permissions.IsAdminUser]


__all__ = ["ProductCreateAPIView"]
