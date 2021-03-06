# Generated by Django 2.0.1 on 2018-02-01 14:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0007_auto_20180201_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time_end',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time_start',
        ),
        migrations.AddField(
            model_name='reservation',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.date(2018, 2, 1)),
        ),
        migrations.AddField(
            model_name='reservation',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.date(2018, 2, 1)),
        ),
    ]
