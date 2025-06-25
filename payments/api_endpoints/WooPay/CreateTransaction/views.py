from rest_framework.generics import CreateAPIView
from rest_framework import permissions

from payments.models import Transaction
from payments.api_endpoints.WooPay.CreateTransaction.serializers import (
    WooPayCreateTransactionSerializer,
)


class WooPayCreateTransactionAPIView(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = WooPayCreateTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context
