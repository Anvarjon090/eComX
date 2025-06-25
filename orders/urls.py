from django.urls import path

from orders.api_endpoints import CheckoutAPIView


urlpatterns = [
    path("checkout/", CheckoutAPIView.as_view(), name="checkout"),
]
