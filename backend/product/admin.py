from django.contrib import admin

from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    resource_class = models.Product

    list_display = ('id', 'name', 'desc', 'price')