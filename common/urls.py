from django.urls import path

from accounts import views
from common.views import (
    CheckoutView,
    HomeView,
    ContactView,
    BlogView,
    BlogDetailView,
    ShopDetailsView,
    ShopGridView,
    ShoppingCartView,
)
from common.api_endpoints import MediaFileCreateAPIView, MediaFileDestroyAPIView

app_name = "common"

urlpatterns = [
    path("media/upload/", MediaFileCreateAPIView.as_view(), name="media-upload"),
    path(
        "media/delete/<int:id>/", MediaFileDestroyAPIView.as_view(), name="media-delete"
    ),
    # templates
    path('index/', HomeView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('shop-grid/', ShopGridView.as_view(), name='shop_grid'),
    path('blog-details/', BlogDetailView.as_view(), name='blog_details'),
    path('shopping-cart/', ShoppingCartView.as_view(), name='shopping_cart'),
    path('shop-details/', ShopDetailsView.as_view(), name='shop_details'),
]