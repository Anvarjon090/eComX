from rest_framework.generics import GenericAPIView
from rest_framework import permissions

from accounts.models import CartItem
from accounts.api_endpoints.CartItemUpdate.serializers import CartItemUpdateSerializer


class CartItemsUpdateAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


__all__ = ["CartItemsUpdateAPIView"]
