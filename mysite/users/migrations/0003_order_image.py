# Generated by Django 5.0.1 on 2024-02-04 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_order_customer_order_seller_alter_pet_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pet_images'),
        ),
    ]
