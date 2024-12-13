from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_service.settings')

app = Celery('order_service')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Ensure this setting matches the correct broker URL (redis://127.0.0.1:6379/)
app.conf.broker_url = 'redis://127.0.0.1:6379/0'  # Use database 0
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')