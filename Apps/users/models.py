from django.db import models

# Create your models here.


class User(models.Model):
    class Meta(object):
        db_table = "user"
    user_name = models.CharField(
        "user name", blank=False, null=False, max_length=100, db_index=True)
    password = models.CharField(
        "password", blank=False, null=False, max_length=5000, db_index=True)
    email = models.EmailField("email", blank=False,
                              null=False, max_length=5000, db_index=True)
    token = models.CharField(
        "token", blank=True, null=True, max_length=100, db_index=True)
    token_expires = models.DateTimeField(
        "Token expires date/time: ", blank=True, null=True)
    created_at = models.DateTimeField(
        "Created date/time: ", blank=True, auto_now_add=True)
    updated_at = models.DateTimeField(
        "Updated date/time: ", blank=True, auto_now=True)
