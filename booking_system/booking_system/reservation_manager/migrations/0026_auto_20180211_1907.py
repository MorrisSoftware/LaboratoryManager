# Generated by Django 2.0.2 on 2018-02-11 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0025_auto_20180211_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 19, 7, 2, 36329)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 11, 19, 7, 2, 36329)),
        ),
    ]
