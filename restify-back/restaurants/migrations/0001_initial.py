# Generated by Django 4.0.2 on 2022-03-13 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=12)),
                ('address', models.TextField(max_length=200)),
                ('logo', models.ImageField(upload_to='restaurant_logos/')),
                ('postal_code', models.TextField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=200, null=True)),
                ('schedule', models.TextField(blank=True, max_length=200, null=True)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('owner', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='restaurant_menu/')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='menu', to='restaurants.restaurant')),
            ],
            options={
                'unique_together': {('restaurant', 'id')},
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='restaurant_images/')),
                ('restaurant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='image', to='restaurants.restaurant')),
            ],
            options={
                'unique_together': {('restaurant', 'id')},
            },
        ),
    ]