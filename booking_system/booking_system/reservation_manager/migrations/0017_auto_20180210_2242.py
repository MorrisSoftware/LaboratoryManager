# Generated by Django 2.0.2 on 2018-02-10 20:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0016_auto_20180208_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='datetime_end',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 10, 22, 42, 18, 830388)),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_start',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 10, 22, 42, 18, 830388)),
        ),
    ]