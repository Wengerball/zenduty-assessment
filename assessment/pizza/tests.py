from unittest.mock import patch
from django.test import TestCase
from rest_framework.test import APIClient
from pizza.constants import PizzaBaseConstant, CheeseConstant, ToppingConstant
from pizza.models import PizzaBase, Cheese, Topping
from pizza.serializers import PizzaSerializer


class PizzaOrderTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.thin_crust = PizzaBaseConstant.thin_crust
        cls.mozzarella_cheese = CheeseConstant.cheddar
        cls.pepperoni = ToppingConstant.pepperoni
        cls.onions = ToppingConstant.onions
        cls.black_olives = ToppingConstant.black_olives
        cls.bacon = ToppingConstant.bacon
        cls.capsicum = ToppingConstant.capsicum
        cls.potato = 'Potato'
        cls.moz_cheese = 'Moz'
        cls.handmade = 'Handmade'

        cls.thin_crust_base_obj = PizzaBase.objects.create(
            name=cls.thin_crust)
        cls.mozzarella_cheese_obj = Cheese.objects.create(
            name=cls.mozzarella_cheese)
        cls.pepperoni_obj = Topping.objects.create(name=cls.pepperoni)
        cls.onions_obj = Topping.objects.create(name=cls.onions)
        cls.black_olives_obj = Topping.objects.create(
            name=cls.black_olives)
        cls.bacon_obj = Topping.objects.create(name=cls.bacon)
        cls.capsicum_obj = Topping.objects.create(name=cls.capsicum)

    def test_pizza_serializer_with_valid_data(self):
        valid_data = {
            'pizza_base': self.thin_crust,
            'cheese': self.mozzarella_cheese,
            'toppings': [self.onions, self.capsicum, self.black_olives,
                         self.bacon, self.pepperoni],
        }
        serializer = PizzaSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    def test_pizza_serializer_with_same_toppings(self):
        valid_data = {
            'pizza_base': self.thin_crust,
            'cheese': self.mozzarella_cheese,
            'toppings': [self.onions, self.capsicum, self.black_olives,
                         self.pepperoni, self.pepperoni],
        }
        serializer = PizzaSerializer(data=valid_data)
        self.assertFalse(serializer.is_valid())

    def test_pizza_serializer_with_four_toppings(self):
        valid_data = {
            'pizza_base': self.thin_crust,
            'cheese': self.mozzarella_cheese,
            'toppings': [self.onions, self.capsicum, self.black_olives,
                         self.pepperoni],
        }
        serializer = PizzaSerializer(data=valid_data)
        self.assertFalse(serializer.is_valid())

    def test_pizza_serializer_with_two_pizza_bases(self):
        valid_data = {
            'pizza_base': [self.thin_crust, self.handmade],
            'cheese': self.mozzarella_cheese,
            'toppings': [self.onions, self.capsicum, self.black_olives,
                         self.pepperoni],
        }
        serializer = PizzaSerializer(data=valid_data)
        self.assertFalse(serializer.is_valid())

    def test_pizza_serializer_with_invalid_data(self):
        valid_data = {
            'pizza_base': self.handmade,
            'cheese': self.mozzarella_cheese,
            'toppings': [self.onions, self.capsicum, self.black_olives,
                         self.pepperoni],
        }
        serializer = PizzaSerializer(data=valid_data)
        self.assertFalse(serializer.is_valid())

    @patch('pizza.tasks.handle_order.update_order_status.apply_async')
    def test_create_order_with_valid_pizzas(self, mock_task):
        client = APIClient()
        order_data = {
            'pizzas': [
                {
                    'pizza_base': self.thin_crust,
                    'cheese': self.mozzarella_cheese,
                    'toppings': [self.onions, self.capsicum, self.black_olives,
                                 self.bacon, self.pepperoni],
                },
                {
                    'pizza_base': self.thin_crust,
                    'cheese': self.mozzarella_cheese,
                    'toppings': [self.onions, self.capsicum, self.black_olives,
                                 self.bacon, self.pepperoni],
                }
            ]
        }
        from pizza.models import Order
        response = client.post(
            'http://0.0.0.0:8000/api/pizza-order', order_data, format='json')
        print(response)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 1)
        mock_task.assert_called()
