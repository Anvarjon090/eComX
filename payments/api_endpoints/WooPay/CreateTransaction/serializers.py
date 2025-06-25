from rest_framework import serializers

from payments.models import Transaction
from payments.choices import TransactionStatus


class WooPayCreateTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "order",
            "user",
            "remote_id",
            "amount",
        ]
        read_only_fields = ["id", "user", "remote_id"]

    def validate(self, attrs):
        print(attrs, self.context)
        user = self.context["user"]
        order = attrs["order"]
        amount = attrs["amount"]

        existing_transaction = Transaction.objects.filter(order=order)

        if user != order.user:
            raise serializers.ValidationError("You can't pay for someone else's order.")
        if amount <= 1000 * 100:
            raise serializers.ValidationError("Amount must be greater than 1000.")
        if amount != order.total_price:
            raise serializers.ValidationError(
                "Amount must be equal to order total price."
            )
        if existing_transaction.exists():
            raise serializers.ValidationError(
                "You can't create multiple transactions for a single Order."
            )

        # TODO: change this
        # User can pay multiple times to get the order.
        # Anyway you have to check for the paid bill amount to the order total price,
        # but allow to pay multiple times
        return attrs

    def create(self, validated_data):
        new_transaction = Transaction.objects.create(
            order=validated_data["order"],
            user=self.context["user"],
            remote_id="-",
            amount=validated_data["amount"],
            status=TransactionStatus.PENDING,
        )
        return new_transaction
