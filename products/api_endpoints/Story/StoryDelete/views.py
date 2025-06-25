from rest_framework.generics import DestroyAPIView
from rest_framework import permissions

from products.models import Story


class StoryDeleteAPIView(DestroyAPIView):
    queryset = Story.objects.filter(is_active=True)
    permission_classes = [permissions.IsAdminUser]
