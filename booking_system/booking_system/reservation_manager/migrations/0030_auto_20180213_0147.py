# Generated by Django 2.0.2 on 2018-02-12 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation_manager', '0029_auto_20180213_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='image',
            field=models.ImageField(default='img/default.jpg', upload_to='instrument'),
        ),
    ]
