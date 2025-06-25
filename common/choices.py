from django.db.models import TextChoices


class OrderStatus(TextChoices):
    PENDING = "PENDING", "PENDING"
    DELIVERED = "DELIVERED", "DELIVERED"
    CANCELLED = "CANCELLED", "CANCELLED"
