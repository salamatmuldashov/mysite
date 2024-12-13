from celery import shared_task
from django.core.mail import send_mail
from .models import Order


@shared_task
def send_order_confirmation(order_id, user): 
    subject = f"Order Confirmation #{order_id}"
    message = f"Thank you for your order, {user.get('username')}. Your order is being processed."
    recipient_list = [user.get('email')]

    return (f"{subject} was sent succesfully!" )


@shared_task
def process_payment(order_id):
    order = Order.objects.get(id=order_id)

    order.status = "paid"
    order.save()
    return f"Payment processed for Order #{order.id}"
