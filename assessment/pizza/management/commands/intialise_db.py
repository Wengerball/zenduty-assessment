from django.core.management.base import BaseCommand
from pizza.models import PizzaBase, Cheese, Topping
from pizza.constants import PizzaBaseConstant, CheeseConstant, ToppingConstant


class Command(BaseCommand):
    help = 'Initializes the database with PizzaBase, Cheese, and Topping data'

    def handle(self, *args, **kwargs):
        for base_name, _ in PizzaBaseConstant.choices:
            PizzaBase.objects.get_or_create(name=base_name)

        for cheese_name, _ in CheeseConstant.choices:
            Cheese.objects.get_or_create(name=cheese_name)

        for topping_name, _ in ToppingConstant.choices:
            Topping.objects.get_or_create(name=topping_name)

        self.stdout.write(self.style.SUCCESS(
            'Database initialized successfully!'))
