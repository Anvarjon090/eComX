from rest_framework.generics import CreateAPIView
from rest_framework import permissions, parsers

from products.models import Story
from products.api_endpoints.Story.StoryCreate.serializers import StoryCreateSerializer


class StoryCreateAPIView(CreateAPIView):
    queryset = Story.objects.all()
    serializer_class = StoryCreateSerializer
    permission_classes = [permissions.IsAdminUser]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
