# Generated by Django 3.2.9 on 2022-01-12 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20220112_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_option',
            name='shopping_basket',
            field=models.ManyToManyField(to='product.Product'),
        ),
    ]
