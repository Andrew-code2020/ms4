# Generated by Django 3.1.7 on 2021-04-09 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_has_days'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]