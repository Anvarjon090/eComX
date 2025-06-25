from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "phone_number", "avatar", "bio"]
        read_only_fields = ["id"]
