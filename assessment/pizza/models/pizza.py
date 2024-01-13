from django.db import models


class PizzaBase(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Cheese(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    pizza_base = models.ForeignKey(PizzaBase, on_delete=models.CASCADE)
    cheese = models.ForeignKey(
        Cheese, null=True, blank=True, on_delete=models.CASCADE)
    toppings = models.ManyToManyField(Topping)
    price = models.IntegerField(default=500)
