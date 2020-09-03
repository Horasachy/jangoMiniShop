from django.contrib.auth.models import User
from django.db import models

from products.models import Product


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users")
    quantity = models.IntegerField()

    def price_total(self):
        return self.product.price * self.quantity


