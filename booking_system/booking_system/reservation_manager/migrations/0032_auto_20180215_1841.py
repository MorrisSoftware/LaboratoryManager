# Generated by Django 2.0.2 on 2018-02-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0031_auto_20180213_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrumentcategory',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
