# Generated by Django 4.2.11 on 2024-03-27 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_orderitem_is_returned'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='is_returned',
        ),
    ]
