from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions

from payments.models import Transaction
from payments.api_endpoints.WooPay.PerformTransaction.serializers import (
    WooPayPerformTransactionSerializer,
)
from payments.api_endpoints.WooPay.PerformTransaction.services import (
    handle_perform_transaction,
)


class WooPayPerformTransactionAPIView(GenericAPIView):
    queryset = Transaction.objects.all()
    serializer_class = WooPayPerformTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        detail_message = handle_perform_transaction(serializer.validated_data)

        if not detail_message:
            return Response(
                {"detail": "You can't perform a transaction for non-existent order."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({"detail": detail_message}, status=status.HTTP_200_OK)
