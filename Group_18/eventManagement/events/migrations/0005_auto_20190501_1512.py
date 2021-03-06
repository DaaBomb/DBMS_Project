# Generated by Django 2.1.7 on 2019-05-01 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20190501_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 15, 12, 32, 778511, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='event_archive',
            name='ev_start_date',
            field=models.DateField(default=datetime.datetime(2019, 5, 1, 15, 12, 32, 780266, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 1, 15, 12, 32, 782038, tzinfo=utc)),
        ),
    ]
