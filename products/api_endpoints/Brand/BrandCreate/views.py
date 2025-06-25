from rest_framework.generics import CreateAPIView
from rest_framework import permissions, parsers

from products.models import Brand
from products.api_endpoints.Brand.BrandCreate.serializers import BrandCreateSerializer


class BrandCreateAPIView(CreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
