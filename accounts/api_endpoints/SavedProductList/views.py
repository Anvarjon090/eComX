from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from accounts.api_endpoints.SavedProductList.serializers import (
    SavedProductsListSerializer,
)


class SavedProductsListAPIView(ListAPIView):
    serializer_class = SavedProductsListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.saved_products.all()
