from django.db import models
from cloudinary.models import CloudinaryField
from Apps.tags.models import Tag

# Create your models here.


class Home(models.Model):
    class Meta(object):
        db_table = 'home'
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE, db_index=True
    )
    price = models.IntegerField(
        "Price", blank=False, db_index=True
    )
    rent_price = models.IntegerField(
        "Rent price", blank=False, db_index=True
    )
    main_image = CloudinaryField(
        "Main image", blank=True, null=True
    )
    sub_image1 = CloudinaryField(
        "Sub image 1", blank=True, null=True
    )
    sub_image2 = CloudinaryField(
        "Sub image 2", blank=True, null=True
    )
    sub_image3 = CloudinaryField(
        "Sub image 3", blank=True, null=True
    )
    sub_image4 = CloudinaryField(
        "Sub image 4", blank=True, null=True
    )
    state = models.CharField(
        "State", blank=False, null=False, db_index=True, max_length=50, default="State"
    )
    address = models.CharField(
        "Address", blank=False, null=False, db_index=True, max_length=50, default="Address"
    )
    layout = models.CharField(
        "Layout", blank=False, null=False, db_index=True, max_length=50, default="2,231 sqft"
    )
    created_at = models.DateTimeField(
        "Created at", blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Updated at", blank=True, auto_now=True
    )
