# Generated by Django 4.0 on 2022-02-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshopapp', '0007_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.IntegerField(verbose_name=10)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='product/upload'),
        ),
    ]
