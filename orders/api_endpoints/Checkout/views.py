from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from orders.api_endpoints.Checkout.serializers import CheckoutSerializer


class CheckoutAPIView(CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CheckoutSerializer

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
