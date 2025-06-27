from django.urls import path

from accounts import views
from accounts.api_endpoints import (
    RegisterUserAPIView,
    RegisterConfirmAPIView,
    SessionLoginAPIView,
    SessionLogoutAPIView,
    CartItemsListAPIView,
    CartItemsCreateAPIView,
    CartItemsUpdateAPIView,
    CartItemsDeleteAPIView,
    ProfileUpdateAPIView,
    ProfileDeleteAPIView,
    PasswordResetRequestAPIView,
    PasswordResetConfirmAPIView,
    SavedProductsListAPIView,
    SaveProductAPIView,
)
from products.api_endpoints import UserReviewsListAPIView
from accounts.template_views import RegisterView, LoginView, ProfileView


app_name = 'accounts' 

apis = [
    path("register/", RegisterUserAPIView.as_view(), name="register"),
    path(
        "register/confirm/", RegisterConfirmAPIView.as_view(), name="register-confirm"
    ),
    path("login/", SessionLoginAPIView.as_view(), name="login-session"),
    path("logout/", SessionLogoutAPIView.as_view(), name="logout-session"),
    path("cart/", CartItemsListAPIView.as_view(), name="cart-items"),
    path(
        "cart/cartitems/create/",
        CartItemsCreateAPIView.as_view(),
        name="cart-items-create",
    ),
    path(
        "cart/cartitems/<int:pk>/update/",
        CartItemsUpdateAPIView.as_view(),
        name="cart-items-update",
    ),
    path(
        "cart/cartitems/<int:pk>/delete/",
        CartItemsDeleteAPIView.as_view(),
        name="cart-items-delete",
    ),
    # reviews and comments list
    path("profile/reviews/", UserReviewsListAPIView.as_view(), name="user-reviews"),
    # path("profile/comments/", UserCommentsListAPIView.as_view(), name="user-comments"),
    path(
        "products/save-unsave/",
        SaveProductAPIView.as_view(),
        name="save-unsave-products",
    ),
    path("products/saved/", SavedProductsListAPIView.as_view(), name="saved-products"),
    # profile
    path("profile/update/", ProfileUpdateAPIView.as_view(), name="profile-update"),
    path("profile/delete/", ProfileDeleteAPIView.as_view(), name="profile-delete"),
    path(
        "password-reset/request/",
        PasswordResetRequestAPIView.as_view(),
        name="password-reset",
    ),
    path(
        "password-reset/confirm/",
        PasswordResetConfirmAPIView.as_view(),
        name="password-reset-confirm",
    ),
]

template_urls = [
    path("profile/update/", views.update_profile, name="profile-update"),
    path("template/register/", RegisterView.as_view(), name="register-template"),
    path("template/login/", LoginView.as_view(), name="login-template"),
    path("template/profile/", ProfileView.as_view(), name="profile-template"),
    # path("template/reset-password/", PasswordResetView.as_view(), name="reset-password-template"),
    path('profile/', views.profile_view, name='profile'),
    path('login/', views.login_view, name='login-session'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register-session'),
]

urlpatterns = apis + template_urls
