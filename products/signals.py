import logging

from django.dispatch import receiver
from django.db.models.signals import post_save
from django_celery_beat.models import ClockedSchedule, PeriodicTask
from celery.schedules import timedelta

from products.models import Story
from products.constants import STORY_EXPIRE_HOURS

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Story)
def story_post_save(sender, instance, created, **kwargs):
    logger.debug("Signal is working")
    if created:
        expire_time = instance.created_at + timedelta(hours=STORY_EXPIRE_HOURS)
        args = [instance.id]
        logger.debug(f"args: {args}, expire_time: {expire_time}")

        clocked, created = ClockedSchedule.objects.get_or_create(
            clocked_time=expire_time,
        )

        task, created = PeriodicTask.objects.get_or_create(
            name=f"task_expire_story_{instance.id}",
            task="products.tasks.create_story_expirer_task",
            clocked=clocked,
            start_time=expire_time,
            one_off=True,
            args=args,
        )
