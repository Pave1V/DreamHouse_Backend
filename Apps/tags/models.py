from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

# name, image, description, created_at, updated_at


class Tag(models.Model):
    class Meta(object):
        db_table = "tag"
    name = models.CharField("name", blank=False,
                            null=False, max_length=100, db_index=True)
    image = CloudinaryField("image", blank=True, null=True)
    description = models.TextField("description", max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField("type", blank=False, null=True,
                            max_length=50, db_index=True)

    def __str__(self):
        return self.name
