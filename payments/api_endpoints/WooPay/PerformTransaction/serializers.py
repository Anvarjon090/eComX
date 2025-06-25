from rest_framework import serializers

from payments.choices import TransactionStatus


class WooPayPerformTransactionSerializer(serializers.Serializer):
    order_id = serializers.IntegerField(required=True)
    remote_id = serializers.CharField(required=True)
    status = serializers.ChoiceField(choices=TransactionStatus.choices, required=True)
