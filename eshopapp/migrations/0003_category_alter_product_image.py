# Generated by Django 4.0 on 2021-12-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0002_alter_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='upload/product/'),
        ),
    ]
