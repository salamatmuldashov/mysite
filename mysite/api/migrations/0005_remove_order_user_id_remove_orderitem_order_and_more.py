# Generated by Django 5.1.4 on 2024-12-12 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product_api_product_categor_5c53c5_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
