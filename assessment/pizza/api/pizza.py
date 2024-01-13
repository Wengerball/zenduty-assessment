from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pizza.tasks.handle_order import update_order_status
from pizza.models import Order, Pizza, PizzaBase, Topping, Cheese
from pizza.constants import OrderStatusConstant
from pizza.serializers import PizzaSerializer


class CreatePizzaAndOrderAPIView(APIView):

    def handle_new_order(self, order_id):
        try:
            Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            print("Order not found.")
            return

        update_order_status.apply_async(
            (order_id, 'ACCEPTED'), countdown=30)
        update_order_status.apply_async(
            (order_id, 'PREPARING'), countdown=60)
        update_order_status.apply_async(
            (order_id, 'DISPATCHED'), countdown=3*60)
        update_order_status.apply_async(
            (order_id, 'DELIVERED'), countdown=5*60)

    def post(self, request, format=None):
        pizzas_data = request.data.get('pizzas', [])
        serializer = PizzaSerializer(data=pizzas_data, many=True)

        if not serializer.is_valid():
            return Response(
                {
                    'message': 'Invalid pizza choices',
                    'errors': serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        pizza_bases = {base.name: base for base in PizzaBase.objects.all()}
        print(pizza_bases)
        cheeses = {cheese.name: cheese for cheese in Cheese.objects.all()}
        print(cheeses)
        toppings = Topping.objects.all()
        toppings_dict = {t.name: t for t in toppings}

        pizzas = []
        for pizza_data in serializer.validated_data:
            pizza = Pizza(
                pizza_base=pizza_bases[pizza_data['pizza_base']],
                cheese=cheeses[pizza_data['cheese']]
            )
            pizza.save()
            pizza_toppings = [toppings_dict[topping]
                              for topping in pizza_data['toppings']]
            pizza.toppings.set(pizza_toppings)
            pizzas.append(pizza)

        order = Order.objects.create(
            status=OrderStatusConstant.placed,
            total_bill=sum(pizza.price for pizza in pizzas))
        order.pizzas.set(pizzas)
        order.save()

        self.handle_new_order(order.id)

        return Response(
            {'message': 'Order created successfully', 'order_id': order.id},
            status=status.HTTP_201_CREATED)
