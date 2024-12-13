import requests
from rest_framework import viewsets
from .models import Order, OrderItem, Payment
from .serializers import OrderSerializer, OrderItemSerializer, PaymentSerializer
from rest_framework.response import Response
from rest_framework import status
from .tasks import send_order_confirmation, process_payment


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user_id')
        if not user_id:
            return Response({"detail": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        user_service_url = f'http://127.0.0.1:8001/api/users/{user_id}/'
        try:
            user_response = requests.get(user_service_url)
            if user_response.status_code != 200:
                return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

            user_data = user_response.json()  # The user data as a dictionary
            order_data = {
                'user_id': user_id,
                'status': request.data.get('status', 'pending')
            }

            serializer = self.get_serializer(data=order_data)
            if serializer.is_valid():
                order = serializer.save()

                send_order_confirmation.delay(order.id, user_data)
                process_payment.delay(order.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except requests.exceptions.RequestException as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
