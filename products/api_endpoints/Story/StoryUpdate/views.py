from rest_framework.generics import UpdateAPIView
from rest_framework import permissions

from products.models import Story
from products.api_endpoints.Story.StoryUpdate.serializers import StoryUpdateSerializer


class StoryUpdateAPIView(UpdateAPIView):
    queryset = Story.objects.filter(is_active=True)
    serializer_class = StoryUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
