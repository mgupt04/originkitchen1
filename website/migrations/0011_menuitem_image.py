# Generated by Django 5.1.4 on 2025-01-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_remove_orderitem_order_remove_orderitem_menu_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='menu_images/'),
        ),
    ]
