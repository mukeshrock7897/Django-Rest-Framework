# Generated by Django 2.2 on 2019-12-01 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0002_auto_20191201_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='inserted_timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
