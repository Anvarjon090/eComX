from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response

from accounts.api_endpoints.CartItemsList.serializers import CartItemSerializer
from accounts.models import CartItem


class CartItemsListAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.cart)

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(serializer.data)


__all__ = ["CartItemsListAPIView"]
