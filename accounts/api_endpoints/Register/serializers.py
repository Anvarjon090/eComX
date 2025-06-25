from rest_framework import serializers


class RegisterInputSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class ConfirmTokenSerializer(serializers.Serializer):
    token = serializers.CharField()
