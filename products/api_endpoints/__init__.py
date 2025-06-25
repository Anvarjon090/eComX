from .Brand import (
    BrandCreateAPIView,
    BrandListAPIView,
    BrandUpdateAPIView,
    BrandDeleteAPIView,
    BrandRetrieveAPIView,
)
from .Category import (
    CategoryListAPIView,
    CategoryCreateAPIView,
    CategoryUpdateAPIView,
    CategoryDeleteAPIView,
    CategoryRetrieveAPIView,
)
from .Product import (
    ProductCreateAPIView,
    ProductListAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,
    ProductRetrieveAPIView,
)
from .Size import SizeListCreateView, SizeRetrieveUpdateDestroyView
from .Color import ColorListCreateView, ColorRetrieveUpdateDestroyView
from .ReviewComment import (
    ReviewCreateAPIView,
    UserReviewsListAPIView,
    ReviewDeleteAPIView,
    CommentCreateAPIView,
    UserCommentsListAPIView,
    CommentDeleteAPIView,
)
from .Story import (
    StoryCreateAPIView,
    StoryListAPIView,
    StoryRetrieveAPIView,
    StoryUpdateAPIView,
    StoryDeleteAPIView,
)

__all__ = [
    "BrandCreateAPIView",
    "BrandListAPIView",
    "BrandUpdateAPIView",
    "BrandDeleteAPIView",
    "BrandRetrieveAPIView",
    "CategoryListAPIView",
    "CategoryCreateAPIView",
    "CategoryUpdateAPIView",
    "CategoryDeleteAPIView",
    "CategoryRetrieveAPIView",
    "ProductCreateAPIView",
    "ProductListAPIView",
    "ProductUpdateAPIView",
    "ProductDeleteAPIView",
    "ProductRetrieveAPIView",
    "SizeListCreateView",
    "SizeRetrieveUpdateDestroyView",
    "ColorListCreateView",
    "ColorRetrieveUpdateDestroyView",
    "ReviewCreateAPIView",
    "UserReviewsListAPIView",
    "ReviewDeleteAPIView",
    "CommentCreateAPIView",
    "UserCommentsListAPIView",
    "CommentDeleteAPIView",
    "StoryCreateAPIView",
    "StoryListAPIView",
    "StoryRetrieveAPIView",
    "StoryUpdateAPIView",
    "StoryDeleteAPIView",
]
