from rest_framework import serializers
from pizza.constants import PizzaBaseConstant, CheeseConstant, ToppingConstant


class PizzaSerializer(serializers.Serializer):
    pizza_base = serializers.ChoiceField(choices=PizzaBaseConstant.choices)
    cheese = serializers.ChoiceField(choices=CheeseConstant.choices)
    toppings = serializers.ListField(
        child=serializers.ChoiceField(choices=ToppingConstant.choices),
        min_length=5,
        max_length=5
    )

    def validate(self, data):
        if (len(list(data['pizza_base'])) == 1 and
                data['pizza_base'] not in PizzaBaseConstant.values):
            raise serializers.ValidationError("Invalid pizza base selected")
        if (len(list(data['cheese'])) == 1 and
                data['cheese'] not in CheeseConstant.values):
            raise serializers.ValidationError("Invalid cheese type selected")
        if (any(topping not in ToppingConstant.values
                for topping in data['toppings'])):
            raise serializers.ValidationError("Invalid toppings selected")
        if len(set(data['toppings'])) != 5:
            raise serializers.ValidationError(
                "Exactly 5 unique toppings should be selected")

        return data
