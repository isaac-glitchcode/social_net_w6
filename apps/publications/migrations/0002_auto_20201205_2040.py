# Generated by Django 2.2.14 on 2020-12-06 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publication',
            old_name='public_satus',
            new_name='public_status',
        ),
    ]
