# Generated by Django 4.2.11 on 2024-03-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='status',
            field=models.CharField(choices=[('seller', 'Seller'), ('buyer', 'Buyer')], default='buyer', max_length=10),
        ),
    ]
