# Generated by Django 3.0.5 on 2020-05-12 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
