from django.urls import path, include


urlpatterns = [
    path("woopay/", include("payments.api_endpoints.WooPay.urls")),
]
