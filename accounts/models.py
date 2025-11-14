from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER_TYPES = (
    ('customer', 'Customer'),
    ('vendor', 'Vendor'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='customer')
    phone = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100)


    def __str__(self):
        return self.username


    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


