# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0004_auto_20150409_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingassignment',
            name='day',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='meetingassignment',
            name='time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='room',
            name='day_times_available',
            field=models.DateTimeField(),
        ),
    ]
