from django.core.exceptions import ValidationError
from django.db import models


class Product(models.Model):
    vendor = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ('available', 'Available'),
        ('out_of_stock', 'Out of Stock'),
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='media/products/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    #  Validate a vendor to be of type vendor
    def clean(self):
        if not self.vendor.user_type == 'vendor':
            raise ValidationError('Vendor must be a vendor')


