# Generated by Django 2.2 on 2019-12-03 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0014_auto_20191203_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drone',
            name='owner',
        ),
    ]
