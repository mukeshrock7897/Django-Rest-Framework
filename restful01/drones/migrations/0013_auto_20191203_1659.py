# Generated by Django 2.2 on 2019-12-03 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0012_auto_20191203_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]