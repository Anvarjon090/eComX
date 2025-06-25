from rest_framework.generics import GenericAPIView
from rest_framework import permissions
from rest_framework.response import Response

from accounts.api_endpoints.CartItemCreate.serializers import CartItemCreateSerializer
from accounts.models import CartItem


class CartItemsCreateAPIView(GenericAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


__all__ = ["CartItemsCreateAPIView"]
