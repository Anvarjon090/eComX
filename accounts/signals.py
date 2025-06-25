from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cart, User

import logging

logger = logging.getLogger(__name__)


@receiver(post_save, sender=User)
def create_cart(sender, instance, created, **kwargs):
    logger.debug("Signal is working")
    if created:
        Cart.objects.create(user=instance)
