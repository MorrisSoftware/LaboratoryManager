# Generated by Django 2.0.2 on 2018-02-10 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title displayed on home page', max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
