from django.db import models
from pizza.models import Pizza
from pizza.constants import OrderStatusConstant


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    total_bill = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20,
        default=OrderStatusConstant.placed)
    created_at = models.DateTimeField(auto_now=True)
