# Generated by Django 2.2 on 2019-12-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0007_auto_20191202_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='manufacturing_date',
            field=models.DateTimeField(),
        ),
    ]