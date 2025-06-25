from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    brand = models.ForeignKey(
        "products.Brand", on_delete=models.SET_NULL, null=True, blank=True
    )
    slug = models.SlugField(null=False, blank=False, unique=True)
    default_images = models.ManyToManyField("common.MediaFile", blank=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(
        "products.Category", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class ProductVariant(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.BigIntegerField(null=False, blank=False)
    product = models.ForeignKey(
        "products.Product", on_delete=models.SET_NULL, null=True, blank=True
    )
    images = models.ManyToManyField("common.MediaFile", blank=True)
    stock = models.IntegerField(default=0, null=False, blank=False)
    color = models.ForeignKey(
        "products.Color", on_delete=models.SET_NULL, null=True, blank=True
    )
    size = models.ForeignKey(
        "products.Size", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product.name} - {self.price}"

    class Meta:
        verbose_name = _("Product Variant")
        verbose_name_plural = _("Product Variants")


class Brand(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    logo = models.ImageField(upload_to="brands", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")


class Category(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to="categories", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


class Size(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")


class Color(BaseModel):
    name = models.CharField(max_length=255, null=False, blank=False)
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Color")
        verbose_name_plural = _("Colors")


class Review(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reviews",
    )
    rating = models.IntegerField(
        default=0,
        null=False,
        blank=False,
        validators=[MinValueValidator(0), MaxValueValidator(5)],
    )
    review = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Review({self.id})"

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")


class Comment(BaseModel):
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="comments",
    )
    text = models.TextField(max_length=500, null=False, blank=False)
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    def __str__(self):
        return f"Comment({self.id})"

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")


class Story(BaseModel):
    title = models.CharField(max_length=255, null=False, blank=False)
    image = models.ImageField(upload_to="stories", null=False, blank=False)
    product = models.ForeignKey(
        "products.Product", on_delete=models.SET_NULL, null=True, blank=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Story({self.title})"

    class Meta:
        verbose_name = _("Story")
        verbose_name_plural = _("Stories")
