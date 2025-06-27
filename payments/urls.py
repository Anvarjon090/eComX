from django.urls import include, path
from . import views

urlpatterns = [
    path("checkout/", views.create_checkout_session, name="checkout-session"),
    path("woopay/", include("payments.api_endpoints.WooPay.urls")),
]