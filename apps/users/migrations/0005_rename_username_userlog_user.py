# Generated by Django 4.1 on 2022-09-05 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_usernamez_userlog_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlog',
            old_name='username',
            new_name='user',
        ),
    ]
