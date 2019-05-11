# Generated by Django 2.0.2 on 2018-02-12 22:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0028_auto_20180213_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_end',
            field=models.TimeField(default='00:00:00'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='datetime_start',
            field=models.TimeField(default='00:00:00'),
        ),
    ]