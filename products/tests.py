from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()


class ProductListAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("product-list")

        self.user = User.objects._create_user(
            email="testuser@gmail.com", password="testpass123"
        )

        # Generate token and authenticate
        token = AccessToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_authenticated_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
