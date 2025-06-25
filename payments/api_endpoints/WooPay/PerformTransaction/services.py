from payments.models import Transaction
from payments.choices import TransactionStatus
from orders.models import Order


def handle_perform_transaction(validated_data: dict) -> str:
    try:
        order = Order.objects.get(id=validated_data["order_id"])
    except Order.DoesNotExist:
        return None

    if validated_data["status"] == TransactionStatus.SUCCESS:
        transaction = Transaction.objects.get(order=order)
        transaction.remote_id = validated_data["remote_id"]
        transaction.status = validated_data["status"]
        transaction.save()

        return "Transaction has been completed successfully."
    else:
        transaction = Transaction.objects.get(order=order)
        transaction.remote_id = validated_data["remote_id"]
        transaction.status = validated_data["status"]
        transaction.save()

        return "Transaction has been failed."
