# Generated by Django 2.2.14 on 2020-12-07 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='publication',
            new_name='publications',
        ),
    ]