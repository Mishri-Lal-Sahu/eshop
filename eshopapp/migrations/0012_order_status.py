# Generated by Django 3.2.9 on 2022-03-06 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0011_rename_cusrtomer_order_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
