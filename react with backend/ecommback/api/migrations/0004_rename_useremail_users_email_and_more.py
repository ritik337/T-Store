# Generated by Django 4.2.4 on 2023-11-27 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='UserEmail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='usermobile',
            new_name='mobile',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='userpassword',
            new_name='password',
        ),
    ]
