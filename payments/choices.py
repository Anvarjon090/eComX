from django.db.models import TextChoices


class TransactionStatus(TextChoices):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
