# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_auto_20150409_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingassignment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
