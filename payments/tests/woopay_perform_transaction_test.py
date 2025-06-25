import pytest

from payments.api_endpoints.WooPay.PerformTransaction.services import (
    handle_perform_transaction,
)
from payments.choices import TransactionStatus


@pytest.mark.django_db
class TestHandlePerformTransaction:
    def test_success(self):
        validated_data = {
            "order_id": 1,
            "remote_id": "123",
            "status": TransactionStatus.SUCCESS,
        }

        detail_message = handle_perform_transaction(validated_data)

        assert detail_message == "Transaction has been completed successfully."

    def test_failed(self):
        validated_data = {
            "order_id": 1,
            "remote_id": "123",
            "status": TransactionStatus.FAILED,
        }

        detail_message = handle_perform_transaction(validated_data)

        assert detail_message == "Transaction has been failed."
