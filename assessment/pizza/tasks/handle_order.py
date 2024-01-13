from celery import shared_task
from pizza.models import Order


@shared_task
def update_order_status(order_id, new_status):
    order = Order.objects.get(id=order_id)
    order.status = new_status
    order.save()
