# Generated by Django 4.2.11 on 2024-03-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='is_returned',
            field=models.BooleanField(default=False),
        ),
    ]
