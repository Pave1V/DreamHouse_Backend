from django.db import models
from Apps.home.models import Home
from Apps.users.models import User

# Create your models here.

class Favourite(models.Model):
    home = models.ForeignKey(
        Home, on_delete = models.CASCADE, db_index = True
    )
    user = models.ForeignKey(
        User, on_delete = models.CASCADE, db_index = True
    )
    created_at = models.DateTimeField(
        "Created at", blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        "Updated at", blank=True, auto_now=True
    )
