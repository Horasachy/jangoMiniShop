from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    preview_image = models.ImageField(upload_to='product', default='photo')
    description = models.CharField(max_length=1000)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="photos")
    image = models.ImageField(upload_to='product', default='photo')
