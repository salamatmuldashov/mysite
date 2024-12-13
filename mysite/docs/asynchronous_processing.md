Asynchronous Processing with Celery
Overview
Celery is used for handling background tasks such as sending order confirmation emails and processing payments asynchronously. It helps offload time-consuming tasks from the main web server, improving performance.

Celery Setup
Installed Celery and configured it to use Redis as the broker.
Defined Celery tasks in orders/tasks.py.

@shared_task
def send_order_confirmation(order_id, user): 
    subject = f"Order Confirmation #{order_id}"
    message = f"Thank you for your order, {user.get('username')}. Your order is being processed."
    recipient_list = [user.get('email')]

    return (f"{subject} was sent succesfully!" )


@shared_task
def process_payment(order_id):
    order = Order.objects.get(id=order_id)
    print(f"Processing payment for Order #{order.id}")
    order.status = "paid"
    order.save()
    return f"Payment processed for Order #{order.id}"

You can check if it working properly by running: "127.0.0.1:6379> keys *"
    1. "celery-task-meta-d16eca8e-2486-4086-b069-e805e9e1dcbd"
    2. "_kombu.binding.celeryev"
    3. "celery-task-meta-cd5fefd9-dbb2-413c-bca1-21a5df904a7c"
    4. "_kombu.binding.celery"
    5. "_kombu.binding.celery.pidbox"

127.0.0.1:6379> get celery-task-meta-d16eca8e-2486-4086-b069-e805e9e1dcbd
    "{\"status\": \"SUCCESS\", \"result\": \"Order Confirmation #29 was sent succesfully!\", \"traceback\": null, \"children\": [], \"date_done\": \"2024-12-12T18:49:43.857365+00:00\", \"task_id\": \"d16eca8e-2486-4086-b069-e805e9e1dcbd\"}"

127.0.0.1:6379> get celery-task-meta-cd5fefd9-dbb2-413c-bca1-21a5df904a7c
    "{\"status\": \"SUCCESS\", \"result\": \"Payment processed for Order #29\", \"traceback\": null, \"children\": [], \"date_done\": \"2024-12-12T18:49:43.930500+00:00\", \"task_id\": \"cd5fefd9-dbb2-413c-bca1-21a5df904a7c\"}"