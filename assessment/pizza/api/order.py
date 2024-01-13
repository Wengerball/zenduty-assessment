from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from pizza.models import Order


class TrackOrderAPIView(APIView):

    def get(self, request, *args, **kwargs):
        order_id = request.GET.get('order_id', None)
        status_intervals = {
            'ACCEPTED': 1,
            'PREPARING': 3,
            'DISPATCHED': 5
        }

        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response(
                {'message': 'Order ID does not exists'},
                status=status.HTTP_400_BAD_REQUEST
            )
        created_at = order.created_at
        created_at_naive = created_at.replace(tzinfo=None)
        current_status = order.status
        elapsed_time = (datetime.now() - created_at_naive).total_seconds() / 60
        print(elapsed_time)
        expected_status = None

        if current_status == 'DELIVERED':
            time_left = "Order has been delivered"
        else:
            for interval_status, interval in status_intervals.items():
                print(interval_status, interval)
                if elapsed_time < interval:
                    expected_status = interval_status
                    remaining_time = interval - elapsed_time
                    break

            if expected_status is None:
                current_status = 'Delivered'
                time_left = "Order has been delivered"
            else:
                time_left = f"{int(remaining_time)} minutes "\
                    f"left for {expected_status}"

        response_data = {
            "current_status": current_status,
            "expected_status": time_left
        }

        return Response(
            response_data,
            status=status.HTTP_200_OK
        )
