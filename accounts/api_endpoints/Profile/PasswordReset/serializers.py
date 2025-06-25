from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from accounts.tokens import generate_email_confirm_token, verify_email_confirm_token

User = get_user_model()


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value, is_active=True)
        except User.DoesNotExist:
            raise serializers.ValidationError("No active user found with this email.")
        return value

    def save(self):
        token = generate_email_confirm_token(self.user)
        send_email_task = self.context["send_email"]
        send_email_task.delay(
            subject="Reset your password",
            intro_text="Click the link below to reset your password.",
            email=self.validated_data["email"],
            token=token,
            template="email/reset_password_email.html",
        )


class PasswordResetConfirmSerializer(serializers.Serializer):
    token = serializers.CharField()
    new_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user_id = verify_email_confirm_token(attrs["token"])
        if not user_id:
            raise serializers.ValidationError("Invalid or expired token.")
        self.user = User.objects.get(pk=user_id)
        validate_password(attrs["new_password"], self.user)
        return attrs

    def save(self):
        self.user.set_password(self.validated_data["new_password"])
        self.user.save()
