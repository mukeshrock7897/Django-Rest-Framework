# Generated by Django 2.2 on 2019-12-03 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0016_drone_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drone',
            name='owner',
        ),
    ]
