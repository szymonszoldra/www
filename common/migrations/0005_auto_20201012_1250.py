# Generated by Django 3.1.2 on 2020-10-12 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0004_auto_20201012_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationmenuentry',
            name='link_url',
            field=models.URLField(blank=True, help_text='Overridden by linked page', max_length=500, null=True, verbose_name='link url'),
        ),
    ]
