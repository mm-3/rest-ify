# Generated by Django 4.0.2 on 2022-03-13 19:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0002_alter_notification_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='owner',
            new_name='user',
        ),
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('user', 'id')},
        ),
    ]