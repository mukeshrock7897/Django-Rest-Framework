# Generated by Django 2.2 on 2019-11-28 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0002_auto_20191128_2040'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='toy',
            options={'ordering': ('created',)},
        ),
    ]
