# Generated by Django 2.2 on 2019-07-22 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='gml',
            new_name='gmail',
        ),
        migrations.RenameField(
            model_name='login',
            old_name='psw',
            new_name='password',
        ),
    ]
