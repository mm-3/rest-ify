# Generated by Django 4.0.2 on 2022-03-13 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
        ('accounts', '0006_alter_likesblog_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurantcomments', to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usercomment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follows',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurantfollow', to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='follows',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userfollow', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likesblog',
            name='blog',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogliked', to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='likesblog',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userlikesblog', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='likesrestaurant',
            name='restaurant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurantlike', to='restaurants.restaurant'),
        ),
        migrations.AlterField(
            model_name='likesrestaurant',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userlike', to=settings.AUTH_USER_MODEL),
        ),
    ]
