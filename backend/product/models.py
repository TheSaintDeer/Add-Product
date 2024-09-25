from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):

    name = models.CharField(
        max_length=255
    )
    desc = models.TextField()
    price = models.FloatField(
        validators=[MinValueValidator(0.0)]
    )