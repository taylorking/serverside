# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0006_auto_20150414_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingassignment',
            name='day',
            field=models.CharField(max_length=3, choices=[('MON', 'Monday'), ('TUE', 'Tuesday'), ('WED', 'Wednesday'), ('THU', 'Thursday'), ('FRI', 'Friday')]),
        ),
        migrations.AlterField(
            model_name='meetingassignment',
            name='time',
            field=models.FloatField(),
        ),
    ]
