from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions

from products.models import Story
from products.api_endpoints.Story.StoryList.serializers import StoryListSerializer


class StoryListAPIView(ListAPIView):
    queryset = Story.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = StoryListSerializer
    permission_classes = [permissions.IsAuthenticated]


class StoryRetrieveAPIView(RetrieveAPIView):
    queryset = Story.objects.filter(is_active=True).order_by("-created_at")
    serializer_class = StoryListSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "id"
