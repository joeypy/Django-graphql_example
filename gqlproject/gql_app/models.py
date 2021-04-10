from django.db import models


# Create your models here.
class ProductModel(models.Model):
    segment = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    units = models.IntegerField()
    sales = models.IntegerField()
    date_sold = models.CharField(max_length=100)

    def __str__(self):
        return self.product
