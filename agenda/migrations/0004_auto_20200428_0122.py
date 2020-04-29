# Generated by Django 3.0.5 on 2020-04-27 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_auto_20200427_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='edition',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Edition end date'),
        ),
        migrations.AlterField(
            model_name='edition',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Edition start date'),
        ),
    ]
