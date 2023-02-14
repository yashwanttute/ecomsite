# Generated by Django 4.1.4 on 2023-02-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_rename_image_cart_item_remove_cart_title_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.RemoveField(
            model_name='products',
            name='title',
        ),
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
