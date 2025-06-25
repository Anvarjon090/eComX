from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class MediaFile(BaseModel):
    file = models.FileField(upload_to="files")

    def __str__(self):
        return self.file.name

    class Meta:
        verbose_name = _("Media File")
        verbose_name_plural = _("Media Files")
