from django.contrib import admin

from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'vendor')
    list_filter = ('vendor',)
    search_fields = ('name', 'vendor__username')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
