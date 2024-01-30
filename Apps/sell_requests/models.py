from django.db import models
from Apps.users.models import User

# Create your models here.


class SellRequest(models.Model):
    class Meta(object):
        db_table = 'sell_request'
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, db_index=True
    )
    address = models.CharField(
        "Address", blank=False, null=False, db_index=True, max_length=100, default='address'
    )
    sqft = models.CharField(
        "SQFT", blank=False, null=False, db_index=True, max_length=20, default='SQFT'
    )
    age_building = models.IntegerField(
        "Age Building", blank=False, null=False, db_index=True
    )
    created_at = models.DateTimeField(
        "Created at", blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Updated at", blank=True, auto_now=True
    )
