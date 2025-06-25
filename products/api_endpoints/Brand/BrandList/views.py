from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from products.models import Brand
from products.api_endpoints.Brand.BrandList.serializers import BrandListSerializer


class BrandListAPIView(ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = [permissions.IsAuthenticated]


class BrandRetrieveAPIView(RetrieveAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "slug"
