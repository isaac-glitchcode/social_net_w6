# Generated by Django 2.2.14 on 2020-12-06 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_auto_20201206_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]