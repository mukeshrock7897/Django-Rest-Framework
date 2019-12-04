# Generated by Django 2.2 on 2019-12-03 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0010_auto_20191203_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drone',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='drones', to=settings.AUTH_USER_MODEL),
        ),
    ]