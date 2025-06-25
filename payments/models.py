from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel
from payments.choices import TransactionStatus


class Transaction(BaseModel):
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="transactions"
    )
    user = models.ForeignKey(
        "accounts.User", on_delete=models.SET_NULL, null=True, blank=True
    )
    remote_id = models.CharField(max_length=255, null=False, blank=False)
    amount = models.BigIntegerField(null=False, blank=False)
    status = models.CharField(
        choices=TransactionStatus.choices, null=False, blank=False
    )

    def __str__(self):
        return f"Transaction<user={self.user.email}, order={self.order}>"

    class Meta:
        verbose_name = _("Transaction")
        verbose_name_plural = _("Transactions")
