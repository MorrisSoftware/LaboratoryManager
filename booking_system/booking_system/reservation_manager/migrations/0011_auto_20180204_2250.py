# Generated by Django 2.0.2 on 2018-02-04 20:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0010_auto_20180204_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 4, 22, 50, 22, 628366)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 4, 22, 50, 22, 628366)),
        ),
    ]