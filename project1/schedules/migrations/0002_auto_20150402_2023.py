# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='date_time_field',
        ),
        migrations.AddField(
            model_name='meetingassignment',
            name='day',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 20, 23, 3, 231595, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='day_times_available',
            field=models.DateTimeField(default=datetime.datetime(2015, 4, 2, 20, 23, 7, 287082, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
