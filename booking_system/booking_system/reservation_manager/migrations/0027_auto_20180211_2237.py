# Generated by Django 2.0.2 on 2018-02-11 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0026_auto_20180211_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 22, 37, 39, 797957)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 22, 37, 39, 797957)),
        ),
    ]
