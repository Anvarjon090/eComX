from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

from accounts.tokens import (
    generate_email_confirm_token,
    verify_email_confirm_token,
    generate_temporary_password,
)
from accounts.email_send import send_email
from accounts.api_endpoints.Register.serializers import (
    RegisterInputSerializer,
    ConfirmTokenSerializer,
)


User = get_user_model()


class RegisterUserAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=RegisterInputSerializer)
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response(
                {"detail": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        existing = User.objects.filter(email=email, is_active=True).first()
        if existing:
            if not existing.is_confirmed:
                token = generate_email_confirm_token(existing)
                new_pass = generate_temporary_password()
                existing.set_password(new_pass)
                existing.save()

                send_email(
                    subject="Reset your password",
                    intro_text="Click the link below to reset your password.",
                    email=email,
                    token=token,
                    template="email/reset_password_email.html",
                    password=new_pass,
                )

                return Response(
                    {
                        "detail": "User already exists but not confirmed yet. Confirmation email sent."
                    },
                    status=status.HTTP_200_OK,
                )

            return Response(
                {"detail": "This email is already registered."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects._create_user(
            email=email, password=password, is_confirmed=False
        )
        token = generate_email_confirm_token(user)

        send_email(
            subject="Reset your password",
            intro_text="Click the link below to reset your password.",
            email=email,
            token=token,
            template="email/reset_password_email.html",
        )

        return Response(
            {"detail": "User created. Confirmation email sent."},
            status=status.HTTP_201_CREATED,
        )


class RegisterConfirmAPIView(APIView):
    permission_classes = []

    @swagger_auto_schema(request_body=ConfirmTokenSerializer)
    def post(self, request):
        token = request.data.get("token")

        if not token:
            return Response(
                {"detail": "Token is required."}, status=status.HTTP_400_BAD_REQUEST
            )

        user_id = verify_email_confirm_token(token)

        if not user_id:
            return Response(
                {"detail": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )

        if user.is_confirmed:
            return Response(
                {"detail": "Email already confirmed."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.is_confirmed = True
        user.save()

        return Response(
            {"detail": "Email successfully confirmed."}, status=status.HTTP_200_OK
        )
