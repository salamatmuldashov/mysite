# Generated by Django 5.1.4 on 2024-12-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_product_api_product_categor_5c53c5_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='product',
            index=models.Index(fields=['category'], name='api_product_categor_5c53c5_idx'),
        ),
    ]