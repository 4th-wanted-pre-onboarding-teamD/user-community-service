# Generated by Django 4.1 on 2022-09-05 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userlog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userlog',
            old_name='usernamez',
            new_name='username',
        ),
    ]
