# Generated by Django 2.0.2 on 2018-02-07 23:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0014_auto_20180208_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 1, 13, 58, 181174)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 8, 1, 13, 58, 181174)),
        ),
    ]
