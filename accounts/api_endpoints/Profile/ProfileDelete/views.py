from rest_framework.generics import DestroyAPIView
from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class ProfileDeleteAPIView(DestroyAPIView):
    queryset = User.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
