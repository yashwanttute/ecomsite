# Generated by Django 4.1.4 on 2023-02-10 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_delete_cart_remove_products_title_products_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
    ]
