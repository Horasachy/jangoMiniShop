from django.db import models
from products.models import Product


class TelegramOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    username = models.CharField(max_length=1000)




