from djchoices import ChoiceItem, DjangoChoices


class PizzaBaseConstant(DjangoChoices):
    thin_crust = ChoiceItem(value="THIN-CRUST", label=("thin-crust"))
    normal = ChoiceItem(value="NORMAL", label=("normal"))
    cheese_burst = ChoiceItem(value="CHEESE BURST", label=("cheese burst"))


class CheeseConstant(DjangoChoices):
    mozzarella = ChoiceItem(value="MOZZARELLA", label=("mozzarella"))
    cheddar = ChoiceItem(value="CHEDDAR", label=("cheddar"))
    parmesan = ChoiceItem(value="PARMESAN", label=("parmesan"))
    gouda = ChoiceItem(value="GOUDA", label=("gouda"))


class ToppingConstant(DjangoChoices):
    pepperoni = ChoiceItem(value="PEPPERONI", label=("pepperoni"))
    mushrooms = ChoiceItem(value="MUSHROOMS", label=("mushrooms"))
    onions = ChoiceItem(value="ONIONS", label=("onions"))
    sausage = ChoiceItem(value="SAUSAGE", label=("sausage"))
    bacon = ChoiceItem(value="BACON", label=("mushrooms"))
    black_olives = ChoiceItem(value="BLACK_OLIVES", label=("black_olives"))
    capsicum = ChoiceItem(value="CAPSICUM", label=("capsicum"))


class OrderStatusConstant(DjangoChoices):
    placed = ChoiceItem(value="PLACED", label=("placed"))
    accepted = ChoiceItem(value="ACCEPTED", label=("accepted"))
    preparing = ChoiceItem(value="PREPARING", label=("preparing"))
    dispatched = ChoiceItem(value="DISPATCHED", label=("dispatched"))
    delivered = ChoiceItem(value="DELIVERED", label=("delivered"))
