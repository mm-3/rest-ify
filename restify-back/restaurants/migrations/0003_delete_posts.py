# Generated by Django 4.0.2 on 2022-03-15 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_alter_image_restaurant_alter_menu_restaurant_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
