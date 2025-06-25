from django.urls import path

from payments.api_endpoints.WooPay import (
    WooPayCreateTransactionAPIView,
    WooPayPerformTransactionAPIView,
)

urlpatterns = [
    path(
        "CreateTransaction/",
        WooPayCreateTransactionAPIView.as_view(),
        name="WooPayCreateTransaction",
    ),
    path(
        "PerformTransaction/",
        WooPayPerformTransactionAPIView.as_view(),
        name="WooPayPerformTransaction",
    ),
]
