from django.db.models import TextChoices


class CheckoutSourceChoices(TextChoices):
    CART = "cart", "Cart"
    PRODUCT = "product", "Product"
