from celery import shared_task

from products.models import Story


@shared_task
def create_story_expirer_task(story_id: int):
    try:
        story = Story.objects.get(id=story_id)
        story.is_active = False
        story.save()
    except Story.DoesNotExist:
        return f"Story with id {story_id} does not exist."
