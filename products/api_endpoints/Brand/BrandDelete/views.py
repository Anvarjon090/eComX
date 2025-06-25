from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Brand
from products.api_endpoints.Brand.BrandDelete.serializers import BrandDeleteSerializer


class BrandDeleteAPIView(DestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDeleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
