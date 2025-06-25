from django.urls import path

from products.api_endpoints import (
    ProductListAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
    ProductRetrieveAPIView,
    ProductDeleteAPIView,
    BrandListAPIView,
    BrandUpdateAPIView,
    BrandCreateAPIView,
    BrandDeleteAPIView,
    BrandRetrieveAPIView,
    SizeListCreateView,
    SizeRetrieveUpdateDestroyView,
    ColorListCreateView,
    ColorRetrieveUpdateDestroyView,
    CategoryListAPIView,
    CategoryRetrieveAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,
    ReviewCreateAPIView,
    ReviewDeleteAPIView,
    CommentCreateAPIView,
    CommentDeleteAPIView,
    StoryListAPIView,
    StoryRetrieveAPIView,
    StoryCreateAPIView,
    StoryUpdateAPIView,
    StoryDeleteAPIView,
)


urlpatterns = [
    # products
    path("", ProductListAPIView.as_view(), name="product-list"),
    path("create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("<str:slug>/", ProductRetrieveAPIView.as_view(), name="product-retrieve"),
    path("<str:slug>/update/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("<str:slug>/delete/", ProductDeleteAPIView.as_view(), name="product-delete"),
    # brands
    path("brands/", BrandListAPIView.as_view(), name="brand-list"),
    path("brands/create/", BrandCreateAPIView.as_view(), name="brand-create"),
    path("brands/<str:slug>/", BrandRetrieveAPIView.as_view(), name="brand-retrieve"),
    path(
        "brands/<str:slug>/update/", BrandUpdateAPIView.as_view(), name="brand-update"
    ),
    path(
        "brands/<str:slug>/delete/", BrandDeleteAPIView.as_view(), name="brand-delete"
    ),
    # sizes
    path("sizes/", SizeListCreateView.as_view(), name="size-list-create"),
    path(
        "sizes/<int:pk>/", SizeRetrieveUpdateDestroyView.as_view(), name="size-detail"
    ),
    # colors
    path("colors/", ColorListCreateView.as_view(), name="color-list-create"),
    path(
        "colors/<int:pk>/",
        ColorRetrieveUpdateDestroyView.as_view(),
        name="color-detail",
    ),
    # categories
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("categories/create/", CategoryCreateAPIView.as_view(), name="category-create"),
    path(
        "categories/<str:slug>/",
        CategoryRetrieveAPIView.as_view(),
        name="category-retrieve",
    ),
    path(
        "categories/<str:slug>/update/",
        CategoryUpdateAPIView.as_view(),
        name="category-update",
    ),
    path(
        "categories/<str:slug>/delete/",
        CategoryDeleteAPIView.as_view(),
        name="category-delete",
    ),
    # reviews and comments
    path("reviews/create/", ReviewCreateAPIView.as_view(), name="review-create"),
    path(
        "reviews/delete/<int:id>/", ReviewDeleteAPIView.as_view(), name="review-delete"
    ),
    path("comments/create/", CommentCreateAPIView.as_view(), name="comment-create"),
    path(
        "comments/delete/<int:id>/",
        CommentDeleteAPIView.as_view(),
        name="comment-delete",
    ),
    # stories
    path("stories/", StoryListAPIView.as_view(), name="story-list"),
    path("stories/create/", StoryCreateAPIView.as_view(), name="story-create"),
    path("stories/<str:slug>/", StoryRetrieveAPIView.as_view(), name="story-retrieve"),
    path(
        "stories/<str:slug>/update/",
        StoryUpdateAPIView.as_view(),
        name="story-update",
    ),
    path(
        "stories/<str:slug>/delete/",
        StoryDeleteAPIView.as_view(),
        name="story-delete",
    ),
]
